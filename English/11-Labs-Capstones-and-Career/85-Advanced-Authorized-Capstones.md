# Advanced Authorized Capstones

> **Purpose:** Integrate the advanced modules into realistic, evidence-driven security projects that prove deep understanding without attacking third-party systems.

## Capstone rules

Every capstone must use one of these environments:

- software you wrote;
- infrastructure/accounts you own;
- intentionally vulnerable training systems;
- a CTF whose rules explicitly permit the tested technique;
- an environment covered by written authorization.

Do not expand scope because a neighboring system looks interesting. Advanced skill includes restraint and evidence discipline.

## Deliverables for every capstone

Produce:

1. scope/authorization statement;
2. architecture/trust-boundary diagram;
3. threat model and invariants;
4. test plan;
5. environment versions/hashes;
6. evidence;
7. findings with confidence and impact;
8. remediation;
9. regression/detection tests;
10. cleanup/recovery proof;
11. lessons learned.

## Capstone 1 — Binary assurance pipeline

Build a small native parser you own. Compile debug and hardened builds. Inspect ELF/PE metadata, disassemble key functions, run sanitizers, create a fuzz harness, triage one controlled failure, fix it, and add regression tests.

**Skills:** Modules 62–68, 84.

**Success criterion:** You can connect source invariant → assembly/binary representation → runtime evidence → fix without producing an exploit payload.

## Capstone 2 — Local web trust-boundary review

Build a localhost application with two users, two tenants, reverse proxy, cache layer if available, and API endpoints. Define authorization matrix, origin policy, cache rules, forwarded-header trust, redirect policy, and server-side fetch restrictions.

Test only benign representations and negative authorization cases. Fix one intentionally introduced logic/configuration error.

**Skills:** Modules 52, 61, 68–71, 78, 84.

## Capstone 3 — Enterprise identity graph

Create a disposable Windows lab domain with synthetic users/groups/service accounts/GPOs. Map Kerberos roles, group nesting, directory ACLs, service identities, and GPO authority.

Introduce one intentionally excessive test permission, prove the resulting graph path administratively, remove it, and verify the path is gone. Do not dump credentials or forge tickets.

**Skills:** Modules 21, 32, 72, 73, 80, 81.

## Capstone 4 — Linux isolation report

On a disposable Linux VM, run a containerized service and inventory credentials, capabilities, namespaces, cgroups, seccomp/LSM, mounts, network reachability, and service user.

Harden the workload by dropping unnecessary capabilities, making filesystem regions read-only where possible, applying resource limits, and restricting network access.

**Skills:** Modules 24, 33, 62, 74, 75, 80.

## Capstone 5 — Kubernetes privilege graph

Use a local development cluster. Create namespaces, synthetic service accounts, RBAC roles, and a benign workload. Build an authority graph covering API permissions, secret access, pod creation, node boundary, and external/cloud identity if present.

Remove one unnecessary edge and verify both denial and audit visibility.

**Skills:** Modules 19, 21, 24, 49, 75, 76, 80.

## Capstone 6 — Cloud IAM sandbox

In a disposable cloud sandbox, model humans, workloads, roles, trust policies, secrets, and control-plane permissions. Use only low-cost/reversible resources.

Demonstrate least-privilege with a reader role that can perform expected reads but cannot change policy or create privileged resources. Confirm control-plane logging.

**Skills:** Modules 19, 21, 49, 61, 76, 80, 81.

## Capstone 7 — Protocol reverse engineering

Write a custom localhost protocol, capture it, then pretend you lost the source. Infer framing, endian, message types, request IDs, state, and errors. Implement a parser/dissector and fuzz it.

Compare the final inferred specification with original source.

**Skills:** Modules 51, 61, 68, 77, 78.

## Capstone 8 — Malware-analysis simulation

Use a harmless simulator that creates temporary files, starts a child process, touches a test configuration, and makes a localhost connection. Analyze it as if it were suspicious.

Build a timeline, process tree, static triage, behavior report, and one detection rule/query concept. Reset the environment afterward.

**Skills:** Modules 07, 23, 37, 64, 67, 79–81.

## Capstone 9 — Android application security review

Build or choose an open-source training Android app. Review manifest, exported components, deep links, storage, network security config, WebView, Keystore usage, native libraries, and signer identity.

Trace one external input to a sensitive action and confirm server-side/IPC authorization.

**Skills:** Modules 17, 39, 53–56, 63–67, 78, 82.

## Capstone 10 — Firmware trust chain

Use a development board or training firmware image. Identify image/container format, filesystem, boot components, update metadata, signing/trust design, rollback model, exposed interfaces, and network services.

Do not disable boot/debug protections. The project is a **trust review**, not a bypass challenge.

**Skills:** Modules 18, 49, 54, 64, 67, 77, 78, 83.

## Capstone 11 — Detection engineering lifecycle

Choose one benign lab behavior and implement the complete lifecycle: hypothesis, telemetry requirements, event generation, collection, normalization, rule, test fixture, false-positive analysis, ATT&CK v19.2 mapping, and analyst procedure.

Measure what happens when telemetry is unavailable.

**Skills:** Modules 12, 23, 47, 59, 80, 81.

## Capstone 12 — Patch-to-prevention study

Select a bug in your own code or a fully disclosed public fix. Reconstruct the root cause, write the invariant, build a safe regression, search for variants, identify defense-in-depth controls, and create a short advisory.

**Skills:** Modules 40, 61, 65–68, 84.

## Capstone 13 — Termux security research workstation

Use Termux as the organization/analysis layer for a safe project:

- Git repository for notes/scripts;
- Python virtual environment if needed;
- hashes of lab artifacts;
- offline search with `Hacking Guide Project.py`;
- local parser/fuzz harness;
- localhost HTTP service;
- structured reports exported to shared storage only when needed.

Document Android/Termux limitations instead of trying to defeat them.

**Skills:** Modules 28–31, 36, 51, 61, 68, 77.

## Capstone 14 — Incident reconstruction tabletop

Create synthetic endpoint, identity, DNS, cloud, and application logs for a fictional incident. Seed several benign distractors and three related suspicious events. Give the dataset to another learner without the answer.

They must produce timeline, hypotheses, evidence, uncertainty, containment plan, and detection improvement. Compare with the scenario design.

**Skills:** Modules 23, 37, 47, 72, 76, 80, 81.

## Capstone 15 — Security architecture review

Design a small SaaS system with browser/mobile clients, API gateway, application services, database, object storage, background queue, identity provider, CI/CD, cloud roles, observability, and backups.

Create asset/identity/data/privilege/dependency/observation graphs. Define 25 security invariants and map each to preventive and detective controls.

**Skills:** Modules 21, 22, 39–41, 49, 61, 69–76, 80.

## Scoring rubric

Score each capstone from 0–4 in these dimensions:

- **Scope discipline** — authorization and boundaries explicit.
- **System model** — accurate components/identities/trust edges.
- **Technical depth** — explains internals, not only tools.
- **Evidence** — minimal, reproducible, correctly interpreted.
- **Security reasoning** — invariant/root cause/impact clear.
- **Remediation** — addresses root cause and defense in depth.
- **Validation** — regression/detection proves the fix.
- **Communication** — report understandable to technical and non-technical readers.
- **Cleanup** — lab restored and sensitive artifacts handled safely.

A strong portfolio contains a few capstones scored deeply rather than dozens of shallow screenshots.

## Advanced mastery checklist

Before calling yourself comfortable with the advanced track, you should be able to:

- read basic x86-64 and ARM64 control flow;
- explain executable loading and dynamic linking;
- triage a crash and identify root cause with sanitizers/debuggers;
- design a fuzz harness and minimize a failure;
- reverse a small binary you compiled;
- reason about HTTP intermediaries and parser boundaries;
- build an API authorization matrix/state machine;
- explain Kerberos and AD privilege graphs;
- distinguish Windows tokens/ACLs/privileges;
- distinguish Linux namespaces/cgroups/seccomp/LSM;
- explain Kubernetes RBAC plus runtime isolation;
- map cloud IAM/role/metadata trust;
- reverse a simple custom protocol;
- explain TLS identity/nonce/key lifecycle;
- analyze a benign suspicious binary safely;
- build and validate a detection;
- construct a forensic timeline;
- review an Android package and firmware trust chain;
- convert a security patch into an invariant/regression test.

## Guided study workflow

### Before you begin

Complete the foundational path and the prerequisite modules for your chosen capstone. Read `ADVANCED-TRACK.md` and `LAB-GUIDE.md`.

### Practice task

Complete one capstone end-to-end and have another person reproduce at least one result using only your documentation.

### Evidence to keep

Keep the final report, diagrams, source/configuration, sanitized evidence, regression/detection tests, and cleanup record.

### Common mistakes to avoid

- maximizing tool count instead of depth;
- omitting the expected invariant;
- treating a screenshot as sufficient evidence;
- skipping remediation validation;
- leaving vulnerable lab services exposed;
- expanding scope beyond authorization.

### Mastery check

A capstone is complete when you can explain **system → trust boundary → hypothesis → evidence → root cause → impact → fix → verification** without depending on unexplained commands.

### Continue with

From the main menu, open **Learning paths**, revisit weak areas with the Advanced path, then specialize in reverse engineering, exploit-research foundations, identity, protocols, or detection.
