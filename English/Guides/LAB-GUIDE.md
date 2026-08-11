# Authorized Lab Guide

Use this guide to convert theory into repeatable, safe practice.

## The lab contract

Before touching the system write: owner, scope, allowed actions, prohibited actions, test window, data classification, rollback method and stop conditions. For a personal lab the owner may simply be you, but writing the boundary trains professional habits.

## Preferred lab order

1. Read-only observation.
2. Configuration review.
3. Harmless functional test.
4. State-changing test only when necessary.
5. Restore/rollback.
6. Retest the defensive control.

## Good lab environments

Localhost services, disposable VMs, containers without sensitive mounts, Android emulators, intentionally vulnerable training apps, sample binaries, synthetic logs and test identity providers.

## Evidence model

Keep timestamps, versions, sanitized config, packet/trace metadata, hashes, screenshots only when they add evidence, and before/after results. Do not collect real passwords, tokens, private keys or unrelated personal data.

## Stop conditions

Stop immediately if the test reaches a system outside scope, causes unexpected availability impact, touches real user data, creates persistence you did not plan, or produces a result you do not understand well enough to reverse safely.

## Reporting

Separate observation from inference. A good finding explains condition, evidence, impact, root cause, affected scope, remediation and a retest method. State uncertainty explicitly.
