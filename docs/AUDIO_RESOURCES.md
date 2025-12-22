# Audio Resources for Project H.A.L.O

This document provides curated audio resources for use with H.A.L.O. protocols.

## Protocol A: Bilateral Stimulation (EMDR)

### YouTube Resources (Free)

**EMDR Bilateral Audio Tracks:**

- [EMDR Bilateral Audio - 1 Hour](https://www.youtube.com/results?search_query=emdr+bilateral+audio+1+hour) - Search for various options
- [Bilateral Music for EMDR](https://www.youtube.com/results?search_query=bilateral+music+emdr)
- [Nature Sounds Bilateral](https://www.youtube.com/results?search_query=bilateral+rain+sounds+emdr)

**Key Features to Look For:**

- Clear L/R channel separation
- 1-2 Hz alternation rate (60-120 beats per minute)
- Duration: 30-60 minutes
- No sudden loud sounds (startle can interrupt processing)

### Spotify Playlists

Search for:

- "EMDR Therapy Music"
- "Bilateral Stimulation"
- "EMDR Meditation"

### Apps (Paid)

**EMDR Kit** (iOS/Android)

- Professional EMDR app
- Customizable bilateral sounds
- Haptic feedback option
- ~$5

**BLS (Bilateral Stimulation)** (iOS)

- Simple, focused on bilateral audio
- Multiple sound options (tones, music, nature)
- ~$3

**Bilateral Sounds** (Android)

- Free with ads, or premium ($2)
- Variety of soundscapes

## Protocol B: Binaural Beats / Isochronic Tones

### Brainwave Entrainment Theory

**Frequency Ranges:**

- **Theta (4-8 Hz)**: Deep meditation, insight, mystical states
- **Alpha (8-12 Hz)**: Relaxed awareness, creativity, flow
- **Delta (0.5-4 Hz)**: Deep sleep, unconscious processing

**Recommended Starting Points:**

- Beginners: 10 Hz Alpha
- Intermediate: 6 Hz Theta
- Advanced: 4 Hz Deep Theta

### YouTube Resources for Binaural Beats (Free)

**Theta Binaural Beats:**

- [6 Hz Theta Binaural Beats - 1 Hour](https://www.youtube.com/results?search_query=6hz+theta+binaural+beats)
- [Theta Waves for Deep Meditation](https://www.youtube.com/results?search_query=theta+waves+deep+meditation)

**Alpha Binaural Beats:**

- [10 Hz Alpha Waves](https://www.youtube.com/results?search_query=10hz+alpha+waves)
- [Alpha Brainwave Entrainment](https://www.youtube.com/results?search_query=alpha+brainwave+entrainment)

**IMPORTANT**:

- Must use **headphones/earbuds** (binaural beats require L/R frequency difference)
- Test with headphones on - you should NOT hear a beat in one ear, but a "wobbling" sensation in your head

### Apps & Services (Paid)

**Brain.fm** (Subscription: ~$7/month)

- AI-generated functional music
- Science-backed entrainment
- Modes: Focus, Meditation, Sleep
- Recommended for serious practitioners

**Insight Timer** (Free/Premium)

- Large library of guided meditations
- Many with binaural beats
- Free tier sufficient for most users

**Hemi-Sync / Monroe Institute** (Paid courses)

- Gold standard for binaural entrainment
- Gateway Experience (~$200) is comprehensive
- Designed specifically for consciousness exploration

**EquiSync** (One-time purchase: ~$100)

- Progressive entrainment program
- Multiple levels (beginner → advanced)
- Lifetime access

### Specific Recommendations by Goal

**For Trauma Processing (Protocol A):**

- Bilateral EMDR audio (not binaural beats)
- Nature sounds with L/R panning
- Avoid music with lyrics (taxes working memory too much)

**For Mystical States (Protocol B):**

- 6 Hz Theta binaural beats
- 4 Hz Deep Theta (advanced only)
- Monroe Institute Gateway Experience

**For Creative Insight:**

- 10 Hz Alpha binaural beats
- Brain.fm "Deep Work" mode
- Alpha isochronic tones

**For Lucid Dreaming Practice:**

- 6-8 Hz Theta range
- 40 Hz Gamma bursts (brief, for awareness boost)
- Use during hypnagogic state (falling asleep)

## DIY Audio Creation

### Using Audacity (Free)

1. **Generate Bilateral EMDR Audio:**
   - Generate → Tone → 440 Hz, 0.5 sec
   - Split to Stereo
   - Effect → Pan → Left -100%
   - Duplicate track, Pan → Right +100%
   - Offset second track by 0.5 sec
   - Repeat/loop to desired length

2. **Generate Binaural Beats:**
   - Generate → Tone → 200 Hz (Left), 206 Hz (Right) for 6 Hz beat
   - Must be stereo track
   - Export as WAV or high-quality MP3

### Python Script (for nerds)

```python
import numpy as np
from scipy.io import wavfile

# Binaural beat generator
def generate_binaural(freq_left, freq_right, duration_sec=600, sample_rate=44100):
    t = np.linspace(0, duration_sec, int(sample_rate * duration_sec))
    left = np.sin(2 * np.pi * freq_left * t)
    right = np.sin(2 * np.pi * freq_right * t)
    stereo = np.column_stack([left, right])
    wavfile.write('binaural_6hz.wav', sample_rate, (stereo * 0.3).astype(np.float32))

# 6 Hz Theta: 200 Hz L, 206 Hz R
generate_binaural(200, 206, duration_sec=600)
```

## Audio Settings & Best Practices

### Volume Levels

**Protocol A (EMDR):**

- Moderate volume - should be clear but not dominating
- You should hear bilateral movement distinctly
- Too loud: Can't think about trauma
- Too quiet: Can't track stimulus

**Protocol B (Binaural):**

- Low to moderate volume
- Should be barely audible in quiet room
- Too loud: Distracting, headache-inducing
- Too quiet: No entrainment effect

### Audio Quality

- **Minimum**: 128 kbps MP3 (low frequencies preserved)
- **Recommended**: 256 kbps MP3 or FLAC
- **Avoid**: Heavily compressed YouTube rips, very low bitrate files

### Equipment

**Acceptable:**

- Any stereo earbuds/headphones
- Apple EarPods (wired)
- Basic Bluetooth earbuds

**Recommended:**

- Over-ear headphones (better bass for low frequencies)
- Google Pixel Buds Pro (noise cancellation for immersion)
- Bose QuietComfort (industry standard for meditation)

**Avoid:**

- Mono audio devices (single earbud)
- Laptop/phone speakers (binaural beats won't work)
- Very cheap earbuds (frequency response too limited)

## Safety Notes

### Potential Side Effects

**Binaural Beats:**

- Headache (if too loud or too long)
- Dizziness (especially Delta/low Theta)
- Irritability (wrong frequency for your state)
- Sleep disruption (if used before bed inappropriately)

**Bilateral EMDR:**

- Emotional intensity (expected, not a bug)
- Fatigue (processing is work)
- Temporary increase in symptoms (re-consolidation process)

### Contraindications

**Do not use binaural beats/isochronic tones if:**

- History of seizures/epilepsy (flashing lights + rhythmic audio can trigger)
- Currently using psychoactive medications (check with prescriber)
- Under age 18 (brain still developing)
- Pregnant (unknown effects on fetal development)

**Reduce volume or stop if:**

- Headache develops
- Feel nauseous or dizzy
- Hearing any distortion or painful sounds
- Feeling "spaced out" hours after session

## Community Resources

### Reddit

- r/BinauralBeats - User experiences and recommendations
- r/EMDR - Clinical EMDR community
- r/Meditation - General meditation discussions

### Forums

- Monroe Institute Forums - Gateway Experience discussions
- Brain.fm Community - User tips and science

### Discord/Telegram

- (Create Project H.A.L.O. Discord server for community)

## Testing Your Audio

### Stereo Test

1. Play a known stereo test track (YouTube "left right audio test")
2. Verify you hear "left" only in left ear, "right" only in right ear
3. If not: Check L/R on earbuds, check system audio balance

### Binaural Beat Verification

1. Play a 6 Hz theta binaural track
2. Close eyes, focus on the sound
3. You should perceive a "wobbling" or "pulsing" (6 times per second)
4. This is the beat frequency (206 Hz - 200 Hz = 6 Hz)
5. If you hear two steady tones: Not working, check stereo setup

---

## Quick Reference

| Protocol | Audio Type | Frequency | Duration | Volume |
| ---------- | ----------- | ----------- | ---------- | --------- |
| A - Hunter | EMDR Bilateral | 1-2 Hz LR | 20-30 min | Medium |
| B - Lucid Diver (Alpha) | Binaural | 10 Hz | 30-60 min | Low-Med |
| B - Lucid Diver (Theta) | Binaural | 6 Hz | 30-60 min | Low |
| B - Advanced (Deep Theta) | Binaural | 4 Hz | 20-40 min | Low |

---

> *"Sound is vibration. Vibration is frequency. Frequency is consciousness. Choose your soundtrack wisely."*
