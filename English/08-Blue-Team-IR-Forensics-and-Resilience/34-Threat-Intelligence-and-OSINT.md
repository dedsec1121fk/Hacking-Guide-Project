# Threat Intelligence and OSINT

> **Purpose:** Collect and evaluate public information ethically, transform it into defensible intelligence, and avoid confusing search results with verified facts.

## Intelligence versus information

Information is collected data. Intelligence is information that has been evaluated in context and supports a decision.

A useful intelligence product answers:

- What happened or may happen?
- What evidence supports that conclusion?
- How confident are we?
- Why does it matter to this organization?
- What action should follow?

## Intelligence cycle

1. Direction and requirements.
2. Collection.
3. Processing.
4. Analysis.
5. Dissemination.
6. Feedback.

Without a collection requirement, analysts can spend hours gathering interesting but irrelevant data.

## OSINT scope

Open-source intelligence uses lawfully available public or authorized information. Publicly reachable does not automatically mean appropriate to collect, retain, republish, or correlate. Respect privacy, platform terms, intellectual property, and local law.

## Source evaluation

For each claim, track:

- original source versus repost;
- publication date and event date;
- author or organization;
- direct evidence versus inference;
- independent corroboration;
- potential bias or incentive;
- confidence.

Screenshots are useful evidence but can lose context. Preserve source metadata and timestamps where appropriate.

## Threat intelligence layers

**Strategic:** business-level trends and risk decisions.
**Operational:** campaigns, infrastructure, and adversary objectives.
**Tactical:** behaviors, techniques, and detection opportunities.
**Technical:** artifacts such as hashes, domains, addresses, or signatures.

Technical indicators often expire quickly; behavior-focused detections can be more durable.

## ATT&CK as a knowledge base

MITRE ATT&CK organizes observed adversary behaviors into tactics and techniques. Use it to communicate behaviors and identify detection/control gaps. Do not treat ATT&CK coverage percentages as proof of security.

## Indicators of compromise

An IOC without context can produce noise. Record:

- what it represents;
- first/last seen when known;
- source confidence;
- expected false positives;
- scope of use;
- expiration/review date.

## Vulnerability intelligence

A CVSS score describes severity, not your complete remediation priority. Consider exposure, exploitability, asset importance, compensating controls, and evidence of exploitation. CISA's Known Exploited Vulnerabilities catalog is one source of confirmed in-the-wild exploitation context.

## Domain and infrastructure research

Defensive OSINT may use DNS records, certificate-transparency data, registrar information, official company records, and public web metadata to understand assets you own or threats you are investigating. Avoid doxxing individuals or turning public fragments into invasive profiles unrelated to a legitimate security purpose.

## Social-media verification

Check original upload, timestamp, location claims, edits, and cross-source corroboration. Viral repetition is not independent confirmation.

## Intelligence writing

Separate **facts**, **assessments**, and **unknowns**. Use confidence terms consistently. A strong report can say “we do not know” and specify what evidence would change the assessment.

## Safe OSINT lab

Choose your own public project or a fictional organization. Build an asset-information table using only official/public sources:

- official domains;
- public code repositories;
- public contact/security policy;
- published technologies only where responsibly observable;
- certificate transparency for owned domains;
- public vulnerability disclosures.

Do not collect personal data unrelated to the exercise.

**Learning goal:** produce a concise intelligence note with source quality and confidence, not a pile of links.

## Primary references

- MITRE ATT&CK: https://attack.mitre.org/
- CISA KEV: https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- CVE Program: https://www.cve.org/
- NVD: https://nvd.nist.gov/

## Intelligence quality and analysis

OSINT becomes intelligence only when it answers a defined question. Begin with a requirement such as “What infrastructure and behaviors were publicly attributed to campaign X during a defined historical period?” Then collect sources that directly help answer it.

### Source grading

Separate source reliability from information credibility. A reliable publisher can still repeat an unverified claim; an unfamiliar source can sometimes provide primary evidence. Record publication date, event date, whether the source is primary/secondary, whether multiple independent sources corroborate the claim, and what uncertainty remains.

### Indicators versus behaviors

IP addresses, domains, hashes, and filenames can be useful but age quickly and may be shared/reassigned. Behavior and technique descriptions can remain useful longer. When mapping to ATT&CK, only map what the evidence actually supports and avoid inflating confidence to fill a matrix.

### Privacy boundary

Do not turn intelligence work into personal surveillance. Public data should be collected proportionately, and private accounts/access controls must not be bypassed. Remove unnecessary personal identifiers from reports and distinguish public-interest/security context from curiosity.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 01, 02, and ethics/privacy.

### Practice task

Write an intelligence requirement for a historical public incident, collect only public non-sensitive sources, grade source confidence, create a timeline, and state uncertainty.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **23, 37, 43, 57**.
