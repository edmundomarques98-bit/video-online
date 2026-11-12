#!/usr/bin/env bash
# Monta o vídeo de ambientação em 16:9 (1920x1080).
# Uso (de qualquer pasta):  bash projeto-casa/montagem/montar.sh
#
# - Trechos do passeio real saem de bruto/passeio.mp4 (acelerados).
# - Para cada cena, se existir veo/cenaNN-veo.mp4, usa o clipe do Veo.
#   Senão, entra um espaço reservado (foto com zoom lento + aviso).
# - Se existir marca/logo.png, a logo entra grande na abertura e depois
#   fica como marca d'água no canto inferior.
set -euo pipefail
cd "$(dirname "$0")/.."

SRC=bruto/passeio.mp4
OUT=saida
TMP=$OUT/tmp
W=1920; H=1080; FPS=30
VEL_PASSEIO=2        # velocidade do passeio real (2 = 2x mais rápido)
DUR_VEO=3.5          # duração da transformação na edição (s)
SEGURA=1.2           # tempo segurando o render pronto (s)
DUR_RESERVA=4.5      # duração do espaço reservado quando não há clipe do Veo
INCLUIR_LAVANDERIA=0 # 1 para incluir a cena 9
FONTE=/usr/share/fonts/opentype/inter/Inter-Bold.otf
[ -f "$FONTE" ] || FONTE=$(fc-match -f '%{file}' 'sans:bold')

rm -rf "$TMP"; mkdir -p "$TMP"
BASE="scale=${W}:${H}:flags=lanczos,setsar=1,fps=${FPS},format=yuv420p"
ENC=(-an -c:v libx264 -preset fast -crf 18 -r $FPS)
LISTA=$TMP/lista.txt; : > "$LISTA"
n=0

add() { echo "file '$(basename "$1")'" >> "$LISTA"; }

passeio() { # inicio fim
  n=$((n+1)); local f=$TMP/$(printf %03d $n)-passeio.mp4
  ffmpeg -v error -y -ss "$1" -to "$2" -i "$SRC" -vf "setpts=PTS/${VEL_PASSEIO},${BASE}" "${ENC[@]}" "$f"
  add "$f"
}

cena() { # numero rotulo arquivo_foto
  n=$((n+1)); local f=$TMP/$(printf %03d $n)-cena$1.mp4
  local veo=veo/cena$1-veo.mp4
  if [ -f "$veo" ]; then
    local d; d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$veo")
    ffmpeg -v error -y -i "$veo" -vf "setpts=PTS*${DUR_VEO}/${d},${BASE},tpad=stop_mode=clone:stop_duration=${SEGURA}" "${ENC[@]}" "$f"
    echo "cena $1: clipe do Veo"
  else
    local fr; fr=$(python3 -c "print(round(${DUR_RESERVA}*${FPS}))")
    ffmpeg -v error -y -loop 1 -i "fotos/$3" -t "$DUR_RESERVA" -vf "scale=3840:2160:flags=lanczos,zoompan=z='min(zoom+0.0006,1.08)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=${fr}:s=${W}x${H}:fps=${FPS},drawbox=y=ih-130:w=iw:h=130:color=black@0.55:t=fill,drawtext=fontfile=${FONTE}:text='CENA $1 · $2  —  aguardando clipe do Veo (veo/cena$1-veo.mp4)':fontsize=40:fontcolor=white:x=(w-tw)/2:y=h-85,${BASE}" "${ENC[@]}" "$f"
    echo "cena $1: espaço reservado"
  fi
  add "$f"
}

# ---------------- ROTEIRO ----------------
passeio 0 5;        cena 01 "FACHADA"         cena01-fachada.jpg
passeio 5 12;       cena 02 "FRENTE E GARAGEM" cena02-frente-garagem.jpg
passeio 15.5 19;    cena 03 "CHUVEIRÃO"       cena03-chuveirao.jpg
passeio 23 29.5;    cena 04 "SALA"            cena04-sala.jpg
passeio 35 41;      cena 05 "COZINHA"         cena05-cozinha.jpg
passeio 63 67; passeio 74 76.5; cena 06 "QUARTO 1" cena06-quarto1.jpg
passeio 80 83.5;    cena 07 "BANHEIRO"        cena07-banheiro.jpg
passeio 92 97;      cena 08 "QUARTO 2"        cena08-quarto2-frame-video.jpg
[ "$INCLUIR_LAVANDERIA" = 1 ] && cena 09 "LAVANDERIA" cena09-lavanderia.jpg
cena 10 "ÁREA GOURMET"  cena10-fundos.jpg
# -----------------------------------------

ffmpeg -v error -y -f concat -safe 0 -i "$LISTA" -c copy "$TMP/juntado.mp4"

FINAL=$OUT/casa-ambientacao-16x9.mp4
if [ -f marca/logo.png ]; then
  # Logo grande no centro de 0,3 a 2,5 s; depois marca d'água no rodapé central.
  ffmpeg -v error -y -i "$TMP/juntado.mp4" -i marca/logo.png -i marca/logo.png -filter_complex "\
[1:v]scale=700:-1[grande];[2:v]scale=260:-1,format=rgba,colorchannelmixer=aa=0.9[peq];\
[0:v][grande]overlay=(W-w)/2:(H-h)/2:enable='between(t,0.3,2.5)'[a];\
[a][peq]overlay=(W-w)/2:H-h-40:enable='gte(t,2.5)'[v]" -map "[v]" "${ENC[@]}" "$FINAL"
else
  cp "$TMP/juntado.mp4" "$FINAL"
  echo "aviso: sem marca/logo.png — vídeo saiu sem logo"
fi

# Música: se existir marca/musica.mp3, entra com fade no fim.
if [ -f marca/musica.mp3 ]; then
  d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$FINAL")
  ffmpeg -v error -y -i "$FINAL" -i marca/musica.mp3 -filter_complex "[1:a]afade=t=out:st=$(python3 -c "print(max(0,$d-2))"):d=2[a]" -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -shortest "$OUT/tmp-musica.mp4"
  mv "$OUT/tmp-musica.mp4" "$FINAL"
fi

echo "pronto: $FINAL ($(ffprobe -v error -show_entries format=duration -of csv=p=0 "$FINAL") s)"
