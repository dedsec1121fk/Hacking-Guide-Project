# Detection Engineering, Incident Response, and Threat Hunting

> **Purpose:** Turn telemetry into reliable security outcomes and build a repeatable process for investigation, containment, recovery, and learning.

## Detection engineering lifecycle

1. Define the behavior or risk to detect.
2. Identify required telemetry and fields.
3. Build analytic logic with explicit assumptions.
4. Generate benign test events in a lab.
5. Validate parsing, enrichment, severity, and routing.
6. Document investigation steps and likely false positives.
7. Measure alert volume, precision, time-to-triage, and coverage gaps.
8. Revalidate after environment/parser changes.

## Telemetry layers

Correlate endpoint, identity, DNS/proxy/firewall, cloud control-plane, application/API, email, asset, vulnerability, and ownership context.

## Incident response lifecycle

### Preparation

Define severity, contacts, evidence handling, escalation, backup strategy, and decision authority before an incident.

### Detection and analysis

Establish what happened, when, affected identities/assets, likely path, data at risk, and confidence. Preserve important evidence before disruptive actions where feasible.

### Containment

Contain according to business impact and evidence needs—for example disabling a test/compromised account, isolating a host, revoking tokens, or disabling a vulnerable feature. Record what changed and why.

### Eradication and recovery

Remove persistence/root cause, rotate affected credentials, patch/reconfigure, restore from known-good sources, and monitor for recurrence.

### Lessons learned

Turn control failures, detection delays, and communication gaps into owned engineering work.

## Threat hunting

A hunt begins with a hypothesis, not a random query. Define the data needed, query period, expected normal behavior, and conditions that would support or falsify the hypothesis.

## Safe exercise

Generate a benign event such as creating/removing a local test account. Verify which logs record it and build a simple timeline.

## Designing useful telemetry

A log is useful only when it can answer investigation questions. For security-relevant events, useful fields often include timestamp with timezone, actor identity, source context, target resource, action, outcome, authentication method, session or request identifier, application/service name, and enough correlation data to connect events across systems. Avoid logging secrets, session tokens, full credentials, or unnecessary personal data.

### Time and normalization

Incident timelines fail quickly when clocks, timezones, usernames, hostnames, and field names are inconsistent. Centralize time synchronization, preserve original event timestamps, normalize carefully, and retain raw events when feasible. A parser change should be treated as a production change because it can silently break analytics.

## Detection engineering from behavior

A useful detection describes a security-relevant behavior and the evidence expected to accompany it. Avoid rules that merely search for a famous tool name. Tools change; behaviors often persist.

For each analytic, document:

- **Objective:** what risky behavior should be visible?
- **Data requirement:** which sources and fields are mandatory?
- **Logic:** what combination or sequence is suspicious?
- **Scope:** which hosts, identities, applications, or environments apply?
- **Exceptions:** what legitimate workflows resemble the behavior?
- **Severity:** what changes urgency?
- **Triage:** what should an analyst check first?
- **Containment:** what low-risk actions are available?
- **Validation:** how can a benign simulation prove the analytic still works?

## Detection coverage mapping

Frameworks such as MITRE ATT&CK can help organize hypotheses and communicate behavioral coverage, but a technique label is not proof that a detection is effective. Coverage should be tied to actual telemetry, validated analytics, environments, and test evidence. Record whether coverage is preventive, detective, investigative only, or currently absent.

A mature matrix might distinguish:

- telemetry exists but is not centralized;
- telemetry is centralized but not parsed;
- a query exists but has never been tested;
- an alert is tested but noisy;
- an alert is reliable and has a runbook;
- prevention blocks the behavior and detection confirms the block.

## Alert triage

Triage should reduce uncertainty quickly. Start with identity, asset criticality, event sequence, recent changes, known administrative activity, and whether the behavior is isolated or widespread. Avoid irreversible containment before understanding the likely impact unless immediate action is necessary to protect systems or people.

### A compact triage structure

1. **What triggered?** State the observed behavior, not the alert title alone.
2. **Who/what is involved?** Identify user, service, host, application, and resource.
3. **Is it expected?** Check change windows, automation, and known maintenance.
4. **What happened immediately before and after?** Build a local timeline.
5. **What is the potential blast radius?** Determine accessible resources and shared credentials.
6. **What evidence must be preserved?** Protect logs and volatile evidence as appropriate.
7. **What containment is proportionate?** Prefer reversible actions when possible.

## Incident severity

Severity should combine technical impact with business context. A low-complexity event on a public training system may be less urgent than suspicious authentication to a privileged production identity. Define criteria before incidents so teams do not invent severity under pressure.

Useful inputs include affected data, privilege level, persistence, number of assets, production impact, regulatory obligations, confidence, active adversary behavior, and availability of compensating controls.

## Evidence handling

Maintain an evidence log for important incidents: source, acquisition time, collector, method, hash where appropriate, storage location, and any transformations. Work from copies when possible. Clearly distinguish observed facts, analyst interpretation, and unverified hypotheses.

## Containment strategy

Containment is a business decision as well as a technical one. Options can include revoking sessions, resetting or disabling an identity, isolating a host, blocking an integration, restricting network paths, disabling a vulnerable feature, rotating a secret, or temporarily increasing monitoring. Record the expected effect and rollback plan.

## Recovery and validation

Recovery should address both the immediate compromise and the root cause. Restoring a server without rotating exposed credentials or correcting the vulnerable configuration simply resets the clock. Define explicit recovery criteria: patched state, credential rotation, policy correction, known-good configuration, restored monitoring, backup validation, and observation period.

## Threat hunting methodology

A hunt should be falsifiable. Example hypothesis: “A compromised service identity would show access to resource types outside its normal automation role.” Required data might include service identity, resource, action, outcome, and historical baseline. The hunt then looks for deviations and records whether they were malicious, benign, or unexplained.

Hunts can originate from intelligence, incident lessons, control gaps, unusual telemetry, or high-value asset reviews. The best outcome is often not “we found an attacker,” but “we discovered a logging gap, ownership problem, or behavior that deserves a durable analytic.”

## Tabletop exercise

Use a fictional scenario: a privileged cloud account authenticates from an unusual device, creates a new credential, and changes a logging policy. Ask participants to identify the first five facts they need, which logs should exist, which actions they would take immediately, what requires approval, and how they would prove recovery. Capture gaps as engineering tasks with owners and deadlines.

## Detection maintenance

Review analytics after major platform upgrades, parser changes, identity migrations, network redesigns, and incidents. Retire rules that no longer represent real risk. Version control detection logic and runbooks where practical so changes are attributable and reversible.

## Primary reference

- MITRE ATT&CK — https://attack.mitre.org/

## 2026 incident-response update — NIST SP 800-61 Rev. 3

NIST finalized SP 800-61 Revision 3 in April 2025. The revision integrates incident response with cybersecurity risk management and the six NIST CSF 2.0 Functions rather than treating preparation, detection, response, and recovery as an isolated linear process. Use incident lessons learned to improve governance, identification, protection, detection, response, and recovery capabilities continuously.

Primary reference: https://csrc.nist.gov/pubs/sp/800/61/r3/final

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 05, 07, 08, and 12.

### Practice task

Use synthetic logs to build an incident timeline, separate facts from hypotheses, choose proportional containment, and write recovery plus lessons-learned actions.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **37, 38, 47, 48**.
