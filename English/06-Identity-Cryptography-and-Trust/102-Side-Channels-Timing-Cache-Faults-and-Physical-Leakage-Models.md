# Side Channels, Timing, Cache, Faults and Physical Leakage Models

Security can fail through information that escapes outside the intended logical interface: timing, cache state, power, electromagnetic behavior, memory access patterns, shared resources, or injected faults. This module teaches the models and mitigations using safe local experiments.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, or lab environments you own or are explicitly authorized to test. The exercises in this module are designed to prove security properties without targeting third parties.

## Learning objectives

By the end of this module you should be able to:

- Explain **Side-channel model** and connect it to a concrete trust boundary or security invariant.
- Explain **Timing** and connect it to a concrete trust boundary or security invariant.
- Explain **Caches and microarchitecture** and connect it to a concrete trust boundary or security invariant.
- Explain **Power and EM** and connect it to a concrete trust boundary or security invariant.
- Explain **Fault injection** and connect it to a concrete trust boundary or security invariant.
- Explain **Remote vs local feasibility** and connect it to a concrete trust boundary or security invariant.

## Analysis method

Use the shared [Study Method](../Guides/STUDY-METHOD.md). For this module, first draw the relevant components and state transitions, then state one security invariant and identify the minimum evidence needed to test it safely.

## Deep concepts

### 1. Side-channel model

A side channel is an observable correlated with secret-dependent computation. Define attacker proximity, measurement capability, shared resources, number of observations, and noise before judging feasibility.



### 2. Timing

Secret-dependent branches, early exits, variable-time arithmetic, database lookups, network jitter, and rate limiting can all affect timing. Constant-time cryptographic code aims to remove secret-dependent timing at the implementation level.



### 3. Caches and microarchitecture

Shared caches, branch predictors, speculative execution, memory deduplication, and execution units can create cross-context observations. Platform mitigations often trade performance and depend on hardware/OS scheduling.



### 4. Power and EM

Embedded devices can leak information through power consumption or electromagnetic emissions. Countermeasures include constant-pattern implementations, masking, filtering, secure hardware, and limiting physical access.



### 5. Fault injection

Voltage, clock, electromagnetic, laser, or software-induced faults can alter computation. Secure designs validate critical state, use redundancy where justified, and avoid treating one successful computation as unquestionable.



### 6. Remote vs local feasibility

A signal measurable with physical access may disappear over a network; conversely application-level timing can remain remotely visible when amplified. Threat models must state measurement distance and noise.



### 7. Mitigation layers

Constant-time libraries, isolation, scheduler/core policy, hardware mitigations, removal of secret-dependent behavior, blinding/masking, rate limits, and physical protections address different channels.



### 8. Validation

Use statistical experiments on toy code and public benchmark methods. Avoid experiments that target third-party co-tenants or systems you do not own.



## Review focus

Apply the failure-mode taxonomy in [Study Method](../Guides/STUDY-METHOD.md), but keep the analysis specific to this lesson: identify the principal, resource, authority, mutable state, parser or policy boundary, and the telemetry that would distinguish a real control failure from misconfiguration or an observation gap.

## Authorized exercises

### Exercise 1 — Write two localhost toy string-comparison functions—one early-exit and one constant-work—and measure timing distributions using random non-secret data

Write two localhost toy string-comparison functions—one early-exit and one constant-work—and measure timing distributions using random non-secret data.


### Exercise 2 — Create a threat model for a cryptographic operation in a cloud VM versus an embedded device with physical attacker access

Create a threat model for a cryptographic operation in a cloud VM versus an embedded device with physical attacker access.


### Exercise 3 — Document which side-channel mitigations belong to application code, cryptographic library, OS/hypervisor, hardware, and physical security

Document which side-channel mitigations belong to application code, cryptographic library, OS/hypervisor, hardware, and physical security.

Use the lab-record format in [Study Method](../Guides/STUDY-METHOD.md) for each exercise and keep all inputs synthetic or confined to the authorized lab.

## Knowledge checks

1. Explain the most important trust boundary in **Side Channels, Timing, Cache, Faults and Physical Leakage Models** without naming a security tool.
2. Give one example where cryptographic or authentication success still does **not** imply authorization success.
3. Describe one stale-state or replay condition relevant to this module.
4. Identify one telemetry source that can support a strong conclusion and one blind spot it still leaves.
5. Explain how you would turn a discovered weakness into a regression test rather than a one-time finding.

## Guided study workflow

Use [Study Method](../Guides/STUDY-METHOD.md). Complete at least one authorized exercise, preserve the evidence that supports your conclusion, and explain the module's main trust boundary and failure modes in your own words before moving on.

### Continue with

Choose **Learning paths** from the main menu for an ordered specialization, or use **Search lessons** to follow a concept into related modules.
