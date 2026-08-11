# Cloud IAM, Control Planes, Metadata and Temporary Credentials

> **Purpose:** Understand cloud security at the authority-flow level: identities call control-plane APIs, workloads receive temporary credentials, policies combine across layers, and metadata/control-plane access can change blast radius.

## Learning objectives

- Distinguish human, workload, service, and federated identities.
- Reason about effective permissions across multiple policy layers.
- Understand temporary credentials, role assumption, metadata services, and identity federation.
- Analyze control-plane attack paths without attempting cloud compromise.
- Design least-privilege and telemetry verification in a sandbox account/project/subscription.

## Cloud security is API security at infrastructure scale

Most cloud infrastructure is controlled by authenticated APIs. Creating a VM, changing a firewall, reading object storage, attaching a role, rotating a key, altering logging, and creating a database are API-authorized state transitions.

Therefore, cloud security starts with **who can call which API on which resource under which conditions**. Network exposure matters, but identity and control-plane authority often matter more.

## Identity types

Cloud environments commonly include:

- human workforce identities;
- workload/service identities;
- managed identities/roles attached to compute;
- CI/CD identities;
- external/federated identities from an enterprise IdP;
- break-glass/emergency identities;
- vendor/integration identities.

Long-lived access keys should be minimized when short-lived federation or managed workload identity is available.

## Temporary credentials

Temporary credentials have a bounded lifetime and are frequently issued after a principal assumes a role or exchanges an identity assertion. They reduce the persistence of leaked credentials but still grant real authority while valid.

Security properties to review include audience, subject, role, session duration, source identity, conditions, session policy, revocation behavior, and logging.

## Effective permission

Cloud authorization is rarely a single allowlist. Effective permission can depend on identity policy, resource policy, organization policy, permission boundary, session constraints, network context, service-control rules, explicit denies, and service-specific behavior.

Do not infer privilege from one policy document. Evaluate the combined decision and test a narrow allowed/denied operation in the sandbox.

## Role assumption

Role assumption creates an authority edge from one principal to another role. Review both sides:

1. Can principal A request the role?
2. Does the role's trust policy accept A under the intended conditions?
3. What permissions does the resulting role session have?
4. Can the role assume additional roles?
5. Is the chain logged with source identity?

A role graph can reveal privilege paths that are not obvious from individual policies.

## Workload identity

Workloads need credentials to call managed services. Prefer platform mechanisms that issue short-lived identity bound to the workload rather than embedding API keys in images, environment files, or repositories.

The workload's identity should have only the operations required for its runtime task. Separate build-time, deploy-time, and runtime identities.

## Metadata services

Cloud compute platforms may expose instance/workload metadata through a link-local or platform-specific endpoint. Metadata can include identity credentials or configuration intended for the local workload.

The security issue arises when an application with server-side fetch capability can reach metadata it should not expose to the caller. Modern platforms provide stronger metadata protections, tokenized access, hop limits, identity isolation, and workload-specific mechanisms. Enable current platform controls and combine them with application SSRF defenses and egress policy.

This guide does not provide metadata credential-extraction payloads.

## Control plane versus data plane

**Control-plane** operations configure resources and policy. **Data-plane** operations use the resource: read an object, query a database, send a message. Permissions and logs can differ.

A principal may need data access but not permission to alter the resource policy. Separating those responsibilities limits privilege escalation paths.

## Organization-level guardrails

Large environments can apply policies above individual accounts/projects/subscriptions to prohibit dangerous configurations, require logging, restrict regions, control public exposure, or constrain identity behavior.

Guardrails should be designed as invariants and continuously tested. Exception processes need ownership and expiry.

## Secrets and key services

Managed secret/key systems centralize access control and auditing, but applications still need authority to retrieve/decrypt material. Review which identity can call the service, which keys can decrypt which data, rotation, backup/restore, and whether logs record access.

Envelope encryption separates data encryption keys from key-encryption keys and limits the amount of data directly processed by a central KMS.

## Public exposure

Cloud resources can become reachable through public IPs, load balancers, storage policies, serverless URLs, database settings, API gateways, or sharing links. An exposure inventory should join network reachability with identity policy and data sensitivity.

“Not in our VPC” does not mean “not exposed,” and “private IP” does not mean “authorized.”

## Cloud logging

At minimum, collect control-plane audit logs, identity/authentication events, network flow/edge logs where useful, workload/application logs, and security-service findings. Protect logs in a separate administrative/security boundary where feasible.

Detections should focus on meaningful authority changes: new privileged grants, logging disablement, public policy changes, unusual role assumption, new access keys, secret access anomalies, and unexpected region/account activity.

## Safe sandbox lab

Use a disposable cloud sandbox with budget controls or a local emulator. Create two roles: a reader and an administrator-equivalent test role. Allow a synthetic user to assume only the reader. Verify one allowed read-like API and one denied change operation.

Map the trust relationship and inspect audit logs. Then add a condition such as short session duration or a sandbox-specific tag and verify behavior.

## Privilege graph questions

- Who can create/modify identities?
- Who can attach policies?
- Who can assume privileged roles?
- Who can change resource policies?
- Which workloads can read secrets?
- Which CI jobs can deploy production?
- Who can disable/alter logging?
- Which identity can modify network exposure?
- Can one role grant itself more authority indirectly?

## Guided study workflow

### Before you begin

Complete Modules 19, 21, 22, 24, 39, 49, 61, and 75.

### Practice task

Build an identity/role/resource graph in a sandbox and verify at least five allow/deny expectations using read-only or reversible operations. Remove one unnecessary permission edge.

### Evidence to keep

Policy/trust excerpts, graph, audit records, and before/after effective-permission test.

### Common mistakes to avoid

- reading one policy in isolation;
- keeping long-lived keys because they are convenient;
- mixing build/deploy/runtime identities;
- treating metadata as ordinary public web content;
- testing against accounts/resources you do not own.

### Mastery check

Explain how a workload receives temporary authority, how a role assumption creates a graph edge, and why control-plane permission can matter more than network location.

### Continue with

Modules **75, 80, 81, and 85**.
