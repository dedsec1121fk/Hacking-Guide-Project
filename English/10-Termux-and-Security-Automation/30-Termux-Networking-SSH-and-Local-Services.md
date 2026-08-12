# Termux Networking, SSH and Local Services

> **Purpose:** Learn networking from an Android/Termux environment while keeping exercises limited to localhost, owned devices, and explicitly authorized systems.

## Networking mental model

Separate these layers when troubleshooting:

1. interface and address;
2. route;
3. name resolution;
4. transport connection;
5. TLS;
6. application protocol;
7. authentication and authorization.

A browser error saying a page did not load does not tell you which layer failed.

## Local interfaces and routes

Inspect your own device configuration with platform-available tools. `ip addr` and `ip route` show addressing and routing when supported by the environment. `ss` can show local listening sockets and established connections.

The important security question is **what address a service is bound to**:

- `127.0.0.1` / `::1` — local device only.
- a Wi-Fi/LAN address — potentially reachable by peers on that network.
- `0.0.0.0` / `::` — all available interfaces, often broader than intended.

For learning services, default to localhost.

## DNS basics

DNS maps names to records such as A/AAAA, MX, TXT, CNAME, and others. Learn to distinguish a DNS failure from a routing or TLS failure. Do not assume a successful DNS lookup means the service is trustworthy.

## HTTP and HTTPS inspection

`curl` is useful for defensive validation:

```bash
curl -I https://example.com
```

Headers can reveal redirects, cache controls, content types, and security policies. For your own services, compare expected versus observed behavior.

## Running a localhost-only development service

A safe exercise is serving a disposable directory to the same device:

```bash
mkdir -p ~/projects/local-demo
cd ~/projects/local-demo
printf 'hello\n' > index.html
python -m http.server 8000 --bind 127.0.0.1
```

This is not a production server. It is intentionally simple and useful for learning ports, processes, requests, and logs.

## SSH concepts

SSH provides encrypted remote terminal and file-transfer capabilities. The security model depends on:

- host authenticity;
- user authentication;
- private-key protection;
- server configuration;
- authorized keys;
- network exposure.

Termux can act as an SSH client and, when deliberately configured, can run an SSH server for your own device. If you do this, use strong key-based authentication, understand the listening address, and avoid exposing the service to the public internet.

## Host-key verification

The first SSH connection usually introduces a host key. Treat unexpected host-key changes as an event to investigate rather than clicking through automatically. Legitimate causes include reinstallations and key rotations, but an unexpected change can also indicate connecting to the wrong host.

## Port forwarding concepts

SSH tunneling can securely connect applications across trusted endpoints, but it can also bypass intended network boundaries if misused. In authorized environments, document tunnel purpose, endpoints, ports, and lifespan. Remove temporary tunnels after use.

## File transfer

Use `scp`, `sftp`, or another encrypted transfer mechanism for owned systems. Validate destination paths before sending sensitive files from a phone, where autocomplete and touch input make mistakes easy.

## Local service inventory

Periodically check which programs are listening:

```bash
ss -lnt
```

For every listening service, be able to answer:

- What process owns it?
- Why is it running?
- Which interface is it bound to?
- Does it need authentication?
- Should it start automatically?

## VPNs and Android

Android VPN apps affect routing from the device, but behavior depends on VPN implementation, split tunneling, always-on settings, and app exclusions. When troubleshooting, record whether the VPN is active before drawing conclusions from network tests.

## Wireless limitations

A normal non-root Termux environment does not magically provide monitor mode or low-level Wi-Fi capabilities. Hardware, kernel, driver, Android permission, and root constraints matter. This guide does not depend on bypassing those constraints.

## Mini lab — Local service map

1. Start two harmless services on different localhost ports.
2. Use `ss` to record listeners.
3. Use `curl` to query the HTTP service.
4. Stop one service.
5. Repeat the inventory and document the difference.
6. Explain what would change if the service were bound to the LAN address instead.

**Learning goal:** connect processes, ports, interfaces, and application behavior.

## Mini lab — SSH trust checklist

On two devices you own, create a checklist covering:

- server address;
- expected host-key fingerprint;
- user account;
- authentication method;
- key revocation plan;
- listening interface;
- firewall/network boundary;
- backup access method.

The lab is complete when you can explain the trust relationship, not merely when a login succeeds.

## Practical networking drills in Termux

### Loopback first

Before exposing any development service to Wi-Fi or another interface, make it work on `127.0.0.1`. Verify the listening socket and application log. This separates application problems from network-reachability problems and dramatically reduces accidental exposure.

### SSH administration checklist

For an SSH server you own, document the account used, authentication method, listening interface, port, host-key verification, client key storage, log location, and shutdown procedure. Prefer key-based authentication and never place the private key in Android shared storage merely to make it easier to find.

### Name-resolution exercise

Use a domain you control or a well-known public documentation domain to observe ordinary DNS resolution. Compare the name you typed with the returned addresses and explain why a DNS answer is only one step in establishing application identity; TLS certificate validation and application authentication are separate controls.

## Mobile networking limitations

Some low-level networking tools need kernel capabilities or interfaces unavailable to an unrooted Android app. Treat that as a platform boundary, not a problem to bypass. Focus Termux on user-space networking, local services, SSH, HTTP clients, DNS tools, log analysis, automation, and interaction with systems you are explicitly authorized to administer.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 28, 29, and 51.

### Practice task

Run a loopback-only HTTP service and inspect your own listening socket plus request logs. Explain why binding to loopback is safer than exposing a learning service on every interface.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **31, 36, 51, 52**.
