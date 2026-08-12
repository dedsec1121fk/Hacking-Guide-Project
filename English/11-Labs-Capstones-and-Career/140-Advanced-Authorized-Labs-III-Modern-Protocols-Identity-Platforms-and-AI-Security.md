# Advanced Authorized Labs III: Modern Protocols, Identity, Platforms and AI Security

A third capstone lab collection that integrates the new expansion. Every exercise is designed for localhost, synthetic data, disposable VMs/containers or documentation-based modeling.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, captures, or lab environments you own or are explicitly authorized to test. Prefer localhost, synthetic data, disposable VMs/containers, prerecorded traces, and read-only analysis whenever possible.

## Learning objectives

By the end of this module you should be able to:

- Explain **memory-lifetime lab** and identify its most important trust boundary, state transition, and evidence source.
- Explain **race-condition and TOCTOU lab** and identify its most important trust boundary, state transition, and evidence source.
- Explain **IPC/broker authorization lab** and identify its most important trust boundary, state transition, and evidence source.
- Explain **HTTP/3 and edge trust lab** and identify its most important trust boundary, state transition, and evidence source.
- Explain **SAML/SCIM lifecycle lab** and identify its most important trust boundary, state transition, and evidence source.
- Explain **WebAuthn/passkey threat-model lab** and identify its most important trust boundary, state transition, and evidence source.

## Analysis method

Use [Study Method](../Guides/STUDY-METHOD.md). Start by identifying ownership or identity, the state transition that can fail, and the evidence that would distinguish a real boundary violation from a diagnostic artifact.

## Deep concepts

### 1. memory-lifetime lab

Use a small owned program with a deliberate lifetime bug and sanitizer instrumentation. The learning goal is to identify allocation, ownership transfer, invalidation, first bad access, and the code-level fix—not to turn corruption into code execution.

### 2. race-condition and TOCTOU lab

Build a toy concurrent workflow with a controlled race or check/use gap, then use synchronization or an atomic operation to remove it. Preserve a repeatable stress case and verify that the fixed invariant survives many interleavings.

### 3. IPC and broker authorization lab

Create a local low-privilege client and a narrow broker service that exposes one harmless privileged action. Test valid and invalid caller/resource combinations and confirm the broker authorizes using trusted peer context rather than client-declared identity.

### 4. HTTP/3 and edge trust lab

Use a local or disposable stack that exposes an application through a proxy/edge path. Compare protocol/forwarding behavior and verify that host, client identity, authorization, and cache decisions remain consistent without sending tests to public infrastructure.

### 5. SAML and SCIM lifecycle lab

Use synthetic identities in a test IdP/application. Model login, attribute mapping, provisioning, role change, disable, session revocation, and reconciliation; measure which state changes propagate and where stale access can remain.

### 6. WebAuthn and passkey threat-model lab

Use a development relying party or documented test environment to trace registration, challenge, origin/RP binding, user verification, authentication, lost-device recovery, and credential revocation. Record which controls are cryptographic and which are account-lifecycle policy.

### 7. Kubernetes policy lab

In a disposable cluster, define a small admission or workload policy and test known-allowed and known-denied manifests. Record policy version, user/service account, object, decision, exception behavior, and a regression case after policy changes.

### 8. RAG and AI-code review lab

Build a synthetic RAG corpus and a small AI-assisted code change. Test tenant filtering, untrusted document instructions, source provenance, dependency verification, authorization, and negative tests while ensuring tools have only lab-scoped permissions.

## Engineering focus

For this module, convert each important claim into a security invariant and a regression test. Prefer controls that remove unnecessary authority, make state transitions explicit, bound resource use, and leave enough telemetry to explain a failure. The reusable evidence and lab-record format is in [Study Method](../Guides/STUDY-METHOD.md).

## Authorized lab sequence

### Lab 1 — Complete one systems lab using sanitizers or race detection on code you own.



### Lab 2 — Complete one identity lab using synthetic SAML/SCIM/WebAuthn data and explicit validation rules.



### Lab 3 — Complete one cloud/AI architecture lab with policy matrices, telemetry plan and a retest checklist.

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

Recommended related modules: **027, 045, 085, 110, 115, 116, 117, 124, 128, 131, 135, 138, 139**. From the main menu, choose **Search lessons** to find related sections across the full guide.
