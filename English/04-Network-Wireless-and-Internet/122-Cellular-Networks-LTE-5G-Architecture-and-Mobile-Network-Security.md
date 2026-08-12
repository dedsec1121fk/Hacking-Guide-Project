# Cellular Networks, LTE/5G Architecture and Mobile Network Security

Understand cellular security as a layered identity, radio, transport and core-network problem. The focus is architecture, privacy, trust and defensive analysis—not interception of third-party traffic.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, captures, or lab environments you own or are explicitly authorized to test. Prefer localhost, synthetic data, disposable VMs/containers, prerecorded traces, and read-only analysis whenever possible.

## Learning objectives

By the end of this module you should be able to:

- Explain **UE, SIM/eSIM and subscriber identity** and identify its most important trust boundary, state transition, and evidence source.
- Explain **RAN, core network and control/user planes** and identify its most important trust boundary, state transition, and evidence source.
- Explain **LTE EPC and 5G Core concepts** and identify its most important trust boundary, state transition, and evidence source.
- Explain **AKA authentication families** and identify its most important trust boundary, state transition, and evidence source.
- Explain **temporary identifiers and privacy** and identify its most important trust boundary, state transition, and evidence source.
- Explain **roaming and inter-operator trust** and identify its most important trust boundary, state transition, and evidence source.

## Analysis method

Use [Study Method](../Guides/STUDY-METHOD.md). Start by identifying ownership or identity, the state transition that can fail, and the evidence that would distinguish a real boundary violation from a diagnostic artifact.

## Deep concepts

### 1. UE, SIM/eSIM and subscriber identity

Cellular security begins with the user equipment and subscription credentials held by SIM/eSIM infrastructure. Separate device identity, subscription identity, phone number, and application identity; they have different owners and are not interchangeable authentication factors.

### 2. RAN, core, control and user planes

The radio access network connects devices to a core network that separates signaling/control functions from user data forwarding. Threat modeling should identify which interfaces carry subscriber state, routing decisions, authentication context, and application traffic.

### 3. LTE EPC and 5G Core

LTE EPC and 5G Core use different service architecture and function boundaries, but both depend on authenticated subscriber state and tightly controlled inter-function communication. Inventory exposed service interfaces and administrative APIs rather than reasoning only about radio encryption.

### 4. AKA families

Authentication and Key Agreement protocols derive session keys from subscription secrets without transmitting the long-term secret directly. Security review should focus on identity binding, freshness, network authentication, key separation, and correct failure handling.

### 5. temporary identifiers and privacy

Temporary identifiers reduce repeated exposure of long-lived subscriber identity over radio interfaces. Privacy analysis should still consider paging, timing, mobility metadata, application identifiers, and operational logs that can correlate a device over time.

### 6. roaming and inter-operator trust

Roaming extends trust across providers and signaling/interconnect boundaries. Apply explicit peer policy, message validation, least privilege, monitoring, and contractual/security controls because compromise of a partner path can affect subscribers outside one administrative domain.

### 7. network slicing and service exposure

5G slicing and service-based interfaces create logical segmentation and APIs that require strong identity and authorization. A slice label alone is not a security boundary; verify isolation in policy, routing, resource allocation, and telemetry.

### 8. baseband isolation and telemetry

Baseband processors handle complex untrusted radio protocols and are intentionally isolated from application processors. Device security benefits from hardware/OS boundaries, firmware updates, crash telemetry, and minimizing the authority that radio components have over higher-level data.

## Engineering focus

For this module, convert each important claim into a security invariant and a regression test. Prefer controls that remove unnecessary authority, make state transitions explicit, bound resource use, and leave enough telemetry to explain a failure. The reusable evidence and lab-record format is in [Study Method](../Guides/STUDY-METHOD.md).

## Authorized lab sequence

### Lab 1 — Draw a 5G connection-flow diagram from device to application service using public standards diagrams.



### Lab 2 — Threat-model a fictional roaming scenario and list which parties must trust which assertions.



### Lab 3 — Compare Wi-Fi and cellular identity/privacy assumptions without capturing any third-party radio traffic.

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

Recommended related modules: **016, 017, 051, 055, 056, 123**. From the main menu, choose **Search lessons** to find related sections across the full guide.
