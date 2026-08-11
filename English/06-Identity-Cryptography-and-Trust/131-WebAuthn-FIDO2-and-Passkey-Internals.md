# WebAuthn, FIDO2 and Passkey Internals

Go beyond “passkeys are phishing resistant.” Understand relying-party scope, origins, credential IDs, discoverable credentials, authenticators, attestation, user verification and recovery.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, captures, or lab environments you own or are explicitly authorized to test. Prefer localhost, synthetic data, disposable VMs/containers, prerecorded traces, and read-only analysis whenever possible.

## Learning objectives

By the end of this module you should be able to:

- Explain **WebAuthn ceremony roles** and identify its most important trust boundary, state transition, and evidence source.
- Explain **Relying Party ID and origin binding** and identify its most important trust boundary, state transition, and evidence source.
- Explain **credential creation and assertions** and identify its most important trust boundary, state transition, and evidence source.
- Explain **authenticator data and counters** and identify its most important trust boundary, state transition, and evidence source.
- Explain **user presence versus user verification** and identify its most important trust boundary, state transition, and evidence source.
- Explain **discoverable/syncable credentials** and identify its most important trust boundary, state transition, and evidence source.

## Analysis method

Use [Study Method](../Guides/STUDY-METHOD.md). Start by identifying ownership or identity, the state transition that can fail, and the evidence that would distinguish a real boundary violation from a diagnostic artifact.

## Deep concepts

### 1. ceremony roles

WebAuthn involves a relying party, browser/client, authenticator, and user. The ceremony binds these actors using origin/RP context and public-key credentials so authentication does not depend on sending a reusable password secret to the relying party.

### 2. RP ID and origin binding

The RP ID scopes credentials to an expected web domain relationship, while the browser supplies origin context. Correct validation prevents a credential assertion created for one site from being accepted by an unrelated site simply because the account name matches.

### 3. creation and assertion

Registration creates a credential and stores its public information; authentication requests a signed assertion over fresh challenge/context. Challenges must be unpredictable, single-use, session-bound, and expire so captured responses cannot be reused as generic bearer credentials.

### 4. authenticator data and counters

Authenticator data carries RP binding, flags, and additional authenticator state; some authenticators also expose signature counters. Counters can be a risk signal but should not be treated as universally reliable because synchronization and authenticator behavior vary.

### 5. user presence versus verification

User presence shows that someone interacted with the authenticator, while user verification adds a local factor such as PIN or biometric policy. Relying parties should request the level appropriate to the transaction and validate returned flags against that policy.

### 6. discoverable and syncable credentials

Discoverable credentials can support username-less sign-in, and passkeys may be synchronized across a user’s trusted device ecosystem. Threat modeling must therefore include account recovery, device enrollment, sync-provider security, and user notification—not only the hardware authenticator.

### 7. attestation and privacy

Attestation can provide information about authenticator provenance but can also add deployment complexity and privacy implications. Require it only when a concrete assurance need justifies the operational cost; authentication security does not generally depend on identifying a user’s device model.

### 8. recovery and multi-device lifecycle

Passkey deployments need recovery, new-device onboarding, credential inventory, revocation, lost-device response, and multiple-authenticator support. A weak recovery channel can become the easiest way around otherwise phishing-resistant authentication.

## Engineering focus

For this module, convert each important claim into a security invariant and a regression test. Prefer controls that remove unnecessary authority, make state transitions explicit, bound resource use, and leave enough telemetry to explain a failure. The reusable evidence and lab-record format is in [Study Method](../Guides/STUDY-METHOD.md).

## Authorized lab sequence

### Lab 1 — Design a WebAuthn registration/authentication sequence diagram with challenge, origin and RP-ID validation points.



### Lab 2 — Compare password+OTP, device-bound WebAuthn and syncable passkeys across phishing resistance, recovery and device loss.



### Lab 3 — Create a recovery threat model for a fictional passkey-only service.

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

Recommended related modules: **021, 039, 049, 078, 092, 100**. From the main menu, choose **Search lessons** to find related sections across the full guide.
