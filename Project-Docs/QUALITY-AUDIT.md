# Quality Audit

<!-- MAINTENANCE: Update this report whenever a release receives a full-project quality review. -->

## Release reviewed

**Review date:** 11 August 2026  
**Scope:** the complete Hacking Guide Project source tree, both language editions, generated combined editions, launcher, manifest, indexes, and maintenance scripts.

This project is large enough that no responsible maintainer should claim it is literally incapable of containing an error. The release is instead described as **quality-reviewed and validation-clean**: the checks below completed successfully at release time, and the project includes automated checks intended to catch regressions.

## What was reviewed

The release review covered:

- every source Markdown file line by line with automated structural and content linting;
- all 140 English and 140 Greek numbered lesson files;
- English/Greek module-number and category parity;
- headings and fenced code blocks;
- relative Markdown links and URL-decoded paths;
- trailing whitespace, malformed replacement characters, and NUL bytes;
- remote Markdown image dependencies;
- stale project naming and obsolete launcher references;
- selected unsafe legacy material, including anti-forensics, destructive flooding, credential-dumping syntax, public-target examples, shell-spawning examples, and operational detection-evasion patterns;
- repeated long paragraphs within individual source files;
- Python syntax and JSON parsing;
- generated category indexes;
- generated combined Markdown and HTML editions;
- the Termux-friendly numbered interface, including first-run language selection, English/Greek search, bilingual search, lesson opening, categories, quick guides, progress, bookmarks, recent history, and state persistence.

## Repairs made during the review

The audit did not merely verify the previous build. It found and corrected defects, including:

- an unbalanced Markdown code fence;
- inherited heading-hierarchy problems;
- stale exam-oriented legacy wording and public-target examples in early lessons;
- anti-forensics/log-clearing material in the legacy system-hacking chapter;
- old detection-evasion framing;
- remote image dependencies and legacy HTML formatting;
- repeated generic study boilerplate in later English lessons;
- repeated/condensed template material in parts of the Greek edition;
- inconsistent Greek lab headings;
- superseded pre-August-2026 ATT&CK references, updated to the current v19.2 release used by this edition;
- an interactive-reader bug where Complete or Bookmark reopened a long lesson from page one;
- a validator bug where importing the audit module could create `__pycache__` and then fail its own cleanliness rule.

Reusable study methodology is now centralized in `English/Guides/STUDY-METHOD.md` and `Greek/Guides/STUDY-METHOD.md`, allowing individual modules to focus on their actual technical subject.

## Validation commands

Run these from the repository root before a release:

```console
PYTHONDONTWRITEBYTECODE=1 python3 scripts/quality_audit.py
PYTHONDONTWRITEBYTECODE=1 python3 scripts/build_all.py
PYTHONDONTWRITEBYTECODE=1 python3 scripts/build_all.py --check
PYTHONDONTWRITEBYTECODE=1 python3 scripts/quality_audit.py --include-generated
PYTHONDONTWRITEBYTECODE=1 python3 scripts/smoke_test.py
python "Hacking Guide Project.py" --language both --doctor
```

`Combined/All-Modules.md` and `Combined/All-Modules.html` are generated artifacts. Do not hand-edit them; edit the numbered source lessons and rebuild.

## Content-maintenance standard

For future changes:

1. Keep English and Greek module numbering/category placement synchronized.
2. Prefer current primary specifications and first-party documentation for version-sensitive claims.
3. Keep exercises confined to owned, explicitly authorized, localhost, disposable, or intentionally vulnerable lab environments.
4. Teach mechanism, evidence, mitigation, and verification without adding destructive, credential-theft, stealth, persistence, or public-target operational recipes.
5. Avoid generic filler. Reusable study process belongs in the Study Method guides; lesson files should contain topic-specific knowledge.
6. Run both the structural builder and strict quality audit after every significant content or navigation change.

## Release metrics

- English numbered lessons: **140 modules / 128,013 words / 3,031 indexed sections**.
- Greek numbered lessons: **140 modules / 116,097 words / 1,789 indexed sections**.
- Total numbered-lesson content: **244,110 words**.
- Total indexed lesson sections: **4,820**.
- Category structure: **11 English + 11 Greek category folders**, each with a generated `README.md` index.
- Root Markdown footprint: **two files (`README.md` and `LICENSE.md`)**. The GitHub security policy lives at `.github/SECURITY.md`.

The two language editions intentionally preserve the same module numbers and category placement. Greek technical prose retains international protocol, API, standard, command, and product terminology in English where translating the term would reduce technical precision.

## Release status

At the time this report was produced, the source and generated trees passed the project validators with no reported audit findings. Runtime menu regression tests also completed successfully using a clean temporary state file.
