# Virtualization, Hypervisors, Virtual Machines and Confidential Computing

Virtualization creates strong but not absolute boundaries. This module explains hypervisor architecture, virtual devices, management planes, snapshots, host integration, nested virtualization, and confidential-computing concepts from a defensive research perspective.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, or lab environments you own or are explicitly authorized to test. The exercises in this module are designed to prove security properties without targeting third parties.

## Learning objectives

By the end of this module you should be able to:

- Explain **Hypervisor models** and connect it to a concrete trust boundary or security invariant.
- Explain **Hardware virtualization** and connect it to a concrete trust boundary or security invariant.
- Explain **Virtual devices** and connect it to a concrete trust boundary or security invariant.
- Explain **Snapshots and images** and connect it to a concrete trust boundary or security invariant.
- Explain **Management plane** and connect it to a concrete trust boundary or security invariant.
- Explain **Nested virtualization** and connect it to a concrete trust boundary or security invariant.

## Analysis method

Use the shared [Study Method](../Guides/STUDY-METHOD.md). For this module, first draw the relevant components and state transitions, then state one security invariant and identify the minimum evidence needed to test it safely.

## Deep concepts

### 1. Hypervisor models

Type-1 and hosted hypervisors differ in deployment architecture, but both mediate CPU, memory, interrupts, and devices. The management plane and device-emulation surface are often as important as the core scheduler.



### 2. Hardware virtualization

CPU extensions and second-level address translation allow guest execution while retaining host control over privileged operations and memory mappings. Security analysis should distinguish guest virtual, guest physical, and host physical addresses.



### 3. Virtual devices

Network cards, storage controllers, graphics, USB, shared folders, clipboard, and guest agents expand the interface between guest and host. Disable integration features that are unnecessary for the workload.



### 4. Snapshots and images

VM images and snapshots can contain credentials, encryption keys, tokens, memory-resident secrets, and stale software. Treat them as sensitive artifacts with lifecycle controls.



### 5. Management plane

Hypervisor APIs, consoles, orchestration, templates, and backup systems can control many guests at once. Strong MFA, dedicated administration paths, logging, and separation of duties are essential.



### 6. Nested virtualization

Nested guests add more layers and make performance/security assumptions harder to reason about. Document which layer owns each security feature rather than assuming the inner guest can enforce host-level guarantees.



### 7. Confidential computing

Hardware-backed confidential VMs/TEEs aim to protect workload memory from parts of the host stack. Attestation and key-release policy become central; side channels, availability, and trusted I/O remain separate concerns.



### 8. Boundary verification

A good test plan checks device exposure, guest-agent privileges, network isolation, image provenance, snapshot handling, time synchronization, logging, and management-plane authorization without attempting host escape.



## Review focus

Apply the failure-mode taxonomy in [Study Method](../Guides/STUDY-METHOD.md), but keep the analysis specific to this lesson: identify the principal, resource, authority, mutable state, parser or policy boundary, and the telemetry that would distinguish a real control failure from misconfiguration or an observation gap.

## Authorized exercises

### Exercise 1 — Build a local VM threat model listing every host/guest integration feature and justify whether it is required

Build a local VM threat model listing every host/guest integration feature and justify whether it is required.


### Exercise 2 — Take a disposable VM snapshot with non-sensitive test data and document what security-sensitive state a real snapshot could preserve

Take a disposable VM snapshot with non-sensitive test data and document what security-sensitive state a real snapshot could preserve.


### Exercise 3 — Compare the trust assumptions of a normal VM, container, and confidential VM in a one-page matrix

Compare the trust assumptions of a normal VM, container, and confidential VM in a one-page matrix.

Use the lab-record format in [Study Method](../Guides/STUDY-METHOD.md) for each exercise and keep all inputs synthetic or confined to the authorized lab.

## Knowledge checks

1. Explain the most important trust boundary in **Virtualization, Hypervisors, Virtual Machines and Confidential Computing** without naming a security tool.
2. Give one example where cryptographic or authentication success still does **not** imply authorization success.
3. Describe one stale-state or replay condition relevant to this module.
4. Identify one telemetry source that can support a strong conclusion and one blind spot it still leaves.
5. Explain how you would turn a discovered weakness into a regression test rather than a one-time finding.

## Guided study workflow

Use [Study Method](../Guides/STUDY-METHOD.md). Complete at least one authorized exercise, preserve the evidence that supports your conclusion, and explain the module's main trust boundary and failure modes in your own words before moving on.

### Continue with

Choose **Learning paths** from the main menu for an ordered specialization, or use **Search lessons** to follow a concept into related modules.
