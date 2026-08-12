# AI-Generated Code, Vibe Coding and Secure Review

AI-assisted development increases speed but can amplify insecure assumptions. This module provides a disciplined review pipeline for generated code, dependencies, secrets, tests, threat models and deployment.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, captures, or lab environments you own or are explicitly authorized to test. Prefer localhost, synthetic data, disposable VMs/containers, prerecorded traces, and read-only analysis whenever possible.

## Learning objectives

By the end of this module you should be able to:

- Explain **generated-code trust model** and identify its most important trust boundary, state transition, and evidence source.
- Explain **specification before generation** and identify its most important trust boundary, state transition, and evidence source.
- Explain **dependency and package verification** and identify its most important trust boundary, state transition, and evidence source.
- Explain **secret handling and configuration** and identify its most important trust boundary, state transition, and evidence source.
- Explain **authentication/authorization review** and identify its most important trust boundary, state transition, and evidence source.
- Explain **input validation and unsafe parsing** and identify its most important trust boundary, state transition, and evidence source.

## Analysis method

Use [Study Method](../Guides/STUDY-METHOD.md). Start by identifying ownership or identity, the state transition that can fail, and the evidence that would distinguish a real boundary violation from a diagnostic artifact.

## Deep concepts

### 1. AI-generated code trust model

Treat generated code like code from an untrusted external contributor: it may be plausible, incomplete, outdated, insecure, or reference nonexistent APIs. Human ownership, repository review, automated tests, and security controls remain responsible for the final behavior.

### 2. specification before generation

Write security invariants, data types, trust boundaries, error behavior, and non-functional constraints before asking a model to implement code. A precise specification lets reviewers test correctness instead of accepting whichever architecture the generator happened to choose.

### 3. dependency and package verification

Models can suggest stale, wrong, typo-squatted, or nonexistent packages. Verify package identity from the official ecosystem, pin/lock appropriate versions, review transitive dependencies, and never install a dependency solely because generated instructions mention it.

### 4. secrets and configuration

Generated examples often contain placeholder tokens, permissive debug settings, broad CORS, weak defaults, or secrets loaded incorrectly. Keep secrets out of prompts/source, use environment/secret managers appropriately, and review production configuration separately from demo code.

### 5. authentication and authorization review

Generated handlers can check that a user is logged in while omitting object- or tenant-level authorization. Review every sensitive operation for subject, resource, action, tenant, and privilege context, and write negative tests with multiple synthetic identities.

### 6. input validation and parsing

Models frequently generate happy-path parsers with weak bounds or ambiguous error handling. Define schemas, size/depth limits, canonicalization, safe deserialization, and output encoding according to the actual sink and protocol.

### 7. generated tests and false confidence

AI-generated tests can reproduce the same incorrect assumption as generated implementation code. Include adversarial/negative cases derived independently from the specification and measure whether tests fail when the security control is deliberately broken in a toy branch.

### 8. human review, provenance and change control

Record which code was generated or heavily assisted when policy requires it, but judge the resulting artifact by normal engineering evidence. Protected branches, code review, CI, provenance, dependency scanning, secrets scanning, and rollback should apply regardless of authorship.

## Engineering focus

For this module, convert each important claim into a security invariant and a regression test. Prefer controls that remove unnecessary authority, make state transitions explicit, bound resource use, and leave enough telemetry to explain a failure. The reusable evidence and lab-record format is in [Study Method](../Guides/STUDY-METHOD.md).

## Authorized lab sequence

### Lab 1 — Take a small local script you own and build a security-review checklist covering inputs, files, subprocesses, network, secrets and dependencies.



### Lab 2 — Write five negative tests for a generated login/API example using fictional data.



### Lab 3 — Compare two AI-generated designs for the same feature and choose the one with smaller authority and fewer dependencies, documenting why.

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

Recommended related modules: **022, 025, 036, 040, 041, 046, 097, 098, 108, 109**. From the main menu, choose **Search lessons** to find related sections across the full guide.
