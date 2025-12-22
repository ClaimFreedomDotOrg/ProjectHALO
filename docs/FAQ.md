# Frequently Asked Questions (FAQ)

## General Questions

### What is Project H.A.L.O.?

Project H.A.L.O. (Hemispheric Alignment & Limbic Override) is an open-source system that uses EEG monitoring and vagus nerve stimulation to help people process trauma and explore consciousness states. It combines the Muse S headband for brain monitoring with TENS for gentle electrical stimulation.

### Is this a medical device?

**No.** Project H.A.L.O. is experimental research software, not a medical device. It is not FDA-approved and is not intended to diagnose, treat, cure, or prevent any disease. Use at your own risk.

### Is this safe?

When used according to the safety guidelines in SETUP.md, the individual components (Muse S, TENS unit) are generally safe. However, TENS has contraindications (pacemaker, heart conditions, epilepsy). **Always consult a healthcare provider before starting.**

### How much does it cost?

- Muse S headband: ~$400
- TENS unit: ~$35
- Electrodes: ~$10-15
- Earbuds (if you don't have): $20-200
- **Total**: ~$465-650

### Can I build this myself?

Yes! That's the point. All documentation is open source, and we use off-the-shelf consumer hardware. No soldering required for the basic version.

### Is this affiliated with Muse/InteraXon?

**No.** We use the Muse S headband, but we are not affiliated with, endorsed by, or approved by InteraXon Inc.

---

## Technical Questions

### Why OpenMuse instead of BlueMuse?

OpenMuse is a newer Python library specifically designed for the Muse S Athena. It provides direct access to the raw data stream without needing LSL middleware, making the setup simpler and more reliable.

### What operating systems are supported?

- **Windows**: Fully tested
- **macOS**: Should work (Bluetooth + Python)
- **Linux**: Should work (requires Bluez)

Not extensively tested on macOS/Linux yet - contributions welcome!

### Can I use a different EEG headset?

In theory, yes. You'd need to adapt the `halo` package to work with your device's data format. OpenBCI and Neurosity Crown are potential alternatives. We may add support in future versions.

### Why is the trigger threshold set to 0.7?

This is an empirical starting point. The ratio of Alpha/Beta power tends to drop below 0.7 when someone transitions from a calm state to an anxious/triggered state. However, this may need adjustment per individual.

### How accurate is the EEG detection?

The Muse S is consumer-grade EEG, not research-grade. It's sufficient for detecting general state changes (calm vs. stressed) but not precise enough for detailed brain mapping. For this application (trauma work), it's adequate.

### Why does the monitor need 5 seconds of data?

FFT (Fast Fourier Transform) requires a sufficient number of samples to accurately detect low-frequency waves like Alpha (8-12 Hz). With 256 Hz sampling rate, 5 seconds gives us good frequency resolution.

### Can I record sessions for later analysis?

Not in the current MVP version, but this is planned. You can manually modify the `halo` package to save data, or use the `examples/analyze_recording.py` script with OpenMuse's recording feature.

---

## Protocol Questions

### Which protocol should I start with?

**Protocol A (The Hunter)** - It's the most straightforward and has a clear target (process a specific memory). Protocol B is more advanced and can be disorienting if you're not familiar with altered states.

### How often should I use H.A.L.O.?

- **Protocol A (Trauma work)**: 2-3 times per week maximum. Processing is taxing; you need integration time.
- **Protocol B (Exploration)**: As desired, but give yourself 24-48 hours between sessions.

Start conservatively. More is not always better.

### How long until I see results?

This is highly individual. Some people report immediate relief after one session. For complex trauma, it may take multiple sessions over weeks or months. This is a tool, not a magic bullet.

### Can H.A.L.O. replace therapy?

**No.** It can be a valuable adjunct to therapy, especially EMDR or somatic therapies, but it's not a replacement for professional mental health care.

### What if the "SHADOW DETECTED" alert never triggers?

This could mean:

1. You're already in a calm state (good!)
2. You're dissociated (disconnected from emotions)
3. The threshold needs adjustment (try `--threshold 0.8`)
4. You need to engage more actively with the target memory

### What if I get triggered but don't want to process it right now?

Turn off the TENS, stop the audio, open your eyes. You're in control. The system alerts you, but you decide when to engage.

---

## TENS Questions

### Why the left ear specifically?

The vagus nerve has better accessibility on the left side via the auricular branch (at the tragus). The right side can work but is less reliable.

### What should the TENS sensation feel like?

A gentle tingle or "buzz". **NOT pain, NOT muscle twitching.** If your ear is jumping or it hurts, turn it down immediately.

### Can I use a different TENS unit?

Yes, as long as it has:

- Adjustable pulse width (200 µs)
- Adjustable frequency (25-30 Hz range)
- Standard electrode connectors

### How do I know if I'm hitting the vagus nerve?

You should feel:

- Slight tingling in the ear
- Possible subtle slowing of heart rate
- Sense of calm or relaxation

You should NOT feel:

- Pain
- Muscle twitching/spasms
- Dizziness or nausea

### Can I use TENS on other parts of the body simultaneously?

**No.** Stick to the left ear/shoulder configuration only. Other placements could interfere with the vagus nerve stimulation or create safety issues.

---

## Safety Questions

### What are the main risks?

- **TENS misuse**: Placing electrodes incorrectly (near heart) or using too high intensity
- **Psychological distress**: Trauma work can be intense
- **Dissociation**: Getting "stuck" in an altered state
- **Overuse**: Processing too much too fast

All are manageable with proper precautions.

### What should I do if I panic during a session?

1. **Immediately** turn TENS to zero
2. Stop audio
3. Open eyes
4. Stand up and move around
5. Use 5-4-3-2-1 grounding technique
6. Call a friend or crisis line if needed

### Can I use this while on medication?

**Check with your prescriber.** Some medications affect brainwaves or seizure threshold. Antidepressants, antipsychotics, and mood stabilizers should be discussed with your doctor first.

### Can I use this if I have PTSD?

This system was designed with PTSD in mind (inspired by EMDR). However, if you have severe PTSD, **work with a trauma therapist** first. Do not use this as a replacement for professional care.

### What if I have a history of seizures?

**Do not use binaural beats or isochronic tones** (Protocol B). The rhythmic stimulation could potentially trigger seizures. Protocol A with bilateral audio may be safer, but consult a neurologist first.

---

## Hardware Questions

### My Muse won't connect. What do I do?

1. Ensure it's powered on (hold button, blue LED should appear)
2. Check Bluetooth is enabled on your computer
3. Make sure no other apps are connected to it (close official Muse app)
4. Try moving closer to the computer
5. Restart the Muse (hold power button to turn off, then on)

### The EEG signals look noisy. Is that normal?

Some noise is expected, especially if:

- Hair is interfering with sensors
- Sensors aren't making good contact
- You're moving or clenching jaw
- Room has electrical interference (LED lights)

Try: moistening sensors slightly, pushing hair aside, sitting still.

### Can I use this with long hair?

Yes, but you may need to:

- Part hair to expose TP9/TP10 areas behind ears
- Slightly moisten sensors for better contact
- Use hair gel or water on contact points

### Do I need to clean the Muse sensors?

Yes, after each session:

- Wipe sensors with alcohol wipe or damp cloth
- Remove any skin oils or hair products
- Let air dry

This improves signal quality and extends sensor life.

### The TENS electrodes aren't sticking. Help?

- Clean skin with alcohol wipe first (removes oils)
- Ensure sticky pads aren't dried out (replace if old)
- Consider using conductive gel
- Store pads in sealed bag to retain moisture

---

## Audio Questions

### Do binaural beats actually work?

The research is mixed. Some studies show effects, others don't. Anecdotally, many people report state changes. Your mileage may vary. What matters is whether it works for YOU.

### Can I use speakers instead of headphones?

**No** for binaural beats (Protocol B) - they require stereo separation between ears.

**Maybe** for bilateral EMDR (Protocol A), but headphones are strongly recommended for better effect.

### What if I don't hear anything with binaural beats?

Binaural beats aren't a "sound" you hear directly. They're a perceived "wobbling" or "pulsing" created by your brain processing two slightly different frequencies. Turn up the volume slightly and close your eyes - you should feel a subtle pulse.

### Can I use music with lyrics?

**Not recommended for Protocol A.** Lyrics tax working memory, which interferes with trauma processing. Use instrumental bilateral audio instead.

For Protocol B, it depends. Mantras or chants can enhance the experience, but pop songs will likely pull you out of the state.

---

## Results & Expectations

### How will I know if it's working?

For Protocol A (trauma processing):

- Emotional release (crying, anger)
- New perspectives on old memories
- Reduced "charge" on the memory (lower SUDS score)
- Physical sensations (yawning, shaking - trauma release)
- Spontaneous insights

For Protocol B (exploration):

- Visual imagery (geometric patterns, symbols)
- "Knowing" without thinking
- Time dilation
- Sense of presence or communication
- Mystical unity experiences

### What if nothing happens?

Possible reasons:

1. Need to adjust settings (threshold, TENS intensity)
2. Need more sessions to build up effect
3. Expectations too high (subtle effects are normal)
4. Not the right tool for your particular needs

Not everyone responds the same way. That's okay.

### Can this "cure" my trauma?

Trauma doesn't get "cured" - it gets integrated. The goal is not to erase memories but to change your relationship to them, so they no longer control you. This tool can help with that process, but it's not a silver bullet.

### Will my personality change?

Some people report feeling more "themselves" after releasing old patterns. Others notice they're calmer, less reactive, more present. But you're not becoming a different person - you're becoming a healed version of yourself.

---

## Community & Support

### Where can I ask more questions?

- **GitHub Issues**: For bugs and technical problems
- **GitHub Discussions**: For general questions and sharing experiences
- (Future: Discord/Telegram community)

### Can I share my session logs?

Please do! (Anonymized, of course). Data sharing helps improve the algorithms. Consider contributing to future research.

### How can I contribute to the project?

See [CONTRIBUTING.md](CONTRIBUTING.md). We need:

- Testers
- Code contributors
- Documentation writers
- Hardware developers
- Researchers

### Is there a certification or training program?

Not currently. This is a DIY tool. If you're a therapist interested in using this with clients, we'd love to hear from you, but we don't have formal training yet.

---

## Troubleshooting Common Issues

### "Import Error: No module named OpenMuse"

**Solution**: Install OpenMuse:

```bash
pip install https://github.com/DominiqueMakowski/OpenMuse/zipball/main
```

### "Bluetooth device not found"

**Solution**:

- Turn Bluetooth on/off
- Restart computer
- Update Bluetooth drivers
- Try a different Bluetooth adapter (USB dongles work well)

### "Permission denied" error on Linux

**Solution**: Add your user to the `bluetooth` group:

```bash
sudo usermod -a -G bluetooth $USER
```

Then log out and back in.

### Monitor shows all zeros or flatline

**Solution**:

- Check Muse sensor contact (all should be green in official app)
- Restart Muse headband
- Restart monitor script
- Try different preset: `--preset p1035`

### Can't reach therapeutic TENS level without pain

**Solution**:

- Try different electrode position (slightly adjust tragus clip)
- Use conductive gel on electrodes
- Your sensitivity may be high - lower intensity is fine if you feel the effect
- Consider your unit may be too powerful - try a different model

---

## Philosophical Questions

### Is this playing God / messing with nature?

We're using the same principles that underlie meditation, prayer, and ancient practices. We're just making them more accessible and consistent through technology. You could argue that all tools (from fire to eyeglasses) are "messing with nature."

### Is this transhumanism?

In a sense, yes - we're using technology to enhance human capabilities. But it's also deeply humanist: we're trying to heal trauma and connect people to their own innate potential.

### What about the spiritual/religious aspects?

The system works regardless of your belief system. The neuroscience is real. However, the *interpretation* of the experiences (are they brain states or genuine mystical encounters?) is up to you.

### Can this technology be misused?

Any powerful tool can be misused. That's why we emphasize:

- Open source (transparency)
- Safety guidelines
- User autonomy (you control the system)
- Ethical use (healing, not manipulation)

---

## Future Development

### What's on the roadmap?

See [CHANGELOG.md](CHANGELOG.md) for details. Key goals:

- Automated TENS control (V2)
- Real-time visualization
- Session analytics
- Mobile app
- Custom hardware (closed-loop, V3)

### When will Protocol C (Automated Shield) be available?

Estimated 12-24 months. Requires:

- Custom PCB design
- Safety testing
- Regulatory considerations

### Can I help accelerate development?

Yes! See [CONTRIBUTING.md](CONTRIBUTING.md). We especially need:

- Engineers with PCB design experience
- Embedded systems programmers
- People with BCI research background

---

**Still have questions? Open a Discussion on GitHub or create an Issue.**

> *"The only bad question is the one you don't ask."*
