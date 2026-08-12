# Threat Modeling and Security Architecture

> **Purpose:** Find security problems while systems are still diagrams and requirements, when fixes are cheaper and less disruptive.

## Start with the system

Threat modeling requires a useful model of what exists:

- users and roles;
- services/components;
- data stores;
- external dependencies;
- trust boundaries;
- data flows;
- administrative paths;
- secrets/keys;
- deployment environments.

A threat model with no architecture model is mostly guessing.

## Assets and security objectives

List what must be protected and why. Examples:

- account integrity;
- customer confidentiality;
- service availability;
- transaction correctness;
- signing keys;
- audit evidence;
- administrative control.

Different assets can require different controls.

## Trust boundaries

Mark every point where data or authority crosses between different trust assumptions: internet to edge, browser to API, workload to database, tenant to tenant, CI to production, employee device to admin plane, model output to tool execution.

## STRIDE

STRIDE is one useful prompt set:

- Spoofing
- Tampering
- Repudiation
- Information disclosure
- Denial of service
- Elevation of privilege

It is a brainstorming aid, not a proof that every threat was found.

## Abuse cases

Ask how a legitimate feature could be misused. Examples:

- password reset used to take over accounts;
- export function used for bulk data theft;
- invitation workflow used to cross tenant boundaries;
- AI tool integration used to perform an action without adequate approval.

## Security architecture patterns

Common patterns include:

- centralized identity with strong authorization at services;
- least-privilege service identities;
- segmented administrative planes;
- secure defaults;
- explicit tenant isolation;
- defense in depth;
- immutable deployment artifacts;
- short-lived credentials;
- centralized audit trails;
- fail-safe behavior.

## Failure modes

Model not only malicious input but also failures:

- dependency timeout;
- message duplication;
- partial transaction;
- stale authorization data;
- clock skew;
- key rotation failure;
- storage exhaustion;
- malformed parser input;
- unavailable identity provider.

Security incidents frequently emerge from exceptional conditions and unsafe recovery behavior.

## Prioritization

For each threat, capture:

```text
Threat:
Asset:
Preconditions:
Impact:
Existing controls:
Residual risk:
Decision:
Owner:
Verification:
```

Do not multiply arbitrary numbers merely to create false precision.

## Architecture decision records

Record security-relevant design decisions and alternatives. Future engineers should know why a boundary or control exists before removing it.

## AI systems

Add model providers, retrieval stores, system prompts, tool calls, user content, output consumers, and human approvals to the architecture. Treat model output as untrusted data when it influences code, queries, or actions.

## Supply chain

Model build systems and dependency registries as part of production. An attacker who changes the artifact before deployment may never need to attack the running service directly.

## Lab — Threat model a notes app

Model a fictional multi-user notes application with browser, API, database, object storage, email provider, and CI/CD pipeline. Identify at least ten threats across identity, authorization, data handling, availability, supply chain, and operations. Select controls and define one verification test for each high-priority threat.

**Learning goal:** make security requirements emerge from architecture rather than from a generic checklist.

## Threat-modeling depth

A threat model is a living explanation of how a system can fail securely or insecurely. Begin with architecture rather than threat names.

### Build the model

Document users/services, assets, data stores, external dependencies, entry points, trust boundaries, privilege levels, and important data flows. Mark where identity changes, where data becomes executable/parsed, and where privileged actions occur.

### Abuse cases

For each important action ask how an unauthorized user, compromised service, malicious dependency, operator mistake, outage, or replay could cause harm. Include privacy and availability abuse cases, not only confidentiality breaches.

### Mitigation quality

A mitigation should name the control owner, enforcement point, evidence, failure mode, and residual risk. “Use encryption” is incomplete unless the model states where keys live, who authenticates whom, and what happens when keys rotate or are lost.

### Review triggers

Update threat models when authentication changes, new integrations/tools are added, trust boundaries move, data sensitivity changes, a major incident occurs, or deployment architecture changes.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 01, 21, 22.

### Practice task

Threat-model a small system: assets, data flows, trust boundaries, identities, dependencies, abuse cases, mitigations, assumptions, and residual risk. Review it after one architecture change.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **42, 46, 54**.
