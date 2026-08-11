# DNSSEC, DoH, DoQ, Resolver Privacy and DNS Trust

Extend DNS knowledge into validation and privacy: DNSSEC trust chains, encrypted resolver transports, resolver discovery, split-horizon behavior, caching and operational failure modes.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, captures, or lab environments you own or are explicitly authorized to test. Prefer localhost, synthetic data, disposable VMs/containers, prerecorded traces, and read-only analysis whenever possible.

## Learning objectives

By the end of this module you should be able to:

- Explain **DNSSEC chain of trust** and identify its most important trust boundary, state transition, and evidence source.
- Explain **DS, DNSKEY and RRSIG roles** and identify its most important trust boundary, state transition, and evidence source.
- Explain **negative answers and authenticated denial** and identify its most important trust boundary, state transition, and evidence source.
- Explain **DoH and DoT** and identify its most important trust boundary, state transition, and evidence source.
- Explain **DNS over QUIC (DoQ)** and identify its most important trust boundary, state transition, and evidence source.
- Explain **resolver policy and discovery** and identify its most important trust boundary, state transition, and evidence source.

## Analysis method

Use [Study Method](../Guides/STUDY-METHOD.md). Start by identifying ownership or identity, the state transition that can fail, and the evidence that would distinguish a real boundary violation from a diagnostic artifact.

## Deep concepts

### 1. DNSSEC chain of trust

DNSSEC authenticates DNS data through signatures and a chain of trust from configured trust anchors through DS and DNSKEY relationships. It provides origin authentication/integrity for DNS records, not confidentiality and not proof that the destination application itself is trustworthy.

### 2. DS, DNSKEY and RRSIG

DNSKEY records publish zone signing keys, DS records link parent and child zones, and RRSIG records carry signatures over RRsets. Operational security depends on correct key rollover, timing, algorithm support, and avoiding broken delegation state during changes.

### 3. authenticated denial of existence

DNSSEC can prove that a requested name or type does not exist using authenticated denial mechanisms. Negative answers are security-relevant state and must be validated/cached with the same care as positive answers.

### 4. DoH and DoT

DNS over HTTPS and DNS over TLS protect resolver traffic in transit to a chosen resolver. Encryption changes visibility and policy enforcement but does not by itself guarantee that the resolver is trustworthy or that returned data is DNSSEC-valid.

### 5. DoQ

DNS over QUIC carries DNS messages over QUIC and inherits encrypted transport, connection, and operational properties from QUIC. Resolver policy, authentication, resource limits, and fallback behavior should be explicit across all supported transports.

### 6. resolver policy and discovery

Endpoints can learn resolvers through network configuration, operating-system policy, applications, enterprise management, or encrypted-DNS discovery. Security teams should know which component wins when policies conflict and which paths bypass enterprise logging/filtering.

### 7. split-horizon DNS

Internal and external resolvers may intentionally return different data. Document the expected namespace and trust boundary so caching, VPN changes, encrypted resolvers, or application-specific DNS do not expose internal names or route users to the wrong service.

### 8. cache TTL and stale answers

Resolvers cache positive and negative answers according to TTL and local policy; some systems can serve stale data during outages. Incident response must account for propagation delay and cache state when rotating addresses, certificates, or maliciously altered records.

## Engineering focus

For this module, convert each important claim into a security invariant and a regression test. Prefer controls that remove unnecessary authority, make state transitions explicit, bound resource use, and leave enough telemetry to explain a failure. The reusable evidence and lab-record format is in [Study Method](../Guides/STUDY-METHOD.md).

## Authorized lab sequence

### Lab 1 — Use public DNSSEC test domains or offline packet examples to follow a validation chain without altering DNS infrastructure.



### Lab 2 — Compare plain DNS, DoH and DoQ at the architecture level: who can observe queries and where trust terminates.



### Lab 3 — Build a cache-timeline exercise showing TTL, stale data and key rollover dependencies.

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

Recommended related modules: **035, 051, 077, 078, 087, 124**. From the main menu, choose **Search lessons** to find related sections across the full guide.
