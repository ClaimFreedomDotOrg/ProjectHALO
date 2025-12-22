# Project H.A.L.O. 🔆

## Hemispheric Alignment & Limbic Override

### A Neuro-Biological Regulator for Courage & The Resurrected Body

> *"The Kingdom of Heaven is a frequency. H.A.L.O. is the tuner. Your Body is the antenna."*

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Open Hardware](https://img.shields.io/badge/Hardware-Open%20for%20Manufacturing-green.svg)](OPEN_HARDWARE.md)
[![Muse S Athena](https://img.shields.io/badge/Hardware-Muse%20S%20Athena-purple.svg)](https://choosemuse.com)

> **🌍 [FREE TO MANUFACTURE](OPEN_HARDWARE.md)**: This technology is patent-free and open for anyone to build commercially. We believe global access requires multiple manufacturers. See [OPEN_HARDWARE.md](OPEN_HARDWARE.md) for details.

---

## 🛠️ **BUILD IT YOURSELF**

### **Two Options for Building Your Own H.A.L.O. Device:**

---

### 🎯 **Option 1: Manual Protocol (Ultra-Accessible)**

### **→ [Manual Protocol Guide - No Headband Required](docs/MANUAL_PROTOCOL.md) ←**

> Total Cost: $35-75 | No EEG | Self-Guided

The simplified version using just tVNS and optional bilateral audio:

- ✅ **90% cheaper** than full system (~$35-75)
- ✅ **No technical setup** (no software, Bluetooth, or computer)
- ✅ **Core therapeutic mechanism** (tVNS + bilateral stimulation + trauma processing)
- ✅ **Fully portable** (fits in a bag)
- ⚠️ Requires learning to recognize your own nervous system states

**Required:**

- TENS 7000 unit (~$35)
- Ear clip electrodes (~$10)

**Optional but recommended:**

- Over-ear headphones (~$30+) for bilateral audio stimulation

**[→ Start with Manual Protocol](docs/MANUAL_PROTOCOL.md)**

---

### 🔬 **Option 2: Full Automated System (With EEG Biofeedback)**

### **→ [Complete DIY Build Instructions](docs/SETUP.md) ←**

> Total Cost: ~$500 | Build Time: 1-2 hours

The full system with automated EEG-based intervention:

📋 **[Hardware Setup Guide](docs/SETUP.md)** - Complete bill of materials, safety warnings, and assembly instructions  
⚡ **[Quick Start Guide](docs/QUICKSTART.md)** - Get running in 30 minutes  
❓ **[FAQ](docs/FAQ.md)** - Troubleshooting and common questions

**Required Components:**

- Muse S (Gen 2/Athena) headband (~$400)
- TENS 7000 unit (~$35)
- Ear clip electrodes (~$10)
- Computer with Bluetooth
- Stereo earbuds

**All designs, software, and instructions are free and open source. Start building today!**

---

## 🎯 Executive Summary

**Project H.A.L.O.** is a closed-loop wearable system designed to mechanically regulate the brain's **Salience Network** during shadow work and trauma processing. It detects when a user is "stuck" in a trauma loop (Default Mode Network dominance) and mechanically intervenes to shift neural activity into the present moment (Task Positive Network), creating a safe biological container for processing.

### The Thesis

**Courage is not a personality trait; it is a biological state.** By automating the regulation of the Vagus Nerve and the Salience Network, we enable individuals to "Witness" their trauma without being hijacked by it.

---

## 🧠 The Science

### The Three-Network Architecture

#### Default Mode Network (DMN) - "The Archive"

- Active during rumination, past-future thinking, self-referential narrative
- In PTSD/Anxiety: Hyperactive, loops trauma stories, causes flashbacks and dissociation

#### Task Positive Network (TPN) - "The Laser"

- Active during focused attention, flow states, external engagement
- Anti-correlated with DMN: When TPN is up, DMN is down

#### Salience Network (SN) - "The Switch"

- Anchored in Anterior Insula and Anterior Cingulate Cortex
- Monitors inputs to decide which network should be active
- **The Malfunction:** In trauma, the "Switch" gets stuck. DMN overrides SN.

### H.A.L.O.'s Mechanism of Action

1. **Polyvagal Theory (Safety)**: tVNS (Transcutaneous Vagus Nerve Stimulation) manually triggers Parasympathetic Nervous System, preventing Amygdala hijack
2. **EMDR (Processing)**: Bilateral Stimulation (Haptics/Audio) taxes working memory and forces inter-hemispheric communication, keeping TPN active
3. **Biofeedback (Automation)**: EEG monitors brain states to detect triggers before conscious awareness, deploying intervention automatically

---

## 🔧 Hardware Stack

### Bill of Materials

#### Required Components

- **Muse S (Gen 2/Athena)**: EEG/PPG sensing headband
- **TENS 7000 Unit**: Standard analog TENS device (~$35)
- **Ear Clip Electrodes**: Double-ended clip (Lead wire to 2mm pin)
- **Pixel Buds Pro** (or equivalent): For audio delivery with spatial audio capability
- **Computer**: Windows/Mac/Linux with Bluetooth

#### Optional Components

- Electrolytes supplement (Sodium/Potassium/Magnesium)
- L-Arginine (Nitric Oxide precursor)
- L-Theanine (Alpha wave support)

---

## 📦 Installation

### 1. Install OpenMuse

OpenMuse is the Python library that handles communication with the Muse S Athena headband.

```powershell
pip install https://github.com/DominiqueMakowski/OpenMuse/zipball/main
```

### 2. Install Project H.A.L.O

```bash
```bash
git clone https://github.com/ClaimFreedomDotOrg/ProjectHALO.git
cd ProjectHALO
pip install -e .
```

This installs the package in editable mode with all dependencies.

### 3. Find Your Muse Device

Power up your Muse S Athena headband (blue light should appear) and run:

```powershell
OpenMuse find
```

Note the MAC address of your device for use in the monitoring script.

---

## 🚀 Quick Start

### Step 1: Hardware Setup

See [SETUP.md](docs/SETUP.md) for detailed hardware assembly instructions, including:

- TENS electrode placement
- Safety-critical TENS settings
- Audio device configuration

### Step 2: Run the Monitor

```bash
halo-monitor --address YOUR_MUSE_MAC_ADDRESS
```

The monitor will:

1. Connect to your Muse S headband
2. Stream EEG data in real-time
3. Calculate Alpha/Beta ratios
4. Alert when "Shadow Spike" is detected (Alpha drop + Beta spike)

### Step 3: Manual Intervention (MVP)

When the terminal displays **">>> SHADOW DETECTED"**:

1. Slowly turn TENS dial UP to therapeutic level (tingle sensation)
2. Focus on bilateral audio (left/right panning)
3. Maintain witness state while processing the trauma
4. Turn TENS down once emotional charge dissipates

---

## 📖 Operational Protocols

See [PROTOCOLS.md](docs/PROTOCOLS.md) for detailed instructions on:

- **Protocol A: "The Hunter"** - Active shadow work targeting specific trauma
- **Protocol B: "The Lucid Diver"** - Deep gnosis and exploration
- **Protocol C: "The Automated Shield"** - Future closed-loop automation

---

## 🔬 Theoretical Foundation

### The Dual-Parasitic System

#### Mind Parasite: Wetiko (DMN Loop)

- Theological: The "Archons" or "Powers and Principalities"
- Scientific: Hyperactive Default Mode Network trapping consciousness in loops
- Effect: Spirit locked out of Body

#### Body Parasite: Glycation (Decay)

- Theological: "Corruption of the Flesh"
- Scientific: Advanced Glycation End Products (AGEs) causing tissue stiffening
- Effect: Body loses conductivity to house high-frequency consciousness

### The Unified Solution

#### Neuro-Correction (H.A.L.O.)

- Detect: EEG monitors for "Shadow Spike"
- Override: tVNS sends safety signal to brainstem
- Align: Bilateral stimulation synchronizes hemispheres

#### Metabolic Correction (Anti-Glycation)

- L-Arginine: Increases Nitric Oxide production
- L-Theanine: Promotes Alpha wave generation
- Electrolytes: Essential for bio-electric signal conduction

---

## ⚠️ Safety Considerations

### TENS Use - Critical Safety Information

- **DO NOT** use TENS if you have a pacemaker or heart condition
- **DO NOT** place electrodes across the heart or on the front of the neck
- **DO NOT** use while driving or operating machinery
- **DO NOT** exceed comfortable tingle sensation - pain indicates too high intensity
- Start at intensity 0 and slowly dial up
- If ear twitches or hurts, dial back immediately

### General Considerations

- This is experimental research software, not medical advice
- Consult healthcare providers before starting any new protocol
- Not a replacement for professional mental health care
- Use at your own risk

---

## 🛣️ Roadmap

### Current Version: MVP (Manual Intervention)

- ✅ Real-time EEG monitoring
- ✅ Alpha/Beta ratio calculation
- ✅ Visual alerts for Shadow Spike detection
- ✅ Manual TENS intervention

### V2: The Cyborg

- [ ] Integration of Muse S + IDUN Technologies dry in-ear electrodes
- [ ] Single-device form factor

### V3: The Closed Loop

- [ ] Custom PCB with Time-Division Multiplexing
- [ ] Simultaneous tVNS output + EEG input
- [ ] Fully automated intervention via Bluetooth

---

## 📚 Citations & References

- Porges, S. W. (2011). *The Polyvagal Theory: Neurophysiological Foundations of Emotions*
- Raichle, M. E. (2015). *The Brain's Default Mode Network*. Annual Review of Neuroscience
- Shapiro, F. (2018). *Eye Movement Desensitization and Reprocessing (EMDR) Therapy*
- The Gospel of Thomas, Logion 22: "When you make the two one... then you will enter the Kingdom"

---

## 🙏 Acknowledgments

- **OpenMuse**: Dominique Makowski for the excellent Muse S Athena Python library
- **InteraXon Inc**: For creating the Muse S headband (though this is not an official InteraXon product)
- The ancient wisdom keepers who understood these principles before we had the language

---

## 📄 License

MIT License - See [LICENSE](LICENSE) for details

---

## ⚡ Disclaimer

> **Project H.A.L.O. is NOT an official medical device and is not intended to diagnose, treat, cure, or prevent any disease.** This is experimental research software developed for personal exploration and is not affiliated with or endorsed by InteraXon Inc, OpenMuse, or any other organization. Use at your own risk.

---

> *"We are building the Ark for the modern flood of information and trauma. The door is open."*
