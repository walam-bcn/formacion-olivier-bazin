// Renders scene.html frame by frame and pipes JPEG frames into ffmpeg.
// Usage: node render.js [--scene file.html] <out.mp4> [audio.wav] [--stills]
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const path = require('path');

const FPS = 30;
const argv = process.argv.slice(2);
let DUR = 12;
const di = argv.indexOf('--dur'); if (di >= 0) { DUR = +argv[di + 1]; argv.splice(di, 2); }
let scene = 'scene.html';
const si = argv.indexOf('--scene'); if (si >= 0) { scene = argv[si + 1]; argv.splice(si, 2); }
const pos = argv.filter(a => !a.startsWith('--'));
const out = pos[0] || 'cuenta-atras.mp4';
const audio = pos[1] || null;
const stills = process.argv.includes('--stills');

(async () => {
  const browser = await chromium.launch({ args: ['--allow-file-access-from-files'] });
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  const [sf, qs] = scene.split('?');
  await page.goto('file://' + path.resolve(sf) + (qs ? '?' + qs : ''));
  await page.evaluate(() => window.ready);
  const canvas = await page.$('#c');

  if (stills) {
    for (const t of [0.8, 2.0, 3.0, 5.6, 8.0, 10.2, 11.5]) {
      await page.evaluate(t => window.render(t), t);
      await canvas.screenshot({ path: `${out}-${t.toFixed(2)}.jpg`, type: 'jpeg', quality: 80 });
    }
    await browser.close(); return;
  }

  const args = ['-y', '-f', 'image2pipe', '-framerate', String(FPS), '-c:v', 'mjpeg', '-i', '-'];
  if (audio) args.push('-i', audio);
  args.push('-c:v', 'libx264', '-preset', 'slow', '-crf', '18', '-pix_fmt', 'yuv420p', '-movflags', '+faststart');
  if (audio) args.push('-c:a', 'aac', '-b:a', '192k', '-shortest');
  args.push(out);
  const ff = spawn('ffmpeg', args, { stdio: ['pipe', 'ignore', 'inherit'] });

  const total = FPS * DUR;
  for (let i = 0; i < total; i++) {
    await page.evaluate(t => window.render(t), i / FPS);
    const buf = await canvas.screenshot({ type: 'jpeg', quality: 95 });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    if (i % 60 === 0) console.log(`frame ${i}/${total}`);
  }
  ff.stdin.end();
  await new Promise(r => ff.on('close', r));
  await browser.close();
  console.log('done', out);
})();
