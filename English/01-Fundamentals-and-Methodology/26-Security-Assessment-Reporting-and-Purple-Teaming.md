# Security Assessment Reporting and Purple Teaming

> **Purpose:** Make security testing measurable, reproducible, and useful to engineering and operations teams.

## Evidence quality

Capture asset/environment, timestamp/timezone, exact condition, sanitized evidence, test identity/role, expected versus actual behavior, impact, remediation, and retest criteria. Avoid evidence that exposes unrelated secrets or personal data.

## Finding anatomy

1. **Title:** security condition, not tool name.
2. **Summary:** what is wrong.
3. **Affected assets:** exact scope.
4. **Evidence:** enough to reproduce safely.
5. **Impact:** realistic consequences.
6. **Likelihood/context:** exposure, prerequisites, controls.
7. **Remediation:** specific feasible actions.
8. **Validation:** how to prove the fix.

## Attack paths

Multiple moderate weaknesses can combine into high impact. Map prerequisites and trust boundaries, and distinguish confirmed observations from inference.

## Purple teaming

Purple teaming is collaboration between offensive and defensive roles to improve controls and visibility.

### Exercise loop

1. Choose a behavior to validate.
2. Define expected telemetry.
3. Generate a benign or lab-contained simulation.
4. Observe what defenders receive.
5. Improve prevention/logging/analytics/runbooks.
6. Re-test.
7. Record the control improvement.

## Metrics that matter

Track critical-asset telemetry coverage, detection coverage, alert precision, time to triage/contain, retest closure, recurrence of fixed root causes, and findings without an owner or deadline.

## Rules of engagement

A professional assessment begins with written scope and authority. Record in-scope assets, excluded assets, testing window, source addresses if relevant, allowed and prohibited techniques, data-handling requirements, contacts, stop conditions, evidence-retention period, and escalation process. Ambiguity should be resolved before a high-impact action, not after it.

### Stop conditions

Examples include unexpected production instability, access to unrelated sensitive data, evidence that a third party owns the system, impact beyond the agreed environment, or a request from the designated incident contact. A stop condition protects both the client and the assessment team.

## Assessment planning

Organize work around objectives and attack surface rather than a checklist of tools. Typical workstreams include external exposure, identity, network services, web/API, cloud configuration, endpoint controls, wireless, mobile, source/build pipeline, and detection validation. Not every engagement needs every workstream.

For each workstream, define:

- objective and business context;
- assets and owners;
- test identities/roles;
- assumptions;
- evidence needed;
- safety constraints;
- completion criteria.

## Evidence standards

Strong evidence is reproducible but minimized. Capture only what proves the condition. If a broken authorization check exposes a record, one synthetic or specifically authorized record is preferable to bulk extraction. Mask tokens, passwords, API keys, personal data, and unrelated customer content in screenshots and reports.

Each artifact should be traceable to the finding and timestamp. Keep raw evidence in a restricted location and publish sanitized evidence in the report.

## Risk rating

A numerical score can support consistency but should not replace context. Consider exploit prerequisites, exposure, privileges required, user interaction, control bypass, data sensitivity, business criticality, blast radius, detection capability, known exploitation, and remediation difficulty. Explain why the rating matters to the organization.

If CVSS is used, record the vector and version rather than only a decimal score. Supplement it with environmental/business context so readers understand why two technically similar findings may have different priorities.

## Writing actionable findings

A useful title states the condition and affected boundary, for example **“Cross-tenant object authorization missing in invoice API”** rather than **“IDOR”** or **“Burp finding.”** The report should let an engineer reproduce the control failure safely and let a manager understand consequence and priority.

### Example finding structure

**Condition:** The API verifies that a caller is authenticated but does not verify ownership of an invoice object before returning it.

**Evidence:** User A requests their own synthetic invoice and receives HTTP 200. With only the object identifier changed to User B's test invoice, the same session also receives HTTP 200.

**Impact:** A user could access another tenant's invoice data if object identifiers become known or predictable.

**Remediation:** Enforce object-level authorization using the authenticated tenant/user context on every read and write. Centralize the check where practical and add cross-tenant negative tests.

**Retest:** Repeat the authorized test with User A against User B's synthetic object and confirm denial plus appropriate logging.

The example proves the issue without instructing readers to enumerate or extract real third-party data.

## Executive summary

The executive summary should answer:

1. What was assessed?
2. What was the overall security posture relative to the stated objectives?
3. Which few risks matter most?
4. Are those risks isolated bugs or systemic patterns?
5. What should leadership prioritize next?

Avoid filling the summary with scanner counts. Ten low-value informational observations do not outweigh one systemic identity flaw.

## Technical appendix

A technical appendix can contain methodology, tools and versions, test accounts, timestamps, affected endpoints, sanitized requests/responses, log evidence, CVSS vectors, and retest results. Keep exploit-like detail proportional to what maintainers need to reproduce the issue safely.

## Root-cause analysis

Findings often cluster around a smaller number of root causes: missing ownership, inconsistent authorization middleware, unsafe defaults, incomplete asset inventory, weak secrets management, lack of dependency ownership, insufficient logging, or absence of security tests. Reporting these patterns can create more value than treating every symptom as unrelated.

## Purple-team planning

A purple-team exercise should have a control-improvement objective, not an objective to “beat the blue team.” Define the behavior, expected prevention, expected telemetry, analytic/runbook, safe simulation method, and success criteria before execution.

### Example exercise card

- **Behavior:** test account receives an unexpected privileged role.
- **Environment:** isolated staging tenant.
- **Expected prevention:** change requires approved admin workflow.
- **Expected telemetry:** actor, target, old/new role, timestamp, source context.
- **Expected alert:** high-risk privilege change outside approved workflow.
- **Simulation:** administrator assigns and removes a test role.
- **Success:** event is logged, alert routes correctly, analyst identifies actor/target, and rollback is documented.

## Retesting

A retest should verify the root condition, not only that one payload no longer works. Confirm the control applies across relevant methods, endpoints, roles, and object types. Record fixed, partially fixed, not fixed, or unable to retest, with evidence and date.

## Metrics and program improvement

Useful program metrics include median age of critical findings, percentage with named owners, retest success rate, recurrence by root cause, high-value assets without adequate telemetry, percentage of privileged identities with strong MFA, and percentage of release paths with provenance. Metrics should drive decisions rather than reward teams for generating more findings.

## Assessment closeout checklist

- [ ] Scope and authorization are archived.
- [ ] High-impact observations were communicated promptly.
- [ ] Sensitive evidence is minimized and access-controlled.
- [ ] Findings have owners and retest criteria.
- [ ] Credentials/test accounts created for the assessment are removed or transferred appropriately.
- [ ] Temporary firewall rules, agents, or debug settings are reverted.
- [ ] Data-retention and destruction commitments are scheduled.
- [ ] Lessons learned are converted into backlog items.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 05 and 15.

### Practice task

Take one safe lab finding and write three versions: technical evidence, remediation guidance for an engineer, and a concise risk summary for a manager. Keep certainty aligned with evidence.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **42, 45, 59**.
