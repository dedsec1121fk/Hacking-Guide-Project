# Privacy, Data Protection and Operational Hygiene

> **Purpose:** Teach the data-handling discipline required for security work so collection, testing, logs, reports, and automation do not create unnecessary privacy or secret-management risk.

## Learning objectives

- Apply data minimization, purpose limitation, retention, and access control to security workflows.
- Separate secrets, personal data, telemetry, and public information.
- Build safe note-taking and evidence-handling habits.
- Understand privacy tradeoffs in logging, OSINT, incident response, and AI tools.

## Collect less

Security work often creates pressure to collect “everything.” More data can create more risk, storage cost, access-control complexity, breach impact, and legal obligations. Before collecting a field ask:

- What decision does this field support?
- Could a less sensitive value answer the same question?
- How long is it needed?
- Who needs access?
- How will it be deleted?

## Separate identifiers from secrets

Usernames, device IDs, IP addresses, account IDs, tokens, passwords, private keys, and session cookies are not interchangeable categories. A log can safely contain a synthetic account identifier while it should not contain the account's password or bearer token.

## Redaction

Reports and screenshots should redact secrets and unnecessary personal data while preserving enough context to prove the finding. Keep an unredacted evidence copy only when authorization and evidence requirements justify it, and protect it accordingly.

## Retention

Define retention before the test. Temporary captures and debug logs often outlive their purpose. A professional workflow includes deletion/archival rules and verifies that copies were not left in Downloads, messaging apps, clipboard managers, cloud sync folders, or temporary directories.

## OSINT ethics

Public availability does not automatically justify unlimited collection or redistribution. Use clear intelligence requirements, avoid doxxing, minimize personal data, distinguish fact from inference, and avoid accessing private accounts or bypassing access controls.

## Incident-response privacy

Incident responders sometimes need broader telemetry, but collection should still be proportionate. Limit access to investigation data, document purpose, preserve chain-of-custody requirements where relevant, and delete or archive according to policy after the investigation.

## AI/LLM data handling

Before sending security data to an AI service, determine whether it contains secrets, customer data, proprietary code, incident evidence, personal data, or regulated information. Use approved services and data-handling settings. Prefer synthetic examples when the real data is unnecessary.

## Device operational hygiene

- Use device encryption and strong screen lock.
- Keep OS/apps updated.
- Separate test and personal accounts where practical.
- Use password managers/passkeys/MFA appropriately.
- Avoid storing private keys or tokens in shared Android storage.
- Review app permissions.
- Back up important notes securely.
- Remove stale test credentials.

## Evidence-folder pattern

A project can use:

```text
case-or-lab/
├── scope.md
├── notes.md
├── evidence/
├── redacted/
├── report/
└── cleanup.md
```

Keep raw evidence access-controlled. Put only sanitized/export-ready material in `redacted/`.

## Checkpoint

You should be able to justify every sensitive data field you collect during a lab or assessment and explain how it is protected, retained, and deleted. Continue with Modules 34, 37, 42, 43, and 49.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Module 42 helps.

### Practice task

Take a sample assessment folder and classify each artifact by sensitivity, purpose, access, retention, redaction, and deletion rule. Remove any data that is not necessary.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **34, 37, 42, 43**.
