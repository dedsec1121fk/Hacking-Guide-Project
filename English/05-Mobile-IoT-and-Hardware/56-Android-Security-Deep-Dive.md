# Android Security Deep Dive

> **Purpose:** Understand Android's application sandbox, permissions, signing, storage, components, WebView, keystore, updates, and mobile security architecture—especially as context for Termux and defensive mobile development.

## Learning objectives

- Explain Android application UIDs, sandboxing, permissions, app signing, and component exposure.
- Understand private versus shared storage and scoped-storage implications.
- Identify safe handling of secrets and sensitive data.
- Understand intents, exported components, deep links, WebView, and network security at a conceptual level.
- Relate Android security controls to the Termux environment.

## Application sandbox

Android assigns applications identities and isolates their private data/processes using OS-level controls. Apps should not assume access to another app's private files. Security design should minimize permissions and exposed components rather than relying on users to understand every prompt.

## Permissions

Permissions can be install-time, runtime, special, or mediated through platform APIs depending on Android version and capability. Request only what a feature requires, at the point where the user can understand why it is needed. Handle denial gracefully.

## App signing

Android uses application signing as part of update identity and trust relationships. Signing keys are high-value secrets. Protect them with strong access control, backup/recovery procedures, and modern platform-supported signing workflows.

## Storage

Distinguish:

- app-private internal storage;
- app-specific external areas;
- shared/media/document storage;
- caches;
- secure key storage.

Sensitive secrets should not be placed in public/shared files merely for convenience. Termux `$HOME` is private to the Termux app context; Android shared storage has different semantics and is intended for exchange with other apps/users.

## Android Keystore

The Android Keystore can keep cryptographic keys non-exportable and may use hardware-backed protection depending on device/capability. Applications should use supported cryptographic APIs and design recovery around key lifecycle rather than storing raw keys in ordinary files.

## Components and IPC

Activities, services, broadcast receivers, and content providers can create cross-application interfaces. Developers should explicitly control exported behavior, permissions, intent validation, and data sharing. Treat incoming intents/URIs as untrusted input.

## Deep links

Deep links and app links can route external input into application flows. Validate hosts, schemes, paths, parameters, and authorization state. A link opening a screen should not bypass the permissions that would normally protect the same action.

## WebView

WebView combines web content with native application context and therefore deserves careful configuration. Avoid unnecessary JavaScript interfaces, restrict untrusted navigation, use safe URL validation, keep components updated, and do not expose native privileged actions to arbitrary web content.

## Network security

Use TLS with correct certificate/host validation. Avoid disabling verification to “fix” development errors. Separate development endpoints from production configuration and do not ship debug trust settings unintentionally.

## Logging

Do not log passwords, tokens, private keys, full payment data, or other unnecessary secrets. Mobile logs can be collected during support/debugging and may expose more than developers expect. Log identifiers and event context sufficient for diagnosis without reproducing sensitive payloads.

## Backups and screenshots

Decide whether sensitive application data should be included in platform backup and whether sensitive screens should be capturable. These are product/security decisions that depend on the data and recovery requirements.

## Updates and dependencies

Mobile security depends on OS patch support, application updates, SDK/library versions, and backend services. An app cannot compensate indefinitely for an unsupported device platform. Document minimum supported versions and end-of-support policy.

## Termux relationship

Termux gives a powerful Linux-like user space but remains an Android application. This means:

- it is subject to Android lifecycle and permission behavior;
- `$HOME` is within app-private storage;
- shared storage is different from a Linux home filesystem;
- root-only Linux assumptions usually do not apply on normal devices;
- long-running background processes can be affected by Android power management.

## Safe developer review

For an Android app you own, review:

1. requested permissions;
2. exported components;
3. deep-link handlers;
4. WebView usage;
5. secrets/config files;
6. network/TLS configuration;
7. logs;
8. local data storage;
9. backup behavior;
10. dependency/update policy.

Map findings to OWASP MASVS where appropriate.

## Checkpoint

You should be able to explain where an Android app's trust boundaries sit and why Termux is not equivalent to a rooted desktop Linux system. Continue with Modules 17, 28–31, 39, and 44.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 17 and 28.

### Practice task

Review an Android app you own or a training app for permissions, exported components, storage, logs, WebView, TLS settings, and update policy. Map observations to MASVS concepts.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **39, 44, 54, 57**.
