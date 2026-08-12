# Secrets, PKI and Key Management

> **Purpose:** Manage passwords, API keys, certificates, cryptographic keys, signing identities, and recovery material across their full lifecycle.

## Secret lifecycle

Every secret needs:

- owner;
- purpose;
- scope;
- creation source;
- storage location;
- distribution mechanism;
- rotation/revocation process;
- expiry where appropriate;
- audit trail;
- recovery or replacement plan.

Unknown secrets become permanent risk.

## Secret types

Examples include:

- passwords;
- API keys;
- OAuth client secrets;
- service credentials;
- SSH private keys;
- TLS private keys;
- code-signing keys;
- database credentials;
- encryption keys;
- recovery codes.

Each has different storage and rotation requirements.

## Avoid secrets in source code

Repositories are optimized for copying and history. Once a real secret is committed, remove it from use by rotating/revoking it; deleting only the latest line does not erase previous exposure.

## Secret managers

Centralized secret-management systems can enforce access, rotation, auditing, and short-lived credentials. Their administrative and recovery paths become highly privileged and must be protected accordingly.

## PKI concepts

Public Key Infrastructure combines key pairs, certificates, identities, certificate authorities, validation, revocation/status, policies, and operational processes.

A certificate binds claims to a public key under an issuer's trust model. Protecting the private key is critical.

## Certificate lifecycle

Track:

- subject/SANs;
- issuer;
- key algorithm/size;
- validity;
- private-key location;
- owner;
- renewal method;
- deployment targets;
- revocation path.

Automate renewal where appropriate, but alert on failure.

## Key rotation

Rotation should be designed before compromise. Support overlapping keys/certificates during controlled transitions where necessary, and know how consumers discover the new key.

## Signing keys

Code/package/container signing keys can affect many downstream users. Isolate high-value signing operations, require strong authorization, log use, and have a compromise response plan.

## Encryption key separation

Separate data-encryption keys and key-encryption/master keys where architecture requires it. Limit who can both access encrypted data and manage the keys that decrypt it.

## Backups and escrow

If losing a key permanently destroys critical data, define secure backup/recovery. If a key must never be recoverable, document that property and its consequences.

## Lab — Secret inventory

Create a fictional application with database password, API credential, TLS key, signing key, and recovery code. For each, record lifecycle fields, access boundaries, rotation trigger, and incident action.

Then redesign the application to replace one long-lived credential with a short-lived identity mechanism.

**Learning goal:** secrets are managed assets, not strings hidden in configuration.

## Key-management depth

Cryptographic strength depends on the lifecycle around the key: generation, storage, distribution, use, rotation, backup/recovery, revocation, expiration, and destruction.

### Secret classes

Separate human passwords, API tokens, OAuth credentials, SSH keys, TLS private keys, signing keys, database credentials, encryption keys, recovery codes, and machine identities. Their rotation and recovery patterns differ.

### PKI

Certificates bind names/identities to public keys under a trust model. Operations should track issuance authority, SAN/name requirements, expiration, renewal automation, revocation, private-key protection, intermediate/root trust, and emergency rotation.

### Signing keys

Code/package/document signing keys can have organization-wide impact. Restrict access, prefer hardware-backed/HSM-style protection for high-value uses, require auditable workflows, and maintain a compromise/revocation plan.

### Rotation

Rotation is not complete until all consumers use the new secret and the old one is revoked. Track dependencies and avoid rotations that leave stale credentials active indefinitely.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 20, 21, and 39.

### Practice task

Create a secrets inventory for a fictional application: secret type, owner, storage, rotation, consumers, expiration, backup/recovery, revocation, and audit evidence.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **22, 24, 48**.
