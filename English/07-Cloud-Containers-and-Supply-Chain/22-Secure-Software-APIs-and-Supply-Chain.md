# Secure Software, APIs, and Supply Chain

> **Purpose:** Reduce vulnerabilities before deployment and manage risk introduced by dependencies, build systems, APIs, and third-party components.

## Secure by design

Secure software starts with architecture and product decisions. CISA's Secure by Design principles emphasize making customer security a core business requirement rather than an optional feature.

Key practices include threat modeling, secure defaults, least privilege, safe error handling, security acceptance criteria, review of high-risk changes, automated checks in CI/CD, and a supported update/vulnerability-disclosure process.

## API security

The OWASP API Security Top 10 2023 highlights authorization, authentication, object-property access, resource consumption, sensitive business flows, server-side request forgery, inventory, and unsafe third-party API consumption.

### API review checklist

- Authenticate callers with a supported mechanism.
- Authorize **every** object and sensitive operation server-side.
- Validate request size, structure, type, and allowed fields.
- Apply pagination, quotas, and rate limits to expensive operations.
- Keep an inventory of endpoints, versions, owners, and data classifications.
- Remove deprecated endpoints.
- Restrict outbound integrations and validate destination/response data.
- Log actor, target, outcome, and correlation identifiers for security-relevant actions.

## Software supply-chain security

Supply-chain risk includes source code, dependencies, registries, build runners, CI credentials, artifacts, container images, signing keys, and update channels.

### Defensive controls

1. Pin or constrain dependencies deliberately and review updates.
2. Generate/retain an SBOM where useful.
3. Protect CI/CD credentials and prefer short-lived workload identities.
4. Separate untrusted pull-request execution from release credentials.
5. Sign or attest release artifacts according to project needs.
6. Retain build provenance sufficient for investigation.
7. Scan for secrets before commits/releases.
8. Maintain a way to identify where a vulnerable component is deployed.

## Safe lab

Create a tiny local API with two users and two objects. Write tests proving each user can access only their own object. Add rate limiting and structured audit logging.

## References

- OWASP API Security Project — https://owasp.org/www-project-api-security/
- OWASP Top 10:2025 — https://owasp.org/Top10/2025/
- CISA Secure by Design — https://www.cisa.gov/securebydesign

## Secure development lifecycle

Security should be represented in the normal engineering workflow rather than added only before release. A practical lifecycle includes security requirements, architecture review, threat modeling, safe implementation patterns, code review, automated checks, pre-release validation, vulnerability handling, supported updates, and retirement planning.

### Security requirements

Write requirements that can be tested. “Use strong security” is not verifiable; “administrative actions require MFA and produce an immutable audit event containing actor, action, target, outcome, and timestamp” is. High-risk requirements should have an owner and an acceptance test.

### Threat modeling

Threat modeling identifies valuable assets, trust boundaries, entry points, dependencies, privileged components, and misuse cases before implementation choices harden. The goal is not to predict every attacker technique. The goal is to expose assumptions early enough that architecture can change cheaply.

A lightweight review can ask:

1. What data or capability is valuable?
2. Who should be allowed to use it?
3. Where does trust change?
4. What input comes from an untrusted party or system?
5. Which component can make an irreversible or high-impact change?
6. What happens if a dependency, identity, or build system is compromised?
7. What evidence would help investigate misuse?

## API authorization patterns

APIs should not infer authorization from possession of an object identifier or from a client-side control. For each endpoint, define the caller, object, action, and policy condition. Test negative cases as carefully as success cases.

### Object-level authorization

When an API receives an object ID, it must verify that the authenticated caller is permitted to perform the requested action on that object. Automated tests should include cross-user and cross-tenant requests, not just valid requests.

### Function-level authorization

Administrative or sensitive functions should have explicit policy checks. Hiding an endpoint in a UI, using an obscure route name, or assuming “normal users will never call it” is not authorization.

### Property-level authorization

Mass assignment can occur when a server binds arbitrary client-supplied fields to an internal object. Define which fields are writable for each operation and role. Sensitive properties such as role, tenant, price, owner, or approval status should not become writable merely because they appear in a JSON body.

## Resource and business-flow protection

Rate limiting should reflect resource cost and abuse risk, not only requests per second. Expensive exports, password-reset messages, image processing, AI inference, search, and bulk operations may need separate quotas. Business flows such as purchasing scarce inventory, sending invitations, creating accounts, or applying promotional credits can be abused even when each individual API request is technically valid.

## API inventory and lifecycle

Maintain an inventory containing endpoint or service name, owner, environment, authentication method, data classification, public/private exposure, supported version, and retirement date. Unknown or forgotten APIs are difficult to patch, monitor, or decommission safely.

Version retirement should include consumer discovery, migration communication, telemetry to identify remaining use, and a controlled shutdown. “Deprecated” endpoints that remain reachable indefinitely are part of the active attack surface.

## Third-party API consumption

Treat responses from external APIs as untrusted input. Validate schema and size, constrain redirects and destinations where relevant, use timeouts, handle partial failure safely, and avoid passing external content directly to interpreters. Store only the data required for the business purpose and document what happens when the provider is unavailable or compromised.

## Software supply-chain model

A release can be compromised without a vulnerability in the application source code. Important trust points include:

- developer accounts and signing credentials;
- source repositories and branch protections;
- package managers and dependency registries;
- CI runners and build images;
- build scripts and reusable workflow actions;
- artifact registries and release buckets;
- container base images;
- update mechanisms and signing keys;
- generated code, model files, plugins, and vendor binaries.

### Dependency governance

Inventory direct and transitive dependencies where practical. Remove unused packages, constrain versions intentionally, understand update ownership, and know which deployed applications contain a vulnerable component. An SBOM can support this inventory, but an SBOM by itself does not determine whether a component is reachable, exploitable, or business-critical.

### CI/CD hardening

CI systems often hold powerful credentials and execute untrusted or semi-trusted code. Separate pull-request validation from release privileges, minimize runner persistence, restrict outbound access where practical, use short-lived identity federation instead of stored cloud keys, protect environment approvals, and review changes to workflow files with the same care as application code.

### Build provenance and artifact integrity

For important releases, retain enough evidence to answer: which source revision produced this artifact, what build environment ran, which dependencies were resolved, who approved the release, and whether the artifact changed afterward? Signing and attestations can strengthen this chain, but key protection and verification policy remain essential.

## Secure by default checklist

- New accounts begin with the least privilege required.
- Security logging is enabled without requiring a premium add-on.
- Dangerous legacy protocols or compatibility modes are disabled by default.
- Secrets are not shipped as sample production credentials.
- Administrative interfaces are not publicly exposed by default.
- High-risk features require explicit enablement and clear documentation.
- Updates can be delivered safely and customers receive actionable vulnerability information.
- Failures default to a safe state when authorization or policy evaluation cannot complete.

## Code review security prompts

During review, ask whether the change adds a new trust boundary, parser, external call, file operation, privilege, secret, deserialization path, authentication state, background job, or user-controlled redirect. These prompts make review more consistent than relying on a reviewer to remember every vulnerability category.

## Defensive lab extension

Extend the toy API lab with a CI workflow that runs unit tests, dependency checks, and a secret scanner. Create a mock release artifact and record its source commit and checksum. Then simulate a dependency update and document how you would determine which environments need the new build. No external exploitation is required; the exercise is about traceability and control quality.

## Further primary references

- NIST Secure Software Development Framework — https://csrc.nist.gov/projects/ssdf
- CISA Secure by Design — https://www.cisa.gov/securebydesign

## 2026 application-assurance update — OWASP ASVS 5.0 and exploitation context

OWASP ASVS 5.0.0 is the current major verification-standard release. Use ASVS as a source of testable application-security requirements, especially where a broad awareness list such as the OWASP Top 10 is not detailed enough.

For vulnerability prioritization, technical severity should be combined with asset context and credible exploitation evidence. CISA's Known Exploited Vulnerabilities catalog is a useful source for vulnerabilities known to be exploited in the wild.

Primary references:
- https://owasp.org/www-project-application-security-verification-standard/
- https://www.cisa.gov/known-exploited-vulnerabilities-catalog

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 14, 20, and Git basics.

### Practice task

For a small project you own, inventory dependencies, create an SBOM if your ecosystem supports it, define API authorization tests, and document CI/CD secret boundaries.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **24, 40, 41, 50**.
