# Post-Quantum Migration, Crypto Agility and Hybrid Deployment

Post-quantum security is now an engineering migration problem. NIST has standardized ML-KEM, ML-DSA, and SLH-DSA and urges organizations to begin migration planning. This module focuses on discovery, dependency mapping, protocol readiness, testing, and long-lived data risk.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, or lab environments you own or are explicitly authorized to test. The exercises in this module are designed to prove security properties without targeting third parties.

## Learning objectives

By the end of this module you should be able to:

- Explain **Cryptographic inventory** and connect it to a concrete trust boundary or security invariant.
- Explain **Harvest-now risk** and connect it to a concrete trust boundary or security invariant.
- Explain **Standards** and connect it to a concrete trust boundary or security invariant.
- Explain **Crypto agility** and connect it to a concrete trust boundary or security invariant.
- Explain **Hybrid approaches** and connect it to a concrete trust boundary or security invariant.
- Explain **PKI impact** and connect it to a concrete trust boundary or security invariant.

## Analysis method

Use the shared [Study Method](../Guides/STUDY-METHOD.md). For this module, first draw the relevant components and state transitions, then state one security invariant and identify the minimum evidence needed to test it safely.

## Deep concepts

### 1. Cryptographic inventory

Find where public-key cryptography is used: TLS, VPNs, SSH, code signing, certificates, document signatures, device identity, firmware, backups, HSMs, libraries, protocols, and third-party services.



### 2. Harvest-now risk

Data with long confidentiality lifetimes may need earlier protection because captured ciphertext could be stored and attacked later. Prioritize based on sensitivity and required secrecy duration rather than hype.



### 3. Standards

FIPS 203 standardizes ML-KEM; FIPS 204 ML-DSA; FIPS 205 SLH-DSA. Migration decisions must also consider protocol profiles, ecosystem support, certification, performance, and interoperability.



### 4. Crypto agility

Applications should avoid hard-coded assumptions about key size, signature size, certificate shape, or one algorithm. Build explicit algorithm identifiers, versioning, test coverage, and policy controls.



### 5. Hybrid approaches

Some deployments combine classical and post-quantum mechanisms during transition. Security depends on how secrets/signatures are combined and whether the surrounding protocol specifies the hybrid construction correctly.



### 6. PKI impact

Larger keys/signatures can affect certificate chains, handshake sizes, embedded storage, MTU-sensitive protocols, HSM support, and constrained devices. Measure rather than assume compatibility.



### 7. Migration sequencing

Inventory → classify data/uses → identify dependencies → test libraries/protocols → prioritize high-value use cases → deploy with rollback → monitor interoperability → retire quantum-vulnerable use when policy requires.



### 8. Evidence

Track algorithm, key size/type, owner, library/provider, protocol, certificate profile, data lifetime, replacement plan, test status, and deprecation date. A spreadsheet without system ownership is not an actionable inventory.



## Review focus

Apply the failure-mode taxonomy in [Study Method](../Guides/STUDY-METHOD.md), but keep the analysis specific to this lesson: identify the principal, resource, authority, mutable state, parser or policy boundary, and the telemetry that would distinguish a real control failure from misconfiguration or an observation gap.

## Authorized exercises

### Exercise 1 — Build a cryptographic inventory for a small local application and record every library/API that creates or validates keys/signatures

Build a cryptographic inventory for a small local application and record every library/API that creates or validates keys/signatures.


### Exercise 2 — Create a compatibility test plan that anticipates larger key/signature objects and handshake messages without claiming unsupported algorithms are production-ready

Create a compatibility test plan that anticipates larger key/signature objects and handshake messages without claiming unsupported algorithms are production-ready.


### Exercise 3 — Classify sample data sets by confidentiality lifetime and use that to rank migration priority

Classify sample data sets by confidentiality lifetime and use that to rank migration priority.

Use the lab-record format in [Study Method](../Guides/STUDY-METHOD.md) for each exercise and keep all inputs synthetic or confined to the authorized lab.

## Knowledge checks

1. Explain the most important trust boundary in **Post-Quantum Migration, Crypto Agility and Hybrid Deployment** without naming a security tool.
2. Give one example where cryptographic or authentication success still does **not** imply authorization success.
3. Describe one stale-state or replay condition relevant to this module.
4. Identify one telemetry source that can support a strong conclusion and one blind spot it still leaves.
5. Explain how you would turn a discovered weakness into a regression test rather than a one-time finding.

## Guided study workflow

Use [Study Method](../Guides/STUDY-METHOD.md). Complete at least one authorized exercise, preserve the evidence that supports your conclusion, and explain the module's main trust boundary and failure modes in your own words before moving on.

### Continue with

Choose **Learning paths** from the main menu for an ordered specialization, or use **Search lessons** to follow a concept into related modules.
