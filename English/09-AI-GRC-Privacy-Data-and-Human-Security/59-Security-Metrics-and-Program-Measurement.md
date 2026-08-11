# Security Metrics and Program Measurement

> **Purpose:** Measure whether security work is reducing risk and improving capability instead of counting activity for its own sake.

## Learning objectives

- Distinguish activity, output, outcome, risk, and control-effectiveness metrics.
- Design metrics with clear definitions and data sources.
- Avoid vanity metrics and misleading averages.
- Connect technical telemetry to management decisions.

## Activity is not outcome

Examples of activity metrics:

- number of scans run;
- number of alerts generated;
- number of training sessions delivered;
- number of tickets opened.

These can describe workload but do not prove improved security. Outcome-oriented questions include:

- Are critical exposed vulnerabilities remediated faster?
- Are high-risk identities better protected?
- Are backups more reliably recoverable?
- Are detections finding meaningful events with manageable noise?
- Is the attack surface shrinking?

## Define every metric

A useful metric has:

- name;
- purpose/decision it supports;
- exact numerator/denominator where relevant;
- data source;
- collection frequency;
- owner;
- target/threshold;
- known limitations;
- segmentation dimensions such as severity/business unit/asset class.

## Vulnerability metrics

Better than “open vulnerabilities” alone:

- age by risk tier;
- externally exposed critical findings;
- known-exploited vulnerabilities overdue;
- remediation SLA attainment by asset criticality;
- reopen/regression rate;
- time from asset discovery to first assessment;
- accepted-risk inventory and expiration.

## Detection/SOC metrics

Consider:

- coverage of prioritized threat behaviors;
- alert precision/false-positive burden;
- time to triage;
- time to meaningful containment;
- percentage of detections with documented response playbooks;
- detection regression-test success;
- telemetry gaps.

Be careful with simple “MTTD/MTTR” averages. Averages can hide long-tail incidents; medians/percentiles and severity segmentation are often more informative.

## Identity metrics

Examples:

- privileged accounts with phishing-resistant MFA;
- stale/inactive accounts;
- standing privilege versus just-in-time access;
- orphaned service accounts;
- secrets/certificates approaching expiration;
- access-review completion and exception age.

## Recovery metrics

Security resilience requires measured recovery:

- backup success is not enough;
- restore-test success rate;
- observed recovery time versus RTO;
- restored data point versus RPO;
- percentage of critical services with tested runbooks;
- dependencies missing from recovery exercises.

## Application-security metrics

Useful examples:

- security requirements covered by automated tests;
- authorization negative-test coverage;
- high-risk dependency age;
- secrets detected before merge;
- time to remediate production findings;
- percentage of critical services with current threat models;
- recurrence rate of previously fixed vulnerability classes.

## Risk indicators

Key risk indicators should have a plausible relationship to risk. Examples include unsupported critical systems, internet-exposed admin interfaces, stale privileged credentials, untested backups, or high-value services without logs.

## Dashboard guidance

A dashboard should answer a decision question. Avoid putting dozens of unrelated numbers on one screen. Show trend, target, exception, owner, and context. Make it possible to drill into the underlying evidence.

## Metric anti-patterns

- counting alerts as success;
- rewarding teams for closing tickets without verifying fixes;
- comparing vulnerability counts between environments of very different size;
- using a single risk score without asset/exposure context;
- hiding uncertainty/data gaps;
- setting targets that encourage under-reporting;
- measuring only what is easy to count.

## Safe lab

Create synthetic monthly data for vulnerabilities, restore tests, and detection alerts. Build a small Python report that calculates medians, percentages, overdue items, and trend direction. Then write three management decisions that the metrics support.

## Checkpoint

You should be able to explain how a metric could be gamed and what evidence would validate that it represents a real improvement. Continue with Modules 42, 47, 48, and 50.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 42, 47, 48, and 50 help.

### Practice task

Create synthetic monthly security data and build a simple report that shows trend, target, exception, owner, and decision supported. Identify how each metric could be gamed.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **42, 47, 48, 50**.
