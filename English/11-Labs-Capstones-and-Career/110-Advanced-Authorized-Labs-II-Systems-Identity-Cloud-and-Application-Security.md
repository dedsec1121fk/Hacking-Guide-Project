# Advanced Authorized Labs II: Systems, Identity, Cloud and Application Security

This lab module integrates the advanced lessons into bounded projects. Every exercise uses owned systems, disposable VMs/containers, localhost services, synthetic identities, or static/public artifacts. The goal is evidence and defensive understanding rather than gaining access.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, or lab environments you own or are explicitly authorized to test. The exercises in this module are designed to prove security properties without targeting third parties.

## Learning objectives

By the end of this module you should be able to:

- Explain **Lab architecture** and connect it to a concrete trust boundary or security invariant.
- Explain **Evidence package** and connect it to a concrete trust boundary or security invariant.
- Explain **Identity lab** and connect it to a concrete trust boundary or security invariant.
- Explain **Web/API lab** and connect it to a concrete trust boundary or security invariant.
- Explain **Linux isolation lab** and connect it to a concrete trust boundary or security invariant.
- Explain **Supply-chain lab** and connect it to a concrete trust boundary or security invariant.

## Analysis method

Use the shared [Study Method](../Guides/STUDY-METHOD.md). For this module, first draw the relevant components and state transitions, then state one security invariant and identify the minimum evidence needed to test it safely.

## Deep concepts

### 1. Lab architecture

Use snapshots, isolated networks, synthetic data, dedicated test identities, clear IP/domain allowlists, and a written objective before execution.



### 2. Evidence package

For each lab keep environment metadata, hypothesis, commands/configuration used, hashes, screenshots/log excerpts where useful, interpretation, cleanup, and regression result.



### 3. Identity lab

Build a toy identity graph with users, groups, roles, workload identities, and resource policies; detect an unintended privilege path and repair the policy.



### 4. Web/API lab

Create a localhost API with object-level authorization and deliberately add then fix one broken authorization test. Verify the fix with negative regression cases.



### 5. Linux isolation lab

Run a disposable service with reduced capabilities, filesystem permissions, and network exposure; compare before/after effective privilege.



### 6. Supply-chain lab

Create a source commit, local build artifact, SBOM-like dependency list, provenance record, and verification script that rejects an altered artifact digest.



### 7. Detection lab

Generate benign process/file/network events, verify telemetry, write a detection, tune one false positive, and retain a replay fixture.



### 8. Forensics lab

Build a synthetic incident timeline from prepared logs/files and produce a short evidence-based narrative with uncertainty explicitly marked.



## Review focus

Apply the failure-mode taxonomy in [Study Method](../Guides/STUDY-METHOD.md), but keep the analysis specific to this lesson: identify the principal, resource, authority, mutable state, parser or policy boundary, and the telemetry that would distinguish a real control failure from misconfiguration or an observation gap.

## Authorized exercises

### Exercise 1 — Complete any four integrated labs and produce one consistent report template across all of them

Complete any four integrated labs and produce one consistent report template across all of them.


### Exercise 2 — For one lab, intentionally remove a telemetry source and explain what conclusions are no longer supportable

For one lab, intentionally remove a telemetry source and explain what conclusions are no longer supportable.


### Exercise 3 — For one lab, change the environment version/configuration and verify whether the regression test still proves the same invariant

For one lab, change the environment version/configuration and verify whether the regression test still proves the same invariant.

Use the lab-record format in [Study Method](../Guides/STUDY-METHOD.md) for each exercise and keep all inputs synthetic or confined to the authorized lab.

## Knowledge checks

1. Explain the most important trust boundary in **Advanced Authorized Labs II: Systems, Identity, Cloud and Application Security** without naming a security tool.
2. Give one example where cryptographic or authentication success still does **not** imply authorization success.
3. Describe one stale-state or replay condition relevant to this module.
4. Identify one telemetry source that can support a strong conclusion and one blind spot it still leaves.
5. Explain how you would turn a discovered weakness into a regression test rather than a one-time finding.

## Guided study workflow

Use [Study Method](../Guides/STUDY-METHOD.md). Complete at least one authorized exercise, preserve the evidence that supports your conclusion, and explain the module's main trust boundary and failure modes in your own words before moving on.

### Continue with

Choose **Learning paths** from the main menu for an ordered specialization, or use **Search lessons** to follow a concept into related modules.
