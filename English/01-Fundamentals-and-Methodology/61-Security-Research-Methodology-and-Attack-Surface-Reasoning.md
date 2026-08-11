# Security Research Methodology and Attack-Surface Reasoning

> **Purpose:** Learn how experienced security researchers reason about systems before touching tools. This module is about building accurate models, finding trust assumptions, and turning observations into testable hypotheses inside authorized environments.

## Learning objectives

- Convert a vague target description into assets, identities, trust boundaries, data flows, and security properties.
- Distinguish an attack surface from an exploit and a vulnerability from an exposure.
- Build hypotheses from evidence rather than tool output alone.
- Use differential testing, negative testing, and invariant checking in a safe lab.
- Recognize where complex systems fail: boundaries, parsers, state transitions, identity translation, and recovery paths.

## The research mindset

Deep security work starts with a model. A scanner can tell you that a port is open; it cannot by itself tell you why the service exists, which identity it trusts, what business state it changes, what data crosses the boundary, or what evidence would prove that authorization is enforced correctly. Experienced researchers move repeatedly between **model → hypothesis → experiment → evidence → revised model**.

A useful model asks five questions. What are the assets? Who or what can act on them? Which boundaries separate levels of trust? Which state transitions matter? Which observations are available if something goes wrong? A weakness often appears where two parts of the system disagree about one of these questions.

## Attack surface versus vulnerability

The **attack surface** is the set of reachable inputs, interfaces, identities, dependencies, parsers, update paths, administrative workflows, and physical interfaces that could influence a security-relevant state. A vulnerability is a specific weakness within that surface. Exposure is the degree to which the weakness is reachable under actual deployment conditions.

For example, an internal parser may contain a memory bug but be unreachable from untrusted data. A public API may contain no memory corruption at all but expose a high-impact authorization mistake. Risk reasoning must include reachability, privilege, preconditions, observability, recovery, and business impact.

## Model the system as graphs

A practical way to reason deeply is to use several overlapping graphs:

- **Asset graph:** databases, files, secrets, devices, queues, APIs, control planes.
- **Identity graph:** users, service accounts, workload identities, groups, roles, tokens, trust relationships.
- **Data-flow graph:** where input enters, how it is transformed, where it is stored, and where it leaves.
- **Privilege graph:** which principal can cause which security-relevant state changes.
- **Dependency graph:** libraries, build systems, package registries, CI/CD, cloud services, DNS, identity providers.
- **Observation graph:** logs, traces, audit records, alerts, telemetry gaps.

Security failures are frequently graph problems. A single edge that grants too much authority can matter more than dozens of hardened nodes.

## Trust boundaries

A trust boundary exists wherever data or authority moves between components with different assumptions. Common examples include browser to server, application to database, user process to kernel, container to host, workload to cloud metadata service, mobile app to exported component, CI runner to signing key, and domain user to privileged administration tier.

At each boundary document:

1. input format;
2. caller identity;
3. authentication mechanism;
4. authorization decision;
5. validation and canonicalization;
6. output or side effect;
7. logging and correlation fields;
8. failure behavior.

The most interesting research question is often not “can I send strange input?” but “what does the receiving component believe about this input that the sender can influence?”

## Security properties and invariants

An **invariant** is something that should remain true regardless of normal input variation. Examples:

- a user cannot read another tenant's object without an explicit grant;
- an unsigned update cannot become trusted code;
- a low-privilege process cannot write a protected configuration;
- a refresh token cannot be accepted by a different client than intended;
- a parser must never read beyond the supplied buffer;
- a recovery workflow cannot bypass the normal identity proofing requirement.

Write invariants before testing. They turn security testing from random exploration into falsifiable engineering.

## State-machine thinking

Many high-impact weaknesses are not single malformed inputs; they are invalid **sequences** of otherwise valid actions. Model workflows as states and transitions. Registration, password reset, checkout, invitation acceptance, device enrollment, OAuth consent, key rotation, and account recovery are all state machines.

For each transition, ask:

- what must already be true?
- who is allowed to trigger it?
- can it be replayed?
- can steps be skipped or reordered?
- is the object identity bound to the authenticated principal?
- can two concurrent transitions violate an invariant?
- what happens after timeout, retry, or partial failure?

## Differential testing

Differential testing compares two executions that should differ in a predictable way. In a local test application, compare the same request as two users, with and without a required role, before and after an object is transferred, or with equivalent encodings. Differences can reveal hidden assumptions.

The key is controlled change: alter one variable at a time and record the result. When many variables change together, conclusions become weak.

## Canonicalization and representation gaps

Security boundaries often fail because two components interpret the “same” value differently. Paths may have multiple encodings. Hostnames can be normalized. Unicode can have equivalent representations. HTTP intermediaries may disagree about message boundaries. JSON numbers, duplicate keys, URL encodings, and case rules can differ between libraries.

A safe research approach is to create a small local parser pair and feed both the same synthetic corpus. Flag inputs where the parsers disagree. The goal is understanding semantic mismatch, not targeting a public service.

## Identity translation

Distributed systems frequently translate identity: browser session → API token → service account → database role; or domain account → Kerberos ticket → service identity. Each translation can lose context. Ask what claims survive, what audience restrictions exist, how delegation works, and whether downstream authorization rechecks the correct subject.

A recurring design smell is **confused deputy** behavior: a privileged component performs an action because an untrusted caller can influence the target of that action without providing equivalent authority.

## Failure-path analysis

Security controls are often designed for the success path and forgotten during errors. Study timeouts, partial writes, duplicate messages, retries, expired credentials, failover, restore, rollback, and emergency access. Questions include:

- does failure become fail-open or fail-closed?
- can a retry repeat a security-sensitive state change?
- is an authorization decision cached longer than the authority that justified it?
- do backups restore old secrets or old permissions?
- do emergency procedures bypass monitoring?

## Evidence quality

A finding should be reproducible from minimal evidence. Keep the exact environment, a synthetic identifier, the smallest request/response or log excerpt that proves the behavior, and the expected invariant. Avoid huge terminal dumps. Strong evidence isolates cause and effect.

Separate **observation** from **interpretation**. “The server returned object B while authenticated as user A” is an observation. “This is broken object authorization” is an interpretation supported by that observation plus the expected policy.

## Safe advanced practice

Build a small localhost application with two synthetic users and three objects. Define a policy matrix for read, update, and delete. Write tests that assert every unauthorized transition fails. Then intentionally introduce one harmless logic bug, observe which invariant breaks, fix it, and keep the regression test.

A second exercise is a parser differential lab: parse the same synthetic URL or JSON samples with two standard-library functions and record normalization differences. Do not aim the test at external systems.

## Research notebook template

For each hypothesis record:

- **System model:** component and trust boundary.
- **Invariant:** what should always be true.
- **Hypothesis:** the specific condition that may violate it.
- **Independent variable:** the one thing you will change.
- **Expected result:** behavior if the system is correct.
- **Observed result:** evidence only.
- **Interpretation:** why the evidence supports or rejects the hypothesis.
- **Risk:** preconditions, reachable assets, privilege, and blast radius.
- **Fix:** root-cause remediation.
- **Regression:** test that should fail if the bug returns.

## Deep-study checkpoint

You should be able to take an unfamiliar architecture diagram and produce a test plan without naming a security tool. If your plan is mostly tool names, revisit trust boundaries, invariants, identities, and state transitions.

## Guided study workflow

### Before you begin

Complete Modules 01, 05, 15, 41, 51, and 52. Use only a localhost or private lab you control.

### Practice task

Choose one small application you wrote or an intentionally vulnerable local training application. Draw its asset, identity, privilege, dependency, and observation graphs. Define ten invariants, then create negative tests for at least five of them.

### Evidence to keep

Keep the diagrams, invariant list, test cases, and one example showing how evidence changed your original model.

### Common mistakes to avoid

- treating a scanner result as a conclusion;
- changing multiple variables at once;
- confusing unusual behavior with security impact;
- testing without a written expected policy;
- ignoring recovery and failure paths;
- expanding beyond authorized scope.

### Mastery check

Explain an attack surface without listing vulnerabilities, explain a confused deputy, and show how one invariant becomes a repeatable regression test.

### Continue with

Modules **62, 69, 71, 72, 76, 84, and 85**.
