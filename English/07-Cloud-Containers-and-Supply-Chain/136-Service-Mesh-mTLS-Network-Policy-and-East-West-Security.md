# Service Mesh, mTLS, Network Policy and East-West Security

Service-to-service traffic needs explicit identity and policy. Study sidecar/ambient models, mTLS, workload identity, network policy, authorization, observability and failure handling.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, captures, or lab environments you own or are explicitly authorized to test. Prefer localhost, synthetic data, disposable VMs/containers, prerecorded traces, and read-only analysis whenever possible.

## Learning objectives

By the end of this module you should be able to:

- Explain **east-west versus north-south traffic** and identify its most important trust boundary, state transition, and evidence source.
- Explain **service mesh data/control planes** and identify its most important trust boundary, state transition, and evidence source.
- Explain **mTLS identity establishment** and identify its most important trust boundary, state transition, and evidence source.
- Explain **service authorization policy** and identify its most important trust boundary, state transition, and evidence source.
- Explain **Kubernetes NetworkPolicy concepts** and identify its most important trust boundary, state transition, and evidence source.
- Explain **sidecar versus ambient interception** and identify its most important trust boundary, state transition, and evidence source.

## Analysis method

Use [Study Method](../Guides/STUDY-METHOD.md). Start by identifying ownership or identity, the state transition that can fail, and the evidence that would distinguish a real boundary violation from a diagnostic artifact.

## Deep concepts

### 1. east-west versus north-south traffic

North-south controls protect entry/exit paths, while east-west policy governs service-to-service communication inside an environment. Microservices should not inherit broad mutual trust merely because workloads share a cluster or private network.

### 2. data plane and control plane

A service mesh data plane handles workload traffic while the control plane distributes identity, routing, certificate, and policy state. Protect control-plane administration strongly because a policy or trust-bundle change can influence many services simultaneously.

### 3. mTLS workload identity

Mutual TLS can authenticate both workloads and encrypt traffic, but authorization must still decide which identity may call which service/action. Validate certificate/trust-domain mapping and avoid treating successful TLS as permission to access every endpoint.

### 4. service authorization policy

Service policy should express source workload identity, destination, operation/path where relevant, and environment/tenant context. Default-deny plus explicit grants is easier to audit than implicit connectivity derived from network location.

### 5. Kubernetes NetworkPolicy

NetworkPolicy constrains network reachability at the Kubernetes networking layer and complements, rather than duplicates, identity-aware mesh policy. Confirm CNI support, namespace/pod selectors, egress paths, DNS needs, and default behavior with safe connectivity tests.

### 6. sidecar versus ambient models

Sidecar and ambient mesh designs place enforcement/telemetry components differently. Threat models should identify which process/node component can observe or influence traffic and what happens when that component is unavailable, bypassed, or misconfigured.

### 7. certificate rotation and trust bundles

Short-lived workload certificates reduce long-term credential exposure but require dependable issuance, clock, rotation, and trust-bundle rollout. Test overlap and failure behavior so a CA/key transition does not create either a broad trust window or service outage.

### 8. telemetry and failure behavior

Mesh telemetry should connect source/destination workload identity, policy decision, protocol, request outcome, and certificate context. Define whether policy/control-plane failures fail closed or degrade, and make that behavior visible during incident response.

## Engineering focus

For this module, convert each important claim into a security invariant and a regression test. Prefer controls that remove unnecessary authority, make state transitions explicit, bound resource use, and leave enough telemetry to explain a failure. The reusable evidence and lab-record format is in [Study Method](../Guides/STUDY-METHOD.md).

## Authorized lab sequence

### Lab 1 — Draw a three-service architecture and write both network reachability and identity authorization matrices.



### Lab 2 — Model certificate rotation with overlapping trust bundles and define how stale workloads recover.



### Lab 3 — Compare a direct call, sidecar-proxied call and ambient-mesh call in terms of trust boundaries and telemetry.

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

Recommended related modules: **021, 024, 075, 093, 113, 135**. From the main menu, choose **Search lessons** to find related sections across the full guide.
