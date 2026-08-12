# Multi-Cloud, SaaS Federation, Tenant Isolation and Control Planes

Organizations increasingly depend on several clouds and SaaS platforms linked by federation and automation. The security challenge is not mastering every provider command—it is understanding control-plane authority, identity translation, tenant boundaries, and where policy drift occurs.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, or lab environments you own or are explicitly authorized to test. The exercises in this module are designed to prove security properties without targeting third parties.

## Learning objectives

By the end of this module you should be able to:

- Explain **Control vs data plane** and connect it to a concrete trust boundary or security invariant.
- Explain **Federation** and connect it to a concrete trust boundary or security invariant.
- Explain **Organization hierarchy** and connect it to a concrete trust boundary or security invariant.
- Explain **SaaS administrators** and connect it to a concrete trust boundary or security invariant.
- Explain **Tenant isolation** and connect it to a concrete trust boundary or security invariant.
- Explain **Cross-cloud automation** and connect it to a concrete trust boundary or security invariant.

## Analysis method

Use the shared [Study Method](../Guides/STUDY-METHOD.md). For this module, first draw the relevant components and state transitions, then state one security invariant and identify the minimum evidence needed to test it safely.

## Deep concepts

### 1. Control vs data plane

Control planes create identities, networks, keys, policies, and workloads. Data planes process application traffic. A control-plane identity may indirectly control enormous data-plane reach without touching the data directly.



### 2. Federation

Workforce and workload federation reduce static credentials but introduce trust between issuers, audiences, claims, tenants, and role mappings. Validate exact issuer/audience and constrain which external identities can assume local authority.



### 3. Organization hierarchy

Accounts/subscriptions/projects/folders/organizations define inheritance and administrative boundaries. Review where policy is inherited and which principals can move resources or alter parent-level controls.



### 4. SaaS administrators

SaaS global administrators, app-consent roles, API tokens, integrations, and marketplace apps can bypass ordinary user-level controls. Inventory and monitor privileged integrations.



### 5. Tenant isolation

Multi-tenant services need technical and operational separation across identity, storage, encryption context, support tooling, analytics, backups, and logs.



### 6. Cross-cloud automation

CI/CD and infrastructure automation frequently hold credentials to several providers. Prefer workload federation/short-lived credentials and limit the ability of one pipeline compromise to pivot across clouds.



### 7. Policy drift

Equivalent concepts have different names and semantics across providers. Use a normalized control model for MFA, public exposure, encryption, logging, network egress, key ownership, and break-glass access.



### 8. Central evidence

Aggregate identity changes, role assumptions, app-consent grants, resource-policy changes, key events, and network/public-exposure changes with provider/account context preserved.



## Review focus

Apply the failure-mode taxonomy in [Study Method](../Guides/STUDY-METHOD.md), but keep the analysis specific to this lesson: identify the principal, resource, authority, mutable state, parser or policy boundary, and the telemetry that would distinguish a real control failure from misconfiguration or an observation gap.

## Authorized exercises

### Exercise 1 — Create a provider-neutral matrix for identity, admin hierarchy, network policy, key management, audit logs, and public exposure across two hypothetical clouds

Create a provider-neutral matrix for identity, admin hierarchy, network policy, key management, audit logs, and public exposure across two hypothetical clouds.


### Exercise 2 — Model a SaaS marketplace integration and list every permission it could obtain, how it is revoked, and what happens when the employee owner leaves

Model a SaaS marketplace integration and list every permission it could obtain, how it is revoked, and what happens when the employee owner leaves.


### Exercise 3 — Design a cross-cloud break-glass procedure that avoids one shared permanent super-admin credential

Design a cross-cloud break-glass procedure that avoids one shared permanent super-admin credential.

Use the lab-record format in [Study Method](../Guides/STUDY-METHOD.md) for each exercise and keep all inputs synthetic or confined to the authorized lab.

## Knowledge checks

1. Explain the most important trust boundary in **Multi-Cloud, SaaS Federation, Tenant Isolation and Control Planes** without naming a security tool.
2. Give one example where cryptographic or authentication success still does **not** imply authorization success.
3. Describe one stale-state or replay condition relevant to this module.
4. Identify one telemetry source that can support a strong conclusion and one blind spot it still leaves.
5. Explain how you would turn a discovered weakness into a regression test rather than a one-time finding.

## Guided study workflow

Use [Study Method](../Guides/STUDY-METHOD.md). Complete at least one authorized exercise, preserve the evidence that supports your conclusion, and explain the module's main trust boundary and failure modes in your own words before moving on.

### Continue with

Choose **Learning paths** from the main menu for an ordered specialization, or use **Search lessons** to follow a concept into related modules.
