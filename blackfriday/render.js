// Renderiza index.html quadro a quadro (30 fps) e gera o MP4 com ffmpeg.
// Uso: node render.js [--frames 0.5,2,4]  (gera só PNGs de prévia)
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const path = require('path');
const fs = require('fs');

const FPS = 30, W = 1080, H = 1920;
const out = path.join(__dirname, 'output', 'moveletro-super-black-friday.mp4');
const args = process.argv.slice(2);
const previewIdx = args.indexOf('--frames');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 1 });
  await page.goto('file://' + path.join(__dirname, 'index.html'));
  await page.evaluate(() => window.ready);

  if (previewIdx >= 0) {
    const dir = args[previewIdx + 2] || path.join(__dirname, 'output', 'preview');
    fs.mkdirSync(dir, { recursive: true });
    for (const t of args[previewIdx + 1].split(',').map(Number)) {
      await page.evaluate(t => window.seek(t), t);
      await page.screenshot({ path: path.join(dir, `t${t.toFixed(2)}.png`) });
    }
    await browser.close();
    return;
  }

  const dur = await page.evaluate(() => window.DURATION);
  const total = Math.round(dur * FPS);
  fs.mkdirSync(path.dirname(out), { recursive: true });
  const ff = spawn('ffmpeg', ['-y', '-v', 'error', '-f', 'image2pipe', '-framerate', String(FPS), '-i', '-',
    '-c:v', 'libx264', '-preset', 'slow', '-crf', '18', '-pix_fmt', 'yuv420p', '-r', String(FPS),
    '-movflags', '+faststart', out], { stdio: ['pipe', 'inherit', 'inherit'] });

  for (let i = 0; i < total; i++) {
    await page.evaluate(t => window.seek(t), i / FPS);
    const buf = await page.screenshot({ type: 'png' });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    if (i % 30 === 0) process.stdout.write(`frame ${i}/${total}\n`);
  }
  ff.stdin.end();
  await new Promise(r => ff.on('close', r));
  await browser.close();
  console.log('OK ->', out);
})();
