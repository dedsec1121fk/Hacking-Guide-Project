# Kubernetes Admission Control, Policy-as-Code and Runtime Guardrails

Deepen Kubernetes security by focusing on the control path between an API request and a running workload: admission, mutation, validation, pod-security controls, policy engines and runtime drift.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, captures, or lab environments you own or are explicitly authorized to test. Prefer localhost, synthetic data, disposable VMs/containers, prerecorded traces, and read-only analysis whenever possible.

## Learning objectives

By the end of this module you should be able to:

- Explain **API admission lifecycle** and identify its most important trust boundary, state transition, and evidence source.
- Explain **mutating versus validating admission** and identify its most important trust boundary, state transition, and evidence source.
- Explain **Pod Security Standards concepts** and identify its most important trust boundary, state transition, and evidence source.
- Explain **policy-as-code engines** and identify its most important trust boundary, state transition, and evidence source.
- Explain **image provenance and allowlists** and identify its most important trust boundary, state transition, and evidence source.
- Explain **namespace and service-account context** and identify its most important trust boundary, state transition, and evidence source.

## Analysis method

Use [Study Method](../Guides/STUDY-METHOD.md). Start by identifying ownership or identity, the state transition that can fail, and the evidence that would distinguish a real boundary violation from a diagnostic artifact.

## Deep concepts

### 1. admission lifecycle

Kubernetes admission runs after authentication/authorization but before an API object is persisted. It is a policy enforcement point for resource configuration, not a replacement for runtime isolation, RBAC, image security, or continuous drift detection.

### 2. mutating versus validating admission

Mutating admission can add/default fields before validation; validating admission accepts or rejects the resulting object. Keep mutations predictable and observable because hidden changes make policy reasoning, debugging, and signed-manifest expectations harder.

### 3. Pod Security Standards

Pod Security Standards define baseline/restricted expectations for risky pod settings such as privilege, host namespaces, capabilities, volume types, and seccomp. Apply profiles according to workload need and manage narrow exceptions explicitly.

### 4. policy engines

Admission policy engines evaluate manifests against organization-specific rules. Version policies as code, test allow/deny cases in CI, use clear messages, scope rules carefully, and monitor exceptions so a temporary bypass does not become permanent architecture.

### 5. image provenance and allowlists

Admission can restrict registries, digests, signatures/attestations, or provenance according to deployment policy. Prefer immutable digests and verified provenance for high-assurance workloads rather than trusting a mutable image tag alone.

### 6. namespace and service-account context

The same manifest can have different risk depending on namespace labels, service account, secrets, network policy, quotas, and target environment. Admission decisions should include the context that actually determines workload authority.

### 7. runtime drift

Admission checks desired objects at creation/update time, but containers, nodes, credentials, external services, or manually changed infrastructure can drift afterward. Combine admission with runtime telemetry, configuration reconciliation, and periodic policy checks.

### 8. telemetry and exceptions

Record policy/version, object, namespace, user/service account, decision, violated rule, and exception identity. Exception workflows should require owner, reason, scope, and expiry, with dashboards showing which high-risk workloads are outside normal policy.

## Engineering focus

For this module, convert each important claim into a security invariant and a regression test. Prefer controls that remove unnecessary authority, make state transitions explicit, bound resource use, and leave enough telemetry to explain a failure. The reusable evidence and lab-record format is in [Study Method](../Guides/STUDY-METHOD.md).

## Authorized lab sequence

### Lab 1 — Write policy requirements for a toy Kubernetes manifest: non-root, restricted capabilities, approved image source and resource limits.



### Lab 2 — Compare admission-time and runtime evidence for the same fictional workload.



### Lab 3 — Create an exception record with owner, reason, expiry and compensating control, then define an automated review trigger.

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

Recommended related modules: **024, 041, 075, 093, 097, 113**. From the main menu, choose **Search lessons** to find related sections across the full guide.
