#!/usr/bin/env python3
"""
Schumann-Orbital Alignment Test
================================

Question: Is the Schumann resonance spectrum (the Earth-ionosphere cavity
standing wave) phase-locked to the orbital beat-frequency geometry of the
classical seven, or is it independent?

Method: Take the full orbital beat spectrum (fundamentals, pairwise beats,
triple beats — 133 voices). Sweep the single compression scalar across many
orders of magnitude. At each compression, measure how close the orbital
spectrum lines up with the Schumann mode set {7.83, 14.3, 20.8, 27.3, 33.8}.

If there is structural phase-lock between the orbital field and the
Earth-cavity field, we expect to see one or more compressions where the
total alignment error drops sharply — natural minima — not just where one
voice happens to coincide. A natural alignment would manifest as multiple
voices landing on multiple Schumann modes simultaneously at the same
compression.

If no such minima exist, the systems are likely independent and any single-
voice alignment is just where you set the dial.

This script does no tuning. It computes the orbital geometry from raw
sidereal periods and reports what falls out.
"""

import math
import numpy as np

# Sidereal orbital periods in days (same as song_of_the_spheres.py).
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

# Schumann resonance modes (Hz). Standard textbook values for the first
# five modes of the Earth-ionosphere cavity.
SCHUMANN_MODES_HZ = [7.83, 14.3, 20.8, 27.3, 33.8]


def orbital_frequency_hz(period_days: float) -> float:
    return 1.0 / (period_days * SECONDS_PER_DAY)


def all_orbital_voices_hz(compression: float):
    """
    Returns a list of (label, frequency_hz) for every voice in the song:
    7 fundamentals + 21 pairwise beats + 105 triple beats = 133 voices.
    """
    names = list(ORBITS_DAYS.keys())
    f = {n: orbital_frequency_hz(ORBITS_DAYS[n]) * compression for n in names}
    voices = []
    # Fundamentals
    for n in names:
        voices.append((f"{n}", f[n]))
    # Pairwise beats
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            a, b = names[i], names[j]
            beat = abs(f[a] - f[b])
            voices.append((f"|{a}-{b}|", beat))
    # Triple beats: |f_i + f_j - f_k|, k != i, j
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            for k in range(len(names)):
                if k == i or k == j:
                    continue
                a, b, c = names[i], names[j], names[k]
                triple = abs(f[a] + f[b] - f[c])
                voices.append((f"|{a}+{b}-{c}|", triple))
    return voices


def alignment_error(compression: float,
                    schumann_modes=SCHUMANN_MODES_HZ,
                    log_metric: bool = True):
    """
    Total alignment error between orbital spectrum and Schumann modes at a
    given compression scalar.

    For each Schumann mode, find the orbital voice with the smallest
    relative offset. Sum (or take RMS of) those offsets.

    Using log-frequency distance because we're comparing across decades.
    A 0.1 Hz offset at 8 Hz is meaningful; the same offset at 800 Hz is
    not. Log distance is scale-invariant.
    """
    voices = all_orbital_voices_hz(compression)
    voice_freqs = np.array([v[1] for v in voices if v[1] > 0])
    if len(voice_freqs) == 0:
        return float("inf")
    log_voices = np.log(voice_freqs)
    total = 0.0
    per_mode = []
    for mode in schumann_modes:
        log_mode = math.log(mode)
        # Smallest log-distance from this mode to any orbital voice.
        offsets = np.abs(log_voices - log_mode)
        best = float(np.min(offsets))
        per_mode.append(best)
        if log_metric:
            total += best * best
        else:
            total += best
    if log_metric:
        total = math.sqrt(total / len(schumann_modes))
    else:
        total = total / len(schumann_modes)
    return total, per_mode


def closest_voices_to_schumann(compression: float,
                               schumann_modes=SCHUMANN_MODES_HZ,
                               n_per_mode: int = 3):
    """
    For each Schumann mode at this compression, list the n closest orbital
    voices with their frequencies and relative offsets.
    """
    voices = all_orbital_voices_hz(compression)
    out = {}
    for mode in schumann_modes:
        ranked = []
        for label, f in voices:
            if f <= 0:
                continue
            rel_offset = abs(f - mode) / mode
            ranked.append((rel_offset, label, f))
        ranked.sort()
        out[mode] = ranked[:n_per_mode]
    return out


def sweep_compression(c_min_log10: float = 7.0,
                      c_max_log10: float = 11.0,
                      n_steps: int = 4001):
    """
    Sweep compression scalar logarithmically from 10^c_min_log10 to
    10^c_max_log10. At each step, compute total alignment error to the
    Schumann mode set.

    Returns arrays (compressions, errors, per_mode_errors).
    """
    log_cs = np.linspace(c_min_log10, c_max_log10, n_steps)
    cs = 10.0 ** log_cs
    errors = np.zeros_like(cs)
    per_mode = np.zeros((n_steps, len(SCHUMANN_MODES_HZ)))
    for idx, c in enumerate(cs):
        e, pm = alignment_error(c)
        errors[idx] = e
        per_mode[idx] = pm
    return cs, errors, per_mode


def find_local_minima(cs, errors, top_n: int = 10):
    """
    Find the deepest local minima in the error curve.
    A point is a local min if it's lower than its immediate neighbors.
    """
    minima = []
    for i in range(1, len(errors) - 1):
        if errors[i] < errors[i - 1] and errors[i] < errors[i + 1]:
            minima.append((errors[i], cs[i], i))
    minima.sort()
    return minima[:top_n]


def baseline_random_test(n_trials: int = 200,
                         compression: float = 1.0e9,
                         seed: int = 42):
    """
    Null hypothesis test: is the orbital-Schumann alignment at a given
    compression any better than alignment to a *random* set of 5 frequencies
    in the same Schumann band?

    We generate n_trials random "fake Schumann" sets — 5 frequencies drawn
    uniformly in [5, 40] Hz — and measure the alignment error of the same
    orbital spectrum to each fake set. Then we report where the real
    Schumann alignment ranks in the distribution.
    """
    rng = np.random.default_rng(seed)
    real_err, _ = alignment_error(compression, SCHUMANN_MODES_HZ)
    null_errs = []
    for _ in range(n_trials):
        fake = sorted(rng.uniform(5.0, 40.0, size=len(SCHUMANN_MODES_HZ)).tolist())
        e, _ = alignment_error(compression, fake)
        null_errs.append(e)
    null_errs = np.array(null_errs)
    rank = int(np.sum(null_errs < real_err))
    pct = rank / n_trials * 100
    return {
        "real_error": real_err,
        "null_mean": float(np.mean(null_errs)),
        "null_median": float(np.median(null_errs)),
        "null_min": float(np.min(null_errs)),
        "null_max": float(np.max(null_errs)),
        "rank_among_null": rank,
        "percentile": pct,  # lower is better; <5 means real alignment is better than 95% of random sets
        "n_trials": n_trials,
    }


def main():
    print("=" * 72)
    print("Schumann-Orbital Alignment Test")
    print("=" * 72)
    print(f"\nSchumann modes (Hz): {SCHUMANN_MODES_HZ}")
    print(f"Orbital voices: 133 (7 fundamentals + 21 beats + 105 triples)")
    print(f"Metric: RMS log-frequency distance (scale-invariant)\n")

    # 1. Sweep across 4 orders of magnitude of compression.
    print("Sweeping compression scalar from 1e7 to 1e11 (4001 steps)...")
    cs, errors, per_mode = sweep_compression()

    # 2. Find the deepest local minima.
    minima = find_local_minima(cs, errors, top_n=15)
    print(f"\nDeepest 15 local minima of alignment error:\n")
    print(f"  {'rank':>4}  {'compression':>14}  {'rms log err':>12}")
    for rank, (err, c, idx) in enumerate(minima, start=1):
        print(f"  {rank:>4}  {c:>14.3e}  {err:>12.5f}")

    # 3. At the deepest minimum, show which orbital voices align with which
    #    Schumann modes.
    if minima:
        best_err, best_c, best_idx = minima[0]
        print(f"\n--- Best alignment found at compression = {best_c:.3e} ---")
        print(f"RMS log-distance error = {best_err:.5f}")
        print(f"\nClosest 3 orbital voices to each Schumann mode at this compression:\n")
        closest = closest_voices_to_schumann(best_c, n_per_mode=3)
        for mode, ranked in closest.items():
            print(f"  Schumann {mode} Hz:")
            for rel_off, label, f in ranked:
                pct_off = rel_off * 100
                print(f"    {label:>30s}  =  {f:>10.4f} Hz   ({pct_off:>6.2f}% off)")

    # 4. Compare alignment quality at our original compression (1e9) and at
    #    the best-found compression vs. random Schumann-like sets.
    print(f"\n--- Null hypothesis test ---")
    print(f"Is the real Schumann set's alignment any better than a random set\n"
          f"of 5 frequencies drawn uniformly in [5, 40] Hz?\n")

    for label, c in [("Original 1e9 compression", 1.0e9),
                     ("Best-found compression", minima[0][1] if minima else 1.0e9)]:
        result = baseline_random_test(n_trials=500, compression=c)
        print(f"  {label} (c = {c:.3e}):")
        print(f"    Real Schumann alignment error:  {result['real_error']:.5f}")
        print(f"    Random sets (n={result['n_trials']}):")
        print(f"      mean   = {result['null_mean']:.5f}")
        print(f"      median = {result['null_median']:.5f}")
        print(f"      min    = {result['null_min']:.5f}")
        print(f"      max    = {result['null_max']:.5f}")
        print(f"    Real ranks at percentile {result['percentile']:.1f}% of random distribution")
        print(f"    (lower = real is more aligned than random; <5% would be significant)\n")

    # 5. Look at where the per-mode errors all simultaneously dip — the
    #    signature of *multi-mode* phase-lock rather than just one voice
    #    happening to land on one mode.
    print("--- Multi-mode coincidence search ---")
    print("Finding compressions where ALL 5 Schumann modes have low offset")
    print("simultaneously (each mode within 5% of an orbital voice):\n")
    multi_lock = []
    for i, c in enumerate(cs):
        # offset for mode m = exp(per_mode[i,m]) - 1 approximately, but for
        # log distances < 0.1 the relation is roughly linear.
        # Convert log distance back to relative offset.
        rel_offsets = np.exp(per_mode[i]) - 1.0
        if np.all(rel_offsets < 0.05):
            multi_lock.append((float(np.max(rel_offsets)), c))
    multi_lock.sort()
    if multi_lock:
        print(f"  Found {len(multi_lock)} compressions where all 5 modes")
        print(f"  align within 5% of an orbital voice.")
        print(f"\n  Top 10 (sorted by worst-mode offset, smallest first):")
        for rank, (worst, c) in enumerate(multi_lock[:10], start=1):
            print(f"    {rank:>3}.  compression = {c:.3e}   worst-mode offset = {worst*100:.2f}%")
    else:
        print("  No compression found where all 5 Schumann modes are within")
        print("  5% of an orbital voice simultaneously.")

    print("\n" + "=" * 72)
    print("Interpretation:")
    print("=" * 72)
    print("""
  - If the deepest minima have RMS log-error << random-set median, that's
    evidence the orbital geometry has structural phase-lock points with
    the Schumann set that are NOT explainable by chance density of voices.

  - If the multi-mode coincidence search returns many compressions where
    all 5 modes lock simultaneously, that's strong structural evidence.
    If it returns zero, single-voice coincidences at any compression are
    explained by the sheer number of voices (133) covering the band.

  - If the random-set null distribution overlaps the real Schumann error,
    the systems are likely independent, and any apparent alignment in the
    original 1e9 rendering is the "you'll find SOMETHING when you have 133
    voices and 5 targets" effect.
""")


if __name__ == "__main__":
    main()
