# Responsible Disclosure and Bug Bounty Ethics

> **Purpose:** Learn how to report vulnerabilities safely and professionally while respecting authorization boundaries.

## Authorization first

A public website, IP address, mobile app, or API is not automatically permission to test. Authorization comes from ownership, a contract, a written testing agreement, or a published vulnerability disclosure/bug bounty policy whose scope includes the system and technique.

Read the policy before testing.

## Scope

A good program defines:

- in-scope domains/apps/APIs;
- out-of-scope systems;
- allowed techniques;
- prohibited impact;
- rate limits;
- data handling rules;
- test account requirements;
- reporting channel;
- disclosure timeline;
- reward eligibility if applicable.

When scope is ambiguous, do not expand it yourself.

## Minimize impact

Prove a vulnerability with the least invasive evidence. Do not access additional records merely to demonstrate that more records might be accessible. Use your own accounts and synthetic data whenever possible.

Do not persist, pivot, disrupt, delete, alter unrelated data, or collect credentials beyond what is necessary for an authorized proof.

## Stop conditions

Stop and report when you encounter:

- real user personal data beyond minimal proof;
- credentials/secrets belonging to others;
- production instability;
- an out-of-scope asset;
- evidence of an unrelated active compromise;
- a technique explicitly prohibited by policy.

## High-quality report

A report should include:

1. concise title;
2. affected asset/version;
3. authorization/scope context;
4. preconditions;
5. reproducible minimal steps;
6. expected versus actual behavior;
7. impact in realistic terms;
8. minimal redacted evidence;
9. remediation idea;
10. retest notes when fixed.

Avoid inflated severity and dramatic language. Clear evidence is more persuasive.

## Duplicate and known issues

Programs may already know about a finding. Maintain your own notes so you can explain what you tested and when. Do not attempt to make a duplicate “more serious” by increasing impact.

## Disclosure

Coordinated vulnerability disclosure balances user protection, vendor remediation, researcher credit, and public interest. Follow program terms and applicable law. If no policy exists, use a vendor security contact or recognized coordination channel and minimize further testing.

## Data retention

Delete collected test data when the program requires it and keep only the evidence necessary for the report. Protect reports because they may contain sensitive details before remediation.

## Safe practice

Use intentionally vulnerable platforms, CTFs, and your own applications to practice reproduction and report writing. The professional skill is demonstrating the flaw safely, not maximizing access.

## Reporting lab

Take a fictional broken-access-control issue in a toy app. Write a complete report using only User A and User B accounts you created. Include minimal request/response evidence and a server-side authorization recommendation.

**Learning goal:** show impact without harming unrelated users.

## Disclosure workflow in more depth

Responsible disclosure starts with scope. Read the program policy before testing: eligible assets, excluded techniques, rate limits, data handling, safe harbor, disclosure timing, duplicate rules, and contact method.

### Minimize impact

Use the least invasive proof that demonstrates the issue. Avoid accessing more records than necessary, changing other users' data, creating persistence, interrupting services, or collecting credentials. If a safe proof is impossible within scope, report the hypothesis and supporting evidence rather than escalating recklessly.

### Report quality

A strong report contains clear affected asset/version, prerequisites, minimal reproduction in the authorized environment, expected versus actual behavior, evidence, impact, remediation direction, and cleanup. Separate confirmed facts from assumptions.

### Stop and disclose

If testing unexpectedly exposes sensitive data, crosses into an excluded asset, or risks production impact, stop. Preserve minimal evidence, avoid further exploration, and use the program's escalation path.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 15, 26, and legal/authorization concepts.

### Practice task

Write a responsible-disclosure template for a fictional finding: affected scope, reproducible safe evidence, impact, remediation, timeline, and data-handling statement.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **26, 42, 57**.
