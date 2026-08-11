# Hardware, Firmware and Boot Security

> **Purpose:** Extend security thinking below the operating system into firmware, boot integrity, hardware-backed keys, device lifecycle, and supply-chain trust.

## Learning objectives

- Explain firmware, UEFI/bootloaders, Secure Boot, measured boot, TPM/secure elements, and hardware-backed key storage.
- Understand firmware update and recovery risks.
- Recognize why physical access changes the threat model.
- Evaluate device lifecycle and supply-chain controls.

## Layers below the OS

A system may depend on CPU microcode, platform firmware, UEFI/bootloader, storage firmware, peripheral firmware, secure elements, and other controllers before the operating system begins normal execution. These layers can have high privilege and may be difficult for ordinary endpoint controls to inspect.

## Secure Boot

Secure Boot aims to restrict the boot chain to trusted, signed components according to configured policy. It helps prevent unauthorized boot components but does not guarantee that every signed component is vulnerability-free or correctly configured.

## Measured boot

Measured boot records cryptographic measurements of boot components into protected facilities such as TPM registers. Those measurements can support attestation and forensic reasoning. Measurement is not the same as enforcement: a system can measure something without necessarily blocking it.

## TPMs and secure elements

Hardware-backed security components can protect keys, measurements, or cryptographic operations. Good design avoids exporting private key material unnecessarily and binds sensitive operations to appropriate device/user state. Recovery planning remains essential because hardware-backed protection can make key loss unrecoverable if no authorized recovery path exists.

## Firmware updates

Treat firmware as patchable software. Inventory versions, obtain updates from trusted vendor channels, verify authenticity using the vendor's supported mechanism, understand power/reboot requirements, and maintain recovery instructions. Unsupported devices can become security liabilities when firmware updates stop.

## Physical access

Physical access can enable attacks unavailable to a remote adversary: booting alternate media, removing storage, attaching debug interfaces, resetting devices, or observing/replacing peripherals. Mitigations may include full-disk encryption, secure boot policy, firmware/boot settings, hardware-backed keys, port controls, screen lock, tamper procedures, and asset custody.

## Full-disk encryption and boot trust

Disk encryption protects data at rest, especially against lost/stolen storage, but its security depends on key management and the state in which the device is captured. A running unlocked device has a different threat model from a powered-off encrypted device.

## Mobile device hardware security

Modern phones commonly use verified boot, hardware-backed keystores, secure execution environments, rollback protection, and app sandboxing. Security decisions should use supported platform APIs rather than attempting to replicate key protection in ordinary application storage.

## IoT/embedded guidance

For embedded devices, ask:

- Is firmware signed?
- Can rollback to vulnerable firmware occur?
- How are device identities/keys provisioned?
- Is the debug interface disabled or controlled in production?
- What happens when the vendor ends support?
- Can the device recover safely from a failed update?
- Are default/shared credentials eliminated?
- Is management traffic authenticated and encrypted?

## Supply-chain questions

Hardware security also includes procurement and provenance:

- approved suppliers;
- tamper-evident shipping/receiving where justified;
- component lifecycle tracking;
- firmware/software bills of materials where available;
- update-channel authenticity;
- end-of-life replacement planning;
- secure disposal and key/data destruction.

## Safe learning exercise

Create an inventory of devices you own. Record model, OS/firmware version, support status, encryption state, update channel, backup/recovery method, and whether important keys are hardware-backed. Do not change firmware settings merely to complete a lab; the objective is understanding the trust chain.

## Checkpoint

You should be able to draw the boot chain of one device you own and identify where trust is established, where keys live, how updates are verified, and how recovery works. Continue with Modules 17, 18, 33, 48, and 49.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 01 and 20.

### Practice task

Inventory the boot/update/encryption/recovery security of devices you own. Record trust chain and support lifecycle without changing critical firmware settings just for practice.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **17, 18, 48, 49, 56**.
