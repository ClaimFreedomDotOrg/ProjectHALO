# Quick Start Guide - Project H.A.L.O

**Time required**: 30 minutes for first setup, 5 minutes for subsequent sessions

## Prerequisites Checklist

Before starting, ensure you have:

- [ ] Muse S (Gen 2 or Athena) headband - **charged**
- [ ] TENS 7000 unit with fresh batteries
- [ ] Ear clip electrodes or sticky pads
- [ ] Earbuds or headphones (stereo)
- [ ] Computer with Bluetooth
- [ ] Python 3.8 or higher installed

## 5-Minute Software Setup

### 1. Install Dependencies

```bash
# Install OpenMuse
pip install https://github.com/DominiqueMakowski/OpenMuse/zipball/main

# Clone Project H.A.L.O.
git clone https://github.com/ClaimFreedomDotOrg/ProjectHALO.git
cd ProjectHALO

# Install package
pip install -e .
```

### 2. Find Your Muse Device

```bash
# Power on Muse headband (hold button until blue LED appears)
OpenMuse find
```

**Copy your MAC address** - looks like: `00:55:DA:B9:FA:20`

### 3. Test Connection

```bash
halo-monitor --address YOUR_MAC_ADDRESS --duration 30
```

If you see EEG data streaming, you're ready!

## 10-Minute Hardware Setup

### 1. Muse S Placement

- AF7/AF8 sensors on forehead (above eyebrows)
- TP9/TP10 sensors behind ears (on bone)
- Adjust until snug but comfortable

### 2. TENS Electrode Placement

- **Anode (Red +)**: Clip to LEFT ear tragus (cartilage flap)
- **Cathode (Black -)**: Stick pad on LEFT shoulder
- **Critical**: Do NOT place near heart or on neck front

### 3. TENS Settings

- Mode: **Normal** (not burst/modulate)
- Pulse Width: **200 µs**
- Frequency: **25 Hz**
- Intensity: **Start at 0** (will adjust during session)

### 4. Audio Preparation

Download ONE of these:

- **For trauma work**: YouTube "EMDR bilateral audio" (save/bookmark)
- **For exploration**: YouTube "theta binaural beats 6hz"

## Your First 20-Minute Session (Protocol A)

### Step 1: Start Monitor (1 min)

```bash
halo-monitor --address YOUR_MAC_ADDRESS
```

Wait for "OBSERVER" state to appear.

### Step 2: Baseline (3 min)

- Put on all equipment
- Close eyes
- Breathe deeply (4-7-8 pattern)
- Start bilateral audio (low volume)
- Watch monitor show "OBSERVER" state

### Step 3: Target Memory (2 min)

- Think of a mildly uncomfortable memory (not your worst trauma for first session!)
- Rate discomfort 0-10 (start with 4-6 intensity)
- Notice where you feel it in your body

### Step 4: Engage (10 min)

- Hold the memory in mind
- Allow emotion to rise
- When terminal shows **"SHADOW DETECTED"**:
  - Slowly turn TENS dial up until you feel gentle tingle
  - Focus on the left/right audio movement
  - Stay with the feeling without suppressing
- Continue until emotion naturally decreases

### Step 5: Integration (5 min)

- Turn TENS back to 0
- Stop bilateral audio
- Sit in silence, breathe deeply
- Open eyes when ready

### Step 6: Journal (5 min)

Write immediately:

- What did you notice?
- Did the intensity change?
- Any insights or images?

## Troubleshooting

**"Connection failed" error**
→ Ensure Muse is powered on, Bluetooth enabled, no other apps using device

**No "SHADOW DETECTED" trigger**
→ Normal if memory not emotionally charged. Try different target or wait naturally.

**TENS causes pain or muscle twitching**
→ IMMEDIATELY turn down. Should be a tingle, not painful. Reposition if needed.

**Feeling overwhelmed**
→ Stop session, turn off TENS, open eyes. Use 5-4-3-2-1 grounding technique.

**Monitor shows errors**
→ Check Python version (`python --version` should be 3.8+), reinstall OpenMuse

## What's Normal

### During Session

- Crying, anger, or laughter (emotional release)
- Yawning or shaking (nervous system discharge)
- New perspectives on old memories
- Feeling "lighter" or relieved
- Tiredness afterward

### After Session

- Thirst (drink water!)
- Need to sleep (integration)
- Continued emotional processing for 24-48 hours
- Dreams related to target memory
- Spontaneous insights days later

## Safety Reminders

**STOP and seek help if:**

- Chest pain or irregular heartbeat
- Severe panic that doesn't resolve
- Dissociation lasting hours after session
- Suicidal thoughts (Call 988 in US)

**Best practices:**

- Start with 1-2 sessions per week
- Process lighter memories first
- Have support person available for first session
- Don't use if sleep-deprived or intoxicated

## Next Steps

Once comfortable with basic Protocol A:

- Read [PROTOCOLS.md](PROTOCOLS.md) for advanced techniques
- Explore Protocol B (Lucid Diver) for mystical states
- Join discussions on GitHub to share experiences
- Consider working with EMDR therapist for deeper trauma

## Quick Reference - Session Commands

```bash
# Standard session (infinite duration)
halo-monitor --address XX:XX:XX:XX:XX:XX

# Timed session (300 seconds = 5 minutes)
halo-monitor --address XX:XX:XX:XX:XX:XX --duration 300

# Custom trigger threshold
halo-monitor --address XX:XX:XX:XX:XX:XX --threshold 0.8

# Help
halo-monitor --help
```

## Getting Help

- **Documentation**: README.md, SETUP.md, PROTOCOLS.md
- **Issues**: GitHub Issues for bugs
- **Discussions**: GitHub Discussions for questions
- **Crisis**: 988 (US) or your local emergency services

---

**You're ready to begin. Welcome to Project H.A.L.O.**

> *"The door is open. You've always had the key."*
