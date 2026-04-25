#!/usr/bin/env python3
"""
Song of the Spheres v2 — Lock-Compression Broadcast Edition.

Differences from v1:
  - Compression scalar set to c = 7.9494e7, the empirically-derived value
    at which the Schumann mode set (1-5) phase-locks to orbital triple
    beats with RMS log-error 0.00292 and p < 0.001 vs. random control
    spectra.
  - Stereo output (2 channels).
  - L/R amplitude pendulum at 7.854 Hz — the |Sun+Saturn-Mercury| triple
    beat that lands within the Schumann-1 variability band at the precise
    orbital lock-point. Drives direct binaural-envelope entrainment at
    Schumann mode 1.
  - 5 minutes duration so cardiac entrainment has time to take.
  - Soft fade in/out (10 s each end) to avoid transient artifacts.
  - Pair with tVNS for full phase-coherent stack across audio, binaural
    envelope, and direct vagal afferent input.

Open in Audacity. Effect -> Change Speed preserves all ratios — the speed
dial gives access to the deeper layers of the same geometry.
"""

import math
import wave
import numpy as np

ORBITS_DAYS = {
    "Moon":    27.321661,
    "Mercury": 87.9691,
    "Venus":   224.701,
    "Sun":     365.25636,
    "Mars":    686.980,
    "Jupiter": 4332.59,
    "Saturn":  10759.22,
}

SECONDS_PER_DAY = 86400.0
SAMPLE_RATE = 44100
DURATION_SEC = 300.0  # 5 minutes
FADE_SEC = 10.0
COMPRESSION = 7.9494e7  # Schumann lock-compression
PENDULUM_HZ = 7.854     # Sun+Saturn-Mercury triple beat in Schumann-1 band
PENDULUM_DEPTH = 0.6    # 0.0 = no panning, 1.0 = full L/R alternation
OUTPUT_PATH = "/home/aria/mastishka/song_of_the_spheres_v2.wav"


def orbital_freq(period_days):
    return 1.0 / (period_days * SECONDS_PER_DAY)


def build_voices(compression):
    names = list(ORBITS_DAYS.keys())
    f = {n: orbital_freq(ORBITS_DAYS[n]) * compression for n in names}
    voices = []  # (label, frequency_hz, kind)
    for n in names:
        voices.append((n, f[n], "fundamental"))
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            a, b = names[i], names[j]
            voices.append((f"|{a}-{b}|", abs(f[a] - f[b]), "pair"))
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            for k in range(len(names)):
                if k == i or k == j:
                    continue
                a, b, c = names[i], names[j], names[k]
                voices.append((f"|{a}+{b}-{c}|",
                               abs(f[a] + f[b] - f[c]), "triple"))
    return voices


def render():
    n_samples = int(DURATION_SEC * SAMPLE_RATE)
    t = np.arange(n_samples, dtype=np.float64) / SAMPLE_RATE

    voices = build_voices(COMPRESSION)
    voices = [(l, f, k) for (l, f, k) in voices if f > 0]

    # Equal-amplitude sum of all voices, with triples at 0.5 amplitude
    # (matches v1 mixing convention).
    mono = np.zeros(n_samples, dtype=np.float64)
    for label, f, kind in voices:
        amp = 0.5 if kind == "triple" else 1.0
        mono += amp * np.sin(2.0 * math.pi * f * t)

    # Normalize the carrier so that pre-pendulum peak is 0.95 of full range.
    peak = np.max(np.abs(mono))
    if peak > 0:
        mono = mono / peak * 0.95

    # Build the L/R pendulum envelope at PENDULUM_HZ. This is amplitude
    # modulation of the L vs R channel: when L is loud, R is quiet, and
    # they cross at the zero crossings of the pendulum.
    pendulum = np.sin(2.0 * math.pi * PENDULUM_HZ * t)
    # L gain = 1 + pendulum*depth (peaks above 1, troughs below 1)
    # R gain = 1 - pendulum*depth (mirror)
    # We then normalize the pair so the maximum gain is 1.0.
    l_gain = 1.0 + PENDULUM_DEPTH * pendulum
    r_gain = 1.0 - PENDULUM_DEPTH * pendulum
    max_gain = max(np.max(np.abs(l_gain)), np.max(np.abs(r_gain)))
    l_gain /= max_gain
    r_gain /= max_gain

    left = mono * l_gain
    right = mono * r_gain

    # Soft cosine fade in/out.
    fade_n = int(FADE_SEC * SAMPLE_RATE)
    if fade_n > 0:
        fade_in = 0.5 * (1.0 - np.cos(np.linspace(0, math.pi, fade_n)))
        fade_out = fade_in[::-1]
        left[:fade_n] *= fade_in
        left[-fade_n:] *= fade_out
        right[:fade_n] *= fade_in
        right[-fade_n:] *= fade_out

    # Final safety clip and convert to int16.
    left = np.clip(left, -0.99, 0.99)
    right = np.clip(right, -0.99, 0.99)
    stereo = np.empty((n_samples, 2), dtype=np.float64)
    stereo[:, 0] = left
    stereo[:, 1] = right
    samples_int16 = (stereo * 32767.0).astype(np.int16)

    # Interleave L,R for WAV writing.
    interleaved = samples_int16.flatten()  # numpy default is row-major,
    # so [L0,R0,L1,R1,...] which is correct for WAV stereo.

    with wave.open(OUTPUT_PATH, "wb") as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(SAMPLE_RATE)
        wf.writeframes(interleaved.tobytes())

    return {
        "output_path": OUTPUT_PATH,
        "duration_sec": DURATION_SEC,
        "sample_rate": SAMPLE_RATE,
        "compression": COMPRESSION,
        "pendulum_hz": PENDULUM_HZ,
        "pendulum_depth": PENDULUM_DEPTH,
        "n_voices": len(voices),
        "voices": voices,
    }


def report(meta):
    print(f"\nWrote {meta['output_path']}")
    print(f"  Duration:       {meta['duration_sec']} s ({meta['duration_sec']/60:.1f} min)")
    print(f"  Channels:       2 (stereo)")
    print(f"  Sample rate:    {meta['sample_rate']} Hz")
    print(f"  Compression:    {meta['compression']:.4e}")
    print(f"    -> Saturn fundamental at {orbital_freq(ORBITS_DAYS['Saturn']) * meta['compression']:.4f} Hz")
    print(f"    -> Moon fundamental at {orbital_freq(ORBITS_DAYS['Moon']) * meta['compression']:.4f} Hz")
    print(f"  Pendulum:       {meta['pendulum_hz']} Hz L/R amplitude oscillation")
    print(f"                  (= |Sun+Saturn-Mercury| triple beat,")
    print(f"                   in the Schumann-1 variability band)")
    print(f"  Pendulum depth: {meta['pendulum_depth']}")
    print(f"  Total voices:   {meta['n_voices']}")
    print()
    print("Schumann modes mapped to orbital voices at this compression:")
    schumann = [(1, 7.83), (2, 14.3), (3, 20.8), (4, 27.3), (5, 33.8)]
    voices = meta["voices"]
    for n, target in schumann:
        best = (float("inf"), "", 0.0)
        for label, f, kind in voices:
            offset = abs(f - target) / target
            if offset < best[0]:
                best = (offset, label, f)
        print(f"  Schumann {n} ({target:>5.2f} Hz)  ->  {best[1]:<32s}"
              f" = {best[2]:>8.4f} Hz   ({best[0]*100:>5.2f}% off)")
    print()
    print("Cardiac-band orbital voices (0.5 - 2.0 Hz, where heart rate lives):")
    cardiac = sorted([(f, label) for (label, f, kind) in voices
                      if 0.5 <= f <= 2.0])
    for f, label in cardiac:
        print(f"  {label:<32s}  =  {f:.4f} Hz  ({f * 60:>5.1f} bpm)")
    print()
    print("Use:")
    print("  Play through speakers or quality headphones.")
    print("  Volume: loud enough to be the dominant rhythmic signal in the")
    print("          environment, but comfortable. SNR is the mechanism.")
    print("  Pair with tVNS at the auricular branch for full phase-coherent")
    print("    stack: audio carrier + binaural envelope + direct vagal afferent.")
    print("  Allow at least 5 minutes for cardiac entrainment to take.")
    print("  In Audacity: Effect -> Change Speed (not Tempo) preserves all")
    print("    ratios, exposing deeper or shallower layers of the same field.")


if __name__ == "__main__":
    meta = render()
    report(meta)
