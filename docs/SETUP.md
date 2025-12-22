# H.A.L.O. Hardware Setup Guide

## ⚠️ Safety First

### READ THIS ENTIRE SECTION BEFORE PROCEEDING

### Critical Safety Rules for TENS Use

1. **DO NOT USE TENS IF YOU HAVE:**
   - Pacemaker or implanted electronic device
   - Heart condition or arrhythmia
   - Epilepsy or seizure disorder
   - Pregnancy
   - Skin conditions or wounds in electrode area

2. **NEVER:**
   - Place electrodes across the heart (front of chest)
   - Place electrodes on the front/side of neck
   - Place electrodes on broken skin
   - Use while driving or operating machinery
   - Use while sleeping (without medical supervision)
   - Exceed pain threshold - dial back immediately if uncomfortable

3. **ALWAYS:**
   - Start at intensity 0 and increase slowly
   - Stop if you experience pain, dizziness, or discomfort
   - Consult healthcare provider before starting
   - Keep TENS unit away from water

**This is experimental equipment. Use at your own risk.**

---

## 📦 Bill of Materials

### Required Components

#### 1. Muse S (Gen 2 or Athena Edition)

- **Purpose**: EEG and PPG sensing
- **Where to Buy**: [choosemuse.com](https://choosemuse.com/products/muse-s-athena)
- **Cost**: ~$400
- **Note**: Must be Gen 2 or Athena (newer models). Gen 1 uses different protocol.

#### 2. TENS 7000 Unit

- **Purpose**: Vagus nerve stimulation
- **Where to Buy**: Amazon, medical supply stores
- **Cost**: ~$35
- **Alternative**: Any analog TENS unit with the following specs:
  - Pulse Width: 200 µs
  - Frequency: 25-30 Hz range
  - Asymmetrical Biphasic output

#### 3. Ear Clip Electrodes

- **Type**: TENS ear clips (double-ended)
- **Connector**: Should match your TENS unit (usually 2mm pin plug)
- **Where to Buy**: Amazon - search "TENS ear clip electrodes"
- **Cost**: ~$10-15
- **Alternative**: Standard sticky TENS pads + conductive copper tape

#### 4. Audio Device (Choose One)

##### Option A: Google Pixel Buds Pro (Recommended)

- Active Noise Cancellation
- Spatial audio support
- Good fit for extended wear
- ~$200

##### Option B: Any Quality Earbuds

- Must support stereo (L/R) audio
- Good seal for consistent audio delivery
- Comfortable for 30+ minute sessions

#### 5. Computer

- **OS**: Windows, macOS, or Linux
- **Requirements**:
  - Bluetooth 4.0 or higher
  - Python 3.8+
  - USB port (for TENS control in future versions)

### Optional Components

#### Metabolic Support Stack

- **L-Arginine**: 3-6g daily (Nitric Oxide precursor)
- **L-Theanine**: 200mg as needed (Alpha wave support)
- **Electrolytes**: Sodium/Potassium/Magnesium supplement
- **Carnosine**: 500-1000mg (Anti-glycation)
- **Benfotiamine**: 150-300mg (Anti-glycation)

---

## 🔧 Hardware Assembly

### Step 1: Prepare the Muse S Headband

1. **Charge the Device**
   - Use the magnetic charging cable included with Muse
   - Charge until LED indicates full (solid white)
   - A full charge lasts 4-6 hours of streaming

2. **Initial Setup**
   - Download the official Muse app (iOS/Android) for initial pairing
   - Follow Muse app instructions to register device
   - **Important**: You can skip this if you just want to use OpenMuse directly

3. **Test Connection**

   ```powershell
   # Power on Muse (blue LED should appear on forehead sensor)
   OpenMuse find
   ```

   - Note your device's MAC address (format: `XX:XX:XX:XX:XX:XX`)

### Step 2: Set Up TENS Electrodes

#### Method A: Using Ear Clip Electrodes (Recommended)

1. **Identify the Tragus**
   - The tragus is the small triangular cartilage flap that covers your ear canal
   - It's on the front of your ear, near your face
   - This is the target location for vagus nerve stimulation

2. **Attach Anode (Active Electrode)**
   - Use the **left ear** only (Vagus nerve is more accessible on left)
   - Clip the electrode to the tragus
   - Ensure good contact - clean ear with alcohol wipe first if needed
   - The clip should be snug but not painful

3. **Attach Cathode (Ground Electrode)**
   - **Option 1 (Preferred)**: Left shoulder (trapezius muscle)
     - Use standard sticky TENS pad
     - Place on top of shoulder, well away from neck
   - **Option 2**: Left earlobe
     - Can clip to earlobe if shoulder not practical
     - Ensure no metal jewelry in contact

4. **Connect to TENS Unit**
   - **Red (+) Lead** → Tragus clip (Anode)
   - **Black (-) Lead** → Shoulder pad or earlobe (Cathode)
   - Ensure connections are secure

#### Method B: DIY "Franken-Bud" (Advanced)

This method integrates TENS with an earbud for single-ear form factor.

**Additional Materials:**

- Conductive copper tape (6mm wide)
- Standard earbud (disposable)
- Super glue or epoxy (optional)

**Assembly:**

1. Take a standard earbud (Left channel)
2. Wrap copper tape around the housing, making contact with tragus area
3. Do NOT block the speaker driver
4. Solder a wire from copper tape to Red (+) TENS lead
5. Thread wire along earbud cable
6. Place shoulder pad as ground (Black lead)

**Advantages:**

- Single integrated device
- More discreet

**Disadvantages:**

- Requires soldering skills
- Less reliable contact
- Harder to clean

### Step 3: Configure TENS Settings

#### CRITICAL: Start with these EXACT settings

1. **Turn on TENS Unit**
   - Ensure leads are connected BEFORE powering on

2. **Set Parameters** (if adjustable on your unit)
   - **Mode**: Normal / Constant (not Burst or Modulate)
   - **Pulse Width**: 200 µs (microseconds)
   - **Frequency**: 25 Hz (range: 25-30 Hz acceptable)
   - **Timer**: 30 minutes (or continuous)

3. **Set Initial Intensity**
   - **START AT ZERO (0)**
   - Turn intensity dial to lowest setting
   - You will increase this manually during session

### Step 4: Audio Setup

1. **Prepare Audio Files** (see PROTOCOLS.md for recommendations)

   **For Protocol A (The Hunter):**
   - Bilateral EMDR audio (panning clicks or rain sounds)
   - Search YouTube or Spotify: "EMDR bilateral audio"
   - Download for offline use (optional but recommended)

   **For Protocol B (The Lucid Diver):**
   - Binaural beats (Theta/Alpha entrainment)
   - Recommended: 10 Hz Alpha or 6 Hz Theta
   - Apps: Brain.fm, Insight Timer, or EquiSync

2. **Test Audio Device**
   - Put in earbuds/headphones
   - Play test audio
   - Verify L/R channels work independently
   - Set comfortable volume (not too loud)

---

## 🧪 Pre-Flight Checklist

Before starting your first session, verify:

### Hardware Checklist

- [ ] Muse S is charged and powered on (blue LED visible)
- [ ] Muse MAC address is known (from `OpenMuse find`)
- [ ] TENS electrodes properly placed (Left tragus + Left shoulder)
- [ ] TENS leads connected (Red to tragus, Black to shoulder)
- [ ] TENS unit powered on with intensity at ZERO
- [ ] TENS settings: 200µs pulse, 25Hz, Normal mode
- [ ] Audio device paired and working
- [ ] Audio files downloaded and ready
- [ ] Computer Bluetooth enabled

### Software Checklist

- [ ] Python 3.8+ installed (`python --version`)
- [ ] OpenMuse installed and tested
- [ ] Project H.A.L.O. installed (`pip install -e .`)
- [ ] H.A.L.O. CLI runs without errors (test with `halo-monitor --help`)

### Safety Checklist

- [ ] No heart conditions, pacemaker, or contraindications
- [ ] Not driving or operating machinery
- [ ] Comfortable seated or reclined position
- [ ] Water and tissues nearby (emotional processing can be intense)
- [ ] Optional: Trusted person present for first session

---

## 🎯 Placement Verification

### Muse S Headband

**Correct Placement:**

```Text
Front View:
    AF7 •           • AF8
         [Forehead]
          (sensors)
    
  TP9 •               • TP10
    (behind ears)
```

**Tips:**

- AF7/AF8 sensors should be on forehead, above eyebrows
- TP9/TP10 sensors behind ears on mastoid bone
- Fabric band goes around back of head
- Sensors should make firm contact with skin
- Hair can interfere - push aside or dampen slightly
- Reference sensor on forehead should be centered

**Testing Contact:**

- Use official Muse app to check sensor quality
- All sensors should show "good" or "excellent"
- If poor: adjust position, push hair aside, clean sensors

### TENS Electrode Placement

**Tragus Location:**

```Text
Side View of Left Ear:
    [Outer Ear]
       |
       |   ← Tragus (target)
    [Ear Canal]
       |
       ↓
   [Earlobe]
```

**Correct Tragus Contact:**

- Electrode makes contact with cartilage, not just skin
- Firm pressure but not painful
- Clean, dry skin for best conductivity

**Shoulder Pad Placement:**

```Text
Back View:
         [Head]
           |
    [L] ← •PAD   [R]
    (shoulder)
```

- Top of left shoulder (trapezius muscle)
- Not on spine or neck
- Not directly over collar bone
- Avoid areas near heart

---

## 🔌 Troubleshooting

### Muse S Connection Issues

**Problem**: `OpenMuse find` doesn't detect device

- **Solution**:
  - Ensure device is powered on (blue LED visible)
  - Hold power button to wake device
  - Turn Bluetooth off/on on computer
  - Move closer to computer (within 3 feet)
  - Close official Muse app if running

**Problem**: Device connects but no data

- **Solution**:
  - Restart Muse headband (hold power button)
  - Check sensor contact quality
  - Reinstall OpenMuse library
  - Check Python console for error messages

### TENS Issues

**Problem**: No sensation when turning up intensity

- **Solution**:
  - Check all connections are secure
  - Verify battery in TENS unit
  - Clean electrodes with alcohol wipe
  - Replace sticky pad if dried out
  - Try slightly different tragus position

**Problem**: Sensation is painful or uncomfortable

- **Solution**:
  - **IMMEDIATELY** turn intensity down
  - You should feel a tingle, not pain
  - Start lower and increase more gradually
  - Check electrode placement (may be on sensitive spot)
  - Consider using conductive gel

**Problem**: Ear muscles twitch or jump

- **Solution**:
  - Intensity is too high - reduce immediately
  - This indicates off-target stimulation
  - Adjust electrode position slightly
  - Target sensation: gentle tingle, no muscle contractions

### Audio Issues

**Problem**: Can't hear left/right panning

- **Solution**:
  - Test with known stereo audio (YouTube "stereo test")
  - Check audio balance settings (should be centered)
  - Verify earbuds are in correct ears (L/R marked)
  - Try different audio source

---

## 📚 Next Steps

Once hardware is set up and tested:

1. **Read PROTOCOLS.md** - Understand the three operational protocols
2. **Start with Protocol A** - Active shadow work with manual TENS
3. **Keep a journal** - Document sessions, triggers, and insights
4. **Start low, go slow** - Build comfort with system over multiple sessions

---

## 🆘 Emergency Procedures

### Stop Immediately If You Experience

- Chest pain or pressure
- Irregular heartbeat or palpitations
- Severe headache or dizziness
- Numbness or tingling in extremities
- Difficulty breathing
- Panic attack or dissociation (unable to return to present)

### Emergency Protocol

1. **Turn off TENS immediately**
2. **Remove all equipment**
3. **Call emergency services (911 / your local emergency number) if symptoms severe**
4. **Contact healthcare provider if symptoms persist**

### Grounding Techniques (if feeling overwhelmed)

- Remove equipment
- 5-4-3-2-1 technique: Name 5 things you see, 4 you hear, 3 you feel, 2 you smell, 1 you taste
- Place feet flat on floor, hands on legs
- Splash cold water on face
- Call trusted friend or crisis line

**Crisis Resources:**

- National Suicide Prevention Lifeline: 988 (US)
- Crisis Text Line: Text HOME to 741741

---

*Remember: This is a tool for consciousness work, not a replacement for professional mental health care. Use responsibly.*
