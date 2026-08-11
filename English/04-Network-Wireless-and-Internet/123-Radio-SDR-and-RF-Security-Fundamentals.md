# Radio, SDR and RF Security Fundamentals

Build the signal-processing literacy needed to reason about wireless systems safely: spectrum, modulation, framing, synchronization, RF fingerprints, replay risk and legal/ethical lab boundaries.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, captures, or lab environments you own or are explicitly authorized to test. Prefer localhost, synthetic data, disposable VMs/containers, prerecorded traces, and read-only analysis whenever possible.

## Learning objectives

By the end of this module you should be able to:

- Explain **frequency, bandwidth and sampling** and identify its most important trust boundary, state transition, and evidence source.
- Explain **I/Q representation** and identify its most important trust boundary, state transition, and evidence source.
- Explain **modulation and symbol timing** and identify its most important trust boundary, state transition, and evidence source.
- Explain **preambles, frames and checksums** and identify its most important trust boundary, state transition, and evidence source.
- Explain **noise, interference and SNR** and identify its most important trust boundary, state transition, and evidence source.
- Explain **receive-only spectrum analysis** and identify its most important trust boundary, state transition, and evidence source.

## Analysis method

Use [Study Method](../Guides/STUDY-METHOD.md). Start by identifying ownership or identity, the state transition that can fail, and the evidence that would distinguish a real boundary violation from a diagnostic artifact.

## Deep concepts

### 1. frequency, bandwidth and sampling

RF analysis starts with frequency range, occupied bandwidth, sample rate, and receiver limitations. A sampled signal is only a representation of energy within the configured front end, so document gain, filters, antenna, clock, and environment before drawing protocol conclusions.

### 2. I/Q representation

Software-defined radios commonly represent a signal as in-phase and quadrature samples. I/Q preserves amplitude and phase information needed for digital demodulation, but raw samples do not identify a protocol or sender without additional framing and context.

### 3. modulation and symbol timing

Modulation maps information onto changes in amplitude, phase, frequency, or combinations of them. Correct decoding also depends on symbol timing, carrier synchronization, channel conditions, and protocol parameters, which should be measured rather than guessed.

### 4. preambles, frames and checksums

Wireless protocols use synchronization/preamble patterns, headers, payloads, checksums or stronger integrity mechanisms to frame data. A checksum detects accidental corruption but is not an authentication mechanism unless a cryptographic construction explicitly provides authenticity.

### 5. noise, interference and SNR

Noise and interference can look like protocol failure or security events. Measure signal-to-noise ratio, channel occupancy, receiver saturation, and environmental changes before attributing missing or malformed frames to an attacker.

### 6. receive-only spectrum analysis

Receive-only analysis is the safest default for learning RF behavior. Use owned devices or licensed/public test signals, record only what is necessary, and avoid decoding private communications that you are not authorized to inspect.

### 7. authentication versus signal presence

Detecting a waveform or valid-looking frame proves only that energy or syntax was observed. Security decisions require cryptographic or trusted identity context; physical proximity and RF strength are not reliable authentication by themselves.

### 8. replay resistance and rolling state

Protocols that authorize physical actions need freshness such as nonces, counters, challenge-response, or carefully managed rolling state. Test replay resistance with synthetic/owned devices and focus on state synchronization and recovery rather than reproducing unauthorized control actions.

## Engineering focus

For this module, convert each important claim into a security invariant and a regression test. Prefer controls that remove unnecessary authority, make state transitions explicit, bound resource use, and leave enough telemetry to explain a failure. The reusable evidence and lab-record format is in [Study Method](../Guides/STUDY-METHOD.md).

## Authorized lab sequence

### Lab 1 — Use a prerecorded or synthetic IQ dataset and identify signal bandwidth, bursts and framing without transmitting.



### Lab 2 — Create a toy digital-radio frame format and add sequence numbers plus a MAC in software to demonstrate freshness/integrity.



### Lab 3 — Document how a rolling-code design differs from a static replayable identifier.

For every lab, use only owned/synthetic inputs and record objective, scope, version, expected behavior, observed evidence, cleanup, remediation, and regression result as described in [Study Method](../Guides/STUDY-METHOD.md).

## Knowledge checks

Answer these without looking at the notes:

1. What is the primary trust boundary in this topic?
2. Which state or identity transition is easiest to misunderstand?
3. What observation would disprove your first hypothesis?
4. Which control removes authority rather than merely adding detection?
5. How would you reproduce the behavior safely after remediation?

## Guided study workflow

Complete at least one authorized lab and explain the mechanism, trust boundary, failure state, evidence, and defensive fix in your own words. Use **Bookmarks**, **Progress**, and **Learning paths** in the numbered menu instead of memorizing command-line flags.

## Next modules

Recommended related modules: **016, 051, 055, 077, 083, 122**. From the main menu, choose **Search lessons** to find related sections across the full guide.
