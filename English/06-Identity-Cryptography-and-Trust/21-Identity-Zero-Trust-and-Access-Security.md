# Identity, Zero Trust, and Access Security

> **Purpose:** Build an identity-centric security model that limits the effect of stolen credentials and over-privileged accounts.

## Learning objectives

- Understand identity as a primary control plane.
- Apply least privilege, separation of duties, and lifecycle management.
- Distinguish authentication, authorization, session management, and privileged access.
- Understand Zero Trust as an architecture principle, not a product.
- Design telemetry for identity abuse and account compromise.

## Identity lifecycle

A secure identity program covers **joiner, mover, and leaver** events. Accounts should be created from authoritative business records, assigned only necessary access, reviewed when roles change, and disabled promptly when access is no longer required. Service and workload identities need the same ownership discipline as human accounts.

### Authentication

Prefer phishing-resistant MFA for high-risk access when available. Passwords should be long, unique, and protected by a password manager. Recovery workflows are part of authentication security; strong MFA can be undermined by a weak reset process.

### Authorization

Authorization answers what an authenticated identity may do. Common models include RBAC, ABAC, policy-based access control, and resource ACLs. Deny by default where practical and test authorization server-side.

## Privileged Access Management

- Separate administrative and daily-use accounts.
- Use just-in-time or time-bounded elevation where possible.
- Require stronger authentication and device controls.
- Monitor especially sensitive actions.
- Maintain tightly controlled break-glass access.

## Zero Trust

NIST describes Zero Trust as removing implicit trust based only on network location or ownership. Access decisions should consider the subject, device/workload, resource, policy, and current context. Zero Trust does not mean replacing every network control; it means that network location alone is not sufficient evidence of trust.

## Identity telemetry

Monitor for unusual sign-ins, repeated MFA failures, new MFA methods, privilege changes, new API keys or service principals, unmanaged devices, logging/policy changes, and access inconsistent with role.

## Safe lab

Create two local test accounts with different roles. Build a permissions matrix, verify allowed and denied actions, record the audit events, remove one privilege, and retest.

## References

- NIST SP 800-207 — https://csrc.nist.gov/pubs/sp/800/207/final
- NIST Cybersecurity Framework 2.0 — https://www.nist.gov/cyberframework

## Identity architecture in practice

An identity system normally contains several layers that should be reviewed separately: the authoritative source of a person or workload, the identity provider, authenticators, directories, federation relationships, application sessions, authorization policies, privileged-access systems, and audit logs. A weakness in any one layer can undermine strong controls elsewhere. For example, phishing-resistant authentication is less valuable if account recovery accepts weak evidence, and carefully designed application roles are less valuable if a broad directory group can silently grant them.

### Human identities

Human-account controls should answer four questions: **who owns the account, why does it exist, what can it reach, and how is access removed?** Use named accounts for normal activity, avoid shared administrative users, and maintain a reliable mapping from employment or contractual status to account lifecycle. Review dormant identities, stale group memberships, guest users, forgotten test accounts, and emergency accounts separately because their risk profiles differ.

### Workload and machine identities

Applications, CI jobs, containers, scheduled tasks, service accounts, API clients, and automation also need identities. Prefer short-lived credentials or platform-issued workload identities over static secrets. Give each workload an owner and purpose, restrict where its identity can be used, and log token issuance and sensitive use. A service identity that survives for years without an owner is effectively unmanaged privileged infrastructure.

## Authentication design

Authentication strength is determined by the complete flow rather than the login screen alone. Review enrollment, recovery, device replacement, lost-factor handling, support-desk procedures, session reauthentication, and step-up requirements for sensitive actions.

Useful design principles include:

- Prefer phishing-resistant authentication for administrators and other high-impact roles.
- Avoid security questions based on discoverable biographical facts.
- Protect enrollment and recovery at least as strongly as normal authentication.
- Rate-limit and monitor failed attempts without creating easy denial-of-service conditions.
- Notify users of important authenticator and recovery changes.
- Reauthenticate for security-sensitive changes such as adding a new factor, exporting sensitive data, or changing payment details.
- Keep authentication errors useful to legitimate users without unnecessarily disclosing whether an account exists.

## Authorization design

Authorization should be explicit, server-side, and testable. A useful review starts with a matrix of **subjects × resources × actions × conditions**. This exposes accidental privilege inheritance and helps turn policy into automated tests.

### Common failure modes

- A role grants more permissions than its name implies.
- Front-end controls hide an action while the backend still permits it.
- Object ownership is checked for reads but not updates or deletes.
- Administrative APIs trust a network location instead of an identity and policy decision.
- A service account can access every tenant because it was designed before multi-tenancy existed.
- Temporary access becomes permanent because there is no expiry or review process.
- Group nesting creates effective permissions nobody can easily explain.

### Access review questions

For every sensitive permission, record the business justification, approver, owner, grant date, expiry or review date, and evidence of last meaningful use. Reviews should focus on whether access is still required, not merely whether a manager recognizes the account name.

## Privilege boundaries and break-glass access

Privileged identities deserve a different operating model. Administrative sessions can be isolated from email and browsing, privileged elevation can be time-bounded, and particularly sensitive changes can require additional approval or step-up authentication. Break-glass accounts should be few, strongly protected, tested periodically, and monitored so that their use is immediately visible. A break-glass mechanism that has never been tested may fail exactly when the normal identity system is unavailable.

## Zero Trust decision model

A Zero Trust design can be reasoned about as a sequence:

1. **Identify the resource** being requested.
2. **Identify the subject** and the strength of its authentication.
3. **Evaluate device or workload posture** if relevant.
4. **Evaluate context** such as risk, location, time, session state, and recent events.
5. **Apply policy** for the requested action.
6. **Grant the minimum required access** for the required duration.
7. **Observe the session** and be prepared to re-evaluate or terminate access.

This model is useful even in small systems. It discourages assumptions such as “inside the VPN means trusted” or “the service account already authenticated once, therefore every future action is safe.”

## Identity threat scenarios for defenders

Defenders should be able to recognize and investigate scenarios such as impossible or unusual sign-in patterns, token use from a new environment, repeated MFA failures, suspicious recovery events, newly created API credentials, privilege escalation through group changes, inactive accounts becoming active, consent to risky third-party applications, and service identities behaving differently from their normal workload.

For each scenario, define the telemetry source, minimum useful fields, expected false positives, investigation steps, containment options, and the business owner who can confirm whether the activity is legitimate.

## Identity security review worksheet

| Area | Questions | Evidence |
|---|---|---|
| Lifecycle | Are joiner/mover/leaver events automated and timely? | HR/IdP workflow, disable timestamps |
| MFA | Which roles lack strong MFA? | Authentication policy export |
| Recovery | Can recovery bypass normal assurance? | Recovery policy and test results |
| Authorization | Are object/action checks server-side? | Policy, unit/integration tests |
| Privilege | Is elevation temporary and attributable? | PAM/JIT logs |
| Workloads | Are long-lived secrets still required? | Secret inventory, token configuration |
| Guests | Are external users reviewed and expired? | Guest inventory |
| Logging | Can security changes be reconstructed? | Identity audit logs |
| Resilience | Is emergency access tested? | Break-glass test record |

## Practical defensive exercise

Create a small role matrix for a fictional company with Employee, Support, Billing, Developer, and Administrator roles. Add three resources—customer profile, billing record, and deployment pipeline—and define read/write/admin actions. Deliberately create one over-privileged role, then perform an access review and correct it. Finally, list the audit events that should be generated when the privilege is granted, used, and removed.

## 2026 identity update — NIST SP 800-63 Revision 4

NIST finalized SP 800-63 Revision 4 in 2025. When designing identity systems, distinguish identity proofing, authentication, authenticator management, and federation rather than reducing identity security to password complexity. Prioritize phishing-resistant authentication for higher-risk use cases, secure recovery, lifecycle management, and privacy-aware identity proofing.

Primary reference: https://csrc.nist.gov/pubs/sp/800/63/4/final

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 01 and authentication basics.

### Practice task

Create a fictional access matrix for employees, admins, service accounts, and emergency access. Remove standing privileges that are unnecessary and define review/revocation evidence.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **32, 39, 42, 49**.
