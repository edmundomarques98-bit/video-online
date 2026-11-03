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
