# Cloud Security

> **Authorized-use boundary:** Use cloud labs, sandbox accounts, training tenants, or environments you own or are explicitly authorized to assess. Do not test provider infrastructure or other tenants.

## Learning objectives

By the end of this module, you should be able to:

- explain the shared-responsibility model without assuming that “the provider handles security”,
- distinguish identity-plane, control-plane, data-plane, and workload risk,
- reason about blast radius across accounts/projects/subscriptions and tenants,
- design least-privilege human and workload access,
- evaluate storage, network, secret, logging, backup, and deployment controls,
- produce a small cloud threat model and evidence-based hardening plan.

## Cloud service models

### Infrastructure as a Service (IaaS)

IaaS exposes virtualized compute, networking, and storage while the provider operates the underlying physical infrastructure. The customer typically remains responsible for guest operating systems, applications, identities, data, workload configuration, and much of the network policy.

### Platform as a Service (PaaS)

PaaS removes more operating-system and runtime administration from the customer. That does **not** remove application, identity, data, secret, authorization, or configuration responsibilities. A managed database can still be publicly exposed; a managed application platform can still run vulnerable code; a managed identity integration can still be over-privileged.

### Software as a Service (SaaS)

SaaS shifts most infrastructure and application operation to the provider. Customer risk concentrates around identity, tenant configuration, data sharing, integrations, API tokens, administrator roles, retention, endpoint/session security, and the ability to investigate incidents.

The useful question is not “who owns the server?” but **which security decisions are still under your control?**

## Deployment and tenancy models

Public, private, hybrid, and community-style environments differ in ownership and connectivity, but tenancy boundaries matter more than labels. Document which resources share an administrative plane, identity system, network, encryption keys, logging destination, and recovery path.

A “private” environment can still have weak identity controls. A public-cloud workload can be strongly isolated. Security depends on the actual architecture and policies.

## Shared responsibility

Build a responsibility matrix for each service. Include at least:

| Area | Provider responsibility | Customer responsibility to verify |
|---|---|---|
| Physical facilities | Data-center protection | Contract/compliance requirements |
| Hypervisor / managed platform | Provider-operated isolation | Service choice and exposure assumptions |
| Human identities | Identity service availability | MFA, lifecycle, roles, recovery |
| Workload identities | Platform primitives | Scope, issuance, rotation, revocation |
| Data | Service durability features | Classification, access, encryption, lifecycle |
| Network | Fabric availability | Ingress, egress, segmentation, private access |
| Logging | Logging capability | Enablement, retention, protection, alerting |
| Backups | Service mechanisms | Coverage, isolation, restore testing |
| Application code | Usually customer | Secure design, dependencies, secrets, authz |

Managed service does not mean managed **risk**.

## Cloud trust boundaries

Cloud environments contain several interacting boundaries:

- **identity plane:** users, service accounts, workload identities, federation;
- **control plane:** APIs that create, modify, or delete resources;
- **data plane:** application and storage traffic;
- **management plane:** organization, billing, policy, audit, and security tooling;
- **workload boundary:** VM, container, function, managed runtime, or SaaS integration;
- **tenant boundary:** separation from other customers or business units;
- **recovery boundary:** backups, break-glass identities, immutable logs, and alternate access paths.

A threat model should show where authority crosses these boundaries and which identity performs each action.

## Identity-first cloud security

Long-lived access keys create avoidable risk. Prefer centrally managed human identities, MFA, federation, workload identity, and short-lived credentials where supported.

### Human access

Review:

- joiner/mover/leaver lifecycle,
- privileged-role assignment,
- MFA and phishing-resistant authentication for high-impact roles,
- just-in-time elevation where available,
- break-glass account protection,
- dormant accounts and stale API tokens,
- cross-account or cross-tenant trust.

### Workload access

A workload should receive only the permissions it needs for its current role. Avoid sharing one powerful service identity across unrelated applications. Document credential issuance, audience/scope, lifetime, revocation, and what happens when the workload is moved or rebuilt.

## Control-plane security

Cloud APIs are extremely powerful because infrastructure itself is programmable. A control-plane credential may be able to create identities, modify network routes, replace images, change logging, expose storage, or destroy resources.

Protect control-plane actions with:

- least privilege,
- organization-level guardrails,
- separation of duties,
- strong authentication,
- infrastructure-as-code review,
- protected deployment pipelines,
- immutable or independently protected audit logs,
- alerts for high-impact policy and identity changes.

## Network architecture

Cloud networking should be designed from required flows rather than from broad “internal” trust.

Document:

- internet-facing entry points,
- load balancers and API gateways,
- private endpoints,
- east-west workload traffic,
- administrative access paths,
- DNS dependencies,
- egress destinations,
- peering/transit relationships,
- network-policy enforcement points.

A security group or firewall rule is only one layer. Application authorization and workload identity still matter after network admission.

## Storage and data security

For each data store, identify:

1. owner and classification,
2. permitted identities,
3. public-access state,
4. encryption and key ownership,
5. replication/location requirements,
6. retention and deletion policy,
7. backup and restore behavior,
8. audit events that prove access or policy change.

Do not treat encryption at rest as a substitute for authorization. If an over-privileged identity can decrypt data through the normal service API, the cryptography is working exactly as designed while the access model remains unsafe.

## Secrets and key management

Secrets should not be embedded in images, repositories, deployment templates, shell history, or application logs. Prefer managed secret stores or workload identity.

Separate:

- secret **storage**,
- authorization to **read** a secret,
- authorization to **use** a key without exporting it,
- rotation,
- revocation,
- audit evidence.

For high-value keys, understand whether the platform uses software-protected keys, HSM-backed keys, customer-managed keys, or externally managed key material.

## Logging and detection

A cloud incident can involve identity, control-plane, network, storage, workload, and SaaS events simultaneously. Centralize enough telemetry to reconstruct those relationships.

Useful categories include:

- authentication and federation events,
- privileged-role changes,
- control-plane API calls,
- policy changes,
- storage access and public-access changes,
- network-flow or gateway logs,
- workload logs,
- key/secret access,
- CI/CD and artifact events,
- backup/recovery operations.

Protect security logs from the same identities that administer production wherever practical.

## Infrastructure as code and policy as code

Infrastructure as code improves repeatability, but insecure configuration can also be repeated perfectly. Use code review, automated checks, protected branches, plan/diff review, deployment identity separation, and drift detection.

Policy as code can enforce organization-wide invariants such as:

- approved regions,
- required logging,
- prohibited public storage,
- mandatory encryption,
- allowed workload identities,
- restricted network exposure.

The policy must be tested for both false negatives and false positives.

## Multi-account and multi-project design

Separate environments to limit blast radius. Production, development, security tooling, logging, and backup administration may justify different accounts/projects/subscriptions or equivalent boundaries.

Do not assume separation is effective merely because resources have different names. Verify federation, organization roles, shared automation identities, networking, logging, and recovery permissions.

## Backup and destructive-action resilience

Backups are part of the security boundary. Test whether a compromised production administrator can also delete backups, disable retention, alter recovery settings, or destroy the logging needed to investigate the event.

Recovery design should include:

- isolated or immutable copies where appropriate,
- separate administrative authority,
- documented restore procedures,
- regular restoration tests,
- dependency ordering,
- recovery when the primary identity provider is unavailable.

## SaaS and third-party integrations

SaaS risk often enters through OAuth grants, API tokens, marketplace applications, automation accounts, synchronization tools, and external administrators.

Inventory integrations and record:

- owner,
- permissions/scopes,
- data accessed,
- credential lifetime,
- revocation process,
- audit capability,
- business dependency.

A forgotten integration can retain effective access long after the employee who installed it has left.

## Threat scenarios to reason about

Model scenarios such as:

- a phishing-resistant MFA gap on a privileged account,
- an over-scoped workload identity,
- a public object-storage configuration,
- a leaked deployment secret,
- an infrastructure-as-code change that weakens logging,
- a compromised CI runner publishing an untrusted artifact,
- a cross-account trust relationship with excessive authority,
- a destructive administrator who can also remove backups,
- a SaaS integration retaining stale access.

For each scenario, record prevention, detection, containment, and recovery controls.

## Assessment questions

- Can a compromised low-privilege identity reach sensitive resources?
- Can one administrator both modify production and erase the evidence of that change?
- Are workload credentials short-lived and tightly scoped?
- Are public-access controls and organization guardrails centrally enforced?
- Are infrastructure changes attributable and recoverable?
- Can backups survive compromise of the production administrative plane?
- Can responders investigate if the primary cloud identity provider is unavailable?
- Do you know which external integrations can access sensitive data today?

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the cloud-specific preparation and exercise below.

### Before you begin

Complete Modules 01 and 21 and understand basic IP networking, DNS, authentication, authorization, and logging.

### Practice task

Design a fictional three-tier cloud application. Draw its human identities, workload identities, control plane, network paths, storage, secrets, logging, deployment pipeline, and backups. Then write five security invariants and identify the minimum evidence needed to verify each one.

### Mastery check

Explain why cloud security is primarily an **authority and control-plane problem**, identify one realistic blast-radius path, and describe a control plus a log source that would prove the control is operating.

### Continue with

Recommended next modules: **21, 24, 41, 47, 49, 76, 104, 105**.
