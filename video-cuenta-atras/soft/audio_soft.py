"""Gentle soundtracks for the soft countdown scenes (12 s, 48 kHz stereo).
Usage: python3 audio_soft.py <amanecer|petalos|luna> out.wav

Timeline matches common.js: counts at 1.6/2.6/3.6 s, Spanish title at 4.9 s,
English title at 7.2 s, date at 8.9 s, breathe out from 10.9 s.
"""
import sys, wave
import numpy as np

style = sys.argv[1]
out = sys.argv[2]
SR, DUR = 48000, 12.0
N = int(SR * DUR)
t = np.arange(N) / SR
L = np.zeros(N); R = np.zeros(N)
rng = np.random.default_rng(9)


def hz(note):
    names = {'C': -9, 'D': -7, 'E': -5, 'F': -4, 'G': -2, 'A': 0, 'B': 2}
    n = names[note[0]]; i = 1
    if note[i] == 'b': n -= 1; i += 1
    elif note[i] == '#': n += 1; i += 1
    octv = int(note[i:])
    return 440 * 2 ** ((n + (octv - 4) * 12) / 12)


def add(sig, pan=0.0, g=1.0):
    global L, R
    L += sig * g * np.sqrt((1 - pan) / 2); R += sig * g * np.sqrt((1 + pan) / 2)


def seg(t0, t1, att, rel):
    e = np.clip((t - t0) / att, 0, 1) * np.clip((t1 - t) / rel, 0, 1)
    return eSine(e)


def eSine(x):
    return -(np.cos(np.pi * x) - 1) / 2


def pad(chords, gain, bright=1.0):
    for t0, t1, notes in chords:
        e = seg(t0, t1 + 0.8, 1.2, 1.4)
        for j, n in enumerate(notes):
            f = hz(n)
            s = (np.sin(2 * np.pi * f * t) + 0.5 * np.sin(2 * np.pi * f * 1.003 * t + j)
                 + 0.18 * bright * np.sin(2 * np.pi * 2 * f * t))
            s *= 1 + 0.15 * np.sin(2 * np.pi * (0.2 + 0.05 * j) * t)
            add(s * e, (j / max(1, len(notes) - 1) - 0.5) * 0.8, gain / len(notes))


def note(t0, n, kind, g=1.0, pan=0.0):
    f = hz(n); x = t - t0; m = x >= 0; x = np.where(m, x, 0)
    if kind == 'piano':
        s = (np.sin(2 * np.pi * f * x) + 0.35 * np.sin(2 * np.pi * 2 * f * x) * np.exp(-x * 3)
             + 0.12 * np.sin(2 * np.pi * 3 * f * x) * np.exp(-x * 5))
        e = np.minimum(x / 0.006, 1) * np.exp(-x * 1.4)
    elif kind == 'box':  # music box: pure + inharmonic sparkle, short
        s = (np.sin(2 * np.pi * f * x) + 0.4 * np.sin(2 * np.pi * 4.2 * f * x) * np.exp(-x * 9)
             + 0.2 * np.sin(2 * np.pi * 2 * f * x))
        e = np.minimum(x / 0.002, 1) * np.exp(-x * 2.6)
    else:  # bell / chime
        s = (np.sin(2 * np.pi * f * x) + 0.5 * np.sin(2 * np.pi * 2.76 * f * x) * np.exp(-x * 2)
             + 0.25 * np.sin(2 * np.pi * 5.4 * f * x) * np.exp(-x * 4))
        e = np.minimum(x / 0.003, 1) * np.exp(-x * 0.9)
    add(s * e * m, pan, g)


def drop(t0, g=0.3, pan=0.0):
    x = t - t0; m = x >= 0; x = np.where(m, x, 0)
    f = 900 + 1400 * np.exp(-x * 40)
    s = np.sin(2 * np.pi * np.cumsum(f * m) / SR) * np.exp(-x * 22) * m
    add(s, pan, g)


def shimmer(t0, notes, kind, step, g, spread=0.6):
    for i, n in enumerate(notes):
        note(t0 + i * step, n, kind, g, (i / max(1, len(notes) - 1) - 0.5) * spread * 2)


# Shared harmony in F major: Fmaj7 · Dm9 · Bbmaj7 · Fadd9
CH = [(0.0, 3.4, ['F3', 'A3', 'C4', 'E4']), (3.4, 6.6, ['D3', 'F3', 'A3', 'E4']),
      (6.6, 9.4, ['Bb2', 'D3', 'F3', 'A3']), (9.4, 12.0, ['F3', 'C4', 'G4', 'A4'])]
counts = [(1.6, 'C6'), (2.6, 'A5'), (3.6, 'F5')]

if style == 'amanecer':
    pad(CH, 0.5, 1.0)
    for t0, n in counts:
        note(t0, n, 'piano', 0.5); note(t0, n[:-1] + str(int(n[-1]) - 1), 'piano', 0.25)
    shimmer(4.9, ['F4', 'A4', 'C5', 'E5', 'G5', 'A5'], 'piano', 0.11, 0.3)
    mel = [(5.9, 'A5'), (6.5, 'G5'), (7.2, 'F5'), (7.8, 'E5'), (8.4, 'D5'), (8.9, 'C5'), (9.5, 'A4'), (10.1, 'C5'), (10.7, 'F5')]
    for t0, n in mel: note(t0, n, 'piano', 0.35, 0.15)
    shimmer(8.9, ['C6', 'F6'], 'bell', 0.25, 0.12)
elif style == 'petalos':
    pad(CH, 0.32, 0.6)
    for t0, n in counts: note(t0, n, 'box', 0.5)
    mel = [(4.9, 'C6'), (5.2, 'A5'), (5.5, 'F5'), (5.8, 'A5'), (6.1, 'C6'), (6.7, 'D6'), (7.0, 'C6'), (7.3, 'A5'),
           (7.6, 'G5'), (8.2, 'F5'), (8.5, 'G5'), (8.8, 'A5'), (9.1, 'C6'), (9.7, 'A5'), (10.3, 'F5'), (10.9, 'C6'), (11.2, 'F6')]
    for i, (t0, n) in enumerate(mel): note(t0, n, 'box', 0.38, 0.3 if i % 2 else -0.3)
    for t0 in (4.9, 6.6, 8.2, 9.7): note(t0, 'F4', 'box', 0.18)
    shimmer(8.9, ['A6', 'C7', 'F7'], 'bell', 0.09, 0.06)
else:  # luna
    pad(CH, 0.45, 0.4)
    # gentle night air
    air = np.convolve(rng.standard_normal(N), np.ones(200) / 200, 'same') * 0.6
    add(air * seg(0, 12, 2, 1.5), -0.5, 1.0); add(np.roll(air, 3000) * seg(0, 12, 2, 1.5), 0.5, 1.0)
    for t0, n in counts:
        note(t0, n, 'bell', 0.35); drop(t0 + 0.02, 0.25)
    drop(5.1, 0.2, -0.2)
    shimmer(4.9, ['F5', 'C6', 'A5', 'E6', 'C6'], 'bell', 0.22, 0.16)
    shimmer(7.2, ['A5', 'G5', 'F5', 'C5'], 'bell', 0.5, 0.18)
    # shooting star sparkle + wish
    shimmer(8.6, ['C7', 'A6', 'F6', 'E6', 'C6', 'A5'], 'bell', 0.07, 0.07, 0.9)
    note(9.6, 'F5', 'bell', 0.22); note(10.4, 'C6', 'bell', 0.15)

# Lush reverb
def reverb(x, seed, decay):
    n_ir = int(SR * 3.0); r = np.random.default_rng(seed)
    ir = r.standard_normal(n_ir) * np.exp(-np.arange(n_ir) / (SR * decay)); ir /= np.sqrt(np.sum(ir ** 2))
    n = len(x) + n_ir
    return np.fft.irfft(np.fft.rfft(x, n) * np.fft.rfft(ir, n), n)[:len(x)]

dec = {'amanecer': 0.7, 'petalos': 0.55, 'luna': 0.9}[style]
L2 = L + 0.45 * reverb(L, 1, dec); R2 = R + 0.45 * reverb(R, 2, dec)
mixd = np.stack([L2, R2], 1)
mixd = np.tanh(mixd * 0.9)
mixd /= np.max(np.abs(mixd)) / 0.85
fade = np.clip(t / 0.6, 0, 1) * np.clip((12 - t) / 1.0, 0, 1)
mixd *= fade[:, None]
with wave.open(out, 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((mixd * 32767).astype('<i2').tobytes())
print('wrote', out)
