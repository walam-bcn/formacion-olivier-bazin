"""Synthesizes the soundtrack (12 s, 48 kHz stereo) synced to scene.html.
Usage: python3 audio.py out.wav
"""
import sys, wave
import numpy as np

SR, DUR = 48000, 12.0
N = int(SR * DUR)
t = np.arange(N) / SR
rng = np.random.default_rng(3)
L = np.zeros(N); R = np.zeros(N)


@np.errstate(over="ignore")
def env(t0, a, d, length=None):
    """attack/exp-decay envelope starting at t0"""
    x = t - t0
    e = np.where(x < 0, 0, np.where(x < a, x / max(a, 1e-6), np.exp(-(x - a) / d)))
    if length:
        e *= (x < length)
    return e


def lowpass(x, cutoff):
    a = np.exp(-2 * np.pi * cutoff / SR)
    y = np.empty_like(x); acc = 0.0
    for i in range(len(x)):
        acc = (1 - a) * x[i] + a * acc; y[i] = acc
    return y


def add(sig, pan=0.0, gain=1.0):
    global L, R
    L += sig * gain * np.sqrt((1 - pan) / 2)
    R += sig * gain * np.sqrt((1 + pan) / 2)


# 1. Drone: detuned low sines + slow LFO, swells in, cuts at the end
fade_in = np.clip((t - 0.3) / 2.0, 0, 1)
fade_out = np.clip((11.7 - t) / 0.6, 0, 1)
lfo = 0.7 + 0.3 * np.sin(2 * np.pi * 0.25 * t)
drone = (np.sin(2 * np.pi * 41.2 * t) + 0.7 * np.sin(2 * np.pi * 41.6 * t + 1)
         + 0.35 * np.sin(2 * np.pi * 82.4 * t) + 0.15 * np.sin(2 * np.pi * 123.5 * t))
drone *= fade_in * fade_out * lfo * 0.22
add(drone, -0.1); add(np.roll(drone, 300), 0.1)

# airy pad (filtered noise) after the impact
pad = lowpass(rng.standard_normal(N), 900) * np.clip((t - 5.1) / 1.5, 0, 1) * fade_out * 0.35
add(pad, -0.6); add(np.roll(pad, 2000), 0.6)

# 2. Laser intro: rising sine sweep 0.25-1.3 s
seg = (t > 0.2) & (t < 1.6)
f = 180 + 2200 * np.clip((t - 0.25) / 1.05, 0, 1) ** 2
ph = 2 * np.pi * np.cumsum(f) / SR
las = np.sin(ph) * seg * np.clip((t - 0.2) / 0.3, 0, 1) * np.clip((1.6 - t) / 0.35, 0, 1) * 0.12
add(las, -0.4); add(np.roll(las, 900), 0.4)


# 3. Hits on 3-2-1 (t = 2,3,4) and the big impact at 5
def hit(t0, big=False):
    x = np.clip(t - t0, 0, None)
    fsweep = 45 + (140 if big else 110) * np.exp(-x * 18)
    kick = np.sin(2 * np.pi * np.cumsum(fsweep) / SR) * env(t0, 0.002, 0.55 if big else 0.28)
    click = rng.standard_normal(N) * env(t0, 0.0005, 0.012)
    ping = (np.sin(2 * np.pi * 1760 * x) + 0.5 * np.sin(2 * np.pi * 2637 * x)) * env(t0, 0.001, 0.18) * 0.25
    add(kick, 0, 0.9 if big else 0.75)
    add(click, 0, 0.25)
    add(ping, -0.3, 0.6); add(np.roll(ping, 600), 0.3, 0.6)
    if big:
        boom = lowpass(rng.standard_normal(N), 300) * env(t0, 0.003, 1.2) * 2.2
        crash = rng.standard_normal(N) * env(t0, 0.001, 0.6) * 0.18
        add(boom, -0.2); add(np.roll(boom, 700), 0.2)
        add(crash, -0.5); add(np.roll(crash, 450), 0.5)


for t0 in (2.0, 3.0, 4.0):
    hit(t0)
hit(5.0, big=True)

# 4. Riser 4.0 -> 5.0: noise with rising brightness + pitch
rmask = np.clip((t - 3.9) / 1.1, 0, 1) * (t < 5.0)
noise = rng.standard_normal(N)
riser = (lowpass(noise, 1500) * 0.6 + noise * 0.15) * rmask ** 2.5
f = 300 + 1800 * rmask ** 2
riser += np.sin(2 * np.pi * np.cumsum(f) / SR) * rmask ** 3 * 0.15
add(riser, -0.3, 0.7); add(np.roll(riser, 500), 0.3, 0.7)

# reverse swell before the outro
rev = lowpass(noise, 2500) * np.clip((t - 10.2) / 0.8, 0, 1) ** 3 * (t < 11.0) * 0.5
add(rev, 0)

# 5. Glitch blips (synced with visual glitch bursts + text decode)
for i, g in enumerate((1.95, 2.95, 3.95, 5.3, 6.4, 7.28, 8.9, 9.7, 10.85)):
    for k in range(6):
        t0 = g - 0.05 + k * 0.022 + rng.random() * 0.01
        fq = rng.choice([880, 1320, 2200, 3300, 660])
        sq = np.sign(np.sin(2 * np.pi * fq * (t - t0))) * env(t0, 0.0005, 0.008, 0.03) * 0.09
        add(sq, rng.uniform(-0.8, 0.8))

# decode "typing" ticks during titles
for t0 in np.arange(5.25, 6.4, 0.045):
    add(rng.standard_normal(N) * env(t0, 0.0003, 0.004, 0.02) * 0.12, rng.uniform(-0.5, 0.5))
for t0 in np.arange(7.3, 8.4, 0.05):
    add(rng.standard_normal(N) * env(t0, 0.0003, 0.004, 0.02) * 0.10, rng.uniform(-0.5, 0.5))

# 6. Clock ticks every 0.5 s while titles hold
for t0 in np.arange(5.5, 10.6, 0.5):
    x = t - t0
    add(np.sin(2 * np.pi * 4200 * x) * env(t0, 0.0005, 0.01, 0.05) * 0.12, 0.5 if int(t0 * 2) % 2 else -0.5)

# outro hit + tail
x = np.clip(t - 11.05, 0, None)
add(np.sin(2 * np.pi * np.cumsum(40 + 90 * np.exp(-x * 14)) / SR) * env(11.05, 0.002, 0.45), 0, 0.8)
add((np.sin(2 * np.pi * 1318 * x) + 0.6 * np.sin(2 * np.pi * 1975 * x)) * env(11.05, 0.002, 0.35) * 0.2, 0)

# simple stereo reverb (exp-decay noise IR, FFT convolution)
def reverb(x, seed):
    ir_len = int(SR * 1.8)
    r = np.random.default_rng(seed)
    ir = r.standard_normal(ir_len) * np.exp(-np.arange(ir_len) / (SR * 0.45))
    ir /= np.sqrt(np.sum(ir ** 2))
    n = len(x) + ir_len
    y = np.fft.irfft(np.fft.rfft(x, n) * np.fft.rfft(ir, n), n)[:len(x)]
    return y

L = L + 0.28 * reverb(L, 11); R = R + 0.28 * reverb(R, 12)

# master: soft clip + normalize + fade edges
mix = np.stack([L, R], 1)
mix = np.tanh(mix * 1.2)
mix /= np.max(np.abs(mix)) / 0.89
mix[: int(0.02 * SR)] *= np.linspace(0, 1, int(0.02 * SR))[:, None]
mix[-int(0.3 * SR):] *= np.linspace(1, 0, int(0.3 * SR))[:, None]

out = sys.argv[1] if len(sys.argv) > 1 else 'soundtrack.wav'
with wave.open(out, 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((mix * 32767).astype('<i2').tobytes())
print('wrote', out)
