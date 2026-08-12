# SOC, SIEM, SOAR and Detection Operations

> **Purpose:** Understand how security operations turns telemetry into validated detections, investigations, response actions, and continuous improvement.

## SOC operating model

A Security Operations Center is a capability, not just a room or product. It combines people, processes, telemetry, detections, case management, threat context, response authority, and measurement.

## Telemetry pipeline

Typical stages:

1. source generates event;
2. collector receives it;
3. parser/normalizer extracts fields;
4. storage/index retains it;
5. detection logic evaluates it;
6. alert/case is created;
7. analyst investigates;
8. response action is authorized;
9. lessons feed back into controls.

Failures at any stage can create blind spots.

## SIEM

A SIEM centralizes and correlates security-relevant logs. More ingestion is not always better. Prioritize high-value sources and ensure fields are parsed consistently.

For each log source record:

- owner;
- source system;
- event types;
- timestamp/timezone;
- retention;
- parser status;
- expected volume;
- security use cases;
- health monitoring.

## Detection engineering

A detection should have:

- threat/use-case hypothesis;
- required data;
- query/rule;
- expected true positives;
- known false positives;
- severity rationale;
- response playbook;
- test method;
- owner;
- review date.

Detection-as-code practices can add version control, peer review, tests, and rollback.

## Alert quality

Track whether alerts are actionable, not merely numerous. A useful alert contains enough context for the next decision and does not require an analyst to reconstruct basic fields manually.

## SOAR and automation

Automate deterministic, low-risk work first: enrichment, formatting, duplicate suppression, evidence collection, or ticket routing. Sensitive containment actions should have safeguards, scope checks, approvals, and rollback where possible.

## Case management

Cases need chronology, evidence, ownership, decisions, and outcomes. Preserve source links/IDs so another responder can reproduce the investigation.

## Detection coverage

Map detections to your own threat model and critical assets. ATT&CK mapping helps communication but coverage counts can be misleading if rules are untested or data is missing.

## Health monitoring

Detect failures of security controls themselves:

- agent stopped reporting;
- log volume unexpectedly zero;
- parser errors;
- time drift;
- rule disabled;
- retention failure;
- EDR exclusions changed;
- integration token expired.

## Lab — Detection lifecycle

Create synthetic authentication logs with normal logins and one benign pattern of repeated failures followed by success. Write a detection, test it against positive and negative datasets, document false positives, and create a response checklist.

Then remove a required field from the logs and document how detection quality degrades.

**Learning goal:** detection is a tested data product, not just a query.

## SOC operating model in more depth

A SOC is a feedback system, not an alert queue. Telemetry, detections, triage, investigation, response, lessons learned, and engineering changes should form a loop.

### Telemetry quality

Before writing a rule, verify that the required fields are reliably collected, timestamped, parsed, retained, and attributable to an asset/identity. A perfect query cannot compensate for missing or misleading telemetry.

### Detection lifecycle

Document hypothesis, data sources, query/rule logic, expected benign test, false-positive conditions, severity, triage steps, response ownership, and regression tests. Version detections like code.

### SOAR

Automate deterministic low-risk steps first: enrichment, ticket formatting, evidence collection, duplicate suppression. High-impact containment should have appropriate approvals and safeguards until the automation is proven reliable.

### Triage

A good triage result states what is observed, confidence, affected entities, business context, next evidence needed, and whether containment is justified. Do not equate an alert with an incident.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 12 and 23.

### Practice task

Build a synthetic event pipeline: generate events, normalize fields, write one detection, route an alert, triage it with a playbook, measure false positives, and document telemetry gaps.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **37, 38, 59**.
