# Bluetooth, NFC and Proximity Security

> **Purpose:** Understand short-range radio and proximity security with emphasis on pairing, identity, privacy, configuration, and safe testing of devices you own.

## Learning objectives

- Distinguish Bluetooth Classic and Bluetooth Low Energy at a practical level.
- Understand discovery, pairing/bonding, services/characteristics, and permissions conceptually.
- Explain NFC's proximity model and common use cases.
- Evaluate device privacy, update, and pairing hygiene.

## Bluetooth security model

Bluetooth security depends on protocol version, pairing method, device capabilities, implementation quality, user confirmation, key storage, and application-layer design. “Short range” should never be treated as authentication.

## Pairing guidance

When pairing devices you own:

- verify the intended device name/model and physical context;
- prefer pairing methods that provide meaningful user confirmation;
- remove stale pairings;
- keep firmware/OS updated;
- disable unnecessary discoverability;
- avoid pairing sensitive devices in crowded/untrusted environments when confirmation is weak.

## BLE services and characteristics

Bluetooth Low Energy applications commonly expose GATT services and characteristics. Security can depend on whether operations require an encrypted/authenticated connection and whether the application performs its own authorization. A characteristic being discoverable does not imply every write/read should be public.

## Privacy

Bluetooth identifiers and advertising behavior can create tracking concerns. Modern platforms use address randomization and permission controls, but applications should still minimize persistent identifiers and unnecessary background scanning.

## NFC

NFC is commonly used for tags, payments, access, device setup, and data exchange. Proximity reduces some risks but does not prove user intent or authorization. Treat data read from tags as untrusted input and require confirmation for sensitive state changes.

## UWB and proximity claims

Ultra-wideband and related ranging technologies can improve distance estimation, but secure proximity systems still need cryptographic identity, replay resistance, protocol hardening, and safe failure behavior. Distance alone is not authorization.

## Device inventory exercise

For devices you own, document:

- radio types enabled;
- pairing/bonded devices;
- last update date;
- whether discoverability is normally enabled;
- app permissions related to nearby devices/location;
- how lost/stolen-device access is revoked;
- whether the device stores sensitive data.

## Safe lab ideas

Use only your own devices. You can safely practice by:

- observing your phone's paired-device list;
- documenting permission prompts;
- testing what happens when a device is unpaired and re-paired;
- verifying whether a device reconnects automatically;
- reviewing vendor firmware update procedures;
- reading your own NFC tag that contains synthetic text/URL data.

Do not attempt to intercept, impersonate, or interfere with nearby third-party devices.

## Defensive checklist

- Keep radio stacks and device firmware updated.
- Remove unused pairings.
- Disable discoverability when unnecessary.
- Use strong device unlock and encryption.
- Restrict app permissions.
- Require explicit authorization for sensitive actions.
- Log security-relevant pairing/account changes where the platform supports it.
- Have a revocation process for lost devices.

## Checkpoint

You should be able to explain why radio range is not a trust boundary and why application-layer authorization remains important. Continue with Modules 16, 17, 18, and 44.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 16 and 17 help.

### Practice task

Audit pairings, permissions, update state, and proximity-security behavior only on devices/tags you own. Document what proves user intent versus mere physical proximity.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **44, 56, 60**.
