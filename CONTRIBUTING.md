# Contributing to Project H.A.L.O

Thank you for your interest in contributing to Project H.A.L.O.! This project is at the intersection of neuroscience, spiritual practice, and open-source hardware/software.

## Project Vision

Project H.A.L.O. aims to democratize access to advanced neuro-regulation tools for trauma healing and consciousness exploration. We believe that these tools should be:

- Open source and transparent
- Accessible (affordable, DIY-friendly)
- Grounded in both science and wisdom traditions
- Safe and ethical

## Ways to Contribute

### 1. Testing & Feedback

- **Build the system** and document your experience
- **Report bugs** via GitHub Issues
- **Share session logs** (anonymized) to improve algorithms
- **Test on different hardware** configurations

### 2. Code Contributions

- **Improve the `halo` package**:
  - Better signal processing algorithms
  - Real-time visualization (matplotlib/plotly)
  - Machine learning for trigger prediction
- **New features**:
  - Data logging and export
  - Session analytics dashboard
  - Mobile app companion
- **Hardware integration**:
  - Automated TENS control via serial/USB
  - Support for other EEG devices (OpenBCI, Neurosity Crown)
  - Haptic feedback devices

### 3. Documentation

- **Improve guides**: Clarify setup instructions, add photos/diagrams
- **Translations**: Make docs accessible in other languages
- **Video tutorials**: Screen recordings or hardware assembly guides
- **Case studies**: Anonymized reports of effectiveness

### 4. Research & Validation

- **Experimental validation**:
  - Verify timestamp accuracy
  - Validate Alpha/Beta detection against known triggers
  - Compare with clinical EMDR outcomes
- **Literature review**: Connect to relevant research papers
- **Theoretical framework**: Refine the neuroscience/theology synthesis

### 5. Hardware Development

- **V2 Goals** (Single-device form factor):
  - IDUN Technologies ear-EEG integration
  - 3D-printable electrode housings
- **V3 Goals** (Closed-loop automation):
  - Custom PCB design for TDM (Time-Division Multiplexing)
  - Bluetooth-controlled TENS unit
  - Wearable haptic actuators

## Code Style Guidelines

### Python

- **PEP 8** compliant (use `black` formatter)
- **Type hints** where helpful (Python 3.8+)
- **Docstrings** for all public functions (Google style)
- **Comments** for complex signal processing logic

### Git Workflow

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit with clear messages: `git commit -m "Add: real-time FFT visualization"`
4. Push to your fork: `git push origin feature/your-feature-name`
5. Open a Pull Request with description of changes

### Commit Message Format

```Markdown
Type: Brief description (50 chars max)

Longer explanation if needed (wrap at 72 chars).
- Bullet points for multiple changes
- Reference issues: "Fixes #42"

Types: Add, Fix, Update, Remove, Refactor, Docs, Test
```

## Safety & Ethics

### Critical Rules for Contributors

1. **Never compromise safety**:
   - All TENS-related code must include safety checks
   - Document maximum safe intensities
   - Always warn about contraindications

2. **Respect user autonomy**:
   - No forced interventions without user control
   - Clear documentation of what system does
   - Easy emergency stop mechanisms

3. **Scientific integrity**:
   - Don't overstate effectiveness
   - Distinguish between hypothesis and validated findings
   - Cite sources for claims

4. **Privacy & data**:
   - No telemetry without explicit opt-in
   - No sharing of EEG data without consent
   - Anonymize all shared logs/examples

5. **Medical disclaimers**:
   - Never claim this is medical treatment
   - Always recommend professional help for serious conditions
   - Maintain "research/exploration tool" framing

## Testing Requirements

Before submitting code:

- [ ] Test with real Muse S hardware (if modifying core monitoring code)
- [ ] Verify no new dependencies without updating `pyproject.toml`
- [ ] Check that safety warnings are preserved
- [ ] Run basic smoke test: `halo-monitor --help`
- [ ] Update relevant documentation

## Areas Needing Help

### High Priority

- [ ] **Signal quality validation**: Verify EEG signal processing accuracy
- [ ] **Cross-platform testing**: Test on macOS, Linux (currently Windows-focused)
- [ ] **Automated TENS control**: Research safe methods for programmatic intensity adjustment
- [ ] **Real-time visualization**: Add live Alpha/Beta plots to monitor

### Medium Priority

- [ ] **Session analytics**: Statistical analysis of multiple sessions over time
- [ ] **Audio integration**: Automatically trigger bilateral audio on detection
- [ ] **Alternative EEG devices**: Support for OpenBCI, Neurosity Crown, etc.
- [ ] **Mobile companion app**: Remote monitoring/control via phone

### Research Questions

- [ ] **Optimal trigger threshold**: Is 0.7 Alpha/Beta ratio best, or should it be adaptive?
- [ ] **TENS frequency tuning**: Is 25Hz optimal, or should it vary by individual?
- [ ] **Bilateral stimulation rate**: What L/R alternation speed is most effective?
- [ ] **Buffer window**: Is 5 seconds the right analysis window?

## Communication

### GitHub Issues

- **Bug reports**: Use "Bug" label, include Python version, OS, hardware
- **Feature requests**: Use "Enhancement" label, explain use case
- **Questions**: Use "Question" label, check docs first

### Discussions

- Use GitHub Discussions for:
  - Sharing experiences and insights
  - Theoretical discussions
  - Hardware recommendations
  - Integration ideas

### Code of Conduct

- **Be respectful**: This intersects personal beliefs (spiritual/religious)
- **Assume good faith**: We're all learning
- **Focus on ideas, not people**: Critique code, not coders
- **Be patient**: Trauma work is sensitive; meet people where they are

## Recognition

Contributors will be acknowledged in:

- README.md "Contributors" section
- Release notes for significant contributions
- Documentation for major features

## Legal

By contributing, you agree that:

- Your contributions are your original work
- You grant the project an MIT license to your contributions
- You have read and agree to the safety disclaimers
- You will not hold the project liable for any consequences of your contributions

---

## Getting Started

Ready to contribute?

1. **Read the docs**: README.md, SETUP.md, PROTOCOLS.md
2. **Build the system**: Follow SETUP.md to get hardware working
3. **Run the code**: Install package with `pip install -e .` and test with your Muse S
4. **Pick an issue**: Check "good first issue" label on GitHub
5. **Ask questions**: Open a Discussion if stuck

**Welcome to the project. Let's build tools for liberation together.**

---

> *"We are building the Ark for the modern flood. Your contribution is a plank in that vessel."*
