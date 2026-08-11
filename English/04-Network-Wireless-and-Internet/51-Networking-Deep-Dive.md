# Networking Deep Dive

> **Purpose:** Build the networking knowledge required to understand traffic, segmentation, services, logs, and security controls without treating network tools as black boxes.

## Learning objectives

- Explain Ethernet/Wi-Fi links, IP addressing, routing, transport protocols, DNS, DHCP, NAT, TLS, and proxies.
- Read a basic packet or flow record and identify the important fields.
- Distinguish local-link problems from routing, name-resolution, transport, and application problems.
- Understand IPv6 well enough to avoid designing IPv4-only security assumptions.
- Build a small authorized lab and document how traffic is expected to flow.

## Start with a mental model

A useful practical model is:

1. **Application:** HTTP, DNS, SSH, SMTP, APIs, custom protocols.
2. **Transport:** TCP or UDP identifies endpoints with ports and provides different delivery properties.
3. **Internet/network:** IPv4 or IPv6 addresses packets and routes them between networks.
4. **Link:** Ethernet, Wi-Fi, or another local medium moves frames between directly connected neighbors.

The OSI model is useful vocabulary, but do not let memorizing seven layers replace understanding real data flow.

## Addresses are contextual

A device can have multiple addresses at the same time: loopback, Wi-Fi, cellular, VPN, container, IPv4, and IPv6. Security rules should therefore be based on intended trust boundaries and interfaces rather than the assumption that one device equals one IP address.

Loopback (`127.0.0.1` for IPv4 and `::1` for IPv6) is especially useful for local labs because a service bound only to loopback is not intended to accept connections from other devices.

## Subnets and routing

A subnet prefix identifies which address bits describe the network. For IPv4, CIDR notation such as `/24` is common. For IPv6, `/64` is common on local segments. You should be able to answer:

- Is the destination local or remote?
- Which route will be selected?
- Which gateway is used?
- Which interface sends the traffic?
- Which security control sits on that path?

A routing table is evidence of intended forwarding behavior, not proof that the destination is reachable. Firewalls, policy routing, VPNs, broken gateways, or application binding can still prevent communication.

## TCP and UDP

TCP provides a connection-oriented byte stream with sequencing, retransmission, and congestion control. UDP provides datagrams without TCP's connection state and delivery guarantees. Neither tells you whether the application itself is secure.

When reading network logs, distinguish:

- source/destination address;
- source/destination port;
- transport protocol;
- connection direction;
- bytes/packets;
- start/end timestamps;
- TCP state where available.

## DNS is more than name-to-address lookup

DNS stores multiple record types and is part of many security workflows. Common records include A/AAAA, CNAME, MX, TXT, NS, SOA, PTR, CAA, and service-related records. Security teams should understand:

- recursive versus authoritative resolution;
- caching and TTLs;
- split-horizon/internal DNS;
- DNSSEC's authenticity/integrity role;
- why DNS logs are useful telemetry;
- why a DNS name does not guarantee the identity of the application behind it.

## DHCP and local configuration

DHCP commonly provides clients with addresses, default gateways, DNS servers, and lease information. A network can be operational while still using unsafe configuration. Validate expected DNS, gateway, and address ranges instead of assuming automatically supplied values are trustworthy.

## ARP and IPv6 Neighbor Discovery

IPv4 networks commonly use ARP to resolve local IPv4 neighbors to link-layer addresses. IPv6 uses Neighbor Discovery. Security monitoring should account for both. Networks that deploy IPv6 but only monitor or filter IPv4 can create blind spots.

## NAT is not a security policy

NAT changes address/port information. It is not a substitute for a stateful firewall, authentication, authorization, segmentation, or endpoint hardening. A design should explicitly state which traffic is allowed and why.

## TLS and trust

TLS can provide confidentiality and integrity in transit and authenticate endpoints when certificate validation is correct. Important concepts include:

- certificate chains;
- trust anchors;
- host-name validation;
- protocol/cipher negotiation;
- certificate expiration/rotation;
- application-layer authentication on top of TLS.

Encrypting a malicious or unauthorized request does not make it safe. Transport security and application authorization solve different problems.

## Proxies, gateways, and load balancers

Modern traffic often passes through reverse proxies, API gateways, WAFs, load balancers, service meshes, VPN gateways, and cloud edges. This affects:

- source-address visibility;
- TLS termination;
- logging locations;
- rate limiting;
- authentication context;
- header trust;
- incident investigation.

Document which component is authoritative for client identity and which forwarded headers are trusted.

## IPv6 security guidance

Do not disable or ignore IPv6 merely because the team is more familiar with IPv4. Instead:

- inventory IPv6 interfaces and addresses;
- define equivalent firewall policy;
- monitor IPv6 DNS and traffic;
- understand link-local addresses;
- test applications on both address families where supported;
- document transition mechanisms if present.

## Safe local practice

On your own system, inspect local addressing and listening services using the operating system's standard tools. In Termux, availability varies by Android/version, so use `ip`, `ss`, or documented alternatives when installed.

A safe exercise is to start a loopback-only HTTP server:

```bash
mkdir -p ~/security-lab/network-demo
cd ~/security-lab/network-demo
printf 'network lab\n' > index.txt
python -m http.server --bind 127.0.0.1 8000
```

Then, from another local terminal session, retrieve it:

```bash
curl http://127.0.0.1:8000/index.txt
```

Record the server log, local socket state, and request/response. Stop the service with `Ctrl+C`.

## Troubleshooting ladder

When communication fails, troubleshoot from the simplest dependency outward:

1. Is the process running?
2. Is it bound to the expected address and port?
3. Does loopback access work?
4. Does name resolution produce the expected address?
5. Is a route available?
6. Does a firewall/policy allow the traffic?
7. Does TLS validation succeed?
8. Does the application accept the request and authorization context?
9. Are proxies/gateways changing the request?
10. What do logs on both sides say?

## Security design questions

For every networked service ask:

- Which interfaces should it bind to?
- Who needs to reach it?
- Is network access enough, or is strong application authentication also required?
- What protects traffic in transit?
- Where is access logged?
- What happens if DNS fails or an upstream service is unavailable?
- Can one compromised segment reach another unnecessarily?
- How is IPv6 handled?

## Checkpoint

You are ready to continue when you can draw a request from client to service and label DNS, IPs, ports, routing, TLS termination, identity, and major logs. Next: Module 52 for HTTP/browser depth, Modules 03/04 for authorized discovery concepts, and Module 12 for controls/detection.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Module 01.

### Practice task

Use the localhost exercise in this module, draw the request path, and explain address, route, port, transport, application, and log evidence.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **03, 08, 12, 52**.
