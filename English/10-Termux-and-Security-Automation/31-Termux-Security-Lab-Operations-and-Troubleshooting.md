# Termux Security Lab Operations and Troubleshooting

> **Purpose:** Build safe cybersecurity labs on Android and diagnose common Termux failures without turning the phone into an uncontrolled tool dump.

## Lab design principles

A good mobile lab has five properties:

1. **Authorized** — every target is yours or explicitly provided for training.
2. **Isolated** — localhost, private test networks, emulators, or disposable cloud labs with explicit permission.
3. **Resettable** — data and configuration can be recreated.
4. **Observable** — logs and expected behavior are available.
5. **Documented** — scope, objective, steps, result, and cleanup are recorded.

## What Termux is excellent for

- Python and shell programming.
- Git-based coursework.
- HTTP/API client experiments against local labs.
- Cryptography demonstrations.
- Log parsing and text processing.
- Hashing and integrity checks.
- Static inspection of files you own.
- SSH administration of systems you control.
- Local documentation and note search.
- Lightweight web development.

## What often needs a different environment

Some exercises depend on kernel features, drivers, virtualization, packet-capture privileges, or desktop tooling that an ordinary Android sandbox does not provide. Use a VM, dedicated lab machine, emulator, or authorized cloud environment when the learning objective requires those capabilities.

Do not force a tool to work on Termux by weakening the phone's security when a safer lab platform is available.

## Proot distributions

User-space distribution environments can provide familiar Linux package layouts, but they do not turn Android into a native virtual machine and do not remove kernel or hardware limitations. Treat them as compatibility environments, not privilege boundaries.

## Dependency troubleshooting

When installation fails, capture:

```bash
python --version
pkg list-installed
uname -a
```

Then identify whether the failure is caused by:

- missing compiler or headers;
- package not available for Android architecture;
- Python wheel unavailable for the platform;
- native dependency expecting glibc rather than Android's C library;
- outdated installation instructions;
- storage path or permission problems.

Prefer maintained packages from the Termux repositories when they satisfy the requirement.

## Repository troubleshooting

If package metadata fails to refresh, consult the current Termux package-management guidance rather than copying a random mirror command. Repository infrastructure changes over time.

## Python troubleshooting

Useful checks:

```bash
python -m pip --version
python -c "import sys; print(sys.executable); print(sys.path)"
```

When a package fails to build, read the first meaningful compiler/error line rather than only the final `pip` summary.

## Storage troubleshooting

If a script works in `$HOME` but fails in Downloads, investigate Android storage semantics and permissions. Do not paper over the problem with broad recursive permission changes.

## Long-running processes

Android battery optimization can stop background activity. For legitimate long-running administration, understand Android power-management constraints and design around resumable state. A security learning script should save progress rather than assume it will run forever.

## Safe local vulnerable applications

Deliberately vulnerable applications are useful when they are isolated and their license permits local training. Keep them bound to localhost or a private lab network and remove them after the exercise.

Never expose an intentionally vulnerable service directly to the internet.

## Note-taking workflow

For each lesson, save:

```text
Objective:
Scope:
Environment:
Expected result:
Observed result:
Evidence:
What failed:
Why it failed:
Fix:
Security lesson:
```

This turns troubleshooting into reusable knowledge.

## The Hacking Guide Project browser and search menu

This edition includes `Hacking Guide Project.py`, a local browser and full-text search interface designed for Termux and desktop Python. It uses the Python standard library and searches only the local guide files.

For normal use, start the launcher once and use the numbered menus. **Search lessons** accepts ordinary words, **Popular topics** provides shortcuts, **Categories** groups related modules, **Learning paths** gives an ordered route, and **Continue** returns to the last lesson. No search flags or module commands are required.

The browser does not scan networks, enumerate targets, or perform exploitation. It only reads and indexes the local Markdown knowledge base.

## Termux capstone — Portable defensive notebook

Build a small repository containing:

- Markdown study notes;
- a file integrity checker;
- a log parser for synthetic logs;
- a local HTTP service inventory;
- JSON output;
- tests;
- a README explaining safe scope.

Use Git history to show how the project evolves. The capstone demonstrates the core skill of turning commands into controlled, auditable workflows.

## Troubleshooting decision tree

1. **Does the command exist?** Use `command -v`.
2. **Is the path correct?** Use `pwd`, `ls`, and quoted paths.
3. **Is permission denied?** Identify which Android/Unix permission is involved.
4. **Is a port unavailable?** Inspect local listeners.
5. **Is Python importing the wrong environment?** Check `sys.executable` and active venv.
6. **Is a package outdated or renamed?** Check current official package metadata.
7. **Is the tutorial assuming desktop Linux?** Identify unsupported assumptions.
8. **Can the task be reproduced in a minimal directory?** Reduce variables.

## Safety rule

If solving a Termux problem would require bypassing device security, disabling protections globally, or testing an unknown third-party system, change the lab design instead.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 28–30.

### Practice task

Practice recovery: verify paths, permissions, package availability, Python version, storage links, and a backup of your notes. Write a troubleshooting decision tree for your device.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **36, 45, 56**.
