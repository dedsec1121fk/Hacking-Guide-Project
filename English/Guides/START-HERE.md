# Start Here — Learning Guidance

This guide is a curriculum, reference library and lab notebook framework. You do **not** need to read every module in numeric order.

## Recommended first route

For a new learner: **001 → 028 → 029 → 051 → 052 → 005 → 011 → 014 → 021 → 027 → 045**.

At each module use the same loop: understand the security model, identify trust boundaries, perform only the safe practice task, keep evidence, explain one limitation, and decide what to learn next.

## Choose a specialization

From the main menu choose **Learning paths**. Useful tracks include Termux, Blue Team, AppSec, Cloud, Mobile, AI, Reverse Engineering, Identity, Protocols, Detection, Supply Chain, Modern Cryptography, Cloud Native, Purple Team, and Code Audit.

## How to study a hard topic

1. **Vocabulary:** define unfamiliar terms in one sentence.
2. **Architecture:** draw components, data flows, identities and trust boundaries.
3. **State:** identify what changes over time—sessions, tickets, processes, routes, keys, leases or policy decisions.
4. **Evidence:** decide which logs, packets, traces, settings or artifacts would prove the expected behavior.
5. **Failure mode:** explain how an incorrect assumption could fail.
6. **Control:** choose a preventive, detective or recovery control.
7. **Retest:** define how you would prove the control works after remediation.

## Safe practice standard

Use localhost, isolated VMs/containers, emulators, synthetic identities and intentionally vulnerable training systems. Never interpret a public IP, nearby Wi‑Fi network, third-party account or exposed service as permission to test it.

## Notes that become a portfolio

For meaningful labs keep: objective, scope, environment/version, diagram, procedure, evidence, result, limitation, remediation and retest. A reproducible five-page lab report demonstrates more skill than a long list of commands with no reasoning.
