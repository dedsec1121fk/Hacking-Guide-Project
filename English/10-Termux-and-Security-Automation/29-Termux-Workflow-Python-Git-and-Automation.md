# Termux Workflow, Python, Git and Automation

> **Purpose:** Turn a basic Termux installation into a disciplined coding, automation, and study environment.

## Learning objectives

- Use Git safely from Android.
- Manage Python virtual environments and dependencies.
- Write maintainable shell and Python utilities.
- Back up work without leaking secrets.
- Build repeatable project structures rather than one-off command histories.

## A simple workspace model

Keep active projects under one predictable directory:

```text
~/projects/
  project-a/
  project-b/
~/notes/
~/backups/
```

Each project should explain what it is, how to run it, what it depends on, and what data it writes. A small `README.md` is more valuable than a complicated folder tree nobody understands later.

## Git fundamentals

Install Git with the Termux package manager and configure identity deliberately. Learn these concepts before automation:

- repository
- working tree
- staging area
- commit
- branch
- remote
- merge/rebase
- `.gitignore`

A safe daily sequence is:

```bash
git status
git diff
git add path/to/file
git commit -m "Describe the change"
```

Review `git diff --cached` before committing important changes. Never place API tokens, private keys, recovery codes, or production credentials in a repository.

## SSH keys for Git hosting

For accounts that support SSH authentication, use a modern key type supported by your provider and protect the private key. The public key can be shared; the private key cannot.

Use separate keys when separation improves risk management, and know how to revoke them. A key is a credential, not just a file.

## Python in Termux

Python is well suited to local automation because Termux provides a normal command-line interpreter and much of the standard library.

Create a project-specific virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

Prefer pinned or constrained dependency versions for reproducibility. Keep dependency files under source control, but never include `.venv/` itself.

## Standard-library-first automation

Before adding a package, check whether Python already provides what you need:

- `argparse` — command-line interfaces
- `pathlib` — paths
- `json` / `csv` — structured data
- `sqlite3` — local databases
- `hashlib` — integrity hashing
- `subprocess` — controlled external commands
- `urllib` — basic HTTP clients
- `logging` — logs
- `re` — regular expressions
- `concurrent.futures` — bounded concurrency

Reducing dependencies lowers setup friction and supply-chain exposure.

## Shell scripting discipline

For Bash scripts, quote variables and enable defensive modes when appropriate:

```bash
set -euo pipefail
```

But understand what those options do before copying them into every script. Error handling should be intentional: a maintenance script may need to stop on the first failure, while a diagnostic collector may need to continue and report partial results.

## Configuration versus code

Do not hardcode machine-specific paths, tokens, or usernames when a configuration file or environment variable is more appropriate. Validate configuration before use and provide safe defaults.

Example pattern:

```python
from pathlib import Path

workspace = Path.home() / "projects"
workspace.mkdir(exist_ok=True)
```

## Logging

Good automation explains what happened without exposing secrets. Logs should contain enough context to troubleshoot:

- timestamp
- operation
- target file or local component
- outcome
- error category

Do not log passwords, bearer tokens, session cookies, full private keys, or sensitive personal data.

## Safe subprocess use

Prefer argument arrays rather than building shell commands from untrusted text:

```python
subprocess.run(["git", "status"], check=True)
```

Avoid `shell=True` unless the shell itself is required and every value is controlled. This is a core defense against command-injection bugs in automation.

## Data formats

Use JSON for structured machine-readable records and Markdown for human notes. CSV works well for flat inventories. SQLite is useful when searches and relationships become more complex.

## Backups

A project is not backed up merely because it is on the phone. Use at least one independent copy. For Git projects, a remote repository can protect source history, but secret material and generated data may need a different encrypted backup path.

Test restoration. A backup that has never been restored is an assumption.

## Termux-friendly editor workflow

Use whichever editor you can operate reliably. The security goal is not a particular editor; it is making small, reviewable changes with history. Pair the editor with `git diff` and lint/test commands.

## Automation project template

```text
project/
  README.md
  src/
  tests/
  data/
  output/
  .gitignore
```

Keep inputs separate from outputs. This makes cleanup, backup, and evidence handling easier.

## Mini lab — Build a local file inventory tool

Create a Python program that walks a test directory and records filename, size, modification time, and SHA-256 hash into JSON. Add:

1. command-line argument for the root directory;
2. clear errors for missing paths;
3. exclusion for the output file itself;
4. deterministic ordering;
5. a verification mode that reports changed files.

Use only synthetic files.

**Learning goal:** combine paths, hashing, structured output, and safe CLI design.

## Maintenance checklist

- Can the project be installed from the README?
- Are dependencies documented?
- Are secrets excluded?
- Are output paths predictable?
- Are errors actionable?
- Is there a dry-run mode for destructive maintenance tasks?
- Are tests available for parsing and validation logic?

## Practical workflow drills

### Project isolation

Create separate directories for notes, scripts, samples, and generated output. Keep generated data out of Git unless it is intentionally part of the project. A clean project makes errors easier to reproduce and protects you from accidentally committing sensitive or bulky artifacts.

### Python error-handling exercise

Write a small script that accepts a local filename, verifies the file exists, reads text using UTF-8 with a documented fallback policy, counts lines, and exits with a clear error when the input is missing. Add `argparse` help. This teaches input validation and predictable command-line behavior without depending on external APIs.

### Git recovery exercise

Commit a working file, make a deliberate harmless change, inspect `git diff`, commit again, and use `git log` to explain the history. Learn to restore a file from a known commit in a disposable repository. Version control is part of security engineering because it makes changes attributable and recoverable.

## Automation design guidance

A good mobile automation script should have explicit inputs, deterministic output, useful exit codes, no embedded secrets, safe defaults, and a `--help` path. Prefer creating output files rather than silently modifying source data. When an operation is destructive, require a deliberate option and document rollback.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Module 28.

### Practice task

Create a Git-backed notes project and a Python virtual environment. Write a small script that parses a local text file, commit it, deliberately break it, then use Git history and your notes to recover.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **30, 31, 36**.
