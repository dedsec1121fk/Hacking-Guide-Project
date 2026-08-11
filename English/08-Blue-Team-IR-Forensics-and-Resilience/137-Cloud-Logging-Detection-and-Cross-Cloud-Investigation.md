# Cloud Logging, Detection and Cross-Cloud Investigation

Cloud investigations depend on control-plane and identity evidence distributed across services. Learn normalized event models, immutable collection, correlation, time, multi-account structure and investigation playbooks.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, captures, or lab environments you own or are explicitly authorized to test. Prefer localhost, synthetic data, disposable VMs/containers, prerecorded traces, and read-only analysis whenever possible.

## Learning objectives

By the end of this module you should be able to:

- Explain **control-plane audit logs** and identify its most important trust boundary, state transition, and evidence source.
- Explain **identity and token context** and identify its most important trust boundary, state transition, and evidence source.
- Explain **data-plane versus management-plane telemetry** and identify its most important trust boundary, state transition, and evidence source.
- Explain **multi-account/project/subscription aggregation** and identify its most important trust boundary, state transition, and evidence source.
- Explain **log integrity and retention** and identify its most important trust boundary, state transition, and evidence source.
- Explain **time synchronization and event ordering** and identify its most important trust boundary, state transition, and evidence source.

## Analysis method

Use [Study Method](../Guides/STUDY-METHOD.md). Start by identifying ownership or identity, the state transition that can fail, and the evidence that would distinguish a real boundary violation from a diagnostic artifact.

## Deep concepts

### 1. control-plane audit logs

Cloud audit logs record administrative/API actions such as identity, policy, networking, storage, and resource changes. Enable and centralize them before an incident; retroactive investigation is impossible for events the provider/account never retained.

### 2. identity and token context

A cloud event is meaningful only when caller identity, assumed role/service principal, session/token context, source, target resource, and organization/account/tenant are correlated. Normalize temporary identities back to their parent workload or human where possible.

### 3. data-plane versus management-plane logs

Management-plane logs describe configuration/control actions, while data-plane logs describe access to workloads or stored data. High-value investigations often require both because a policy change and subsequent data access happen in different telemetry systems.

### 4. central aggregation

Send logs to a security account/project or independent store with narrow write/admin permissions. Cross-account aggregation reduces the chance that compromise of one workload lets an attacker erase the only copy of its control-plane evidence.

### 5. integrity and retention

Use provider/object controls, immutability where appropriate, retention policy, export verification, and restricted deletion to preserve evidence. Retention should reflect incident-detection latency, legal/privacy requirements, and cost rather than a single arbitrary number.

### 6. time synchronization and ordering

Distributed cloud events may arrive late, use different timestamps, or represent server/client time differently. Preserve original timestamps and ingestion time, correlate with stable request/session IDs, and avoid assuming displayed order equals causal order.

### 7. cross-cloud normalization

AWS, Azure, GCP, SaaS, and identity providers use different names for principals, resources, actions, and outcomes. Normalize into a common investigation schema while preserving provider-specific raw fields so analysts can pivot without losing semantics.

### 8. investigation pivots and evidence preservation

Start from a known indicator—identity, resource, IP, request ID, key, or time window—and pivot across identity, control plane, workload, network, and data access. Export only necessary evidence, hash important artifacts, and document query/time-zone assumptions for reproducibility.

## Engineering focus

For this module, convert each important claim into a security invariant and a regression test. Prefer controls that remove unnecessary authority, make state transitions explicit, bound resource use, and leave enough telemetry to explain a failure. The reusable evidence and lab-record format is in [Study Method](../Guides/STUDY-METHOD.md).

## Authorized lab sequence

### Lab 1 — Create a synthetic multi-cloud event dataset and normalize five fields across three provider-style schemas.



### Lab 2 — Build an investigation timeline for a fictional policy change followed by unusual access and remediation.



### Lab 3 — Design retention tiers for high-value audit logs, noisy data-plane logs and forensic snapshots.

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

Recommended related modules: **019, 023, 037, 047, 059, 076, 080, 105, 106**. From the main menu, choose **Search lessons** to find related sections across the full guide.
