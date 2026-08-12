# Workload Identity, SPIFFE/SPIRE, mTLS and Zero-Trust Service Identity

Modern infrastructure increasingly replaces static service passwords with short-lived workload identities. This module explains identity issuance, attestation, trust domains, certificate/token rotation, service-to-service policy, and failure modes.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, or lab environments you own or are explicitly authorized to test. The exercises in this module are designed to prove security properties without targeting third parties.

## Learning objectives

By the end of this module you should be able to:

- Explain **Workload identity** and connect it to a concrete trust boundary or security invariant.
- Explain **SPIFFE IDs** and connect it to a concrete trust boundary or security invariant.
- Explain **Attestation** and connect it to a concrete trust boundary or security invariant.
- Explain **Short-lived credentials** and connect it to a concrete trust boundary or security invariant.
- Explain **mTLS** and connect it to a concrete trust boundary or security invariant.
- Explain **Trust domains** and connect it to a concrete trust boundary or security invariant.

## Analysis method

Use the shared [Study Method](../Guides/STUDY-METHOD.md). For this module, first draw the relevant components and state transitions, then state one security invariant and identify the minimum evidence needed to test it safely.

## Deep concepts

### 1. Workload identity

A workload identity represents a running service/process instance rather than a human. It should be derived from trusted workload/platform attributes and have a lifecycle aligned with the workload.



### 2. SPIFFE IDs

SPIFFE defines identity names within trust domains. The ID is an identifier, not authorization itself; policy decides what that identity may access.



### 3. Attestation

Identity issuance depends on node/workload attestation. The issuer needs trustworthy signals about where and what is running before minting credentials.



### 4. Short-lived credentials

Short-lived X.509 SVIDs or JWT-style credentials reduce dependence on manual secret rotation. Availability and clock/time correctness become important operational dependencies.



### 5. mTLS

Mutual TLS can authenticate both ends of a connection. Authorization still needs service/resource context, and certificate trust must be scoped so unrelated trust domains are not accepted accidentally.



### 6. Trust domains

Federating trust domains creates explicit cross-domain identity relationships. Keep mappings narrow and avoid translating broad external identities into powerful local ones.



### 7. Rotation and revocation

Short lifetimes can reduce the need for immediate revocation but do not eliminate emergency response. Plan issuer/key rotation, trust-bundle updates, compromised-node handling, and stale workload cleanup.



### 8. Policy and telemetry

Log workload identity, destination service, authorization decision, policy version, and certificate/token metadata without storing private keys. This makes service-to-service authority paths auditable.



## Review focus

Apply the failure-mode taxonomy in [Study Method](../Guides/STUDY-METHOD.md), but keep the analysis specific to this lesson: identify the principal, resource, authority, mutable state, parser or policy boundary, and the telemetry that would distinguish a real control failure from misconfiguration or an observation gap.

## Authorized exercises

### Exercise 1 — Design a three-service toy architecture using short-lived workload identities and write an allow matrix for service-to-service calls

Design a three-service toy architecture using short-lived workload identities and write an allow matrix for service-to-service calls.


### Exercise 2 — Model what changes when one node is considered untrusted: which credentials expire, what should be denied, and what evidence is needed

Model what changes when one node is considered untrusted: which credentials expire, what should be denied, and what evidence is needed.


### Exercise 3 — Compare static API keys, cloud workload federation, and SPIFFE-style identities across rotation, attribution, and blast radius

Compare static API keys, cloud workload federation, and SPIFFE-style identities across rotation, attribution, and blast radius.

Use the lab-record format in [Study Method](../Guides/STUDY-METHOD.md) for each exercise and keep all inputs synthetic or confined to the authorized lab.

## Knowledge checks

1. Explain the most important trust boundary in **Workload Identity, SPIFFE/SPIRE, mTLS and Zero-Trust Service Identity** without naming a security tool.
2. Give one example where cryptographic or authentication success still does **not** imply authorization success.
3. Describe one stale-state or replay condition relevant to this module.
4. Identify one telemetry source that can support a strong conclusion and one blind spot it still leaves.
5. Explain how you would turn a discovered weakness into a regression test rather than a one-time finding.

## Guided study workflow

Use [Study Method](../Guides/STUDY-METHOD.md). Complete at least one authorized exercise, preserve the evidence that supports your conclusion, and explain the module's main trust boundary and failure modes in your own words before moving on.

### Continue with

Choose **Learning paths** from the main menu for an ordered specialization, or use **Search lessons** to follow a concept into related modules.
