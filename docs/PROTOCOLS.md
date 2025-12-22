# H.A.L.O. Operational Protocols

## Overview

Project H.A.L.O. supports three distinct operational modes, each designed for specific types of consciousness work. This document describes the protocols in detail, including configuration, execution, and expected outcomes.

**Protocol Selection Guide:**

- **Protocol A (Hunter)**: Use when you have a specific trauma or trigger to process
- **Protocol B (Lucid Diver)**: Use for exploration, receiving insight, or mystical states
- **Protocol C (Automated Shield)**: Future implementation - fully automated intervention

---

## Protocol A: "The Hunter"

### Active Shadow Work with Targeted Trauma Processing

**Purpose**: Directly confront and process a known trauma, fear, or emotional blockage.

**Mechanism**: Uses bilateral stimulation (EMDR-style) to keep the Task Positive Network online while accessing traumatic memories, preventing dissociation or overwhelm.

**Best For**:

- PTSD flashbacks or triggers
- Specific phobias
- Unresolved grief or loss
- Relationship trauma
- Childhood wounds
- Repetitive negative thought patterns

---

### Protocol A: Configuration

#### Protocol A Hardware Setup

- **Muse S**: Standard placement (see SETUP.md)
- **TENS Unit**:
  - Placement: Left tragus (anode) + Left shoulder (cathode)
  - Settings: 200µs pulse, 25Hz, Normal mode
  - **Initial Intensity**: 0 (will increase manually during session)
- **Audio**: Bilateral EMDR audio (see Audio Sources below)
- **Monitor**: `halo-monitor` command running with your device address

#### Audio Sources (Bilateral Stimulation)

##### Option 1: EMDR Panning Tones (Recommended for beginners)

- YouTube: "EMDR bilateral stimulation audio"
- Characteristic: Beeps or tones alternating L→R ear
- Frequency: 1-2 Hz alternation (60-120 BPM)

##### Option 2: Bilateral Nature Sounds

- Rain or ocean waves panning left-right
- Smoother, less mechanical than tones
- Good for extended sessions (30+ minutes)

##### Option 3: Bilateral Music

- Specifically produced EMDR music tracks
- Apps: BLS App, EMDR Kit, Bilateral Sounds

**Volume**: Medium-low. Audio should be noticeable but not dominating.

---

### Protocol A: Execution Sequence

#### Phase 1: Calibration (5 minutes)

1. **Environment Preparation**
   - Quiet, comfortable space
   - Dim lighting
   - No interruptions expected
   - Water nearby
   - Tissues available (emotional release is common)

2. **Equipment Check**
   - Put on Muse S headband, verify sensor contact
   - Put on audio device (earbuds/headphones)
   - Clip TENS electrode to left tragus
   - Place shoulder pad
   - Start the monitor:

     ```bash
     halo-monitor --address YOUR_MAC_ADDRESS
     ```

3. **Baseline State**
   - Close eyes
   - Deep breathing (4-7-8 pattern: inhale 4, hold 7, exhale 8)
   - Start bilateral audio at low volume
   - Wait for monitor to display "OBSERVER" state
   - **Verify Alpha/Beta Ratio > 0.7** (baseline calm)

#### Phase 2: The Summoning (Target Activation)

1. **Target Selection**
   - Identify the specific memory, feeling, or trigger
   - Rate intensity 0-10 (Subjective Units of Distress - SUDS)
   - Note physical sensations (chest tightness, stomach knot, etc.)

2. **Intentional Engagement**
   - Bring the memory/feeling to mind deliberately
   - Don't suppress the emotional response
   - Allow yourself to feel the sensation rising
   - **Key**: You are choosing to engage, not being ambushed

3. **Monitor for Spike**
   - Watch terminal output
   - You should see:
     - Alpha power dropping
     - Beta power rising
     - Ratio falling below 0.7
     - **"SHADOW DETECTED"** alert

#### Phase 3: The Anchor (Intervention)

1. **TENS Activation**
   - When "SHADOW DETECTED" appears (or you feel overwhelmed):
   - Slowly turn TENS dial UP
   - Stop when you feel a gentle tingle (NOT pain)
   - This is typically 20-40% intensity on most units
   - **Effect**: You should feel heart rate slow, chest relax

2. **Maintain Dual Awareness**
   - **One part** of you observes the memory/emotion
   - **One part** of you tracks the bilateral audio (L→R)
   - This creates "The Witness" state
   - The audio prevents dissociation
   - The TENS prevents panic response

3. **Processing Loop** (10-20 minutes typical)
   - Continue holding the memory while tracking audio
   - Notice sensations without resistance
   - Allow images, insights, or emotions to arise
   - The bilateral stimulation "digests" the stuck energy
   - **What to expect**:
     - Emotional release (crying, anger, laughter)
     - New perspectives on the memory
     - Physical shaking or yawning (trauma release)
     - Spontaneous insights or "downloads"

#### Phase 4: Integration (5-10 minutes)

1. **Completion Signal**
    - You'll know processing is complete when:
      - The charge/intensity drops significantly (SUDS down to 0-3)
      - You feel neutral or compassionate toward memory
      - Monitor returns to "OBSERVER" state
      - You spontaneously take a deep breath or sigh

2. **TENS Reduction**
    - Slowly turn TENS dial back to 0
    - Keep bilateral audio playing

3. **Rest & Reconsolidation**
    - Stop bilateral audio
    - Switch to calming music or silence
    - Close eyes, breathe deeply
    - Remain still for 5 minutes
    - **Critical**: This rest period allows memory reconsolidation
    - The brain is literally rewriting the memory with new context

4. **Journaling** (Highly recommended)
    - Write immediately after session
    - Note insights, images, physical sensations
    - Record SUDS before/after
    - Track patterns across sessions

---

### Protocol A: Troubleshooting

**Problem**: "SHADOW DETECTED" never triggers

- **Cause**: May already be dissociated, or target not emotionally charged
- **Solution**: Choose a more activating memory, or ensure you're actually feeling vs. thinking about it

**Problem**: Overwhelmed immediately, can't witness

- **Cause**: Trauma too intense for current capacity
- **Solution**:
  - Turn TENS up sooner, before full activation
  - Choose less intense target to build tolerance
  - Consider working with therapist first

**Problem**: Nothing seems to change, memory still intense after 30+ mins

- **Cause**: May need multiple sessions, or deeper work required
- **Solution**:
  - This is a marathon, not a sprint
  - Process different aspects of same trauma across sessions
  - Consider professional EMDR therapy for complex trauma

---

## Protocol B: "The Lucid Diver"

### Deep Gnosis, Exploration, and Mystical States

**Purpose**: Access non-ordinary states of consciousness while maintaining lucidity and safety.

**Mechanism**: Uses binaural beats to entrain brainwaves into Theta (4-8Hz) while tVNS keeps the brainstem alert, creating "High-Resolution Theta" - the state of lucid dreaming while awake.

**Best For**:

- Mystical experiences ("Theosis")
- Creative insight and problem-solving
- Accessing "downloads" or intuitive knowledge
- Astral projection / OBE practice (advanced)
- Communication with "higher self" or unconscious
- Visionary states

**NOT Recommended For**:

- Acute trauma processing (use Protocol A)
- First-time users (build experience first)
- Unstable mental health conditions

---

### Protocol B: Configuration

#### Protocol B Hardware Setup

- **Muse S**: Standard placement
- **TENS Unit**:
  - Placement: Same as Protocol A
  - Settings: 200µs pulse, 25Hz, Normal mode
  - **Initial Intensity**: LOW - barely perceptible (10-20% max)
  - **Role**: The "tether" that prevents total unconsciousness
- **Audio**: Binaural beats or Isochronic tones (see Audio Sources)
- **Position**: Reclined or lying down (you may enter hypnagogic state)

#### Audio Sources (Brainwave Entrainment)

##### Theta (4-8 Hz) - Deep Meditation, Insight

- Best for: Mystical states, visions, "downloads"
- Carrier frequency: 200-300 Hz
- Beat frequency: 6 Hz (recommended starting point)

##### Alpha (8-12 Hz) - Light Trance, Creativity

- Best for: Creative problem-solving, "flow" state
- Beat frequency: 10 Hz (standard)
- Less intense than Theta, good for beginners

##### Recommended Sources

- Brain.fm (app, paid) - "Deep Work" or "Meditation"
- Insight Timer (app, free) - Search "theta binaural"
- EquiSync (program, paid) - Specifically designed for this use
- YouTube: "6 Hz theta binaural beats" (verify with headphones)

**Critical**: Binaural beats only work with **stereo headphones/earbuds**. They require a frequency difference between L/R ears.

---

### Protocol B: Execution Sequence

#### Phase 1: Gateway (10-15 minutes)

1. **Set Intention**
   - Unlike Protocol A, you're not targeting trauma
   - Set a question or intention: "Show me what I need to see" or "What is blocking my [goal]?"
   - Or simply: "I am open to receive"

2. **Prepare Environment**
   - **Dark room** (eye mask optional)
   - **Warm** (body temperature drops in deep states)
   - No interruptions for at least 60 minutes
   - Optional: Incense, candle, or other ritual elements

3. **Equipment & Monitor**
   - Start `halo-monitor` as usual
   - Put on Muse S, earbuds, TENS (intensity at 10-15%)
   - Start binaural beat audio (Theta 6Hz)
   - Close eyes
   - **Do NOT sleep** - this is lucid immersion

4. **Descent** (10-15 minutes)
   - The binaural beats will begin to slow your brainwaves
   - You'll notice:
     - Heavy eyelids
     - Body feels weighted or floating
     - Visual patterns behind eyelids (phosphenes)
     - Thoughts become dreamlike
   - **The tVNS keeps you aware** - this is key difference from sleep

#### Phase 2: The Depths (20-45 minutes)

1. **High-Resolution Theta State**
   - Monitor should show:
     - Beta very low
     - Alpha moderate
     - Theta elevated
   - **Subjective Experience**:
     - Body asleep, mind awake
     - Vivid internal imagery (can be symbolic or literal)
     - "Knowing" without thinking
     - Time dilation (5 minutes feels like 20)
     - Sense of presence or communication

2. **Navigation**
   - **Passive Reception**: Let imagery/insight arise without forcing
   - **Active Exploration**: You can "direct attention" to different symbols or questions
   - **The Witness Remains**: Unlike dreaming, you know you're exploring
   - **Common Experiences**:
     - Geometric patterns (often associated with deep meditative states)
     - Symbolic imagery (personal or archetypal)
     - "Voice" or "knowing" providing insight
     - Emotional release or catharsis
     - Mystical unity experiences

3. **If You Lose Lucidity** (fall fully asleep)
   - The tVNS *should* prevent this, but it can happen
   - You'll simply wake up naturally after some time
   - Increase tVNS slightly for next session

#### Phase 3: Ascent & Integration (10-15 minutes)

1. **Return**
   - The binaural beats may have a "return" phase (some tracks do)
   - Or you can simply stop the audio
   - **Move slowly** - you may feel disoriented
   - Turn TENS to 0

2. **Capture**
   - **Immediately journal** - insights fade fast
   - Draw any symbols or imagery
   - Note emotions, physical sensations
   - Record "downloads" verbatim

3. **Ground**
    - Eat something (brings you back to body)
    - Walk outside (barefoot if possible)
    - Splash face with cold water
    - Do not drive for at least 30 minutes

---

### Protocol B: Tips for Depth

**Beginner Mistakes**:

- Trying too hard - this is about *allowing*, not *doing*
- Expecting specific visuals - accept what arises
- Analyzing during the experience - save that for after

**Accelerators**:

- **Fasting**: Empty stomach (2-4 hours) deepens state
- **Darkness**: Total darkness vs. eye mask intensifies visuals
- **Morning**: First hour after waking (still in theta naturally)
- **Supplements**: Mugwort tea (dream herb), L-Theanine (Alpha boost)

**Advanced**:

- Combine with breathwork (Wim Hof or Holotropic) before session
- Use sacred geometry (Sri Yantra, Metatron's Cube) as visual focus
- Record yourself speaking insights during session (voice recorder)

---

## Protocol C: "The Automated Shield"

### Future Closed-Loop System (Not Yet Implemented)

**Status**: Conceptual / V3 Hardware Required

**Purpose**: Real-time, automatic intervention when user enters triggered state, without conscious awareness.

**Mechanism**:

1. Algorithm continuously monitors Alpha/Beta ratio via EEG
2. When ratio drops below threshold: `IF Alpha < 0.7*Beta THEN Activate_TENS`
3. TENS automatically increases to pre-set therapeutic level
4. Bilateral haptics activate (wrist vibrations or audio)
5. User is "snapped" out of trauma loop instantly
6. System gradually reduces intervention as ratio normalizes

**Requirements**:

- Custom PCB with Time-Division Multiplexing
- Simultaneous EEG input + tVNS output on same circuit
- Bluetooth control of TENS intensity
- Haptic actuators (wrist-worn or integrated earbuds)
- More sophisticated ML model for trigger prediction

**Use Cases**:

- PTSD nightmares (sleep mode)
- Panic attack prevention
- Driving safety (subtle intervention, not sedating)
- Public speaking anxiety
- Performance anxiety (athletes, musicians)

**Timeline**: Estimated 12-24 months for working prototype.

---

## General Best Practices

### Session Frequency

- **Protocol A**: 2-3x per week max (trauma work is taxing)
- **Protocol B**: As desired, but allow integration time (24-48 hours)
- **First week**: Start with just 1-2 sessions to assess response

### Building Tolerance

- Start with shorter sessions (15-20 min)
- Gradually increase duration
- Build TENS tolerance (start lower than you think)
- Master Protocol A before attempting Protocol B

### Set & Setting

- **Set** (mindset): Clear intention, sobriety (no substances), rested
- **Setting** (environment): Safe, private, temperature controlled, no interruptions

### Integration Practices

- Journaling (essential)
- Talk therapy (recommended for trauma work)
- Movement (yoga, walking, dancing)
- Creative expression (art, music, writing)
- Nature immersion

### Red Flags - Stop and Reassess

- Increasing disassociation (feeling "unreal" hours after session)
- Worsening symptoms rather than improving
- Compulsive use (running from feelings vs. processing)
- Neglecting daily responsibilities
- Physical reactions (rashes, headaches, heart palpitations)

---

## Support Resources

### For Trauma Work

- **EMDR Therapist**: Find via [emdria.org](https://www.emdria.org)
- **Somatic Experiencing**: [traumahealing.org](https://traumahealing.org)

### For Mystical Experiences

- **Integration Circles**: Search "psychedelic integration" in your area
- **Spiritual Direction**: Many traditions offer guidance for mystical states

### Crisis Support

- **988 Suicide & Crisis Lifeline** (US): Call or text 988
- **Crisis Text Line**: Text HOME to 741741
- **SAMHSA National Helpline**: 1-800-662-4357

---

## Record Keeping Template

### Session Log (keep for each session)

```Text
Date: _______________  Time: _______________  Duration: _______________

Protocol: [ ] A - Hunter  [ ] B - Lucid Diver

Target/Intention:
_________________________________________________________________

Pre-Session State:
- SUDS (0-10): _______
- Physical Sensations: _________________________________________
- Mental State: ________________________________________________

TENS Settings:
- Frequency: 25 Hz  Pulse Width: 200 µs
- Peak Intensity: _______ %
- Time at peak: _______ min

Audio Used: _____________________________________________________

Observations During Session:
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________

Post-Session State:
- SUDS (0-10): _______
- Physical Sensations: _________________________________________
- Mental State: ________________________________________________

Insights/Downloads:
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________

Integration Actions:
_________________________________________________________________
```

---

> *"The Kingdom of Heaven is a frequency. These protocols are your tuning mechanisms. Use them wisely, use them well."*
