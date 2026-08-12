# Maintenance Guide

<!-- MAINTENANCE: Review whenever module names or the build workflow change. -->

## Review cadence

Review at least every six months and whenever a major referenced standard changes.

### High-churn items

- OWASP Top 10, API, Mobile, and GenAI guidance.
- NIST CSF and referenced security publications.
- CVSS and NVD/CVE terminology.
- Cryptographic deprecations and PQC standards.
- Cloud, container, Kubernetes, identity, and software-supply-chain practices.
- Android/Termux platform behavior, mobile security, browser/web standards, agentic-AI guidance, MITRE ATT&CK versions, Windows identity documentation, Linux kernel isolation/security interfaces, and Kubernetes security guidance.

## Content rules

1. Prefer primary sources for standards and product/protocol documentation.
2. Mark deprecated technology as **legacy**.
3. Keep commands lab-safe; do not add packet floods, credential theft/dumping, anti-forensics, destructive payloads, or stealth-bypass recipes.
4. Use localhost or deliberately vulnerable training targets in examples.
5. Explain control, evidence, remediation, and retest—not just attack names.
6. Distinguish vulnerabilities from informational observations.

## Release checklist

- [ ] `PYTHONDONTWRITEBYTECODE=1 python3 scripts/quality_audit.py` passes.
- [ ] `PYTHONDONTWRITEBYTECODE=1 python3 scripts/build_all.py --check` passes.
- [ ] README module links work.
- [ ] Combined Markdown/HTML rebuilt with `PYTHONDONTWRITEBYTECODE=1 python3 scripts/build_all.py`.
- [ ] `PYTHONDONTWRITEBYTECODE=1 python3 scripts/quality_audit.py --include-generated` passes after rebuilding.
- [ ] `PYTHONDONTWRITEBYTECODE=1 python3 scripts/smoke_test.py` passes.
- [ ] No duplicate module numbers.
- [ ] No accidental credentials/tokens/private data.
- [ ] High-risk legacy commands were not reintroduced.
- [ ] Versioned standards were checked against primary sources.



The release-level review procedure and audit scope are documented in `Project-Docs/QUALITY-AUDIT.md`.

## Hacking Guide Project search utility

`Hacking Guide Project.py` must remain Python-standard-library-only so a fresh Termux installation needs only the `python` package. After changing module parsing, search behavior, or filenames, run:

```console
python "Hacking Guide Project.py" --start
python "Hacking Guide Project.py" --paths
python "Hacking Guide Project.py" --path termux
python "Hacking Guide Project.py" --advanced
python "Hacking Guide Project.py" --path advanced
python "Hacking Guide Project.py" --stats
python "Hacking Guide Project.py" --search "termux storage" --limit 3
python "Hacking Guide Project.py" --search "incident response" --json
python "Hacking Guide Project.py" --doctor
```

The search utility must remain local/offline: it is a documentation search and reading tool, not a network scanner.

## Advanced-tier maintenance

Modules 61–140 intentionally separate **mechanism understanding** from harmful operationalization. When extending them:

1. Prefer sanitizer reports, policy graphs, local parsers, benign simulations, and regression tests as evidence.
2. Do not add credential dumping, ticket forging, stealth/evasion recipes, persistence deployment, public-target request-smuggling payloads, container escapes, cloud metadata credential extraction, or weaponized exploit chains.
3. Verify ATT&CK release/version before changing Module 80.
4. Re-check Windows, Linux kernel, Kubernetes, Android, OWASP, and crypto references against current primary documentation.
5. Keep `ADVANCED-TRACK.md` and the advanced paths in `Hacking Guide Project.py` synchronized with module numbering.


## Bilingual category architecture

The repository now uses `manifest.json` as the source of truth for module placement.

- `English/<category>/<module>.md` contains the English lesson.
- `Greek/<category>/<module>.md` contains the matching Greek lesson.
- Both languages must contain **exactly Modules 001–140** with the same filenames and category IDs.
- `English/Combined/` and `Greek/Combined/` are generated outputs; do not edit them directly.
- Language guidance lives under each language's `Guides/` folder.
- The repository root should contain only `README.md` and `LICENSE.md` as Markdown files. Keep the security policy at `.github/SECURITY.md`.

When adding, moving, or renaming a lesson, update `manifest.json`, make the change in **both languages**, regenerate the category `README.md` files if needed, and run:

```console
python scripts/build_all.py
python "Hacking Guide Project.py" --language both --doctor
python "Hacking Guide Project.py" --language en --search "test query" --limit 3
python "Hacking Guide Project.py" --language gr --search "δοκιμή" --limit 3
```

Do not allow English and Greek module numbering or category placement to drift apart.
