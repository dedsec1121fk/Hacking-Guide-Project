# OAuth 2.0 Security BCP, OIDC Federation and Token Defense

Modern OAuth security guidance has moved beyond older deployment patterns. This module centers RFC 9700/BCP 240 concepts, authorization-code flows with PKCE, sender constraints, redirect integrity, token audience, and the difference between authorization delegation and identity.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, or lab environments you own or are explicitly authorized to test. The exercises in this module are designed to prove security properties without targeting third parties.

## Learning objectives

By the end of this module you should be able to:

- Explain **OAuth roles and purpose** and connect it to a concrete trust boundary or security invariant.
- Explain **Authorization code and PKCE** and connect it to a concrete trust boundary or security invariant.
- Explain **Redirect URI integrity** and connect it to a concrete trust boundary or security invariant.
- Explain **Issuer and mix-up defenses** and connect it to a concrete trust boundary or security invariant.
- Explain **Token audience and scope** and connect it to a concrete trust boundary or security invariant.
- Explain **Refresh tokens** and connect it to a concrete trust boundary or security invariant.

## Analysis method

Use the shared [Study Method](../Guides/STUDY-METHOD.md). For this module, first draw the relevant components and state transitions, then state one security invariant and identify the minimum evidence needed to test it safely.

## Deep concepts

### 1. OAuth roles and purpose

Resource owner, client, authorization server, and resource server are different roles. OAuth delegates authorization; OpenID Connect adds an identity layer. Confusing an access token with an ID token is a recurring design error.



### 2. Authorization code and PKCE

Authorization-code flows keep access tokens out of front-channel URLs. PKCE binds the authorization response to the initiating client instance and is a key defense for public clients and modern deployments.



### 3. Redirect URI integrity

Redirect URIs are security-critical. Use exact matching according to the protocol profile, avoid open redirectors, and treat mobile/custom URI handling and claimed HTTPS links as platform-specific trust decisions.



### 4. Issuer and mix-up defenses

Clients interacting with multiple authorization servers need strong issuer binding and metadata validation so a response from one security domain is not accepted in another context.



### 5. Token audience and scope

A resource server should validate issuer, audience/resource, signature/key, expiry, and authorization claims appropriate to that API. Scope strings are not a substitute for object-level authorization.



### 6. Refresh tokens

Refresh tokens are long-lived authorization artifacts. Rotation, sender constraints, secure storage, revocation, inactivity limits, and anomaly detection reduce the impact of theft.



### 7. Sender-constrained tokens

Mechanisms such as mTLS or proof-of-possession approaches can bind a token to a client-held key. They change the theft model but do not fix an over-privileged token or a compromised client.



### 8. Federation lifecycle

Identity-provider federation adds metadata, signing keys, trust anchors, account linking, tenant discovery, session propagation, logout, and deprovisioning. Model the full lifecycle, not only the login redirect.



## Review focus

Apply the failure-mode taxonomy in [Study Method](../Guides/STUDY-METHOD.md), but keep the analysis specific to this lesson: identify the principal, resource, authority, mutable state, parser or policy boundary, and the telemetry that would distinguish a real control failure from misconfiguration or an observation gap.

## Authorized exercises

### Exercise 1 — Draw an authorization-code + PKCE sequence for a localhost demo and label every value that must be bound to the initiating transaction

Draw an authorization-code + PKCE sequence for a localhost demo and label every value that must be bound to the initiating transaction.


### Exercise 2 — Create a token-validation checklist separating cryptographic validity from authorization decisions at the API

Create a token-validation checklist separating cryptographic validity from authorization decisions at the API.


### Exercise 3 — Review a hypothetical federation design for account-linking ambiguity, stale signing keys, incorrect issuer/audience checks, and deprovisioning gaps

Review a hypothetical federation design for account-linking ambiguity, stale signing keys, incorrect issuer/audience checks, and deprovisioning gaps.

Use the lab-record format in [Study Method](../Guides/STUDY-METHOD.md) for each exercise and keep all inputs synthetic or confined to the authorized lab.

## Knowledge checks

1. Explain the most important trust boundary in **OAuth 2.0 Security BCP, OIDC Federation and Token Defense** without naming a security tool.
2. Give one example where cryptographic or authentication success still does **not** imply authorization success.
3. Describe one stale-state or replay condition relevant to this module.
4. Identify one telemetry source that can support a strong conclusion and one blind spot it still leaves.
5. Explain how you would turn a discovered weakness into a regression test rather than a one-time finding.

## Guided study workflow

Use [Study Method](../Guides/STUDY-METHOD.md). Complete at least one authorized exercise, preserve the evidence that supports your conclusion, and explain the module's main trust boundary and failure modes in your own words before moving on.

### Continue with

Choose **Learning paths** from the main menu for an ordered specialization, or use **Search lessons** to follow a concept into related modules.
