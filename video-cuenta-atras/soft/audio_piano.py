"""Enveloping piano piece for the hourglass reel (12 s, 48 kHz stereo).
Usage: python3 audio_piano.py out.wav

Synced to common.js: counts 1.6/2.6/3.6 s, Spanish title 4.9 s,
English 7.2 s, date 8.9 s, breathe out from 10.9 s.
"""
import sys, wave
import numpy as np

SR, DUR = 48000, 12.0
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


# ---------------- the piece (D major, ~72 bpm feel) ----------------
# Intro: low resonant octave + slow rising arpeggio (Dmaj9)
piano(0.15, 'D2', 0.55, 6); piano(0.15, 'D3', 0.4, 6)
arp(0.35, ['A3', 'D4', 'F#4', 'A4', 'E5'], 0.24, 0.35, 5.5)

# Countdown 3 · 2 · 1 — descending high notes over shifting bass
piano(1.6, 'F#5', 0.55, 4); piano(1.6, 'B2', 0.45, 3.5); piano(1.62, 'F#3', 0.3, 3.5)       # Bm
piano(2.6, 'E5', 0.52, 4); piano(2.6, 'G2', 0.45, 3.5); piano(2.62, 'D3', 0.3, 3.5)         # Gmaj
piano(3.6, 'D5', 0.5, 4); piano(3.6, 'A2', 0.5, 3.5); piano(3.62, 'E3', 0.32, 3.5)          # A sus
arp(4.0, ['A3', 'C#4', 'E4', 'G4'], 0.18, 0.3, 3)                                           # A7 lift

# Title (4.9): full open D chord + melody, strings swell in
piano(4.9, 'D2', 0.7, 7); piano(4.9, 'A2', 0.55, 7)
arp(4.9, ['D3', 'A3', 'E4', 'F#4'], 0.06, 0.45, 6)
mel = [(4.9, 'A5', 0.62), (5.75, 'F#5', 0.5), (6.2, 'E5', 0.45), (6.6, 'D5', 0.5),
       (7.2, 'E5', 0.55), (7.65, 'F#5', 0.5), (8.1, 'B5', 0.6), (8.9, 'A5', 0.62),
       (9.4, 'F#5', 0.5), (9.85, 'E5', 0.45), (10.3, 'D5', 0.5), (10.9, 'A5', 0.45), (11.15, 'D6', 0.4)]
for t0, n, v in mel: piano(t0, n, v, 4.5)
strings(4.6, 12.0, ['D3', 'A3', 'F#4'], 0.05)

# English (7.2): Bm9 — rolling left hand
piano(7.2, 'B1', 0.55, 5); piano(7.2, 'B2', 0.45, 5)
arp(7.3, ['F#3', 'A3', 'C#4', 'D4', 'F#4', 'D4', 'C#4', 'A3'], 0.2, 0.28, 3.5)
strings(7.0, 12.0, ['B2', 'F#3', 'D4'], 0.035)

# Date (8.9): Gmaj7 → A → home on D
piano(8.9, 'G1', 0.55, 4); piano(8.9, 'G2', 0.45, 4)
arp(8.95, ['D3', 'F#3', 'B3', 'D4'], 0.16, 0.3, 3.5)
piano(9.9, 'A1', 0.5, 3); piano(9.9, 'E3', 0.3, 3)
piano(10.9, 'D2', 0.55, 1.4); piano(10.9, 'A2', 0.4, 1.4)
arp(10.9, ['D3', 'F#3', 'A3', 'E4', 'A4'], 0.09, 0.3, 1.4)

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
mix *= (np.clip(t / 0.08, 0, 1) * np.clip((12 - t) / 1.1, 0, 1))[:, None]
with wave.open(sys.argv[1], 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((mix * 32767).astype('<i2').tobytes())
print('wrote', sys.argv[1])
