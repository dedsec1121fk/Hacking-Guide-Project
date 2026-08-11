# Master Capstones, Research Portfolio and Deep Security Practice

The final module turns the guide into demonstrable skill. The capstones require architecture reasoning, safe experiments, evidence, remediation, detection, and clear writing. A strong portfolio shows repeatable thinking rather than screenshots of tools.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, or lab environments you own or are explicitly authorized to test. The exercises in this module are designed to prove security properties without targeting third parties.

## Learning objectives

By the end of this module you should be able to:

- Explain **Capstone standard** and connect it to a concrete trust boundary or security invariant.
- Explain **Systems capstone** and connect it to a concrete trust boundary or security invariant.
- Explain **Application capstone** and connect it to a concrete trust boundary or security invariant.
- Explain **Cloud/supply-chain capstone** and connect it to a concrete trust boundary or security invariant.
- Explain **Detection/forensics capstone** and connect it to a concrete trust boundary or security invariant.
- Explain **Research capstone** and connect it to a concrete trust boundary or security invariant.

## Analysis method

Use the shared [Study Method](../Guides/STUDY-METHOD.md). For this module, first draw the relevant components and state transitions, then state one security invariant and identify the minimum evidence needed to test it safely.

## Deep concepts

### 1. Capstone standard

Each project should state scope, authorization, architecture, threat model, hypothesis, procedure, evidence, findings, remediation, regression, cleanup, and limitations.



### 2. Systems capstone

Analyze one disposable Linux/Windows/Android environment from boot/identity through process/file/network boundaries. Document attack surface and reduce unnecessary privilege/exposure.



### 3. Application capstone

Build or use an intentionally vulnerable local application, identify one root-cause authorization/parser/session flaw, fix it, and prove the fix with negative regression tests.



### 4. Cloud/supply-chain capstone

Model a small cloud deployment from source to CI to registry to workload identity. Add provenance, least privilege, logging, and a recovery plan for compromised build credentials.



### 5. Detection/forensics capstone

Generate a synthetic sequence of benign events representing a security hypothesis, detect it, intentionally remove one telemetry source, and explain the resulting evidence gap.



### 6. Research capstone

Take a public fixed bug or toy vulnerable program, reproduce safely, minimize the trigger, identify root cause, compare the patch, and build a regression test—without weaponization.



### 7. Writing quality

Use precise claims: observed, inferred, unverified, not tested. Include hashes, versions, timestamps, diagrams, and minimal reproducer artifacts. Explain why the evidence supports the conclusion.



### 8. Portfolio hygiene

Remove secrets, personal data, customer data, proprietary details, live targets, and unnecessary exploit code. Publish sanitized diagrams, tests, defensive findings, and lessons learned.



## Review focus

Apply the failure-mode taxonomy in [Study Method](../Guides/STUDY-METHOD.md), but keep the analysis specific to this lesson: identify the principal, resource, authority, mutable state, parser or policy boundary, and the telemetry that would distinguish a real control failure from misconfiguration or an observation gap.

## Authorized exercises

### Exercise 1 — Complete one capstone from systems/application/cloud/detection/research and have another person reproduce the result from your documentation

Complete one capstone from systems/application/cloud/detection/research and have another person reproduce the result from your documentation.


### Exercise 2 — Create a portfolio index that links each project to the skills and security invariants demonstrated

Create a portfolio index that links each project to the skills and security invariants demonstrated.


### Exercise 3 — Revisit an early guide lab and redo it using the advanced evidence standard; compare the quality of the old and new conclusions

Revisit an early guide lab and redo it using the advanced evidence standard; compare the quality of the old and new conclusions.

Use the lab-record format in [Study Method](../Guides/STUDY-METHOD.md) for each exercise and keep all inputs synthetic or confined to the authorized lab.

## Knowledge checks

1. Explain the most important trust boundary in **Master Capstones, Research Portfolio and Deep Security Practice** without naming a security tool.
2. Give one example where cryptographic or authentication success still does **not** imply authorization success.
3. Describe one stale-state or replay condition relevant to this module.
4. Identify one telemetry source that can support a strong conclusion and one blind spot it still leaves.
5. Explain how you would turn a discovered weakness into a regression test rather than a one-time finding.

## Guided study workflow

Use [Study Method](../Guides/STUDY-METHOD.md). Complete at least one authorized exercise, preserve the evidence that supports your conclusion, and explain the module's main trust boundary and failure modes in your own words before moving on.

### Continue with

Choose **Learning paths** from the main menu for an ordered specialization, or use **Search lessons** to follow a concept into related modules.
