# 2026 Full Quality Review — 11 August 2026

- Performed an independent line-by-line Markdown audit across the complete English/Greek source tree and then reran it against generated outputs.
- Rewrote legacy core Modules 1–16 to remove exam-oriented legacy framing, public-target examples, anti-forensics instructions, operational detection-evasion material, and obsolete remote lab dependencies.
- Modernized Modules 17–20, including mobile, IoT/OT, cloud, and cryptography coverage.
- Removed repeated generic workflow boilerplate from older and advanced English lessons and centralized reusable learning methodology in `STUDY-METHOD.md`.
- Reworked Greek Modules 17–85 so they no longer rely on repeated condensed study templates; retained mirrored module numbering and category placement.
- Reworked the advanced 86–140 material to emphasize topic-specific mechanisms rather than repeated stock paragraphs.
- Fixed Markdown fence/heading defects, trailing whitespace, legacy HTML, remote-image dependencies, stale names, and inconsistent Greek lab headings.
- Fixed the interactive reader so Complete and Bookmark update in place rather than restarting the lesson from page one.
- Localized the Greek pager and additional navigation text.
- Added `scripts/quality_audit.py` and integrated strict audit checks into `scripts/build_all.py`.
- Added `scripts/smoke_test.py` for reproducible launcher/search/menu/state regression testing using only the Python standard library.
- Updated MITRE ATT&CK references from v19.1 to v19.2, the August 2026 data release used by this edition.
- Added `Project-Docs/QUALITY-AUDIT.md` to document the release review and reproducible validation procedure.

## 2026 Expansion III — Hacking Guide Project rename and Modules 116–140

- Standardized the project/browser branding as **Hacking Guide Project** everywhere, including the launcher filename, commands, menus, documentation and local state path.
- Expanded bilingual parity to **140 English + 140 Greek modules**.
- Added Modules 116–140 covering heap allocators, concurrency/TOCTOU, IPC/RPC, sandboxing, macOS/iOS internals, cellular/RF security, HTTP/3/QUIC, DNSSEC/encrypted DNS, CDN/cache security, serialization/deserialization, SAML/SCIM/PAM/WebAuthn, KMS/HSM architecture, Git/SBOM trust, Kubernetes admission, service mesh, cloud detection, RAG security, AI-generated-code review and Advanced Authorized Labs III.
- Made the build validator derive the expected module range from `manifest.json` rather than hard-coding 115.
- Extended learning paths with `identity-federation`, `modern-transport`, `platform-security`, and `secure-ai-development`.

# Expanded Edition — Revision Notes

This revision modernizes the uploaded handbook while preserving its role as an ethical-cybersecurity learning reference.

## Structural changes

- Repaired duplicate and missing module numbering.
- Split enumeration into its own Module 04.
- Corrected Module 15 to Penetration Testing.
- Split the former combined mobile/IoT material into Module 17 Mobile Security and Module 18 IoT/OT Security.
- Renamed and reframed the legacy IDS/firewall-evasion chapter around defensive detection validation.
- Added Modules 21–27 for identity/Zero Trust, secure software/APIs/supply chain, detection/IR/hunting, containers/Kubernetes/DevSecOps, AI/LLM security, assessment reporting/purple teaming, and authorized labs.
- Added Modules 28–31 as a dedicated Termux curriculum.
- Added Modules 32–50 covering Windows/Active Directory, Linux hardening, threat intelligence/OSINT, email/DNS, Python automation, forensics, ransomware recovery, OAuth/OIDC/passkeys, ASVS 5.0, threat modeling, GRC/privacy, disclosure ethics, endpoint/SaaS security, capstones, agentic AI/MCP, SOC/SIEM/SOAR, disaster recovery, PKI/secrets, and vulnerability/attack-surface management.
- Added Modules 51–60 for networking fundamentals, HTTP/browser internals, memory-safety defenses, hardware/firmware/boot security, Bluetooth/NFC, Android internals, privacy/data handling, career/portfolio development, security metrics, and physical/human resilience.
- Added Modules 61–85 as an advanced security-research tier covering research methodology, CPU/syscall/process internals, x86-64/ARM64 assembly, ELF/PE loaders, crash triage, memory-corruption mechanics and mitigations, reverse engineering, fuzzing, advanced web/browser/API internals, Kerberos/AD, Windows/Linux internals, Kubernetes/container isolation, cloud IAM/control planes, protocol reverse engineering, TLS/PKI implementation failures, malware analysis, ATT&CK v19 detection engineering, advanced forensics, Android reversing, firmware analysis, patch diffing, and authorized capstones.
- Added Modules 86–140 covering IPv6/Neighbor Discovery, DNS/BGP infrastructure, enterprise wireless, GraphQL/gRPC/WebSockets, data stores, event streaming, OAuth 2.0 Security BCP, authorization models, virtualization/confidential computing, kernel security/eBPF, SLSA 1.2 and package ecosystems, compiler/toolchain hardening, cryptographic protocol engineering, PQC migration, side channels, TPM/attestation/TEEs, serverless and multi-cloud security, EDR internals, purple-team design, advanced code auditing, vulnerability research workflow, WebAssembly/managed runtimes, Electron/extensions, workload identity, data security, and master capstones.

## Modernization

- OWASP Top 10 updated to the 2025 release.
- OWASP Mobile Top 10 updated to the 2024 release.
- Vulnerability-prioritization material updated for CVSS v4.0.
- Cybersecurity-framework material updated for NIST CSF 2.0.
- Added NIST Zero Trust Architecture concepts.
- Added NIST post-quantum standards: ML-KEM, ML-DSA, and SLH-DSA.
- Added OWASP API Security Top 10 2023 coverage.
- Added OWASP GenAI/LLM 2026 security coverage.
- Added current secure-software, cloud-native, Kubernetes, CI/CD, and software-supply-chain material.
- Added NIST SP 800-61 Rev. 3 incident-response concepts and NIST SP 800-63 Revision 4 identity guidance.
- Added OWASP ASVS 5.0.0, OWASP Top 10 for Agentic Applications 2026, and current MCP security guidance.
- Added official Termux ecosystem references and Android/Termux platform lessons.
- Added current Android security/Keystore/permission references and deeper browser/networking guidance.
- Updated the advanced detection tier for MITRE ATT&CK v19.2 (August 2026), while retaining the v19 tactic-model changes introduced in April 2026.

## Safety and quality changes

- Removed live packet-flood recipes.
- Removed reverse-shell command examples.
- Removed anti-forensics/log-clearing commands.
- Removed operational IDS/firewall-bypass recipes.
- Replaced Wi-Fi password-cracking walkthroughs with authorized configuration and resilience testing.
- Reframed credential-dumping/cracking material as defensive password and credential-store auditing.
- Replaced sensitive file-reading demonstrations with harmless lab fixtures.
- Added explicit authorization, scope, evidence-minimization, and stop-condition guidance.
- Added 30 localhost/owned-system/deliberately-vulnerable labs.
- Added a guided-study workflow to every module: prerequisites, practice task, evidence, common mistakes, mastery check, and next steps.
- Added START-HERE.md, LAB-GUIDE.md, TERMUX-QUICKSTART.md, REFERENCE-CHEATSHEET.md, and ADVANCED-TRACK.md.

## Maintenance workflow

`scripts/build_all.py` now validates:

- continuous module numbering and bilingual/category parity;
- duplicate module numbers;
- URL-decoded relative Markdown links;
- strict source-quality rules provided by `scripts/quality_audit.py`, including Markdown structure, stale naming, selected unsafe legacy patterns, repeated long paragraphs, Python syntax, JSON validity, and cache-file cleanliness.

It also rebuilds `All-Modules.md` and `All-Modules.html` from the numbered source modules so the combined editions do not drift.

The edition now includes `Hacking Guide Project.py`, a dependency-free local full-text search and lesson browser designed for Termux and desktop Python.

## Size

After the quality review removed duplicated boilerplate, the project still contains a large bilingual curriculum while being materially denser and less repetitive. Exact English, Greek, and combined word/section counts should be taken from `python "Hacking Guide Project.py" --language both --stats` for the current checkout rather than copied into documentation as a stale hard-coded figure.

## Bilingual categorized restructuring

- Moved all numbered Markdown lessons out of the repository root.
- Added 11 stable category folders under both `English/` and `Greek/`.
- Added a Greek lesson for every Module 001–140 with Greek study guidance, lab methodology, evidence requirements, mastery checks, and English technical terminology where appropriate.
- Added matching English and Greek `Guides/`, `Combined/`, README files, and per-category indexes.
- Added `manifest.json` so module numbers map deterministically to category folders.
- Reworked `Hacking Guide Project.py` for recursive category discovery and `--language en`, `--language gr`, or `--language both` searches.
- Reworked `scripts/build_all.py` to enforce 140/140 language parity, validate category structure and links, and rebuild both combined editions.
## Easier browsing update

- Reworked the `Hacking Guide Project.py` home screen around Continue, Categories, Search, Paths, Bookmarks, Progress, Guides, and All Modules.
- Added persistent progress, recent-lesson history, and bookmarks in `~/.hacking-guide-project/state.json`.
- Added in-reader Next/Previous navigation and complete/bookmark actions.
- Interactive search now deduplicates repeated section hits so the first screen favors distinct modules.
- Replaced category `INDEX.md` files with category `README.md` files so GitHub automatically renders each lesson index when a category folder is opened.
- Added friendly English and Greek category names and completion counts.
- Updated the build validator to regenerate and verify category `README.md` indexes.
## License and security policy

- Added `LICENSE.md` using the MIT License.
- Added bilingual `.github/SECURITY.md` with private-reporting guidance, repository scope, safe-research expectations and disclosure guidance.
- Updated README, contributing guidance, maintenance documentation and automated validators to require the policy files.

