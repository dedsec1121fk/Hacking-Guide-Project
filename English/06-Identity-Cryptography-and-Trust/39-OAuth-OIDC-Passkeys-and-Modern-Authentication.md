# OAuth, OIDC, Passkeys and Modern Authentication

> **Purpose:** Understand modern authentication and authorization protocols well enough to design, review, and troubleshoot secure identity flows.

## Authentication versus authorization

- **Authentication** establishes an identity or authenticator relationship.
- **Authorization** decides whether an identity/client can perform an action.
- **Federation** allows one security domain to rely on identity assertions from another.

OAuth 2.x is primarily an authorization framework. OpenID Connect adds an identity layer. Treating an OAuth access token and an OIDC ID token as interchangeable is a common design error.

## Core actors

OAuth terminology includes:

- resource owner;
- client;
- authorization server;
- resource server.

OIDC adds identity concepts such as the ID token and user information.

## Redirect URIs

Redirect URI handling is a major trust boundary. Register exact, minimal redirect destinations and avoid permissive wildcard patterns when possible. The authorization server must not send sensitive authorization results to attacker-controlled locations.

## State, nonce, and PKCE

These mechanisms solve different problems. Designs should use protocol-recommended protections rather than inventing custom request correlation.

PKCE binds authorization requests to the client instance that initiated them and is particularly important for public clients.

## Token handling

Access tokens are bearer credentials unless a sender-constrained design is used. Minimize exposure:

- do not place tokens in logs;
- use TLS;
- use short lifetimes appropriate to risk;
- scope tokens narrowly;
- rotate/revoke refresh tokens as supported;
- validate issuer, audience, expiry, signature, and relevant claims.

## Session versus token

A browser application can use a server-side session even when the backend uses OAuth. “JWT everywhere” is not inherently more secure. Choose the simplest model that satisfies trust boundaries and operational needs.

## MFA

MFA strength depends on authenticator properties and resistance to phishing/replay, not merely the number of screens shown. NIST SP 800-63 Revision 4 provides current digital identity and authenticator guidance.

## Passkeys

Passkeys are based on FIDO/WebAuthn public-key credentials and can provide strong phishing resistance. The private key remains bound to an authenticator ecosystem rather than being sent to the relying party.

Account recovery remains critical. A strong login method can be undermined by a weak recovery flow.

## Federation risks

Review:

- identity-provider trust;
- client registration;
- signing keys;
- key rotation;
- audience restrictions;
- tenant boundaries;
- logout/session revocation;
- account linking;
- deprovisioning.

## Service-to-service identity

Machine identities require lifecycle management too. Avoid permanent shared API keys where short-lived workload identities or managed credentials are available.

## Safe design lab

Draw an OIDC authorization-code flow for a fictional web app. Mark:

1. browser;
2. application backend;
3. identity provider;
4. redirect URI;
5. authorization code;
6. PKCE verifier/challenge;
7. ID token;
8. access token;
9. session cookie.

For each artifact, state who may see it, where it is stored, and how long it is valid.

**Learning goal:** security improves when token purpose and trust boundaries are explicit.

## Primary references

- NIST SP 800-63-4: https://csrc.nist.gov/pubs/sp/800/63/4/final
- WebAuthn: https://www.w3.org/TR/webauthn-3/
- FIDO Alliance passkeys: https://fidoalliance.org/passkeys/

## Modern authentication in more depth

OAuth 2.x is primarily an authorization framework; OpenID Connect adds an identity layer. Treat access tokens, refresh tokens, ID tokens, sessions, cookies, passkeys, and recovery credentials as different objects with different audiences and lifecycles.

### Redirect and client trust

Redirect URI handling, client type, PKCE, state/nonce, issuer validation, audience validation, and token storage are core design decisions. Mobile/public clients cannot safely keep a client secret in the same way as a backend confidential client.

### Passkeys

Passkeys use public-key credentials and can provide phishing-resistant authentication. Deployment still requires account recovery, device lifecycle, enrollment security, and policies for high-risk actions. A strong login can be undermined by weak recovery or session management.

### Step-up and transaction authorization

Do not treat one successful login as permanent authorization for every action. High-impact changes may require fresh authentication, stronger factors, explicit user confirmation, or policy checks based on risk.

### Telemetry

Log authenticator enrollment/removal, recovery events, token/session issuance/revocation, unusual sign-ins, administrative identity changes, and high-risk authorization failures without logging secret token contents.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 11, 20, and 21.

### Practice task

Draw an OAuth/OIDC authorization flow for a fictional app, identify client/resource/authorization-server roles, token audience, redirect URI, session boundaries, and passkey recovery assumptions.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **40, 41, 49, 52**.
