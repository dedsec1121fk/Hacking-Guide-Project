# Endpoint, Browser and SaaS Security

> **Purpose:** Cover the everyday control plane where users, browsers, SaaS applications, extensions, endpoints, and cloud identity intersect.

## Endpoint security

Modern endpoint protection combines platform hardening, patching, disk encryption, device identity, EDR, application controls, browser policy, and least privilege.

A device should have a known owner, supported OS, update state, encryption status, management state, and recovery process.

## Mobile endpoints

Phones hold authenticator apps, passkeys, email, cloud sessions, and recovery channels. Use screen lock, hardware-backed security where available, current updates, remote-lost-device controls, and careful app permissions.

## Browser as an application platform

Browsers store sessions, passwords/passkeys, history, extensions, and enterprise identity. Keep browsers updated and reduce unnecessary extensions.

Extensions can read or modify web content depending on permissions. Review publisher, permissions, update history, necessity, and enterprise allow/deny policy.

## Session theft risk

Strong MFA does not make stolen authenticated sessions harmless. Protect endpoints, use short/appropriate session lifetime, re-authentication for sensitive operations, risk-based controls, and server-side revocation.

## SaaS administration

For each SaaS product, identify:

- business owner;
- technical admin;
- SSO/MFA state;
- local accounts that bypass SSO;
- privileged roles;
- API tokens/integrations;
- audit-log availability;
- data classification;
- sharing defaults;
- guest/external users;
- offboarding procedure;
- backup/export capability.

## OAuth application consent

Third-party integrations can gain long-lived API access even without user passwords. Govern app consent, scopes, publisher trust, review, revocation, and service-account ownership.

## Shadow SaaS

Users often adopt tools before security teams know. Solve this with usable approved alternatives, discovery, procurement workflows, and risk-based review rather than only blocking domains.

## DLP and sharing

Data-loss prevention can reduce accidental exposure but depends on classification and context. Review public links, external collaborators, default sharing, and sensitive exports.

## Endpoint detection

EDR visibility is only valuable when alerts are monitored, exclusions are governed, agents are healthy, and responders can isolate/recover hosts.

## Browser lab

On a test browser profile:

1. list installed extensions;
2. record permissions;
3. remove one unnecessary extension;
4. review saved site permissions;
5. inspect active sessions for a test account;
6. revoke one session and verify logout behavior.

**Learning goal:** understand the browser as part of the identity and endpoint attack surface.

## SaaS inventory lab

Create a fictional ten-app SaaS inventory and classify each by identity integration, data sensitivity, administrator count, external sharing, audit logging, and offboarding maturity. Prioritize three improvements.

## Endpoint, browser and SaaS operational depth

Endpoint security is an ecosystem: OS patching, disk encryption, endpoint protection, browser configuration, extensions, SaaS sessions, OAuth grants, identity recovery, device management, and user behavior interact.

### Browser review

Inventory extensions, remove unused ones, restrict permissions where possible, keep the browser updated, review download/autofill/password behavior, and separate managed/work profiles where policy requires. Browser sync can replicate sensitive state across devices, so account security matters.

### SaaS review

For critical SaaS applications document admins, MFA/passkey posture, external sharing, API tokens, OAuth integrations, dormant accounts, audit logs, retention, backup/export options, and recovery contacts.

### Endpoint loss

A lost encrypted device can still require session/token revocation and account review. Define who can remotely lock/wipe devices, what evidence is available, and how users regain access without weakening recovery security.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 17, 21, and 39.

### Practice task

Audit your own endpoint/browser/SaaS settings: updates, extensions, account MFA/passkeys, session/device inventory, recovery methods, sharing permissions, and admin roles.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **47, 49, 55, 56**.
