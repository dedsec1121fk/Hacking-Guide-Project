# Authorization Models: RBAC, ABAC, ReBAC and Policy Engines

Authorization is the core question “may this principal perform this action on this resource under these conditions?” This module treats authorization as a graph/state problem and shows how models such as RBAC, ABAC, ReBAC, ACLs, and policy engines fail when context or lifecycle is incomplete.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, or lab environments you own or are explicitly authorized to test. The exercises in this module are designed to prove security properties without targeting third parties.

## Learning objectives

By the end of this module you should be able to:

- Explain **Reference monitor** and connect it to a concrete trust boundary or security invariant.
- Explain **RBAC** and connect it to a concrete trust boundary or security invariant.
- Explain **ABAC** and connect it to a concrete trust boundary or security invariant.
- Explain **ReBAC** and connect it to a concrete trust boundary or security invariant.
- Explain **Deny and default semantics** and connect it to a concrete trust boundary or security invariant.
- Explain **Caching** and connect it to a concrete trust boundary or security invariant.

## Analysis method

Use the shared [Study Method](../Guides/STUDY-METHOD.md). For this module, first draw the relevant components and state transitions, then state one security invariant and identify the minimum evidence needed to test it safely.

## Deep concepts

### 1. Reference monitor

A strong authorization design has a small, consistently invoked decision point, complete mediation, trustworthy inputs, and auditable policy. Scattered ad hoc checks tend to drift.



### 2. RBAC

Roles simplify permission management but can create role explosion and over-broad bundles. Separate business roles from technical implementation roles and review inherited privileges.



### 3. ABAC

Attribute-based decisions combine properties of users, resources, actions, and environment. The security problem shifts to attribute provenance, freshness, default behavior, and policy complexity.



### 4. ReBAC

Relationship-based models express ownership, membership, hierarchy, and sharing. Graph traversal rules must define direction, transitivity, cycles, revocation, and the maximum relationship depth considered.



### 5. Deny and default semantics

Policy engines differ in how they combine permits, denies, errors, and missing data. A safe design documents fail-open/fail-closed behavior for every dependency.



### 6. Caching

Authorization caches improve performance but create revocation windows. Cache keys must include all security-relevant context, and invalidation needs to be designed rather than hoped for.



### 7. Administrative authorization

Who may change policy is often more important than the policy language itself. Separate policy authorship, deployment, emergency override, and audit responsibilities.



### 8. Testing policy

Test positive, negative, boundary, stale-attribute, cross-tenant, inherited-role, revoked-access, and dependency-failure cases. Property-based tests can be useful for invariants such as “no user can read another tenant without an explicit relationship.”



## Review focus

Apply the failure-mode taxonomy in [Study Method](../Guides/STUDY-METHOD.md), but keep the analysis specific to this lesson: identify the principal, resource, authority, mutable state, parser or policy boundary, and the telemetry that would distinguish a real control failure from misconfiguration or an observation gap.

## Authorized exercises

### Exercise 1 — Model a file-sharing application using RBAC and then ReBAC; compare which rules become simpler and which new risks appear

Model a file-sharing application using RBAC and then ReBAC; compare which rules become simpler and which new risks appear.


### Exercise 2 — Write an authorization decision table with principal, action, resource, tenant, relationship, device posture, and time context

Write an authorization decision table with principal, action, resource, tenant, relationship, device posture, and time context.


### Exercise 3 — Create regression tests for revocation and stale-cache behavior in a toy policy evaluator

Create regression tests for revocation and stale-cache behavior in a toy policy evaluator.

Use the lab-record format in [Study Method](../Guides/STUDY-METHOD.md) for each exercise and keep all inputs synthetic or confined to the authorized lab.

## Knowledge checks

1. Explain the most important trust boundary in **Authorization Models: RBAC, ABAC, ReBAC and Policy Engines** without naming a security tool.
2. Give one example where cryptographic or authentication success still does **not** imply authorization success.
3. Describe one stale-state or replay condition relevant to this module.
4. Identify one telemetry source that can support a strong conclusion and one blind spot it still leaves.
5. Explain how you would turn a discovered weakness into a regression test rather than a one-time finding.

## Guided study workflow

Use [Study Method](../Guides/STUDY-METHOD.md). Complete at least one authorized exercise, preserve the evidence that supports your conclusion, and explain the module's main trust boundary and failure modes in your own words before moving on.

### Continue with

Choose **Learning paths** from the main menu for an ordered specialization, or use **Search lessons** to follow a concept into related modules.
