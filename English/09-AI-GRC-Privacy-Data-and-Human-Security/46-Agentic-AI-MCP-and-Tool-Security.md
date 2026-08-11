# Agentic AI, MCP and Tool Security

> **Purpose:** Secure AI systems that can plan, call tools, access data, keep memory, and perform actions on behalf of users.

## Why agents change the threat model

A chatbot that only returns text has a narrower action surface than an agent that can send email, edit files, query business systems, deploy code, or invoke external tools. The model becomes part of an orchestration system with identities, credentials, permissions, memory, tool metadata, and side effects.

OWASP's 2026 agentic-security work emphasizes risks such as goal hijacking, tool misuse, identity and privilege abuse, memory poisoning, insecure inter-agent communication, cascading failures, and rogue behavior. Treat those risks as architecture problems, not merely prompt-writing problems.

## Agent components to model

- user and operator identities;
- model/provider;
- system/developer instructions;
- conversation context;
- retrieval sources;
- long-term memory;
- tools and tool descriptions;
- MCP clients/servers where used;
- credentials and delegated tokens;
- approval gates;
- output consumers;
- audit logs.

## Prompt injection is an authorization problem too

Untrusted content can influence a model's behavior. The defensive goal is not to find a magical prompt that can never be manipulated. Instead, prevent model text from acquiring authority it should not have.

Controls include:

- separate instructions from untrusted content;
- constrain tool permissions;
- validate tool arguments independently;
- require approval for sensitive actions;
- prevent cross-tenant retrieval;
- treat model output as untrusted before code/query/action execution;
- limit memory writes;
- maintain action logs and attribution.

## Least privilege for tools

An agent that only needs to read a ticket should not receive credentials that can delete users. Give each tool the smallest useful scope and separate read from write operations where possible.

Short-lived, workload-specific credentials are preferable to broad permanent API keys.

## Tool descriptions are part of the trust surface

Tool metadata can shape model behavior. Review third-party tool/MCP server descriptions, schemas, permissions, origin, update mechanism, and ownership. Do not assume a tool is safe because its JSON schema looks harmless.

## Model Context Protocol

MCP standardizes connections between AI applications and external tools/data. Its 2026 specification and security guidance emphasize access controls, validation, user consent for sensitive operations, credential protection, and secure authorization flows.

For an MCP deployment, document:

- server owner and origin;
- transport and authentication;
- OAuth/client configuration if used;
- scopes;
- tools/resources/prompts exposed;
- data destinations;
- token storage;
- session isolation;
- rate limits;
- audit logs;
- revocation and removal process.

## Human approval

Approval is meaningful only when the user sees enough information to understand the action. “Allow?” without target, data, and consequence is not informed consent.

For high-impact actions, show:

- exact operation;
- destination/recipient;
- data being shared;
- permissions used;
- whether the action is reversible.

## Memory security

Long-term agent memory can become a persistence layer for bad instructions or sensitive data. Apply provenance, tenant/user isolation, retention rules, validation, and deletion controls. Do not let arbitrary retrieved text silently rewrite durable policy.

## Inter-agent communication

Multiple agents can amplify mistakes. Authenticate agent identities, authorize actions at the receiving service, validate messages, constrain delegation, and preserve traceability across hops.

## Safe failure

Agents need budgets and stop conditions:

- maximum tool calls;
- maximum spend/time;
- retry limits;
- bounded recursion;
- transaction boundaries;
- reversible staging;
- approval escalation.

## Evaluation

Test both normal and adversarial inputs in a local/sandbox environment. Measure whether the system:

- refuses unauthorized tool use;
- preserves tenant boundaries;
- handles conflicting instructions;
- protects secrets;
- asks for approval at the correct point;
- fails safely when a dependency returns malformed output.

## Lab — Harmless agent tool boundary

Build a toy local agent with two tools: calculator and note writer. The note writer may only write under a temporary lab directory. Add a policy layer that rejects absolute paths, traversal, and writes outside the lab. Require confirmation before writes.

Feed the agent untrusted text that requests a write outside the allowed directory and verify the policy layer blocks it regardless of model output.

**Learning goal:** authorization belongs in deterministic controls, not in model obedience.

## Primary references

- OWASP Top 10 for Agentic Applications 2026: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- OWASP secure MCP server development: https://genai.owasp.org/resource/a-practical-guide-for-secure-mcp-server-development/
- MCP security best practices: https://modelcontextprotocol.io/specification/draft/basic/security_best_practices

## Agent/tool security depth

Agentic systems combine model uncertainty with tool authority. The dangerous boundary is often not the model text itself but the transition from untrusted content to privileged action.

### Tool contracts

Each tool should have a narrow purpose, typed/validated inputs, explicit authorization, bounded output, timeout/resource limits, and audit logging. Avoid giving a general shell/filesystem/network tool when a purpose-built capability can perform the required action with less authority.

### Untrusted context

Retrieved documents, emails, webpages, issue text, memory, and tool output can contain instructions. Treat them as data, not authority. System/developer policy and user-approved actions must not be overridden by content merely because it looks like an instruction.

### High-impact actions

Require human confirmation or strong policy gates for deletion, external communication, money movement, credential changes, privilege changes, publication, or other irreversible/high-impact actions. Design idempotency and rollback where possible.

### Observability

Record which model/session requested a tool, validated arguments, authorization decision, result summary, errors, and downstream state change while protecting secrets. Evaluate agents with adversarial/synthetic cases before increasing tool authority.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 25, 39, 41.

### Practice task

Design a fictional agent with no network or destructive tools first. Define tool permissions, user approval boundaries, data provenance, prompt/tool injection defenses, logs, limits, and rollback.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **22, 26, 49, 59**.
