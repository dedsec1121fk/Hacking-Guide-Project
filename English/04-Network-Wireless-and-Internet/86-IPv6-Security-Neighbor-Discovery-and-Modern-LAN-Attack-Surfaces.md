# IPv6 Security, Neighbor Discovery and Modern LAN Attack Surfaces

IPv6 changes host discovery, address assignment, local-link trust, routing behavior, firewall assumptions, and evidence collection. This lesson treats IPv6 as a first-class security architecture rather than an optional extension of IPv4.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, or lab environments you own or are explicitly authorized to test. The exercises in this module are designed to prove security properties without targeting third parties.

## Learning objectives

By the end of this module you should be able to:

- Explain **Address architecture** and connect it to a concrete trust boundary or security invariant.
- Explain **Neighbor Discovery** and connect it to a concrete trust boundary or security invariant.
- Explain **SLAAC and DHCPv6** and connect it to a concrete trust boundary or security invariant.
- Explain **Extension headers** and connect it to a concrete trust boundary or security invariant.
- Explain **Fragmentation and PMTUD** and connect it to a concrete trust boundary or security invariant.
- Explain **Dual-stack exposure** and connect it to a concrete trust boundary or security invariant.

## Analysis method

Use the shared [Study Method](../Guides/STUDY-METHOD.md). For this module, first draw the relevant components and state transitions, then state one security invariant and identify the minimum evidence needed to test it safely.

## Deep concepts

### 1. Address architecture

Global unicast, unique-local, link-local, multicast, temporary/privacy addresses, and interface identifiers have different security and observability implications. Security reviews should identify which address classes are expected on each interface and which should never cross a routing boundary.



### 2. Neighbor Discovery

IPv6 replaces ARP with ICMPv6 Neighbor Discovery. Router Advertisements, Neighbor Solicitations, Neighbor Advertisements, and Redirects are control-plane messages; filtering them blindly can break connectivity, while trusting them blindly can create local-network risk.



### 3. SLAAC and DHCPv6

Stateless autoconfiguration and DHCPv6 can coexist. A network can therefore have several sources of addressing, DNS configuration, and default-route state. Asset inventories and NAC controls need to account for those sources rather than assuming one DHCP lease equals one endpoint.



### 4. Extension headers

IPv6 extension headers separate optional functions from the fixed header. Security devices must parse chains consistently, apply bounded work, and avoid policy gaps caused by unusual ordering, fragmentation, or unsupported combinations.



### 5. Fragmentation and PMTUD

Only endpoints fragment ordinary IPv6 packets. Path MTU Discovery and ICMPv6 Packet Too Big messages are operationally important; over-aggressive ICMPv6 blocking can create reliability failures that masquerade as application problems.



### 6. Dual-stack exposure

A service hardened on IPv4 can remain reachable through IPv6. Every listening socket, ACL, reverse proxy, VPN rule, DNS record, and monitoring pipeline should be checked for parity across both protocol families.



### 7. Local-link trust

First-hop security depends on switch features, RA policy, segmentation, endpoint firewalls, and predictable configuration. Treat the local segment as potentially hostile rather than assuming devices sharing a VLAN are mutually trusted.



### 8. Telemetry

Useful IPv6 evidence includes address lifetimes, RA sources, neighbor-cache changes, DNS AAAA responses, route changes, firewall decisions, and application bind addresses. Normalize addresses before correlation to avoid equivalent textual forms being treated as different hosts.



## Review focus

Apply the failure-mode taxonomy in [Study Method](../Guides/STUDY-METHOD.md), but keep the analysis specific to this lesson: identify the principal, resource, authority, mutable state, parser or policy boundary, and the telemetry that would distinguish a real control failure from misconfiguration or an observation gap.

## Authorized exercises

### Exercise 1 — Build a two-host or two-namespace IPv6-only localhost lab and document addresses, routes, neighbor entries, and DNS behavior without sending traffic outside the lab

Build a two-host or two-namespace IPv6-only localhost lab and document addresses, routes, neighbor entries, and DNS behavior without sending traffic outside the lab.


### Exercise 2 — Compare an application bound to 127

Compare an application bound to 127.0.0.1, ::1, 0.0.0.0, and :: in an owned environment; record exactly which interfaces become reachable.


### Exercise 3 — Create a firewall-review worksheet that checks IPv4 and IPv6 policy parity for one lab service

Create a firewall-review worksheet that checks IPv4 and IPv6 policy parity for one lab service.

Use the lab-record format in [Study Method](../Guides/STUDY-METHOD.md) for each exercise and keep all inputs synthetic or confined to the authorized lab.

## Knowledge checks

1. Explain the most important trust boundary in **IPv6 Security, Neighbor Discovery and Modern LAN Attack Surfaces** without naming a security tool.
2. Give one example where cryptographic or authentication success still does **not** imply authorization success.
3. Describe one stale-state or replay condition relevant to this module.
4. Identify one telemetry source that can support a strong conclusion and one blind spot it still leaves.
5. Explain how you would turn a discovered weakness into a regression test rather than a one-time finding.

## Guided study workflow

Use [Study Method](../Guides/STUDY-METHOD.md). Complete at least one authorized exercise, preserve the evidence that supports your conclusion, and explain the module's main trust boundary and failure modes in your own words before moving on.

### Continue with

Choose **Learning paths** from the main menu for an ordered specialization, or use **Search lessons** to follow a concept into related modules.
