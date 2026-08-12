# Android Application Reverse Engineering and Mobile App Internals

> **Purpose:** Deepen Android security analysis by connecting APK structure, bytecode/native code, manifests, components, IPC, signing, storage, WebView, and runtime behavior in apps you own or are authorized to test.

## Learning objectives

- Understand APK/AAB packaging, DEX, resources, manifests, and native libraries.
- Trace exported component and intent/Binder trust boundaries.
- Understand application signing and update identity.
- Review local storage, Keystore use, WebView bridges, and network security configuration.
- Perform static/dynamic analysis without bypassing another app's sandbox.

## Package anatomy

An installed Android application originates from one or more APKs generated from an app bundle or traditional package. APK content can include:

- `AndroidManifest.xml`;
- DEX bytecode;
- resources/assets;
- native `.so` libraries for supported ABIs;
- signing metadata;
- configuration/resources split across packages in modern delivery models.

Static analysis begins by identifying which code and resources actually ship to the device.

## DEX and ART

Java/Kotlin application code is compiled into DEX bytecode, then executed/compiled by Android Runtime mechanisms. Decompilers can reconstruct Java-like source, but names may be obfuscated and compiler-generated code can differ significantly from original Kotlin/Java.

Treat reconstructed source like pseudocode and confirm security-sensitive logic with bytecode/runtime behavior when needed.

## Manifest as attack-surface map

The manifest defines components, permissions, intent filters, SDK/version metadata, network/security settings, and exported behavior. Activities, services, receivers, and content providers can cross application boundaries when exported or otherwise reachable.

For each exported component, document required permission, accepted inputs, caller identity assumptions, returned data, and side effects.

## Intent trust boundaries

Intents can carry actions, categories, URIs, extras, and flags. An exported component must treat caller-controlled intent data as untrusted. Validate both syntax and authorization before performing sensitive work.

Explicit intents reduce accidental routing ambiguity but do not replace permission or caller validation when crossing app boundaries.

## Binder and IPC

Binder is Android's core IPC mechanism. Higher-level services, AIDL interfaces, content providers, and framework calls use Binder under the hood. IPC code can inspect caller identity in appropriate contexts, but identity can be lost if work is deferred incorrectly.

A privileged service should validate the caller before clearing identity or dispatching work to a context that no longer carries the original subject.

## Application sandbox

Each ordinary Android app runs under a distinct Linux UID with SELinux policy and platform restrictions. Private app data is inaccessible to other ordinary apps by default. Shared/external storage has different rules and should not be used for secrets merely because a filename is obscure.

Termux is also an app sandbox. It is excellent for learning and local tooling but does not automatically gain access to other apps' private data.

## Signing and update identity

Android app signing establishes the package's update identity and can participate in signature-level permissions. Protect signing keys and use supported key rotation/app-signing mechanisms. A leaked signing key can have long-lived ecosystem impact.

When analyzing an APK you own, compare signer/certificate fingerprints between builds to verify expected lineage.

## Network Security Configuration

Android apps can define trust anchors, cleartext policy, domain-specific TLS settings, and debug overrides. Debug-only trust exceptions should never become production defaults.

Certificate pinning can reduce selected PKI risks but adds rotation/availability complexity; use it only with an explicit threat model and operational plan.

## Keystore

Android Keystore can protect key material so cryptographic operations occur under platform/hardware-backed controls where supported. Key attestation and secure hardware can strengthen assurance, but application authorization and device state still matter.

Do not hard-code cryptographic keys in APK resources; static app packages should be assumed observable by users who possess the app.

## WebView

WebView embeds web content inside an app, bridging web and native trust models. Risks include unsafe URL loading, JavaScript interfaces, file/content access, mixed content, weak origin validation, and navigation to untrusted content.

A JavaScript bridge exposed to untrusted web content can become a privileged API. Keep interfaces minimal and restrict trusted origins/content.

## Deep links and app links

URI-based navigation can route external input into application states. Validate parameters and authorization after navigation. Verified App Links improve domain association but do not prove the user is authorized for the target object.

## Content providers

Content providers expose structured data/URIs and can enforce read/write permissions. Review exported state, URI grants, path permissions, query parameterization, and whether temporary grants outlive intended workflows.

## Native/JNI boundary

JNI connects managed Java/Kotlin code to native C/C++. It introduces memory-safety and type/lifetime boundaries. Validate array/string lengths and ownership. Native libraries should use platform hardening and be fuzzed where they parse untrusted input.

## Obfuscation

R8/ProGuard-like tools can rename/shrink code, which raises reverse-engineering cost but is not an authorization or secret-storage control. Secrets embedded in client code remain recoverable in principle.

## Dynamic analysis

For an app you own, use a debug build/emulator and platform-supported debugging/logging to observe lifecycle, network requests to your lab server, local files, and IPC. Avoid techniques designed to bypass anti-debugging or tamper protections in third-party apps.

## Static analysis lab

Create a small Android app or use an open-source training app you are authorized to inspect. Analyze:

- manifest exported components;
- permissions;
- deep links;
- network security config;
- WebView use;
- local storage choices;
- embedded native libraries;
- signer fingerprint.

Then compare findings with source/configuration.

## Termux role

Termux can organize APK hashes, notes, scripts, JSON/XML processing, local HTTP endpoints, and source repositories. Android sandbox restrictions may prevent direct inspection of another app's private runtime state; use emulator/debug tooling designed for the tested app rather than attempting to bypass the OS.

## Guided study workflow

### Before you begin

Complete Modules 17, 28–31, 39, 53–56, 63–67, and 78.

### Practice task

Analyze an Android app you built or a recognized training APK. Produce an exported-component map, data-storage inventory, network trust model, and one secure-code improvement.

### Evidence to keep

APK hash, signer fingerprint, manifest excerpts, component graph, source/decompiler comparison, and remediation note.

### Common mistakes to avoid

- treating obfuscation as secret protection;
- assuming deep-link verification equals authorization;
- exposing WebView bridges to arbitrary content;
- bypassing sandbox/debug restrictions in third-party apps;
- hard-coding secrets in client packages.

### Mastery check

Trace one external intent or deep link from entry point to data/action and identify every authorization/validation boundary.

### Continue with

Modules **83, 84, and 85**.
