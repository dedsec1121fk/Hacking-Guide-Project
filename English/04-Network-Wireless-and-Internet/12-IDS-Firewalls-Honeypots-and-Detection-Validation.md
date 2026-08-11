# Firewalls, IDS/IPS, Honeypots and Detection Validation

Preventive and detective controls are valuable only when their policy, coverage, telemetry, and failure modes are understood. This module explains how to validate network and host controls without attempting to bypass or disable them.

> **Authorized-use boundary:** Detection testing must use approved events and known test sources. Do not evade monitoring, disable controls, flood sensors, or create deceptive activity outside an authorized lab or coordinated purple-team exercise.

## Learning objectives

- distinguish stateless filtering, stateful filtering, proxies, WAFs, IDS, IPS, EDR, and deception systems;
- understand policy order, default action, zones, identity, and application context;
- design detection-validation tests with expected telemetry;
- measure false positives, false negatives, and visibility gaps;
- use honeypots safely;
- turn test results into control improvements.

## Firewalls

A firewall enforces policy between trust zones or workloads. Rules should be reviewed for source, destination, protocol, port/application, identity where supported, direction, action, logging, owner, and expiry.

Common weaknesses include overly broad sources, `any/any` rules, shadowed rules, forgotten temporary exceptions, IPv4/IPv6 mismatch, management interfaces exposed to user networks, and rules whose business owner no longer exists.

## Stateful filtering

Stateful devices track connection state, but “stateful” does not mean “secure.” Policy still needs correct direction, service identity, timeout behavior, and logging. Asymmetric routing or proxies can complicate interpretation.

## Proxies and WAFs

Reverse proxies and WAFs terminate or inspect application traffic and can enforce normalization, rate limits, authentication integration, or application-layer rules. They should not be treated as substitutes for secure application code and server-side authorization.

## IDS and IPS

An IDS observes and alerts; an IPS can block or modify traffic depending on design. Detection quality depends on placement, parsing, signatures/analytics, tuning, encryption visibility, time synchronization, asset context, and downstream triage.

A detection test should state the expected result in advance: which sensor sees the event, which log contains it, whether an alert is expected, and who receives it.

## EDR and host telemetry

Endpoint controls may observe process creation, file changes, network activity, registry/configuration changes, identity events, memory behavior, or script execution. Coverage differs by platform and policy. Validate specific telemetry rather than assuming “EDR installed” equals “everything visible.”

## Honeypots and deception

A honeypot is a deliberately monitored decoy. It should be isolated, contain no real sensitive data, have no path to become a pivot into production, and clearly fall under organizational policy. The value is high-signal observation, not retaliation.

## A detection-validation loop

1. Define a benign event representing the behavior to detect.
2. Record source, target, identity, and time.
3. Predict which telemetry should exist.
4. Generate the event in an approved lab.
5. Verify raw telemetry before alert logic.
6. Verify detection and triage routing.
7. Document blind spots and false assumptions.
8. Tune the control and rerun the same test.

## Useful metrics

- telemetry coverage;
- alert precision and recall where measurable;
- time from event to ingest;
- time from ingest to alert;
- time to triage;
- percentage of alerts with enough identity/asset context;
- rule ownership and last validation date.

## Common mistakes

- Testing whether monitoring can be bypassed rather than whether it detects the intended behavior.
- Assuming an alert proves the underlying event occurred exactly as described.
- Ignoring raw telemetry and only checking the SIEM rule.
- Leaving temporary firewall rules indefinitely.
- Deploying deception systems with real credentials or production reachability.
- Forgetting IPv6 and cloud control-plane logs.

## Safe lab

Create a local service and a host firewall rule that allows only localhost. Generate one allowed and one denied connection from controlled sources. Verify the firewall evidence. Then generate a harmless known test event and trace it from raw log to alert or dashboard.

## Knowledge check

1. Why does control placement matter?
2. What is the difference between raw telemetry and a detection?
3. Why is an `any/any` rule hard to govern?
4. What makes a honeypot safe to operate?
5. Why should detection validation be repeatable?

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md). Preserve expected-versus-observed evidence for every control test.

### Continue with

Recommended next modules: **23, 47, 59, 80, 106**.
