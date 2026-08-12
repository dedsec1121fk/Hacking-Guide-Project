# Packet Capture, Sniffing and Network Visibility

Packet capture provides direct evidence about communication between systems. It is valuable for troubleshooting, incident response, protocol analysis, and authorized security testing, but captured traffic can contain credentials, tokens, personal data, and sensitive business information.

> **Authorized-use boundary:** Capture traffic only on networks and interfaces you own or are explicitly authorized to monitor. Prefer your own localhost/VM lab or prerecorded captures. Do not intercept third-party wireless or switched-network traffic.

## Learning objectives

- understand packet capture points and visibility limitations;
- distinguish Ethernet, IP, TCP/UDP, DNS, TLS, and application-layer evidence;
- use capture filters and display filters conceptually;
- understand switched networks, SPAN/TAP, and host capture points;
- protect sensitive packet-capture data;
- correlate packet evidence with host/application logs.

## What a packet capture proves

A capture proves what the capture point observed. It does not automatically prove what happened elsewhere. Packets can be lost before capture, offloaded by the NIC, altered by proxies, encrypted, retransmitted, or observed on only one side of a NAT or load balancer.

Always record:

- capture interface and location;
- timestamps and time source;
- capture filter;
- relevant IP addresses and ports;
- whether traffic is before or after NAT/proxying;
- packet loss or capture limitations.

## Protocol layers

A useful analysis sequence is:

1. **Link layer:** source/destination MAC, VLAN, frame type.
2. **Network layer:** IPv4/IPv6 addresses, TTL/hop limit, fragmentation.
3. **Transport:** TCP sequence/state or UDP datagrams.
4. **Naming/control:** DNS, ICMP, routing or discovery messages.
5. **Security:** TLS handshake metadata, certificate information, negotiated protocol.
6. **Application:** HTTP or other cleartext protocol only when legitimately observable.

Encryption may hide payload content while still leaving useful metadata such as endpoints, timing, volume, protocol negotiation, and certificate information.

## Switched networks

On a normal switched Ethernet network, a host does not automatically receive every other host's unicast traffic. Defenders use approved capture points such as switch mirror/SPAN ports, network TAPs, gateway sensors, host agents, or cloud traffic-mirroring features.

Do not use address-poisoning or interception techniques on shared networks simply to “see more traffic.” Build an isolated lab if you need to study those protocol failure modes.

## Filters

Capture filters reduce what is collected; display filters reduce what is shown after collection. A narrow capture can protect privacy and reduce storage but may omit context needed later. A broad capture can contain excessive sensitive data. Choose based on the investigation question.

Example with `tcpdump` on your own localhost interface:

```bash
tcpdump -i lo tcp port 8000
```

Then generate a normal local request to a service you started yourself. Stop the capture immediately after the test.

## TCP analysis

Useful TCP evidence includes SYN/SYN-ACK/ACK, sequence numbers, retransmissions, resets, window behavior, and connection teardown. Retransmissions can indicate packet loss or congestion; they are not automatically malicious.

## DNS analysis

DNS captures can reveal queried names, resolver behavior, response codes, TTLs, and differences between A/AAAA responses. Encrypted DNS may move visibility to endpoints or approved resolver logs instead of network payload inspection.

## TLS analysis

Without session keys, modern TLS normally protects application content. Analysts can still examine protocol versions, certificate metadata, server names where exposed by the protocol/deployment, connection timing, and endpoint relationships. Do not weaken TLS in production just to make packet inspection easier.

## Packet-capture handling

PCAP files can contain passwords from legacy cleartext protocols, bearer tokens, cookies, email content, identifiers, internal hostnames, or confidential documents. Store captures with access controls, short retention where possible, and sanitized extracts for reports.

## Common mistakes

- Capturing on an interface without knowing where it sits in the path.
- Assuming absence of a packet means the event never occurred.
- Keeping huge captures full of unnecessary sensitive data.
- Treating retransmissions or resets as attacks without context.
- Disabling encryption for visibility rather than using endpoint telemetry.
- Capturing traffic that belongs to third parties.

## Safe lab

Start a localhost HTTP server, capture only TCP/8000 on the loopback interface, make two requests, and stop the capture. Identify connection setup, request/response packets, teardown, and timestamps. Then compare the packet timeline with the server's access log.

## Knowledge check

1. What does a packet capture prove and what does it not prove?
2. Why does capture location matter?
3. What is the difference between capture and display filters?
4. Why can encrypted traffic still provide useful metadata?
5. What privacy risks exist in PCAP files?

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md). Build conclusions from packet evidence plus at least one other source such as host or application logs.

### Continue with

Recommended next modules: **12, 23, 51, 77**.
