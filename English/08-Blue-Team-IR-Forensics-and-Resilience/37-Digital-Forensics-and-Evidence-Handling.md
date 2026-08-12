# Digital Forensics and Evidence Handling

> **Purpose:** Preserve and analyze digital evidence with integrity, repeatability, and clear separation between observation and interpretation.

## Forensics principles

Digital forensics asks what can be supported by evidence. A technically plausible story is not the same as a proven timeline.

Core principles:

- minimize alteration of source evidence;
- record acquisition method and time;
- hash collected files/images where appropriate;
- maintain chain-of-custody records when required;
- work from copies when possible;
- document tools and versions;
- preserve timezone context;
- separate facts from inference.

## Order of volatility

Some evidence disappears quickly: memory, active connections, running processes, temporary data. Other evidence is relatively persistent. An incident-response collection plan should prioritize volatile evidence when doing so is safe and authorized.

Do not improvise destructive acquisition steps on a critical system. Business continuity and legal requirements may override textbook collection order.

## Timestamps

Files and logs can contain creation, modification, access, metadata-change, event, ingestion, or cloud-generated timestamps. They may use different timezones and clocks.

Normalize timelines carefully and retain the original timestamp plus source timezone when possible.

## Hashes

Cryptographic hashes are useful for proving that an evidence file has not changed between collection and later analysis. Record algorithm, value, filename, collector, and time.

## Logs as evidence

A single log source rarely tells the full story. Correlate endpoint, identity, application, network, cloud, and security-product events when available.

Absence of a log entry is not automatically proof that an action did not occur. Logging may have been disabled, filtered, delayed, or never designed to capture that event.

## Mobile evidence

Mobile devices add encryption, app sandboxing, cloud synchronization, lock state, and privacy constraints. Use established forensic procedures and lawful authority where applicable. This guide does not cover bypassing device locks or extracting third-party private data.

## Cloud evidence

Cloud platforms may provide audit logs, snapshots, object versions, identity histories, and control-plane events. Preserve relevant logs quickly because retention windows can be short or configurable.

## File metadata

Metadata can support an investigation but should be corroborated. File names, EXIF fields, author strings, and timestamps can be copied or edited.

## Evidence notes

A defensible entry contains:

```text
Evidence ID:
Source:
Collector:
Acquisition time:
Original path/resource:
Hash:
Tool/version:
Actions performed:
Observations:
Interpretation:
Limitations:
```

## Root-cause caution

The earliest event you found is not necessarily the initial cause. State “earliest observed evidence” when that is what the data supports.

## Safe lab — Synthetic timeline

Create three local text logs with UTC, local time, and offset timestamps. Include a login, file creation, configuration change, and logout. Normalize them to UTC, sort them, and label each event with source and confidence.

Then alter one copied log and show that its SHA-256 no longer matches the recorded value.

**Learning goal:** practice evidence integrity and timeline reasoning without private data.

## Reporting

A forensic report should allow another qualified analyst to understand what you collected, what you did, what you observed, and where uncertainty remains.

## Forensic reasoning in more depth

Forensics is not merely collecting files. It is preserving evidence, understanding provenance, reconstructing events, and communicating confidence.

### Provenance

For each artifact record where it came from, how it was acquired, by whom, when, with which tool/version, and whether acquisition changed the source. Hashes help demonstrate that a collected artifact has not changed after acquisition, but they do not prove the artifact was truthful or complete.

### Time

Timelines fail when analysts ignore timezone, clock drift, timestamp semantics, log ingestion delay, and differing event sources. Normalize timestamps while retaining original values. Treat “created,” “modified,” “observed,” and “ingested” as different concepts.

### Fact versus inference

Write “the log records account X authenticating at time Y” separately from “this likely indicates the attacker used account X.” The first may be evidence; the second is an interpretation that needs corroboration.

### Scope and minimization

Acquire only what is justified by the investigation and authorization. Protect sensitive case data, use access controls, maintain chain-of-custody requirements where relevant, and define retention/disposal after closure.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 23 and filesystem basics.

### Practice task

Create synthetic evidence files, hash them, preserve originals, normalize timestamps, build a timeline, and write which conclusions are fact versus inference.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **38, 48, 57**.
