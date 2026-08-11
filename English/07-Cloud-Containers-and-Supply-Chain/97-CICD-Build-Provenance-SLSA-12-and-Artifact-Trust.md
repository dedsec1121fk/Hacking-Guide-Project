# CI/CD, Build Provenance, SLSA 1.2 and Artifact Trust

Software supply-chain security is about proving how source becomes an artifact and reducing opportunities for unauthorized modification. SLSA 1.2 separates tracks and emphasizes provenance and source/build controls. This module connects repository governance, builders, attestations, signing, and deployment verification.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, or lab environments you own or are explicitly authorized to test. The exercises in this module are designed to prove security properties without targeting third parties.

## Learning objectives

By the end of this module you should be able to:

- Explain **Source control trust** and connect it to a concrete trust boundary or security invariant.
- Explain **Build isolation** and connect it to a concrete trust boundary or security invariant.
- Explain **Provenance** and connect it to a concrete trust boundary or security invariant.
- Explain **SLSA 1.2** and connect it to a concrete trust boundary or security invariant.
- Explain **Artifact signing** and connect it to a concrete trust boundary or security invariant.
- Explain **Promotion** and connect it to a concrete trust boundary or security invariant.

## Analysis method

Use the shared [Study Method](../Guides/STUDY-METHOD.md). For this module, first draw the relevant components and state transitions, then state one security invariant and identify the minimum evidence needed to test it safely.

## Deep concepts

### 1. Source control trust

Branch protection, review, protected tags, signed changes where appropriate, repository administration, and account recovery define who can alter source and release metadata.



### 2. Build isolation

A trusted build should have controlled inputs, ephemeral or well-managed execution, explicit dependencies, and limited credentials. Long-lived mutable runners create hidden state and increase cross-build risk.



### 3. Provenance

Provenance records who/what built an artifact, from which source and dependencies, under which process. It supports verification but only if the builder and attestation signing path are trustworthy.



### 4. SLSA 1.2

SLSA 1.2 is the current specification and includes Build and Source tracks. Use levels/requirements as a structured improvement path rather than a marketing badge.



### 5. Artifact signing

Signatures bind an identity/key to an artifact digest. Verification policy must define which identities are trusted, what provenance is required, and what happens when verification cannot be completed.



### 6. Promotion

Promote the same immutable artifact between environments instead of rebuilding from source independently for staging and production. This narrows the number of build events that can affect production.



### 7. Secrets in CI

CI tokens often have broad repository, cloud, registry, and signing privileges. Prefer short-lived workload identity, environment protection, minimal scopes, and explicit approval for high-impact stages.



### 8. Verification at deploy

Deployment systems should verify digest, expected source/ref, builder identity, provenance policy, vulnerability policy where appropriate, and environment authorization before rollout.



## Review focus

Apply the failure-mode taxonomy in [Study Method](../Guides/STUDY-METHOD.md), but keep the analysis specific to this lesson: identify the principal, resource, authority, mutable state, parser or policy boundary, and the telemetry that would distinguish a real control failure from misconfiguration or an observation gap.

## Authorized exercises

### Exercise 1 — Draw the source→build→registry→deployment chain for a small project and mark every identity that can change the final artifact

Draw the source→build→registry→deployment chain for a small project and mark every identity that can change the final artifact.


### Exercise 2 — Generate a harmless local artifact and a JSON provenance record containing source hash, builder, timestamp, and output digest; verify consistency with a Python script

Generate a harmless local artifact and a JSON provenance record containing source hash, builder, timestamp, and output digest; verify consistency with a Python script.


### Exercise 3 — Create a CI hardening checklist that distinguishes source-track controls from build-track controls

Create a CI hardening checklist that distinguishes source-track controls from build-track controls.

Use the lab-record format in [Study Method](../Guides/STUDY-METHOD.md) for each exercise and keep all inputs synthetic or confined to the authorized lab.

## Knowledge checks

1. Explain the most important trust boundary in **CI/CD, Build Provenance, SLSA 1.2 and Artifact Trust** without naming a security tool.
2. Give one example where cryptographic or authentication success still does **not** imply authorization success.
3. Describe one stale-state or replay condition relevant to this module.
4. Identify one telemetry source that can support a strong conclusion and one blind spot it still leaves.
5. Explain how you would turn a discovered weakness into a regression test rather than a one-time finding.

## Guided study workflow

Use [Study Method](../Guides/STUDY-METHOD.md). Complete at least one authorized exercise, preserve the evidence that supports your conclusion, and explain the module's main trust boundary and failure modes in your own words before moving on.

### Continue with

Choose **Learning paths** from the main menu for an ordered specialization, or use **Search lessons** to follow a concept into related modules.
