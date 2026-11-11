# Moveletro: Super Black Friday (motion graphics)

Vídeo vertical 1080×1920, 18 s, 30 fps, sem áudio. Feito em HTML/CSS + GSAP e renderizado quadro a quadro com Playwright + ffmpeg.

- `index.html`: animação (timeline determinística, `window.seek(t)`)
- `assets/`: selo Super Black Friday e placa Moveletro (recortada do selo)
- `output/moveletro-super-black-friday.mp4`: vídeo final

## Renderizar de novo
```bash
cd blackfriday && npm install
mkdir -p assets/veo && ffmpeg -ss 1.6 -t 6 -i "<clipe Veo original>.mp4" -vf fps=30 -q:v 2 assets/veo/f%04d.jpg
node render.js
```
Os quadros do clipe (`assets/veo/`) não são versionados. A cópia sem áudio do clipe está em `assets/ia/veo-entrega.mp4`, e ela começa no mesmo ponto do original, então dá para extrair dela com o mesmo comando.
Prévia de quadros: `node render.js --frames 1,4,7,10,14 output/preview`

## Roteiro
| Tempo | Cena |
|---|---|
| 0 a 2,5 s | Selo acende com flicker de neon e varredura de luz |
| 2,5 a 5 s | Selo sobe, entram "Chama no Zap", o WhatsApp e o telefone |
| 5 a 8,5 s | "E aproveite / Frete e montagem / Grátis e rápido", com caixas Moveletro caindo |
| 8,5 a 14,5 s | Entrega: clipe Veo do caminhão e do casal recebendo as caixas numa rua do interior do Ceará, com o selo e "Frete e montagem grátis" por cima |
| 14,5 a 18 s | Cartaz final (selo, Zap, telefone, frete e montagem) |

---

# Moveletro: Black Friday, vídeo do vendedor (`vendedor/`)

Edição do vídeo gravado na loja (IMG_0826.MOV, 30 s) no mesmo padrão visual da peça acima: 1080×1920, 30 fps, 34,2 s, com o áudio original (limpo e normalizado em -14 LUFS).

- `vendedor/index.html`: montagem (quadros do vídeo + legendas palavra a palavra + cartões animados + cartaz final)
- `vendedor/assets/audio.m4a`: áudio tratado do vídeo
- `vendedor/output/moveletro-black-friday-vendedor.mp4`: vídeo final

## Renderizar de novo
```bash
cd blackfriday && npm install
mkdir -p vendedor/assets/frames && ffmpeg -i IMG_0826.MOV -vf "scale=1080:1920:flags=lanczos,eq=contrast=1.05:saturation=1.08" -q:v 3 vendedor/assets/frames/f%04d.jpg
node vendedor/render.js
```
Os quadros (`vendedor/assets/frames/`) não são versionados.

## Roteiro
| Tempo | Cena |
|---|---|
| 0 a 2,3 s | Selo Super Black Friday acende com neon sobre o vídeo e vai para o canto |
| 2,4 a 4,8 s | "É hoje / 11/11" (11/11 em neon) |
| 4,9 a 9,1 s | Legendas palavra a palavra |
| 9,2 a 10,8 s | Faixa amarela "Já começou!" com flash |
| 10,9 a 21,6 s | Legendas palavra a palavra, com cortes de zoom no ritmo da fala |
| 21,8 a 24,1 s | "Hoje até às / 18 horas" |
| 25,6 a 29 s | "Desconto de 30% 40% até 50%" (50% em neon, com flash e tremida) |
| 29,1 a 30,6 s | "Vem pra" + placa Moveletro |
| 30,6 a 34,2 s | Cartaz final: selo, Chama no Zap, telefone e "Hoje até às 18h" |
