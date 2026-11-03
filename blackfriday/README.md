# Moveletro: Super Black Friday (motion graphics)

Vídeo vertical 1080×1920, 15 s, 30 fps, sem áudio. Feito em HTML/CSS + GSAP e renderizado quadro a quadro com Playwright + ffmpeg.

- `index.html`: animação (timeline determinística, `window.seek(t)`)
- `assets/`: selo Super Black Friday e placa Moveletro (recortada do selo)
- `output/moveletro-super-black-friday.mp4`: vídeo final

## Renderizar de novo
```bash
cd blackfriday && npm install && node render.js
```
Prévia de quadros: `node render.js --frames 1,4,7,10,14 output/preview`

## Roteiro
| Tempo | Cena |
|---|---|
| 0 a 2,5 s | Selo acende com flicker de neon e varredura de luz |
| 2,5 a 5 s | Selo sobe, entram "Chama no Zap", o WhatsApp e o telefone |
| 5 a 8,5 s | "E aproveite / Frete e montagem / Grátis e rápido", com caixas Moveletro caindo |
| 8,5 a 11,5 s | Flash, depois "Só na Black Friday" em neon com caixas em parallax |
| 11,5 a 15 s | Cartaz final (selo, Zap, telefone, frete e montagem) |
