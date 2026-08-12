# Governance, Risk, Compliance and Privacy

> **Purpose:** Connect technical security work to ownership, business risk, policy, privacy, assurance, and measurable outcomes.

## Governance

Governance defines who makes cybersecurity decisions, who owns risk, how priorities are set, and how accountability is demonstrated. NIST CSF 2.0 explicitly includes **Govern** alongside Identify, Protect, Detect, Respond, and Recover.

Technical teams need clear policy owners and exception processes. “Security says no” is not a governance model.

## Risk

A practical risk statement describes:

- asset/process;
- threat/event;
- weakness or exposure;
- business impact;
- likelihood/context;
- existing controls;
- owner;
- treatment decision.

Risk treatment options generally include mitigate, avoid, transfer/share, or accept. Acceptance should be explicit, time-bounded where appropriate, and owned at the right level.

## Asset and data classification

You cannot protect everything identically. Define classes for business information and systems, then map handling requirements such as encryption, access, retention, backup, and sharing.

## Policies, standards, procedures, guidelines

- **Policy:** management intent and mandatory direction.
- **Standard:** specific mandatory requirements.
- **Procedure:** steps to perform an activity.
- **Guideline:** recommended practice.

Keep them distinguishable so audits and operators know what is required.

## Control frameworks

Frameworks organize outcomes and controls, but implementation must match business context. Examples include NIST CSF, NIST SP 800-53, ISO/IEC 27001 ecosystems, CIS Controls, and sector-specific requirements.

Compliance is evidence that defined requirements were met at a point or period in time; it is not proof that an organization cannot be compromised.

## Privacy engineering

Privacy involves more than confidentiality. Ask:

- Why is personal data collected?
- Is the amount proportionate?
- Who can use it?
- How long is it retained?
- Where is it transferred?
- Can inaccurate data be corrected?
- Can unnecessary data be deleted?
- What happens during an incident?

Data minimization reduces both privacy risk and breach impact.

## Third-party risk

Vendors can become identity providers, data processors, code suppliers, remote administrators, or operational dependencies. Due diligence should match the service's access and criticality.

Track contract/security requirements, data flows, subprocessors, breach notification obligations, access methods, and exit/termination processes.

## Exceptions

Security exceptions should record:

```text
Requirement:
Reason:
Scope:
Compensating controls:
Risk owner:
Approval:
Expiry/review date:
Remediation plan:
```

Permanent undocumented exceptions become hidden architecture.

## Metrics

Useful metrics connect to outcomes, for example:

- percentage of critical assets with known owners;
- MFA coverage for privileged accounts;
- restore-test success rate;
- median time to revoke departing-user access;
- high-risk findings past SLA;
- detection rules with recent validation;
- unsupported systems remaining.

Avoid vanity metrics such as raw alert volume without quality context.

## Risk register lab

Create five fictional risks for a small SaaS company. Assign owner, business impact, current controls, treatment, target date, and measurable residual-risk indicator. Include one accepted risk and justify why acceptance is reasonable.

**Learning goal:** translate technical observations into accountable business decisions.

## Primary reference

- NIST CSF 2.0: https://www.nist.gov/cyberframework

## Governance and risk depth

Governance defines who makes cybersecurity decisions, based on what evidence, with which accountability. Risk management connects technical conditions to objectives and treatment decisions.

### Risk statement structure

A useful risk statement describes a cause/threat, affected asset/process, unwanted event, and impact. Record existing controls, evidence, likelihood/context, impact, owner, treatment, due date, and residual risk.

### Treatment choices

Risks may be reduced, avoided, transferred/shared, or accepted according to governance. “Accepted” should mean a responsible owner understands the residual risk and review/expiration conditions—not that a ticket was closed without remediation.

### Control evidence

Policies are not proof of implementation. Evidence can include configuration, logs, tests, access reviews, restore exercises, training records, vulnerability verification, or independent assessment. Define how frequently evidence must be refreshed.

### Privacy integration

Security and privacy overlap but are not identical. Data minimization, purpose limitation, user transparency, retention, and lawful/organizational requirements should be considered alongside confidentiality/integrity/availability controls.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Module 01 and basic organizational context.

### Practice task

Create a small risk register for a fictional organization, link each risk to owner, controls, evidence, treatment, review date, privacy impact, and residual risk.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **43, 45, 59**.
