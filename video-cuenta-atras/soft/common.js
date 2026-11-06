// Shared helpers for the soft / peaceful countdown scenes.
const W = 1080, H = 1920, CX = W / 2, CY = H / 2;
const cv = document.getElementById('c');
const ctx = cv.getContext('2d');

function rng(seed) { return function () { seed |= 0; seed = seed + 0x6D2B79F5 | 0; let t = Math.imul(seed ^ seed >>> 15, 1 | seed); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; }; }
const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
const lin = (t, a, b) => clamp((t - a) / (b - a));
const eOut = x => 1 - Math.pow(1 - x, 3);
const eIO = x => x < .5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2;
const eSine = x => -(Math.cos(Math.PI * x) - 1) / 2;
const mix = (a, b, k) => a + (b - a) * k;

// Timeline shared by every soft scene (seconds)
const T = {
  nums: [1.6, 2.6, 3.6],      // 3 · 2 · 1
  es: 4.9,                    // "Empieza la cuenta atrás"
  en: 7.2,                    // "The countdown begins"
  out: 10.9,                  // everything breathes out
  end: 12,
};

function fitFont(text, font, max, start, weight = '') {
  let s = start; ctx.font = `${weight} ${s}px ${font}`;
  while (s > 10 && ctx.measureText(text).width > max) { s -= 2; ctx.font = `${weight} ${s}px ${font}`; }
  return s;
}

// Word-by-word reveal: each word un-blurs, rises and fades in.
function revealWords(text, x, y, font, size, color, t, start, stagger = 0.22, dur = 1.1, opts = {}) {
  const words = text.split(' ');
  ctx.font = `${opts.weight || ''} ${size}px ${font}`;
  ctx.textBaseline = 'alphabetic';
  ctx.textAlign = 'left';
  const space = ctx.measureText(' ').width * (opts.spaceMul || 1);
  const ws = words.map(w => ctx.measureText(w).width);
  const total = ws.reduce((a, b) => a + b, 0) + space * (words.length - 1);
  let px = x - total / 2;
  const fadeOut = opts.fadeOut == null ? 1 : opts.fadeOut;
  words.forEach((w, i) => {
    const k = eOut(lin(t, start + i * stagger, start + i * stagger + dur));
    if (k > 0.001) {
      ctx.save();
      ctx.globalAlpha = k * fadeOut;
      const b = (1 - k) * 14;
      if (b > 0.3) ctx.filter = `blur(${b.toFixed(1)}px)`;
      if (opts.glow) { ctx.shadowColor = opts.glow; ctx.shadowBlur = 30; }
      ctx.fillStyle = color;
      ctx.fillText(w, px, y + (1 - k) * 26);
      ctx.restore();
    }
    px += ws[i] + space;
  });
}

// Soft number: breathes in (blur→sharp, slight scale), then dissolves.
function softNumber(t, font, size, color, y = CY, opts = {}) {
  T.nums.forEach((s, i) => {
    const lt = t - s;
    if (lt < -0.05 || lt > 1.05) return;
    const kin = eSine(lin(lt, 0, 0.45));
    const kout = eSine(lin(lt, 0.62, 1.0));
    const a = kin * (1 - kout);
    if (a <= 0.001) return;
    const sc = 0.9 + 0.1 * kin + 0.06 * kout;
    ctx.save();
    ctx.translate(CX, y); ctx.scale(sc, sc);
    ctx.globalAlpha = a;
    const b = (1 - kin) * 18 + kout * 22;
    if (b > 0.3) ctx.filter = `blur(${b.toFixed(1)}px)`;
    if (opts.glow) { ctx.shadowColor = opts.glow; ctx.shadowBlur = 50; }
    ctx.font = `${size}px ${font}`; ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
    ctx.fillStyle = color; ctx.fillText(['3', '2', '1'][i], 0, 0);
    ctx.restore();
  });
}

// Paper-like grain to keep gradients from banding.
const grain = (() => {
  const g = document.createElement('canvas'); g.width = 540; g.height = 960;
  const gx = g.getContext('2d'); const id = gx.createImageData(540, 960); const r = rng(5);
  for (let i = 0; i < id.data.length; i += 4) { const v = r() * 255; id.data[i] = id.data[i + 1] = id.data[i + 2] = v; id.data[i + 3] = 14; }
  gx.putImageData(id, 0, 0); return g;
})();
function finish(t, fadeColor = '255,255,255') {
  ctx.save(); ctx.globalCompositeOperation = 'overlay'; ctx.drawImage(grain, 0, 0, W, H); ctx.restore();
  const fi = 1 - lin(t, 0, 1.0), fo = lin(t, T.end - 0.7, T.end);
  const a = Math.max(fi, fo);
  if (a > 0) { ctx.fillStyle = `rgba(${fadeColor},${a})`; ctx.fillRect(0, 0, W, H); }
}

function reset() {
  ctx.setTransform(1, 0, 0, 1, 0, 0); ctx.globalAlpha = 1; ctx.filter = 'none';
  ctx.globalCompositeOperation = 'source-over'; ctx.shadowBlur = 0; ctx.letterSpacing = '0px';
}

async function loadFonts(list) {
  await Promise.all(list.map(f => document.fonts.load(`40px ${f}`, 'Aá3')));
  await document.fonts.ready; return true;
}

// Subtle birthday hint: "14 · 11" fading in with wide tracking.
T.date = 8.9;
function dateMark(t, y, font, size, color, opts = {}) {
  const k = eOut(lin(t, T.date, T.date + 1.4));
  if (k <= 0.001) return;
  ctx.save();
  ctx.globalAlpha = k * (opts.fadeOut == null ? 1 : opts.fadeOut);
  const b = (1 - k) * 10; if (b > 0.3) ctx.filter = `blur(${b.toFixed(1)}px)`;
  ctx.font = `${size}px ${font}`; ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
  ctx.letterSpacing = `${Math.round(size * (0.35 + 0.25 * (1 - k)))}px`;
  ctx.fillStyle = color; ctx.fillText(opts.text || '14 · 11', CX + size * 0.17, y);
  ctx.restore();
}
