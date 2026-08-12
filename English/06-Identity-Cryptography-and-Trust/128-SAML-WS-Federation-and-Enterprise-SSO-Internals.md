# SAML, WS-Federation and Enterprise SSO Internals

Develop a deep model of enterprise browser federation: assertions, bindings, metadata, signatures, audience, subject confirmation, relay state, session lifetime and trust between identity providers and service providers.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, captures, or lab environments you own or are explicitly authorized to test. Prefer localhost, synthetic data, disposable VMs/containers, prerecorded traces, and read-only analysis whenever possible.

## Learning objectives

By the end of this module you should be able to:

- Explain **IdP and SP trust roles** and identify its most important trust boundary, state transition, and evidence source.
- Explain **SAML assertions and conditions** and identify its most important trust boundary, state transition, and evidence source.
- Explain **browser SSO profiles and bindings** and identify its most important trust boundary, state transition, and evidence source.
- Explain **metadata and signing keys** and identify its most important trust boundary, state transition, and evidence source.
- Explain **audience and recipient validation** and identify its most important trust boundary, state transition, and evidence source.
- Explain **NameID and attribute mapping** and identify its most important trust boundary, state transition, and evidence source.

## Analysis method

Use [Study Method](../Guides/STUDY-METHOD.md). Start by identifying ownership or identity, the state transition that can fail, and the evidence that would distinguish a real boundary violation from a diagnostic artifact.

## Deep concepts

### 1. IdP and SP trust

SAML separates an Identity Provider that asserts identity from a Service Provider that consumes assertions. The SP must trust only configured issuers/keys and apply its own authorization; a valid assertion from the wrong tenant or relationship is not sufficient.

### 2. assertions and conditions

Assertions contain subject, authentication, attributes, and conditions such as time windows. Validate the complete security context—issuer, signature, audience, recipient/destination, time, subject confirmation, and expected flow—not just the presence of a signature.

### 3. browser SSO profiles and bindings

SAML browser SSO moves protocol messages through the browser using defined bindings. Track which message is request/response state, which values are attacker-controlled in transit, and how the SP correlates the response to the initiating session.

### 4. metadata and signing keys

Metadata distributes entity identifiers, endpoints, certificates, and capabilities. Treat metadata changes and key rollover as high-impact configuration events with authenticated distribution, overlap windows, audit trail, and tested rollback.

### 5. audience and recipient validation

Audience and recipient/destination fields prevent an assertion intended for one service or endpoint from being reused elsewhere. Validation must compare against canonical local configuration rather than values learned from the incoming request.

### 6. NameID and attribute mapping

Attributes become local identity/role data only after mapping rules are applied. Avoid trusting mutable display names or email strings as stable privileged identifiers; define collision, case, domain, and missing-attribute behavior explicitly.

### 7. RelayState and request correlation

RelayState carries application navigation/context and should not become an unvalidated open redirect or authorization source. Correlate responses with the original authentication request/session and keep application state separate from identity proof.

### 8. logout and session lifetime

SAML logout and local application sessions have different lifecycles and reliability. Define what local tokens are revoked when upstream identity changes, what happens if single logout fails, and how administrators terminate sessions during an incident.

## Engineering focus

For this module, convert each important claim into a security invariant and a regression test. Prefer controls that remove unnecessary authority, make state transitions explicit, bound resource use, and leave enough telemetry to explain a failure. The reusable evidence and lab-record format is in [Study Method](../Guides/STUDY-METHOD.md).

## Authorized lab sequence

### Lab 1 — Draw an SP-initiated SSO flow and annotate every signed/unsigned value plus who validates it.



### Lab 2 — Create a fictional assertion-validation checklist and test it against synthetic good/bad assertion descriptions, not real accounts.



### Lab 3 — Model key rollover where old and new IdP signing keys overlap and define safe acceptance windows.

For every lab, use only owned/synthetic inputs and record objective, scope, version, expected behavior, observed evidence, cleanup, remediation, and regression result as described in [Study Method](../Guides/STUDY-METHOD.md).

## Knowledge checks

Answer these without looking at the notes:

1. What is the primary trust boundary in this topic?
2. Which state or identity transition is easiest to misunderstand?
3. What observation would disprove your first hypothesis?
4. Which control removes authority rather than merely adding detection?
5. How would you reproduce the behavior safely after remediation?

## Guided study workflow

Complete at least one authorized lab and explain the mechanism, trust boundary, failure state, evidence, and defensive fix in your own words. Use **Bookmarks**, **Progress**, and **Learning paths** in the numbered menu instead of memorizing command-line flags.

## Next modules

Recommended related modules: **021, 032, 039, 072, 092, 093**. From the main menu, choose **Search lessons** to find related sections across the full guide.
