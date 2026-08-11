# Secrets Rotation, Envelope Encryption, KMS and HSM Architecture

Build a practical key-management architecture model: data keys, key-encryption keys, KMS/HSM boundaries, envelope encryption, rotation, grants, audit trails and recovery.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, captures, or lab environments you own or are explicitly authorized to test. Prefer localhost, synthetic data, disposable VMs/containers, prerecorded traces, and read-only analysis whenever possible.

## Learning objectives

By the end of this module you should be able to:

- Explain **data keys and key-encryption keys** and identify its most important trust boundary, state transition, and evidence source.
- Explain **envelope encryption** and identify its most important trust boundary, state transition, and evidence source.
- Explain **KMS authorization and grants** and identify its most important trust boundary, state transition, and evidence source.
- Explain **HSM trust boundaries** and identify its most important trust boundary, state transition, and evidence source.
- Explain **rotation versus re-encryption** and identify its most important trust boundary, state transition, and evidence source.
- Explain **key versioning and cryptoperiods** and identify its most important trust boundary, state transition, and evidence source.

## Analysis method

Use [Study Method](../Guides/STUDY-METHOD.md). Start by identifying ownership or identity, the state transition that can fail, and the evidence that would distinguish a real boundary violation from a diagnostic artifact.

## Deep concepts

### 1. data keys and key-encryption keys

Envelope encryption separates data-encryption keys from higher-level keys that protect or wrap them. This limits direct use of root keys and lets applications rotate wrapping policy without necessarily rewriting every byte of protected data.

### 2. envelope encryption

A common design generates a fresh data key, encrypts data locally, then stores only the ciphertext plus a wrapped form of that data key. Bind context such as tenant/resource identifiers where supported so a wrapped key cannot be moved silently to an unrelated object.

### 3. KMS authentication and grants

Cloud or enterprise KMS operations are authorization decisions over high-value keys. Restrict which workload identities may encrypt, decrypt, sign, or administer; separate key administrators from data users and log resource, operation, key version, and caller context.

### 4. HSM boundaries

Hardware Security Modules isolate key material and cryptographic operations behind a controlled interface. An HSM does not fix application authorization: if an overly privileged service is allowed to request decryption for arbitrary data, the hardware will faithfully perform the wrong authorized operation.

### 5. rotation versus re-encryption

Rotating a master/wrapping key can mean new writes use a new version while old ciphertext remains decryptable with old versions. Full re-encryption is a separate migration task with availability, integrity, cost, and rollback considerations.

### 6. versioning and cryptoperiods

Keys should have stable identifiers and explicit versions so systems know which material produced an artifact. Cryptoperiods depend on algorithm, exposure, data sensitivity, usage volume, recovery, and operational constraints rather than one universal rotation interval.

### 7. backup and recovery

Key loss can be as damaging as key theft. Define whether keys are recoverable, how backups are protected, who can authorize recovery, what quorum or offline controls exist, and how a recovery event is audited and tested.

### 8. audit and key-use attribution

Every sensitive key operation should be attributable to a workload/user identity, key/version, operation, resource context, policy decision, and time. Avoid logging plaintext secrets or data while retaining enough correlation to investigate unexpected decrypt/sign activity.

## Engineering focus

For this module, convert each important claim into a security invariant and a regression test. Prefer controls that remove unnecessary authority, make state transitions explicit, bound resource use, and leave enough telemetry to explain a failure. The reusable evidence and lab-record format is in [Study Method](../Guides/STUDY-METHOD.md).

## Authorized lab sequence

### Lab 1 — Design envelope encryption for a fictional database record and show what is stored beside ciphertext.



### Lab 2 — Create a rotation matrix for API secrets, TLS keys, database encryption keys and signing keys.



### Lab 3 — Model KMS outage and key-revocation scenarios and define what should fail open versus fail closed.

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

Recommended related modules: **020, 049, 078, 100, 101, 103, 113**. From the main menu, choose **Search lessons** to find related sections across the full guide.
