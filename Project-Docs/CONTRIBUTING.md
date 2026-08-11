# Contributing

Good contributions include factual corrections with primary sources, clearer defensive explanations, safe labs, detection/remediation/retest guidance, and updates for supported technology.

## Do not add

- commands intended to disrupt third-party services;
- credential theft/dumping instructions;
- stealth/evasion recipes intended to bypass monitoring;
- destructive malware/persistence code;
- anti-forensics/log-clearing procedures;
- real secrets, private data, or stolen datasets.

## Style

Define acronyms on first use, distinguish legacy behavior from current guidance, and include references when a claim depends on a living standard.

Before changes are published:

```console
python3 scripts/build_all.py --check
python3 scripts/build_all.py
```
## Security reports

Do not publish exploitable repository vulnerabilities in a normal issue. Follow the [Security Policy](../.github/SECURITY.md) and use private vulnerability reporting when available.

