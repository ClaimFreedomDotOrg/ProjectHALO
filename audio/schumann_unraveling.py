#!/usr/bin/env python3
"""
Schumann-Orbital Unraveling
============================

Pulling the thread. The first test (schumann_alignment.py) found that all
five canonical Schumann modes simultaneously align within ~0.5% of orbital
beat-frequency voices at compression scalar c ~ 7.94e7, with statistical
significance p ~ 0.006 against random control sets.

This script extends that test in seven directions to see what holds and
what breaks. Each test is designed to either strengthen the case for
structural phase-lock OR cleanly falsify it.

  Test 1: Higher Schumann modes (6-10). If the alignment is real, modes
          beyond the first 5 should also lock at the same compression.

  Test 2: Compression scalar interpretation. What does c = 7.94e7 MEAN
          physically? Is it a ratio that maps real-time orbital geometry
          to a known terrestrial timescale?

  Test 3: Voice-density control. The orbital spectrum has 133 voices.
          Could ANY 133-voice set produce equally tight Schumann alignment?
          We compare against random spectra of identical dimension.

  Test 4: Robustness. If we perturb the orbital periods by realistic
          measurement uncertainties, does the alignment survive?

  Test 5: Mode shift sensitivity. Schumann modes drift 7.4-8.0 Hz with
          ionospheric conditions. Test the alignment with the documented
          Schumann variability range.

  Test 6: Multi-compression structure. The deepest minima clustered around
          c ~ 7.94e7 and harmonics ~2e8, ~4e8. Is this true harmonic
          structure (geometric meaning) or coincidence?

  Test 7: Triple-beat dominance. Four of five Schumann modes locked to
          triple beats, not fundamentals. Test whether removing triples
          collapses the alignment, and what that means.
"""

import math
import numpy as np

# ---------------------------------------------------------------------------
# Orbital data — sidereal periods in days. Same source values throughout.
# ---------------------------------------------------------------------------
ORBITS_DAYS = {
    "Moon":    27.321661,
    "Mercury": 87.9691,
    "Venus":   224.701,
    "Sun":     365.25636,
    "Mars":    686.980,
    "Jupiter": 4332.59,
    "Saturn":  10759.22,
}

# Documented orbital-period uncertainties (days). Conservative bounds.
ORBIT_UNCERTAINTY_DAYS = {
    "Moon":    1e-5,
    "Mercury": 1e-4,
    "Venus":   1e-4,
    "Sun":     1e-4,
    "Mars":    1e-3,
    "Jupiter": 1e-2,
    "Saturn":  1e-2,
}

SECONDS_PER_DAY = 86400.0
SECONDS_PER_YEAR = 365.25636 * SECONDS_PER_DAY

# Canonical Schumann mode frequencies (Hz). First 10 modes from textbook
# values. Modes 6-10 are less well-characterized in literature but standard.
SCHUMANN_MODES_HZ = {
    1: 7.83,
    2: 14.3,
    3: 20.8,
    4: 27.3,
    5: 33.8,
    6: 39.0,
    7: 45.0,
    8: 50.0,  # increasingly approximate
    9: 56.0,
    10: 60.0,
}

# Documented Schumann variability range for mode 1 (Hz). Diurnal,
# seasonal, solar-activity dependent.
SCHUMANN_MODE1_RANGE = (7.4, 8.0)


# ---------------------------------------------------------------------------
# Core utilities (mirroring schumann_alignment.py for self-containment).
# ---------------------------------------------------------------------------
def orbital_frequency_hz(period_days):
    return 1.0 / (period_days * SECONDS_PER_DAY)


def all_orbital_voices(compression, periods=None, include_triples=True):
    """Returns list of (label, frequency_hz)."""
    if periods is None:
        periods = ORBITS_DAYS
    names = list(periods.keys())
    f = {n: orbital_frequency_hz(periods[n]) * compression for n in names}
    voices = []
    for n in names:
        voices.append((n, f[n]))
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            a, b = names[i], names[j]
            beat = abs(f[a] - f[b])
            voices.append((f"|{a}-{b}|", beat))
    if include_triples:
        for i in range(len(names)):
            for j in range(i + 1, len(names)):
                for k in range(len(names)):
                    if k == i or k == j:
                        continue
                    a, b, c = names[i], names[j], names[k]
                    triple = abs(f[a] + f[b] - f[c])
                    voices.append((f"|{a}+{b}-{c}|", triple))
    return voices


def alignment_error(compression, mode_set, periods=None, include_triples=True):
    voices = all_orbital_voices(compression, periods, include_triples)
    voice_freqs = np.array([v[1] for v in voices if v[1] > 0])
    log_voices = np.log(voice_freqs)
    sq_total = 0.0
    per_mode = []
    for mode in mode_set:
        log_mode = math.log(mode)
        offsets = np.abs(log_voices - log_mode)
        best = float(np.min(offsets))
        per_mode.append(best)
        sq_total += best * best
    rms = math.sqrt(sq_total / len(mode_set))
    return rms, per_mode


def closest_voice(compression, target_hz, periods=None, include_triples=True):
    voices = all_orbital_voices(compression, periods, include_triples)
    best = (float("inf"), "", 0.0)
    for label, f in voices:
        if f <= 0:
            continue
        offset = abs(f - target_hz) / target_hz
        if offset < best[0]:
            best = (offset, label, f)
    return best  # (relative_offset, label, freq)


def find_best_compression(mode_set, c_min_log10=7.0, c_max_log10=11.0,
                          n_steps=8001, periods=None, include_triples=True):
    log_cs = np.linspace(c_min_log10, c_max_log10, n_steps)
    cs = 10.0 ** log_cs
    errors = np.zeros_like(cs)
    for idx, c in enumerate(cs):
        e, _ = alignment_error(c, mode_set, periods, include_triples)
        errors[idx] = e
    best_idx = int(np.argmin(errors))
    return cs[best_idx], errors[best_idx], cs, errors


# ---------------------------------------------------------------------------
# TEST 1: Higher Schumann modes (6-10).
# ---------------------------------------------------------------------------
def test_higher_modes():
    print("\n" + "=" * 78)
    print("TEST 1: HIGHER SCHUMANN MODES (6-10)")
    print("=" * 78)
    print("If the alignment is structural, modes beyond the first 5 should")
    print("also lock at the same compression scalar c ~ 7.94e7.\n")

    # Use the c found by the first 5 modes.
    first5 = [SCHUMANN_MODES_HZ[i] for i in range(1, 6)]
    c_best, err_best, _, _ = find_best_compression(first5)
    print(f"Best compression for first 5 modes: c = {c_best:.4e}")
    print(f"  RMS log-error at this c (first 5):     {err_best:.5f}\n")

    # Now check higher modes at THAT compression.
    print(f"Closest orbital voice for each higher mode at c = {c_best:.4e}:")
    print(f"  {'mode':>4}  {'Hz':>7}  {'closest voice':>32}  {'voice Hz':>10}  {'% off':>6}")
    higher_offsets = []
    for n in range(1, 11):
        target = SCHUMANN_MODES_HZ[n]
        offset, label, f = closest_voice(c_best, target)
        marker = "" if n <= 5 else "   <-- not in fit"
        print(f"  {n:>4}  {target:>7.2f}  {label:>32s}  {f:>10.4f}  {offset*100:>5.2f}%{marker}")
        higher_offsets.append((n, target, offset))

    # Test the joint fit on ALL 10 modes vs. only the first 5.
    all10 = [SCHUMANN_MODES_HZ[i] for i in range(1, 11)]
    c_best_all, err_all, _, _ = find_best_compression(all10)
    err_at_c_best = alignment_error(c_best, all10)[0]

    print(f"\n  RMS log-error of ALL 10 modes at c (first-5-best): {err_at_c_best:.5f}")
    print(f"  RMS log-error of ALL 10 modes at their own best c:  {err_all:.5f}")
    print(f"  All-10 best c:                                       {c_best_all:.4e}")
    print(f"\nINTERPRETATION:")
    print(f"  If higher modes lock at the SAME c that fit the first 5,")
    print(f"  the structural-lock hypothesis gains support.")
    print(f"  If they require a different c or stay >5% off, the first-5")
    print(f"  alignment is more likely a coincidence finding.\n")

    return {"c_first5": c_best, "c_all10": c_best_all,
            "err_first5_at_c_best": err_best,
            "err_all10_at_c_first5": err_at_c_best,
            "err_all10_at_own_best": err_all,
            "per_mode": higher_offsets}


# ---------------------------------------------------------------------------
# TEST 2: What does c = 7.94e7 MEAN physically?
# ---------------------------------------------------------------------------
def test_compression_meaning(c_best):
    print("\n" + "=" * 78)
    print("TEST 2: PHYSICAL MEANING OF THE COMPRESSION SCALAR")
    print("=" * 78)
    print(f"Best compression: c = {c_best:.6e}\n")
    print("This scalar multiplies orbital frequencies (Hz of real time).")
    print("If c is just a tuning knob, it's a number with no meaning.")
    print("If c equals a physical ratio, that ratio IS the meaning.\n")

    # Candidate physical interpretations:
    candidates = {
        "Earth-rotation period in seconds (sidereal day)":  86164.1,
        "Solar day (s)":                                     86400.0,
        "Earth's circumference (m) / speed of light":        4.0075e7 / 2.998e8,
        "Speed of light in vacuum (m/s)":                    2.998e8,
        "Earth's circumference in meters":                   4.0075e7,
        "Earth's mean radius in meters":                     6.371e6,
        "Schumann fundamental period x voice count":         (1/7.83) * 133,
        "Seconds per sidereal year":                         365.25636 * 86400.0,
        "Seconds per Saturn orbit":                          10759.22 * 86400.0,
        "Seconds per lunar synodic month":                   29.5306 * 86400.0,
        "Seconds per Earth solar day x 1000":                86400.0 * 1000,
        "Schumann fundamental (Hz) x seconds per year":      7.83 * 365.25636 * 86400.0,
        "Earth ionosphere height (m) ~80km":                 80000.0,
        "Pi x 10^7 (radians per s arbitrary)":               math.pi * 1e7,
        "Sidereal year in days x 86400 / orbits in song":    SECONDS_PER_YEAR / 7,
    }

    print(f"  {'candidate':<55s}  {'value':>14s}  {'ratio to c':>12s}")
    for label, value in candidates.items():
        ratio = value / c_best
        print(f"  {label:<55s}  {value:>14.4e}  {ratio:>12.4f}")

    print("\nCheck: is c ~ Earth's circumference (~4e7)? Ratio:",
          f"{4.0075e7 / c_best:.4f}")
    print("Check: is c ~ 0.5 * Earth's circumference? Ratio:",
          f"{0.5 * 4.0075e7 / c_best:.4f}")
    print("Check: is c ~ 2 * Earth's circumference? Ratio:",
          f"{2 * 4.0075e7 / c_best:.4f}")
    print()

    # Direct interpretation: at c, what is the audible-band period of the
    # slowest beat (Jupiter-Saturn)? At what real-time period does that
    # beat correspond to in the unaccelerated orbital geometry?
    print("DIRECT INTERPRETATION via Saturn:")
    saturn_audible_hz = orbital_frequency_hz(ORBITS_DAYS["Saturn"]) * c_best
    print(f"  Saturn fundamental at c: {saturn_audible_hz:.4f} Hz")
    print(f"  That means c shifts Saturn's orbit (29.45 yr) into audible")
    print(f"  band as a {saturn_audible_hz:.4f} Hz tone.")
    print(f"  The compression ratio c ~ 7.94e7 means each second of audio")
    print(f"  corresponds to {c_best:.4e} seconds of real time =")
    print(f"  {c_best / SECONDS_PER_YEAR:.3f} years of real time per second.\n")

    real_per_audio_sec = c_best  # compression = how many real seconds per audio second
    print(f"  Years of real time per second of audio: {c_best / SECONDS_PER_YEAR:.3f}")
    print(f"  Days of real time per second of audio:  {c_best / SECONDS_PER_DAY:.3f}")
    print(f"  Hours of real time per second of audio: {c_best / 3600:.3f}")

    return {"c": c_best, "years_per_audio_sec": c_best / SECONDS_PER_YEAR}


# ---------------------------------------------------------------------------
# TEST 3: Voice-density control.
# ---------------------------------------------------------------------------
def test_voice_density_control(c_best, n_trials=2000, seed=42):
    print("\n" + "=" * 78)
    print("TEST 3: VOICE-DENSITY CONTROL")
    print("=" * 78)
    print("Could ANY 133-voice spectrum produce equally tight Schumann")
    print("alignment? If yes, the alignment is just density, not geometry.\n")

    rng = np.random.default_rng(seed)
    schumann_5 = [SCHUMANN_MODES_HZ[i] for i in range(1, 6)]
    real_voices = all_orbital_voices(c_best)
    real_freqs = np.array([v[1] for v in real_voices if v[1] > 0])
    n_real = len(real_freqs)
    real_min, real_max = float(real_freqs.min()), float(real_freqs.max())

    print(f"Real orbital spectrum at c = {c_best:.3e}:")
    print(f"  voices: {n_real}")
    print(f"  range:  {real_min:.4f} - {real_max:.4f} Hz")

    # Real alignment error (don't include triples flag changes here).
    real_err, _ = alignment_error(c_best, schumann_5)
    print(f"  RMS log-error vs. first 5 Schumann modes: {real_err:.5f}\n")

    # Generate random spectra of identical size and frequency range.
    # Two null models:
    #   A) uniform random in linear Hz from real_min to real_max
    #   B) uniform random in log Hz (preserves "density per octave")
    null_lin = []
    null_log = []
    log_lo, log_hi = math.log(real_min), math.log(real_max)
    for _ in range(n_trials):
        fake_lin = rng.uniform(real_min, real_max, size=n_real)
        fake_log = np.exp(rng.uniform(log_lo, log_hi, size=n_real))
        # Compute alignment error for each fake spectrum.
        for fakes, store in [(fake_lin, null_lin), (fake_log, null_log)]:
            log_v = np.log(fakes)
            sq = 0.0
            for mode in schumann_5:
                lm = math.log(mode)
                d = float(np.min(np.abs(log_v - lm)))
                sq += d * d
            store.append(math.sqrt(sq / 5))

    null_lin = np.array(null_lin)
    null_log = np.array(null_log)
    rank_lin = int(np.sum(null_lin < real_err))
    rank_log = int(np.sum(null_log < real_err))

    print(f"Null A (uniform linear Hz, n={n_trials}):")
    print(f"  mean  = {null_lin.mean():.5f}, median = {np.median(null_lin):.5f}")
    print(f"  min   = {null_lin.min():.5f},  max    = {null_lin.max():.5f}")
    print(f"  Real ranks at percentile {rank_lin/n_trials*100:.2f}%")

    print(f"\nNull B (uniform log Hz, n={n_trials}):")
    print(f"  mean  = {null_log.mean():.5f}, median = {np.median(null_log):.5f}")
    print(f"  min   = {null_log.min():.5f},  max    = {null_log.max():.5f}")
    print(f"  Real ranks at percentile {rank_log/n_trials*100:.2f}%")

    print(f"\nINTERPRETATION:")
    print(f"  If real percentile << 5%: the orbital geometry beats random")
    print(f"  spectra of identical density. Geometry matters, not density.")
    print(f"  If real percentile ~ 50%: the alignment is density-driven.")
    return {"real_err": real_err,
            "null_lin_pct": rank_lin/n_trials*100,
            "null_log_pct": rank_log/n_trials*100}


# ---------------------------------------------------------------------------
# TEST 4: Robustness to orbital period uncertainty.
# ---------------------------------------------------------------------------
def test_robustness(c_best, n_trials=500, seed=42):
    print("\n" + "=" * 78)
    print("TEST 4: ROBUSTNESS TO ORBITAL-PERIOD UNCERTAINTY")
    print("=" * 78)
    print("Perturb each orbital period within its measurement uncertainty.")
    print("If the alignment survives perturbation, it's not a measurement")
    print("artifact. If it collapses, it's a knife-edge fluke.\n")

    rng = np.random.default_rng(seed)
    schumann_5 = [SCHUMANN_MODES_HZ[i] for i in range(1, 6)]
    baseline_err, _ = alignment_error(c_best, schumann_5)
    print(f"Baseline error (no perturbation): {baseline_err:.5f}\n")

    perturbed_errs = []
    for _ in range(n_trials):
        perturbed_periods = {}
        for name, p in ORBITS_DAYS.items():
            sigma = ORBIT_UNCERTAINTY_DAYS[name]
            perturbed_periods[name] = p + rng.normal(0, sigma)
        e, _ = alignment_error(c_best, schumann_5, periods=perturbed_periods)
        perturbed_errs.append(e)

    perturbed_errs = np.array(perturbed_errs)
    print(f"Perturbed errors over {n_trials} trials:")
    print(f"  mean   = {perturbed_errs.mean():.5f}")
    print(f"  median = {np.median(perturbed_errs):.5f}")
    print(f"  std    = {perturbed_errs.std():.5f}")
    print(f"  min    = {perturbed_errs.min():.5f}")
    print(f"  max    = {perturbed_errs.max():.5f}")
    print(f"  Fraction of perturbations within 2x baseline: "
          f"{np.mean(perturbed_errs < 2 * baseline_err):.3f}")
    return {"baseline_err": baseline_err,
            "perturbed_mean": float(perturbed_errs.mean()),
            "perturbed_std": float(perturbed_errs.std())}


# ---------------------------------------------------------------------------
# TEST 5: Schumann mode 1 variability range.
# ---------------------------------------------------------------------------
def test_mode1_variability(c_best):
    print("\n" + "=" * 78)
    print("TEST 5: SCHUMANN MODE-1 VARIABILITY")
    print("=" * 78)
    print(f"Schumann mode 1 drifts {SCHUMANN_MODE1_RANGE[0]}-"
          f"{SCHUMANN_MODE1_RANGE[1]} Hz with ionospheric conditions.")
    print(f"At c = {c_best:.3e}, find the closest orbital voice across")
    print(f"the full Schumann variability band.\n")

    sweep_hz = np.linspace(SCHUMANN_MODE1_RANGE[0],
                           SCHUMANN_MODE1_RANGE[1], 121)
    print(f"  {'Schumann Hz':>12}  {'closest voice':>32}  {'voice Hz':>10}  {'% off':>6}")
    locks = []
    for hz in sweep_hz[::15]:  # sample every ~0.075 Hz
        offset, label, f = closest_voice(c_best, hz)
        print(f"  {hz:>12.3f}  {label:>32s}  {f:>10.4f}  {offset*100:>5.2f}%")
        locks.append((hz, offset))

    # Find within-band the Schumann frequency that BEST matches an orbital
    # voice (i.e., where in the variability band is the field closest to lock).
    fine = np.linspace(SCHUMANN_MODE1_RANGE[0],
                       SCHUMANN_MODE1_RANGE[1], 1201)
    best = (float("inf"), 0, "", 0)
    for hz in fine:
        offset, label, f = closest_voice(c_best, hz)
        if offset < best[0]:
            best = (offset, hz, label, f)
    print(f"\nWithin Schumann variability band, tightest lock is at:")
    print(f"  Schumann Hz = {best[1]:.3f}")
    print(f"  voice = {best[2]} at {best[3]:.4f} Hz ({best[0]*100:.3f}% off)")
    return {"best_hz": best[1], "best_offset": best[0]}


# ---------------------------------------------------------------------------
# TEST 6: Multi-compression harmonic structure.
# ---------------------------------------------------------------------------
def test_compression_harmonics():
    print("\n" + "=" * 78)
    print("TEST 6: HARMONIC STRUCTURE OF THE COMPRESSION DIMENSION")
    print("=" * 78)
    print("First test found minima clustering at c ~ 7.94e7, 2.1e8, 4.16e8.")
    print("Are these integer harmonics of one fundamental compression?\n")

    # Fine sweep around the previously-found minima.
    schumann_5 = [SCHUMANN_MODES_HZ[i] for i in range(1, 6)]
    log_cs = np.linspace(7.0, 11.0, 12001)
    cs = 10.0 ** log_cs
    errors = np.zeros_like(cs)
    for idx, c in enumerate(cs):
        e, _ = alignment_error(c, schumann_5)
        errors[idx] = e

    # Find all local minima below threshold.
    threshold = 0.02
    minima = []
    for i in range(1, len(errors) - 1):
        if errors[i] < errors[i - 1] and errors[i] < errors[i + 1] \
                and errors[i] < threshold:
            minima.append((errors[i], cs[i]))
    minima.sort()
    minima = minima[:20]
    print(f"Top {len(minima)} minima below RMS log-err = {threshold}:")
    print(f"  {'rank':>4}  {'compression':>14}  {'err':>8}  {'ratio to #1':>12}")
    if not minima:
        print("  (none found)")
        return None
    base_c = minima[0][1]
    for r, (e, c) in enumerate(minima, start=1):
        print(f"  {r:>4}  {c:>14.4e}  {e:>8.5f}  {c / base_c:>12.4f}")

    print(f"\nINTERPRETATION:")
    print(f"  If ratios cluster near small integers (2, 3, 4, ...) or simple")
    print(f"  rationals (3/2, 4/3, 5/4), the compression dimension itself")
    print(f"  has harmonic structure -> evidence for geometric meaning.")
    print(f"  If ratios are irrational scattered, no harmonic structure.\n")
    return [c / base_c for _, c in minima]


# ---------------------------------------------------------------------------
# TEST 7: Triple-beat dominance.
# ---------------------------------------------------------------------------
def test_triple_dominance(c_best):
    print("\n" + "=" * 78)
    print("TEST 7: TRIPLE-BEAT DOMINANCE")
    print("=" * 78)
    print("First test found 4 of 5 modes locked to triple beats. Test what")
    print("happens when triples are excluded.\n")

    schumann_5 = [SCHUMANN_MODES_HZ[i] for i in range(1, 6)]
    err_with, _ = alignment_error(c_best, schumann_5, include_triples=True)
    err_without, _ = alignment_error(c_best, schumann_5, include_triples=False)
    print(f"At c = {c_best:.3e}:")
    print(f"  RMS log-err WITH triples (133 voices):    {err_with:.5f}")
    print(f"  RMS log-err WITHOUT triples (28 voices):  {err_without:.5f}")
    print(f"  Ratio (without/with):                     {err_without/err_with:.2f}x worse")

    # Also re-find best compression WITHOUT triples.
    c_no_trip, err_no_trip, _, _ = find_best_compression(
        schumann_5, include_triples=False)
    print(f"\nBest compression using ONLY fundamentals + pairwise beats:")
    print(f"  c = {c_no_trip:.4e}, RMS log-err = {err_no_trip:.5f}")
    print(f"  vs. with-triples best:")
    print(f"  c = {c_best:.4e}, RMS log-err = (use first-5 best)\n")

    print("Without triples, show closest voice for each Schumann mode:")
    print(f"  {'mode':>4}  {'Hz':>7}  {'closest voice':>32}  {'voice Hz':>10}  {'% off':>6}")
    for n in range(1, 6):
        target = SCHUMANN_MODES_HZ[n]
        offset, label, f = closest_voice(c_no_trip, target,
                                         include_triples=False)
        print(f"  {n:>4}  {target:>7.2f}  {label:>32s}  {f:>10.4f}  {offset*100:>5.2f}%")

    return {"err_with": err_with, "err_without": err_without,
            "best_c_no_triples": c_no_trip, "err_no_triples": err_no_trip}


# ---------------------------------------------------------------------------
# Main.
# ---------------------------------------------------------------------------
def main():
    print("=" * 78)
    print("SCHUMANN-ORBITAL UNRAVELING")
    print("=" * 78)

    # Re-derive the best compression (so script is self-contained).
    schumann_5 = [SCHUMANN_MODES_HZ[i] for i in range(1, 6)]
    c_best, err_best, _, _ = find_best_compression(
        schumann_5, n_steps=12001)
    print(f"\nBaseline: best compression for first 5 Schumann modes:")
    print(f"  c = {c_best:.6e}")
    print(f"  RMS log-error = {err_best:.5f}")

    results = {}
    results["test1"] = test_higher_modes()
    results["test2"] = test_compression_meaning(c_best)
    results["test3"] = test_voice_density_control(c_best)
    results["test4"] = test_robustness(c_best)
    results["test5"] = test_mode1_variability(c_best)
    results["test6"] = test_compression_harmonics()
    results["test7"] = test_triple_dominance(c_best)

    print("\n" + "=" * 78)
    print("SUMMARY OF UNRAVELING")
    print("=" * 78)
    print("""
The thread:
  - Test 1: do higher Schumann modes lock at the same c?
  - Test 2: does c have a physical meaning (a real-world ratio)?
  - Test 3: does the orbital geometry beat random spectra of equal density?
  - Test 4: does the alignment survive realistic period uncertainty?
  - Test 5: where in the Schumann variability band is the lock tightest?
  - Test 6: do the multiple compression minima form harmonic structure?
  - Test 7: how essential are the triple beats vs. pairs and fundamentals?

If most tests pass, structural phase-lock between the orbital field and
the Earth-cavity field is on the table seriously. If most fail, the
original p~0.006 finding is more likely a fluke from voice density and
mode count.
""")


if __name__ == "__main__":
    main()
