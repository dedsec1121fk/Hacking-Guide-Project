# Cybersecurity Foundations and Ethical Hacking Methodology

Cybersecurity is the discipline of protecting systems, identities, software, networks, and data while preserving the ability of legitimate users to work. Ethical hacking is one part of that discipline: an authorized attempt to test security assumptions and produce evidence that helps an owner reduce risk.

> **Authorized-use boundary:** Perform practical testing only on systems, accounts, applications, networks, or devices you own or are explicitly authorized to assess. When learning, prefer localhost, disposable virtual machines, containers, emulators, synthetic accounts, and intentionally vulnerable training applications.

## Learning objectives

By the end of this module you should be able to:

- distinguish assets, threats, vulnerabilities, exposures, controls, and risk;
- explain confidentiality, integrity, availability, authenticity, accountability, and resilience;
- distinguish authentication from authorization;
- describe a modern security-assessment lifecycle;
- define scope and evidence requirements before testing;
- explain why remediation and retesting are part of ethical hacking.

## Security properties

### Confidentiality

Confidentiality limits information to authorized subjects. Encryption can protect confidentiality in transit or at rest, but confidentiality also depends on authorization, secret handling, logging practices, backups, screenshots, exports, and operational procedures.

### Integrity

Integrity means data and system state remain correct and unauthorized modification is prevented or detectable. Hashes, digital signatures, access control, transaction validation, version control, immutable logging, and change-management processes can all contribute to integrity.

### Availability

Availability means an authorized user can obtain a required service or resource when needed. Capacity, redundancy, backups, dependency management, rate limits, monitoring, recovery procedures, and protection against resource exhaustion all affect availability.

### Authenticity and accountability

Authenticity concerns whether an identity, artifact, or message is what it claims to be. Accountability concerns whether actions can be associated with the correct actor and investigated later. Strong authentication is useful only when authorization decisions and audit evidence are also correct.

### Resilience

A secure system should not depend on the assumption that prevention always succeeds. Resilience includes detection, containment, recovery, restoration, lessons learned, and the ability to operate safely during partial failure.

## Core security vocabulary

- **Asset:** something that has value and requires protection.
- **Threat:** a circumstance or actor capable of causing harm.
- **Vulnerability:** a weakness that can violate a security property.
- **Exposure:** a condition that makes a weakness reachable or relevant.
- **Exploit:** a method that takes advantage of a vulnerability. In this guide, exploit research is limited to controlled labs and defensive understanding.
- **Control:** a safeguard that prevents, detects, limits, or helps recover from an unwanted event.
- **Risk:** the combination of likelihood, impact, exposure, business context, and uncertainty.
- **Attack surface:** the set of reachable interfaces, identities, inputs, services, dependencies, and trust boundaries that could be abused.
- **Trust boundary:** a point where data, identity, authority, or execution crosses between components with different trust assumptions.

## Authentication and authorization

Authentication answers, “Who or what is presenting this credential?” Authorization answers, “May this identity perform this action on this resource in this context?” A system can authenticate a user correctly and still be vulnerable if authorization checks are missing, performed on the wrong object, or based on stale state.

## Threat actors and motivations

Security analysis should focus on capabilities and goals rather than stereotypes. Relevant actors can include financially motivated criminals, insiders, state-linked groups, opportunistic attackers, hacktivists, fraud groups, competitors, and automated abuse. Defenders should ask what access the actor begins with, what they are trying to achieve, what constraints they face, and what evidence their activity would leave.

## Vulnerability management basics

CVE identifiers provide common names for publicly disclosed vulnerabilities. NVD and vendor advisories enrich vulnerability information. CVSS provides a standardized severity framework, but a score is not a complete risk decision: exploitability, exposure, asset importance, compensating controls, and business impact still matter.

A useful vulnerability workflow is:

1. identify the affected asset and exact version;
2. verify whether the issue is applicable;
3. determine exposure and required privileges;
4. collect evidence without causing unnecessary impact;
5. prioritize using technical and business context;
6. remediate or mitigate;
7. retest and record the result.

## A modern ethical-assessment lifecycle

### 1. Authorization and scope

Write down the owner, systems, accounts, time window, allowed techniques, prohibited actions, data-handling rules, contacts, and stop conditions. “It is public on the Internet” is not authorization.

### 2. Discovery and modeling

Build an inventory of assets, identities, interfaces, dependencies, and trust boundaries. Start with passive or read-only evidence where possible.

### 3. Validation

Test security assumptions using the least invasive method that answers the question. Prefer a proof that demonstrates the weakness over a technique that maximizes access or impact.

### 4. Evidence and analysis

Record timestamps, versions, configuration, requests/responses, logs, screenshots only when necessary, and the exact condition that made the result possible. Separate observation from inference.

### 5. Remediation and retest

Explain the root cause, recommended control, expected residual risk, and a repeatable regression test. A finding is not complete until the owner can verify that the control changed the result.

### 6. Cleanup and reporting

Remove test accounts, temporary files, lab data, or configuration changes that were created as part of the authorized assessment. Preserve legitimate audit evidence; do **not** delete or tamper with security logs to conceal activity.

## Defensive thinking

A useful habit is to analyze every system with five questions:

1. What asset or security property matters?
2. Which identity or process has authority?
3. Where does untrusted input enter?
4. What state can become stale, confused, or inconsistent?
5. What evidence would prove the control is working?

## Safe lab

Create a one-page threat model for a local application or device you own. Draw the user, application, data store, network boundary, and one external dependency. Mark where authentication occurs, where authorization occurs, what data is sensitive, and what logs would be useful during an incident.

**Evidence to keep:** the diagram, three security assumptions, three possible failure modes, and one defensive test for each failure mode.

## Common mistakes

- Starting with tools before defining a security question.
- Treating a scanner finding as proof without verification.
- Confusing severity with business risk.
- Confusing encryption with authorization.
- Testing outside the written scope because a target is technically reachable.
- Keeping secrets, tokens, or unnecessary personal data in lab notes.
- Treating cleanup as permission to erase evidence.

## Knowledge check

1. Give an example of authentication succeeding while authorization fails.
2. Explain the difference between a vulnerability and risk.
3. Name three items that belong in assessment scope.
4. Why is retesting part of an ethical assessment?
5. What evidence would you collect before changing a security control?

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md). For this module, finish the safe lab and be able to explain the assessment lifecycle without referring to tool names.

### Continue with

Recommended next modules: **02, 05, 28, 51**.
