# Windows and Active Directory Security

> **Purpose:** Understand Windows enterprise security and Active Directory from a defender, administrator, and authorized-assessment perspective.

## Learning objectives

- Understand domains, forests, trusts, domain controllers, identities, groups, and Group Policy.
- Recognize why identity tiering, credential protection, patching, logging, and delegation matter.
- Review common enterprise failure modes without relying on credential theft or destructive techniques.
- Build safer AD labs for configuration review and detection validation.

## Active Directory mental model

Active Directory Domain Services is both a directory and an authentication/authorization control plane. Important objects include users, computers, groups, service accounts, organizational units, Group Policy Objects, and trusts.

Security depends on relationships. A low-value workstation account may matter because it can modify a group, a group may control a server, and that server may hold credentials or administration paths into more critical systems.

## Authentication concepts

Windows environments commonly use Kerberos and may retain NTLM for compatibility. Defenders should know where legacy authentication remains, why modern protocols are preferred, and how authentication events are logged.

Do not equate authentication with authorization. Successful sign-in answers “who are you?”; resource ACLs, group membership, privileges, and policy answer “what can you do?”

## Privileged identities

Separate day-to-day accounts from administrative identities. Critical administrators should not use privileged accounts for browsing, email, or routine workstation activity.

High-value controls include:

- phishing-resistant MFA where supported;
- privileged access workstations or equivalent hardened admin paths;
- just-in-time/just-enough administration;
- unique local administrator credentials;
- service-account lifecycle management;
- removal of stale group memberships;
- protection of directory backups and recovery credentials.

## Group Policy

Group Policy can enforce powerful security settings at scale, but a misconfigured GPO can also propagate risk quickly. Treat GPO creation, linking, delegation, and modification as privileged operations and monitor changes.

## Service accounts

Service accounts frequently become long-lived because application owners fear breaking dependencies. Inventory owner, purpose, privileges, logon rights, rotation mechanism, and dependencies. Prefer managed service-account mechanisms where supported.

## Local administrator risk

Reusing one local administrator password across many endpoints creates a broad blast radius. Use platform-supported local password management and avoid shared static credentials.

## Delegation and ACL review

Active Directory has many permission paths beyond obvious administrator groups. Review who can create users, reset passwords, modify group membership, write to sensitive objects, link policy, enroll certificates, or modify service configuration.

## Certificate services

Enterprise PKI and certificate enrollment add another identity plane. Secure template permissions, enrollment rights, issuing CAs, private keys, renewal paths, and administrative roles. Certificate-based authentication should receive the same seriousness as passwords and tokens.

## Windows logging

Useful sources include security event logs, PowerShell logs, endpoint detection telemetry, directory-service logs, authentication provider logs, and configuration-management records. Centralize important logs so compromising one endpoint does not erase the only evidence.

## Hardening priorities

1. Patch supported operating systems and critical applications.
2. Remove unsupported protocols and unnecessary services.
3. Enforce secure boot/device protections where appropriate.
4. Use application control for high-risk systems.
5. Reduce local admin rights.
6. Protect credential material.
7. Segment administrative paths.
8. Monitor identity and policy changes.
9. Test backup and directory recovery.

## Authorized lab

Build a disposable evaluation domain using test VMs. Create normal users, one admin role, two departments, and a service account. Document:

- group membership;
- GPO scope;
- password/MFA policy;
- local admin handling;
- service-account owner;
- logging coverage;
- recovery plan.

Then make one benign policy change and verify the change appears in the expected logs.

**Learning goal:** understand AD as a permission graph and governance system, not just a login server.

## Windows security model in more depth

Windows security decisions are built around security principals, access tokens, ACLs, privileges, integrity boundaries, services, and policy. In an Active Directory environment, domain identity, Kerberos/NTLM authentication, Group Policy, certificate services, DNS, endpoint management, and privileged administration create additional dependencies.

### Identity tiers

Separate ordinary user activity from privileged administration. Highly privileged accounts should not be used for email, browsing, or routine productivity. Service identities need owners, documented purpose, minimal rights, rotation/recovery, and monitoring. Emergency access should be controlled, tested, and auditable.

### Authentication and domain dependencies

Kerberos depends on accurate time, DNS, service identity, and key material. NTLM may remain for compatibility but should be reduced where feasible. Authentication failures should be investigated with the surrounding account/device/service context rather than treated as isolated event IDs.

### Logging baseline

A useful Windows/AD telemetry design considers logon activity, privileged group changes, service creation/change, process telemetry where enabled, PowerShell/script logging according to policy, endpoint security events, directory changes, and identity-provider signals. Centralization improves correlation but does not eliminate the need to protect local evidence and time synchronization.

### Hardening questions

Ask whether local admin is needed, whether legacy protocols remain enabled, whether remote administration is restricted, whether endpoint protection/tamper protections are healthy, whether credential material is exposed unnecessarily, and whether recovery procedures exist for domain controllers and identity infrastructure.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 01, 21, and basic Windows administration.

### Practice task

In a Windows lab you administer, inventory local/domain identities, privilege groups, logging, update status, and authentication policy. Build a least-privilege remediation checklist.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **23, 37, 47, 49**.
