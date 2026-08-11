# AI and LLM Security

> **Purpose:** Secure applications that use large language models, retrieval, tools, agents, and external data sources.

## Current landscape

OWASP released its **GenAI LLM Top 10 2026** on August 3, 2026. AI security changes quickly, so treat fixed lists as a starting point and verify current project guidance.

## Core risk families

### Prompt and context manipulation

Direct user input or indirect retrieved content can influence model behavior. Treat external content as untrusted data even when an LLM reads it.

### Sensitive information disclosure

Avoid placing secrets, unnecessary personal data, privileged internal instructions, or raw credentials into model context. Apply minimization/redaction before data enters logs, prompts, vector stores, or evaluation sets.

### Supply chain and provenance

Track model providers/versions, adapters, embeddings, datasets, libraries, plugins, and external services. Review update paths and security impact when any component changes.

### Unsafe output handling

LLM output is untrusted input. Do not pass model text directly into a shell, SQL query, template, interpreter, or privileged API without deterministic validation and constrained interfaces.

### Excessive agency

Agents become high risk when broad permissions, many tools, weak approvals, and ambiguous goals combine. Limit tools, scope credentials, require approval for high-impact actions, and make destructive changes reversible where possible.

### Retrieval and memory risk

RAG/vector systems can ingest poisoned content. Maintain source provenance, access control, tenancy boundaries, ingestion validation, and removal/invalidations.

### Resource abuse

Apply quotas, token/request limits, timeouts, concurrency controls, caching, and cost monitoring.

## Secure architecture pattern

Separate user input, system policy, untrusted retrieved content, model output, deterministic validation, authorization, tool execution, and audit logging. The model should not be the final authorization decision-maker for sensitive actions.

## Safe lab

Build a toy assistant with one harmless tool such as a calculator. Test whether untrusted retrieved text can cause unexpected tool calls, then add allow-lists and explicit approval.

## References

- OWASP GenAI LLM Top 10 2026 — https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/
- OWASP GenAI Security Project — https://genai.owasp.org/

## AI system threat modeling

An AI-enabled application is still a software system. Model security should be reviewed together with identity, authorization, data handling, APIs, dependencies, logging, infrastructure, and business logic. Start by drawing the complete data flow: user input, preprocessing, retrieval, system instructions, model call, memory, tools, external APIs, post-processing, storage, analytics, and human approval points.

For each component, identify what it trusts and what it can change. A model that can only draft text has a very different risk profile from an agent that can send email, modify cloud infrastructure, approve refunds, or execute code.

## Trust boundaries for prompts and context

Prompt text is not a security boundary. System instructions can guide behavior, but untrusted content can still compete with or manipulate those instructions. Therefore, authorization and safety-critical constraints should be enforced outside the model in deterministic application code or policy systems.

Distinguish at least four classes of context:

1. **Trusted application policy** — rules controlled by the application owner.
2. **Authenticated user input** — attributable but still untrusted data.
3. **Retrieved/external content** — documents, webpages, email, files, search results, database records, and tool output that may contain adversarial text.
4. **Model-generated content** — probabilistic output that must not be assumed correct or safe.

Maintain provenance where possible so downstream controls know where content came from.

## Indirect prompt injection

Indirect prompt injection occurs when malicious or misleading instructions are embedded in content the model later reads, rather than directly typed by the user. Defenses should reduce the authority of retrieved text, constrain tool use, separate data from policy, and require deterministic checks before high-impact actions.

A useful design question is: **If every retrieved document were controlled by an attacker, what could the model make the application do?** The answer defines the blast radius of retrieval compromise.

## Tool and agent security

Tools turn model output into actions. Every tool should have a narrow purpose, explicit input schema, authorization checks, bounded output, and an audit trail.

### Tool design principles

- Expose business operations rather than a generic shell or unrestricted HTTP client.
- Validate arguments deterministically.
- Scope credentials to the tool's minimum permissions.
- Re-check authorization at execution time.
- Separate read-only and write-capable tools.
- Require confirmation for irreversible or high-impact actions.
- Define rate, cost, and concurrency limits.
- Make retries idempotent where possible.
- Return structured errors rather than sensitive internal state.

### Human approval

Human-in-the-loop controls are useful only when the reviewer receives enough context to make a decision and when the application enforces the result. Avoid approval prompts that encourage routine clicking. Highlight the exact action, target, data affected, and whether the operation is reversible.

## Retrieval-Augmented Generation security

RAG systems add ingestion pipelines, vector databases, embedding models, document permissions, ranking logic, and source provenance to the attack surface.

### RAG controls

- Enforce document authorization before retrieval, not after generation.
- Preserve tenant boundaries in both metadata and query logic.
- Track source and ingestion time.
- Validate and sanitize supported file formats.
- Limit document size and recursive expansion.
- Define deletion and re-indexing procedures.
- Detect unusual bulk ingestion or retrieval activity.
- Avoid treating retrieved instructions as privileged policy.
- Test whether a user can cause retrieval of documents they cannot normally access.

## Memory and personalization

Persistent memory can accidentally convert temporary sensitive information into long-lived context. Define what is eligible for memory, how users inspect or delete it, retention periods, tenant isolation, and whether sensitive categories are excluded. Memory writes should be treated as state changes with authorization and audit requirements.

## Data leakage controls

Minimize data before it reaches the model. Mask or tokenize sensitive values when the task does not require raw values. Avoid embedding secrets in system prompts. Understand provider retention and training settings, contractual controls, and regional requirements for production data.

Output filtering can reduce accidental disclosure but should not be the only protection. The stronger control is preventing the model from receiving data the requester was never authorized to access.

## Model and dependency supply chain

Record model provider, model/version identifier, deployment configuration, fine-tunes/adapters, system prompt revision, retrieval corpus version, tool set, and important library versions for production systems. Changes to any of these can alter behavior even when application source code is unchanged.

Treat model files and adapters as artifacts. Verify origin, access control, integrity, licensing, and update process. Avoid silently replacing a production model with a new revision without evaluation of security-sensitive behavior.

## Evaluation and red teaming

AI security testing should combine deterministic software tests with behavioral evaluations. Build a repeatable corpus of benign and adversarial test cases covering data leakage, instruction conflicts, unauthorized tool requests, unsafe output handling, cross-tenant retrieval, excessive resource use, and refusal/approval boundaries.

Record the exact model version and configuration because results may change across releases. A single successful refusal is not proof of a robust control; test variants and measure failure rates.

## Logging and privacy

Useful AI audit data can include user/session identity, model/version, prompt template version, retrieval source identifiers, tool requested, tool authorized/denied, execution outcome, safety-control decision, latency, and token/cost metrics. Avoid storing full prompts and outputs by default when they may contain secrets or personal data. Use redaction and purpose-limited retention.

## Resource and cost security

AI systems can consume material compute and third-party API spend. Define per-user and per-tenant quotas, maximum context size, tool-call limits, recursion/depth limits for agents, timeouts, concurrency limits, and budget alarms. Cache only when it does not violate privacy or authorization boundaries.

## Secure AI deployment checklist

- [ ] The model cannot directly authorize sensitive actions.
- [ ] Retrieved content is treated as untrusted.
- [ ] Tool interfaces are narrow and schema-validated.
- [ ] Credentials are scoped per tool/workload.
- [ ] Cross-tenant retrieval tests exist.
- [ ] High-impact actions require policy checks and, when appropriate, approval.
- [ ] Prompt/output logs follow data-minimization rules.
- [ ] Model and prompt versions are traceable.
- [ ] Resource limits and cost monitoring are configured.
- [ ] Security evaluations are repeatable after model/configuration changes.
- [ ] A rollback path exists for a problematic model or prompt release.

## Extended safe lab

Create a local mock “support assistant” with two harmless tools: `lookup_order(order_id)` using synthetic data and `calculator(expression)` with a strict arithmetic parser. Give User A and User B separate synthetic orders. Test that the assistant cannot retrieve User B's order even when a prompt explicitly asks it to, and that text embedded inside an order description cannot cause an unauthorized tool call. The authorization check must live in the tool/application layer rather than relying on the model to remember the rule.

## Additional primary reference

- NIST SP 800-218A — https://csrc.nist.gov/pubs/sp/800/218/a/final

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 14, 22, and 41.

### Practice task

Threat-model a fictional LLM application with untrusted prompts/content, data boundaries, tool access, output handling, evaluation, and human approval for high-impact actions.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **40, 41, 46**.
