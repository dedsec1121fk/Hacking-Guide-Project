# Study Method

This guide provides one reusable method for studying every Hacking Guide Project module without repeating the same generic instructions in each lesson.

## 1. Confirm the boundary first

Before any practical work, write down what you own or are explicitly authorized to test, which accounts and data are synthetic, which actions are prohibited, and when the exercise must stop. If the boundary is unclear, keep the work conceptual or use an isolated local lab.

## 2. Learn in three passes

### Pass A — Build the model

Read the lesson once without trying to memorize commands. Identify the assets, identities, trust boundaries, data flows, security invariants, and failure modes. If you cannot explain the architecture in plain language, do not rush into tooling.

### Pass B — Find the evidence

For each claim, ask what evidence would prove or disprove it: configuration, request/response, packet trace, log event, process state, file metadata, policy decision, or a controlled test result. Prefer primary evidence over screenshots of tool summaries.

### Pass C — Practice safely

Use the smallest harmless exercise that demonstrates the concept. Start from a baseline, change one variable at a time, collect before/after evidence, restore the environment, and document what you learned.

## 3. Keep a lab record

For every exercise, record:

- objective and security question;
- authorized scope and environment;
- starting configuration or baseline;
- exact benign action performed;
- expected result;
- observed result;
- relevant logs, outputs, or artifacts;
- explanation of the root cause or control;
- cleanup/recovery action;
- one follow-up question.

Do not copy real credentials, unrelated personal data, or production secrets into notes.

## 4. Separate observation from inference

Write **Observed** for facts directly supported by evidence and **Inferred** for conclusions that depend on assumptions. Add a confidence level when the distinction matters. This habit prevents scanner output, log fragments, or partial tests from becoming overconfident findings.

## 5. Use security invariants

A security invariant is a statement that should remain true, for example:

- a normal user can access only their own tenant's objects;
- a guest network cannot reach the management plane;
- an unsigned build cannot become a release artifact;
- a revoked identity cannot continue using a protected service.

Testing an invariant is usually more useful than executing a long list of unrelated commands.

## 6. Evidence hygiene

Prefer synthetic accounts and test objects. Redact secrets. Hash downloaded artifacts when integrity matters. Preserve timestamps and time-zone context. Keep legitimate security/audit logs intact. Store lab evidence only as long as needed for the exercise.

## 7. Common cross-cutting mistakes

- Starting with a tool before understanding the system.
- Expanding scope because something interesting appears nearby.
- Treating a successful request as proof of business impact.
- Collecting more data than the test requires.
- Changing several variables at once.
- Failing to record a baseline.
- Reporting uncertainty as certainty.
- Leaving test accounts, files, or configuration behind.

## 8. Mastery check

A module is complete when you can:

1. explain the core model without reading the lesson;
2. identify the important trust boundaries and failure modes;
3. choose evidence that would validate a security claim;
4. complete at least one safe exercise;
5. explain both the weakness and the defensive control;
6. describe what you would test next and why.

## 9. Use the menu, not memorized commands

Start `Hacking Guide Project.py` and use the numbered interface. **Search lessons** finds concepts, **Browse categories** keeps related modules together, **Learning paths** gives an ordered specialization, **Bookmarks** saves useful lessons, and **Progress & recent lessons** lets you continue where you stopped.

## 10. Recommended learning rhythm

For difficult material, one deeply understood module is better than several skimmed modules. Read, model, practice, write evidence, review the knowledge check, and only then continue. Revisit older modules whenever a later chapter exposes a missing prerequisite.
