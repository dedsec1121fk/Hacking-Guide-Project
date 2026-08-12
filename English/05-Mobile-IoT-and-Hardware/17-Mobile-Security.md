# Mobile Security

> **Authorized-use boundary:** Assess only applications, devices, emulators, accounts, and backends you own or are explicitly authorized to test. Mobile testing often touches personal data, so use synthetic accounts and minimize collected evidence.

## Security model

A mobile system spans more than the handset. Model at least four interacting surfaces:

- **Device and operating system:** sandboxing, permissions, secure/verified boot, key storage, updates, local attack surface, and device-integrity signals.
- **Application:** components, deep links, WebViews, local storage, IPC, third-party SDKs, signing, and release configuration.
- **Network and nearby transports:** TLS, Wi-Fi, Bluetooth, NFC, push channels, proxies, and untrusted networks.
- **Backend and cloud services:** authentication, authorization, APIs, data stores, analytics, account recovery, notifications, and administrative controls.

The mobile client should not be treated as the final authority for high-value permissions or business state because users control the device and client software can be inspected or modified.

## OWASP Mobile Top 10:2024 awareness baseline

1. **M1 Improper Credential Usage**
2. **M2 Inadequate Supply Chain Security**
3. **M3 Insecure Authentication/Authorization**
4. **M4 Insufficient Input/Output Validation**
5. **M5 Insecure Communication**
6. **M6 Inadequate Privacy Controls**
7. **M7 Insufficient Binary Protections**
8. **M8 Security Misconfiguration**
9. **M9 Insecure Data Storage**
10. **M10 Insufficient Cryptography**

Use the Top 10 to organize risk awareness, then use MASVS/MASWE and platform documentation for verification requirements and testing depth.

## Mobile Platforms

- **Android** uses application sandboxing, permissions, verified boot, SELinux, platform keystores, and increasingly hardware-backed security features. Security reviews should examine exported components, intents/deep links, WebViews, backup behavior, local data, permissions, and backend trust decisions.
- **iOS/iPadOS** use code signing, sandboxing, entitlements, Keychain, Data Protection classes, and hardware-backed protections. Reviews should focus on entitlement scope, local storage, URL schemes/universal links, network security, privacy permissions, and server-side authorization.
- **Rooted or jailbroken devices** change the local trust model. Applications handling high-value data should define a risk-based policy rather than assuming client-side checks alone can prevent compromise.
- **Enterprise mobility** commonly relies on MDM/MAM, managed identities, device-compliance signals, managed app configuration, remote wipe, and conditional access.
- **BYOD** requires explicit separation of corporate and personal data, privacy-aware policy, and clear off-boarding procedures.

## Mobile Threat Model

Common mobile risks include phishing and malicious links, unsafe deep links, excessive permissions, insecure local storage, weak TLS validation, vulnerable third-party SDKs, exposed application components, account/session takeover, privacy leakage, and compromised devices. Bluetooth, Wi-Fi, NFC, QR codes, and push-notification flows can add attack surface when trust decisions are weak.

For Bluetooth and nearby-device features, minimize discoverability, require authenticated pairing where supported, remove stale pairings, and validate that application behavior does not trust a nearby device solely because a transport connection exists.

## Mobile hardening priorities

- Keep the operating system, applications, and device-management components supported and updated.
- Use a strong screen lock and phishing-resistant account authentication where available.
- Minimize app permissions and remove applications or profiles that no longer have a business purpose.
- Protect sensitive keys with platform keystores rather than ordinary application storage.
- Avoid making high-value authorization decisions solely from client-side state or root/jailbreak checks.
- Use managed configuration, MDM/MAM, conditional access, and remote-wipe capabilities where the organization requires them.
- Minimize sensitive local data, backups, screenshots, clipboard exposure, notification content, and verbose logs.
- Use official or organizationally approved distribution channels and protect release-signing credentials.
- Treat device-integrity and endpoint-security signals as risk inputs, not as perfect proof that a device is trustworthy.

## Modern mobile-security additions

- Prefer platform-backed keystores for long-lived secrets and cryptographic keys.
- Treat deep links, exported components, WebViews, clipboard use, screenshots, backups, and notifications as possible data-exposure paths.
- Use certificate validation correctly; do not disable TLS verification in production builds.
- Minimize sensitive data retained on-device and use platform storage protections.
- Enforce authentication and authorization server-side; a modified client must not become a trust boundary.
- Review mobile dependency and SDK supply-chain risk, including analytics and advertising libraries.

### Verification standards

Use the OWASP Mobile Top 10:2024 as an awareness baseline and complement it with the OWASP Mobile Application Security Verification Standard (MASVS) and testing guidance for authorized assessments.

## Safe lab ideas

Use an emulator or a deliberately vulnerable training application. Review permissions, exported components, local storage, TLS configuration, and server-side authorization without targeting third-party applications or accounts.

## Mobile application architecture review

A mobile application usually consists of more than the installed package. Review the client, backend APIs, identity provider, push-notification service, analytics/advertising SDKs, deep-link handlers, cloud storage, payment integrations, update channel, and any device-management controls. The client device should not be the final authority for permissions or business-critical state.

## Credential and secret handling

Do not embed reusable server secrets in an application package. Anything shipped to a client should be assumed recoverable by a determined user of that device. Use user- or workload-specific tokens, short lifetimes where practical, server-side authorization, and platform keystores for secrets that genuinely must persist locally.

Review whether logs, crash reports, clipboard content, screenshots, notifications, backups, or analytics events accidentally include tokens or sensitive user data.

## Authentication and authorization

Biometric prompts and device PIN checks can improve local user experience, but server-side access still needs a valid authenticated session and authorization decision. Define token expiry, refresh behavior, revocation, logout, device replacement, account recovery, and step-up authentication for sensitive actions.

Negative tests should confirm that changing a local UI state, modifying a request parameter, or using a different object identifier does not grant server-side access.

## Platform storage

Classify data before deciding where to store it. Avoid retaining sensitive data when it can be fetched again securely. Use platform-provided protected storage for cryptographic keys and small high-value secrets. Understand backup behavior and whether app data can be copied to cloud backups or desktop sync mechanisms.

## Network security

Use TLS correctly and validate certificates. Do not disable certificate verification in production because a development proxy was convenient. Review clear-text exceptions, custom trust stores, certificate pinning strategy where used, proxy behavior, and whether sensitive parameters appear in URLs or logs.

Pinning can reduce some interception risk but creates operational complexity; it should not replace normal certificate validation, server-side authentication, or secure key management.

## Deep links, intents, and URL schemes

Deep links and inter-app communication can cross trust boundaries. Validate parameters, require authentication again for sensitive actions, and ensure that an external application cannot invoke internal-only functionality. Prefer platform mechanisms that bind verified domains where appropriate and test ambiguous routing behavior.

## WebViews and embedded browsers

Treat content loaded into a WebView as web content with additional native integration risk. Minimize JavaScript bridges, restrict navigation where feasible, avoid exposing privileged native methods to untrusted pages, and ensure authentication/session data is not unintentionally shared.

## Permissions and privacy

Request only permissions needed for current functionality and explain high-sensitivity use clearly. Review camera, microphone, location, contacts, photos, nearby devices, Bluetooth, notifications, accessibility, and background execution. A permission can create privacy and security risk even when the code using it is technically correct.

Track third-party SDK data collection separately from first-party behavior. Analytics, advertising, crash reporting, and identity SDKs can expand the set of organizations and systems that receive user data.

## Build and release security

Protect signing keys and release credentials, separate debug and production configuration, remove debug endpoints, and verify that test API keys or verbose logging are not shipped. Maintain dependency ownership and know which mobile releases contain a vulnerable SDK.

Mobile applications can remain installed for long periods, so backend compatibility and forced-upgrade policy should account for clients that cannot immediately update.

## Device integrity and risk signals

Root/jailbreak and device-integrity signals can inform risk decisions but are not perfect trust proofs. Treat them as one input alongside account risk, device enrollment, session behavior, and transaction sensitivity. High-value actions should remain protected server-side even if a client reports a “trusted” device state.

## Enterprise mobile controls

Organizations can combine MDM/MAM, managed app configuration, conditional access, certificate-based device identity, data-loss controls, remote wipe, and minimum OS version requirements. Policies should distinguish corporate-owned from personal devices and explain what administrators can and cannot see on BYOD devices.

## Mobile logging

Log authentication changes, security-sensitive settings, backend authorization failures, device enrollment, token revocation, and privileged actions. Avoid logging passwords, access tokens, full payment data, or sensitive message contents. Correlate mobile events with backend request IDs when possible.

## Mobile security review checklist

- [ ] OWASP Mobile Top 10:2024 categories have been considered.
- [ ] No reusable server secret is embedded in the client.
- [ ] Server-side authorization is tested with negative cases.
- [ ] Sensitive local data is minimized and protected.
- [ ] TLS verification is enabled in production.
- [ ] Deep links and exported components have explicit trust rules.
- [ ] WebView/native bridges are minimized.
- [ ] Permissions match actual functionality.
- [ ] Third-party SDK data flows are documented.
- [ ] Release signing and CI credentials are protected.
- [ ] Debug settings are absent from production builds.
- [ ] Backend can revoke sessions and vulnerable client versions when necessary.
- [ ] Security events are logged without exposing secrets.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 01, 39, and basic Android concepts.

### Practice task

Review permissions, exported surfaces, storage, network security, logs, and update policy for an app you own or a deliberately vulnerable mobile lab.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **28, 39, 44, 56**.
