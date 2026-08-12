# Python for Security Automation

> **Purpose:** Use Python to automate defensive security work safely, reproducibly, and with strong input/output controls.

## Security automation mindset

Automation should reduce repetitive work without hiding decisions. A script that can change many systems quickly needs stronger safeguards than a command used once by an experienced operator.

Design for:

- explicit scope;
- validated input;
- deterministic output;
- bounded concurrency;
- dry-run modes where changes occur;
- useful logs;
- graceful errors;
- testability.

## Parsing structured data

Security tools often emit JSON, CSV, XML, or line-oriented logs. Prefer structured formats over scraping colorful terminal output.

Example pattern:

```python
import json
from pathlib import Path

data = json.loads(Path("findings.json").read_text())
for finding in data:
    print(finding.get("severity"), finding.get("title"))
```

Never assume keys exist or types are correct when ingesting untrusted data.

## Hashing and integrity

SHA-256 is useful for file integrity identifiers:

```python
import hashlib
from pathlib import Path

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()
```

A hash proves equality of bytes when computed correctly; it does not prove the file is benign or trustworthy.

## HTTP clients

When automating authorized API checks, define timeouts, validate TLS, handle rate limits, and avoid logging secrets. Do not disable certificate verification to make errors disappear.

## Concurrency

Concurrency can accidentally turn a harmless checker into a service-impacting load generator. Use small explicit worker limits, rate limits, and retry budgets. Default to conservative values.

## Subprocess security

Prefer:

```python
subprocess.run(["program", "--flag", value], check=True)
```

over command strings. Validate file paths and arguments. Avoid passing untrusted text to a shell.

## Secrets

Read secrets from an appropriate secret store or environment rather than source code. Redact them in logs and exception messages. Rotate any real secret that reaches Git history.

## SQLite for local evidence

Python's built-in SQLite support is useful for normalized local collections such as asset inventories, lab results, and detection-test records. Use parameterized queries rather than string formatting SQL statements.

## Logging pattern

```python
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
```

Decide what belongs in logs before production use.

## CLI design

Use `argparse` for clear help, required arguments, defaults, and mutually exclusive options. A good tool should explain itself with `--help`.

## Safe project ideas

- Local guide search engine.
- File-integrity inventory.
- CVE/asset correlation using downloaded authorized datasets.
- Log normalizer for synthetic events.
- Configuration linter.
- SBOM comparison tool.
- Certificate-expiry inventory for owned services.
- Backup verification utility.
- Markdown link validator.

## Testing

Separate parsing and decision logic from I/O so it can be unit tested. Include malformed input, empty data, Unicode, duplicate entries, and partial files.

## Lab — Security findings normalizer

Create three sample scanner-export files in different JSON shapes. Write an adapter for each format and normalize to:

```text
asset, finding_id, title, severity, evidence, status
```

Then deduplicate exact duplicates and produce a Markdown summary. Use only synthetic data.

**Learning goal:** automation is most valuable when it improves data quality and repeatability.

## Python automation engineering

Security scripts often start as one-off utilities and quietly become operational dependencies. Design them as small software projects from the beginning.

### Inputs and validation

Accept explicit command-line arguments, validate file paths and expected schema, bound input sizes where practical, and fail with clear messages. Never assume external JSON/CSV/log data contains every field or valid types.

### Secrets

Do not hardcode tokens/passwords. Use environment variables, OS/application secret stores, or approved vault systems as appropriate. Avoid printing secret values in debug output. If a token must be tested, log only a safe identifier or last few characters if policy permits.

### Determinism and evidence

Include timestamps/timezone in reports, preserve original input when evidence matters, and make output reproducible. For parsers, keep a small synthetic fixture so you can test behavior after code changes.

### Error handling

Differentiate expected operational errors (missing file, malformed record, timeout) from programming bugs. Use non-zero exit codes for failure and avoid broad exception handlers that silently hide errors.

### Dependencies

Prefer the standard library when it meets the need. When third-party packages are justified, pin/manage them according to the project's policy, monitor vulnerabilities, and document why the dependency is required.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 28–31 and Python basics.

### Practice task

Write a local defensive utility that reads synthetic JSON/log data, validates input, produces a report, handles errors, and includes tests. Do not make network exploitation the program's purpose.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **23, 37, 45, 59**.
