# SCIM, Identity Lifecycle and Provisioning Security

Authentication is only one phase of identity. This module covers account creation, updates, group membership, deprovisioning, authoritative sources, drift and SCIM security controls.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, captures, or lab environments you own or are explicitly authorized to test. Prefer localhost, synthetic data, disposable VMs/containers, prerecorded traces, and read-only analysis whenever possible.

## Learning objectives

By the end of this module you should be able to:

- Explain **identity lifecycle states** and identify its most important trust boundary, state transition, and evidence source.
- Explain **SCIM resources and schemas** and identify its most important trust boundary, state transition, and evidence source.
- Explain **provisioning clients and service providers** and identify its most important trust boundary, state transition, and evidence source.
- Explain **group and role synchronization** and identify its most important trust boundary, state transition, and evidence source.
- Explain **deprovisioning and disable semantics** and identify its most important trust boundary, state transition, and evidence source.
- Explain **source-of-truth conflicts** and identify its most important trust boundary, state transition, and evidence source.

## Analysis method

Use [Study Method](../Guides/STUDY-METHOD.md). Start by identifying ownership or identity, the state transition that can fail, and the evidence that would distinguish a real boundary violation from a diagnostic artifact.

## Deep concepts

### 1. identity lifecycle states

Provisioning is a state machine: invited, active, suspended, disabled, deleted, restored, and sometimes external/contractor states have different authority. Define transitions and which source is allowed to initiate each one.

### 2. SCIM resources and schemas

SCIM represents users, groups, and extensions with standardized resource schemas. Validate identifiers, mutability, uniqueness, enterprise extensions, and tenant scope instead of mapping every received field directly into privileged directory attributes.

### 3. clients and service providers

A SCIM client usually has powerful lifecycle authority over a service provider. Use narrowly scoped credentials, authenticate the client strongly, limit tenant/environment, and log every create/update/deactivate operation with a stable correlation identifier.

### 4. group and role synchronization

Group membership can translate directly into application roles or access. Review nested groups, default groups, name collisions, delayed propagation, and whether an external identity source is actually authoritative for the target privilege.

### 5. deprovision and disable

Offboarding security depends on rapid removal of active sessions, tokens, group membership, service credentials, and downstream access—not just marking a profile inactive. Measure deprovisioning latency and reconcile systems that were offline or failed updates.

### 6. source-of-truth conflicts

HR, directory, IdP, application, and manual admin changes can disagree about identity state. Define precedence and conflict handling so a stale system cannot silently re-enable a user or overwrite a security-sensitive attribute.

### 7. pagination, filtering and bulk

Large SCIM deployments use pagination, filters, PATCH, and bulk operations that can create partial-success and retry behavior. Make updates idempotent where practical, validate per-object authorization, and retain enough status to reconcile failed subsets safely.

### 8. telemetry and reconciliation

Periodic reconciliation detects drift between intended identity state and application reality. Compare active users, groups, privilege, unmanaged accounts, failed provisioning events, and last-success timestamps rather than trusting one provisioning API response.

## Engineering focus

For this module, convert each important claim into a security invariant and a regression test. Prefer controls that remove unnecessary authority, make state transitions explicit, bound resource use, and leave enough telemetry to explain a failure. The reusable evidence and lab-record format is in [Study Method](../Guides/STUDY-METHOD.md).

## Authorized lab sequence

### Lab 1 — Build a synthetic HR→IdP→SaaS lifecycle diagram for joiner/mover/leaver events.



### Lab 2 — Design a SCIM-like local JSON dataset and verify that group changes produce expected least-privilege outcomes.



### Lab 3 — Write a deprovisioning checklist that includes active sessions, API tokens, shared resources and audit evidence.

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

Recommended related modules: **021, 039, 042, 059, 092, 093, 128**. From the main menu, choose **Search lessons** to find related sections across the full guide.
