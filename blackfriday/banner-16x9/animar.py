"""Anima a arte Super Black Friday Moveletro (1920x1080) sem redesenhar nada.

Os efeitos são só luz somada por cima da arte original e movimento de câmera
(zoom e tremor). Textos, logo, telefone e site continuam sendo os pixels da arte.
Loop perfeito de 8 s a 30 fps (120 BPM: uma batida a cada 0,5 s).

Uso: python3 animar.py            -> output/moveletro-black-friday-16x9.mp4
     python3 animar.py --preview  -> só alguns quadros PNG em output/preview/
"""
import math
import os
import subprocess
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

AQUI = os.path.dirname(os.path.abspath(__file__))
W, H, FPS, DUR = 1920, 1080, 30, 8.0
N = int(FPS * DUR)
BEAT = 0.5

arte = Image.open(os.path.join(AQUI, "arte-original.webp")).convert("RGB")
assert arte.size == (W, H)
base = np.asarray(arte).astype(np.float32) / 255.0
R, G, B = base[..., 0], base[..., 1], base[..., 2]
lum = 0.299 * R + 0.587 * G + 0.114 * B

yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)


def rect(x0, y0, x1, y1, feather=0):
    m = ((xx >= x0) & (xx <= x1) & (yy >= y0) & (yy <= y1)).astype(np.float32)
    if feather:
        m = blur(m, feather)
    return m


def blur(a, r):
    """Desfoque quase gaussiano (3 passadas de box blur separável) de um canal float."""
    k = max(1, int(round(r * 0.9)))
    out = a.astype(np.float32)
    for _ in range(3):
        for ax in (0, 1):
            pad = [(0, 0), (0, 0)]
            pad[ax] = (k + 1, k)
            c = np.cumsum(np.pad(out, pad, mode="edge"), axis=ax, dtype=np.float64)
            hi = np.take(c, np.arange(2 * k + 1, c.shape[ax]), axis=ax)
            lo = np.take(c, np.arange(0, c.shape[ax] - 2 * k - 1), axis=ax)
            out = ((hi - lo) / (2 * k + 1)).astype(np.float32)
    return out


def blur_rgb(a, r):
    return np.stack([blur(a[..., c], r) for c in range(3)], -1)


# ---------------- máscaras tiradas da própria arte ----------------
amarelo = np.clip((R - 0.55) * 4, 0, 1) * np.clip((G - 0.45) * 4, 0, 1) * np.clip((0.55 - B) * 4, 0, 1)

# Letreiro (selo) e lâmpadas
selo = rect(430, 70, 1470, 700, feather=20)
neon = amarelo * selo
glow_neon = blur_rgb(base * neon[..., None], 16) * 1.6
brilho_forte = np.clip((lum - 0.62) * 3.5, 0, 1) * selo
glow_lampadas = blur_rgb(base * brilho_forte[..., None], 6) * 2.2
cx, cy = 945.0, 400.0
ang = np.arctan2((yy - cy) / 330.0, (xx - cx) / 520.0)

# Áreas de informação (nada de partículas ou fumaça por cima)
caixa_logo = rect(668, 690, 1210, 838)
area_10x = rect(175, 830, 625, 1020)
amarelo_10x = amarelo * area_10x
glow_10x = blur_rgb(base * amarelo_10x[..., None], 14)
area_zap = rect(1388, 745, 1712, 1026)
caixa_zap = rect(1390, 888, 1688, 966) + rect(1390, 970, 1688, 1024)
caixa_zap = np.clip(caixa_zap, 0, 1)
area_url = rect(700, 915, 1292, 968)
protegido = np.clip(
    rect(650, 680, 1225, 850) + rect(165, 820, 640, 1030) + rect(1380, 735, 1720, 1035) + rect(690, 905, 1300, 978), 0, 1
)
livre = 1.0 - blur(protegido, 18)

# Fundo escuro: onde a fumaça pode aparecer
escuro = np.clip((0.45 - lum) * 3, 0, 1) * livre

# WhatsApp: brilho verde pulsando em volta do ícone
wpp = np.exp(-(((xx - 1672) ** 2 + (yy - 785) ** 2) / (2 * 42.0 ** 2)))
wpp_cor = np.array([0.15, 0.95, 0.35], np.float32)

ouro = np.array([1.0, 0.78, 0.22], np.float32)

# ---------------- fumaça (ruído que faz loop) ----------------
rng = np.random.default_rng(7)


def ruido_tile(tw, th, cel, seed):
    r = np.random.default_rng(seed)
    small = r.random((th // cel, tw // cel)).astype(np.float32)
    big = Image.fromarray((small * 255).astype(np.uint8)).resize((tw, th), Image.BICUBIC)
    return np.asarray(big, np.float32) / 255.0


fumaca_a = ruido_tile(W, H, 120, 1)
fumaca_b = ruido_tile(W, H, 60, 2)

# ---------------- partículas douradas ----------------
NP = 170
p_x = rng.uniform(0, W, NP)
p_y = rng.uniform(0, H, NP)
p_vel = rng.choice([1, 2], NP)  # voltas na tela em 8 s (inteiro = loop)
p_tam = rng.uniform(1.2, 3.6, NP)
p_fase = rng.uniform(0, 2 * math.pi, NP)
p_amp = rng.uniform(8, 30, NP)
p_pisca = rng.choice([1, 2, 3], NP)


def particulas(t):
    camada = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(camada)
    for i in range(NP):
        y = (p_y[i] - p_vel[i] * (H + 60) * t / DUR) % (H + 60) - 30
        x = p_x[i] + p_amp[i] * math.sin(2 * math.pi * t / DUR * 2 + p_fase[i])
        a = 0.55 + 0.45 * math.sin(2 * math.pi * p_pisca[i] * t / DUR + p_fase[i])
        r = p_tam[i]
        d.ellipse((x - r, y - r, x + r, y + r), fill=int(255 * a))
    m = np.asarray(camada, np.float32) / 255.0
    m = m + blur(m, 4) * 1.5
    return m * livre


# ---------------- ritmo ----------------
def pulso(t, periodo, decai, fase=0.0):
    dt = (t - fase) % periodo
    return math.exp(-dt / decai)


def flicker(t):
    """Piscadas de neon: quedas rápidas em pontos fixos do loop."""
    quedas = [0.62, 0.70, 2.31, 3.85, 3.93, 5.12, 6.66, 6.74, 7.40]
    v = 1.0
    for q in quedas:
        if 0 <= t - q < 0.05:
            v = 0.15
    return v


def faixa_diagonal(t, t0, dur, x0, x1, largura=90):
    """Faixa de brilho diagonal que atravessa de x0 até x1 entre t0 e t0+dur."""
    if not (t0 <= t <= t0 + dur):
        return None
    k = (t - t0) / dur
    k = k * k * (3 - 2 * k)
    pos = x0 + (x1 - x0) * k
    d = (xx - pos) + (yy - 540) * 0.45
    return np.exp(-(d / largura) ** 2)


def quadro(i):
    t = i / FPS
    out = base.copy()

    # Fumaça girando no fundo
    sx = int(W * t / DUR) % W
    sy = int(H * t / DUR) % H
    fum = 0.6 * np.roll(fumaca_a, sx, axis=1) + 0.4 * np.roll(fumaca_b, (-sx * 2) % W, axis=1)
    fum = np.roll(fum, -sy // 2, axis=0)
    fum = np.clip((fum - 0.45) * 2.2, 0, 1)
    out += (fum * escuro * 0.16)[..., None] * np.array([0.85, 0.6, 0.25], np.float32)

    # Batida: pancada a cada 2 batidas (1 s), forte a cada 4 s
    p1 = pulso(t, 2 * BEAT, 0.14)
    p4 = pulso(t, 4.0, 0.22)

    # Neon do letreiro: pulso + flicker
    fl = flicker(t)
    inten = (0.35 + 0.25 * math.sin(2 * math.pi * 4 * t / DUR) ** 2 + 0.55 * p1) * fl
    out += glow_neon * inten
    if fl < 1:
        out -= (neon * 0.35)[..., None] * out

    # Lâmpadas: luz correndo em volta do letreiro (perseguição)
    chase = np.clip(np.sin(10 * ang - 2 * math.pi * 4 * t / DUR), 0, 1) ** 6
    out += glow_lampadas * (0.25 + 0.9 * chase)[..., None]

    # Brilhos passando (logo, 10X, Zap)
    for t0, alvo, x0, x1 in [
        (1.05, "logo", 560, 1350), (5.05, "logo", 560, 1350),
        (2.05, "10x", 120, 760), (6.05, "10x", 120, 760),
        (3.05, "zap", 1300, 1820), (7.05, "zap", 1300, 1820),
    ]:
        f = faixa_diagonal(t, t0, 0.7, x0, x1, largura=70 if alvo != "logo" else 95)
        if f is None:
            continue
        m = {"logo": caixa_logo * 0.55, "10x": amarelo_10x * 0.75, "zap": caixa_zap * 0.5}[alvo]
        out += (f * m)[..., None]

    # 10X pulsa na batida
    out += glow_10x * (0.25 + 0.6 * p1)

    # WhatsApp
    out += (wpp * (0.25 + 0.45 * pulso(t, 2 * BEAT, 0.2, 0.5)))[..., None] * wpp_cor * 0.6

    # Partículas
    out += particulas(t)[..., None] * ouro

    # Flash dourado na batida forte
    out += (0.22 * p4 * livre)[..., None] * ouro * 0.5 + 0.06 * p4

    out = np.clip(out, 0, 1)
    img = Image.fromarray((out * 255 + 0.5).astype(np.uint8))

    # Câmera: aproximação lenta em loop + pancada + tremor
    s = 1.0 + 0.035 * (1 - math.cos(2 * math.pi * t / DUR)) / 2 + 0.018 * p1 + 0.02 * p4
    tremor = 7 * p1 + 9 * p4
    dx = tremor * math.sin(t * 91.0)
    dy = tremor * math.cos(t * 77.0)
    cw, ch = W / s, H / s
    x0 = (W - cw) / 2 + dx / s
    y0 = (H - ch) / 2 + dy / s
    x0 = min(max(x0, 0), W - cw)
    y0 = min(max(y0, 0), H - ch)
    img = img.transform((W, H), Image.EXTENT, (x0, y0, x0 + cw, y0 + ch), Image.BICUBIC)
    return img


def main():
    os.makedirs(os.path.join(AQUI, "output"), exist_ok=True)
    if "--preview" in sys.argv:
        d = os.path.join(AQUI, "output", "preview")
        os.makedirs(d, exist_ok=True)
        for t in [0.0, 0.3, 0.65, 1.3, 2.3, 3.3, 4.0, 5.4, 7.9]:
            quadro(int(round(t * FPS)) % N).save(os.path.join(d, f"t{t:.2f}.png"))
        return
    destino = os.path.join(AQUI, "output", "moveletro-black-friday-16x9.mp4")
    ff = subprocess.Popen(
        ["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
         "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "slow", "-crf", "16",
         "-pix_fmt", "yuv420p", "-movflags", "+faststart", destino],
        stdin=subprocess.PIPE,
    )
    for i in range(N):
        ff.stdin.write(quadro(i).tobytes())
        if i % 30 == 0:
            print(f"quadro {i}/{N}", flush=True)
    ff.stdin.close()
    ff.wait()
    print("OK ->", destino)


if __name__ == "__main__":
    main()
