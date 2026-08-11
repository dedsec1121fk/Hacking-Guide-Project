# Capstones, Checklists and Study Roadmaps

> **Purpose:** Turn the handbook into a progression of demonstrable skills instead of a collection of notes.

## How to use this module

Choose a learning path, complete small labs, then complete at least one capstone. Keep all targets local, owned, deliberately vulnerable, or explicitly authorized.

## Beginner roadmap

1. Security fundamentals and networking.
2. Linux/Termux foundations.
3. Python/Git workflow.
4. Web and API concepts.
5. Identity and access control.
6. Vulnerability analysis.
7. Logging/detection basics.
8. Reporting.

Evidence of progress should be projects and explanations, not just tool installation screenshots.

## Blue-team roadmap

Study:

- asset inventory;
- Windows/Linux logging;
- identity telemetry;
- endpoint controls;
- network visibility;
- detection engineering;
- incident response;
- threat hunting;
- forensics;
- ransomware recovery;
- cloud/SaaS logs.

Capstone: build a synthetic incident, generate logs, detect it, investigate it, contain it in the lab, recover, and write lessons learned.

## Application-security roadmap

Study:

- HTTP/TLS;
- authentication/session management;
- authorization;
- input/output handling;
- APIs;
- OAuth/OIDC;
- ASVS;
- secure coding;
- threat modeling;
- software supply chain;
- CI/CD and container security.

Capstone: build a small web app, define security requirements, write negative tests, generate an SBOM, threat model it, fix findings, and produce an assessment report.

## Cloud/DevSecOps roadmap

Study:

- IAM;
- network boundaries;
- secret management;
- infrastructure as code;
- containers/Kubernetes;
- logging;
- software provenance;
- CI/CD identity;
- vulnerability prioritization;
- backup/recovery.

Capstone: deploy a local or authorized sandbox application through a pipeline with policy checks, least-privilege identity, logs, and rollback.

## Termux/mobile roadmap

1. Module 28 — Foundations.
2. Module 29 — Python/Git/automation.
3. Module 30 — Networking/SSH/local services.
4. Module 31 — Lab operations/troubleshooting.
5. Module 36 — Python security automation.
6. Module 27 — Authorized labs.
7. Use `Hacking Guide Project.py` to search and review the full guide offline.

Capstone: create a portable defensive notebook in Termux containing local search, file integrity, synthetic log analysis, and documentation.

## Security assessment checklist

### Before

- Written authorization.
- Scope and exclusions.
- Contacts and escalation.
- Allowed techniques.
- Time windows.
- Data-handling requirements.
- Stop conditions.
- Test accounts.
- Evidence plan.

### During

- Verify target before every action.
- Minimize data access.
- Keep timestamps/notes.
- Preserve important evidence.
- Avoid production impact.
- Report critical safety issues promptly.

### After

- Validate findings.
- Remove test artifacts.
- Protect/delete collected data as required.
- Write remediation-oriented reports.
- Retest fixes.
- Record lessons learned.

## Incident-response checklist

- Confirm and classify.
- Establish incident leadership.
- Preserve evidence proportionately.
- Contain identities/endpoints/services.
- Determine scope.
- Protect recovery systems.
- Eradicate root causes.
- Restore from known-good state.
- Monitor for recurrence.
- Complete lessons learned.

NIST SP 800-61 Rev. 3 integrates incident response across the CSF 2.0 Functions rather than treating response as an isolated activity.

## Secure software release checklist

- Threat model updated.
- Security requirements tested.
- Authorization negative tests passing.
- Secrets scan clean.
- Dependencies/SBOM reviewed.
- High-risk vulnerabilities dispositioned.
- Build provenance/permissions reviewed.
- Production configuration checked.
- Logging/alerts ready.
- Backup/rollback verified.
- Incident owner known.

## Capstone 1 — Defensive home lab

Build a private lab with one Linux host, one Windows host if available, a small application, centralized synthetic logs, and documented users. Demonstrate inventory, hardening, backup, logging, one benign detection test, and recovery.

## Capstone 2 — Secure API

Build a localhost API with authentication, object-level authorization, rate limits, input schema validation, structured logs, and tests. Threat model it and map controls to relevant OWASP API/ASVS requirements.

## Capstone 3 — Digital forensics notebook

Create synthetic evidence from three sources, hash it, normalize timestamps, construct a timeline, distinguish fact from inference, and write a concise incident report.

## Capstone 4 — Threat intelligence brief

Using public non-sensitive sources about a historical campaign, write a two-page brief with intelligence requirements, source grading, ATT&CK mapping, detection ideas, confidence, and limitations. Do not collect private personal information.

## Capstone 5 — Ransomware tabletop

Run a tabletop for a fictional organization. Define roles, backup dependencies, identity recovery, legal/comms decisions, RPO/RTO, clean-room recovery, and evidence requirements.

## Capstone 6 — Termux security companion

Use `Hacking Guide Project.py` plus your own safe local utilities to create a mobile study workspace. Required features:

- offline guide search;
- project notes;
- Git history;
- integrity checker;
- synthetic log parser;
- exportable Markdown report;
- setup/recovery instructions.

## What mastery looks like

You should be able to explain:

- why a control exists;
- what threat it addresses;
- what evidence proves it works;
- what it does not protect against;
- how it fails;
- how to recover;
- how to communicate the residual risk.

That is more valuable than memorizing hundreds of commands.

## Turning roadmaps into a weekly system

A roadmap works only when it produces artifacts and review. Use a weekly loop:

- one concept block;
- one safe lab;
- one written explanation;
- one small automation/configuration improvement;
- one review session using `Hacking Guide Project.py` search;
- one Git commit or organized note that preserves the result.

At the end of each month, choose one old lab and repeat it from your documentation. If you cannot reproduce it, improve the documentation. If the result changes because software changed, record the version difference and update the guide notes.

## Capstone scoring rubric

Score each capstone from 0–2 in these dimensions: scope/ethics, architecture understanding, reproducibility, evidence quality, security reasoning, mitigation quality, retest/recovery, documentation, limitations, and communication. A high score requires not only a working result but evidence that another learner could understand and safely reproduce the process.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Use after completing at least one foundational path.

### Practice task

Choose one capstone and define acceptance criteria before building. Keep a decision log, evidence index, test plan, cleanup plan, and retrospective.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **Repeat with a different specialization**.
