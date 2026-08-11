# Advanced Detection Engineering and MITRE ATT&CK v19

> **Purpose:** Build detections from observable behavior, data-source reality, and testable hypotheses rather than from tool names or copied signatures.

## Learning objectives

- Convert threat behavior into data requirements and detection logic.
- Understand ATT&CK as a behavioral knowledge base, not a checklist of alerts.
- Design correlation, sequence, rarity, and stateful detections.
- Test false-positive assumptions with benign emulation.
- Track coverage and telemetry gaps explicitly.

## ATT&CK in 2026

MITRE ATT&CK **v19.2** is the current data release as of August 6, 2026. The major v19 release introduced on April 28, 2026 split the former Enterprise Defense Evasion tactic into **Stealth** and **Defense Impairment**. The v19.2 Agile update primarily refreshed Groups and Software rather than changing that tactic model.

Use the current ATT&CK website/data as the source of truth for technique IDs and relationships. Do not hard-code old tactic assumptions into long-lived analytics without version tracking.

## Start with behavior

A useful detection statement has this shape:

**When subject/process/workload X performs observable behavior Y under context Z, the combination is unusual or policy-violating because reason R.**

Then ask which telemetry can prove each part. If no data records the behavior, writing a query first is premature.

## Detection pipeline

1. Threat/behavior hypothesis.
2. Required data source and fields.
3. Collection validation.
4. Normalization.
5. Candidate logic.
6. Benign test data/emulation.
7. False-positive review.
8. Severity/context enrichment.
9. Alert routing and analyst procedure.
10. Versioning/tuning/retirement.

A detection is a maintained software artifact.

## Atomic versus correlated analytics

An **atomic** detection triggers on one event. A **correlated** detection combines events over time, identity, host, process tree, session, workload, or resource.

Examples of safe correlation concepts:

- privileged group change followed by privileged sign-in;
- new service configuration followed by service start;
- cloud role grant followed by sensitive API use;
- unusual child process followed by outbound connection;
- security control configuration change followed by telemetry loss.

Correlation often improves context but introduces state, timing, and data-quality complexity.

## Sequence detections

Some behaviors are suspicious because of order. Define expected time window, entity key, allowed interruptions, and reset conditions. Sequence logic can be brittle if clocks are skewed or event ingestion is delayed.

Always distinguish event time from ingest time.

## Rarity and baseline

Rarity can surface unusual process paths, parents, cloud APIs, geolocations, authentication methods, or service-account activity. But “rare” is not “malicious.” Baselines change with software releases and business cycles.

Use rarity to prioritize evidence, not as sole conviction.

## Entity context

Enrichment turns raw events into security meaning. Useful context includes asset criticality, user role, device management state, signer reputation, known automation, vulnerability exposure, network zone, tenant, and change-ticket context.

Enrichment should be versioned and explainable so analysts know why severity changed.

## Detection of defense impairment

Defense impairment covers actions that degrade logging, endpoint protection, firewall policy, cloud audit, authentication controls, or other security mechanisms. Build high-confidence alerts for unauthorized state changes to critical controls.

Avoid relying only on “absence of logs,” which can also result from pipeline failure. Pair telemetry health monitoring with configuration/audit events.

## Stealth-related behavior

Stealth behavior attempts to reduce observable signals or blend into expected activity. Defensive analytics should emphasize invariant violations and cross-source correlation rather than trying to guess every evasion trick.

Do not publish step-by-step evasion recipes in a training guide. Study the ATT&CK behavior descriptions and map them to telemetry/mitigations.

## Data quality

For every source document:

- who/what emits it;
- field semantics;
- timestamp source/timezone;
- retention;
- delay/drop behavior;
- identity/hostname stability;
- parsing/normalization transformations;
- known blind spots;
- sampling/filtering.

A perfect query over unreliable data is an unreliable detection.

## Sigma and portable logic

Sigma provides a portable rule representation for many log detections. Treat portable rules as source code requiring adaptation to your schema and environment. Field names, event IDs, command-line availability, and audit policy vary.

Test translated rules against real benign data before deployment.

## Network detections

Network analytics can use DNS, flow, TLS metadata, HTTP proxy logs, firewall events, and protocol-specific telemetry. Encrypted traffic reduces payload visibility but still leaves useful metadata depending on environment/privacy policy.

Focus on policy violations and unusual relationships rather than trying to decrypt traffic you are not authorized to inspect.

## Identity detections

High-value identity analytics include changes to privileged groups/roles, new credentials, impossible policy transitions, unusual service-account use, risky delegation changes, repeated authentication anomalies, and abnormal role-assumption chains.

Identity events need context from directory/cloud role state to avoid stale interpretations.

## Detection testing

Use benign simulations that create the intended telemetry without harmful payloads. Examples: create/delete a test local user, start a harmless test service, perform a denied cloud sandbox API action, or modify a lab logging setting and immediately restore it.

Record expected events before running the test. If the detection fails, determine whether the behavior did not emit data, collection dropped it, normalization lost fields, or logic is wrong.

## False positives and tuning

Do not simply exclude entire directories/users to quiet a rule. Understand legitimate behaviors and narrow with stable context: signer, managed software inventory, service account, approved automation, parent process, destination class, or change window.

Every suppression is a blind spot that should be documented and reviewed.

## Detection-as-code

Store rules, tests, sample sanitized events, metadata, owner, ATT&CK mapping, severity, data dependencies, and change history in version control. CI can lint rules and run test fixtures.

A rule without an owner and validation history decays quickly.

## Coverage metrics

ATT&CK technique counts are not sufficient. Better measures include:

- percentage of prioritized behaviors with validated telemetry;
- percentage with tested detections;
- false-positive burden;
- time from telemetry failure to detection;
- alert-to-investigation conversion;
- time since last validation;
- critical assets lacking expected data.

## Guided study workflow

### Before you begin

Complete Modules 12, 23, 26, 47, 59, 72–76, and 79.

### Practice task

Choose one benign behavior in a lab. Write the threat hypothesis, required fields, sample event, detection logic, expected false positives, and test procedure. Validate end-to-end collection.

### Evidence to keep

Rule/query, fixture event, ATT&CK version/mapping, test output, tuning notes, and telemetry dependency list.

### Common mistakes to avoid

- copying ATT&CK technique names directly into alerts;
- writing logic before verifying data exists;
- treating rarity as maliciousness;
- suppressing broad categories to reduce noise;
- testing evasion instead of validating observability.

### Mastery check

Explain the difference between technique coverage, telemetry coverage, and validated detection coverage, and demonstrate one end-to-end test.

### Continue with

Modules **81, 84, and 85**.
