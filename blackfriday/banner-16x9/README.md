# Moveletro: Super Black Friday 16:9 animado

Arte 1920×1080 animada sem IA, para os textos não mudarem. Os efeitos são só luz somada por cima da arte original e movimento de câmera.

- `arte-original.webp`: arte do cliente (fonte única)
- `animar.py`: animação (Python + numpy + Pillow, saída via ffmpeg)
- `output/moveletro-black-friday-16x9.mp4`: 8 s, 30 fps, loop perfeito, sem áudio

Efeitos: zoom lento com pancada e tremor a cada 1 s (120 BPM), neon pulsando com piscadas, luz correndo pelas lâmpadas do letreiro, brilho passando no logo, no 10X e no bloco do Zap, brilho verde no WhatsApp, fumaça e partículas douradas só no fundo, e flash dourado a cada 4 s.

```bash
python3 animar.py            # vídeo final
python3 animar.py --preview  # só quadros PNG em output/preview/
```
