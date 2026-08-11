# Cybersecurity Reference Cheatsheet

## Core questions

- What asset is being protected?
- What identity/process has authority?
- Where is the trust boundary?
- What input/state crosses it?
- Which security property can fail?
- What evidence proves the behavior?
- What control prevents, detects or contains it?
- How will the fix be retested?

## Networking

Remember layers, addresses, routes, ports, state and name resolution. A packet capture shows traffic visible at one observation point; it does not automatically explain application intent.

## Web/API

Trace: client → proxy/CDN → server → framework/router → authorization → data store/downstream service. Check normalization, method/path, headers, body parser, session/token context and object-level authorization.

## Identity

Separate authentication, authorization, session/token lifecycle, federation, key trust and recovery. Short-lived credentials help only when issuance and revocation are also controlled.

## Systems

Think in users/tokens, processes, memory, files, services, syscalls, executable loading and telemetry. Privilege is a graph of capabilities, not only a username.

## Cloud/container

Control plane, workload identity, network/data plane, secrets, build provenance, artifact trust and audit logs are separate layers.

## Evidence quality

Prefer reproducible commands, sanitized logs, hashes, packet/trace metadata, configuration excerpts and before/after validation. Record versions and time.
