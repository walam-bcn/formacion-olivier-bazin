"""Satie, Gymnopédie No. 1 (public domain) on the synthesized piano, for the hourglass reel (12 s, 48 kHz stereo).
Usage: python3 audio_piano.py out.wav

Synced to common.js: counts 1.6/2.6/3.6 s, Spanish title 4.9 s,
English 7.2 s, date 8.9 s, breathe out from 10.9 s.
"""
import sys, wave
import numpy as np

SR = 48000
DUR = float(sys.argv[2]) if len(sys.argv) > 2 else 12.0
N = int(SR * DUR)
L = np.zeros(N); R = np.zeros(N)
rng = np.random.default_rng(1)
NAMES = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}


def midi(n):
    s = NAMES[n[0]]; i = 1
    if n[i] == 'b': s -= 1; i += 1
    elif n[i] == '#': s += 1; i += 1
    return 12 * (int(n[i:]) + 1) + s


def piano(t0, n, vel=0.6, length=6.0, pan=None):
    """Additive piano: inharmonic partials, detuned string pairs, two-stage decay, hammer."""
    m = midi(n); f0 = 440 * 2 ** ((m - 69) / 12)
    if m < 48: vel *= 0.7   # keep the low end warm, not boomy
    i0 = int(t0 * SR); ln = min(int(length * SR), N - i0)
    if ln <= 0: return
    x = np.arange(ln) / SR
    B = 0.00035 * (1 + (m - 60) / 40)                 # inharmonicity
    bright = 0.6 + vel * 0.8
    sig = np.zeros(ln)
    for k in range(1, 12):
        fk = k * f0 * np.sqrt(1 + B * k * k)
        if fk > 16000: break
        amp = (1 / k ** (1.6 - 0.5 * bright)) * (1.0 if k == 1 else 0.85)
        fast = 2.5 + k * 0.9 + (m - 60) * 0.04
        slow = 0.35 + k * 0.12 + max(0, (m - 60)) * 0.02
        env = 0.55 * np.exp(-x * fast) + 0.45 * np.exp(-x * slow)
        det = 1 + 0.0007 * (1 + k * 0.1)                # second string, slight beating
        sig += amp * env * (np.sin(2 * np.pi * fk * x) + 0.6 * np.sin(2 * np.pi * fk * det * x + k))
    att = np.minimum(x / 0.004, 1)
    hammer = np.convolve(rng.standard_normal(ln), np.ones(8) / 8, 'same') * np.exp(-x * 120) * 0.05 * vel
    sig = (sig * att + hammer) * vel
    sig *= np.clip((length - x) / 0.6, 0, 1)            # release (pedal up)
    p = pan if pan is not None else np.clip((m - 62) / 30, -0.7, 0.7)
    L[i0:i0 + ln] += sig * np.sqrt((1 - p) / 2)
    R[i0:i0 + ln] += sig * np.sqrt((1 + p) / 2)


def strings(t0, t1, notes, g):
    """Soft string pad: detuned filtered saws, slow swell."""
    i0, i1 = int(t0 * SR), min(int(t1 * SR), N)
    x = np.arange(i1 - i0) / SR; d = t1 - t0
    env = np.clip(x / 1.6, 0, 1) ** 2 * np.clip((d - x) / 1.4, 0, 1)
    for j, n in enumerate(notes):
        f = 440 * 2 ** ((midi(n) - 69) / 12)
        s = np.zeros_like(x)
        for dt in (-0.004, 0.0, 0.005):
            ph = (f * (1 + dt) * x + rng.random()) % 1
            s += 2 * ph - 1
        # one-pole lowpass for warmth
        a = np.exp(-2 * np.pi * 1400 / SR); y = np.empty_like(s); acc = 0.0
        for i in range(len(s)):
            acc = (1 - a) * s[i] + a * acc; y[i] = acc
        vib = 1 + 0.08 * np.sin(2 * np.pi * 0.3 * x + j)
        p = (j / max(1, len(notes) - 1) - 0.5) * 1.2
        L[i0:i1] += y * env * vib * g * np.sqrt((1 - p) / 2)
        R[i0:i1] += y * env * vib * g * np.sqrt((1 + p) / 2)


def arp(t0, notes, step, vel, length=5.0):
    for i, n in enumerate(notes):
        piano(t0 + i * step, n, vel * (0.85 + 0.15 * rng.random()), length)


# ---------------- Erik Satie — Gymnopédie No. 1 (1888, public domain) ----------------
# Opening: two bars of the swaying G / D accompaniment, the melody enters with the title (4.9 s).
BAR = 2.2; Q = BAR / 3; T0 = 0.5
def bar_acc(i, root, chord):
    t = T0 + i * BAR
    piano(t, root, 0.5, BAR * 1.9)
    for j, n in enumerate(chord):
        piano(t + Q + j * 0.012, n, 0.3, BAR * 1.2)
G = ('G2', ['B3', 'D4', 'F#4']); D = ('D2', ['A3', 'C#4', 'F#4'])
if DUR < 20:
    for i, (r, c) in enumerate([G, D, G, D, G, D]):
        bar_acc(i, r, c)
    m = [(2, 1, 'F#5'), (2, 2, 'A5'), (3, 0, 'G5'), (3, 1, 'F#5'), (3, 2, 'C#5'),
         (4, 0, 'B4'), (4, 1, 'C#5'), (4, 2, 'D5'), (5, 0, 'A4')]
else:
    # full four-bar introduction, then the first phrase; the long F# rests over the sway
    for i in range(12):
        bar_acc(i, *(G if i % 2 == 0 else D))
    m = [(4, 1, 'F#5'), (4, 2, 'A5'), (5, 0, 'G5'), (5, 1, 'F#5'), (5, 2, 'C#5'),
         (6, 0, 'B4'), (6, 1, 'C#5'), (6, 2, 'D5'), (7, 0, 'A4'), (8, 0, 'F#4')]
    # closing: a last open G chord with the high F# ringing out
    t = T0 + 12 * BAR
    piano(t, 'G2', 0.45, 4); piano(t, 'D3', 0.3, 4)
    for j, n in enumerate(['B3', 'D4', 'F#4']): piano(t + Q + j * 0.02, n, 0.28, 3.5)
    piano(t + Q, 'F#5', 0.45, 3.5, pan=0.1)
for b, beat, n in m:
    piano(T0 + b * BAR + beat * Q, n, 0.58 if n not in ('A4', 'F#4') else 0.5, 9.0 if n == 'F#4' else 5.0, pan=0.1)

# ---------------- space: pre-delay + long stereo hall ----------------
def hall(x, seed, decay=1.25, pre=0.025):
    n_ir = int(SR * 4.0); r = np.random.default_rng(seed)
    tt = np.arange(n_ir) / SR
    ir = r.standard_normal(n_ir) * np.exp(-tt / decay) * np.clip(tt / 0.04, 0, 1)
    # darker tail: soften high end progressively
    ir = np.convolve(ir, np.ones(6) / 6, 'same')
    ir = np.concatenate([np.zeros(int(pre * SR)), ir]); ir /= np.sqrt(np.sum(ir ** 2))
    n = len(x) + len(ir)
    return np.fft.irfft(np.fft.rfft(x, n) * np.fft.rfft(ir, n), n)[:len(x)]

dry = np.stack([L, R], 1)
wetL, wetR = hall(L, 11), hall(R, 12)
mix = 0.8 * dry + 0.55 * np.stack([wetL, wetR], 1)
# clean low end: gentle high-pass (FFT, ramp 45-90 Hz) to remove rumble/mud
F = np.fft.rfft(mix, axis=0); fr = np.fft.rfftfreq(N, 1 / SR)
F *= np.clip((fr - 45) / 45, 0, 1)[:, None]
mix = np.fft.irfft(F, N, axis=0)
mix = np.tanh(mix / np.max(np.abs(mix)) * 1.1)
mix /= np.max(np.abs(mix)) / 0.88
t = np.arange(N) / SR
mix *= (np.clip(t / 0.08, 0, 1) * np.clip((DUR - t) / 1.1, 0, 1))[:, None]
with wave.open(sys.argv[1], 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((mix * 32767).astype('<i2').tobytes())
print('wrote', sys.argv[1])
