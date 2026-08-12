# Hacking Guide Project — All Modules

> Generated from the categorized English modules. Edit individual lessons, then rebuild.

## Index

### 01-Fundamentals-and-Methodology

- 001. [Cybersecurity Foundations and Ethical Hacking Methodology](#cybersecurity-foundations-and-ethical-hacking-methodology)
- 005. [Vulnerability Analysis and Prioritization](#vulnerability-analysis-and-prioritization)
- 026. [Security Assessment Reporting and Purple Teaming](#security-assessment-reporting-and-purple-teaming)
- 041. [Threat Modeling and Security Architecture](#threat-modeling-and-security-architecture)
- 043. [Responsible Disclosure and Bug Bounty Ethics](#responsible-disclosure-and-bug-bounty-ethics)
- 050. [Vulnerability Management and Attack Surface Management](#vulnerability-management-and-attack-surface-management)
- 061. [Security Research Methodology and Attack-Surface Reasoning](#security-research-methodology-and-attack-surface-reasoning)

### 02-Recon-Pentesting-Web-and-AppSec

- 002. [Footprinting, Reconnaissance and Attack-Surface Discovery](#footprinting-reconnaissance-and-attack-surface-discovery)
- 003. [Network Scanning and Service Discovery](#network-scanning-and-service-discovery)
- 004. [Service Enumeration and Protocol-Aware Validation](#service-enumeration-and-protocol-aware-validation)
- 013. [Web Server and Reverse-Proxy Security](#web-server-and-reverse-proxy-security)
- 014. [Web Application Security](#web-application-security)
- 015. [Penetration Testing: Scope, Evidence, Reporting and Retest](#penetration-testing-scope-evidence-reporting-and-retest)
- 040. [Secure Coding and OWASP ASVS](#secure-coding-and-owasp-asvs)
- 052. [Web, Browser and HTTP Deep Dive](#web-browser-and-http-deep-dive)
- 069. [Advanced Web Request Processing and Parser Differentials](#advanced-web-request-processing-and-parser-differentials)
- 070. [Browser Isolation, Origins, CORS, CSP and Client-Side Trust](#browser-isolation-origins-cors-csp-and-client-side-trust)
- 071. [API Authorization, State Machines and Distributed Abuse Cases](#api-authorization-state-machines-and-distributed-abuse-cases)
- 089. [GraphQL, gRPC, WebSockets and Real-Time API Security](#graphql-grpc-websockets-and-real-time-api-security)
- 090. [Database, Data-Layer and Query-Engine Security](#database-data-layer-and-query-engine-security)
- 108. [Advanced Code Auditing, Static Analysis, Dataflow and Taint Reasoning](#advanced-code-auditing-static-analysis-dataflow-and-taint-reasoning)
- 124. [HTTP/2, HTTP/3, QUIC and Modern Web Transport Security](#http2-http3-quic-and-modern-web-transport-security)
- 126. [CDN, Reverse Proxy, Cache and Edge Security](#cdn-reverse-proxy-cache-and-edge-security)
- 127. [Serialization, Deserialization and Parser Security](#serialization-deserialization-and-parser-security)

### 03-Systems-Malware-and-Reverse-Engineering

- 006. [Host Security Assessment and System Hardening](#host-security-assessment-and-system-hardening)
- 007. [Malware Concepts, Analysis and Defensive Triage](#malware-concepts-analysis-and-defensive-triage)
- 011. [Session Security, Cookies, Tokens and Hijacking Prevention](#session-security-cookies-tokens-and-hijacking-prevention)
- 033. [Linux Security and Hardening](#linux-security-and-hardening)
- 053. [Memory Safety and Exploit Mitigations](#memory-safety-and-exploit-mitigations)
- 062. [CPU Privilege, Syscalls and Process Internals](#cpu-privilege-syscalls-and-process-internals)
- 063. [Assembly for Security Analysis — x86-64 and ARM64](#assembly-for-security-analysis-x86-64-and-arm64)
- 064. [Executable Formats, Loaders and Dynamic Linking](#executable-formats-loaders-and-dynamic-linking)
- 065. [Debugging, Crash Triage and Root-Cause Analysis](#debugging-crash-triage-and-root-cause-analysis)
- 066. [Memory Corruption Mechanics and Mitigation Analysis](#memory-corruption-mechanics-and-mitigation-analysis)
- 067. [Reverse Engineering and Program Analysis](#reverse-engineering-and-program-analysis)
- 068. [Fuzzing, Harness Design and Coverage-Guided Testing](#fuzzing-harness-design-and-coverage-guided-testing)
- 073. [Windows Internals — Tokens, Services, Registry, ETW and Security Boundaries](#windows-internals-tokens-services-registry-etw-and-security-boundaries)
- 074. [Linux Internals — Capabilities, Namespaces, Seccomp, LSM and eBPF Security](#linux-internals-capabilities-namespaces-seccomp-lsm-and-ebpf-security)
- 079. [Malware Analysis and Behavioral Triage](#malware-analysis-and-behavioral-triage)
- 084. [Patch Diffing, Vulnerability Root Cause and Secure Regression Analysis](#patch-diffing-vulnerability-root-cause-and-secure-regression-analysis)
- 095. [Kernel Security Primitives, Attack Surface and Runtime Trust](#kernel-security-primitives-attack-surface-and-runtime-trust)
- 096. [eBPF Observability, Linux Telemetry and Detection Engineering](#ebpf-observability-linux-telemetry-and-detection-engineering)
- 099. [Compiler Toolchains, Sanitizers, CFI and Binary Hardening](#compiler-toolchains-sanitizers-cfi-and-binary-hardening)
- 109. [Vulnerability Research: Reproduction, Regression and Coordinated Disclosure](#vulnerability-research-reproduction-regression-and-coordinated-disclosure)
- 111. [WebAssembly, JVM, CLR and Managed Runtime Security](#webassembly-jvm-clr-and-managed-runtime-security)
- 112. [Browser Extensions, Electron and Desktop Web Runtime Security](#browser-extensions-electron-and-desktop-web-runtime-security)
- 116. [Heap Allocators, Object Lifetimes and Memory Debugging](#heap-allocators-object-lifetimes-and-memory-debugging)
- 117. [Concurrency, Race Conditions, TOCTOU and Atomicity](#concurrency-race-conditions-toctou-and-atomicity)
- 118. [IPC, RPC, D-Bus, COM and Local Trust Boundaries](#ipc-rpc-d-bus-com-and-local-trust-boundaries)
- 119. [Sandboxing, Broker Architectures and Isolation Assurance](#sandboxing-broker-architectures-and-isolation-assurance)
- 120. [macOS Security Internals: TCC, SIP, Gatekeeper, Notarization and XProtect](#macos-security-internals-tcc-sip-gatekeeper-notarization-and-xprotect)

### 04-Network-Wireless-and-Internet

- 008. [Packet Capture, Sniffing and Network Visibility](#packet-capture-sniffing-and-network-visibility)
- 010. [Denial-of-Service Resilience and Resource-Exhaustion Testing](#denial-of-service-resilience-and-resource-exhaustion-testing)
- 012. [Firewalls, IDS/IPS, Honeypots and Detection Validation](#firewalls-idsips-honeypots-and-detection-validation)
- 016. [Wireless Network Security](#wireless-network-security)
- 035. [Email, DNS and Domain Security](#email-dns-and-domain-security)
- 051. [Networking Deep Dive](#networking-deep-dive)
- 077. [Network Protocol Reverse Engineering and Traffic Analysis](#network-protocol-reverse-engineering-and-traffic-analysis)
- 086. [IPv6 Security, Neighbor Discovery and Modern LAN Attack Surfaces](#ipv6-security-neighbor-discovery-and-modern-lan-attack-surfaces)
- 087. [DNS, Routing, BGP and Internet Infrastructure Security](#dns-routing-bgp-and-internet-infrastructure-security)
- 088. [Enterprise Wireless, WPA3, 802.1X and Wi-Fi 6/6E/7 Security](#enterprise-wireless-wpa3-8021x-and-wi-fi-66e7-security)
- 122. [Cellular Networks, LTE/5G Architecture and Mobile Network Security](#cellular-networks-lte5g-architecture-and-mobile-network-security)
- 123. [Radio, SDR and RF Security Fundamentals](#radio-sdr-and-rf-security-fundamentals)
- 125. [DNSSEC, DoH, DoQ, Resolver Privacy and DNS Trust](#dnssec-doh-doq-resolver-privacy-and-dns-trust)

### 05-Mobile-IoT-and-Hardware

- 017. [Mobile Security](#mobile-security)
- 018. [IoT and OT Security](#iot-and-ot-security)
- 054. [Hardware, Firmware and Boot Security](#hardware-firmware-and-boot-security)
- 055. [Bluetooth, NFC and Proximity Security](#bluetooth-nfc-and-proximity-security)
- 056. [Android Security Deep Dive](#android-security-deep-dive)
- 082. [Android Application Reverse Engineering and Mobile App Internals](#android-application-reverse-engineering-and-mobile-app-internals)
- 083. [Firmware, Embedded Systems and Hardware Interface Analysis](#firmware-embedded-systems-and-hardware-interface-analysis)
- 103. [TPM, Secure Boot, Attestation, TEEs and Device Identity](#tpm-secure-boot-attestation-tees-and-device-identity)
- 121. [iOS Security Internals: Entitlements, Code Signing, Keychain and Data Protection](#ios-security-internals-entitlements-code-signing-keychain-and-data-protection)

### 06-Identity-Cryptography-and-Trust

- 020. [Cryptography](#cryptography)
- 021. [Identity, Zero Trust, and Access Security](#identity-zero-trust-and-access-security)
- 032. [Windows and Active Directory Security](#windows-and-active-directory-security)
- 039. [OAuth, OIDC, Passkeys and Modern Authentication](#oauth-oidc-passkeys-and-modern-authentication)
- 049. [Secrets, PKI and Key Management](#secrets-pki-and-key-management)
- 072. [Kerberos, Active Directory and Enterprise Identity Internals](#kerberos-active-directory-and-enterprise-identity-internals)
- 078. [TLS, PKI and Cryptographic Implementation Failures](#tls-pki-and-cryptographic-implementation-failures)
- 092. [OAuth 2.0 Security BCP, OIDC Federation and Token Defense](#oauth-20-security-bcp-oidc-federation-and-token-defense)
- 093. [Authorization Models: RBAC, ABAC, ReBAC and Policy Engines](#authorization-models-rbac-abac-rebac-and-policy-engines)
- 100. [Cryptographic Protocol Engineering, Key Agreement and State Machines](#cryptographic-protocol-engineering-key-agreement-and-state-machines)
- 101. [Post-Quantum Migration, Crypto Agility and Hybrid Deployment](#post-quantum-migration-crypto-agility-and-hybrid-deployment)
- 102. [Side Channels, Timing, Cache, Faults and Physical Leakage Models](#side-channels-timing-cache-faults-and-physical-leakage-models)
- 113. [Workload Identity, SPIFFE/SPIRE, mTLS and Zero-Trust Service Identity](#workload-identity-spiffespire-mtls-and-zero-trust-service-identity)
- 128. [SAML, WS-Federation and Enterprise SSO Internals](#saml-ws-federation-and-enterprise-sso-internals)
- 129. [SCIM, Identity Lifecycle and Provisioning Security](#scim-identity-lifecycle-and-provisioning-security)
- 130. [PAM, Just-in-Time Access, JEA and Privileged Access Engineering](#pam-just-in-time-access-jea-and-privileged-access-engineering)
- 131. [WebAuthn, FIDO2 and Passkey Internals](#webauthn-fido2-and-passkey-internals)
- 132. [Secrets Rotation, Envelope Encryption, KMS and HSM Architecture](#secrets-rotation-envelope-encryption-kms-and-hsm-architecture)

### 07-Cloud-Containers-and-Supply-Chain

- 019. [Cloud Security](#cloud-security)
- 022. [Secure Software, APIs, and Supply Chain](#secure-software-apis-and-supply-chain)
- 024. [Containers, Kubernetes, and DevSecOps](#containers-kubernetes-and-devsecops)
- 075. [Container and Kubernetes Isolation Internals](#container-and-kubernetes-isolation-internals)
- 076. [Cloud IAM, Control Planes, Metadata and Temporary Credentials](#cloud-iam-control-planes-metadata-and-temporary-credentials)
- 091. [Message Queues, Event Streaming and Distributed-System Security](#message-queues-event-streaming-and-distributed-system-security)
- 094. [Virtualization, Hypervisors, Virtual Machines and Confidential Computing](#virtualization-hypervisors-virtual-machines-and-confidential-computing)
- 097. [CI/CD, Build Provenance, SLSA 1.2 and Artifact Trust](#cicd-build-provenance-slsa-12-and-artifact-trust)
- 098. [Package Managers, Registries, Dependency and Ecosystem Security](#package-managers-registries-dependency-and-ecosystem-security)
- 104. [Serverless, Edge Workers, Functions and Event-Driven Cloud Security](#serverless-edge-workers-functions-and-event-driven-cloud-security)
- 105. [Multi-Cloud, SaaS Federation, Tenant Isolation and Control Planes](#multi-cloud-saas-federation-tenant-isolation-and-control-planes)
- 133. [Git Security, Signed Commits, Branch Protection and Repository Trust](#git-security-signed-commits-branch-protection-and-repository-trust)
- 134. [SBOM, VEX, Provenance and Vulnerability Intelligence Pipelines](#sbom-vex-provenance-and-vulnerability-intelligence-pipelines)
- 135. [Kubernetes Admission Control, Policy-as-Code and Runtime Guardrails](#kubernetes-admission-control-policy-as-code-and-runtime-guardrails)
- 136. [Service Mesh, mTLS, Network Policy and East-West Security](#service-mesh-mtls-network-policy-and-east-west-security)

### 08-Blue-Team-IR-Forensics-and-Resilience

- 023. [Detection Engineering, Incident Response, and Threat Hunting](#detection-engineering-incident-response-and-threat-hunting)
- 034. [Threat Intelligence and OSINT](#threat-intelligence-and-osint)
- 037. [Digital Forensics and Evidence Handling](#digital-forensics-and-evidence-handling)
- 038. [Ransomware Resilience and Recovery](#ransomware-resilience-and-recovery)
- 044. [Endpoint, Browser and SaaS Security](#endpoint-browser-and-saas-security)
- 047. [SOC, SIEM, SOAR and Detection Operations](#soc-siem-soar-and-detection-operations)
- 048. [Business Continuity, Disaster Recovery and Backup Engineering](#business-continuity-disaster-recovery-and-backup-engineering)
- 080. [Advanced Detection Engineering and MITRE ATT&CK v19](#advanced-detection-engineering-and-mitre-attck-v19)
- 081. [Digital Forensics — Filesystem Timelines and Memory Artifacts](#digital-forensics-filesystem-timelines-and-memory-artifacts)
- 106. [Endpoint EDR Internals, Telemetry and Response Architecture](#endpoint-edr-internals-telemetry-and-response-architecture)
- 107. [Threat Emulation, Adversary Simulation and Purple-Team Lab Design](#threat-emulation-adversary-simulation-and-purple-team-lab-design)
- 137. [Cloud Logging, Detection and Cross-Cloud Investigation](#cloud-logging-detection-and-cross-cloud-investigation)

### 09-AI-GRC-Privacy-Data-and-Human-Security

- 009. [Social Engineering Defense and Human-Factor Security](#social-engineering-defense-and-human-factor-security)
- 025. [AI and LLM Security](#ai-and-llm-security)
- 042. [Governance, Risk, Compliance and Privacy](#governance-risk-compliance-and-privacy)
- 046. [Agentic AI, MCP and Tool Security](#agentic-ai-mcp-and-tool-security)
- 057. [Privacy, Data Protection and Operational Hygiene](#privacy-data-protection-and-operational-hygiene)
- 059. [Security Metrics and Program Measurement](#security-metrics-and-program-measurement)
- 060. [Physical Security and Human Resilience](#physical-security-and-human-resilience)
- 114. [Data Security, DLP, Tokenization, Privacy Engineering and Data Lifecycle](#data-security-dlp-tokenization-privacy-engineering-and-data-lifecycle)
- 138. [RAG, Vector Databases and AI Retrieval Security](#rag-vector-databases-and-ai-retrieval-security)
- 139. [AI-Generated Code, Vibe Coding and Secure Review](#ai-generated-code-vibe-coding-and-secure-review)

### 10-Termux-and-Security-Automation

- 028. [Termux Foundations and Android Linux](#termux-foundations-and-android-linux)
- 029. [Termux Workflow, Python, Git and Automation](#termux-workflow-python-git-and-automation)
- 030. [Termux Networking, SSH and Local Services](#termux-networking-ssh-and-local-services)
- 031. [Termux Security Lab Operations and Troubleshooting](#termux-security-lab-operations-and-troubleshooting)
- 036. [Python for Security Automation](#python-for-security-automation)

### 11-Labs-Capstones-and-Career

- 027. [Authorized Hands-On Labs](#authorized-hands-on-labs)
- 045. [Capstones, Checklists and Study Roadmaps](#capstones-checklists-and-study-roadmaps)
- 058. [Cybersecurity Career and Portfolio Guidance](#cybersecurity-career-and-portfolio-guidance)
- 085. [Advanced Authorized Capstones](#advanced-authorized-capstones)
- 110. [Advanced Authorized Labs II: Systems, Identity, Cloud and Application Security](#advanced-authorized-labs-ii-systems-identity-cloud-and-application-security)
- 115. [Master Capstones, Research Portfolio and Deep Security Practice](#master-capstones-research-portfolio-and-deep-security-practice)
- 140. [Advanced Authorized Labs III: Modern Protocols, Identity, Platforms and AI Security](#advanced-authorized-labs-iii-modern-protocols-identity-platforms-and-ai-security)

---

# Cybersecurity Foundations and Ethical Hacking Methodology

Cybersecurity is the discipline of protecting systems, identities, software, networks, and data while preserving the ability of legitimate users to work. Ethical hacking is one part of that discipline: an authorized attempt to test security assumptions and produce evidence that helps an owner reduce risk.

> **Authorized-use boundary:** Perform practical testing only on systems, accounts, applications, networks, or devices you own or are explicitly authorized to assess. When learning, prefer localhost, disposable virtual machines, containers, emulators, synthetic accounts, and intentionally vulnerable training applications.

## Learning objectives

By the end of this module you should be able to:

- distinguish assets, threats, vulnerabilities, exposures, controls, and risk;
- explain confidentiality, integrity, availability, authenticity, accountability, and resilience;
- distinguish authentication from authorization;
- describe a modern security-assessment lifecycle;
- define scope and evidence requirements before testing;
- explain why remediation and retesting are part of ethical hacking.

## Security properties

### Confidentiality

Confidentiality limits information to authorized subjects. Encryption can protect confidentiality in transit or at rest, but confidentiality also depends on authorization, secret handling, logging practices, backups, screenshots, exports, and operational procedures.

### Integrity

Integrity means data and system state remain correct and unauthorized modification is prevented or detectable. Hashes, digital signatures, access control, transaction validation, version control, immutable logging, and change-management processes can all contribute to integrity.

### Availability

Availability means an authorized user can obtain a required service or resource when needed. Capacity, redundancy, backups, dependency management, rate limits, monitoring, recovery procedures, and protection against resource exhaustion all affect availability.

### Authenticity and accountability

Authenticity concerns whether an identity, artifact, or message is what it claims to be. Accountability concerns whether actions can be associated with the correct actor and investigated later. Strong authentication is useful only when authorization decisions and audit evidence are also correct.

### Resilience

A secure system should not depend on the assumption that prevention always succeeds. Resilience includes detection, containment, recovery, restoration, lessons learned, and the ability to operate safely during partial failure.

## Core security vocabulary

- **Asset:** something that has value and requires protection.
- **Threat:** a circumstance or actor capable of causing harm.
- **Vulnerability:** a weakness that can violate a security property.
- **Exposure:** a condition that makes a weakness reachable or relevant.
- **Exploit:** a method that takes advantage of a vulnerability. In this guide, exploit research is limited to controlled labs and defensive understanding.
- **Control:** a safeguard that prevents, detects, limits, or helps recover from an unwanted event.
- **Risk:** the combination of likelihood, impact, exposure, business context, and uncertainty.
- **Attack surface:** the set of reachable interfaces, identities, inputs, services, dependencies, and trust boundaries that could be abused.
- **Trust boundary:** a point where data, identity, authority, or execution crosses between components with different trust assumptions.

## Authentication and authorization

Authentication answers, “Who or what is presenting this credential?” Authorization answers, “May this identity perform this action on this resource in this context?” A system can authenticate a user correctly and still be vulnerable if authorization checks are missing, performed on the wrong object, or based on stale state.

## Threat actors and motivations

Security analysis should focus on capabilities and goals rather than stereotypes. Relevant actors can include financially motivated criminals, insiders, state-linked groups, opportunistic attackers, hacktivists, fraud groups, competitors, and automated abuse. Defenders should ask what access the actor begins with, what they are trying to achieve, what constraints they face, and what evidence their activity would leave.

## Vulnerability management basics

CVE identifiers provide common names for publicly disclosed vulnerabilities. NVD and vendor advisories enrich vulnerability information. CVSS provides a standardized severity framework, but a score is not a complete risk decision: exploitability, exposure, asset importance, compensating controls, and business impact still matter.

A useful vulnerability workflow is:

1. identify the affected asset and exact version;
2. verify whether the issue is applicable;
3. determine exposure and required privileges;
4. collect evidence without causing unnecessary impact;
5. prioritize using technical and business context;
6. remediate or mitigate;
7. retest and record the result.

## A modern ethical-assessment lifecycle

### 1. Authorization and scope

Write down the owner, systems, accounts, time window, allowed techniques, prohibited actions, data-handling rules, contacts, and stop conditions. “It is public on the Internet” is not authorization.

### 2. Discovery and modeling

Build an inventory of assets, identities, interfaces, dependencies, and trust boundaries. Start with passive or read-only evidence where possible.

### 3. Validation

Test security assumptions using the least invasive method that answers the question. Prefer a proof that demonstrates the weakness over a technique that maximizes access or impact.

### 4. Evidence and analysis

Record timestamps, versions, configuration, requests/responses, logs, screenshots only when necessary, and the exact condition that made the result possible. Separate observation from inference.

### 5. Remediation and retest

Explain the root cause, recommended control, expected residual risk, and a repeatable regression test. A finding is not complete until the owner can verify that the control changed the result.

### 6. Cleanup and reporting

Remove test accounts, temporary files, lab data, or configuration changes that were created as part of the authorized assessment. Preserve legitimate audit evidence; do **not** delete or tamper with security logs to conceal activity.

## Defensive thinking

A useful habit is to analyze every system with five questions:

1. What asset or security property matters?
2. Which identity or process has authority?
3. Where does untrusted input enter?
4. What state can become stale, confused, or inconsistent?
5. What evidence would prove the control is working?

## Safe lab

Create a one-page threat model for a local application or device you own. Draw the user, application, data store, network boundary, and one external dependency. Mark where authentication occurs, where authorization occurs, what data is sensitive, and what logs would be useful during an incident.

**Evidence to keep:** the diagram, three security assumptions, three possible failure modes, and one defensive test for each failure mode.

## Common mistakes

- Starting with tools before defining a security question.
- Treating a scanner finding as proof without verification.
- Confusing severity with business risk.
- Confusing encryption with authorization.
- Testing outside the written scope because a target is technically reachable.
- Keeping secrets, tokens, or unnecessary personal data in lab notes.
- Treating cleanup as permission to erase evidence.

## Knowledge check

1. Give an example of authentication succeeding while authorization fails.
2. Explain the difference between a vulnerability and risk.
3. Name three items that belong in assessment scope.
4. Why is retesting part of an ethical assessment?
5. What evidence would you collect before changing a security control?

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md). For this module, finish the safe lab and be able to explain the assessment lifecycle without referring to tool names.

### Continue with

Recommended next modules: **02, 05, 28, 51**.

---

# Footprinting, Reconnaissance and Attack-Surface Discovery

Reconnaissance is the process of building an accurate picture of an authorized target before deeper testing. Good reconnaissance is evidence-driven: it distinguishes information that is publicly observable from information obtained through direct interaction, and it records the source and confidence of each claim.

> **Authorized-use boundary:** Passive research can still involve privacy, contractual, or policy constraints. Active discovery must remain inside the written assessment scope. Use `example.com`, localhost, or a lab domain for exercises in this module.

## Learning objectives

- distinguish passive, active, authenticated, and internal discovery;
- build an asset inventory from multiple evidence sources;
- understand DNS, certificate, registration, and web metadata;
- identify cloud, SaaS, repository, and identity exposure safely;
- track provenance and confidence for reconnaissance findings;
- turn reconnaissance into a prioritized attack-surface map.

## Reconnaissance is an inventory problem

The goal is not to collect the largest number of names. The goal is to answer useful questions: Which assets belong to the organization? Which are Internet-facing? Which identities administer them? Which technologies and third-party dependencies are present? Which assets appear abandoned or inconsistently managed? Which observations are confirmed and which are only hypotheses?

## Passive discovery

Passive sources do not require sending probes to the target service. Examples include:

- public DNS and certificate-transparency data;
- registration and autonomous-system information;
- public code repositories and package registries;
- organization websites, documentation, job postings, and status pages;
- vendor security advisories and public asset documentation;
- public cloud/SaaS references deliberately published by the owner.

Passive does not mean unrestricted. Avoid collecting unnecessary personal data and do not attempt to access private accounts or content.

## DNS fundamentals for reconnaissance

Useful record types include:

- **A / AAAA:** IPv4 and IPv6 addresses;
- **CNAME:** alias to another hostname;
- **MX:** mail exchangers;
- **NS:** authoritative name servers;
- **TXT:** text records used by mechanisms such as SPF, DKIM, domain verification, and other services;
- **CAA:** certificate-authority authorization policy.

Safe local or documentation-oriented examples:

```bash
nslookup example.com
dig example.com A
dig example.com AAAA
dig example.com MX
```

A DNS answer is evidence about DNS state, not proof that a specific application, owner, or security control is present. Record resolver, timestamp, TTL, and whether the answer may be split-horizon or cached.

## Certificate and TLS metadata

Certificates can reveal hostnames, issuing authorities, validity periods, and organizational deployment patterns. Certificate Transparency can help find publicly issued names, but a certificate entry does not prove that the hostname is currently reachable or still owned by the same team.

## Web metadata

For an authorized web property, useful read-only observations include:

- response status and redirect chain;
- TLS configuration and certificate metadata;
- security headers;
- server or framework hints that are intentionally exposed;
- `robots.txt`, `security.txt`, and public sitemaps;
- documented API endpoints and public OpenAPI descriptions;
- public JavaScript bundle names and source-map exposure.

Do not turn a reconnaissance exercise into uncontrolled content brute forcing. If directory enumeration is in scope, perform it against a deliberately vulnerable or locally hosted training application with an agreed request rate.

## Repository and package exposure

Public repositories can reveal architecture, dependencies, historical filenames, issue discussions, CI configuration, and accidentally committed secrets. Never assume a string that looks like a credential is safe to test. Report suspected secrets through the agreed channel and allow the owner to rotate them.

For dependency research, distinguish:

- direct dependency versus transitive dependency;
- declared version versus actually deployed version;
- package name similarity versus verified package identity;
- public vulnerability match versus reachable vulnerable code path.

## Cloud and SaaS attack surface

Organizations may expose cloud load balancers, object-storage endpoints, identity-provider domains, SaaS tenants, support portals, and development platforms. A hostname pattern is not sufficient evidence of ownership. Confirm through approved inventories, DNS relationships, certificate data, or customer-provided context.

## Provenance and confidence

For every discovered asset, record:

| Field | Example |
|---|---|
| Asset | `portal.lab.example` |
| Source | DNS / certificate / owner inventory |
| First seen | timestamp |
| Confidence | confirmed / probable / unconfirmed |
| Environment | production / staging / unknown |
| Owner | team or system owner if known |
| Exposure | public / internal / unknown |
| Next validation | minimal authorized test |

This prevents a common failure: treating stale search-engine or certificate data as current truth.

## Active reconnaissance in a lab

Active reconnaissance directly interacts with a system. Examples include resolving a hostname, making a normal HTTP request, checking a small approved port list, or retrieving a service banner. Keep the rate bounded and document exactly what was sent.

A safe local exercise can use Python's HTTP server:

```bash
mkdir -p ~/hgp-lab/recon && cd ~/hgp-lab/recon
printf 'lab page\n' > index.html
python -m http.server 8000 --bind 127.0.0.1
```

In another Termux session:

```bash
curl -I http://127.0.0.1:8000/
```

Stop the server when finished.

## Turning findings into an attack-surface map

Group assets by trust boundary rather than only by hostname. Useful groups include Internet edge, identity, email, source control, CI/CD, cloud control plane, APIs, remote access, mobile backends, third-party integrations, and monitoring/recovery systems.

Prioritize assets that combine high authority, sensitive data, broad exposure, weak ownership, or weak observability.

## Common mistakes

- Copying old command examples against public domains.
- Equating a discovered hostname with an in-scope asset.
- Treating a technology fingerprint as a confirmed vulnerable version.
- Collecting personal data that is irrelevant to the security objective.
- Ignoring IPv6, alternate domains, or third-party identity surfaces.
- Failing to timestamp findings that can change quickly.

## Safe lab

Build an attack-surface worksheet for a fictional organization with five assets: website, API, identity provider, code repository, and cloud account. For each, record trust boundary, owner, evidence source, likely sensitive data, and one minimal validation step.

## Knowledge check

1. Why is provenance important in OSINT?
2. What is the difference between passive and active reconnaissance?
3. Why can certificate data become stale?
4. What would make a repository finding high priority?
5. How do you avoid treating search results as proof of ownership?

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md). Complete the attack-surface worksheet before moving to active scanning.

### Continue with

Recommended next modules: **03, 34, 35, 43**.

---

# Network Scanning and Service Discovery

Network scanning answers bounded questions about hosts, ports, protocols, and exposed services. In an ethical assessment, scanning is not a stealth exercise: scope, rate, expected traffic, monitoring coordination, and evidence quality matter more than concealment.

> **Authorized-use boundary:** Scan only addresses and services explicitly included in your scope. For learning, use localhost, a host-only VM network, containers, or an isolated lab such as `192.168.56.0/24` that you control.

## Learning objectives

- explain TCP/UDP discovery and the limits of scan results;
- understand open, closed, and filtered observations;
- use Nmap safely in a small lab;
- identify service versions without over-trusting banners;
- understand why IPv4/IPv6 and firewall policy must be reviewed together;
- correlate scanner output with packet and server-side evidence.

## Start with a question

A scan should answer a defined question such as “Which approved lab hosts expose TCP/22 and TCP/443?” or “Did the firewall change remove access from this test segment?” Avoid broad scans when a narrower test will answer the same question.

## TCP state

TCP uses a stateful connection model. A typical connection begins with SYN, SYN/ACK, and ACK. A listening service may respond differently from a closed port, while a firewall or host policy may drop, reject, rate-limit, proxy, or otherwise alter traffic.

The terms **open**, **closed**, and **filtered** describe an observation from the scanner's position. They are not permanent properties of the target. Routing, source address, protocol family, network policy, load balancing, and time can change the result.

## UDP state

UDP has no connection handshake. A silent UDP probe can mean many things: open service, filtered traffic, application-specific behavior, or packet loss. Strong conclusions usually require protocol-aware requests or server-side evidence.

## Host discovery

ICMP echo is only one discovery signal. Hosts may block echo but still expose TCP or UDP services. Conversely, a gateway or load balancer may answer in ways that do not prove the application behind it is healthy.

In a lab, compare:

```bash
ping -c 2 192.168.56.10
nmap -sn 192.168.56.0/24
```

Use a small host-only subnet you control, not an arbitrary Internet range.

## Nmap basics

Nmap supports many scan types. Begin with the least complex option that answers the question.

```bash
nmap -sT -p 22,80,443 192.168.56.10
```

A TCP connect scan uses the operating system's normal connection mechanism and is appropriate for many labs without raw-packet privileges.

Version detection can be useful when explicitly authorized:

```bash
nmap -sT -sV -p 22,80,443 192.168.56.10
```

Treat version output as a hypothesis. Reverse proxies, custom banners, backported patches, or service wrappers can make banner-based conclusions wrong.

## Scan rate and reliability

Faster is not always better. Excessive concurrency can cause packet loss, trigger rate limits, overload fragile lab services, or create misleading results. Record timing options and retry conditions when results matter.

## Firewalls and detection validation

Do not use scanning options to “get around” monitoring. If the assessment includes control validation, coordinate with the defensive team and ask whether the expected traffic was logged, correlated, and alerted on. A useful test produces evidence on both sides:

- scanner timestamp and source;
- target/service response;
- firewall or security-group decision;
- host log or application log;
- SIEM/EDR/network-detection evidence where applicable.

## IPv6 parity

A service may be reachable through IPv6 even when IPv4 is restricted. Check listening sockets, DNS AAAA records, host firewall rules, cloud security policies, and monitoring coverage for both protocol families. Module 86 covers IPv6 in greater depth.

## Service discovery and validation

After identifying a listening port, ask:

1. What protocol is expected?
2. Does the service require TLS?
3. What identity or authorization boundary protects it?
4. Is the service intended to be reachable from this network segment?
5. What evidence confirms the actual application and version?

Avoid assuming “port 443 = secure web server” or “port 22 = OpenSSH.” Ports are conventions, not identities.

## Network diagrams

A useful scan report includes a simple diagram showing the scanner, routing boundary, firewall/security group, target, and relevant monitoring point. This makes it easier to distinguish target behavior from network filtering.

## Common mistakes

- Scanning outside the approved CIDR range.
- Using broad port ranges when a small approved list is sufficient.
- Treating lack of ICMP echo as proof a host is offline.
- Treating scanner version detection as definitive.
- Ignoring IPv6.
- Trying to bypass monitoring rather than validating its coverage.
- Failing to correlate scan timestamps with defensive telemetry.

## Safe lab

Create two local services on a VM or container you own, one on a known open port and one deliberately stopped. Scan only those ports, predict the expected state, capture the result, then change one firewall or service setting and repeat. Explain why the observation changed.

## Knowledge check

1. Why is UDP scanning inherently ambiguous?
2. What does “filtered” describe?
3. Why can a service banner be misleading?
4. What evidence should accompany a firewall-validation scan?
5. Why must IPv6 be considered separately?

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md). The mastery goal is to explain a scan result from TCP/UDP behavior and network policy, not from memorized Nmap switches.

### Continue with

Recommended next modules: **04, 05, 12, 51**.

---

# Service Enumeration and Protocol-Aware Validation

Enumeration turns a basic “service exists” observation into a structured understanding of protocol behavior, identities, configuration, and exposed metadata. The objective is not to extract everything possible; it is to collect the minimum evidence needed to evaluate an authorized security question.

> **Authorized-use boundary:** Enumerate only services and accounts included in scope. Use lab accounts, synthetic data, and read-only requests where possible. Do not attempt password guessing, user harvesting, or sensitive-data extraction unless a controlled test explicitly authorizes it.

## Learning objectives

- distinguish scanning from enumeration;
- understand protocol-aware evidence collection;
- enumerate HTTP, SSH, DNS, SMB, SNMP, and directory services safely;
- recognize authentication and authorization boundaries;
- avoid false conclusions caused by banners, anonymous access, or stale metadata;
- document evidence in a reproducible way.

## Scanning versus enumeration

Scanning normally asks whether a host or service is reachable. Enumeration asks what the service exposes and how it behaves. For example, a scan might show TCP/443 open; enumeration might establish that a reverse proxy presents a specific certificate, routes to an application, requires an identity provider, and exposes certain security headers.

## HTTP and HTTPS

Start with normal application behavior:

```bash
curl -I http://127.0.0.1:8000/
```

Record response status, redirect behavior, headers, and whether the service is supposed to be available from your location. For TLS, also record certificate subject/issuer and hostname validation. Do not infer the backend technology solely from a `Server` header.

## SSH

SSH enumeration should focus on configuration and trust boundaries, not credential attacks. Useful questions include:

- Is SSH supposed to be reachable from this segment?
- Which protocol and host-key algorithms are enabled?
- Is password authentication allowed or are keys required?
- Are privileged accounts allowed to log in directly?
- Are access decisions logged centrally?

If you administer the lab host, validate configuration from the server as well as from the network.

## DNS

DNS enumeration can reveal address records, mail routing, name-server relationships, and security records. Zone transfers should be tested only against your own authoritative lab server or when explicitly authorized; an unrestricted transfer on a production domain may expose an internal naming inventory.

## SMB and file-sharing services

For a Windows/Samba lab, validate shares using an account created for the assessment. Check whether guest/anonymous access exists, which permissions are granted, and whether write access is appropriate. The security question is authorization: can this identity perform an action it should not be able to perform?

Never treat a readable share as automatically vulnerable; it may be intentionally public. Record the expected access policy.

## SNMP

SNMP can expose operational and inventory data. Modern environments should prefer authenticated and encrypted configurations where supported. During an assessment, do not brute-force community strings. Use credentials supplied for the lab or inspect configuration on a device you administer.

## LDAP and directory services

Directory enumeration must distinguish public directory metadata from authenticated data. Record bind type, identity, search base, returned attributes, and whether sensitive attributes are unnecessarily exposed. For Active Directory depth, continue with Modules 32 and 72.

## Service fingerprints are hypotheses

Banners, response headers, protocol negotiation, and error messages can suggest a product or version, but backported fixes and intermediary devices complicate interpretation. Confirm high-impact version claims with asset inventory, package information, authenticated management data, or owner-provided evidence.

## Authorization matrix

A simple way to test access control is to build a matrix:

| Identity | Resource | Read | Write | Admin | Expected? |
|---|---|---:|---:|---:|---|
| anonymous | public share | yes | no | no | yes |
| test-user | team share | yes | no | no | yes |
| test-admin | team share | yes | yes | yes | yes |

Test only the rows required to prove the policy. Avoid collecting unrelated data.

## Common mistakes

- Treating anonymous access as a vulnerability without checking policy.
- Guessing credentials instead of using approved test accounts.
- Trusting banners as authoritative version evidence.
- Enumerating more data than the objective requires.
- Forgetting to record the identity used for each result.
- Ignoring service-side logs and authorization decisions.

## Safe lab

On a VM or container you own, expose one HTTP service and one authenticated service. Create two test identities with different permissions. Build an authorization matrix, make only the requests required to validate it, and record server-side evidence for allowed and denied actions.

## Knowledge check

1. What distinguishes enumeration from scanning?
2. Why must an enumeration result record the identity used?
3. Why is banner-based versioning insufficient for high-confidence findings?
4. How does an authorization matrix reduce unnecessary testing?
5. What makes an SNMP or SMB observation a security finding rather than merely information?

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md). Focus on evidence, identity context, and expected policy rather than tool output volume.

### Continue with

Recommended next modules: **05, 13, 32, 33**.

---

# Vulnerability Analysis and Prioritization

Vulnerability analysis determines whether a weakness applies to a real asset, how it can affect a security property, and what should be done about it. A scanner or CVE match is the beginning of analysis, not the conclusion.

> **Authorized-use boundary:** Validate vulnerabilities using the least invasive method that answers the question. Use vendor information, package/version evidence, configuration review, safe requests, and lab reproduction before considering any intrusive proof.

## Learning objectives

- distinguish vulnerability, exposure, exploitability, severity, and risk;
- understand CVE, CWE, CVSS, vendor advisories, and vulnerability databases;
- validate applicability and avoid version-only false positives;
- prioritize findings using asset and business context;
- write remediation and retest criteria;
- manage uncertainty explicitly.

## Sources of vulnerability information

### CVE

CVE provides identifiers for publicly disclosed vulnerabilities. A CVE record is a common reference, not a complete technical analysis.

### CWE

CWE describes classes of software and hardware weaknesses such as improper input validation, authorization errors, or memory-safety defects. CWE is useful for root-cause analysis because many CVEs share the same weakness pattern.

### Vendor advisories

Vendor or upstream project advisories are often the best source for affected versions, patches, workarounds, prerequisites, and product-specific details.

### NVD and other enrichment

Enrichment services can provide scoring, references, and metadata. Always verify high-impact claims against primary vendor or upstream sources when possible.

## CVSS and context

CVSS expresses standardized technical severity. It does not know whether your vulnerable service is Internet-facing, whether the affected feature is disabled, whether compensating controls exist, whether the asset contains sensitive data, or whether exploitation would disrupt a critical process.

A practical priority decision combines:

- technical severity;
- confirmed applicability;
- exposure and reachability;
- required privileges and user interaction;
- exploit maturity where relevant;
- asset criticality and data sensitivity;
- compensating controls;
- detection and recovery capability;
- patch complexity and operational risk.

## Applicability analysis

Before reporting a vulnerability, answer:

1. Is the affected product actually installed?
2. Is the exact component/version affected?
3. Is the vulnerable feature enabled and reachable?
4. Is required authentication or privilege available to the threat model?
5. Has the vendor backported a fix without changing the visible version?
6. Does a reverse proxy, WAF, sandbox, or other control materially change exploitability?

Do not assume a product string is enough.

## Safe validation ladder

Use the least invasive level that produces sufficient confidence:

1. **Inventory evidence:** package, SBOM, image digest, or asset record.
2. **Configuration evidence:** affected feature enabled/disabled.
3. **Normal protocol evidence:** benign request confirms behavior.
4. **Local reproduction:** intentionally vulnerable sample in an isolated lab.
5. **Intrusive validation:** only when explicitly approved and necessary.

Stop as soon as the security question is answered.

## Writing a useful finding

A strong finding contains:

- affected asset and component;
- evidence and timestamp;
- root cause or vulnerability reference;
- realistic impact in this environment;
- prerequisites and limitations;
- severity/risk rationale;
- remediation or mitigation;
- retest procedure.

Avoid dramatic language. Describe what you proved and what remains uncertain.

## Remediation patterns

Possible responses include patching, upgrading, disabling an unused feature, reducing exposure, strengthening authorization, isolating the service, rotating affected credentials, adding detection, or accepting documented residual risk.

A workaround is not automatically equivalent to a patch. Record what risk remains.

## Common mistakes

- Reporting every scanner match as a confirmed vulnerability.
- Using CVSS as the only prioritization input.
- Failing to identify the exact affected component.
- Running a proof of concept when inventory/configuration evidence is sufficient.
- Ignoring compensating controls or environmental prerequisites.
- Writing remediation without a regression test.

## Safe lab

Create a fictional asset record for three systems: an Internet-facing web service, an internal workstation, and an isolated development container. Give each one the same hypothetical high-severity library vulnerability. Write three different priority decisions based on exposure, data, privilege, and recovery context.

## Knowledge check

1. Why is a CVE match not automatically a finding?
2. What does CWE add to vulnerability analysis?
3. What information does CVSS not know about your environment?
4. When should intrusive validation be avoided?
5. What makes a retest criterion reproducible?

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md). Practice explaining why two assets with the same CVE can have different operational priority.

### Continue with

Recommended next modules: **15, 26, 50, 84**.

---

# Host Security Assessment and System Hardening

Host security assessment examines how an operating system protects identities, privileges, processes, services, files, secrets, persistence mechanisms, and telemetry. The goal is to find weak trust boundaries and harden them—not to hide activity or disable evidence.

> **Authorized-use boundary:** Perform host testing only on systems you administer or are explicitly authorized to assess. Do not deploy persistence, credential stealers, keyloggers, hidden backdoors, or anti-forensics techniques. Use harmless test accounts and disposable VMs for exercises.

## Learning objectives

- assess local accounts, authentication, and privilege boundaries;
- reason about least privilege and privilege escalation risk;
- review services, scheduled tasks, startup mechanisms, and software inventory;
- protect secrets and credentials;
- understand persistence as a defensive detection category;
- preserve and centralize logs so tampering is detectable;
- design a repeatable hardening baseline.

## Identity and local accounts

Start with an inventory of human users, service accounts, groups, administrative roles, and authentication methods. Ask whether every identity has a current owner and a valid business purpose.

High-value checks include:

- unused or stale accounts;
- shared administrator credentials;
- direct root/administrator use instead of delegated elevation;
- weak password or MFA policy where applicable;
- service accounts with interactive login unnecessarily enabled;
- accounts whose privileges no longer match their role.

Authentication proves identity; group membership, sudoers policy, access tokens, ACLs, capabilities, and service configuration determine authorization.

## Privilege boundaries

Privilege escalation risk appears when a less-trusted identity can influence something executed by a more-trusted identity. Common classes include:

- writable service binaries or startup scripts;
- unsafe search paths or environment variables;
- over-permissive scheduled jobs;
- dangerous delegated administration rights;
- weak file or registry ACLs;
- unnecessary Linux capabilities or set-user-ID programs;
- services running with more authority than required.

In an assessment, prefer permission and configuration review over exploitation. If a proof is needed, use a harmless marker file or synthetic action in a disposable lab.

## Services and exposed software

Inventory listening services and installed software. For each service, record owner, purpose, network exposure, execution identity, configuration location, update source, and relevant logs. Disable or remove services that have no operational purpose rather than merely blocking them at one network layer.

## Secrets and credential material

Credentials can exist in configuration files, environment variables, shell history, browser storage, CI files, source repositories, password managers, OS credential stores, and process memory. Security review should minimize secret lifetime and access, not attempt to dump real credentials.

Use synthetic secrets for labs. If a real secret is accidentally exposed during an authorized assessment, stop unnecessary handling, notify the owner, and rotate/revoke it according to the incident process.

## Persistence as a defensive concept

Attackers may attempt to survive restarts or credential changes through services, scheduled tasks, startup items, browser extensions, login hooks, management tools, or modified configuration. Defenders should establish a known-good baseline and monitor unexpected changes.

A safe lab can create a clearly named benign scheduled task that writes a timestamp to a temporary file, verify the expected telemetry, then remove it. The learning objective is to understand how legitimate persistence appears in logs—not to create stealthy persistence.

## Logging and anti-forensics detection

Security logs are evidence. Do not clear, truncate, falsify, or disable them to conceal testing. Instead:

- forward important logs to a separate system when possible;
- restrict who can change audit configuration;
- alert on audit-service changes, log truncation, deletion, or retention-policy changes;
- synchronize time;
- protect log integrity and retention;
- document planned maintenance that legitimately affects telemetry.

During a lab, you can safely test detection by creating a benign event and confirming it appears in the expected local and centralized logs.

## File and permission review

On Linux, inspect ownership and mode bits; on Windows, inspect ACLs and inherited permissions. Focus on security-relevant paths such as service configuration, executable directories, scheduled-task definitions, sensitive data, key material, and administrative tooling.

Avoid “fixing” permission problems by applying broad recursive write access. Correct the specific owner/group/ACL that should have authority.

## Patch and configuration baselines

A host baseline should include:

- supported OS version and patch state;
- disk encryption where appropriate;
- host firewall policy;
- endpoint protection and logging;
- secure boot/platform protections where supported;
- account and privilege policy;
- exposed services;
- application allowlisting or execution control where appropriate;
- backup and recovery status;
- time synchronization;
- configuration-management source of truth.

## Evidence-driven assessment workflow

1. Record system/version and assessment scope.
2. Collect read-only inventory first.
3. Map privileged identities and execution boundaries.
4. Identify writable or user-influenced inputs to privileged components.
5. Validate one hypothesis at a time with a harmless test.
6. Correlate host logs, endpoint telemetry, and configuration.
7. Restore the baseline and verify remediation.

## Common mistakes

- Treating “administrator access obtained” as the only goal of host security.
- Running credential-dumping tools where configuration evidence is enough.
- Installing backdoors or stealth mechanisms in a learning environment.
- Deleting logs during cleanup.
- Ignoring service accounts and scheduled automation.
- Hardening a host without documenting rollback and recovery.
- Applying broad permissions to make an application work.

## Safe lab

Create two local users in a disposable VM: a standard user and an administrator. Create one directory writable only by the administrator and another intended for both. Verify permissions from each account, create a benign scheduled task or service under the intended identity, generate a normal event, and confirm the event is logged. Remove the test object and record the before/after state.

## Knowledge check

1. What makes a writable file a privilege-escalation concern?
2. Why should logging be centralized?
3. How can persistence be studied without deploying a backdoor?
4. What is the difference between an authentication weakness and an authorization weakness on a host?
5. Why should a hardening change include a rollback plan?

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md). The mastery goal is to identify one real privilege boundary in a lab host, collect evidence, harden it, and prove the control changed the result.

### Continue with

Recommended next modules: **12, 32, 33, 73, 74**.

---

# Malware Concepts, Analysis and Defensive Triage

Malware is software or code intentionally used to violate a security property: steal information, disrupt operations, gain unauthorized control, persist, spy, encrypt data, or abuse system resources. Security professionals need to understand malware behavior without developing or deploying harmful code.

> **Authorized-use boundary:** Analyze malware only in an isolated environment you control and only when you are authorized to possess the sample. Prefer harmless training samples, known test strings, prerecorded telemetry, or intentionally non-malicious binaries when learning.

## Learning objectives

- classify malware by behavior rather than sensational labels;
- understand infection, execution, persistence, command-and-control, and impact as behavioral stages;
- perform safe static and behavioral triage;
- identify useful host and network evidence;
- distinguish indicators of compromise from durable behavioral detections;
- design containment and recovery steps.

## Malware categories

Common labels include trojan, worm, ransomware, spyware, downloader, bot, rootkit, wiper, cryptominer, and information stealer. Real malware can combine several behaviors, so defenders should record what the sample actually does rather than assuming the label describes every capability.

## Initial triage

Before execution, collect basic evidence:

- cryptographic hash;
- file type and architecture;
- digital-signature status;
- size and timestamps, while remembering timestamps can be misleading;
- printable strings and embedded configuration where safe;
- import/library information;
- packaging or compression indicators;
- source and chain of custody.

Do not upload confidential samples or documents to public analysis services unless policy explicitly permits it.

## Static analysis

Static analysis inspects a file without running it. It can reveal executable format, imported APIs, strings, resources, metadata, and code structure. Obfuscation and packing reduce visibility, so absence of obvious malicious strings is not evidence of safety.

Modules 64, 67, and 79 cover executable formats, reverse engineering, and malware analysis in greater depth.

## Behavioral analysis

Behavioral analysis observes what a sample does in a controlled sandbox. Useful evidence includes:

- process tree and parent/child relationships;
- file and registry/configuration changes;
- service or scheduled-task changes;
- DNS and network destinations;
- loaded libraries;
- authentication or privilege events;
- security-control changes;
- created mutexes, sockets, pipes, or other IPC objects.

A learning lab should use a harmless program that performs known actions, such as creating a file, starting a child process, and making a request to a localhost service. The objective is learning telemetry, not creating malicious behavior.

## Persistence and privilege

Persistence describes mechanisms that cause code to execute again later. Privilege describes the authority available to that code. They are separate questions: a persistent process can have low privilege, while a one-time process can execute with high privilege.

Defenders should baseline services, scheduled tasks, startup items, extensions, and other autorun mechanisms and investigate unexpected changes.

## Command-and-control concepts

Remote-control malware needs some way to receive instructions or exfiltrate results. Defenders analyze protocol, destination reputation, certificate/DNS metadata, timing, beacon regularity, process ownership, and the relationship between network traffic and host activity. Do not reproduce real command-and-control infrastructure for learning; use localhost or prerecorded packet captures.

## Ransomware and destructive behavior

Ransomware resilience depends on prevention, detection, segmentation, least privilege, protected backups, restoration testing, and incident response. Never test encryption or destructive payloads against real user data. Module 38 covers ransomware resilience and recovery.

## Indicators and detections

An **indicator of compromise (IOC)** might be a hash, domain, filename, or registry path. IOCs can be useful but often change quickly. Behavioral detections can be more durable because they describe suspicious relationships, such as an unexpected office application spawning a script interpreter or an unsigned process changing a protected startup location.

High-quality detections include context: actor/process, target resource, operation, result, time, and expected baseline.

## Containment and recovery

A generic response sequence is:

1. validate the alert and preserve evidence;
2. isolate affected systems if necessary;
3. identify impacted identities and secrets;
4. stop propagation while maintaining investigation visibility;
5. eradicate the root cause;
6. restore from trusted sources;
7. rotate compromised credentials or keys;
8. monitor for recurrence;
9. document lessons learned.

## Common mistakes

- Executing unknown samples on a personal device.
- Disabling security controls just to make a sample run.
- Treating one antivirus label as a complete analysis.
- Focusing only on hashes and ignoring behavior.
- Uploading confidential samples to public services.
- Restoring systems without addressing the initial access path.

## Safe lab

Write a small benign script that creates a temporary file, launches a harmless child process, and writes one log entry. Observe the process tree and filesystem changes using built-in tools. Document what telemetry would allow a defender to distinguish the activity from normal software behavior.

## Knowledge check

1. Why is a malware family label insufficient for analysis?
2. What is the difference between an IOC and a behavioral detection?
3. Why should static and behavioral analysis be combined?
4. What evidence should be collected before executing a suspicious sample?
5. Why is restoration alone insufficient after ransomware?

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md). Keep all practical work harmless and isolated; the goal is analysis, detection, containment, and recovery.

### Continue with

Recommended next modules: **23, 37, 67, 79, 81**.

---

# Packet Capture, Sniffing and Network Visibility

Packet capture provides direct evidence about communication between systems. It is valuable for troubleshooting, incident response, protocol analysis, and authorized security testing, but captured traffic can contain credentials, tokens, personal data, and sensitive business information.

> **Authorized-use boundary:** Capture traffic only on networks and interfaces you own or are explicitly authorized to monitor. Prefer your own localhost/VM lab or prerecorded captures. Do not intercept third-party wireless or switched-network traffic.

## Learning objectives

- understand packet capture points and visibility limitations;
- distinguish Ethernet, IP, TCP/UDP, DNS, TLS, and application-layer evidence;
- use capture filters and display filters conceptually;
- understand switched networks, SPAN/TAP, and host capture points;
- protect sensitive packet-capture data;
- correlate packet evidence with host/application logs.

## What a packet capture proves

A capture proves what the capture point observed. It does not automatically prove what happened elsewhere. Packets can be lost before capture, offloaded by the NIC, altered by proxies, encrypted, retransmitted, or observed on only one side of a NAT or load balancer.

Always record:

- capture interface and location;
- timestamps and time source;
- capture filter;
- relevant IP addresses and ports;
- whether traffic is before or after NAT/proxying;
- packet loss or capture limitations.

## Protocol layers

A useful analysis sequence is:

1. **Link layer:** source/destination MAC, VLAN, frame type.
2. **Network layer:** IPv4/IPv6 addresses, TTL/hop limit, fragmentation.
3. **Transport:** TCP sequence/state or UDP datagrams.
4. **Naming/control:** DNS, ICMP, routing or discovery messages.
5. **Security:** TLS handshake metadata, certificate information, negotiated protocol.
6. **Application:** HTTP or other cleartext protocol only when legitimately observable.

Encryption may hide payload content while still leaving useful metadata such as endpoints, timing, volume, protocol negotiation, and certificate information.

## Switched networks

On a normal switched Ethernet network, a host does not automatically receive every other host's unicast traffic. Defenders use approved capture points such as switch mirror/SPAN ports, network TAPs, gateway sensors, host agents, or cloud traffic-mirroring features.

Do not use address-poisoning or interception techniques on shared networks simply to “see more traffic.” Build an isolated lab if you need to study those protocol failure modes.

## Filters

Capture filters reduce what is collected; display filters reduce what is shown after collection. A narrow capture can protect privacy and reduce storage but may omit context needed later. A broad capture can contain excessive sensitive data. Choose based on the investigation question.

Example with `tcpdump` on your own localhost interface:

```bash
tcpdump -i lo tcp port 8000
```

Then generate a normal local request to a service you started yourself. Stop the capture immediately after the test.

## TCP analysis

Useful TCP evidence includes SYN/SYN-ACK/ACK, sequence numbers, retransmissions, resets, window behavior, and connection teardown. Retransmissions can indicate packet loss or congestion; they are not automatically malicious.

## DNS analysis

DNS captures can reveal queried names, resolver behavior, response codes, TTLs, and differences between A/AAAA responses. Encrypted DNS may move visibility to endpoints or approved resolver logs instead of network payload inspection.

## TLS analysis

Without session keys, modern TLS normally protects application content. Analysts can still examine protocol versions, certificate metadata, server names where exposed by the protocol/deployment, connection timing, and endpoint relationships. Do not weaken TLS in production just to make packet inspection easier.

## Packet-capture handling

PCAP files can contain passwords from legacy cleartext protocols, bearer tokens, cookies, email content, identifiers, internal hostnames, or confidential documents. Store captures with access controls, short retention where possible, and sanitized extracts for reports.

## Common mistakes

- Capturing on an interface without knowing where it sits in the path.
- Assuming absence of a packet means the event never occurred.
- Keeping huge captures full of unnecessary sensitive data.
- Treating retransmissions or resets as attacks without context.
- Disabling encryption for visibility rather than using endpoint telemetry.
- Capturing traffic that belongs to third parties.

## Safe lab

Start a localhost HTTP server, capture only TCP/8000 on the loopback interface, make two requests, and stop the capture. Identify connection setup, request/response packets, teardown, and timestamps. Then compare the packet timeline with the server's access log.

## Knowledge check

1. What does a packet capture prove and what does it not prove?
2. Why does capture location matter?
3. What is the difference between capture and display filters?
4. Why can encrypted traffic still provide useful metadata?
5. What privacy risks exist in PCAP files?

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md). Build conclusions from packet evidence plus at least one other source such as host or application logs.

### Continue with

Recommended next modules: **12, 23, 51, 77**.

---

# Social Engineering Defense and Human-Factor Security

Social engineering abuses trust, urgency, authority, curiosity, fear, or routine business processes to persuade people into unsafe actions. Ethical security work focuses on reducing human-system risk, designing safer workflows, and conducting simulations only with explicit organizational approval.

> **Authorized-use boundary:** Do not deceive real people, collect their credentials, impersonate trusted parties, or conduct phishing/vishing exercises without explicit written authorization, legal/HR approval where required, defined data-handling rules, and a safe stop process.

## Learning objectives

- recognize common social-engineering patterns;
- understand why workflow design matters more than blaming users;
- identify controls for phishing, business-email compromise, help-desk abuse, and physical pretexts;
- design ethical simulations;
- measure resilience without collecting unnecessary personal data;
- improve reporting and recovery processes.

## Common influence patterns

Attackers often combine:

- **urgency:** “act now” or a deadline;
- **authority:** executive, support, bank, government, or administrator impersonation;
- **scarcity or reward:** limited offer, invoice refund, prize;
- **fear:** account closure, legal issue, security incident;
- **familiarity:** copied branding, prior conversation, vendor context;
- **workflow pressure:** request that bypasses normal approval because “the usual person is unavailable.”

The defense is not simply “be less gullible.” Systems should make dangerous actions difficult even when a user is stressed or mistaken.

## Phishing-resistant controls

Useful controls include:

- phishing-resistant authentication such as well-deployed passkeys/security keys;
- password managers that bind credentials to the correct origin;
- email authentication and filtering;
- browser and endpoint protections;
- out-of-band verification for high-risk transactions;
- least privilege;
- easy reporting mechanisms;
- clear approval workflows for payment, payroll, and account recovery.

## Business email compromise

BEC often targets business processes rather than software vulnerabilities. High-risk workflows include vendor bank-detail changes, payroll changes, gift-card purchases, urgent wire transfers, and executive impersonation.

Defenses should require an independent verification channel for sensitive changes. The same email thread or phone number provided inside the suspicious message should not be the only verification source.

## Help-desk and account recovery

Recovery processes can become the weakest authentication factor. Review which evidence is accepted, whether an attacker can socially engineer support staff, whether recovery bypasses MFA, how identity changes are logged, and whether high-risk resets require secondary approval.

## Physical and removable-media scenarios

Unattended devices, tailgating, visitor handling, badges, printed documents, and removable media can all create risk. Simulations should never create safety hazards, damage property, or secretly collect unrelated information.

## Designing an ethical simulation

A simulation plan should define:

1. objective and hypothesis;
2. authorized population;
3. dates and stop conditions;
4. prohibited pretexts or sensitive themes;
5. whether credentials are ever requested—prefer that they are not;
6. what data is collected;
7. who can access results;
8. how incidents caused by the simulation are handled;
9. how participants receive useful feedback.

Measure systems and processes as well as individual actions.

## Metrics that help

Useful measurements can include report rate, time to report, time to contain, percentage of high-risk requests receiving independent verification, help-desk adherence to recovery policy, and whether technical controls prevented credential use.

Avoid simplistic “clicked / did not click” leaderboards that shame individuals and provide little root-cause insight.

## Common mistakes

- Blaming users instead of fixing unsafe workflows.
- Running surprise simulations without proper approval.
- Collecting real passwords during training.
- Using traumatic or highly sensitive pretexts.
- Measuring only click rate.
- Failing to provide an easy reporting path.
- Ignoring account-recovery and help-desk processes.

## Safe lab

Create five fictional messages: legitimate invoice, fake urgent payment request, password-reset lure, collaboration invite, and help-desk request. For each, list observable warning signs, the safe verification action, and the technical/process control that would reduce risk even if a user made a mistake.

## Knowledge check

1. Why is social engineering partly a systems-design problem?
2. What makes a verification channel independent?
3. Why can account recovery undermine strong MFA?
4. Which metrics are more useful than click rate alone?
5. What controls should exist before a simulation begins?

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md). Keep all exercises fictional or explicitly approved and focus on process improvement.

### Continue with

Recommended next modules: **42, 43, 57, 60, 131**.

---

# Denial-of-Service Resilience and Resource-Exhaustion Testing

Denial of service (DoS) is any condition that prevents legitimate users from obtaining a required service. Causes include malicious traffic, software defects, dependency failure, capacity exhaustion, queue saturation, lock contention, storage pressure, and misconfiguration. Defensive engineering focuses on resilience and controlled capacity testing—not flooding third-party systems.

> **Authorized-use boundary:** Never generate high-volume or disruptive traffic toward public or shared systems. Perform load and resource-exhaustion tests only in isolated environments with explicit limits, monitoring, stop conditions, and owner approval.

## Learning objectives

- identify CPU, memory, connection, thread, queue, disk, and dependency bottlenecks;
- distinguish volumetric, protocol, and application-layer resource exhaustion;
- understand rate limiting, quotas, backpressure, timeouts, and circuit breakers;
- design safe capacity tests;
- collect evidence that separates attack traffic from ordinary failure;
- plan graceful degradation and recovery.

## Availability as a system property

Availability is affected by every dependency required to serve a request. A frontend can be healthy while its database connection pool is exhausted; a network can be reachable while a queue is full; an API can return quickly while an asynchronous worker backlog grows uncontrollably.

Map the full request path and identify bounded resources.

## Resource-exhaustion classes

### Compute

Expensive parsing, compression, regular expressions, cryptography, image processing, or poorly bounded algorithms can consume CPU.

### Memory

Unbounded request bodies, caches, queues, decompression, object retention, or too many concurrent sessions can exhaust memory.

### Connections and file descriptors

Servers have finite sockets, descriptors, worker threads, and connection-pool entries. Slow or abandoned clients can consume these resources even without high bandwidth.

### Storage and logs

Large uploads, runaway logs, temporary files, and database growth can fill storage. Logging every rejected request at excessive detail can itself become a resource problem.

### Dependencies

DNS, identity providers, databases, third-party APIs, cloud control planes, and message queues can become unavailable or slow. Timeouts and retry behavior determine whether a local failure remains local or cascades.

## Defensive controls

- per-identity and per-resource quotas;
- rate limits with appropriate burst handling;
- bounded request/body sizes;
- connection and execution timeouts;
- queue limits and backpressure;
- circuit breakers and retry budgets;
- caching where safe;
- autoscaling with cost limits;
- graceful degradation;
- upstream DDoS protection for Internet services;
- monitoring of saturation, latency, errors, and dropped work.

A rate limit without identity context can punish many legitimate users behind one NAT or fail to stop distributed abuse. Choose the key carefully.

## Safe load testing

A capacity test needs:

1. isolated or dedicated environment;
2. explicit maximum request rate and concurrency;
3. baseline measurements;
4. telemetry for CPU, memory, connections, queue depth, latency, and errors;
5. automatic stop conditions;
6. rollback/recovery plan;
7. owner present or reachable during the test.

Use a normal load-testing framework in your lab and increase load gradually. The objective is to find the knee of the curve and verify controls, not to make the system fail as violently as possible.

## Detection

Useful signals include sudden changes in request rate, unique source/identity distribution, endpoint mix, error rate, queue depth, connection states, CPU/memory saturation, cache hit ratio, and dependency latency.

Do not label every traffic spike as malicious. Product launches, software updates, backup jobs, or misbehaving clients can produce similar symptoms.

## Recovery

Resilience includes the ability to shed load, protect critical functions, restore dependencies, clear backlogs safely, and verify data consistency after pressure is removed.

## Common mistakes

- Testing production without explicit limits.
- Measuring only requests per second.
- Ignoring dependency saturation and queues.
- Using retries without budgets or jitter.
- Logging so aggressively that the defense consumes the resource.
- Treating autoscaling as unlimited protection.

## Safe lab

Create a local service with a deliberately small worker or queue limit. Send a slowly increasing number of normal requests from the same device, staying within a low preset ceiling. Record latency, errors, and resource use. Add a simple rate limit or queue bound and compare behavior. Stop before the host becomes unstable.

## Knowledge check

1. Why can low-bandwidth traffic still create DoS conditions?
2. What is backpressure?
3. Why can retries make an outage worse?
4. Which measurements identify saturation before total failure?
5. What belongs in a safe load-test stop condition?

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md). Practice capacity reasoning with bounded localhost tests only.

### Continue with

Recommended next modules: **12, 48, 59, 91**.

---

# Session Security, Cookies, Tokens and Hijacking Prevention

A session links a sequence of requests to an authenticated or otherwise stateful context. Session security fails when identifiers are exposed, predictable, accepted in the wrong context, insufficiently protected, or not revoked when the underlying authorization changes.

> **Authorized-use boundary:** Test session controls only with accounts and applications you own or are explicitly authorized to assess. Use synthetic accounts and disposable tokens. Do not intercept or reuse another person's session.

## Learning objectives

- understand server-side sessions and bearer tokens;
- evaluate cookie attributes and browser boundaries;
- distinguish token theft, fixation, replay, and authorization flaws;
- understand session rotation and revocation;
- reason about CSRF, XSS, and token storage relationships;
- design safe session tests.

## Session identifiers

A session identifier should be unpredictable, sufficiently long, and meaningless to the client. The server maps it to state such as user identity, authentication strength, permissions, creation time, and expiry.

If a session identifier is a bearer credential, possession may be enough to act as that session. Protect it like a secret.

## Cookie protections

Important attributes include:

- **Secure:** send the cookie only over HTTPS;
- **HttpOnly:** prevents ordinary JavaScript access, reducing some token-theft paths;
- **SameSite:** constrains cross-site sending and helps reduce CSRF risk;
- **Path/Domain:** limit where the cookie is sent;
- appropriate lifetime and deletion behavior.

Cookie attributes do not replace server-side authorization.

## Session fixation

Session fixation occurs when an application keeps an identifier across a security-sensitive transition such as login. A strong pattern is to rotate the session identifier after authentication, privilege elevation, password reset, or other major trust changes.

## Replay and revocation

Long-lived bearer tokens increase the window in which theft matters. Systems should define expiry, refresh behavior, revocation, logout semantics, password-reset behavior, device/session management, and what happens when an account is disabled.

## Tokens and context

A signed token can still be unsafe if it is accepted by the wrong service, tenant, audience, or workflow. Validate issuer, audience, expiry, intended algorithm/key, and authorization state. Do not assume “signature valid” means “request authorized.”

OAuth/OIDC depth is covered in Modules 39 and 92.

## XSS and session theft

If an application has cross-site scripting, an attacker may be able to act within the victim's browser context even when `HttpOnly` protects direct cookie reading. XSS prevention therefore remains important to session security.

## CSRF

Cross-site request forgery abuses the browser's ability to send credentials automatically. Defenses can include SameSite cookies, anti-CSRF tokens, origin checks where appropriate, and avoiding state-changing GET requests.

## Safe session tests

With two test accounts in a local application, verify:

- session identifier changes after login;
- logout invalidates the session server-side;
- password change or account disable has the expected session effect;
- one user's identifier cannot authorize another user's object;
- expired tokens are rejected;
- cookies use appropriate attributes.

Use only your own test sessions.

## Logging

Session logs should support investigation without recording raw bearer tokens. Useful context includes user/subject identifier, session or token fingerprint, client/device context where appropriate, authentication event, privilege changes, logout/revocation, and authorization failures.

## Common mistakes

- Logging full session cookies or bearer tokens.
- Treating logout as a client-side UI action only.
- Keeping the same session identifier before and after login.
- Validating token signature but not audience or authorization.
- Storing long-lived tokens in insecure locations.
- Testing by stealing another person's session.

## Safe lab

Use a deliberately vulnerable local web application or a small test app with two synthetic users. Observe cookie attributes, log in and log out, verify identifier rotation, and test whether a revoked session remains accepted. Record only sanitized token fingerprints.

## Knowledge check

1. Why are bearer tokens sensitive?
2. What problem does session rotation address?
3. Why is a valid JWT signature insufficient for authorization?
4. How does SameSite relate to CSRF?
5. What session evidence can be logged without storing secrets?

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md). Focus on lifecycle and authorization, not token collection.

### Continue with

Recommended next modules: **14, 39, 52, 70, 92**.

---

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

---

# Web Server and Reverse-Proxy Security

Web-server security covers the software and infrastructure that accepts HTTP(S) traffic before or alongside the application: TLS termination, virtual hosts, reverse proxies, static files, process identity, modules, file permissions, logging, and administrative interfaces.

> **Authorized-use boundary:** Test web servers only in scope. Use localhost or an intentionally vulnerable training environment for configuration experiments. Do not brute-force directories or stress public servers.

## Learning objectives

- map client, CDN/proxy, web server, application, and backend boundaries;
- review TLS, virtual hosts, methods, headers, and file exposure;
- understand process privilege and filesystem permissions;
- identify dangerous default/demo/admin content;
- review reverse-proxy trust headers;
- collect server-side evidence for findings.

## Architecture first

A request may pass through CDN, load balancer, WAF, reverse proxy, web server, application framework, and backend services. Record where TLS terminates, which component authenticates the client, which component decides the original client IP/scheme/host, and which logs contain the request.

## TLS and transport

Use HTTPS for sensitive applications and manage certificates, protocol versions, redirect behavior, HSTS policy where appropriate, and private-key access. A valid certificate proves control of a name/key relationship under the certificate ecosystem; it does not prove the application is secure.

## Virtual hosts and Host handling

One server can host several applications. Validate which hostnames are expected and what happens to unknown `Host` values. Reverse proxies and applications should agree on the trusted host/origin context so generated links, redirects, cache keys, and security decisions are not based on untrusted values.

## HTTP methods

Enable only methods required by the application. The presence of a method is not automatically a vulnerability; evaluate what action it permits, authentication requirements, and authorization checks.

## Static files and document roots

Review document-root boundaries, symlink behavior, directory listings, backup files, editor artifacts, source maps, environment files, and configuration files. Sensitive files should live outside publicly served directories and be protected by OS permissions as well as web configuration.

## Process identity

The web server and application should run with only the privileges they require. Writable directories should be narrowly scoped. Avoid running a normal web application as root/administrator.

## Reverse-proxy headers

Headers such as `X-Forwarded-For`, `Forwarded`, and scheme/host forwarding can be useful only when the application knows which proxy is trusted to set or overwrite them. Never trust client-supplied forwarding headers by default for security decisions.

## Administrative interfaces

Management consoles, status pages, metrics, debug endpoints, and health endpoints need explicit exposure decisions. Prefer dedicated management networks or authenticated access rather than relying on obscure paths.

## Logging

Record request time, normalized host, method, path, response status, latency, correlation ID, and authenticated identity where appropriate. Avoid logging passwords, authorization headers, session cookies, or sensitive request bodies.

## Safe configuration review

For a local Nginx/Apache/Caddy test instance, verify:

- bind addresses;
- document root;
- process identity;
- enabled modules/features;
- TLS configuration if used;
- default virtual host behavior;
- directory listing;
- admin/status endpoints;
- access/error logging;
- reverse-proxy trust settings.

## Common mistakes

- Assuming the application sees the original client connection directly.
- Trusting forwarding headers from arbitrary clients.
- Leaving sample or backup files under the document root.
- Running the web process with excessive privilege.
- Logging secrets.
- Treating a server banner as proof of patch state.

## Safe lab

Run a local web server bound to `127.0.0.1`. Create one public file and one file that should remain outside the document root. Verify only the public file is reachable. Then change one harmless configuration value, reload, and correlate access/error logs with the request.

## Knowledge check

1. Why can proxy headers become a trust-boundary issue?
2. Why is server version disclosure not enough to confirm a vulnerability?
3. Which files should never depend only on web-server deny rules?
4. Why should management endpoints be separated from public traffic?
5. What request data should generally not be logged?

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md). Draw the full request path before evaluating any server setting.

### Continue with

Recommended next modules: **14, 19, 40, 52, 69**.

---

# Web Application Security

Web application security is the study of how user-controlled requests move through browsers, proxies, application code, identity systems, databases, queues, and external services. The most important question is not “which payload works?” but “which security invariant can fail, at what trust boundary, and how can we prove and fix it safely?”

> **Authorized-use boundary:** Test only applications and accounts in scope. Prefer intentionally vulnerable training applications or your own local code. Avoid destructive payloads, mass data extraction, real credential capture, or uncontrolled automated scanning.

## Learning objectives

- understand input handling, output encoding, authentication, authorization, session management, and business logic;
- reason about injection, XSS, CSRF, SSRF, path handling, and insecure deserialization at a defensive level;
- test access control with synthetic accounts;
- understand browser-origin and cookie boundaries;
- write minimal proofs and remediation tests;
- use OWASP resources as structured guidance rather than a checklist substitute.

## Input is not the same as authority

Applications receive path parameters, query strings, headers, cookies, JSON/XML bodies, uploaded files, messages, and data retrieved from other services. Validation should enforce the expected schema and business rules, but authorization must still be evaluated separately.

## Injection

Injection occurs when untrusted data is interpreted as part of a command or query language rather than as data. Common defenses include parameterized queries, safe APIs, context-aware escaping where appropriate, avoiding shell construction, and least privilege for the downstream interpreter.

In labs, prove injection with harmless values and minimal output. Do not use a database flaw to extract unrelated records.

## Cross-site scripting

XSS occurs when attacker-controlled data becomes executable script in another user's browser context. Defenses include correct output encoding for the destination context, safe templating, avoiding dangerous DOM sinks, sanitizing user-authored HTML with a maintained library, and Content Security Policy as defense in depth.

## Authorization

Broken object-level or function-level authorization occurs when the server trusts an identifier or client-side UI decision without checking whether the current identity may access the specific resource/action.

A safe authorization test uses two synthetic accounts and a small set of test objects. Record expected versus observed access without reading real users' data.

## CSRF

CSRF exploits automatically attached browser credentials to trigger unwanted state changes. Use SameSite cookies, anti-CSRF tokens, origin checks where appropriate, and sound request semantics. State-changing actions should not be implemented as ordinary GET requests.

## SSRF

Server-side request forgery occurs when an application fetches a destination influenced by untrusted input and the server has more network authority than the user. Defenses include allowlists where practical, strict URL parsing, network egress controls, blocking sensitive address ranges, and separating fetch services from high-privilege networks.

Use localhost toy services for SSRF labs; do not query cloud metadata or third-party internal services.

## File handling

Uploads and path operations need content/size limits, safe storage names, separation from executable web roots, malware/content scanning where appropriate, and authorization for download/delete actions. Path traversal risk appears when untrusted path fragments are joined without safe normalization and base-directory enforcement.

## Security headers and browser controls

CSP, HSTS, frame-embedding policy, MIME controls, cookie attributes, and CORS can reduce risk, but each solves a specific problem. CORS is not an authorization mechanism, and CSP does not fix server-side access control.

## Business logic

Some vulnerabilities are valid operations performed in an unsafe sequence or quantity: duplicate redemption, negative quantity, race conditions, workflow-step skipping, or inconsistent state across services. Model state transitions and invariants rather than looking only for malformed input.

## Safe testing workflow

1. Create synthetic users/objects.
2. Record expected policy.
3. Capture a normal request.
4. Change one variable.
5. Observe response and server-side evidence.
6. Stop when the invariant is proven or disproven.
7. Apply a fix and turn the test into a regression case.

## Common mistakes

- Running large automated scans before understanding the application.
- Treating CORS as access control.
- Testing authorization with real customer data.
- Reporting reflected input as XSS without proving executable context.
- Using intrusive SQL injection techniques when a harmless boolean proof is enough.
- Ignoring business logic and state transitions.

## Safe lab

Use an intentionally vulnerable local application with two synthetic users. Build a small authorization matrix, test one reflected-input path using inert markers, inspect cookie attributes, and identify one state-changing request that should have CSRF protection. Do not collect or alter unrelated data.

## Knowledge check

1. Why are validation and authorization separate controls?
2. What makes parameterized queries effective against SQL injection?
3. Why is CORS not an authorization mechanism?
4. How can SSRF increase authority beyond the user?
5. What makes a business-logic flaw different from a parser bug?

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md). For deeper browser and parser behavior continue with Modules 52, 69, 70, 71, and 127.

### Continue with

Recommended next modules: **22, 39, 40, 41, 52**.

---

# Penetration Testing: Scope, Evidence, Reporting and Retest

Penetration testing is an authorized security assessment that combines discovery, validation, controlled exploitation where necessary, evidence collection, and reporting. A professional test is judged by accuracy, safety, reproducibility, and the usefulness of its remediation—not by the amount of access obtained.

> **Authorized-use boundary:** A penetration test requires explicit permission, defined systems, allowed techniques, data-handling rules, contacts, and stop conditions. If a requested action is outside scope, do not perform it merely because it is technically possible.

## Learning objectives

- create a rules-of-engagement document;
- design tests around security objectives;
- manage accounts, test data, and evidence safely;
- validate findings with minimal impact;
- communicate severity, uncertainty, and limitations;
- retest remediation and close findings cleanly.

## Pre-engagement

Clarify:

- legal/organizational owner of the systems;
- in-scope and out-of-scope assets;
- source addresses and test accounts;
- dates/time windows;
- allowed and prohibited techniques;
- social engineering or physical testing, if any;
- production-safety constraints;
- third-party and cloud-provider restrictions;
- emergency/stop contacts;
- data retention and encryption;
- reporting expectations.

## Threat model and objectives

A useful test begins with questions such as:

- Can a normal user access another tenant's object?
- Can an Internet-facing service reach an internal management network?
- Can a compromised workstation identity modify a protected build artifact?
- Will monitoring detect a known benign simulation of a specific behavior?

This makes testing measurable.

## Discovery

Use inventories and passive evidence first. Active scanning should be bounded to the scope and rate needed. Record every source of truth and note uncertainty.

## Validation and controlled proof

Prefer the smallest proof that demonstrates impact. Examples include reading a synthetic test object, creating a harmless marker, invoking a non-destructive test function, or reproducing a crash in a local copy.

Avoid collecting real data merely to strengthen a screenshot. Do not create persistent access unless explicitly required—and even then, prefer a benign simulation whenever possible.

## Evidence management

Evidence should include:

- timestamp and tester identity;
- affected asset/version;
- request/configuration/test input;
- relevant response or log excerpt;
- authentication/authorization context;
- expected versus observed behavior;
- screenshots only when they add information;
- hashes for downloaded artifacts when appropriate.

Redact secrets and personal data from the report.

## Severity and risk

Separate technical severity from business risk. Describe prerequisites, exploitability, blast radius, asset criticality, existing controls, and confidence. If you did not validate an assumption, say so.

## Reporting structure

A useful finding contains:

1. title and affected assets;
2. concise summary;
3. evidence/reproduction using safe steps;
4. impact in the tested environment;
5. root cause;
6. remediation;
7. retest criteria;
8. references.

An executive summary should describe themes and business consequences rather than listing tool output.

## Retest

A retest repeats the original security invariant after remediation. Confirm both that the weakness is fixed and that the intended functionality still works. If the remediation is partial, document residual risk and next actions.

## Cleanup

Remove test accounts, synthetic records, temporary files, and configuration changes that were created by the assessment. Preserve legitimate audit and security logs. Return credentials/secrets through the agreed process and confirm data-retention requirements.

## Common mistakes

- Treating a scanner report as a penetration test.
- Expanding scope informally.
- Collecting unnecessary production data.
- Creating persistence or destructive impact to “prove” severity.
- Hiding uncertainty.
- Reporting only technical details without remediation.
- Failing to retest.

## Safe lab

Write rules of engagement for a fictional two-host lab. Define one authorization objective, one network-exposure objective, and one detection objective. For each, state evidence, safe stop condition, and retest criteria. Then write one sample finding using only synthetic data.

## Knowledge check

1. What makes rules of engagement different from a target list?
2. Why is minimal proof preferred?
3. What should be redacted from evidence?
4. How does a retest differ from simply checking that a patch installed?
5. Why should logs be preserved during cleanup?

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md). A completed lab should produce a scope document and a professional finding, not merely command output.

### Continue with

Recommended next modules: **26, 27, 43, 50, 85**.

---

# Wireless Network Security

Wireless security combines radio behavior, authentication, encryption, network segmentation, device identity, roaming, and management. A secure Wi-Fi deployment is not simply “uses WPA”: the security mode, credential lifecycle, client isolation, management plane, and monitoring all matter.

> **Authorized-use boundary:** Perform active wireless testing only on access points and clients you own or are explicitly authorized to assess. Radio signals cross physical boundaries; do not capture, disrupt, impersonate, or attempt to recover credentials belonging to nearby third-party networks.

## Learning objectives

- understand 802.11 roles and basic frame categories;
- compare open, WPA2, WPA3, and enterprise authentication at a high level;
- understand PSK versus 802.1X identity models;
- identify legacy and transition-mode risks;
- review segmentation, management, and guest access;
- collect wireless evidence safely.

## 802.11 roles

A basic infrastructure network includes a **station (client)** and an **access point (AP)** associated with an SSID/BSSID. Enterprise deployments add controllers, authentication servers, certificate infrastructure, NAC, and roaming systems.

Management, control, and data frames serve different purposes. Protected Management Frames can reduce some classes of forged management traffic when required and correctly supported.

## Open networks

An open SSID provides no link-layer confidentiality between the client and AP. Application-layer TLS can still protect properly configured applications, but users remain exposed to metadata and network-level manipulation. Treat untrusted Wi-Fi as an untrusted network and rely on strong end-to-end application security.

## WPA2/WPA3 Personal

Personal mode uses a shared credential or derived password-based secret. Security depends heavily on passphrase quality and safe distribution. Shared credentials provide weak individual accountability and can be difficult to revoke for one user/device.

WPA3-Personal uses SAE, which improves resistance to offline password-guessing compared with older PSK handshakes when deployed correctly. Transition modes can reintroduce weaker compatibility paths and should be reviewed deliberately.

## Enterprise Wi-Fi and 802.1X

Enterprise mode authenticates users/devices through EAP and a backend such as RADIUS. Security depends on the chosen EAP method, client validation of the authentication server certificate, identity lifecycle, certificate/credential protection, and network policy after authentication.

A major configuration goal is preventing clients from accepting an untrusted authentication server merely because the SSID looks familiar.

## Legacy protocols

WEP is obsolete and should not be used. TKIP and older compatibility modes should be removed where supported. Legacy security belongs in historical analysis, not new deployments.

## Guest and IoT segmentation

Guest, unmanaged, and IoT devices often have different trust requirements. Use segmentation, client isolation where appropriate, restricted east-west access, DNS/egress policy, and separate management interfaces. “Connected to Wi-Fi” should not imply access to internal administration networks.

## Management plane

Protect AP/controller administration with strong authentication, restricted management networks, current software, backups, logging, and documented ownership. Avoid exposing web/SSH management broadly to client networks.

## Wireless monitoring

Useful evidence includes association/authentication events, RADIUS outcomes, AP/controller configuration changes, rogue/unknown AP observations, channel/interference health, client roaming failures, and repeated authentication errors.

Monitoring should respect privacy and legal boundaries. Do not retain unrelated client payload data.

## Safe assessment checklist

For your own AP/lab:

- document security mode;
- confirm legacy WEP/TKIP modes are disabled;
- review WPA3 transition mode intentionally;
- confirm management is not exposed to guest clients;
- verify guest/client isolation as required;
- review passphrase or enterprise credential lifecycle;
- check AP/controller update status;
- review logs for successful and failed authentication;
- confirm recovery configuration/backups exist.

## Common mistakes

- Treating signal reachability as authorization to test.
- Using a shared PSK for high-assurance enterprise identity.
- Failing to validate RADIUS/server certificates on clients.
- Leaving legacy transition modes indefinitely.
- Placing IoT, guests, and management interfaces on the same trust zone.
- Performing disruptive deauthentication tests on shared spectrum.

## Safe lab

Use an AP you own. Record its security mode, client isolation, management exposure, and update status. Connect one test device, generate normal authentication events, and verify the logs. If you have a second isolated guest network, confirm a guest cannot reach the AP's management interface.

## Knowledge check

1. Why is a shared PSK weak for individual accountability?
2. What does WPA3-SAE improve?
3. Why must enterprise clients validate the authentication server?
4. Why should guest and management networks be separated?
5. Why do radio boundaries require special authorization care?

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md). Keep experiments on owned APs and focus on configuration, identity, segmentation, and evidence.

### Continue with

Recommended next modules: **44, 51, 55, 88, 122, 123**.

---

# Mobile Security

> **Authorized-use boundary:** Assess only applications, devices, emulators, accounts, and backends you own or are explicitly authorized to test. Mobile testing often touches personal data, so use synthetic accounts and minimize collected evidence.

## Security model

A mobile system spans more than the handset. Model at least four interacting surfaces:

- **Device and operating system:** sandboxing, permissions, secure/verified boot, key storage, updates, local attack surface, and device-integrity signals.
- **Application:** components, deep links, WebViews, local storage, IPC, third-party SDKs, signing, and release configuration.
- **Network and nearby transports:** TLS, Wi-Fi, Bluetooth, NFC, push channels, proxies, and untrusted networks.
- **Backend and cloud services:** authentication, authorization, APIs, data stores, analytics, account recovery, notifications, and administrative controls.

The mobile client should not be treated as the final authority for high-value permissions or business state because users control the device and client software can be inspected or modified.

## OWASP Mobile Top 10:2024 awareness baseline

1. **M1 Improper Credential Usage**
2. **M2 Inadequate Supply Chain Security**
3. **M3 Insecure Authentication/Authorization**
4. **M4 Insufficient Input/Output Validation**
5. **M5 Insecure Communication**
6. **M6 Inadequate Privacy Controls**
7. **M7 Insufficient Binary Protections**
8. **M8 Security Misconfiguration**
9. **M9 Insecure Data Storage**
10. **M10 Insufficient Cryptography**

Use the Top 10 to organize risk awareness, then use MASVS/MASWE and platform documentation for verification requirements and testing depth.

## Mobile Platforms

- **Android** uses application sandboxing, permissions, verified boot, SELinux, platform keystores, and increasingly hardware-backed security features. Security reviews should examine exported components, intents/deep links, WebViews, backup behavior, local data, permissions, and backend trust decisions.
- **iOS/iPadOS** use code signing, sandboxing, entitlements, Keychain, Data Protection classes, and hardware-backed protections. Reviews should focus on entitlement scope, local storage, URL schemes/universal links, network security, privacy permissions, and server-side authorization.
- **Rooted or jailbroken devices** change the local trust model. Applications handling high-value data should define a risk-based policy rather than assuming client-side checks alone can prevent compromise.
- **Enterprise mobility** commonly relies on MDM/MAM, managed identities, device-compliance signals, managed app configuration, remote wipe, and conditional access.
- **BYOD** requires explicit separation of corporate and personal data, privacy-aware policy, and clear off-boarding procedures.

## Mobile Threat Model

Common mobile risks include phishing and malicious links, unsafe deep links, excessive permissions, insecure local storage, weak TLS validation, vulnerable third-party SDKs, exposed application components, account/session takeover, privacy leakage, and compromised devices. Bluetooth, Wi-Fi, NFC, QR codes, and push-notification flows can add attack surface when trust decisions are weak.

For Bluetooth and nearby-device features, minimize discoverability, require authenticated pairing where supported, remove stale pairings, and validate that application behavior does not trust a nearby device solely because a transport connection exists.

## Mobile hardening priorities

- Keep the operating system, applications, and device-management components supported and updated.
- Use a strong screen lock and phishing-resistant account authentication where available.
- Minimize app permissions and remove applications or profiles that no longer have a business purpose.
- Protect sensitive keys with platform keystores rather than ordinary application storage.
- Avoid making high-value authorization decisions solely from client-side state or root/jailbreak checks.
- Use managed configuration, MDM/MAM, conditional access, and remote-wipe capabilities where the organization requires them.
- Minimize sensitive local data, backups, screenshots, clipboard exposure, notification content, and verbose logs.
- Use official or organizationally approved distribution channels and protect release-signing credentials.
- Treat device-integrity and endpoint-security signals as risk inputs, not as perfect proof that a device is trustworthy.

## Modern mobile-security additions

- Prefer platform-backed keystores for long-lived secrets and cryptographic keys.
- Treat deep links, exported components, WebViews, clipboard use, screenshots, backups, and notifications as possible data-exposure paths.
- Use certificate validation correctly; do not disable TLS verification in production builds.
- Minimize sensitive data retained on-device and use platform storage protections.
- Enforce authentication and authorization server-side; a modified client must not become a trust boundary.
- Review mobile dependency and SDK supply-chain risk, including analytics and advertising libraries.

### Verification standards

Use the OWASP Mobile Top 10:2024 as an awareness baseline and complement it with the OWASP Mobile Application Security Verification Standard (MASVS) and testing guidance for authorized assessments.

## Safe lab ideas

Use an emulator or a deliberately vulnerable training application. Review permissions, exported components, local storage, TLS configuration, and server-side authorization without targeting third-party applications or accounts.

## Mobile application architecture review

A mobile application usually consists of more than the installed package. Review the client, backend APIs, identity provider, push-notification service, analytics/advertising SDKs, deep-link handlers, cloud storage, payment integrations, update channel, and any device-management controls. The client device should not be the final authority for permissions or business-critical state.

## Credential and secret handling

Do not embed reusable server secrets in an application package. Anything shipped to a client should be assumed recoverable by a determined user of that device. Use user- or workload-specific tokens, short lifetimes where practical, server-side authorization, and platform keystores for secrets that genuinely must persist locally.

Review whether logs, crash reports, clipboard content, screenshots, notifications, backups, or analytics events accidentally include tokens or sensitive user data.

## Authentication and authorization

Biometric prompts and device PIN checks can improve local user experience, but server-side access still needs a valid authenticated session and authorization decision. Define token expiry, refresh behavior, revocation, logout, device replacement, account recovery, and step-up authentication for sensitive actions.

Negative tests should confirm that changing a local UI state, modifying a request parameter, or using a different object identifier does not grant server-side access.

## Platform storage

Classify data before deciding where to store it. Avoid retaining sensitive data when it can be fetched again securely. Use platform-provided protected storage for cryptographic keys and small high-value secrets. Understand backup behavior and whether app data can be copied to cloud backups or desktop sync mechanisms.

## Network security

Use TLS correctly and validate certificates. Do not disable certificate verification in production because a development proxy was convenient. Review clear-text exceptions, custom trust stores, certificate pinning strategy where used, proxy behavior, and whether sensitive parameters appear in URLs or logs.

Pinning can reduce some interception risk but creates operational complexity; it should not replace normal certificate validation, server-side authentication, or secure key management.

## Deep links, intents, and URL schemes

Deep links and inter-app communication can cross trust boundaries. Validate parameters, require authentication again for sensitive actions, and ensure that an external application cannot invoke internal-only functionality. Prefer platform mechanisms that bind verified domains where appropriate and test ambiguous routing behavior.

## WebViews and embedded browsers

Treat content loaded into a WebView as web content with additional native integration risk. Minimize JavaScript bridges, restrict navigation where feasible, avoid exposing privileged native methods to untrusted pages, and ensure authentication/session data is not unintentionally shared.

## Permissions and privacy

Request only permissions needed for current functionality and explain high-sensitivity use clearly. Review camera, microphone, location, contacts, photos, nearby devices, Bluetooth, notifications, accessibility, and background execution. A permission can create privacy and security risk even when the code using it is technically correct.

Track third-party SDK data collection separately from first-party behavior. Analytics, advertising, crash reporting, and identity SDKs can expand the set of organizations and systems that receive user data.

## Build and release security

Protect signing keys and release credentials, separate debug and production configuration, remove debug endpoints, and verify that test API keys or verbose logging are not shipped. Maintain dependency ownership and know which mobile releases contain a vulnerable SDK.

Mobile applications can remain installed for long periods, so backend compatibility and forced-upgrade policy should account for clients that cannot immediately update.

## Device integrity and risk signals

Root/jailbreak and device-integrity signals can inform risk decisions but are not perfect trust proofs. Treat them as one input alongside account risk, device enrollment, session behavior, and transaction sensitivity. High-value actions should remain protected server-side even if a client reports a “trusted” device state.

## Enterprise mobile controls

Organizations can combine MDM/MAM, managed app configuration, conditional access, certificate-based device identity, data-loss controls, remote wipe, and minimum OS version requirements. Policies should distinguish corporate-owned from personal devices and explain what administrators can and cannot see on BYOD devices.

## Mobile logging

Log authentication changes, security-sensitive settings, backend authorization failures, device enrollment, token revocation, and privileged actions. Avoid logging passwords, access tokens, full payment data, or sensitive message contents. Correlate mobile events with backend request IDs when possible.

## Mobile security review checklist

- [ ] OWASP Mobile Top 10:2024 categories have been considered.
- [ ] No reusable server secret is embedded in the client.
- [ ] Server-side authorization is tested with negative cases.
- [ ] Sensitive local data is minimized and protected.
- [ ] TLS verification is enabled in production.
- [ ] Deep links and exported components have explicit trust rules.
- [ ] WebView/native bridges are minimized.
- [ ] Permissions match actual functionality.
- [ ] Third-party SDK data flows are documented.
- [ ] Release signing and CI credentials are protected.
- [ ] Debug settings are absent from production builds.
- [ ] Backend can revoke sessions and vulnerable client versions when necessary.
- [ ] Security events are logged without exposing secrets.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 01, 39, and basic Android concepts.

### Practice task

Review permissions, exported surfaces, storage, network security, logs, and update policy for an app you own or a deliberately vulnerable mobile lab.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **28, 39, 44, 56**.

---

# IoT and OT Security

Internet of Things (IoT) and Operational Technology (OT) environments join software, embedded hardware, radios, physical processes, cloud services, mobile applications, update systems, and long device lifecycles. Security reviews must therefore consider both digital compromise and the effect a failure could have on the physical world.

> **Authorized-use boundary:** Assess only devices, networks, firmware, cloud accounts, and physical processes you own or are explicitly authorized to test. Avoid disruptive radio, control-system, safety, or availability tests on shared or production environments. Prefer emulators, development boards, captured data, vendor documentation, and isolated labs.

## Learning objectives

- distinguish common IoT and OT trust boundaries;
- map device, gateway, cloud, mobile-app, and update relationships;
- evaluate identity, secrets, management interfaces, and update trust;
- understand why safety and availability change the testing model;
- identify useful evidence for embedded and operational environments;
- design safe, recoverable labs.

## IoT architecture

A typical IoT product can include sensors or actuators, a microcontroller or embedded Linux system, local radios, a gateway, vendor cloud APIs, a mobile application, and an update/signing pipeline. Draw these as separate trust zones. A weakness in a companion app can expose device credentials; a weak cloud authorization rule can affect many devices; a compromised update key can cross every local network boundary.

## Device identity and provisioning

Ask how a device receives its first identity, whether credentials are unique per unit, where keys are stored, how ownership transfer works, and how a device is decommissioned. Shared factory passwords and undocumented recovery accounts create fleet-wide risk. Provisioning should bind a device to the intended owner or tenant and should be auditable.

## Management interfaces and local services

Inventory listening services, debug interfaces, serial/JTAG access, web administration, Bluetooth/Wi-Fi pairing, discovery protocols, and maintenance ports. A service that is needed only during manufacturing should not remain broadly exposed in production. Management paths need authentication, authorization, rate/resource controls, and clear recovery behavior.

## Firmware and secure updates

An update system should answer four questions: who is authorized to publish, how the device authenticates the artifact, how rollback/downgrade is controlled, and what happens after a failed update. Digital signatures protect authenticity only when verification keys, version policy, boot chain, and recovery are also trustworthy.

## Secrets and storage

Do not assume filesystem obscurity protects credentials. Review hard-coded secrets, API tokens, Wi-Fi credentials, certificates, debug logs, crash dumps, and backup/export files. Prefer per-device secrets, hardware-backed storage when available, rotation, and minimal privilege at the cloud/API layer.

## Cloud and API authorization

IoT cloud systems often expose object identifiers for devices, homes, fleets, users, or tenants. Every operation must authorize the caller against the target object and action. A valid token is not proof that the caller owns the referenced device. Use synthetic devices/accounts when validating tenant isolation.

## OT and cyber-physical systems

OT includes industrial control, building automation, energy, manufacturing, transport, and other systems where integrity and availability can affect physical processes. Change management, safety interlocks, deterministic operation, vendor support windows, legacy protocols, and recovery procedures may matter more than aggressive vulnerability probing.

Passive discovery and configuration review are often safer starting points than active scanning. Any state-changing test should have an operator-approved rollback and safety plan.

## Segmentation and gateways

Separate device networks from user workstations and management planes. Gateways should enforce narrow protocol and destination rules. Document required east-west and north-south flows rather than granting broad connectivity because a device is difficult to manage.

## Logging and fleet visibility

Useful evidence can include firmware version, secure-boot/update status, device identity, provisioning events, authentication failures, configuration changes, cloud API decisions, gateway connections, and recovery actions. Logs should avoid recording secrets and should be time-correlated across device, gateway, and cloud components.

## Common mistakes

- Treating every device on a local network as trusted.
- Shared default or fleet-wide credentials.
- Updates without authenticated provenance or rollback policy.
- Debug interfaces left enabled without ownership controls.
- Cloud authorization based only on object IDs supplied by clients.
- Testing safety-critical equipment as if it were a disposable web lab.
- No documented recovery path when a device becomes unusable.

## Safe lab

Use a development board, emulator, or spare IoT device you own. Draw the device-to-cloud/app data flow, inventory local services, record firmware/update information, and identify where credentials are stored. Change one harmless configuration in the lab and verify which local/cloud logs record the event. Restore the original state and document the recovery steps.

## Knowledge check

1. Why is per-device identity preferable to a fleet-wide password?
2. What must be trustworthy besides an update signature?
3. Why is OT testing more constrained than an ordinary disposable lab?
4. Which authorization check belongs in a multi-tenant IoT API?
5. What evidence helps correlate a device event with a cloud decision?

## Guided study workflow

Use [Study Method](../Guides/STUDY-METHOD.md). Focus on the complete lifecycle—manufacture, provisioning, normal operation, update, ownership change, incident recovery, and decommissioning—rather than only the device's open ports.

### Continue with

Recommended next modules: **41, 48, 54, 56, 83, 103, 122, 123**. From the main menu, choose **Search lessons** for related embedded, hardware, and radio topics.

---

# Cloud Security

> **Authorized-use boundary:** Use cloud labs, sandbox accounts, training tenants, or environments you own or are explicitly authorized to assess. Do not test provider infrastructure or other tenants.

## Learning objectives

By the end of this module, you should be able to:

- explain the shared-responsibility model without assuming that “the provider handles security”,
- distinguish identity-plane, control-plane, data-plane, and workload risk,
- reason about blast radius across accounts/projects/subscriptions and tenants,
- design least-privilege human and workload access,
- evaluate storage, network, secret, logging, backup, and deployment controls,
- produce a small cloud threat model and evidence-based hardening plan.

## Cloud service models

### Infrastructure as a Service (IaaS)

IaaS exposes virtualized compute, networking, and storage while the provider operates the underlying physical infrastructure. The customer typically remains responsible for guest operating systems, applications, identities, data, workload configuration, and much of the network policy.

### Platform as a Service (PaaS)

PaaS removes more operating-system and runtime administration from the customer. That does **not** remove application, identity, data, secret, authorization, or configuration responsibilities. A managed database can still be publicly exposed; a managed application platform can still run vulnerable code; a managed identity integration can still be over-privileged.

### Software as a Service (SaaS)

SaaS shifts most infrastructure and application operation to the provider. Customer risk concentrates around identity, tenant configuration, data sharing, integrations, API tokens, administrator roles, retention, endpoint/session security, and the ability to investigate incidents.

The useful question is not “who owns the server?” but **which security decisions are still under your control?**

## Deployment and tenancy models

Public, private, hybrid, and community-style environments differ in ownership and connectivity, but tenancy boundaries matter more than labels. Document which resources share an administrative plane, identity system, network, encryption keys, logging destination, and recovery path.

A “private” environment can still have weak identity controls. A public-cloud workload can be strongly isolated. Security depends on the actual architecture and policies.

## Shared responsibility

Build a responsibility matrix for each service. Include at least:

| Area | Provider responsibility | Customer responsibility to verify |
|---|---|---|
| Physical facilities | Data-center protection | Contract/compliance requirements |
| Hypervisor / managed platform | Provider-operated isolation | Service choice and exposure assumptions |
| Human identities | Identity service availability | MFA, lifecycle, roles, recovery |
| Workload identities | Platform primitives | Scope, issuance, rotation, revocation |
| Data | Service durability features | Classification, access, encryption, lifecycle |
| Network | Fabric availability | Ingress, egress, segmentation, private access |
| Logging | Logging capability | Enablement, retention, protection, alerting |
| Backups | Service mechanisms | Coverage, isolation, restore testing |
| Application code | Usually customer | Secure design, dependencies, secrets, authz |

Managed service does not mean managed **risk**.

## Cloud trust boundaries

Cloud environments contain several interacting boundaries:

- **identity plane:** users, service accounts, workload identities, federation;
- **control plane:** APIs that create, modify, or delete resources;
- **data plane:** application and storage traffic;
- **management plane:** organization, billing, policy, audit, and security tooling;
- **workload boundary:** VM, container, function, managed runtime, or SaaS integration;
- **tenant boundary:** separation from other customers or business units;
- **recovery boundary:** backups, break-glass identities, immutable logs, and alternate access paths.

A threat model should show where authority crosses these boundaries and which identity performs each action.

## Identity-first cloud security

Long-lived access keys create avoidable risk. Prefer centrally managed human identities, MFA, federation, workload identity, and short-lived credentials where supported.

### Human access

Review:

- joiner/mover/leaver lifecycle,
- privileged-role assignment,
- MFA and phishing-resistant authentication for high-impact roles,
- just-in-time elevation where available,
- break-glass account protection,
- dormant accounts and stale API tokens,
- cross-account or cross-tenant trust.

### Workload access

A workload should receive only the permissions it needs for its current role. Avoid sharing one powerful service identity across unrelated applications. Document credential issuance, audience/scope, lifetime, revocation, and what happens when the workload is moved or rebuilt.

## Control-plane security

Cloud APIs are extremely powerful because infrastructure itself is programmable. A control-plane credential may be able to create identities, modify network routes, replace images, change logging, expose storage, or destroy resources.

Protect control-plane actions with:

- least privilege,
- organization-level guardrails,
- separation of duties,
- strong authentication,
- infrastructure-as-code review,
- protected deployment pipelines,
- immutable or independently protected audit logs,
- alerts for high-impact policy and identity changes.

## Network architecture

Cloud networking should be designed from required flows rather than from broad “internal” trust.

Document:

- internet-facing entry points,
- load balancers and API gateways,
- private endpoints,
- east-west workload traffic,
- administrative access paths,
- DNS dependencies,
- egress destinations,
- peering/transit relationships,
- network-policy enforcement points.

A security group or firewall rule is only one layer. Application authorization and workload identity still matter after network admission.

## Storage and data security

For each data store, identify:

1. owner and classification,
2. permitted identities,
3. public-access state,
4. encryption and key ownership,
5. replication/location requirements,
6. retention and deletion policy,
7. backup and restore behavior,
8. audit events that prove access or policy change.

Do not treat encryption at rest as a substitute for authorization. If an over-privileged identity can decrypt data through the normal service API, the cryptography is working exactly as designed while the access model remains unsafe.

## Secrets and key management

Secrets should not be embedded in images, repositories, deployment templates, shell history, or application logs. Prefer managed secret stores or workload identity.

Separate:

- secret **storage**,
- authorization to **read** a secret,
- authorization to **use** a key without exporting it,
- rotation,
- revocation,
- audit evidence.

For high-value keys, understand whether the platform uses software-protected keys, HSM-backed keys, customer-managed keys, or externally managed key material.

## Logging and detection

A cloud incident can involve identity, control-plane, network, storage, workload, and SaaS events simultaneously. Centralize enough telemetry to reconstruct those relationships.

Useful categories include:

- authentication and federation events,
- privileged-role changes,
- control-plane API calls,
- policy changes,
- storage access and public-access changes,
- network-flow or gateway logs,
- workload logs,
- key/secret access,
- CI/CD and artifact events,
- backup/recovery operations.

Protect security logs from the same identities that administer production wherever practical.

## Infrastructure as code and policy as code

Infrastructure as code improves repeatability, but insecure configuration can also be repeated perfectly. Use code review, automated checks, protected branches, plan/diff review, deployment identity separation, and drift detection.

Policy as code can enforce organization-wide invariants such as:

- approved regions,
- required logging,
- prohibited public storage,
- mandatory encryption,
- allowed workload identities,
- restricted network exposure.

The policy must be tested for both false negatives and false positives.

## Multi-account and multi-project design

Separate environments to limit blast radius. Production, development, security tooling, logging, and backup administration may justify different accounts/projects/subscriptions or equivalent boundaries.

Do not assume separation is effective merely because resources have different names. Verify federation, organization roles, shared automation identities, networking, logging, and recovery permissions.

## Backup and destructive-action resilience

Backups are part of the security boundary. Test whether a compromised production administrator can also delete backups, disable retention, alter recovery settings, or destroy the logging needed to investigate the event.

Recovery design should include:

- isolated or immutable copies where appropriate,
- separate administrative authority,
- documented restore procedures,
- regular restoration tests,
- dependency ordering,
- recovery when the primary identity provider is unavailable.

## SaaS and third-party integrations

SaaS risk often enters through OAuth grants, API tokens, marketplace applications, automation accounts, synchronization tools, and external administrators.

Inventory integrations and record:

- owner,
- permissions/scopes,
- data accessed,
- credential lifetime,
- revocation process,
- audit capability,
- business dependency.

A forgotten integration can retain effective access long after the employee who installed it has left.

## Threat scenarios to reason about

Model scenarios such as:

- a phishing-resistant MFA gap on a privileged account,
- an over-scoped workload identity,
- a public object-storage configuration,
- a leaked deployment secret,
- an infrastructure-as-code change that weakens logging,
- a compromised CI runner publishing an untrusted artifact,
- a cross-account trust relationship with excessive authority,
- a destructive administrator who can also remove backups,
- a SaaS integration retaining stale access.

For each scenario, record prevention, detection, containment, and recovery controls.

## Assessment questions

- Can a compromised low-privilege identity reach sensitive resources?
- Can one administrator both modify production and erase the evidence of that change?
- Are workload credentials short-lived and tightly scoped?
- Are public-access controls and organization guardrails centrally enforced?
- Are infrastructure changes attributable and recoverable?
- Can backups survive compromise of the production administrative plane?
- Can responders investigate if the primary cloud identity provider is unavailable?
- Do you know which external integrations can access sensitive data today?

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the cloud-specific preparation and exercise below.

### Before you begin

Complete Modules 01 and 21 and understand basic IP networking, DNS, authentication, authorization, and logging.

### Practice task

Design a fictional three-tier cloud application. Draw its human identities, workload identities, control plane, network paths, storage, secrets, logging, deployment pipeline, and backups. Then write five security invariants and identify the minimum evidence needed to verify each one.

### Mastery check

Explain why cloud security is primarily an **authority and control-plane problem**, identify one realistic blast-radius path, and describe a control plus a log source that would prove the control is operating.

### Continue with

Recommended next modules: **21, 24, 41, 47, 49, 76, 104, 105**.

---

# Cryptography

Cryptography provides tools for confidentiality, integrity, authenticity, key establishment, and verifiable data origin. Security depends not only on choosing a strong algorithm but also on protocol design, key lifecycle, randomness, implementation, identity binding, error handling, and operational recovery.

> **Authorized-use boundary:** Use cryptographic exercises with your own keys and synthetic data. Do not attempt to recover other people's credentials, decrypt data you are not authorized to access, or weaken real systems for experimentation.

## Learning objectives

- distinguish encryption, hashing, MACs, signatures, and key derivation;
- understand symmetric and asymmetric key roles;
- reason about nonces, IVs, salts, randomness, and replay protection;
- understand certificates, trust anchors, revocation, and key rotation;
- recognize common implementation and protocol-design mistakes;
- plan for cryptographic agility and post-quantum migration.

## Security goals

**Confidentiality** limits who can read data. **Integrity** detects unauthorized modification. **Authenticity** gives evidence about an identity or key that produced a message. **Non-repudiation** is a broader legal/operational claim and should not be assumed merely because a digital signature exists.

Cryptography does not decide authorization. A perfectly valid signature can authorize the wrong action if application policy binds it to the wrong tenant, resource, audience, or workflow state.

## Symmetric encryption

Symmetric algorithms use a shared secret key and are efficient for bulk data. Modern systems should normally use an authenticated-encryption construction so confidentiality and integrity are handled together. Key reuse, nonce/IV misuse, insecure modes, or failure to authenticate metadata can undermine an otherwise strong primitive.

## Hash functions and passwords

Cryptographic hashes provide fixed-size digests and are useful for integrity, identifiers, and protocol constructions. Password storage is different: passwords are low-entropy human secrets and should use a dedicated password-hashing/KDF design with a unique salt and suitable work parameters. A plain fast hash is not an adequate password-storage scheme.

## Message authentication codes

A MAC proves that a party possessing the shared key produced or authenticated a message. It does not provide public verifiability like a digital signature. Protocols must define exactly which fields are authenticated and how messages are encoded before the MAC is calculated.

## Public-key cryptography and signatures

Asymmetric systems use mathematically related public/private keys for key establishment, signatures, or encryption depending on the scheme. Private keys require strong access control and lifecycle management. Signature verification should validate the intended algorithm, key, context, and message representation—not just return a boolean result disconnected from policy.

## Randomness, nonces and salts

Random keys require a cryptographically secure source. A **nonce** generally needs uniqueness within the protocol's rules; an **IV** has algorithm-specific requirements; a **salt** makes otherwise identical password/hash inputs produce different derived values. These terms are not interchangeable.

## Key lifecycle

Map generation, storage, distribution, activation, use, rotation, revocation, backup, recovery, archival, and destruction. The security of data encrypted for years depends on whether the organization can protect and recover keys throughout that period without granting excessive access.

## PKI and certificates

Certificates bind public keys to identities or names under a trust model. Validation may involve chain building, hostname/identity checks, validity periods, key usage, policy, revocation strategy, and trust-store management. TLS protects a connection only if both endpoints interpret identity and authorization correctly.

## Common cryptographic failures

- inventing a custom cipher or protocol without expert review;
- nonce/IV reuse where uniqueness is required;
- keys embedded in source code or public client applications;
- encryption without integrity/authentication;
- accepting any certificate or disabling verification;
- storing passwords with a fast unsalted hash;
- using long-lived keys without rotation/revocation planning;
- logging plaintext secrets or key material.

## Cryptographic agility and post-quantum planning

Long-lived systems should know which algorithms and keys they depend on and be able to change them without redesigning the entire application. Post-quantum migration is primarily an inventory, dependency, interoperability, testing, and lifecycle problem: identify where vulnerable public-key algorithms are used, prioritize long-lived sensitive data, test standardized replacements in controlled environments, and avoid unreviewed home-grown hybrid designs.

## Safe lab

With synthetic text, create a small local program that hashes a file, computes a MAC with a temporary lab key, and performs authenticated encryption using a well-maintained library. Change one byte of the ciphertext or authenticated data and observe verification failure. Record which property each primitive provides and which key/state must remain protected.

## Knowledge check

1. Why is encryption alone not the same as authenticated encryption?
2. Why are salts, nonces, and IVs different concepts?
3. Why is a fast hash unsuitable for password storage?
4. What does certificate validation need beyond checking a signature?
5. Why is cryptographic agility an architectural property?

## Guided study workflow

Use [Study Method](../Guides/STUDY-METHOD.md). For each primitive, write the security property, required secret/public state, misuse conditions, lifecycle requirements, and evidence that would demonstrate correct use.

### Continue with

Recommended next modules: **39, 49, 78, 100, 101, 102, 103, 131, 132**. From the main menu, use **Search lessons** for a specific cryptographic primitive or protocol.

---

# Identity, Zero Trust, and Access Security

> **Purpose:** Build an identity-centric security model that limits the effect of stolen credentials and over-privileged accounts.

## Learning objectives

- Understand identity as a primary control plane.
- Apply least privilege, separation of duties, and lifecycle management.
- Distinguish authentication, authorization, session management, and privileged access.
- Understand Zero Trust as an architecture principle, not a product.
- Design telemetry for identity abuse and account compromise.

## Identity lifecycle

A secure identity program covers **joiner, mover, and leaver** events. Accounts should be created from authoritative business records, assigned only necessary access, reviewed when roles change, and disabled promptly when access is no longer required. Service and workload identities need the same ownership discipline as human accounts.

### Authentication

Prefer phishing-resistant MFA for high-risk access when available. Passwords should be long, unique, and protected by a password manager. Recovery workflows are part of authentication security; strong MFA can be undermined by a weak reset process.

### Authorization

Authorization answers what an authenticated identity may do. Common models include RBAC, ABAC, policy-based access control, and resource ACLs. Deny by default where practical and test authorization server-side.

## Privileged Access Management

- Separate administrative and daily-use accounts.
- Use just-in-time or time-bounded elevation where possible.
- Require stronger authentication and device controls.
- Monitor especially sensitive actions.
- Maintain tightly controlled break-glass access.

## Zero Trust

NIST describes Zero Trust as removing implicit trust based only on network location or ownership. Access decisions should consider the subject, device/workload, resource, policy, and current context. Zero Trust does not mean replacing every network control; it means that network location alone is not sufficient evidence of trust.

## Identity telemetry

Monitor for unusual sign-ins, repeated MFA failures, new MFA methods, privilege changes, new API keys or service principals, unmanaged devices, logging/policy changes, and access inconsistent with role.

## Safe lab

Create two local test accounts with different roles. Build a permissions matrix, verify allowed and denied actions, record the audit events, remove one privilege, and retest.

## References

- NIST SP 800-207 — https://csrc.nist.gov/pubs/sp/800/207/final
- NIST Cybersecurity Framework 2.0 — https://www.nist.gov/cyberframework

## Identity architecture in practice

An identity system normally contains several layers that should be reviewed separately: the authoritative source of a person or workload, the identity provider, authenticators, directories, federation relationships, application sessions, authorization policies, privileged-access systems, and audit logs. A weakness in any one layer can undermine strong controls elsewhere. For example, phishing-resistant authentication is less valuable if account recovery accepts weak evidence, and carefully designed application roles are less valuable if a broad directory group can silently grant them.

### Human identities

Human-account controls should answer four questions: **who owns the account, why does it exist, what can it reach, and how is access removed?** Use named accounts for normal activity, avoid shared administrative users, and maintain a reliable mapping from employment or contractual status to account lifecycle. Review dormant identities, stale group memberships, guest users, forgotten test accounts, and emergency accounts separately because their risk profiles differ.

### Workload and machine identities

Applications, CI jobs, containers, scheduled tasks, service accounts, API clients, and automation also need identities. Prefer short-lived credentials or platform-issued workload identities over static secrets. Give each workload an owner and purpose, restrict where its identity can be used, and log token issuance and sensitive use. A service identity that survives for years without an owner is effectively unmanaged privileged infrastructure.

## Authentication design

Authentication strength is determined by the complete flow rather than the login screen alone. Review enrollment, recovery, device replacement, lost-factor handling, support-desk procedures, session reauthentication, and step-up requirements for sensitive actions.

Useful design principles include:

- Prefer phishing-resistant authentication for administrators and other high-impact roles.
- Avoid security questions based on discoverable biographical facts.
- Protect enrollment and recovery at least as strongly as normal authentication.
- Rate-limit and monitor failed attempts without creating easy denial-of-service conditions.
- Notify users of important authenticator and recovery changes.
- Reauthenticate for security-sensitive changes such as adding a new factor, exporting sensitive data, or changing payment details.
- Keep authentication errors useful to legitimate users without unnecessarily disclosing whether an account exists.

## Authorization design

Authorization should be explicit, server-side, and testable. A useful review starts with a matrix of **subjects × resources × actions × conditions**. This exposes accidental privilege inheritance and helps turn policy into automated tests.

### Common failure modes

- A role grants more permissions than its name implies.
- Front-end controls hide an action while the backend still permits it.
- Object ownership is checked for reads but not updates or deletes.
- Administrative APIs trust a network location instead of an identity and policy decision.
- A service account can access every tenant because it was designed before multi-tenancy existed.
- Temporary access becomes permanent because there is no expiry or review process.
- Group nesting creates effective permissions nobody can easily explain.

### Access review questions

For every sensitive permission, record the business justification, approver, owner, grant date, expiry or review date, and evidence of last meaningful use. Reviews should focus on whether access is still required, not merely whether a manager recognizes the account name.

## Privilege boundaries and break-glass access

Privileged identities deserve a different operating model. Administrative sessions can be isolated from email and browsing, privileged elevation can be time-bounded, and particularly sensitive changes can require additional approval or step-up authentication. Break-glass accounts should be few, strongly protected, tested periodically, and monitored so that their use is immediately visible. A break-glass mechanism that has never been tested may fail exactly when the normal identity system is unavailable.

## Zero Trust decision model

A Zero Trust design can be reasoned about as a sequence:

1. **Identify the resource** being requested.
2. **Identify the subject** and the strength of its authentication.
3. **Evaluate device or workload posture** if relevant.
4. **Evaluate context** such as risk, location, time, session state, and recent events.
5. **Apply policy** for the requested action.
6. **Grant the minimum required access** for the required duration.
7. **Observe the session** and be prepared to re-evaluate or terminate access.

This model is useful even in small systems. It discourages assumptions such as “inside the VPN means trusted” or “the service account already authenticated once, therefore every future action is safe.”

## Identity threat scenarios for defenders

Defenders should be able to recognize and investigate scenarios such as impossible or unusual sign-in patterns, token use from a new environment, repeated MFA failures, suspicious recovery events, newly created API credentials, privilege escalation through group changes, inactive accounts becoming active, consent to risky third-party applications, and service identities behaving differently from their normal workload.

For each scenario, define the telemetry source, minimum useful fields, expected false positives, investigation steps, containment options, and the business owner who can confirm whether the activity is legitimate.

## Identity security review worksheet

| Area | Questions | Evidence |
|---|---|---|
| Lifecycle | Are joiner/mover/leaver events automated and timely? | HR/IdP workflow, disable timestamps |
| MFA | Which roles lack strong MFA? | Authentication policy export |
| Recovery | Can recovery bypass normal assurance? | Recovery policy and test results |
| Authorization | Are object/action checks server-side? | Policy, unit/integration tests |
| Privilege | Is elevation temporary and attributable? | PAM/JIT logs |
| Workloads | Are long-lived secrets still required? | Secret inventory, token configuration |
| Guests | Are external users reviewed and expired? | Guest inventory |
| Logging | Can security changes be reconstructed? | Identity audit logs |
| Resilience | Is emergency access tested? | Break-glass test record |

## Practical defensive exercise

Create a small role matrix for a fictional company with Employee, Support, Billing, Developer, and Administrator roles. Add three resources—customer profile, billing record, and deployment pipeline—and define read/write/admin actions. Deliberately create one over-privileged role, then perform an access review and correct it. Finally, list the audit events that should be generated when the privilege is granted, used, and removed.

## 2026 identity update — NIST SP 800-63 Revision 4

NIST finalized SP 800-63 Revision 4 in 2025. When designing identity systems, distinguish identity proofing, authentication, authenticator management, and federation rather than reducing identity security to password complexity. Prioritize phishing-resistant authentication for higher-risk use cases, secure recovery, lifecycle management, and privacy-aware identity proofing.

Primary reference: https://csrc.nist.gov/pubs/sp/800/63/4/final

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 01 and authentication basics.

### Practice task

Create a fictional access matrix for employees, admins, service accounts, and emergency access. Remove standing privileges that are unnecessary and define review/revocation evidence.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **32, 39, 42, 49**.

---

# Secure Software, APIs, and Supply Chain

> **Purpose:** Reduce vulnerabilities before deployment and manage risk introduced by dependencies, build systems, APIs, and third-party components.

## Secure by design

Secure software starts with architecture and product decisions. CISA's Secure by Design principles emphasize making customer security a core business requirement rather than an optional feature.

Key practices include threat modeling, secure defaults, least privilege, safe error handling, security acceptance criteria, review of high-risk changes, automated checks in CI/CD, and a supported update/vulnerability-disclosure process.

## API security

The OWASP API Security Top 10 2023 highlights authorization, authentication, object-property access, resource consumption, sensitive business flows, server-side request forgery, inventory, and unsafe third-party API consumption.

### API review checklist

- Authenticate callers with a supported mechanism.
- Authorize **every** object and sensitive operation server-side.
- Validate request size, structure, type, and allowed fields.
- Apply pagination, quotas, and rate limits to expensive operations.
- Keep an inventory of endpoints, versions, owners, and data classifications.
- Remove deprecated endpoints.
- Restrict outbound integrations and validate destination/response data.
- Log actor, target, outcome, and correlation identifiers for security-relevant actions.

## Software supply-chain security

Supply-chain risk includes source code, dependencies, registries, build runners, CI credentials, artifacts, container images, signing keys, and update channels.

### Defensive controls

1. Pin or constrain dependencies deliberately and review updates.
2. Generate/retain an SBOM where useful.
3. Protect CI/CD credentials and prefer short-lived workload identities.
4. Separate untrusted pull-request execution from release credentials.
5. Sign or attest release artifacts according to project needs.
6. Retain build provenance sufficient for investigation.
7. Scan for secrets before commits/releases.
8. Maintain a way to identify where a vulnerable component is deployed.

## Safe lab

Create a tiny local API with two users and two objects. Write tests proving each user can access only their own object. Add rate limiting and structured audit logging.

## References

- OWASP API Security Project — https://owasp.org/www-project-api-security/
- OWASP Top 10:2025 — https://owasp.org/Top10/2025/
- CISA Secure by Design — https://www.cisa.gov/securebydesign

## Secure development lifecycle

Security should be represented in the normal engineering workflow rather than added only before release. A practical lifecycle includes security requirements, architecture review, threat modeling, safe implementation patterns, code review, automated checks, pre-release validation, vulnerability handling, supported updates, and retirement planning.

### Security requirements

Write requirements that can be tested. “Use strong security” is not verifiable; “administrative actions require MFA and produce an immutable audit event containing actor, action, target, outcome, and timestamp” is. High-risk requirements should have an owner and an acceptance test.

### Threat modeling

Threat modeling identifies valuable assets, trust boundaries, entry points, dependencies, privileged components, and misuse cases before implementation choices harden. The goal is not to predict every attacker technique. The goal is to expose assumptions early enough that architecture can change cheaply.

A lightweight review can ask:

1. What data or capability is valuable?
2. Who should be allowed to use it?
3. Where does trust change?
4. What input comes from an untrusted party or system?
5. Which component can make an irreversible or high-impact change?
6. What happens if a dependency, identity, or build system is compromised?
7. What evidence would help investigate misuse?

## API authorization patterns

APIs should not infer authorization from possession of an object identifier or from a client-side control. For each endpoint, define the caller, object, action, and policy condition. Test negative cases as carefully as success cases.

### Object-level authorization

When an API receives an object ID, it must verify that the authenticated caller is permitted to perform the requested action on that object. Automated tests should include cross-user and cross-tenant requests, not just valid requests.

### Function-level authorization

Administrative or sensitive functions should have explicit policy checks. Hiding an endpoint in a UI, using an obscure route name, or assuming “normal users will never call it” is not authorization.

### Property-level authorization

Mass assignment can occur when a server binds arbitrary client-supplied fields to an internal object. Define which fields are writable for each operation and role. Sensitive properties such as role, tenant, price, owner, or approval status should not become writable merely because they appear in a JSON body.

## Resource and business-flow protection

Rate limiting should reflect resource cost and abuse risk, not only requests per second. Expensive exports, password-reset messages, image processing, AI inference, search, and bulk operations may need separate quotas. Business flows such as purchasing scarce inventory, sending invitations, creating accounts, or applying promotional credits can be abused even when each individual API request is technically valid.

## API inventory and lifecycle

Maintain an inventory containing endpoint or service name, owner, environment, authentication method, data classification, public/private exposure, supported version, and retirement date. Unknown or forgotten APIs are difficult to patch, monitor, or decommission safely.

Version retirement should include consumer discovery, migration communication, telemetry to identify remaining use, and a controlled shutdown. “Deprecated” endpoints that remain reachable indefinitely are part of the active attack surface.

## Third-party API consumption

Treat responses from external APIs as untrusted input. Validate schema and size, constrain redirects and destinations where relevant, use timeouts, handle partial failure safely, and avoid passing external content directly to interpreters. Store only the data required for the business purpose and document what happens when the provider is unavailable or compromised.

## Software supply-chain model

A release can be compromised without a vulnerability in the application source code. Important trust points include:

- developer accounts and signing credentials;
- source repositories and branch protections;
- package managers and dependency registries;
- CI runners and build images;
- build scripts and reusable workflow actions;
- artifact registries and release buckets;
- container base images;
- update mechanisms and signing keys;
- generated code, model files, plugins, and vendor binaries.

### Dependency governance

Inventory direct and transitive dependencies where practical. Remove unused packages, constrain versions intentionally, understand update ownership, and know which deployed applications contain a vulnerable component. An SBOM can support this inventory, but an SBOM by itself does not determine whether a component is reachable, exploitable, or business-critical.

### CI/CD hardening

CI systems often hold powerful credentials and execute untrusted or semi-trusted code. Separate pull-request validation from release privileges, minimize runner persistence, restrict outbound access where practical, use short-lived identity federation instead of stored cloud keys, protect environment approvals, and review changes to workflow files with the same care as application code.

### Build provenance and artifact integrity

For important releases, retain enough evidence to answer: which source revision produced this artifact, what build environment ran, which dependencies were resolved, who approved the release, and whether the artifact changed afterward? Signing and attestations can strengthen this chain, but key protection and verification policy remain essential.

## Secure by default checklist

- New accounts begin with the least privilege required.
- Security logging is enabled without requiring a premium add-on.
- Dangerous legacy protocols or compatibility modes are disabled by default.
- Secrets are not shipped as sample production credentials.
- Administrative interfaces are not publicly exposed by default.
- High-risk features require explicit enablement and clear documentation.
- Updates can be delivered safely and customers receive actionable vulnerability information.
- Failures default to a safe state when authorization or policy evaluation cannot complete.

## Code review security prompts

During review, ask whether the change adds a new trust boundary, parser, external call, file operation, privilege, secret, deserialization path, authentication state, background job, or user-controlled redirect. These prompts make review more consistent than relying on a reviewer to remember every vulnerability category.

## Defensive lab extension

Extend the toy API lab with a CI workflow that runs unit tests, dependency checks, and a secret scanner. Create a mock release artifact and record its source commit and checksum. Then simulate a dependency update and document how you would determine which environments need the new build. No external exploitation is required; the exercise is about traceability and control quality.

## Further primary references

- NIST Secure Software Development Framework — https://csrc.nist.gov/projects/ssdf
- CISA Secure by Design — https://www.cisa.gov/securebydesign

## 2026 application-assurance update — OWASP ASVS 5.0 and exploitation context

OWASP ASVS 5.0.0 is the current major verification-standard release. Use ASVS as a source of testable application-security requirements, especially where a broad awareness list such as the OWASP Top 10 is not detailed enough.

For vulnerability prioritization, technical severity should be combined with asset context and credible exploitation evidence. CISA's Known Exploited Vulnerabilities catalog is a useful source for vulnerabilities known to be exploited in the wild.

Primary references:
- https://owasp.org/www-project-application-security-verification-standard/
- https://www.cisa.gov/known-exploited-vulnerabilities-catalog

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 14, 20, and Git basics.

### Practice task

For a small project you own, inventory dependencies, create an SBOM if your ecosystem supports it, define API authorization tests, and document CI/CD secret boundaries.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **24, 40, 41, 50**.

---

# Detection Engineering, Incident Response, and Threat Hunting

> **Purpose:** Turn telemetry into reliable security outcomes and build a repeatable process for investigation, containment, recovery, and learning.

## Detection engineering lifecycle

1. Define the behavior or risk to detect.
2. Identify required telemetry and fields.
3. Build analytic logic with explicit assumptions.
4. Generate benign test events in a lab.
5. Validate parsing, enrichment, severity, and routing.
6. Document investigation steps and likely false positives.
7. Measure alert volume, precision, time-to-triage, and coverage gaps.
8. Revalidate after environment/parser changes.

## Telemetry layers

Correlate endpoint, identity, DNS/proxy/firewall, cloud control-plane, application/API, email, asset, vulnerability, and ownership context.

## Incident response lifecycle

### Preparation

Define severity, contacts, evidence handling, escalation, backup strategy, and decision authority before an incident.

### Detection and analysis

Establish what happened, when, affected identities/assets, likely path, data at risk, and confidence. Preserve important evidence before disruptive actions where feasible.

### Containment

Contain according to business impact and evidence needs—for example disabling a test/compromised account, isolating a host, revoking tokens, or disabling a vulnerable feature. Record what changed and why.

### Eradication and recovery

Remove persistence/root cause, rotate affected credentials, patch/reconfigure, restore from known-good sources, and monitor for recurrence.

### Lessons learned

Turn control failures, detection delays, and communication gaps into owned engineering work.

## Threat hunting

A hunt begins with a hypothesis, not a random query. Define the data needed, query period, expected normal behavior, and conditions that would support or falsify the hypothesis.

## Safe exercise

Generate a benign event such as creating/removing a local test account. Verify which logs record it and build a simple timeline.

## Designing useful telemetry

A log is useful only when it can answer investigation questions. For security-relevant events, useful fields often include timestamp with timezone, actor identity, source context, target resource, action, outcome, authentication method, session or request identifier, application/service name, and enough correlation data to connect events across systems. Avoid logging secrets, session tokens, full credentials, or unnecessary personal data.

### Time and normalization

Incident timelines fail quickly when clocks, timezones, usernames, hostnames, and field names are inconsistent. Centralize time synchronization, preserve original event timestamps, normalize carefully, and retain raw events when feasible. A parser change should be treated as a production change because it can silently break analytics.

## Detection engineering from behavior

A useful detection describes a security-relevant behavior and the evidence expected to accompany it. Avoid rules that merely search for a famous tool name. Tools change; behaviors often persist.

For each analytic, document:

- **Objective:** what risky behavior should be visible?
- **Data requirement:** which sources and fields are mandatory?
- **Logic:** what combination or sequence is suspicious?
- **Scope:** which hosts, identities, applications, or environments apply?
- **Exceptions:** what legitimate workflows resemble the behavior?
- **Severity:** what changes urgency?
- **Triage:** what should an analyst check first?
- **Containment:** what low-risk actions are available?
- **Validation:** how can a benign simulation prove the analytic still works?

## Detection coverage mapping

Frameworks such as MITRE ATT&CK can help organize hypotheses and communicate behavioral coverage, but a technique label is not proof that a detection is effective. Coverage should be tied to actual telemetry, validated analytics, environments, and test evidence. Record whether coverage is preventive, detective, investigative only, or currently absent.

A mature matrix might distinguish:

- telemetry exists but is not centralized;
- telemetry is centralized but not parsed;
- a query exists but has never been tested;
- an alert is tested but noisy;
- an alert is reliable and has a runbook;
- prevention blocks the behavior and detection confirms the block.

## Alert triage

Triage should reduce uncertainty quickly. Start with identity, asset criticality, event sequence, recent changes, known administrative activity, and whether the behavior is isolated or widespread. Avoid irreversible containment before understanding the likely impact unless immediate action is necessary to protect systems or people.

### A compact triage structure

1. **What triggered?** State the observed behavior, not the alert title alone.
2. **Who/what is involved?** Identify user, service, host, application, and resource.
3. **Is it expected?** Check change windows, automation, and known maintenance.
4. **What happened immediately before and after?** Build a local timeline.
5. **What is the potential blast radius?** Determine accessible resources and shared credentials.
6. **What evidence must be preserved?** Protect logs and volatile evidence as appropriate.
7. **What containment is proportionate?** Prefer reversible actions when possible.

## Incident severity

Severity should combine technical impact with business context. A low-complexity event on a public training system may be less urgent than suspicious authentication to a privileged production identity. Define criteria before incidents so teams do not invent severity under pressure.

Useful inputs include affected data, privilege level, persistence, number of assets, production impact, regulatory obligations, confidence, active adversary behavior, and availability of compensating controls.

## Evidence handling

Maintain an evidence log for important incidents: source, acquisition time, collector, method, hash where appropriate, storage location, and any transformations. Work from copies when possible. Clearly distinguish observed facts, analyst interpretation, and unverified hypotheses.

## Containment strategy

Containment is a business decision as well as a technical one. Options can include revoking sessions, resetting or disabling an identity, isolating a host, blocking an integration, restricting network paths, disabling a vulnerable feature, rotating a secret, or temporarily increasing monitoring. Record the expected effect and rollback plan.

## Recovery and validation

Recovery should address both the immediate compromise and the root cause. Restoring a server without rotating exposed credentials or correcting the vulnerable configuration simply resets the clock. Define explicit recovery criteria: patched state, credential rotation, policy correction, known-good configuration, restored monitoring, backup validation, and observation period.

## Threat hunting methodology

A hunt should be falsifiable. Example hypothesis: “A compromised service identity would show access to resource types outside its normal automation role.” Required data might include service identity, resource, action, outcome, and historical baseline. The hunt then looks for deviations and records whether they were malicious, benign, or unexplained.

Hunts can originate from intelligence, incident lessons, control gaps, unusual telemetry, or high-value asset reviews. The best outcome is often not “we found an attacker,” but “we discovered a logging gap, ownership problem, or behavior that deserves a durable analytic.”

## Tabletop exercise

Use a fictional scenario: a privileged cloud account authenticates from an unusual device, creates a new credential, and changes a logging policy. Ask participants to identify the first five facts they need, which logs should exist, which actions they would take immediately, what requires approval, and how they would prove recovery. Capture gaps as engineering tasks with owners and deadlines.

## Detection maintenance

Review analytics after major platform upgrades, parser changes, identity migrations, network redesigns, and incidents. Retire rules that no longer represent real risk. Version control detection logic and runbooks where practical so changes are attributable and reversible.

## Primary reference

- MITRE ATT&CK — https://attack.mitre.org/

## 2026 incident-response update — NIST SP 800-61 Rev. 3

NIST finalized SP 800-61 Revision 3 in April 2025. The revision integrates incident response with cybersecurity risk management and the six NIST CSF 2.0 Functions rather than treating preparation, detection, response, and recovery as an isolated linear process. Use incident lessons learned to improve governance, identification, protection, detection, response, and recovery capabilities continuously.

Primary reference: https://csrc.nist.gov/pubs/sp/800/61/r3/final

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 05, 07, 08, and 12.

### Practice task

Use synthetic logs to build an incident timeline, separate facts from hypotheses, choose proportional containment, and write recovery plus lessons-learned actions.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **37, 38, 47, 48**.

---

# Containers, Kubernetes, and DevSecOps

> **Purpose:** Secure build pipelines and cloud-native workloads by reducing privileges, protecting the control plane, and treating configuration as code.

## Container security model

Containers share a host kernel, so a container boundary is not identical to a VM boundary. Minimize images, avoid unnecessary root privileges, limit capabilities, use read-only filesystems where practical, and restrict network reachability.

### Image hygiene

Use maintained bases, remove unnecessary build tools from runtime images, pin images deliberately, scan for vulnerabilities/secrets, rebuild regularly, and keep release provenance.

## Kubernetes security areas

### Identity and RBAC

Use separate service accounts, grant only required verbs/resources, and avoid broad cluster-admin access.

### Workload isolation

Use security contexts, seccomp/AppArmor/SELinux where supported, resource limits, namespace boundaries, and network policies.

### Secrets

Kubernetes Secret objects are an API storage mechanism, not a complete secret-management strategy. Protect etcd, RBAC, backups, logs, and deployment pipelines.

### Admission and policy

Admission controls can reject privileged containers, dangerous host mounts, untrusted registries, or missing limits before runtime.

## DevSecOps controls

Use secret scanning, dependency/container scanning, tuned static analysis, IaC policy checks, authorization tests, protected release environments, short-lived CI identities, isolated runners, and controlled artifact promotion.

## Safe lab

Run a local static-page container, then switch to a non-root user and read-only filesystem. Document what functionality truly required write access or elevated privileges.

## Container image lifecycle

An image should have a clear owner, source repository, build definition, base-image policy, and update process. Prefer reproducible automated builds over manually modified running containers. Multi-stage builds can reduce runtime content by leaving compilers and package managers out of the final image.

### Runtime minimization

A smaller runtime reduces accidental exposure and makes behavior easier to understand. Remove shells or package managers only when the application does not require them; security controls should not break operability or incident response. Document the expected process tree, listening ports, writable paths, and outbound destinations for important workloads.

## Linux privilege controls

Containers can be constrained with several independent controls:

- run as a non-root UID/GID;
- prevent privilege escalation;
- drop unnecessary Linux capabilities;
- use seccomp profiles where supported;
- use AppArmor or SELinux confinement where available;
- mount the root filesystem read-only when feasible;
- provide narrowly scoped writable volumes;
- avoid host PID, IPC, or network namespaces unless required;
- avoid mounting sensitive host sockets or paths.

No single setting is a complete sandbox. The goal is layered reduction of what a compromised process can affect.

## Kubernetes control-plane security

The Kubernetes API is a central security boundary. Protect administrator credentials, restrict API exposure, use strong authentication, define RBAC deliberately, and monitor security-sensitive API operations. Backups and snapshots of cluster state can contain secrets and should receive the same protection as the live control plane.

### RBAC review

Review effective permissions rather than role names. Broad verbs such as `*`, broad resources, cluster-wide bindings, permission to create privileged workloads, and permission to read secrets deserve particular attention. Service accounts should map to actual workload needs, not a generic namespace-wide identity used by every application.

### Namespace design

Namespaces are useful organizational and policy boundaries but are not automatically strong tenant isolation. Combine them with RBAC, network policies, admission controls, quotas, and workload security policies. High-risk multi-tenant environments may need stronger isolation mechanisms beyond namespaces.

## Pod Security Standards

Kubernetes documents Pod Security Standards with three policy levels: **Privileged**, **Baseline**, and **Restricted**. Use these as a reference point for admission policy and workload review. The appropriate level depends on workload requirements, but exceptions should be explicit and documented rather than becoming the default.

## Network policy

Kubernetes networking is often permissive unless policy is added. Define which workloads need to communicate and implement ingress and egress restrictions appropriate to the network plugin and environment. DNS, telemetry, update repositories, identity endpoints, and external APIs should be considered explicitly so that egress policy remains usable.

## Secrets and configuration

A Kubernetes Secret is not automatically safe because the API object is named “Secret.” Protect access through RBAC, enable appropriate encryption-at-rest configuration, protect etcd and backups, avoid exposing secrets in environment dumps or logs, and prefer external secret-management integrations where they improve lifecycle control. Rotate secrets when ownership or exposure changes.

## Admission policy

Admission controls can enforce invariants before workloads enter the cluster. Examples include rejecting privileged pods, host namespace access, risky volume mounts, missing resource limits, unapproved registries, mutable image tags for production, or unsigned/unattested artifacts when your environment uses such verification.

Policy should include an exception workflow. Teams will otherwise bypass controls informally when legitimate edge cases arise.

## Observability for containers

Useful telemetry includes API audit logs, workload start/stop events, image identity, namespace, service account, node placement, network flows where available, admission denials, and runtime process/activity signals. Correlating a runtime event to the image digest and deployment revision improves incident response.

## DevSecOps pipeline architecture

Treat the delivery pipeline as production infrastructure. It can change what runs in production and often has access to secrets, registries, signing keys, or cloud deployment identities.

### Pipeline controls

- Require review for changes to build and deployment definitions.
- Separate untrusted contribution jobs from jobs with production credentials.
- Use ephemeral or well-isolated runners for sensitive builds.
- Prefer identity federation and short-lived credentials.
- Protect branch and release rules from unilateral bypass.
- Record artifact digests and deployment provenance.
- Scan for secrets before they reach shared history.
- Run dependency, container, and IaC checks with tuned policies rather than failing on every informational result.
- Require human approval for genuinely high-impact production actions where appropriate.

## Infrastructure as code

IaC makes configuration reviewable and repeatable, but it can also reproduce a mistake across every environment. Validate public exposure, IAM policy, encryption, logging, backup, network rules, and deletion protection before deployment. Keep emergency manual changes visible and reconcile them back into code to prevent long-term drift.

## Vulnerability management for images

An image scan is a starting point, not a risk decision. Consider whether the vulnerable package is present in the runtime image, reachable from the application, exposed to untrusted input, fixed upstream, and deployed on critical systems. Rebuild images regularly so patched base layers actually reach production.

## Safe Kubernetes lab

Use a local cluster such as kind, minikube, or another isolated training environment. Deploy a simple web application, then:

1. assign a dedicated service account;
2. run it as non-root;
3. disable privilege escalation;
4. drop unnecessary capabilities;
5. set CPU/memory requests and limits;
6. apply an ingress network policy;
7. inspect its effective RBAC permissions;
8. record the image digest;
9. enable an admission rule that blocks a deliberately non-compliant test manifest;
10. document each control and the failure mode it addresses.

The exercise should remain local and should not attempt container escape or cluster compromise.

## Primary references

- Kubernetes Pod Security Standards — https://kubernetes.io/docs/concepts/security/pod-security-standards/
- NIST Secure Software Development Framework — https://csrc.nist.gov/projects/ssdf

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 19, 22, and Linux basics.

### Practice task

Deploy a disposable local container, inventory image/source/dependencies, run it with minimal permissions, enable logs, and document how you would patch and roll back it.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **40, 41, 47, 49**.

---

# AI and LLM Security

> **Purpose:** Secure applications that use large language models, retrieval, tools, agents, and external data sources.

## Current landscape

OWASP released its **GenAI LLM Top 10 2026** on August 3, 2026. AI security changes quickly, so treat fixed lists as a starting point and verify current project guidance.

## Core risk families

### Prompt and context manipulation

Direct user input or indirect retrieved content can influence model behavior. Treat external content as untrusted data even when an LLM reads it.

### Sensitive information disclosure

Avoid placing secrets, unnecessary personal data, privileged internal instructions, or raw credentials into model context. Apply minimization/redaction before data enters logs, prompts, vector stores, or evaluation sets.

### Supply chain and provenance

Track model providers/versions, adapters, embeddings, datasets, libraries, plugins, and external services. Review update paths and security impact when any component changes.

### Unsafe output handling

LLM output is untrusted input. Do not pass model text directly into a shell, SQL query, template, interpreter, or privileged API without deterministic validation and constrained interfaces.

### Excessive agency

Agents become high risk when broad permissions, many tools, weak approvals, and ambiguous goals combine. Limit tools, scope credentials, require approval for high-impact actions, and make destructive changes reversible where possible.

### Retrieval and memory risk

RAG/vector systems can ingest poisoned content. Maintain source provenance, access control, tenancy boundaries, ingestion validation, and removal/invalidations.

### Resource abuse

Apply quotas, token/request limits, timeouts, concurrency controls, caching, and cost monitoring.

## Secure architecture pattern

Separate user input, system policy, untrusted retrieved content, model output, deterministic validation, authorization, tool execution, and audit logging. The model should not be the final authorization decision-maker for sensitive actions.

## Safe lab

Build a toy assistant with one harmless tool such as a calculator. Test whether untrusted retrieved text can cause unexpected tool calls, then add allow-lists and explicit approval.

## References

- OWASP GenAI LLM Top 10 2026 — https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/
- OWASP GenAI Security Project — https://genai.owasp.org/

## AI system threat modeling

An AI-enabled application is still a software system. Model security should be reviewed together with identity, authorization, data handling, APIs, dependencies, logging, infrastructure, and business logic. Start by drawing the complete data flow: user input, preprocessing, retrieval, system instructions, model call, memory, tools, external APIs, post-processing, storage, analytics, and human approval points.

For each component, identify what it trusts and what it can change. A model that can only draft text has a very different risk profile from an agent that can send email, modify cloud infrastructure, approve refunds, or execute code.

## Trust boundaries for prompts and context

Prompt text is not a security boundary. System instructions can guide behavior, but untrusted content can still compete with or manipulate those instructions. Therefore, authorization and safety-critical constraints should be enforced outside the model in deterministic application code or policy systems.

Distinguish at least four classes of context:

1. **Trusted application policy** — rules controlled by the application owner.
2. **Authenticated user input** — attributable but still untrusted data.
3. **Retrieved/external content** — documents, webpages, email, files, search results, database records, and tool output that may contain adversarial text.
4. **Model-generated content** — probabilistic output that must not be assumed correct or safe.

Maintain provenance where possible so downstream controls know where content came from.

## Indirect prompt injection

Indirect prompt injection occurs when malicious or misleading instructions are embedded in content the model later reads, rather than directly typed by the user. Defenses should reduce the authority of retrieved text, constrain tool use, separate data from policy, and require deterministic checks before high-impact actions.

A useful design question is: **If every retrieved document were controlled by an attacker, what could the model make the application do?** The answer defines the blast radius of retrieval compromise.

## Tool and agent security

Tools turn model output into actions. Every tool should have a narrow purpose, explicit input schema, authorization checks, bounded output, and an audit trail.

### Tool design principles

- Expose business operations rather than a generic shell or unrestricted HTTP client.
- Validate arguments deterministically.
- Scope credentials to the tool's minimum permissions.
- Re-check authorization at execution time.
- Separate read-only and write-capable tools.
- Require confirmation for irreversible or high-impact actions.
- Define rate, cost, and concurrency limits.
- Make retries idempotent where possible.
- Return structured errors rather than sensitive internal state.

### Human approval

Human-in-the-loop controls are useful only when the reviewer receives enough context to make a decision and when the application enforces the result. Avoid approval prompts that encourage routine clicking. Highlight the exact action, target, data affected, and whether the operation is reversible.

## Retrieval-Augmented Generation security

RAG systems add ingestion pipelines, vector databases, embedding models, document permissions, ranking logic, and source provenance to the attack surface.

### RAG controls

- Enforce document authorization before retrieval, not after generation.
- Preserve tenant boundaries in both metadata and query logic.
- Track source and ingestion time.
- Validate and sanitize supported file formats.
- Limit document size and recursive expansion.
- Define deletion and re-indexing procedures.
- Detect unusual bulk ingestion or retrieval activity.
- Avoid treating retrieved instructions as privileged policy.
- Test whether a user can cause retrieval of documents they cannot normally access.

## Memory and personalization

Persistent memory can accidentally convert temporary sensitive information into long-lived context. Define what is eligible for memory, how users inspect or delete it, retention periods, tenant isolation, and whether sensitive categories are excluded. Memory writes should be treated as state changes with authorization and audit requirements.

## Data leakage controls

Minimize data before it reaches the model. Mask or tokenize sensitive values when the task does not require raw values. Avoid embedding secrets in system prompts. Understand provider retention and training settings, contractual controls, and regional requirements for production data.

Output filtering can reduce accidental disclosure but should not be the only protection. The stronger control is preventing the model from receiving data the requester was never authorized to access.

## Model and dependency supply chain

Record model provider, model/version identifier, deployment configuration, fine-tunes/adapters, system prompt revision, retrieval corpus version, tool set, and important library versions for production systems. Changes to any of these can alter behavior even when application source code is unchanged.

Treat model files and adapters as artifacts. Verify origin, access control, integrity, licensing, and update process. Avoid silently replacing a production model with a new revision without evaluation of security-sensitive behavior.

## Evaluation and red teaming

AI security testing should combine deterministic software tests with behavioral evaluations. Build a repeatable corpus of benign and adversarial test cases covering data leakage, instruction conflicts, unauthorized tool requests, unsafe output handling, cross-tenant retrieval, excessive resource use, and refusal/approval boundaries.

Record the exact model version and configuration because results may change across releases. A single successful refusal is not proof of a robust control; test variants and measure failure rates.

## Logging and privacy

Useful AI audit data can include user/session identity, model/version, prompt template version, retrieval source identifiers, tool requested, tool authorized/denied, execution outcome, safety-control decision, latency, and token/cost metrics. Avoid storing full prompts and outputs by default when they may contain secrets or personal data. Use redaction and purpose-limited retention.

## Resource and cost security

AI systems can consume material compute and third-party API spend. Define per-user and per-tenant quotas, maximum context size, tool-call limits, recursion/depth limits for agents, timeouts, concurrency limits, and budget alarms. Cache only when it does not violate privacy or authorization boundaries.

## Secure AI deployment checklist

- [ ] The model cannot directly authorize sensitive actions.
- [ ] Retrieved content is treated as untrusted.
- [ ] Tool interfaces are narrow and schema-validated.
- [ ] Credentials are scoped per tool/workload.
- [ ] Cross-tenant retrieval tests exist.
- [ ] High-impact actions require policy checks and, when appropriate, approval.
- [ ] Prompt/output logs follow data-minimization rules.
- [ ] Model and prompt versions are traceable.
- [ ] Resource limits and cost monitoring are configured.
- [ ] Security evaluations are repeatable after model/configuration changes.
- [ ] A rollback path exists for a problematic model or prompt release.

## Extended safe lab

Create a local mock “support assistant” with two harmless tools: `lookup_order(order_id)` using synthetic data and `calculator(expression)` with a strict arithmetic parser. Give User A and User B separate synthetic orders. Test that the assistant cannot retrieve User B's order even when a prompt explicitly asks it to, and that text embedded inside an order description cannot cause an unauthorized tool call. The authorization check must live in the tool/application layer rather than relying on the model to remember the rule.

## Additional primary reference

- NIST SP 800-218A — https://csrc.nist.gov/pubs/sp/800/218/a/final

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 14, 22, and 41.

### Practice task

Threat-model a fictional LLM application with untrusted prompts/content, data boundaries, tool access, output handling, evaluation, and human approval for high-impact actions.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **40, 41, 46**.

---

# Security Assessment Reporting and Purple Teaming

> **Purpose:** Make security testing measurable, reproducible, and useful to engineering and operations teams.

## Evidence quality

Capture asset/environment, timestamp/timezone, exact condition, sanitized evidence, test identity/role, expected versus actual behavior, impact, remediation, and retest criteria. Avoid evidence that exposes unrelated secrets or personal data.

## Finding anatomy

1. **Title:** security condition, not tool name.
2. **Summary:** what is wrong.
3. **Affected assets:** exact scope.
4. **Evidence:** enough to reproduce safely.
5. **Impact:** realistic consequences.
6. **Likelihood/context:** exposure, prerequisites, controls.
7. **Remediation:** specific feasible actions.
8. **Validation:** how to prove the fix.

## Attack paths

Multiple moderate weaknesses can combine into high impact. Map prerequisites and trust boundaries, and distinguish confirmed observations from inference.

## Purple teaming

Purple teaming is collaboration between offensive and defensive roles to improve controls and visibility.

### Exercise loop

1. Choose a behavior to validate.
2. Define expected telemetry.
3. Generate a benign or lab-contained simulation.
4. Observe what defenders receive.
5. Improve prevention/logging/analytics/runbooks.
6. Re-test.
7. Record the control improvement.

## Metrics that matter

Track critical-asset telemetry coverage, detection coverage, alert precision, time to triage/contain, retest closure, recurrence of fixed root causes, and findings without an owner or deadline.

## Rules of engagement

A professional assessment begins with written scope and authority. Record in-scope assets, excluded assets, testing window, source addresses if relevant, allowed and prohibited techniques, data-handling requirements, contacts, stop conditions, evidence-retention period, and escalation process. Ambiguity should be resolved before a high-impact action, not after it.

### Stop conditions

Examples include unexpected production instability, access to unrelated sensitive data, evidence that a third party owns the system, impact beyond the agreed environment, or a request from the designated incident contact. A stop condition protects both the client and the assessment team.

## Assessment planning

Organize work around objectives and attack surface rather than a checklist of tools. Typical workstreams include external exposure, identity, network services, web/API, cloud configuration, endpoint controls, wireless, mobile, source/build pipeline, and detection validation. Not every engagement needs every workstream.

For each workstream, define:

- objective and business context;
- assets and owners;
- test identities/roles;
- assumptions;
- evidence needed;
- safety constraints;
- completion criteria.

## Evidence standards

Strong evidence is reproducible but minimized. Capture only what proves the condition. If a broken authorization check exposes a record, one synthetic or specifically authorized record is preferable to bulk extraction. Mask tokens, passwords, API keys, personal data, and unrelated customer content in screenshots and reports.

Each artifact should be traceable to the finding and timestamp. Keep raw evidence in a restricted location and publish sanitized evidence in the report.

## Risk rating

A numerical score can support consistency but should not replace context. Consider exploit prerequisites, exposure, privileges required, user interaction, control bypass, data sensitivity, business criticality, blast radius, detection capability, known exploitation, and remediation difficulty. Explain why the rating matters to the organization.

If CVSS is used, record the vector and version rather than only a decimal score. Supplement it with environmental/business context so readers understand why two technically similar findings may have different priorities.

## Writing actionable findings

A useful title states the condition and affected boundary, for example **“Cross-tenant object authorization missing in invoice API”** rather than **“IDOR”** or **“Burp finding.”** The report should let an engineer reproduce the control failure safely and let a manager understand consequence and priority.

### Example finding structure

**Condition:** The API verifies that a caller is authenticated but does not verify ownership of an invoice object before returning it.

**Evidence:** User A requests their own synthetic invoice and receives HTTP 200. With only the object identifier changed to User B's test invoice, the same session also receives HTTP 200.

**Impact:** A user could access another tenant's invoice data if object identifiers become known or predictable.

**Remediation:** Enforce object-level authorization using the authenticated tenant/user context on every read and write. Centralize the check where practical and add cross-tenant negative tests.

**Retest:** Repeat the authorized test with User A against User B's synthetic object and confirm denial plus appropriate logging.

The example proves the issue without instructing readers to enumerate or extract real third-party data.

## Executive summary

The executive summary should answer:

1. What was assessed?
2. What was the overall security posture relative to the stated objectives?
3. Which few risks matter most?
4. Are those risks isolated bugs or systemic patterns?
5. What should leadership prioritize next?

Avoid filling the summary with scanner counts. Ten low-value informational observations do not outweigh one systemic identity flaw.

## Technical appendix

A technical appendix can contain methodology, tools and versions, test accounts, timestamps, affected endpoints, sanitized requests/responses, log evidence, CVSS vectors, and retest results. Keep exploit-like detail proportional to what maintainers need to reproduce the issue safely.

## Root-cause analysis

Findings often cluster around a smaller number of root causes: missing ownership, inconsistent authorization middleware, unsafe defaults, incomplete asset inventory, weak secrets management, lack of dependency ownership, insufficient logging, or absence of security tests. Reporting these patterns can create more value than treating every symptom as unrelated.

## Purple-team planning

A purple-team exercise should have a control-improvement objective, not an objective to “beat the blue team.” Define the behavior, expected prevention, expected telemetry, analytic/runbook, safe simulation method, and success criteria before execution.

### Example exercise card

- **Behavior:** test account receives an unexpected privileged role.
- **Environment:** isolated staging tenant.
- **Expected prevention:** change requires approved admin workflow.
- **Expected telemetry:** actor, target, old/new role, timestamp, source context.
- **Expected alert:** high-risk privilege change outside approved workflow.
- **Simulation:** administrator assigns and removes a test role.
- **Success:** event is logged, alert routes correctly, analyst identifies actor/target, and rollback is documented.

## Retesting

A retest should verify the root condition, not only that one payload no longer works. Confirm the control applies across relevant methods, endpoints, roles, and object types. Record fixed, partially fixed, not fixed, or unable to retest, with evidence and date.

## Metrics and program improvement

Useful program metrics include median age of critical findings, percentage with named owners, retest success rate, recurrence by root cause, high-value assets without adequate telemetry, percentage of privileged identities with strong MFA, and percentage of release paths with provenance. Metrics should drive decisions rather than reward teams for generating more findings.

## Assessment closeout checklist

- [ ] Scope and authorization are archived.
- [ ] High-impact observations were communicated promptly.
- [ ] Sensitive evidence is minimized and access-controlled.
- [ ] Findings have owners and retest criteria.
- [ ] Credentials/test accounts created for the assessment are removed or transferred appropriately.
- [ ] Temporary firewall rules, agents, or debug settings are reverted.
- [ ] Data-retention and destruction commitments are scheduled.
- [ ] Lessons learned are converted into backlog items.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 05 and 15.

### Practice task

Take one safe lab finding and write three versions: technical evidence, remediation guidance for an engineer, and a concise risk summary for a manager. Keep certainty aligned with evidence.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **42, 45, 59**.

---

# Authorized Hands-On Labs

> **Scope rule:** Every exercise is for systems you own, localhost, isolated VMs/containers, or deliberately vulnerable training applications. Never point the exercises at third-party systems without explicit authorization.

## Lab 1 — Local attack-surface inventory

```console
nmap -sT -sV 127.0.0.1
```

For each listening service, document owner/process, purpose, bind address, authentication, and whether it is required.

## Lab 2 — Packet capture of your own traffic

Capture a small amount of traffic generated by your own machine. Identify DNS, TCP handshakes, TLS sessions, and local broadcast/multicast traffic. Do not capture networks where you are not authorized to inspect other users' traffic.

## Lab 3 — Web application security

Run OWASP Juice Shop or WebGoat locally. Choose one beginner lesson and focus on the control failure, evidence, and secure design change.

## Lab 4 — Authorization unit tests

Create a toy app with User A and User B, each owning one object. Write automated tests proving cross-user reads/writes are denied.

## Lab 5 — Secure password storage

Use sample passwords that are not real credentials. Compare a fast general-purpose hash with a password-specific KDF conceptually and measure why deliberate cost slows guessing.

## Lab 6 — TLS inspection

Inspect TLS on a service you operate or a public test endpoint intended for inspection. Record certificate SANs, issuer, validity, negotiated protocol, and cipher.

## Lab 7 — Detection validation

Generate a benign failed login to a local test account, locate the log event, and write a simple rule/query for repeated failures with reasonable noise control.

## Lab 8 — Incident timeline

Create a synthetic sequence: test-account creation, login, file creation, privilege change, and account removal. Build a timeline from local logs.

## Lab 9 — Container hardening

Run a local container, then use a non-root user, reduce capabilities, and use a read-only filesystem where possible. Document the minimum permissions needed.

## Lab 10 — LLM tool-boundary exercise

Build a toy assistant with a harmless calculator tool. Feed it untrusted text that requests an unexpected tool call, then add an allow-list and explicit approval layer.

## Lab report template

Record objective, environment, scope/authorization, steps, evidence, result, security lesson, remediation/control change, and retest result.

## Building a safe lab environment

A good lab is intentionally isolated, easy to reset, and clearly distinguishable from production. Prefer localhost, private virtual networks, disposable VMs/containers, and deliberately vulnerable training applications. Use synthetic names, addresses, tokens, and documents rather than copied production data.

### Lab safety checklist

- Use private/local addresses and verify the target before running a command.
- Disable bridged networking unless the exercise requires it and you understand the exposure.
- Take snapshots or keep rebuild scripts so damaged systems can be restored.
- Never reuse real passwords, API keys, customer records, or production tokens.
- Keep vulnerable training services inaccessible from the public internet.
- Stop if an exercise reaches a system that is not part of the lab.
- Capture notes and evidence as though writing a professional assessment.

## Lab 11 — Asset inventory from local evidence

Create three local services or containers with different ports and owners. Build an inventory containing hostname/container name, IP/bind address, port, protocol, process, owner, purpose, authentication requirement, and data classification. Then stop one service and verify that the inventory and scan results both change.

**Learning goal:** distinguish discovery from asset ownership. A scanner can tell you that something is reachable; it cannot tell you whether the service is approved or important.

## Lab 12 — Vulnerability prioritization tabletop

Create five fictional findings with different conditions: a critical CVSS issue on an isolated test host, a medium authorization issue on a public production API, an outdated library that is not reachable, a weak admin MFA policy, and a missing log source on a critical server. Rank them using technical severity plus business context. Explain why your order differs from sorting by score alone.

**Learning goal:** practice risk reasoning without exploiting anything.

## Lab 13 — Web security headers and TLS

Run a local HTTPS-capable development server or an intentionally configured test service. Inspect its certificate, redirect behavior, cookie flags, and relevant security headers. Change one configuration at a time and document the effect.

**Learning goal:** connect configuration to observable client behavior.

## Lab 14 — Input validation unit tests

Write a tiny local function or web endpoint that accepts a username, age, or filename. Define allowed types, length, character policy, and failure behavior. Add automated tests for empty input, oversized input, unexpected Unicode, wrong type, and path separators. Keep every test local and non-destructive.

**Learning goal:** understand validation as a positive contract rather than a blacklist of “bad strings.”

## Lab 15 — Access-control matrix

Create two users and three resources in a toy application. Define a matrix for read, update, delete, and admin operations. Implement or mock policy checks and write both positive and negative tests.

**Learning goal:** prove that authorization decisions are based on identity, action, and resource rather than UI state or object IDs.

## Lab 16 — API rate and quota design

Use a local API endpoint that performs a harmless expensive action such as generating a large synthetic report. Add a per-user quota and a maximum request size. Confirm that normal use succeeds and excessive synthetic requests are rejected predictably without crashing the service.

**Learning goal:** resource-consumption protection and graceful failure.

## Lab 17 — Secret scanning in a toy repository

Create a local Git repository and add a fake token such as `DEMO_TOKEN_DO_NOT_USE_12345`. Configure a secret-scanning pattern or pre-commit check that catches the marker. Remove it from the current file and discuss why rotating a real exposed secret would still be required even after deleting it from the latest commit.

**Learning goal:** prevention, history, and credential lifecycle.

## Lab 18 — SBOM and dependency inventory

Create a small application with a few harmless dependencies. Generate a dependency list or SBOM using an ecosystem-appropriate tool, record package versions, and identify which are direct versus transitive. Simulate an advisory by marking one package “needs review” and document how you would find deployments containing it.

**Learning goal:** software supply-chain traceability.

## Lab 19 — Identity lifecycle simulation

Create a fictional employee account and document joiner, role-change, and leaver events. During the “mover” stage, remove one old permission before adding the new one. During “leaver,” disable sign-in, revoke active sessions, remove group membership, and record which logs prove completion.

**Learning goal:** identity security is a lifecycle, not only login.

## Lab 20 — Detection rule validation

Generate a benign sequence such as five failed logins to a local test account followed by one successful login. Build a query or simple script that detects the pattern. Repeat with normal background activity and tune the rule so expected noise does not trigger unnecessarily.

**Learning goal:** detection requires both positive and negative test cases.

## Lab 21 — Incident evidence timeline

Prepare synthetic log lines from an application, identity provider, and host with timestamps in different timezones. Normalize them into one timeline and label each entry as fact, inference, or unanswered question.

**Learning goal:** evidence quality and temporal reasoning.

## Lab 22 — Backup recovery tabletop

Create a disposable directory with sample files, archive it, delete or corrupt one copy, and restore from the backup. Record recovery time, missing data, integrity checks, and the credentials required for restoration.

**Learning goal:** a backup strategy is only proven by recovery.

## Lab 23 — Cloud IAM policy review without a cloud account

Create a fictional JSON-like policy containing an overly broad wildcard permission and a second policy containing only the actions required by a mock backup job. Compare the blast radius conceptually and write a least-privilege review checklist.

**Learning goal:** reason about permissions without interacting with a real provider.

## Lab 24 — Container image minimization

Build two local images for the same static application: one with a broad development base and one with a minimal runtime base. Compare package count, image size, running user, writable paths, and exposed ports. Do not attempt escape techniques.

**Learning goal:** reduce unnecessary runtime surface.

## Lab 25 — Kubernetes admission policy

In a local cluster, create a deliberately non-compliant manifest that requests a privileged container or runs as root. Configure a local policy mechanism to reject it, then correct the manifest and verify successful deployment.

**Learning goal:** prevent dangerous configuration before runtime.

## Lab 26 — Mobile application review with an emulator

Use a deliberately vulnerable or self-written app in an emulator. Review requested permissions, exported components, local storage, network-security configuration, and backend authorization assumptions. Record findings and remediations without attacking third-party apps or accounts.

**Learning goal:** separate client hardening from server-side trust.

## Lab 27 — Phishing-awareness design tabletop

Draft a fictional internal training scenario using a non-routable example domain and no real credential collection. Define the learning objective, employee notification/consent requirements, metrics that do not shame individuals, support process for reports, and follow-up education.

**Learning goal:** build human-security exercises ethically and safely.

## Lab 28 — Logging completeness test

For a toy application, define five security-relevant actions: login, failed login, password change, privilege change, and data export. Trigger each action and verify the log contains actor, action, target, outcome, and timestamp without storing passwords or session tokens.

**Learning goal:** test logging as an application requirement.

## Lab 29 — RAG authorization test

Create a tiny local retrieval system with two sets of synthetic documents tagged `tenant=A` and `tenant=B`. Query as Tenant A and verify that retrieval filters prevent Tenant B documents from entering model context. Add negative automated tests.

**Learning goal:** enforce authorization before model generation.

## Lab 30 — Security report and retest

Pick any earlier lab result and write a complete finding: title, scope, condition, sanitized evidence, impact, remediation, and retest criteria. Apply the fix, retest, and mark the finding fixed or partially fixed with evidence.

**Learning goal:** turn technical observations into actionable security work.

## Suggested lab progression

**Foundation:** 1, 2, 7, 8, 11, 21
**Application security:** 3, 4, 14, 15, 16, 30
**Identity/defense:** 7, 8, 19, 20, 21, 28
**Cloud-native/DevSecOps:** 9, 17, 18, 23, 24, 25
**Mobile/AI:** 10, 26, 29, 30

## Lab evidence template

```text
Lab:
Date/time/timezone:
Environment:
Authorization/scope:
Objective:
Preconditions:
Actions performed:
Expected result:
Observed result:
Evidence location:
Security lesson:
Remediation/control change:
Retest result:
Cleanup completed:
```

A completed lab should end in a known state. Stop test services, remove synthetic accounts and temporary permissions, delete fake secrets, and preserve only the notes needed for learning.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Complete the prerequisites named by each selected lab.

### Practice task

Complete labs progressively. For every lab use the template in LAB-GUIDE.md and include before/after evidence plus cleanup.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **45 and the domain-specific module for each lab**.

---

# Termux Foundations and Android Linux

> **Purpose:** Learn how Termux works on Android, how its environment differs from a conventional GNU/Linux installation, and how to build a safe, maintainable mobile command-line workspace.

## Learning objectives

- Install Termux from an official source and understand package/signature compatibility.
- Navigate the Termux filesystem and Android shared storage without confusing the two.
- Use `pkg`, `apt`, shell tools, permissions, environment variables, and process controls confidently.
- Understand Android sandboxing, application UIDs, scoped storage, and why Termux is not a rooted Linux distribution.
- Build a clean baseline that can be backed up and recovered.

## What Termux actually is

Termux is an Android terminal application and Linux environment. It provides a user-space package ecosystem compiled for Android and exposes a familiar shell without requiring root. This is important: the environment feels Linux-like, but Android remains the host operating system and continues to enforce its application sandbox and permission model.

The default Termux home directory is private application storage. That private area is normally the best place for scripts, Git repositories, virtual environments, configuration files, SSH keys, and other content that needs normal Unix permissions. Android shared storage is convenient for exchanging files with Downloads, Documents, and other apps, but it does not behave exactly like a normal Linux filesystem.

## Installation and update hygiene

Use an official Termux distribution source. The upstream Termux project documents F-Droid and GitHub builds. Keep the main app and add-ons from compatible signing sources; Android package signatures matter for Termux add-ons that communicate with the main app.

After installation, refresh package metadata and upgrade installed packages:

```bash
pkg update
pkg upgrade
```

Use `pkg search NAME` before assuming a package exists. Termux package availability and names can differ from Debian, Ubuntu, Kali, or Arch.

## Storage model

Important locations include:

- `$HOME` — private Termux home. Prefer this for code and configuration.
- `$PREFIX` — Termux installation prefix, normally containing `bin`, `lib`, `etc`, and package data.
- `~/storage` — convenience links created after storage access is configured on supported Android versions.
- Android Downloads/Documents — useful for user-visible exports and imports.

A common setup command is:

```bash
termux-setup-storage
```

Grant only the Android permissions you actually need. Do not treat shared storage as a replacement for `$HOME`: executable bits, symlinks, ownership semantics, and filesystem behavior can differ.

## Core shell navigation

```bash
pwd
ls -la
cd "$HOME"
mkdir -p ~/projects
cp source.txt destination.txt
mv old-name.txt new-name.txt
rm -i unwanted.txt
```

Prefer quoting variables and paths. Mobile storage often contains spaces, punctuation, or filenames copied from browsers and messaging apps.

## Files, permissions, and executables

Unix permission notation still matters inside the Termux private filesystem:

```bash
ls -l
chmod u+x script.py
```

Avoid reflexively using `chmod 777`. Broad write permissions usually hide a design problem and make accidental modification easier.

For secrets such as private keys or token files, use restrictive permissions where supported:

```bash
chmod 600 ~/.ssh/id_ed25519
```

## Environment variables

Useful values:

```bash
printf '%s\n' "$HOME"
printf '%s\n' "$PREFIX"
printf '%s\n' "$PATH"
```

Put persistent shell customizations in the configuration file for the shell you actually use. Keep configuration readable and comment non-obvious changes.

## Package management fundamentals

Common operations:

```bash
pkg search python
pkg install python git
pkg list-installed
pkg show python
```

Before adding third-party repositories, understand who maintains them, what signing model they use, and whether you need them at all. Fewer repositories mean a smaller trust surface.

## Processes and jobs

Learn the difference between foreground, background, and suspended jobs:

```bash
ps -ef
jobs
```

Android may stop background work to save battery. A command that works indefinitely on a server can be interrupted on a phone because Android lifecycle and battery policies still apply.

## Networking basics in Termux

Useful defensive and diagnostic commands include:

```bash
ip addr
ip route
ss -lnt
curl -I https://example.com
```

Use network tools only against systems you own or are authorized to test. Localhost (`127.0.0.1`) is ideal for learning service behavior safely.

## Android sandboxing and root

Without root, Termux cannot bypass Android's application sandbox. It does not automatically gain access to another application's private data, privileged network interfaces, protected kernel features, or system partitions.

Rooting changes the trust and attack model of the entire device. It is not required for the learning paths in this guide.

## Termux add-ons

The Termux ecosystem includes add-ons such as Termux:API and Termux:X11. Add-ons should come from compatible official sources. Termux:API exposes selected Android device functions to command-line programs after the corresponding app and package are installed and permissions are granted. Termux:X11 can provide graphical application support on compatible Android versions, but it is optional for this guide.

## Baseline setup lesson

Create a clean workspace:

```bash
mkdir -p ~/projects ~/notes ~/backups
printf '# Termux notes\n' > ~/notes/README.md
```

Then record:

1. Android version.
2. Termux source and build.
3. Shell in use.
4. Installed packages needed for your studies.
5. Storage permissions granted.
6. Backup method.

The goal is reproducibility, not collecting as many packages as possible.

## Common mistakes

- Installing obsolete Termux builds from random APK mirrors.
- Mixing app/add-on signing sources.
- Keeping code only in shared storage.
- Copying Linux tutorials that assume `systemd`, `sudo`, or a standard filesystem layout.
- Running every command as root on a rooted device.
- Installing large tool collections without understanding dependencies or maintenance.
- Exposing development services on `0.0.0.0` when localhost would be sufficient.

## Mini lab — Build a known-good Termux baseline

1. Update packages.
2. Create `~/projects`, `~/notes`, and `~/backups`.
3. Install only Python and Git.
4. Record `python --version`, `git --version`, `$PREFIX`, and `$HOME` in a notes file.
5. Start a localhost-only Python web server in a disposable directory and confirm it is reachable from the same device.
6. Stop the service and verify with `ss` that it is no longer listening.

**Learning goal:** understand the environment before using it for security work.

## Primary references

- Termux app: https://github.com/termux/termux-app
- Termux packages: https://github.com/termux/termux-packages
- Termux:API: https://github.com/termux/termux-api
- Termux:X11: https://github.com/termux/termux-x11

## Practical Termux foundation drills

### Drill 1 — Know your environment

Record the output of `pwd`, `echo "$HOME"`, `echo "$PREFIX"`, `python -V`, and `uname -a` in a lab note. Do not treat the strings as trivia: explain what each value tells you about paths, package locations, interpreter version, and host/kernel context. Then identify which files are private to Termux and which are intentionally shared with Android.

### Drill 2 — Permission reasoning

Create a disposable file and directory under `$HOME`. Inspect permissions with `ls -la`, change only the owner's permissions, and explain the difference between read, write, and execute for a file versus a directory. Avoid applying broad permissions recursively. The goal is to understand access semantics, not to make permission errors disappear.

### Drill 3 — Rebuildability

Create `~/notes/termux-baseline.md` containing the packages you intentionally installed, storage setup, important project directories, and any configuration you changed. Imagine the app is removed tomorrow: your notes should tell you how to recreate the workspace without copying unknown caches or hidden state.

## Android-specific guidance

When desktop Linux instructions fail in Termux, check whether they assume systemd, root access, `/usr`, privileged raw sockets, kernel modules, desktop filesystem layout, or always-on background services. Termux uses its own prefix and runs inside Android's application model. Adapt the workflow rather than trying to force Android to behave like a conventional server.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

No Linux experience required; Module 01 helps.

### Practice task

Build a clean Termux workspace under $HOME, configure shared storage only if needed, install a minimal baseline, and write a recovery note explaining where every important file lives.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **29, 30, 31, 56**.

---

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

---

# Termux Networking, SSH and Local Services

> **Purpose:** Learn networking from an Android/Termux environment while keeping exercises limited to localhost, owned devices, and explicitly authorized systems.

## Networking mental model

Separate these layers when troubleshooting:

1. interface and address;
2. route;
3. name resolution;
4. transport connection;
5. TLS;
6. application protocol;
7. authentication and authorization.

A browser error saying a page did not load does not tell you which layer failed.

## Local interfaces and routes

Inspect your own device configuration with platform-available tools. `ip addr` and `ip route` show addressing and routing when supported by the environment. `ss` can show local listening sockets and established connections.

The important security question is **what address a service is bound to**:

- `127.0.0.1` / `::1` — local device only.
- a Wi-Fi/LAN address — potentially reachable by peers on that network.
- `0.0.0.0` / `::` — all available interfaces, often broader than intended.

For learning services, default to localhost.

## DNS basics

DNS maps names to records such as A/AAAA, MX, TXT, CNAME, and others. Learn to distinguish a DNS failure from a routing or TLS failure. Do not assume a successful DNS lookup means the service is trustworthy.

## HTTP and HTTPS inspection

`curl` is useful for defensive validation:

```bash
curl -I https://example.com
```

Headers can reveal redirects, cache controls, content types, and security policies. For your own services, compare expected versus observed behavior.

## Running a localhost-only development service

A safe exercise is serving a disposable directory to the same device:

```bash
mkdir -p ~/projects/local-demo
cd ~/projects/local-demo
printf 'hello\n' > index.html
python -m http.server 8000 --bind 127.0.0.1
```

This is not a production server. It is intentionally simple and useful for learning ports, processes, requests, and logs.

## SSH concepts

SSH provides encrypted remote terminal and file-transfer capabilities. The security model depends on:

- host authenticity;
- user authentication;
- private-key protection;
- server configuration;
- authorized keys;
- network exposure.

Termux can act as an SSH client and, when deliberately configured, can run an SSH server for your own device. If you do this, use strong key-based authentication, understand the listening address, and avoid exposing the service to the public internet.

## Host-key verification

The first SSH connection usually introduces a host key. Treat unexpected host-key changes as an event to investigate rather than clicking through automatically. Legitimate causes include reinstallations and key rotations, but an unexpected change can also indicate connecting to the wrong host.

## Port forwarding concepts

SSH tunneling can securely connect applications across trusted endpoints, but it can also bypass intended network boundaries if misused. In authorized environments, document tunnel purpose, endpoints, ports, and lifespan. Remove temporary tunnels after use.

## File transfer

Use `scp`, `sftp`, or another encrypted transfer mechanism for owned systems. Validate destination paths before sending sensitive files from a phone, where autocomplete and touch input make mistakes easy.

## Local service inventory

Periodically check which programs are listening:

```bash
ss -lnt
```

For every listening service, be able to answer:

- What process owns it?
- Why is it running?
- Which interface is it bound to?
- Does it need authentication?
- Should it start automatically?

## VPNs and Android

Android VPN apps affect routing from the device, but behavior depends on VPN implementation, split tunneling, always-on settings, and app exclusions. When troubleshooting, record whether the VPN is active before drawing conclusions from network tests.

## Wireless limitations

A normal non-root Termux environment does not magically provide monitor mode or low-level Wi-Fi capabilities. Hardware, kernel, driver, Android permission, and root constraints matter. This guide does not depend on bypassing those constraints.

## Mini lab — Local service map

1. Start two harmless services on different localhost ports.
2. Use `ss` to record listeners.
3. Use `curl` to query the HTTP service.
4. Stop one service.
5. Repeat the inventory and document the difference.
6. Explain what would change if the service were bound to the LAN address instead.

**Learning goal:** connect processes, ports, interfaces, and application behavior.

## Mini lab — SSH trust checklist

On two devices you own, create a checklist covering:

- server address;
- expected host-key fingerprint;
- user account;
- authentication method;
- key revocation plan;
- listening interface;
- firewall/network boundary;
- backup access method.

The lab is complete when you can explain the trust relationship, not merely when a login succeeds.

## Practical networking drills in Termux

### Loopback first

Before exposing any development service to Wi-Fi or another interface, make it work on `127.0.0.1`. Verify the listening socket and application log. This separates application problems from network-reachability problems and dramatically reduces accidental exposure.

### SSH administration checklist

For an SSH server you own, document the account used, authentication method, listening interface, port, host-key verification, client key storage, log location, and shutdown procedure. Prefer key-based authentication and never place the private key in Android shared storage merely to make it easier to find.

### Name-resolution exercise

Use a domain you control or a well-known public documentation domain to observe ordinary DNS resolution. Compare the name you typed with the returned addresses and explain why a DNS answer is only one step in establishing application identity; TLS certificate validation and application authentication are separate controls.

## Mobile networking limitations

Some low-level networking tools need kernel capabilities or interfaces unavailable to an unrooted Android app. Treat that as a platform boundary, not a problem to bypass. Focus Termux on user-space networking, local services, SSH, HTTP clients, DNS tools, log analysis, automation, and interaction with systems you are explicitly authorized to administer.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 28, 29, and 51.

### Practice task

Run a loopback-only HTTP service and inspect your own listening socket plus request logs. Explain why binding to loopback is safer than exposing a learning service on every interface.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **31, 36, 51, 52**.

---

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

---

# Windows and Active Directory Security

> **Purpose:** Understand Windows enterprise security and Active Directory from a defender, administrator, and authorized-assessment perspective.

## Learning objectives

- Understand domains, forests, trusts, domain controllers, identities, groups, and Group Policy.
- Recognize why identity tiering, credential protection, patching, logging, and delegation matter.
- Review common enterprise failure modes without relying on credential theft or destructive techniques.
- Build safer AD labs for configuration review and detection validation.

## Active Directory mental model

Active Directory Domain Services is both a directory and an authentication/authorization control plane. Important objects include users, computers, groups, service accounts, organizational units, Group Policy Objects, and trusts.

Security depends on relationships. A low-value workstation account may matter because it can modify a group, a group may control a server, and that server may hold credentials or administration paths into more critical systems.

## Authentication concepts

Windows environments commonly use Kerberos and may retain NTLM for compatibility. Defenders should know where legacy authentication remains, why modern protocols are preferred, and how authentication events are logged.

Do not equate authentication with authorization. Successful sign-in answers “who are you?”; resource ACLs, group membership, privileges, and policy answer “what can you do?”

## Privileged identities

Separate day-to-day accounts from administrative identities. Critical administrators should not use privileged accounts for browsing, email, or routine workstation activity.

High-value controls include:

- phishing-resistant MFA where supported;
- privileged access workstations or equivalent hardened admin paths;
- just-in-time/just-enough administration;
- unique local administrator credentials;
- service-account lifecycle management;
- removal of stale group memberships;
- protection of directory backups and recovery credentials.

## Group Policy

Group Policy can enforce powerful security settings at scale, but a misconfigured GPO can also propagate risk quickly. Treat GPO creation, linking, delegation, and modification as privileged operations and monitor changes.

## Service accounts

Service accounts frequently become long-lived because application owners fear breaking dependencies. Inventory owner, purpose, privileges, logon rights, rotation mechanism, and dependencies. Prefer managed service-account mechanisms where supported.

## Local administrator risk

Reusing one local administrator password across many endpoints creates a broad blast radius. Use platform-supported local password management and avoid shared static credentials.

## Delegation and ACL review

Active Directory has many permission paths beyond obvious administrator groups. Review who can create users, reset passwords, modify group membership, write to sensitive objects, link policy, enroll certificates, or modify service configuration.

## Certificate services

Enterprise PKI and certificate enrollment add another identity plane. Secure template permissions, enrollment rights, issuing CAs, private keys, renewal paths, and administrative roles. Certificate-based authentication should receive the same seriousness as passwords and tokens.

## Windows logging

Useful sources include security event logs, PowerShell logs, endpoint detection telemetry, directory-service logs, authentication provider logs, and configuration-management records. Centralize important logs so compromising one endpoint does not erase the only evidence.

## Hardening priorities

1. Patch supported operating systems and critical applications.
2. Remove unsupported protocols and unnecessary services.
3. Enforce secure boot/device protections where appropriate.
4. Use application control for high-risk systems.
5. Reduce local admin rights.
6. Protect credential material.
7. Segment administrative paths.
8. Monitor identity and policy changes.
9. Test backup and directory recovery.

## Authorized lab

Build a disposable evaluation domain using test VMs. Create normal users, one admin role, two departments, and a service account. Document:

- group membership;
- GPO scope;
- password/MFA policy;
- local admin handling;
- service-account owner;
- logging coverage;
- recovery plan.

Then make one benign policy change and verify the change appears in the expected logs.

**Learning goal:** understand AD as a permission graph and governance system, not just a login server.

## Windows security model in more depth

Windows security decisions are built around security principals, access tokens, ACLs, privileges, integrity boundaries, services, and policy. In an Active Directory environment, domain identity, Kerberos/NTLM authentication, Group Policy, certificate services, DNS, endpoint management, and privileged administration create additional dependencies.

### Identity tiers

Separate ordinary user activity from privileged administration. Highly privileged accounts should not be used for email, browsing, or routine productivity. Service identities need owners, documented purpose, minimal rights, rotation/recovery, and monitoring. Emergency access should be controlled, tested, and auditable.

### Authentication and domain dependencies

Kerberos depends on accurate time, DNS, service identity, and key material. NTLM may remain for compatibility but should be reduced where feasible. Authentication failures should be investigated with the surrounding account/device/service context rather than treated as isolated event IDs.

### Logging baseline

A useful Windows/AD telemetry design considers logon activity, privileged group changes, service creation/change, process telemetry where enabled, PowerShell/script logging according to policy, endpoint security events, directory changes, and identity-provider signals. Centralization improves correlation but does not eliminate the need to protect local evidence and time synchronization.

### Hardening questions

Ask whether local admin is needed, whether legacy protocols remain enabled, whether remote administration is restricted, whether endpoint protection/tamper protections are healthy, whether credential material is exposed unnecessarily, and whether recovery procedures exist for domain controllers and identity infrastructure.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 01, 21, and basic Windows administration.

### Practice task

In a Windows lab you administer, inventory local/domain identities, privilege groups, logging, update status, and authentication policy. Build a least-privilege remediation checklist.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **23, 37, 47, 49**.

---

# Linux Security and Hardening

> **Purpose:** Build a systematic approach to hardening Linux hosts and diagnosing security-relevant configuration.

## Security model

Linux security is layered across identities, discretionary permissions, capabilities, mandatory access controls, kernel boundaries, services, packages, network policy, and application configuration.

Hardening is not a list of commands. Start with the system's role and remove what it does not need.

## Accounts and privilege

Inventory local accounts, service identities, login shells, sudo policy, SSH access, and dormant accounts. Prefer named administrative users over shared accounts so actions remain attributable.

Avoid granting broad passwordless sudo access unless the workflow truly requires it. Narrow command delegation is better than making every operator equivalent to root.

## Filesystem permissions

Review ownership and write permissions on:

- service configuration;
- startup files;
- scheduled-task definitions;
- SSH configuration and keys;
- secrets;
- application directories;
- log destinations;
- backup paths.

World-writable paths in privileged workflows deserve particular attention.

## Services

For each listening service, document owner, purpose, bind address, authentication, data handled, and update mechanism. Disable unnecessary services rather than trying to harden software the host does not need.

## SSH hardening

Prefer modern key-based authentication, restrict administrative access, review authorized keys, protect host keys, and log sign-ins. Whether password authentication is appropriate depends on environment and compensating controls, but internet-facing administration requires especially strong controls.

## Software updates

Know which repositories the host trusts. Use supported distributions and security updates. For critical production systems, pair updates with inventory, testing, rollback plans, and maintenance windows.

## Mandatory access control

SELinux and AppArmor can constrain processes beyond normal file permissions. Do not disable them merely because a policy blocks an application; determine whether the application or policy should change.

## Linux capabilities

Capabilities split some traditional root powers into smaller privileges. Review unusual file and process capabilities. Grant only what a service requires.

## Containers do not replace host hardening

Container isolation still relies on the host kernel. Protect the host, container runtime socket, image supply chain, runtime permissions, and orchestration credentials.

## Logging and time

Central logs need consistent timestamps. Synchronize time, protect logging configuration, and retain security events according to operational and legal requirements.

## Integrity monitoring

File hashes can detect change but do not explain whether it was authorized. Combine integrity data with package manager records, deployment logs, configuration management, and administrator change history.

## Backups

Protect backups from the same credentials used to administer production. Test restore procedures and define recovery objectives.

## Safe review commands

On systems you administer, benign checks may include identifying listeners, disk usage, processes, package status, service status, and permission metadata. Record outputs as evidence rather than making immediate changes you cannot reverse.

## Hardening checklist

- Supported OS release.
- Security updates current.
- Minimal packages/services.
- Unique named accounts.
- Least-privilege sudo.
- SSH keys reviewed.
- Secrets protected.
- Firewall rules justified.
- Mandatory access control enabled where supported.
- Time synchronization working.
- Central logging present.
- Backups isolated and restored in tests.
- Configuration drift monitored.

## Authorized lab

Create a disposable Linux VM or container host. Establish a baseline of accounts, services, listening ports, packages, and key configuration. Disable one unnecessary service, tighten one file permission, and add one logging control. Re-run the baseline and document exactly what changed.

**Learning goal:** hardening should produce measurable, explainable state changes.

## Linux hardening in more depth

Start with the smallest required service set. Every daemon, package, account, scheduled task, network listener, and privileged helper adds maintenance responsibility. A hardened system is one whose purpose is understood and whose unnecessary capabilities have been removed.

### Accounts and privilege

Disable or remove stale accounts, use groups deliberately, restrict sudo rules, avoid shared administrator credentials, and prefer logged privileged elevation over persistent root sessions. Service accounts should not have interactive shells unless required.

### Services and network exposure

Inventory listeners, map each one to a package/process/owner, and decide which interface it should bind to. A host firewall should reflect intended service exposure, but application authentication and authorization are still required.

### Filesystem and secrets

Protect SSH keys, service credentials, environment/config files, backups, and logs. World-writable paths and unsafe temporary-file handling deserve attention. Mount options and mandatory-access-control systems such as SELinux/AppArmor can provide additional containment where supported and correctly configured.

### Updates and reboot reality

Patch management includes knowing when an update actually becomes active. Kernel, library, service, and container updates can require restart/reboot/redeployment. Track support lifecycle and test recovery before making risky production changes.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 01, 06, and Linux/Termux basics.

### Practice task

Harden a Linux test system you own: users, sudo, SSH policy, services, permissions, updates, firewall, logs, and backups. Capture before/after evidence.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **23, 47, 48, 49**.

---

# Threat Intelligence and OSINT

> **Purpose:** Collect and evaluate public information ethically, transform it into defensible intelligence, and avoid confusing search results with verified facts.

## Intelligence versus information

Information is collected data. Intelligence is information that has been evaluated in context and supports a decision.

A useful intelligence product answers:

- What happened or may happen?
- What evidence supports that conclusion?
- How confident are we?
- Why does it matter to this organization?
- What action should follow?

## Intelligence cycle

1. Direction and requirements.
2. Collection.
3. Processing.
4. Analysis.
5. Dissemination.
6. Feedback.

Without a collection requirement, analysts can spend hours gathering interesting but irrelevant data.

## OSINT scope

Open-source intelligence uses lawfully available public or authorized information. Publicly reachable does not automatically mean appropriate to collect, retain, republish, or correlate. Respect privacy, platform terms, intellectual property, and local law.

## Source evaluation

For each claim, track:

- original source versus repost;
- publication date and event date;
- author or organization;
- direct evidence versus inference;
- independent corroboration;
- potential bias or incentive;
- confidence.

Screenshots are useful evidence but can lose context. Preserve source metadata and timestamps where appropriate.

## Threat intelligence layers

**Strategic:** business-level trends and risk decisions.
**Operational:** campaigns, infrastructure, and adversary objectives.
**Tactical:** behaviors, techniques, and detection opportunities.
**Technical:** artifacts such as hashes, domains, addresses, or signatures.

Technical indicators often expire quickly; behavior-focused detections can be more durable.

## ATT&CK as a knowledge base

MITRE ATT&CK organizes observed adversary behaviors into tactics and techniques. Use it to communicate behaviors and identify detection/control gaps. Do not treat ATT&CK coverage percentages as proof of security.

## Indicators of compromise

An IOC without context can produce noise. Record:

- what it represents;
- first/last seen when known;
- source confidence;
- expected false positives;
- scope of use;
- expiration/review date.

## Vulnerability intelligence

A CVSS score describes severity, not your complete remediation priority. Consider exposure, exploitability, asset importance, compensating controls, and evidence of exploitation. CISA's Known Exploited Vulnerabilities catalog is one source of confirmed in-the-wild exploitation context.

## Domain and infrastructure research

Defensive OSINT may use DNS records, certificate-transparency data, registrar information, official company records, and public web metadata to understand assets you own or threats you are investigating. Avoid doxxing individuals or turning public fragments into invasive profiles unrelated to a legitimate security purpose.

## Social-media verification

Check original upload, timestamp, location claims, edits, and cross-source corroboration. Viral repetition is not independent confirmation.

## Intelligence writing

Separate **facts**, **assessments**, and **unknowns**. Use confidence terms consistently. A strong report can say “we do not know” and specify what evidence would change the assessment.

## Safe OSINT lab

Choose your own public project or a fictional organization. Build an asset-information table using only official/public sources:

- official domains;
- public code repositories;
- public contact/security policy;
- published technologies only where responsibly observable;
- certificate transparency for owned domains;
- public vulnerability disclosures.

Do not collect personal data unrelated to the exercise.

**Learning goal:** produce a concise intelligence note with source quality and confidence, not a pile of links.

## Primary references

- MITRE ATT&CK: https://attack.mitre.org/
- CISA KEV: https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- CVE Program: https://www.cve.org/
- NVD: https://nvd.nist.gov/

## Intelligence quality and analysis

OSINT becomes intelligence only when it answers a defined question. Begin with a requirement such as “What infrastructure and behaviors were publicly attributed to campaign X during a defined historical period?” Then collect sources that directly help answer it.

### Source grading

Separate source reliability from information credibility. A reliable publisher can still repeat an unverified claim; an unfamiliar source can sometimes provide primary evidence. Record publication date, event date, whether the source is primary/secondary, whether multiple independent sources corroborate the claim, and what uncertainty remains.

### Indicators versus behaviors

IP addresses, domains, hashes, and filenames can be useful but age quickly and may be shared/reassigned. Behavior and technique descriptions can remain useful longer. When mapping to ATT&CK, only map what the evidence actually supports and avoid inflating confidence to fill a matrix.

### Privacy boundary

Do not turn intelligence work into personal surveillance. Public data should be collected proportionately, and private accounts/access controls must not be bypassed. Remove unnecessary personal identifiers from reports and distinguish public-interest/security context from curiosity.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 01, 02, and ethics/privacy.

### Practice task

Write an intelligence requirement for a historical public incident, collect only public non-sensitive sources, grade source confidence, create a timeline, and state uncertainty.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **23, 37, 43, 57**.

---

# Email, DNS and Domain Security

> **Purpose:** Understand the controls that protect organizational domains, email identity, and name resolution.

## Why domains are security-critical

A domain name is often connected to websites, email, SSO, password resets, APIs, documentation, and public trust. Losing registrar or DNS control can undermine multiple security layers simultaneously.

## Registrar security

Protect registrar accounts with strong MFA, limited administrators, recovery controls, and change notifications. Record who owns the account and how emergency recovery works.

Use registry/registrar locking features where appropriate for high-value domains. Review nameserver changes as security events.

## DNS fundamentals

Important record types include:

- A / AAAA — addresses;
- CNAME — alias;
- MX — mail exchanger;
- TXT — policy/verification data;
- NS — authoritative nameservers;
- CAA — certificate-authority authorization;
- DS/DNSKEY and related records — DNSSEC.

DNS configuration is infrastructure-as-code in many organizations and deserves peer review and history.

## DNSSEC

DNSSEC provides authenticity/integrity for signed DNS data. It does not encrypt DNS queries and does not make a malicious domain trustworthy. Deployment requires careful key and delegation management.

## Email authentication

SPF, DKIM, and DMARC solve different parts of mail authentication.

- **SPF** identifies permitted sending infrastructure for a domain.
- **DKIM** cryptographically signs selected message content/headers with a domain-associated key.
- **DMARC** defines alignment and policy using SPF/DKIM results and can provide reporting.

A correct deployment requires inventory of legitimate senders. Jumping directly to strict rejection without understanding third-party mail flows can break valid mail.

## MTA-STS and TLS reporting

Organizations can add controls that improve transport-security expectations for email between supporting mail systems. Treat these as part of a broader mail-security program, not a substitute for user authentication or phishing defenses.

## Certificate management

Inventory certificates, owners, domains/SANs, expiry, private-key location, issuer, and renewal mechanism. Automated renewal is helpful only if failure is monitored.

CAA can restrict which certificate authorities are authorized to issue for a domain, but operational processes still matter.

## Subdomain lifecycle

Abandoned SaaS mappings and forgotten DNS records can create takeover risk. When retiring a service, remove or repoint DNS records as part of the same change.

## Defensive domain monitoring

Monitor your own domains for unexpected:

- nameserver changes;
- MX changes;
- certificate issuance;
- new subdomains in authorized asset inventories;
- DMARC authentication failures;
- registrar-account changes.

## Phishing defense

Technical email authentication reduces some spoofing but not lookalike domains, compromised legitimate accounts, or convincing social engineering. Combine controls with MFA, secure recovery, user reporting, mail filtering, and incident response.

## Safe lab

Use a domain you own or a reserved/example domain for tabletop work. Design a DNS/email security plan containing:

- registrar MFA and recovery;
- nameservers;
- SPF sender inventory;
- DKIM key ownership/rotation;
- DMARC rollout stages;
- certificate inventory;
- subdomain retirement procedure;
- alerting.

**Learning goal:** understand domain control as part of identity and business continuity.

## Domain and email defense in more depth

Domain control is an identity dependency. A compromise at the registrar, DNS provider, mailbox administrator, or recovery account can undermine otherwise strong application security.

### Registrar and DNS control plane

Use strong MFA/passkeys where available, restrict administrative accounts, protect recovery methods, enable change notifications, and document who can modify nameservers or critical records. DNS changes should be auditable and recoverable.

### SPF, DKIM and DMARC

SPF describes authorized sending infrastructure for envelope sender domains; DKIM cryptographically signs selected message content/headers; DMARC evaluates alignment and policy for the visible From domain. These controls complement rather than replace mailbox security, phishing-resistant authentication, content filtering, and user verification processes.

### Mail transport and mailbox security

TLS can protect mail transport hops but does not guarantee sender legitimacy. Protect administrative interfaces and mailbox accounts, review forwarding/delegation rules, monitor suspicious sign-ins, and have a process for revoking sessions and rotating credentials after compromise.

### Domain lifecycle

Track certificate expiration, DNSSEC where used, registrar renewal, stale subdomains, abandoned SaaS mappings, and third-party verification records. Decommissioning is a security operation: remove DNS entries, tokens, certificates, OAuth grants, and vendor access deliberately.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 20 and 51.

### Practice task

For a domain you own or a fictional zone, map DNS/email controls conceptually: SPF, DKIM, DMARC, MX, TLS, account protection, logging, and incident response. Explain what each control does not solve.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **39, 44, 49, 51**.

---

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

---

# Digital Forensics and Evidence Handling

> **Purpose:** Preserve and analyze digital evidence with integrity, repeatability, and clear separation between observation and interpretation.

## Forensics principles

Digital forensics asks what can be supported by evidence. A technically plausible story is not the same as a proven timeline.

Core principles:

- minimize alteration of source evidence;
- record acquisition method and time;
- hash collected files/images where appropriate;
- maintain chain-of-custody records when required;
- work from copies when possible;
- document tools and versions;
- preserve timezone context;
- separate facts from inference.

## Order of volatility

Some evidence disappears quickly: memory, active connections, running processes, temporary data. Other evidence is relatively persistent. An incident-response collection plan should prioritize volatile evidence when doing so is safe and authorized.

Do not improvise destructive acquisition steps on a critical system. Business continuity and legal requirements may override textbook collection order.

## Timestamps

Files and logs can contain creation, modification, access, metadata-change, event, ingestion, or cloud-generated timestamps. They may use different timezones and clocks.

Normalize timelines carefully and retain the original timestamp plus source timezone when possible.

## Hashes

Cryptographic hashes are useful for proving that an evidence file has not changed between collection and later analysis. Record algorithm, value, filename, collector, and time.

## Logs as evidence

A single log source rarely tells the full story. Correlate endpoint, identity, application, network, cloud, and security-product events when available.

Absence of a log entry is not automatically proof that an action did not occur. Logging may have been disabled, filtered, delayed, or never designed to capture that event.

## Mobile evidence

Mobile devices add encryption, app sandboxing, cloud synchronization, lock state, and privacy constraints. Use established forensic procedures and lawful authority where applicable. This guide does not cover bypassing device locks or extracting third-party private data.

## Cloud evidence

Cloud platforms may provide audit logs, snapshots, object versions, identity histories, and control-plane events. Preserve relevant logs quickly because retention windows can be short or configurable.

## File metadata

Metadata can support an investigation but should be corroborated. File names, EXIF fields, author strings, and timestamps can be copied or edited.

## Evidence notes

A defensible entry contains:

```text
Evidence ID:
Source:
Collector:
Acquisition time:
Original path/resource:
Hash:
Tool/version:
Actions performed:
Observations:
Interpretation:
Limitations:
```

## Root-cause caution

The earliest event you found is not necessarily the initial cause. State “earliest observed evidence” when that is what the data supports.

## Safe lab — Synthetic timeline

Create three local text logs with UTC, local time, and offset timestamps. Include a login, file creation, configuration change, and logout. Normalize them to UTC, sort them, and label each event with source and confidence.

Then alter one copied log and show that its SHA-256 no longer matches the recorded value.

**Learning goal:** practice evidence integrity and timeline reasoning without private data.

## Reporting

A forensic report should allow another qualified analyst to understand what you collected, what you did, what you observed, and where uncertainty remains.

## Forensic reasoning in more depth

Forensics is not merely collecting files. It is preserving evidence, understanding provenance, reconstructing events, and communicating confidence.

### Provenance

For each artifact record where it came from, how it was acquired, by whom, when, with which tool/version, and whether acquisition changed the source. Hashes help demonstrate that a collected artifact has not changed after acquisition, but they do not prove the artifact was truthful or complete.

### Time

Timelines fail when analysts ignore timezone, clock drift, timestamp semantics, log ingestion delay, and differing event sources. Normalize timestamps while retaining original values. Treat “created,” “modified,” “observed,” and “ingested” as different concepts.

### Fact versus inference

Write “the log records account X authenticating at time Y” separately from “this likely indicates the attacker used account X.” The first may be evidence; the second is an interpretation that needs corroboration.

### Scope and minimization

Acquire only what is justified by the investigation and authorization. Protect sensitive case data, use access controls, maintain chain-of-custody requirements where relevant, and define retention/disposal after closure.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 23 and filesystem basics.

### Practice task

Create synthetic evidence files, hash them, preserve originals, normalize timestamps, build a timeline, and write which conclusions are fact versus inference.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **38, 48, 57**.

---

# Ransomware Resilience and Recovery

> **Purpose:** Prepare organizations to prevent, contain, recover from, and learn from ransomware incidents without relying on ransom payment as a recovery strategy.

## Ransomware is an operational crisis

Modern ransomware incidents may involve data theft, credential compromise, service disruption, and extortion in addition to file encryption. Recovery planning therefore spans identity, endpoints, networks, backups, legal/privacy obligations, communications, and business continuity.

## Prevention layers

High-value controls include:

- strong identity and phishing-resistant MFA;
- privileged-access separation;
- supported and patched systems;
- exposure reduction;
- endpoint detection and response;
- application control where feasible;
- segmentation;
- secure remote administration;
- tested backups;
- centralized logging;
- security awareness and reporting paths.

No single product is a ransomware control.

## Backup architecture

A resilient backup strategy considers:

- multiple copies;
- separate failure domains;
- offline or logically isolated copies;
- immutable/object-locked copies where appropriate;
- protected backup-admin credentials;
- monitored backup deletion/configuration changes;
- regular restore tests.

Recovery objectives should be defined before an incident: **RPO** describes acceptable data loss in time; **RTO** describes acceptable restoration time.

## Identity recovery

If directory or SSO systems are compromised, restoring servers without restoring trusted identity can recreate the incident. Maintain protected recovery accounts, procedures, keys, and documentation.

## Initial response priorities

During a suspected ransomware event:

1. activate the incident process;
2. protect life/safety and critical operations;
3. preserve evidence appropriate to the case;
4. contain affected identities/endpoints/network paths;
5. determine business impact;
6. protect backups and recovery infrastructure;
7. engage legal, privacy, insurance, law enforcement, or regulators as required;
8. communicate through trusted channels.

Do not rush to wipe systems before understanding scope and preserving necessary evidence.

## Recovery sequencing

Restore dependencies in a known order. Identity, DNS, network services, virtualization, databases, and business applications may depend on one another.

Define “minimum viable business service” for critical operations rather than trying to restore everything simultaneously.

## Clean recovery

Rebuilding from known-good sources is often safer than trusting a heavily compromised system after superficial cleanup. Validate:

- operating system/image provenance;
- patches;
- credentials/keys;
- persistence mechanisms removed;
- configuration baselines;
- logging/EDR functioning;
- application data integrity.

## Communications

Prepare internal and external communication templates before an incident. Avoid speculation. Maintain a single source of truth and clearly mark verified facts, current impact, actions, and next update point.

## Payment considerations

Ransom payment can involve legal, sanctions, fraud, ethics, and operational risks and does not guarantee recovery or deletion of stolen data. Decisions require executive and legal involvement; prevention and recoverability should not depend on payment.

## Tabletop exercise

Scenario: file shares become unavailable and an endpoint alert indicates suspicious mass file changes. Build a two-hour response timeline covering:

- who declares an incident;
- who can isolate systems;
- backup protection;
- evidence capture;
- executive communications;
- customer/regulatory assessment;
- restore priorities;
- criteria for returning systems to service.

**Learning goal:** expose decision and dependency gaps before a real crisis.

## Primary reference

- NIST ransomware and CSF resources: https://www.nist.gov/cyberframework
- CISA StopRansomware: https://www.cisa.gov/stopransomware

## Ransomware resilience in more depth

Ransomware is a business-recovery problem as much as a malware problem. Resilience depends on identity, segmentation, endpoint controls, backups, monitoring, vendor dependencies, communications, and practiced recovery.

### Identity containment

Plan how to revoke sessions, disable/rotate privileged credentials, protect identity infrastructure, and establish clean administrative access. If identity is compromised, rebuilding endpoints without recovering trust in accounts/tokens can lead to reinfection or renewed access.

### Backup architecture

Maintain multiple copies with appropriate isolation/immutability, protect backup administration separately, monitor deletion/tampering, and test restores. A backup whose credentials are reachable from a compromised administrator account may not provide meaningful resilience.

### Recovery order

Define dependencies: identity/DNS/networking, management, databases/storage, applications, endpoints, and external integrations. Restoration must use known-good images/configuration and address the root cause before reconnecting systems broadly.

### Tabletop realism

Include legal/regulatory/comms decisions, third-party support, hardware capacity, clean-room access, forensic preservation, and business workaround processes. Record actual gaps discovered during the exercise and assign owners/dates.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 23, 37, and 48.

### Practice task

Run a ransomware tabletop with fictional systems. Identify identity containment, backup isolation, clean recovery, communications, evidence needs, and business priorities.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **42, 47, 48, 59**.

---

# OAuth, OIDC, Passkeys and Modern Authentication

> **Purpose:** Understand modern authentication and authorization protocols well enough to design, review, and troubleshoot secure identity flows.

## Authentication versus authorization

- **Authentication** establishes an identity or authenticator relationship.
- **Authorization** decides whether an identity/client can perform an action.
- **Federation** allows one security domain to rely on identity assertions from another.

OAuth 2.x is primarily an authorization framework. OpenID Connect adds an identity layer. Treating an OAuth access token and an OIDC ID token as interchangeable is a common design error.

## Core actors

OAuth terminology includes:

- resource owner;
- client;
- authorization server;
- resource server.

OIDC adds identity concepts such as the ID token and user information.

## Redirect URIs

Redirect URI handling is a major trust boundary. Register exact, minimal redirect destinations and avoid permissive wildcard patterns when possible. The authorization server must not send sensitive authorization results to attacker-controlled locations.

## State, nonce, and PKCE

These mechanisms solve different problems. Designs should use protocol-recommended protections rather than inventing custom request correlation.

PKCE binds authorization requests to the client instance that initiated them and is particularly important for public clients.

## Token handling

Access tokens are bearer credentials unless a sender-constrained design is used. Minimize exposure:

- do not place tokens in logs;
- use TLS;
- use short lifetimes appropriate to risk;
- scope tokens narrowly;
- rotate/revoke refresh tokens as supported;
- validate issuer, audience, expiry, signature, and relevant claims.

## Session versus token

A browser application can use a server-side session even when the backend uses OAuth. “JWT everywhere” is not inherently more secure. Choose the simplest model that satisfies trust boundaries and operational needs.

## MFA

MFA strength depends on authenticator properties and resistance to phishing/replay, not merely the number of screens shown. NIST SP 800-63 Revision 4 provides current digital identity and authenticator guidance.

## Passkeys

Passkeys are based on FIDO/WebAuthn public-key credentials and can provide strong phishing resistance. The private key remains bound to an authenticator ecosystem rather than being sent to the relying party.

Account recovery remains critical. A strong login method can be undermined by a weak recovery flow.

## Federation risks

Review:

- identity-provider trust;
- client registration;
- signing keys;
- key rotation;
- audience restrictions;
- tenant boundaries;
- logout/session revocation;
- account linking;
- deprovisioning.

## Service-to-service identity

Machine identities require lifecycle management too. Avoid permanent shared API keys where short-lived workload identities or managed credentials are available.

## Safe design lab

Draw an OIDC authorization-code flow for a fictional web app. Mark:

1. browser;
2. application backend;
3. identity provider;
4. redirect URI;
5. authorization code;
6. PKCE verifier/challenge;
7. ID token;
8. access token;
9. session cookie.

For each artifact, state who may see it, where it is stored, and how long it is valid.

**Learning goal:** security improves when token purpose and trust boundaries are explicit.

## Primary references

- NIST SP 800-63-4: https://csrc.nist.gov/pubs/sp/800/63/4/final
- WebAuthn: https://www.w3.org/TR/webauthn-3/
- FIDO Alliance passkeys: https://fidoalliance.org/passkeys/

## Modern authentication in more depth

OAuth 2.x is primarily an authorization framework; OpenID Connect adds an identity layer. Treat access tokens, refresh tokens, ID tokens, sessions, cookies, passkeys, and recovery credentials as different objects with different audiences and lifecycles.

### Redirect and client trust

Redirect URI handling, client type, PKCE, state/nonce, issuer validation, audience validation, and token storage are core design decisions. Mobile/public clients cannot safely keep a client secret in the same way as a backend confidential client.

### Passkeys

Passkeys use public-key credentials and can provide phishing-resistant authentication. Deployment still requires account recovery, device lifecycle, enrollment security, and policies for high-risk actions. A strong login can be undermined by weak recovery or session management.

### Step-up and transaction authorization

Do not treat one successful login as permanent authorization for every action. High-impact changes may require fresh authentication, stronger factors, explicit user confirmation, or policy checks based on risk.

### Telemetry

Log authenticator enrollment/removal, recovery events, token/session issuance/revocation, unusual sign-ins, administrative identity changes, and high-risk authorization failures without logging secret token contents.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 11, 20, and 21.

### Practice task

Draw an OAuth/OIDC authorization flow for a fictional app, identify client/resource/authorization-server roles, token audience, redirect URI, session boundaries, and passkey recovery assumptions.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **40, 41, 49, 52**.

---

# Secure Coding and OWASP ASVS

> **Purpose:** Convert security expectations into concrete software requirements and verification tests using modern secure-development practices and OWASP ASVS 5.0.

## Secure coding is a system

Secure code depends on architecture, frameworks, dependencies, deployment, secrets, logging, identity, and operational controls. A developer can write memory-safe input handling and still ship an insecure product if authorization is missing.

## ASVS as a requirements catalog

OWASP Application Security Verification Standard (ASVS) 5.0.0 provides application-security requirements that teams can use for architecture, development, procurement, and verification. Use the requirements relevant to the application's risk and context rather than treating ASVS as a checkbox contest.

## Input validation

Define the allowed shape of data by type, length, range, format, encoding, and business rules. Validate on the trusted side of the boundary. Client-side validation improves UX but cannot enforce server security.

## Output handling

Encode data for the destination context: HTML text, HTML attribute, JavaScript, URL, SQL, shell, and other interpreters have different syntax and risks. Prefer frameworks and APIs that provide context-aware escaping or parameterization.

## SQL and data stores

Use parameterized queries or safe ORM patterns. Database authorization should also limit application account privileges; preventing injection is not a reason to run the application as a database superuser.

## Command execution

Avoid invoking shells with user-controlled strings. Prefer direct process APIs and allow-listed operations. Separate data from code.

## Authorization

Implement authorization server-side on every protected action. Test both allowed and denied paths. Object identifiers are references, not authorization decisions.

## Authentication and session management

Use mature identity libraries and standards. Protect session cookies, rotate session identifiers after security-relevant transitions, enforce logout/revocation behavior, and design secure account recovery.

## Error handling

OWASP Top 10:2025 includes mishandling of exceptional conditions as a major risk area. Fail securely, return appropriate client errors, and send detailed diagnostics to protected logs rather than users.

## Secrets

Do not embed production secrets in code, mobile binaries, browser JavaScript, container images, or Git history. Use managed secret storage and rotation. Build processes should fail when required secrets are absent rather than silently using weak defaults.

## File handling

Treat uploaded filenames, metadata, MIME types, archives, and document formats as untrusted. Generate server-side storage names, enforce size/type policies, isolate processing, and prevent path traversal.

## Deserialization and parsers

Prefer simple data formats with strict schemas. Avoid unsafe object deserialization from untrusted sources. Keep parsers updated because complex file formats and protocol implementations carry their own attack surface.

## Logging requirements

Applications should log security-significant events with actor, action, target, outcome, and timestamp while excluding passwords, tokens, payment data, and unnecessary personal information.

## Dependency security

Track direct and transitive dependencies. Use lockfiles, SBOMs where appropriate, trusted registries, provenance/signing capabilities, and vulnerability monitoring. Remove abandoned dependencies rather than carrying them indefinitely.

## Security tests

Include:

- unit tests for validation and authorization;
- integration tests for identity/session behavior;
- negative tests;
- dependency and secret scans;
- static/dynamic analysis where useful;
- infrastructure/configuration checks;
- regression tests for fixed vulnerabilities.

## Code review questions

- What data crosses a trust boundary?
- Where is authorization enforced?
- What happens on malformed/unexpected state?
- Could a secret reach logs?
- Does this introduce a new dependency?
- Is concurrency/race behavior safe?
- What happens when the downstream service fails?
- Is there a secure default?

## Lab — Security requirement to test

Choose five ASVS requirements relevant to a toy local web app. For each, write:

1. requirement;
2. implementation location;
3. positive test;
4. negative test;
5. evidence;
6. owner.

**Learning goal:** transform broad security advice into verifiable engineering work.

## Primary reference

- OWASP ASVS 5.0: https://owasp.org/www-project-application-security-verification-standard/

## Secure coding program guidance

Secure coding works best when security requirements are part of normal development rather than a late penetration-test gate.

### Requirements to tests

Convert statements such as “users may only access their own invoices” into automated positive and negative tests. Security requirements should be reviewable, testable, and attached to the code paths that enforce them.

### Trust-boundary validation

Validate at the boundary where untrusted data becomes trusted structure. Use schema/type/length/range validation and context-appropriate output encoding. Avoid copying sanitization functions between contexts where their assumptions differ.

### Dependencies and build

Review dependency provenance, update policy, transitive risk, build identities, artifact signing/provenance where available, and secret access in CI/CD. A secure source file can still produce an unsafe product through a compromised build/dependency path.

### Error and state handling

Define safe behavior for duplicate requests, retries, timeouts, partial failure, invalid state transitions, and dependency outages. Unexpected conditions should fail safely and leave enough audit information to investigate.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 14, 22, and basic development.

### Practice task

Choose a small application you own. Define five security requirements, map them to ASVS-style verification ideas, add negative tests, fix one issue, and retain evidence of the regression test.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **41, 52, 53**.

---

# Threat Modeling and Security Architecture

> **Purpose:** Find security problems while systems are still diagrams and requirements, when fixes are cheaper and less disruptive.

## Start with the system

Threat modeling requires a useful model of what exists:

- users and roles;
- services/components;
- data stores;
- external dependencies;
- trust boundaries;
- data flows;
- administrative paths;
- secrets/keys;
- deployment environments.

A threat model with no architecture model is mostly guessing.

## Assets and security objectives

List what must be protected and why. Examples:

- account integrity;
- customer confidentiality;
- service availability;
- transaction correctness;
- signing keys;
- audit evidence;
- administrative control.

Different assets can require different controls.

## Trust boundaries

Mark every point where data or authority crosses between different trust assumptions: internet to edge, browser to API, workload to database, tenant to tenant, CI to production, employee device to admin plane, model output to tool execution.

## STRIDE

STRIDE is one useful prompt set:

- Spoofing
- Tampering
- Repudiation
- Information disclosure
- Denial of service
- Elevation of privilege

It is a brainstorming aid, not a proof that every threat was found.

## Abuse cases

Ask how a legitimate feature could be misused. Examples:

- password reset used to take over accounts;
- export function used for bulk data theft;
- invitation workflow used to cross tenant boundaries;
- AI tool integration used to perform an action without adequate approval.

## Security architecture patterns

Common patterns include:

- centralized identity with strong authorization at services;
- least-privilege service identities;
- segmented administrative planes;
- secure defaults;
- explicit tenant isolation;
- defense in depth;
- immutable deployment artifacts;
- short-lived credentials;
- centralized audit trails;
- fail-safe behavior.

## Failure modes

Model not only malicious input but also failures:

- dependency timeout;
- message duplication;
- partial transaction;
- stale authorization data;
- clock skew;
- key rotation failure;
- storage exhaustion;
- malformed parser input;
- unavailable identity provider.

Security incidents frequently emerge from exceptional conditions and unsafe recovery behavior.

## Prioritization

For each threat, capture:

```text
Threat:
Asset:
Preconditions:
Impact:
Existing controls:
Residual risk:
Decision:
Owner:
Verification:
```

Do not multiply arbitrary numbers merely to create false precision.

## Architecture decision records

Record security-relevant design decisions and alternatives. Future engineers should know why a boundary or control exists before removing it.

## AI systems

Add model providers, retrieval stores, system prompts, tool calls, user content, output consumers, and human approvals to the architecture. Treat model output as untrusted data when it influences code, queries, or actions.

## Supply chain

Model build systems and dependency registries as part of production. An attacker who changes the artifact before deployment may never need to attack the running service directly.

## Lab — Threat model a notes app

Model a fictional multi-user notes application with browser, API, database, object storage, email provider, and CI/CD pipeline. Identify at least ten threats across identity, authorization, data handling, availability, supply chain, and operations. Select controls and define one verification test for each high-priority threat.

**Learning goal:** make security requirements emerge from architecture rather than from a generic checklist.

## Threat-modeling depth

A threat model is a living explanation of how a system can fail securely or insecurely. Begin with architecture rather than threat names.

### Build the model

Document users/services, assets, data stores, external dependencies, entry points, trust boundaries, privilege levels, and important data flows. Mark where identity changes, where data becomes executable/parsed, and where privileged actions occur.

### Abuse cases

For each important action ask how an unauthorized user, compromised service, malicious dependency, operator mistake, outage, or replay could cause harm. Include privacy and availability abuse cases, not only confidentiality breaches.

### Mitigation quality

A mitigation should name the control owner, enforcement point, evidence, failure mode, and residual risk. “Use encryption” is incomplete unless the model states where keys live, who authenticates whom, and what happens when keys rotate or are lost.

### Review triggers

Update threat models when authentication changes, new integrations/tools are added, trust boundaries move, data sensitivity changes, a major incident occurs, or deployment architecture changes.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 01, 21, 22.

### Practice task

Threat-model a small system: assets, data flows, trust boundaries, identities, dependencies, abuse cases, mitigations, assumptions, and residual risk. Review it after one architecture change.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **42, 46, 54**.

---

# Governance, Risk, Compliance and Privacy

> **Purpose:** Connect technical security work to ownership, business risk, policy, privacy, assurance, and measurable outcomes.

## Governance

Governance defines who makes cybersecurity decisions, who owns risk, how priorities are set, and how accountability is demonstrated. NIST CSF 2.0 explicitly includes **Govern** alongside Identify, Protect, Detect, Respond, and Recover.

Technical teams need clear policy owners and exception processes. “Security says no” is not a governance model.

## Risk

A practical risk statement describes:

- asset/process;
- threat/event;
- weakness or exposure;
- business impact;
- likelihood/context;
- existing controls;
- owner;
- treatment decision.

Risk treatment options generally include mitigate, avoid, transfer/share, or accept. Acceptance should be explicit, time-bounded where appropriate, and owned at the right level.

## Asset and data classification

You cannot protect everything identically. Define classes for business information and systems, then map handling requirements such as encryption, access, retention, backup, and sharing.

## Policies, standards, procedures, guidelines

- **Policy:** management intent and mandatory direction.
- **Standard:** specific mandatory requirements.
- **Procedure:** steps to perform an activity.
- **Guideline:** recommended practice.

Keep them distinguishable so audits and operators know what is required.

## Control frameworks

Frameworks organize outcomes and controls, but implementation must match business context. Examples include NIST CSF, NIST SP 800-53, ISO/IEC 27001 ecosystems, CIS Controls, and sector-specific requirements.

Compliance is evidence that defined requirements were met at a point or period in time; it is not proof that an organization cannot be compromised.

## Privacy engineering

Privacy involves more than confidentiality. Ask:

- Why is personal data collected?
- Is the amount proportionate?
- Who can use it?
- How long is it retained?
- Where is it transferred?
- Can inaccurate data be corrected?
- Can unnecessary data be deleted?
- What happens during an incident?

Data minimization reduces both privacy risk and breach impact.

## Third-party risk

Vendors can become identity providers, data processors, code suppliers, remote administrators, or operational dependencies. Due diligence should match the service's access and criticality.

Track contract/security requirements, data flows, subprocessors, breach notification obligations, access methods, and exit/termination processes.

## Exceptions

Security exceptions should record:

```text
Requirement:
Reason:
Scope:
Compensating controls:
Risk owner:
Approval:
Expiry/review date:
Remediation plan:
```

Permanent undocumented exceptions become hidden architecture.

## Metrics

Useful metrics connect to outcomes, for example:

- percentage of critical assets with known owners;
- MFA coverage for privileged accounts;
- restore-test success rate;
- median time to revoke departing-user access;
- high-risk findings past SLA;
- detection rules with recent validation;
- unsupported systems remaining.

Avoid vanity metrics such as raw alert volume without quality context.

## Risk register lab

Create five fictional risks for a small SaaS company. Assign owner, business impact, current controls, treatment, target date, and measurable residual-risk indicator. Include one accepted risk and justify why acceptance is reasonable.

**Learning goal:** translate technical observations into accountable business decisions.

## Primary reference

- NIST CSF 2.0: https://www.nist.gov/cyberframework

## Governance and risk depth

Governance defines who makes cybersecurity decisions, based on what evidence, with which accountability. Risk management connects technical conditions to objectives and treatment decisions.

### Risk statement structure

A useful risk statement describes a cause/threat, affected asset/process, unwanted event, and impact. Record existing controls, evidence, likelihood/context, impact, owner, treatment, due date, and residual risk.

### Treatment choices

Risks may be reduced, avoided, transferred/shared, or accepted according to governance. “Accepted” should mean a responsible owner understands the residual risk and review/expiration conditions—not that a ticket was closed without remediation.

### Control evidence

Policies are not proof of implementation. Evidence can include configuration, logs, tests, access reviews, restore exercises, training records, vulnerability verification, or independent assessment. Define how frequently evidence must be refreshed.

### Privacy integration

Security and privacy overlap but are not identical. Data minimization, purpose limitation, user transparency, retention, and lawful/organizational requirements should be considered alongside confidentiality/integrity/availability controls.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Module 01 and basic organizational context.

### Practice task

Create a small risk register for a fictional organization, link each risk to owner, controls, evidence, treatment, review date, privacy impact, and residual risk.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **43, 45, 59**.

---

# Responsible Disclosure and Bug Bounty Ethics

> **Purpose:** Learn how to report vulnerabilities safely and professionally while respecting authorization boundaries.

## Authorization first

A public website, IP address, mobile app, or API is not automatically permission to test. Authorization comes from ownership, a contract, a written testing agreement, or a published vulnerability disclosure/bug bounty policy whose scope includes the system and technique.

Read the policy before testing.

## Scope

A good program defines:

- in-scope domains/apps/APIs;
- out-of-scope systems;
- allowed techniques;
- prohibited impact;
- rate limits;
- data handling rules;
- test account requirements;
- reporting channel;
- disclosure timeline;
- reward eligibility if applicable.

When scope is ambiguous, do not expand it yourself.

## Minimize impact

Prove a vulnerability with the least invasive evidence. Do not access additional records merely to demonstrate that more records might be accessible. Use your own accounts and synthetic data whenever possible.

Do not persist, pivot, disrupt, delete, alter unrelated data, or collect credentials beyond what is necessary for an authorized proof.

## Stop conditions

Stop and report when you encounter:

- real user personal data beyond minimal proof;
- credentials/secrets belonging to others;
- production instability;
- an out-of-scope asset;
- evidence of an unrelated active compromise;
- a technique explicitly prohibited by policy.

## High-quality report

A report should include:

1. concise title;
2. affected asset/version;
3. authorization/scope context;
4. preconditions;
5. reproducible minimal steps;
6. expected versus actual behavior;
7. impact in realistic terms;
8. minimal redacted evidence;
9. remediation idea;
10. retest notes when fixed.

Avoid inflated severity and dramatic language. Clear evidence is more persuasive.

## Duplicate and known issues

Programs may already know about a finding. Maintain your own notes so you can explain what you tested and when. Do not attempt to make a duplicate “more serious” by increasing impact.

## Disclosure

Coordinated vulnerability disclosure balances user protection, vendor remediation, researcher credit, and public interest. Follow program terms and applicable law. If no policy exists, use a vendor security contact or recognized coordination channel and minimize further testing.

## Data retention

Delete collected test data when the program requires it and keep only the evidence necessary for the report. Protect reports because they may contain sensitive details before remediation.

## Safe practice

Use intentionally vulnerable platforms, CTFs, and your own applications to practice reproduction and report writing. The professional skill is demonstrating the flaw safely, not maximizing access.

## Reporting lab

Take a fictional broken-access-control issue in a toy app. Write a complete report using only User A and User B accounts you created. Include minimal request/response evidence and a server-side authorization recommendation.

**Learning goal:** show impact without harming unrelated users.

## Disclosure workflow in more depth

Responsible disclosure starts with scope. Read the program policy before testing: eligible assets, excluded techniques, rate limits, data handling, safe harbor, disclosure timing, duplicate rules, and contact method.

### Minimize impact

Use the least invasive proof that demonstrates the issue. Avoid accessing more records than necessary, changing other users' data, creating persistence, interrupting services, or collecting credentials. If a safe proof is impossible within scope, report the hypothesis and supporting evidence rather than escalating recklessly.

### Report quality

A strong report contains clear affected asset/version, prerequisites, minimal reproduction in the authorized environment, expected versus actual behavior, evidence, impact, remediation direction, and cleanup. Separate confirmed facts from assumptions.

### Stop and disclose

If testing unexpectedly exposes sensitive data, crosses into an excluded asset, or risks production impact, stop. Preserve minimal evidence, avoid further exploration, and use the program's escalation path.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 15, 26, and legal/authorization concepts.

### Practice task

Write a responsible-disclosure template for a fictional finding: affected scope, reproducible safe evidence, impact, remediation, timeline, and data-handling statement.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **26, 42, 57**.

---

# Endpoint, Browser and SaaS Security

> **Purpose:** Cover the everyday control plane where users, browsers, SaaS applications, extensions, endpoints, and cloud identity intersect.

## Endpoint security

Modern endpoint protection combines platform hardening, patching, disk encryption, device identity, EDR, application controls, browser policy, and least privilege.

A device should have a known owner, supported OS, update state, encryption status, management state, and recovery process.

## Mobile endpoints

Phones hold authenticator apps, passkeys, email, cloud sessions, and recovery channels. Use screen lock, hardware-backed security where available, current updates, remote-lost-device controls, and careful app permissions.

## Browser as an application platform

Browsers store sessions, passwords/passkeys, history, extensions, and enterprise identity. Keep browsers updated and reduce unnecessary extensions.

Extensions can read or modify web content depending on permissions. Review publisher, permissions, update history, necessity, and enterprise allow/deny policy.

## Session theft risk

Strong MFA does not make stolen authenticated sessions harmless. Protect endpoints, use short/appropriate session lifetime, re-authentication for sensitive operations, risk-based controls, and server-side revocation.

## SaaS administration

For each SaaS product, identify:

- business owner;
- technical admin;
- SSO/MFA state;
- local accounts that bypass SSO;
- privileged roles;
- API tokens/integrations;
- audit-log availability;
- data classification;
- sharing defaults;
- guest/external users;
- offboarding procedure;
- backup/export capability.

## OAuth application consent

Third-party integrations can gain long-lived API access even without user passwords. Govern app consent, scopes, publisher trust, review, revocation, and service-account ownership.

## Shadow SaaS

Users often adopt tools before security teams know. Solve this with usable approved alternatives, discovery, procurement workflows, and risk-based review rather than only blocking domains.

## DLP and sharing

Data-loss prevention can reduce accidental exposure but depends on classification and context. Review public links, external collaborators, default sharing, and sensitive exports.

## Endpoint detection

EDR visibility is only valuable when alerts are monitored, exclusions are governed, agents are healthy, and responders can isolate/recover hosts.

## Browser lab

On a test browser profile:

1. list installed extensions;
2. record permissions;
3. remove one unnecessary extension;
4. review saved site permissions;
5. inspect active sessions for a test account;
6. revoke one session and verify logout behavior.

**Learning goal:** understand the browser as part of the identity and endpoint attack surface.

## SaaS inventory lab

Create a fictional ten-app SaaS inventory and classify each by identity integration, data sensitivity, administrator count, external sharing, audit logging, and offboarding maturity. Prioritize three improvements.

## Endpoint, browser and SaaS operational depth

Endpoint security is an ecosystem: OS patching, disk encryption, endpoint protection, browser configuration, extensions, SaaS sessions, OAuth grants, identity recovery, device management, and user behavior interact.

### Browser review

Inventory extensions, remove unused ones, restrict permissions where possible, keep the browser updated, review download/autofill/password behavior, and separate managed/work profiles where policy requires. Browser sync can replicate sensitive state across devices, so account security matters.

### SaaS review

For critical SaaS applications document admins, MFA/passkey posture, external sharing, API tokens, OAuth integrations, dormant accounts, audit logs, retention, backup/export options, and recovery contacts.

### Endpoint loss

A lost encrypted device can still require session/token revocation and account review. Define who can remotely lock/wipe devices, what evidence is available, and how users regain access without weakening recovery security.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 17, 21, and 39.

### Practice task

Audit your own endpoint/browser/SaaS settings: updates, extensions, account MFA/passkeys, session/device inventory, recovery methods, sharing permissions, and admin roles.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **47, 49, 55, 56**.

---

# Capstones, Checklists and Study Roadmaps

> **Purpose:** Turn the handbook into a progression of demonstrable skills instead of a collection of notes.

## How to use this module

Choose a learning path, complete small labs, then complete at least one capstone. Keep all targets local, owned, deliberately vulnerable, or explicitly authorized.

## Beginner roadmap

1. Security fundamentals and networking.
2. Linux/Termux foundations.
3. Python/Git workflow.
4. Web and API concepts.
5. Identity and access control.
6. Vulnerability analysis.
7. Logging/detection basics.
8. Reporting.

Evidence of progress should be projects and explanations, not just tool installation screenshots.

## Blue-team roadmap

Study:

- asset inventory;
- Windows/Linux logging;
- identity telemetry;
- endpoint controls;
- network visibility;
- detection engineering;
- incident response;
- threat hunting;
- forensics;
- ransomware recovery;
- cloud/SaaS logs.

Capstone: build a synthetic incident, generate logs, detect it, investigate it, contain it in the lab, recover, and write lessons learned.

## Application-security roadmap

Study:

- HTTP/TLS;
- authentication/session management;
- authorization;
- input/output handling;
- APIs;
- OAuth/OIDC;
- ASVS;
- secure coding;
- threat modeling;
- software supply chain;
- CI/CD and container security.

Capstone: build a small web app, define security requirements, write negative tests, generate an SBOM, threat model it, fix findings, and produce an assessment report.

## Cloud/DevSecOps roadmap

Study:

- IAM;
- network boundaries;
- secret management;
- infrastructure as code;
- containers/Kubernetes;
- logging;
- software provenance;
- CI/CD identity;
- vulnerability prioritization;
- backup/recovery.

Capstone: deploy a local or authorized sandbox application through a pipeline with policy checks, least-privilege identity, logs, and rollback.

## Termux/mobile roadmap

1. Module 28 — Foundations.
2. Module 29 — Python/Git/automation.
3. Module 30 — Networking/SSH/local services.
4. Module 31 — Lab operations/troubleshooting.
5. Module 36 — Python security automation.
6. Module 27 — Authorized labs.
7. Use `Hacking Guide Project.py` to search and review the full guide offline.

Capstone: create a portable defensive notebook in Termux containing local search, file integrity, synthetic log analysis, and documentation.

## Security assessment checklist

### Before

- Written authorization.
- Scope and exclusions.
- Contacts and escalation.
- Allowed techniques.
- Time windows.
- Data-handling requirements.
- Stop conditions.
- Test accounts.
- Evidence plan.

### During

- Verify target before every action.
- Minimize data access.
- Keep timestamps/notes.
- Preserve important evidence.
- Avoid production impact.
- Report critical safety issues promptly.

### After

- Validate findings.
- Remove test artifacts.
- Protect/delete collected data as required.
- Write remediation-oriented reports.
- Retest fixes.
- Record lessons learned.

## Incident-response checklist

- Confirm and classify.
- Establish incident leadership.
- Preserve evidence proportionately.
- Contain identities/endpoints/services.
- Determine scope.
- Protect recovery systems.
- Eradicate root causes.
- Restore from known-good state.
- Monitor for recurrence.
- Complete lessons learned.

NIST SP 800-61 Rev. 3 integrates incident response across the CSF 2.0 Functions rather than treating response as an isolated activity.

## Secure software release checklist

- Threat model updated.
- Security requirements tested.
- Authorization negative tests passing.
- Secrets scan clean.
- Dependencies/SBOM reviewed.
- High-risk vulnerabilities dispositioned.
- Build provenance/permissions reviewed.
- Production configuration checked.
- Logging/alerts ready.
- Backup/rollback verified.
- Incident owner known.

## Capstone 1 — Defensive home lab

Build a private lab with one Linux host, one Windows host if available, a small application, centralized synthetic logs, and documented users. Demonstrate inventory, hardening, backup, logging, one benign detection test, and recovery.

## Capstone 2 — Secure API

Build a localhost API with authentication, object-level authorization, rate limits, input schema validation, structured logs, and tests. Threat model it and map controls to relevant OWASP API/ASVS requirements.

## Capstone 3 — Digital forensics notebook

Create synthetic evidence from three sources, hash it, normalize timestamps, construct a timeline, distinguish fact from inference, and write a concise incident report.

## Capstone 4 — Threat intelligence brief

Using public non-sensitive sources about a historical campaign, write a two-page brief with intelligence requirements, source grading, ATT&CK mapping, detection ideas, confidence, and limitations. Do not collect private personal information.

## Capstone 5 — Ransomware tabletop

Run a tabletop for a fictional organization. Define roles, backup dependencies, identity recovery, legal/comms decisions, RPO/RTO, clean-room recovery, and evidence requirements.

## Capstone 6 — Termux security companion

Use `Hacking Guide Project.py` plus your own safe local utilities to create a mobile study workspace. Required features:

- offline guide search;
- project notes;
- Git history;
- integrity checker;
- synthetic log parser;
- exportable Markdown report;
- setup/recovery instructions.

## What mastery looks like

You should be able to explain:

- why a control exists;
- what threat it addresses;
- what evidence proves it works;
- what it does not protect against;
- how it fails;
- how to recover;
- how to communicate the residual risk.

That is more valuable than memorizing hundreds of commands.

## Turning roadmaps into a weekly system

A roadmap works only when it produces artifacts and review. Use a weekly loop:

- one concept block;
- one safe lab;
- one written explanation;
- one small automation/configuration improvement;
- one review session using `Hacking Guide Project.py` search;
- one Git commit or organized note that preserves the result.

At the end of each month, choose one old lab and repeat it from your documentation. If you cannot reproduce it, improve the documentation. If the result changes because software changed, record the version difference and update the guide notes.

## Capstone scoring rubric

Score each capstone from 0–2 in these dimensions: scope/ethics, architecture understanding, reproducibility, evidence quality, security reasoning, mitigation quality, retest/recovery, documentation, limitations, and communication. A high score requires not only a working result but evidence that another learner could understand and safely reproduce the process.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Use after completing at least one foundational path.

### Practice task

Choose one capstone and define acceptance criteria before building. Keep a decision log, evidence index, test plan, cleanup plan, and retrospective.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **Repeat with a different specialization**.

---

# Agentic AI, MCP and Tool Security

> **Purpose:** Secure AI systems that can plan, call tools, access data, keep memory, and perform actions on behalf of users.

## Why agents change the threat model

A chatbot that only returns text has a narrower action surface than an agent that can send email, edit files, query business systems, deploy code, or invoke external tools. The model becomes part of an orchestration system with identities, credentials, permissions, memory, tool metadata, and side effects.

OWASP's 2026 agentic-security work emphasizes risks such as goal hijacking, tool misuse, identity and privilege abuse, memory poisoning, insecure inter-agent communication, cascading failures, and rogue behavior. Treat those risks as architecture problems, not merely prompt-writing problems.

## Agent components to model

- user and operator identities;
- model/provider;
- system/developer instructions;
- conversation context;
- retrieval sources;
- long-term memory;
- tools and tool descriptions;
- MCP clients/servers where used;
- credentials and delegated tokens;
- approval gates;
- output consumers;
- audit logs.

## Prompt injection is an authorization problem too

Untrusted content can influence a model's behavior. The defensive goal is not to find a magical prompt that can never be manipulated. Instead, prevent model text from acquiring authority it should not have.

Controls include:

- separate instructions from untrusted content;
- constrain tool permissions;
- validate tool arguments independently;
- require approval for sensitive actions;
- prevent cross-tenant retrieval;
- treat model output as untrusted before code/query/action execution;
- limit memory writes;
- maintain action logs and attribution.

## Least privilege for tools

An agent that only needs to read a ticket should not receive credentials that can delete users. Give each tool the smallest useful scope and separate read from write operations where possible.

Short-lived, workload-specific credentials are preferable to broad permanent API keys.

## Tool descriptions are part of the trust surface

Tool metadata can shape model behavior. Review third-party tool/MCP server descriptions, schemas, permissions, origin, update mechanism, and ownership. Do not assume a tool is safe because its JSON schema looks harmless.

## Model Context Protocol

MCP standardizes connections between AI applications and external tools/data. Its 2026 specification and security guidance emphasize access controls, validation, user consent for sensitive operations, credential protection, and secure authorization flows.

For an MCP deployment, document:

- server owner and origin;
- transport and authentication;
- OAuth/client configuration if used;
- scopes;
- tools/resources/prompts exposed;
- data destinations;
- token storage;
- session isolation;
- rate limits;
- audit logs;
- revocation and removal process.

## Human approval

Approval is meaningful only when the user sees enough information to understand the action. “Allow?” without target, data, and consequence is not informed consent.

For high-impact actions, show:

- exact operation;
- destination/recipient;
- data being shared;
- permissions used;
- whether the action is reversible.

## Memory security

Long-term agent memory can become a persistence layer for bad instructions or sensitive data. Apply provenance, tenant/user isolation, retention rules, validation, and deletion controls. Do not let arbitrary retrieved text silently rewrite durable policy.

## Inter-agent communication

Multiple agents can amplify mistakes. Authenticate agent identities, authorize actions at the receiving service, validate messages, constrain delegation, and preserve traceability across hops.

## Safe failure

Agents need budgets and stop conditions:

- maximum tool calls;
- maximum spend/time;
- retry limits;
- bounded recursion;
- transaction boundaries;
- reversible staging;
- approval escalation.

## Evaluation

Test both normal and adversarial inputs in a local/sandbox environment. Measure whether the system:

- refuses unauthorized tool use;
- preserves tenant boundaries;
- handles conflicting instructions;
- protects secrets;
- asks for approval at the correct point;
- fails safely when a dependency returns malformed output.

## Lab — Harmless agent tool boundary

Build a toy local agent with two tools: calculator and note writer. The note writer may only write under a temporary lab directory. Add a policy layer that rejects absolute paths, traversal, and writes outside the lab. Require confirmation before writes.

Feed the agent untrusted text that requests a write outside the allowed directory and verify the policy layer blocks it regardless of model output.

**Learning goal:** authorization belongs in deterministic controls, not in model obedience.

## Primary references

- OWASP Top 10 for Agentic Applications 2026: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- OWASP secure MCP server development: https://genai.owasp.org/resource/a-practical-guide-for-secure-mcp-server-development/
- MCP security best practices: https://modelcontextprotocol.io/specification/draft/basic/security_best_practices

## Agent/tool security depth

Agentic systems combine model uncertainty with tool authority. The dangerous boundary is often not the model text itself but the transition from untrusted content to privileged action.

### Tool contracts

Each tool should have a narrow purpose, typed/validated inputs, explicit authorization, bounded output, timeout/resource limits, and audit logging. Avoid giving a general shell/filesystem/network tool when a purpose-built capability can perform the required action with less authority.

### Untrusted context

Retrieved documents, emails, webpages, issue text, memory, and tool output can contain instructions. Treat them as data, not authority. System/developer policy and user-approved actions must not be overridden by content merely because it looks like an instruction.

### High-impact actions

Require human confirmation or strong policy gates for deletion, external communication, money movement, credential changes, privilege changes, publication, or other irreversible/high-impact actions. Design idempotency and rollback where possible.

### Observability

Record which model/session requested a tool, validated arguments, authorization decision, result summary, errors, and downstream state change while protecting secrets. Evaluate agents with adversarial/synthetic cases before increasing tool authority.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 25, 39, 41.

### Practice task

Design a fictional agent with no network or destructive tools first. Define tool permissions, user approval boundaries, data provenance, prompt/tool injection defenses, logs, limits, and rollback.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **22, 26, 49, 59**.

---

# SOC, SIEM, SOAR and Detection Operations

> **Purpose:** Understand how security operations turns telemetry into validated detections, investigations, response actions, and continuous improvement.

## SOC operating model

A Security Operations Center is a capability, not just a room or product. It combines people, processes, telemetry, detections, case management, threat context, response authority, and measurement.

## Telemetry pipeline

Typical stages:

1. source generates event;
2. collector receives it;
3. parser/normalizer extracts fields;
4. storage/index retains it;
5. detection logic evaluates it;
6. alert/case is created;
7. analyst investigates;
8. response action is authorized;
9. lessons feed back into controls.

Failures at any stage can create blind spots.

## SIEM

A SIEM centralizes and correlates security-relevant logs. More ingestion is not always better. Prioritize high-value sources and ensure fields are parsed consistently.

For each log source record:

- owner;
- source system;
- event types;
- timestamp/timezone;
- retention;
- parser status;
- expected volume;
- security use cases;
- health monitoring.

## Detection engineering

A detection should have:

- threat/use-case hypothesis;
- required data;
- query/rule;
- expected true positives;
- known false positives;
- severity rationale;
- response playbook;
- test method;
- owner;
- review date.

Detection-as-code practices can add version control, peer review, tests, and rollback.

## Alert quality

Track whether alerts are actionable, not merely numerous. A useful alert contains enough context for the next decision and does not require an analyst to reconstruct basic fields manually.

## SOAR and automation

Automate deterministic, low-risk work first: enrichment, formatting, duplicate suppression, evidence collection, or ticket routing. Sensitive containment actions should have safeguards, scope checks, approvals, and rollback where possible.

## Case management

Cases need chronology, evidence, ownership, decisions, and outcomes. Preserve source links/IDs so another responder can reproduce the investigation.

## Detection coverage

Map detections to your own threat model and critical assets. ATT&CK mapping helps communication but coverage counts can be misleading if rules are untested or data is missing.

## Health monitoring

Detect failures of security controls themselves:

- agent stopped reporting;
- log volume unexpectedly zero;
- parser errors;
- time drift;
- rule disabled;
- retention failure;
- EDR exclusions changed;
- integration token expired.

## Lab — Detection lifecycle

Create synthetic authentication logs with normal logins and one benign pattern of repeated failures followed by success. Write a detection, test it against positive and negative datasets, document false positives, and create a response checklist.

Then remove a required field from the logs and document how detection quality degrades.

**Learning goal:** detection is a tested data product, not just a query.

## SOC operating model in more depth

A SOC is a feedback system, not an alert queue. Telemetry, detections, triage, investigation, response, lessons learned, and engineering changes should form a loop.

### Telemetry quality

Before writing a rule, verify that the required fields are reliably collected, timestamped, parsed, retained, and attributable to an asset/identity. A perfect query cannot compensate for missing or misleading telemetry.

### Detection lifecycle

Document hypothesis, data sources, query/rule logic, expected benign test, false-positive conditions, severity, triage steps, response ownership, and regression tests. Version detections like code.

### SOAR

Automate deterministic low-risk steps first: enrichment, ticket formatting, evidence collection, duplicate suppression. High-impact containment should have appropriate approvals and safeguards until the automation is proven reliable.

### Triage

A good triage result states what is observed, confidence, affected entities, business context, next evidence needed, and whether containment is justified. Do not equate an alert with an incident.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 12 and 23.

### Practice task

Build a synthetic event pipeline: generate events, normalize fields, write one detection, route an alert, triage it with a playbook, measure false positives, and document telemetry gaps.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **37, 38, 59**.

---

# Business Continuity, Disaster Recovery and Backup Engineering

> **Purpose:** Design recovery capabilities that remain usable when systems, identities, facilities, providers, or data are unavailable.

## Three related disciplines

**Business continuity** keeps critical business processes operating.
**Disaster recovery** restores technology capabilities.
**Backup engineering** preserves recoverable copies of data/configuration.

They overlap but are not interchangeable.

## Business impact analysis

Identify critical processes and their dependencies:

- people;
- identity;
- applications;
- databases;
- networks;
- DNS;
- SaaS/cloud providers;
- facilities;
- suppliers;
- communication channels.

## Recovery objectives

**RTO:** target time to restore a service.
**RPO:** maximum tolerable data-loss window.

These should be business decisions informed by technical feasibility and cost.

## Backup design

Consider independent copies, geographic/provider separation where needed, immutable/offline options, encryption, key recovery, privileged-access separation, retention, and monitoring.

Backups should include more than user data when recovery depends on configuration, certificates, infrastructure code, application packages, or identity systems.

## Restore testing

A successful backup job is not a successful recovery. Test:

- file restore;
- database restore;
- application restore;
- identity dependency;
- key/certificate availability;
- clean-room recovery;
- time required;
- integrity checks.

## Dependency maps

Recovery plans fail when teams restore components in the wrong order. Document upstream dependencies and minimum viable service chains.

## Crisis communications

Maintain out-of-band contacts and communication channels that do not depend on the affected identity or collaboration platform.

## Provider failure

Cloud and SaaS improve resilience in many scenarios but create provider and account dependencies. Define export/backup capability, alternative communication, and administrator recovery.

## Exercises

Use increasing realism:

1. checklist review;
2. tabletop;
3. component restore;
4. partial service recovery;
5. full disaster-recovery exercise.

Record lessons and assign remediation owners.

## Lab — Recovery proof

Create a small local service with configuration and sample data. Back up both. Delete the working copy, restore from backup, verify hashes/data, and record actual recovery time. Repeat after changing one undocumented dependency and observe the failure.

**Learning goal:** recovery capability must be demonstrated, not assumed.

## Recovery engineering in more depth

Business continuity keeps critical work functioning; disaster recovery restores technology; backup engineering preserves recoverable copies. They overlap but answer different questions.

### RTO and RPO

RTO describes how quickly a service should be restored. RPO describes how much data loss in time is acceptable. These targets must be tied to real business processes and tested against observed recovery performance.

### Dependency mapping

A recovery plan for an application is incomplete if it ignores identity, DNS, certificates/keys, network configuration, storage, secrets, external providers, build artifacts, licenses, and administrators' access paths.

### Clean recovery

After a security incident, restore from a known-good point, rotate compromised identities/secrets, patch the entry condition, validate configurations, and monitor before declaring recovery complete. Reconnecting a restored but still vulnerable system can recreate the incident.

### Exercises

Use tabletop, partial restore, and full technical recovery exercises at appropriate intervals. Record gaps, owners, deadlines, and actual recovery times. A runbook that has never been exercised is an assumption.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 23 and basic backup concepts.

### Practice task

Back up disposable lab data, record RPO/RTO targets, delete/alter the disposable copy, restore it, verify integrity, measure actual recovery time, and update the runbook.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **38, 49, 59**.

---

# Secrets, PKI and Key Management

> **Purpose:** Manage passwords, API keys, certificates, cryptographic keys, signing identities, and recovery material across their full lifecycle.

## Secret lifecycle

Every secret needs:

- owner;
- purpose;
- scope;
- creation source;
- storage location;
- distribution mechanism;
- rotation/revocation process;
- expiry where appropriate;
- audit trail;
- recovery or replacement plan.

Unknown secrets become permanent risk.

## Secret types

Examples include:

- passwords;
- API keys;
- OAuth client secrets;
- service credentials;
- SSH private keys;
- TLS private keys;
- code-signing keys;
- database credentials;
- encryption keys;
- recovery codes.

Each has different storage and rotation requirements.

## Avoid secrets in source code

Repositories are optimized for copying and history. Once a real secret is committed, remove it from use by rotating/revoking it; deleting only the latest line does not erase previous exposure.

## Secret managers

Centralized secret-management systems can enforce access, rotation, auditing, and short-lived credentials. Their administrative and recovery paths become highly privileged and must be protected accordingly.

## PKI concepts

Public Key Infrastructure combines key pairs, certificates, identities, certificate authorities, validation, revocation/status, policies, and operational processes.

A certificate binds claims to a public key under an issuer's trust model. Protecting the private key is critical.

## Certificate lifecycle

Track:

- subject/SANs;
- issuer;
- key algorithm/size;
- validity;
- private-key location;
- owner;
- renewal method;
- deployment targets;
- revocation path.

Automate renewal where appropriate, but alert on failure.

## Key rotation

Rotation should be designed before compromise. Support overlapping keys/certificates during controlled transitions where necessary, and know how consumers discover the new key.

## Signing keys

Code/package/container signing keys can affect many downstream users. Isolate high-value signing operations, require strong authorization, log use, and have a compromise response plan.

## Encryption key separation

Separate data-encryption keys and key-encryption/master keys where architecture requires it. Limit who can both access encrypted data and manage the keys that decrypt it.

## Backups and escrow

If losing a key permanently destroys critical data, define secure backup/recovery. If a key must never be recoverable, document that property and its consequences.

## Lab — Secret inventory

Create a fictional application with database password, API credential, TLS key, signing key, and recovery code. For each, record lifecycle fields, access boundaries, rotation trigger, and incident action.

Then redesign the application to replace one long-lived credential with a short-lived identity mechanism.

**Learning goal:** secrets are managed assets, not strings hidden in configuration.

## Key-management depth

Cryptographic strength depends on the lifecycle around the key: generation, storage, distribution, use, rotation, backup/recovery, revocation, expiration, and destruction.

### Secret classes

Separate human passwords, API tokens, OAuth credentials, SSH keys, TLS private keys, signing keys, database credentials, encryption keys, recovery codes, and machine identities. Their rotation and recovery patterns differ.

### PKI

Certificates bind names/identities to public keys under a trust model. Operations should track issuance authority, SAN/name requirements, expiration, renewal automation, revocation, private-key protection, intermediate/root trust, and emergency rotation.

### Signing keys

Code/package/document signing keys can have organization-wide impact. Restrict access, prefer hardware-backed/HSM-style protection for high-value uses, require auditable workflows, and maintain a compromise/revocation plan.

### Rotation

Rotation is not complete until all consumers use the new secret and the old one is revoked. Track dependencies and avoid rotations that leave stale credentials active indefinitely.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 20, 21, and 39.

### Practice task

Create a secrets inventory for a fictional application: secret type, owner, storage, rotation, consumers, expiration, backup/recovery, revocation, and audit evidence.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **22, 24, 48**.

---

# Vulnerability Management and Attack Surface Management

> **Purpose:** Move from one-time scanning to a continuous process for knowing assets, identifying weaknesses, prioritizing real risk, remediating, and proving closure.

## Vulnerability management lifecycle

1. Know the assets.
2. Collect vulnerability/configuration evidence.
3. Validate and deduplicate findings.
4. Enrich with exposure and threat context.
5. Prioritize.
6. Assign an accountable owner.
7. Remediate or mitigate.
8. Retest.
9. Measure and improve.

## Asset inventory comes first

A scanner cannot tell you whether an unknown host is abandoned, critical, ownerless, temporary, or duplicated. Maintain identifiers, owner, business service, environment, exposure, platform, data sensitivity, and lifecycle status.

## Severity is not priority

CVSS v4.0 describes technical severity. Remediation priority should also consider:

- internet/external exposure;
- exploitability and known exploitation;
- asset criticality;
- reachable vulnerable feature;
- privileges required;
- compensating controls;
- business deadlines/dependencies;
- fix availability.

CISA KEV is useful evidence when a vulnerability is known to be exploited in the wild.

## Attack surface management

Attack surface management focuses on discovering and understanding externally or internally reachable assets and exposures over time. The goal is not “scan everything harder”; it is maintaining ownership and reducing unexpected exposure.

## False positives and validation

Keep evidence of why a finding is valid or invalid. Suppressions need owner, reason, scope, and expiry/review date.

## Patch versus mitigation

Sometimes a patch cannot be deployed immediately. Temporary mitigations may include disabling a feature, restricting network access, removing exposure, adding authentication, or increasing monitoring. Track temporary controls until the underlying issue is resolved.

## End-of-life software

Unsupported software creates accumulated risk because future vulnerabilities may not receive fixes. Migration plans should be treated as risk-reduction projects, not postponed indefinitely.

## SLAs and risk-based timelines

Use remediation targets that reflect risk. “All critical findings in X days” is simple but can mis-prioritize isolated assets while lower-severity internet-facing weaknesses wait.

## Retest

A ticket marked fixed is not proof. Validate the vulnerable condition is gone and that the remediation did not create a new failure.

## Metrics

Useful measures:

- critical assets with current scan/config evidence;
- known-exploited vulnerabilities open;
- age of high-priority findings;
- percentage of findings with owners;
- mean/median remediation time by risk tier;
- recurring root causes;
- unsupported assets;
- retest pass rate.

## Lab — Prioritization board

Create ten fictional assets and ten fictional findings with different CVSS scores, exposure, criticality, exploit status, and compensating controls. Rank remediation work and explain each top-five decision.

Then add one new fact—credible active exploitation—and show how priorities change.

**Learning goal:** vulnerability management is an operational risk process, not a sorted scanner report.

## Primary references

- FIRST CVSS v4.0: https://www.first.org/cvss/v4.0/
- CISA KEV: https://www.cisa.gov/known-exploited-vulnerabilities-catalog

## Vulnerability-management depth

Vulnerability management is a continuous control loop: discover assets, assess, validate, prioritize, remediate, verify, learn, and improve the asset inventory.

### Asset context

Every finding should link to an owner, service purpose, environment, exposure, data sensitivity, criticality, and lifecycle status. Unowned assets are themselves a risk signal.

### Prioritization

Use severity with context: exploitability, known exploitation, reachability, external exposure, privileges, compensating controls, business impact, and recovery difficulty. CISA KEV can be one important exploitation signal, but organizations still need local asset context.

### Exceptions

An exception should include reason, compensating controls, responsible risk owner, expiration/review date, and measurable condition for closure. Permanent undocumented exceptions turn backlog into hidden risk.

### Verification

Do not close a finding solely because a patch ticket says “done.” Re-assess the affected control/version/configuration and ensure the service still functions. Track recurrence so systemic causes can be fixed in build images, templates, dependency policy, or provisioning.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 05, 19, and 22.

### Practice task

Create an attack-surface inventory for a fictional service, link assets to owners/exposure, add sample findings, prioritize remediation, track exceptions, and verify closure.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **42, 59**.

---

# Networking Deep Dive

> **Purpose:** Build the networking knowledge required to understand traffic, segmentation, services, logs, and security controls without treating network tools as black boxes.

## Learning objectives

- Explain Ethernet/Wi-Fi links, IP addressing, routing, transport protocols, DNS, DHCP, NAT, TLS, and proxies.
- Read a basic packet or flow record and identify the important fields.
- Distinguish local-link problems from routing, name-resolution, transport, and application problems.
- Understand IPv6 well enough to avoid designing IPv4-only security assumptions.
- Build a small authorized lab and document how traffic is expected to flow.

## Start with a mental model

A useful practical model is:

1. **Application:** HTTP, DNS, SSH, SMTP, APIs, custom protocols.
2. **Transport:** TCP or UDP identifies endpoints with ports and provides different delivery properties.
3. **Internet/network:** IPv4 or IPv6 addresses packets and routes them between networks.
4. **Link:** Ethernet, Wi-Fi, or another local medium moves frames between directly connected neighbors.

The OSI model is useful vocabulary, but do not let memorizing seven layers replace understanding real data flow.

## Addresses are contextual

A device can have multiple addresses at the same time: loopback, Wi-Fi, cellular, VPN, container, IPv4, and IPv6. Security rules should therefore be based on intended trust boundaries and interfaces rather than the assumption that one device equals one IP address.

Loopback (`127.0.0.1` for IPv4 and `::1` for IPv6) is especially useful for local labs because a service bound only to loopback is not intended to accept connections from other devices.

## Subnets and routing

A subnet prefix identifies which address bits describe the network. For IPv4, CIDR notation such as `/24` is common. For IPv6, `/64` is common on local segments. You should be able to answer:

- Is the destination local or remote?
- Which route will be selected?
- Which gateway is used?
- Which interface sends the traffic?
- Which security control sits on that path?

A routing table is evidence of intended forwarding behavior, not proof that the destination is reachable. Firewalls, policy routing, VPNs, broken gateways, or application binding can still prevent communication.

## TCP and UDP

TCP provides a connection-oriented byte stream with sequencing, retransmission, and congestion control. UDP provides datagrams without TCP's connection state and delivery guarantees. Neither tells you whether the application itself is secure.

When reading network logs, distinguish:

- source/destination address;
- source/destination port;
- transport protocol;
- connection direction;
- bytes/packets;
- start/end timestamps;
- TCP state where available.

## DNS is more than name-to-address lookup

DNS stores multiple record types and is part of many security workflows. Common records include A/AAAA, CNAME, MX, TXT, NS, SOA, PTR, CAA, and service-related records. Security teams should understand:

- recursive versus authoritative resolution;
- caching and TTLs;
- split-horizon/internal DNS;
- DNSSEC's authenticity/integrity role;
- why DNS logs are useful telemetry;
- why a DNS name does not guarantee the identity of the application behind it.

## DHCP and local configuration

DHCP commonly provides clients with addresses, default gateways, DNS servers, and lease information. A network can be operational while still using unsafe configuration. Validate expected DNS, gateway, and address ranges instead of assuming automatically supplied values are trustworthy.

## ARP and IPv6 Neighbor Discovery

IPv4 networks commonly use ARP to resolve local IPv4 neighbors to link-layer addresses. IPv6 uses Neighbor Discovery. Security monitoring should account for both. Networks that deploy IPv6 but only monitor or filter IPv4 can create blind spots.

## NAT is not a security policy

NAT changes address/port information. It is not a substitute for a stateful firewall, authentication, authorization, segmentation, or endpoint hardening. A design should explicitly state which traffic is allowed and why.

## TLS and trust

TLS can provide confidentiality and integrity in transit and authenticate endpoints when certificate validation is correct. Important concepts include:

- certificate chains;
- trust anchors;
- host-name validation;
- protocol/cipher negotiation;
- certificate expiration/rotation;
- application-layer authentication on top of TLS.

Encrypting a malicious or unauthorized request does not make it safe. Transport security and application authorization solve different problems.

## Proxies, gateways, and load balancers

Modern traffic often passes through reverse proxies, API gateways, WAFs, load balancers, service meshes, VPN gateways, and cloud edges. This affects:

- source-address visibility;
- TLS termination;
- logging locations;
- rate limiting;
- authentication context;
- header trust;
- incident investigation.

Document which component is authoritative for client identity and which forwarded headers are trusted.

## IPv6 security guidance

Do not disable or ignore IPv6 merely because the team is more familiar with IPv4. Instead:

- inventory IPv6 interfaces and addresses;
- define equivalent firewall policy;
- monitor IPv6 DNS and traffic;
- understand link-local addresses;
- test applications on both address families where supported;
- document transition mechanisms if present.

## Safe local practice

On your own system, inspect local addressing and listening services using the operating system's standard tools. In Termux, availability varies by Android/version, so use `ip`, `ss`, or documented alternatives when installed.

A safe exercise is to start a loopback-only HTTP server:

```bash
mkdir -p ~/security-lab/network-demo
cd ~/security-lab/network-demo
printf 'network lab\n' > index.txt
python -m http.server --bind 127.0.0.1 8000
```

Then, from another local terminal session, retrieve it:

```bash
curl http://127.0.0.1:8000/index.txt
```

Record the server log, local socket state, and request/response. Stop the service with `Ctrl+C`.

## Troubleshooting ladder

When communication fails, troubleshoot from the simplest dependency outward:

1. Is the process running?
2. Is it bound to the expected address and port?
3. Does loopback access work?
4. Does name resolution produce the expected address?
5. Is a route available?
6. Does a firewall/policy allow the traffic?
7. Does TLS validation succeed?
8. Does the application accept the request and authorization context?
9. Are proxies/gateways changing the request?
10. What do logs on both sides say?

## Security design questions

For every networked service ask:

- Which interfaces should it bind to?
- Who needs to reach it?
- Is network access enough, or is strong application authentication also required?
- What protects traffic in transit?
- Where is access logged?
- What happens if DNS fails or an upstream service is unavailable?
- Can one compromised segment reach another unnecessarily?
- How is IPv6 handled?

## Checkpoint

You are ready to continue when you can draw a request from client to service and label DNS, IPs, ports, routing, TLS termination, identity, and major logs. Next: Module 52 for HTTP/browser depth, Modules 03/04 for authorized discovery concepts, and Module 12 for controls/detection.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Module 01.

### Practice task

Use the localhost exercise in this module, draw the request path, and explain address, route, port, transport, application, and log evidence.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **03, 08, 12, 52**.

---

# Web, Browser and HTTP Deep Dive

> **Purpose:** Understand the protocol and browser security model underneath modern web applications so application-security findings can be reasoned about rather than memorized.

## Learning objectives

- Explain HTTP requests/responses, methods, status codes, headers, caching, cookies, and content types.
- Understand origins, same-origin policy, CORS, CSP, browser storage, and session boundaries.
- Distinguish authentication, session management, authorization, and CSRF protections.
- Understand why HTTP/2 and HTTP/3 change transport behavior without eliminating application-layer risks.
- Build safe localhost experiments that show the protocol clearly.

## Anatomy of an HTTP request

A request contains a method, target, headers, and sometimes a body. Important methods include GET, POST, PUT, PATCH, DELETE, HEAD, and OPTIONS. Method names describe intent but do not enforce authorization. Server-side policy must decide whether the caller may perform the action.

Important request headers include `Host`, `Content-Type`, `Accept`, `Authorization`, `Cookie`, and conditional/caching headers. Treat headers received through proxies carefully: a server should have an explicit trust model for forwarded client-address, scheme, and host information.

## Anatomy of an HTTP response

A response includes a status code, headers, and usually a body. Security-relevant headers can influence caching, browser execution policy, transport behavior, framing, MIME handling, and cookie policy. Application code still needs secure authorization and data handling even when headers are configured well.

## Origins and the browser security model

An origin is based on scheme, host, and port. The same-origin policy limits how documents/scripts from one origin can interact with resources from another. CORS selectively relaxes parts of this policy for HTTP requests. CORS is not a server-side authorization mechanism: a non-browser client is not constrained by browser CORS enforcement.

## Cookies and sessions

Session cookies should be treated as credentials. Important attributes include:

- `Secure` to restrict transmission to secure transport;
- `HttpOnly` to reduce script access;
- `SameSite` to control cross-site sending behavior;
- appropriate `Path`/`Domain` scope;
- expiration aligned with the session policy.

Session design should include rotation at important authentication transitions, logout/invalidation behavior, idle/absolute timeouts where appropriate, and server-side authorization on every protected operation.

## Browser storage

Cookies, local storage, session storage, IndexedDB, caches, and service workers have different lifecycles and exposure. Avoid placing long-lived high-value secrets in browser-accessible storage unless the architecture explicitly requires and protects them. Threat modeling should include browser extensions, XSS, shared devices, and session recovery.

## CSRF

Cross-site request forgery abuses a browser's ability to send ambient credentials such as cookies. Defenses may include SameSite cookie policy, anti-CSRF tokens, origin/referer validation where appropriate, and avoiding unsafe state changes through requests intended to be idempotent. The correct defense depends on the application architecture.

## Content Security Policy

CSP can reduce the impact of some content-injection problems by controlling allowed script/style/resource sources and execution behavior. It is a defense-in-depth control, not permission to ignore output encoding, template safety, DOM APIs, or dependency trust.

## Caching and sensitive data

Understand where responses can be cached: browser, shared proxy, CDN, service worker, or application cache. Sensitive responses need appropriate cache policy. Authentication state should not be inferred from stale client-side cache alone.

## HTTP/2 and HTTP/3

HTTP/2 multiplexes streams over a connection; HTTP/3 runs over QUIC. These protocols improve transport behavior but the application still uses concepts such as methods, headers, authority, authentication, and authorization. Infrastructure components must agree on request interpretation; inconsistent parsing between layers can create security problems.

## Error handling

Modern secure design includes exceptional conditions. Errors should:

- fail safely;
- avoid revealing secrets or unnecessary internals;
- produce useful correlation identifiers for operations;
- return consistent client behavior;
- log enough context for diagnosis without logging sensitive values;
- avoid turning unexpected input into an authorization bypass.

## Local protocol exercise

Start a loopback-only server as shown in Module 51. Use `curl -i` to view response headers from your own service:

```bash
curl -i http://127.0.0.1:8000/
```

Create a simple local application later and compare GET versus POST, different content types, and intentional 4xx/5xx errors. Your goal is to observe protocol behavior, not bypass controls.

## Application authorization exercise

Build a tiny local app with two synthetic users and two objects. Write automated tests asserting that:

- each user can access their own object;
- each user is denied access to the other's object;
- anonymous users are denied;
- invalid object IDs fail safely;
- denied actions generate an appropriate audit event.

This teaches object-level authorization more effectively than memorizing vulnerability names.

## Review checklist

When reviewing a web feature ask:

1. Who can call it?
2. What identity does the server trust?
3. What object/action is being authorized?
4. What input formats and size limits apply?
5. What happens on malformed or duplicate input?
6. Where does output enter HTML/JS/SQL/OS/template contexts?
7. Which cookies/tokens are used and how do they expire?
8. Which origins are trusted and why?
9. What security headers are appropriate?
10. Which logs prove success, failure, and privileged changes?

## Checkpoint

You are ready to continue when you can explain an HTTP transaction end to end and distinguish browser-enforced policy from server-side authorization. Continue with Modules 11, 14, 22, 39, and 40.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 11 and 51 help.

### Practice task

Use a local app/service you own to observe requests, responses, headers, cookies, errors, and authorization tests. Keep the exercise local and synthetic.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **14, 22, 39, 40**.

---

# Memory Safety and Exploit Mitigations

> **Purpose:** Understand memory-corruption risk and modern platform mitigations from a defensive engineering perspective, without requiring exploit development.

## Learning objectives

- Explain stack, heap, object lifetime, bounds, and unsafe memory access at a conceptual level.
- Recognize common memory-safety failure classes.
- Understand ASLR, NX/DEP, stack canaries, control-flow protections, sandboxing, and memory-safe languages.
- Use compiler/runtime diagnostics and fuzzing safely against code you own.
- Understand why mitigations reduce risk but do not make vulnerable code correct.

## Why memory safety matters

Languages that allow direct memory manipulation give developers powerful control but require strict discipline. Bugs involving bounds, lifetime, initialization, integer conversion, or type confusion can corrupt program state. Security consequences range from crashes and data disclosure to control-flow compromise.

## Core failure classes

Important concepts include:

- out-of-bounds read/write;
- use-after-free;
- double free;
- uninitialized memory use;
- unsafe integer arithmetic leading to size mistakes;
- type confusion;
- format-string misuse;
- race conditions affecting object lifetime/state.

The correct response is to eliminate the bug and reduce exposure, not to rely only on runtime mitigations.

## Stack and heap mental model

The stack commonly stores function-local state and call metadata; the heap commonly stores dynamically allocated objects. Actual compiler/runtime behavior is more complex. Security learning should focus on object lifetime, bounds, ownership, and control data rather than assuming every platform uses an identical layout.

## ASLR

Address Space Layout Randomization makes selected memory locations less predictable. Its effectiveness depends on platform, entropy, module configuration, information disclosure, and process architecture. ASLR is defense in depth; it does not fix memory corruption.

## NX / DEP

Non-executable memory policies separate writable data from executable code where possible. This blocks some direct execution patterns but does not prevent all code-reuse or data-oriented attacks. Again, the underlying memory error must be fixed.

## Stack canaries

Compilers can place integrity values around sensitive stack data and check them before returning from a function. They can detect some stack corruption, but coverage is not universal and they do not address every memory-safety bug.

## Control-flow protections

Modern platforms may use control-flow integrity, Intel CET-related mechanisms, ARM pointer authentication, shadow stacks, or related protections. These raise exploitation difficulty and can constrain unexpected control transfers. Security teams should know whether builds/platforms enable relevant protections and test deployment assumptions.

## Sandboxing

Sandboxing reduces what a compromised process can access. Browser processes, mobile apps, containers, seccomp-like controls, application sandboxes, and least-privilege identities all reduce blast radius. A sandbox boundary should be treated as a security control that requires maintenance and testing.

## Memory-safe languages

Where practical, using memory-safe languages for new components can remove broad classes of memory errors. Migration decisions still need to account for unsafe interfaces, FFI boundaries, dependencies, performance, and existing native code.

## Compiler and runtime diagnostics

For software you own, use development-time diagnostics such as compiler warnings, sanitizers, static analysis, and runtime checks. Treat warnings as engineering signals. Security-sensitive builds should document which hardening flags and mitigations are enabled and how they are verified.

## Fuzzing safely

Fuzzing feeds generated/mutated inputs into software to discover crashes and unexpected behavior. Keep fuzzing confined to code and services you own. A good fuzzing workflow includes:

- deterministic corpus/seeds where practical;
- resource limits;
- crash artifact retention;
- deduplication;
- sanitizer-enabled builds;
- minimizing a crashing input;
- fixing the root cause;
- regression tests for the fixed input class.

## Triage a crash

When your own program crashes:

1. preserve the exact input;
2. record build/version and environment;
3. reproduce reliably;
4. collect stack trace/sanitizer output;
5. determine whether it is memory safety, logic, resource exhaustion, or another failure;
6. minimize the reproducer;
7. fix root cause;
8. add a regression test;
9. verify hardening remains enabled.

## Secure design guidance

Prefer designs that reduce unsafe parsing and privilege:

- validate lengths before copying/decoding;
- use safe standard abstractions;
- avoid custom parsers/cryptography when mature libraries exist;
- isolate risky parsers in low-privilege processes;
- minimize native-code exposure to untrusted input;
- keep dependencies/toolchains maintained;
- enable platform/compiler hardening;
- add fuzzing at trust boundaries.

## Checkpoint

You should be able to explain what each mitigation does, what it does not do, and why fixing the memory bug is still necessary. Continue with Modules 07, 24, 40, 41, and 54.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Basic programming and Module 40 help.

### Practice task

Compile/run a tiny program you own with warnings and safe diagnostics; intentionally create only benign test failures and use them to understand defensive tooling. Do not develop weaponized exploits.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **40, 54**.

---

# Hardware, Firmware and Boot Security

> **Purpose:** Extend security thinking below the operating system into firmware, boot integrity, hardware-backed keys, device lifecycle, and supply-chain trust.

## Learning objectives

- Explain firmware, UEFI/bootloaders, Secure Boot, measured boot, TPM/secure elements, and hardware-backed key storage.
- Understand firmware update and recovery risks.
- Recognize why physical access changes the threat model.
- Evaluate device lifecycle and supply-chain controls.

## Layers below the OS

A system may depend on CPU microcode, platform firmware, UEFI/bootloader, storage firmware, peripheral firmware, secure elements, and other controllers before the operating system begins normal execution. These layers can have high privilege and may be difficult for ordinary endpoint controls to inspect.

## Secure Boot

Secure Boot aims to restrict the boot chain to trusted, signed components according to configured policy. It helps prevent unauthorized boot components but does not guarantee that every signed component is vulnerability-free or correctly configured.

## Measured boot

Measured boot records cryptographic measurements of boot components into protected facilities such as TPM registers. Those measurements can support attestation and forensic reasoning. Measurement is not the same as enforcement: a system can measure something without necessarily blocking it.

## TPMs and secure elements

Hardware-backed security components can protect keys, measurements, or cryptographic operations. Good design avoids exporting private key material unnecessarily and binds sensitive operations to appropriate device/user state. Recovery planning remains essential because hardware-backed protection can make key loss unrecoverable if no authorized recovery path exists.

## Firmware updates

Treat firmware as patchable software. Inventory versions, obtain updates from trusted vendor channels, verify authenticity using the vendor's supported mechanism, understand power/reboot requirements, and maintain recovery instructions. Unsupported devices can become security liabilities when firmware updates stop.

## Physical access

Physical access can enable attacks unavailable to a remote adversary: booting alternate media, removing storage, attaching debug interfaces, resetting devices, or observing/replacing peripherals. Mitigations may include full-disk encryption, secure boot policy, firmware/boot settings, hardware-backed keys, port controls, screen lock, tamper procedures, and asset custody.

## Full-disk encryption and boot trust

Disk encryption protects data at rest, especially against lost/stolen storage, but its security depends on key management and the state in which the device is captured. A running unlocked device has a different threat model from a powered-off encrypted device.

## Mobile device hardware security

Modern phones commonly use verified boot, hardware-backed keystores, secure execution environments, rollback protection, and app sandboxing. Security decisions should use supported platform APIs rather than attempting to replicate key protection in ordinary application storage.

## IoT/embedded guidance

For embedded devices, ask:

- Is firmware signed?
- Can rollback to vulnerable firmware occur?
- How are device identities/keys provisioned?
- Is the debug interface disabled or controlled in production?
- What happens when the vendor ends support?
- Can the device recover safely from a failed update?
- Are default/shared credentials eliminated?
- Is management traffic authenticated and encrypted?

## Supply-chain questions

Hardware security also includes procurement and provenance:

- approved suppliers;
- tamper-evident shipping/receiving where justified;
- component lifecycle tracking;
- firmware/software bills of materials where available;
- update-channel authenticity;
- end-of-life replacement planning;
- secure disposal and key/data destruction.

## Safe learning exercise

Create an inventory of devices you own. Record model, OS/firmware version, support status, encryption state, update channel, backup/recovery method, and whether important keys are hardware-backed. Do not change firmware settings merely to complete a lab; the objective is understanding the trust chain.

## Checkpoint

You should be able to draw the boot chain of one device you own and identify where trust is established, where keys live, how updates are verified, and how recovery works. Continue with Modules 17, 18, 33, 48, and 49.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 01 and 20.

### Practice task

Inventory the boot/update/encryption/recovery security of devices you own. Record trust chain and support lifecycle without changing critical firmware settings just for practice.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **17, 18, 48, 49, 56**.

---

# Bluetooth, NFC and Proximity Security

> **Purpose:** Understand short-range radio and proximity security with emphasis on pairing, identity, privacy, configuration, and safe testing of devices you own.

## Learning objectives

- Distinguish Bluetooth Classic and Bluetooth Low Energy at a practical level.
- Understand discovery, pairing/bonding, services/characteristics, and permissions conceptually.
- Explain NFC's proximity model and common use cases.
- Evaluate device privacy, update, and pairing hygiene.

## Bluetooth security model

Bluetooth security depends on protocol version, pairing method, device capabilities, implementation quality, user confirmation, key storage, and application-layer design. “Short range” should never be treated as authentication.

## Pairing guidance

When pairing devices you own:

- verify the intended device name/model and physical context;
- prefer pairing methods that provide meaningful user confirmation;
- remove stale pairings;
- keep firmware/OS updated;
- disable unnecessary discoverability;
- avoid pairing sensitive devices in crowded/untrusted environments when confirmation is weak.

## BLE services and characteristics

Bluetooth Low Energy applications commonly expose GATT services and characteristics. Security can depend on whether operations require an encrypted/authenticated connection and whether the application performs its own authorization. A characteristic being discoverable does not imply every write/read should be public.

## Privacy

Bluetooth identifiers and advertising behavior can create tracking concerns. Modern platforms use address randomization and permission controls, but applications should still minimize persistent identifiers and unnecessary background scanning.

## NFC

NFC is commonly used for tags, payments, access, device setup, and data exchange. Proximity reduces some risks but does not prove user intent or authorization. Treat data read from tags as untrusted input and require confirmation for sensitive state changes.

## UWB and proximity claims

Ultra-wideband and related ranging technologies can improve distance estimation, but secure proximity systems still need cryptographic identity, replay resistance, protocol hardening, and safe failure behavior. Distance alone is not authorization.

## Device inventory exercise

For devices you own, document:

- radio types enabled;
- pairing/bonded devices;
- last update date;
- whether discoverability is normally enabled;
- app permissions related to nearby devices/location;
- how lost/stolen-device access is revoked;
- whether the device stores sensitive data.

## Safe lab ideas

Use only your own devices. You can safely practice by:

- observing your phone's paired-device list;
- documenting permission prompts;
- testing what happens when a device is unpaired and re-paired;
- verifying whether a device reconnects automatically;
- reviewing vendor firmware update procedures;
- reading your own NFC tag that contains synthetic text/URL data.

Do not attempt to intercept, impersonate, or interfere with nearby third-party devices.

## Defensive checklist

- Keep radio stacks and device firmware updated.
- Remove unused pairings.
- Disable discoverability when unnecessary.
- Use strong device unlock and encryption.
- Restrict app permissions.
- Require explicit authorization for sensitive actions.
- Log security-relevant pairing/account changes where the platform supports it.
- Have a revocation process for lost devices.

## Checkpoint

You should be able to explain why radio range is not a trust boundary and why application-layer authorization remains important. Continue with Modules 16, 17, 18, and 44.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 16 and 17 help.

### Practice task

Audit pairings, permissions, update state, and proximity-security behavior only on devices/tags you own. Document what proves user intent versus mere physical proximity.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **44, 56, 60**.

---

# Android Security Deep Dive

> **Purpose:** Understand Android's application sandbox, permissions, signing, storage, components, WebView, keystore, updates, and mobile security architecture—especially as context for Termux and defensive mobile development.

## Learning objectives

- Explain Android application UIDs, sandboxing, permissions, app signing, and component exposure.
- Understand private versus shared storage and scoped-storage implications.
- Identify safe handling of secrets and sensitive data.
- Understand intents, exported components, deep links, WebView, and network security at a conceptual level.
- Relate Android security controls to the Termux environment.

## Application sandbox

Android assigns applications identities and isolates their private data/processes using OS-level controls. Apps should not assume access to another app's private files. Security design should minimize permissions and exposed components rather than relying on users to understand every prompt.

## Permissions

Permissions can be install-time, runtime, special, or mediated through platform APIs depending on Android version and capability. Request only what a feature requires, at the point where the user can understand why it is needed. Handle denial gracefully.

## App signing

Android uses application signing as part of update identity and trust relationships. Signing keys are high-value secrets. Protect them with strong access control, backup/recovery procedures, and modern platform-supported signing workflows.

## Storage

Distinguish:

- app-private internal storage;
- app-specific external areas;
- shared/media/document storage;
- caches;
- secure key storage.

Sensitive secrets should not be placed in public/shared files merely for convenience. Termux `$HOME` is private to the Termux app context; Android shared storage has different semantics and is intended for exchange with other apps/users.

## Android Keystore

The Android Keystore can keep cryptographic keys non-exportable and may use hardware-backed protection depending on device/capability. Applications should use supported cryptographic APIs and design recovery around key lifecycle rather than storing raw keys in ordinary files.

## Components and IPC

Activities, services, broadcast receivers, and content providers can create cross-application interfaces. Developers should explicitly control exported behavior, permissions, intent validation, and data sharing. Treat incoming intents/URIs as untrusted input.

## Deep links

Deep links and app links can route external input into application flows. Validate hosts, schemes, paths, parameters, and authorization state. A link opening a screen should not bypass the permissions that would normally protect the same action.

## WebView

WebView combines web content with native application context and therefore deserves careful configuration. Avoid unnecessary JavaScript interfaces, restrict untrusted navigation, use safe URL validation, keep components updated, and do not expose native privileged actions to arbitrary web content.

## Network security

Use TLS with correct certificate/host validation. Avoid disabling verification to “fix” development errors. Separate development endpoints from production configuration and do not ship debug trust settings unintentionally.

## Logging

Do not log passwords, tokens, private keys, full payment data, or other unnecessary secrets. Mobile logs can be collected during support/debugging and may expose more than developers expect. Log identifiers and event context sufficient for diagnosis without reproducing sensitive payloads.

## Backups and screenshots

Decide whether sensitive application data should be included in platform backup and whether sensitive screens should be capturable. These are product/security decisions that depend on the data and recovery requirements.

## Updates and dependencies

Mobile security depends on OS patch support, application updates, SDK/library versions, and backend services. An app cannot compensate indefinitely for an unsupported device platform. Document minimum supported versions and end-of-support policy.

## Termux relationship

Termux gives a powerful Linux-like user space but remains an Android application. This means:

- it is subject to Android lifecycle and permission behavior;
- `$HOME` is within app-private storage;
- shared storage is different from a Linux home filesystem;
- root-only Linux assumptions usually do not apply on normal devices;
- long-running background processes can be affected by Android power management.

## Safe developer review

For an Android app you own, review:

1. requested permissions;
2. exported components;
3. deep-link handlers;
4. WebView usage;
5. secrets/config files;
6. network/TLS configuration;
7. logs;
8. local data storage;
9. backup behavior;
10. dependency/update policy.

Map findings to OWASP MASVS where appropriate.

## Checkpoint

You should be able to explain where an Android app's trust boundaries sit and why Termux is not equivalent to a rooted desktop Linux system. Continue with Modules 17, 28–31, 39, and 44.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 17 and 28.

### Practice task

Review an Android app you own or a training app for permissions, exported components, storage, logs, WebView, TLS settings, and update policy. Map observations to MASVS concepts.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **39, 44, 54, 57**.

---

# Privacy, Data Protection and Operational Hygiene

> **Purpose:** Teach the data-handling discipline required for security work so collection, testing, logs, reports, and automation do not create unnecessary privacy or secret-management risk.

## Learning objectives

- Apply data minimization, purpose limitation, retention, and access control to security workflows.
- Separate secrets, personal data, telemetry, and public information.
- Build safe note-taking and evidence-handling habits.
- Understand privacy tradeoffs in logging, OSINT, incident response, and AI tools.

## Collect less

Security work often creates pressure to collect “everything.” More data can create more risk, storage cost, access-control complexity, breach impact, and legal obligations. Before collecting a field ask:

- What decision does this field support?
- Could a less sensitive value answer the same question?
- How long is it needed?
- Who needs access?
- How will it be deleted?

## Separate identifiers from secrets

Usernames, device IDs, IP addresses, account IDs, tokens, passwords, private keys, and session cookies are not interchangeable categories. A log can safely contain a synthetic account identifier while it should not contain the account's password or bearer token.

## Redaction

Reports and screenshots should redact secrets and unnecessary personal data while preserving enough context to prove the finding. Keep an unredacted evidence copy only when authorization and evidence requirements justify it, and protect it accordingly.

## Retention

Define retention before the test. Temporary captures and debug logs often outlive their purpose. A professional workflow includes deletion/archival rules and verifies that copies were not left in Downloads, messaging apps, clipboard managers, cloud sync folders, or temporary directories.

## OSINT ethics

Public availability does not automatically justify unlimited collection or redistribution. Use clear intelligence requirements, avoid doxxing, minimize personal data, distinguish fact from inference, and avoid accessing private accounts or bypassing access controls.

## Incident-response privacy

Incident responders sometimes need broader telemetry, but collection should still be proportionate. Limit access to investigation data, document purpose, preserve chain-of-custody requirements where relevant, and delete or archive according to policy after the investigation.

## AI/LLM data handling

Before sending security data to an AI service, determine whether it contains secrets, customer data, proprietary code, incident evidence, personal data, or regulated information. Use approved services and data-handling settings. Prefer synthetic examples when the real data is unnecessary.

## Device operational hygiene

- Use device encryption and strong screen lock.
- Keep OS/apps updated.
- Separate test and personal accounts where practical.
- Use password managers/passkeys/MFA appropriately.
- Avoid storing private keys or tokens in shared Android storage.
- Review app permissions.
- Back up important notes securely.
- Remove stale test credentials.

## Evidence-folder pattern

A project can use:

```text
case-or-lab/
├── scope.md
├── notes.md
├── evidence/
├── redacted/
├── report/
└── cleanup.md
```

Keep raw evidence access-controlled. Put only sanitized/export-ready material in `redacted/`.

## Checkpoint

You should be able to justify every sensitive data field you collect during a lab or assessment and explain how it is protected, retained, and deleted. Continue with Modules 34, 37, 42, 43, and 49.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Module 42 helps.

### Practice task

Take a sample assessment folder and classify each artifact by sensitivity, purpose, access, retention, redaction, and deletion rule. Remove any data that is not necessary.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **34, 37, 42, 43**.

---

# Cybersecurity Career and Portfolio Guidance

> **Purpose:** Convert learning into demonstrable, ethical work that employers, clients, teachers, or collaborators can evaluate.

## Skills before titles

Cybersecurity roles vary widely. Instead of trying to become “a hacker,” build evidence in several foundations:

- operating systems;
- networking;
- scripting/automation;
- web/application concepts;
- identity/access control;
- logging/detection;
- vulnerability management;
- reporting;
- recovery;
- ethics/authorization.

Then specialize.

## Portfolio principles

A strong portfolio shows how you think. Good artifacts include:

- a documented Termux setup/recovery guide;
- a Python parser for synthetic logs;
- a threat model for a small app;
- a secure-code change with tests;
- a hardening checklist applied to a lab VM;
- a backup/restore exercise with measured recovery time;
- a detection rule with sample events and false-positive notes;
- a vulnerability report written against your own lab;
- an incident tabletop report;
- an SBOM/dependency review for a project you maintain.

Avoid publishing real credentials, private personal data, unauthorized findings, or code designed primarily to compromise third-party systems.

## Explain each project

Every portfolio project should answer:

1. What problem were you solving?
2. What environment did you use?
3. What security property mattered?
4. What did you build/test?
5. What evidence showed the result?
6. What did you improve?
7. What limitations remain?
8. What would you do next?

## GitHub hygiene

Keep repositories understandable:

- clear README;
- setup instructions;
- license where appropriate;
- `.gitignore`;
- no secrets;
- small meaningful commits;
- screenshots only when they add evidence;
- tests/examples;
- maintenance notes.

## Role directions

### SOC / blue team

Show log analysis, detection design, incident triage, endpoint/network concepts, identity telemetry, and communication.

### Application security

Show secure coding, threat modeling, authorization tests, OWASP/ASVS mapping, API reasoning, and developer-friendly remediation.

### Security engineering

Show automation, identity, cloud/infrastructure controls, CI/CD, secrets, observability, and reliable operations.

### GRC / risk

Show risk registers, control mapping, policy writing, evidence collection, privacy reasoning, tabletop exercises, and executive communication.

### Vulnerability management

Show asset inventory, prioritization methodology, remediation tracking, exception handling, and verification—not just scanner output.

## Certifications

Certifications can structure study or help pass hiring filters, but they are not substitutes for skills. Choose certifications based on the role you want, local employer requirements, cost, and the amount of practical work in the curriculum. Re-check exam versions/objectives before paying because certification programs change.

## Interview preparation

Practice explaining fundamentals out loud:

- authentication versus authorization;
- hash versus encryption;
- TCP versus UDP;
- DNS resolution;
- what happens when a browser visits an HTTPS URL;
- least privilege;
- how to prioritize vulnerabilities;
- what makes a useful alert;
- how to contain an incident without destroying evidence;
- how to prove a backup is usable.

Use examples from your own labs.

## Professional communication

A technically correct finding can still fail if the reader cannot act on it. Reports should identify impact, evidence, affected scope, likelihood/context, remediation, verification, and limitations. Avoid dramatic language when evidence is weak.

## 30-day portfolio plan

### Week 1
Termux/Linux foundations + notes repository.

### Week 2
Python synthetic-log parser + unit tests.

### Week 3
Small local web/API project + threat model + authorization tests.

### Week 4
Write one assessment report and one incident tabletop report; clean the repositories and publish only sanitized material.

## Checkpoint

You should be able to show at least three artifacts that demonstrate different skills and explain every line of code/configuration you claim as your work. Continue with Module 45 for capstones and Module 26 for reporting.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Complete a few hands-on modules first.

### Practice task

Publish or prepare three sanitized portfolio artifacts: one automation project, one security analysis/report, and one recovery/detection project. Explain limitations and what you personally built.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **26, 45**.

---

# Security Metrics and Program Measurement

> **Purpose:** Measure whether security work is reducing risk and improving capability instead of counting activity for its own sake.

## Learning objectives

- Distinguish activity, output, outcome, risk, and control-effectiveness metrics.
- Design metrics with clear definitions and data sources.
- Avoid vanity metrics and misleading averages.
- Connect technical telemetry to management decisions.

## Activity is not outcome

Examples of activity metrics:

- number of scans run;
- number of alerts generated;
- number of training sessions delivered;
- number of tickets opened.

These can describe workload but do not prove improved security. Outcome-oriented questions include:

- Are critical exposed vulnerabilities remediated faster?
- Are high-risk identities better protected?
- Are backups more reliably recoverable?
- Are detections finding meaningful events with manageable noise?
- Is the attack surface shrinking?

## Define every metric

A useful metric has:

- name;
- purpose/decision it supports;
- exact numerator/denominator where relevant;
- data source;
- collection frequency;
- owner;
- target/threshold;
- known limitations;
- segmentation dimensions such as severity/business unit/asset class.

## Vulnerability metrics

Better than “open vulnerabilities” alone:

- age by risk tier;
- externally exposed critical findings;
- known-exploited vulnerabilities overdue;
- remediation SLA attainment by asset criticality;
- reopen/regression rate;
- time from asset discovery to first assessment;
- accepted-risk inventory and expiration.

## Detection/SOC metrics

Consider:

- coverage of prioritized threat behaviors;
- alert precision/false-positive burden;
- time to triage;
- time to meaningful containment;
- percentage of detections with documented response playbooks;
- detection regression-test success;
- telemetry gaps.

Be careful with simple “MTTD/MTTR” averages. Averages can hide long-tail incidents; medians/percentiles and severity segmentation are often more informative.

## Identity metrics

Examples:

- privileged accounts with phishing-resistant MFA;
- stale/inactive accounts;
- standing privilege versus just-in-time access;
- orphaned service accounts;
- secrets/certificates approaching expiration;
- access-review completion and exception age.

## Recovery metrics

Security resilience requires measured recovery:

- backup success is not enough;
- restore-test success rate;
- observed recovery time versus RTO;
- restored data point versus RPO;
- percentage of critical services with tested runbooks;
- dependencies missing from recovery exercises.

## Application-security metrics

Useful examples:

- security requirements covered by automated tests;
- authorization negative-test coverage;
- high-risk dependency age;
- secrets detected before merge;
- time to remediate production findings;
- percentage of critical services with current threat models;
- recurrence rate of previously fixed vulnerability classes.

## Risk indicators

Key risk indicators should have a plausible relationship to risk. Examples include unsupported critical systems, internet-exposed admin interfaces, stale privileged credentials, untested backups, or high-value services without logs.

## Dashboard guidance

A dashboard should answer a decision question. Avoid putting dozens of unrelated numbers on one screen. Show trend, target, exception, owner, and context. Make it possible to drill into the underlying evidence.

## Metric anti-patterns

- counting alerts as success;
- rewarding teams for closing tickets without verifying fixes;
- comparing vulnerability counts between environments of very different size;
- using a single risk score without asset/exposure context;
- hiding uncertainty/data gaps;
- setting targets that encourage under-reporting;
- measuring only what is easy to count.

## Safe lab

Create synthetic monthly data for vulnerabilities, restore tests, and detection alerts. Build a small Python report that calculates medians, percentages, overdue items, and trend direction. Then write three management decisions that the metrics support.

## Checkpoint

You should be able to explain how a metric could be gamed and what evidence would validate that it represents a real improvement. Continue with Modules 42, 47, 48, and 50.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 42, 47, 48, and 50 help.

### Practice task

Create synthetic monthly security data and build a simple report that shows trend, target, exception, owner, and decision supported. Identify how each metric could be gamed.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **42, 47, 48, 50**.

---

# Physical Security and Human Resilience

> **Purpose:** Cover physical access, device loss, workspace controls, visitor processes, and human-centered resilience without relying on deceptive offensive exercises.

## Learning objectives

- Explain how physical access changes technical risk.
- Design basic controls for devices, rooms, visitors, media, and disposal.
- Use awareness exercises that teach safe decisions rather than tricking people.
- Integrate physical incidents into response and recovery planning.

## Physical access changes the threat model

A person with direct access may be able to remove storage, connect peripherals, observe screens, reset equipment, steal tokens, photograph information, or interrupt power/network links. Technical controls should assume that some devices may eventually be lost or stolen.

## Device controls

For laptops/phones/workstations:

- strong screen lock;
- full-disk/device encryption;
- current OS/firmware;
- secure boot where supported;
- controlled removable media;
- asset identification;
- remote revocation/wipe capabilities where appropriate;
- recovery keys protected separately;
- documented lost-device process.

## Workspace controls

Protect sensitive conversations and screens based on environment. Use clean-desk practices where justified, secure printed material, avoid leaving unlocked devices unattended, and separate public/visitor space from restricted infrastructure.

## Visitor and contractor process

A simple process should define:

- who approves visitors;
- identification/badge method;
- escort requirements;
- areas allowed;
- equipment/media rules;
- badge return/expiration;
- reporting of anomalies.

Do not rely on employees confronting suspicious people without a safe escalation procedure.

## Removable media

USB drives and external storage can introduce malware or cause data leakage. Organizations may restrict them, use managed encrypted media, scan content, or disable ports depending on risk. Disposal should account for whether data can be recovered from the media.

## Secure disposal

Deleting a file is not always equivalent to securely disposing of data. Use organization/vendor-supported sanitization methods appropriate to the media type and sensitivity. For encrypted devices, key destruction can be part of a disposal strategy when correctly designed.

## Awareness without harmful deception

Security awareness should teach repeatable behaviors:

- verify unusual requests through a trusted channel;
- do not share MFA codes/passwords;
- report suspicious messages promptly;
- avoid plugging in unknown media;
- lock devices;
- challenge/escalate visitors according to policy;
- report lost devices immediately.

Exercises should be approved, proportionate, and designed to improve behavior rather than embarrass participants.

## Lost-device tabletop

Use a fictional scenario:

1. employee reports a lost phone/laptop;
2. identify device, owner, data classification, and last known state;
3. revoke sessions/tokens where appropriate;
4. assess encryption and lock state;
5. decide whether remote wipe is justified/available;
6. preserve relevant account/device logs;
7. replace/recover access;
8. document notification/escalation requirements;
9. review whether any control failed.

## Facility outage tabletop

Simulate loss of power, cooling, office access, or network connectivity. Ask:

- which systems/services are critical?
- can staff work remotely?
- what alternate communication channel exists?
- how are backups and recovery systems accessed?
- which dependencies are outside the facility?
- who has authority to declare/close the incident?

## Checkpoint

You should be able to integrate physical events into identity, incident-response, and recovery plans rather than treating physical security as a separate discipline. Continue with Modules 09, 37, 42, 48, and 54.

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 09 and 54 help.

### Practice task

Run a fictional lost-device or facility-outage tabletop. Document escalation, identity revocation, evidence, recovery, communications, and lessons learned.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **37, 42, 48, 54**.

---

# Security Research Methodology and Attack-Surface Reasoning

> **Purpose:** Learn how experienced security researchers reason about systems before touching tools. This module is about building accurate models, finding trust assumptions, and turning observations into testable hypotheses inside authorized environments.

## Learning objectives

- Convert a vague target description into assets, identities, trust boundaries, data flows, and security properties.
- Distinguish an attack surface from an exploit and a vulnerability from an exposure.
- Build hypotheses from evidence rather than tool output alone.
- Use differential testing, negative testing, and invariant checking in a safe lab.
- Recognize where complex systems fail: boundaries, parsers, state transitions, identity translation, and recovery paths.

## The research mindset

Deep security work starts with a model. A scanner can tell you that a port is open; it cannot by itself tell you why the service exists, which identity it trusts, what business state it changes, what data crosses the boundary, or what evidence would prove that authorization is enforced correctly. Experienced researchers move repeatedly between **model → hypothesis → experiment → evidence → revised model**.

A useful model asks five questions. What are the assets? Who or what can act on them? Which boundaries separate levels of trust? Which state transitions matter? Which observations are available if something goes wrong? A weakness often appears where two parts of the system disagree about one of these questions.

## Attack surface versus vulnerability

The **attack surface** is the set of reachable inputs, interfaces, identities, dependencies, parsers, update paths, administrative workflows, and physical interfaces that could influence a security-relevant state. A vulnerability is a specific weakness within that surface. Exposure is the degree to which the weakness is reachable under actual deployment conditions.

For example, an internal parser may contain a memory bug but be unreachable from untrusted data. A public API may contain no memory corruption at all but expose a high-impact authorization mistake. Risk reasoning must include reachability, privilege, preconditions, observability, recovery, and business impact.

## Model the system as graphs

A practical way to reason deeply is to use several overlapping graphs:

- **Asset graph:** databases, files, secrets, devices, queues, APIs, control planes.
- **Identity graph:** users, service accounts, workload identities, groups, roles, tokens, trust relationships.
- **Data-flow graph:** where input enters, how it is transformed, where it is stored, and where it leaves.
- **Privilege graph:** which principal can cause which security-relevant state changes.
- **Dependency graph:** libraries, build systems, package registries, CI/CD, cloud services, DNS, identity providers.
- **Observation graph:** logs, traces, audit records, alerts, telemetry gaps.

Security failures are frequently graph problems. A single edge that grants too much authority can matter more than dozens of hardened nodes.

## Trust boundaries

A trust boundary exists wherever data or authority moves between components with different assumptions. Common examples include browser to server, application to database, user process to kernel, container to host, workload to cloud metadata service, mobile app to exported component, CI runner to signing key, and domain user to privileged administration tier.

At each boundary document:

1. input format;
2. caller identity;
3. authentication mechanism;
4. authorization decision;
5. validation and canonicalization;
6. output or side effect;
7. logging and correlation fields;
8. failure behavior.

The most interesting research question is often not “can I send strange input?” but “what does the receiving component believe about this input that the sender can influence?”

## Security properties and invariants

An **invariant** is something that should remain true regardless of normal input variation. Examples:

- a user cannot read another tenant's object without an explicit grant;
- an unsigned update cannot become trusted code;
- a low-privilege process cannot write a protected configuration;
- a refresh token cannot be accepted by a different client than intended;
- a parser must never read beyond the supplied buffer;
- a recovery workflow cannot bypass the normal identity proofing requirement.

Write invariants before testing. They turn security testing from random exploration into falsifiable engineering.

## State-machine thinking

Many high-impact weaknesses are not single malformed inputs; they are invalid **sequences** of otherwise valid actions. Model workflows as states and transitions. Registration, password reset, checkout, invitation acceptance, device enrollment, OAuth consent, key rotation, and account recovery are all state machines.

For each transition, ask:

- what must already be true?
- who is allowed to trigger it?
- can it be replayed?
- can steps be skipped or reordered?
- is the object identity bound to the authenticated principal?
- can two concurrent transitions violate an invariant?
- what happens after timeout, retry, or partial failure?

## Differential testing

Differential testing compares two executions that should differ in a predictable way. In a local test application, compare the same request as two users, with and without a required role, before and after an object is transferred, or with equivalent encodings. Differences can reveal hidden assumptions.

The key is controlled change: alter one variable at a time and record the result. When many variables change together, conclusions become weak.

## Canonicalization and representation gaps

Security boundaries often fail because two components interpret the “same” value differently. Paths may have multiple encodings. Hostnames can be normalized. Unicode can have equivalent representations. HTTP intermediaries may disagree about message boundaries. JSON numbers, duplicate keys, URL encodings, and case rules can differ between libraries.

A safe research approach is to create a small local parser pair and feed both the same synthetic corpus. Flag inputs where the parsers disagree. The goal is understanding semantic mismatch, not targeting a public service.

## Identity translation

Distributed systems frequently translate identity: browser session → API token → service account → database role; or domain account → Kerberos ticket → service identity. Each translation can lose context. Ask what claims survive, what audience restrictions exist, how delegation works, and whether downstream authorization rechecks the correct subject.

A recurring design smell is **confused deputy** behavior: a privileged component performs an action because an untrusted caller can influence the target of that action without providing equivalent authority.

## Failure-path analysis

Security controls are often designed for the success path and forgotten during errors. Study timeouts, partial writes, duplicate messages, retries, expired credentials, failover, restore, rollback, and emergency access. Questions include:

- does failure become fail-open or fail-closed?
- can a retry repeat a security-sensitive state change?
- is an authorization decision cached longer than the authority that justified it?
- do backups restore old secrets or old permissions?
- do emergency procedures bypass monitoring?

## Evidence quality

A finding should be reproducible from minimal evidence. Keep the exact environment, a synthetic identifier, the smallest request/response or log excerpt that proves the behavior, and the expected invariant. Avoid huge terminal dumps. Strong evidence isolates cause and effect.

Separate **observation** from **interpretation**. “The server returned object B while authenticated as user A” is an observation. “This is broken object authorization” is an interpretation supported by that observation plus the expected policy.

## Safe advanced practice

Build a small localhost application with two synthetic users and three objects. Define a policy matrix for read, update, and delete. Write tests that assert every unauthorized transition fails. Then intentionally introduce one harmless logic bug, observe which invariant breaks, fix it, and keep the regression test.

A second exercise is a parser differential lab: parse the same synthetic URL or JSON samples with two standard-library functions and record normalization differences. Do not aim the test at external systems.

## Research notebook template

For each hypothesis record:

- **System model:** component and trust boundary.
- **Invariant:** what should always be true.
- **Hypothesis:** the specific condition that may violate it.
- **Independent variable:** the one thing you will change.
- **Expected result:** behavior if the system is correct.
- **Observed result:** evidence only.
- **Interpretation:** why the evidence supports or rejects the hypothesis.
- **Risk:** preconditions, reachable assets, privilege, and blast radius.
- **Fix:** root-cause remediation.
- **Regression:** test that should fail if the bug returns.

## Deep-study checkpoint

You should be able to take an unfamiliar architecture diagram and produce a test plan without naming a security tool. If your plan is mostly tool names, revisit trust boundaries, invariants, identities, and state transitions.

## Guided study workflow

### Before you begin

Complete Modules 01, 05, 15, 41, 51, and 52. Use only a localhost or private lab you control.

### Practice task

Choose one small application you wrote or an intentionally vulnerable local training application. Draw its asset, identity, privilege, dependency, and observation graphs. Define ten invariants, then create negative tests for at least five of them.

### Evidence to keep

Keep the diagrams, invariant list, test cases, and one example showing how evidence changed your original model.

### Common mistakes to avoid

- treating a scanner result as a conclusion;
- changing multiple variables at once;
- confusing unusual behavior with security impact;
- testing without a written expected policy;
- ignoring recovery and failure paths;
- expanding beyond authorized scope.

### Mastery check

Explain an attack surface without listing vulnerabilities, explain a confused deputy, and show how one invariant becomes a repeatable regression test.

### Continue with

Modules **62, 69, 71, 72, 76, 84, and 85**.

---

# CPU Privilege, Syscalls and Process Internals

> **Purpose:** Build the operating-system mental model needed for deeper vulnerability research, reverse engineering, sandbox analysis, and endpoint defense.

## Learning objectives

- Explain user mode, kernel mode, virtual memory, page permissions, and process isolation.
- Understand a system call as a controlled transition into the kernel.
- Trace the lifecycle of a process from executable loading through threads, files, memory mappings, signals, and exit.
- Recognize why privilege-boundary bugs are especially important.
- Use read-only local tools to inspect your own processes.

## Why internals matter

Security tools eventually reduce to operating-system primitives. A process opens files, maps memory, creates sockets, spawns threads, communicates through IPC, and requests privileged kernel operations through system calls. If you understand those primitives, logs and detections become easier to interpret and reverse-engineered behavior stops looking mysterious.

## CPU privilege model

Modern operating systems separate ordinary application execution from privileged kernel execution. On x86, this is commonly described using privilege rings even though mainstream kernels mostly use ring 3 for user applications and ring 0 for kernel code. ARM systems use exception levels with similar separation goals.

The important security idea is not the numeric ring. It is that code executing with ordinary application privilege cannot directly perform operations reserved for the kernel. It must cross a controlled interface. A vulnerability that crosses this boundary can transform a local application bug into a system-level compromise, which is why kernel attack surface receives intense scrutiny.

## Virtual memory

Each process sees a virtual address space. The operating system and hardware memory-management unit translate virtual addresses into physical memory mappings while enforcing permissions. Pages can be readable, writable, executable, or combinations allowed by the architecture and operating system.

Virtual memory provides isolation, relocation, demand paging, shared mappings, copy-on-write, guard regions, and memory-mapped files. Security mitigations such as ASLR and non-executable memory depend on this machinery.

Do not assume an address observed in one run is meaningful in another. ASLR deliberately changes selected locations. Also distinguish an address being mapped from the mapped content being valid for the operation you intend.

## User-kernel transition

A **system call** is a defined interface by which a user process asks the kernel to perform an operation. Examples include opening a file, reading from a descriptor, creating a socket, changing memory mappings, or creating another process/thread. Architectures use specialized instructions to transition safely to kernel code.

From a security perspective, every syscall handler is part of the kernel's reachable interface. The kernel must validate pointers, lengths, flags, object lifetimes, permissions, namespaces, and concurrent state because callers are not trusted merely because they are local.

## File descriptors and object handles

Unix-like systems expose many resources as file descriptors: files, pipes, sockets, event interfaces, devices, and more. Windows uses object handles with a different object model but a similar lesson: possession of a reference can carry authority.

A common security design question is whether authority is checked when the reference is created, every time it is used, or both. Descriptor/handle inheritance also matters. A child process may unintentionally inherit access to sensitive resources unless they are explicitly closed or marked non-inheritable.

## Process creation

On Unix-like systems, process creation often involves `fork()`-style duplication followed by `exec()` replacement, although modern implementations and APIs have optimizations and alternatives. Windows commonly creates a new process from an executable image with an explicit creation API.

Security-relevant properties include environment variables, current directory, inherited descriptors/handles, credentials, namespaces, working token, executable search path, loaded libraries, and parent-child relationships.

## Threads and concurrency

Threads share much of a process's address space. Concurrency creates security problems when checks and uses are separated in time, objects can change ownership, or references remain after a lifetime ends. Race conditions, time-of-check/time-of-use errors, deadlocks, and reference-count bugs are all easier to understand once you model concurrent actors explicitly.

## Memory mappings

Executable code, shared libraries, stacks, heaps, anonymous mappings, and memory-mapped files occupy regions with different properties. On Linux, `/proc/<pid>/maps` exposes mapping metadata for processes you are allowed to inspect. Use it only for your own processes in this lab.

Try:

```console
python -c 'import os,time; print(os.getpid()); time.sleep(60)'
```

In another local shell, inspect the printed PID:

```console
cat /proc/PID/maps | head
```

Observe categories and permissions; do not treat the exact addresses as stable.

## Credentials and security context

A process runs with a security context. On Unix-like systems this includes real/effective/saved user and group IDs, supplementary groups, capabilities, namespaces, and security-module labels where applicable. On Windows, access tokens contain identity, groups, privileges, integrity information, and other claims.

The deep lesson is that “administrator” or “root” is too coarse a mental model. Real authorization decisions depend on the current subject, object, requested operation, policy, namespace, label, and sometimes impersonation/delegation state.

## IPC and local trust boundaries

Processes communicate through pipes, Unix-domain sockets, shared memory, RPC mechanisms, message buses, loopback TCP, named pipes, files, and framework-specific brokers. Local IPC is still a trust boundary when peers have different privileges.

Review IPC designs for peer authentication, object ownership, message framing, replay, confused deputy behavior, and inherited authority.

## Signals, exceptions, and asynchronous control flow

Signals on Unix and exceptions/events on other platforms interrupt normal control flow. Handlers have constraints; unsafe operations inside signal contexts can cause subtle bugs. From a security-analysis standpoint, asynchronous events also complicate crash reproduction because state can change between observations.

## `/proc` as a learning surface

On Linux/Termux, `/proc` exposes kernel-generated process and system views. Availability differs on Android because SELinux, app sandboxing, kernel configuration, and platform restrictions limit access. Useful read-only observations for your own process include:

```console
cat /proc/self/status
cat /proc/self/maps | head
ls -l /proc/self/fd
```

Record what exists on your device rather than assuming desktop Linux behavior.

## Syscall tracing as explanation

Where available in a disposable Linux lab, syscall tracing can explain what a program asks the OS to do. The objective is not bypassing controls; it is correlating application behavior with OS events. Trace a program you wrote that opens one file and prints it. Identify the open/read/write/close lifecycle and note library/runtime noise around the core operations.

On Android/Termux, tracing support and ptrace restrictions vary. Treat inability to trace as a platform fact, not an error to defeat.

## Privilege-boundary review checklist

When reviewing a privileged service, ask:

- Which unprivileged inputs reach it?
- How are message lengths and types validated?
- How is the peer identity established?
- Does it resolve file paths after checking them?
- Does it operate on caller-controlled file descriptors?
- Can objects change between authorization and use?
- Are environment variables or search paths trusted?
- Are inherited handles/descriptors restricted?
- Is the privileged portion minimal?

## Safe lab: process anatomy

Write a small Python program that opens a temporary file, creates a socket bound only to `127.0.0.1`, starts a thread, waits for input, and exits. While it runs, inspect its `/proc` status, descriptors, and mappings. Draw a diagram connecting language-level operations to OS resources.

The exercise develops the ability to reason from high-level code to kernel-visible artifacts without attacking anything.

## Guided study workflow

### Before you begin

Complete Modules 28, 33, 51, 53, and 61. A Linux VM is ideal; Termux can cover many observations but Android deliberately restricts some interfaces.

### Practice task

Map one program you own: executable/interpreter, process, threads, descriptors, mappings, sockets, and credentials. Identify which operations require kernel mediation.

### Evidence to keep

Keep sanitized `/proc` excerpts, your diagram, and a table mapping application actions to OS resources.

### Common mistakes to avoid

- assuming Linux desktop behavior is identical to Android;
- treating virtual and physical addresses as the same concept;
- assuming all local IPC is trusted;
- describing root/admin as the only meaningful privilege boundary;
- attempting to bypass platform restrictions for a learning exercise.

### Mastery check

Explain why a syscall is a security boundary, why descriptor inheritance matters, and how virtual-memory permissions support exploit mitigations.

### Continue with

Modules **63, 64, 65, 66, 73, and 74**.

---

# Assembly for Security Analysis — x86-64 and ARM64

> **Purpose:** Learn enough assembly to follow control flow, calling conventions, data movement, and compiler output during debugging and reverse engineering. This is analysis-oriented, not exploit construction.

## Learning objectives

- Read basic x86-64 and AArch64/ARM64 instructions.
- Understand registers, stack frames, calls, returns, condition flags, and branches.
- Connect C/Python-extension behavior to compiled machine code.
- Recognize function prologues, epilogues, loops, comparisons, and common compiler transformations.
- Use local disassembly to explain code you compiled yourself.

## Machine code, assembly, and architecture

A CPU executes encoded instructions. **Machine code** is the bytes; **assembly** is a human-readable representation of those instructions. The mapping depends on the instruction-set architecture. x86-64 uses variable-length instructions and a large historical instruction set. AArch64 uses fixed-width 32-bit instructions and a different register/calling model.

Security analysis does not require memorizing every opcode. You need a small vocabulary plus the ability to consult architecture references.

## Registers

Registers are tiny CPU storage locations used for operands, addresses, return values, arguments, flags, and control state.

On x86-64, general-purpose registers include `rax`, `rbx`, `rcx`, `rdx`, `rsi`, `rdi`, `rsp`, `rbp`, and `r8`–`r15`. `rip` tracks the instruction pointer. On AArch64, general-purpose registers are `x0`–`x30` (with 32-bit views `w0`–`w30`), plus `sp` and program counter behavior managed by branch instructions. `x30` commonly carries the link register for return addresses.

Register roles depend partly on the ABI/calling convention rather than hardware alone.

## Calling conventions

A calling convention specifies how functions exchange arguments, return values, and register ownership. On common System V x86-64 environments, early integer/pointer arguments use registers such as `rdi`, `rsi`, `rdx`, `rcx`, `r8`, and `r9`, while return values commonly use `rax`. Windows x64 uses a different argument-register sequence. AArch64 commonly uses `x0`–`x7` for early arguments and `x0` for the return value.

When reversing, identify the platform ABI first. Otherwise you may mislabel arguments and data flow.

## Stack concepts

The stack stores function-local state, saved registers, spill slots, and sometimes arguments. `rsp` on x86-64 and `sp` on AArch64 identify current stack position. Compilers may omit a traditional frame pointer, especially under optimization.

Do not assume source variables map one-to-one to fixed stack locations. Optimizers can keep values only in registers, merge variables, eliminate code, or transform loops completely.

## Core x86-64 vocabulary

Common instructions you will see include:

- `mov` — copy data between registers/memory/immediates;
- `lea` — compute an address-like expression without dereferencing it;
- `push` / `pop` — adjust stack while storing/loading a value;
- `call` / `ret` — function call and return;
- `cmp` / `test` — update condition flags from a comparison;
- `je/jz`, `jne/jnz`, `jg`, `jl`, and related jumps — conditional control flow;
- `jmp` — unconditional branch;
- `add`, `sub`, `and`, `or`, `xor`, shifts — arithmetic/bit operations.

`xor eax,eax` is often compiler shorthand for setting `eax` to zero. `lea` is frequently arithmetic, not necessarily a pointer dereference.

## Core AArch64 vocabulary

Common instructions include:

- `mov` or aliases for register/immediate movement;
- `ldr` / `str` — load/store from memory;
- `add` / `sub` — arithmetic and stack adjustments;
- `cmp` — comparison alias affecting flags;
- `b`, `b.eq`, `b.ne`, and other conditional branches;
- `bl` — branch with link (function call);
- `ret` — return, commonly using `x30`;
- `adrp` plus `add`/`ldr` — common position-independent address construction;
- `stp` / `ldp` — store/load register pairs, often in prologues and epilogues.

ARM64 devices also increasingly use pointer-authentication and branch-target protections, which may add instructions around calls/returns.

## Endianness and integer width

Most x86-64 and mainstream AArch64 systems are little-endian. Multi-byte integer bytes therefore appear least-significant byte first in memory. Analysts routinely make mistakes by mixing the numeric representation with byte order.

Track widths carefully. Writing a 32-bit x86 register such as `eax` zero-extends into the full `rax`. AArch64 `wN` accesses the low 32 bits of `xN`. Signed versus unsigned comparisons also choose different branch conditions.

## Pointers versus values

Assembly syntax does not magically label a number as a pointer. Context tells you whether a register contains an address. On x86 Intel-style syntax, brackets such as `[rax]` indicate memory at the address in `rax`. On AArch64, loads/stores use bracketed base addressing such as `[x0]`.

During analysis, annotate each register with your current hypothesis: integer, pointer, length, file descriptor, flags, object pointer, return code. Revise the annotation when evidence changes.

## Control-flow reconstruction

To recover a function's logic:

1. identify entry and return points;
2. mark calls;
3. mark conditional branches and their join points;
4. identify loops from backward branches;
5. label comparisons with the values being tested;
6. trace inputs to outputs;
7. ignore optimization noise until the main structure is clear.

A control-flow graph is often more useful than a line-by-line translation.

## Data-flow reconstruction

Security bugs frequently concern where an untrusted value flows. Track the origin, transformations, bounds checks, type conversions, and final sensitive use. This is conceptually similar to taint analysis.

If a length is converted from signed to unsigned, multiplied, truncated, or used for both allocation and copy with different widths, note the transformation. You do not need to build an exploit to identify a dangerous mismatch.

## Compiler optimizations

Optimization can inline functions, reorder operations, remove checks it proves redundant, use vector instructions, and turn switch statements into jump tables. Compare `-O0` and `-O2` output for code you own to learn how source structure changes.

Security research benefits from recognizing **semantic** operations rather than expecting source-like assembly.

## Safe local disassembly lab

Create this benign program:

```c
#include <stdio.h>
int classify(int x) {
    if (x < 0) return -1;
    if (x == 0) return 0;
    return 1;
}
int main(void) {
    printf("%d\n", classify(7));
    return 0;
}
```

Compile on a Linux lab if a C compiler is available:

```console
cc -O0 -g demo.c -o demo
objdump -d demo | less
```

Then compare:

```console
cc -O2 -g demo.c -o demo-o2
objdump -d demo-o2 | less
```

Find the comparisons, return values, call to output, and differences introduced by optimization. The program has no vulnerability; the point is learning representation.

## ARM64 and Termux

Most modern Android devices use ARM64. If Termux provides a compiler/toolchain on your device, compiling tiny programs locally can make AArch64 assembly concrete. Android binaries also use ELF, dynamic linking, ASLR, SELinux, and platform-specific hardening. Access to debugging other apps is restricted by the Android sandbox and should remain so.

## Recognizing defensive mitigations in code

Disassembly may show stack-protector checks, indirect-branch protection, pointer-authentication instructions, fortified library calls, or sanitizer instrumentation. Learn to identify these as compiler/platform evidence. Their presence does not prove the program is bug-free; their absence may increase the impact of certain bug classes.

## Guided study workflow

### Before you begin

Complete Modules 20, 53, and 62. Basic C syntax helps.

### Practice task

Compile three tiny programs you own: a branch, a loop, and a function with two arguments. Compare debug and optimized disassembly. Annotate registers, calls, and branches.

### Evidence to keep

Keep source code, compiler command, architecture, selected disassembly snippets, and your reconstructed pseudocode.

### Common mistakes to avoid

- assuming one ABI applies everywhere;
- reading an address as a value or vice versa;
- ignoring signed/unsigned width;
- expecting optimized code to mirror source lines;
- copying exploit-oriented assembly snippets from the internet instead of learning on benign code.

### Mastery check

Given a small function, identify its arguments, return path, conditions, and major data flow without relying on source code.

### Continue with

Modules **64, 65, 66, 67, and 82**.

---

# Executable Formats, Loaders and Dynamic Linking

> **Purpose:** Understand how operating systems transform executable files into running processes and how imports, relocations, shared libraries, and loader policy affect security analysis.

## Learning objectives

- Explain the difference between file format, loader, linker, and runtime dynamic linker.
- Read the high-level structure of ELF and PE files.
- Understand sections versus segments, imports/exports, relocations, symbols, and position-independent code.
- Recognize security implications of library search paths, writable code locations, and loader configuration.
- Inspect binaries you compiled yourself using read-only tools.

## From source to process

Source code is compiled or interpreted into forms the runtime can execute. For native code, the path commonly includes compilation into object files, linking into an executable or shared library, storage in a platform file format, and loading/mapping by the operating system. Dynamic dependencies may be resolved at process start or lazily later.

Each stage introduces metadata that is valuable to an analyst: symbols, relocation records, import tables, section permissions, debug information, build IDs, dependencies, and hardening flags.

## ELF mental model

ELF is common on Linux, Android native code, and many Unix-like systems. It contains headers describing the file and program loading. **Sections** organize link-time information such as code, data, symbols, and relocations. **Program headers/segments** tell the loader what to map into memory and with what permissions.

A frequent beginner error is treating sections and segments as identical. A stripped production binary can still be loaded even when much link-time naming information is absent because the loader primarily follows program headers.

## PE/COFF mental model

Windows executables and DLLs use the PE/COFF family. Relevant structures include DOS/PE headers, section table, import/export data, relocation information, resources, debug directories, and optional-header fields describing image layout and security characteristics.

For security analysis, imports often provide behavioral clues: networking, cryptography, process creation, registry access, or file operations. Imports are evidence, not proof—a program can resolve functions dynamically or contain unused imports.

## Static versus dynamic linking

Static linking copies required library code into the final binary. Dynamic linking leaves dependencies to shared libraries/DLLs that are resolved at runtime. Dynamic linking reduces duplication and supports centralized library updates but creates dependency-resolution and search-path considerations.

Security questions include:

- where does the loader search?
- can an unprivileged user influence that search path?
- are dependencies signed or otherwise trusted?
- can an application directory be written by a lower-privilege principal?
- does the binary use an absolute, relative, or platform-defined lookup?

Study these questions defensively on software you own; do not attempt library hijacking on third-party systems.

## Imports, exports, and symbols

An **import** is an external symbol a module expects another component to provide. An **export** is a symbol made available to others. Symbol tables may include function and variable names; stripped binaries remove much human-friendly naming but must retain whatever runtime resolution still requires.

C++ and other languages may mangle names to encode type information. Demangling can recover readable signatures. Debug symbols can provide rich type and source mappings when available.

## Relocations and ASLR

Code and data often contain references that depend on where the image is loaded. Relocations describe places that need adjustment. Position-independent code minimizes fixed-address assumptions and supports address randomization.

On ELF systems, concepts such as the GOT and PLT participate in dynamic symbol resolution. On Windows, import-address tables play a related role. Learn the architecture as a data-flow mechanism rather than memorizing offensive techniques around it.

## W^X and memory permissions

A strong design goal is that memory should not be writable and executable at the same time unless absolutely required. Loaders map code and data with different permissions. Inspecting segment/section flags reveals whether an image follows expected separation.

The loader may also enforce stack execute policy, relocation protections, control-flow features, signatures, or platform entitlements depending on the OS.

## Initialization and entry points

Execution does not always begin directly at `main`. Runtime startup code initializes the process, dynamic loader, thread-local storage, constructors, language runtime, and environment before application logic runs. Reverse engineers therefore distinguish the **image entry point** from the high-level program entry function.

Likewise, shared libraries can have initialization routines. Security review should consider initialization order because privileged state or environment may exist before normal application checks.

## File hashing and provenance

When analyzing a binary, record a cryptographic hash, file size, architecture, timestamp metadata, source/provenance if known, and tool versions. Hashes identify exact bytes; they do not prove trustworthiness. Signing and reproducible builds provide additional provenance signals.

## Safe ELF lab

Compile the benign program from Module 63. Then inspect it:

```console
file ./demo
readelf -h ./demo
readelf -l ./demo
readelf -S ./demo
readelf -d ./demo
```

If available:

```console
objdump -p ./demo
nm ./demo | head
```

Write down architecture, entry point, loadable segments, dependencies, and which regions are executable versus writable.

## Safe Windows/PE lab

On a Windows VM, compile a hello-world application you own. Use platform tools such as `dumpbin /headers` when available, or a trusted PE-inspection utility in read-only mode. Identify sections, imports, architecture, and security-related characteristics. Do not modify system binaries.

## Loader security review

For an application you maintain, review:

- executable and library directory ACLs/permissions;
- whether untrusted directories are in search paths;
- whether runtime environment variables can alter dependency lookup;
- signature/notarization expectations;
- dependency pinning and update provenance;
- whether debug symbols or sensitive paths leak unnecessarily;
- whether executable pages are also writable;
- ASLR/PIE support and control-flow hardening.

## Android native libraries

Android packages can contain native `.so` libraries for one or more ABIs. The application sandbox still applies, while native code introduces memory-safety and JNI boundary concerns. APK signing establishes package/update identity, while ELF hardening affects native components separately.

## Guided study workflow

### Before you begin

Complete Modules 53, 62, and 63.

### Practice task

Compile one tiny program and one shared library you own. Inspect headers, dependencies, symbols, and memory permission layout. Draw the path from file bytes to mapped process segments.

### Evidence to keep

Keep hashes, tool output excerpts, a loader diagram, and a brief hardening inventory.

### Common mistakes to avoid

- confusing sections with loadable segments;
- assuming stripped means encrypted or obfuscated;
- treating imports as definite behavior;
- ignoring runtime initialization before `main`;
- modifying system binaries for a learning task.

### Mastery check

Explain how a dynamic dependency becomes mapped code, how ASLR changes load addresses, and where loader trust decisions can fail.

### Continue with

Modules **65, 66, 67, 73, 79, and 82**.

---

# Debugging, Crash Triage and Root-Cause Analysis

> **Purpose:** Turn crashes and anomalous behavior in software you own into reproducible engineering evidence. The focus is diagnosis and remediation, not exploit weaponization.

## Learning objectives

- Build a disciplined crash-triage workflow.
- Distinguish access violations, assertions, aborts, resource failures, races, and logic faults.
- Read stack traces and register/memory context at a high level.
- Use sanitizers, core dumps, debuggers, and minimal reproducers safely.
- Separate crashability from security exploitability.

## Why a crash is only the beginning

A crash tells you that one execution violated an assumption. It does not automatically tell you root cause or security impact. The same visible fault can result from an out-of-bounds access, null dereference, use-after-free, integer bug, concurrency issue, corrupted input, failed assertion, or resource exhaustion.

Good triage works backward from evidence while preserving reproducibility.

## First-response checklist

When your own application crashes:

1. preserve the exact input and environment;
2. record executable/library hashes and build identifiers;
3. capture logs, exit code, signal/exception type, and stack trace;
4. reproduce without changing multiple variables;
5. determine whether the crash is deterministic;
6. reduce the input or action sequence;
7. classify the likely bug family;
8. inspect the earliest corrupting event, not only the final crash;
9. fix root cause;
10. add a regression test.

## Crash classes

### Invalid memory access

A process reads/writes/executes an address that is not valid under current mappings/permissions. The faulting instruction and address provide clues, but corruption may have occurred earlier.

### Assertion or explicit abort

The application intentionally terminates because an invariant failed. Assertions can reveal logic errors and corrupted state, but an assertion failure is not equivalent to arbitrary code execution.

### Stack exhaustion

Deep recursion or unusually large stack use can exhaust guard limits. Determine whether input controls recursion depth and whether a bounded algorithm is possible.

### Resource exhaustion

Memory allocation, descriptor limits, thread limits, disk capacity, or queue growth can terminate or stall software. This can be availability-relevant without being memory corruption.

### Race-related fault

Crashes that disappear under a debugger or vary between runs may involve concurrency. Record timing, thread IDs, and synchronization state. Sanitizers specialized for thread races can help in owned code.

## Build for diagnosis

Debug builds improve observability. On C/C++ projects you own, retain symbols and enable warnings. Sanitizers can convert silent corruption into precise diagnostic failures near the root cause.

A typical local development example with a modern compiler may look like:

```console
cc -g -O1 -Wall -Wextra -fsanitize=address,undefined demo.c -o demo
```

Toolchain support varies. Use the compiler documentation for your environment. Sanitizers are development diagnostics, not production hardening by themselves.

## Reading a stack trace

A stack trace shows nested call frames at the time of observation. Start at the top faulting frame, then ask which caller supplied the relevant object, pointer, index, or length. If symbols are missing, addresses may require symbolization against the exact build.

Optimized builds can inline functions, omit frames, or rearrange code. Treat the trace as evidence constrained by optimization, not a perfect source-level history.

## Registers and fault context

For native crashes, debugger output may include the instruction pointer, stack pointer, general registers, and flags. Your task is to identify which operand caused the fault and how that operand was derived.

Do not jump from “instruction pointer contains unusual bytes” to an exploitability claim. Security impact requires understanding attacker control, mitigations, reachable privileges, and whether control is reliable.

## Core dumps and minidumps

A dump is a snapshot of selected process state after a crash. It can contain sensitive data from memory, so protect it like potentially confidential evidence. Store only in the lab, restrict access, and delete it when no longer needed.

Dump analysis is most useful when paired with exact binaries and symbols. A dump from build A analyzed using build B can produce misleading stacks.

## Minimize the reproducer

A minimal reproducer removes irrelevant complexity. If a 10 MB file triggers a parser crash, determine whether a tiny input preserves the fault. If a 20-step UI sequence crashes, find the shortest sequence that does.

Reduction improves root-cause reasoning, regression testing, and remediation confidence. Automated test-case minimizers are especially useful after fuzzing.

## Triage memory corruption

For an owned program, ask:

- was the invalid access a read, write, or execute?
- was the address null-like, near a valid object, freed, or wildly invalid?
- did a sanitizer report the allocation/free stack?
- which input controlled the index or size?
- did integer conversion occur before allocation/copy?
- is object lifetime shared across threads?
- does the issue cross a trust boundary?

The goal is locating the first invariant violation.

## Exploitability is a separate assessment

A memory bug may be security-critical, low impact, or non-exploitable under realistic constraints. Factors include control over corrupted data, ability to repeat, reachable security boundary, memory layout, mitigations, sandboxing, process privileges, and available disclosures.

For this guide, stop at **root cause + security impact reasoning + fix**. Do not build a weaponized payload.

## Patch quality

A strong fix addresses the class of failure. If an index can exceed a buffer, fix bounds/ownership logic rather than catching one crashing input. Add a regression test that represents the invalid class and, where practical, a fuzzing target for the trust boundary.

Review nearby code for sibling patterns. One discovered bug may indicate a repeated API misuse.

## Safe debugger lab

Use the benign C program below:

```c
#include <stdio.h>
#include <stdlib.h>
int main(void) {
    int *p = malloc(sizeof(int));
    if (!p) return 1;
    free(p);
    puts("allocation lifecycle completed");
    return 0;
}
```

Compile with debug information and step through allocation and free. Inspect the call stack before and after the calls. Do **not** add use-after-free behavior; the learning goal is debugger navigation and object lifetime.

Then create a separate harmless assertion failure in your own code and practice distinguishing deliberate abort from memory fault.

## Crash-report template

- build/hash;
- platform/architecture;
- trigger input or action;
- deterministic? yes/no;
- exception/signal;
- top relevant frames;
- suspected object/length/state;
- root cause;
- security boundary crossed?;
- mitigation/hardening context;
- fix commit;
- regression test;
- residual uncertainty.

## Guided study workflow

### Before you begin

Complete Modules 53, 62, 63, and 64.

### Practice task

Create three controlled failures in programs you own: an assertion, a handled parser error, and a resource-limit failure. Capture evidence and explain why each class is different. Optionally use sanitizer diagnostics on a deliberately buggy toy program from a recognized training lab.

### Evidence to keep

Keep exact source/build hashes, minimal reproducers, selected traces, and regression tests. Treat dumps as sensitive.

### Common mistakes to avoid

- changing code before preserving the reproducer;
- debugging against mismatched symbols;
- declaring exploitability from a crash alone;
- fixing only the sample input;
- sharing memory dumps containing secrets.

### Mastery check

Given a crash report, explain what is known, what remains unknown, and the next experiment that would reduce uncertainty.

### Continue with

Modules **66, 67, 68, 79, 81, and 84**.

---

# Memory Corruption Mechanics and Mitigation Analysis

> **Purpose:** Go beyond the introductory memory-safety module and understand how corruption changes program state, how modern mitigations constrain impact, and how to diagnose the bug class without constructing weaponized exploits.

## Learning objectives

- Reason about stack and heap object layout, bounds, lifetime, and control data.
- Distinguish spatial from temporal memory errors.
- Understand how ASLR, NX/DEP, canaries, CFI, CET, PAC, RELRO, and sandboxing change exploitability.
- Analyze a sanitizer report and connect it to the violated invariant.
- Understand the concepts behind code-reuse attacks without building a payload.

## Spatial and temporal safety

**Spatial safety** means an access stays within the bounds of the object it is intended to access. Out-of-bounds reads/writes violate this property. **Temporal safety** means the object is still alive when it is accessed. Use-after-free and double-free failures violate lifetime assumptions.

This distinction is useful because mitigations differ. Bounds-checked abstractions help spatial safety; ownership and lifetime systems help temporal safety. Some allocators add quarantine or metadata checks, but they do not turn unsafe code into memory-safe code.

## Stack objects

A function may have local variables, saved registers, spill slots, alignment padding, and call metadata in or around its stack frame. Exact layout is compiler-, architecture-, ABI-, and optimization-dependent. Security analysis should therefore derive layout from the build rather than from a diagram copied from another platform.

A stack out-of-bounds write can corrupt adjacent locals or control data. But the result depends on layout and protections. Modern stack protectors can detect some corruption before a return, while shadow stacks or control-flow protections can defend control data separately.

## Heap objects

The heap is managed by an allocator that maps requests to blocks and maintains metadata. Different allocators organize size classes, arenas, caches, freelists, quarantine, and metadata differently. A heap bug should be analyzed at the object-lifetime level first: which allocation created the object, who owns it, when was it freed, and which reference outlived that event?

Avoid learning allocator internals only through exploitation recipes. The durable skill is reconstructing allocation and reference lifetimes.

## Integer errors as memory precursors

Many memory bugs begin before a pointer is dereferenced. A size can overflow during multiplication, be truncated into a narrower integer, change sign, or be validated in one unit and used in another. For every length, track:

- source type and width;
- signed/unsigned status;
- arithmetic performed;
- conversion points;
- allocation size;
- copy/parse size;
- maximum legal semantic value.

The allocation and the later use must agree on the same validated quantity.

## Type confusion

Type confusion occurs when memory holding one object type is interpreted as another incompatible type. In native code this can arise from unsafe casts or corrupted metadata; in managed runtimes it can arise from engine/runtime bugs. Security impact depends on what fields are subsequently treated as pointers, lengths, function references, or security state.

The defensive review question is: **what establishes the type invariant, and can untrusted state violate it?**

## Control data versus ordinary data

Not all corruption needs to change instruction flow to be serious. Data-only corruption can change authorization flags, object identities, lengths, or policy decisions. Modern control-flow defenses therefore reduce one class of impact while leaving data integrity as a major concern.

When triaging, ask what semantic field was corrupted before asking whether control flow was hijacked.

## ASLR in detail

ASLR randomizes selected virtual address locations. Its effectiveness depends on entropy, architecture, process lifetime, module configuration, memory disclosures, and whether code/data has fixed mappings. Position-independent executables and libraries allow more components to move.

An information disclosure can weaken ASLR because addresses reveal layout. This is why an apparently “read-only” memory bug can materially change the impact of a separate write bug.

## NX / DEP and executable permissions

NX/DEP marks data regions non-executable when supported. This prevents directly executing injected bytes from ordinary writable data pages, but it does not stop corruption itself. Attack research historically shifted toward reusing existing code and manipulating data because of this separation.

The defensive lesson is layered controls: W^X, CFI, sandboxing, memory-safe code, and least privilege complement one another.

## Stack canaries

A compiler can place a random/integrity value near sensitive stack state and verify it before function return. If a sequential overwrite crosses the canary, the process aborts. Coverage and implementation vary; a corruption that does not touch the canary may remain undetected.

Use compiler metadata or hardening inspection rather than assuming every build has a protector enabled.

## RELRO and relocation hardening

On ELF systems, relocation metadata and dynamic-linking structures can be made read-only after startup. Full RELRO reduces the amount of loader-related state that remains writable at runtime. This is an example of a general principle: initialization data that should not change after setup should become immutable.

## Control-Flow Integrity, CET, and shadow stacks

Control-Flow Integrity constrains indirect branches to expected targets based on compiler/runtime policy. Intel CET includes mechanisms such as shadow stacks and indirect branch tracking. Shadow stacks maintain protected return-address state separately from ordinary writable stack memory.

These controls make some control-flow corruption substantially harder, but they do not prevent all logic/data attacks. Security assessment should identify what class each control covers.

## ARM pointer authentication and branch protection

ARMv8.3-A and later architectures can support Pointer Authentication (PAC), which adds authentication information to selected pointers using secret keys held in architectural state. Modern ARM64 platforms may also use branch target identification. Exact adoption differs by OS, device, and compiler.

For Android/mobile analysis, recognize PAC-related instructions as mitigation evidence rather than ordinary application logic.

## Memory tagging

Memory tagging associates metadata with allocations/pointers so invalid spatial or temporal accesses can be detected probabilistically or deterministically depending on the technology. ARM Memory Tagging Extension (MTE) is especially relevant to modern Android devices. Tagging improves detection/containment but does not remove the need for correct ownership and bounds.

## Safe code-reuse concepts

When data pages are non-executable, historic exploitation research demonstrated that existing instruction sequences can be chained rather than injecting new code. You should understand this as a reason **NX alone is insufficient**. This guide intentionally stops at the concept and defensive implications; it does not provide gadget-chain construction or payload instructions.

## Exploitability triage matrix

For a memory bug in owned code, record:

| Question | Why it matters |
|---|---|
| Can untrusted input reach it? | Reachability |
| Read, write, execute, or lifetime error? | Primitive class |
| Which object/state is affected? | Semantic impact |
| Is the corruption attacker-controlled? | Reliability/impact |
| Are addresses disclosed? | ASLR context |
| Is the process sandboxed? | Blast radius |
| What privileges/credentials exist? | Security boundary |
| Which mitigations are enabled? | Constraints |
| Is reproduction deterministic? | Engineering confidence |

Do not reduce the analysis to one “exploitable/not exploitable” guess without evidence.

## Sanitizer-guided local lab

Use a deliberately buggy **training** program from a course or create a toy out-of-bounds example that only runs locally. Compile with AddressSanitizer/UndefinedBehaviorSanitizer where supported. Your deliverable is not a payload; it is a root-cause report containing allocation/object bounds, the first invalid access, source line, fix, and regression test.

Then rebuild with hardening enabled and document what mitigations exist. Note that hardening should remain enabled even after the source bug is fixed.

## Guided study workflow

### Before you begin

Complete Modules 53, 62, 63, 64, and 65.

### Practice task

Analyze one sanitizer-detected bug in toy code. Classify it as spatial/temporal, identify the violated invariant, and produce a source-level fix plus regression test. Inventory platform mitigations separately.

### Evidence to keep

Keep source, sanitizer report, build flags, mitigation inventory, and regression test. Do not create or retain weaponized payloads.

### Common mistakes to avoid

- confusing a mitigation with a source-code fix;
- assuming the same stack/heap layout across builds;
- ignoring integer transformations;
- assuming only control-flow corruption matters;
- declaring reliability without repeated evidence.

### Mastery check

Explain how an out-of-bounds write differs from use-after-free, how NX and ASLR constrain different things, and why data-only corruption can still be critical.

### Continue with

Modules **67, 68, 79, 82, and 84**.

---

# Reverse Engineering and Program Analysis

> **Purpose:** Develop a disciplined workflow for understanding binaries, libraries, and mobile/native components you are authorized to analyze.

## Learning objectives

- Combine static and dynamic analysis rather than relying on one view.
- Recover function boundaries, strings, data structures, control flow, and high-level behavior.
- Recognize compiler artifacts, indirect calls, virtual dispatch, and stripped symbols.
- Maintain an evidence-backed hypothesis notebook.
- Avoid over-interpreting decompiler output.

## Static versus dynamic analysis

**Static analysis** examines code and metadata without executing the sample. It can reveal strings, imports, functions, control flow, constants, embedded resources, and cross-references. **Dynamic analysis** observes behavior during execution: files, sockets, syscalls, memory, logs, and state transitions.

Static analysis offers breadth; dynamic analysis offers concrete runtime evidence. Deep reverse engineering alternates between them.

## Start with provenance

Before opening a binary, record:

- source and authorization;
- hash and size;
- file type and architecture;
- signature information if applicable;
- timestamps as metadata, not proof;
- surrounding package/container;
- analysis environment and tool versions.

For untrusted samples, use an isolated environment. For this guide's labs, prefer binaries you compile yourself or recognized training samples.

## Triage before decompiling everything

A fast first pass asks:

- What format and architecture is it?
- Is it stripped?
- What libraries does it import?
- What strings expose configuration, paths, URLs, error messages, or protocol names?
- What sections/resources exist?
- Is there packing or compression?
- Does the binary contain debug/build identifiers?

This creates hypotheses about where to focus.

## Strings as clues, not conclusions

Strings can reveal user-visible text, logs, function names, URLs, SQL fragments, file paths, or format strings. But they can be unused, obfuscated, compressed, dynamically built, or included by libraries. Always follow cross-references to see where and how a string is used.

## Function identification

With symbols, functions may be named. Without them, tools infer boundaries from call targets, control flow, unwind metadata, signatures, and heuristics. Compiler optimizations can inline, split, merge, or tail-call functions, so “one decompiler function equals one source function” is not always true.

Rename functions based on evidence and confidence: `parse_header_candidate` is better than prematurely naming it `decrypt_password`.

## Decompiler output

A decompiler reconstructs high-level pseudocode from machine instructions. Variable names and types are inferred. Loops and conditionals may look source-like while hiding low-level details.

Always confirm security-sensitive behavior in disassembly when types, signedness, exact bounds, pointer arithmetic, or indirect calls matter.

## Cross-references

Cross-references answer “who calls this?” and “where is this data used?” They are among the most valuable reverse-engineering tools. Starting from an interesting string, imported API, error message, or comparison constant, follow inbound and outbound references until the surrounding state machine becomes clear.

## Recovering data structures

Repeated memory accesses at consistent offsets often suggest fields in a structure/object. Track offset, width, use, and inferred meaning. A field read at offset `+0x10` and compared to a length may be a size; a pointer dereferenced from another offset may reference a buffer.

Treat the layout as a hypothesis and test it against multiple functions.

## Indirect calls and virtual dispatch

Object-oriented code frequently invokes methods through function tables/vtables. Callback-heavy code, event loops, plugin systems, and dynamically resolved APIs also produce indirect calls. Recovering possible targets requires type/context reasoning, not just following direct `call` instructions.

Control-flow protections may insert validation around indirect branches; recognize this as compiler/runtime infrastructure.

## State-machine reconstruction

For parsers, protocols, and authentication logic, reconstruct states rather than isolated functions. Identify input ingestion, validation, parsing, transformation, authorization, side effects, and error handling.

A useful technique is to create a table: state, accepted input, transition condition, next state, security check, observable output.

## Dynamic observation

Run owned/training code with benign inputs and observe:

- file access;
- process/thread creation;
- DNS/socket activity to lab endpoints only;
- log messages;
- loaded modules;
- configuration reads;
- error behavior;
- timing and retries.

Then map observations back to static locations. A log message can become a cross-reference anchor; a file path can lead to parsing code.

## Patching as a learning tool

Binary patching can teach control flow, but use only binaries you own or training artifacts. Prefer harmless changes such as modifying a displayed string or changing a toy feature flag. Do not patch security controls in third-party software.

Document original hash, modified bytes, purpose, and rollback.

## Obfuscation and packing

Obfuscation aims to make analysis harder by hiding names/control flow/data. Packing compresses/encrypts code that is reconstructed at runtime. These techniques can appear in legitimate protectors as well as malware.

Do not infer maliciousness from packing alone. Dynamic behavior, signature provenance, context, and observed actions matter.

## Safe local reverse-engineering lab

Build a small program containing:

- three functions;
- one lookup table;
- one command-line option;
- one error string;
- one dynamically allocated structure;
- one checksum using a standard library.

Compile once with symbols and once stripped. Analyze the stripped copy and create pseudocode. Then compare with source to measure where your inferences were right or wrong.

## Reverse-engineering notebook

For each renamed function record:

- original address/identifier;
- proposed name;
- confidence: low/medium/high;
- evidence: callers, strings, imports, fields;
- inputs/outputs;
- side effects;
- unanswered questions.

This prevents guesses from becoming “facts.”

## Guided study workflow

### Before you begin

Complete Modules 63–66.

### Practice task

Reverse a stripped binary you compiled yourself without looking at source until the end. Recover program purpose, major functions, input handling, and at least one data structure.

### Evidence to keep

Keep the exact binary hash, annotated function map, pseudocode, confidence notes, and comparison against source.

### Common mistakes to avoid

- trusting decompiler types blindly;
- naming behavior from one string;
- ignoring optimization artifacts;
- running untrusted binaries outside isolation;
- patching software you do not own.

### Mastery check

Explain one recovered function using both static evidence and a matching runtime observation.

### Continue with

Modules **68, 79, 82, 83, and 84**.

---

# Fuzzing, Harness Design and Coverage-Guided Testing

> **Purpose:** Learn fuzzing as a software-assurance discipline: expose parsers and state machines to diverse inputs, detect failures early, minimize them, and turn them into regression tests.

## Learning objectives

- Distinguish mutation, generation, coverage-guided, property-based, and stateful fuzzing.
- Design a small deterministic harness around code you own.
- Understand corpus quality, coverage feedback, sanitizers, timeouts, and crash deduplication.
- Minimize failing inputs and fix root causes.
- Reason about why harness quality often matters more than raw execution count.

## What fuzzing actually does

Fuzzing explores an input space automatically. The central engineering problem is not “generate random bytes”; it is making generated inputs reach meaningful code while preserving enough variation to find broken assumptions.

A high-quality harness isolates the target, makes runs deterministic, resets state, imposes resource limits, and exposes relevant input directly to the parser or component under test.

## Fuzzing models

### Mutation-based

Start with valid or semi-valid seed inputs and mutate bytes/tokens/fields. This is effective when the format has structure and seeds get the fuzzer past early parsing gates.

### Generation-based

Generate inputs from a grammar or model. This can reach deep semantic states but requires more knowledge of the protocol or format.

### Coverage-guided

Use instrumentation feedback to retain inputs that execute new control-flow edges or regions. The fuzzer gradually builds a corpus that reaches more code.

### Property-based

Generate structured values and assert invariants. Examples: serialization round trips, parser never crashes, output length is bounded, unauthorized transitions never succeed.

### Stateful/protocol fuzzing

Explore sequences of messages or API calls rather than one input. Reset/reproducibility become more difficult but state-machine bugs become reachable.

## Harness design

A harness should:

- accept bytes or a structured test value;
- invoke the narrow target directly where possible;
- avoid unrelated networking/UI/database setup;
- avoid nondeterministic timestamps/randomness unless controlled;
- clean state between executions;
- return quickly;
- classify normal rejection as success, not crash.

Fuzz a parser function, not an entire production deployment.

## Corpus design

A seed corpus should be small but diverse. Include minimum valid input, typical valid input, boundary sizes, optional fields, nested structures, Unicode where relevant, and historically problematic examples from fixed bugs.

A huge corpus slows startup and can duplicate coverage. Measure what seeds contribute.

## Coverage is a guide, not a goal

More coverage does not automatically equal better security testing. A harness can achieve high line coverage while never varying the security-critical state. Conversely, a focused property test may find an authorization flaw with modest code coverage.

Use coverage to discover unexplored paths, then reason about whether those paths represent trust boundaries.

## Sanitizers

Memory and undefined-behavior sanitizers make native fuzzing far more informative. They detect invalid accesses, lifetime errors, integer/undefined operations, and similar failures close to the source.

Sanitizer overhead is acceptable in a dedicated testing build. Reproduce important failures in a controlled debug environment and confirm the root cause.

## Timeouts and hangs

A hang may indicate an infinite loop, pathological algorithmic complexity, deadlock, or enormous resource request. Capture the smallest input that triggers it and distinguish CPU-bound from blocked I/O or synchronization.

Availability bugs can be security-relevant when untrusted input can trigger disproportionate work.

## Crash deduplication

Thousands of failing inputs may map to one underlying bug. Deduplicate by sanitizer signature, top stack frames, faulting location, or root-cause analysis. Do not report every generated input as a separate vulnerability.

## Minimization

A minimized reproducer is easier to understand and keep as a regression. Reduction algorithms remove bytes/fields while preserving the failure. For structured inputs, grammar-aware minimization may produce much clearer results than byte deletion.

## Differential fuzzing

Feed equivalent input to two implementations and compare outputs. Useful targets include URL parsers, JSON libraries, archive decoders, image parsers, protocol implementations, and cryptographic libraries where exact semantics are defined.

Security interest is highest when disagreement occurs across a trust boundary, such as proxy versus backend interpretation.

## Metamorphic testing

Sometimes there is no simple expected output, but you know relationships that should hold. Examples:

- parsing then serializing then parsing should preserve meaning;
- reordering irrelevant fields should not change authorization;
- case normalization should not change identity unexpectedly;
- adding harmless whitespace should not bypass validation;
- a denied action should remain denied after retry.

These relationships are powerful fuzzing oracles.

## Safe Python micro-fuzzer

For a parser you wrote, a small standard-library mutator can teach the loop:

```python
import os, random

def mutate(data: bytes) -> bytes:
    b = bytearray(data or b"A")
    for _ in range(random.randint(1, 4)):
        i = random.randrange(len(b))
        b[i] ^= 1 << random.randrange(8)
    return bytes(b)

seed = b"name=alice&role=user"
for _ in range(1000):
    sample = mutate(seed)
    # call YOUR local parser here inside try/except
```

Do not aim arbitrary generated traffic at remote systems. The lab should call a local function or localhost-only service you control.

## Fuzzing authorization logic

Fuzzing is not only for memory safety. Represent a small authorization policy as structured objects: subject, action, resource, tenant, role, ownership. Generate combinations and assert that policy invariants hold.

This often finds “missing combination” bugs that example-based tests miss.

## CI integration

Keep a fast regression corpus in normal CI and run longer fuzzing jobs separately. Store minimized crashers with tests when safe. Track time-to-first-failure and coverage trends, but focus on fixed root causes rather than vanity metrics.

## Guided study workflow

### Before you begin

Complete Modules 36, 40, 52, 65, and 66.

### Practice task

Write a small parser or reuse one you own. Build a deterministic harness, seed corpus, timeout, and invariant. Run a bounded local fuzz session. Fix one harmless bug or document why no failure occurred.

### Evidence to keep

Harness code, corpus rationale, coverage/paths if available, minimized failing input, root-cause note, and regression test.

### Common mistakes to avoid

- fuzzing production endpoints;
- treating random bytes as sufficient strategy;
- keeping non-deterministic state;
- counting duplicate crashes as separate bugs;
- chasing coverage without security invariants.

### Mastery check

Explain how harness design affects reachable code and how a minimized input becomes a durable regression test.

### Continue with

Modules **69, 71, 78, 84, and 85**.

---

# Advanced Web Request Processing and Parser Differentials

> **Purpose:** Understand the web request path deeply enough to reason about proxy/backend disagreement, routing ambiguity, cache behavior, request normalization, and server-side request boundaries in controlled labs.

## Learning objectives

- Trace an HTTP request through DNS, TLS termination, CDN/WAF, reverse proxy, application server, framework, and handler.
- Explain how parser or normalization differences create security risk.
- Understand request desynchronization, cache confusion, host handling, path canonicalization, and SSRF at a conceptual/defensive level.
- Design regression tests that ensure intermediaries agree.
- Analyze raw HTTP safely against localhost services you own.

## One request, many parsers

A browser-visible URL may be interpreted by DNS resolvers, proxies, CDNs, TLS terminators, WAFs, load balancers, web servers, frameworks, routers, and application code. Each layer may parse host, path, query, headers, body framing, encodings, and connection state.

The dangerous condition is **semantic disagreement**: layer A believes input means one thing while layer B believes it means another. Security controls placed at A can then protect the wrong interpretation of what B executes.

## Message framing

HTTP/1.x messages use start lines, headers, and body-framing rules. HTTP/2 and HTTP/3 use binary framing and multiplexed streams with their own translation considerations when intermediaries convert protocols.

A defensive architecture should reject ambiguous framing rather than guessing. Normalize and validate at one well-defined boundary, use updated intermediaries, and avoid configurations where multiple independent parsers reinterpret the same raw message differently.

## Request desynchronization concept

Request desynchronization occurs when front and back components disagree about where one request ends and the next begins. Historically this has involved conflicting or malformed length/framing semantics. The risk is that subsequent bytes can be associated with the wrong logical request.

For safety, this guide does not provide attack payload sequences. The engineering takeaway is to test supported proxy/backend combinations with vendor guidance and purpose-built local regression suites, and to reject ambiguous framing consistently.

## HTTP/2 and downgrade boundaries

An edge may accept HTTP/2 while forwarding HTTP/1.1 internally. Translation must preserve a single unambiguous interpretation. Pay attention to prohibited/normalized headers, pseudo-headers, authority/host translation, body length, and connection-specific fields.

Protocol translation is a trust boundary and deserves version-aware security testing.

## Host and authority handling

Applications often use host/authority values for routing, absolute links, password-reset URLs, tenant selection, cache keys, and security policy. A reverse proxy may know the external host while the backend sees an internal hostname.

Define one trusted source for external scheme/host after verifying the proxy relationship. Never blindly trust forwarding headers from arbitrary clients.

## Forwarded headers

Headers such as `Forwarded` or `X-Forwarded-*` can carry original client/protocol information. They are safe only when the application knows which proxy added them and strips/replaces untrusted incoming versions.

A robust deployment documents the trusted proxy chain and tests direct-backend access separately.

## Path normalization

Paths can contain percent encodings, repeated separators, dot segments, Unicode, case variation, and framework-specific decoding. A WAF, web server, and application router may normalize in a different order.

Create local tests for canonical equivalents and assert that authorization is evaluated on the same canonical resource that the handler ultimately uses.

## Cache keys and security context

A cache key must include every request property that changes the response's security meaning. Common dimensions include host, path, query, language/encoding negotiation, authenticated state, tenant, and selected headers.

Cache poisoning and cache deception are both fundamentally about disagreement between cache identity and application identity. Test that personalized or authorization-sensitive responses are not stored under a key reusable by another context.

## Origin versus cache response

When debugging cache security, record whether a response came from origin or intermediary, the cache status, age, vary metadata, and relevant key inputs. A response that changes only after cache warm-up is a different class of problem from an origin authorization failure.

## SSRF as a trust-boundary problem

Server-Side Request Forgery occurs when an application causes a server-side network request to a destination influenced by untrusted input without adequate policy. The important property is not merely “the server can fetch URLs.” It is whether the caller can cross a network/identity boundary using the server's connectivity or credentials.

Defenses include destination allowlists when feasible, DNS/IP validation with careful re-resolution handling, blocked private/link-local ranges where not needed, egress controls, metadata-service protections, protocol restrictions, request timeouts, and avoiding credential forwarding.

## URL parser differentials

URLs contain scheme, authority, userinfo, host, port, path, query, and fragment concepts, with complex encoding and Unicode/IDNA rules. Different libraries can interpret unusual input differently.

A safe lab is to pass a synthetic corpus through two standard-library URL parsers and compare normalized host/path values. Do not use the results to probe external systems.

## Redirect handling

A destination can change after an HTTP redirect. If an application validates only the first URL but follows redirects automatically, the final destination may violate policy. Security-sensitive fetchers should validate every hop and constrain protocols, redirect counts, DNS resolution, and destination classes.

## Server-side templates and interpreters

Template engines, query builders, shell invocation, and expression languages form further parser boundaries. The deep rule is: keep data as data. Use parameterized APIs, context-aware output encoding, and structured libraries rather than concatenating input into another language.

## Raw HTTP localhost lab

Create a localhost-only Python HTTP service that logs the request method, path, host, and selected headers. Send normal requests using `curl` and observe what the framework exposes. Put a local reverse proxy in front only if you already know how to configure it safely. Compare host/path values at each layer.

The objective is understanding transformation, not crafting desynchronization payloads.

## Deployment regression checklist

- one supported interpretation of request framing;
- updated proxy/web-server/framework versions;
- strict forwarding-header trust configuration;
- direct backend not publicly reachable where inappropriate;
- canonical path tested before authorization;
- cache key includes security-relevant dimensions;
- authenticated responses have correct cache controls;
- server-side fetchers enforce egress/destination policy;
- protocol translation covered by integration tests;
- ambiguous requests rejected.

## Guided study workflow

### Before you begin

Complete Modules 11, 13, 14, 22, 52, 61, and 68.

### Practice task

Map a localhost request through client → optional local proxy → application. Record raw and parsed method/host/path/query/body-length values. Add regression tests for canonical path and forwarding-header behavior.

### Evidence to keep

Architecture diagram, raw benign requests, parsed values at each layer, cache/redirect observations, and regression tests.

### Common mistakes to avoid

- assuming every HTTP component uses identical parsing rules;
- trusting forwarding headers from arbitrary clients;
- validating only the first redirect hop;
- testing parser ambiguity against public services;
- confusing a cache issue with origin authorization.

### Mastery check

Explain how two individually “correct” components can become unsafe when they disagree about request meaning.

### Continue with

Modules **70, 71, 76, 78, and 84**.

---

# Browser Isolation, Origins, CORS, CSP and Client-Side Trust

> **Purpose:** Understand browser security as a set of isolation boundaries and delegated capabilities rather than a collection of headers.

## Learning objectives

- Explain origins, sites, schemeful boundaries, and why browser isolation matters.
- Understand Same-Origin Policy, CORS, CSP, cookies, storage, frames, postMessage, and service workers as interacting controls.
- Distinguish browser-enforced read restrictions from server-side authorization.
- Review client-side trust decisions and cross-origin messaging safely.
- Build local tests for origin and policy behavior.

## Origin as a security principal

A web **origin** is based on scheme, host, and port. The browser uses origin relationships to decide whether scripts can read or manipulate resources from another context. This is one of the core isolation mechanisms of the web platform.

“Site” is a related but different concept used by cookie and browser policies. Modern browsers increasingly use schemeful site concepts and storage partitioning, so do not treat origin and site as interchangeable.

## Same-Origin Policy

The Same-Origin Policy limits how one origin can interact with data from another. It is not a network firewall and it does not stop a browser from sending every type of cross-origin request. In many cases, the critical restriction is whether script can **read** the response.

Server-side authorization remains mandatory because requests can be initiated outside a browser entirely.

## CORS

Cross-Origin Resource Sharing lets a server relax selected browser read restrictions by returning policy headers. CORS is an opt-in browser mechanism; it is not authentication.

A strong CORS review asks:

- which origins are allowed?
- are credentials permitted?
- is the origin reflected after exact validation or loosely matched?
- which methods/headers are exposed?
- is preflight caching appropriate?
- does the server still enforce authorization independently?

Wildcard plus credentials is restricted by browsers for good reason, but many unsafe custom reflection patterns remain possible.

## Preflight requests

For certain cross-origin requests the browser sends an `OPTIONS` preflight describing intended method and headers. The server replies with allowed policy. Preflight behavior can reduce accidental cross-origin capability but cannot be treated as an access-control barrier because non-browser clients do not need to obey it.

## Cookies and SameSite

Cookies are scoped by attributes such as Domain, Path, Secure, HttpOnly, SameSite, and lifetime. Host-only cookies reduce scope compared with Domain cookies. `HttpOnly` prevents ordinary script access but does not stop the browser sending the cookie.

SameSite influences when cookies accompany cross-site requests and is an important CSRF defense layer. Sensitive state changes should also use origin-aware request design and anti-CSRF techniques appropriate to the application.

## Content Security Policy

CSP constrains which sources a document may load/execute and can reduce the impact of injection flaws. A robust policy minimizes broad wildcards and unsafe script allowances. Nonces/hashes can support strict script policies.

CSP is defense in depth: fix the injection source rather than using CSP as the only control.

## Frame isolation

Applications may need to prevent or control embedding. CSP `frame-ancestors` is the modern policy mechanism; legacy frame options may also exist. Framing risk is especially important for sensitive confirmation flows because UI redressing can cause a user to click an action they do not understand.

## `postMessage`

Cross-origin windows can deliberately exchange messages. The receiver must validate `event.origin`, message schema, and expected sender context. The sender should use an exact target origin rather than `*` when the message is sensitive.

Treat the message payload like any other untrusted input even after origin validation.

## Browser storage

LocalStorage, sessionStorage, IndexedDB, Cache API, service-worker storage, and cookies have different lifetimes and access semantics. Do not place long-lived bearer secrets in script-readable storage without carefully understanding XSS impact and threat model.

Storage partitioning and privacy features vary by browser version; test your supported browsers rather than relying on old assumptions.

## Service workers

A service worker can intercept requests within its scope and support offline/caching behavior. Because it persists beyond one page load, insecure cache logic or compromised script can have longer-lived effects.

Secure service-worker design includes narrow scope, controlled updates, cache versioning, no caching of inappropriate authenticated content, and clear invalidation behavior.

## DOM trust boundaries

Client-side code often reads URL fragments, query values, `postMessage`, storage, DOM attributes, and API responses. Those values remain untrusted. Use safe DOM APIs and context-appropriate encoding. Avoid converting strings into executable code or HTML when a text/content API is sufficient.

## Client-side authorization is not authorization

Disabling a button, hiding a route, or checking a role in JavaScript improves UX but does not secure the backend. The server must authorize every protected operation using authenticated identity and current policy.

## Trusted Types and safer sinks

Modern browser mechanisms such as Trusted Types can reduce DOM XSS risk by restricting assignment to dangerous sinks unless values are produced through approved policies. Availability and deployment details vary; treat them as a hardening layer alongside output encoding and safe APIs.

## Safe local origin lab

Run two localhost services on different ports, such as `127.0.0.1:8000` and `127.0.0.1:8001`. They are different origins because the port differs. Create a tiny page that attempts `fetch()` between them. Observe browser console behavior before and after adding a narrowly scoped CORS policy to the second service.

Use only synthetic data. The goal is observing browser enforcement, not bypassing another site's policy.

## Security review checklist

- server-side authorization independent of browser policy;
- exact CORS origin rules;
- secure cookie attributes;
- CSRF model documented;
- CSP deployed and monitored where appropriate;
- cross-origin messages validate origin + schema;
- sensitive data kept out of unnecessary browser storage;
- service-worker cache policy reviewed;
- DOM sinks minimized;
- frame embedding controlled.

## Guided study workflow

### Before you begin

Complete Modules 11, 14, 39, 44, 52, and 69.

### Practice task

Build two localhost origins. Demonstrate SOP blocking a cross-origin read, then configure an exact CORS allow rule. Add a `postMessage` demo that rejects messages from unexpected origins.

### Evidence to keep

Browser console/network observations, response headers, origin diagram, and the code enforcing exact origin checks.

### Common mistakes to avoid

- treating CORS as server authorization;
- using `*` for sensitive `postMessage` traffic;
- assuming hidden UI controls protect backend actions;
- storing long-lived bearer secrets unnecessarily;
- relying on CSP instead of fixing injection.

### Mastery check

Explain the difference between SOP, CORS, CSRF defenses, CSP, and server authorization in one coherent request flow.

### Continue with

Modules **71, 78, and 84**.

---

# API Authorization, State Machines and Distributed Abuse Cases

> **Purpose:** Study API security at the level where serious logic bugs occur: object identity, function authority, workflow state, concurrency, tenancy, delegation, and distributed consistency.

## Learning objectives

- Model object-level and function-level authorization separately.
- Build an authorization matrix from subjects, actions, resources, and context.
- Analyze state-machine and race-condition failures.
- Understand tenancy boundaries, delegation, replay, idempotency, and event-driven authorization.
- Create negative tests that prove a policy rather than merely exercise happy paths.

## Authentication is only the first gate

An API can strongly authenticate a caller and still be insecure if it authorizes the wrong object or action. The decision should conceptually answer:

**May subject S perform action A on resource R under context C?**

Context can include tenant, ownership, group membership, transaction state, device posture, time, delegation, approval state, and policy version. If code checks only “is the caller logged in?”, the policy is incomplete.

## Object-level authorization

Object-level authorization determines whether the caller can access a particular record, document, account, project, invoice, message, or other object. Identifiers should be treated as locators, not proof of authority.

A strong test suite creates at least two users and multiple objects in different ownership/tenant states, then verifies read/update/delete behavior for every relevant combination.

## Function-level authorization

Function-level authorization determines whether a caller can invoke an administrative or privileged operation at all. Routes such as user management, billing adjustment, export, key rotation, configuration, moderation, or support impersonation need explicit policy independent of whether their URLs are hidden from ordinary clients.

Backend routing should not infer privilege from UI visibility or client-supplied role fields.

## Property-level authorization

A caller may be authorized to update an object but not every field on it. Mass-assignment and over-posting bugs happen when a framework binds all supplied properties to a model, including fields the caller should not control.

Define writable fields by operation and caller class. Treat server-owned fields—role, tenant ID, approval state, balance, ownership, verification state—as protected unless a specific workflow grants change authority.

## Authorization matrix

Before writing tests, build a matrix:

| Subject | Action | Resource relationship | Expected |
|---|---|---|---|
| owner | read | own object | allow |
| owner | update | own object | allow |
| user | read | another user's object | deny |
| tenant admin | read | same-tenant object | policy-dependent |
| tenant admin | read | other tenant | deny |
| service A | write | service B namespace | deny unless delegated |

This makes missing cases obvious.

## Multi-tenancy

Tenant isolation is a high-value invariant. Tenant context should come from trusted identity/session state, not a request field the caller can arbitrarily choose. Database queries, cache keys, object storage paths, search indexes, background jobs, exports, and logs all need tenant-aware design.

A common failure is enforcing tenant filters in the web handler but forgetting them in a background worker or secondary query path.

## State-machine authorization

An action may be legal only in one state. An order can be canceled before shipment but not after. A recovery token can be used before expiry but only once. An invitation can be accepted by the intended recipient while pending, not after revocation.

Test transitions, not just endpoints. Attempt skip, repeat, reverse, and concurrent execution in your local lab.

## Replay and idempotency

Distributed systems retry. A network timeout does not reveal whether the server processed a request. Idempotency keys or transaction identifiers can prevent duplicate effects for operations such as payments or provisioning.

Security-sensitive one-time actions should bind tokens to purpose, subject, audience, object, and lifetime and mark successful consumption atomically.

## Race conditions and TOCTOU

Two requests can both pass a check before either commits the change. This can violate quotas, balances, one-time token semantics, role changes, or ownership rules.

Mitigations include transactions, row/version locks, unique constraints, atomic compare-and-swap, serializable operations where appropriate, and designing invariants into the data layer rather than only application code.

## Event-driven systems

Authorization becomes harder when a frontend writes an event and a worker later performs the action. The worker must know which principal authorized the request, what policy applied, whether authority is still valid, and whether the event can be replayed.

Do not blindly trust fields inside a message merely because it came from an internal queue. Internal components can be buggy or compromised.

## Delegation

Delegation allows one principal to act on behalf of another under bounded authority. OAuth scopes, service-to-service tokens, signed job capabilities, and support workflows are examples.

Good delegation is explicit about subject, actor, audience, scope, lifetime, and revocation. Logging should preserve both the human/original subject and the acting service when possible.

## Confused deputy in APIs

A privileged service becomes a confused deputy when an unprivileged caller can cause it to use its authority on a caller-chosen target. Server-side URL fetchers, file converters, cloud management helpers, and integration brokers are common shapes.

Prevent this by binding target choices to policy and minimizing the service's own ambient authority.

## Pagination, filters, and exports

Authorization must survive alternative data access paths. Bulk exports, search endpoints, GraphQL resolvers, analytics views, pagination cursors, filters, and autocomplete can leak objects even when the main record endpoint is correct.

Treat every representation as a separate policy enforcement point unless authorization is centralized below them.

## GraphQL considerations

GraphQL exposes a flexible query graph. Security review should cover resolver authorization, field-level policy, query complexity/depth, batching, introspection policy, object identifiers, subscriptions, and data-loader caching across users/tenants.

The schema's flexibility does not remove the need for server-side per-object decisions.

## Rate controls and abuse economics

Some API weaknesses are valid functionality used at harmful scale: enumeration, scraping, expensive search, bulk invitation, or high-cost AI operations. Combine authorization with quotas, anomaly detection, bounded pagination, per-identity limits, and business rules.

Rate limiting is not a substitute for access control; it reduces abuse volume.

## Safe local authorization lab

Implement an in-memory API model with two tenants, two users per tenant, objects, and roles. You do not need a framework; Python functions are enough. Define `authorize(subject, action, resource, context)` and generate all subject/action/resource combinations.

Add a transfer workflow with states `pending → approved → completed` and assert that skipping or repeating a state fails. Then simulate two concurrent “use once” operations using threads and fix the race with an atomic/locked operation.

## Guided study workflow

### Before you begin

Complete Modules 21, 22, 39, 40, 41, 61, 68, and 69.

### Practice task

Build an authorization matrix containing at least 30 cases and automate it. Include two tenants, property-level restrictions, and one stateful workflow.

### Evidence to keep

Policy matrix, test output, state diagram, one intentionally introduced local failure, fix, and regression test.

### Common mistakes to avoid

- treating object IDs as authorization;
- trusting tenant IDs from request bodies;
- checking policy only in the UI;
- ignoring workers/export/search paths;
- testing only successful workflows.

### Mastery check

Explain object-, function-, and property-level authorization, then show how concurrency can violate a correct-looking check.

### Continue with

Modules **72, 76, 84, and 85**.

---

# Kerberos, Active Directory and Enterprise Identity Internals

> **Purpose:** Understand Windows domain authentication and authorization deeply enough to reason about attack paths, configuration weaknesses, and defensive telemetry without relying on credential-theft walkthroughs.

## Learning objectives

- Explain Kerberos principals, KDC functions, tickets, authenticators, SPNs, and delegation.
- Understand how Active Directory identities, groups, ACLs, GPOs, and trust relationships combine into privilege paths.
- Recognize why service accounts and delegation settings are security-sensitive.
- Map common enterprise identity abuse concepts to prevention and detection.
- Validate a lab domain using administrative and audit evidence rather than offensive credential extraction.

## Domain identity as a graph

Active Directory is not merely a user database. It is a graph of users, computers, groups, service accounts, organizational units, Group Policy Objects, directory objects, ACLs, trusts, and authentication services.

A low-privilege account can become high-impact through graph edges: membership in a group that controls another group, write permission over a service account, GPO edit rights over privileged machines, delegated directory rights, or a trust relationship that grants access elsewhere.

## Kerberos actors

In a Windows domain, the Key Distribution Center role is provided by domain controllers. Conceptually, Kerberos involves:

- a **client principal** requesting authentication;
- a **KDC**, which includes authentication and ticket-granting functions;
- a **service principal**, identified using a service principal name (SPN);
- tickets that let the client prove authorization to request or access services;
- authenticators that provide freshness and client proof.

The exact Windows implementation has protocol extensions and Active Directory integration, but the conceptual flow remains valuable.

## TGT and service-ticket flow

After successful initial authentication, a client obtains a Ticket-Granting Ticket (TGT). The TGT is then presented to request a service ticket for a specific service principal. The client presents the service ticket to the service, which validates it using the service's key material and obtains authorization information associated with the user.

The security lesson is that credentials are transformed into delegated cryptographic artifacts. Protecting keys, ticket lifetimes, time synchronization, service identities, and delegation policy is therefore central.

## SPNs

A Service Principal Name binds a service instance to an account. Duplicate, stale, or incorrectly assigned SPNs can cause authentication problems and expand risk. Service accounts associated with SPNs deserve strong credential management and least privilege.

Inventory SPNs in an authorized administrative environment and understand which account owns each one. The objective is configuration hygiene, not offline password attacks.

## PAC and authorization data

Windows Kerberos tickets can carry authorization data such as group membership information in the Privilege Attribute Certificate (PAC). Services use this context to build an access decision. Large group memberships, stale groups, and nested privilege relationships affect resulting authorization.

Authorization is still enforced by the service/resource using ACLs and token semantics; a valid ticket does not mean unrestricted access.

## NTLM coexistence

Windows environments may still use NTLM in scenarios where Kerberos is unavailable or not selected. NTLM lacks several properties of Kerberos and has a long history of relay and downgrade-related risk. Modern hardening aims to understand where NTLM remains, reduce unnecessary use, require stronger channel protections where supported, and avoid silent fallback assumptions.

Do not disable authentication mechanisms blindly; inventory dependencies and follow current Microsoft guidance.

## Directory ACLs

Every AD object can have a security descriptor defining who can read, write, modify ownership, reset credentials, change membership, or perform extended rights. High-impact permissions are not limited to “Domain Admins.”

Review directory ACLs as a graph. A helpdesk group legitimately allowed to reset ordinary users should not automatically gain control over privileged administrators or service identities.

## Group Policy

Group Policy can configure security settings, scripts, registry values, software deployment, firewall policy, and many other endpoint behaviors. Therefore, principals who can edit or link a GPO affecting privileged systems effectively hold substantial authority.

Protect GPO editing, linking, and delegation rights; monitor changes; and separate administrative tiers.

## Delegation

Kerberos delegation lets services act on behalf of users under defined conditions. Unconstrained, constrained, and resource-based constrained delegation have different trust models. Delegation can be required for legitimate multi-tier applications, but unnecessary delegation increases the number of identities capable of impersonated downstream access.

Review which services need delegation, to which destinations, and whether modern constrained models can replace broad delegation.

## Service accounts

Service accounts should have:

- only required logon rights and privileges;
- long, managed, rotated secrets or managed service-account mechanisms;
- no interactive/admin rights unless required;
- explicit SPN ownership;
- monitored changes;
- constrained delegation only when needed.

Group Managed Service Accounts (gMSAs) can reduce manual password-management risk for compatible services.

## Trusts

Forests/domains can establish trusts that affect authentication and resource access. Trust direction, transitivity, SID filtering, selective authentication, and resource ACLs determine actual reachability.

Draw trust arrows carefully: “A trusts B” is frequently misunderstood. Write which users from which side can authenticate to which resources and why.

## Privileged administration tiers

Administrative identities should not routinely sign into lower-trust endpoints where credentials/tokens can be exposed. Separate workstation/admin tiers, just-enough administration, privileged access workstations, modern MFA, credential protections, and limited delegation reduce credential exposure.

## Attack-path thinking without credential theft

You can study AD attack paths entirely from permissions and configuration. Example path:

`User → can edit Group X → Group X can edit GPO Y → GPO Y applies to Server Z → Server Z holds privileged service capability`.

That graph is already enough to identify excessive authority. There is no need to dump credentials to prove the design flaw in a training review.

## Telemetry

Defenders should correlate directory changes, group membership changes, service-account changes, GPO modifications, authentication patterns, new trust/delegation configuration, privileged logons, and suspicious ticket anomalies. Event IDs and availability vary by Windows version/audit policy; validate against current Microsoft documentation and your lab.

## Safe domain lab

In a disposable Windows Server lab domain, create synthetic users, groups, one service account, and an OU. Assign a deliberately overbroad **non-production** ACL such as allowing a test helpdesk group to modify another test group. Document the resulting privilege graph using administrative tools. Then remove the excess permission and verify the path disappears.

Do not perform password extraction, ticket forging, or stealth exercises.

## Current-reference note

Microsoft's Windows Server Kerberos documentation was updated in 2025 and remains the primary platform reference for protocol behavior. MITRE ATT&CK v19.2 is current as of August 6, 2026; use ATT&CK for adversary-behavior mapping, not as a substitute for protocol documentation.

## Guided study workflow

### Before you begin

Complete Modules 21, 32, 39, 47, 61, and 73 when available. Use a disposable lab domain only.

### Practice task

Map users, groups, SPNs, GPO edit rights, directory ACLs, and delegation settings for a tiny lab domain. Build a graph and remove one unnecessary privilege edge.

### Evidence to keep

Architecture/trust diagram, synthetic ACL output, before/after group/GPO rights, and audit evidence of the administrative change.

### Common mistakes to avoid

- equating valid authentication with authorization;
- focusing only on Domain Admin membership;
- treating service accounts as ordinary users;
- misunderstanding trust direction;
- using credential-dumping techniques when permission evidence already proves the path.

### Mastery check

Explain TGT → service ticket → service access, then show how an AD ACL edge can create privilege without any password change.

### Continue with

Modules **73, 80, 81, and 85**.

---

# Windows Internals — Tokens, Services, Registry, ETW and Security Boundaries

> **Purpose:** Build a Windows internals model for defensive research, secure configuration review, reverse engineering, and incident investigation.

## Learning objectives

- Understand processes, threads, access tokens, integrity levels, privileges, and security descriptors.
- Explain the Service Control Manager, Windows services, registry security, object namespaces, and IPC boundaries.
- Understand UAC as an elevation/consent boundary rather than a replacement for account separation.
- Recognize ETW and Windows logging as observability infrastructure.
- Review local privilege boundaries without attempting elevation exploits.

## Windows object/security model

Windows represents many resources as kernel objects with handles and security descriptors. Files, registry keys, processes, threads, events, mutexes, sections, tokens, and named pipes have distinct object types and access masks.

A process does not simply “have access” to an object. It opens a handle requesting specific rights; the Security Reference Monitor evaluates the caller's token against the object's security descriptor and other policy.

## Access tokens

An access token describes the security context of a process or thread. It can contain:

- user SID;
- group SIDs and attributes;
- privileges;
- integrity level;
- restrictions;
- session-related context;
- elevation information.

Threads can impersonate another security context for specific operations, which is critical in servers handling requests from different clients.

## SIDs and groups

Windows security principals are identified by Security Identifiers (SIDs). Human-readable account names can change; the SID is the durable identity used by access-control structures. Nested groups create transitive authority and should be reviewed as a graph.

## Privileges

Token privileges are capabilities for sensitive OS operations. They are distinct from ordinary object ACL rights. A process may carry a privilege disabled until enabled, and some privileges are extremely powerful.

Defensive review should inventory which service identities receive sensitive privileges and remove unnecessary assignments.

## Integrity levels

Mandatory Integrity Control adds an integrity label that can restrict lower-integrity subjects from writing to higher-integrity objects even where discretionary ACLs might otherwise allow access. Browsers and sandboxed components may use low/app-container integrity mechanisms as part of containment.

Integrity is one layer, not a full security model.

## UAC

User Account Control separates a standard/elevated token experience for administrative users and introduces explicit elevation prompts/consent. UAC helps reduce accidental administrative execution but should not be treated as equivalent to using a separate non-admin identity for routine activity.

Enterprise hardening still benefits from standard-user operation and dedicated privileged identities.

## Services

Windows services are managed by the Service Control Manager. A service definition includes executable path, startup behavior, service account, dependencies, recovery settings, and permissions controlling who can reconfigure/start/stop it.

Service security review asks:

- who can modify the service configuration?
- who can write the executable or its directory?
- what identity does it run as?
- are command-line arguments/config files writable by lower privilege?
- are recovery actions safe?
- is the service unnecessarily privileged?

Do not “test” by replacing executables; ACL evidence is sufficient in a lab review.

## Registry

The registry stores system/application configuration in hierarchical hives/keys with ACLs. Security-sensitive areas include service configuration, startup behavior, authentication/security policy, application settings, and COM-related metadata.

Treat writable configuration consumed by a privileged process as a potential authority edge. Verify expected ACLs with administrative read-only tools.

## Named pipes and RPC

Windows services often communicate over named pipes, RPC/ALPC, COM, or sockets. A privileged server must authenticate/authorize its client before performing sensitive work. Named object ACLs also matter: an unexpected user-writable IPC endpoint can allow spoofing or data manipulation.

Model local IPC exactly like a network trust boundary.

## Process creation and parentage

Windows process creation includes executable path, command line, environment, token, inherited handles, mitigation policies, and parent/process attributes. Security telemetry frequently uses process image, signer, command line, parent, user, integrity, and hash together.

Parent-child relationships are useful context but are not infallible proof of causality.

## DLL loading

Applications load DLL dependencies according to Windows loader rules and application configuration. Secure deployments protect directories, avoid unsafe search-path assumptions, and use supported mitigations/signing. Review writable directories and dependency provenance rather than attempting library hijacking.

## ETW

Event Tracing for Windows (ETW) is a high-performance event infrastructure used by Windows and applications. Providers emit events consumed by diagnostic/security tooling. Some security products use ETW-derived telemetry alongside Windows Event Log, Sysmon, Defender, and other sources.

Understanding the telemetry path helps defenders distinguish “no event generated” from “event generated but not collected.”

## Windows Event Log

Audit policy determines which security events are emitted. Domain controllers, endpoints, PowerShell, Defender, and application logs each provide different visibility. Collection architecture should preserve timestamps, host/user identity, event source, and correlation fields.

Avoid memorizing event IDs without context; Windows versions and auditing configuration matter.

## Safe local review lab

On a disposable Windows VM:

- inspect your own process token/group membership;
- inspect ACLs on a temporary file and registry key you create;
- create a harmless test service only if you are comfortable administering the VM, then inspect its configuration and permissions;
- review recent process/security events generated by your own activity.

Do not change protected system services or attempt privilege escalation.

## Security-boundary checklist

- standard users cannot modify privileged executables/configuration;
- service identities use least privilege;
- sensitive token privileges minimized;
- privileged groups reviewed;
- IPC endpoints authenticate clients;
- elevated tasks are auditable;
- logs cover process/service/account changes;
- writable search/config paths are controlled;
- admin identities separated from daily use.

## Guided study workflow

### Before you begin

Complete Modules 32, 37, 44, 62, and 72.

### Practice task

Create a table of ten Windows objects in your lab, the subject accessing each, requested rights, enforcement mechanism, and relevant telemetry.

### Evidence to keep

Token/group output, synthetic file/registry ACLs, service configuration if created, and selected event-log evidence.

### Common mistakes to avoid

- treating UAC as a full security boundary between malicious code and admin intent;
- assuming ACL and privilege are the same concept;
- modifying production/system services for a learning task;
- trusting parent process alone as definitive evidence;
- memorizing event IDs without audit-policy context.

### Mastery check

Explain how a token and security descriptor produce an access decision and how a writable privileged service configuration becomes a security risk.

### Continue with

Modules **72, 80, 81, and 85**.

---

# Linux Internals — Capabilities, Namespaces, Seccomp, LSM and eBPF Security

> **Purpose:** Understand Linux isolation and privilege mechanisms deeply enough to review services, containers, Android/Termux constraints, and kernel-facing attack surface.

## Learning objectives

- Explain Linux credentials, capabilities, namespaces, cgroups, seccomp, and LSM roles.
- Understand why root inside a container is not automatically host root, yet remains high risk.
- Recognize the kernel as a shared security boundary.
- Understand eBPF's security/observability role at a high level.
- Inspect your own process isolation without bypassing restrictions.

## Linux credentials

Linux processes carry real/effective/saved user and group identifiers, supplementary groups, capability sets, namespaces, and security-module context. Files and IPC objects have ownership, mode bits, ACLs, labels, and other metadata.

Authorization is layered. A UID match may permit something that an SELinux policy denies, or a capability may permit an operation otherwise reserved for UID 0.

## Capabilities

Linux capabilities divide traditional root authority into named units such as network administration, ownership override, raw I/O, or process-control abilities. A process can have permitted, effective, inheritable, bounding, and ambient capability sets depending on execution context.

Least privilege means removing capabilities not required by the workload. Some capabilities are so broad that they effectively undermine container boundaries when granted unnecessarily.

## Namespaces

Namespaces provide separate views of selected kernel resources. Common namespace classes include:

- PID;
- mount;
- network;
- IPC;
- UTS/hostname;
- user;
- cgroup;
- time on supporting kernels.

Namespaces change **view and identity context**; they do not create a separate kernel. Containers combine namespaces with cgroups, capabilities, seccomp, LSM policy, filesystem layout, and runtime configuration.

## User namespaces

User namespaces can map a process's namespace-local UIDs/GIDs to different host IDs. They support rootless containers and reduce host authority in some designs. Kernel attack surface reachable from unprivileged user namespaces must be carefully maintained, which is why distributions may differ in enablement policy.

## Cgroups

Control groups account for and limit resources such as CPU, memory, process count, and I/O. They are important for availability containment. Namespaces answer “what can the process see?” while cgroups help answer “how much can it consume?”

Resource isolation is security-relevant because unlimited memory/process creation can become denial of service even when filesystem permissions are correct.

## Seccomp

Seccomp filtering restricts which system calls a process may make. The Linux kernel documentation describes seccomp-BPF as a way to filter incoming system calls and reduce reachable kernel entry points.

A good seccomp profile is workload-specific. An overly broad profile offers little reduction; an overly narrow one breaks legitimate behavior. Generate policy from understanding, then test failure handling.

## Landlock and unprivileged sandboxing

Landlock is a stackable Linux Security Module interface designed to let processes restrict their own ambient filesystem/network rights where supported. It illustrates an important pattern: applications can voluntarily reduce what compromised code would be able to reach.

Availability depends on kernel version/configuration; do not assume a specific Android/Termux device exposes it.

## Linux Security Modules

LSM provides hooks for security modules such as SELinux and AppArmor. These systems can enforce mandatory policy beyond traditional discretionary permissions.

Android relies heavily on SELinux plus the application sandbox. Termux runs as an ordinary Android application UID and cannot simply acquire host root or bypass SELinux without the device itself being modified.

## `no_new_privs`

The `no_new_privs` process attribute prevents `execve()` from granting additional privilege through mechanisms such as set-user-ID binaries. It is commonly combined with sandboxing/seccomp designs.

The principle is monotonic privilege reduction: after a process enters an untrusted parsing stage, it should be difficult to gain new authority.

## Chroot versus isolation

`chroot` changes path resolution root for a process but is not a complete container/security sandbox by itself, especially for privileged processes. Modern isolation uses multiple controls rather than treating a changed filesystem root as sufficient.

## Kernel attack surface

Every enabled syscall, filesystem, protocol, device driver, ioctl, eBPF interface, namespace operation, and kernel parser may contribute reachable code. Kernel self-protection aims to reduce exposed functionality and make exploitation harder through memory protections, read-only data, stack protections, CFI-like mechanisms, and restricted interfaces.

Keep kernels patched and minimize unnecessary privileged device access.

## eBPF

eBPF executes verified programs in kernel-related contexts for networking, tracing, observability, and security. Because eBPF is powerful, kernel versions and configuration place restrictions on who can load programs and what helpers/types are available.

Defenders use eBPF for high-fidelity telemetry; platform maintainers also treat verifier/runtime bugs as serious kernel security issues. Do not attempt to bypass unprivileged eBPF restrictions.

## `/proc`, `/sys`, and observability

Linux exposes process/system state through virtual filesystems. Containers and Android may mount filtered views. Read-only inspection can reveal namespace IDs, capability masks, cgroup membership, and mount layout.

For your own process, examples may include:

```console
cat /proc/self/status
cat /proc/self/cgroup
cat /proc/self/mountinfo | head
```

Interpret what is available on your environment; permissions intentionally differ.

## Safe isolation lab

On a disposable Linux VM with a container runtime, run a minimal container and compare inside/outside:

- PID view;
- hostname;
- network interfaces;
- mount table;
- UID mapping;
- capability set;
- cgroup membership.

Do not attempt to escape the container. Your goal is proving which boundaries exist and which kernel is shared.

## Hardening review

For a service/container ask:

- can it run as non-root?
- which capabilities can be dropped?
- is the filesystem read-only where possible?
- are host devices/sockets mounted?
- is privileged mode disabled?
- are resource limits defined?
- is seccomp/LSM policy active?
- are secrets mounted narrowly?
- can it reach unnecessary networks?
- is the kernel maintained?

## Guided study workflow

### Before you begin

Complete Modules 24, 33, 53, 62, and 73 for comparison.

### Practice task

Inventory namespaces, capabilities, cgroups, and security-module context for a process you own and a disposable container. Explain what each control isolates and what remains shared.

### Evidence to keep

Sanitized `/proc` output, capability list, namespace diagram, and a least-privilege hardening plan.

### Common mistakes to avoid

- assuming namespace root equals host root;
- treating containers as VMs;
- granting broad capabilities to fix permissions quickly;
- using `chroot` as a complete sandbox;
- trying to bypass Android/Linux security restrictions for a learning task.

### Mastery check

Explain namespaces versus cgroups versus seccomp versus LSM, and identify which layer reduces kernel attack surface.

### Continue with

Modules **75, 76, 80, 81, and 85**.

---

# Container and Kubernetes Isolation Internals

> **Purpose:** Move from basic container security into runtime internals, workload identity, Kubernetes authorization, pod security boundaries, and cluster-level blast-radius reasoning.

## Learning objectives

- Explain how container runtime isolation is assembled from Linux primitives.
- Understand Kubernetes API authentication, authorization, admission, controllers, and workload identity.
- Identify dangerous pod/runtime configuration without attempting container escape.
- Reason about service accounts, RBAC, secrets, network policy, admission, and node trust.
- Design safe cluster validation tests.

## Container boundary recap

A container is a process isolated by namespaces and constrained using capabilities, cgroups, seccomp/LSM policy, filesystem mounts, and runtime configuration. It shares the host kernel. Therefore, a container boundary depends on both runtime configuration and kernel correctness.

The highest-risk configurations intentionally remove isolation: privileged mode, host PID/network namespaces, broad host mounts, device access, excessive capabilities, or access to the runtime socket.

## Kubernetes control plane

Kubernetes adds an orchestration/control plane around workloads. Major security-relevant components include:

- API server;
- authentication mechanisms;
- RBAC/authorization;
- admission control;
- controllers;
- scheduler;
- kubelet/node agents;
- etcd/state storage;
- cluster networking;
- workload/service-account identity.

The API server is the central policy gateway for desired-state changes.

## Authentication and authorization

Kubernetes can authenticate users and workloads through several mechanisms. After authentication, authorization—commonly RBAC—determines whether a subject may perform a verb on a resource within a scope.

RBAC is powerful because permissions can create other permissions. A role that can create pods may indirectly gain access to service-account tokens, mounted secrets, or node capabilities depending on cluster policy. Analyze effective privilege, not only role names.

## Service accounts

Pods often run with a Kubernetes service account. Tokens should have only the API permissions the workload requires. Modern projected service-account tokens are audience/lifetime bounded compared with historical long-lived token patterns.

Disable automatic token mounting for workloads that do not call the Kubernetes API.

## Admission control

Admission controllers evaluate API objects after authentication/authorization but before persistence. They can enforce pod security, image policy, required labels, allowed registries, resource limits, signature checks, or organization-specific invariants.

Authorization answers “may this caller create a pod?” Admission can answer “is this pod specification acceptable?”

## Pod security settings

Review workloads for:

- non-root user;
- no privilege escalation;
- minimal/drop capabilities;
- read-only root filesystem where feasible;
- seccomp profile;
- SELinux/AppArmor policy where available;
- no privileged mode;
- no host namespaces unless required;
- no broad hostPath mounts;
- controlled device access;
- resource limits.

These settings constrain the consequences of a compromised application.

## Secrets

Kubernetes Secrets are API objects, not a magical hardware vault. Access depends on RBAC, etcd encryption/configuration, node/pod exposure, and external secret integration. A pod that can read a secret effectively possesses it during runtime.

Prefer workload identity and short-lived credentials where services support them.

## Network policy

By default, many clusters allow broad pod-to-pod communication unless a network plugin/policy restricts it. NetworkPolicy can define allowed ingress/egress at workload labels/namespaces depending on implementation.

Segmentation reduces lateral reach but does not replace application authentication.

## Node trust

A node runs many pods and interacts with the control plane. Node compromise can affect workloads scheduled there and potentially credentials/tokens available to that node. Protect kubelet interfaces, node credentials, host OS, runtime, kernel, and cloud instance permissions.

Separate highly sensitive workloads where stronger isolation is required; consider sandboxed runtimes or VM-based isolation for specific threat models.

## Runtime socket risk

Access to a container runtime management socket can grant extremely broad control over host workloads. Do not mount runtime sockets into ordinary application containers merely for convenience. If an automation component truly needs runtime management, isolate and constrain it as privileged infrastructure.

## Image supply chain

Images should have known provenance, minimal content, pinned dependencies, vulnerability scanning, signature/attestation where appropriate, and reproducible build metadata. Runtime policy should complement CI controls.

Avoid mutable tags for security-critical deployment decisions when immutable digests are available.

## Kubernetes audit telemetry

API audit logs can show who requested which resource operation, from where, and with what result, depending on policy. Combine them with workload, node, cloud, admission, and network telemetry for investigation.

A detection should identify a meaningful behavior, such as unexpected privileged pod creation, broad RBAC changes, secret access anomalies, or service-account use from unusual contexts.

## Safe cluster lab

Use a disposable local cluster such as a VM-based or development cluster. Create two namespaces and synthetic service accounts. Grant one account read-only access to ConfigMaps in its namespace. Verify allowed and denied API operations using supported administrative tooling.

Then deploy a benign pod with deliberately weak security settings, inspect why policy allows it, and tighten an admission/pod security configuration. Do not attempt node/container escape.

## Attack-path reasoning

A cluster privilege graph can include:

`service account → RBAC create pods → pod can use stronger service account → access to namespace secret → cloud credential → external resource`.

The correct remediation can be at any edge: reduce RBAC, block service-account selection, remove secret, use workload identity, constrain network/cloud IAM, or isolate workloads.

## Guided study workflow

### Before you begin

Complete Modules 19, 21, 24, 41, 49, 74, and 76 when available.

### Practice task

Build a Kubernetes privilege graph for a tiny local cluster: users, service accounts, roles, role bindings, namespaces, secrets, pods, nodes, and external identity. Remove one unnecessary privilege edge and verify denial.

### Evidence to keep

RBAC manifests, pod security settings, denied/allowed API evidence, privilege graph, and audit excerpt if enabled.

### Common mistakes to avoid

- assuming RBAC names imply actual privilege;
- granting cluster-admin to fix deployment problems;
- mounting runtime sockets casually;
- treating Secrets as automatically encrypted from every threat;
- attempting escape techniques instead of proving dangerous configuration through policy evidence.

### Mastery check

Explain how Kubernetes authorization and Linux isolation combine, then trace one hypothetical workload-to-cloud attack path and identify controls at each edge.

### Continue with

Modules **76, 80, 81, and 85**.

---

# Cloud IAM, Control Planes, Metadata and Temporary Credentials

> **Purpose:** Understand cloud security at the authority-flow level: identities call control-plane APIs, workloads receive temporary credentials, policies combine across layers, and metadata/control-plane access can change blast radius.

## Learning objectives

- Distinguish human, workload, service, and federated identities.
- Reason about effective permissions across multiple policy layers.
- Understand temporary credentials, role assumption, metadata services, and identity federation.
- Analyze control-plane attack paths without attempting cloud compromise.
- Design least-privilege and telemetry verification in a sandbox account/project/subscription.

## Cloud security is API security at infrastructure scale

Most cloud infrastructure is controlled by authenticated APIs. Creating a VM, changing a firewall, reading object storage, attaching a role, rotating a key, altering logging, and creating a database are API-authorized state transitions.

Therefore, cloud security starts with **who can call which API on which resource under which conditions**. Network exposure matters, but identity and control-plane authority often matter more.

## Identity types

Cloud environments commonly include:

- human workforce identities;
- workload/service identities;
- managed identities/roles attached to compute;
- CI/CD identities;
- external/federated identities from an enterprise IdP;
- break-glass/emergency identities;
- vendor/integration identities.

Long-lived access keys should be minimized when short-lived federation or managed workload identity is available.

## Temporary credentials

Temporary credentials have a bounded lifetime and are frequently issued after a principal assumes a role or exchanges an identity assertion. They reduce the persistence of leaked credentials but still grant real authority while valid.

Security properties to review include audience, subject, role, session duration, source identity, conditions, session policy, revocation behavior, and logging.

## Effective permission

Cloud authorization is rarely a single allowlist. Effective permission can depend on identity policy, resource policy, organization policy, permission boundary, session constraints, network context, service-control rules, explicit denies, and service-specific behavior.

Do not infer privilege from one policy document. Evaluate the combined decision and test a narrow allowed/denied operation in the sandbox.

## Role assumption

Role assumption creates an authority edge from one principal to another role. Review both sides:

1. Can principal A request the role?
2. Does the role's trust policy accept A under the intended conditions?
3. What permissions does the resulting role session have?
4. Can the role assume additional roles?
5. Is the chain logged with source identity?

A role graph can reveal privilege paths that are not obvious from individual policies.

## Workload identity

Workloads need credentials to call managed services. Prefer platform mechanisms that issue short-lived identity bound to the workload rather than embedding API keys in images, environment files, or repositories.

The workload's identity should have only the operations required for its runtime task. Separate build-time, deploy-time, and runtime identities.

## Metadata services

Cloud compute platforms may expose instance/workload metadata through a link-local or platform-specific endpoint. Metadata can include identity credentials or configuration intended for the local workload.

The security issue arises when an application with server-side fetch capability can reach metadata it should not expose to the caller. Modern platforms provide stronger metadata protections, tokenized access, hop limits, identity isolation, and workload-specific mechanisms. Enable current platform controls and combine them with application SSRF defenses and egress policy.

This guide does not provide metadata credential-extraction payloads.

## Control plane versus data plane

**Control-plane** operations configure resources and policy. **Data-plane** operations use the resource: read an object, query a database, send a message. Permissions and logs can differ.

A principal may need data access but not permission to alter the resource policy. Separating those responsibilities limits privilege escalation paths.

## Organization-level guardrails

Large environments can apply policies above individual accounts/projects/subscriptions to prohibit dangerous configurations, require logging, restrict regions, control public exposure, or constrain identity behavior.

Guardrails should be designed as invariants and continuously tested. Exception processes need ownership and expiry.

## Secrets and key services

Managed secret/key systems centralize access control and auditing, but applications still need authority to retrieve/decrypt material. Review which identity can call the service, which keys can decrypt which data, rotation, backup/restore, and whether logs record access.

Envelope encryption separates data encryption keys from key-encryption keys and limits the amount of data directly processed by a central KMS.

## Public exposure

Cloud resources can become reachable through public IPs, load balancers, storage policies, serverless URLs, database settings, API gateways, or sharing links. An exposure inventory should join network reachability with identity policy and data sensitivity.

“Not in our VPC” does not mean “not exposed,” and “private IP” does not mean “authorized.”

## Cloud logging

At minimum, collect control-plane audit logs, identity/authentication events, network flow/edge logs where useful, workload/application logs, and security-service findings. Protect logs in a separate administrative/security boundary where feasible.

Detections should focus on meaningful authority changes: new privileged grants, logging disablement, public policy changes, unusual role assumption, new access keys, secret access anomalies, and unexpected region/account activity.

## Safe sandbox lab

Use a disposable cloud sandbox with budget controls or a local emulator. Create two roles: a reader and an administrator-equivalent test role. Allow a synthetic user to assume only the reader. Verify one allowed read-like API and one denied change operation.

Map the trust relationship and inspect audit logs. Then add a condition such as short session duration or a sandbox-specific tag and verify behavior.

## Privilege graph questions

- Who can create/modify identities?
- Who can attach policies?
- Who can assume privileged roles?
- Who can change resource policies?
- Which workloads can read secrets?
- Which CI jobs can deploy production?
- Who can disable/alter logging?
- Which identity can modify network exposure?
- Can one role grant itself more authority indirectly?

## Guided study workflow

### Before you begin

Complete Modules 19, 21, 22, 24, 39, 49, 61, and 75.

### Practice task

Build an identity/role/resource graph in a sandbox and verify at least five allow/deny expectations using read-only or reversible operations. Remove one unnecessary permission edge.

### Evidence to keep

Policy/trust excerpts, graph, audit records, and before/after effective-permission test.

### Common mistakes to avoid

- reading one policy in isolation;
- keeping long-lived keys because they are convenient;
- mixing build/deploy/runtime identities;
- treating metadata as ordinary public web content;
- testing against accounts/resources you do not own.

### Mastery check

Explain how a workload receives temporary authority, how a role assumption creates a graph edge, and why control-plane permission can matter more than network location.

### Continue with

Modules **75, 80, 81, and 85**.

---

# Network Protocol Reverse Engineering and Traffic Analysis

> **Purpose:** Learn how to reconstruct an unknown or poorly documented protocol from packet captures and a controlled implementation you own.

## Learning objectives

- Separate transport framing from application semantics.
- Infer fields, lengths, message types, state, checksums, and encodings.
- Use controlled input variation to identify field meaning.
- Distinguish encrypted, compressed, encoded, and binary data.
- Build a minimal protocol specification from evidence.

## Start below the application

Before interpreting payload bytes, identify transport facts: TCP, UDP, QUIC, Unix socket, serial, BLE characteristic, or another carrier. TCP is a byte stream, not a message protocol. Application message boundaries must be defined separately by lengths, delimiters, fixed-size records, higher-level framing, or connection lifecycle.

UDP preserves datagram boundaries but applications may still fragment logical messages themselves.

## Direction and roles

Determine which endpoint initiates the connection and which sends the first application message. Label directions `client → server` and `server → client` rather than relying on IP addresses that may change.

Identify handshake, steady-state requests, responses, keepalives, errors, and shutdown behavior.

## Capture discipline

For a protocol you own, capture one simple action at a time:

1. connect and do nothing;
2. connect and authenticate using synthetic credentials if the lab requires it;
3. perform action A once;
4. repeat A with one field changed;
5. perform action B;
6. intentionally cause a benign validation error;
7. disconnect cleanly.

The controlled variation makes field inference much stronger.

## Hex and ASCII views

Binary analysis uses both byte offsets and decoded representations. ASCII/UTF-8 text may be embedded among binary lengths and identifiers. Repeated constants can indicate magic values, protocol versions, opcodes, separators, or flags.

Do not assume a recognizable string means the entire protocol is text-based.

## Fixed header hypothesis

Many protocols start with a fixed header containing fields such as:

- magic/version;
- message type;
- flags;
- sequence/request ID;
- payload length;
- checksum;
- timestamp.

Compare multiple messages and mark bytes that remain constant, increment, correlate with payload size, or change with action type.

## Endianness

To infer integer byte order, choose a value you can control. If setting a synthetic count to `0x0102` yields bytes `01 02`, the field is big-endian; `02 01` suggests little-endian. Confirm with more than one value.

Network standards often use big-endian, but custom protocols may not.

## Length-prefixed framing

If a field changes exactly with message size, test whether it includes the header itself or only payload. A common parser bug occurs when sender and receiver disagree about units, signedness, maximum size, or nested lengths.

Your protocol specification should state exact offset, width, endian, allowed range, and whether the field includes headers.

## Type-length-value structures

TLV designs encode a type identifier, a length, then a value. Variants may align/pad fields, nest TLVs, or use variable-length integers. Once you suspect TLV, compare messages with optional fields and see whether unknown elements can be skipped based on their declared length.

## Checksums and integrity

A changing field near the end/header may be a checksum, MAC, or hash. A checksum detects accidental corruption but does not prove authenticity. A keyed MAC provides authenticity/integrity when keys are protected.

Do not attempt to defeat authentication in third-party protocols. In your own lab, simply identify whether a field changes with payload and consult source/specification afterward.

## Compression versus encryption

High-entropy payloads can result from encryption, compression, or encoded binary data. Clues include handshake negotiation, fixed magic headers, length behavior, repeated plaintext metadata, and whether identical inputs produce identical output.

Encryption should be assumed opaque unless you possess legitimate keys in your own environment.

## Stateful protocols

A message may only be valid after a handshake or prior state transition. Build a state diagram. Track sequence numbers, session IDs, negotiated version/features, authentication state, and timeouts.

Protocol security often fails when a parser accepts a message in the wrong state.

## Error messages as an oracle

In your own implementation, errors reveal parser expectations. Compare malformed-but-benign local inputs: truncated message, unsupported version, unknown type, invalid length. Map each failure to the validation stage.

A production protocol should avoid leaking unnecessary secrets while still logging enough server-side detail for diagnosis.

## Wireshark/tshark methodology

If using packet-analysis tools, begin with filters that isolate your own lab endpoints and one connection. Follow the stream, mark message boundaries, export only the payloads you are authorized to analyze, and annotate offsets.

A custom Wireshark dissector is an excellent advanced project after you understand the format. It turns reverse-engineered fields into reusable analysis and can improve defensive visibility.

## Python parser project

Once the format is understood, write a parser that:

- accepts bytes, not a network target;
- validates minimum header length;
- checks declared lengths before slicing;
- rejects unsupported versions/types;
- uses explicit endian conversions;
- returns structured fields;
- preserves unknown fields safely;
- never allocates unbounded memory from a declared length.

Then fuzz the parser locally using Module 68.

## Safe lab

Write a tiny localhost client/server with a custom frame: 4-byte magic, 1-byte version, 1-byte type, 2-byte big-endian payload length, payload. Capture three benign message types and reverse the format without looking at the server source. Then compare with source.

## Guided study workflow

### Before you begin

Complete Modules 08, 20, 51, 61, 68, and 78 when available.

### Practice task

Reverse-engineer a protocol you wrote yourself from a packet capture, then implement a standalone parser and a short specification.

### Evidence to keep

PCAP from the private lab, annotated hex, state diagram, inferred field table, parser, and source comparison.

### Common mistakes to avoid

- treating TCP packets as application messages;
- guessing endian from one sample;
- mistaking compression for encryption;
- capturing third-party/private traffic;
- writing a parser that trusts declared lengths.

### Mastery check

Given several captures, explain how you would infer framing, field width, endian, and state without access to source code.

### Continue with

Modules **78, 79, 80, 83, and 85**.

---

# TLS, PKI and Cryptographic Implementation Failures

> **Purpose:** Move from cryptographic primitives into real protocol assurance: identity, key exchange, certificate validation, downgrade resistance, nonce discipline, and implementation mistakes.

## Learning objectives

- Explain the security goals of modern TLS at a practical protocol level.
- Understand certificate chains, hostname validation, revocation limitations, and trust stores.
- Distinguish algorithm weakness from implementation/protocol misuse.
- Recognize nonce reuse, insecure randomness, key lifecycle, and side-channel concepts.
- Validate a localhost TLS deployment safely.

## Cryptography is a system, not an algorithm

Using AES or a modern elliptic curve does not automatically create a secure system. Security depends on mode, nonce generation, key derivation, certificate validation, protocol transcript binding, random number quality, key storage, error handling, and implementation behavior.

The most important rule is to use mature, reviewed protocol libraries rather than inventing cryptographic protocols.

## TLS goals

Modern TLS aims to provide confidentiality and integrity for a connection plus authentication of the server and optionally the client. TLS 1.3 simplifies the handshake and removes many legacy constructions, but configuration and certificate identity still matter.

A successful encrypted handshake to the wrong endpoint is not secure if certificate/hostname validation is disabled.

## Certificate chain

A server certificate is typically validated through one or more intermediate CAs to a trust anchor in the client's trust store. Validation includes signatures, validity periods, constraints, key usage, name constraints where applicable, and server-name identity.

The chain that a server sends and the trust anchor that a client already trusts are separate concepts.

## Hostname validation

Clients must verify that the certificate identity matches the intended DNS name according to current platform rules. Accepting any valid certificate regardless of name defeats server authentication.

Development environments sometimes disable verification to “make it work”; that habit must not leak into production code.

## Private PKI

Organizations may operate private CAs for internal services. Root keys are extremely sensitive and should be protected offline or in dedicated key-management/HSM infrastructure depending on risk. Intermediate CAs reduce direct root exposure.

Certificate issuance policy should bind identities to authorized subjects and support rotation/revocation processes.

## Forward secrecy

Ephemeral key exchange means compromise of a long-term server key does not automatically decrypt previously captured sessions. Modern TLS configurations use ephemeral key-agreement mechanisms to provide forward secrecy.

This property depends on protocol/version/cipher choices and correct implementation.

## Nonces and AEAD

Authenticated-encryption modes such as AES-GCM or ChaCha20-Poly1305 combine confidentiality and integrity but require correct nonce use. Reusing a nonce with the same key can catastrophically break security properties for some modes.

Applications should rely on high-level library APIs that manage nonce generation/counters safely and should never truncate authentication tags without a protocol design that explicitly justifies it.

## Randomness

Cryptographic keys, nonces, salts, tokens, and challenges need appropriate randomness. Use the OS cryptographic random generator through a secure library. Language-level pseudorandom functions intended for simulation/games are not necessarily suitable for secrets.

Entropy problems at device boot or embedded systems deserve special review.

## Password storage

Passwords should be processed with dedicated password-hashing/KDF algorithms using unique salts and appropriate cost parameters. A fast generic hash such as raw SHA-256 is not a password-storage design.

Pepper can add a separately protected secret layer in some architectures, but it complicates rotation/recovery and does not replace strong password hashing.

## Key derivation

Key Derivation Functions convert secret material into one or more cryptographic keys with domain separation/context. Reusing one raw key for unrelated purposes increases cross-protocol risk. Mature protocols derive separate traffic/exporter keys from a handshake secret.

## Downgrade resistance

Protocol negotiation must prevent an attacker from forcing both sides onto a weaker mutually supported option. Modern TLS removed many legacy modes and binds negotiation into authenticated transcript state.

Operationally, disable obsolete protocol versions/ciphers rather than relying solely on clients to choose the strongest option.

## Certificate revocation reality

Revocation mechanisms include CRLs and OCSP, while browsers/platforms use additional mechanisms and policies. Real-world revocation is complex because availability/privacy/performance interact. Short certificate lifetimes and automated renewal reduce reliance on emergency revocation for ordinary operation.

Understand your platform rather than assuming every client performs real-time OCSP checks.

## Side channels

An implementation can leak secrets through timing, cache behavior, power consumption, electromagnetic emissions, branch behavior, or error distinctions. Constant-time cryptographic libraries reduce selected timing risks.

Do not attempt side-channel attacks on devices you do not own. For a software lab, compare why secret-dependent branches are discouraged in cryptographic code.

## Padding and error oracles

Historic protocol failures have occurred when error behavior reveals whether decrypted structure or padding is valid. The deep lesson is that error channels can leak one bit at a time and turn a cryptographic check into an oracle.

Use modern AEAD protocols/libraries and uniform failure behavior rather than implementing custom CBC/padding schemes.

## Key lifecycle

Every key has generation, activation, storage, use, rotation, backup, revocation, recovery, and destruction stages. Most key-management failures are lifecycle failures, not broken math.

Document which principal/system can retrieve plaintext keys and which can only request cryptographic operations.

## Safe localhost TLS lab

Create a self-signed **lab** CA and a localhost certificate only if you understand the trust implications. Prefer a disposable browser/profile or command-line client configured to trust only that temporary CA. Observe successful validation, then demonstrate that a hostname mismatch is correctly rejected.

Delete the test trust anchor afterward so it cannot accidentally become a persistent trust expansion.

## Guided study workflow

### Before you begin

Complete Modules 20, 39, 49, 51, 52, and 77.

### Practice task

Document one local TLS handshake: endpoint identity, certificate chain, protocol version, key-exchange properties, and validation result. Test one expected failure such as wrong hostname.

### Evidence to keep

Temporary certificate metadata, sanitized client output, trust-chain diagram, and cleanup note confirming the temporary CA was removed.

### Common mistakes to avoid

- disabling certificate verification permanently;
- confusing encryption with authenticated identity;
- using generic hashes for password storage;
- reusing keys/nonces across contexts;
- inventing custom crypto protocols.

### Mastery check

Explain why a strong cipher with broken certificate validation is insecure and why nonce/key lifecycle can matter more than algorithm name.

### Continue with

Modules **79, 82, 83, and 84**.

---

# Malware Analysis and Behavioral Triage

> **Purpose:** Learn professional malware-analysis methodology using isolated samples and benign training binaries, with emphasis on understanding behavior, extracting defensive indicators, and protecting the analyst environment.

## Learning objectives

- Separate static triage, dynamic analysis, unpacking/obfuscation recognition, and reverse engineering.
- Build an isolated analysis environment and evidence workflow.
- Interpret imports, strings, persistence indicators, process/network/file behavior, and configuration.
- Produce defensive IOCs and behavior-based detections without developing malware.
- Understand the limitations of sandbox observations.

## Safety first

Unknown binaries can destroy data, steal tokens, encrypt files, spread over reachable networks, or detect analysis environments. Use purpose-built isolated VMs with snapshots, no personal accounts, no shared clipboard/folders unless necessary, synthetic data, and tightly controlled networking.

For this guide, prefer known benign training samples or binaries you write yourself to simulate behaviors. Do not download live malware merely to complete a lesson.

## Analysis phases

A disciplined workflow is:

1. provenance/hash and containment;
2. static triage;
3. behavioral hypotheses;
4. controlled dynamic execution if safe/authorized;
5. targeted reverse engineering;
6. configuration/IOC extraction;
7. detection opportunities;
8. remediation/context;
9. report and evidence cleanup.

Not every sample needs full disassembly.

## Static triage

Without execution, record file type, architecture, size, signatures, sections, imports, strings, resources, entropy patterns, packer/protector hints, and embedded URLs/domains. Compare hashes against internal threat intelligence where authorized.

Static clues prioritize dynamic observation. They are not proof that an import or string is actually used.

## Packing and obfuscation

Packers compress/encrypt code and restore it at runtime. Obfuscators alter control flow, names, strings, or data representation. Legitimate commercial software also uses these techniques.

Indicators include unusually small import tables, high-entropy executable sections, runtime memory allocation + permission changes, or a small stub that transfers control elsewhere. Treat these as hypotheses.

## Dynamic behavior

Observe in isolation:

- created/modified files;
- registry/config changes;
- new processes/threads;
- loaded modules;
- service/task/autostart changes;
- DNS/network attempts redirected to a safe sinkhole if needed;
- mutexes/pipes/IPC;
- logs and error behavior.

Behavior should be timestamped so events can be correlated.

## Process tree

A process tree helps explain execution chain. Record image, parent, command line, user/token, signer, hashes, start/end time, and major child relationships. Malware may inject or use legitimate processes, so parentage alone is not sufficient to attribute behavior.

## Persistence concepts

Persistence is any mechanism that causes code/access to survive restart, logon, or another lifecycle boundary. Categories include startup entries, services, scheduled tasks, browser extensions, application plugins, cloud persistence, identity modifications, and firmware-level mechanisms.

This module focuses on **detecting and removing** persistence. It does not provide instructions for hiding persistence.

## Network behavior

Capture DNS names, destination IPs, ports, TLS certificate metadata, HTTP host/path patterns, protocol timing, and connection periodicity in the isolated lab. Avoid contacting real command-and-control infrastructure; use blocked networking, simulation, or sinkholing under controlled conditions.

An IOC such as one IP may change quickly. Behavioral detections such as an unusual process creating persistence and immediately initiating outbound communication can be more durable.

## Configuration extraction

Malware families often store configuration such as domains, campaign IDs, encryption keys, mutex names, paths, or protocol constants in encoded/obfuscated form. Extracting configuration can improve detection and scoping.

Only analyze samples you are authorized to possess. Do not repurpose configuration to connect to criminal infrastructure.

## Behavioral signatures

A high-quality behavior description may be:

“Unsigned executable launched from user-writable directory creates a new autostart entry, writes a second executable, and starts outbound TLS shortly afterward.”

This is more resilient than a single file hash. Translate behaviors into telemetry requirements before writing rules.

## YARA concepts

YARA can identify file/memory patterns using strings and conditions. Good rules choose distinctive features while avoiding unstable absolute offsets or common library strings. Test rules against clean corpora to reduce false positives.

Avoid publishing overly specific sensitive detection logic if doing so would materially aid active evasion in a real incident; coordinate with defenders.

## Sandbox limitations

A sample may sleep, require user interaction, expect a particular locale/domain, need internet resources, or detect virtualization. “No behavior observed” does not mean “benign.” Static analysis and environment modeling are needed to interpret absence.

Do not disable safety controls merely to force a sample to execute. Use vetted research infrastructure when deeper analysis is necessary.

## Benign simulation lab

Write a harmless program that:

- creates a file in a temporary lab directory;
- spawns a child process that prints text;
- opens a localhost connection;
- writes a JSON configuration;
- exits.

Capture its process/file/network behavior and write a behavioral detection description. This teaches the analysis workflow without malicious capability.

## Report structure

- sample provenance/hash;
- environment;
- static characteristics;
- observed behaviors;
- confidence and gaps;
- IOCs with stability rating;
- behavioral detection opportunities;
- remediation/scoping recommendations;
- screenshots/log excerpts;
- cleanup/snapshot reset.

## Guided study workflow

### Before you begin

Complete Modules 07, 23, 37, 47, 64, 65, and 67.

### Practice task

Analyze a benign simulator or recognized safe training sample in an isolated VM. Produce a one-page behavior report and one non-destructive YARA-style or telemetry-based detection concept.

### Evidence to keep

Hash, static triage, timeline, process tree, file/network observations, and detection rationale.

### Common mistakes to avoid

- running unknown samples on a daily-use machine;
- letting a sample contact real infrastructure;
- treating one hash as a durable detection;
- assuming no sandbox behavior means benign;
- turning analysis into malware-development experimentation.

### Mastery check

Explain how static evidence, dynamic behavior, and reverse engineering support one another and identify what your analysis still cannot prove.

### Continue with

Modules **80, 81, 83, 84, and 85**.

---

# Advanced Detection Engineering and MITRE ATT&CK v19

> **Purpose:** Build detections from observable behavior, data-source reality, and testable hypotheses rather than from tool names or copied signatures.

## Learning objectives

- Convert threat behavior into data requirements and detection logic.
- Understand ATT&CK as a behavioral knowledge base, not a checklist of alerts.
- Design correlation, sequence, rarity, and stateful detections.
- Test false-positive assumptions with benign emulation.
- Track coverage and telemetry gaps explicitly.

## ATT&CK in 2026

MITRE ATT&CK **v19.2** is the current data release as of August 6, 2026. The major v19 release introduced on April 28, 2026 split the former Enterprise Defense Evasion tactic into **Stealth** and **Defense Impairment**. The v19.2 Agile update primarily refreshed Groups and Software rather than changing that tactic model.

Use the current ATT&CK website/data as the source of truth for technique IDs and relationships. Do not hard-code old tactic assumptions into long-lived analytics without version tracking.

## Start with behavior

A useful detection statement has this shape:

**When subject/process/workload X performs observable behavior Y under context Z, the combination is unusual or policy-violating because reason R.**

Then ask which telemetry can prove each part. If no data records the behavior, writing a query first is premature.

## Detection pipeline

1. Threat/behavior hypothesis.
2. Required data source and fields.
3. Collection validation.
4. Normalization.
5. Candidate logic.
6. Benign test data/emulation.
7. False-positive review.
8. Severity/context enrichment.
9. Alert routing and analyst procedure.
10. Versioning/tuning/retirement.

A detection is a maintained software artifact.

## Atomic versus correlated analytics

An **atomic** detection triggers on one event. A **correlated** detection combines events over time, identity, host, process tree, session, workload, or resource.

Examples of safe correlation concepts:

- privileged group change followed by privileged sign-in;
- new service configuration followed by service start;
- cloud role grant followed by sensitive API use;
- unusual child process followed by outbound connection;
- security control configuration change followed by telemetry loss.

Correlation often improves context but introduces state, timing, and data-quality complexity.

## Sequence detections

Some behaviors are suspicious because of order. Define expected time window, entity key, allowed interruptions, and reset conditions. Sequence logic can be brittle if clocks are skewed or event ingestion is delayed.

Always distinguish event time from ingest time.

## Rarity and baseline

Rarity can surface unusual process paths, parents, cloud APIs, geolocations, authentication methods, or service-account activity. But “rare” is not “malicious.” Baselines change with software releases and business cycles.

Use rarity to prioritize evidence, not as sole conviction.

## Entity context

Enrichment turns raw events into security meaning. Useful context includes asset criticality, user role, device management state, signer reputation, known automation, vulnerability exposure, network zone, tenant, and change-ticket context.

Enrichment should be versioned and explainable so analysts know why severity changed.

## Detection of defense impairment

Defense impairment covers actions that degrade logging, endpoint protection, firewall policy, cloud audit, authentication controls, or other security mechanisms. Build high-confidence alerts for unauthorized state changes to critical controls.

Avoid relying only on “absence of logs,” which can also result from pipeline failure. Pair telemetry health monitoring with configuration/audit events.

## Stealth-related behavior

Stealth behavior attempts to reduce observable signals or blend into expected activity. Defensive analytics should emphasize invariant violations and cross-source correlation rather than trying to guess every evasion trick.

Do not publish step-by-step evasion recipes in a training guide. Study the ATT&CK behavior descriptions and map them to telemetry/mitigations.

## Data quality

For every source document:

- who/what emits it;
- field semantics;
- timestamp source/timezone;
- retention;
- delay/drop behavior;
- identity/hostname stability;
- parsing/normalization transformations;
- known blind spots;
- sampling/filtering.

A perfect query over unreliable data is an unreliable detection.

## Sigma and portable logic

Sigma provides a portable rule representation for many log detections. Treat portable rules as source code requiring adaptation to your schema and environment. Field names, event IDs, command-line availability, and audit policy vary.

Test translated rules against real benign data before deployment.

## Network detections

Network analytics can use DNS, flow, TLS metadata, HTTP proxy logs, firewall events, and protocol-specific telemetry. Encrypted traffic reduces payload visibility but still leaves useful metadata depending on environment/privacy policy.

Focus on policy violations and unusual relationships rather than trying to decrypt traffic you are not authorized to inspect.

## Identity detections

High-value identity analytics include changes to privileged groups/roles, new credentials, impossible policy transitions, unusual service-account use, risky delegation changes, repeated authentication anomalies, and abnormal role-assumption chains.

Identity events need context from directory/cloud role state to avoid stale interpretations.

## Detection testing

Use benign simulations that create the intended telemetry without harmful payloads. Examples: create/delete a test local user, start a harmless test service, perform a denied cloud sandbox API action, or modify a lab logging setting and immediately restore it.

Record expected events before running the test. If the detection fails, determine whether the behavior did not emit data, collection dropped it, normalization lost fields, or logic is wrong.

## False positives and tuning

Do not simply exclude entire directories/users to quiet a rule. Understand legitimate behaviors and narrow with stable context: signer, managed software inventory, service account, approved automation, parent process, destination class, or change window.

Every suppression is a blind spot that should be documented and reviewed.

## Detection-as-code

Store rules, tests, sample sanitized events, metadata, owner, ATT&CK mapping, severity, data dependencies, and change history in version control. CI can lint rules and run test fixtures.

A rule without an owner and validation history decays quickly.

## Coverage metrics

ATT&CK technique counts are not sufficient. Better measures include:

- percentage of prioritized behaviors with validated telemetry;
- percentage with tested detections;
- false-positive burden;
- time from telemetry failure to detection;
- alert-to-investigation conversion;
- time since last validation;
- critical assets lacking expected data.

## Guided study workflow

### Before you begin

Complete Modules 12, 23, 26, 47, 59, 72–76, and 79.

### Practice task

Choose one benign behavior in a lab. Write the threat hypothesis, required fields, sample event, detection logic, expected false positives, and test procedure. Validate end-to-end collection.

### Evidence to keep

Rule/query, fixture event, ATT&CK version/mapping, test output, tuning notes, and telemetry dependency list.

### Common mistakes to avoid

- copying ATT&CK technique names directly into alerts;
- writing logic before verifying data exists;
- treating rarity as maliciousness;
- suppressing broad categories to reduce noise;
- testing evasion instead of validating observability.

### Mastery check

Explain the difference between technique coverage, telemetry coverage, and validated detection coverage, and demonstrate one end-to-end test.

### Continue with

Modules **81, 84, and 85**.

---

# Digital Forensics — Filesystem Timelines and Memory Artifacts

> **Purpose:** Deepen forensic reasoning: preserve evidence, understand filesystem metadata, construct timelines, correlate volatile and persistent artifacts, and communicate uncertainty.

## Learning objectives

- Distinguish acquisition, preservation, examination, analysis, and reporting.
- Understand common filesystem timestamp and metadata limitations.
- Build multi-source timelines with normalized time.
- Understand what memory can reveal that disk cannot and vice versa.
- Correlate identity, process, network, and persistence artifacts without overclaiming.

## Forensics is reconstruction under uncertainty

A forensic conclusion is an inference from artifacts left by systems. Artifacts may be incomplete, overwritten, tampered with, time-skewed, or generated by normal software. Strong analysis records both supporting and contradicting evidence and distinguishes observed fact from hypothesis.

## Evidence preservation

Before analysis, document source, collector, date/time/timezone, acquisition method, hashes, storage location, and access history appropriate to your organization. Work from copies when possible.

Do not collect more personal or confidential data than the investigation requires. Legal/HR/privacy requirements may constrain acquisition and retention.

## Filesystem metadata

Filesystems store metadata such as names, paths, size, ownership, permissions, allocation information, and timestamps. Semantics vary by filesystem and OS. A single “modified time” cannot answer every question.

For NTFS, analysts may encounter multiple timestamp sources and metadata structures; for ext-family filesystems and mobile storage, semantics differ. Learn the specific filesystem rather than applying one universal timestamp model.

## Timestamp caveats

Timestamps can change because of copying, extraction, backup/restore, software behavior, clock corrections, virtualization, or deliberate manipulation. Some timestamps have different precision or update rules.

Use timestamps as one evidence source and correlate with logs, process execution, network activity, package/application metadata, and user actions.

## Timeline normalization

Pick a canonical analysis timezone, often UTC, while preserving original timezone/offset. Record clock skew where known. Distinguish **event time**, **write time**, **collection time**, and **ingest time**.

A useful timeline row includes: normalized time, source, host, user/principal, artifact type, action, object, confidence, and raw reference.

## Super-timelines

A super-timeline merges many artifact sources: filesystem events, authentication logs, process telemetry, browser history, cloud audit, EDR, DNS, firewall, application logs, and memory artifacts.

The value is correlation. A process execution followed by a file write followed by a network connection is more informative than any one event alone.

## Process execution artifacts

Different operating systems record execution in different ways. Potential sources include event logs, EDR, shell/application history, prefetch-like mechanisms, service/task metadata, package records, and memory remnants.

Do not assume absence from one source proves the process never ran.

## Persistence review

For incident response, examine legitimate startup mechanisms: services, scheduled tasks, startup folders/registry, shell profiles, browser extensions, systemd units/timers, cron, launch mechanisms, cloud startup scripts, mobile app receivers, and management policies.

The objective is identify unexpected configuration and restore a known-good state, not to teach persistence creation.

## Memory forensics concepts

Volatile memory can contain process lists, mapped modules, open handles, network endpoints, command-line fragments, decrypted application data, cryptographic material, kernel structures, and artifacts of recently exited activity depending on platform and timing.

Memory collection is highly sensitive. It can contain passwords, tokens, messages, keys, and personal data. Restrict access and retention.

## Process-versus-module anomalies

Analysts compare expected process image, path, signer, loaded modules, memory mappings, thread start addresses, parent context, and executable permissions. An anomaly is a lead, not proof. Legitimate debuggers, JIT runtimes, security software, and updaters can create unusual patterns.

## Network artifacts

Correlate active/recent connections with process identity, DNS resolution, firewall/proxy logs, TLS metadata, and cloud/VPN logs. NAT and proxies can complicate attribution.

A remote IP alone rarely proves which user/process initiated activity.

## Browser and user artifacts

Browser history, downloads, cache, extensions, cookies, and local storage can provide context, but browser profiles contain personal/sensitive information. Scope searches narrowly and follow policy.

Downloads should be hashed and correlated with process execution rather than assumed malicious from filename alone.

## Cloud and SaaS forensics

Cloud audit logs may show role assumption, object access, policy changes, login events, OAuth grants, mailbox rules, file shares, and device/session information. Retention and licensing can limit history.

Preserve critical cloud logs early because some sources have short retention windows.

## Hypothesis-driven investigation

Instead of “look at everything,” write hypotheses:

- Did account A authenticate from a new context?
- Did process P create persistence?
- Did data object D leave the environment?
- Did role R gain unexpected authority?
- Did security control C stop reporting before or after event E?

For each, list evidence that would support, weaken, or falsify it.

## Root cause versus patient zero

The first observed alert is not necessarily the initial compromise or root cause. Work backward and forward from strong anchor events. Track gaps explicitly.

Avoid forcing a complete narrative when data cannot support one.

## Safe timeline lab

Generate synthetic activity on a disposable VM: log in, create a file, run a benign script, start/stop a test service, make a localhost request, and delete a temporary file. Collect available logs and filesystem metadata. Build a 10–20 event timeline and identify which actions are visible in which sources.

## Forensic report structure

- scope and authority;
- systems/accounts examined;
- acquisition details and hashes;
- time normalization and known skew;
- executive findings;
- detailed timeline;
- evidence per finding;
- confidence level;
- alternate explanations considered;
- containment/remediation;
- evidence retention/cleanup.

## Guided study workflow

### Before you begin

Complete Modules 23, 37, 47, 72–80.

### Practice task

Build a multi-source timeline from your synthetic lab activity. Deliberately omit one source, explain the resulting blind spot, then add it and update the conclusion.

### Evidence to keep

Timeline CSV/Markdown, source inventory, hashes where appropriate, timezone notes, and uncertainty annotations.

### Common mistakes to avoid

- treating one timestamp as definitive;
- collecting unrelated personal data;
- assuming missing telemetry means no activity;
- using mismatched timezones;
- presenting hypotheses as facts.

### Mastery check

Given three conflicting artifacts, explain how you would rank them, normalize time, and state a defensible conclusion with uncertainty.

### Continue with

Modules **82, 83, 84, and 85**.

---

# Android Application Reverse Engineering and Mobile App Internals

> **Purpose:** Deepen Android security analysis by connecting APK structure, bytecode/native code, manifests, components, IPC, signing, storage, WebView, and runtime behavior in apps you own or are authorized to test.

## Learning objectives

- Understand APK/AAB packaging, DEX, resources, manifests, and native libraries.
- Trace exported component and intent/Binder trust boundaries.
- Understand application signing and update identity.
- Review local storage, Keystore use, WebView bridges, and network security configuration.
- Perform static/dynamic analysis without bypassing another app's sandbox.

## Package anatomy

An installed Android application originates from one or more APKs generated from an app bundle or traditional package. APK content can include:

- `AndroidManifest.xml`;
- DEX bytecode;
- resources/assets;
- native `.so` libraries for supported ABIs;
- signing metadata;
- configuration/resources split across packages in modern delivery models.

Static analysis begins by identifying which code and resources actually ship to the device.

## DEX and ART

Java/Kotlin application code is compiled into DEX bytecode, then executed/compiled by Android Runtime mechanisms. Decompilers can reconstruct Java-like source, but names may be obfuscated and compiler-generated code can differ significantly from original Kotlin/Java.

Treat reconstructed source like pseudocode and confirm security-sensitive logic with bytecode/runtime behavior when needed.

## Manifest as attack-surface map

The manifest defines components, permissions, intent filters, SDK/version metadata, network/security settings, and exported behavior. Activities, services, receivers, and content providers can cross application boundaries when exported or otherwise reachable.

For each exported component, document required permission, accepted inputs, caller identity assumptions, returned data, and side effects.

## Intent trust boundaries

Intents can carry actions, categories, URIs, extras, and flags. An exported component must treat caller-controlled intent data as untrusted. Validate both syntax and authorization before performing sensitive work.

Explicit intents reduce accidental routing ambiguity but do not replace permission or caller validation when crossing app boundaries.

## Binder and IPC

Binder is Android's core IPC mechanism. Higher-level services, AIDL interfaces, content providers, and framework calls use Binder under the hood. IPC code can inspect caller identity in appropriate contexts, but identity can be lost if work is deferred incorrectly.

A privileged service should validate the caller before clearing identity or dispatching work to a context that no longer carries the original subject.

## Application sandbox

Each ordinary Android app runs under a distinct Linux UID with SELinux policy and platform restrictions. Private app data is inaccessible to other ordinary apps by default. Shared/external storage has different rules and should not be used for secrets merely because a filename is obscure.

Termux is also an app sandbox. It is excellent for learning and local tooling but does not automatically gain access to other apps' private data.

## Signing and update identity

Android app signing establishes the package's update identity and can participate in signature-level permissions. Protect signing keys and use supported key rotation/app-signing mechanisms. A leaked signing key can have long-lived ecosystem impact.

When analyzing an APK you own, compare signer/certificate fingerprints between builds to verify expected lineage.

## Network Security Configuration

Android apps can define trust anchors, cleartext policy, domain-specific TLS settings, and debug overrides. Debug-only trust exceptions should never become production defaults.

Certificate pinning can reduce selected PKI risks but adds rotation/availability complexity; use it only with an explicit threat model and operational plan.

## Keystore

Android Keystore can protect key material so cryptographic operations occur under platform/hardware-backed controls where supported. Key attestation and secure hardware can strengthen assurance, but application authorization and device state still matter.

Do not hard-code cryptographic keys in APK resources; static app packages should be assumed observable by users who possess the app.

## WebView

WebView embeds web content inside an app, bridging web and native trust models. Risks include unsafe URL loading, JavaScript interfaces, file/content access, mixed content, weak origin validation, and navigation to untrusted content.

A JavaScript bridge exposed to untrusted web content can become a privileged API. Keep interfaces minimal and restrict trusted origins/content.

## Deep links and app links

URI-based navigation can route external input into application states. Validate parameters and authorization after navigation. Verified App Links improve domain association but do not prove the user is authorized for the target object.

## Content providers

Content providers expose structured data/URIs and can enforce read/write permissions. Review exported state, URI grants, path permissions, query parameterization, and whether temporary grants outlive intended workflows.

## Native/JNI boundary

JNI connects managed Java/Kotlin code to native C/C++. It introduces memory-safety and type/lifetime boundaries. Validate array/string lengths and ownership. Native libraries should use platform hardening and be fuzzed where they parse untrusted input.

## Obfuscation

R8/ProGuard-like tools can rename/shrink code, which raises reverse-engineering cost but is not an authorization or secret-storage control. Secrets embedded in client code remain recoverable in principle.

## Dynamic analysis

For an app you own, use a debug build/emulator and platform-supported debugging/logging to observe lifecycle, network requests to your lab server, local files, and IPC. Avoid techniques designed to bypass anti-debugging or tamper protections in third-party apps.

## Static analysis lab

Create a small Android app or use an open-source training app you are authorized to inspect. Analyze:

- manifest exported components;
- permissions;
- deep links;
- network security config;
- WebView use;
- local storage choices;
- embedded native libraries;
- signer fingerprint.

Then compare findings with source/configuration.

## Termux role

Termux can organize APK hashes, notes, scripts, JSON/XML processing, local HTTP endpoints, and source repositories. Android sandbox restrictions may prevent direct inspection of another app's private runtime state; use emulator/debug tooling designed for the tested app rather than attempting to bypass the OS.

## Guided study workflow

### Before you begin

Complete Modules 17, 28–31, 39, 53–56, 63–67, and 78.

### Practice task

Analyze an Android app you built or a recognized training APK. Produce an exported-component map, data-storage inventory, network trust model, and one secure-code improvement.

### Evidence to keep

APK hash, signer fingerprint, manifest excerpts, component graph, source/decompiler comparison, and remediation note.

### Common mistakes to avoid

- treating obfuscation as secret protection;
- assuming deep-link verification equals authorization;
- exposing WebView bridges to arbitrary content;
- bypassing sandbox/debug restrictions in third-party apps;
- hard-coding secrets in client packages.

### Mastery check

Trace one external intent or deep link from entry point to data/action and identify every authorization/validation boundary.

### Continue with

Modules **83, 84, and 85**.

---

# Firmware, Embedded Systems and Hardware Interface Analysis

> **Purpose:** Deepen device security analysis using firmware structure, boot chains, update trust, debug interfaces, serial buses, filesystem images, and safe hardware-lab methodology.

## Learning objectives

- Understand a typical embedded boot chain from immutable/ROM code through bootloader, kernel/RTOS, and application.
- Identify firmware containers, filesystems, configuration, and update metadata.
- Understand UART, JTAG/SWD, SPI, I2C, and flash interfaces conceptually.
- Analyze update authenticity/rollback protections without bypassing them on third-party devices.
- Build a safe evidence workflow for hardware you own.

## Embedded threat model

Embedded devices may combine physical access, network services, radio interfaces, cloud management, mobile apps, update servers, and supply-chain trust. Unlike a server, a device can be stolen and probed physically, so secrets and trust anchors must tolerate hostile possession according to the product threat model.

## Boot chain

A secure boot chain typically starts from a small immutable or hardware-protected root of trust. Each stage verifies the next stage before transferring control. Measured boot can additionally record hashes into protected registers for later attestation.

The chain is only as strong as its key provisioning, rollback protection, verification coverage, and recovery/update paths.

## Firmware images

A firmware file may be:

- raw flash image;
- vendor container with headers/checksums/signatures;
- compressed archive;
- partitioned disk image;
- filesystem image;
- encrypted/signed update package;
- delta patch.

Start with file signatures, entropy, strings, and container metadata. Do not flash modified firmware onto safety-critical devices for experimentation.

## Filesystems

Common embedded filesystems include squashfs, cramfs, ext variants, UBIFS/JFFS2, FAT, and vendor formats. Extracted files can reveal web UI assets, configuration defaults, startup scripts, certificates, and binaries.

Finding a credential-looking string is not proof it is active. Determine whether it is an example, default, test artifact, hash, certificate, or runtime secret.

## UART

UART provides asynchronous serial communication and is commonly exposed as pads/headers during development. It may provide boot logs, diagnostics, or a console depending on product configuration.

Before connecting hardware, identify voltage levels and ground. Incorrect voltage can damage the device. Use a USB-UART adapter designed for the voltage; do not connect power pins unless you understand the board.

This guide limits labs to devices you own and does not provide methods to bypass login or protected boot.

## JTAG and SWD

JTAG and Serial Wire Debug are hardware debugging interfaces used for testing/programming processors. Production devices may disable, lock, authenticate, or restrict them because unrestricted debug can expose memory and firmware.

A security review should verify intended lifecycle state: development units may allow debug; production units should enforce the product's debug policy.

## SPI and flash

External flash chips may store bootloader, firmware, filesystem, or configuration. Board schematics/datasheets can identify buses and voltage. Reading chips requires careful electrical handling and may violate warranty or device integrity.

For training, use a development board designed for experimentation rather than consumer/safety equipment.

## I2C

I2C connects sensors, secure elements, EEPROMs, and peripherals over a shared bus. It was not originally designed as a hostile network. Threat models involving physical attackers must consider whether sensitive operations rely on unauthenticated bus messages.

Modern secure elements can provide authenticated cryptographic operations rather than exposing raw keys over general-purpose buses.

## Secrets at rest

Device secrets may live in secure elements, TPM-like components, one-time-programmable fuses, encrypted flash, filesystem files, environment blocks, or compiled constants. The security question is whether an attacker with the assumed physical access can extract or reuse them.

Per-device keys limit fleet-wide impact compared with one global key.

## Firmware update security

A secure updater should verify authenticity and integrity before activation, protect against unauthorized downgrade, handle power failure safely, and support recovery without creating an unsigned bypass path.

Separate transport security from package authenticity. HTTPS protects delivery in transit; the device should still verify a signed update package so mirrors/storage cannot substitute arbitrary firmware.

## Rollback protection

If an attacker can install an older correctly signed but vulnerable image, signature verification alone is insufficient. Anti-rollback can use monotonic version counters or hardware-backed state.

Recovery images also need version/security policy.

## Hardware root of trust

A hardware root can anchor secure boot, attestation, device identity, or key storage. But system security still depends on software policy using the root correctly. A secure element cannot fix an application that authorizes the wrong user.

## Safe firmware lab

Use an inexpensive development board or firmware image explicitly licensed for study. Record hash and extract the image read-only. Identify architecture, filesystem, startup configuration, network service configuration, certificate stores, and update metadata.

If using a board UART, capture boot logs only. Do not alter fuses, boot protection, or debug locks as part of the guide.

## Firmware SBOM and provenance

Embedded products contain bootloaders, kernels, libraries, web servers, language runtimes, and vendor components. Maintain an SBOM where practical, track CVEs against actual version/configuration, and preserve build provenance for updates.

Long device lifetimes make patch/update strategy a product requirement, not an afterthought.

## Guided study workflow

### Before you begin

Complete Modules 18, 20, 49, 54, 63, 64, 67, 77, and 78.

### Practice task

Analyze a training firmware image or development board you own. Produce a boot/update trust diagram and inventory exposed hardware/software interfaces.

### Evidence to keep

Image hash, extraction notes, architecture/filesystem evidence, interface photos/labels if appropriate, boot log, and trust diagram.

### Common mistakes to avoid

- connecting unknown voltage pins;
- treating HTTPS as sufficient firmware authenticity;
- assuming a string is a live credential;
- experimenting on safety-critical/third-party hardware;
- disabling debug/boot protections merely to “see if possible.”

### Mastery check

Explain secure boot versus measured boot versus signed update and identify where rollback protection fits.

### Continue with

Modules **84 and 85**.

---

# Patch Diffing, Vulnerability Root Cause and Secure Regression Analysis

> **Purpose:** Learn how to study security fixes in software you maintain or public patches after disclosure, identify the underlying bug class, and build durable regression tests without converting patches into weaponized exploits.

## Learning objectives

- Separate symptom patch from root-cause fix.
- Compare source/binary versions to identify security-relevant changes.
- Infer the violated invariant from a patch.
- Search for variant/sibling bugs using safe static reasoning.
- Turn a patch into tests, hardening, and secure-development lessons.

## Why patch analysis matters

Security advisories often summarize impact at a high level. The actual patch can teach much more: which trust assumption was wrong, which validation was missing, which lifetime was mishandled, or which state transition lacked authorization.

Defenders and developers should study patches to prevent variants, not merely apply them.

## Start with source when available

For open-source or internal code you are authorized to examine, compare the fixed and vulnerable revisions. Ask:

- Which functions changed?
- Which data types/lengths changed?
- Was a new bounds/permission/state check added?
- Did ownership/lifetime change?
- Did parsing move before or after authentication?
- Did a default change from allow to deny?
- Did new logging reveal previously silent failure?

The smallest textual diff is not necessarily the full conceptual fix.

## Security invariant extraction

Rewrite the patch as an invariant. Examples:

- declared length must not exceed remaining buffer;
- object tenant must equal authenticated tenant;
- only verified package signatures may reach activation;
- token audience must equal this service;
- privileged helper must resolve and authorize the same file object;
- state transition must be atomic and single-use.

Once the invariant is explicit, search for other places where the same invariant should hold.

## Variant analysis

A variant is a related bug caused by the same conceptual mistake in another code path, data type, protocol version, or component. Search by semantics rather than copy/pasted lines.

If a parser fixed one 16-bit length, inspect sibling length fields and nested structures. If one API added tenant authorization, inspect bulk/export/background-worker paths. If one service corrected a writable config path, inventory similar privileged services.

## Binary diffing

When source is unavailable but analysis is authorized, compare symbols, imports, function sizes, strings, control-flow graphs, and changed basic blocks between versions. Compiler/build differences can create enormous noise, so exact build provenance matters.

Use public/owned binaries and focus on understanding the fix. This guide does not provide steps to transform a diff into a working exploit.

## Patch timing and exposure

When a vendor releases a fix, organizations need to understand:

- which versions/configurations are affected;
- whether the vulnerable feature is enabled/reachable;
- internet/internal exposure;
- privileges required;
- available compensating controls;
- telemetry for attempted exploitation;
- rollback/deployment risk;
- whether active exploitation is known from authoritative sources.

This turns “CVSS number” into operational prioritization.

## Regression test design

A regression test should represent the bug class with the smallest safe input/state. For memory issues, test invalid lengths/lifetimes under sanitizers. For authorization, test subjects/resources across boundaries. For parser differentials, test canonical equivalents. For concurrency, create repeatable race-invariant tests where feasible.

The test should fail on the vulnerable build and pass on the fixed build without requiring harmful exploitation.

## Negative tests

Security regression suites need negative cases: invalid token, wrong tenant, expired state, malformed length, unauthorized role, unsigned artifact, unexpected redirect destination, untrusted origin.

A system tested only for success tends to accumulate missing-deny bugs.

## Hardening after root cause

Fix source first, then ask what defense-in-depth would reduce future impact:

- safer language/library;
- sanitizer/fuzzing coverage;
- compiler hardening;
- sandbox/least privilege;
- egress restriction;
- centralized authorization;
- schema validation;
- code review/static analysis rule;
- logging/detection;
- architectural simplification.

## Security advisories

A good advisory gives affected versions, impact, preconditions, fixed versions, mitigations/workarounds, acknowledgments, and references without unnecessary exploit detail. Coordinate disclosure timelines with maintainers and affected downstream users.

## Public patch ethics

Once a patch is public, studying it is legitimate research, but publishing a turnkey exploit can increase harm while users are still patching. Prefer educational root-cause analysis, defensive indicators, and safe regression tests.

Follow project disclosure policies and laws applicable to your environment.

## Safe source-diff lab

Create a small parser or authorization function with a deliberate harmless bug in git. Commit it, fix the invariant in the next commit, and compare:

```console
git diff HEAD~1..HEAD
```

Write a security note that explains the root cause without relying on the line numbers alone. Add a regression test, then search the project for the same conceptual pattern.

## Advanced case-study method

For a public vulnerability after vendor disclosure:

1. read the vendor advisory;
2. identify affected component/version;
3. read the fix commit if available;
4. state the invariant;
5. identify the bug class;
6. list preconditions and mitigations;
7. design a non-weaponized regression test concept;
8. map telemetry that could detect abuse;
9. extract a secure-coding lesson.

Do not reproduce exploitation against public targets.

## Guided study workflow

### Before you begin

Complete Modules 05, 26, 40, 53, 61, 65–80.

### Practice task

Perform patch analysis on a bug you create in your own toy project or a fully disclosed public fix. Produce invariant, root cause, variant search, regression test, and hardening recommendations.

### Evidence to keep

Commit hashes, diff excerpt, invariant statement, regression test, variant-search notes, and security advisory draft.

### Common mistakes to avoid

- assuming the changed line is the full root cause;
- reproducing a public exploit when a regression test is enough;
- searching only for identical syntax rather than conceptual variants;
- ignoring build/configuration exposure;
- treating patch deployment as the end of learning.

### Mastery check

Given a security patch, explain the invariant it restores and identify at least three places to search for variants.

### Continue with

Module **85** and revisit the relevant specialization track.

---

# Advanced Authorized Capstones

> **Purpose:** Integrate the advanced modules into realistic, evidence-driven security projects that prove deep understanding without attacking third-party systems.

## Capstone rules

Every capstone must use one of these environments:

- software you wrote;
- infrastructure/accounts you own;
- intentionally vulnerable training systems;
- a CTF whose rules explicitly permit the tested technique;
- an environment covered by written authorization.

Do not expand scope because a neighboring system looks interesting. Advanced skill includes restraint and evidence discipline.

## Deliverables for every capstone

Produce:

1. scope/authorization statement;
2. architecture/trust-boundary diagram;
3. threat model and invariants;
4. test plan;
5. environment versions/hashes;
6. evidence;
7. findings with confidence and impact;
8. remediation;
9. regression/detection tests;
10. cleanup/recovery proof;
11. lessons learned.

## Capstone 1 — Binary assurance pipeline

Build a small native parser you own. Compile debug and hardened builds. Inspect ELF/PE metadata, disassemble key functions, run sanitizers, create a fuzz harness, triage one controlled failure, fix it, and add regression tests.

**Skills:** Modules 62–68, 84.

**Success criterion:** You can connect source invariant → assembly/binary representation → runtime evidence → fix without producing an exploit payload.

## Capstone 2 — Local web trust-boundary review

Build a localhost application with two users, two tenants, reverse proxy, cache layer if available, and API endpoints. Define authorization matrix, origin policy, cache rules, forwarded-header trust, redirect policy, and server-side fetch restrictions.

Test only benign representations and negative authorization cases. Fix one intentionally introduced logic/configuration error.

**Skills:** Modules 52, 61, 68–71, 78, 84.

## Capstone 3 — Enterprise identity graph

Create a disposable Windows lab domain with synthetic users/groups/service accounts/GPOs. Map Kerberos roles, group nesting, directory ACLs, service identities, and GPO authority.

Introduce one intentionally excessive test permission, prove the resulting graph path administratively, remove it, and verify the path is gone. Do not dump credentials or forge tickets.

**Skills:** Modules 21, 32, 72, 73, 80, 81.

## Capstone 4 — Linux isolation report

On a disposable Linux VM, run a containerized service and inventory credentials, capabilities, namespaces, cgroups, seccomp/LSM, mounts, network reachability, and service user.

Harden the workload by dropping unnecessary capabilities, making filesystem regions read-only where possible, applying resource limits, and restricting network access.

**Skills:** Modules 24, 33, 62, 74, 75, 80.

## Capstone 5 — Kubernetes privilege graph

Use a local development cluster. Create namespaces, synthetic service accounts, RBAC roles, and a benign workload. Build an authority graph covering API permissions, secret access, pod creation, node boundary, and external/cloud identity if present.

Remove one unnecessary edge and verify both denial and audit visibility.

**Skills:** Modules 19, 21, 24, 49, 75, 76, 80.

## Capstone 6 — Cloud IAM sandbox

In a disposable cloud sandbox, model humans, workloads, roles, trust policies, secrets, and control-plane permissions. Use only low-cost/reversible resources.

Demonstrate least-privilege with a reader role that can perform expected reads but cannot change policy or create privileged resources. Confirm control-plane logging.

**Skills:** Modules 19, 21, 49, 61, 76, 80, 81.

## Capstone 7 — Protocol reverse engineering

Write a custom localhost protocol, capture it, then pretend you lost the source. Infer framing, endian, message types, request IDs, state, and errors. Implement a parser/dissector and fuzz it.

Compare the final inferred specification with original source.

**Skills:** Modules 51, 61, 68, 77, 78.

## Capstone 8 — Malware-analysis simulation

Use a harmless simulator that creates temporary files, starts a child process, touches a test configuration, and makes a localhost connection. Analyze it as if it were suspicious.

Build a timeline, process tree, static triage, behavior report, and one detection rule/query concept. Reset the environment afterward.

**Skills:** Modules 07, 23, 37, 64, 67, 79–81.

## Capstone 9 — Android application security review

Build or choose an open-source training Android app. Review manifest, exported components, deep links, storage, network security config, WebView, Keystore usage, native libraries, and signer identity.

Trace one external input to a sensitive action and confirm server-side/IPC authorization.

**Skills:** Modules 17, 39, 53–56, 63–67, 78, 82.

## Capstone 10 — Firmware trust chain

Use a development board or training firmware image. Identify image/container format, filesystem, boot components, update metadata, signing/trust design, rollback model, exposed interfaces, and network services.

Do not disable boot/debug protections. The project is a **trust review**, not a bypass challenge.

**Skills:** Modules 18, 49, 54, 64, 67, 77, 78, 83.

## Capstone 11 — Detection engineering lifecycle

Choose one benign lab behavior and implement the complete lifecycle: hypothesis, telemetry requirements, event generation, collection, normalization, rule, test fixture, false-positive analysis, ATT&CK v19.2 mapping, and analyst procedure.

Measure what happens when telemetry is unavailable.

**Skills:** Modules 12, 23, 47, 59, 80, 81.

## Capstone 12 — Patch-to-prevention study

Select a bug in your own code or a fully disclosed public fix. Reconstruct the root cause, write the invariant, build a safe regression, search for variants, identify defense-in-depth controls, and create a short advisory.

**Skills:** Modules 40, 61, 65–68, 84.

## Capstone 13 — Termux security research workstation

Use Termux as the organization/analysis layer for a safe project:

- Git repository for notes/scripts;
- Python virtual environment if needed;
- hashes of lab artifacts;
- offline search with `Hacking Guide Project.py`;
- local parser/fuzz harness;
- localhost HTTP service;
- structured reports exported to shared storage only when needed.

Document Android/Termux limitations instead of trying to defeat them.

**Skills:** Modules 28–31, 36, 51, 61, 68, 77.

## Capstone 14 — Incident reconstruction tabletop

Create synthetic endpoint, identity, DNS, cloud, and application logs for a fictional incident. Seed several benign distractors and three related suspicious events. Give the dataset to another learner without the answer.

They must produce timeline, hypotheses, evidence, uncertainty, containment plan, and detection improvement. Compare with the scenario design.

**Skills:** Modules 23, 37, 47, 72, 76, 80, 81.

## Capstone 15 — Security architecture review

Design a small SaaS system with browser/mobile clients, API gateway, application services, database, object storage, background queue, identity provider, CI/CD, cloud roles, observability, and backups.

Create asset/identity/data/privilege/dependency/observation graphs. Define 25 security invariants and map each to preventive and detective controls.

**Skills:** Modules 21, 22, 39–41, 49, 61, 69–76, 80.

## Scoring rubric

Score each capstone from 0–4 in these dimensions:

- **Scope discipline** — authorization and boundaries explicit.
- **System model** — accurate components/identities/trust edges.
- **Technical depth** — explains internals, not only tools.
- **Evidence** — minimal, reproducible, correctly interpreted.
- **Security reasoning** — invariant/root cause/impact clear.
- **Remediation** — addresses root cause and defense in depth.
- **Validation** — regression/detection proves the fix.
- **Communication** — report understandable to technical and non-technical readers.
- **Cleanup** — lab restored and sensitive artifacts handled safely.

A strong portfolio contains a few capstones scored deeply rather than dozens of shallow screenshots.

## Advanced mastery checklist

Before calling yourself comfortable with the advanced track, you should be able to:

- read basic x86-64 and ARM64 control flow;
- explain executable loading and dynamic linking;
- triage a crash and identify root cause with sanitizers/debuggers;
- design a fuzz harness and minimize a failure;
- reverse a small binary you compiled;
- reason about HTTP intermediaries and parser boundaries;
- build an API authorization matrix/state machine;
- explain Kerberos and AD privilege graphs;
- distinguish Windows tokens/ACLs/privileges;
- distinguish Linux namespaces/cgroups/seccomp/LSM;
- explain Kubernetes RBAC plus runtime isolation;
- map cloud IAM/role/metadata trust;
- reverse a simple custom protocol;
- explain TLS identity/nonce/key lifecycle;
- analyze a benign suspicious binary safely;
- build and validate a detection;
- construct a forensic timeline;
- review an Android package and firmware trust chain;
- convert a security patch into an invariant/regression test.

## Guided study workflow

### Before you begin

Complete the foundational path and the prerequisite modules for your chosen capstone. Read `ADVANCED-TRACK.md` and `LAB-GUIDE.md`.

### Practice task

Complete one capstone end-to-end and have another person reproduce at least one result using only your documentation.

### Evidence to keep

Keep the final report, diagrams, source/configuration, sanitized evidence, regression/detection tests, and cleanup record.

### Common mistakes to avoid

- maximizing tool count instead of depth;
- omitting the expected invariant;
- treating a screenshot as sufficient evidence;
- skipping remediation validation;
- leaving vulnerable lab services exposed;
- expanding scope beyond authorization.

### Mastery check

A capstone is complete when you can explain **system → trust boundary → hypothesis → evidence → root cause → impact → fix → verification** without depending on unexplained commands.

### Continue with

From the main menu, open **Learning paths**, revisit weak areas with the Advanced path, then specialize in reverse engineering, exploit-research foundations, identity, protocols, or detection.

---

# IPv6 Security, Neighbor Discovery and Modern LAN Attack Surfaces

IPv6 changes host discovery, address assignment, local-link trust, routing behavior, firewall assumptions, and evidence collection. This lesson treats IPv6 as a first-class security architecture rather than an optional extension of IPv4.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, or lab environments you own or are explicitly authorized to test. The exercises in this module are designed to prove security properties without targeting third parties.

## Learning objectives

By the end of this module you should be able to:

- Explain **Address architecture** and connect it to a concrete trust boundary or security invariant.
- Explain **Neighbor Discovery** and connect it to a concrete trust boundary or security invariant.
- Explain **SLAAC and DHCPv6** and connect it to a concrete trust boundary or security invariant.
- Explain **Extension headers** and connect it to a concrete trust boundary or security invariant.
- Explain **Fragmentation and PMTUD** and connect it to a concrete trust boundary or security invariant.
- Explain **Dual-stack exposure** and connect it to a concrete trust boundary or security invariant.

## Analysis method

Use the shared [Study Method](../Guides/STUDY-METHOD.md). For this module, first draw the relevant components and state transitions, then state one security invariant and identify the minimum evidence needed to test it safely.

## Deep concepts

### 1. Address architecture

Global unicast, unique-local, link-local, multicast, temporary/privacy addresses, and interface identifiers have different security and observability implications. Security reviews should identify which address classes are expected on each interface and which should never cross a routing boundary.



### 2. Neighbor Discovery

IPv6 replaces ARP with ICMPv6 Neighbor Discovery. Router Advertisements, Neighbor Solicitations, Neighbor Advertisements, and Redirects are control-plane messages; filtering them blindly can break connectivity, while trusting them blindly can create local-network risk.



### 3. SLAAC and DHCPv6

Stateless autoconfiguration and DHCPv6 can coexist. A network can therefore have several sources of addressing, DNS configuration, and default-route state. Asset inventories and NAC controls need to account for those sources rather than assuming one DHCP lease equals one endpoint.



### 4. Extension headers

IPv6 extension headers separate optional functions from the fixed header. Security devices must parse chains consistently, apply bounded work, and avoid policy gaps caused by unusual ordering, fragmentation, or unsupported combinations.



### 5. Fragmentation and PMTUD

Only endpoints fragment ordinary IPv6 packets. Path MTU Discovery and ICMPv6 Packet Too Big messages are operationally important; over-aggressive ICMPv6 blocking can create reliability failures that masquerade as application problems.



### 6. Dual-stack exposure

A service hardened on IPv4 can remain reachable through IPv6. Every listening socket, ACL, reverse proxy, VPN rule, DNS record, and monitoring pipeline should be checked for parity across both protocol families.



### 7. Local-link trust

First-hop security depends on switch features, RA policy, segmentation, endpoint firewalls, and predictable configuration. Treat the local segment as potentially hostile rather than assuming devices sharing a VLAN are mutually trusted.



### 8. Telemetry

Useful IPv6 evidence includes address lifetimes, RA sources, neighbor-cache changes, DNS AAAA responses, route changes, firewall decisions, and application bind addresses. Normalize addresses before correlation to avoid equivalent textual forms being treated as different hosts.



## Review focus

Apply the failure-mode taxonomy in [Study Method](../Guides/STUDY-METHOD.md), but keep the analysis specific to this lesson: identify the principal, resource, authority, mutable state, parser or policy boundary, and the telemetry that would distinguish a real control failure from misconfiguration or an observation gap.

## Authorized exercises

### Exercise 1 — Build a two-host or two-namespace IPv6-only localhost lab and document addresses, routes, neighbor entries, and DNS behavior without sending traffic outside the lab

Build a two-host or two-namespace IPv6-only localhost lab and document addresses, routes, neighbor entries, and DNS behavior without sending traffic outside the lab.


### Exercise 2 — Compare an application bound to 127

Compare an application bound to 127.0.0.1, ::1, 0.0.0.0, and :: in an owned environment; record exactly which interfaces become reachable.


### Exercise 3 — Create a firewall-review worksheet that checks IPv4 and IPv6 policy parity for one lab service

Create a firewall-review worksheet that checks IPv4 and IPv6 policy parity for one lab service.

Use the lab-record format in [Study Method](../Guides/STUDY-METHOD.md) for each exercise and keep all inputs synthetic or confined to the authorized lab.

## Knowledge checks

1. Explain the most important trust boundary in **IPv6 Security, Neighbor Discovery and Modern LAN Attack Surfaces** without naming a security tool.
2. Give one example where cryptographic or authentication success still does **not** imply authorization success.
3. Describe one stale-state or replay condition relevant to this module.
4. Identify one telemetry source that can support a strong conclusion and one blind spot it still leaves.
5. Explain how you would turn a discovered weakness into a regression test rather than a one-time finding.

## Guided study workflow

Use [Study Method](../Guides/STUDY-METHOD.md). Complete at least one authorized exercise, preserve the evidence that supports your conclusion, and explain the module's main trust boundary and failure modes in your own words before moving on.

### Continue with

Choose **Learning paths** from the main menu for an ordered specialization, or use **Search lessons** to follow a concept into related modules.

---

# DNS, Routing, BGP and Internet Infrastructure Security

Internet security depends on naming and routing systems that are distributed, cached, policy-driven, and only partially under any single organization’s control. This module explains the trust model and failure modes without treating Internet infrastructure as a target.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, or lab environments you own or are explicitly authorized to test. The exercises in this module are designed to prove security properties without targeting third parties.

## Learning objectives

By the end of this module you should be able to:

- Explain **DNS resolution chain** and connect it to a concrete trust boundary or security invariant.
- Explain **DNSSEC** and connect it to a concrete trust boundary or security invariant.
- Explain **Registrar and zone control** and connect it to a concrete trust boundary or security invariant.
- Explain **Anycast and recursive services** and connect it to a concrete trust boundary or security invariant.
- Explain **BGP path selection** and connect it to a concrete trust boundary or security invariant.
- Explain **Route-origin validation** and connect it to a concrete trust boundary or security invariant.

## Analysis method

Use the shared [Study Method](../Guides/STUDY-METHOD.md). For this module, first draw the relevant components and state transitions, then state one security invariant and identify the minimum evidence needed to test it safely.

## Deep concepts

### 1. DNS resolution chain

Stub resolvers, recursive resolvers, authoritative servers, delegations, caching, negative caching, and DNSSEC each participate in answering a name. A useful investigation separates “who asked,” “who recursed,” “who is authoritative,” and “what was cached.”



### 2. DNSSEC

DNSSEC provides origin authentication and integrity for signed DNS data; it does not encrypt queries and it does not make a maliciously registered domain trustworthy. Validation failures should be distinguished from ordinary NXDOMAIN, SERVFAIL, and transport failures.



### 3. Registrar and zone control

Domain takeover risk often begins in account security, delegation mistakes, stale records, or forgotten cloud resources rather than in the DNS protocol itself. Protect registrar identity, enforce MFA, inventory NS/DS records, and track ownership of every externally referenced resource.



### 4. Anycast and recursive services

Large DNS services commonly use anycast. The same service address can terminate at different sites, so latency, path, and incident evidence can vary geographically even when the logical destination is unchanged.



### 5. BGP path selection

BGP exchanges reachability between autonomous systems. Routing policy, prefix specificity, local preference, AS paths, communities, and business relationships influence which path is selected; BGP is not a shortest-path protocol in the ordinary sense.



### 6. Route-origin validation

RPKI and route-origin validation help networks evaluate whether an AS is authorized to originate a prefix. They improve one part of routing assurance but do not prove the entire AS path is legitimate.



### 7. Control-plane monitoring

Defenders should baseline authoritative DNS changes, certificate issuance, route announcements, RPKI state, nameserver changes, and cloud endpoint ownership. External control-plane drift can be an early sign of configuration failure or account compromise.



### 8. Resilience design

Use multiple authoritative DNS servers/providers where appropriate, protect registrar recovery, document TTL strategy, maintain break-glass contacts, and rehearse domain/routing incident playbooks before an outage occurs.



## Review focus

Apply the failure-mode taxonomy in [Study Method](../Guides/STUDY-METHOD.md), but keep the analysis specific to this lesson: identify the principal, resource, authority, mutable state, parser or policy boundary, and the telemetry that would distinguish a real control failure from misconfiguration or an observation gap.

## Authorized exercises

### Exercise 1 — Trace the full resolution path for a domain you own using passive/publicly documented information and draw the delegation chain

Trace the full resolution path for a domain you own using passive/publicly documented information and draw the delegation chain.


### Exercise 2 — Create a tabletop exercise for accidental deletion of a DNS zone and list recovery dependencies in order

Create a tabletop exercise for accidental deletion of a DNS zone and list recovery dependencies in order.


### Exercise 3 — Build a worksheet that separates DNS integrity, DNS confidentiality, registrar security, certificate issuance, and routing security controls

Build a worksheet that separates DNS integrity, DNS confidentiality, registrar security, certificate issuance, and routing security controls.

Use the lab-record format in [Study Method](../Guides/STUDY-METHOD.md) for each exercise and keep all inputs synthetic or confined to the authorized lab.

## Knowledge checks

1. Explain the most important trust boundary in **DNS, Routing, BGP and Internet Infrastructure Security** without naming a security tool.
2. Give one example where cryptographic or authentication success still does **not** imply authorization success.
3. Describe one stale-state or replay condition relevant to this module.
4. Identify one telemetry source that can support a strong conclusion and one blind spot it still leaves.
5. Explain how you would turn a discovered weakness into a regression test rather than a one-time finding.

## Guided study workflow

Use [Study Method](../Guides/STUDY-METHOD.md). Complete at least one authorized exercise, preserve the evidence that supports your conclusion, and explain the module's main trust boundary and failure modes in your own words before moving on.

### Continue with

Choose **Learning paths** from the main menu for an ordered specialization, or use **Search lessons** to follow a concept into related modules.

---

# Enterprise Wireless, WPA3, 802.1X and Wi-Fi 6/6E/7 Security

Modern wireless security is primarily an identity, configuration, RF exposure, and endpoint-trust problem. This module goes beyond password-centric Wi-Fi discussions and focuses on enterprise authentication, management-frame protection, segmentation, roaming, and observability.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, or lab environments you own or are explicitly authorized to test. The exercises in this module are designed to prove security properties without targeting third parties.

## Learning objectives

By the end of this module you should be able to:

- Explain **WPA3 modes** and connect it to a concrete trust boundary or security invariant.
- Explain **802.1X architecture** and connect it to a concrete trust boundary or security invariant.
- Explain **Protected management frames** and connect it to a concrete trust boundary or security invariant.
- Explain **Roaming and key hierarchy** and connect it to a concrete trust boundary or security invariant.
- Explain **6 GHz and newer bands** and connect it to a concrete trust boundary or security invariant.
- Explain **Guest and IoT segmentation** and connect it to a concrete trust boundary or security invariant.

## Analysis method

Use the shared [Study Method](../Guides/STUDY-METHOD.md). For this module, first draw the relevant components and state transitions, then state one security invariant and identify the minimum evidence needed to test it safely.

## Deep concepts

### 1. WPA3 modes

WPA3-Personal uses SAE while enterprise deployments can use stronger enterprise profiles. Security depends on client support, transition-mode choices, credential lifecycle, and whether legacy compatibility silently lowers guarantees.



### 2. 802.1X architecture

Supplicant, authenticator, and authentication server are distinct roles. EAP method selection, server-certificate validation, identity privacy, and RADIUS security determine whether enterprise authentication actually resists impersonation.



### 3. Protected management frames

802.11w/PMF protects selected management frames from forgery. Requiring PMF where the device population supports it reduces a class of local disruption and downgrade opportunities, but does not replace good RF and identity design.



### 4. Roaming and key hierarchy

Fast roaming improves mobility but expands the importance of key hierarchy, controller trust, AP configuration consistency, and client behavior. Security reviews should understand where authentication state is cached and which components can authorize movement between APs.



### 5. 6 GHz and newer bands

Wi-Fi 6E/7 introduce new channel/band behavior and often stronger baseline security requirements. Inventory tools and monitoring must support those bands or the organization can create blind spots by upgrading the WLAN faster than its sensors.



### 6. Guest and IoT segmentation

Guest, BYOD, managed endpoints, and embedded devices should not receive the same trust merely because they share wireless infrastructure. Use role/identity-based policy and explicit east-west restrictions.



### 7. Rogue and misconfigured infrastructure

A rogue AP, accidental hotspot, duplicate SSID, weak transition network, or incorrectly trusted EAP certificate can undermine an otherwise strong design. Detection should emphasize configuration drift and identity validation, not just SSID names.



### 8. Wireless evidence

Preserve controller logs, RADIUS outcomes, AP associations, client identity, channel/BSSID information, DHCP/DNS data, and timestamps. RF observations alone rarely establish who the user was or what authorization decision occurred.



## Review focus

Apply the failure-mode taxonomy in [Study Method](../Guides/STUDY-METHOD.md), but keep the analysis specific to this lesson: identify the principal, resource, authority, mutable state, parser or policy boundary, and the telemetry that would distinguish a real control failure from misconfiguration or an observation gap.

## Authorized exercises

### Exercise 1 — Design three WLAN roles—managed, guest, IoT—and write the exact trust assumptions and allowed flows between them

Design three WLAN roles—managed, guest, IoT—and write the exact trust assumptions and allowed flows between them.


### Exercise 2 — On equipment you own, inspect whether client devices validate the expected enterprise authentication certificate and document the trust path

On equipment you own, inspect whether client devices validate the expected enterprise authentication certificate and document the trust path.


### Exercise 3 — Create an upgrade checklist for moving from a mixed WPA2/WPA3 deployment to a stricter policy without stranding unsupported devices

Create an upgrade checklist for moving from a mixed WPA2/WPA3 deployment to a stricter policy without stranding unsupported devices.

Use the lab-record format in [Study Method](../Guides/STUDY-METHOD.md) for each exercise and keep all inputs synthetic or confined to the authorized lab.

## Knowledge checks

1. Explain the most important trust boundary in **Enterprise Wireless, WPA3, 802.1X and Wi-Fi 6/6E/7 Security** without naming a security tool.
2. Give one example where cryptographic or authentication success still does **not** imply authorization success.
3. Describe one stale-state or replay condition relevant to this module.
4. Identify one telemetry source that can support a strong conclusion and one blind spot it still leaves.
5. Explain how you would turn a discovered weakness into a regression test rather than a one-time finding.

## Guided study workflow

Use [Study Method](../Guides/STUDY-METHOD.md). Complete at least one authorized exercise, preserve the evidence that supports your conclusion, and explain the module's main trust boundary and failure modes in your own words before moving on.

### Continue with

Choose **Learning paths** from the main menu for an ordered specialization, or use **Search lessons** to follow a concept into related modules.

---

# GraphQL, gRPC, WebSockets and Real-Time API Security

Modern applications expose more than REST. GraphQL, gRPC, WebSockets, server-sent events, and asynchronous APIs move authorization and resource-control decisions into different protocol shapes. Security testing must follow the application’s state model, not assume every request is a simple HTTP endpoint.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, or lab environments you own or are explicitly authorized to test. The exercises in this module are designed to prove security properties without targeting third parties.

## Learning objectives

By the end of this module you should be able to:

- Explain **GraphQL schema surface** and connect it to a concrete trust boundary or security invariant.
- Explain **Query complexity** and connect it to a concrete trust boundary or security invariant.
- Explain **Object and field authorization** and connect it to a concrete trust boundary or security invariant.
- Explain **gRPC semantics** and connect it to a concrete trust boundary or security invariant.
- Explain **WebSocket lifecycle** and connect it to a concrete trust boundary or security invariant.
- Explain **Realtime multi-tenancy** and connect it to a concrete trust boundary or security invariant.

## Analysis method

Use the shared [Study Method](../Guides/STUDY-METHOD.md). For this module, first draw the relevant components and state transitions, then state one security invariant and identify the minimum evidence needed to test it safely.

## Deep concepts

### 1. GraphQL schema surface

A GraphQL schema exposes types, fields, arguments, mutations, and relationships. Authorization must be enforced on resolvers and business objects, not inferred from whether a field is hidden from introspection.



### 2. Query complexity

Nested queries, aliases, batching, pagination, and expensive resolvers can amplify backend work. Define query-depth/complexity budgets, data-loader behavior, timeouts, and per-principal resource limits.



### 3. Object and field authorization

A user allowed to read an object may not be allowed to read every field or invoke every mutation. Model object-level, property-level, and function-level authorization separately.



### 4. gRPC semantics

gRPC uses HTTP/2 framing and strongly typed protobuf messages, but serialization does not provide authorization. Interceptors, metadata, service/method policy, message limits, deadline propagation, and reflection exposure need explicit review.



### 5. WebSocket lifecycle

Authorization can change after a WebSocket upgrade. Validate the initial handshake, authenticate subscriptions/actions, handle token expiry/revocation, enforce message-size/rate limits, and close stale sessions deliberately.



### 6. Realtime multi-tenancy

Subscriptions and event channels can leak cross-tenant data if routing keys, topics, or filters are built from attacker-controlled identifiers without server-side ownership checks.



### 7. Protocol translation

Gateways often translate JSON/HTTP into gRPC or events. Security assumptions can be lost when one layer normalizes headers, paths, identities, or error codes differently from the next.



### 8. Observability

Log principal, operation/method, object or tenant scope, complexity/cost, result class, and correlation IDs. Avoid logging raw secrets or entire message bodies by default.



## Review focus

Apply the failure-mode taxonomy in [Study Method](../Guides/STUDY-METHOD.md), but keep the analysis specific to this lesson: identify the principal, resource, authority, mutable state, parser or policy boundary, and the telemetry that would distinguish a real control failure from misconfiguration or an observation gap.

## Authorized exercises

### Exercise 1 — Implement a tiny localhost GraphQL-like toy resolver in Python and write authorization tests for object and field access without exposing it beyond loopback

Implement a tiny localhost GraphQL-like toy resolver in Python and write authorization tests for object and field access without exposing it beyond loopback.


### Exercise 2 — Model a WebSocket session as states: unauthenticated, authenticated, reauthenticated, revoked, closed; define allowed messages in each state

Model a WebSocket session as states: unauthenticated, authenticated, reauthenticated, revoked, closed; define allowed messages in each state.


### Exercise 3 — Create a gRPC security review checklist covering identity propagation, method authorization, deadlines, message limits, and logging

Create a gRPC security review checklist covering identity propagation, method authorization, deadlines, message limits, and logging.

Use the lab-record format in [Study Method](../Guides/STUDY-METHOD.md) for each exercise and keep all inputs synthetic or confined to the authorized lab.

## Knowledge checks

1. Explain the most important trust boundary in **GraphQL, gRPC, WebSockets and Real-Time API Security** without naming a security tool.
2. Give one example where cryptographic or authentication success still does **not** imply authorization success.
3. Describe one stale-state or replay condition relevant to this module.
4. Identify one telemetry source that can support a strong conclusion and one blind spot it still leaves.
5. Explain how you would turn a discovered weakness into a regression test rather than a one-time finding.

## Guided study workflow

Use [Study Method](../Guides/STUDY-METHOD.md). Complete at least one authorized exercise, preserve the evidence that supports your conclusion, and explain the module's main trust boundary and failure modes in your own words before moving on.

### Continue with

Choose **Learning paths** from the main menu for an ordered specialization, or use **Search lessons** to follow a concept into related modules.

---

# Database, Data-Layer and Query-Engine Security

Database security is broader than SQL injection. It includes identity, query construction, stored logic, tenancy, replication, backups, search engines, caching, encryption, and data lifecycle. This module teaches how to reason from a data asset to every component that can read or mutate it.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, or lab environments you own or are explicitly authorized to test. The exercises in this module are designed to prove security properties without targeting third parties.

## Learning objectives

By the end of this module you should be able to:

- Explain **Query construction** and connect it to a concrete trust boundary or security invariant.
- Explain **Database identity** and connect it to a concrete trust boundary or security invariant.
- Explain **Row and tenant isolation** and connect it to a concrete trust boundary or security invariant.
- Explain **Stored logic and triggers** and connect it to a concrete trust boundary or security invariant.
- Explain **NoSQL and search engines** and connect it to a concrete trust boundary or security invariant.
- Explain **Replication and backups** and connect it to a concrete trust boundary or security invariant.

## Analysis method

Use the shared [Study Method](../Guides/STUDY-METHOD.md). For this module, first draw the relevant components and state transitions, then state one security invariant and identify the minimum evidence needed to test it safely.

## Deep concepts

### 1. Query construction

Parameterized queries separate code from data for supported values, but dynamic identifiers, sort expressions, filters, and stored procedures still require allowlisting and careful composition.



### 2. Database identity

Applications should use narrowly scoped service identities rather than owner/admin accounts. Distinguish schema migration privileges, runtime read/write privileges, analytics access, backup access, and emergency administration.



### 3. Row and tenant isolation

Multi-tenant systems need authorization at every path that reaches tenant data. Row-level security can add defense in depth, but application context, connection pooling, background jobs, exports, and caches must preserve tenant identity correctly.



### 4. Stored logic and triggers

Triggers, procedures, functions, extensions, and scheduled jobs execute inside a privileged data plane. Review ownership, definer/invoker behavior, search paths, extension provenance, and change control.



### 5. NoSQL and search engines

Document stores, key-value systems, and search engines have their own query languages and authorization models. Treat user-controlled operators, field selection, scriptable queries, and administrative APIs as distinct attack surfaces.



### 6. Replication and backups

Replicas, WAL/binlog streams, snapshots, exports, and backups are copies of sensitive data. Encryption, access control, retention, deletion, and restoration testing must include them.



### 7. Encryption boundaries

At-rest encryption protects media and some snapshot scenarios but does not stop an authorized database process from reading plaintext. Field-level/application-layer encryption changes key management and query capabilities and should be used intentionally.



### 8. Audit and anomaly detection

High-value events include privilege changes, schema changes, mass reads, unusual export jobs, authentication anomalies, failed authorization, and access from unexpected application identities.



## Review focus

Apply the failure-mode taxonomy in [Study Method](../Guides/STUDY-METHOD.md), but keep the analysis specific to this lesson: identify the principal, resource, authority, mutable state, parser or policy boundary, and the telemetry that would distinguish a real control failure from misconfiguration or an observation gap.

## Authorized exercises

### Exercise 1 — Build a localhost SQLite or PostgreSQL toy application with separate migration and runtime roles; document which statements each role should be able to execute

Build a localhost SQLite or PostgreSQL toy application with separate migration and runtime roles; document which statements each role should be able to execute.


### Exercise 2 — Create a tenant-isolation test matrix that covers API calls, background jobs, exports, caching, and administrative tools

Create a tenant-isolation test matrix that covers API calls, background jobs, exports, caching, and administrative tools.


### Exercise 3 — Take a harmless sample backup, restore it into an isolated lab, and verify the restore procedure includes permissions and secrets—not just data files

Take a harmless sample backup, restore it into an isolated lab, and verify the restore procedure includes permissions and secrets—not just data files.

Use the lab-record format in [Study Method](../Guides/STUDY-METHOD.md) for each exercise and keep all inputs synthetic or confined to the authorized lab.

## Knowledge checks

1. Explain the most important trust boundary in **Database, Data-Layer and Query-Engine Security** without naming a security tool.
2. Give one example where cryptographic or authentication success still does **not** imply authorization success.
3. Describe one stale-state or replay condition relevant to this module.
4. Identify one telemetry source that can support a strong conclusion and one blind spot it still leaves.
5. Explain how you would turn a discovered weakness into a regression test rather than a one-time finding.

## Guided study workflow

Use [Study Method](../Guides/STUDY-METHOD.md). Complete at least one authorized exercise, preserve the evidence that supports your conclusion, and explain the module's main trust boundary and failure modes in your own words before moving on.

### Continue with

Choose **Learning paths** from the main menu for an ordered specialization, or use **Search lessons** to follow a concept into related modules.

---

# Message Queues, Event Streaming and Distributed-System Security

Event-driven systems move trust through brokers, topics, schemas, consumers, retries, and background workers. Security failures often appear as confused-deputy problems, cross-tenant routing mistakes, replay, or privilege hidden inside automation.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, or lab environments you own or are explicitly authorized to test. The exercises in this module are designed to prove security properties without targeting third parties.

## Learning objectives

By the end of this module you should be able to:

- Explain **Producer and consumer identity** and connect it to a concrete trust boundary or security invariant.
- Explain **Topic and routing design** and connect it to a concrete trust boundary or security invariant.
- Explain **Message authenticity and replay** and connect it to a concrete trust boundary or security invariant.
- Explain **Schema evolution** and connect it to a concrete trust boundary or security invariant.
- Explain **Retries and idempotency** and connect it to a concrete trust boundary or security invariant.
- Explain **Dead-letter queues** and connect it to a concrete trust boundary or security invariant.

## Analysis method

Use the shared [Study Method](../Guides/STUDY-METHOD.md). For this module, first draw the relevant components and state transitions, then state one security invariant and identify the minimum evidence needed to test it safely.

## Deep concepts

### 1. Producer and consumer identity

Treat every producer and consumer as a principal with explicit topic/queue permissions. Avoid one broad service credential shared by unrelated workloads.



### 2. Topic and routing design

Names, routing keys, partitions, consumer groups, and dead-letter destinations can carry tenant or sensitivity boundaries. Authorization should not rely solely on a client choosing the “right” topic.



### 3. Message authenticity and replay

Transport encryption protects links; it does not necessarily prove an old message is fresh or that an authorized producer created it. For high-risk workflows consider identifiers, timestamps, deduplication, signatures/MACs, and idempotency.



### 4. Schema evolution

Loose schemas can allow security-relevant fields to appear, disappear, or change meaning. Version schemas, validate at trust boundaries, and define safe defaults for unknown fields.



### 5. Retries and idempotency

At-least-once delivery means a consumer may process the same event more than once. Security-sensitive actions such as payments, account changes, or provisioning need idempotency keys and replay-aware state transitions.



### 6. Dead-letter queues

Dead-letter storage often contains malformed or sensitive payloads and can become a forgotten data repository. Protect access, define retention, and prevent automated reprocessing from bypassing the original validation path.



### 7. Background privilege

Workers frequently hold broader permissions than front-end services. Map what each worker can do, what message fields influence that behavior, and whether a less-trusted producer can indirectly invoke privileged operations.



### 8. Distributed tracing

Correlation IDs, producer identity, consumer identity, schema version, retry count, and outcome make event chains explainable. Observability should support reconstruction without recording unnecessary secrets.



## Review focus

Apply the failure-mode taxonomy in [Study Method](../Guides/STUDY-METHOD.md), but keep the analysis specific to this lesson: identify the principal, resource, authority, mutable state, parser or policy boundary, and the telemetry that would distinguish a real control failure from misconfiguration or an observation gap.

## Authorized exercises

### Exercise 1 — Model an order-processing pipeline with producer, broker, three consumers, dead-letter queue, and admin replay tool; mark each trust boundary

Model an order-processing pipeline with producer, broker, three consumers, dead-letter queue, and admin replay tool; mark each trust boundary.


### Exercise 2 — Write test cases for duplicate delivery, out-of-order delivery, expired messages, malformed schemas, and unauthorized routing using toy data

Write test cases for duplicate delivery, out-of-order delivery, expired messages, malformed schemas, and unauthorized routing using toy data.


### Exercise 3 — Design a least-privilege matrix for producers and consumers and identify where one compromised workload would currently have excessive reach

Design a least-privilege matrix for producers and consumers and identify where one compromised workload would currently have excessive reach.

Use the lab-record format in [Study Method](../Guides/STUDY-METHOD.md) for each exercise and keep all inputs synthetic or confined to the authorized lab.

## Knowledge checks

1. Explain the most important trust boundary in **Message Queues, Event Streaming and Distributed-System Security** without naming a security tool.
2. Give one example where cryptographic or authentication success still does **not** imply authorization success.
3. Describe one stale-state or replay condition relevant to this module.
4. Identify one telemetry source that can support a strong conclusion and one blind spot it still leaves.
5. Explain how you would turn a discovered weakness into a regression test rather than a one-time finding.

## Guided study workflow

Use [Study Method](../Guides/STUDY-METHOD.md). Complete at least one authorized exercise, preserve the evidence that supports your conclusion, and explain the module's main trust boundary and failure modes in your own words before moving on.

### Continue with

Choose **Learning paths** from the main menu for an ordered specialization, or use **Search lessons** to follow a concept into related modules.

---

# OAuth 2.0 Security BCP, OIDC Federation and Token Defense

Modern OAuth security guidance has moved beyond older deployment patterns. This module centers RFC 9700/BCP 240 concepts, authorization-code flows with PKCE, sender constraints, redirect integrity, token audience, and the difference between authorization delegation and identity.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, or lab environments you own or are explicitly authorized to test. The exercises in this module are designed to prove security properties without targeting third parties.

## Learning objectives

By the end of this module you should be able to:

- Explain **OAuth roles and purpose** and connect it to a concrete trust boundary or security invariant.
- Explain **Authorization code and PKCE** and connect it to a concrete trust boundary or security invariant.
- Explain **Redirect URI integrity** and connect it to a concrete trust boundary or security invariant.
- Explain **Issuer and mix-up defenses** and connect it to a concrete trust boundary or security invariant.
- Explain **Token audience and scope** and connect it to a concrete trust boundary or security invariant.
- Explain **Refresh tokens** and connect it to a concrete trust boundary or security invariant.

## Analysis method

Use the shared [Study Method](../Guides/STUDY-METHOD.md). For this module, first draw the relevant components and state transitions, then state one security invariant and identify the minimum evidence needed to test it safely.

## Deep concepts

### 1. OAuth roles and purpose

Resource owner, client, authorization server, and resource server are different roles. OAuth delegates authorization; OpenID Connect adds an identity layer. Confusing an access token with an ID token is a recurring design error.



### 2. Authorization code and PKCE

Authorization-code flows keep access tokens out of front-channel URLs. PKCE binds the authorization response to the initiating client instance and is a key defense for public clients and modern deployments.



### 3. Redirect URI integrity

Redirect URIs are security-critical. Use exact matching according to the protocol profile, avoid open redirectors, and treat mobile/custom URI handling and claimed HTTPS links as platform-specific trust decisions.



### 4. Issuer and mix-up defenses

Clients interacting with multiple authorization servers need strong issuer binding and metadata validation so a response from one security domain is not accepted in another context.



### 5. Token audience and scope

A resource server should validate issuer, audience/resource, signature/key, expiry, and authorization claims appropriate to that API. Scope strings are not a substitute for object-level authorization.



### 6. Refresh tokens

Refresh tokens are long-lived authorization artifacts. Rotation, sender constraints, secure storage, revocation, inactivity limits, and anomaly detection reduce the impact of theft.



### 7. Sender-constrained tokens

Mechanisms such as mTLS or proof-of-possession approaches can bind a token to a client-held key. They change the theft model but do not fix an over-privileged token or a compromised client.



### 8. Federation lifecycle

Identity-provider federation adds metadata, signing keys, trust anchors, account linking, tenant discovery, session propagation, logout, and deprovisioning. Model the full lifecycle, not only the login redirect.



## Review focus

Apply the failure-mode taxonomy in [Study Method](../Guides/STUDY-METHOD.md), but keep the analysis specific to this lesson: identify the principal, resource, authority, mutable state, parser or policy boundary, and the telemetry that would distinguish a real control failure from misconfiguration or an observation gap.

## Authorized exercises

### Exercise 1 — Draw an authorization-code + PKCE sequence for a localhost demo and label every value that must be bound to the initiating transaction

Draw an authorization-code + PKCE sequence for a localhost demo and label every value that must be bound to the initiating transaction.


### Exercise 2 — Create a token-validation checklist separating cryptographic validity from authorization decisions at the API

Create a token-validation checklist separating cryptographic validity from authorization decisions at the API.


### Exercise 3 — Review a hypothetical federation design for account-linking ambiguity, stale signing keys, incorrect issuer/audience checks, and deprovisioning gaps

Review a hypothetical federation design for account-linking ambiguity, stale signing keys, incorrect issuer/audience checks, and deprovisioning gaps.

Use the lab-record format in [Study Method](../Guides/STUDY-METHOD.md) for each exercise and keep all inputs synthetic or confined to the authorized lab.

## Knowledge checks

1. Explain the most important trust boundary in **OAuth 2.0 Security BCP, OIDC Federation and Token Defense** without naming a security tool.
2. Give one example where cryptographic or authentication success still does **not** imply authorization success.
3. Describe one stale-state or replay condition relevant to this module.
4. Identify one telemetry source that can support a strong conclusion and one blind spot it still leaves.
5. Explain how you would turn a discovered weakness into a regression test rather than a one-time finding.

## Guided study workflow

Use [Study Method](../Guides/STUDY-METHOD.md). Complete at least one authorized exercise, preserve the evidence that supports your conclusion, and explain the module's main trust boundary and failure modes in your own words before moving on.

### Continue with

Choose **Learning paths** from the main menu for an ordered specialization, or use **Search lessons** to follow a concept into related modules.

---

# Authorization Models: RBAC, ABAC, ReBAC and Policy Engines

Authorization is the core question “may this principal perform this action on this resource under these conditions?” This module treats authorization as a graph/state problem and shows how models such as RBAC, ABAC, ReBAC, ACLs, and policy engines fail when context or lifecycle is incomplete.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, or lab environments you own or are explicitly authorized to test. The exercises in this module are designed to prove security properties without targeting third parties.

## Learning objectives

By the end of this module you should be able to:

- Explain **Reference monitor** and connect it to a concrete trust boundary or security invariant.
- Explain **RBAC** and connect it to a concrete trust boundary or security invariant.
- Explain **ABAC** and connect it to a concrete trust boundary or security invariant.
- Explain **ReBAC** and connect it to a concrete trust boundary or security invariant.
- Explain **Deny and default semantics** and connect it to a concrete trust boundary or security invariant.
- Explain **Caching** and connect it to a concrete trust boundary or security invariant.

## Analysis method

Use the shared [Study Method](../Guides/STUDY-METHOD.md). For this module, first draw the relevant components and state transitions, then state one security invariant and identify the minimum evidence needed to test it safely.

## Deep concepts

### 1. Reference monitor

A strong authorization design has a small, consistently invoked decision point, complete mediation, trustworthy inputs, and auditable policy. Scattered ad hoc checks tend to drift.



### 2. RBAC

Roles simplify permission management but can create role explosion and over-broad bundles. Separate business roles from technical implementation roles and review inherited privileges.



### 3. ABAC

Attribute-based decisions combine properties of users, resources, actions, and environment. The security problem shifts to attribute provenance, freshness, default behavior, and policy complexity.



### 4. ReBAC

Relationship-based models express ownership, membership, hierarchy, and sharing. Graph traversal rules must define direction, transitivity, cycles, revocation, and the maximum relationship depth considered.



### 5. Deny and default semantics

Policy engines differ in how they combine permits, denies, errors, and missing data. A safe design documents fail-open/fail-closed behavior for every dependency.



### 6. Caching

Authorization caches improve performance but create revocation windows. Cache keys must include all security-relevant context, and invalidation needs to be designed rather than hoped for.



### 7. Administrative authorization

Who may change policy is often more important than the policy language itself. Separate policy authorship, deployment, emergency override, and audit responsibilities.



### 8. Testing policy

Test positive, negative, boundary, stale-attribute, cross-tenant, inherited-role, revoked-access, and dependency-failure cases. Property-based tests can be useful for invariants such as “no user can read another tenant without an explicit relationship.”



## Review focus

Apply the failure-mode taxonomy in [Study Method](../Guides/STUDY-METHOD.md), but keep the analysis specific to this lesson: identify the principal, resource, authority, mutable state, parser or policy boundary, and the telemetry that would distinguish a real control failure from misconfiguration or an observation gap.

## Authorized exercises

### Exercise 1 — Model a file-sharing application using RBAC and then ReBAC; compare which rules become simpler and which new risks appear

Model a file-sharing application using RBAC and then ReBAC; compare which rules become simpler and which new risks appear.


### Exercise 2 — Write an authorization decision table with principal, action, resource, tenant, relationship, device posture, and time context

Write an authorization decision table with principal, action, resource, tenant, relationship, device posture, and time context.


### Exercise 3 — Create regression tests for revocation and stale-cache behavior in a toy policy evaluator

Create regression tests for revocation and stale-cache behavior in a toy policy evaluator.

Use the lab-record format in [Study Method](../Guides/STUDY-METHOD.md) for each exercise and keep all inputs synthetic or confined to the authorized lab.

## Knowledge checks

1. Explain the most important trust boundary in **Authorization Models: RBAC, ABAC, ReBAC and Policy Engines** without naming a security tool.
2. Give one example where cryptographic or authentication success still does **not** imply authorization success.
3. Describe one stale-state or replay condition relevant to this module.
4. Identify one telemetry source that can support a strong conclusion and one blind spot it still leaves.
5. Explain how you would turn a discovered weakness into a regression test rather than a one-time finding.

## Guided study workflow

Use [Study Method](../Guides/STUDY-METHOD.md). Complete at least one authorized exercise, preserve the evidence that supports your conclusion, and explain the module's main trust boundary and failure modes in your own words before moving on.

### Continue with

Choose **Learning paths** from the main menu for an ordered specialization, or use **Search lessons** to follow a concept into related modules.

---

# Virtualization, Hypervisors, Virtual Machines and Confidential Computing

Virtualization creates strong but not absolute boundaries. This module explains hypervisor architecture, virtual devices, management planes, snapshots, host integration, nested virtualization, and confidential-computing concepts from a defensive research perspective.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, or lab environments you own or are explicitly authorized to test. The exercises in this module are designed to prove security properties without targeting third parties.

## Learning objectives

By the end of this module you should be able to:

- Explain **Hypervisor models** and connect it to a concrete trust boundary or security invariant.
- Explain **Hardware virtualization** and connect it to a concrete trust boundary or security invariant.
- Explain **Virtual devices** and connect it to a concrete trust boundary or security invariant.
- Explain **Snapshots and images** and connect it to a concrete trust boundary or security invariant.
- Explain **Management plane** and connect it to a concrete trust boundary or security invariant.
- Explain **Nested virtualization** and connect it to a concrete trust boundary or security invariant.

## Analysis method

Use the shared [Study Method](../Guides/STUDY-METHOD.md). For this module, first draw the relevant components and state transitions, then state one security invariant and identify the minimum evidence needed to test it safely.

## Deep concepts

### 1. Hypervisor models

Type-1 and hosted hypervisors differ in deployment architecture, but both mediate CPU, memory, interrupts, and devices. The management plane and device-emulation surface are often as important as the core scheduler.



### 2. Hardware virtualization

CPU extensions and second-level address translation allow guest execution while retaining host control over privileged operations and memory mappings. Security analysis should distinguish guest virtual, guest physical, and host physical addresses.



### 3. Virtual devices

Network cards, storage controllers, graphics, USB, shared folders, clipboard, and guest agents expand the interface between guest and host. Disable integration features that are unnecessary for the workload.



### 4. Snapshots and images

VM images and snapshots can contain credentials, encryption keys, tokens, memory-resident secrets, and stale software. Treat them as sensitive artifacts with lifecycle controls.



### 5. Management plane

Hypervisor APIs, consoles, orchestration, templates, and backup systems can control many guests at once. Strong MFA, dedicated administration paths, logging, and separation of duties are essential.



### 6. Nested virtualization

Nested guests add more layers and make performance/security assumptions harder to reason about. Document which layer owns each security feature rather than assuming the inner guest can enforce host-level guarantees.



### 7. Confidential computing

Hardware-backed confidential VMs/TEEs aim to protect workload memory from parts of the host stack. Attestation and key-release policy become central; side channels, availability, and trusted I/O remain separate concerns.



### 8. Boundary verification

A good test plan checks device exposure, guest-agent privileges, network isolation, image provenance, snapshot handling, time synchronization, logging, and management-plane authorization without attempting host escape.



## Review focus

Apply the failure-mode taxonomy in [Study Method](../Guides/STUDY-METHOD.md), but keep the analysis specific to this lesson: identify the principal, resource, authority, mutable state, parser or policy boundary, and the telemetry that would distinguish a real control failure from misconfiguration or an observation gap.

## Authorized exercises

### Exercise 1 — Build a local VM threat model listing every host/guest integration feature and justify whether it is required

Build a local VM threat model listing every host/guest integration feature and justify whether it is required.


### Exercise 2 — Take a disposable VM snapshot with non-sensitive test data and document what security-sensitive state a real snapshot could preserve

Take a disposable VM snapshot with non-sensitive test data and document what security-sensitive state a real snapshot could preserve.


### Exercise 3 — Compare the trust assumptions of a normal VM, container, and confidential VM in a one-page matrix

Compare the trust assumptions of a normal VM, container, and confidential VM in a one-page matrix.

Use the lab-record format in [Study Method](../Guides/STUDY-METHOD.md) for each exercise and keep all inputs synthetic or confined to the authorized lab.

## Knowledge checks

1. Explain the most important trust boundary in **Virtualization, Hypervisors, Virtual Machines and Confidential Computing** without naming a security tool.
2. Give one example where cryptographic or authentication success still does **not** imply authorization success.
3. Describe one stale-state or replay condition relevant to this module.
4. Identify one telemetry source that can support a strong conclusion and one blind spot it still leaves.
5. Explain how you would turn a discovered weakness into a regression test rather than a one-time finding.

## Guided study workflow

Use [Study Method](../Guides/STUDY-METHOD.md). Complete at least one authorized exercise, preserve the evidence that supports your conclusion, and explain the module's main trust boundary and failure modes in your own words before moving on.

### Continue with

Choose **Learning paths** from the main menu for an ordered specialization, or use **Search lessons** to follow a concept into related modules.

---

# Kernel Security Primitives, Attack Surface and Runtime Trust

The kernel is the mediator for memory, processes, files, devices, networking, and privilege. This module deepens the earlier OS lessons by teaching how to map kernel attack surface and hardening primitives without turning kernel exploitation into an operational recipe.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, or lab environments you own or are explicitly authorized to test. The exercises in this module are designed to prove security properties without targeting third parties.

## Learning objectives

By the end of this module you should be able to:

- Explain **System-call boundary** and connect it to a concrete trust boundary or security invariant.
- Explain **Drivers and device interfaces** and connect it to a concrete trust boundary or security invariant.
- Explain **Kernel memory safety** and connect it to a concrete trust boundary or security invariant.
- Explain **Privilege model** and connect it to a concrete trust boundary or security invariant.
- Explain **Module and boot trust** and connect it to a concrete trust boundary or security invariant.
- Explain **Race conditions** and connect it to a concrete trust boundary or security invariant.

## Analysis method

Use the shared [Study Method](../Guides/STUDY-METHOD.md). For this module, first draw the relevant components and state transitions, then state one security invariant and identify the minimum evidence needed to test it safely.

## Deep concepts

### 1. System-call boundary

System calls expose kernel services to user processes. The reachable syscall set depends on architecture, kernel configuration, namespaces, seccomp, capabilities, and the process execution model.



### 2. Drivers and device interfaces

Device drivers, filesystems, network protocols, ioctls, USB, Bluetooth, graphics, and virtual devices add complex parsers and state machines inside privileged code. Reducing unused functionality reduces risk.



### 3. Kernel memory safety

Kernel bugs include out-of-bounds access, use-after-free, races, integer issues, and reference-lifetime mistakes. Modern kernels deploy hardening such as KASLR, stack protections, hardened allocators, CFI-related defenses, and memory-safety improvements, but none replaces correct code.



### 4. Privilege model

UIDs, capabilities, namespaces, LSMs, keyrings, credentials, and file permissions interact. “root inside a namespace” is not automatically equivalent to unrestricted host privilege.



### 5. Module and boot trust

Secure Boot, module signing, measured boot, lockdown modes, and update provenance constrain which privileged code is accepted. Operational key management determines whether those features remain meaningful.



### 6. Race conditions

Kernel concurrency means an object can change between validation and use. Security analysis must consider locking, reference counting, RCU-style lifetimes, interrupt contexts, and multi-core scheduling.



### 7. Attack-surface reduction

Disable unused filesystems/protocols/modules, minimize device access, constrain containers, keep kernels updated, and select hardened configurations appropriate to the workload rather than relying on one mitigation.



### 8. Telemetry

Audit, LSM logs, eBPF-based observability, kernel warnings, crash reports, module events, and integrity measurements can reveal abnormal kernel-adjacent activity. Capture enough context to distinguish faults from malicious behavior.



## Review focus

Apply the failure-mode taxonomy in [Study Method](../Guides/STUDY-METHOD.md), but keep the analysis specific to this lesson: identify the principal, resource, authority, mutable state, parser or policy boundary, and the telemetry that would distinguish a real control failure from misconfiguration or an observation gap.

## Authorized exercises

### Exercise 1 — Inventory the enabled kernel-facing interfaces in an owned Linux VM: devices, filesystems, modules, namespaces, and exposed sockets; classify them by necessity

Inventory the enabled kernel-facing interfaces in an owned Linux VM: devices, filesystems, modules, namespaces, and exposed sockets; classify them by necessity.


### Exercise 2 — Compare process capabilities before and after applying a least-privilege service configuration in a disposable lab

Compare process capabilities before and after applying a least-privilege service configuration in a disposable lab.


### Exercise 3 — Read a harmless kernel crash report or public bug description and identify object lifetime, privilege context, and mitigation layers without reproducing exploitation

Read a harmless kernel crash report or public bug description and identify object lifetime, privilege context, and mitigation layers without reproducing exploitation.

Use the lab-record format in [Study Method](../Guides/STUDY-METHOD.md) for each exercise and keep all inputs synthetic or confined to the authorized lab.

## Knowledge checks

1. Explain the most important trust boundary in **Kernel Security Primitives, Attack Surface and Runtime Trust** without naming a security tool.
2. Give one example where cryptographic or authentication success still does **not** imply authorization success.
3. Describe one stale-state or replay condition relevant to this module.
4. Identify one telemetry source that can support a strong conclusion and one blind spot it still leaves.
5. Explain how you would turn a discovered weakness into a regression test rather than a one-time finding.

## Guided study workflow

Use [Study Method](../Guides/STUDY-METHOD.md). Complete at least one authorized exercise, preserve the evidence that supports your conclusion, and explain the module's main trust boundary and failure modes in your own words before moving on.

### Continue with

Choose **Learning paths** from the main menu for an ordered specialization, or use **Search lessons** to follow a concept into related modules.

---

# eBPF Observability, Linux Telemetry and Detection Engineering

eBPF allows constrained programs to observe or influence selected kernel events depending on hook and privilege. For defenders it enables powerful telemetry, but it also introduces governance, performance, and trust questions. This module focuses on safe observability and detection design.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, or lab environments you own or are explicitly authorized to test. The exercises in this module are designed to prove security properties without targeting third parties.

## Learning objectives

By the end of this module you should be able to:

- Explain **Program and map model** and connect it to a concrete trust boundary or security invariant.
- Explain **Verifier and privilege** and connect it to a concrete trust boundary or security invariant.
- Explain **Tracepoints and probes** and connect it to a concrete trust boundary or security invariant.
- Explain **Network hooks** and connect it to a concrete trust boundary or security invariant.
- Explain **Telemetry design** and connect it to a concrete trust boundary or security invariant.
- Explain **Tamper and blind spots** and connect it to a concrete trust boundary or security invariant.

## Analysis method

Use the shared [Study Method](../Guides/STUDY-METHOD.md). For this module, first draw the relevant components and state transitions, then state one security invariant and identify the minimum evidence needed to test it safely.

## Deep concepts

### 1. Program and map model

eBPF programs run at defined hooks and communicate through maps. Program type, verifier constraints, helpers, and attachment point determine what data is visible and what actions are possible.



### 2. Verifier and privilege

The verifier reasons about program safety properties such as bounded execution and memory access. Kernel configuration and privilege determine who may load programs; organizations should treat eBPF loading as a privileged administration capability.



### 3. Tracepoints and probes

Stable tracepoints are preferable when available. Kprobes/uprobes can expose implementation detail but may be more version-sensitive. Choose the least fragile observation point that answers the detection question.



### 4. Network hooks

XDP and traffic-control hooks can observe packets early in the stack. Security teams should separate passive measurement from enforcement and test performance/failure behavior before production use.



### 5. Telemetry design

Collect fields that support a hypothesis: process lineage, executable identity, UID, namespace/container, file path, network tuple, capability change, or syscall class. More events are not automatically better detections.



### 6. Tamper and blind spots

An agent running with high privilege can itself become a sensitive component. Protect loader/configuration paths, record program changes, and understand what happens if telemetry is disabled or overloaded.



### 7. Performance

High-frequency hooks can generate enormous volume. Use sampling, aggregation, maps, filters, rate limits, and bounded cardinality to protect the host and downstream pipeline.



### 8. Detection lifecycle

Write the behavioral hypothesis first, validate with controlled activity, measure expected false positives, version the rule, and keep a known-good replay/test fixture.



## Review focus

Apply the failure-mode taxonomy in [Study Method](../Guides/STUDY-METHOD.md), but keep the analysis specific to this lesson: identify the principal, resource, authority, mutable state, parser or policy boundary, and the telemetry that would distinguish a real control failure from misconfiguration or an observation gap.

## Authorized exercises

### Exercise 1 — Write a detection hypothesis for unexpected interactive shells in a server container and specify which kernel/process fields would prove or refute it—without collecting real user content

Write a detection hypothesis for unexpected interactive shells in a server container and specify which kernel/process fields would prove or refute it—without collecting real user content.


### Exercise 2 — Compare audit logs, process accounting, and eBPF telemetry for the same harmless process-start event in a lab

Compare audit logs, process accounting, and eBPF telemetry for the same harmless process-start event in a lab.


### Exercise 3 — Design a rollback plan for an observability agent that begins consuming excessive CPU or producing unbounded event volume

Design a rollback plan for an observability agent that begins consuming excessive CPU or producing unbounded event volume.

Use the lab-record format in [Study Method](../Guides/STUDY-METHOD.md) for each exercise and keep all inputs synthetic or confined to the authorized lab.

## Knowledge checks

1. Explain the most important trust boundary in **eBPF Observability, Linux Telemetry and Detection Engineering** without naming a security tool.
2. Give one example where cryptographic or authentication success still does **not** imply authorization success.
3. Describe one stale-state or replay condition relevant to this module.
4. Identify one telemetry source that can support a strong conclusion and one blind spot it still leaves.
5. Explain how you would turn a discovered weakness into a regression test rather than a one-time finding.

## Guided study workflow

Use [Study Method](../Guides/STUDY-METHOD.md). Complete at least one authorized exercise, preserve the evidence that supports your conclusion, and explain the module's main trust boundary and failure modes in your own words before moving on.

### Continue with

Choose **Learning paths** from the main menu for an ordered specialization, or use **Search lessons** to follow a concept into related modules.

---

# CI/CD, Build Provenance, SLSA 1.2 and Artifact Trust

Software supply-chain security is about proving how source becomes an artifact and reducing opportunities for unauthorized modification. SLSA 1.2 separates tracks and emphasizes provenance and source/build controls. This module connects repository governance, builders, attestations, signing, and deployment verification.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, or lab environments you own or are explicitly authorized to test. The exercises in this module are designed to prove security properties without targeting third parties.

## Learning objectives

By the end of this module you should be able to:

- Explain **Source control trust** and connect it to a concrete trust boundary or security invariant.
- Explain **Build isolation** and connect it to a concrete trust boundary or security invariant.
- Explain **Provenance** and connect it to a concrete trust boundary or security invariant.
- Explain **SLSA 1.2** and connect it to a concrete trust boundary or security invariant.
- Explain **Artifact signing** and connect it to a concrete trust boundary or security invariant.
- Explain **Promotion** and connect it to a concrete trust boundary or security invariant.

## Analysis method

Use the shared [Study Method](../Guides/STUDY-METHOD.md). For this module, first draw the relevant components and state transitions, then state one security invariant and identify the minimum evidence needed to test it safely.

## Deep concepts

### 1. Source control trust

Branch protection, review, protected tags, signed changes where appropriate, repository administration, and account recovery define who can alter source and release metadata.



### 2. Build isolation

A trusted build should have controlled inputs, ephemeral or well-managed execution, explicit dependencies, and limited credentials. Long-lived mutable runners create hidden state and increase cross-build risk.



### 3. Provenance

Provenance records who/what built an artifact, from which source and dependencies, under which process. It supports verification but only if the builder and attestation signing path are trustworthy.



### 4. SLSA 1.2

SLSA 1.2 is the current specification and includes Build and Source tracks. Use levels/requirements as a structured improvement path rather than a marketing badge.



### 5. Artifact signing

Signatures bind an identity/key to an artifact digest. Verification policy must define which identities are trusted, what provenance is required, and what happens when verification cannot be completed.



### 6. Promotion

Promote the same immutable artifact between environments instead of rebuilding from source independently for staging and production. This narrows the number of build events that can affect production.



### 7. Secrets in CI

CI tokens often have broad repository, cloud, registry, and signing privileges. Prefer short-lived workload identity, environment protection, minimal scopes, and explicit approval for high-impact stages.



### 8. Verification at deploy

Deployment systems should verify digest, expected source/ref, builder identity, provenance policy, vulnerability policy where appropriate, and environment authorization before rollout.



## Review focus

Apply the failure-mode taxonomy in [Study Method](../Guides/STUDY-METHOD.md), but keep the analysis specific to this lesson: identify the principal, resource, authority, mutable state, parser or policy boundary, and the telemetry that would distinguish a real control failure from misconfiguration or an observation gap.

## Authorized exercises

### Exercise 1 — Draw the source→build→registry→deployment chain for a small project and mark every identity that can change the final artifact

Draw the source→build→registry→deployment chain for a small project and mark every identity that can change the final artifact.


### Exercise 2 — Generate a harmless local artifact and a JSON provenance record containing source hash, builder, timestamp, and output digest; verify consistency with a Python script

Generate a harmless local artifact and a JSON provenance record containing source hash, builder, timestamp, and output digest; verify consistency with a Python script.


### Exercise 3 — Create a CI hardening checklist that distinguishes source-track controls from build-track controls

Create a CI hardening checklist that distinguishes source-track controls from build-track controls.

Use the lab-record format in [Study Method](../Guides/STUDY-METHOD.md) for each exercise and keep all inputs synthetic or confined to the authorized lab.

## Knowledge checks

1. Explain the most important trust boundary in **CI/CD, Build Provenance, SLSA 1.2 and Artifact Trust** without naming a security tool.
2. Give one example where cryptographic or authentication success still does **not** imply authorization success.
3. Describe one stale-state or replay condition relevant to this module.
4. Identify one telemetry source that can support a strong conclusion and one blind spot it still leaves.
5. Explain how you would turn a discovered weakness into a regression test rather than a one-time finding.

## Guided study workflow

Use [Study Method](../Guides/STUDY-METHOD.md). Complete at least one authorized exercise, preserve the evidence that supports your conclusion, and explain the module's main trust boundary and failure modes in your own words before moving on.

### Continue with

Choose **Learning paths** from the main menu for an ordered specialization, or use **Search lessons** to follow a concept into related modules.

---

# Package Managers, Registries, Dependency and Ecosystem Security

Dependency risk is an ecosystem problem involving names, versions, maintainers, registries, resolver behavior, lockfiles, mirrors, build scripts, and transitive trust. This module focuses on how to control dependency introduction and detect suspicious changes.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, or lab environments you own or are explicitly authorized to test. The exercises in this module are designed to prove security properties without targeting third parties.

## Learning objectives

By the end of this module you should be able to:

- Explain **Name and namespace trust** and connect it to a concrete trust boundary or security invariant.
- Explain **Semantic versioning limits** and connect it to a concrete trust boundary or security invariant.
- Explain **Lockfiles** and connect it to a concrete trust boundary or security invariant.
- Explain **Install/build scripts** and connect it to a concrete trust boundary or security invariant.
- Explain **Transitive dependencies** and connect it to a concrete trust boundary or security invariant.
- Explain **Maintainer and release trust** and connect it to a concrete trust boundary or security invariant.

## Analysis method

Use the shared [Study Method](../Guides/STUDY-METHOD.md). For this module, first draw the relevant components and state transitions, then state one security invariant and identify the minimum evidence needed to test it safely.

## Deep concepts

### 1. Name and namespace trust

Typosquatting, namespace confusion, abandoned packages, and internal/public name collisions can redirect developers to unintended code. Reserve important names and define registry precedence.



### 2. Semantic versioning limits

Version ranges express compatibility intent, not security trust. A syntactically compatible update can still add risky behavior. Know when production builds are pinned and when updates are deliberately refreshed.



### 3. Lockfiles

Lockfiles make resolved dependency graphs more reproducible, but their integrity and review matter. They should change for explainable reasons and be included in code review.



### 4. Install/build scripts

Package lifecycle hooks and native builds may execute code during installation. Treat dependency installation as code execution, especially in CI and developer environments.



### 5. Transitive dependencies

Most projects depend on far more packages than are listed directly. Generate an SBOM/dependency graph, identify critical/transitively privileged packages, and reduce unnecessary depth.



### 6. Maintainer and release trust

Protect maintainer accounts, use strong MFA, separate release authority, monitor ownership changes, and verify release automation. Package metadata alone does not prove source provenance.



### 7. Mirrors and proxies

Internal registries can enforce allowlists, caching, provenance, scanning, and namespace policy. They also become high-impact infrastructure that requires backup, access control, and monitoring.



### 8. Response

When a dependency is compromised, identify affected versions, where they were built/deployed, what execution privileges they had, and whether credentials or build artifacts need rotation/rebuild—not just a version bump.



## Review focus

Apply the failure-mode taxonomy in [Study Method](../Guides/STUDY-METHOD.md), but keep the analysis specific to this lesson: identify the principal, resource, authority, mutable state, parser or policy boundary, and the telemetry that would distinguish a real control failure from misconfiguration or an observation gap.

## Authorized exercises

### Exercise 1 — Create a dependency inventory for a small harmless Python project and classify direct vs transitive packages

Create a dependency inventory for a small harmless Python project and classify direct vs transitive packages.


### Exercise 2 — Compare reproducibility with and without a lockfile or fully pinned requirements in an isolated virtual environment

Compare reproducibility with and without a lockfile or fully pinned requirements in an isolated virtual environment.


### Exercise 3 — Write an incident checklist for a compromised package version: identify exposure, builds, credentials, artifacts, and verification steps

Write an incident checklist for a compromised package version: identify exposure, builds, credentials, artifacts, and verification steps.

Use the lab-record format in [Study Method](../Guides/STUDY-METHOD.md) for each exercise and keep all inputs synthetic or confined to the authorized lab.

## Knowledge checks

1. Explain the most important trust boundary in **Package Managers, Registries, Dependency and Ecosystem Security** without naming a security tool.
2. Give one example where cryptographic or authentication success still does **not** imply authorization success.
3. Describe one stale-state or replay condition relevant to this module.
4. Identify one telemetry source that can support a strong conclusion and one blind spot it still leaves.
5. Explain how you would turn a discovered weakness into a regression test rather than a one-time finding.

## Guided study workflow

Use [Study Method](../Guides/STUDY-METHOD.md). Complete at least one authorized exercise, preserve the evidence that supports your conclusion, and explain the module's main trust boundary and failure modes in your own words before moving on.

### Continue with

Choose **Learning paths** from the main menu for an ordered specialization, or use **Search lessons** to follow a concept into related modules.

---

# Compiler Toolchains, Sanitizers, CFI and Binary Hardening

Compilers are part of the security boundary because they transform source assumptions into machine-level behavior. This module explains optimization, undefined behavior, sanitizers, stack protection, CFI-related techniques, linker hardening, and reproducible builds as security engineering tools.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, or lab environments you own or are explicitly authorized to test. The exercises in this module are designed to prove security properties without targeting third parties.

## Learning objectives

By the end of this module you should be able to:

- Explain **Undefined behavior** and connect it to a concrete trust boundary or security invariant.
- Explain **Sanitizers** and connect it to a concrete trust boundary or security invariant.
- Explain **Stack and object protections** and connect it to a concrete trust boundary or security invariant.
- Explain **Control-flow integrity** and connect it to a concrete trust boundary or security invariant.
- Explain **Linker hardening** and connect it to a concrete trust boundary or security invariant.
- Explain **LTO and optimization** and connect it to a concrete trust boundary or security invariant.

## Analysis method

Use the shared [Study Method](../Guides/STUDY-METHOD.md). For this module, first draw the relevant components and state transitions, then state one security invariant and identify the minimum evidence needed to test it safely.

## Deep concepts

### 1. Undefined behavior

In languages such as C/C++, undefined behavior allows the compiler to assume certain invalid states never occur. Security debugging must consider that optimized code may not preserve the intuitive behavior seen in an unoptimized build.



### 2. Sanitizers

AddressSanitizer, UndefinedBehaviorSanitizer, MemorySanitizer, and related tools detect classes of mistakes during testing. They trade performance/memory for visibility and are generally not substitutes for production hardening.



### 3. Stack and object protections

Stack canaries, fortified library calls, bounds-aware APIs, hardened allocators, and compiler diagnostics can turn silent memory corruption into earlier failures or eliminate common bug patterns.



### 4. Control-flow integrity

CFI-style protections constrain indirect control transfers according to a policy/type model. Their effectiveness depends on compilation coverage, language/runtime, dynamic linking, and where uninstrumented code remains.



### 5. Linker hardening

PIE, RELRO, non-executable mappings, symbol visibility, library search policy, and load-time configuration shape the binary attack surface. Verify actual produced binaries rather than assuming build flags took effect.



### 6. LTO and optimization

Link-time optimization can improve whole-program visibility but changes build reproducibility, debugging, and instrumentation. Security pipelines should test release-like optimization levels.



### 7. Toolchain provenance

The compiler, linker, SDK, sysroot, plugins, and build scripts are dependencies. Pin/verify toolchains appropriate to the threat model and keep a record of which toolchain produced each release.



### 8. Regression strategy

A fixed vulnerability should become a test: unit test, sanitizer test, fuzz regression input, static-analysis rule, or invariant. The goal is to prevent the bug class from silently returning.



## Review focus

Apply the failure-mode taxonomy in [Study Method](../Guides/STUDY-METHOD.md), but keep the analysis specific to this lesson: identify the principal, resource, authority, mutable state, parser or policy boundary, and the telemetry that would distinguish a real control failure from misconfiguration or an observation gap.

## Authorized exercises

### Exercise 1 — Compile a harmless toy C program with and without common hardening flags and inspect the resulting binary properties—without developing an exploit

Compile a harmless toy C program with and without common hardening flags and inspect the resulting binary properties—without developing an exploit.


### Exercise 2 — Use a sanitizer on intentionally buggy toy code to capture a diagnostic and explain root cause, object lifetime, and fix

Use a sanitizer on intentionally buggy toy code to capture a diagnostic and explain root cause, object lifetime, and fix.


### Exercise 3 — Create a build-metadata record containing compiler version, flags, source hash, dependency lock, and output digest

Create a build-metadata record containing compiler version, flags, source hash, dependency lock, and output digest.

Use the lab-record format in [Study Method](../Guides/STUDY-METHOD.md) for each exercise and keep all inputs synthetic or confined to the authorized lab.

## Knowledge checks

1. Explain the most important trust boundary in **Compiler Toolchains, Sanitizers, CFI and Binary Hardening** without naming a security tool.
2. Give one example where cryptographic or authentication success still does **not** imply authorization success.
3. Describe one stale-state or replay condition relevant to this module.
4. Identify one telemetry source that can support a strong conclusion and one blind spot it still leaves.
5. Explain how you would turn a discovered weakness into a regression test rather than a one-time finding.

## Guided study workflow

Use [Study Method](../Guides/STUDY-METHOD.md). Complete at least one authorized exercise, preserve the evidence that supports your conclusion, and explain the module's main trust boundary and failure modes in your own words before moving on.

### Continue with

Choose **Learning paths** from the main menu for an ordered specialization, or use **Search lessons** to follow a concept into related modules.

---

# Cryptographic Protocol Engineering, Key Agreement and State Machines

Strong primitives can still produce an insecure protocol if identities, transcript binding, nonces, key separation, error handling, or state transitions are wrong. This module teaches how to reason about cryptographic protocols as authenticated state machines.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, or lab environments you own or are explicitly authorized to test. The exercises in this module are designed to prove security properties without targeting third parties.

## Learning objectives

By the end of this module you should be able to:

- Explain **Security goals** and connect it to a concrete trust boundary or security invariant.
- Explain **Key agreement** and connect it to a concrete trust boundary or security invariant.
- Explain **Transcript binding** and connect it to a concrete trust boundary or security invariant.
- Explain **Nonces and sequence numbers** and connect it to a concrete trust boundary or security invariant.
- Explain **Key derivation** and connect it to a concrete trust boundary or security invariant.
- Explain **Algorithm agility** and connect it to a concrete trust boundary or security invariant.

## Analysis method

Use the shared [Study Method](../Guides/STUDY-METHOD.md). For this module, first draw the relevant components and state transitions, then state one security invariant and identify the minimum evidence needed to test it safely.

## Deep concepts

### 1. Security goals

Write goals before algorithms: confidentiality, integrity, peer authentication, forward secrecy, replay resistance, channel binding, deniability, key confirmation, or post-compromise properties. Different protocols need different combinations.



### 2. Key agreement

Key exchange establishes shared secret material but does not automatically authenticate peers. Authentication must bind identities/credentials to the transcript and agreed parameters.



### 3. Transcript binding

Security-critical negotiation should be included in authenticated transcript data so an intermediary cannot alter algorithms, identities, roles, or context without detection.



### 4. Nonces and sequence numbers

Fresh unpredictable nonces or monotonic sequence state prevent reuse/replay depending on the construction. Define uniqueness requirements precisely; “random-looking” is not the same as guaranteed unique.



### 5. Key derivation

Use a KDF to derive independent keys for different directions and purposes. Domain separation prevents one key/context from being accidentally reused for encryption, authentication, export, or another protocol.



### 6. Algorithm agility

Negotiation can enable migration but also creates downgrade risk. The protocol must authenticate the negotiation and have policy for removing obsolete algorithms.



### 7. Error handling

Different errors, timing, retry behavior, and partial state can leak information. Protocols should define failure states, cleanup, retry limits, and whether an error is safe to reveal.



### 8. Formal and empirical validation

Threat modeling, test vectors, interoperability tests, negative tests, state-machine fuzzing, and formal methods can complement code review. Cryptographic protocol design should be independently reviewed rather than invented casually.



## Review focus

Apply the failure-mode taxonomy in [Study Method](../Guides/STUDY-METHOD.md), but keep the analysis specific to this lesson: identify the principal, resource, authority, mutable state, parser or policy boundary, and the telemetry that would distinguish a real control failure from misconfiguration or an observation gap.

## Authorized exercises

### Exercise 1 — Design a toy authenticated message protocol on paper and identify where identities, roles, nonces, sequence numbers, and transcript data are bound

Design a toy authenticated message protocol on paper and identify where identities, roles, nonces, sequence numbers, and transcript data are bound.


### Exercise 2 — Create negative test cases for replay, reordered messages, algorithm downgrade, expired credentials, and duplicate session identifiers

Create negative test cases for replay, reordered messages, algorithm downgrade, expired credentials, and duplicate session identifiers.


### Exercise 3 — Compare “encrypted transport” with “end-to-end authenticated message” and list which intermediaries can still read or modify data in each model

Compare “encrypted transport” with “end-to-end authenticated message” and list which intermediaries can still read or modify data in each model.

Use the lab-record format in [Study Method](../Guides/STUDY-METHOD.md) for each exercise and keep all inputs synthetic or confined to the authorized lab.

## Knowledge checks

1. Explain the most important trust boundary in **Cryptographic Protocol Engineering, Key Agreement and State Machines** without naming a security tool.
2. Give one example where cryptographic or authentication success still does **not** imply authorization success.
3. Describe one stale-state or replay condition relevant to this module.
4. Identify one telemetry source that can support a strong conclusion and one blind spot it still leaves.
5. Explain how you would turn a discovered weakness into a regression test rather than a one-time finding.

## Guided study workflow

Use [Study Method](../Guides/STUDY-METHOD.md). Complete at least one authorized exercise, preserve the evidence that supports your conclusion, and explain the module's main trust boundary and failure modes in your own words before moving on.

### Continue with

Choose **Learning paths** from the main menu for an ordered specialization, or use **Search lessons** to follow a concept into related modules.

---

# Post-Quantum Migration, Crypto Agility and Hybrid Deployment

Post-quantum security is now an engineering migration problem. NIST has standardized ML-KEM, ML-DSA, and SLH-DSA and urges organizations to begin migration planning. This module focuses on discovery, dependency mapping, protocol readiness, testing, and long-lived data risk.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, or lab environments you own or are explicitly authorized to test. The exercises in this module are designed to prove security properties without targeting third parties.

## Learning objectives

By the end of this module you should be able to:

- Explain **Cryptographic inventory** and connect it to a concrete trust boundary or security invariant.
- Explain **Harvest-now risk** and connect it to a concrete trust boundary or security invariant.
- Explain **Standards** and connect it to a concrete trust boundary or security invariant.
- Explain **Crypto agility** and connect it to a concrete trust boundary or security invariant.
- Explain **Hybrid approaches** and connect it to a concrete trust boundary or security invariant.
- Explain **PKI impact** and connect it to a concrete trust boundary or security invariant.

## Analysis method

Use the shared [Study Method](../Guides/STUDY-METHOD.md). For this module, first draw the relevant components and state transitions, then state one security invariant and identify the minimum evidence needed to test it safely.

## Deep concepts

### 1. Cryptographic inventory

Find where public-key cryptography is used: TLS, VPNs, SSH, code signing, certificates, document signatures, device identity, firmware, backups, HSMs, libraries, protocols, and third-party services.



### 2. Harvest-now risk

Data with long confidentiality lifetimes may need earlier protection because captured ciphertext could be stored and attacked later. Prioritize based on sensitivity and required secrecy duration rather than hype.



### 3. Standards

FIPS 203 standardizes ML-KEM; FIPS 204 ML-DSA; FIPS 205 SLH-DSA. Migration decisions must also consider protocol profiles, ecosystem support, certification, performance, and interoperability.



### 4. Crypto agility

Applications should avoid hard-coded assumptions about key size, signature size, certificate shape, or one algorithm. Build explicit algorithm identifiers, versioning, test coverage, and policy controls.



### 5. Hybrid approaches

Some deployments combine classical and post-quantum mechanisms during transition. Security depends on how secrets/signatures are combined and whether the surrounding protocol specifies the hybrid construction correctly.



### 6. PKI impact

Larger keys/signatures can affect certificate chains, handshake sizes, embedded storage, MTU-sensitive protocols, HSM support, and constrained devices. Measure rather than assume compatibility.



### 7. Migration sequencing

Inventory → classify data/uses → identify dependencies → test libraries/protocols → prioritize high-value use cases → deploy with rollback → monitor interoperability → retire quantum-vulnerable use when policy requires.



### 8. Evidence

Track algorithm, key size/type, owner, library/provider, protocol, certificate profile, data lifetime, replacement plan, test status, and deprecation date. A spreadsheet without system ownership is not an actionable inventory.



## Review focus

Apply the failure-mode taxonomy in [Study Method](../Guides/STUDY-METHOD.md), but keep the analysis specific to this lesson: identify the principal, resource, authority, mutable state, parser or policy boundary, and the telemetry that would distinguish a real control failure from misconfiguration or an observation gap.

## Authorized exercises

### Exercise 1 — Build a cryptographic inventory for a small local application and record every library/API that creates or validates keys/signatures

Build a cryptographic inventory for a small local application and record every library/API that creates or validates keys/signatures.


### Exercise 2 — Create a compatibility test plan that anticipates larger key/signature objects and handshake messages without claiming unsupported algorithms are production-ready

Create a compatibility test plan that anticipates larger key/signature objects and handshake messages without claiming unsupported algorithms are production-ready.


### Exercise 3 — Classify sample data sets by confidentiality lifetime and use that to rank migration priority

Classify sample data sets by confidentiality lifetime and use that to rank migration priority.

Use the lab-record format in [Study Method](../Guides/STUDY-METHOD.md) for each exercise and keep all inputs synthetic or confined to the authorized lab.

## Knowledge checks

1. Explain the most important trust boundary in **Post-Quantum Migration, Crypto Agility and Hybrid Deployment** without naming a security tool.
2. Give one example where cryptographic or authentication success still does **not** imply authorization success.
3. Describe one stale-state or replay condition relevant to this module.
4. Identify one telemetry source that can support a strong conclusion and one blind spot it still leaves.
5. Explain how you would turn a discovered weakness into a regression test rather than a one-time finding.

## Guided study workflow

Use [Study Method](../Guides/STUDY-METHOD.md). Complete at least one authorized exercise, preserve the evidence that supports your conclusion, and explain the module's main trust boundary and failure modes in your own words before moving on.

### Continue with

Choose **Learning paths** from the main menu for an ordered specialization, or use **Search lessons** to follow a concept into related modules.

---

# Side Channels, Timing, Cache, Faults and Physical Leakage Models

Security can fail through information that escapes outside the intended logical interface: timing, cache state, power, electromagnetic behavior, memory access patterns, shared resources, or injected faults. This module teaches the models and mitigations using safe local experiments.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, or lab environments you own or are explicitly authorized to test. The exercises in this module are designed to prove security properties without targeting third parties.

## Learning objectives

By the end of this module you should be able to:

- Explain **Side-channel model** and connect it to a concrete trust boundary or security invariant.
- Explain **Timing** and connect it to a concrete trust boundary or security invariant.
- Explain **Caches and microarchitecture** and connect it to a concrete trust boundary or security invariant.
- Explain **Power and EM** and connect it to a concrete trust boundary or security invariant.
- Explain **Fault injection** and connect it to a concrete trust boundary or security invariant.
- Explain **Remote vs local feasibility** and connect it to a concrete trust boundary or security invariant.

## Analysis method

Use the shared [Study Method](../Guides/STUDY-METHOD.md). For this module, first draw the relevant components and state transitions, then state one security invariant and identify the minimum evidence needed to test it safely.

## Deep concepts

### 1. Side-channel model

A side channel is an observable correlated with secret-dependent computation. Define attacker proximity, measurement capability, shared resources, number of observations, and noise before judging feasibility.



### 2. Timing

Secret-dependent branches, early exits, variable-time arithmetic, database lookups, network jitter, and rate limiting can all affect timing. Constant-time cryptographic code aims to remove secret-dependent timing at the implementation level.



### 3. Caches and microarchitecture

Shared caches, branch predictors, speculative execution, memory deduplication, and execution units can create cross-context observations. Platform mitigations often trade performance and depend on hardware/OS scheduling.



### 4. Power and EM

Embedded devices can leak information through power consumption or electromagnetic emissions. Countermeasures include constant-pattern implementations, masking, filtering, secure hardware, and limiting physical access.



### 5. Fault injection

Voltage, clock, electromagnetic, laser, or software-induced faults can alter computation. Secure designs validate critical state, use redundancy where justified, and avoid treating one successful computation as unquestionable.



### 6. Remote vs local feasibility

A signal measurable with physical access may disappear over a network; conversely application-level timing can remain remotely visible when amplified. Threat models must state measurement distance and noise.



### 7. Mitigation layers

Constant-time libraries, isolation, scheduler/core policy, hardware mitigations, removal of secret-dependent behavior, blinding/masking, rate limits, and physical protections address different channels.



### 8. Validation

Use statistical experiments on toy code and public benchmark methods. Avoid experiments that target third-party co-tenants or systems you do not own.



## Review focus

Apply the failure-mode taxonomy in [Study Method](../Guides/STUDY-METHOD.md), but keep the analysis specific to this lesson: identify the principal, resource, authority, mutable state, parser or policy boundary, and the telemetry that would distinguish a real control failure from misconfiguration or an observation gap.

## Authorized exercises

### Exercise 1 — Write two localhost toy string-comparison functions—one early-exit and one constant-work—and measure timing distributions using random non-secret data

Write two localhost toy string-comparison functions—one early-exit and one constant-work—and measure timing distributions using random non-secret data.


### Exercise 2 — Create a threat model for a cryptographic operation in a cloud VM versus an embedded device with physical attacker access

Create a threat model for a cryptographic operation in a cloud VM versus an embedded device with physical attacker access.


### Exercise 3 — Document which side-channel mitigations belong to application code, cryptographic library, OS/hypervisor, hardware, and physical security

Document which side-channel mitigations belong to application code, cryptographic library, OS/hypervisor, hardware, and physical security.

Use the lab-record format in [Study Method](../Guides/STUDY-METHOD.md) for each exercise and keep all inputs synthetic or confined to the authorized lab.

## Knowledge checks

1. Explain the most important trust boundary in **Side Channels, Timing, Cache, Faults and Physical Leakage Models** without naming a security tool.
2. Give one example where cryptographic or authentication success still does **not** imply authorization success.
3. Describe one stale-state or replay condition relevant to this module.
4. Identify one telemetry source that can support a strong conclusion and one blind spot it still leaves.
5. Explain how you would turn a discovered weakness into a regression test rather than a one-time finding.

## Guided study workflow

Use [Study Method](../Guides/STUDY-METHOD.md). Complete at least one authorized exercise, preserve the evidence that supports your conclusion, and explain the module's main trust boundary and failure modes in your own words before moving on.

### Continue with

Choose **Learning paths** from the main menu for an ordered specialization, or use **Search lessons** to follow a concept into related modules.

---

# TPM, Secure Boot, Attestation, TEEs and Device Identity

Modern device trust uses hardware-backed keys, measured boot, secure boot, attestation, and trusted execution concepts. These mechanisms answer different questions and should not be collapsed into “the hardware is secure.”

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, or lab environments you own or are explicitly authorized to test. The exercises in this module are designed to prove security properties without targeting third parties.

## Learning objectives

By the end of this module you should be able to:

- Explain **Secure Boot** and connect it to a concrete trust boundary or security invariant.
- Explain **Measured boot** and connect it to a concrete trust boundary or security invariant.
- Explain **TPM keys** and connect it to a concrete trust boundary or security invariant.
- Explain **Attestation** and connect it to a concrete trust boundary or security invariant.
- Explain **TEEs** and connect it to a concrete trust boundary or security invariant.
- Explain **Device identity** and connect it to a concrete trust boundary or security invariant.

## Analysis method

Use the shared [Study Method](../Guides/STUDY-METHOD.md). For this module, first draw the relevant components and state transitions, then state one security invariant and identify the minimum evidence needed to test it safely.

## Deep concepts

### 1. Secure Boot

Secure Boot verifies components against an allowed trust policy before execution. It constrains unauthorized boot code but does not attest that a running application is correctly configured.



### 2. Measured boot

Measured boot records cryptographic measurements of boot components into protected state such as TPM PCRs. Measurements provide evidence; a verifier still needs policy for what measurements are acceptable.



### 3. TPM keys

TPMs can generate/seal keys, protect private key operations, and bind release to platform state. Backup/recovery design must consider what happens when hardware is replaced or measurements legitimately change.



### 4. Attestation

Attestation is evidence about a platform/workload state signed or vouched for by a trust anchor. Freshness, nonce/challenge handling, verifier trust, endorsement, privacy, and policy evaluation matter as much as the signature.



### 5. TEEs

Trusted execution environments aim to isolate code/data from parts of the surrounding system. Their boundary, memory protections, I/O path, side channels, rollback protection, and update mechanism are platform-specific.



### 6. Device identity

Hardware-backed device credentials can improve enrollment and workload identity, but device identity is not automatically user identity or authorization to a resource.



### 7. Key release

A powerful pattern is releasing a secret only when attestation satisfies policy. This turns measurement verification into an authorization dependency that must handle updates, failures, and revocation safely.



### 8. Lifecycle

Manufacturing, enrollment, ownership transfer, firmware update, credential rotation, RMA, decommissioning, and key destruction all affect hardware-rooted trust.



## Review focus

Apply the failure-mode taxonomy in [Study Method](../Guides/STUDY-METHOD.md), but keep the analysis specific to this lesson: identify the principal, resource, authority, mutable state, parser or policy boundary, and the telemetry that would distinguish a real control failure from misconfiguration or an observation gap.

## Authorized exercises

### Exercise 1 — Draw a boot trust chain for a modern laptop or phone using public vendor documentation and distinguish verification from measurement

Draw a boot trust chain for a modern laptop or phone using public vendor documentation and distinguish verification from measurement.


### Exercise 2 — Design an attestation verifier state machine: challenge, evidence, freshness check, identity validation, policy evaluation, decision, logging

Design an attestation verifier state machine: challenge, evidence, freshness check, identity validation, policy evaluation, decision, logging.


### Exercise 3 — Create a recovery plan for an application whose encryption key is sealed to hardware state and the motherboard must be replaced

Create a recovery plan for an application whose encryption key is sealed to hardware state and the motherboard must be replaced.

Use the lab-record format in [Study Method](../Guides/STUDY-METHOD.md) for each exercise and keep all inputs synthetic or confined to the authorized lab.

## Knowledge checks

1. Explain the most important trust boundary in **TPM, Secure Boot, Attestation, TEEs and Device Identity** without naming a security tool.
2. Give one example where cryptographic or authentication success still does **not** imply authorization success.
3. Describe one stale-state or replay condition relevant to this module.
4. Identify one telemetry source that can support a strong conclusion and one blind spot it still leaves.
5. Explain how you would turn a discovered weakness into a regression test rather than a one-time finding.

## Guided study workflow

Use [Study Method](../Guides/STUDY-METHOD.md). Complete at least one authorized exercise, preserve the evidence that supports your conclusion, and explain the module's main trust boundary and failure modes in your own words before moving on.

### Continue with

Choose **Learning paths** from the main menu for an ordered specialization, or use **Search lessons** to follow a concept into related modules.

---

# Serverless, Edge Workers, Functions and Event-Driven Cloud Security

Serverless platforms reduce infrastructure management while increasing reliance on IAM, event sources, managed services, deployment packages, and provider isolation. Security work shifts from host hardening toward authority, data flow, event validation, and observability.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, or lab environments you own or are explicitly authorized to test. The exercises in this module are designed to prove security properties without targeting third parties.

## Learning objectives

By the end of this module you should be able to:

- Explain **Invocation surface** and connect it to a concrete trust boundary or security invariant.
- Explain **Execution identity** and connect it to a concrete trust boundary or security invariant.
- Explain **Event trust** and connect it to a concrete trust boundary or security invariant.
- Explain **Ephemeral runtime** and connect it to a concrete trust boundary or security invariant.
- Explain **Secrets** and connect it to a concrete trust boundary or security invariant.
- Explain **Dependency packaging** and connect it to a concrete trust boundary or security invariant.

## Analysis method

Use the shared [Study Method](../Guides/STUDY-METHOD.md). For this module, first draw the relevant components and state transitions, then state one security invariant and identify the minimum evidence needed to test it safely.

## Deep concepts

### 1. Invocation surface

Functions can be invoked by HTTP, queues, storage events, schedules, database changes, or internal services. Inventory every trigger and the identity/context it supplies.



### 2. Execution identity

A function’s service role often defines its real blast radius. Apply least privilege per function or narrowly related workload; avoid broad shared roles.



### 3. Event trust

Cloud events are structured input, not inherently trusted input. Validate resource identity, tenant/account, event type, object path, replay/idempotency, and authorization assumptions.



### 4. Ephemeral runtime

Instances may be reused even though they are conceptually ephemeral. Do not depend on local process state for security, and avoid leaving sensitive data in temporary storage longer than necessary.



### 5. Secrets

Use managed secret/workload identity mechanisms and avoid embedding credentials in deployment packages or environment variables when a safer provider mechanism is available.



### 6. Dependency packaging

A small function can still contain a large dependency tree. Apply provenance, pinning, scanning, and minimal packaging just as for long-running services.



### 7. Edge execution

Edge workers run closer to users and may have constrained APIs but large request volume. Understand provider-specific isolation, regional data handling, cache behavior, and identity to origin services.



### 8. Observability and cost abuse

Log trigger identity, request/event IDs, principal, downstream calls, errors, throttling, and cost-related anomalies. Resource-consumption abuse can be a security and financial-availability issue.



## Review focus

Apply the failure-mode taxonomy in [Study Method](../Guides/STUDY-METHOD.md), but keep the analysis specific to this lesson: identify the principal, resource, authority, mutable state, parser or policy boundary, and the telemetry that would distinguish a real control failure from misconfiguration or an observation gap.

## Authorized exercises

### Exercise 1 — Model one photo-processing function triggered by object storage and identify what prevents another tenant/object path from being processed

Model one photo-processing function triggered by object storage and identify what prevents another tenant/object path from being processed.


### Exercise 2 — Write an IAM policy matrix for three functions that each need different storage/database actions

Write an IAM policy matrix for three functions that each need different storage/database actions.


### Exercise 3 — Create a replay/idempotency test plan for a harmless event-driven workflow

Create a replay/idempotency test plan for a harmless event-driven workflow.

Use the lab-record format in [Study Method](../Guides/STUDY-METHOD.md) for each exercise and keep all inputs synthetic or confined to the authorized lab.

## Knowledge checks

1. Explain the most important trust boundary in **Serverless, Edge Workers, Functions and Event-Driven Cloud Security** without naming a security tool.
2. Give one example where cryptographic or authentication success still does **not** imply authorization success.
3. Describe one stale-state or replay condition relevant to this module.
4. Identify one telemetry source that can support a strong conclusion and one blind spot it still leaves.
5. Explain how you would turn a discovered weakness into a regression test rather than a one-time finding.

## Guided study workflow

Use [Study Method](../Guides/STUDY-METHOD.md). Complete at least one authorized exercise, preserve the evidence that supports your conclusion, and explain the module's main trust boundary and failure modes in your own words before moving on.

### Continue with

Choose **Learning paths** from the main menu for an ordered specialization, or use **Search lessons** to follow a concept into related modules.

---

# Multi-Cloud, SaaS Federation, Tenant Isolation and Control Planes

Organizations increasingly depend on several clouds and SaaS platforms linked by federation and automation. The security challenge is not mastering every provider command—it is understanding control-plane authority, identity translation, tenant boundaries, and where policy drift occurs.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, or lab environments you own or are explicitly authorized to test. The exercises in this module are designed to prove security properties without targeting third parties.

## Learning objectives

By the end of this module you should be able to:

- Explain **Control vs data plane** and connect it to a concrete trust boundary or security invariant.
- Explain **Federation** and connect it to a concrete trust boundary or security invariant.
- Explain **Organization hierarchy** and connect it to a concrete trust boundary or security invariant.
- Explain **SaaS administrators** and connect it to a concrete trust boundary or security invariant.
- Explain **Tenant isolation** and connect it to a concrete trust boundary or security invariant.
- Explain **Cross-cloud automation** and connect it to a concrete trust boundary or security invariant.

## Analysis method

Use the shared [Study Method](../Guides/STUDY-METHOD.md). For this module, first draw the relevant components and state transitions, then state one security invariant and identify the minimum evidence needed to test it safely.

## Deep concepts

### 1. Control vs data plane

Control planes create identities, networks, keys, policies, and workloads. Data planes process application traffic. A control-plane identity may indirectly control enormous data-plane reach without touching the data directly.



### 2. Federation

Workforce and workload federation reduce static credentials but introduce trust between issuers, audiences, claims, tenants, and role mappings. Validate exact issuer/audience and constrain which external identities can assume local authority.



### 3. Organization hierarchy

Accounts/subscriptions/projects/folders/organizations define inheritance and administrative boundaries. Review where policy is inherited and which principals can move resources or alter parent-level controls.



### 4. SaaS administrators

SaaS global administrators, app-consent roles, API tokens, integrations, and marketplace apps can bypass ordinary user-level controls. Inventory and monitor privileged integrations.



### 5. Tenant isolation

Multi-tenant services need technical and operational separation across identity, storage, encryption context, support tooling, analytics, backups, and logs.



### 6. Cross-cloud automation

CI/CD and infrastructure automation frequently hold credentials to several providers. Prefer workload federation/short-lived credentials and limit the ability of one pipeline compromise to pivot across clouds.



### 7. Policy drift

Equivalent concepts have different names and semantics across providers. Use a normalized control model for MFA, public exposure, encryption, logging, network egress, key ownership, and break-glass access.



### 8. Central evidence

Aggregate identity changes, role assumptions, app-consent grants, resource-policy changes, key events, and network/public-exposure changes with provider/account context preserved.



## Review focus

Apply the failure-mode taxonomy in [Study Method](../Guides/STUDY-METHOD.md), but keep the analysis specific to this lesson: identify the principal, resource, authority, mutable state, parser or policy boundary, and the telemetry that would distinguish a real control failure from misconfiguration or an observation gap.

## Authorized exercises

### Exercise 1 — Create a provider-neutral matrix for identity, admin hierarchy, network policy, key management, audit logs, and public exposure across two hypothetical clouds

Create a provider-neutral matrix for identity, admin hierarchy, network policy, key management, audit logs, and public exposure across two hypothetical clouds.


### Exercise 2 — Model a SaaS marketplace integration and list every permission it could obtain, how it is revoked, and what happens when the employee owner leaves

Model a SaaS marketplace integration and list every permission it could obtain, how it is revoked, and what happens when the employee owner leaves.


### Exercise 3 — Design a cross-cloud break-glass procedure that avoids one shared permanent super-admin credential

Design a cross-cloud break-glass procedure that avoids one shared permanent super-admin credential.

Use the lab-record format in [Study Method](../Guides/STUDY-METHOD.md) for each exercise and keep all inputs synthetic or confined to the authorized lab.

## Knowledge checks

1. Explain the most important trust boundary in **Multi-Cloud, SaaS Federation, Tenant Isolation and Control Planes** without naming a security tool.
2. Give one example where cryptographic or authentication success still does **not** imply authorization success.
3. Describe one stale-state or replay condition relevant to this module.
4. Identify one telemetry source that can support a strong conclusion and one blind spot it still leaves.
5. Explain how you would turn a discovered weakness into a regression test rather than a one-time finding.

## Guided study workflow

Use [Study Method](../Guides/STUDY-METHOD.md). Complete at least one authorized exercise, preserve the evidence that supports your conclusion, and explain the module's main trust boundary and failure modes in your own words before moving on.

### Continue with

Choose **Learning paths** from the main menu for an ordered specialization, or use **Search lessons** to follow a concept into related modules.

---

# Endpoint EDR Internals, Telemetry and Response Architecture

Endpoint detection and response combines sensors, event collection, enrichment, behavioral analytics, response controls, and central management. This module explains the architecture so analysts can reason about what EDR can and cannot prove.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, or lab environments you own or are explicitly authorized to test. The exercises in this module are designed to prove security properties without targeting third parties.

## Learning objectives

By the end of this module you should be able to:

- Explain **Sensor placement** and connect it to a concrete trust boundary or security invariant.
- Explain **Process lineage** and connect it to a concrete trust boundary or security invariant.
- Explain **Content vs metadata** and connect it to a concrete trust boundary or security invariant.
- Explain **Behavioral detections** and connect it to a concrete trust boundary or security invariant.
- Explain **Response actions** and connect it to a concrete trust boundary or security invariant.
- Explain **Tamper protection** and connect it to a concrete trust boundary or security invariant.

## Analysis method

Use the shared [Study Method](../Guides/STUDY-METHOD.md). For this module, first draw the relevant components and state transitions, then state one security invariant and identify the minimum evidence needed to test it safely.

## Deep concepts

### 1. Sensor placement

Endpoint sensors may observe process creation, image loads, files, registry/configuration, network connections, authentication, scripts, kernel events, or security-provider telemetry. Coverage is platform/version dependent.



### 2. Process lineage

Parent/child trees are useful but imperfect: service managers, schedulers, shells, browsers, containers, and IPC can separate the logical initiator from the direct parent. Use multiple contextual fields.



### 3. Content vs metadata

Collecting hashes, paths, signer identity, command metadata, and behavior often provides value with lower privacy cost than indiscriminate content capture. Define collection boundaries explicitly.



### 4. Behavioral detections

Strong detections identify a meaningful behavior chain or invariant violation rather than a single tool name. Tool-independent logic survives renaming and benign administrative overlap better.



### 5. Response actions

Isolation, process termination, file quarantine, credential/session revocation, and remote collection have different risks. Response playbooks need approval thresholds and recovery paths.



### 6. Tamper protection

Security agents require privileged components and therefore need update integrity, configuration protection, service health monitoring, and clear behavior when the sensor stops reporting.



### 7. Cloud analytics

Central platforms correlate endpoint data with identity, email, cloud, and network signals. Preserve source timestamps, device identity, tenant, and schema version so correlation remains defensible.



### 8. Validation

Test detections with benign simulations that exercise the intended telemetry, and confirm both positive evidence and expected non-events. Avoid assuming a green dashboard means complete visibility.



## Review focus

Apply the failure-mode taxonomy in [Study Method](../Guides/STUDY-METHOD.md), but keep the analysis specific to this lesson: identify the principal, resource, authority, mutable state, parser or policy boundary, and the telemetry that would distinguish a real control failure from misconfiguration or an observation gap.

## Authorized exercises

### Exercise 1 — Design an endpoint event schema for process start that includes identity, parent, signer/hash, session, container context, and correlation ID

Design an endpoint event schema for process start that includes identity, parent, signer/hash, session, container context, and correlation ID.


### Exercise 2 — Create a detection test for a harmless unusual child-process pattern using local scripts; document false-positive conditions

Create a detection test for a harmless unusual child-process pattern using local scripts; document false-positive conditions.


### Exercise 3 — Write a response decision matrix for isolate host vs revoke session vs terminate process vs observe only

Write a response decision matrix for isolate host vs revoke session vs terminate process vs observe only.

Use the lab-record format in [Study Method](../Guides/STUDY-METHOD.md) for each exercise and keep all inputs synthetic or confined to the authorized lab.

## Knowledge checks

1. Explain the most important trust boundary in **Endpoint EDR Internals, Telemetry and Response Architecture** without naming a security tool.
2. Give one example where cryptographic or authentication success still does **not** imply authorization success.
3. Describe one stale-state or replay condition relevant to this module.
4. Identify one telemetry source that can support a strong conclusion and one blind spot it still leaves.
5. Explain how you would turn a discovered weakness into a regression test rather than a one-time finding.

## Guided study workflow

Use [Study Method](../Guides/STUDY-METHOD.md). Complete at least one authorized exercise, preserve the evidence that supports your conclusion, and explain the module's main trust boundary and failure modes in your own words before moving on.

### Continue with

Choose **Learning paths** from the main menu for an ordered specialization, or use **Search lessons** to follow a concept into related modules.

---

# Threat Emulation, Adversary Simulation and Purple-Team Lab Design

Threat emulation is useful when it validates controls against realistic behavior while remaining bounded and observable. This module teaches how to translate threat intelligence or ATT&CK techniques into safe tests, expected telemetry, and remediation loops.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, or lab environments you own or are explicitly authorized to test. The exercises in this module are designed to prove security properties without targeting third parties.

## Learning objectives

By the end of this module you should be able to:

- Explain **Objective first** and connect it to a concrete trust boundary or security invariant.
- Explain **Behavior abstraction** and connect it to a concrete trust boundary or security invariant.
- Explain **Safety constraints** and connect it to a concrete trust boundary or security invariant.
- Explain **ATT&CK mapping** and connect it to a concrete trust boundary or security invariant.
- Explain **Detection contract** and connect it to a concrete trust boundary or security invariant.
- Explain **Purple-team loop** and connect it to a concrete trust boundary or security invariant.

## Analysis method

Use the shared [Study Method](../Guides/STUDY-METHOD.md). For this module, first draw the relevant components and state transitions, then state one security invariant and identify the minimum evidence needed to test it safely.

## Deep concepts

### 1. Objective first

Define the control or detection question before choosing a technique. “Can we detect this credential-access behavior?” is testable; “act like an attacker” is too vague.



### 2. Behavior abstraction

Represent the behavior independently of a specific offensive tool. Describe required privileges, system action, data touched, telemetry expected, and stop conditions.



### 3. Safety constraints

Use synthetic accounts/data, rate limits, test hosts, pre-approved commands, bounded network destinations, snapshots, and immediate stop triggers. High realism is not worth uncontrolled impact.



### 4. ATT&CK mapping

ATT&CK technique IDs can organize coverage, but mapping should follow observed behavior rather than labels copied from a tool. Record tactic, technique/sub-technique, platform, and evidence.



### 5. Detection contract

For each test, define which sensor/log should observe it, which fields are required, expected alert logic, acceptable delay, and what missing telemetry means.



### 6. Purple-team loop

Prepare → execute bounded behavior → observe → explain gaps → improve logging/detection/control → rerun → retain a regression fixture.



### 7. Metrics

Useful measures include test pass rate, telemetry completeness, alert latency, analyst interpretation accuracy, remediation time, and regression stability—not just number of techniques executed.



### 8. Reporting

Separate control failure, telemetry failure, detection-logic failure, triage failure, and response failure. They require different fixes.



## Review focus

Apply the failure-mode taxonomy in [Study Method](../Guides/STUDY-METHOD.md), but keep the analysis specific to this lesson: identify the principal, resource, authority, mutable state, parser or policy boundary, and the telemetry that would distinguish a real control failure from misconfiguration or an observation gap.

## Authorized exercises

### Exercise 1 — Create a five-test purple-team plan using harmless local behaviors such as file creation, process start, failed login, service restart, and DNS lookup

Create a five-test purple-team plan using harmless local behaviors such as file creation, process start, failed login, service restart, and DNS lookup.


### Exercise 2 — For each test, define ATT&CK mapping only after describing the actual behavior and expected evidence

For each test, define ATT&CK mapping only after describing the actual behavior and expected evidence.


### Exercise 3 — Build a regression sheet that records test version, environment, expected events, alert outcome, and remediation status

Build a regression sheet that records test version, environment, expected events, alert outcome, and remediation status.

Use the lab-record format in [Study Method](../Guides/STUDY-METHOD.md) for each exercise and keep all inputs synthetic or confined to the authorized lab.

## Knowledge checks

1. Explain the most important trust boundary in **Threat Emulation, Adversary Simulation and Purple-Team Lab Design** without naming a security tool.
2. Give one example where cryptographic or authentication success still does **not** imply authorization success.
3. Describe one stale-state or replay condition relevant to this module.
4. Identify one telemetry source that can support a strong conclusion and one blind spot it still leaves.
5. Explain how you would turn a discovered weakness into a regression test rather than a one-time finding.

## Guided study workflow

Use [Study Method](../Guides/STUDY-METHOD.md). Complete at least one authorized exercise, preserve the evidence that supports your conclusion, and explain the module's main trust boundary and failure modes in your own words before moving on.

### Continue with

Choose **Learning paths** from the main menu for an ordered specialization, or use **Search lessons** to follow a concept into related modules.

---

# Advanced Code Auditing, Static Analysis, Dataflow and Taint Reasoning

Manual code review becomes much more effective when paired with explicit dataflow, trust-boundary, and state reasoning. This module teaches source-to-sink analysis, interprocedural thinking, variant analysis, and how static-analysis tools approximate program behavior.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, or lab environments you own or are explicitly authorized to test. The exercises in this module are designed to prove security properties without targeting third parties.

## Learning objectives

By the end of this module you should be able to:

- Explain **Sources and sinks** and connect it to a concrete trust boundary or security invariant.
- Explain **Taint analysis** and connect it to a concrete trust boundary or security invariant.
- Explain **Control flow** and connect it to a concrete trust boundary or security invariant.
- Explain **Interprocedural analysis** and connect it to a concrete trust boundary or security invariant.
- Explain **Stateful bugs** and connect it to a concrete trust boundary or security invariant.
- Explain **Variant analysis** and connect it to a concrete trust boundary or security invariant.

## Analysis method

Use the shared [Study Method](../Guides/STUDY-METHOD.md). For this module, first draw the relevant components and state transitions, then state one security invariant and identify the minimum evidence needed to test it safely.

## Deep concepts

### 1. Sources and sinks

A source introduces untrusted or security-relevant data; a sink performs a sensitive operation. The key question is which transformations, validations, encodings, and authorization checks occur on every feasible path between them.



### 2. Taint analysis

Taint engines approximate how labeled data flows through variables, calls, objects, and frameworks. Good rules model sanitizers precisely; marking every validation as a sanitizer creates false negatives.



### 3. Control flow

Conditions, exceptions, callbacks, asynchronous tasks, early returns, and error paths can bypass intended checks. Review the less-common paths, not only the happy path.



### 4. Interprocedural analysis

Security decisions often cross helper functions, middleware, ORMs, RPC layers, and framework-generated code. Build summaries for security-relevant functions and track caller/callee assumptions.



### 5. Stateful bugs

Authorization, race conditions, replay, and workflow abuse require state-machine reasoning that pure taint flow may miss. Annotate states and allowed transitions alongside dataflow.



### 6. Variant analysis

After finding one root cause, search for structurally similar code: same helper, same unsafe API, same missing authorization pattern, same parser, or same data transformation.



### 7. Tool limitations

Static analyzers trade soundness, completeness, performance, and framework knowledge. A clean scan is evidence about the tool/model, not proof the code is secure.



### 8. Review output

A high-quality finding includes reachable input, security-sensitive sink/state change, missing invariant, realistic preconditions, root cause, fix pattern, and a regression test.



## Review focus

Apply the failure-mode taxonomy in [Study Method](../Guides/STUDY-METHOD.md), but keep the analysis specific to this lesson: identify the principal, resource, authority, mutable state, parser or policy boundary, and the telemetry that would distinguish a real control failure from misconfiguration or an observation gap.

## Authorized exercises

### Exercise 1 — Audit a deliberately small local program and draw a source→transform→validation→sink dataflow for one input

Audit a deliberately small local program and draw a source→transform→validation→sink dataflow for one input.


### Exercise 2 — Write a toy static-analysis rule or grep-like check for one unsafe coding pattern and document its false positives/false negatives

Write a toy static-analysis rule or grep-like check for one unsafe coding pattern and document its false positives/false negatives.


### Exercise 3 — Perform variant analysis after fixing one toy bug and search sibling functions for the same root cause

Perform variant analysis after fixing one toy bug and search sibling functions for the same root cause.

Use the lab-record format in [Study Method](../Guides/STUDY-METHOD.md) for each exercise and keep all inputs synthetic or confined to the authorized lab.

## Knowledge checks

1. Explain the most important trust boundary in **Advanced Code Auditing, Static Analysis, Dataflow and Taint Reasoning** without naming a security tool.
2. Give one example where cryptographic or authentication success still does **not** imply authorization success.
3. Describe one stale-state or replay condition relevant to this module.
4. Identify one telemetry source that can support a strong conclusion and one blind spot it still leaves.
5. Explain how you would turn a discovered weakness into a regression test rather than a one-time finding.

## Guided study workflow

Use [Study Method](../Guides/STUDY-METHOD.md). Complete at least one authorized exercise, preserve the evidence that supports your conclusion, and explain the module's main trust boundary and failure modes in your own words before moving on.

### Continue with

Choose **Learning paths** from the main menu for an ordered specialization, or use **Search lessons** to follow a concept into related modules.

---

# Vulnerability Research: Reproduction, Regression and Coordinated Disclosure

Professional vulnerability research is an evidence discipline. This module focuses on reproducing public/owned-lab issues safely, identifying root cause, proving a fix, comparing versions, and communicating findings without expanding harm.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, or lab environments you own or are explicitly authorized to test. The exercises in this module are designed to prove security properties without targeting third parties.

## Learning objectives

By the end of this module you should be able to:

- Explain **Reproduction environment** and connect it to a concrete trust boundary or security invariant.
- Explain **Minimal trigger** and connect it to a concrete trust boundary or security invariant.
- Explain **Root cause** and connect it to a concrete trust boundary or security invariant.
- Explain **Version comparison** and connect it to a concrete trust boundary or security invariant.
- Explain **Severity** and connect it to a concrete trust boundary or security invariant.
- Explain **Regression** and connect it to a concrete trust boundary or security invariant.

## Analysis method

Use the shared [Study Method](../Guides/STUDY-METHOD.md). For this module, first draw the relevant components and state transitions, then state one security invariant and identify the minimum evidence needed to test it safely.

## Deep concepts

### 1. Reproduction environment

Record exact version, build options, architecture, configuration, input fixture, dependency versions, and isolation. A reproduction that depends on undocumented machine state is difficult to trust.



### 2. Minimal trigger

Reduce a failing input to the smallest artifact that still demonstrates the bug. Minimization separates root cause from incidental complexity and makes regression tests stable.



### 3. Root cause

Distinguish symptom, vulnerable condition, security boundary violated, and root-cause coding/design error. A crash alone does not establish exploitability or impact.



### 4. Version comparison

Patch diffing and bisecting can identify when behavior changed. Treat public patches as engineering evidence, not an invitation to weaponize a vulnerability against deployed systems.



### 5. Severity

Estimate impact using realistic privileges, reachability, user interaction, data/control affected, exploit reliability, mitigations, and environmental context. Avoid inflating severity from theoretical outcomes unsupported by evidence.



### 6. Regression

Turn the minimized trigger and security invariant into a test that passes after the fix. Prefer a test that catches the bug class when feasible.



### 7. Disclosure

Follow vendor/project policy, send minimal sufficient details privately when appropriate, agree on timelines when possible, avoid publishing secrets or unnecessary exploitation detail, and preserve correspondence/evidence.



### 8. Research ethics

Stop when a test reaches third-party data, production impact, unknown authorization, or a step whose main value is offensive capability rather than proving the flaw.



## Review focus

Apply the failure-mode taxonomy in [Study Method](../Guides/STUDY-METHOD.md), but keep the analysis specific to this lesson: identify the principal, resource, authority, mutable state, parser or policy boundary, and the telemetry that would distinguish a real control failure from misconfiguration or an observation gap.

## Authorized exercises

### Exercise 1 — Take a harmless intentionally buggy parser and practice input minimization until only the root-cause trigger remains

Take a harmless intentionally buggy parser and practice input minimization until only the root-cause trigger remains.


### Exercise 2 — Compare two local versions of toy source code, identify the security-relevant change, and write a regression test

Compare two local versions of toy source code, identify the security-relevant change, and write a regression test.


### Exercise 3 — Draft a coordinated-disclosure report for the toy bug including scope, impact, reproduction, root cause, remediation, and timeline

Draft a coordinated-disclosure report for the toy bug including scope, impact, reproduction, root cause, remediation, and timeline.

Use the lab-record format in [Study Method](../Guides/STUDY-METHOD.md) for each exercise and keep all inputs synthetic or confined to the authorized lab.

## Knowledge checks

1. Explain the most important trust boundary in **Vulnerability Research: Reproduction, Regression and Coordinated Disclosure** without naming a security tool.
2. Give one example where cryptographic or authentication success still does **not** imply authorization success.
3. Describe one stale-state or replay condition relevant to this module.
4. Identify one telemetry source that can support a strong conclusion and one blind spot it still leaves.
5. Explain how you would turn a discovered weakness into a regression test rather than a one-time finding.

## Guided study workflow

Use [Study Method](../Guides/STUDY-METHOD.md). Complete at least one authorized exercise, preserve the evidence that supports your conclusion, and explain the module's main trust boundary and failure modes in your own words before moving on.

### Continue with

Choose **Learning paths** from the main menu for an ordered specialization, or use **Search lessons** to follow a concept into related modules.

---

# Advanced Authorized Labs II: Systems, Identity, Cloud and Application Security

This lab module integrates the advanced lessons into bounded projects. Every exercise uses owned systems, disposable VMs/containers, localhost services, synthetic identities, or static/public artifacts. The goal is evidence and defensive understanding rather than gaining access.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, or lab environments you own or are explicitly authorized to test. The exercises in this module are designed to prove security properties without targeting third parties.

## Learning objectives

By the end of this module you should be able to:

- Explain **Lab architecture** and connect it to a concrete trust boundary or security invariant.
- Explain **Evidence package** and connect it to a concrete trust boundary or security invariant.
- Explain **Identity lab** and connect it to a concrete trust boundary or security invariant.
- Explain **Web/API lab** and connect it to a concrete trust boundary or security invariant.
- Explain **Linux isolation lab** and connect it to a concrete trust boundary or security invariant.
- Explain **Supply-chain lab** and connect it to a concrete trust boundary or security invariant.

## Analysis method

Use the shared [Study Method](../Guides/STUDY-METHOD.md). For this module, first draw the relevant components and state transitions, then state one security invariant and identify the minimum evidence needed to test it safely.

## Deep concepts

### 1. Lab architecture

Use snapshots, isolated networks, synthetic data, dedicated test identities, clear IP/domain allowlists, and a written objective before execution.



### 2. Evidence package

For each lab keep environment metadata, hypothesis, commands/configuration used, hashes, screenshots/log excerpts where useful, interpretation, cleanup, and regression result.



### 3. Identity lab

Build a toy identity graph with users, groups, roles, workload identities, and resource policies; detect an unintended privilege path and repair the policy.



### 4. Web/API lab

Create a localhost API with object-level authorization and deliberately add then fix one broken authorization test. Verify the fix with negative regression cases.



### 5. Linux isolation lab

Run a disposable service with reduced capabilities, filesystem permissions, and network exposure; compare before/after effective privilege.



### 6. Supply-chain lab

Create a source commit, local build artifact, SBOM-like dependency list, provenance record, and verification script that rejects an altered artifact digest.



### 7. Detection lab

Generate benign process/file/network events, verify telemetry, write a detection, tune one false positive, and retain a replay fixture.



### 8. Forensics lab

Build a synthetic incident timeline from prepared logs/files and produce a short evidence-based narrative with uncertainty explicitly marked.



## Review focus

Apply the failure-mode taxonomy in [Study Method](../Guides/STUDY-METHOD.md), but keep the analysis specific to this lesson: identify the principal, resource, authority, mutable state, parser or policy boundary, and the telemetry that would distinguish a real control failure from misconfiguration or an observation gap.

## Authorized exercises

### Exercise 1 — Complete any four integrated labs and produce one consistent report template across all of them

Complete any four integrated labs and produce one consistent report template across all of them.


### Exercise 2 — For one lab, intentionally remove a telemetry source and explain what conclusions are no longer supportable

For one lab, intentionally remove a telemetry source and explain what conclusions are no longer supportable.


### Exercise 3 — For one lab, change the environment version/configuration and verify whether the regression test still proves the same invariant

For one lab, change the environment version/configuration and verify whether the regression test still proves the same invariant.

Use the lab-record format in [Study Method](../Guides/STUDY-METHOD.md) for each exercise and keep all inputs synthetic or confined to the authorized lab.

## Knowledge checks

1. Explain the most important trust boundary in **Advanced Authorized Labs II: Systems, Identity, Cloud and Application Security** without naming a security tool.
2. Give one example where cryptographic or authentication success still does **not** imply authorization success.
3. Describe one stale-state or replay condition relevant to this module.
4. Identify one telemetry source that can support a strong conclusion and one blind spot it still leaves.
5. Explain how you would turn a discovered weakness into a regression test rather than a one-time finding.

## Guided study workflow

Use [Study Method](../Guides/STUDY-METHOD.md). Complete at least one authorized exercise, preserve the evidence that supports your conclusion, and explain the module's main trust boundary and failure modes in your own words before moving on.

### Continue with

Choose **Learning paths** from the main menu for an ordered specialization, or use **Search lessons** to follow a concept into related modules.

---

# WebAssembly, JVM, CLR and Managed Runtime Security

Managed runtimes and bytecode VMs create different security boundaries from native binaries. Memory safety may improve, but deserialization, reflection, dynamic loading, sandbox escapes, native interfaces, JIT compilation, and capability exposure remain important.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, or lab environments you own or are explicitly authorized to test. The exercises in this module are designed to prove security properties without targeting third parties.

## Learning objectives

By the end of this module you should be able to:

- Explain **Bytecode verification** and connect it to a concrete trust boundary or security invariant.
- Explain **Memory model** and connect it to a concrete trust boundary or security invariant.
- Explain **JIT trust** and connect it to a concrete trust boundary or security invariant.
- Explain **Reflection and dynamic loading** and connect it to a concrete trust boundary or security invariant.
- Explain **Deserialization** and connect it to a concrete trust boundary or security invariant.
- Explain **WebAssembly imports** and connect it to a concrete trust boundary or security invariant.

## Analysis method

Use the shared [Study Method](../Guides/STUDY-METHOD.md). For this module, first draw the relevant components and state transitions, then state one security invariant and identify the minimum evidence needed to test it safely.

## Deep concepts

### 1. Bytecode verification

Managed runtimes validate or constrain bytecode/module structure before execution. Verification reduces classes of malformed code but does not prove application authorization or logic is safe.



### 2. Memory model

JVM/CLR memory safety prevents many direct pointer errors in ordinary managed code, while unsafe/native interop reintroduces native memory risks. WebAssembly uses linear memory and explicit host imports.



### 3. JIT trust

Just-in-time compilers translate frequently executed code into native instructions. They are complex privileged components inside the runtime security model and require regular patching/hardening.



### 4. Reflection and dynamic loading

Reflection, plugins, class loading, expression engines, and dynamic assembly/module loading can convert data or configuration into powerful behavior. Apply allowlists and signature/provenance controls where appropriate.



### 5. Deserialization

Object serialization frameworks can instantiate types or invoke callbacks. Prefer simple data formats/schemas and treat untrusted native object deserialization as a high-risk design choice.



### 6. WebAssembly imports

A Wasm module can access only capabilities exposed by its host/runtime model. The host import surface, filesystem/network preopens, and embedding application are the real security boundary.



### 7. Native interfaces

JNI, P/Invoke, FFI, browser/runtime host calls, and native extensions cross from managed assumptions into native code. Inventory those edges and validate data/length/ownership carefully.



### 8. Sandbox verification

Test what the runtime can actually access: files, environment, network, clocks, randomness, devices, host calls, and process creation. Configuration determines the practical sandbox.



## Review focus

Apply the failure-mode taxonomy in [Study Method](../Guides/STUDY-METHOD.md), but keep the analysis specific to this lesson: identify the principal, resource, authority, mutable state, parser or policy boundary, and the telemetry that would distinguish a real control failure from misconfiguration or an observation gap.

## Authorized exercises

### Exercise 1 — Create a harmless local Wasm or managed-language hello-world and document every capability the runtime exposes to it

Create a harmless local Wasm or managed-language hello-world and document every capability the runtime exposes to it.


### Exercise 2 — Build a safe deserialization threat model comparing plain JSON DTO parsing with native object deserialization

Build a safe deserialization threat model comparing plain JSON DTO parsing with native object deserialization.


### Exercise 3 — Inventory native/FFI dependencies in a small managed application and classify why each trust-boundary crossing exists

Inventory native/FFI dependencies in a small managed application and classify why each trust-boundary crossing exists.

Use the lab-record format in [Study Method](../Guides/STUDY-METHOD.md) for each exercise and keep all inputs synthetic or confined to the authorized lab.

## Knowledge checks

1. Explain the most important trust boundary in **WebAssembly, JVM, CLR and Managed Runtime Security** without naming a security tool.
2. Give one example where cryptographic or authentication success still does **not** imply authorization success.
3. Describe one stale-state or replay condition relevant to this module.
4. Identify one telemetry source that can support a strong conclusion and one blind spot it still leaves.
5. Explain how you would turn a discovered weakness into a regression test rather than a one-time finding.

## Guided study workflow

Use [Study Method](../Guides/STUDY-METHOD.md). Complete at least one authorized exercise, preserve the evidence that supports your conclusion, and explain the module's main trust boundary and failure modes in your own words before moving on.

### Continue with

Choose **Learning paths** from the main menu for an ordered specialization, or use **Search lessons** to follow a concept into related modules.

---

# Browser Extensions, Electron and Desktop Web Runtime Security

Browser extensions and desktop web runtimes combine web content with privileged APIs. Security depends on permission scope, origin isolation, IPC boundaries, update trust, content handling, and whether remote data can reach privileged native functionality.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, or lab environments you own or are explicitly authorized to test. The exercises in this module are designed to prove security properties without targeting third parties.

## Learning objectives

By the end of this module you should be able to:

- Explain **Extension permissions** and connect it to a concrete trust boundary or security invariant.
- Explain **Content scripts** and connect it to a concrete trust boundary or security invariant.
- Explain **Extension CSP** and connect it to a concrete trust boundary or security invariant.
- Explain **Electron isolation** and connect it to a concrete trust boundary or security invariant.
- Explain **IPC authorization** and connect it to a concrete trust boundary or security invariant.
- Explain **Update trust** and connect it to a concrete trust boundary or security invariant.

## Analysis method

Use the shared [Study Method](../Guides/STUDY-METHOD.md). For this module, first draw the relevant components and state transitions, then state one security invariant and identify the minimum evidence needed to test it safely.

## Deep concepts

### 1. Extension permissions

Host permissions and privileged APIs should be minimal and user-understandable. Broad match patterns can turn one extension compromise into access across many sites.



### 2. Content scripts

Content scripts interact with page DOM but operate under extension-specific isolation rules. Message passing between page, content script, and background/service worker should validate sender and message shape.



### 3. Extension CSP

Content Security Policy and restrictions on remote code reduce the risk of turning web injection into extension-level code execution. Bundled, reviewable code is easier to trust than runtime-fetched logic.



### 4. Electron isolation

Context isolation, sandboxing, nodeIntegration settings, preload scripts, IPC handlers, navigation controls, and external-link handling define the renderer-to-native trust boundary.



### 5. IPC authorization

An IPC channel is effectively an API. Validate caller context, operation, arguments, allowed paths/URLs, and response data rather than exposing generic “run/read/write” primitives.



### 6. Update trust

Extensions and desktop apps often auto-update. Protect signing/release infrastructure, verify update channels, and consider rollback/downgrade behavior.



### 7. Remote content

Loading arbitrary remote pages into privileged desktop contexts is dangerous. Separate untrusted content from native-capable contexts and use explicit allowlists/navigation policies.



### 8. Secrets and local data

Browser storage, extension storage, app config, local databases, caches, and logs can contain tokens or sensitive history. Minimize retention and use OS-backed protection where appropriate.



## Review focus

Apply the failure-mode taxonomy in [Study Method](../Guides/STUDY-METHOD.md), but keep the analysis specific to this lesson: identify the principal, resource, authority, mutable state, parser or policy boundary, and the telemetry that would distinguish a real control failure from misconfiguration or an observation gap.

## Authorized exercises

### Exercise 1 — Review the manifest/permissions of an extension you own or a sample extension and justify each requested permission

Review the manifest/permissions of an extension you own or a sample extension and justify each requested permission.


### Exercise 2 — Design an Electron IPC API with three narrowly scoped operations instead of one generic privileged operation

Design an Electron IPC API with three narrowly scoped operations instead of one generic privileged operation.


### Exercise 3 — Create a trust-boundary diagram for page → content script → extension worker → native helper and list validation required at each edge

Create a trust-boundary diagram for page → content script → extension worker → native helper and list validation required at each edge.

Use the lab-record format in [Study Method](../Guides/STUDY-METHOD.md) for each exercise and keep all inputs synthetic or confined to the authorized lab.

## Knowledge checks

1. Explain the most important trust boundary in **Browser Extensions, Electron and Desktop Web Runtime Security** without naming a security tool.
2. Give one example where cryptographic or authentication success still does **not** imply authorization success.
3. Describe one stale-state or replay condition relevant to this module.
4. Identify one telemetry source that can support a strong conclusion and one blind spot it still leaves.
5. Explain how you would turn a discovered weakness into a regression test rather than a one-time finding.

## Guided study workflow

Use [Study Method](../Guides/STUDY-METHOD.md). Complete at least one authorized exercise, preserve the evidence that supports your conclusion, and explain the module's main trust boundary and failure modes in your own words before moving on.

### Continue with

Choose **Learning paths** from the main menu for an ordered specialization, or use **Search lessons** to follow a concept into related modules.

---

# Workload Identity, SPIFFE/SPIRE, mTLS and Zero-Trust Service Identity

Modern infrastructure increasingly replaces static service passwords with short-lived workload identities. This module explains identity issuance, attestation, trust domains, certificate/token rotation, service-to-service policy, and failure modes.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, or lab environments you own or are explicitly authorized to test. The exercises in this module are designed to prove security properties without targeting third parties.

## Learning objectives

By the end of this module you should be able to:

- Explain **Workload identity** and connect it to a concrete trust boundary or security invariant.
- Explain **SPIFFE IDs** and connect it to a concrete trust boundary or security invariant.
- Explain **Attestation** and connect it to a concrete trust boundary or security invariant.
- Explain **Short-lived credentials** and connect it to a concrete trust boundary or security invariant.
- Explain **mTLS** and connect it to a concrete trust boundary or security invariant.
- Explain **Trust domains** and connect it to a concrete trust boundary or security invariant.

## Analysis method

Use the shared [Study Method](../Guides/STUDY-METHOD.md). For this module, first draw the relevant components and state transitions, then state one security invariant and identify the minimum evidence needed to test it safely.

## Deep concepts

### 1. Workload identity

A workload identity represents a running service/process instance rather than a human. It should be derived from trusted workload/platform attributes and have a lifecycle aligned with the workload.



### 2. SPIFFE IDs

SPIFFE defines identity names within trust domains. The ID is an identifier, not authorization itself; policy decides what that identity may access.



### 3. Attestation

Identity issuance depends on node/workload attestation. The issuer needs trustworthy signals about where and what is running before minting credentials.



### 4. Short-lived credentials

Short-lived X.509 SVIDs or JWT-style credentials reduce dependence on manual secret rotation. Availability and clock/time correctness become important operational dependencies.



### 5. mTLS

Mutual TLS can authenticate both ends of a connection. Authorization still needs service/resource context, and certificate trust must be scoped so unrelated trust domains are not accepted accidentally.



### 6. Trust domains

Federating trust domains creates explicit cross-domain identity relationships. Keep mappings narrow and avoid translating broad external identities into powerful local ones.



### 7. Rotation and revocation

Short lifetimes can reduce the need for immediate revocation but do not eliminate emergency response. Plan issuer/key rotation, trust-bundle updates, compromised-node handling, and stale workload cleanup.



### 8. Policy and telemetry

Log workload identity, destination service, authorization decision, policy version, and certificate/token metadata without storing private keys. This makes service-to-service authority paths auditable.



## Review focus

Apply the failure-mode taxonomy in [Study Method](../Guides/STUDY-METHOD.md), but keep the analysis specific to this lesson: identify the principal, resource, authority, mutable state, parser or policy boundary, and the telemetry that would distinguish a real control failure from misconfiguration or an observation gap.

## Authorized exercises

### Exercise 1 — Design a three-service toy architecture using short-lived workload identities and write an allow matrix for service-to-service calls

Design a three-service toy architecture using short-lived workload identities and write an allow matrix for service-to-service calls.


### Exercise 2 — Model what changes when one node is considered untrusted: which credentials expire, what should be denied, and what evidence is needed

Model what changes when one node is considered untrusted: which credentials expire, what should be denied, and what evidence is needed.


### Exercise 3 — Compare static API keys, cloud workload federation, and SPIFFE-style identities across rotation, attribution, and blast radius

Compare static API keys, cloud workload federation, and SPIFFE-style identities across rotation, attribution, and blast radius.

Use the lab-record format in [Study Method](../Guides/STUDY-METHOD.md) for each exercise and keep all inputs synthetic or confined to the authorized lab.

## Knowledge checks

1. Explain the most important trust boundary in **Workload Identity, SPIFFE/SPIRE, mTLS and Zero-Trust Service Identity** without naming a security tool.
2. Give one example where cryptographic or authentication success still does **not** imply authorization success.
3. Describe one stale-state or replay condition relevant to this module.
4. Identify one telemetry source that can support a strong conclusion and one blind spot it still leaves.
5. Explain how you would turn a discovered weakness into a regression test rather than a one-time finding.

## Guided study workflow

Use [Study Method](../Guides/STUDY-METHOD.md). Complete at least one authorized exercise, preserve the evidence that supports your conclusion, and explain the module's main trust boundary and failure modes in your own words before moving on.

### Continue with

Choose **Learning paths** from the main menu for an ordered specialization, or use **Search lessons** to follow a concept into related modules.

---

# Data Security, DLP, Tokenization, Privacy Engineering and Data Lifecycle

Security programs often protect infrastructure better than the data itself. This module maps data from collection through use, sharing, analytics, backup, archival, and deletion, then connects classification, minimization, tokenization, DLP, access control, and privacy engineering.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, or lab environments you own or are explicitly authorized to test. The exercises in this module are designed to prove security properties without targeting third parties.

## Learning objectives

By the end of this module you should be able to:

- Explain **Data inventory** and connect it to a concrete trust boundary or security invariant.
- Explain **Minimization** and connect it to a concrete trust boundary or security invariant.
- Explain **Classification** and connect it to a concrete trust boundary or security invariant.
- Explain **Tokenization** and connect it to a concrete trust boundary or security invariant.
- Explain **DLP** and connect it to a concrete trust boundary or security invariant.
- Explain **Analytics and AI** and connect it to a concrete trust boundary or security invariant.

## Analysis method

Use the shared [Study Method](../Guides/STUDY-METHOD.md). For this module, first draw the relevant components and state transitions, then state one security invariant and identify the minimum evidence needed to test it safely.

## Deep concepts

### 1. Data inventory

Know what data exists, purpose, owner, sensitivity, location, format, residency, users, retention, and downstream copies. Discovery without ownership does not create accountability.



### 2. Minimization

The safest sensitive field is often the one never collected. Limit collection, precision, retention, and propagation to what the business purpose actually requires.



### 3. Classification

Classification should drive concrete controls such as access, encryption, logging, export restrictions, retention, and review—not merely add labels.



### 4. Tokenization

Tokenization replaces a sensitive value with a surrogate while a protected service maps between them. The token vault/service becomes a critical trust boundary; format-preserving tokens can still reveal structural information.



### 5. DLP

DLP uses content, context, labels, destination, and behavior to detect/limit data movement. High-quality deployment tunes false positives and defines whether controls block, warn, encrypt, quarantine, or simply log.



### 6. Analytics and AI

Training, analytics, and AI pipelines often create secondary copies/features/embeddings. Include them in data lineage, retention, access control, and deletion design.



### 7. Deletion

Deletion must address primary stores, replicas, caches, indexes, object versions, backups, exports, logs, and derived datasets according to policy and technical feasibility.



### 8. Privacy engineering

Purpose limitation, transparency, user rights, minimization, pseudonymization, access controls, and measurable retention are engineering requirements, not only legal-document concerns.



## Review focus

Apply the failure-mode taxonomy in [Study Method](../Guides/STUDY-METHOD.md), but keep the analysis specific to this lesson: identify the principal, resource, authority, mutable state, parser or policy boundary, and the telemetry that would distinguish a real control failure from misconfiguration or an observation gap.

## Authorized exercises

### Exercise 1 — Build a data-flow map for a hypothetical signup form from browser to API, database, analytics, logs, backups, and support tools

Build a data-flow map for a hypothetical signup form from browser to API, database, analytics, logs, backups, and support tools.


### Exercise 2 — Replace one sensitive identifier in the design with a tokenization service and analyze the new trust boundary

Replace one sensitive identifier in the design with a tokenization service and analyze the new trust boundary.


### Exercise 3 — Create a retention/deletion matrix listing primary data, caches, logs, backups, exports, and derived analytics

Create a retention/deletion matrix listing primary data, caches, logs, backups, exports, and derived analytics.

Use the lab-record format in [Study Method](../Guides/STUDY-METHOD.md) for each exercise and keep all inputs synthetic or confined to the authorized lab.

## Knowledge checks

1. Explain the most important trust boundary in **Data Security, DLP, Tokenization, Privacy Engineering and Data Lifecycle** without naming a security tool.
2. Give one example where cryptographic or authentication success still does **not** imply authorization success.
3. Describe one stale-state or replay condition relevant to this module.
4. Identify one telemetry source that can support a strong conclusion and one blind spot it still leaves.
5. Explain how you would turn a discovered weakness into a regression test rather than a one-time finding.

## Guided study workflow

Use [Study Method](../Guides/STUDY-METHOD.md). Complete at least one authorized exercise, preserve the evidence that supports your conclusion, and explain the module's main trust boundary and failure modes in your own words before moving on.

### Continue with

Choose **Learning paths** from the main menu for an ordered specialization, or use **Search lessons** to follow a concept into related modules.

---

# Master Capstones, Research Portfolio and Deep Security Practice

The final module turns the guide into demonstrable skill. The capstones require architecture reasoning, safe experiments, evidence, remediation, detection, and clear writing. A strong portfolio shows repeatable thinking rather than screenshots of tools.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, or lab environments you own or are explicitly authorized to test. The exercises in this module are designed to prove security properties without targeting third parties.

## Learning objectives

By the end of this module you should be able to:

- Explain **Capstone standard** and connect it to a concrete trust boundary or security invariant.
- Explain **Systems capstone** and connect it to a concrete trust boundary or security invariant.
- Explain **Application capstone** and connect it to a concrete trust boundary or security invariant.
- Explain **Cloud/supply-chain capstone** and connect it to a concrete trust boundary or security invariant.
- Explain **Detection/forensics capstone** and connect it to a concrete trust boundary or security invariant.
- Explain **Research capstone** and connect it to a concrete trust boundary or security invariant.

## Analysis method

Use the shared [Study Method](../Guides/STUDY-METHOD.md). For this module, first draw the relevant components and state transitions, then state one security invariant and identify the minimum evidence needed to test it safely.

## Deep concepts

### 1. Capstone standard

Each project should state scope, authorization, architecture, threat model, hypothesis, procedure, evidence, findings, remediation, regression, cleanup, and limitations.



### 2. Systems capstone

Analyze one disposable Linux/Windows/Android environment from boot/identity through process/file/network boundaries. Document attack surface and reduce unnecessary privilege/exposure.



### 3. Application capstone

Build or use an intentionally vulnerable local application, identify one root-cause authorization/parser/session flaw, fix it, and prove the fix with negative regression tests.



### 4. Cloud/supply-chain capstone

Model a small cloud deployment from source to CI to registry to workload identity. Add provenance, least privilege, logging, and a recovery plan for compromised build credentials.



### 5. Detection/forensics capstone

Generate a synthetic sequence of benign events representing a security hypothesis, detect it, intentionally remove one telemetry source, and explain the resulting evidence gap.



### 6. Research capstone

Take a public fixed bug or toy vulnerable program, reproduce safely, minimize the trigger, identify root cause, compare the patch, and build a regression test—without weaponization.



### 7. Writing quality

Use precise claims: observed, inferred, unverified, not tested. Include hashes, versions, timestamps, diagrams, and minimal reproducer artifacts. Explain why the evidence supports the conclusion.



### 8. Portfolio hygiene

Remove secrets, personal data, customer data, proprietary details, live targets, and unnecessary exploit code. Publish sanitized diagrams, tests, defensive findings, and lessons learned.



## Review focus

Apply the failure-mode taxonomy in [Study Method](../Guides/STUDY-METHOD.md), but keep the analysis specific to this lesson: identify the principal, resource, authority, mutable state, parser or policy boundary, and the telemetry that would distinguish a real control failure from misconfiguration or an observation gap.

## Authorized exercises

### Exercise 1 — Complete one capstone from systems/application/cloud/detection/research and have another person reproduce the result from your documentation

Complete one capstone from systems/application/cloud/detection/research and have another person reproduce the result from your documentation.


### Exercise 2 — Create a portfolio index that links each project to the skills and security invariants demonstrated

Create a portfolio index that links each project to the skills and security invariants demonstrated.


### Exercise 3 — Revisit an early guide lab and redo it using the advanced evidence standard; compare the quality of the old and new conclusions

Revisit an early guide lab and redo it using the advanced evidence standard; compare the quality of the old and new conclusions.

Use the lab-record format in [Study Method](../Guides/STUDY-METHOD.md) for each exercise and keep all inputs synthetic or confined to the authorized lab.

## Knowledge checks

1. Explain the most important trust boundary in **Master Capstones, Research Portfolio and Deep Security Practice** without naming a security tool.
2. Give one example where cryptographic or authentication success still does **not** imply authorization success.
3. Describe one stale-state or replay condition relevant to this module.
4. Identify one telemetry source that can support a strong conclusion and one blind spot it still leaves.
5. Explain how you would turn a discovered weakness into a regression test rather than a one-time finding.

## Guided study workflow

Use [Study Method](../Guides/STUDY-METHOD.md). Complete at least one authorized exercise, preserve the evidence that supports your conclusion, and explain the module's main trust boundary and failure modes in your own words before moving on.

### Continue with

Choose **Learning paths** from the main menu for an ordered specialization, or use **Search lessons** to follow a concept into related modules.

---

# Heap Allocators, Object Lifetimes and Memory Debugging

Go below generic buffer-overflow theory and study how allocators organize heap state, how object lifetime bugs appear, and how modern debugging tools expose corruption without weaponizing it.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, captures, or lab environments you own or are explicitly authorized to test. Prefer localhost, synthetic data, disposable VMs/containers, prerecorded traces, and read-only analysis whenever possible.

## Learning objectives

By the end of this module you should be able to:

- Explain **allocator metadata and arenas** and identify its most important trust boundary, state transition, and evidence source.
- Explain **size classes, bins and caches** and identify its most important trust boundary, state transition, and evidence source.
- Explain **allocation/free lifecycle** and identify its most important trust boundary, state transition, and evidence source.
- Explain **use-after-free and stale references** and identify its most important trust boundary, state transition, and evidence source.
- Explain **double-free and ownership confusion** and identify its most important trust boundary, state transition, and evidence source.
- Explain **heap fragmentation and determinism** and identify its most important trust boundary, state transition, and evidence source.

## Analysis method

Use [Study Method](../Guides/STUDY-METHOD.md). Start by identifying ownership or identity, the state transition that can fail, and the evidence that would distinguish a real boundary violation from a diagnostic artifact.

## Deep concepts

### 1. allocator metadata and arenas

Heap allocators maintain bookkeeping that maps requested allocations to backing memory. Treat metadata, arenas, and per-thread caches as privileged process state: corruption in bookkeeping can make a later allocation or free fail far from the original programming error.

### 2. size classes, bins and caches

Allocators group chunks by size and frequently cache recently freed memory to reduce contention. Those policies explain why the same lifetime bug can appear deterministic in one build and intermittent in another, so diagnostics should record allocator, architecture, thread behavior, and allocation sequence.

### 3. allocation/free lifecycle

Every heap object has an ownership lifecycle: allocation, initialization, publication, use, ownership transfer, retirement, and free. Security review should identify which references remain valid at each phase and which API is responsible for ending ownership.

### 4. use-after-free and stale references

A use-after-free occurs when code still treats a reference as valid after the object’s lifetime ended. In defensive research, reproduce the bug with a toy program and a memory sanitizer, then trace the stale reference back to the ownership decision that should have invalidated it.

### 5. double-free and ownership confusion

Double-free bugs usually reveal ambiguous ownership or cleanup paths rather than a problem with `free()` itself. Review error handling, reference counting, shared ownership, and exception paths so exactly one component is responsible for final destruction.

### 6. heap fragmentation and determinism

Fragmentation changes where future allocations are placed and can influence whether corruption is immediately visible. For diagnosis, compare repeatable allocation traces and avoid assuming that an address pattern observed in one run is a stable property of the program.

### 7. guard allocators and quarantine

Guard pages, delayed reuse, quarantine, and hardened allocators trade performance or memory for earlier detection of invalid access. They are valuable during testing because they convert silent corruption into a local, attributable failure.

### 8. ASan, GWP-ASan and heap diagnostics

AddressSanitizer and sampled production diagnostics such as GWP-ASan can identify out-of-bounds and lifetime violations with useful stack evidence. Treat sanitizer output as a starting point: confirm the first invalid access, the allocation/free stacks, build options, and whether the root cause survives after remediation.

## Engineering focus

For this module, convert each important claim into a security invariant and a regression test. Prefer controls that remove unnecessary authority, make state transitions explicit, bound resource use, and leave enough telemetry to explain a failure. The reusable evidence and lab-record format is in [Study Method](../Guides/STUDY-METHOD.md).

## Authorized lab sequence

### Lab 1 — Build a tiny local C/C++ program with intentionally incorrect lifetime handling and observe it under a sanitizer.



### Lab 2 — Draw an allocation timeline that marks ownership transfer, free, stale reference and crash evidence.



### Lab 3 — Compare the same safe toy bug with and without allocator diagnostics enabled.

For every lab, use only owned/synthetic inputs and record objective, scope, version, expected behavior, observed evidence, cleanup, remediation, and regression result as described in [Study Method](../Guides/STUDY-METHOD.md).

## Knowledge checks

Answer these without looking at the notes:

1. What is the primary trust boundary in this topic?
2. Which state or identity transition is easiest to misunderstand?
3. What observation would disprove your first hypothesis?
4. Which control removes authority rather than merely adding detection?
5. How would you reproduce the behavior safely after remediation?

## Guided study workflow

Complete at least one authorized lab and explain the mechanism, trust boundary, failure state, evidence, and defensive fix in your own words. Use **Bookmarks**, **Progress**, and **Learning paths** in the numbered menu instead of memorizing command-line flags.

## Next modules

Recommended related modules: **053, 065, 066, 068, 099, 109**. From the main menu, choose **Search lessons** to find related sections across the full guide.

---

# Concurrency, Race Conditions, TOCTOU and Atomicity

Security bugs are often temporal rather than purely spatial. This module develops a rigorous model for concurrency, races, check-use gaps, lock ordering, atomicity and reproducible lab analysis.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, captures, or lab environments you own or are explicitly authorized to test. Prefer localhost, synthetic data, disposable VMs/containers, prerecorded traces, and read-only analysis whenever possible.

## Learning objectives

By the end of this module you should be able to:

- Explain **threads, tasks and interleavings** and identify its most important trust boundary, state transition, and evidence source.
- Explain **shared mutable state** and identify its most important trust boundary, state transition, and evidence source.
- Explain **check-then-act races** and identify its most important trust boundary, state transition, and evidence source.
- Explain **TOCTOU across filesystem and IPC boundaries** and identify its most important trust boundary, state transition, and evidence source.
- Explain **atomic operations and memory ordering** and identify its most important trust boundary, state transition, and evidence source.
- Explain **locks, deadlocks and lock granularity** and identify its most important trust boundary, state transition, and evidence source.

## Analysis method

Use [Study Method](../Guides/STUDY-METHOD.md). Start by identifying ownership or identity, the state transition that can fail, and the evidence that would distinguish a real boundary violation from a diagnostic artifact.

## Deep concepts

### 1. threads, tasks and interleavings

Concurrent programs permit many valid execution orders even when source code looks sequential. Model shared state and the operations that can overlap; a security invariant must hold for every allowed interleaving, not only the one seen during a normal test run.

### 2. shared mutable state

Mutable state shared across threads, processes, or services needs an explicit synchronization and ownership model. Record which operations are atomic, which state is protected by a lock or transaction, and whether readers can observe partially updated values.

### 3. check-then-act races

A check-then-act race appears when a condition is validated and later used after another actor can change the underlying state. Safer designs combine validation and action under one authority boundary or use an operation that fails atomically if the state no longer matches.

### 4. TOCTOU across filesystems and IPC

Time-of-check/time-of-use problems are especially subtle when paths, handles, IPC messages, or external resources can change between validation and use. Prefer stable handles, descriptor-based operations, immutable identifiers, and server-side revalidation at the point of action.

### 5. atomic operations and memory ordering

Atomic operations prevent torn updates but do not automatically make a multi-step protocol correct. Memory-ordering rules determine which writes become visible to other threads; document the synchronization relation instead of relying on timing observed on one CPU.

### 6. locks, deadlocks and granularity

Locks serialize access but introduce ordering and liveness requirements. Define a lock hierarchy, keep critical sections narrow, and test failure/timeout paths so security-sensitive cleanup does not silently disappear when a lock cannot be acquired.

### 7. idempotency and distributed races

Distributed systems can receive duplicated, delayed, retried, or reordered requests. Idempotency keys, version checks, transactions, and compare-and-swap style updates help keep operations correct when two actors race across service boundaries.

### 8. deterministic stress and race detectors

Race detectors, schedulers, stress loops, and controlled fault injection make timing bugs easier to reproduce without exploiting real systems. Preserve the seed, build, workload, timing assumptions, and trace so a fix can be regression-tested.

## Engineering focus

For this module, convert each important claim into a security invariant and a regression test. Prefer controls that remove unnecessary authority, make state transitions explicit, bound resource use, and leave enough telemetry to explain a failure. The reusable evidence and lab-record format is in [Study Method](../Guides/STUDY-METHOD.md).

## Authorized lab sequence

### Lab 1 — Create a local counter/update race in a toy program and record inconsistent outcomes.



### Lab 2 — Model a safe file-check/file-open example using temporary files you own, then redesign it around safer handles or atomic primitives.



### Lab 3 — Write invariants for a payment-like state machine and test duplicate/reordered events without real transactions.

For every lab, use only owned/synthetic inputs and record objective, scope, version, expected behavior, observed evidence, cleanup, remediation, and regression result as described in [Study Method](../Guides/STUDY-METHOD.md).

## Knowledge checks

Answer these without looking at the notes:

1. What is the primary trust boundary in this topic?
2. Which state or identity transition is easiest to misunderstand?
3. What observation would disprove your first hypothesis?
4. Which control removes authority rather than merely adding detection?
5. How would you reproduce the behavior safely after remediation?

## Guided study workflow

Complete at least one authorized lab and explain the mechanism, trust boundary, failure state, evidence, and defensive fix in your own words. Use **Bookmarks**, **Progress**, and **Learning paths** in the numbered menu instead of memorizing command-line flags.

## Next modules

Recommended related modules: **041, 065, 071, 084, 091, 095**. From the main menu, choose **Search lessons** to find related sections across the full guide.

---

# IPC, RPC, D-Bus, COM and Local Trust Boundaries

Local communication is still a network of trust decisions. Learn how processes expose services, identify callers, marshal data and accidentally create privilege boundaries that are weaker than they look.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, captures, or lab environments you own or are explicitly authorized to test. Prefer localhost, synthetic data, disposable VMs/containers, prerecorded traces, and read-only analysis whenever possible.

## Learning objectives

By the end of this module you should be able to:

- Explain **IPC threat modeling** and identify its most important trust boundary, state transition, and evidence source.
- Explain **Unix sockets and peer credentials** and identify its most important trust boundary, state transition, and evidence source.
- Explain **D-Bus names, policies and activation** and identify its most important trust boundary, state transition, and evidence source.
- Explain **Windows COM/RPC identity and impersonation concepts** and identify its most important trust boundary, state transition, and evidence source.
- Explain **named pipes and local endpoints** and identify its most important trust boundary, state transition, and evidence source.
- Explain **message marshalling and schema validation** and identify its most important trust boundary, state transition, and evidence source.

## Analysis method

Use [Study Method](../Guides/STUDY-METHOD.md). Start by identifying ownership or identity, the state transition that can fail, and the evidence that would distinguish a real boundary violation from a diagnostic artifact.

## Deep concepts

### 1. IPC threat modeling

Inter-process communication crosses a privilege boundary whenever one process can ask another to perform work. Identify caller identity, server privilege, object/operation, message schema, and the exact point where authorization is enforced.

### 2. Unix sockets and peer credentials

Unix-domain sockets can expose filesystem permissions and kernel-provided peer identity such as UID/GID. Applications should use authenticated peer context from the transport where available rather than trusting a caller-supplied username inside the message.

### 3. D-Bus names, policies and activation

D-Bus combines bus names, method calls, policy, and service activation. Review which peers can own or call sensitive names, how activation changes privilege/state, and whether method-level authorization remains correct after policy or package changes.

### 4. Windows COM/RPC identity and impersonation concepts

Windows COM/RPC can carry caller security context into privileged services. Security depends on authentication level, endpoint permissions, impersonation behavior, and whether the server authorizes the original caller before performing a privileged operation.

### 5. named pipes and local endpoints

Named pipes and similar local endpoints are not automatically trusted because they are local. Restrict who can connect or create the endpoint, authenticate the peer, bound message sizes, and prevent untrusted clients from influencing privileged file or process operations.

### 6. marshalling and schema validation

IPC data is untrusted input even when it comes from another local process. Use explicit schemas, bounded lengths, versioning, canonical encodings, and reject unknown or contradictory fields at the component that owns the decision.

### 7. capability-style handles

A narrow, unforgeable handle can represent authority more safely than a global name plus a broad service account. Capability-oriented designs should minimize ambient privilege and ensure handles cannot be confused across users, tenants, or resource types.

### 8. brokered architectures and least privilege

A broker allows a sandboxed or low-privilege client to request a small set of privileged operations. The broker must treat every request as hostile, validate caller context and parameters, and expose the minimum operation surface needed by the client.

## Engineering focus

For this module, convert each important claim into a security invariant and a regression test. Prefer controls that remove unnecessary authority, make state transitions explicit, bound resource use, and leave enough telemetry to explain a failure. The reusable evidence and lab-record format is in [Study Method](../Guides/STUDY-METHOD.md).

## Authorized lab sequence

### Lab 1 — Inventory local IPC endpoints on a disposable Linux VM or Termux environment using read-only tools.



### Lab 2 — Design a toy privileged broker API and write an explicit authorization matrix for each operation.



### Lab 3 — Trace a local client/server exchange and identify where caller identity is established, transformed and checked.

For every lab, use only owned/synthetic inputs and record objective, scope, version, expected behavior, observed evidence, cleanup, remediation, and regression result as described in [Study Method](../Guides/STUDY-METHOD.md).

## Knowledge checks

Answer these without looking at the notes:

1. What is the primary trust boundary in this topic?
2. Which state or identity transition is easiest to misunderstand?
3. What observation would disprove your first hypothesis?
4. Which control removes authority rather than merely adding detection?
5. How would you reproduce the behavior safely after remediation?

## Guided study workflow

Complete at least one authorized lab and explain the mechanism, trust boundary, failure state, evidence, and defensive fix in your own words. Use **Bookmarks**, **Progress**, and **Learning paths** in the numbered menu instead of memorizing command-line flags.

## Next modules

Recommended related modules: **021, 041, 062, 073, 074, 119**. From the main menu, choose **Search lessons** to find related sections across the full guide.

---

# Sandboxing, Broker Architectures and Isolation Assurance

Sandboxes are systems of constrained authority, not magic boxes. This module explains policy surfaces, broker patterns, escape classes, verification strategy and how to reason about isolation guarantees.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, captures, or lab environments you own or are explicitly authorized to test. Prefer localhost, synthetic data, disposable VMs/containers, prerecorded traces, and read-only analysis whenever possible.

## Learning objectives

By the end of this module you should be able to:

- Explain **sandbox threat models** and identify its most important trust boundary, state transition, and evidence source.
- Explain **deny-by-default policy** and identify its most important trust boundary, state transition, and evidence source.
- Explain **syscall and filesystem mediation** and identify its most important trust boundary, state transition, and evidence source.
- Explain **brokers and privileged helpers** and identify its most important trust boundary, state transition, and evidence source.
- Explain **namespace and job-object style isolation** and identify its most important trust boundary, state transition, and evidence source.
- Explain **seccomp, MAC and platform policy concepts** and identify its most important trust boundary, state transition, and evidence source.

## Analysis method

Use [Study Method](../Guides/STUDY-METHOD.md). Start by identifying ownership or identity, the state transition that can fail, and the evidence that would distinguish a real boundary violation from a diagnostic artifact.

## Deep concepts

### 1. sandbox threat models

A sandbox reduces the impact of compromised or untrusted code by limiting reachable resources and operations. State what attacker capability the sandbox assumes and which assets remain outside its boundary; otherwise “sandboxed” becomes an undefined security claim.

### 2. deny-by-default policy

Sandbox policy is easier to reason about when access starts denied and narrowly grants required capabilities. Each exception should have an owner, reason, resource scope, and regression test so compatibility changes do not silently expand authority.

### 3. syscall and filesystem mediation

System calls and filesystem access are common sandbox boundaries because they connect code to kernel-managed resources. Mediation should use stable object identity where possible and account for path resolution, links, mounts, namespaces, and inherited descriptors.

### 4. brokers and privileged helpers

Privileged helpers are intentional escape hatches from a sandbox, so they deserve a smaller and more rigorously validated API than ordinary application code. Pass caller identity and resource context explicitly and reject requests the helper cannot authorize locally.

### 5. namespaces and job-object isolation

Namespaces, cgroups, job objects, tokens, and similar primitives isolate different resource dimensions rather than creating one universal boundary. Verify which resources are actually separated—processes, mounts, network, IPC, users, devices, or quotas—and which are still shared.

### 6. seccomp, MAC and platform policy

Seccomp and mandatory-access-control policy constrain behavior after ordinary discretionary permissions are applied. Policies should be generated from understood requirements, tested for fail-closed behavior, and monitored for denials that indicate drift or missing assumptions.

### 7. escape classes without weaponization

Sandbox escapes usually involve a reachable privileged interface, kernel/runtime bug, policy gap, parser bug, or confused deputy. Defensive analysis should classify the boundary failure and reproduce only on a toy/owned target instead of turning the finding into a reusable escape chain.

### 8. assurance, regression and telemetry

Isolation requires evidence over time: policy versions, broker decisions, denied operations, privileged transitions, and regression tests after runtime updates. A sandbox that cannot be observed or retested is difficult to trust during incident response.

## Engineering focus

For this module, convert each important claim into a security invariant and a regression test. Prefer controls that remove unnecessary authority, make state transitions explicit, bound resource use, and leave enough telemetry to explain a failure. The reusable evidence and lab-record format is in [Study Method](../Guides/STUDY-METHOD.md).

## Authorized lab sequence

### Lab 1 — Build a toy process with an allowlist of file operations and document what is intentionally denied.



### Lab 2 — Compare two container/sandbox configurations by capabilities, mounts, network access and process visibility.



### Lab 3 — Write regression tests that prove a sandboxed component cannot access three lab-only resources outside its policy.

For every lab, use only owned/synthetic inputs and record objective, scope, version, expected behavior, observed evidence, cleanup, remediation, and regression result as described in [Study Method](../Guides/STUDY-METHOD.md).

## Knowledge checks

Answer these without looking at the notes:

1. What is the primary trust boundary in this topic?
2. Which state or identity transition is easiest to misunderstand?
3. What observation would disprove your first hypothesis?
4. Which control removes authority rather than merely adding detection?
5. How would you reproduce the behavior safely after remediation?

## Guided study workflow

Complete at least one authorized lab and explain the mechanism, trust boundary, failure state, evidence, and defensive fix in your own words. Use **Bookmarks**, **Progress**, and **Learning paths** in the numbered menu instead of memorizing command-line flags.

## Next modules

Recommended related modules: **041, 074, 075, 094, 095, 112**. From the main menu, choose **Search lessons** to find related sections across the full guide.

---

# macOS Security Internals: TCC, SIP, Gatekeeper, Notarization and XProtect

Develop a platform-level view of macOS trust: code signing, system integrity, privacy permissions, execution policy, malware defenses, key storage and enterprise observability.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, captures, or lab environments you own or are explicitly authorized to test. Prefer localhost, synthetic data, disposable VMs/containers, prerecorded traces, and read-only analysis whenever possible.

## Learning objectives

By the end of this module you should be able to:

- Explain **code signing and designated requirements** and identify its most important trust boundary, state transition, and evidence source.
- Explain **Gatekeeper and notarization** and identify its most important trust boundary, state transition, and evidence source.
- Explain **System Integrity Protection (SIP)** and identify its most important trust boundary, state transition, and evidence source.
- Explain **Transparency, Consent and Control (TCC)** and identify its most important trust boundary, state transition, and evidence source.
- Explain **sandboxing and entitlements** and identify its most important trust boundary, state transition, and evidence source.
- Explain **Keychain and Secure Enclave concepts** and identify its most important trust boundary, state transition, and evidence source.

## Analysis method

Use [Study Method](../Guides/STUDY-METHOD.md). Start by identifying ownership or identity, the state transition that can fail, and the evidence that would distinguish a real boundary violation from a diagnostic artifact.

## Deep concepts

### 1. code signing and designated requirements

macOS code signing binds executable content to a signing identity and requirements evaluated by the platform. Review the designated requirement and entitlement set rather than assuming that “signed” means trusted for every purpose.

### 2. Gatekeeper and notarization

Gatekeeper evaluates downloaded software using provenance, signing, quarantine context, and notarization-related policy. Notarization is an ecosystem trust signal, not proof that an application is vulnerability-free, so application authorization and runtime controls still matter.

### 3. System Integrity Protection

System Integrity Protection restricts modification of protected operating-system locations and some powerful runtime behaviors even for root. Security analysis should distinguish SIP-protected assets from ordinary root-controlled state and avoid treating administrator access as unlimited platform authority.

### 4. TCC privacy controls

Transparency, Consent, and Control governs access to privacy-sensitive resources such as camera, microphone, contacts, and protected data. TCC decisions depend on application identity, entitlement/context, user/admin policy, and can change across OS versions.

### 5. App Sandbox and entitlements

The App Sandbox combines a restricted process environment with entitlements that request additional capabilities. Review entitlements as authority declarations: broad file, network, automation, or device access increases the impact of an application compromise.

### 6. Keychain and Secure Enclave

Keychain items can be scoped by access-control policy, while Secure Enclave-backed keys can limit where private operations occur. Review accessibility class, authentication requirements, sharing groups, backup/sync behavior, and what happens when a device or account is recovered.

### 7. XProtect and platform remediation

Apple platform protections include malware detection and remediation components that evolve independently from application updates. Treat them as defense-in-depth and preserve OS/security-update evidence during triage rather than assuming their presence guarantees a clean host.

### 8. EndpointSecurity and unified logs

EndpointSecurity exposes structured security-relevant events to approved software, while unified logging provides broader diagnostic context. Good investigations correlate process identity, signing information, parentage, file/network activity, and time without relying on one sensor alone.

## Engineering focus

For this module, convert each important claim into a security invariant and a regression test. Prefer controls that remove unnecessary authority, make state transitions explicit, bound resource use, and leave enough telemetry to explain a failure. The reusable evidence and lab-record format is in [Study Method](../Guides/STUDY-METHOD.md).

## Authorized lab sequence

### Lab 1 — On a Mac you own, map permissions requested by a benign application and compare them with its functional needs.



### Lab 2 — Review Apple Platform Security documentation and build a trust-chain diagram from boot to application launch.



### Lab 3 — Create a defensive checklist for evaluating a signed/notarized application without bypassing platform protections.

For every lab, use only owned/synthetic inputs and record objective, scope, version, expected behavior, observed evidence, cleanup, remediation, and regression result as described in [Study Method](../Guides/STUDY-METHOD.md).

## Knowledge checks

Answer these without looking at the notes:

1. What is the primary trust boundary in this topic?
2. Which state or identity transition is easiest to misunderstand?
3. What observation would disprove your first hypothesis?
4. Which control removes authority rather than merely adding detection?
5. How would you reproduce the behavior safely after remediation?

## Guided study workflow

Complete at least one authorized lab and explain the mechanism, trust boundary, failure state, evidence, and defensive fix in your own words. Use **Bookmarks**, **Progress**, and **Learning paths** in the numbered menu instead of memorizing command-line flags.

## Next modules

Recommended related modules: **021, 044, 049, 054, 103, 119**. From the main menu, choose **Search lessons** to find related sections across the full guide.

---

# iOS Security Internals: Entitlements, Code Signing, Keychain and Data Protection

Go deeper than generic mobile testing by studying iOS trust chains, app identities, entitlements, sandbox containers, keychain access groups, Data Protection classes and secure hardware boundaries.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, captures, or lab environments you own or are explicitly authorized to test. Prefer localhost, synthetic data, disposable VMs/containers, prerecorded traces, and read-only analysis whenever possible.

## Learning objectives

By the end of this module you should be able to:

- Explain **secure boot chain and code signing** and identify its most important trust boundary, state transition, and evidence source.
- Explain **application sandbox containers** and identify its most important trust boundary, state transition, and evidence source.
- Explain **entitlements and capabilities** and identify its most important trust boundary, state transition, and evidence source.
- Explain **Keychain access groups** and identify its most important trust boundary, state transition, and evidence source.
- Explain **Data Protection classes** and identify its most important trust boundary, state transition, and evidence source.
- Explain **Secure Enclave and key handling** and identify its most important trust boundary, state transition, and evidence source.

## Analysis method

Use [Study Method](../Guides/STUDY-METHOD.md). Start by identifying ownership or identity, the state transition that can fail, and the evidence that would distinguish a real boundary violation from a diagnostic artifact.

## Deep concepts

### 1. secure boot and code signing

iOS uses a hardware-rooted boot chain and mandatory code-signing model to establish platform integrity. Security review should distinguish platform trust, application signing, provisioning, and runtime authorization rather than treating them as one control.

### 2. sandbox containers

Applications receive isolated containers and restricted system interfaces. Data leakage often comes from deliberately shared surfaces—extensions, pasteboard, app groups, URL handling, cloud sync, or exported documents—so review those boundaries explicitly.

### 3. entitlements and capabilities

Entitlements declare privileged platform capabilities such as application groups, keychain sharing, associated domains, or special services. Compare the signed entitlement set with actual product requirements and remove capabilities that are no longer needed.

### 4. Keychain access groups

Keychain access groups control which signed applications can share stored credentials. Review group membership, accessibility class, synchronization, and recovery behavior so a helper/extension does not inherit more secret access than intended.

### 5. Data Protection classes

iOS Data Protection ties file encryption behavior to device lock state and key availability. Select protection classes according to when the application genuinely needs data, and test backup/export paths because copies can have different protection semantics.

### 6. Secure Enclave and key handling

Secure Enclave-backed keys can keep private key material outside the normal application processor while still allowing authorized operations. Define user-presence/biometric requirements, fallback behavior, device migration, and what happens when credentials must be recovered.

### 7. privacy permissions

Camera, microphone, photos, location, contacts, Bluetooth, and tracking-related access require platform and application-level justification. Request permission only when needed, handle denial safely, and avoid collecting a broader data set than the feature requires.

### 8. managed-device and enterprise trust

MDM can install configuration, certificates, network settings, managed apps, and restrictions according to organization policy. Enterprise security should separate device management authority from application identity and audit high-impact profile or certificate changes.

## Engineering focus

For this module, convert each important claim into a security invariant and a regression test. Prefer controls that remove unnecessary authority, make state transitions explicit, bound resource use, and leave enough telemetry to explain a failure. The reusable evidence and lab-record format is in [Study Method](../Guides/STUDY-METHOD.md).

## Authorized lab sequence

### Lab 1 — Design an iOS app threat model using only public architecture documentation and a fictional app.



### Lab 2 — Compare storage choices for a sample token: plain file, protected file and Keychain, documenting security properties rather than extracting secrets.



### Lab 3 — Map a fictional app’s entitlements to least-privilege requirements and flag unnecessary capabilities.

For every lab, use only owned/synthetic inputs and record objective, scope, version, expected behavior, observed evidence, cleanup, remediation, and regression result as described in [Study Method](../Guides/STUDY-METHOD.md).

## Knowledge checks

Answer these without looking at the notes:

1. What is the primary trust boundary in this topic?
2. Which state or identity transition is easiest to misunderstand?
3. What observation would disprove your first hypothesis?
4. Which control removes authority rather than merely adding detection?
5. How would you reproduce the behavior safely after remediation?

## Guided study workflow

Complete at least one authorized lab and explain the mechanism, trust boundary, failure state, evidence, and defensive fix in your own words. Use **Bookmarks**, **Progress**, and **Learning paths** in the numbered menu instead of memorizing command-line flags.

## Next modules

Recommended related modules: **017, 039, 054, 056, 082, 103**. From the main menu, choose **Search lessons** to find related sections across the full guide.

---

# Cellular Networks, LTE/5G Architecture and Mobile Network Security

Understand cellular security as a layered identity, radio, transport and core-network problem. The focus is architecture, privacy, trust and defensive analysis—not interception of third-party traffic.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, captures, or lab environments you own or are explicitly authorized to test. Prefer localhost, synthetic data, disposable VMs/containers, prerecorded traces, and read-only analysis whenever possible.

## Learning objectives

By the end of this module you should be able to:

- Explain **UE, SIM/eSIM and subscriber identity** and identify its most important trust boundary, state transition, and evidence source.
- Explain **RAN, core network and control/user planes** and identify its most important trust boundary, state transition, and evidence source.
- Explain **LTE EPC and 5G Core concepts** and identify its most important trust boundary, state transition, and evidence source.
- Explain **AKA authentication families** and identify its most important trust boundary, state transition, and evidence source.
- Explain **temporary identifiers and privacy** and identify its most important trust boundary, state transition, and evidence source.
- Explain **roaming and inter-operator trust** and identify its most important trust boundary, state transition, and evidence source.

## Analysis method

Use [Study Method](../Guides/STUDY-METHOD.md). Start by identifying ownership or identity, the state transition that can fail, and the evidence that would distinguish a real boundary violation from a diagnostic artifact.

## Deep concepts

### 1. UE, SIM/eSIM and subscriber identity

Cellular security begins with the user equipment and subscription credentials held by SIM/eSIM infrastructure. Separate device identity, subscription identity, phone number, and application identity; they have different owners and are not interchangeable authentication factors.

### 2. RAN, core, control and user planes

The radio access network connects devices to a core network that separates signaling/control functions from user data forwarding. Threat modeling should identify which interfaces carry subscriber state, routing decisions, authentication context, and application traffic.

### 3. LTE EPC and 5G Core

LTE EPC and 5G Core use different service architecture and function boundaries, but both depend on authenticated subscriber state and tightly controlled inter-function communication. Inventory exposed service interfaces and administrative APIs rather than reasoning only about radio encryption.

### 4. AKA families

Authentication and Key Agreement protocols derive session keys from subscription secrets without transmitting the long-term secret directly. Security review should focus on identity binding, freshness, network authentication, key separation, and correct failure handling.

### 5. temporary identifiers and privacy

Temporary identifiers reduce repeated exposure of long-lived subscriber identity over radio interfaces. Privacy analysis should still consider paging, timing, mobility metadata, application identifiers, and operational logs that can correlate a device over time.

### 6. roaming and inter-operator trust

Roaming extends trust across providers and signaling/interconnect boundaries. Apply explicit peer policy, message validation, least privilege, monitoring, and contractual/security controls because compromise of a partner path can affect subscribers outside one administrative domain.

### 7. network slicing and service exposure

5G slicing and service-based interfaces create logical segmentation and APIs that require strong identity and authorization. A slice label alone is not a security boundary; verify isolation in policy, routing, resource allocation, and telemetry.

### 8. baseband isolation and telemetry

Baseband processors handle complex untrusted radio protocols and are intentionally isolated from application processors. Device security benefits from hardware/OS boundaries, firmware updates, crash telemetry, and minimizing the authority that radio components have over higher-level data.

## Engineering focus

For this module, convert each important claim into a security invariant and a regression test. Prefer controls that remove unnecessary authority, make state transitions explicit, bound resource use, and leave enough telemetry to explain a failure. The reusable evidence and lab-record format is in [Study Method](../Guides/STUDY-METHOD.md).

## Authorized lab sequence

### Lab 1 — Draw a 5G connection-flow diagram from device to application service using public standards diagrams.



### Lab 2 — Threat-model a fictional roaming scenario and list which parties must trust which assertions.



### Lab 3 — Compare Wi-Fi and cellular identity/privacy assumptions without capturing any third-party radio traffic.

For every lab, use only owned/synthetic inputs and record objective, scope, version, expected behavior, observed evidence, cleanup, remediation, and regression result as described in [Study Method](../Guides/STUDY-METHOD.md).

## Knowledge checks

Answer these without looking at the notes:

1. What is the primary trust boundary in this topic?
2. Which state or identity transition is easiest to misunderstand?
3. What observation would disprove your first hypothesis?
4. Which control removes authority rather than merely adding detection?
5. How would you reproduce the behavior safely after remediation?

## Guided study workflow

Complete at least one authorized lab and explain the mechanism, trust boundary, failure state, evidence, and defensive fix in your own words. Use **Bookmarks**, **Progress**, and **Learning paths** in the numbered menu instead of memorizing command-line flags.

## Next modules

Recommended related modules: **016, 017, 051, 055, 056, 123**. From the main menu, choose **Search lessons** to find related sections across the full guide.

---

# Radio, SDR and RF Security Fundamentals

Build the signal-processing literacy needed to reason about wireless systems safely: spectrum, modulation, framing, synchronization, RF fingerprints, replay risk and legal/ethical lab boundaries.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, captures, or lab environments you own or are explicitly authorized to test. Prefer localhost, synthetic data, disposable VMs/containers, prerecorded traces, and read-only analysis whenever possible.

## Learning objectives

By the end of this module you should be able to:

- Explain **frequency, bandwidth and sampling** and identify its most important trust boundary, state transition, and evidence source.
- Explain **I/Q representation** and identify its most important trust boundary, state transition, and evidence source.
- Explain **modulation and symbol timing** and identify its most important trust boundary, state transition, and evidence source.
- Explain **preambles, frames and checksums** and identify its most important trust boundary, state transition, and evidence source.
- Explain **noise, interference and SNR** and identify its most important trust boundary, state transition, and evidence source.
- Explain **receive-only spectrum analysis** and identify its most important trust boundary, state transition, and evidence source.

## Analysis method

Use [Study Method](../Guides/STUDY-METHOD.md). Start by identifying ownership or identity, the state transition that can fail, and the evidence that would distinguish a real boundary violation from a diagnostic artifact.

## Deep concepts

### 1. frequency, bandwidth and sampling

RF analysis starts with frequency range, occupied bandwidth, sample rate, and receiver limitations. A sampled signal is only a representation of energy within the configured front end, so document gain, filters, antenna, clock, and environment before drawing protocol conclusions.

### 2. I/Q representation

Software-defined radios commonly represent a signal as in-phase and quadrature samples. I/Q preserves amplitude and phase information needed for digital demodulation, but raw samples do not identify a protocol or sender without additional framing and context.

### 3. modulation and symbol timing

Modulation maps information onto changes in amplitude, phase, frequency, or combinations of them. Correct decoding also depends on symbol timing, carrier synchronization, channel conditions, and protocol parameters, which should be measured rather than guessed.

### 4. preambles, frames and checksums

Wireless protocols use synchronization/preamble patterns, headers, payloads, checksums or stronger integrity mechanisms to frame data. A checksum detects accidental corruption but is not an authentication mechanism unless a cryptographic construction explicitly provides authenticity.

### 5. noise, interference and SNR

Noise and interference can look like protocol failure or security events. Measure signal-to-noise ratio, channel occupancy, receiver saturation, and environmental changes before attributing missing or malformed frames to an attacker.

### 6. receive-only spectrum analysis

Receive-only analysis is the safest default for learning RF behavior. Use owned devices or licensed/public test signals, record only what is necessary, and avoid decoding private communications that you are not authorized to inspect.

### 7. authentication versus signal presence

Detecting a waveform or valid-looking frame proves only that energy or syntax was observed. Security decisions require cryptographic or trusted identity context; physical proximity and RF strength are not reliable authentication by themselves.

### 8. replay resistance and rolling state

Protocols that authorize physical actions need freshness such as nonces, counters, challenge-response, or carefully managed rolling state. Test replay resistance with synthetic/owned devices and focus on state synchronization and recovery rather than reproducing unauthorized control actions.

## Engineering focus

For this module, convert each important claim into a security invariant and a regression test. Prefer controls that remove unnecessary authority, make state transitions explicit, bound resource use, and leave enough telemetry to explain a failure. The reusable evidence and lab-record format is in [Study Method](../Guides/STUDY-METHOD.md).

## Authorized lab sequence

### Lab 1 — Use a prerecorded or synthetic IQ dataset and identify signal bandwidth, bursts and framing without transmitting.



### Lab 2 — Create a toy digital-radio frame format and add sequence numbers plus a MAC in software to demonstrate freshness/integrity.



### Lab 3 — Document how a rolling-code design differs from a static replayable identifier.

For every lab, use only owned/synthetic inputs and record objective, scope, version, expected behavior, observed evidence, cleanup, remediation, and regression result as described in [Study Method](../Guides/STUDY-METHOD.md).

## Knowledge checks

Answer these without looking at the notes:

1. What is the primary trust boundary in this topic?
2. Which state or identity transition is easiest to misunderstand?
3. What observation would disprove your first hypothesis?
4. Which control removes authority rather than merely adding detection?
5. How would you reproduce the behavior safely after remediation?

## Guided study workflow

Complete at least one authorized lab and explain the mechanism, trust boundary, failure state, evidence, and defensive fix in your own words. Use **Bookmarks**, **Progress**, and **Learning paths** in the numbered menu instead of memorizing command-line flags.

## Next modules

Recommended related modules: **016, 051, 055, 077, 083, 122**. From the main menu, choose **Search lessons** to find related sections across the full guide.

---

# HTTP/2, HTTP/3, QUIC and Modern Web Transport Security

Study modern HTTP below the application layer: multiplexing, stream state, HPACK/QPACK, QUIC connection IDs, 0-RTT, migration, observability and proxy translation boundaries.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, captures, or lab environments you own or are explicitly authorized to test. Prefer localhost, synthetic data, disposable VMs/containers, prerecorded traces, and read-only analysis whenever possible.

## Learning objectives

By the end of this module you should be able to:

- Explain **HTTP/2 streams and framing** and identify its most important trust boundary, state transition, and evidence source.
- Explain **HPACK/QPACK compression state** and identify its most important trust boundary, state transition, and evidence source.
- Explain **HTTP/3 over QUIC** and identify its most important trust boundary, state transition, and evidence source.
- Explain **QUIC connection IDs and migration** and identify its most important trust boundary, state transition, and evidence source.
- Explain **TLS 1.3 integration** and identify its most important trust boundary, state transition, and evidence source.
- Explain **0-RTT replay considerations** and identify its most important trust boundary, state transition, and evidence source.

## Analysis method

Use [Study Method](../Guides/STUDY-METHOD.md). Start by identifying ownership or identity, the state transition that can fail, and the evidence that would distinguish a real boundary violation from a diagnostic artifact.

## Deep concepts

### 1. HTTP/2 streams and framing

HTTP/2 multiplexes logical streams over one connection using binary frames. Security tooling and reverse proxies must preserve stream boundaries, header semantics, request limits, and error handling so one layer does not validate a different message than the next.

### 2. HPACK and QPACK

HPACK and QPACK compress header fields using dynamic state. Implementations must bound memory/work, isolate compression context appropriately, and handle malformed or blocked state without allowing resource exhaustion or inconsistent header interpretation.

### 3. HTTP/3 over QUIC

HTTP/3 maps HTTP semantics onto QUIC streams over UDP. Application authorization should remain protocol-independent, while network monitoring, rate controls, and troubleshooting must account for encrypted transport metadata and different connection behavior.

### 4. connection IDs and migration

QUIC connection IDs allow a connection to survive path or address changes. Do not use source IP alone as session identity; rate limiting and risk decisions should combine transport state with authenticated application identity and migration-aware telemetry.

### 5. TLS 1.3 integration

QUIC incorporates TLS 1.3 for authentication and key establishment. Correct certificate/identity validation and application authorization are still separate decisions, and transport encryption does not make untrusted HTTP input safe.

### 6. 0-RTT replay considerations

Early data can reduce latency but may be replayed under the protocol threat model. Only idempotent or explicitly replay-safe operations should be eligible; sensitive state changes need application controls that remain correct if the same early request is observed more than once.

### 7. proxy translation boundaries

A request can cross HTTP/3, HTTP/2, and HTTP/1.1 between client, CDN, proxy, and origin. Normalize and validate at each trust boundary and regression-test ambiguous headers, lengths, and routing fields so protocol translation does not create parser differentials.

### 8. visibility with encrypted transport

QUIC encrypts more transport metadata than traditional TCP/TLS deployments expose to middleboxes. Shift detection toward endpoint, proxy, application, DNS, identity, and flow telemetry instead of assuming full packet visibility is available.

## Engineering focus

For this module, convert each important claim into a security invariant and a regression test. Prefer controls that remove unnecessary authority, make state transitions explicit, bound resource use, and leave enough telemetry to explain a failure. The reusable evidence and lab-record format is in [Study Method](../Guides/STUDY-METHOD.md).

## Authorized lab sequence

### Lab 1 — Run a local HTTP service and compare request/response metadata over HTTP/1.1 versus an HTTP/2/3-capable lab stack.



### Lab 2 — Draw stream state for concurrent requests and explain why one transport connection no longer maps neatly to one request at a time.



### Lab 3 — Create a safe replay-sensitivity checklist for operations such as GET-like reads versus state-changing actions.

For every lab, use only owned/synthetic inputs and record objective, scope, version, expected behavior, observed evidence, cleanup, remediation, and regression result as described in [Study Method](../Guides/STUDY-METHOD.md).

## Knowledge checks

Answer these without looking at the notes:

1. What is the primary trust boundary in this topic?
2. Which state or identity transition is easiest to misunderstand?
3. What observation would disprove your first hypothesis?
4. Which control removes authority rather than merely adding detection?
5. How would you reproduce the behavior safely after remediation?

## Guided study workflow

Complete at least one authorized lab and explain the mechanism, trust boundary, failure state, evidence, and defensive fix in your own words. Use **Bookmarks**, **Progress**, and **Learning paths** in the numbered menu instead of memorizing command-line flags.

## Next modules

Recommended related modules: **011, 013, 014, 052, 069, 070, 089**. From the main menu, choose **Search lessons** to find related sections across the full guide.

---

# DNSSEC, DoH, DoQ, Resolver Privacy and DNS Trust

Extend DNS knowledge into validation and privacy: DNSSEC trust chains, encrypted resolver transports, resolver discovery, split-horizon behavior, caching and operational failure modes.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, captures, or lab environments you own or are explicitly authorized to test. Prefer localhost, synthetic data, disposable VMs/containers, prerecorded traces, and read-only analysis whenever possible.

## Learning objectives

By the end of this module you should be able to:

- Explain **DNSSEC chain of trust** and identify its most important trust boundary, state transition, and evidence source.
- Explain **DS, DNSKEY and RRSIG roles** and identify its most important trust boundary, state transition, and evidence source.
- Explain **negative answers and authenticated denial** and identify its most important trust boundary, state transition, and evidence source.
- Explain **DoH and DoT** and identify its most important trust boundary, state transition, and evidence source.
- Explain **DNS over QUIC (DoQ)** and identify its most important trust boundary, state transition, and evidence source.
- Explain **resolver policy and discovery** and identify its most important trust boundary, state transition, and evidence source.

## Analysis method

Use [Study Method](../Guides/STUDY-METHOD.md). Start by identifying ownership or identity, the state transition that can fail, and the evidence that would distinguish a real boundary violation from a diagnostic artifact.

## Deep concepts

### 1. DNSSEC chain of trust

DNSSEC authenticates DNS data through signatures and a chain of trust from configured trust anchors through DS and DNSKEY relationships. It provides origin authentication/integrity for DNS records, not confidentiality and not proof that the destination application itself is trustworthy.

### 2. DS, DNSKEY and RRSIG

DNSKEY records publish zone signing keys, DS records link parent and child zones, and RRSIG records carry signatures over RRsets. Operational security depends on correct key rollover, timing, algorithm support, and avoiding broken delegation state during changes.

### 3. authenticated denial of existence

DNSSEC can prove that a requested name or type does not exist using authenticated denial mechanisms. Negative answers are security-relevant state and must be validated/cached with the same care as positive answers.

### 4. DoH and DoT

DNS over HTTPS and DNS over TLS protect resolver traffic in transit to a chosen resolver. Encryption changes visibility and policy enforcement but does not by itself guarantee that the resolver is trustworthy or that returned data is DNSSEC-valid.

### 5. DoQ

DNS over QUIC carries DNS messages over QUIC and inherits encrypted transport, connection, and operational properties from QUIC. Resolver policy, authentication, resource limits, and fallback behavior should be explicit across all supported transports.

### 6. resolver policy and discovery

Endpoints can learn resolvers through network configuration, operating-system policy, applications, enterprise management, or encrypted-DNS discovery. Security teams should know which component wins when policies conflict and which paths bypass enterprise logging/filtering.

### 7. split-horizon DNS

Internal and external resolvers may intentionally return different data. Document the expected namespace and trust boundary so caching, VPN changes, encrypted resolvers, or application-specific DNS do not expose internal names or route users to the wrong service.

### 8. cache TTL and stale answers

Resolvers cache positive and negative answers according to TTL and local policy; some systems can serve stale data during outages. Incident response must account for propagation delay and cache state when rotating addresses, certificates, or maliciously altered records.

## Engineering focus

For this module, convert each important claim into a security invariant and a regression test. Prefer controls that remove unnecessary authority, make state transitions explicit, bound resource use, and leave enough telemetry to explain a failure. The reusable evidence and lab-record format is in [Study Method](../Guides/STUDY-METHOD.md).

## Authorized lab sequence

### Lab 1 — Use public DNSSEC test domains or offline packet examples to follow a validation chain without altering DNS infrastructure.



### Lab 2 — Compare plain DNS, DoH and DoQ at the architecture level: who can observe queries and where trust terminates.



### Lab 3 — Build a cache-timeline exercise showing TTL, stale data and key rollover dependencies.

For every lab, use only owned/synthetic inputs and record objective, scope, version, expected behavior, observed evidence, cleanup, remediation, and regression result as described in [Study Method](../Guides/STUDY-METHOD.md).

## Knowledge checks

Answer these without looking at the notes:

1. What is the primary trust boundary in this topic?
2. Which state or identity transition is easiest to misunderstand?
3. What observation would disprove your first hypothesis?
4. Which control removes authority rather than merely adding detection?
5. How would you reproduce the behavior safely after remediation?

## Guided study workflow

Complete at least one authorized lab and explain the mechanism, trust boundary, failure state, evidence, and defensive fix in your own words. Use **Bookmarks**, **Progress**, and **Learning paths** in the numbered menu instead of memorizing command-line flags.

## Next modules

Recommended related modules: **035, 051, 077, 078, 087, 124**. From the main menu, choose **Search lessons** to find related sections across the full guide.

---

# CDN, Reverse Proxy, Cache and Edge Security

Modern web applications often have several HTTP-speaking systems before the origin. Learn edge trust, cache keys, normalization, origin protection, signed requests and observability.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, captures, or lab environments you own or are explicitly authorized to test. Prefer localhost, synthetic data, disposable VMs/containers, prerecorded traces, and read-only analysis whenever possible.

## Learning objectives

By the end of this module you should be able to:

- Explain **CDN and reverse-proxy trust boundaries** and identify its most important trust boundary, state transition, and evidence source.
- Explain **cache keys and variation** and identify its most important trust boundary, state transition, and evidence source.
- Explain **header normalization and forwarding** and identify its most important trust boundary, state transition, and evidence source.
- Explain **origin authentication and shielding** and identify its most important trust boundary, state transition, and evidence source.
- Explain **signed URLs/cookies concepts** and identify its most important trust boundary, state transition, and evidence source.
- Explain **cache poisoning classes** and identify its most important trust boundary, state transition, and evidence source.

## Analysis method

Use [Study Method](../Guides/STUDY-METHOD.md). Start by identifying ownership or identity, the state transition that can fail, and the evidence that would distinguish a real boundary violation from a diagnostic artifact.

## Deep concepts

### 1. CDN and reverse-proxy trust boundaries

A CDN or reverse proxy terminates connections and may rewrite routing, identity, cache, and security headers before forwarding to an origin. The origin should authenticate trusted proxy paths and reject client-controlled values that are supposed to be set only by the edge.

### 2. cache keys and Vary

A cache key determines which requests share a stored response. Security review must include host, path, query, headers, cookies, encoding, authorization state, and `Vary` behavior so private or attacker-influenced content is not reused for another context.

### 3. header normalization and forwarding

Edges and origins can disagree about duplicate headers, whitespace, casing, hop-by-hop fields, or forwarding metadata. Define a canonical policy and test it end to end; access-control decisions should not depend on a header that an untrusted client can preserve or inject.

### 4. origin authentication and shielding

Private origins should accept traffic only from intended edge/shield paths and authenticate that relationship where practical. IP allowlists alone can become brittle; combine network restrictions with TLS identity, signed requests, or equivalent service authentication when supported.

### 5. signed URLs and cookies

Signed URLs/cookies delegate time- and resource-bounded access to edge content. Bind signatures to the intended path/resource, expiration, audience/context, and key version; avoid broad wildcards that turn a narrow share link into general origin authority.

### 6. cache poisoning classes

Cache poisoning is a state-integrity problem: an attacker-influenced response becomes associated with a key used by other clients. Defensive testing should use synthetic content and verify key construction, unkeyed inputs, error caching, and purge behavior without affecting public users.

### 7. edge compute and request mutation

Edge functions can authenticate, redirect, transform headers, or fetch additional data, making them part of the application security boundary. Apply code review, least privilege, secret isolation, versioned deployment, and observability comparable to backend services.

### 8. purge and incident response

A corrected origin does not remove already cached unsafe content. Incident plans need authenticated purge/invalidation, scope controls, propagation evidence, rollback, and verification from multiple edge locations without exposing customer data.

## Engineering focus

For this module, convert each important claim into a security invariant and a regression test. Prefer controls that remove unnecessary authority, make state transitions explicit, bound resource use, and leave enough telemetry to explain a failure. The reusable evidence and lab-record format is in [Study Method](../Guides/STUDY-METHOD.md).

## Authorized lab sequence

### Lab 1 — Design a local reverse-proxy lab with two cache variants and verify that private data never enters a shared cache.



### Lab 2 — Write an origin-access policy that distinguishes traffic from the trusted edge from direct internet requests.



### Lab 3 — Create a header-trust matrix showing which layer owns client IP, scheme, host and authenticated identity.

For every lab, use only owned/synthetic inputs and record objective, scope, version, expected behavior, observed evidence, cleanup, remediation, and regression result as described in [Study Method](../Guides/STUDY-METHOD.md).

## Knowledge checks

Answer these without looking at the notes:

1. What is the primary trust boundary in this topic?
2. Which state or identity transition is easiest to misunderstand?
3. What observation would disprove your first hypothesis?
4. Which control removes authority rather than merely adding detection?
5. How would you reproduce the behavior safely after remediation?

## Guided study workflow

Complete at least one authorized lab and explain the mechanism, trust boundary, failure state, evidence, and defensive fix in your own words. Use **Bookmarks**, **Progress**, and **Learning paths** in the numbered menu instead of memorizing command-line flags.

## Next modules

Recommended related modules: **013, 014, 041, 052, 069, 104, 124**. From the main menu, choose **Search lessons** to find related sections across the full guide.

---

# Serialization, Deserialization and Parser Security

Learn why data reconstruction is a high-value security boundary. Compare schema-driven formats, object serialization, polymorphic types, parser differentials and safe validation patterns.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, captures, or lab environments you own or are explicitly authorized to test. Prefer localhost, synthetic data, disposable VMs/containers, prerecorded traces, and read-only analysis whenever possible.

## Learning objectives

By the end of this module you should be able to:

- Explain **serialization versus object graphs** and identify its most important trust boundary, state transition, and evidence source.
- Explain **schema validation and canonical forms** and identify its most important trust boundary, state transition, and evidence source.
- Explain **JSON, XML, YAML and binary formats** and identify its most important trust boundary, state transition, and evidence source.
- Explain **polymorphic type handling** and identify its most important trust boundary, state transition, and evidence source.
- Explain **unsafe object reconstruction** and identify its most important trust boundary, state transition, and evidence source.
- Explain **parser differentials and duplicate fields** and identify its most important trust boundary, state transition, and evidence source.

## Analysis method

Use [Study Method](../Guides/STUDY-METHOD.md). Start by identifying ownership or identity, the state transition that can fail, and the evidence that would distinguish a real boundary violation from a diagnostic artifact.

## Deep concepts

### 1. serialization and object graphs

Serialization converts structured in-memory state into a transport/storage representation; deserialization reconstructs data from untrusted bytes. Keep the wire schema simpler than internal object graphs so external input cannot select arbitrary application types or constructors.

### 2. schemas and canonical forms

Explicit schemas define field types, ranges, required values, and compatibility rules. Canonical representation matters when data is signed, hashed, cached, or compared: two encodings with the same apparent meaning should not produce contradictory security decisions.

### 3. JSON, XML, YAML and binary formats

Each format has different parser behavior, type systems, references, extensions, and resource risks. Disable unnecessary features, bound nesting/size, select maintained parsers, and test duplicate or ambiguous fields at service boundaries.

### 4. polymorphic types

Automatic polymorphic deserialization can let input choose which class/type is instantiated. Prefer explicit discriminators mapped to a narrow allowlist of data-only types, followed by separate application logic that performs authorized actions.

### 5. unsafe reconstruction

Deserialization should not invoke arbitrary constructors, setters, hooks, or object-resolution behaviors with attacker-controlled state. Treat reconstruction as parsing: produce inert data, validate it, then perform side effects only through normal authorized code paths.

### 6. parser differentials and duplicate fields

Proxies, validators, signature layers, and application parsers can handle duplicate keys, numeric forms, encodings, or unknown fields differently. Regression-test the same serialized bytes through every layer that makes a security decision.

### 7. resource exhaustion

Deep nesting, huge collections, decompression, entity expansion, or pathological inputs can consume CPU/memory before business validation runs. Apply input-size, depth, object-count, recursion, and processing-time limits at the earliest trusted boundary.

### 8. safe deserialization patterns

Use explicit schemas, data-only representations, allowlisted types, bounded resources, authenticated transport/storage where required, and version-aware migrations. Preserve parser/version evidence so a future library change can be regression-tested against security-critical samples.

## Engineering focus

For this module, convert each important claim into a security invariant and a regression test. Prefer controls that remove unnecessary authority, make state transitions explicit, bound resource use, and leave enough telemetry to explain a failure. The reusable evidence and lab-record format is in [Study Method](../Guides/STUDY-METHOD.md).

## Authorized lab sequence

### Lab 1 — Create a toy JSON schema and test missing, duplicated, oversized and wrong-type fields locally.



### Lab 2 — Compare how two safe parsers represent duplicate keys using synthetic data and document the trust implication.



### Lab 3 — Refactor a fictional “deserialize directly into privileged object” design into explicit validated data transfer objects.

For every lab, use only owned/synthetic inputs and record objective, scope, version, expected behavior, observed evidence, cleanup, remediation, and regression result as described in [Study Method](../Guides/STUDY-METHOD.md).

## Knowledge checks

Answer these without looking at the notes:

1. What is the primary trust boundary in this topic?
2. Which state or identity transition is easiest to misunderstand?
3. What observation would disprove your first hypothesis?
4. Which control removes authority rather than merely adding detection?
5. How would you reproduce the behavior safely after remediation?

## Guided study workflow

Complete at least one authorized lab and explain the mechanism, trust boundary, failure state, evidence, and defensive fix in your own words. Use **Bookmarks**, **Progress**, and **Learning paths** in the numbered menu instead of memorizing command-line flags.

## Next modules

Recommended related modules: **014, 022, 040, 068, 069, 071, 108**. From the main menu, choose **Search lessons** to find related sections across the full guide.

---

# SAML, WS-Federation and Enterprise SSO Internals

Develop a deep model of enterprise browser federation: assertions, bindings, metadata, signatures, audience, subject confirmation, relay state, session lifetime and trust between identity providers and service providers.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, captures, or lab environments you own or are explicitly authorized to test. Prefer localhost, synthetic data, disposable VMs/containers, prerecorded traces, and read-only analysis whenever possible.

## Learning objectives

By the end of this module you should be able to:

- Explain **IdP and SP trust roles** and identify its most important trust boundary, state transition, and evidence source.
- Explain **SAML assertions and conditions** and identify its most important trust boundary, state transition, and evidence source.
- Explain **browser SSO profiles and bindings** and identify its most important trust boundary, state transition, and evidence source.
- Explain **metadata and signing keys** and identify its most important trust boundary, state transition, and evidence source.
- Explain **audience and recipient validation** and identify its most important trust boundary, state transition, and evidence source.
- Explain **NameID and attribute mapping** and identify its most important trust boundary, state transition, and evidence source.

## Analysis method

Use [Study Method](../Guides/STUDY-METHOD.md). Start by identifying ownership or identity, the state transition that can fail, and the evidence that would distinguish a real boundary violation from a diagnostic artifact.

## Deep concepts

### 1. IdP and SP trust

SAML separates an Identity Provider that asserts identity from a Service Provider that consumes assertions. The SP must trust only configured issuers/keys and apply its own authorization; a valid assertion from the wrong tenant or relationship is not sufficient.

### 2. assertions and conditions

Assertions contain subject, authentication, attributes, and conditions such as time windows. Validate the complete security context—issuer, signature, audience, recipient/destination, time, subject confirmation, and expected flow—not just the presence of a signature.

### 3. browser SSO profiles and bindings

SAML browser SSO moves protocol messages through the browser using defined bindings. Track which message is request/response state, which values are attacker-controlled in transit, and how the SP correlates the response to the initiating session.

### 4. metadata and signing keys

Metadata distributes entity identifiers, endpoints, certificates, and capabilities. Treat metadata changes and key rollover as high-impact configuration events with authenticated distribution, overlap windows, audit trail, and tested rollback.

### 5. audience and recipient validation

Audience and recipient/destination fields prevent an assertion intended for one service or endpoint from being reused elsewhere. Validation must compare against canonical local configuration rather than values learned from the incoming request.

### 6. NameID and attribute mapping

Attributes become local identity/role data only after mapping rules are applied. Avoid trusting mutable display names or email strings as stable privileged identifiers; define collision, case, domain, and missing-attribute behavior explicitly.

### 7. RelayState and request correlation

RelayState carries application navigation/context and should not become an unvalidated open redirect or authorization source. Correlate responses with the original authentication request/session and keep application state separate from identity proof.

### 8. logout and session lifetime

SAML logout and local application sessions have different lifecycles and reliability. Define what local tokens are revoked when upstream identity changes, what happens if single logout fails, and how administrators terminate sessions during an incident.

## Engineering focus

For this module, convert each important claim into a security invariant and a regression test. Prefer controls that remove unnecessary authority, make state transitions explicit, bound resource use, and leave enough telemetry to explain a failure. The reusable evidence and lab-record format is in [Study Method](../Guides/STUDY-METHOD.md).

## Authorized lab sequence

### Lab 1 — Draw an SP-initiated SSO flow and annotate every signed/unsigned value plus who validates it.



### Lab 2 — Create a fictional assertion-validation checklist and test it against synthetic good/bad assertion descriptions, not real accounts.



### Lab 3 — Model key rollover where old and new IdP signing keys overlap and define safe acceptance windows.

For every lab, use only owned/synthetic inputs and record objective, scope, version, expected behavior, observed evidence, cleanup, remediation, and regression result as described in [Study Method](../Guides/STUDY-METHOD.md).

## Knowledge checks

Answer these without looking at the notes:

1. What is the primary trust boundary in this topic?
2. Which state or identity transition is easiest to misunderstand?
3. What observation would disprove your first hypothesis?
4. Which control removes authority rather than merely adding detection?
5. How would you reproduce the behavior safely after remediation?

## Guided study workflow

Complete at least one authorized lab and explain the mechanism, trust boundary, failure state, evidence, and defensive fix in your own words. Use **Bookmarks**, **Progress**, and **Learning paths** in the numbered menu instead of memorizing command-line flags.

## Next modules

Recommended related modules: **021, 032, 039, 072, 092, 093**. From the main menu, choose **Search lessons** to find related sections across the full guide.

---

# SCIM, Identity Lifecycle and Provisioning Security

Authentication is only one phase of identity. This module covers account creation, updates, group membership, deprovisioning, authoritative sources, drift and SCIM security controls.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, captures, or lab environments you own or are explicitly authorized to test. Prefer localhost, synthetic data, disposable VMs/containers, prerecorded traces, and read-only analysis whenever possible.

## Learning objectives

By the end of this module you should be able to:

- Explain **identity lifecycle states** and identify its most important trust boundary, state transition, and evidence source.
- Explain **SCIM resources and schemas** and identify its most important trust boundary, state transition, and evidence source.
- Explain **provisioning clients and service providers** and identify its most important trust boundary, state transition, and evidence source.
- Explain **group and role synchronization** and identify its most important trust boundary, state transition, and evidence source.
- Explain **deprovisioning and disable semantics** and identify its most important trust boundary, state transition, and evidence source.
- Explain **source-of-truth conflicts** and identify its most important trust boundary, state transition, and evidence source.

## Analysis method

Use [Study Method](../Guides/STUDY-METHOD.md). Start by identifying ownership or identity, the state transition that can fail, and the evidence that would distinguish a real boundary violation from a diagnostic artifact.

## Deep concepts

### 1. identity lifecycle states

Provisioning is a state machine: invited, active, suspended, disabled, deleted, restored, and sometimes external/contractor states have different authority. Define transitions and which source is allowed to initiate each one.

### 2. SCIM resources and schemas

SCIM represents users, groups, and extensions with standardized resource schemas. Validate identifiers, mutability, uniqueness, enterprise extensions, and tenant scope instead of mapping every received field directly into privileged directory attributes.

### 3. clients and service providers

A SCIM client usually has powerful lifecycle authority over a service provider. Use narrowly scoped credentials, authenticate the client strongly, limit tenant/environment, and log every create/update/deactivate operation with a stable correlation identifier.

### 4. group and role synchronization

Group membership can translate directly into application roles or access. Review nested groups, default groups, name collisions, delayed propagation, and whether an external identity source is actually authoritative for the target privilege.

### 5. deprovision and disable

Offboarding security depends on rapid removal of active sessions, tokens, group membership, service credentials, and downstream access—not just marking a profile inactive. Measure deprovisioning latency and reconcile systems that were offline or failed updates.

### 6. source-of-truth conflicts

HR, directory, IdP, application, and manual admin changes can disagree about identity state. Define precedence and conflict handling so a stale system cannot silently re-enable a user or overwrite a security-sensitive attribute.

### 7. pagination, filtering and bulk

Large SCIM deployments use pagination, filters, PATCH, and bulk operations that can create partial-success and retry behavior. Make updates idempotent where practical, validate per-object authorization, and retain enough status to reconcile failed subsets safely.

### 8. telemetry and reconciliation

Periodic reconciliation detects drift between intended identity state and application reality. Compare active users, groups, privilege, unmanaged accounts, failed provisioning events, and last-success timestamps rather than trusting one provisioning API response.

## Engineering focus

For this module, convert each important claim into a security invariant and a regression test. Prefer controls that remove unnecessary authority, make state transitions explicit, bound resource use, and leave enough telemetry to explain a failure. The reusable evidence and lab-record format is in [Study Method](../Guides/STUDY-METHOD.md).

## Authorized lab sequence

### Lab 1 — Build a synthetic HR→IdP→SaaS lifecycle diagram for joiner/mover/leaver events.



### Lab 2 — Design a SCIM-like local JSON dataset and verify that group changes produce expected least-privilege outcomes.



### Lab 3 — Write a deprovisioning checklist that includes active sessions, API tokens, shared resources and audit evidence.

For every lab, use only owned/synthetic inputs and record objective, scope, version, expected behavior, observed evidence, cleanup, remediation, and regression result as described in [Study Method](../Guides/STUDY-METHOD.md).

## Knowledge checks

Answer these without looking at the notes:

1. What is the primary trust boundary in this topic?
2. Which state or identity transition is easiest to misunderstand?
3. What observation would disprove your first hypothesis?
4. Which control removes authority rather than merely adding detection?
5. How would you reproduce the behavior safely after remediation?

## Guided study workflow

Complete at least one authorized lab and explain the mechanism, trust boundary, failure state, evidence, and defensive fix in your own words. Use **Bookmarks**, **Progress**, and **Learning paths** in the numbered menu instead of memorizing command-line flags.

## Next modules

Recommended related modules: **021, 039, 042, 059, 092, 093, 128**. From the main menu, choose **Search lessons** to find related sections across the full guide.

---

# PAM, Just-in-Time Access, JEA and Privileged Access Engineering

Privileged access should be exceptional, attributable and short-lived. Study privileged access management, just-in-time elevation, session controls, break-glass design and least-privilege administration.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, captures, or lab environments you own or are explicitly authorized to test. Prefer localhost, synthetic data, disposable VMs/containers, prerecorded traces, and read-only analysis whenever possible.

## Learning objectives

By the end of this module you should be able to:

- Explain **privileged identity separation** and identify its most important trust boundary, state transition, and evidence source.
- Explain **vaulting versus ephemeral credentials** and identify its most important trust boundary, state transition, and evidence source.
- Explain **just-in-time and just-enough access** and identify its most important trust boundary, state transition, and evidence source.
- Explain **approval and policy workflows** and identify its most important trust boundary, state transition, and evidence source.
- Explain **session recording and command context** and identify its most important trust boundary, state transition, and evidence source.
- Explain **break-glass accounts** and identify its most important trust boundary, state transition, and evidence source.

## Analysis method

Use [Study Method](../Guides/STUDY-METHOD.md). Start by identifying ownership or identity, the state transition that can fail, and the evidence that would distinguish a real boundary violation from a diagnostic artifact.

## Deep concepts

### 1. privileged identity separation

Administrative work should use identities separate from ordinary browsing, email, and development. Separate accounts and workstations reduce credential exposure and make privileged actions easier to attribute, restrict, and monitor.

### 2. vaulting versus ephemeral access

A password vault protects long-lived secrets but does not eliminate their lifecycle risk. Ephemeral credentials or short-lived tokens can reduce standing exposure; choose the model according to system capability, recovery requirements, and auditability.

### 3. JIT and JEA

Just-In-Time access grants privilege only for a bounded period, while Just Enough Administration limits the operations available. Combine them so elevation is both short-lived and narrowly scoped, with policy evaluated before the session begins.

### 4. approval and policy workflows

High-impact elevation may require ticket context, approval, risk signals, or separation of duties. The approval object should be bound to the requested identity, target, role, reason, and duration so it cannot be reused for a different action.

### 5. session recording and command context

Privileged-session recording can improve accountability but may capture secrets or sensitive data. Record enough identity, target, command/action, and timing context for investigation while applying retention, access controls, and redaction appropriate to the environment.

### 6. break-glass access

Emergency accounts exist for failure of normal identity systems, so they must not depend on the same control plane. Protect them strongly, monitor every use, test access periodically, and rotate/reseal credentials after an activation.

### 7. de-escalation and expiry

Elevation should expire automatically and remove derived sessions/tokens where possible. Verify the actual effective permissions after expiry; a removed group membership is insufficient if cached credentials or active sessions retain privilege.

### 8. service and administrator boundaries

Human administrators and non-human service identities have different authentication and lifecycle needs. Avoid shared accounts, interactive use of service credentials, and service principals with broad tenant-wide permissions unrelated to their workload.

## Engineering focus

For this module, convert each important claim into a security invariant and a regression test. Prefer controls that remove unnecessary authority, make state transitions explicit, bound resource use, and leave enough telemetry to explain a failure. The reusable evidence and lab-record format is in [Study Method](../Guides/STUDY-METHOD.md).

## Authorized lab sequence

### Lab 1 — Create a fictional admin-task catalog and assign minimum roles, duration and approval conditions.



### Lab 2 — Model a JIT elevation lifecycle from request through expiry and verify what evidence remains afterward.



### Lab 3 — Design a break-glass test plan that proves availability without exposing real emergency credentials.

For every lab, use only owned/synthetic inputs and record objective, scope, version, expected behavior, observed evidence, cleanup, remediation, and regression result as described in [Study Method](../Guides/STUDY-METHOD.md).

## Knowledge checks

Answer these without looking at the notes:

1. What is the primary trust boundary in this topic?
2. Which state or identity transition is easiest to misunderstand?
3. What observation would disprove your first hypothesis?
4. Which control removes authority rather than merely adding detection?
5. How would you reproduce the behavior safely after remediation?

## Guided study workflow

Complete at least one authorized lab and explain the mechanism, trust boundary, failure state, evidence, and defensive fix in your own words. Use **Bookmarks**, **Progress**, and **Learning paths** in the numbered menu instead of memorizing command-line flags.

## Next modules

Recommended related modules: **021, 032, 042, 049, 059, 072, 093**. From the main menu, choose **Search lessons** to find related sections across the full guide.

---

# WebAuthn, FIDO2 and Passkey Internals

Go beyond “passkeys are phishing resistant.” Understand relying-party scope, origins, credential IDs, discoverable credentials, authenticators, attestation, user verification and recovery.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, captures, or lab environments you own or are explicitly authorized to test. Prefer localhost, synthetic data, disposable VMs/containers, prerecorded traces, and read-only analysis whenever possible.

## Learning objectives

By the end of this module you should be able to:

- Explain **WebAuthn ceremony roles** and identify its most important trust boundary, state transition, and evidence source.
- Explain **Relying Party ID and origin binding** and identify its most important trust boundary, state transition, and evidence source.
- Explain **credential creation and assertions** and identify its most important trust boundary, state transition, and evidence source.
- Explain **authenticator data and counters** and identify its most important trust boundary, state transition, and evidence source.
- Explain **user presence versus user verification** and identify its most important trust boundary, state transition, and evidence source.
- Explain **discoverable/syncable credentials** and identify its most important trust boundary, state transition, and evidence source.

## Analysis method

Use [Study Method](../Guides/STUDY-METHOD.md). Start by identifying ownership or identity, the state transition that can fail, and the evidence that would distinguish a real boundary violation from a diagnostic artifact.

## Deep concepts

### 1. ceremony roles

WebAuthn involves a relying party, browser/client, authenticator, and user. The ceremony binds these actors using origin/RP context and public-key credentials so authentication does not depend on sending a reusable password secret to the relying party.

### 2. RP ID and origin binding

The RP ID scopes credentials to an expected web domain relationship, while the browser supplies origin context. Correct validation prevents a credential assertion created for one site from being accepted by an unrelated site simply because the account name matches.

### 3. creation and assertion

Registration creates a credential and stores its public information; authentication requests a signed assertion over fresh challenge/context. Challenges must be unpredictable, single-use, session-bound, and expire so captured responses cannot be reused as generic bearer credentials.

### 4. authenticator data and counters

Authenticator data carries RP binding, flags, and additional authenticator state; some authenticators also expose signature counters. Counters can be a risk signal but should not be treated as universally reliable because synchronization and authenticator behavior vary.

### 5. user presence versus verification

User presence shows that someone interacted with the authenticator, while user verification adds a local factor such as PIN or biometric policy. Relying parties should request the level appropriate to the transaction and validate returned flags against that policy.

### 6. discoverable and syncable credentials

Discoverable credentials can support username-less sign-in, and passkeys may be synchronized across a user’s trusted device ecosystem. Threat modeling must therefore include account recovery, device enrollment, sync-provider security, and user notification—not only the hardware authenticator.

### 7. attestation and privacy

Attestation can provide information about authenticator provenance but can also add deployment complexity and privacy implications. Require it only when a concrete assurance need justifies the operational cost; authentication security does not generally depend on identifying a user’s device model.

### 8. recovery and multi-device lifecycle

Passkey deployments need recovery, new-device onboarding, credential inventory, revocation, lost-device response, and multiple-authenticator support. A weak recovery channel can become the easiest way around otherwise phishing-resistant authentication.

## Engineering focus

For this module, convert each important claim into a security invariant and a regression test. Prefer controls that remove unnecessary authority, make state transitions explicit, bound resource use, and leave enough telemetry to explain a failure. The reusable evidence and lab-record format is in [Study Method](../Guides/STUDY-METHOD.md).

## Authorized lab sequence

### Lab 1 — Design a WebAuthn registration/authentication sequence diagram with challenge, origin and RP-ID validation points.



### Lab 2 — Compare password+OTP, device-bound WebAuthn and syncable passkeys across phishing resistance, recovery and device loss.



### Lab 3 — Create a recovery threat model for a fictional passkey-only service.

For every lab, use only owned/synthetic inputs and record objective, scope, version, expected behavior, observed evidence, cleanup, remediation, and regression result as described in [Study Method](../Guides/STUDY-METHOD.md).

## Knowledge checks

Answer these without looking at the notes:

1. What is the primary trust boundary in this topic?
2. Which state or identity transition is easiest to misunderstand?
3. What observation would disprove your first hypothesis?
4. Which control removes authority rather than merely adding detection?
5. How would you reproduce the behavior safely after remediation?

## Guided study workflow

Complete at least one authorized lab and explain the mechanism, trust boundary, failure state, evidence, and defensive fix in your own words. Use **Bookmarks**, **Progress**, and **Learning paths** in the numbered menu instead of memorizing command-line flags.

## Next modules

Recommended related modules: **021, 039, 049, 078, 092, 100**. From the main menu, choose **Search lessons** to find related sections across the full guide.

---

# Secrets Rotation, Envelope Encryption, KMS and HSM Architecture

Build a practical key-management architecture model: data keys, key-encryption keys, KMS/HSM boundaries, envelope encryption, rotation, grants, audit trails and recovery.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, captures, or lab environments you own or are explicitly authorized to test. Prefer localhost, synthetic data, disposable VMs/containers, prerecorded traces, and read-only analysis whenever possible.

## Learning objectives

By the end of this module you should be able to:

- Explain **data keys and key-encryption keys** and identify its most important trust boundary, state transition, and evidence source.
- Explain **envelope encryption** and identify its most important trust boundary, state transition, and evidence source.
- Explain **KMS authorization and grants** and identify its most important trust boundary, state transition, and evidence source.
- Explain **HSM trust boundaries** and identify its most important trust boundary, state transition, and evidence source.
- Explain **rotation versus re-encryption** and identify its most important trust boundary, state transition, and evidence source.
- Explain **key versioning and cryptoperiods** and identify its most important trust boundary, state transition, and evidence source.

## Analysis method

Use [Study Method](../Guides/STUDY-METHOD.md). Start by identifying ownership or identity, the state transition that can fail, and the evidence that would distinguish a real boundary violation from a diagnostic artifact.

## Deep concepts

### 1. data keys and key-encryption keys

Envelope encryption separates data-encryption keys from higher-level keys that protect or wrap them. This limits direct use of root keys and lets applications rotate wrapping policy without necessarily rewriting every byte of protected data.

### 2. envelope encryption

A common design generates a fresh data key, encrypts data locally, then stores only the ciphertext plus a wrapped form of that data key. Bind context such as tenant/resource identifiers where supported so a wrapped key cannot be moved silently to an unrelated object.

### 3. KMS authentication and grants

Cloud or enterprise KMS operations are authorization decisions over high-value keys. Restrict which workload identities may encrypt, decrypt, sign, or administer; separate key administrators from data users and log resource, operation, key version, and caller context.

### 4. HSM boundaries

Hardware Security Modules isolate key material and cryptographic operations behind a controlled interface. An HSM does not fix application authorization: if an overly privileged service is allowed to request decryption for arbitrary data, the hardware will faithfully perform the wrong authorized operation.

### 5. rotation versus re-encryption

Rotating a master/wrapping key can mean new writes use a new version while old ciphertext remains decryptable with old versions. Full re-encryption is a separate migration task with availability, integrity, cost, and rollback considerations.

### 6. versioning and cryptoperiods

Keys should have stable identifiers and explicit versions so systems know which material produced an artifact. Cryptoperiods depend on algorithm, exposure, data sensitivity, usage volume, recovery, and operational constraints rather than one universal rotation interval.

### 7. backup and recovery

Key loss can be as damaging as key theft. Define whether keys are recoverable, how backups are protected, who can authorize recovery, what quorum or offline controls exist, and how a recovery event is audited and tested.

### 8. audit and key-use attribution

Every sensitive key operation should be attributable to a workload/user identity, key/version, operation, resource context, policy decision, and time. Avoid logging plaintext secrets or data while retaining enough correlation to investigate unexpected decrypt/sign activity.

## Engineering focus

For this module, convert each important claim into a security invariant and a regression test. Prefer controls that remove unnecessary authority, make state transitions explicit, bound resource use, and leave enough telemetry to explain a failure. The reusable evidence and lab-record format is in [Study Method](../Guides/STUDY-METHOD.md).

## Authorized lab sequence

### Lab 1 — Design envelope encryption for a fictional database record and show what is stored beside ciphertext.



### Lab 2 — Create a rotation matrix for API secrets, TLS keys, database encryption keys and signing keys.



### Lab 3 — Model KMS outage and key-revocation scenarios and define what should fail open versus fail closed.

For every lab, use only owned/synthetic inputs and record objective, scope, version, expected behavior, observed evidence, cleanup, remediation, and regression result as described in [Study Method](../Guides/STUDY-METHOD.md).

## Knowledge checks

Answer these without looking at the notes:

1. What is the primary trust boundary in this topic?
2. Which state or identity transition is easiest to misunderstand?
3. What observation would disprove your first hypothesis?
4. Which control removes authority rather than merely adding detection?
5. How would you reproduce the behavior safely after remediation?

## Guided study workflow

Complete at least one authorized lab and explain the mechanism, trust boundary, failure state, evidence, and defensive fix in your own words. Use **Bookmarks**, **Progress**, and **Learning paths** in the numbered menu instead of memorizing command-line flags.

## Next modules

Recommended related modules: **020, 049, 078, 100, 101, 103, 113**. From the main menu, choose **Search lessons** to find related sections across the full guide.

---

# Git Security, Signed Commits, Branch Protection and Repository Trust

Source control is part of the software trust chain. Study identity, review policy, signed objects, protected branches, secrets exposure, dependency changes and repository recovery.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, captures, or lab environments you own or are explicitly authorized to test. Prefer localhost, synthetic data, disposable VMs/containers, prerecorded traces, and read-only analysis whenever possible.

## Learning objectives

By the end of this module you should be able to:

- Explain **Git object integrity and hashes** and identify its most important trust boundary, state transition, and evidence source.
- Explain **commit/tag signatures** and identify its most important trust boundary, state transition, and evidence source.
- Explain **branch protection and required reviews** and identify its most important trust boundary, state transition, and evidence source.
- Explain **CODEOWNERS-style approval concepts** and identify its most important trust boundary, state transition, and evidence source.
- Explain **force pushes and history rewriting** and identify its most important trust boundary, state transition, and evidence source.
- Explain **secret exposure and rotation** and identify its most important trust boundary, state transition, and evidence source.

## Analysis method

Use [Study Method](../Guides/STUDY-METHOD.md). Start by identifying ownership or identity, the state transition that can fail, and the evidence that would distinguish a real boundary violation from a diagnostic artifact.

## Deep concepts

### 1. Git object integrity and hashes

Git addresses objects by cryptographic hashes and links commits into a content history, which helps detect accidental or unauthorized modification. Repository integrity still depends on trusted refs, hosting controls, signatures where required, and protecting the identities allowed to update branches/tags.

### 2. commit and tag signatures

Signed commits or tags can attest that a key approved specific history, but verification needs trusted key ownership and policy. Decide which events must be signed, how keys are enrolled/revoked, and what CI does when a signature is missing or invalid.

### 3. branch protection and reviews

Protected branches should require review, status checks, restricted force pushes, and controlled merge paths according to risk. Review policy must cover automation/bots and administrative bypasses; an emergency override should be visible and followed by retrospective review.

### 4. CODEOWNERS and approval paths

CODEOWNERS can route changes in sensitive directories to appropriate reviewers. Treat it as workflow assistance, not a complete authorization boundary: protect the ownership file itself and enforce required approvals through repository policy.

### 5. force pushes and history rewrite

History rewriting can remove or replace commits referenced by collaborators or releases. Restrict force pushes on protected refs, retain server/audit history, and distinguish cleanup of accidental secrets from an attempt to hide unauthorized changes.

### 6. secret exposure and rotation

Deleting a secret from the latest commit does not revoke copies already cloned, cached, logged, or indexed. Revoke/rotate the credential first, assess usage, then clean history only if policy requires it and coordinate the rewrite carefully.

### 7. submodules and dependency refs

Submodules and other pinned repository references extend trust to another repository/object. Pin immutable reviewed revisions, validate ownership/provenance, and prevent an untrusted dependency location from changing what privileged build automation fetches.

### 8. backup, mirroring and recovery

Repository resilience includes remote mirrors, protected release artifacts, issue/metadata backups where needed, and tested restoration. Recovery should preserve evidence of unauthorized ref changes while allowing teams to re-establish known-good branches and tags.

## Engineering focus

For this module, convert each important claim into a security invariant and a regression test. Prefer controls that remove unnecessary authority, make state transitions explicit, bound resource use, and leave enough telemetry to explain a failure. The reusable evidence and lab-record format is in [Study Method](../Guides/STUDY-METHOD.md).

## Authorized lab sequence

### Lab 1 — Create a throwaway local repository, sign a test tag if you have a test key, and document verification outcomes.



### Lab 2 — Design branch-protection rules for a critical library versus a personal experiment.



### Lab 3 — Simulate accidental placement of a fake secret string and practice safe history cleanup plus “rotate the real secret” reasoning.

For every lab, use only owned/synthetic inputs and record objective, scope, version, expected behavior, observed evidence, cleanup, remediation, and regression result as described in [Study Method](../Guides/STUDY-METHOD.md).

## Knowledge checks

Answer these without looking at the notes:

1. What is the primary trust boundary in this topic?
2. Which state or identity transition is easiest to misunderstand?
3. What observation would disprove your first hypothesis?
4. Which control removes authority rather than merely adding detection?
5. How would you reproduce the behavior safely after remediation?

## Guided study workflow

Complete at least one authorized lab and explain the mechanism, trust boundary, failure state, evidence, and defensive fix in your own words. Use **Bookmarks**, **Progress**, and **Learning paths** in the numbered menu instead of memorizing command-line flags.

## Next modules

Recommended related modules: **022, 029, 040, 084, 097, 098, 109**. From the main menu, choose **Search lessons** to find related sections across the full guide.

---

# SBOM, VEX, Provenance and Vulnerability Intelligence Pipelines

Turn dependency data into decisions. Learn SBOM structure, component identity, VEX statements, exploitability context, build provenance, vulnerability feeds and evidence-based prioritization.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, captures, or lab environments you own or are explicitly authorized to test. Prefer localhost, synthetic data, disposable VMs/containers, prerecorded traces, and read-only analysis whenever possible.

## Learning objectives

By the end of this module you should be able to:

- Explain **SBOM purpose and limitations** and identify its most important trust boundary, state transition, and evidence source.
- Explain **package identity and version matching** and identify its most important trust boundary, state transition, and evidence source.
- Explain **transitive dependencies** and identify its most important trust boundary, state transition, and evidence source.
- Explain **VEX status and justification** and identify its most important trust boundary, state transition, and evidence source.
- Explain **provenance linkage** and identify its most important trust boundary, state transition, and evidence source.
- Explain **vulnerability feeds and enrichment** and identify its most important trust boundary, state transition, and evidence source.

## Analysis method

Use [Study Method](../Guides/STUDY-METHOD.md). Start by identifying ownership or identity, the state transition that can fail, and the evidence that would distinguish a real boundary violation from a diagnostic artifact.

## Deep concepts

### 1. SBOM purpose and limits

A Software Bill of Materials inventories components and relationships to improve visibility, response, and dependency management. It is evidence about composition, not proof of security, reachability, authenticity, or whether the listed software actually executes in a vulnerable way.

### 2. package identity and version

Useful component records need an unambiguous ecosystem/name/version or package URL plus enough provenance to distinguish forks, vendored copies, and rebuilt artifacts. Ambiguous package identity creates false matches and blind spots during vulnerability response.

### 3. transitive dependencies

Direct dependencies pull in transitive components that may carry equal or greater risk. Generate inventories from the resolved build/runtime graph where possible and distinguish build-only, test, optional, bundled, and runtime relationships.

### 4. VEX status and justification

Vulnerability Exploitability eXchange communicates whether a known vulnerability affects a specific product and why. Status needs evidence, scope, author, timestamp, and justification; it should not become a permanent “not affected” label that survives architecture changes without review.

### 5. provenance linkage

SBOMs are stronger when linked to signed/verified build provenance identifying source, builder, inputs, parameters, and resulting artifact. This lets responders ask not only “what packages?” but “which build produced this deployed binary and under what trusted workflow?”

### 6. vulnerability feeds

Scanner/feed matches change as advisories, package mappings, and severity evolve. Preserve feed timestamp/source, normalize identifiers, and verify high-impact matches against authoritative package/advisory data instead of treating one vendor score as final truth.

### 7. reachability and exposure

A vulnerable library may be present but unreachable; conversely, “not reachable” analysis can miss configuration, reflection, native calls, or future paths. Use reachability as prioritization evidence, not an automatic reason to suppress remediation forever.

### 8. gates and exception lifecycle

Build/deploy policy should define which findings block, warn, or require an approved exception. Exceptions need owner, justification, compensating control, expiry, and re-evaluation when package, environment, exploitability, or business exposure changes.

## Engineering focus

For this module, convert each important claim into a security invariant and a regression test. Prefer controls that remove unnecessary authority, make state transitions explicit, bound resource use, and leave enough telemetry to explain a failure. The reusable evidence and lab-record format is in [Study Method](../Guides/STUDY-METHOD.md).

## Authorized lab sequence

### Lab 1 — Create a small SBOM-like inventory for a local Python project using only package metadata you own.



### Lab 2 — For three fictional CVEs, write VEX-style affected/not-affected/under-investigation rationales with evidence requirements.



### Lab 3 — Design a pipeline that links source commit → build provenance → artifact → SBOM → deployment inventory.

For every lab, use only owned/synthetic inputs and record objective, scope, version, expected behavior, observed evidence, cleanup, remediation, and regression result as described in [Study Method](../Guides/STUDY-METHOD.md).

## Knowledge checks

Answer these without looking at the notes:

1. What is the primary trust boundary in this topic?
2. Which state or identity transition is easiest to misunderstand?
3. What observation would disprove your first hypothesis?
4. Which control removes authority rather than merely adding detection?
5. How would you reproduce the behavior safely after remediation?

## Guided study workflow

Complete at least one authorized lab and explain the mechanism, trust boundary, failure state, evidence, and defensive fix in your own words. Use **Bookmarks**, **Progress**, and **Learning paths** in the numbered menu instead of memorizing command-line flags.

## Next modules

Recommended related modules: **005, 022, 050, 084, 097, 098, 109**. From the main menu, choose **Search lessons** to find related sections across the full guide.

---

# Kubernetes Admission Control, Policy-as-Code and Runtime Guardrails

Deepen Kubernetes security by focusing on the control path between an API request and a running workload: admission, mutation, validation, pod-security controls, policy engines and runtime drift.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, captures, or lab environments you own or are explicitly authorized to test. Prefer localhost, synthetic data, disposable VMs/containers, prerecorded traces, and read-only analysis whenever possible.

## Learning objectives

By the end of this module you should be able to:

- Explain **API admission lifecycle** and identify its most important trust boundary, state transition, and evidence source.
- Explain **mutating versus validating admission** and identify its most important trust boundary, state transition, and evidence source.
- Explain **Pod Security Standards concepts** and identify its most important trust boundary, state transition, and evidence source.
- Explain **policy-as-code engines** and identify its most important trust boundary, state transition, and evidence source.
- Explain **image provenance and allowlists** and identify its most important trust boundary, state transition, and evidence source.
- Explain **namespace and service-account context** and identify its most important trust boundary, state transition, and evidence source.

## Analysis method

Use [Study Method](../Guides/STUDY-METHOD.md). Start by identifying ownership or identity, the state transition that can fail, and the evidence that would distinguish a real boundary violation from a diagnostic artifact.

## Deep concepts

### 1. admission lifecycle

Kubernetes admission runs after authentication/authorization but before an API object is persisted. It is a policy enforcement point for resource configuration, not a replacement for runtime isolation, RBAC, image security, or continuous drift detection.

### 2. mutating versus validating admission

Mutating admission can add/default fields before validation; validating admission accepts or rejects the resulting object. Keep mutations predictable and observable because hidden changes make policy reasoning, debugging, and signed-manifest expectations harder.

### 3. Pod Security Standards

Pod Security Standards define baseline/restricted expectations for risky pod settings such as privilege, host namespaces, capabilities, volume types, and seccomp. Apply profiles according to workload need and manage narrow exceptions explicitly.

### 4. policy engines

Admission policy engines evaluate manifests against organization-specific rules. Version policies as code, test allow/deny cases in CI, use clear messages, scope rules carefully, and monitor exceptions so a temporary bypass does not become permanent architecture.

### 5. image provenance and allowlists

Admission can restrict registries, digests, signatures/attestations, or provenance according to deployment policy. Prefer immutable digests and verified provenance for high-assurance workloads rather than trusting a mutable image tag alone.

### 6. namespace and service-account context

The same manifest can have different risk depending on namespace labels, service account, secrets, network policy, quotas, and target environment. Admission decisions should include the context that actually determines workload authority.

### 7. runtime drift

Admission checks desired objects at creation/update time, but containers, nodes, credentials, external services, or manually changed infrastructure can drift afterward. Combine admission with runtime telemetry, configuration reconciliation, and periodic policy checks.

### 8. telemetry and exceptions

Record policy/version, object, namespace, user/service account, decision, violated rule, and exception identity. Exception workflows should require owner, reason, scope, and expiry, with dashboards showing which high-risk workloads are outside normal policy.

## Engineering focus

For this module, convert each important claim into a security invariant and a regression test. Prefer controls that remove unnecessary authority, make state transitions explicit, bound resource use, and leave enough telemetry to explain a failure. The reusable evidence and lab-record format is in [Study Method](../Guides/STUDY-METHOD.md).

## Authorized lab sequence

### Lab 1 — Write policy requirements for a toy Kubernetes manifest: non-root, restricted capabilities, approved image source and resource limits.



### Lab 2 — Compare admission-time and runtime evidence for the same fictional workload.



### Lab 3 — Create an exception record with owner, reason, expiry and compensating control, then define an automated review trigger.

For every lab, use only owned/synthetic inputs and record objective, scope, version, expected behavior, observed evidence, cleanup, remediation, and regression result as described in [Study Method](../Guides/STUDY-METHOD.md).

## Knowledge checks

Answer these without looking at the notes:

1. What is the primary trust boundary in this topic?
2. Which state or identity transition is easiest to misunderstand?
3. What observation would disprove your first hypothesis?
4. Which control removes authority rather than merely adding detection?
5. How would you reproduce the behavior safely after remediation?

## Guided study workflow

Complete at least one authorized lab and explain the mechanism, trust boundary, failure state, evidence, and defensive fix in your own words. Use **Bookmarks**, **Progress**, and **Learning paths** in the numbered menu instead of memorizing command-line flags.

## Next modules

Recommended related modules: **024, 041, 075, 093, 097, 113**. From the main menu, choose **Search lessons** to find related sections across the full guide.

---

# Service Mesh, mTLS, Network Policy and East-West Security

Service-to-service traffic needs explicit identity and policy. Study sidecar/ambient models, mTLS, workload identity, network policy, authorization, observability and failure handling.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, captures, or lab environments you own or are explicitly authorized to test. Prefer localhost, synthetic data, disposable VMs/containers, prerecorded traces, and read-only analysis whenever possible.

## Learning objectives

By the end of this module you should be able to:

- Explain **east-west versus north-south traffic** and identify its most important trust boundary, state transition, and evidence source.
- Explain **service mesh data/control planes** and identify its most important trust boundary, state transition, and evidence source.
- Explain **mTLS identity establishment** and identify its most important trust boundary, state transition, and evidence source.
- Explain **service authorization policy** and identify its most important trust boundary, state transition, and evidence source.
- Explain **Kubernetes NetworkPolicy concepts** and identify its most important trust boundary, state transition, and evidence source.
- Explain **sidecar versus ambient interception** and identify its most important trust boundary, state transition, and evidence source.

## Analysis method

Use [Study Method](../Guides/STUDY-METHOD.md). Start by identifying ownership or identity, the state transition that can fail, and the evidence that would distinguish a real boundary violation from a diagnostic artifact.

## Deep concepts

### 1. east-west versus north-south traffic

North-south controls protect entry/exit paths, while east-west policy governs service-to-service communication inside an environment. Microservices should not inherit broad mutual trust merely because workloads share a cluster or private network.

### 2. data plane and control plane

A service mesh data plane handles workload traffic while the control plane distributes identity, routing, certificate, and policy state. Protect control-plane administration strongly because a policy or trust-bundle change can influence many services simultaneously.

### 3. mTLS workload identity

Mutual TLS can authenticate both workloads and encrypt traffic, but authorization must still decide which identity may call which service/action. Validate certificate/trust-domain mapping and avoid treating successful TLS as permission to access every endpoint.

### 4. service authorization policy

Service policy should express source workload identity, destination, operation/path where relevant, and environment/tenant context. Default-deny plus explicit grants is easier to audit than implicit connectivity derived from network location.

### 5. Kubernetes NetworkPolicy

NetworkPolicy constrains network reachability at the Kubernetes networking layer and complements, rather than duplicates, identity-aware mesh policy. Confirm CNI support, namespace/pod selectors, egress paths, DNS needs, and default behavior with safe connectivity tests.

### 6. sidecar versus ambient models

Sidecar and ambient mesh designs place enforcement/telemetry components differently. Threat models should identify which process/node component can observe or influence traffic and what happens when that component is unavailable, bypassed, or misconfigured.

### 7. certificate rotation and trust bundles

Short-lived workload certificates reduce long-term credential exposure but require dependable issuance, clock, rotation, and trust-bundle rollout. Test overlap and failure behavior so a CA/key transition does not create either a broad trust window or service outage.

### 8. telemetry and failure behavior

Mesh telemetry should connect source/destination workload identity, policy decision, protocol, request outcome, and certificate context. Define whether policy/control-plane failures fail closed or degrade, and make that behavior visible during incident response.

## Engineering focus

For this module, convert each important claim into a security invariant and a regression test. Prefer controls that remove unnecessary authority, make state transitions explicit, bound resource use, and leave enough telemetry to explain a failure. The reusable evidence and lab-record format is in [Study Method](../Guides/STUDY-METHOD.md).

## Authorized lab sequence

### Lab 1 — Draw a three-service architecture and write both network reachability and identity authorization matrices.



### Lab 2 — Model certificate rotation with overlapping trust bundles and define how stale workloads recover.



### Lab 3 — Compare a direct call, sidecar-proxied call and ambient-mesh call in terms of trust boundaries and telemetry.

For every lab, use only owned/synthetic inputs and record objective, scope, version, expected behavior, observed evidence, cleanup, remediation, and regression result as described in [Study Method](../Guides/STUDY-METHOD.md).

## Knowledge checks

Answer these without looking at the notes:

1. What is the primary trust boundary in this topic?
2. Which state or identity transition is easiest to misunderstand?
3. What observation would disprove your first hypothesis?
4. Which control removes authority rather than merely adding detection?
5. How would you reproduce the behavior safely after remediation?

## Guided study workflow

Complete at least one authorized lab and explain the mechanism, trust boundary, failure state, evidence, and defensive fix in your own words. Use **Bookmarks**, **Progress**, and **Learning paths** in the numbered menu instead of memorizing command-line flags.

## Next modules

Recommended related modules: **021, 024, 075, 093, 113, 135**. From the main menu, choose **Search lessons** to find related sections across the full guide.

---

# Cloud Logging, Detection and Cross-Cloud Investigation

Cloud investigations depend on control-plane and identity evidence distributed across services. Learn normalized event models, immutable collection, correlation, time, multi-account structure and investigation playbooks.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, captures, or lab environments you own or are explicitly authorized to test. Prefer localhost, synthetic data, disposable VMs/containers, prerecorded traces, and read-only analysis whenever possible.

## Learning objectives

By the end of this module you should be able to:

- Explain **control-plane audit logs** and identify its most important trust boundary, state transition, and evidence source.
- Explain **identity and token context** and identify its most important trust boundary, state transition, and evidence source.
- Explain **data-plane versus management-plane telemetry** and identify its most important trust boundary, state transition, and evidence source.
- Explain **multi-account/project/subscription aggregation** and identify its most important trust boundary, state transition, and evidence source.
- Explain **log integrity and retention** and identify its most important trust boundary, state transition, and evidence source.
- Explain **time synchronization and event ordering** and identify its most important trust boundary, state transition, and evidence source.

## Analysis method

Use [Study Method](../Guides/STUDY-METHOD.md). Start by identifying ownership or identity, the state transition that can fail, and the evidence that would distinguish a real boundary violation from a diagnostic artifact.

## Deep concepts

### 1. control-plane audit logs

Cloud audit logs record administrative/API actions such as identity, policy, networking, storage, and resource changes. Enable and centralize them before an incident; retroactive investigation is impossible for events the provider/account never retained.

### 2. identity and token context

A cloud event is meaningful only when caller identity, assumed role/service principal, session/token context, source, target resource, and organization/account/tenant are correlated. Normalize temporary identities back to their parent workload or human where possible.

### 3. data-plane versus management-plane logs

Management-plane logs describe configuration/control actions, while data-plane logs describe access to workloads or stored data. High-value investigations often require both because a policy change and subsequent data access happen in different telemetry systems.

### 4. central aggregation

Send logs to a security account/project or independent store with narrow write/admin permissions. Cross-account aggregation reduces the chance that compromise of one workload lets an attacker erase the only copy of its control-plane evidence.

### 5. integrity and retention

Use provider/object controls, immutability where appropriate, retention policy, export verification, and restricted deletion to preserve evidence. Retention should reflect incident-detection latency, legal/privacy requirements, and cost rather than a single arbitrary number.

### 6. time synchronization and ordering

Distributed cloud events may arrive late, use different timestamps, or represent server/client time differently. Preserve original timestamps and ingestion time, correlate with stable request/session IDs, and avoid assuming displayed order equals causal order.

### 7. cross-cloud normalization

AWS, Azure, GCP, SaaS, and identity providers use different names for principals, resources, actions, and outcomes. Normalize into a common investigation schema while preserving provider-specific raw fields so analysts can pivot without losing semantics.

### 8. investigation pivots and evidence preservation

Start from a known indicator—identity, resource, IP, request ID, key, or time window—and pivot across identity, control plane, workload, network, and data access. Export only necessary evidence, hash important artifacts, and document query/time-zone assumptions for reproducibility.

## Engineering focus

For this module, convert each important claim into a security invariant and a regression test. Prefer controls that remove unnecessary authority, make state transitions explicit, bound resource use, and leave enough telemetry to explain a failure. The reusable evidence and lab-record format is in [Study Method](../Guides/STUDY-METHOD.md).

## Authorized lab sequence

### Lab 1 — Create a synthetic multi-cloud event dataset and normalize five fields across three provider-style schemas.



### Lab 2 — Build an investigation timeline for a fictional policy change followed by unusual access and remediation.



### Lab 3 — Design retention tiers for high-value audit logs, noisy data-plane logs and forensic snapshots.

For every lab, use only owned/synthetic inputs and record objective, scope, version, expected behavior, observed evidence, cleanup, remediation, and regression result as described in [Study Method](../Guides/STUDY-METHOD.md).

## Knowledge checks

Answer these without looking at the notes:

1. What is the primary trust boundary in this topic?
2. Which state or identity transition is easiest to misunderstand?
3. What observation would disprove your first hypothesis?
4. Which control removes authority rather than merely adding detection?
5. How would you reproduce the behavior safely after remediation?

## Guided study workflow

Complete at least one authorized lab and explain the mechanism, trust boundary, failure state, evidence, and defensive fix in your own words. Use **Bookmarks**, **Progress**, and **Learning paths** in the numbered menu instead of memorizing command-line flags.

## Next modules

Recommended related modules: **019, 023, 037, 047, 059, 076, 080, 105, 106**. From the main menu, choose **Search lessons** to find related sections across the full guide.

---

# RAG, Vector Databases and AI Retrieval Security

Retrieval-augmented generation introduces a new data and trust pipeline. Study ingestion, embeddings, chunking, metadata authorization, prompt-injection through documents, provenance and output grounding.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, captures, or lab environments you own or are explicitly authorized to test. Prefer localhost, synthetic data, disposable VMs/containers, prerecorded traces, and read-only analysis whenever possible.

## Learning objectives

By the end of this module you should be able to:

- Explain **RAG architecture and trust boundaries** and identify its most important trust boundary, state transition, and evidence source.
- Explain **document ingestion and parsing** and identify its most important trust boundary, state transition, and evidence source.
- Explain **chunking and embeddings** and identify its most important trust boundary, state transition, and evidence source.
- Explain **vector-store tenancy and authorization** and identify its most important trust boundary, state transition, and evidence source.
- Explain **retrieval-time metadata filters** and identify its most important trust boundary, state transition, and evidence source.
- Explain **indirect prompt injection** and identify its most important trust boundary, state transition, and evidence source.

## Analysis method

Use [Study Method](../Guides/STUDY-METHOD.md). Start by identifying ownership or identity, the state transition that can fail, and the evidence that would distinguish a real boundary violation from a diagnostic artifact.

## Deep concepts

### 1. RAG architecture and trust boundaries

Retrieval-Augmented Generation combines ingestion, storage/indexing, retrieval, prompt assembly, model execution, and output handling. Each step has different authority: retrieved text should be treated as untrusted data, not as instructions that automatically override application policy.

### 2. ingestion and parsing

Documents may contain active formats, malformed content, hidden text, metadata, or instructions designed for downstream models. Normalize and parse in a constrained pipeline, restrict supported formats, scan resource usage, and preserve source identity/provenance.

### 3. chunking and embeddings

Chunk size, overlap, metadata, and embedding model affect what content is retrievable and how boundaries are preserved. Security-sensitive labels such as tenant, classification, and source should remain explicit metadata rather than being inferred only from semantic similarity.

### 4. tenancy and authorization

Vector similarity is not authorization. Filter candidate content using server-side tenant/resource permissions before it can enter the model context, and test with two synthetic tenants to ensure nearest-neighbor results cannot cross access boundaries.

### 5. metadata filters

Metadata filters must be constructed from trusted application state and validated by the storage layer. Avoid letting a model or client generate arbitrary filters that broaden tenant, confidentiality, or document-state constraints.

### 6. indirect prompt injection

Retrieved content can contain text that attempts to manipulate the model or connected tools. Separate instructions from data, constrain tool permissions, label provenance, apply deterministic authorization outside the model, and assume untrusted documents may contain adversarial instructions.

### 7. source provenance and citations

Store document identity, version, ingestion time, owner/tenant, classification, and source location so an answer can be traced back to evidence. Citations help auditability but should be generated from the actual retrieved source set, not invented by the model.

### 8. poisoning, deletion and reindexing

A poisoned or outdated document can remain in embeddings after the source changes. Define authenticated ingestion, review, deletion propagation, reindexing, version rollback, and incident procedures that can identify which answers were influenced by a bad corpus version.

## Engineering focus

For this module, convert each important claim into a security invariant and a regression test. Prefer controls that remove unnecessary authority, make state transitions explicit, bound resource use, and leave enough telemetry to explain a failure. The reusable evidence and lab-record format is in [Study Method](../Guides/STUDY-METHOD.md).

## Authorized lab sequence

### Lab 1 — Build a local toy RAG design on paper with public/sample documents and annotate trust boundaries.



### Lab 2 — Create synthetic “malicious instruction inside a document” examples and write expected safe model behavior without connecting external tools.



### Lab 3 — Design metadata filters for two fictional tenants and test access decisions with a table of allowed/denied retrievals.

For every lab, use only owned/synthetic inputs and record objective, scope, version, expected behavior, observed evidence, cleanup, remediation, and regression result as described in [Study Method](../Guides/STUDY-METHOD.md).

## Knowledge checks

Answer these without looking at the notes:

1. What is the primary trust boundary in this topic?
2. Which state or identity transition is easiest to misunderstand?
3. What observation would disprove your first hypothesis?
4. Which control removes authority rather than merely adding detection?
5. How would you reproduce the behavior safely after remediation?

## Guided study workflow

Complete at least one authorized lab and explain the mechanism, trust boundary, failure state, evidence, and defensive fix in your own words. Use **Bookmarks**, **Progress**, and **Learning paths** in the numbered menu instead of memorizing command-line flags.

## Next modules

Recommended related modules: **022, 025, 041, 046, 057, 071, 114**. From the main menu, choose **Search lessons** to find related sections across the full guide.

---

# AI-Generated Code, Vibe Coding and Secure Review

AI-assisted development increases speed but can amplify insecure assumptions. This module provides a disciplined review pipeline for generated code, dependencies, secrets, tests, threat models and deployment.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, captures, or lab environments you own or are explicitly authorized to test. Prefer localhost, synthetic data, disposable VMs/containers, prerecorded traces, and read-only analysis whenever possible.

## Learning objectives

By the end of this module you should be able to:

- Explain **generated-code trust model** and identify its most important trust boundary, state transition, and evidence source.
- Explain **specification before generation** and identify its most important trust boundary, state transition, and evidence source.
- Explain **dependency and package verification** and identify its most important trust boundary, state transition, and evidence source.
- Explain **secret handling and configuration** and identify its most important trust boundary, state transition, and evidence source.
- Explain **authentication/authorization review** and identify its most important trust boundary, state transition, and evidence source.
- Explain **input validation and unsafe parsing** and identify its most important trust boundary, state transition, and evidence source.

## Analysis method

Use [Study Method](../Guides/STUDY-METHOD.md). Start by identifying ownership or identity, the state transition that can fail, and the evidence that would distinguish a real boundary violation from a diagnostic artifact.

## Deep concepts

### 1. AI-generated code trust model

Treat generated code like code from an untrusted external contributor: it may be plausible, incomplete, outdated, insecure, or reference nonexistent APIs. Human ownership, repository review, automated tests, and security controls remain responsible for the final behavior.

### 2. specification before generation

Write security invariants, data types, trust boundaries, error behavior, and non-functional constraints before asking a model to implement code. A precise specification lets reviewers test correctness instead of accepting whichever architecture the generator happened to choose.

### 3. dependency and package verification

Models can suggest stale, wrong, typo-squatted, or nonexistent packages. Verify package identity from the official ecosystem, pin/lock appropriate versions, review transitive dependencies, and never install a dependency solely because generated instructions mention it.

### 4. secrets and configuration

Generated examples often contain placeholder tokens, permissive debug settings, broad CORS, weak defaults, or secrets loaded incorrectly. Keep secrets out of prompts/source, use environment/secret managers appropriately, and review production configuration separately from demo code.

### 5. authentication and authorization review

Generated handlers can check that a user is logged in while omitting object- or tenant-level authorization. Review every sensitive operation for subject, resource, action, tenant, and privilege context, and write negative tests with multiple synthetic identities.

### 6. input validation and parsing

Models frequently generate happy-path parsers with weak bounds or ambiguous error handling. Define schemas, size/depth limits, canonicalization, safe deserialization, and output encoding according to the actual sink and protocol.

### 7. generated tests and false confidence

AI-generated tests can reproduce the same incorrect assumption as generated implementation code. Include adversarial/negative cases derived independently from the specification and measure whether tests fail when the security control is deliberately broken in a toy branch.

### 8. human review, provenance and change control

Record which code was generated or heavily assisted when policy requires it, but judge the resulting artifact by normal engineering evidence. Protected branches, code review, CI, provenance, dependency scanning, secrets scanning, and rollback should apply regardless of authorship.

## Engineering focus

For this module, convert each important claim into a security invariant and a regression test. Prefer controls that remove unnecessary authority, make state transitions explicit, bound resource use, and leave enough telemetry to explain a failure. The reusable evidence and lab-record format is in [Study Method](../Guides/STUDY-METHOD.md).

## Authorized lab sequence

### Lab 1 — Take a small local script you own and build a security-review checklist covering inputs, files, subprocesses, network, secrets and dependencies.



### Lab 2 — Write five negative tests for a generated login/API example using fictional data.



### Lab 3 — Compare two AI-generated designs for the same feature and choose the one with smaller authority and fewer dependencies, documenting why.

For every lab, use only owned/synthetic inputs and record objective, scope, version, expected behavior, observed evidence, cleanup, remediation, and regression result as described in [Study Method](../Guides/STUDY-METHOD.md).

## Knowledge checks

Answer these without looking at the notes:

1. What is the primary trust boundary in this topic?
2. Which state or identity transition is easiest to misunderstand?
3. What observation would disprove your first hypothesis?
4. Which control removes authority rather than merely adding detection?
5. How would you reproduce the behavior safely after remediation?

## Guided study workflow

Complete at least one authorized lab and explain the mechanism, trust boundary, failure state, evidence, and defensive fix in your own words. Use **Bookmarks**, **Progress**, and **Learning paths** in the numbered menu instead of memorizing command-line flags.

## Next modules

Recommended related modules: **022, 025, 036, 040, 041, 046, 097, 098, 108, 109**. From the main menu, choose **Search lessons** to find related sections across the full guide.

---

# Advanced Authorized Labs III: Modern Protocols, Identity, Platforms and AI Security

A third capstone lab collection that integrates the new expansion. Every exercise is designed for localhost, synthetic data, disposable VMs/containers or documentation-based modeling.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, captures, or lab environments you own or are explicitly authorized to test. Prefer localhost, synthetic data, disposable VMs/containers, prerecorded traces, and read-only analysis whenever possible.

## Learning objectives

By the end of this module you should be able to:

- Explain **memory-lifetime lab** and identify its most important trust boundary, state transition, and evidence source.
- Explain **race-condition and TOCTOU lab** and identify its most important trust boundary, state transition, and evidence source.
- Explain **IPC/broker authorization lab** and identify its most important trust boundary, state transition, and evidence source.
- Explain **HTTP/3 and edge trust lab** and identify its most important trust boundary, state transition, and evidence source.
- Explain **SAML/SCIM lifecycle lab** and identify its most important trust boundary, state transition, and evidence source.
- Explain **WebAuthn/passkey threat-model lab** and identify its most important trust boundary, state transition, and evidence source.

## Analysis method

Use [Study Method](../Guides/STUDY-METHOD.md). Start by identifying ownership or identity, the state transition that can fail, and the evidence that would distinguish a real boundary violation from a diagnostic artifact.

## Deep concepts

### 1. memory-lifetime lab

Use a small owned program with a deliberate lifetime bug and sanitizer instrumentation. The learning goal is to identify allocation, ownership transfer, invalidation, first bad access, and the code-level fix—not to turn corruption into code execution.

### 2. race-condition and TOCTOU lab

Build a toy concurrent workflow with a controlled race or check/use gap, then use synchronization or an atomic operation to remove it. Preserve a repeatable stress case and verify that the fixed invariant survives many interleavings.

### 3. IPC and broker authorization lab

Create a local low-privilege client and a narrow broker service that exposes one harmless privileged action. Test valid and invalid caller/resource combinations and confirm the broker authorizes using trusted peer context rather than client-declared identity.

### 4. HTTP/3 and edge trust lab

Use a local or disposable stack that exposes an application through a proxy/edge path. Compare protocol/forwarding behavior and verify that host, client identity, authorization, and cache decisions remain consistent without sending tests to public infrastructure.

### 5. SAML and SCIM lifecycle lab

Use synthetic identities in a test IdP/application. Model login, attribute mapping, provisioning, role change, disable, session revocation, and reconciliation; measure which state changes propagate and where stale access can remain.

### 6. WebAuthn and passkey threat-model lab

Use a development relying party or documented test environment to trace registration, challenge, origin/RP binding, user verification, authentication, lost-device recovery, and credential revocation. Record which controls are cryptographic and which are account-lifecycle policy.

### 7. Kubernetes policy lab

In a disposable cluster, define a small admission or workload policy and test known-allowed and known-denied manifests. Record policy version, user/service account, object, decision, exception behavior, and a regression case after policy changes.

### 8. RAG and AI-code review lab

Build a synthetic RAG corpus and a small AI-assisted code change. Test tenant filtering, untrusted document instructions, source provenance, dependency verification, authorization, and negative tests while ensuring tools have only lab-scoped permissions.

## Engineering focus

For this module, convert each important claim into a security invariant and a regression test. Prefer controls that remove unnecessary authority, make state transitions explicit, bound resource use, and leave enough telemetry to explain a failure. The reusable evidence and lab-record format is in [Study Method](../Guides/STUDY-METHOD.md).

## Authorized lab sequence

### Lab 1 — Complete one systems lab using sanitizers or race detection on code you own.



### Lab 2 — Complete one identity lab using synthetic SAML/SCIM/WebAuthn data and explicit validation rules.



### Lab 3 — Complete one cloud/AI architecture lab with policy matrices, telemetry plan and a retest checklist.

For every lab, use only owned/synthetic inputs and record objective, scope, version, expected behavior, observed evidence, cleanup, remediation, and regression result as described in [Study Method](../Guides/STUDY-METHOD.md).

## Knowledge checks

Answer these without looking at the notes:

1. What is the primary trust boundary in this topic?
2. Which state or identity transition is easiest to misunderstand?
3. What observation would disprove your first hypothesis?
4. Which control removes authority rather than merely adding detection?
5. How would you reproduce the behavior safely after remediation?

## Guided study workflow

Complete at least one authorized lab and explain the mechanism, trust boundary, failure state, evidence, and defensive fix in your own words. Use **Bookmarks**, **Progress**, and **Learning paths** in the numbered menu instead of memorizing command-line flags.

## Next modules

Recommended related modules: **027, 045, 085, 110, 115, 116, 117, 124, 128, 131, 135, 138, 139**. From the main menu, choose **Search lessons** to find related sections across the full guide.
