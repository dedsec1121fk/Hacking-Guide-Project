# DNS, Routing, BGP and Internet Infrastructure Security

Internet security depends on naming and routing systems that are distributed, cached, policy-driven, and only partially under any single organization’s control. This module explains the trust model and failure modes without treating Internet infrastructure as a target.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, or lab environments you own or are explicitly authorized to test. The exercises in this module are designed to prove security properties without targeting third parties.

## Learning objectives

By the end of this module you should be able to:

- Explain **DNS resolution chain** and connect it to a concrete trust boundary or security invariant.
- Explain **DNSSEC** and connect it to a concrete trust boundary or security invariant.
- Explain **Registrar and zone control** and connect it to a concrete trust boundary or security invariant.
- Explain **Anycast and recursive services** and connect it to a concrete trust boundary or security invariant.
- Explain **BGP path selection** and connect it to a concrete trust boundary or security invariant.
- Explain **Route-origin validation** and connect it to a concrete trust boundary or security invariant.

## Analysis method

Use the shared [Study Method](../Guides/STUDY-METHOD.md). For this module, first draw the relevant components and state transitions, then state one security invariant and identify the minimum evidence needed to test it safely.

## Deep concepts

### 1. DNS resolution chain

Stub resolvers, recursive resolvers, authoritative servers, delegations, caching, negative caching, and DNSSEC each participate in answering a name. A useful investigation separates “who asked,” “who recursed,” “who is authoritative,” and “what was cached.”



### 2. DNSSEC

DNSSEC provides origin authentication and integrity for signed DNS data; it does not encrypt queries and it does not make a maliciously registered domain trustworthy. Validation failures should be distinguished from ordinary NXDOMAIN, SERVFAIL, and transport failures.



### 3. Registrar and zone control

Domain takeover risk often begins in account security, delegation mistakes, stale records, or forgotten cloud resources rather than in the DNS protocol itself. Protect registrar identity, enforce MFA, inventory NS/DS records, and track ownership of every externally referenced resource.



### 4. Anycast and recursive services

Large DNS services commonly use anycast. The same service address can terminate at different sites, so latency, path, and incident evidence can vary geographically even when the logical destination is unchanged.



### 5. BGP path selection

BGP exchanges reachability between autonomous systems. Routing policy, prefix specificity, local preference, AS paths, communities, and business relationships influence which path is selected; BGP is not a shortest-path protocol in the ordinary sense.



### 6. Route-origin validation

RPKI and route-origin validation help networks evaluate whether an AS is authorized to originate a prefix. They improve one part of routing assurance but do not prove the entire AS path is legitimate.



### 7. Control-plane monitoring

Defenders should baseline authoritative DNS changes, certificate issuance, route announcements, RPKI state, nameserver changes, and cloud endpoint ownership. External control-plane drift can be an early sign of configuration failure or account compromise.



### 8. Resilience design

Use multiple authoritative DNS servers/providers where appropriate, protect registrar recovery, document TTL strategy, maintain break-glass contacts, and rehearse domain/routing incident playbooks before an outage occurs.



## Review focus

Apply the failure-mode taxonomy in [Study Method](../Guides/STUDY-METHOD.md), but keep the analysis specific to this lesson: identify the principal, resource, authority, mutable state, parser or policy boundary, and the telemetry that would distinguish a real control failure from misconfiguration or an observation gap.

## Authorized exercises

### Exercise 1 — Trace the full resolution path for a domain you own using passive/publicly documented information and draw the delegation chain

Trace the full resolution path for a domain you own using passive/publicly documented information and draw the delegation chain.


### Exercise 2 — Create a tabletop exercise for accidental deletion of a DNS zone and list recovery dependencies in order

Create a tabletop exercise for accidental deletion of a DNS zone and list recovery dependencies in order.


### Exercise 3 — Build a worksheet that separates DNS integrity, DNS confidentiality, registrar security, certificate issuance, and routing security controls

Build a worksheet that separates DNS integrity, DNS confidentiality, registrar security, certificate issuance, and routing security controls.

Use the lab-record format in [Study Method](../Guides/STUDY-METHOD.md) for each exercise and keep all inputs synthetic or confined to the authorized lab.

## Knowledge checks

1. Explain the most important trust boundary in **DNS, Routing, BGP and Internet Infrastructure Security** without naming a security tool.
2. Give one example where cryptographic or authentication success still does **not** imply authorization success.
3. Describe one stale-state or replay condition relevant to this module.
4. Identify one telemetry source that can support a strong conclusion and one blind spot it still leaves.
5. Explain how you would turn a discovered weakness into a regression test rather than a one-time finding.

## Guided study workflow

Use [Study Method](../Guides/STUDY-METHOD.md). Complete at least one authorized exercise, preserve the evidence that supports your conclusion, and explain the module's main trust boundary and failure modes in your own words before moving on.

### Continue with

Choose **Learning paths** from the main menu for an ordered specialization, or use **Search lessons** to follow a concept into related modules.
