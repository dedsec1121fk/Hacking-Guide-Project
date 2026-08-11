# Cybersecurity Career and Portfolio Guidance

> **Purpose:** Convert learning into demonstrable, ethical work that employers, clients, teachers, or collaborators can evaluate.

## Skills before titles

Cybersecurity roles vary widely. Instead of trying to become “a hacker,” build evidence in several foundations:

- operating systems;
- networking;
- scripting/automation;
- web/application concepts;
- identity/access control;
- logging/detection;
- vulnerability management;
- reporting;
- recovery;
- ethics/authorization.

Then specialize.

## Portfolio principles

A strong portfolio shows how you think. Good artifacts include:

- a documented Termux setup/recovery guide;
- a Python parser for synthetic logs;
- a threat model for a small app;
- a secure-code change with tests;
- a hardening checklist applied to a lab VM;
- a backup/restore exercise with measured recovery time;
- a detection rule with sample events and false-positive notes;
- a vulnerability report written against your own lab;
- an incident tabletop report;
- an SBOM/dependency review for a project you maintain.

Avoid publishing real credentials, private personal data, unauthorized findings, or code designed primarily to compromise third-party systems.

## Explain each project

Every portfolio project should answer:

1. What problem were you solving?
2. What environment did you use?
3. What security property mattered?
4. What did you build/test?
5. What evidence showed the result?
6. What did you improve?
7. What limitations remain?
8. What would you do next?

## GitHub hygiene

Keep repositories understandable:

- clear README;
- setup instructions;
- license where appropriate;
- `.gitignore`;
- no secrets;
- small meaningful commits;
- screenshots only when they add evidence;
- tests/examples;
- maintenance notes.

## Role directions

### SOC / blue team

Show log analysis, detection design, incident triage, endpoint/network concepts, identity telemetry, and communication.

### Application security

Show secure coding, threat modeling, authorization tests, OWASP/ASVS mapping, API reasoning, and developer-friendly remediation.

### Security engineering

Show automation, identity, cloud/infrastructure controls, CI/CD, secrets, observability, and reliable operations.

### GRC / risk

Show risk registers, control mapping, policy writing, evidence collection, privacy reasoning, tabletop exercises, and executive communication.

### Vulnerability management

Show asset inventory, prioritization methodology, remediation tracking, exception handling, and verification—not just scanner output.

## Certifications

Certifications can structure study or help pass hiring filters, but they are not substitutes for skills. Choose certifications based on the role you want, local employer requirements, cost, and the amount of practical work in the curriculum. Re-check exam versions/objectives before paying because certification programs change.

## Interview preparation

Practice explaining fundamentals out loud:

- authentication versus authorization;
- hash versus encryption;
- TCP versus UDP;
- DNS resolution;
- what happens when a browser visits an HTTPS URL;
- least privilege;
- how to prioritize vulnerabilities;
- what makes a useful alert;
- how to contain an incident without destroying evidence;
- how to prove a backup is usable.

Use examples from your own labs.

## Professional communication

A technically correct finding can still fail if the reader cannot act on it. Reports should identify impact, evidence, affected scope, likelihood/context, remediation, verification, and limitations. Avoid dramatic language when evidence is weak.

## 30-day portfolio plan

### Week 1
Termux/Linux foundations + notes repository.

### Week 2
Python synthetic-log parser + unit tests.

### Week 3
Small local web/API project + threat model + authorization tests.

### Week 4
Write one assessment report and one incident tabletop report; clean the repositories and publish only sanitized material.

## Checkpoint

You should be able to show at least three artifacts that demonstrate different skills and explain every line of code/configuration you claim as your work. Continue with Module 45 for capstones and Module 26 for reporting.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Complete a few hands-on modules first.

### Practice task

Publish or prepare three sanitized portfolio artifacts: one automation project, one security analysis/report, and one recovery/detection project. Explain limitations and what you personally built.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **26, 45**.
