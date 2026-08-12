# Hacking Guide Project — Όλα τα Μαθήματα

> Δημιουργήθηκε από τα κατηγοριοποιημένα ελληνικά μαθήματα. Επεξεργάσου τα επιμέρους αρχεία και μετά κάνε rebuild.

## Ευρετήριο

### 01-Fundamentals-and-Methodology

- 001. [Βάσεις Κυβερνοασφάλειας και Μεθοδολογία Ethical Hacking](#βάσεις-κυβερνοασφάλειας-και-μεθοδολογία-ethical-hacking)
- 005. [Vulnerability Analysis και Prioritization](#vulnerability-analysis-και-prioritization)
- 026. [Αναφορές Security Assessment και Purple Teaming](#αναφορές-security-assessment-και-purple-teaming)
- 041. [Threat Modeling και Αρχιτεκτονική Ασφάλειας](#threat-modeling-και-αρχιτεκτονική-ασφάλειας)
- 043. [Responsible Disclosure και Ηθική Bug Bounty](#responsible-disclosure-και-ηθική-bug-bounty)
- 050. [Vulnerability Management και Attack Surface Management](#vulnerability-management-και-attack-surface-management)
- 061. [Μεθοδολογία Security Research και Συλλογιστική Attack Surface](#μεθοδολογία-security-research-και-συλλογιστική-attack-surface)

### 02-Recon-Pentesting-Web-and-AppSec

- 002. [Footprinting, Reconnaissance και Ανακάλυψη Attack Surface](#footprinting-reconnaissance-και-ανακάλυψη-attack-surface)
- 003. [Network Scanning και Service Discovery](#network-scanning-και-service-discovery)
- 004. [Service Enumeration και Protocol-Aware Validation](#service-enumeration-και-protocol-aware-validation)
- 013. [Ασφάλεια Web Servers και Reverse Proxies](#ασφάλεια-web-servers-και-reverse-proxies)
- 014. [Ασφάλεια Web Εφαρμογών](#ασφάλεια-web-εφαρμογών)
- 015. [Penetration Testing: Scope, Evidence, Reporting και Retest](#penetration-testing-scope-evidence-reporting-και-retest)
- 040. [Secure Coding και OWASP ASVS](#secure-coding-και-owasp-asvs)
- 052. [Web, Browser και HTTP σε Βάθος](#web-browser-και-http-σε-βάθος)
- 069. [Προχωρημένη Επεξεργασία Web Requests και Parser Differentials](#προχωρημένη-επεξεργασία-web-requests-και-parser-differentials)
- 070. [Browser Isolation, Origins, CORS, CSP και Client-Side Trust](#browser-isolation-origins-cors-csp-και-client-side-trust)
- 071. [API Authorization, State Machines και Distributed Abuse Cases](#api-authorization-state-machines-και-distributed-abuse-cases)
- 089. [Ασφάλεια GraphQL, gRPC, WebSockets και Real-Time APIs](#ασφάλεια-graphql-grpc-websockets-και-real-time-apis)
- 090. [Ασφάλεια Databases, Data Layer και Query Engines](#ασφάλεια-databases-data-layer-και-query-engines)
- 108. [Advanced Code Auditing, Static Analysis, Dataflow και Taint Reasoning](#advanced-code-auditing-static-analysis-dataflow-και-taint-reasoning)
- 124. [HTTP/2, HTTP/3, QUIC και Modern Web Transport Security](#http2-http3-quic-και-modern-web-transport-security)
- 126. [CDN, Reverse Proxy, Cache και Edge Security](#cdn-reverse-proxy-cache-και-edge-security)
- 127. [Serialization, Deserialization και Parser Security](#serialization-deserialization-και-parser-security)

### 03-Systems-Malware-and-Reverse-Engineering

- 006. [Host Security Assessment και System Hardening](#host-security-assessment-και-system-hardening)
- 007. [Malware: Έννοιες, Analysis και Defensive Triage](#malware-έννοιες-analysis-και-defensive-triage)
- 011. [Ασφάλεια Sessions, Cookies, Tokens και Πρόληψη Session Hijacking](#ασφάλεια-sessions-cookies-tokens-και-πρόληψη-session-hijacking)
- 033. [Ασφάλεια και Hardening Linux](#ασφάλεια-και-hardening-linux)
- 053. [Memory Safety και Exploit Mitigations](#memory-safety-και-exploit-mitigations)
- 062. [CPU Privilege, Syscalls και Εσωτερική Λειτουργία Processes](#cpu-privilege-syscalls-και-εσωτερική-λειτουργία-processes)
- 063. [Assembly για Security Analysis — x86-64 και ARM64](#assembly-για-security-analysis-x86-64-και-arm64)
- 064. [Executable Formats, Loaders και Dynamic Linking](#executable-formats-loaders-και-dynamic-linking)
- 065. [Debugging, Crash Triage και Root-Cause Analysis](#debugging-crash-triage-και-root-cause-analysis)
- 066. [Μηχανισμοί Memory Corruption και Ανάλυση Mitigations](#μηχανισμοί-memory-corruption-και-ανάλυση-mitigations)
- 067. [Reverse Engineering και Ανάλυση Προγραμμάτων](#reverse-engineering-και-ανάλυση-προγραμμάτων)
- 068. [Fuzzing, Harness Design και Coverage-Guided Testing](#fuzzing-harness-design-και-coverage-guided-testing)
- 073. [Windows Internals — Tokens, Services, Registry, ETW και Security Boundaries](#windows-internals-tokens-services-registry-etw-και-security-boundaries)
- 074. [Linux Internals — Capabilities, Namespaces, Seccomp, LSM και eBPF](#linux-internals-capabilities-namespaces-seccomp-lsm-και-ebpf)
- 079. [Malware Analysis και Behavioral Triage](#malware-analysis-και-behavioral-triage)
- 084. [Patch Diffing, Root Cause Ευπαθειών και Secure Regression Analysis](#patch-diffing-root-cause-ευπαθειών-και-secure-regression-analysis)
- 095. [Kernel Security Primitives, Attack Surface και Runtime Trust](#kernel-security-primitives-attack-surface-και-runtime-trust)
- 096. [eBPF Observability, Linux Telemetry και Detection Engineering](#ebpf-observability-linux-telemetry-και-detection-engineering)
- 099. [Compiler Toolchains, Sanitizers, CFI και Binary Hardening](#compiler-toolchains-sanitizers-cfi-και-binary-hardening)
- 109. [Vulnerability Research: Reproduction, Regression και Coordinated Disclosure](#vulnerability-research-reproduction-regression-και-coordinated-disclosure)
- 111. [WebAssembly, JVM, CLR και Ασφάλεια Managed Runtimes](#webassembly-jvm-clr-και-ασφάλεια-managed-runtimes)
- 112. [Browser Extensions, Electron και Desktop Web Runtime Security](#browser-extensions-electron-και-desktop-web-runtime-security)
- 116. [Heap Allocators, Object Lifetimes και Memory Debugging](#heap-allocators-object-lifetimes-και-memory-debugging)
- 117. [Concurrency, Race Conditions, TOCTOU και Atomicity](#concurrency-race-conditions-toctou-και-atomicity)
- 118. [IPC, RPC, D-Bus, COM και Local Trust Boundaries](#ipc-rpc-d-bus-com-και-local-trust-boundaries)
- 119. [Sandboxing, Broker Architectures και Isolation Assurance](#sandboxing-broker-architectures-και-isolation-assurance)
- 120. [macOS Security Internals: TCC, SIP, Gatekeeper, Notarization και XProtect](#macos-security-internals-tcc-sip-gatekeeper-notarization-και-xprotect)

### 04-Network-Wireless-and-Internet

- 008. [Packet Capture, Sniffing και Network Visibility](#packet-capture-sniffing-και-network-visibility)
- 010. [Ανθεκτικότητα σε Denial-of-Service και Έλεγχος Εξάντλησης Πόρων](#ανθεκτικότητα-σε-denial-of-service-και-έλεγχος-εξάντλησης-πόρων)
- 012. [Firewalls, IDS/IPS, Honeypots και Επαλήθευση Ανίχνευσης](#firewalls-idsips-honeypots-και-επαλήθευση-ανίχνευσης)
- 016. [Ασφάλεια Ασύρματων Δικτύων](#ασφάλεια-ασύρματων-δικτύων)
- 035. [Ασφάλεια Email, DNS και Domains](#ασφάλεια-email-dns-και-domains)
- 051. [Δικτύωση σε Βάθος](#δικτύωση-σε-βάθος)
- 077. [Reverse Engineering Δικτυακών Πρωτοκόλλων και Traffic Analysis](#reverse-engineering-δικτυακών-πρωτοκόλλων-και-traffic-analysis)
- 086. [Ασφάλεια IPv6, Neighbor Discovery και Σύγχρονα LAN Attack Surfaces](#ασφάλεια-ipv6-neighbor-discovery-και-σύγχρονα-lan-attack-surfaces)
- 087. [Ασφάλεια DNS, Routing, BGP και Υποδομής Internet](#ασφάλεια-dns-routing-bgp-και-υποδομής-internet)
- 088. [Enterprise Wireless, WPA3, 802.1X και Wi‑Fi 6/6E/7](#enterprise-wireless-wpa3-8021x-και-wifi-66e7)
- 122. [Cellular Networks, LTE/5G Architecture και Mobile Network Security](#cellular-networks-lte5g-architecture-και-mobile-network-security)
- 123. [Radio, SDR και RF Security Fundamentals](#radio-sdr-και-rf-security-fundamentals)
- 125. [DNSSEC, DoH, DoQ, Resolver Privacy και DNS Trust](#dnssec-doh-doq-resolver-privacy-και-dns-trust)

### 05-Mobile-IoT-and-Hardware

- 017. [Ασφάλεια Κινητών Συσκευών](#ασφάλεια-κινητών-συσκευών)
- 018. [Ασφάλεια IoT και OT](#ασφάλεια-iot-και-ot)
- 054. [Ασφάλεια Hardware, Firmware και Boot](#ασφάλεια-hardware-firmware-και-boot)
- 055. [Ασφάλεια Bluetooth, NFC και Proximity](#ασφάλεια-bluetooth-nfc-και-proximity)
- 056. [Android Security σε Βάθος](#android-security-σε-βάθος)
- 082. [Reverse Engineering Android Εφαρμογών και Mobile App Internals](#reverse-engineering-android-εφαρμογών-και-mobile-app-internals)
- 083. [Firmware, Embedded Systems και Ανάλυση Hardware Interfaces](#firmware-embedded-systems-και-ανάλυση-hardware-interfaces)
- 103. [TPM, Secure Boot, Attestation, TEEs και Device Identity](#tpm-secure-boot-attestation-tees-και-device-identity)
- 121. [iOS Security Internals: Entitlements, Code Signing, Keychain και Data Protection](#ios-security-internals-entitlements-code-signing-keychain-και-data-protection)

### 06-Identity-Cryptography-and-Trust

- 020. [Κρυπτογραφία](#κρυπτογραφία)
- 021. [Identity, Zero Trust και Ασφάλεια Πρόσβασης](#identity-zero-trust-και-ασφάλεια-πρόσβασης)
- 032. [Ασφάλεια Windows και Active Directory](#ασφάλεια-windows-και-active-directory)
- 039. [OAuth, OIDC, Passkeys και Σύγχρονο Authentication](#oauth-oidc-passkeys-και-σύγχρονο-authentication)
- 049. [Secrets, PKI και Διαχείριση Κλειδιών](#secrets-pki-και-διαχείριση-κλειδιών)
- 072. [Kerberos, Active Directory και Enterprise Identity Internals](#kerberos-active-directory-και-enterprise-identity-internals)
- 078. [TLS, PKI και Αποτυχίες Υλοποίησης Κρυπτογραφίας](#tls-pki-και-αποτυχίες-υλοποίησης-κρυπτογραφίας)
- 092. [OAuth 2.0 Security BCP, OIDC Federation και Token Defense](#oauth-20-security-bcp-oidc-federation-και-token-defense)
- 093. [Μοντέλα Authorization: RBAC, ABAC, ReBAC και Policy Engines](#μοντέλα-authorization-rbac-abac-rebac-και-policy-engines)
- 100. [Cryptographic Protocol Engineering, Key Agreement και State Machines](#cryptographic-protocol-engineering-key-agreement-και-state-machines)
- 101. [Post-Quantum Migration, Crypto Agility και Hybrid Deployment](#post-quantum-migration-crypto-agility-και-hybrid-deployment)
- 102. [Side Channels, Timing, Cache, Faults και Physical Leakage](#side-channels-timing-cache-faults-και-physical-leakage)
- 113. [Workload Identity, SPIFFE/SPIRE, mTLS και Zero-Trust Service Identity](#workload-identity-spiffespire-mtls-και-zero-trust-service-identity)
- 128. [SAML, WS-Federation και Enterprise SSO Internals](#saml-ws-federation-και-enterprise-sso-internals)
- 129. [SCIM, Identity Lifecycle και Provisioning Security](#scim-identity-lifecycle-και-provisioning-security)
- 130. [PAM, Just-in-Time Access, JEA και Privileged Access Engineering](#pam-just-in-time-access-jea-και-privileged-access-engineering)
- 131. [WebAuthn, FIDO2 και Passkey Internals](#webauthn-fido2-και-passkey-internals)
- 132. [Secrets Rotation, Envelope Encryption, KMS και HSM Architecture](#secrets-rotation-envelope-encryption-kms-και-hsm-architecture)

### 07-Cloud-Containers-and-Supply-Chain

- 019. [Ασφάλεια Cloud](#ασφάλεια-cloud)
- 022. [Ασφαλές Λογισμικό, APIs και Εφοδιαστική Αλυσίδα](#ασφαλές-λογισμικό-apis-και-εφοδιαστική-αλυσίδα)
- 024. [Containers, Kubernetes και DevSecOps](#containers-kubernetes-και-devsecops)
- 075. [Εσωτερική Λειτουργία Isolation σε Containers και Kubernetes](#εσωτερική-λειτουργία-isolation-σε-containers-και-kubernetes)
- 076. [Cloud IAM, Control Planes, Metadata και Temporary Credentials](#cloud-iam-control-planes-metadata-και-temporary-credentials)
- 091. [Message Queues, Event Streaming και Ασφάλεια Distributed Systems](#message-queues-event-streaming-και-ασφάλεια-distributed-systems)
- 094. [Virtualization, Hypervisors, VMs και Confidential Computing](#virtualization-hypervisors-vms-και-confidential-computing)
- 097. [CI/CD, Build Provenance, SLSA 1.2 και Artifact Trust](#cicd-build-provenance-slsa-12-και-artifact-trust)
- 098. [Package Managers, Registries, Dependencies και Ecosystem Security](#package-managers-registries-dependencies-και-ecosystem-security)
- 104. [Serverless, Edge Workers, Functions και Event-Driven Cloud Security](#serverless-edge-workers-functions-και-event-driven-cloud-security)
- 105. [Multi-Cloud, SaaS Federation, Tenant Isolation και Control Planes](#multi-cloud-saas-federation-tenant-isolation-και-control-planes)
- 133. [Git Security, Signed Commits, Branch Protection και Repository Trust](#git-security-signed-commits-branch-protection-και-repository-trust)
- 134. [SBOM, VEX, Provenance και Vulnerability Intelligence Pipelines](#sbom-vex-provenance-και-vulnerability-intelligence-pipelines)
- 135. [Kubernetes Admission Control, Policy-as-Code και Runtime Guardrails](#kubernetes-admission-control-policy-as-code-και-runtime-guardrails)
- 136. [Service Mesh, mTLS, Network Policy και East-West Security](#service-mesh-mtls-network-policy-και-east-west-security)

### 08-Blue-Team-IR-Forensics-and-Resilience

- 023. [Detection Engineering, Incident Response και Threat Hunting](#detection-engineering-incident-response-και-threat-hunting)
- 034. [Threat Intelligence και OSINT](#threat-intelligence-και-osint)
- 037. [Digital Forensics και Διαχείριση Αποδεικτικών Στοιχείων](#digital-forensics-και-διαχείριση-αποδεικτικών-στοιχείων)
- 038. [Ανθεκτικότητα και Ανάκαμψη από Ransomware](#ανθεκτικότητα-και-ανάκαμψη-από-ransomware)
- 044. [Ασφάλεια Endpoint, Browser και SaaS](#ασφάλεια-endpoint-browser-και-saas)
- 047. [SOC, SIEM, SOAR και Λειτουργίες Ανίχνευσης](#soc-siem-soar-και-λειτουργίες-ανίχνευσης)
- 048. [Business Continuity, Disaster Recovery και Backup Engineering](#business-continuity-disaster-recovery-και-backup-engineering)
- 080. [Προχωρημένο Detection Engineering και MITRE ATT&CK v19](#προχωρημένο-detection-engineering-και-mitre-attck-v19)
- 081. [Digital Forensics — Filesystem Timelines και Memory Artifacts](#digital-forensics-filesystem-timelines-και-memory-artifacts)
- 106. [Endpoint EDR Internals, Telemetry και Response Architecture](#endpoint-edr-internals-telemetry-και-response-architecture)
- 107. [Threat Emulation, Adversary Simulation και Purple-Team Lab Design](#threat-emulation-adversary-simulation-και-purple-team-lab-design)
- 137. [Cloud Logging, Detection και Cross-Cloud Investigation](#cloud-logging-detection-και-cross-cloud-investigation)

### 09-AI-GRC-Privacy-Data-and-Human-Security

- 009. [Άμυνα απέναντι στην Κοινωνική Μηχανική και Ασφάλεια Ανθρώπινου Παράγοντα](#άμυνα-απέναντι-στην-κοινωνική-μηχανική-και-ασφάλεια-ανθρώπινου-παράγοντα)
- 025. [Ασφάλεια AI και LLM](#ασφάλεια-ai-και-llm)
- 042. [Governance, Risk, Compliance και Privacy](#governance-risk-compliance-και-privacy)
- 046. [Agentic AI, MCP και Ασφάλεια Εργαλείων](#agentic-ai-mcp-και-ασφάλεια-εργαλείων)
- 057. [Privacy, Data Protection και Operational Hygiene](#privacy-data-protection-και-operational-hygiene)
- 059. [Security Metrics και Μέτρηση Προγράμματος](#security-metrics-και-μέτρηση-προγράμματος)
- 060. [Φυσική Ασφάλεια και Ανθρώπινη Ανθεκτικότητα](#φυσική-ασφάλεια-και-ανθρώπινη-ανθεκτικότητα)
- 114. [Data Security, DLP, Tokenization, Privacy Engineering και Data Lifecycle](#data-security-dlp-tokenization-privacy-engineering-και-data-lifecycle)
- 138. [RAG, Vector Databases και AI Retrieval Security](#rag-vector-databases-και-ai-retrieval-security)
- 139. [AI-Generated Code, Vibe Coding και Secure Review](#ai-generated-code-vibe-coding-και-secure-review)

### 10-Termux-and-Security-Automation

- 028. [Βάσεις Termux και Android Linux](#βάσεις-termux-και-android-linux)
- 029. [Ροή Εργασίας Termux, Python, Git και Αυτοματοποίηση](#ροή-εργασίας-termux-python-git-και-αυτοματοποίηση)
- 030. [Δικτύωση Termux, SSH και Τοπικές Υπηρεσίες](#δικτύωση-termux-ssh-και-τοπικές-υπηρεσίες)
- 031. [Λειτουργία Security Lab και Troubleshooting στο Termux](#λειτουργία-security-lab-και-troubleshooting-στο-termux)
- 036. [Python για Αυτοματοποίηση Ασφάλειας](#python-για-αυτοματοποίηση-ασφάλειας)

### 11-Labs-Capstones-and-Career

- 027. [Εξουσιοδοτημένα Hands-On Labs](#εξουσιοδοτημένα-hands-on-labs)
- 045. [Capstones, Checklists και Study Roadmaps](#capstones-checklists-και-study-roadmaps)
- 058. [Καριέρα Cybersecurity και Οδηγίες Portfolio](#καριέρα-cybersecurity-και-οδηγίες-portfolio)
- 085. [Προχωρημένα Εξουσιοδοτημένα Capstones](#προχωρημένα-εξουσιοδοτημένα-capstones)
- 110. [Advanced Authorized Labs II: Systems, Identity, Cloud και Application Security](#advanced-authorized-labs-ii-systems-identity-cloud-και-application-security)
- 115. [Master Capstones, Research Portfolio και Deep Security Practice](#master-capstones-research-portfolio-και-deep-security-practice)
- 140. [Advanced Authorized Labs III: Modern Protocols, Identity, Platforms και AI Security](#advanced-authorized-labs-iii-modern-protocols-identity-platforms-και-ai-security)

---

# Βάσεις Κυβερνοασφάλειας και Μεθοδολογία Ethical Hacking

Η κυβερνοασφάλεια είναι η προστασία συστημάτων, identities, λογισμικού, δικτύων και δεδομένων, χωρίς να εμποδίζεται η νόμιμη λειτουργία τους. Το ethical hacking είναι ένα μέρος αυτής της διαδικασίας: μια **εξουσιοδοτημένη** προσπάθεια να ελεγχθούν security assumptions και να παραχθούν αποδεικτικά στοιχεία που βοηθούν τον ιδιοκτήτη να μειώσει το risk.

> **Όριο εξουσιοδοτημένης χρήσης:** Κάνε πρακτικές δοκιμές μόνο σε συστήματα, accounts, εφαρμογές, δίκτυα ή συσκευές που σου ανήκουν ή για τα οποία έχεις ρητή άδεια. Για εκμάθηση προτίμησε localhost, disposable VMs/containers, emulators, synthetic accounts και intentionally vulnerable training apps.

## Μαθησιακοί στόχοι

Στο τέλος του μαθήματος πρέπει να μπορείς να:

- ξεχωρίζεις asset, threat, vulnerability, exposure, control και risk,
- εξηγείς confidentiality, integrity, availability, authenticity, accountability και resilience,
- ξεχωρίζεις authentication από authorization,
- περιγράφεις έναν σύγχρονο κύκλο security assessment,
- ορίζεις scope και απαιτούμενο evidence πριν από οποιοδήποτε test,
- εξηγείς γιατί remediation και retest είναι βασικά μέρη του ethical hacking.

## Βασικές ιδιότητες ασφάλειας

### Confidentiality — Εμπιστευτικότητα

Η confidentiality περιορίζει την πληροφορία μόνο σε εξουσιοδοτημένα subjects. Η κρυπτογράφηση μπορεί να προστατεύσει δεδομένα σε transit ή at rest, όμως η πραγματική εμπιστευτικότητα εξαρτάται επίσης από authorization, secret handling, logs, backups, exports και operational procedures.

### Integrity — Ακεραιότητα

Integrity σημαίνει ότι δεδομένα και system state παραμένουν σωστά και ότι μη εξουσιοδοτημένες αλλαγές αποτρέπονται ή ανιχνεύονται. Hashes, digital signatures, access control, transaction validation, version control, immutable logging και change management μπορούν να συμβάλουν στην ακεραιότητα.

### Availability — Διαθεσιμότητα

Availability σημαίνει ότι ο εξουσιοδοτημένος χρήστης μπορεί να χρησιμοποιήσει την υπηρεσία όταν τη χρειάζεται. Capacity, redundancy, backups, dependencies, rate limits, monitoring και recovery procedures επηρεάζουν άμεσα τη διαθεσιμότητα.

### Authenticity και accountability

Authenticity είναι η βεβαιότητα ότι identity, artifact ή message είναι αυτό που δηλώνει. Accountability σημαίνει ότι οι ενέργειες μπορούν να συνδεθούν με τον σωστό actor και να διερευνηθούν αργότερα. Ισχυρό authentication χωρίς σωστό authorization και audit evidence δεν αρκεί.

### Resilience — Ανθεκτικότητα

Ένα ασφαλές σύστημα δεν πρέπει να βασίζεται στην υπόθεση ότι η πρόληψη θα πετυχαίνει πάντα. Resilience σημαίνει detection, containment, recovery, restoration και lessons learned μετά από failure ή incident.

## Βασικό λεξιλόγιο

- **Asset:** κάτι που έχει αξία και πρέπει να προστατευτεί.
- **Threat:** κατάσταση ή actor που μπορεί να προκαλέσει ζημιά.
- **Vulnerability:** αδυναμία που μπορεί να παραβιάσει security property.
- **Exposure:** συνθήκη που κάνει μια αδυναμία reachable ή σημαντική.
- **Exploit:** τρόπος αξιοποίησης μιας vulnerability. Στο project χρησιμοποιείται μόνο σε ελεγχόμενα labs και για defensive understanding.
- **Control:** safeguard που προλαμβάνει, ανιχνεύει, περιορίζει ή βοηθά το recovery.
- **Risk:** συνδυασμός likelihood, impact, exposure, business context και uncertainty.
- **Attack surface:** interfaces, identities, inputs, services, dependencies και trust boundaries που μπορεί να γίνουν αντικείμενο abuse.
- **Trust boundary:** σημείο όπου data, identity, authority ή execution περνά μεταξύ components με διαφορετικές assumptions εμπιστοσύνης.

## Authentication και authorization

Authentication απαντά «ποιος παρουσιάζει αυτό το credential;». Authorization απαντά «επιτρέπεται αυτή η identity να κάνει αυτή την ενέργεια πάνω σε αυτό το resource;». Ένα σύστημα μπορεί να κάνει σωστά authentication και να είναι ευάλωτο επειδή λείπει object-level authorization ή επειδή χρησιμοποιείται stale state.

## Threat actors και κίνητρα

Η σωστή ανάλυση εστιάζει σε capabilities και goals αντί για στερεότυπα. Actors μπορεί να είναι οικονομικά υποκινούμενες ομάδες, insiders, state-linked groups, opportunistic attackers, hacktivists, fraud groups ή automated abuse. Ρώτησε τι access έχουν αρχικά, ποιος είναι ο στόχος τους, τι περιορισμούς έχουν και τι evidence θα άφηναν.

## Βασικά vulnerability management

Τα CVE δίνουν κοινά identifiers για δημοσιευμένες vulnerabilities. Vendor advisories και vulnerability databases προσθέτουν affected versions, fixes και context. Το CVSS είναι standardized severity framework αλλά **δεν είναι μόνο του risk decision**. Exposure, asset importance, compensating controls και business impact αλλάζουν την πραγματική προτεραιότητα.

Χρήσιμο workflow:

1. ταυτοποίησε asset και ακριβή version,
2. επιβεβαίωσε applicability,
3. έλεγξε exposure και required privileges,
4. κράτησε evidence με ελάχιστο impact,
5. κάνε prioritization με technical + business context,
6. εφάρμοσε remediation/mitigation,
7. κάνε retest και κατέγραψε το αποτέλεσμα.

## Σύγχρονος κύκλος ethical assessment

### 1. Authorization και scope

Κατέγραψε owner, systems, accounts, time window, allowed techniques, prohibited actions, data-handling rules, contacts και stop conditions. Το ότι κάτι είναι public στο Internet **δεν σημαίνει authorization**.

### 2. Discovery και modeling

Δημιούργησε inventory από assets, identities, interfaces, dependencies και trust boundaries. Ξεκίνα με passive/read-only evidence όπου γίνεται.

### 3. Validation

Έλεγξε security assumptions με τη λιγότερο παρεμβατική μέθοδο που απαντά την ερώτηση. Προτίμησε proof που αποδεικνύει τη weakness χωρίς περιττό impact.

### 4. Evidence και analysis

Κράτησε timestamps, versions, configuration, requests/responses, logs και το ακριβές condition που προκάλεσε το αποτέλεσμα. Ξεχώριζε observation από inference.

### 5. Remediation και retest

Εξήγησε root cause, control, residual risk και repeatable regression test. Ένα finding δεν ολοκληρώνεται μέχρι να μπορεί ο owner να αποδείξει ότι το fix άλλαξε το αποτέλεσμα.

### 6. Cleanup και reporting

Αφαίρεσε test accounts, temporary files και αλλαγές που δημιούργησε το assessment. **Μην διαγράφεις ή αλλοιώνεις security logs για να κρύψεις δραστηριότητα.**

## Καθοδηγούμενο εργαστήριο

Φτιάξε ένα μονοσέλιδο threat model για μια local εφαρμογή ή συσκευή που σου ανήκει. Σχεδίασε user, application, data store, network boundary και μία external dependency. Σημείωσε πού γίνεται authentication, πού authorization, ποια data είναι sensitive και ποια logs θα βοηθούσαν σε incident.

**Evidence:** διάγραμμα, τρεις security assumptions, τρία failure modes και ένα defensive test για κάθε failure mode.

## Συχνά λάθη

- Ξεκίνημα από tools πριν οριστεί security question.
- Θεώρηση scanner finding ως απόδειξη χωρίς verification.
- Σύγχυση severity με business risk.
- Σύγχυση encryption με authorization.
- Test εκτός scope επειδή το target είναι reachable.
- Αποθήκευση secrets/tokens σε lab notes.
- Θεώρηση του cleanup ως άδεια διαγραφής evidence.

## Έλεγχος γνώσεων

1. Δώσε παράδειγμα όπου authentication πετυχαίνει αλλά authorization αποτυγχάνει.
2. Ποια είναι η διαφορά vulnerability και risk;
3. Ποια τρία στοιχεία πρέπει να υπάρχουν στο scope;
4. Γιατί το retest είναι μέρος του assessment;
5. Τι evidence θα κρατούσες πριν αλλάξεις ένα security control;

## Καθοδηγούμενη μελέτη

Χρησιμοποίησε τη κοινή [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Ολοκλήρωσε το safe lab και βεβαιώσου ότι μπορείς να εξηγήσεις τον assessment lifecycle χωρίς να βασίζεσαι σε tool names.

### Συνέχεια

Προτεινόμενα επόμενα μαθήματα: **02, 05, 28, 51**.

---

# Footprinting, Reconnaissance και Ανακάλυψη Attack Surface

Reconnaissance είναι η διαδικασία δημιουργίας μιας ακριβούς εικόνας ενός **εξουσιοδοτημένου** target πριν από βαθύτερο testing. Το καλό reconnaissance είναι evidence-driven: ξεχωρίζει πληροφορίες που είναι δημόσια παρατηρήσιμες από πληροφορίες που αποκτώνται με άμεση αλληλεπίδραση και κρατά source/confidence για κάθε συμπέρασμα.

> **Όριο εξουσιοδοτημένης χρήσης:** Ακόμη και passive OSINT μπορεί να έχει privacy ή policy περιορισμούς. Active discovery πρέπει να παραμένει μέσα στο γραπτό scope. Για labs χρησιμοποίησε `example.com`, localhost ή δικό σου lab domain.

## Μαθησιακοί στόχοι

- ξεχώρισε passive, active, authenticated και internal discovery,
- δημιούργησε asset inventory από πολλαπλές πηγές,
- κατανόησε DNS, certificates, registration και web metadata,
- εντόπισε cloud/SaaS/repository exposure με ασφαλή τρόπο,
- κράτησε provenance και confidence,
- μετέτρεψε recon findings σε prioritized attack-surface map.

## Reconnaissance ως πρόβλημα inventory

Στόχος δεν είναι να συγκεντρώσεις όσες περισσότερες ονομασίες γίνεται. Στόχος είναι να ξέρεις ποια assets ανήκουν στον οργανισμό, ποια είναι Internet-facing, ποια identities τα διαχειρίζονται, ποιες technologies/dependencies χρησιμοποιούνται, ποια assets φαίνονται abandoned και ποια observations είναι confirmed ή μόνο hypotheses.

## Passive discovery

Παραδείγματα passive sources:

- public DNS και Certificate Transparency,
- registration και autonomous-system information,
- public repositories και package registries,
- websites, documentation, job postings και status pages,
- vendor advisories,
- public cloud/SaaS references που δημοσιεύτηκαν από τον owner.

Passive δεν σημαίνει unrestricted. Μην συλλέγεις προσωπικά δεδομένα που δεν χρειάζονται και μην προσπαθείς να αποκτήσεις private account content.

## DNS για reconnaissance

Χρήσιμα records:

- **A / AAAA:** IPv4/IPv6 addresses,
- **CNAME:** alias hostname,
- **MX:** mail exchangers,
- **NS:** authoritative name servers,
- **TXT:** SPF/DKIM/domain verification και άλλα metadata,
- **CAA:** policy για certificate authorities.

Ασφαλή examples:

```bash
nslookup example.com
dig example.com A
dig example.com AAAA
dig example.com MX
```

Ένα DNS answer είναι evidence για DNS state, όχι απόδειξη ownership ή vulnerability. Κατέγραψε resolver, timestamp, TTL και πιθανό caching/split-horizon context.

## Certificate και TLS metadata

Certificates μπορούν να αποκαλύψουν hostnames, issuer και validity periods. Certificate Transparency βοηθά στο discovery δημόσια εκδομένων ονομάτων, αλλά μια παλιά εγγραφή δεν αποδεικνύει ότι το hostname είναι ακόμη reachable ή ανήκει στην ίδια ομάδα.

## Web metadata

Σε authorized property, ασφαλή read-only observations είναι response status, redirect chain, TLS certificate, security headers, public `robots.txt`, `security.txt`, sitemaps, documented APIs και intentionally exposed metadata.

Μην μετατρέπεις reconnaissance σε uncontrolled content brute forcing. Αν directory enumeration είναι στο scope, κάν' το σε deliberately vulnerable ή locally hosted app με συμφωνημένο rate.

## Repositories και packages

Public repositories μπορεί να αποκαλύψουν architecture, dependencies, historical filenames, CI configuration και accidentally committed secrets. Αν βρεις suspected secret, **μην το δοκιμάσεις**. Ενημέρωσε τον owner μέσω του συμφωνημένου channel ώστε να γίνει rotation/revocation.

Για dependency research ξεχώρισε declared package από deployed package, direct από transitive dependency, package-name similarity από verified identity και CVE match από πραγματικά reachable vulnerable code.

## Cloud και SaaS surface

Cloud load balancers, object storage endpoints, IdP domains, SaaS tenants, support portals και development platforms μπορεί να φαίνονται δημόσια. Μην θεωρείς ownership μόνο από naming pattern. Επιβεβαίωσε με approved inventory, DNS/certificate relationships ή owner context.

## Provenance και confidence

Για κάθε asset κράτησε asset name, source, first-seen time, confidence, environment, owner, exposure και next minimal validation. Αυτό αποτρέπει το συχνό λάθος να θεωρείται stale search-engine data ως current truth.

## Active reconnaissance σε lab

Active recon αλληλεπιδρά άμεσα με service. Μπορεί να είναι DNS lookup, normal HTTP request, μικρό approved port check ή benign banner retrieval.

Local lab:

```bash
mkdir -p ~/hgp-lab/recon && cd ~/hgp-lab/recon
printf 'lab page\n' > index.html
python -m http.server 8000 --bind 127.0.0.1
```

Σε δεύτερο Termux session:

```bash
curl -I http://127.0.0.1:8000/
```

Σταμάτησε τον server όταν τελειώσεις.

## Attack-surface map

Ομαδοποίησε assets ανά trust boundary: Internet edge, identity, email, source control, CI/CD, cloud control plane, APIs, remote access, mobile backends, third-party integrations και monitoring/recovery.

Δώσε προτεραιότητα όπου συνδυάζονται υψηλό authority, sensitive data, broad exposure, αδύναμο ownership ή περιορισμένο observability.

## Συχνά λάθη

- Χρήση παλιών command examples πάνω σε public domains.
- Θεώρηση κάθε hostname ως in-scope asset.
- Θεώρηση fingerprint ως confirmed vulnerable version.
- Συλλογή άσχετων προσωπικών δεδομένων.
- Παράβλεψη IPv6 ή third-party identity surfaces.
- Findings χωρίς timestamp.

## Καθοδηγούμενο εργαστήριο

Φτιάξε attack-surface worksheet για fictional organization με website, API, IdP, code repository και cloud account. Για κάθε asset γράψε trust boundary, owner, evidence source, sensitive data και ένα minimal validation step.

## Έλεγχος γνώσεων

1. Γιατί το provenance είναι σημαντικό στο OSINT;
2. Ποια η διαφορά passive και active recon;
3. Γιατί certificate data μπορεί να είναι stale;
4. Τι κάνει ένα repository finding σημαντικό;
5. Πώς αποφεύγεις false ownership conclusions;

## Καθοδηγούμενη μελέτη

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Ολοκλήρωσε πρώτα το attack-surface worksheet.

### Συνέχεια

Προτεινόμενα μαθήματα: **03, 34, 35, 43**.

---

# Network Scanning και Service Discovery

Το network scanning απαντά συγκεκριμένες ερωτήσεις για hosts, ports, protocols και exposed services. Σε ethical assessment το scanning **δεν είναι άσκηση stealth**. Scope, rate, expected traffic, monitoring coordination και quality του evidence είναι πιο σημαντικά από την απόκρυψη.

> **Όριο εξουσιοδοτημένης χρήσης:** Σκάναρε μόνο addresses/services που περιλαμβάνονται ρητά στο scope. Για μάθηση χρησιμοποίησε localhost, host-only VM network, containers ή isolated lab όπως `192.168.56.0/24` που ελέγχεις.

## Μαθησιακοί στόχοι

- κατανόησε TCP/UDP discovery και limitations,
- ξεχώρισε open, closed και filtered observations,
- χρησιμοποίησε Nmap με ασφαλή τρόπο σε μικρό lab,
- κάνε service validation χωρίς υπερβολική εμπιστοσύνη σε banners,
- έλεγξε IPv4/IPv6 και firewall policy μαζί,
- συσχέτισε scanner output με packet και server-side evidence.

## Ξεκίνα από ερώτηση

Ένα scan πρέπει να απαντά κάτι συγκεκριμένο, π.χ. «ποιοι approved lab hosts εκθέτουν TCP/22 και TCP/443;». Μην κάνεις broad scan όταν ένα μικρό test αρκεί.

## TCP state

Το TCP είναι stateful. Συνήθως η σύνδεση αρχίζει με SYN, SYN/ACK και ACK. Open/closed/filtered περιγράφουν το **observation από τη θέση του scanner**, όχι μόνιμη ιδιότητα του target. Routing, firewall, source address, IPv4/IPv6 και time μπορούν να αλλάξουν το αποτέλεσμα.

## UDP state

UDP δεν έχει connection handshake. Silence μπορεί να σημαίνει open service, filtered traffic, εφαρμογή που αγνοεί το request ή packet loss. Χρειάζεται protocol-aware request ή server-side evidence για ισχυρό conclusion.

## Host discovery

ICMP echo είναι μόνο ένα signal. Ένα host μπορεί να blockάρει ping αλλά να έχει TCP service. Αντίστροφα, gateway/load balancer μπορεί να απαντά χωρίς να αποδεικνύει application health.

Σε δικό σου lab:

```bash
ping -c 2 192.168.56.10
nmap -sn 192.168.56.0/24
```

## Nmap basics

Χρησιμοποίησε την απλούστερη επιλογή που απαντά την ερώτηση:

```bash
nmap -sT -p 22,80,443 192.168.56.10
```

Για authorized version detection:

```bash
nmap -sT -sV -p 22,80,443 192.168.56.10
```

Το version result είναι hypothesis. Reverse proxies, custom banners και backported patches μπορεί να το κάνουν λάθος.

## Rate και reliability

Πολύ γρήγορο scan μπορεί να προκαλέσει packet loss, rate limiting ή misleading results. Κατέγραψε timing και retry behavior όταν η ακρίβεια έχει σημασία.

## Firewalls και detection validation

Μην χρησιμοποιείς scanning options με σκοπό να παρακάμψεις monitoring. Σε control validation συνεργάσου με defenders και έλεγξε αν το approved traffic έγινε log, correlation και alert.

Κράτα evidence από scanner timestamp/source, target response, firewall decision, host/application log και SIEM/EDR/network telemetry όπου υπάρχει.

## IPv6 parity

Service μπορεί να είναι blocked σε IPv4 αλλά reachable σε IPv6. Έλεγξε listening sockets, AAAA records, firewall/cloud rules και monitoring coverage και για τα δύο protocol families.

## Service validation

Μετά από open port ρώτησε:

1. Ποιο protocol περιμένουμε;
2. Χρειάζεται TLS;
3. Ποιο identity/authorization boundary το προστατεύει;
4. Επιτρέπεται να είναι reachable από αυτό το segment;
5. Ποιο evidence επιβεβαιώνει application/version;

Το port number είναι convention, όχι identity.

## Συχνά λάθη

- Scan εκτός approved CIDR.
- Broad port range χωρίς λόγο.
- Θεώρηση blocked ICMP ως offline host.
- Θεώρηση version fingerprint ως βέβαιο.
- Παράβλεψη IPv6.
- Προσπάθεια παράκαμψης της παρακολούθησης αντί ελέγχου της κάλυψης των IDS/IPS.
- Μη συσχέτιση scan timestamps με defensive telemetry.

## Καθοδηγούμενο εργαστήριο

Φτιάξε δύο local services σε VM/container, ένα running και ένα stopped. Κάνε scan μόνο στα αντίστοιχα ports, πρόβλεψε το αποτέλεσμα, άλλαξε μία firewall/service setting και επανάλαβε. Εξήγησε **γιατί** άλλαξε το observation.

## Έλεγχος γνώσεων

1. Γιατί UDP scanning είναι ambiguous;
2. Τι περιγράφει το “filtered”;
3. Γιατί ένα banner μπορεί να είναι misleading;
4. Ποιο evidence συνοδεύει detection validation;
5. Γιατί χρειάζεται ξεχωριστός IPv6 έλεγχος;

## Καθοδηγούμενη μελέτη

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Στόχος είναι να εξηγείς result από protocol behavior και policy, όχι από απομνημονευμένα switches.

### Συνέχεια

Προτεινόμενα μαθήματα: **04, 05, 12, 51**.

---

# Service Enumeration και Protocol-Aware Validation

Enumeration σημαίνει ότι προχωράς από το «υπάρχει service» σε δομημένη κατανόηση protocol behavior, identities, configuration και exposed metadata. Στόχος δεν είναι να εξάγεις όσο περισσότερη πληροφορία γίνεται αλλά να συλλέγεις το ελάχιστο evidence που απαιτείται για ένα authorized security question.

> **Όριο εξουσιοδοτημένης χρήσης:** Κάνε enumeration μόνο σε services/accounts μέσα στο scope. Χρησιμοποίησε lab accounts και synthetic data. Μην κάνεις password guessing, user harvesting ή sensitive-data extraction χωρίς συγκεκριμένη άδεια.

## Scanning εναντίον enumeration

Scanning συνήθως απαντά αν host/service είναι reachable. Enumeration απαντά τι εκθέτει και πώς συμπεριφέρεται. TCP/443 open είναι scan result· certificate, reverse proxy behavior, authentication flow και authorization policy είναι enumeration evidence.

## HTTP/HTTPS

Ξεκίνα με normal request:

```bash
curl -I http://127.0.0.1:8000/
```

Κατέγραψε status, redirects, headers και expected exposure. Για TLS κράτησε certificate/hostname validation. Μην θεωρείς το `Server` header definitive product/version evidence.

## SSH

Σε SSH assessment έλεγξε αν πρέπει να είναι reachable, ποια authentication methods επιτρέπονται, αν privileged accounts μπορούν να κάνουν direct login, ποια host keys/algorithms χρησιμοποιούνται και αν τα access decisions γίνονται log. Μην μετατρέπεις enumeration σε credential attack.

## DNS

DNS enumeration μπορεί να δείξει address records, mail routing, NS relationships και security records. Zone-transfer tests γίνονται μόνο σε δικό σου authoritative lab server ή όταν υπάρχει ρητή άδεια.

## SMB και file shares

Χρησιμοποίησε account που δημιουργήθηκε για το assessment. Έλεγξε guest/anonymous access, share permissions και expected policy. Readable share δεν είναι αυτόματα vulnerability αν είναι σχεδιασμένο να είναι public.

## SNMP

SNMP μπορεί να εκθέσει operational/inventory data. Προτίμησε authenticated/encrypted configurations όπου υποστηρίζονται. Μην brute-forceάρεις community strings· χρησιμοποίησε supplied lab credential ή local configuration review.

## LDAP και directories

Κατέγραψε bind identity, search base, returned attributes και αν εκτίθενται unnecessary sensitive attributes. Για Active Directory συνέχισε στα Modules 32 και 72.

## Fingerprints ως hypotheses

Banners, headers και protocol negotiation δίνουν ενδείξεις. Backported fixes και intermediaries μπορούν να αλλάξουν το πραγματικό state. Για σημαντικό finding επιβεβαίωσε με inventory, package data, authenticated management information ή owner evidence.

## Authorization matrix

Χρήσιμο μοντέλο:

| Identity | Resource | Read | Write | Admin | Expected? |
|---|---|---:|---:|---:|---|
| anonymous | public share | yes | no | no | yes |
| test-user | team share | yes | no | no | yes |
| test-admin | team share | yes | yes | yes | yes |

Έλεγξε μόνο τα rows που χρειάζονται για να αποδείξεις την policy.

## Συχνά λάθη

- Αναφορά anonymous access χωρίς expected policy.
- Credential guessing αντί approved accounts.
- Απόλυτη εμπιστοσύνη σε banners.
- Συλλογή περισσότερων data από όσα απαιτεί ο στόχος.
- Result χωρίς identity context.
- Παράβλεψη server-side logs.

## Καθοδηγούμενο εργαστήριο

Σε VM/container δικό σου, expose ένα HTTP service και ένα authenticated service. Φτιάξε δύο identities με διαφορετικά permissions, δημιούργησε authorization matrix και κράτησε server-side evidence για allowed/denied actions.

## Έλεγχος γνώσεων

1. Τι διαφορά έχει enumeration από scanning;
2. Γιατί κάθε result πρέπει να αναφέρει identity;
3. Γιατί banner-based versioning δεν αρκεί;
4. Πώς βοηθά authorization matrix;
5. Πότε ένα SNMP/SMB observation γίνεται security finding;

## Καθοδηγούμενη μελέτη

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Εστίασε σε evidence, identity context και expected policy.

### Συνέχεια

Προτεινόμενα μαθήματα: **05, 13, 32, 33**.

---

# Vulnerability Analysis και Prioritization

Vulnerability analysis εξετάζει αν μια weakness εφαρμόζεται σε πραγματικό asset, ποια security property μπορεί να επηρεάσει και τι πρέπει να γίνει. Scanner output ή CVE match είναι η αρχή της ανάλυσης, όχι το τελικό conclusion.

> **Όριο εξουσιοδοτημένης χρήσης:** Κάνε validation με τη λιγότερο intrusive μέθοδο που απαντά την ερώτηση. Προτίμησε vendor information, package/version evidence, configuration review, safe requests και isolated lab reproduction.

## CVE, CWE και advisories

**CVE** δίνει κοινό identifier σε disclosed vulnerability. **CWE** περιγράφει weakness classes όπως improper authorization, unsafe input handling ή memory-safety defects. Vendor/upstream advisories συνήθως είναι η καλύτερη πηγή για affected versions, patches, workarounds και prerequisites.

## CVSS και πραγματικό risk

CVSS δίνει standardized technical severity. Δεν ξέρει όμως αν το service είναι Internet-facing, αν το affected feature είναι disabled, ποια data περιέχει το asset, ποια compensating controls υπάρχουν ή ποιο business process επηρεάζεται.

Practical priority = severity + applicability + exposure + privileges + asset criticality + data sensitivity + controls + detection/recovery + operational context.

## Applicability analysis

Πριν κάνεις finding, απάντησε:

1. Είναι εγκατεστημένο το affected product/component;
2. Είναι η πραγματική version affected;
3. Είναι το vulnerable feature enabled/reachable;
4. Ποιες privileges/user interaction χρειάζονται;
5. Υπάρχει backported fix;
6. Αλλάζει ουσιαστικά το exploitability κάποιο sandbox, proxy ή isolation control;

## Safe validation ladder

1. Inventory evidence.
2. Configuration evidence.
3. Benign protocol evidence.
4. Local reproduction σε intentionally vulnerable sample.
5. Intrusive validation μόνο αν είναι ρητά approved και απαραίτητο.

Σταμάτα μόλις απαντηθεί το security question.

## Καλό finding

Πρέπει να περιέχει affected asset/component, timestamped evidence, root cause ή vulnerability reference, realistic impact, prerequisites, limitations, severity rationale, remediation και retest procedure.

Μην χρησιμοποιείς δραματική γλώσσα. Γράψε τι αποδείχθηκε και τι παραμένει uncertain.

## Remediation

Μπορεί να είναι patch/upgrade, disable unused feature, exposure reduction, stronger authorization, segmentation, credential rotation, detection ή documented risk acceptance. Workaround δεν είναι πάντα ισοδύναμο με patch· κατέγραψε residual risk.

## Συχνά λάθη

- Κάθε scanner match θεωρείται confirmed vulnerability.
- CVSS ως μοναδικό prioritization input.
- Άγνωστο ακριβές component/version.
- PoC όταν configuration evidence αρκεί.
- Παράβλεψη compensating controls.
- Remediation χωρίς regression test.

## Καθοδηγούμενο εργαστήριο

Δημιούργησε τρία fictional assets: Internet-facing web service, internal workstation και isolated dev container. Δώσε και στα τρία την ίδια hypothetical high-severity library vulnerability και γράψε διαφορετικό priority για το καθένα με βάση exposure, data, privilege και recovery context.

## Έλεγχος γνώσεων

1. Γιατί CVE match δεν είναι αυτόματα finding;
2. Τι προσφέρει το CWE;
3. Τι δεν γνωρίζει το CVSS για το περιβάλλον σου;
4. Πότε αποφεύγεις intrusive validation;
5. Τι κάνει ένα retest criterion reproducible;

## Καθοδηγούμενη μελέτη

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Εξασκήσου στο να εξηγείς γιατί το ίδιο CVE έχει διαφορετικό risk σε διαφορετικά assets.

### Συνέχεια

Προτεινόμενα μαθήματα: **15, 26, 50, 84**.

---

# Host Security Assessment και System Hardening

Το host security assessment εξετάζει πώς ένα λειτουργικό προστατεύει identities, privileges, processes, services, files, secrets, persistence mechanisms και telemetry. Στόχος είναι να βρεις αδύναμα trust boundaries και να τα hardenάρεις — όχι να κρύψεις activity ή να καταστρέψεις evidence.

> **Όριο εξουσιοδοτημένης χρήσης:** Κάνε host testing μόνο σε systems που διαχειρίζεσαι ή έχεις ρητή άδεια. Μην εγκαθιστάς persistence, credential stealers, keyloggers, hidden backdoors ή anti-forensics mechanisms. Χρησιμοποίησε harmless test accounts και disposable VMs.

## Identities και local accounts

Φτιάξε inventory από human users, service accounts, groups, administrative roles και authentication methods. Κάθε identity πρέπει να έχει current owner και business purpose.

Έλεγξε stale accounts, shared admin credentials, unnecessary direct root/admin use, service accounts με interactive login και privileges που δεν ταιριάζουν πλέον στον ρόλο.

## Privilege boundaries

Privilege-escalation risk υπάρχει όταν λιγότερο trusted identity μπορεί να επηρεάσει κάτι που εκτελείται με περισσότερη authority. Παραδείγματα:

- writable service binaries/startup scripts,
- unsafe search paths/environment variables,
- overly permissive scheduled jobs,
- dangerous delegated rights,
- weak ACLs,
- unnecessary Linux capabilities/setuid programs,
- services με υπερβολικά privileges.

Σε assessment προτίμησε permission/configuration review αντί exploitation. Αν χρειάζεται proof, χρησιμοποίησε harmless marker σε disposable lab.

## Services και software inventory

Για κάθε service κατέγραψε owner, purpose, network exposure, execution identity, config, update source και logs. Services χωρίς operational purpose πρέπει να απενεργοποιούνται/αφαιρούνται, όχι απλώς να κρύβονται πίσω από ένα firewall rule.

## Secrets

Credentials μπορεί να υπάρχουν σε config files, environment variables, shell history, CI files, repositories, password managers, OS credential stores και process memory. Το security review πρέπει να μειώνει secret lifetime και access — όχι να κάνει dump πραγματικών credentials.

Αν βρεθεί πραγματικό secret, σταμάτα unnecessary handling και ζήτησε rotation/revocation.

## Persistence ως defensive concept

Defenders πρέπει να baselineάρουν services, scheduled tasks, startup items, extensions και άλλα autorun mechanisms. Σε lab δημιούργησε μόνο benign scheduled action, π.χ. timestamp σε temp file, έλεγξε telemetry και μετά αφαίρεσέ το.

## Logging και anti-forensics detection

Security logs είναι evidence. **Μην τα καθαρίζεις, truncateάρεις, falsify ή disable για απόκρυψη testing.** Αντίθετα:

- forward critical logs off-host,
- περιόρισε ποιος αλλάζει audit configuration,
- alert σε log deletion/truncation ή audit-service changes,
- κράτησε σωστό time synchronization,
- προστάτεψε integrity/retention.

## File/permission review

Σε Linux έλεγξε ownership και mode bits. Σε Windows έλεγξε ACLs/inheritance. Εστίασε σε service config, executable directories, scheduled tasks, sensitive data και key material. Μην «διορθώνεις» προβλήματα με broad recursive permissions.

## Hardening baseline

Περιλαμβάνει supported OS/patch state, disk encryption, host firewall, endpoint telemetry, secure boot όπου υπάρχει, account policy, exposed services, backups/recovery, time sync και configuration-management source of truth.

## Assessment workflow

1. Κατέγραψε system/version και scope.
2. Πάρε read-only inventory.
3. Χαρτογράφησε privileged identities και execution boundaries.
4. Βρες user-controlled inputs προς privileged components.
5. Έλεγξε μία hypothesis τη φορά με harmless action.
6. Συσχέτισε logs, endpoint telemetry και config.
7. Restore baseline και κάνε retest.

## Συχνά λάθη

- Θεώρηση admin access ως μοναδικού στόχου.
- Credential-dumping tools όταν config evidence αρκεί.
- Backdoors/stealth σε learning environment.
- Διαγραφή logs στο cleanup.
- Παράβλεψη service accounts.
- Hardening χωρίς rollback plan.

## Καθοδηγούμενο εργαστήριο

Σε disposable VM φτιάξε standard user και administrator. Δημιούργησε directory μόνο για admin και ένα shared directory. Έλεγξε permissions, δημιούργησε benign scheduled task/service με σωστή identity, παράγαγε normal event και επιβεβαίωσε ότι έγινε log. Αφαίρεσε τα test objects και κράτησε before/after evidence.

## Έλεγχος γνώσεων

1. Πότε writable file γίνεται privilege concern;
2. Γιατί centralized logging είναι σημαντικό;
3. Πώς μελετάς persistence χωρίς backdoor;
4. Authentication vs authorization weakness σε host;
5. Γιατί κάθε hardening change χρειάζεται rollback;

## Καθοδηγούμενη μελέτη

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Στόχος είναι να εντοπίσεις privilege boundary, να το hardenάρεις και να αποδείξεις με retest ότι άλλαξε το αποτέλεσμα.

### Συνέχεια

Προτεινόμενα μαθήματα: **12, 32, 33, 73, 74**.

---

# Malware: Έννοιες, Analysis και Defensive Triage

Malware είναι code/software που χρησιμοποιείται σκόπιμα για παραβίαση security property: κλοπή δεδομένων, disruption, unauthorized control, persistence, spying, encryption ή abuse πόρων. Ο security analyst πρέπει να κατανοεί behavior χωρίς να αναπτύσσει ή να διανέμει harmful code.

> **Όριο εξουσιοδοτημένης χρήσης:** Ανάλυσε samples μόνο σε isolated environment που ελέγχεις και μόνο όταν επιτρέπεται να τα κατέχεις. Για μάθηση προτίμησε harmless training samples, prerecorded telemetry ή benign binaries.

## Malware categories

Trojan, worm, ransomware, spyware, downloader, bot, rootkit, wiper, cryptominer και infostealer είναι labels. Ένα πραγματικό sample μπορεί να συνδυάζει πολλές συμπεριφορές, άρα κατέγραψε **τι κάνει** και όχι μόνο το family name.

## Initial triage

Πριν από execution κράτησε hash, file type/architecture, digital-signature status, size/timestamps, safe printable strings, imports/libraries και chain of custody.

Μην ανεβάζεις confidential samples/documents σε public analysis services χωρίς policy approval.

## Static analysis

Static analysis εξετάζει το αρχείο χωρίς να το τρέχει: executable format, imports, strings, resources, metadata και code structure. Packing/obfuscation μειώνουν visibility· απουσία obvious strings δεν σημαίνει safe binary.

## Behavioral analysis

Σε controlled sandbox παρατήρησε process tree, files, registry/config changes, services/tasks, DNS/network destinations, loaded libraries, privilege events και IPC objects.

Για learning lab χρησιμοποίησε harmless program που δημιουργεί temp file, child process και local request. Στόχος είναι telemetry understanding, όχι malware behavior reproduction.

## Persistence και privilege

Persistence σημαίνει επανεκτέλεση αργότερα. Privilege σημαίνει διαθέσιμη authority. Είναι διαφορετικά concepts. Defenders πρέπει να baseline services, scheduled tasks, startup items, extensions και να ερευνούν unexpected changes.

## Command-and-control concepts

Remote malware χρειάζεται κάποιο communication path. Defenders αναλύουν destination, DNS/certificate metadata, timing, beacon regularity, process ownership και host/network correlation. Για labs χρησιμοποίησε localhost ή prerecorded PCAPs, όχι real C2 infrastructure.

## Ransomware

Ransomware resilience βασίζεται σε least privilege, segmentation, protected backups, restoration tests, detection και incident response. Μην δοκιμάζεις encryption/destructive payloads πάνω σε πραγματικά data.

## IOC και behavior

IOC μπορεί να είναι hash, domain, filename ή path. Αλλάζει εύκολα. Behavioral detection συχνά είναι πιο ανθεκτικό, επειδή περιγράφει σχέση ενεργειών, π.χ. unexpected process που αλλάζει startup location.

## Containment και recovery

1. Validate alert και preserve evidence.
2. Isolate affected systems όπου χρειάζεται.
3. Εντόπισε impacted identities/secrets.
4. Σταμάτησε propagation χωρίς να χάσεις visibility.
5. Eradicate root cause.
6. Restore από trusted source.
7. Rotate credentials/keys.
8. Monitor recurrence.
9. Κατέγραψε lessons learned.

## Συχνά λάθη

- Unknown sample σε προσωπική συσκευή.
- Disable security controls για να «τρέξει» το sample.
- Ένα antivirus label ως πλήρης analysis.
- Μόνο hashes χωρίς behavior.
- Upload confidential sample σε public service.
- Restore χωρίς διόρθωση initial access.

## Καθοδηγούμενο εργαστήριο

Γράψε benign script που δημιουργεί temporary file, ξεκινά harmless child process και γράφει ένα log event. Παρατήρησε process tree/filesystem και εξήγησε ποιο telemetry ξεχωρίζει αυτή τη δραστηριότητα από normal software.

## Έλεγχος γνώσεων

1. Γιατί family label δεν αρκεί;
2. IOC vs behavioral detection;
3. Γιατί static + behavioral analysis μαζί;
4. Τι evidence πριν από execution;
5. Γιατί restore μόνο του δεν αρκεί μετά από ransomware;

## Καθοδηγούμενη μελέτη

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Όλη η πρακτική εργασία παραμένει harmless και isolated.

### Συνέχεια

Προτεινόμενα μαθήματα: **23, 37, 67, 79, 81**.

---

# Packet Capture, Sniffing και Network Visibility

Packet capture δίνει άμεσο evidence για επικοινωνία μεταξύ systems. Είναι χρήσιμο για troubleshooting, incident response και protocol analysis, αλλά ένα PCAP μπορεί να περιέχει credentials, tokens, προσωπικά δεδομένα και confidential information.

> **Όριο εξουσιοδοτημένης χρήσης:** Κάνε capture μόνο σε interfaces/networks που σου ανήκουν ή έχεις ρητή άδεια να monitorάρεις. Προτίμησε localhost/VM lab ή prerecorded captures. Μην interceptάρεις traffic τρίτων.

## Τι αποδεικνύει ένα capture

Αποδεικνύει τι είδε το συγκεκριμένο capture point. Δεν αποδεικνύει απαραίτητα τι συνέβη σε άλλο σημείο. Packets μπορεί να χαθούν, να αλλάξουν από proxy/NAT, να είναι encrypted ή να μην παρατηρούνται λόγω offload.

Κατέγραψε interface/location, timestamps, filter, relevant IP/ports, θέση σε σχέση με NAT/proxy και πιθανό packet loss.

## Protocol layers

Χρήσιμη σειρά:

1. Link layer — MAC/VLAN/frame type.
2. IP — IPv4/IPv6, TTL/hop limit, fragmentation.
3. Transport — TCP state ή UDP datagrams.
4. DNS/ICMP/control traffic.
5. TLS/certificate/protocol negotiation.
6. Application layer μόνο όταν legitimately observable.

Encryption μπορεί να κρύβει payload αλλά να αφήνει useful metadata για endpoints, timing, volume και protocol negotiation.

## Switched networks

Σε normal switched Ethernet ένας host δεν βλέπει αυτόματα όλο το unicast traffic. Defenders χρησιμοποιούν approved SPAN/TAP, gateway sensors, host agents ή cloud traffic mirroring. Μην χρησιμοποιείς poisoning/interception πάνω σε shared network για να «δεις περισσότερα».

## Filters

Capture filter περιορίζει τι αποθηκεύεται. Display filter περιορίζει τι εμφανίζεται μετά. Πολύ narrow capture μπορεί να χάσει context· πολύ broad capture μπορεί να συλλέξει unnecessary sensitive data.

Safe localhost example:

```bash
tcpdump -i lo tcp port 8000
```

Παράγαγε μόνο δικό σου local request και σταμάτησε αμέσως μετά.

## TCP, DNS και TLS evidence

Σε TCP παρατήρησε handshake, sequence behavior, retransmissions, resets και teardown. Retransmission δεν είναι αυτόματα attack.

Σε DNS παρατήρησε queried names, resolver, response codes και TTL. Encrypted DNS μεταφέρει visibility σε endpoint/resolver logs.

Σε TLS μπορείς να δεις protocol/certificate metadata και connection relationships χωρίς να αποδυναμώνεις production encryption.

## PCAP handling

PCAP μπορεί να έχει cleartext passwords από legacy protocols, bearer tokens, cookies, email content ή internal hostnames. Χρησιμοποίησε access controls, minimum retention και sanitized extracts στα reports.

## Συχνά λάθη

- Capture χωρίς γνώση του position στο network path.
- Absence of packet = «δεν έγινε event».
- Τεράστια captures με άσχετα sensitive data.
- Retransmission/reset ως attack χωρίς context.
- Disable TLS για visibility.
- Capture third-party traffic.

## Καθοδηγούμενο εργαστήριο

Ξεκίνα localhost HTTP server, capture μόνο TCP/8000 στο loopback, κάνε δύο requests και σταμάτησε. Εντόπισε setup, request/response και teardown και σύγκρινε timeline με server access log.

## Έλεγχος γνώσεων

1. Τι αποδεικνύει ένα capture;
2. Γιατί έχει σημασία το capture location;
3. Capture filter vs display filter;
4. Τι metadata μένει χρήσιμο με TLS;
5. Ποια privacy risks έχει ένα PCAP;

## Καθοδηγούμενη μελέτη

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Κάθε conclusion να βασίζεται σε packet evidence και τουλάχιστον μία δεύτερη πηγή.

### Συνέχεια

Προτεινόμενα μαθήματα: **12, 23, 51, 77**.

---

# Άμυνα απέναντι στην Κοινωνική Μηχανική και Ασφάλεια Ανθρώπινου Παράγοντα

Η κοινωνική μηχανική εκμεταλλεύεται εμπιστοσύνη, βιασύνη, φόβο, εξουσία και καθημερινές επιχειρησιακές διαδικασίες. Η σωστή άμυνα δεν βασίζεται στην ιδέα ότι «ο χρήστης πρέπει απλώς να προσέχει περισσότερο». Στόχος είναι να σχεδιάζονται διαδικασίες και τεχνικοί έλεγχοι που παραμένουν ασφαλείς ακόμη και όταν ένας άνθρωπος κάνει λάθος.

> **Όριο εξουσιοδότησης:** Μην εξαπατάς πραγματικά άτομα, μην συλλέγεις πραγματικούς κωδικούς και μην εκτελείς phishing, vishing ή φυσικές προσομοιώσεις χωρίς ρητή γραπτή άδεια, καθορισμένο scope, κανόνες διαχείρισης δεδομένων και σαφή διαδικασία διακοπής.

## Μαθησιακοί στόχοι

- Να αναγνωρίζεις μοτίβα πίεσης, πλαστοπροσωπίας και κατάχρησης διαδικασιών.
- Να κατανοείς γιατί η κοινωνική μηχανική είναι πρόβλημα συστήματος και όχι μόνο ανθρώπου.
- Να αξιολογείς phishing, BEC, help-desk recovery και φυσικά σενάρια.
- Να σχεδιάζεις ασφαλείς και δεοντολογικές προσομοιώσεις.
- Να μετράς ανθεκτικότητα χωρίς περιττή συλλογή προσωπικών δεδομένων.

## Μοτίβα επιρροής

Συχνά χρησιμοποιούνται **επείγον**, **εξουσία**, **φόβος**, **ανταμοιβή**, οικεία εταιρική εμφάνιση ή πίεση να παρακαμφθεί μια κανονική διαδικασία. Η σημαντική ερώτηση δεν είναι μόνο «είναι ύποπτο το μήνυμα;», αλλά «ποια δικλείδα ασφαλείας εμποδίζει μια λανθασμένη ενέργεια να γίνει περιστατικό;».

## Phishing-resistant έλεγχοι

Ισχυρότερη άμυνα προσφέρουν passkeys ή security keys όπου υποστηρίζονται, password managers που συσχετίζουν credentials με το σωστό origin, email filtering/authentication, least privilege και ανεξάρτητη επιβεβαίωση για κρίσιμες αλλαγές. Για πληρωμές, αλλαγές IBAN, payroll ή ανάκτηση λογαριασμού, η επιβεβαίωση πρέπει να γίνεται από κανάλι που δεν παρέχεται μέσα στο ύποπτο μήνυμα.

## Business Email Compromise

Το BEC στοχεύει κυρίως διαδικασίες: αλλαγή τραπεζικών στοιχείων προμηθευτή, επείγουσα μεταφορά χρημάτων, αλλαγή μισθοδοσίας ή πλαστοπροσωπία στελέχους. Η άμυνα πρέπει να συνδυάζει τεχνικούς ελέγχους με separation of duties, δεύτερη έγκριση και γνωστό ανεξάρτητο κανάλι επιβεβαίωσης.

## Help desk και account recovery

Η διαδικασία ανάκτησης μπορεί να ακυρώσει ένα ισχυρό MFA. Έλεγξε ποια στοιχεία αποδέχεται το support, ποιος μπορεί να επαναφέρει έναν λογαριασμό, αν η αλλαγή καταγράφεται, αν ειδοποιείται ο πραγματικός χρήστης και αν απαιτείται πρόσθετη έγκριση για κρίσιμες ταυτότητες.

## Φυσική ασφάλεια και αφαιρούμενα μέσα

Tailgating, badges, επισκέπτες, ξεκλείδωτες συσκευές, εκτυπώσεις και USB μπορούν να δημιουργήσουν κίνδυνο. Οι δοκιμές δεν πρέπει να προκαλούν φόβο, κίνδυνο, ζημιά ή συλλογή άσχετων πληροφοριών.

## Σχεδιασμός ηθικής προσομοίωσης

Καθόρισε στόχο, εγκεκριμένο πληθυσμό, ημερομηνίες, stop conditions, απαγορευμένα pretexts, ποια δεδομένα συλλέγονται, ποιος τα βλέπει και πώς θα δοθεί ανατροφοδότηση. Προτίμησε προσομοιώσεις που δεν ζητούν ποτέ πραγματικό password.

## Χρήσιμες μετρήσεις

Πιο χρήσιμα από ένα απλό click rate είναι: χρόνος μέχρι την αναφορά, ποσοστό ανεξάρτητης επιβεβαίωσης κρίσιμων αιτημάτων, χρόνος περιορισμού περιστατικού, συμμόρφωση του help desk και αν τεχνικοί έλεγχοι απέτρεψαν χρήση credentials.

## Συνηθισμένα λάθη

- Επίρριψη ευθύνης μόνο στους χρήστες.
- Προσομοίωση χωρίς κατάλληλη έγκριση.
- Συλλογή πραγματικών passwords.
- Χρήση τραυματικών ή πολύ ευαίσθητων σεναρίων.
- Μέτρηση μόνο clicks.
- Δύσκολη διαδικασία αναφοράς ύποπτου μηνύματος.

## Καθοδηγούμενο εργαστήριο

Δημιούργησε πέντε εντελώς φανταστικά μηνύματα: νόμιμο invoice, επείγουσα ψεύτικη πληρωμή, password-reset lure, collaboration invite και help-desk request. Για κάθε ένα κατέγραψε ενδείξεις, ασφαλή τρόπο επιβεβαίωσης και έλεγχο που μειώνει τον κίνδυνο ακόμη κι αν ο χρήστης κάνει λάθος.

## Έλεγχος γνώσεων

1. Γιατί η κοινωνική μηχανική είναι και πρόβλημα σχεδιασμού διαδικασιών;
2. Τι κάνει ένα verification channel ανεξάρτητο;
3. Πώς μπορεί το account recovery να αποδυναμώσει το MFA;
4. Ποιες μετρήσεις είναι καλύτερες από το click rate;
5. Τι πρέπει να έχει εγκριθεί πριν από μια προσομοίωση;

## Καθοδηγούμενη μελέτη

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Όλα τα παραδείγματα πρέπει να είναι φανταστικά ή ρητά εγκεκριμένα και ο στόχος να είναι η βελτίωση διαδικασιών.

### Συνέχισε με

Προτεινόμενα επόμενα modules: **42, 43, 57, 60, 131**.

---

# Ανθεκτικότητα σε Denial-of-Service και Έλεγχος Εξάντλησης Πόρων

Denial of Service (DoS) είναι κάθε κατάσταση όπου νόμιμοι χρήστες δεν μπορούν να λάβουν την απαιτούμενη υπηρεσία. Αιτία μπορεί να είναι κακόβουλη κίνηση, bug, dependency failure, υπερφόρτωση ουρών, CPU/memory pressure, storage exhaustion ή λανθασμένη ρύθμιση. Η αμυντική προσέγγιση είναι resilience engineering και ελεγχόμενο capacity testing, όχι flooding τρίτων συστημάτων.

> **Όριο εξουσιοδότησης:** Μην παράγεις μεγάλο ή διαταρακτικό traffic προς δημόσια ή κοινόχρηστα συστήματα. Load/resource tests γίνονται μόνο σε απομονωμένο περιβάλλον με σαφή όρια, monitoring, stop conditions και άδεια ιδιοκτήτη.

## Μαθησιακοί στόχοι

- Να εντοπίζεις bottlenecks σε CPU, memory, connections, threads, queues, disk και dependencies.
- Να ξεχωρίζεις volumetric, protocol και application-layer resource exhaustion.
- Να κατανοείς rate limits, quotas, backpressure, timeouts και circuit breakers.
- Να σχεδιάζεις ασφαλή capacity tests και recovery.

## Η διαθεσιμότητα ως ιδιότητα ολόκληρου συστήματος

Ένα frontend μπορεί να φαίνεται υγιές ενώ έχει εξαντληθεί το database connection pool. Ένα API μπορεί να απαντά γρήγορα ενώ ένα asynchronous queue μεγαλώνει χωρίς όριο. Χαρτογράφησε όλη τη διαδρομή ενός request και κατέγραψε κάθε πεπερασμένο resource.

## Κατηγορίες εξάντλησης

### Υπολογιστική ισχύς

Ακριβά regex, parsing, compression, cryptography, image processing ή algorithms χωρίς όρια μπορούν να εξαντλήσουν CPU.

### Μνήμη

Unbounded request bodies, caches, queues, decompression ή υπερβολικά sessions μπορούν να οδηγήσουν σε memory pressure ή OOM.

### Connections και file descriptors

Sockets, workers και connection pools είναι πεπερασμένα. Ακόμη και χαμηλού bandwidth clients μπορούν να κρατήσουν resources δεσμευμένα για μεγάλο διάστημα.

### Storage και logs

Μεγάλα uploads, temporary files, database growth ή υπερβολικό logging μπορούν να γεμίσουν storage. Ένας αμυντικός μηχανισμός που καταγράφει υπερβολικά πολλά δεδομένα μπορεί να δημιουργήσει ο ίδιος DoS.

### Dependencies

DNS, IdP, databases, third-party APIs και queues μπορούν να καθυστερήσουν ή να αποτύχουν. Timeouts, retry budgets και jitter καθορίζουν αν το πρόβλημα θα παραμείνει τοπικό ή θα εξελιχθεί σε cascading failure.

## Αμυντικοί έλεγχοι

Χρησιμοποίησε quotas ανά identity/resource, bounded body sizes, connection/execution timeouts, queue limits, backpressure, circuit breakers, caching όπου είναι ασφαλές, graceful degradation και monitoring για saturation/latency/errors. Τα rate limits πρέπει να επιλέγουν σωστό key· ένα μόνο source IP μπορεί να αντιπροσωπεύει πολλούς νόμιμους χρήστες πίσω από NAT.

## Ασφαλές load testing

Ξεκίνα από baseline. Αύξησε σταδιακά κανονικό traffic μέσα σε προκαθορισμένο μέγιστο rate/concurrency και παρακολούθησε CPU, memory, latency, errors, connections και queue depth. Όρισε αυτόματο stop threshold και σχέδιο rollback. Στόχος είναι να εντοπίσεις πού αρχίζει η υποβάθμιση και αν τα controls λειτουργούν.

## Detection και recovery

Χρήσιμα signals: απότομη αλλαγή request rate, endpoint mix, identity/source distribution, connection states, error rate, queue depth, cache hit ratio και dependency latency. Μην θεωρείς κάθε spike επίθεση—release, backup ή bug μπορεί να μοιάζουν παρόμοια. Μετά το συμβάν έλεγξε backlog, data consistency και επαναφορά dependencies.

## Συνηθισμένα λάθη

- Δοκιμή production χωρίς σαφή όρια.
- Μέτρηση μόνο requests/second.
- Αγνόηση queues και dependencies.
- Ανεξέλεγκτα retries.
- Υπερβολικό logging υπό πίεση.
- Αντιμετώπιση του autoscaling σαν απεριόριστη προστασία.

## Καθοδηγούμενο εργαστήριο

Σε localhost δημιούργησε μια μικρή υπηρεσία με περιορισμένο worker pool ή queue. Αύξησε αργά τον αριθμό φυσιολογικών requests μέσα σε χαμηλό, ασφαλές όριο. Κατέγραψε latency, errors και resource usage και παρατήρησε πότε εμφανίζεται backpressure. Σταμάτησε πριν επηρεαστεί οποιοδήποτε άλλο σύστημα.

## Έλεγχος γνώσεων

1. Γιατί η διαθεσιμότητα εξαρτάται από dependencies;
2. Ποια η διαφορά μεταξύ rate limit και quota;
3. Γιατί τα retries μπορούν να επιδεινώσουν outage;
4. Ποια telemetry χρειάζεσαι σε capacity test;
5. Τι σημαίνει graceful degradation;

## Καθοδηγούμενη μελέτη

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Κάθε load test πρέπει να έχει όριο, telemetry και stop condition πριν ξεκινήσει.

### Συνέχισε με

Προτεινόμενα επόμενα modules: **19, 23, 47, 48, 51**.

---

# Ασφάλεια Sessions, Cookies, Tokens και Πρόληψη Session Hijacking

Μετά την επιτυχημένη αυθεντικοποίηση, μια εφαρμογή πρέπει να διατηρεί την ταυτότητα του χρήστη με ασφάλεια. Session cookies, bearer tokens, refresh tokens και device sessions γίνονται ουσιαστικά credentials: όποιος αποκτήσει έγκυρη τιμή μπορεί συχνά να ενεργήσει ως ο χρήστης μέχρι να λήξει ή να ανακληθεί.

> **Όριο εξουσιοδότησης:** Δοκίμαζε session behavior μόνο σε εφαρμογές και λογαριασμούς που σου ανήκουν ή είναι ρητά εντός scope. Χρησιμοποίησε synthetic accounts και δεδομένα· μην συλλέγεις ή επαναχρησιμοποιείς sessions άλλων χρηστών.

## Μαθησιακοί στόχοι

- Να ξεχωρίζεις authentication από session management.
- Να κατανοείς session IDs, cookies, access/refresh tokens και expiration.
- Να ελέγχεις Secure, HttpOnly, SameSite, scope και rotation.
- Να αξιολογείς logout, password reset και server-side revocation.
- Να εντοπίζεις authorization λάθη που παραμένουν ακόμη με ασφαλή tokens.

## Session lifecycle

Ένα session έχει δημιουργία, χρήση, ανανέωση, πιθανή rotation, λήξη και ανάκληση. Η εφαρμογή πρέπει να αποφεύγει predictable identifiers και να μην κρατά sessions ενεργά επ' αόριστον. Η αλλαγή password, account disable ή κρίσιμη αλλαγή ασφάλειας πρέπει να έχει σαφή επίδραση στα υπάρχοντα sessions.

## Cookies

Το `Secure` περιορίζει cookie transmission σε HTTPS, το `HttpOnly` δυσκολεύει πρόσβαση μέσω JavaScript και το `SameSite` επηρεάζει cross-site αποστολή. Τα `Domain` και `Path` πρέπει να είναι όσο πιο στενά γίνεται. Αυτά είναι σημαντικά controls, αλλά δεν αντικαθιστούν σωστό authorization ή XSS prevention.

## Bearer και refresh tokens

Ένα bearer token παρέχει πρόσβαση σε όποιον το κατέχει. Για αυτό χρειάζονται μικρό lifetime, σωστό audience/scope, ασφαλής αποθήκευση και ανάκληση όπου απαιτείται. Τα refresh tokens έχουν μεγαλύτερη αξία και πρέπει να προστατεύονται ακόμη περισσότερο, συχνά με rotation και reuse detection.

## Session fixation και rotation

Η εφαρμογή δεν πρέπει να διατηρεί attacker-controlled ή προ-authentication identifier μετά το login. Ένα νέο authentication event ή privilege change είναι καλό σημείο για rotation του session identifier.

## Logout και revocation

Ένα κουμπί logout που απλώς διαγράφει local UI state δεν είναι αρκετό όταν το server-side credential παραμένει ενεργό. Έλεγξε τι συμβαίνει σε logout, password reset, MFA reset, account disable, device removal και admin revocation.

## Authorization παραμένει ξεχωριστό

Ένα έγκυρο session αποδεικνύει ποιος είναι ο caller, όχι ότι επιτρέπεται να δει οποιοδήποτε object. Κάθε server-side operation πρέπει να εφαρμόζει authorization στον τρέχοντα user/tenant/object/action συνδυασμό.

## Detection

Χρήσιμα signals περιλαμβάνουν νέα device/location, ασυνήθιστη αλλαγή privilege, token reuse μετά από rotation, session χρήση μετά από logout/revocation και απότομες αλλαγές σε refresh behavior. Τα signals πρέπει να αξιολογούνται με context ώστε να περιορίζονται false positives.

## Καθοδηγούμενο εργαστήριο

Σε δική σου demo εφαρμογή ή training lab, δημιούργησε δύο synthetic users. Κατέγραψε ποια cookies/tokens δημιουργούνται, πότε λήγουν, τι flags έχουν και τι συμβαίνει μετά από logout ή password change. Επιβεβαίωσε ότι ο User A δεν μπορεί να προσπελάσει test object του User B αλλάζοντας μόνο identifier.

## Συνηθισμένα λάθη

- Πολύ μεγάλα token lifetimes.
- Refresh tokens χωρίς rotation ή revocation plan.
- Cookies με υπερβολικά ευρύ Domain/Path.
- Logout μόνο στην πλευρά του browser.
- Υπόθεση ότι authentication σημαίνει authorization.
- Logging ολόκληρων session tokens.

## Έλεγχος γνώσεων

1. Γιατί ένα session token αντιμετωπίζεται σαν credential;
2. Τι προστατεύει το HttpOnly και τι δεν προστατεύει;
3. Γιατί χρειάζεται rotation μετά από authentication/privilege change;
4. Τι πρέπει να συμβεί στα sessions μετά από account disable;
5. Γιατί authorization απαιτείται σε κάθε object access;

## Καθοδηγούμενη μελέτη

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Δούλεψε μόνο με synthetic accounts και κατέγραψε lifecycle, όχι πραγματικά credentials.

### Συνέχισε με

Προτεινόμενα επόμενα modules: **14, 22, 39, 70, 71, 131**.

---

# Firewalls, IDS/IPS, Honeypots και Επαλήθευση Ανίχνευσης

Τα firewalls, IDS/IPS και honeypots εξυπηρετούν διαφορετικούς σκοπούς. Το firewall επιβάλλει επιτρεπόμενες ροές, το IDS/IPS αναλύει activity και μπορεί να ειδοποιεί ή να μπλοκάρει, ενώ ένα honeypot προσφέρει ελεγχόμενο περιβάλλον παρατήρησης. Η σωστή δοκιμή μετρά αν οι έλεγχοι λειτουργούν όπως σχεδιάστηκαν· δεν προσπαθεί να «κρυφτεί» από αυτούς.

> **Όριο εξουσιοδότησης:** Η validation πρέπει να γίνεται σε δική σου ή ρητά εξουσιοδοτημένη υποδομή, με γνωστά test indicators και χωρίς τεχνικές που στοχεύουν στην παράκαμψη πραγματικών αμυνών τρίτων.

## Μαθησιακοί στόχοι

- Να ξεχωρίζεις preventive από detective controls.
- Να αξιολογείς firewall policy, segmentation και default-deny λογική.
- Να κατανοείς signatures, behavior analytics και telemetry dependencies.
- Να σχεδιάζεις benign detection tests.
- Να χρησιμοποιείς honeypots με σωστή απομόνωση και διαχείριση δεδομένων.

## Firewalls και policy

Η πιο χρήσιμη ερώτηση είναι «ποια ροή πρέπει να επιτρέπεται και γιατί;». Κατέγραψε source, destination, protocol, port/service, identity/context και owner. Αφαίρεσε stale rules και απόφυγε υπερβολικά ευρείες εξαιρέσεις. Η segmentation πρέπει να δοκιμάζεται ως security invariant, όχι μόνο ως configuration screenshot.

## IDS και IPS

Signature-based detection αναζητά γνωστά patterns, ενώ behavior/analytics μπορούν να εντοπίσουν αποκλίσεις. Και τα δύο εξαρτώνται από σωστή telemetry, timestamps, parsing και context. Ένα IPS έχει επιπλέον κίνδυνο false-positive blocking, επομένως χρειάζεται controlled rollout και παρακολούθηση.

## Detection engineering

Για κάθε detection όρισε:

1. συμπεριφορά που θέλεις να εντοπίσεις,
2. απαιτούμενη πηγή δεδομένων,
3. benign τρόπο αναπαραγωγής,
4. αναμενόμενο event/alert,
5. triage context,
6. false positives/false negatives,
7. ownership και retest cadence.

Η αποτυχία ενός alert μπορεί να οφείλεται σε sensor gap, parser, normalization, rule logic ή routing του alert—not μόνο στη rule.

## Honeypots

Ένα honeypot πρέπει να είναι απομονωμένο, εύκολα επαναφερόμενο και να μην περιέχει πραγματικά secrets. Κατέγραψε τι telemetry συλλέγει, πόσο διατηρείται και ποιος έχει πρόσβαση. Μην το χρησιμοποιείς ως ανεξέλεγκτο pivot προς άλλα συστήματα.

## Safe validation

Προτίμησε benign markers, synthetic log events, harmless connection attempts σε test service ή επίσημα detection test datasets. Ο στόχος είναι να επαληθεύσεις end-to-end ότι **activity → sensor → parser → rule → alert → analyst** λειτουργεί.

## Συνηθισμένα λάθη

- Άπειρα allow rules χωρίς owner/expiry.
- Υπόθεση ότι «το IDS είναι εγκατεστημένο» σημαίνει ότι βλέπει τα σωστά δεδομένα.
- Αλλαγή detection χωρίς regression test.
- Honeypot με πραγματικά credentials ή ανεπαρκή isolation.
- Tests που προσπαθούν να αποφύγουν την ανίχνευση αντί να την επικυρώσουν.

## Καθοδηγούμενο εργαστήριο

Σε localhost ή απομονωμένο lab, δημιούργησε έναν επιτρεπόμενο και έναν απαγορευμένο network path. Επιβεβαίωσε το αποτέλεσμα με logs. Έπειτα δημιούργησε ένα benign test event και ακολούθησέ το από την πηγή μέχρι το alert. Κατέγραψε κάθε σημείο όπου θα μπορούσε να χαθεί.

## Έλεγχος γνώσεων

1. Ποια η διαφορά preventive και detective control;
2. Γιατί κάθε firewall exception χρειάζεται owner και λόγο;
3. Ποια στάδια υπάρχουν από event μέχρι analyst alert;
4. Γιατί ένα honeypot χρειάζεται ισχυρή isolation;
5. Τι σημαίνει detection regression test;

## Καθοδηγούμενη μελέτη

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Για κάθε test γράψε πρώτα το αναμενόμενο telemetry και μετά εκτέλεσε το benign stimulus.

### Συνέχισε με

Προτεινόμενα επόμενα modules: **23, 26, 47, 80, 107, 108**.

---

# Ασφάλεια Web Servers και Reverse Proxies

Ένας web server δεν είναι μόνο η εφαρμογή που επιστρέφει HTML. Η πραγματική επιφάνεια περιλαμβάνει TLS termination, reverse proxies, virtual hosts, static files, upload paths, modules/plugins, management endpoints, filesystem permissions, logs και upstream εφαρμογές. Η αξιολόγηση πρέπει να εξετάζει ολόκληρη αυτή την αλυσίδα.

> **Όριο εξουσιοδότησης:** Έλεγχε μόνο hosts που ανήκουν στο scope. Μην εκτελείς active probing ή vulnerability validation σε δημόσιους servers τρίτων χωρίς άδεια.

## Μαθησιακοί στόχοι

- Να χαρτογραφείς web server/reverse-proxy αρχιτεκτονική.
- Να αξιολογείς TLS, headers, virtual hosts και management exposure.
- Να εντοπίζεις unsafe default content, directory exposure και permission issues.
- Να κατανοείς proxy trust και forwarded headers.
- Να συνδέεις configuration findings με logs και remediation.

## Αρχιτεκτονική και trust boundaries

Σχεδίασε τη διαδρομή `client → CDN/WAF → reverse proxy → application → data service`. Σημείωσε πού τερματίζει το TLS, πού γίνεται authentication, ποιος γράφει `X-Forwarded-*`/`Forwarded`, ποιο component θεωρείται trusted και ποια network path επιτρέπεται προς management interfaces.

## TLS και HTTP configuration

Έλεγξε certificate lifecycle, hostname coverage, redirect από HTTP σε HTTPS, σύγχρονα protocol/cipher settings και HSTS όπου ταιριάζει. Security headers όπως CSP, frame protections και content-type controls πρέπει να σχεδιάζονται ανά εφαρμογή και όχι να αντιγράφονται τυφλά.

## Virtual hosts και default sites

Default pages, test applications, παλιά virtual hosts και προσωρινά admin endpoints συχνά μένουν ξεχασμένα. Κάθε hostname πρέπει να έχει owner, business purpose και expected backend. Unknown `Host` values δεν πρέπει να δρομολογούνται αυθαίρετα σε ευαίσθητο site.

## Filesystem και static content

Εξέτασε document roots, directory listing, backups, temporary files, source maps, configuration artifacts και upload directories. Η web process πρέπει να έχει μόνο τις permissions που απαιτούνται. Secrets δεν πρέπει να βρίσκονται σε static paths ή repository artifacts.

## Reverse-proxy trust

Headers που υποτίθεται ότι δείχνουν πραγματικό client IP, scheme ή host είναι ασφαλή μόνο όταν ο proxy αφαιρεί μη έμπιστα values και η εφαρμογή εμπιστεύεται αποκλειστικά γνωστούς proxies. Διαφορετική canonicalization ανά layer μπορεί να δημιουργήσει routing ή access-control προβλήματα.

## Management και observability

Admin panels, status pages, metrics και debugging endpoints πρέπει να είναι περιορισμένα. Τα logs πρέπει να καταγράφουν αρκετό context για troubleshooting/incident response χωρίς passwords, session tokens ή άλλα secrets.

## Καθοδηγούμενο εργαστήριο

Στήσε έναν local web server ή reverse proxy. Κατέγραψε listening ports, document root, enabled modules, TLS state, default site, headers και logs. Δημιούργησε ένα harmless test file και επιβεβαίωσε ποιος μπορεί να το διαβάσει. Έλεγξε ότι management endpoint δεν είναι διαθέσιμο από μη έμπιστο test network.

## Συνηθισμένα λάθη

- Ξεχασμένα default/test sites.
- Admin interfaces στο ίδιο trust zone με public clients.
- Blind trust σε forwarded headers.
- Secrets ή backups μέσα στο document root.
- Υπερβολικές filesystem permissions.
- Logs που αποθηκεύουν credentials/tokens.

## Έλεγχος γνώσεων

1. Γιατί το reverse proxy είναι trust boundary;
2. Ποιος πρέπει να γράφει trusted forwarded headers;
3. Γιατί default virtual hosts αυξάνουν attack surface;
4. Ποια δεδομένα δεν πρέπει να γράφονται σε access logs;
5. Τι σημαίνει least privilege για τη web process;

## Καθοδηγούμενη μελέτη

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Ξεκίνα από αρχιτεκτονικό διάγραμμα και απόδειξε κάθε finding με το ελάχιστο μη καταστροφικό evidence.

### Συνέχισε με

Προτεινόμενα επόμενα modules: **14, 22, 40, 52, 69, 126**.

---

# Ασφάλεια Web Εφαρμογών

Η ασφάλεια web εφαρμογών αφορά trust boundaries ανάμεσα σε browser, server, APIs, identities, data stores και third-party integrations. Το ασφαλές testing δεν είναι λίστα payloads· είναι συστηματικός έλεγχος invariants όπως «ο χρήστης βλέπει μόνο τα δικά του δεδομένα», «μη έμπιστη είσοδος δεν αλλάζει τη δομή μιας εντολής» και «κρίσιμες ενέργειες απαιτούν σωστή εξουσιοδότηση».

> **Όριο εξουσιοδότησης:** Δοκίμαζε μόνο εφαρμογές και synthetic accounts που είναι δικά σου ή ρητά εντός scope. Απόφυγε πραγματικά προσωπικά δεδομένα, destructive actions και συλλογή περιττών records.

## Μαθησιακοί στόχοι

- Να μοντελοποιείς requests, sessions, roles, objects και trust boundaries.
- Να κατανοείς injection, XSS, access control, CSRF, SSRF και insecure file handling σε αμυντικό επίπεδο.
- Να αξιολογείς authentication/session lifecycle.
- Να χρησιμοποιείς safe proof και να συνδέεις finding με remediation.

## Access control πρώτα

Πολλά σοβαρά web findings δεν απαιτούν «περίπλοκο exploit». Έλεγξε αν κάθε server-side action επιβεβαιώνει subject, tenant, object και action. Δημιούργησε δύο test users και χρησιμοποίησε synthetic objects ώστε να αποδείξεις isolation χωρίς να αγγίξεις πραγματικά δεδομένα.

## Injection

Injection εμφανίζεται όταν μη έμπιστο input επηρεάζει τη δομή SQL, shell command, template, LDAP query ή άλλης γλώσσας. Η βασική άμυνα είναι parameterization/structured APIs, allowlisting όπου χρειάζεται, separation of data from code και least-privilege execution context. Output encoding δεν διορθώνει SQL injection, όπως και SQL parameters δεν διορθώνουν XSS· κάθε sink χρειάζεται κατάλληλο control.

## Cross-Site Scripting

Το XSS συμβαίνει όταν attacker-controlled data εκτελείται ως script ή ενεργό markup σε browser context. Χρησιμοποίησε context-aware output encoding, ασφαλή DOM APIs, template auto-escaping και CSP ως πρόσθετο layer. Σε lab αρκεί harmless marker που αποδεικνύει context· δεν χρειάζεται συλλογή cookies ή δεδομένων.

## CSRF και state-changing actions

State changes πρέπει να απαιτούν προστασία που δεν μπορεί να προβλέψει ή να επιβάλει τρίτο origin. SameSite cookies, CSRF tokens και origin checks μπορούν να συνδυαστούν. APIs που χρησιμοποιούν bearer tokens σε explicit authorization headers έχουν διαφορετικό threat model από cookie-authenticated endpoints.

## SSRF και outbound trust

Αν ο server κάνει requests σε URL που ελέγχει χρήστης, απαιτείται αυστηρός σχεδιασμός allowlist, DNS/IP handling, redirect policy, protocol restrictions και network egress. Για testing χρησιμοποίησε μόνο localhost/mock services που ελέγχεις.

## File upload και parsing

Έλεγξε πραγματικό file type, storage location, randomized names, execution permissions, size limits και downstream parsers. Το filename ή MIME type του client δεν είναι από μόνο του αξιόπιστο.

## Authentication και session management

Εξέτασε login, MFA, recovery, lockout/rate controls, logout, token rotation και privilege changes ως ένα ενιαίο lifecycle. Η ασφαλής αυθεντικοποίηση δεν διορθώνει ελλιπές authorization.

## Καθοδηγούμενο εργαστήριο

Σε training app με δύο synthetic users, χαρτογράφησε πέντε endpoints και σημείωσε authentication, authorization, input και output sinks. Δοκίμασε αν ο User A μπορεί να διαβάσει ή τροποποιήσει test object του User B χρησιμοποιώντας μόνο harmless identifiers. Κατέγραψε expected/observed behavior και remediation.

## Συνηθισμένα λάθη

- Testing μόνο με scanner.
- Σύγχυση authentication και authorization.
- Χρήση πραγματικών δεδομένων για proof.
- Εστίαση σε payloads χωρίς data-flow model.
- Εμπιστοσύνη σε client-side validation.
- Παράβλεψη recovery και business logic.

## Έλεγχος γνώσεων

1. Τι είναι security invariant σε web εφαρμογή;
2. Γιατί η parameterization μειώνει injection risk;
3. Γιατί το CSP είναι defense-in-depth και όχι μοναδική λύση XSS;
4. Πότε αλλάζει το CSRF threat model;
5. Γιατί το SSRF είναι και πρόβλημα network egress;

## Καθοδηγούμενη μελέτη

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Προτίμησε δύο synthetic accounts, test objects και μικρό evidence που αποδεικνύει το invariant χωρίς πραγματικά δεδομένα.

### Συνέχισε με

Προτεινόμενα επόμενα modules: **22, 39, 40, 52, 69, 70, 71, 124**.

---

# Penetration Testing: Scope, Evidence, Reporting και Retest

Ένα επαγγελματικό penetration test είναι ελεγχόμενη αξιολόγηση συγκεκριμένων security objectives μέσα σε συμφωνημένο scope. Η αξία του δεν μετριέται από το πόσα εργαλεία εκτελέστηκαν, αλλά από την ποιότητα της απόδειξης, τον περιορισμό κινδύνου, την ανάλυση root cause και το αν το αποτέλεσμα μπορεί να διορθωθεί και να επανελεγχθεί.

> **Όριο εξουσιοδότησης:** Πριν από οποιοδήποτε active test χρειάζονται γραπτή εξουσιοδότηση, συγκεκριμένο scope, χρονικό παράθυρο, επιτρεπόμενες/απαγορευμένες τεχνικές, emergency contacts και κανόνες διαχείρισης δεδομένων.

## Μαθησιακοί στόχοι

- Να γράφεις Rules of Engagement (RoE).
- Να μετατρέπεις business/security στόχους σε μετρήσιμα tests.
- Να διαχειρίζεσαι test accounts, δεδομένα και evidence.
- Να χρησιμοποιείς minimal-impact validation.
- Να γράφεις findings με severity, confidence, root cause και remediation.
- Να εκτελείς σωστό retest και cleanup.

## Pre-engagement

Καθόρισε owner συστημάτων, in-scope/out-of-scope assets, source addresses, test accounts, ημερομηνίες, τεχνικές, production constraints, τρίτους/cloud restrictions, stop contacts, retention/encryption evidence και τρόπο παράδοσης report. Ένα απλό target list δεν αντικαθιστά αυτά τα στοιχεία.

## Objectives και threat model

Μετέτρεψε αόριστο «βρες vulnerabilities» σε ερωτήσεις όπως:

- Μπορεί ένας normal test user να προσπελάσει object άλλου tenant;
- Μπορεί public service να επικοινωνήσει με management network που πρέπει να είναι απομονωμένο;
- Αν ένα test identity αλλάξει privilege, καταγράφεται και ανιχνεύεται;

Έτσι κάθε test έχει expected behavior.

## Discovery και validation

Ξεκίνα από inventories και passive evidence. Το active scanning πρέπει να είναι bounded. Για κάθε finding προτίμησε το μικρότερο proof: ανάγνωση synthetic object, harmless marker, local crash reproduction ή non-destructive test function. Μην συλλέγεις πραγματικά δεδομένα απλώς για πιο εντυπωσιακό screenshot.

## Evidence management

Κατέγραψε timestamp, tester, asset/version, request ή configuration, relevant response/log, auth context, expected/observed behavior και hashes όπου χρειάζεται. Κάνε redaction σε secrets και προσωπικά δεδομένα.

## Severity και business risk

Ξεχώρισε technical severity από business impact. Δήλωσε prerequisites, exploitability, blast radius, criticality, existing controls και confidence. Αν μια υπόθεση δεν επαληθεύτηκε, γράψε το ξεκάθαρα.

## Δομή finding

Ένα χρήσιμο finding περιλαμβάνει:

1. τίτλο και affected assets,
2. σύνοψη,
3. ασφαλή reproduction/evidence,
4. impact στο συγκεκριμένο περιβάλλον,
5. root cause,
6. remediation,
7. retest criteria,
8. references.

## Retest και cleanup

Το retest επαναλαμβάνει το αρχικό security invariant μετά τη διόρθωση και ελέγχει ότι η λειτουργικότητα παραμένει σωστή. Στο cleanup αφαίρεσε test accounts, synthetic records και προσωρινές αλλαγές που δημιούργησες, αλλά **διατήρησε τα νόμιμα audit/security logs**.

## Συνηθισμένα λάθη

- Scanner output ως τελικό pentest report.
- Άτυπη επέκταση scope.
- Περιττή συλλογή production data.
- Δημιουργία persistence/destructive impact για «proof».
- Απόκρυψη αβεβαιότητας.
- Finding χωρίς actionable remediation.
- Παράλειψη retest.

## Καθοδηγούμενο εργαστήριο

Γράψε RoE για φανταστικό lab δύο hosts. Όρισε έναν authorization στόχο, έναν network-exposure στόχο και έναν detection στόχο. Για κάθε έναν κατέγραψε evidence, safe stop condition και retest criteria. Έπειτα γράψε ένα sample finding χρησιμοποιώντας μόνο synthetic δεδομένα.

## Έλεγχος γνώσεων

1. Γιατί τα RoE είναι περισσότερα από target list;
2. Γιατί προτιμάται minimal proof;
3. Τι πρέπει να γίνεται redacted από evidence;
4. Πώς διαφέρει retest από απλή επιβεβαίωση ότι εγκαταστάθηκε patch;
5. Γιατί τα security logs δεν διαγράφονται στο cleanup;

## Καθοδηγούμενη μελέτη

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Ένα ολοκληρωμένο lab πρέπει να παράγει scope, evidence και επαγγελματικό finding—not μόνο command output.

### Συνέχισε με

Προτεινόμενα επόμενα modules: **26, 27, 43, 50, 85**.

---

# Ασφάλεια Ασύρματων Δικτύων

Η ασφάλεια Wi-Fi συνδυάζει radio behavior, authentication, encryption, segmentation, device identity, roaming και management. Το «χρησιμοποιεί WPA» δεν αρκεί ως συμπέρασμα· πρέπει να εξετάζονται security mode, credential lifecycle, client isolation, management plane και monitoring.

> **Όριο εξουσιοδότησης:** Active wireless testing γίνεται μόνο σε access points και clients που σου ανήκουν ή έχεις ρητή άδεια να αξιολογήσεις. Τα radio signals ξεπερνούν φυσικά όρια, επομένως μην συλλέγεις, διακόπτεις, impersonate ή προσπαθείς να ανακτήσεις credentials γειτονικών τρίτων δικτύων.

## Μαθησιακοί στόχοι

- Να κατανοείς station, AP, SSID/BSSID και βασικές κατηγορίες 802.11 frames.
- Να συγκρίνεις open, WPA2, WPA3 και enterprise authentication.
- Να ξεχωρίζεις PSK από 802.1X identity model.
- Να αναγνωρίζεις legacy/transition risks.
- Να αξιολογείς guest, IoT και management segmentation.

## 802.11 ρόλοι

Σε infrastructure Wi-Fi υπάρχουν station/client και access point. Enterprise περιβάλλοντα προσθέτουν controller, authentication server, certificates, NAC και roaming. Management, control και data frames έχουν διαφορετικό ρόλο. Protected Management Frames μειώνουν ορισμένες κατηγορίες forged management traffic όταν υποστηρίζονται και απαιτούνται σωστά.

## Open networks

Open SSID δεν προσφέρει link-layer confidentiality ανάμεσα σε client και AP. Σωστά ρυθμισμένο TLS εξακολουθεί να προστατεύει application data, αλλά το δίκτυο πρέπει να θεωρείται untrusted. Η εφαρμογή δεν πρέπει να βασίζεται στο Wi-Fi ως boundary εμπιστοσύνης.

## WPA2/WPA3 Personal

Personal mode χρησιμοποιεί shared secret. Η ασφάλεια εξαρτάται από ισχυρό passphrase και ασφαλή διανομή, αλλά η κοινή τιμή έχει αδύναμο individual accountability και δύσκολη ανάκληση ανά συσκευή. Το WPA3-Personal με SAE βελτιώνει την αντίσταση σε offline password guessing σε σχέση με παλιότερο PSK handshake όταν εφαρμόζεται σωστά. Transition modes χρειάζονται συνειδητή αξιολόγηση.

## Enterprise Wi-Fi και 802.1X

Enterprise mode χρησιμοποιεί EAP και backend όπως RADIUS. Σημαντικά στοιχεία είναι το EAP method, η validation του server certificate από τον client, lifecycle identities/certificates και η policy μετά το authentication. Client που αποδέχεται άγνωστο authentication server μόνο επειδή αναγνωρίζει το SSID δημιουργεί σοβαρό trust problem.

## Legacy protocols

WEP είναι παρωχημένο και δεν πρέπει να χρησιμοποιείται. TKIP και παλιά compatibility modes πρέπει να αφαιρούνται όπου υποστηρίζεται. Legacy τεχνολογία έχει θέση στην ιστορική κατανόηση, όχι σε νέα deployments.

## Guest, IoT και management segmentation

Guests, unmanaged clients και IoT έχουν διαφορετικό trust. Χρησιμοποίησε client isolation όπου ταιριάζει, περιορισμένο east-west access, egress/DNS policy και ξεχωριστό management. Η σύνδεση στο Wi-Fi δεν πρέπει να σημαίνει πρόσβαση σε admin interfaces.

## Management και monitoring

Προστάτευσε AP/controller administration με ισχυρό authentication, restricted management network, updates, backups και logs. Χρήσιμη telemetry είναι authentication/association events, RADIUS results, configuration changes, rogue AP observations, interference/channel health και repeated auth failures. Μην διατηρείς άσχετα client payloads.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε AP που σου ανήκει. Κατέγραψε security mode, client isolation, management exposure και update status. Σύνδεσε test device και επιβεβαίωσε ότι εμφανίζονται φυσιολογικά authentication events. Αν έχεις απομονωμένο guest network, επιβεβαίωσε ότι guest client δεν φτάνει το management interface.

## Συνηθισμένα λάθη

- Θεώρηση ότι επειδή βλέπεις ένα SSID έχεις δικαίωμα testing.
- Shared PSK για περιβάλλον που απαιτεί individual identity.
- Μη validation RADIUS/server certificate.
- Μόνιμα legacy transition modes.
- Guests/IoT/management στο ίδιο trust zone.
- Disruptive tests σε shared spectrum.

## Έλεγχος γνώσεων

1. Γιατί shared PSK έχει αδύναμο individual accountability;
2. Τι βελτιώνει το WPA3-SAE;
3. Γιατί ο enterprise client πρέπει να επαληθεύει τον authentication server;
4. Γιατί guest και management networks πρέπει να χωρίζονται;
5. Γιατί το wireless testing απαιτεί ιδιαίτερη προσοχή στο scope;

## Καθοδηγούμενη μελέτη

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Κράτησε όλες τις δοκιμές σε APs που σου ανήκουν και εστίασε σε configuration, identity, segmentation και evidence.

### Συνέχισε με

Προτεινόμενα επόμενα modules: **44, 51, 55, 88, 122, 123**.

---

# Ασφάλεια Κινητών Συσκευών

> **Ελληνική έκδοση — Μάθημα 017.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Mobile, IoT και embedded συστήματα συνδυάζουν εφαρμογές, λειτουργικό, firmware, radios, hardware roots of trust και φυσική πρόσβαση. Το security model εξαρτάται από secure boot, app sandboxing, permissions, key storage, update trust και τις πραγματικές διεπαφές που εκτίθενται.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Ασφάλεια Κινητών Συσκευών**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Mobile Platforms**
  Στο **Mobile Platforms**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.
- **Mobile Threat Model**
  Στο **Mobile Threat Model**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.
- **Improving Mobile Ασφάλεια**
  Στο **Improving Mobile Ασφάλεια**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.
- **Σύγχρονο mobile-security additions**
  Στο **Σύγχρονο mobile-security additions**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.
- **Verification standards**
  Για το **Verification standards**, ξεχώρισε normative specification από tutorial ή vendor summary. Κατέγραψε έκδοση/ημερομηνία, ποιο requirement στηρίζει το συμπέρασμα και ποιο μέρος του **Ασφάλεια Κινητών Συσκευών** χρειάζεται επανέλεγχο όταν αλλάξει η πηγή.
- **Safe lab ideas**
  Στο **Safe lab ideas**, μετέτρεψε τη θεωρία του **Ασφάλεια Κινητών Συσκευών** σε ελέγξιμα κριτήρια: τι πρέπει να μπορείς να εξηγήσεις, ποιο λάθος assumption εμφανίζεται συχνότερα, ποιο safe lab το αποκαλύπτει και ποιο retest αποδεικνύει ότι το διόρθωσες.
- **Mobile application architecture review**
  Στο **Mobile application architecture review**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.
- **Credential and secret handling**
  Για το **Credential and secret handling**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Authentication and authorization**
  Για το **Authentication and authorization**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Platform storage**
  Για το **Platform storage**, κατέγραψε ποιος μπορεί να γράψει/διαβάσει το state, πού αποθηκεύεται, πώς προστατεύεται at rest, ποιο backup/sync behavior υπάρχει και πότε το data πρέπει να διαγράφεται ή να ανακαλείται.
- **Network security**
  Στο **Network security**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.
- **Deep links, intents, and URL schemes**
  Για το **Deep links, intents, and URL schemes**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **WebViews and embedded browsers**
  Στο **WebViews and embedded browsers**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.
- **Permissions and privacy**
  Για το **Permissions and privacy**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Build and release security**
  Για το **Build and release security**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **Device integrity and risk signals**
  Στο **Device integrity and risk signals**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.
- **Enterprise mobile controls**
  Στο **Enterprise mobile controls**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.
- **Mobile logging**
  Στο **Mobile logging**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Mobile security review checklist**
  Στο **Mobile security review checklist**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Ασφάλεια Κινητών Συσκευών**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε δική σου συσκευή, emulator ή development board. Προτίμησε static analysis, documented debug interfaces και benign sample apps/firmware. Απόφυγε tests σε τρίτες συσκευές ή ασύρματα περιβάλλοντα.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Ασφάλεια Κινητών Συσκευών**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Ασφάλεια Κινητών Συσκευών** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 017](../../English/05-Mobile-IoT-and-Hardware/17-Mobile-Security.md)

---

# Ασφάλεια IoT και OT

Τα Internet of Things (IoT) και Operational Technology (OT) περιβάλλοντα συνδυάζουν software, embedded hardware, radios, φυσικές διεργασίες, cloud services, mobile εφαρμογές, update pipelines και συσκευές με πολύ μεγάλο lifecycle. Η αξιολόγηση ασφάλειας πρέπει να εξετάζει τόσο το ψηφιακό compromise όσο και τις πιθανές επιπτώσεις στον φυσικό κόσμο.

> **Όριο εξουσιοδότησης:** Έλεγχε μόνο συσκευές, δίκτυα, firmware, cloud accounts και φυσικές διεργασίες που σου ανήκουν ή είναι ρητά εντός scope. Απόφυγε disruptive radio/control/safety tests σε shared ή production περιβάλλοντα. Προτίμησε emulator, development board, captured data και απομονωμένο lab.

## Μαθησιακοί στόχοι

- Να αναγνωρίζεις IoT/OT trust boundaries.
- Να χαρτογραφείς device, gateway, cloud, app και update σχέσεις.
- Να αξιολογείς identity, secrets, management interfaces και update trust.
- Να κατανοείς γιατί safety και availability αλλάζουν το testing model.
- Να επιλέγεις κατάλληλο evidence για embedded/operational περιβάλλοντα.

## Αρχιτεκτονική IoT

Ένα IoT προϊόν μπορεί να περιλαμβάνει sensor/actuator, microcontroller ή embedded Linux, local radio, gateway, vendor cloud API, mobile app και signing/update infrastructure. Αντιμετώπισε τα σαν διαφορετικά trust zones. Ένα app bug μπορεί να εκθέσει device credentials, ένα cloud authorization bug να επηρεάσει ολόκληρο fleet και ένα compromised update key να περάσει πολλά τοπικά boundaries.

## Device identity και provisioning

Έλεγξε πώς αποκτά η συσκευή την πρώτη της identity, αν τα credentials είναι μοναδικά ανά unit, πού αποθηκεύονται keys, πώς γίνεται ownership transfer και πώς γίνεται decommission. Shared factory passwords ή undocumented recovery accounts δημιουργούν fleet-wide risk. Το provisioning πρέπει να δένει τη συσκευή με τον σωστό owner/tenant και να αφήνει audit trail.

## Management interfaces και local services

Κατέγραψε listening services, debug interfaces, serial/JTAG access, web administration, Bluetooth/Wi-Fi pairing, discovery protocols και maintenance ports. Interface που χρειάζεται μόνο στην παραγωγή/επισκευή δεν πρέπει να παραμένει broadly exposed. Management paths χρειάζονται authentication, authorization, resource controls και ασφαλές recovery.

## Firmware και secure updates

Για το update system απάντησε: ποιος επιτρέπεται να δημοσιεύσει artifact, πώς επαληθεύεται η αυθεντικότητα, πώς ελέγχεται downgrade/rollback και τι γίνεται μετά από failed update. Η digital signature είναι μόνο ένα μέρος του trust· verification keys, version policy, boot chain και recovery πρέπει επίσης να είναι αξιόπιστα.

## Secrets και storage

Εξέτασε hard-coded secrets, API tokens, Wi-Fi credentials, certificates, debug logs, crash dumps και backup/export files. Προτίμησε per-device secrets, hardware-backed storage όπου υποστηρίζεται, rotation και ελάχιστα permissions στο cloud/API layer.

## Cloud APIs και authorization

IoT APIs συχνά χειρίζονται identifiers για devices, homes, fleets ή tenants. Κάθε operation πρέπει να κάνει server-side authorization του caller απέναντι στο συγκεκριμένο object/action. Έγκυρο token δεν σημαίνει ότι ο caller κατέχει οποιοδήποτε device ID έστειλε.

## OT και cyber-physical systems

OT περιλαμβάνει industrial control, building automation, energy, manufacturing και άλλα συστήματα όπου integrity/availability επηρεάζουν φυσικές διεργασίες. Safety interlocks, deterministic operation, change management, vendor support, legacy protocols και recovery μπορεί να έχουν μεγαλύτερη προτεραιότητα από aggressive probing.

Passive discovery και configuration review είναι συνήθως ασφαλέστερη αρχή. Κάθε state-changing test χρειάζεται operator-approved rollback και safety plan.

## Segmentation και gateways

Χώρισε device networks από user workstations και management planes. Τα gateways πρέπει να επιτρέπουν μόνο τα πραγματικά αναγκαία protocols/destinations. Κατέγραψε required east-west και north-south flows αντί να δίνεις broad connectivity επειδή μια συσκευή είναι δύσκολη στη διαχείριση.

## Logging και fleet visibility

Χρήσιμο evidence: firmware version, secure boot/update state, device identity, provisioning, failed authentication, config changes, cloud API decisions, gateway connections και recovery actions. Απόφυγε secrets στα logs και φρόντισε time correlation μεταξύ device, gateway και cloud.

## Συνηθισμένα λάθη

- Εμπιστοσύνη σε κάθε device του local network.
- Shared default/fleet-wide credentials.
- Updates χωρίς authenticated provenance ή rollback policy.
- Debug interfaces ενεργά χωρίς ownership controls.
- Cloud authorization μόνο με client-supplied object IDs.
- OT testing σαν να είναι disposable web lab.
- Απουσία ασφαλούς recovery όταν μια συσκευή αποτύχει.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε development board, emulator ή spare IoT device που σου ανήκει. Σχεδίασε device→gateway/cloud/app data flow, κατέγραψε local services, firmware/update state και πού φυλάσσονται credentials. Άλλαξε μία ακίνδυνη ρύθμιση και επιβεβαίωσε ποια local/cloud logs καταγράφουν την αλλαγή. Επανέφερε το αρχικό state.

## Έλεγχος γνώσεων

1. Γιατί per-device identity είναι καλύτερη από fleet-wide password;
2. Τι πρέπει να είναι αξιόπιστο πέρα από την update signature;
3. Γιατί OT testing έχει αυστηρότερα όρια;
4. Ποιο authorization check χρειάζεται multi-tenant IoT API;
5. Ποιο evidence συνδέει device event με cloud decision;

## Καθοδηγούμενη μελέτη

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Εξέτασε ολόκληρο lifecycle: manufacture, provisioning, normal operation, update, ownership transfer, incident recovery και decommissioning.

### Συνέχισε με

Προτεινόμενα modules: **41, 48, 54, 56, 83, 103, 122, 123**. Από το menu χρησιμοποίησε **Αναζήτηση μαθημάτων** για embedded, hardware και radio θέματα.

---

# Ασφάλεια Cloud

> **Ελληνική έκδοση — Μάθημα 019.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Cloud-native ασφάλεια σημαίνει έλεγχο control planes, workload identity, artifacts, build systems, containers και data flows. Οι σημαντικότερες αστοχίες συχνά προκύπτουν από υπερβολικά δικαιώματα, implicit trust μεταξύ services, μη επαληθεύσιμα artifacts ή ανεπαρκή provenance.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Ασφάλεια Cloud**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Cloud Computing Βασικές Έννοιες**
  Για το **Cloud Computing Βασικές Έννοιες**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **Cloud Deployment Models**
  Για το **Cloud Deployment Models**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **NIST Cloud Αρχιτεκτονική**
  Για το **NIST Cloud Αρχιτεκτονική**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **Five characteristics of cloud computing**
  Για το **Five characteristics of cloud computing**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **Threats:**
  Για το **Threats:**, στο πλαίσιο του **Ασφάλεια Cloud**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Cloud Threat Scenarios**
  Για το **Cloud Threat Scenarios**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **Assessment questions**
  Για το **Assessment questions**, στο πλαίσιο του **Ασφάλεια Cloud**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Cloud Ασφάλεια Control Layers**
  Για το **Cloud Ασφάλεια Control Layers**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **Σύγχρονο cloud-security model**
  Για το **Σύγχρονο cloud-security model**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **Core control areas**
  Για το **Core control areas**, στο πλαίσιο του **Ασφάλεια Cloud**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Zero Trust connection**
  Για το **Zero Trust connection**, στο πλαίσιο του **Ασφάλεια Cloud**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Ασφάλεια Cloud**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε local containers ή sandbox cloud accounts που σου ανήκουν. Έλεγξε policies και artifacts read-only πριν από αλλαγές και απέφυγε δημόσια exposure στα labs.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Ασφάλεια Cloud**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Ασφάλεια Cloud** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 019](../../English/07-Cloud-Containers-and-Supply-Chain/19-Cloud-Security.md)

---

# Κρυπτογραφία

Η κρυπτογραφία παρέχει μηχανισμούς για confidentiality, integrity, authenticity, key establishment και επαληθεύσιμη προέλευση δεδομένων. Η πραγματική ασφάλεια δεν εξαρτάται μόνο από έναν ισχυρό algorithm αλλά και από protocol design, key lifecycle, randomness, implementation, identity binding, error handling και recovery.

> **Όριο εξουσιοδότησης:** Χρησιμοποίησε δικά σου keys και synthetic data. Μην επιχειρείς ανάκτηση ξένων credentials, αποκρυπτογράφηση δεδομένων χωρίς άδεια ή αποδυνάμωση πραγματικών συστημάτων για πείραμα.

## Μαθησιακοί στόχοι

- Να ξεχωρίζεις encryption, hashes, MACs, signatures και KDFs.
- Να κατανοείς symmetric και asymmetric key roles.
- Να εξηγείς nonces, IVs, salts, randomness και replay protection.
- Να κατανοείς certificates, trust anchors, revocation και rotation.
- Να αναγνωρίζεις συχνά protocol/implementation mistakes.
- Να σχεδιάζεις cryptographic agility και post-quantum migration.

## Security goals

**Confidentiality** περιορίζει ποιος διαβάζει δεδομένα. **Integrity** ανιχνεύει μη εξουσιοδοτημένη αλλαγή. **Authenticity** δίνει evidence για identity/key που παρήγαγε ή αυθεντικοποίησε μήνυμα. Το **non-repudiation** είναι ευρύτερος νομικός/λειτουργικός ισχυρισμός και δεν προκύπτει αυτόματα από μια signature.

Η κρυπτογραφία δεν αποφασίζει authorization. Μια έγκυρη signature μπορεί να συνδέεται με λάθος tenant, resource, audience ή workflow και επομένως να οδηγεί σε λάθος απόφαση.

## Symmetric encryption

Τα symmetric algorithms χρησιμοποιούν shared secret και είναι αποδοτικά για bulk data. Σύγχρονα συστήματα συνήθως χρειάζονται authenticated encryption ώστε confidentiality και integrity να προστατεύονται μαζί. Key reuse, nonce/IV misuse ή μη authenticated metadata μπορούν να ακυρώσουν την ασφάλεια ισχυρού primitive.

## Hash functions και passwords

Τα cryptographic hashes δίνουν fixed-size digest και χρησιμοποιούνται σε integrity και protocol constructions. Password storage είναι διαφορετικό πρόβλημα: τα ανθρώπινα passwords έχουν μικρή entropy και χρειάζονται κατάλληλο password-hashing/KDF με unique salt και σωστές work parameters. Ένα γρήγορο απλό hash δεν είναι επαρκές.

## Message Authentication Codes

MAC αποδεικνύει ότι ο κάτοχος του shared key αυθεντικοποίησε ένα μήνυμα, αλλά δεν παρέχει public verifiability όπως digital signature. Το protocol πρέπει να ορίζει ακριβώς ποια fields και ποια canonical representation μπαίνουν στο MAC.

## Public-key cryptography και signatures

Public/private key pairs χρησιμοποιούνται για key establishment, signatures ή encryption ανάλογα με το scheme. Private keys χρειάζονται αυστηρό access control και lifecycle. Η verification πρέπει να ελέγχει algorithm, key, context και message representation—not απλώς ένα boolean result.

## Randomness, nonces, IVs και salts

Random keys απαιτούν cryptographically secure source. **Nonce** συνήθως χρειάζεται uniqueness σύμφωνα με το protocol, **IV** έχει algorithm-specific requirements και **salt** διαφοροποιεί ίδιες password/hash εισόδους. Οι όροι δεν είναι εναλλάξιμοι.

## Key lifecycle

Χαρτογράφησε generation, storage, distribution, activation, use, rotation, revocation, backup, recovery, archival και destruction. Long-lived encrypted data παραμένουν ασφαλή μόνο αν το organization μπορεί να προστατεύει και να ανακτά τα keys χωρίς υπερβολικό access.

## PKI και certificates

Certificates συνδέουν public keys με identities/names μέσα σε trust model. Validation μπορεί να απαιτεί chain building, hostname/identity checks, validity period, key usage, policy, revocation strategy και trust-store management. TLS προστατεύει connection μόνο όταν identity και authorization ερμηνεύονται σωστά.

## Συνηθισμένες αστοχίες

- Custom cipher/protocol χωρίς expert review.
- Nonce/IV reuse όπου απαιτείται uniqueness.
- Keys μέσα σε source code ή public client apps.
- Encryption χωρίς authentication/integrity.
- Disabled certificate verification.
- Fast unsalted hashes για passwords.
- Long-lived keys χωρίς rotation/revocation.
- Secrets σε logs.

## Crypto agility και post-quantum planning

Long-lived systems πρέπει να γνωρίζουν ποια algorithms/keys χρησιμοποιούν και να μπορούν να αλλάξουν χωρίς redesign. Η post-quantum migration είναι κυρίως inventory, dependency, interoperability, testing και lifecycle πρόβλημα: βρες πού χρησιμοποιούνται ευάλωτα public-key algorithms, προτεραιοποίησε long-lived sensitive data και δοκίμασε standardized replacements σε controlled environment.

## Καθοδηγούμενο εργαστήριο

Με synthetic text, γράψε μικρό local πρόγραμμα που υπολογίζει file hash, MAC με προσωρινό lab key και authenticated encryption μέσω αξιόπιστης library. Άλλαξε ένα byte του ciphertext ή authenticated data και παρατήρησε verification failure. Κατέγραψε ποια ιδιότητα παρέχει κάθε primitive και ποιο state/key πρέπει να προστατεύεται.

## Έλεγχος γνώσεων

1. Γιατί encryption μόνο του δεν ισοδυναμεί με authenticated encryption;
2. Γιατί salt, nonce και IV είναι διαφορετικά;
3. Γιατί fast hash είναι ακατάλληλο για password storage;
4. Τι χρειάζεται certificate validation πέρα από signature check;
5. Γιατί cryptographic agility είναι architectural property;

## Καθοδηγούμενη μελέτη

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Για κάθε primitive κατέγραψε security property, απαιτούμενο secret/public state, misuse conditions, lifecycle και evidence σωστής χρήσης.

### Συνέχισε με

Προτεινόμενα modules: **39, 49, 78, 100, 101, 102, 103, 131, 132**. Από το menu χρησιμοποίησε **Αναζήτηση μαθημάτων** για συγκεκριμένο primitive ή protocol.

---

# Identity, Zero Trust και Ασφάλεια Πρόσβασης

> **Ελληνική έκδοση — Μάθημα 021.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Identity και cryptography είναι μηχανισμοί μεταφοράς εμπιστοσύνης. Authentication απαντά ποιος παρουσιάζει ένα credential, authorization τι επιτρέπεται να κάνει, ενώ cryptography προστατεύει συγκεκριμένες ιδιότητες δεδομένων και πρωτοκόλλων. Κλειδιά, tokens, certificates, federation metadata και policy engines είναι όλα authority-bearing artifacts και χρειάζονται σαφή lifecycle.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Identity, Zero Trust και Ασφάλεια Πρόσβασης**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Identity lifecycle**
  Για το **Identity lifecycle**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Authentication**
  Για το **Authentication**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Authorization**
  Για το **Authorization**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Privileged Access Διαχείριση**
  Για το **Privileged Access Διαχείριση**, στο πλαίσιο του **Identity, Zero Trust και Ασφάλεια Πρόσβασης**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Zero Trust**
  Για το **Zero Trust**, στο πλαίσιο του **Identity, Zero Trust και Ασφάλεια Πρόσβασης**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Identity telemetry**
  Για το **Identity telemetry**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Safe lab**
  Στο **Safe lab**, μετέτρεψε τη θεωρία του **Identity, Zero Trust και Ασφάλεια Πρόσβασης** σε ελέγξιμα κριτήρια: τι πρέπει να μπορείς να εξηγήσεις, ποιο λάθος assumption εμφανίζεται συχνότερα, ποιο safe lab το αποκαλύπτει και ποιο retest αποδεικνύει ότι το διόρθωσες.
- **References**
  Για το **References**, ξεχώρισε normative specification από tutorial ή vendor summary. Κατέγραψε έκδοση/ημερομηνία, ποιο requirement στηρίζει το συμπέρασμα και ποιο μέρος του **Identity, Zero Trust και Ασφάλεια Πρόσβασης** χρειάζεται επανέλεγχο όταν αλλάξει η πηγή.
- **Identity architecture in practice**
  Για το **Identity architecture in practice**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Human identities**
  Για το **Human identities**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Workload and machine identities**
  Για το **Workload and machine identities**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **Authentication design**
  Για το **Authentication design**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Authorization design**
  Για το **Authorization design**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Common failure modes**
  Για το **Common failure modes**, στο πλαίσιο του **Identity, Zero Trust και Ασφάλεια Πρόσβασης**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Access review questions**
  Για το **Access review questions**, στο πλαίσιο του **Identity, Zero Trust και Ασφάλεια Πρόσβασης**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Privilege boundaries and break-glass access**
  Για το **Privilege boundaries and break-glass access**, στο πλαίσιο του **Identity, Zero Trust και Ασφάλεια Πρόσβασης**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Zero Trust decision model**
  Για το **Zero Trust decision model**, στο πλαίσιο του **Identity, Zero Trust και Ασφάλεια Πρόσβασης**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Identity threat scenarios for defenders**
  Για το **Identity threat scenarios for defenders**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Identity security review worksheet**
  Για το **Identity security review worksheet**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Practical defensive exercise**
  Στο **Practical defensive exercise**, όρισε συγκεκριμένο objective, owned/local scope, expected result και stop condition. Κράτησε μόνο sanitized evidence, σύγκρινε expected με observed behavior και ολοκλήρωσε με remediation και ίδιο regression test.
- **2026 identity update — NIST SP 800-63 Revision 4**
  Για το **2026 identity update — NIST SP 800-63 Revision 4**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Identity, Zero Trust και Ασφάλεια Πρόσβασης**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε synthetic identities, test certificates και local identity providers. Χαρτογράφησε issuer, subject, audience, permissions, lifetime, rotation και revocation χωρίς να αποθηκεύεις πραγματικά secrets.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Identity, Zero Trust και Ασφάλεια Πρόσβασης**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Identity, Zero Trust και Ασφάλεια Πρόσβασης** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 021](../../English/06-Identity-Cryptography-and-Trust/21-Identity-Zero-Trust-and-Access-Security.md)

---

# Ασφαλές Λογισμικό, APIs και Εφοδιαστική Αλυσίδα

> **Ελληνική έκδοση — Μάθημα 022.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Cloud-native ασφάλεια σημαίνει έλεγχο control planes, workload identity, artifacts, build systems, containers και data flows. Οι σημαντικότερες αστοχίες συχνά προκύπτουν από υπερβολικά δικαιώματα, implicit trust μεταξύ services, μη επαληθεύσιμα artifacts ή ανεπαρκή provenance.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Ασφαλές Λογισμικό, APIs και Εφοδιαστική Αλυσίδα**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Secure by design**
  Για το **Secure by design**, στο πλαίσιο του **Ασφαλές Λογισμικό, APIs και Εφοδιαστική Αλυσίδα**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **API security**
  Για το **API security**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **API review checklist**
  Για το **API review checklist**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **Software supply-chain security**
  Για το **Software supply-chain security**, ακολούθησε την αλυσίδα trust από immutable/early-boot state μέχρι OS/application. Έλεγξε measured/verified state, key custody, update authorization, anti-rollback και τι αλλάζει όταν ο attacker έχει φυσική πρόσβαση.
- **Defensive controls**
  Για το **Defensive controls**, στο πλαίσιο του **Ασφαλές Λογισμικό, APIs και Εφοδιαστική Αλυσίδα**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Safe lab**
  Στο **Safe lab**, μετέτρεψε τη θεωρία του **Ασφαλές Λογισμικό, APIs και Εφοδιαστική Αλυσίδα** σε ελέγξιμα κριτήρια: τι πρέπει να μπορείς να εξηγήσεις, ποιο λάθος assumption εμφανίζεται συχνότερα, ποιο safe lab το αποκαλύπτει και ποιο retest αποδεικνύει ότι το διόρθωσες.
- **References**
  Για το **References**, ξεχώρισε normative specification από tutorial ή vendor summary. Κατέγραψε έκδοση/ημερομηνία, ποιο requirement στηρίζει το συμπέρασμα και ποιο μέρος του **Ασφαλές Λογισμικό, APIs και Εφοδιαστική Αλυσίδα** χρειάζεται επανέλεγχο όταν αλλάξει η πηγή.
- **Secure development lifecycle**
  Για το **Secure development lifecycle**, στο πλαίσιο του **Ασφαλές Λογισμικό, APIs και Εφοδιαστική Αλυσίδα**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Ασφάλεια requirements**
  Για το **Ασφάλεια requirements**, στο πλαίσιο του **Ασφαλές Λογισμικό, APIs και Εφοδιαστική Αλυσίδα**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Threat modeling**
  Για το **Threat modeling**, στο πλαίσιο του **Ασφαλές Λογισμικό, APIs και Εφοδιαστική Αλυσίδα**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **API authorization patterns**
  Για το **API authorization patterns**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Object-level authorization**
  Για το **Object-level authorization**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Function-level authorization**
  Για το **Function-level authorization**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Property-level authorization**
  Για το **Property-level authorization**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Resource and business-flow protection**
  Για το **Resource and business-flow protection**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **API inventory and lifecycle**
  Για το **API inventory and lifecycle**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **Third-party API consumption**
  Για το **Third-party API consumption**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **Software supply-chain model**
  Για το **Software supply-chain model**, ακολούθησε την αλυσίδα trust από immutable/early-boot state μέχρι OS/application. Έλεγξε measured/verified state, key custody, update authorization, anti-rollback και τι αλλάζει όταν ο attacker έχει φυσική πρόσβαση.
- **Dependency governance**
  Για το **Dependency governance**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **CI/CD hardening**
  Για το **CI/CD hardening**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **Build provenance and artifact integrity**
  Για το **Build provenance and artifact integrity**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **Secure by default checklist**
  Για το **Secure by default checklist**, στο πλαίσιο του **Ασφαλές Λογισμικό, APIs και Εφοδιαστική Αλυσίδα**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Ασφαλές Λογισμικό, APIs και Εφοδιαστική Αλυσίδα**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε local containers ή sandbox cloud accounts που σου ανήκουν. Έλεγξε policies και artifacts read-only πριν από αλλαγές και απέφυγε δημόσια exposure στα labs.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Ασφαλές Λογισμικό, APIs και Εφοδιαστική Αλυσίδα**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Ασφαλές Λογισμικό, APIs και Εφοδιαστική Αλυσίδα** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 022](../../English/07-Cloud-Containers-and-Supply-Chain/22-Secure-Software-APIs-and-Supply-Chain.md)

---

# Detection Engineering, Incident Response και Threat Hunting

> **Ελληνική έκδοση — Μάθημα 023.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Blue-team εργασία σημαίνει να μετατρέπεις telemetry σε τεκμηριωμένα συμπεράσματα. Ένα alert δεν είναι απόδειξη από μόνο του. Χρειάζεται timeline, identity context, process/network relationships, data provenance και κατανόηση του τι δεν καταγράφεται. Η ανθεκτικότητα επεκτείνεται από detection μέχρι containment, recovery και verification.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Detection Engineering, Incident Response και Threat Hunting**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Detection engineering lifecycle**
  Στο **Detection engineering lifecycle**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Telemetry layers**
  Στο **Telemetry layers**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Incident response lifecycle**
  Για το **Incident response lifecycle**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **Preparation**
  Για το **Preparation**, όρισε decision owner, trigger, required telemetry, χρονική σειρά ενεργειών και πιθανό operational impact. Η σωστή απόφαση πρέπει να είναι αναστρέψιμη όπου γίνεται, να διατηρεί evidence και να συνδέεται με σαφές recovery/retest criterion.
- **Detection and analysis**
  Στο **Detection and analysis**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Containment**
  Για το **Containment**, όρισε decision owner, trigger, required telemetry, χρονική σειρά ενεργειών και πιθανό operational impact. Η σωστή απόφαση πρέπει να είναι αναστρέψιμη όπου γίνεται, να διατηρεί evidence και να συνδέεται με σαφές recovery/retest criterion.
- **Eradication and recovery**
  Για το **Eradication and recovery**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Lessons learned**
  Για το **Lessons learned**, όρισε decision owner, trigger, required telemetry, χρονική σειρά ενεργειών και πιθανό operational impact. Η σωστή απόφαση πρέπει να είναι αναστρέψιμη όπου γίνεται, να διατηρεί evidence και να συνδέεται με σαφές recovery/retest criterion.
- **Threat hunting**
  Στο **Threat hunting**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Safe exercise**
  Στο **Safe exercise**, όρισε συγκεκριμένο objective, owned/local scope, expected result και stop condition. Κράτησε μόνο sanitized evidence, σύγκρινε expected με observed behavior και ολοκλήρωσε με remediation και ίδιο regression test.
- **Designing useful telemetry**
  Στο **Designing useful telemetry**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Time and normalization**
  Για το **Time and normalization**, όρισε decision owner, trigger, required telemetry, χρονική σειρά ενεργειών και πιθανό operational impact. Η σωστή απόφαση πρέπει να είναι αναστρέψιμη όπου γίνεται, να διατηρεί evidence και να συνδέεται με σαφές recovery/retest criterion.
- **Detection engineering from behavior**
  Στο **Detection engineering from behavior**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Detection coverage mapping**
  Στο **Detection coverage mapping**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Alert triage**
  Στο **Alert triage**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **A compact triage structure**
  Για το **A compact triage structure**, όρισε decision owner, trigger, required telemetry, χρονική σειρά ενεργειών και πιθανό operational impact. Η σωστή απόφαση πρέπει να είναι αναστρέψιμη όπου γίνεται, να διατηρεί evidence και να συνδέεται με σαφές recovery/retest criterion.
- **Incident severity**
  Στο **Incident severity**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Evidence handling**
  Στο **Evidence handling**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Containment strategy**
  Για το **Containment strategy**, όρισε decision owner, trigger, required telemetry, χρονική σειρά ενεργειών και πιθανό operational impact. Η σωστή απόφαση πρέπει να είναι αναστρέψιμη όπου γίνεται, να διατηρεί evidence και να συνδέεται με σαφές recovery/retest criterion.
- **Recovery and validation**
  Για το **Recovery and validation**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Threat hunting methodology**
  Στο **Threat hunting methodology**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Tabletop exercise**
  Στο **Tabletop exercise**, όρισε συγκεκριμένο objective, owned/local scope, expected result και stop condition. Κράτησε μόνο sanitized evidence, σύγκρινε expected με observed behavior και ολοκλήρωσε με remediation και ίδιο regression test.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Detection Engineering, Incident Response και Threat Hunting**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε synthetic logs και harmless local events. Κατέγραψε expected evidence πριν το test και σύγκρινε με ό,τι πραγματικά συλλέχθηκε.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Detection Engineering, Incident Response και Threat Hunting**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Detection Engineering, Incident Response και Threat Hunting** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 023](../../English/08-Blue-Team-IR-Forensics-and-Resilience/23-Detection-Incident-Response-and-Threat-Hunting.md)

---

# Containers, Kubernetes και DevSecOps

> **Ελληνική έκδοση — Μάθημα 024.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Cloud-native ασφάλεια σημαίνει έλεγχο control planes, workload identity, artifacts, build systems, containers και data flows. Οι σημαντικότερες αστοχίες συχνά προκύπτουν από υπερβολικά δικαιώματα, implicit trust μεταξύ services, μη επαληθεύσιμα artifacts ή ανεπαρκή provenance.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Containers, Kubernetes και DevSecOps**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Container security model**
  Για το **Container security model**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **Image hygiene**
  Για το **Image hygiene**, στο πλαίσιο του **Containers, Kubernetes και DevSecOps**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Kubernetes security areas**
  Για το **Kubernetes security areas**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **Identity and RBAC**
  Για το **Identity and RBAC**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Workload isolation**
  Για το **Workload isolation**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **Secrets**
  Για το **Secrets**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **Admission and policy**
  Για το **Admission and policy**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **DevSecOps controls**
  Για το **DevSecOps controls**, στο πλαίσιο του **Containers, Kubernetes και DevSecOps**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Safe lab**
  Στο **Safe lab**, μετέτρεψε τη θεωρία του **Containers, Kubernetes και DevSecOps** σε ελέγξιμα κριτήρια: τι πρέπει να μπορείς να εξηγήσεις, ποιο λάθος assumption εμφανίζεται συχνότερα, ποιο safe lab το αποκαλύπτει και ποιο retest αποδεικνύει ότι το διόρθωσες.
- **Container image lifecycle**
  Για το **Container image lifecycle**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **Runtime minimization**
  Στο **Runtime minimization**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **Linux privilege controls**
  Για το **Linux privilege controls**, στο πλαίσιο του **Containers, Kubernetes και DevSecOps**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Kubernetes control-plane security**
  Για το **Kubernetes control-plane security**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **RBAC review**
  Για το **RBAC review**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Namespace design**
  Για το **Namespace design**, κατέγραψε Linux UID/GID/capabilities, namespace membership, syscall/filesystem boundary και LSM/seccomp policy. Έλεγξε effective privilege μέσα σε disposable VM/container και χρησιμοποίησε `/proc`, audit/logging και configuration diff ως evidence.
- **Pod Ασφάλεια Standards**
  Για το **Pod Ασφάλεια Standards**, ξεχώρισε normative specification από tutorial ή vendor summary. Κατέγραψε έκδοση/ημερομηνία, ποιο requirement στηρίζει το συμπέρασμα και ποιο μέρος του **Containers, Kubernetes και DevSecOps** χρειάζεται επανέλεγχο όταν αλλάξει η πηγή.
- **Network policy**
  Στο **Network policy**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.
- **Secrets and configuration**
  Για το **Secrets and configuration**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **Admission policy**
  Για το **Admission policy**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Observability for containers**
  Για το **Observability for containers**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **DevSecOps pipeline architecture**
  Για το **DevSecOps pipeline architecture**, στο πλαίσιο του **Containers, Kubernetes και DevSecOps**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Pipeline controls**
  Για το **Pipeline controls**, στο πλαίσιο του **Containers, Kubernetes και DevSecOps**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Containers, Kubernetes και DevSecOps**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε local containers ή sandbox cloud accounts που σου ανήκουν. Έλεγξε policies και artifacts read-only πριν από αλλαγές και απέφυγε δημόσια exposure στα labs.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Containers, Kubernetes και DevSecOps**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Containers, Kubernetes και DevSecOps** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 024](../../English/07-Cloud-Containers-and-Supply-Chain/24-Containers-Kubernetes-and-DevSecOps.md)

---

# Ασφάλεια AI και LLM

> **Ελληνική έκδοση — Μάθημα 025.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Η ασφάλεια δεν είναι μόνο τεχνική εκμετάλλευση. AI systems, privacy, governance, human factors και data lifecycle απαιτούν σαφείς owners, policies, consent, minimization, auditability και περιορισμό authority. Το risk πρέπει να συνδέεται με πραγματικές επιπτώσεις και όχι μόνο με severity labels.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Ασφάλεια AI και LLM**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Current landscape**
  Για το **Current landscape**, στο πλαίσιο του **Ασφάλεια AI και LLM**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Core risk families**
  Για το **Core risk families**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Prompt and context manipulation**
  Στο **Prompt and context manipulation**, ξεχώρισε model behavior από deterministic policy enforcement. Κατέγραψε untrusted inputs, tool/data permissions, retrieval provenance, output validation και human approval points.
- **Sensitive information disclosure**
  Για το **Sensitive information disclosure**, αντιμετώπισε model output ως untrusted suggestion. Βάλε deterministic authorization πριν από tool/data access, schema validation στα inputs/outputs, provenance στο retrieved context, bounded resources και human approval για irreversible ή high-impact ενέργειες.
- **Supply chain and provenance**
  Για το **Supply chain and provenance**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **Unsafe output handling**
  Για το **Unsafe output handling**, αντιμετώπισε model output ως untrusted suggestion. Βάλε deterministic authorization πριν από tool/data access, schema validation στα inputs/outputs, provenance στο retrieved context, bounded resources και human approval για irreversible ή high-impact ενέργειες.
- **Excessive agency**
  Για το **Excessive agency**, αντιμετώπισε model output ως untrusted suggestion. Βάλε deterministic authorization πριν από tool/data access, schema validation στα inputs/outputs, provenance στο retrieved context, bounded resources και human approval για irreversible ή high-impact ενέργειες.
- **Retrieval and memory risk**
  Στο **Retrieval and memory risk**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **Resource abuse**
  Για το **Resource abuse**, αντιμετώπισε model output ως untrusted suggestion. Βάλε deterministic authorization πριν από tool/data access, schema validation στα inputs/outputs, provenance στο retrieved context, bounded resources και human approval για irreversible ή high-impact ενέργειες.
- **Secure architecture pattern**
  Για το **Secure architecture pattern**, στο πλαίσιο του **Ασφάλεια AI και LLM**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Safe lab**
  Στο **Safe lab**, μετέτρεψε τη θεωρία του **Ασφάλεια AI και LLM** σε ελέγξιμα κριτήρια: τι πρέπει να μπορείς να εξηγήσεις, ποιο λάθος assumption εμφανίζεται συχνότερα, ποιο safe lab το αποκαλύπτει και ποιο retest αποδεικνύει ότι το διόρθωσες.
- **References**
  Για το **References**, ξεχώρισε normative specification από tutorial ή vendor summary. Κατέγραψε έκδοση/ημερομηνία, ποιο requirement στηρίζει το συμπέρασμα και ποιο μέρος του **Ασφάλεια AI και LLM** χρειάζεται επανέλεγχο όταν αλλάξει η πηγή.
- **AI system threat modeling**
  Στο **AI system threat modeling**, ξεχώρισε model behavior από deterministic policy enforcement. Κατέγραψε untrusted inputs, tool/data permissions, retrieval provenance, output validation και human approval points.
- **Trust boundaries for prompts and context**
  Για το **Trust boundaries for prompts and context**, αντιμετώπισε model output ως untrusted suggestion. Βάλε deterministic authorization πριν από tool/data access, schema validation στα inputs/outputs, provenance στο retrieved context, bounded resources και human approval για irreversible ή high-impact ενέργειες.
- **Indirect prompt injection**
  Για το **Indirect prompt injection**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **Tool and agent security**
  Στο **Tool and agent security**, ξεχώρισε model behavior από deterministic policy enforcement. Κατέγραψε untrusted inputs, tool/data permissions, retrieval provenance, output validation και human approval points.
- **Tool design principles**
  Για το **Tool design principles**, στο πλαίσιο του **Ασφάλεια AI και LLM**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Human approval**
  Για το **Human approval**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Retrieval-Augmented Generation security**
  Για το **Retrieval-Augmented Generation security**, αντιμετώπισε model output ως untrusted suggestion. Βάλε deterministic authorization πριν από tool/data access, schema validation στα inputs/outputs, provenance στο retrieved context, bounded resources και human approval για irreversible ή high-impact ενέργειες.
- **RAG controls**
  Στο **RAG controls**, ξεχώρισε model behavior από deterministic policy enforcement. Κατέγραψε untrusted inputs, tool/data permissions, retrieval provenance, output validation και human approval points.
- **Memory and personalization**
  Στο **Memory and personalization**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **Data leakage controls**
  Για το **Data leakage controls**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Ασφάλεια AI και LLM**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε synthetic data και role-play scenarios. Μην χρησιμοποιείς πραγματικά προσωπικά δεδομένα ή παραπλανητικές social-engineering δοκιμές χωρίς ρητή έγκριση.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Ασφάλεια AI και LLM**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Ασφάλεια AI και LLM** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 025](../../English/09-AI-GRC-Privacy-Data-and-Human-Security/25-AI-and-LLM-Security.md)

---

# Αναφορές Security Assessment και Purple Teaming

> **Ελληνική έκδοση — Μάθημα 026.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Η κατηγορία αυτή χτίζει τον τρόπο σκέψης που χρειάζεται πριν από οποιοδήποτε τεχνικό test. Η ασφάλεια αντιμετωπίζεται ως σύστημα από assets, identities, trust boundaries, δεδομένα, controls και αποδεικτικά στοιχεία. Το ζητούμενο δεν είναι να απομνημονεύσεις εργαλεία αλλά να μπορείς να εξηγήσεις τι προστατεύεται, από ποια απειλή, με ποια υπόθεση και πώς αποδεικνύεται το αποτέλεσμα.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Αναφορές Security Assessment και Purple Teaming**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Evidence quality**
  Στο **Evidence quality**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Finding anatomy**
  Για το **Finding anatomy**, στο πλαίσιο του **Αναφορές Security Assessment και Purple Teaming**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Attack paths**
  Για το **Attack paths**, στο πλαίσιο του **Αναφορές Security Assessment και Purple Teaming**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Purple teaming**
  Για το **Purple teaming**, στο πλαίσιο του **Αναφορές Security Assessment και Purple Teaming**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Exercise loop**
  Στο **Exercise loop**, όρισε συγκεκριμένο objective, owned/local scope, expected result και stop condition. Κράτησε μόνο sanitized evidence, σύγκρινε expected με observed behavior και ολοκλήρωσε με remediation και ίδιο regression test.
- **Metrics that matter**
  Για το **Metrics that matter**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Rules of engagement**
  Για το **Rules of engagement**, στο πλαίσιο του **Αναφορές Security Assessment και Purple Teaming**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Stop conditions**
  Για το **Stop conditions**, στο πλαίσιο του **Αναφορές Security Assessment και Purple Teaming**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Assessment planning**
  Για το **Assessment planning**, στο πλαίσιο του **Αναφορές Security Assessment και Purple Teaming**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Evidence standards**
  Στο **Evidence standards**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Risk rating**
  Για το **Risk rating**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Writing actionable findings**
  Για το **Writing actionable findings**, στο πλαίσιο του **Αναφορές Security Assessment και Purple Teaming**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Example finding structure**
  Για το **Example finding structure**, στο πλαίσιο του **Αναφορές Security Assessment και Purple Teaming**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Executive summary**
  Για το **Executive summary**, στο πλαίσιο του **Αναφορές Security Assessment και Purple Teaming**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Technical appendix**
  Για το **Technical appendix**, στο πλαίσιο του **Αναφορές Security Assessment και Purple Teaming**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Root-cause analysis**
  Στο **Root-cause analysis**, διατήρησε provenance και χρονικό context για κάθε artifact. Ξεχώρισε fact, inference και hypothesis, έλεγξε clock/timezone effects και μη θεωρείς το πρώτο observable event ούτε root cause ούτε αρχικό σημείο compromise χωρίς corroboration.
- **Purple-team planning**
  Για το **Purple-team planning**, στο πλαίσιο του **Αναφορές Security Assessment και Purple Teaming**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Example exercise card**
  Στο **Example exercise card**, όρισε συγκεκριμένο objective, owned/local scope, expected result και stop condition. Κράτησε μόνο sanitized evidence, σύγκρινε expected με observed behavior και ολοκλήρωσε με remediation και ίδιο regression test.
- **Retesting**
  Για το **Retesting**, δες το workflow σαν reproducible local environment: paths, package/source provenance, permissions, environment state, error handling και rollback. Στο Termux προτίμησε standard-library εργαλεία, explicit paths και δοκιμές σε harmless local files/services.
- **Metrics and program improvement**
  Για το **Metrics and program improvement**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Assessment closeout checklist**
  Για το **Assessment closeout checklist**, στο πλαίσιο του **Αναφορές Security Assessment και Purple Teaming**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Αναφορές Security Assessment και Purple Teaming**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Δούλεψε με ένα υποθετικό ή δικό σου lab. Σχεδίασε scope, assets, trust boundaries και αναμενόμενα evidence πριν αλλάξεις οτιδήποτε.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Αναφορές Security Assessment και Purple Teaming**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Αναφορές Security Assessment και Purple Teaming** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 026](../../English/01-Fundamentals-and-Methodology/26-Security-Assessment-Reporting-and-Purple-Teaming.md)

---

# Εξουσιοδοτημένα Hands-On Labs

> **Ελληνική έκδοση — Μάθημα 027.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Τα capstones μετατρέπουν γνώση σε αποδείξιμη ικανότητα. Ένα καλό project έχει scope, threat model, repeatable procedure, evidence, limitations, remediation και καθαρή τεχνική γραφή. Η ποιότητα μετριέται από το αν τρίτος μπορεί να αναπαράγει το συμπέρασμα χωρίς να μαντεύει.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Εξουσιοδοτημένα Hands-On Labs**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Lab 1 — Local attack-surface inventory**
  Στο **Lab 1 — Local attack-surface inventory**, όρισε συγκεκριμένο objective, owned/local scope, expected result και stop condition. Κράτησε μόνο sanitized evidence, σύγκρινε expected με observed behavior και ολοκλήρωσε με remediation και ίδιο regression test.
- **Lab 2 — Packet capture of your own traffic**
  Στο **Lab 2 — Packet capture of your own traffic**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.
- **Lab 3 — Web application security**
  Για το **Lab 3 — Web application security**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **Lab 4 — Authorization unit tests**
  Για το **Lab 4 — Authorization unit tests**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Lab 5 — Secure password storage**
  Για το **Lab 5 — Secure password storage**, κατέγραψε ποιος μπορεί να γράψει/διαβάσει το state, πού αποθηκεύεται, πώς προστατεύεται at rest, ποιο backup/sync behavior υπάρχει και πότε το data πρέπει να διαγράφεται ή να ανακαλείται.
- **Lab 6 — TLS inspection**
  Στο **Lab 6 — TLS inspection**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.
- **Lab 7 — Detection validation**
  Στο **Lab 7 — Detection validation**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Lab 8 — Incident timeline**
  Στο **Lab 8 — Incident timeline**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Lab 9 — Container hardening**
  Για το **Lab 9 — Container hardening**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **Lab 10 — LLM tool-boundary exercise**
  Στο **Lab 10 — LLM tool-boundary exercise**, ξεχώρισε model behavior από deterministic policy enforcement. Κατέγραψε untrusted inputs, tool/data permissions, retrieval provenance, output validation και human approval points.
- **Lab report template**
  Για το **Lab report template**, στο πλαίσιο του **Εξουσιοδοτημένα Hands-On Labs**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Building a safe lab environment**
  Στο **Building a safe lab environment**, μετέτρεψε τη θεωρία του **Εξουσιοδοτημένα Hands-On Labs** σε ελέγξιμα κριτήρια: τι πρέπει να μπορείς να εξηγήσεις, ποιο λάθος assumption εμφανίζεται συχνότερα, ποιο safe lab το αποκαλύπτει και ποιο retest αποδεικνύει ότι το διόρθωσες.
- **Lab safety checklist**
  Στο **Lab safety checklist**, μετέτρεψε τη θεωρία του **Εξουσιοδοτημένα Hands-On Labs** σε ελέγξιμα κριτήρια: τι πρέπει να μπορείς να εξηγήσεις, ποιο λάθος assumption εμφανίζεται συχνότερα, ποιο safe lab το αποκαλύπτει και ποιο retest αποδεικνύει ότι το διόρθωσες.
- **Lab 11 — Asset inventory from local evidence**
  Στο **Lab 11 — Asset inventory from local evidence**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Lab 12 — Vulnerability prioritization tabletop**
  Στο **Lab 12 — Vulnerability prioritization tabletop**, όρισε συγκεκριμένο objective, owned/local scope, expected result και stop condition. Κράτησε μόνο sanitized evidence, σύγκρινε expected με observed behavior και ολοκλήρωσε με remediation και ίδιο regression test.
- **Lab 13 — Web security headers and TLS**
  Στο **Lab 13 — Web security headers and TLS**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.
- **Lab 14 — Input validation unit tests**
  Για το **Lab 14 — Input validation unit tests**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **Lab 15 — Access-control matrix**
  Στο **Lab 15 — Access-control matrix**, όρισε συγκεκριμένο objective, owned/local scope, expected result και stop condition. Κράτησε μόνο sanitized evidence, σύγκρινε expected με observed behavior και ολοκλήρωσε με remediation και ίδιο regression test.
- **Lab 16 — API rate and quota design**
  Για το **Lab 16 — API rate and quota design**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **Lab 17 — Secret scanning in a toy repository**
  Για το **Lab 17 — Secret scanning in a toy repository**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **Lab 18 — SBOM and dependency inventory**
  Για το **Lab 18 — SBOM and dependency inventory**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **Lab 19 — Identity lifecycle simulation**
  Για το **Lab 19 — Identity lifecycle simulation**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Εξουσιοδοτημένα Hands-On Labs**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χτίσε portfolio μόνο με δικά σου ή ρητά εξουσιοδοτημένα labs. Αφαίρεσε secrets και προσωπικά δεδομένα πριν δημοσιεύσεις artifacts.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Εξουσιοδοτημένα Hands-On Labs**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Εξουσιοδοτημένα Hands-On Labs** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 027](../../English/11-Labs-Capstones-and-Career/27-Authorized-Hands-On-Labs.md)

---

# Βάσεις Termux και Android Linux

> **Ελληνική έκδοση — Μάθημα 028.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Το Termux προσφέρει Linux-like userland πάνω στο Android, αλλά δεν είναι πλήρης desktop διανομή ούτε παρακάμπτει το Android security model. Για αξιόπιστη χρήση πρέπει να κατανοείς storage permissions, package management, process lifetime, networking, SSH, Python environments και τα όρια που επιβάλλει το Android sandbox.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Βάσεις Termux και Android Linux**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **What Termux actually is**
  Για το **What Termux actually is**, δες το workflow σαν reproducible local environment: paths, package/source provenance, permissions, environment state, error handling και rollback. Στο Termux προτίμησε standard-library εργαλεία, explicit paths και δοκιμές σε harmless local files/services.
- **Installation and update hygiene**
  Για το **Installation and update hygiene**, στο πλαίσιο του **Βάσεις Termux και Android Linux**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Storage model**
  Για το **Storage model**, κατέγραψε ποιος μπορεί να γράψει/διαβάσει το state, πού αποθηκεύεται, πώς προστατεύεται at rest, ποιο backup/sync behavior υπάρχει και πότε το data πρέπει να διαγράφεται ή να ανακαλείται.
- **Core shell navigation**
  Για το **Core shell navigation**, δες το workflow σαν reproducible local environment: paths, package/source provenance, permissions, environment state, error handling και rollback. Στο Termux προτίμησε standard-library εργαλεία, explicit paths και δοκιμές σε harmless local files/services.
- **Files, permissions, and executables**
  Για το **Files, permissions, and executables**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Environment variables**
  Για το **Environment variables**, δες το workflow σαν reproducible local environment: paths, package/source provenance, permissions, environment state, error handling και rollback. Στο Termux προτίμησε standard-library εργαλεία, explicit paths και δοκιμές σε harmless local files/services.
- **Package management fundamentals**
  Για το **Package management fundamentals**, δες το workflow σαν reproducible local environment: paths, package/source provenance, permissions, environment state, error handling και rollback. Στο Termux προτίμησε standard-library εργαλεία, explicit paths και δοκιμές σε harmless local files/services.
- **Processes and jobs**
  Στο **Processes and jobs**, χαρτογράφησε process → socket → interface/route → peer και ποια identity/host-key/DNS πληροφορία εμπιστεύεται κάθε βήμα. Ξεκίνα από loopback ή δικό σου SSH endpoint και επιβεβαίωσε listening scope, authentication και logs.
- **Networking basics in Termux**
  Για το **Networking basics in Termux**, δες το workflow σαν reproducible local environment: paths, package/source provenance, permissions, environment state, error handling και rollback. Στο Termux προτίμησε standard-library εργαλεία, explicit paths και δοκιμές σε harmless local files/services.
- **Android sandboxing and root**
  Στο **Android sandboxing and root**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.
- **Termux add-ons**
  Για το **Termux add-ons**, δες το workflow σαν reproducible local environment: paths, package/source provenance, permissions, environment state, error handling και rollback. Στο Termux προτίμησε standard-library εργαλεία, explicit paths και δοκιμές σε harmless local files/services.
- **Baseline setup lesson**
  Για το **Baseline setup lesson**, ξεκίνα από observable behavior και διαθέσιμα data sources, όχι από technique ID μόνο. Γράψε detection hypothesis, required fields, expected benign collisions, tuning strategy και validation event ώστε η κάλυψη να είναι μετρήσιμη.
- **Common mistakes**
  Στο **Common mistakes**, μετέτρεψε τη θεωρία του **Βάσεις Termux και Android Linux** σε ελέγξιμα κριτήρια: τι πρέπει να μπορείς να εξηγήσεις, ποιο λάθος assumption εμφανίζεται συχνότερα, ποιο safe lab το αποκαλύπτει και ποιο retest αποδεικνύει ότι το διόρθωσες.
- **Mini lab — Build a known-good Termux baseline**
  Για το **Mini lab — Build a known-good Termux baseline**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **Primary references**
  Για το **Primary references**, ξεχώρισε normative specification από tutorial ή vendor summary. Κατέγραψε έκδοση/ημερομηνία, ποιο requirement στηρίζει το συμπέρασμα και ποιο μέρος του **Βάσεις Termux και Android Linux** χρειάζεται επανέλεγχο όταν αλλάξει η πηγή.
- **Practical Termux foundation drills**
  Στο **Practical Termux foundation drills**, όρισε συγκεκριμένο objective, owned/local scope, expected result και stop condition. Κράτησε μόνο sanitized evidence, σύγκρινε expected με observed behavior και ολοκλήρωσε με remediation και ίδιο regression test.
- **Drill 1 — Know your environment**
  Στο **Drill 1 — Know your environment**, όρισε συγκεκριμένο objective, owned/local scope, expected result και stop condition. Κράτησε μόνο sanitized evidence, σύγκρινε expected με observed behavior και ολοκλήρωσε με remediation και ίδιο regression test.
- **Drill 2 — Permission reasoning**
  Για το **Drill 2 — Permission reasoning**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Drill 3 — Rebuildability**
  Στο **Drill 3 — Rebuildability**, όρισε συγκεκριμένο objective, owned/local scope, expected result και stop condition. Κράτησε μόνο sanitized evidence, σύγκρινε expected με observed behavior και ολοκλήρωσε με remediation και ίδιο regression test.
- **Android-specific guidance**
  Στο **Android-specific guidance**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Βάσεις Termux και Android Linux**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Κράτησε όλα τα labs μέσα στο δικό σου τηλέφωνο, localhost ή συστήματα που ελέγχεις. Ξεκίνα με read-only commands και διατήρησε backups για scripts/configuration.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Βάσεις Termux και Android Linux**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Βάσεις Termux και Android Linux** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 028](../../English/10-Termux-and-Security-Automation/28-Termux-Foundations-and-Android-Linux.md)

---

# Ροή Εργασίας Termux, Python, Git και Αυτοματοποίηση

> **Ελληνική έκδοση — Μάθημα 029.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Το Termux προσφέρει Linux-like userland πάνω στο Android, αλλά δεν είναι πλήρης desktop διανομή ούτε παρακάμπτει το Android security model. Για αξιόπιστη χρήση πρέπει να κατανοείς storage permissions, package management, process lifetime, networking, SSH, Python environments και τα όρια που επιβάλλει το Android sandbox.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Ροή Εργασίας Termux, Python, Git και Αυτοματοποίηση**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **A simple workspace model**
  Για το **A simple workspace model**, δες το workflow σαν reproducible local environment: paths, package/source provenance, permissions, environment state, error handling και rollback. Στο Termux προτίμησε standard-library εργαλεία, explicit paths και δοκιμές σε harmless local files/services.
- **Git fundamentals**
  Για το **Git fundamentals**, δες το workflow σαν reproducible local environment: paths, package/source provenance, permissions, environment state, error handling και rollback. Στο Termux προτίμησε standard-library εργαλεία, explicit paths και δοκιμές σε harmless local files/services.
- **SSH keys for Git hosting**
  Για το **SSH keys for Git hosting**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **Python in Termux**
  Για το **Python in Termux**, δες το workflow σαν reproducible local environment: paths, package/source provenance, permissions, environment state, error handling και rollback. Στο Termux προτίμησε standard-library εργαλεία, explicit paths και δοκιμές σε harmless local files/services.
- **Standard-library-first automation**
  Για το **Standard-library-first automation**, ξεχώρισε normative specification από tutorial ή vendor summary. Κατέγραψε έκδοση/ημερομηνία, ποιο requirement στηρίζει το συμπέρασμα και ποιο μέρος του **Ροή Εργασίας Termux, Python, Git και Αυτοματοποίηση** χρειάζεται επανέλεγχο όταν αλλάξει η πηγή.
- **Shell scripting discipline**
  Για το **Shell scripting discipline**, δες το workflow σαν reproducible local environment: paths, package/source provenance, permissions, environment state, error handling και rollback. Στο Termux προτίμησε standard-library εργαλεία, explicit paths και δοκιμές σε harmless local files/services.
- **Configuration versus code**
  Για το **Configuration versus code**, ακολούθησε data/control flow από source σε sink, σημείωσε validation και ownership assumptions και έλεγξε πού εφαρμόζεται enforcement. Χρησιμοποίησε tests και static/runtime evidence για να ξεχωρίσεις root cause από απλό code smell.
- **Logging**
  Στο **Logging**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Safe subprocess use**
  Για το **Safe subprocess use**, δες το workflow σαν reproducible local environment: paths, package/source provenance, permissions, environment state, error handling και rollback. Στο Termux προτίμησε standard-library εργαλεία, explicit paths και δοκιμές σε harmless local files/services.
- **Data formats**
  Για το **Data formats**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Backups**
  Για το **Backups**, δες το workflow σαν reproducible local environment: paths, package/source provenance, permissions, environment state, error handling και rollback. Στο Termux προτίμησε standard-library εργαλεία, explicit paths και δοκιμές σε harmless local files/services.
- **Termux-friendly editor workflow**
  Για το **Termux-friendly editor workflow**, δες το workflow σαν reproducible local environment: paths, package/source provenance, permissions, environment state, error handling και rollback. Στο Termux προτίμησε standard-library εργαλεία, explicit paths και δοκιμές σε harmless local files/services.
- **Automation project template**
  Για το **Automation project template**, δες το workflow σαν reproducible local environment: paths, package/source provenance, permissions, environment state, error handling και rollback. Στο Termux προτίμησε standard-library εργαλεία, explicit paths και δοκιμές σε harmless local files/services.
- **Mini lab — Build a local file inventory tool**
  Για το **Mini lab — Build a local file inventory tool**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **Maintenance checklist**
  Για το **Maintenance checklist**, στο πλαίσιο του **Ροή Εργασίας Termux, Python, Git και Αυτοματοποίηση**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Practical workflow drills**
  Στο **Practical workflow drills**, όρισε συγκεκριμένο objective, owned/local scope, expected result και stop condition. Κράτησε μόνο sanitized evidence, σύγκρινε expected με observed behavior και ολοκλήρωσε με remediation και ίδιο regression test.
- **Project isolation**
  Για το **Project isolation**, δες το workflow σαν reproducible local environment: paths, package/source provenance, permissions, environment state, error handling και rollback. Στο Termux προτίμησε standard-library εργαλεία, explicit paths και δοκιμές σε harmless local files/services.
- **Python error-handling exercise**
  Στο **Python error-handling exercise**, όρισε συγκεκριμένο objective, owned/local scope, expected result και stop condition. Κράτησε μόνο sanitized evidence, σύγκρινε expected με observed behavior και ολοκλήρωσε με remediation και ίδιο regression test.
- **Git recovery exercise**
  Για το **Git recovery exercise**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Automation design guidance**
  Για το **Automation design guidance**, δες το workflow σαν reproducible local environment: paths, package/source provenance, permissions, environment state, error handling και rollback. Στο Termux προτίμησε standard-library εργαλεία, explicit paths και δοκιμές σε harmless local files/services.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Ροή Εργασίας Termux, Python, Git και Αυτοματοποίηση**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Κράτησε όλα τα labs μέσα στο δικό σου τηλέφωνο, localhost ή συστήματα που ελέγχεις. Ξεκίνα με read-only commands και διατήρησε backups για scripts/configuration.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Ροή Εργασίας Termux, Python, Git και Αυτοματοποίηση**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Ροή Εργασίας Termux, Python, Git και Αυτοματοποίηση** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 029](../../English/10-Termux-and-Security-Automation/29-Termux-Workflow-Python-Git-and-Automation.md)

---

# Δικτύωση Termux, SSH και Τοπικές Υπηρεσίες

> **Ελληνική έκδοση — Μάθημα 030.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Το Termux προσφέρει Linux-like userland πάνω στο Android, αλλά δεν είναι πλήρης desktop διανομή ούτε παρακάμπτει το Android security model. Για αξιόπιστη χρήση πρέπει να κατανοείς storage permissions, package management, process lifetime, networking, SSH, Python environments και τα όρια που επιβάλλει το Android sandbox.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Δικτύωση Termux, SSH και Τοπικές Υπηρεσίες**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Networking mental model**
  Στο **Networking mental model**, χαρτογράφησε process → socket → interface/route → peer και ποια identity/host-key/DNS πληροφορία εμπιστεύεται κάθε βήμα. Ξεκίνα από loopback ή δικό σου SSH endpoint και επιβεβαίωσε listening scope, authentication και logs.
- **Local interfaces and routes**
  Στο **Local interfaces and routes**, χαρτογράφησε process → socket → interface/route → peer και ποια identity/host-key/DNS πληροφορία εμπιστεύεται κάθε βήμα. Ξεκίνα από loopback ή δικό σου SSH endpoint και επιβεβαίωσε listening scope, authentication και logs.
- **DNS basics**
  Στο **DNS basics**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.
- **HTTP and HTTPS inspection**
  Στο **HTTP and HTTPS inspection**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.
- **Running a localhost-only development service**
  Στο **Running a localhost-only development service**, χαρτογράφησε process → socket → interface/route → peer και ποια identity/host-key/DNS πληροφορία εμπιστεύεται κάθε βήμα. Ξεκίνα από loopback ή δικό σου SSH endpoint και επιβεβαίωσε listening scope, authentication και logs.
- **SSH concepts**
  Στο **SSH concepts**, χαρτογράφησε process → socket → interface/route → peer και ποια identity/host-key/DNS πληροφορία εμπιστεύεται κάθε βήμα. Ξεκίνα από loopback ή δικό σου SSH endpoint και επιβεβαίωσε listening scope, authentication και logs.
- **Host-key verification**
  Για το **Host-key verification**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **Port forwarding concepts**
  Στο **Port forwarding concepts**, χαρτογράφησε process → socket → interface/route → peer και ποια identity/host-key/DNS πληροφορία εμπιστεύεται κάθε βήμα. Ξεκίνα από loopback ή δικό σου SSH endpoint και επιβεβαίωσε listening scope, authentication και logs.
- **File transfer**
  Στο **File transfer**, χαρτογράφησε process → socket → interface/route → peer και ποια identity/host-key/DNS πληροφορία εμπιστεύεται κάθε βήμα. Ξεκίνα από loopback ή δικό σου SSH endpoint και επιβεβαίωσε listening scope, authentication και logs.
- **Local service inventory**
  Στο **Local service inventory**, χαρτογράφησε process → socket → interface/route → peer και ποια identity/host-key/DNS πληροφορία εμπιστεύεται κάθε βήμα. Ξεκίνα από loopback ή δικό σου SSH endpoint και επιβεβαίωσε listening scope, authentication και logs.
- **VPNs and Android**
  Στο **VPNs and Android**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.
- **Wireless limitations**
  Στο **Wireless limitations**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.
- **Mini lab — Local service map**
  Στο **Mini lab — Local service map**, όρισε συγκεκριμένο objective, owned/local scope, expected result και stop condition. Κράτησε μόνο sanitized evidence, σύγκρινε expected με observed behavior και ολοκλήρωσε με remediation και ίδιο regression test.
- **Mini lab — SSH trust checklist**
  Στο **Mini lab — SSH trust checklist**, όρισε συγκεκριμένο objective, owned/local scope, expected result και stop condition. Κράτησε μόνο sanitized evidence, σύγκρινε expected με observed behavior και ολοκλήρωσε με remediation και ίδιο regression test.
- **Practical networking drills in Termux**
  Στο **Practical networking drills in Termux**, όρισε συγκεκριμένο objective, owned/local scope, expected result και stop condition. Κράτησε μόνο sanitized evidence, σύγκρινε expected με observed behavior και ολοκλήρωσε με remediation και ίδιο regression test.
- **Loopback first**
  Στο **Loopback first**, χαρτογράφησε process → socket → interface/route → peer και ποια identity/host-key/DNS πληροφορία εμπιστεύεται κάθε βήμα. Ξεκίνα από loopback ή δικό σου SSH endpoint και επιβεβαίωσε listening scope, authentication και logs.
- **SSH administration checklist**
  Στο **SSH administration checklist**, χαρτογράφησε process → socket → interface/route → peer και ποια identity/host-key/DNS πληροφορία εμπιστεύεται κάθε βήμα. Ξεκίνα από loopback ή δικό σου SSH endpoint και επιβεβαίωσε listening scope, authentication και logs.
- **Name-resolution exercise**
  Στο **Name-resolution exercise**, όρισε συγκεκριμένο objective, owned/local scope, expected result και stop condition. Κράτησε μόνο sanitized evidence, σύγκρινε expected με observed behavior και ολοκλήρωσε με remediation και ίδιο regression test.
- **Mobile networking limitations**
  Στο **Mobile networking limitations**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Δικτύωση Termux, SSH και Τοπικές Υπηρεσίες**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Κράτησε όλα τα labs μέσα στο δικό σου τηλέφωνο, localhost ή συστήματα που ελέγχεις. Ξεκίνα με read-only commands και διατήρησε backups για scripts/configuration.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Δικτύωση Termux, SSH και Τοπικές Υπηρεσίες**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Δικτύωση Termux, SSH και Τοπικές Υπηρεσίες** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 030](../../English/10-Termux-and-Security-Automation/30-Termux-Networking-SSH-and-Local-Services.md)

---

# Λειτουργία Security Lab και Troubleshooting στο Termux

> **Ελληνική έκδοση — Μάθημα 031.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Το Termux προσφέρει Linux-like userland πάνω στο Android, αλλά δεν είναι πλήρης desktop διανομή ούτε παρακάμπτει το Android security model. Για αξιόπιστη χρήση πρέπει να κατανοείς storage permissions, package management, process lifetime, networking, SSH, Python environments και τα όρια που επιβάλλει το Android sandbox.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Λειτουργία Security Lab και Troubleshooting στο Termux**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Lab design principles**
  Για το **Lab design principles**, στο πλαίσιο του **Λειτουργία Security Lab και Troubleshooting στο Termux**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **What Termux is excellent for**
  Για το **What Termux is excellent for**, δες το workflow σαν reproducible local environment: paths, package/source provenance, permissions, environment state, error handling και rollback. Στο Termux προτίμησε standard-library εργαλεία, explicit paths και δοκιμές σε harmless local files/services.
- **What often needs a different environment**
  Για το **What often needs a different environment**, στο πλαίσιο του **Λειτουργία Security Lab και Troubleshooting στο Termux**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Proot distributions**
  Για το **Proot distributions**, στο πλαίσιο του **Λειτουργία Security Lab και Troubleshooting στο Termux**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Dependency troubleshooting**
  Για το **Dependency troubleshooting**, ακολούθησε data/control flow από source σε sink, σημείωσε validation και ownership assumptions και έλεγξε πού εφαρμόζεται enforcement. Χρησιμοποίησε tests και static/runtime evidence για να ξεχωρίσεις root cause από απλό code smell.
- **Repository troubleshooting**
  Για το **Repository troubleshooting**, δες το workflow σαν reproducible local environment: paths, package/source provenance, permissions, environment state, error handling και rollback. Στο Termux προτίμησε standard-library εργαλεία, explicit paths και δοκιμές σε harmless local files/services.
- **Python troubleshooting**
  Για το **Python troubleshooting**, δες το workflow σαν reproducible local environment: paths, package/source provenance, permissions, environment state, error handling και rollback. Στο Termux προτίμησε standard-library εργαλεία, explicit paths και δοκιμές σε harmless local files/services.
- **Storage troubleshooting**
  Για το **Storage troubleshooting**, κατέγραψε ποιος μπορεί να γράψει/διαβάσει το state, πού αποθηκεύεται, πώς προστατεύεται at rest, ποιο backup/sync behavior υπάρχει και πότε το data πρέπει να διαγράφεται ή να ανακαλείται.
- **Long-running processes**
  Στο **Long-running processes**, χαρτογράφησε process → socket → interface/route → peer και ποια identity/host-key/DNS πληροφορία εμπιστεύεται κάθε βήμα. Ξεκίνα από loopback ή δικό σου SSH endpoint και επιβεβαίωσε listening scope, authentication και logs.
- **Safe local vulnerable applications**
  Για το **Safe local vulnerable applications**, στο πλαίσιο του **Λειτουργία Security Lab και Troubleshooting στο Termux**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Note-taking workflow**
  Για το **Note-taking workflow**, στο πλαίσιο του **Λειτουργία Security Lab και Troubleshooting στο Termux**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **The Hacking Guide Project search tool**
  Για το **The Hacking Guide Project search tool**, στο πλαίσιο του **Λειτουργία Security Lab και Troubleshooting στο Termux**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Termux capstone — Portable defensive notebook**
  Στο **Termux capstone — Portable defensive notebook**, όρισε συγκεκριμένο objective, owned/local scope, expected result και stop condition. Κράτησε μόνο sanitized evidence, σύγκρινε expected με observed behavior και ολοκλήρωσε με remediation και ίδιο regression test.
- **Troubleshooting decision tree**
  Για το **Troubleshooting decision tree**, στο πλαίσιο του **Λειτουργία Security Lab και Troubleshooting στο Termux**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Safety rule**
  Στο **Safety rule**, μετέτρεψε τη θεωρία του **Λειτουργία Security Lab και Troubleshooting στο Termux** σε ελέγξιμα κριτήρια: τι πρέπει να μπορείς να εξηγήσεις, ποιο λάθος assumption εμφανίζεται συχνότερα, ποιο safe lab το αποκαλύπτει και ποιο retest αποδεικνύει ότι το διόρθωσες.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Λειτουργία Security Lab και Troubleshooting στο Termux**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Κράτησε όλα τα labs μέσα στο δικό σου τηλέφωνο, localhost ή συστήματα που ελέγχεις. Ξεκίνα με read-only commands και διατήρησε backups για scripts/configuration.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Λειτουργία Security Lab και Troubleshooting στο Termux**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Λειτουργία Security Lab και Troubleshooting στο Termux** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 031](../../English/10-Termux-and-Security-Automation/31-Termux-Security-Lab-Operations-and-Troubleshooting.md)

---

# Ασφάλεια Windows και Active Directory

> **Ελληνική έκδοση — Μάθημα 032.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Identity και cryptography είναι μηχανισμοί μεταφοράς εμπιστοσύνης. Authentication απαντά ποιος παρουσιάζει ένα credential, authorization τι επιτρέπεται να κάνει, ενώ cryptography προστατεύει συγκεκριμένες ιδιότητες δεδομένων και πρωτοκόλλων. Κλειδιά, tokens, certificates, federation metadata και policy engines είναι όλα authority-bearing artifacts και χρειάζονται σαφή lifecycle.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Ασφάλεια Windows και Active Directory**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Active Directory mental model**
  Για το **Active Directory mental model**, στο πλαίσιο του **Ασφάλεια Windows και Active Directory**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Authentication concepts**
  Για το **Authentication concepts**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Privileged identities**
  Για το **Privileged identities**, στο πλαίσιο του **Ασφάλεια Windows και Active Directory**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Group Policy**
  Για το **Group Policy**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Service accounts**
  Για το **Service accounts**, στο πλαίσιο του **Ασφάλεια Windows και Active Directory**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Local administrator risk**
  Για το **Local administrator risk**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Delegation and ACL review**
  Για το **Delegation and ACL review**, στο πλαίσιο του **Ασφάλεια Windows και Active Directory**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Certificate services**
  Για το **Certificate services**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **Windows logging**
  Στο **Windows logging**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Hardening priorities**
  Για το **Hardening priorities**, στο πλαίσιο του **Ασφάλεια Windows και Active Directory**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Authorized lab**
  Για το **Authorized lab**, στο πλαίσιο του **Ασφάλεια Windows και Active Directory**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Windows security model in more depth**
  Για το **Windows security model in more depth**, στο πλαίσιο του **Ασφάλεια Windows και Active Directory**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Identity tiers**
  Για το **Identity tiers**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Authentication and domain dependencies**
  Για το **Authentication and domain dependencies**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Logging baseline**
  Στο **Logging baseline**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Hardening questions**
  Για το **Hardening questions**, στο πλαίσιο του **Ασφάλεια Windows και Active Directory**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Ασφάλεια Windows και Active Directory**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε synthetic identities, test certificates και local identity providers. Χαρτογράφησε issuer, subject, audience, permissions, lifetime, rotation και revocation χωρίς να αποθηκεύεις πραγματικά secrets.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Ασφάλεια Windows και Active Directory**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Ασφάλεια Windows και Active Directory** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 032](../../English/06-Identity-Cryptography-and-Trust/32-Windows-and-Active-Directory-Security.md)

---

# Ασφάλεια και Hardening Linux

> **Ελληνική έκδοση — Μάθημα 033.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Η ασφάλεια συστημάτων βασίζεται στα πραγματικά boundaries του λειτουργικού: processes, memory mappings, privilege levels, handles/file descriptors, executable loading, syscalls, services και telemetry. Σε reverse engineering και vulnerability research το σημαντικό είναι να συνδέεις συμπεριφορά υψηλού επιπέδου με χαμηλού επιπέδου state χωρίς να συμπεραίνεις περισσότερα από όσα δείχνουν τα δεδομένα.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Ασφάλεια και Hardening Linux**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Ασφάλεια model**
  Για το **Ασφάλεια model**, στο πλαίσιο του **Ασφάλεια και Hardening Linux**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Accounts and privilege**
  Για το **Accounts and privilege**, κατέγραψε Linux UID/GID/capabilities, namespace membership, syscall/filesystem boundary και LSM/seccomp policy. Έλεγξε effective privilege μέσα σε disposable VM/container και χρησιμοποίησε `/proc`, audit/logging και configuration diff ως evidence.
- **Filesystem permissions**
  Για το **Filesystem permissions**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Services**
  Για το **Services**, χαρτογράφησε Windows security principal, token/privileges, object ACL ή service/IPC boundary και το audit/ETW evidence που δείχνει την απόφαση πρόσβασης. Δούλεψε σε disposable Windows VM και έλεγξε effective authority, όχι μόνο configuration text.
- **SSH hardening**
  Στο **SSH hardening**, χαρτογράφησε process → socket → interface/route → peer και ποια identity/host-key/DNS πληροφορία εμπιστεύεται κάθε βήμα. Ξεκίνα από loopback ή δικό σου SSH endpoint και επιβεβαίωσε listening scope, authentication και logs.
- **Software updates**
  Για το **Software updates**, κατέγραψε Linux UID/GID/capabilities, namespace membership, syscall/filesystem boundary και LSM/seccomp policy. Έλεγξε effective privilege μέσα σε disposable VM/container και χρησιμοποίησε `/proc`, audit/logging και configuration diff ως evidence.
- **Mandatory access control**
  Για το **Mandatory access control**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Linux capabilities**
  Για το **Linux capabilities**, κατέγραψε Linux UID/GID/capabilities, namespace membership, syscall/filesystem boundary και LSM/seccomp policy. Έλεγξε effective privilege μέσα σε disposable VM/container και χρησιμοποίησε `/proc`, audit/logging και configuration diff ως evidence.
- **Containers do not replace host hardening**
  Για το **Containers do not replace host hardening**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **Logging and time**
  Στο **Logging and time**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Integrity monitoring**
  Για το **Integrity monitoring**, κατέγραψε Linux UID/GID/capabilities, namespace membership, syscall/filesystem boundary και LSM/seccomp policy. Έλεγξε effective privilege μέσα σε disposable VM/container και χρησιμοποίησε `/proc`, audit/logging και configuration diff ως evidence.
- **Backups**
  Για το **Backups**, δες το workflow σαν reproducible local environment: paths, package/source provenance, permissions, environment state, error handling και rollback. Στο Termux προτίμησε standard-library εργαλεία, explicit paths και δοκιμές σε harmless local files/services.
- **Safe review commands**
  Για το **Safe review commands**, κατέγραψε Linux UID/GID/capabilities, namespace membership, syscall/filesystem boundary και LSM/seccomp policy. Έλεγξε effective privilege μέσα σε disposable VM/container και χρησιμοποίησε `/proc`, audit/logging και configuration diff ως evidence.
- **Hardening checklist**
  Για το **Hardening checklist**, στο πλαίσιο του **Ασφάλεια και Hardening Linux**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Authorized lab**
  Για το **Authorized lab**, στο πλαίσιο του **Ασφάλεια και Hardening Linux**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Linux hardening in more depth**
  Για το **Linux hardening in more depth**, στο πλαίσιο του **Ασφάλεια και Hardening Linux**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Services and network exposure**
  Στο **Services and network exposure**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.
- **Filesystem and secrets**
  Για το **Filesystem and secrets**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **Updates and reboot reality**
  Για το **Updates and reboot reality**, ακολούθησε την αλυσίδα trust από immutable/early-boot state μέχρι OS/application. Έλεγξε measured/verified state, key custody, update authorization, anti-rollback και τι αλλάζει όταν ο attacker έχει φυσική πρόσβαση.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Ασφάλεια και Hardening Linux**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Δούλεψε σε disposable VM ή local test binary. Προτίμησε harmless toy programs, sanitizers, debuggers και read-only inspection. Μην μετατρέπεις crash analysis σε weaponized exploitation.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Ασφάλεια και Hardening Linux**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Ασφάλεια και Hardening Linux** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 033](../../English/03-Systems-Malware-and-Reverse-Engineering/33-Linux-Security-and-Hardening.md)

---

# Threat Intelligence και OSINT

> **Ελληνική έκδοση — Μάθημα 034.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Blue-team εργασία σημαίνει να μετατρέπεις telemetry σε τεκμηριωμένα συμπεράσματα. Ένα alert δεν είναι απόδειξη από μόνο του. Χρειάζεται timeline, identity context, process/network relationships, data provenance και κατανόηση του τι δεν καταγράφεται. Η ανθεκτικότητα επεκτείνεται από detection μέχρι containment, recovery και verification.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Threat Intelligence και OSINT**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Intelligence versus information**
  Στο **Intelligence versus information**, ξεχώρισε raw information από assessed intelligence. Βαθμολόγησε source reliability και information credibility, σημείωσε timestamps/provenance, απέφυγε attribution χωρίς επαρκές evidence και σύνδεσε το αποτέλεσμα με συγκεκριμένη defensive decision.
- **Intelligence cycle**
  Στο **Intelligence cycle**, ξεχώρισε raw information από assessed intelligence. Βαθμολόγησε source reliability και information credibility, σημείωσε timestamps/provenance, απέφυγε attribution χωρίς επαρκές evidence και σύνδεσε το αποτέλεσμα με συγκεκριμένη defensive decision.
- **OSINT scope**
  Στο **OSINT scope**, ξεχώρισε raw information από assessed intelligence. Βαθμολόγησε source reliability και information credibility, σημείωσε timestamps/provenance, απέφυγε attribution χωρίς επαρκές evidence και σύνδεσε το αποτέλεσμα με συγκεκριμένη defensive decision.
- **Source evaluation**
  Στο **Source evaluation**, ξεχώρισε raw information από assessed intelligence. Βαθμολόγησε source reliability και information credibility, σημείωσε timestamps/provenance, απέφυγε attribution χωρίς επαρκές evidence και σύνδεσε το αποτέλεσμα με συγκεκριμένη defensive decision.
- **Threat intelligence layers**
  Στο **Threat intelligence layers**, ξεχώρισε raw information από assessed intelligence. Βαθμολόγησε source reliability και information credibility, σημείωσε timestamps/provenance, απέφυγε attribution χωρίς επαρκές evidence και σύνδεσε το αποτέλεσμα με συγκεκριμένη defensive decision.
- **ATT&CK as a knowledge base**
  Στο **ATT&CK as a knowledge base**, ξεχώρισε raw information από assessed intelligence. Βαθμολόγησε source reliability και information credibility, σημείωσε timestamps/provenance, απέφυγε attribution χωρίς επαρκές evidence και σύνδεσε το αποτέλεσμα με συγκεκριμένη defensive decision.
- **Indicators of compromise**
  Στο **Indicators of compromise**, ξεχώρισε raw information από assessed intelligence. Βαθμολόγησε source reliability και information credibility, σημείωσε timestamps/provenance, απέφυγε attribution χωρίς επαρκές evidence και σύνδεσε το αποτέλεσμα με συγκεκριμένη defensive decision.
- **Vulnerability intelligence**
  Στο **Vulnerability intelligence**, ξεχώρισε raw information από assessed intelligence. Βαθμολόγησε source reliability και information credibility, σημείωσε timestamps/provenance, απέφυγε attribution χωρίς επαρκές evidence και σύνδεσε το αποτέλεσμα με συγκεκριμένη defensive decision.
- **Domain and infrastructure research**
  Στο **Domain and infrastructure research**, ξεχώρισε raw information από assessed intelligence. Βαθμολόγησε source reliability και information credibility, σημείωσε timestamps/provenance, απέφυγε attribution χωρίς επαρκές evidence και σύνδεσε το αποτέλεσμα με συγκεκριμένη defensive decision.
- **Social-media verification**
  Στο **Social-media verification**, ξεχώρισε raw information από assessed intelligence. Βαθμολόγησε source reliability και information credibility, σημείωσε timestamps/provenance, απέφυγε attribution χωρίς επαρκές evidence και σύνδεσε το αποτέλεσμα με συγκεκριμένη defensive decision.
- **Intelligence writing**
  Στο **Intelligence writing**, ξεχώρισε raw information από assessed intelligence. Βαθμολόγησε source reliability και information credibility, σημείωσε timestamps/provenance, απέφυγε attribution χωρίς επαρκές evidence και σύνδεσε το αποτέλεσμα με συγκεκριμένη defensive decision.
- **Safe OSINT lab**
  Στο **Safe OSINT lab**, ξεχώρισε raw information από assessed intelligence. Βαθμολόγησε source reliability και information credibility, σημείωσε timestamps/provenance, απέφυγε attribution χωρίς επαρκές evidence και σύνδεσε το αποτέλεσμα με συγκεκριμένη defensive decision.
- **Primary references**
  Για το **Primary references**, ξεχώρισε normative specification από tutorial ή vendor summary. Κατέγραψε έκδοση/ημερομηνία, ποιο requirement στηρίζει το συμπέρασμα και ποιο μέρος του **Threat Intelligence και OSINT** χρειάζεται επανέλεγχο όταν αλλάξει η πηγή.
- **Intelligence quality and analysis**
  Στο **Intelligence quality and analysis**, ξεχώρισε raw information από assessed intelligence. Βαθμολόγησε source reliability και information credibility, σημείωσε timestamps/provenance, απέφυγε attribution χωρίς επαρκές evidence και σύνδεσε το αποτέλεσμα με συγκεκριμένη defensive decision.
- **Source grading**
  Στο **Source grading**, ξεχώρισε raw information από assessed intelligence. Βαθμολόγησε source reliability και information credibility, σημείωσε timestamps/provenance, απέφυγε attribution χωρίς επαρκές evidence και σύνδεσε το αποτέλεσμα με συγκεκριμένη defensive decision.
- **Indicators versus behaviors**
  Στο **Indicators versus behaviors**, ξεχώρισε raw information από assessed intelligence. Βαθμολόγησε source reliability και information credibility, σημείωσε timestamps/provenance, απέφυγε attribution χωρίς επαρκές evidence και σύνδεσε το αποτέλεσμα με συγκεκριμένη defensive decision.
- **Privacy boundary**
  Για το **Privacy boundary**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Threat Intelligence και OSINT**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε synthetic logs και harmless local events. Κατέγραψε expected evidence πριν το test και σύγκρινε με ό,τι πραγματικά συλλέχθηκε.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Threat Intelligence και OSINT**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Threat Intelligence και OSINT** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 034](../../English/08-Blue-Team-IR-Forensics-and-Resilience/34-Threat-Intelligence-and-OSINT.md)

---

# Ασφάλεια Email, DNS και Domains

> **Ελληνική έκδοση — Μάθημα 035.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Τα δίκτυα είναι κατανεμημένα state machines. Routing, neighbor discovery, DNS, TCP/UDP, wireless authentication και middleboxes δημιουργούν διαφορετικά trust boundaries. Για σωστή ανάλυση χρειάζεται να ξεχωρίζεις control plane από data plane, local-link μηχανισμούς από routed traffic και observation από active interference.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Ασφάλεια Email, DNS και Domains**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Why domains are security-critical**
  Για το **Why domains are security-critical**, στο πλαίσιο του **Ασφάλεια Email, DNS και Domains**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Registrar security**
  Για το **Registrar security**, στο πλαίσιο του **Ασφάλεια Email, DNS και Domains**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **DNS fundamentals**
  Στο **DNS fundamentals**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.
- **DNSSEC**
  Για το **DNSSEC**, στο πλαίσιο του **Ασφάλεια Email, DNS και Domains**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Email authentication**
  Για το **Email authentication**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **MTA-STS and TLS reporting**
  Στο **MTA-STS and TLS reporting**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.
- **Certificate management**
  Για το **Certificate management**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **Subdomain lifecycle**
  Για το **Subdomain lifecycle**, στο πλαίσιο του **Ασφάλεια Email, DNS και Domains**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Defensive domain monitoring**
  Για το **Defensive domain monitoring**, στο πλαίσιο του **Ασφάλεια Email, DNS και Domains**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Phishing defense**
  Για το **Phishing defense**, στο πλαίσιο του **Ασφάλεια Email, DNS και Domains**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Safe lab**
  Στο **Safe lab**, μετέτρεψε τη θεωρία του **Ασφάλεια Email, DNS και Domains** σε ελέγξιμα κριτήρια: τι πρέπει να μπορείς να εξηγήσεις, ποιο λάθος assumption εμφανίζεται συχνότερα, ποιο safe lab το αποκαλύπτει και ποιο retest αποδεικνύει ότι το διόρθωσες.
- **Domain and email defense in more depth**
  Για το **Domain and email defense in more depth**, στο πλαίσιο του **Ασφάλεια Email, DNS και Domains**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Registrar and DNS control plane**
  Στο **Registrar and DNS control plane**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.
- **SPF, DKIM and DMARC**
  Για το **SPF, DKIM and DMARC**, στο πλαίσιο του **Ασφάλεια Email, DNS και Domains**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Mail transport and mailbox security**
  Για το **Mail transport and mailbox security**, στο πλαίσιο του **Ασφάλεια Email, DNS και Domains**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Domain lifecycle**
  Για το **Domain lifecycle**, στο πλαίσιο του **Ασφάλεια Email, DNS και Domains**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Ασφάλεια Email, DNS και Domains**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε δικό σου LAN/lab και passive captures όπου γίνεται. Για active tests χρησιμοποίησε isolated namespaces/VMs και κράτησε packet capture πριν και μετά ώστε να αποδεικνύεται η συμπεριφορά.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Ασφάλεια Email, DNS και Domains**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Ασφάλεια Email, DNS και Domains** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 035](../../English/04-Network-Wireless-and-Internet/35-Email-DNS-and-Domain-Security.md)

---

# Python για Αυτοματοποίηση Ασφάλειας

> **Ελληνική έκδοση — Μάθημα 036.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Το Termux προσφέρει Linux-like userland πάνω στο Android, αλλά δεν είναι πλήρης desktop διανομή ούτε παρακάμπτει το Android security model. Για αξιόπιστη χρήση πρέπει να κατανοείς storage permissions, package management, process lifetime, networking, SSH, Python environments και τα όρια που επιβάλλει το Android sandbox.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Python για Αυτοματοποίηση Ασφάλειας**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Ασφάλεια automation mindset**
  Για το **Ασφάλεια automation mindset**, δες το workflow σαν reproducible local environment: paths, package/source provenance, permissions, environment state, error handling και rollback. Στο Termux προτίμησε standard-library εργαλεία, explicit paths και δοκιμές σε harmless local files/services.
- **Parsing structured data**
  Για το **Parsing structured data**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Hashing and integrity**
  Για το **Hashing and integrity**, στο πλαίσιο του **Python για Αυτοματοποίηση Ασφάλειας**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **HTTP clients**
  Στο **HTTP clients**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.
- **Concurrency**
  Για το **Concurrency**, στο πλαίσιο του **Python για Αυτοματοποίηση Ασφάλειας**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Subprocess security**
  Για το **Subprocess security**, δες το workflow σαν reproducible local environment: paths, package/source provenance, permissions, environment state, error handling και rollback. Στο Termux προτίμησε standard-library εργαλεία, explicit paths και δοκιμές σε harmless local files/services.
- **Secrets**
  Για το **Secrets**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **SQLite for local evidence**
  Στο **SQLite for local evidence**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Logging pattern**
  Στο **Logging pattern**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **CLI design**
  Για το **CLI design**, δες το workflow σαν reproducible local environment: paths, package/source provenance, permissions, environment state, error handling και rollback. Στο Termux προτίμησε standard-library εργαλεία, explicit paths και δοκιμές σε harmless local files/services.
- **Safe project ideas**
  Για το **Safe project ideas**, στο πλαίσιο του **Python για Αυτοματοποίηση Ασφάλειας**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Testing**
  Για το **Testing**, δες το workflow σαν reproducible local environment: paths, package/source provenance, permissions, environment state, error handling και rollback. Στο Termux προτίμησε standard-library εργαλεία, explicit paths και δοκιμές σε harmless local files/services.
- **Lab — Ασφάλεια findings normalizer**
  Στο **Lab — Ασφάλεια findings normalizer**, όρισε συγκεκριμένο objective, owned/local scope, expected result και stop condition. Κράτησε μόνο sanitized evidence, σύγκρινε expected με observed behavior και ολοκλήρωσε με remediation και ίδιο regression test.
- **Python automation engineering**
  Για το **Python automation engineering**, δες το workflow σαν reproducible local environment: paths, package/source provenance, permissions, environment state, error handling και rollback. Στο Termux προτίμησε standard-library εργαλεία, explicit paths και δοκιμές σε harmless local files/services.
- **Inputs and validation**
  Για το **Inputs and validation**, δες το workflow σαν reproducible local environment: paths, package/source provenance, permissions, environment state, error handling και rollback. Στο Termux προτίμησε standard-library εργαλεία, explicit paths και δοκιμές σε harmless local files/services.
- **Determinism and evidence**
  Στο **Determinism and evidence**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Error handling**
  Για το **Error handling**, δες το workflow σαν reproducible local environment: paths, package/source provenance, permissions, environment state, error handling και rollback. Στο Termux προτίμησε standard-library εργαλεία, explicit paths και δοκιμές σε harmless local files/services.
- **Dependencies**
  Για το **Dependencies**, ακολούθησε data/control flow από source σε sink, σημείωσε validation και ownership assumptions και έλεγξε πού εφαρμόζεται enforcement. Χρησιμοποίησε tests και static/runtime evidence για να ξεχωρίσεις root cause από απλό code smell.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Python για Αυτοματοποίηση Ασφάλειας**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Κράτησε όλα τα labs μέσα στο δικό σου τηλέφωνο, localhost ή συστήματα που ελέγχεις. Ξεκίνα με read-only commands και διατήρησε backups για scripts/configuration.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Python για Αυτοματοποίηση Ασφάλειας**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Python για Αυτοματοποίηση Ασφάλειας** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 036](../../English/10-Termux-and-Security-Automation/36-Python-for-Security-Automation.md)

---

# Digital Forensics και Διαχείριση Αποδεικτικών Στοιχείων

> **Ελληνική έκδοση — Μάθημα 037.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Blue-team εργασία σημαίνει να μετατρέπεις telemetry σε τεκμηριωμένα συμπεράσματα. Ένα alert δεν είναι απόδειξη από μόνο του. Χρειάζεται timeline, identity context, process/network relationships, data provenance και κατανόηση του τι δεν καταγράφεται. Η ανθεκτικότητα επεκτείνεται από detection μέχρι containment, recovery και verification.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Digital Forensics και Διαχείριση Αποδεικτικών Στοιχείων**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Forensics principles**
  Στο **Forensics principles**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Order of volatility**
  Στο **Order of volatility**, διατήρησε provenance και χρονικό context για κάθε artifact. Ξεχώρισε fact, inference και hypothesis, έλεγξε clock/timezone effects και μη θεωρείς το πρώτο observable event ούτε root cause ούτε αρχικό σημείο compromise χωρίς corroboration.
- **Timestamps**
  Στο **Timestamps**, διατήρησε provenance και χρονικό context για κάθε artifact. Ξεχώρισε fact, inference και hypothesis, έλεγξε clock/timezone effects και μη θεωρείς το πρώτο observable event ούτε root cause ούτε αρχικό σημείο compromise χωρίς corroboration.
- **Hashes**
  Στο **Hashes**, διατήρησε provenance και χρονικό context για κάθε artifact. Ξεχώρισε fact, inference και hypothesis, έλεγξε clock/timezone effects και μη θεωρείς το πρώτο observable event ούτε root cause ούτε αρχικό σημείο compromise χωρίς corroboration.
- **Logs as evidence**
  Στο **Logs as evidence**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Mobile evidence**
  Στο **Mobile evidence**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Cloud evidence**
  Για το **Cloud evidence**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **File metadata**
  Στο **File metadata**, διατήρησε provenance και χρονικό context για κάθε artifact. Ξεχώρισε fact, inference και hypothesis, έλεγξε clock/timezone effects και μη θεωρείς το πρώτο observable event ούτε root cause ούτε αρχικό σημείο compromise χωρίς corroboration.
- **Evidence notes**
  Στο **Evidence notes**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Root-cause caution**
  Στο **Root-cause caution**, διατήρησε provenance και χρονικό context για κάθε artifact. Ξεχώρισε fact, inference και hypothesis, έλεγξε clock/timezone effects και μη θεωρείς το πρώτο observable event ούτε root cause ούτε αρχικό σημείο compromise χωρίς corroboration.
- **Safe lab — Synthetic timeline**
  Στο **Safe lab — Synthetic timeline**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Reporting**
  Στο **Reporting**, διατήρησε provenance και χρονικό context για κάθε artifact. Ξεχώρισε fact, inference και hypothesis, έλεγξε clock/timezone effects και μη θεωρείς το πρώτο observable event ούτε root cause ούτε αρχικό σημείο compromise χωρίς corroboration.
- **Forensic reasoning in more depth**
  Στο **Forensic reasoning in more depth**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Provenance**
  Για το **Provenance**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **Time**
  Για το **Time**, στο πλαίσιο του **Digital Forensics και Διαχείριση Αποδεικτικών Στοιχείων**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Fact versus inference**
  Στο **Fact versus inference**, διατήρησε provenance και χρονικό context για κάθε artifact. Ξεχώρισε fact, inference και hypothesis, έλεγξε clock/timezone effects και μη θεωρείς το πρώτο observable event ούτε root cause ούτε αρχικό σημείο compromise χωρίς corroboration.
- **Scope and minimization**
  Στο **Scope and minimization**, διατήρησε provenance και χρονικό context για κάθε artifact. Ξεχώρισε fact, inference και hypothesis, έλεγξε clock/timezone effects και μη θεωρείς το πρώτο observable event ούτε root cause ούτε αρχικό σημείο compromise χωρίς corroboration.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Digital Forensics και Διαχείριση Αποδεικτικών Στοιχείων**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε synthetic logs και harmless local events. Κατέγραψε expected evidence πριν το test και σύγκρινε με ό,τι πραγματικά συλλέχθηκε.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Digital Forensics και Διαχείριση Αποδεικτικών Στοιχείων**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Digital Forensics και Διαχείριση Αποδεικτικών Στοιχείων** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 037](../../English/08-Blue-Team-IR-Forensics-and-Resilience/37-Digital-Forensics-and-Evidence-Handling.md)

---

# Ανθεκτικότητα και Ανάκαμψη από Ransomware

> **Ελληνική έκδοση — Μάθημα 038.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Blue-team εργασία σημαίνει να μετατρέπεις telemetry σε τεκμηριωμένα συμπεράσματα. Ένα alert δεν είναι απόδειξη από μόνο του. Χρειάζεται timeline, identity context, process/network relationships, data provenance και κατανόηση του τι δεν καταγράφεται. Η ανθεκτικότητα επεκτείνεται από detection μέχρι containment, recovery και verification.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Ανθεκτικότητα και Ανάκαμψη από Ransomware**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Ransomware is an operational crisis**
  Για το **Ransomware is an operational crisis**, αξιολόγησε identity containment, segmentation, immutable/offline recovery copies, restore priority και business communications ως ενιαίο resilience problem. Μέτρα recovery με πραγματικό restore test και όχι μόνο με την ύπαρξη backup.
- **Prevention layers**
  Για το **Prevention layers**, αξιολόγησε identity containment, segmentation, immutable/offline recovery copies, restore priority και business communications ως ενιαίο resilience problem. Μέτρα recovery με πραγματικό restore test και όχι μόνο με την ύπαρξη backup.
- **Backup architecture**
  Για το **Backup architecture**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Identity recovery**
  Για το **Identity recovery**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Initial response priorities**
  Για το **Initial response priorities**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **Recovery sequencing**
  Για το **Recovery sequencing**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Clean recovery**
  Για το **Clean recovery**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Communications**
  Για το **Communications**, αξιολόγησε identity containment, segmentation, immutable/offline recovery copies, restore priority και business communications ως ενιαίο resilience problem. Μέτρα recovery με πραγματικό restore test και όχι μόνο με την ύπαρξη backup.
- **Payment considerations**
  Για το **Payment considerations**, αξιολόγησε identity containment, segmentation, immutable/offline recovery copies, restore priority και business communications ως ενιαίο resilience problem. Μέτρα recovery με πραγματικό restore test και όχι μόνο με την ύπαρξη backup.
- **Tabletop exercise**
  Στο **Tabletop exercise**, όρισε συγκεκριμένο objective, owned/local scope, expected result και stop condition. Κράτησε μόνο sanitized evidence, σύγκρινε expected με observed behavior και ολοκλήρωσε με remediation και ίδιο regression test.
- **Primary reference**
  Για το **Primary reference**, ξεχώρισε normative specification από tutorial ή vendor summary. Κατέγραψε έκδοση/ημερομηνία, ποιο requirement στηρίζει το συμπέρασμα και ποιο μέρος του **Ανθεκτικότητα και Ανάκαμψη από Ransomware** χρειάζεται επανέλεγχο όταν αλλάξει η πηγή.
- **Ransomware resilience in more depth**
  Για το **Ransomware resilience in more depth**, αξιολόγησε identity containment, segmentation, immutable/offline recovery copies, restore priority και business communications ως ενιαίο resilience problem. Μέτρα recovery με πραγματικό restore test και όχι μόνο με την ύπαρξη backup.
- **Identity containment**
  Για το **Identity containment**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Recovery order**
  Για το **Recovery order**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Tabletop realism**
  Στο **Tabletop realism**, όρισε συγκεκριμένο objective, owned/local scope, expected result και stop condition. Κράτησε μόνο sanitized evidence, σύγκρινε expected με observed behavior και ολοκλήρωσε με remediation και ίδιο regression test.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Ανθεκτικότητα και Ανάκαμψη από Ransomware**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε synthetic logs και harmless local events. Κατέγραψε expected evidence πριν το test και σύγκρινε με ό,τι πραγματικά συλλέχθηκε.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Ανθεκτικότητα και Ανάκαμψη από Ransomware**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Ανθεκτικότητα και Ανάκαμψη από Ransomware** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 038](../../English/08-Blue-Team-IR-Forensics-and-Resilience/38-Ransomware-Resilience-and-Recovery.md)

---

# OAuth, OIDC, Passkeys και Σύγχρονο Authentication

> **Ελληνική έκδοση — Μάθημα 039.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Identity και cryptography είναι μηχανισμοί μεταφοράς εμπιστοσύνης. Authentication απαντά ποιος παρουσιάζει ένα credential, authorization τι επιτρέπεται να κάνει, ενώ cryptography προστατεύει συγκεκριμένες ιδιότητες δεδομένων και πρωτοκόλλων. Κλειδιά, tokens, certificates, federation metadata και policy engines είναι όλα authority-bearing artifacts και χρειάζονται σαφή lifecycle.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **OAuth, OIDC, Passkeys και Σύγχρονο Authentication**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Authentication versus authorization**
  Για το **Authentication versus authorization**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Core actors**
  Για το **Core actors**, στο πλαίσιο του **OAuth, OIDC, Passkeys και Σύγχρονο Authentication**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Redirect URIs**
  Για το **Redirect URIs**, στο πλαίσιο του **OAuth, OIDC, Passkeys και Σύγχρονο Authentication**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **State, nonce, and PKCE**
  Για το **State, nonce, and PKCE**, στο πλαίσιο του **OAuth, OIDC, Passkeys και Σύγχρονο Authentication**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Token handling**
  Για το **Token handling**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Session versus token**
  Για το **Session versus token**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **MFA**
  Για το **MFA**, στο πλαίσιο του **OAuth, OIDC, Passkeys και Σύγχρονο Authentication**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Passkeys**
  Για το **Passkeys**, στο πλαίσιο του **OAuth, OIDC, Passkeys και Σύγχρονο Authentication**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Federation risks**
  Για το **Federation risks**, στο πλαίσιο του **OAuth, OIDC, Passkeys και Σύγχρονο Authentication**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Service-to-service identity**
  Για το **Service-to-service identity**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Safe design lab**
  Για το **Safe design lab**, στο πλαίσιο του **OAuth, OIDC, Passkeys και Σύγχρονο Authentication**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Primary references**
  Για το **Primary references**, ξεχώρισε normative specification από tutorial ή vendor summary. Κατέγραψε έκδοση/ημερομηνία, ποιο requirement στηρίζει το συμπέρασμα και ποιο μέρος του **OAuth, OIDC, Passkeys και Σύγχρονο Authentication** χρειάζεται επανέλεγχο όταν αλλάξει η πηγή.
- **Σύγχρονο authentication in more depth**
  Για το **Σύγχρονο authentication in more depth**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Redirect and client trust**
  Για το **Redirect and client trust**, στο πλαίσιο του **OAuth, OIDC, Passkeys και Σύγχρονο Authentication**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Step-up and transaction authorization**
  Για το **Step-up and transaction authorization**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Telemetry**
  Στο **Telemetry**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **OAuth, OIDC, Passkeys και Σύγχρονο Authentication**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε synthetic identities, test certificates και local identity providers. Χαρτογράφησε issuer, subject, audience, permissions, lifetime, rotation και revocation χωρίς να αποθηκεύεις πραγματικά secrets.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **OAuth, OIDC, Passkeys και Σύγχρονο Authentication**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **OAuth, OIDC, Passkeys και Σύγχρονο Authentication** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 039](../../English/06-Identity-Cryptography-and-Trust/39-OAuth-OIDC-Passkeys-and-Modern-Authentication.md)

---

# Secure Coding και OWASP ASVS

> **Ελληνική έκδοση — Μάθημα 040.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Στην εφαρμοσμένη ασφάλεια web και assessments, κάθε request είναι μεταφορά δεδομένων και authority μέσα από πολλαπλά layers. Browser, proxy, web server, framework, API, database και identity provider μπορεί να ερμηνεύουν διαφορετικά την ίδια πληροφορία. Η βαθιά κατανόηση απαιτεί να παρακολουθείς normalization, parsing, state, authentication και authorization αντί να στηρίζεσαι μόνο σε signatures ή έτοιμα scanners.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Secure Coding και OWASP ASVS**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Secure coding is a system**
  Για το **Secure coding is a system**, ακολούθησε data/control flow από source σε sink, σημείωσε validation και ownership assumptions και έλεγξε πού εφαρμόζεται enforcement. Χρησιμοποίησε tests και static/runtime evidence για να ξεχωρίσεις root cause από απλό code smell.
- **ASVS as a requirements catalog**
  Για το **ASVS as a requirements catalog**, στο πλαίσιο του **Secure Coding και OWASP ASVS**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Input validation**
  Για το **Input validation**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **Output handling**
  Για το **Output handling**, στο πλαίσιο του **Secure Coding και OWASP ASVS**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **SQL and data stores**
  Για το **SQL and data stores**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **Command execution**
  Για το **Command execution**, στο πλαίσιο του **Secure Coding και OWASP ASVS**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Authorization**
  Για το **Authorization**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Authentication and session management**
  Για το **Authentication and session management**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Error handling**
  Για το **Error handling**, δες το workflow σαν reproducible local environment: paths, package/source provenance, permissions, environment state, error handling και rollback. Στο Termux προτίμησε standard-library εργαλεία, explicit paths και δοκιμές σε harmless local files/services.
- **Secrets**
  Για το **Secrets**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **File handling**
  Για το **File handling**, στο πλαίσιο του **Secure Coding και OWASP ASVS**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Deserialization and parsers**
  Για το **Deserialization and parsers**, ακολούθησε data/control flow από source σε sink, σημείωσε validation και ownership assumptions και έλεγξε πού εφαρμόζεται enforcement. Χρησιμοποίησε tests και static/runtime evidence για να ξεχωρίσεις root cause από απλό code smell.
- **Logging requirements**
  Στο **Logging requirements**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Dependency security**
  Για το **Dependency security**, ακολούθησε data/control flow από source σε sink, σημείωσε validation και ownership assumptions και έλεγξε πού εφαρμόζεται enforcement. Χρησιμοποίησε tests και static/runtime evidence για να ξεχωρίσεις root cause από απλό code smell.
- **Ασφάλεια tests**
  Για το **Ασφάλεια tests**, στο πλαίσιο του **Secure Coding και OWASP ASVS**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Code review questions**
  Για το **Code review questions**, ακολούθησε data/control flow από source σε sink, σημείωσε validation και ownership assumptions και έλεγξε πού εφαρμόζεται enforcement. Χρησιμοποίησε tests και static/runtime evidence για να ξεχωρίσεις root cause από απλό code smell.
- **Lab — Ασφάλεια requirement to test**
  Στο **Lab — Ασφάλεια requirement to test**, όρισε συγκεκριμένο objective, owned/local scope, expected result και stop condition. Κράτησε μόνο sanitized evidence, σύγκρινε expected με observed behavior και ολοκλήρωσε με remediation και ίδιο regression test.
- **Primary reference**
  Για το **Primary reference**, ξεχώρισε normative specification από tutorial ή vendor summary. Κατέγραψε έκδοση/ημερομηνία, ποιο requirement στηρίζει το συμπέρασμα και ποιο μέρος του **Secure Coding και OWASP ASVS** χρειάζεται επανέλεγχο όταν αλλάξει η πηγή.
- **Secure coding program guidance**
  Για το **Secure coding program guidance**, ακολούθησε data/control flow από source σε sink, σημείωσε validation και ownership assumptions και έλεγξε πού εφαρμόζεται enforcement. Χρησιμοποίησε tests και static/runtime evidence για να ξεχωρίσεις root cause από απλό code smell.
- **Requirements to tests**
  Για το **Requirements to tests**, στο πλαίσιο του **Secure Coding και OWASP ASVS**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Trust-boundary validation**
  Για το **Trust-boundary validation**, στο πλαίσιο του **Secure Coding και OWASP ASVS**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Dependencies and build**
  Για το **Dependencies and build**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Secure Coding και OWASP ASVS**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε μόνο localhost, intentionally vulnerable training apps ή ρητά εξουσιοδοτημένα συστήματα. Κατέγραψε request/response, server-side logs και την ακριβή security invariant που ελέγχεις.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Secure Coding και OWASP ASVS**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Secure Coding και OWASP ASVS** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 040](../../English/02-Recon-Pentesting-Web-and-AppSec/40-Secure-Coding-and-OWASP-ASVS.md)

---

# Threat Modeling και Αρχιτεκτονική Ασφάλειας

> **Ελληνική έκδοση — Μάθημα 041.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Η κατηγορία αυτή χτίζει τον τρόπο σκέψης που χρειάζεται πριν από οποιοδήποτε τεχνικό test. Η ασφάλεια αντιμετωπίζεται ως σύστημα από assets, identities, trust boundaries, δεδομένα, controls και αποδεικτικά στοιχεία. Το ζητούμενο δεν είναι να απομνημονεύσεις εργαλεία αλλά να μπορείς να εξηγήσεις τι προστατεύεται, από ποια απειλή, με ποια υπόθεση και πώς αποδεικνύεται το αποτέλεσμα.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Threat Modeling και Αρχιτεκτονική Ασφάλειας**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Start with the system**
  Για το **Start with the system**, σύνδεσε Android package/runtime behavior με UID sandbox, exported components, Binder/Intent boundaries, signing identity και Keystore-backed secrets. Επιβεβαίωσε το behavior σε δικό σου APK ή emulator και όχι σε τρίτες εφαρμογές.
- **Assets and security objectives**
  Για το **Assets and security objectives**, στο πλαίσιο του **Threat Modeling και Αρχιτεκτονική Ασφάλειας**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Trust boundaries**
  Για το **Trust boundaries**, στο πλαίσιο του **Threat Modeling και Αρχιτεκτονική Ασφάλειας**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **STRIDE**
  Για το **STRIDE**, στο πλαίσιο του **Threat Modeling και Αρχιτεκτονική Ασφάλειας**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Abuse cases**
  Για το **Abuse cases**, στο πλαίσιο του **Threat Modeling και Αρχιτεκτονική Ασφάλειας**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Ασφάλεια architecture patterns**
  Για το **Ασφάλεια architecture patterns**, στο πλαίσιο του **Threat Modeling και Αρχιτεκτονική Ασφάλειας**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Failure modes**
  Για το **Failure modes**, στο πλαίσιο του **Threat Modeling και Αρχιτεκτονική Ασφάλειας**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Prioritization**
  Για το **Prioritization**, στο πλαίσιο του **Threat Modeling και Αρχιτεκτονική Ασφάλειας**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Αρχιτεκτονική decision records**
  Για το **Αρχιτεκτονική decision records**, στο πλαίσιο του **Threat Modeling και Αρχιτεκτονική Ασφάλειας**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **AI systems**
  Στο **AI systems**, ξεχώρισε model behavior από deterministic policy enforcement. Κατέγραψε untrusted inputs, tool/data permissions, retrieval provenance, output validation και human approval points.
- **Supply chain**
  Για το **Supply chain**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **Lab — Threat model a notes app**
  Στο **Lab — Threat model a notes app**, όρισε συγκεκριμένο objective, owned/local scope, expected result και stop condition. Κράτησε μόνο sanitized evidence, σύγκρινε expected με observed behavior και ολοκλήρωσε με remediation και ίδιο regression test.
- **Threat-modeling depth**
  Για το **Threat-modeling depth**, στο πλαίσιο του **Threat Modeling και Αρχιτεκτονική Ασφάλειας**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Build the model**
  Για το **Build the model**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **Mitigation quality**
  Για το **Mitigation quality**, στο πλαίσιο του **Threat Modeling και Αρχιτεκτονική Ασφάλειας**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Review triggers**
  Για το **Review triggers**, στο πλαίσιο του **Threat Modeling και Αρχιτεκτονική Ασφάλειας**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Threat Modeling και Αρχιτεκτονική Ασφάλειας**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Δούλεψε με ένα υποθετικό ή δικό σου lab. Σχεδίασε scope, assets, trust boundaries και αναμενόμενα evidence πριν αλλάξεις οτιδήποτε.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Threat Modeling και Αρχιτεκτονική Ασφάλειας**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Threat Modeling και Αρχιτεκτονική Ασφάλειας** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 041](../../English/01-Fundamentals-and-Methodology/41-Threat-Modeling-and-Security-Architecture.md)

---

# Governance, Risk, Compliance και Privacy

> **Ελληνική έκδοση — Μάθημα 042.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Η ασφάλεια δεν είναι μόνο τεχνική εκμετάλλευση. AI systems, privacy, governance, human factors και data lifecycle απαιτούν σαφείς owners, policies, consent, minimization, auditability και περιορισμό authority. Το risk πρέπει να συνδέεται με πραγματικές επιπτώσεις και όχι μόνο με severity labels.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Governance, Risk, Compliance και Privacy**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Governance**
  Για το **Governance**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Risk**
  Για το **Risk**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Asset and data classification**
  Για το **Asset and data classification**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Policies, standards, procedures, guidelines**
  Για το **Policies, standards, procedures, guidelines**, ξεχώρισε normative specification από tutorial ή vendor summary. Κατέγραψε έκδοση/ημερομηνία, ποιο requirement στηρίζει το συμπέρασμα και ποιο μέρος του **Governance, Risk, Compliance και Privacy** χρειάζεται επανέλεγχο όταν αλλάξει η πηγή.
- **Control frameworks**
  Στο **Control frameworks**, σύνδεσε requirement με owner, asset/data scope, measurable control objective, exception process και evidence. Έλεγξε αν το metric ή policy δείχνει πραγματική μείωση risk και όχι απλώς activity/compliance output.
- **Privacy engineering**
  Για το **Privacy engineering**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Third-party risk**
  Για το **Third-party risk**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Exceptions**
  Στο **Exceptions**, σύνδεσε ABI/OS abstraction με το πραγματικό machine/runtime state: registers, addresses, object handles, loader metadata και privilege transition. Χρησιμοποίησε μικρό δικό σου binary, disassembler/debugger και annotated trace ώστε κάθε inference να έχει observable βάση.
- **Metrics**
  Για το **Metrics**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Risk register lab**
  Για το **Risk register lab**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Primary reference**
  Για το **Primary reference**, ξεχώρισε normative specification από tutorial ή vendor summary. Κατέγραψε έκδοση/ημερομηνία, ποιο requirement στηρίζει το συμπέρασμα και ποιο μέρος του **Governance, Risk, Compliance και Privacy** χρειάζεται επανέλεγχο όταν αλλάξει η πηγή.
- **Governance and risk depth**
  Για το **Governance and risk depth**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Risk statement structure**
  Για το **Risk statement structure**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Treatment choices**
  Στο **Treatment choices**, σύνδεσε requirement με owner, asset/data scope, measurable control objective, exception process και evidence. Έλεγξε αν το metric ή policy δείχνει πραγματική μείωση risk και όχι απλώς activity/compliance output.
- **Control evidence**
  Στο **Control evidence**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Privacy integration**
  Για το **Privacy integration**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Governance, Risk, Compliance και Privacy**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε synthetic data και role-play scenarios. Μην χρησιμοποιείς πραγματικά προσωπικά δεδομένα ή παραπλανητικές social-engineering δοκιμές χωρίς ρητή έγκριση.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Governance, Risk, Compliance και Privacy**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Governance, Risk, Compliance και Privacy** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 042](../../English/09-AI-GRC-Privacy-Data-and-Human-Security/42-Governance-Risk-Compliance-and-Privacy.md)

---

# Responsible Disclosure και Ηθική Bug Bounty

> **Ελληνική έκδοση — Μάθημα 043.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Η κατηγορία αυτή χτίζει τον τρόπο σκέψης που χρειάζεται πριν από οποιοδήποτε τεχνικό test. Η ασφάλεια αντιμετωπίζεται ως σύστημα από assets, identities, trust boundaries, δεδομένα, controls και αποδεικτικά στοιχεία. Το ζητούμενο δεν είναι να απομνημονεύσεις εργαλεία αλλά να μπορείς να εξηγήσεις τι προστατεύεται, από ποια απειλή, με ποια υπόθεση και πώς αποδεικνύεται το αποτέλεσμα.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Responsible Disclosure και Ηθική Bug Bounty**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Authorization first**
  Για το **Authorization first**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Scope**
  Για το **Scope**, στο πλαίσιο του **Responsible Disclosure και Ηθική Bug Bounty**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Minimize impact**
  Για το **Minimize impact**, στο πλαίσιο του **Responsible Disclosure και Ηθική Bug Bounty**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Stop conditions**
  Για το **Stop conditions**, στο πλαίσιο του **Responsible Disclosure και Ηθική Bug Bounty**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **High-quality report**
  Για το **High-quality report**, στο πλαίσιο του **Responsible Disclosure και Ηθική Bug Bounty**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Duplicate and known issues**
  Για το **Duplicate and known issues**, στο πλαίσιο του **Responsible Disclosure και Ηθική Bug Bounty**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Disclosure**
  Για το **Disclosure**, στο πλαίσιο του **Responsible Disclosure και Ηθική Bug Bounty**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Data retention**
  Για το **Data retention**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Safe practice**
  Για το **Safe practice**, στο πλαίσιο του **Responsible Disclosure και Ηθική Bug Bounty**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Reporting lab**
  Στο **Reporting lab**, διατήρησε provenance και χρονικό context για κάθε artifact. Ξεχώρισε fact, inference και hypothesis, έλεγξε clock/timezone effects και μη θεωρείς το πρώτο observable event ούτε root cause ούτε αρχικό σημείο compromise χωρίς corroboration.
- **Disclosure workflow in more depth**
  Για το **Disclosure workflow in more depth**, στο πλαίσιο του **Responsible Disclosure και Ηθική Bug Bounty**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Report quality**
  Για το **Report quality**, στο πλαίσιο του **Responsible Disclosure και Ηθική Bug Bounty**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Stop and disclose**
  Για το **Stop and disclose**, στο πλαίσιο του **Responsible Disclosure και Ηθική Bug Bounty**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Responsible Disclosure και Ηθική Bug Bounty**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Δούλεψε με ένα υποθετικό ή δικό σου lab. Σχεδίασε scope, assets, trust boundaries και αναμενόμενα evidence πριν αλλάξεις οτιδήποτε.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Responsible Disclosure και Ηθική Bug Bounty**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Responsible Disclosure και Ηθική Bug Bounty** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 043](../../English/01-Fundamentals-and-Methodology/43-Responsible-Disclosure-and-Bug-Bounty-Ethics.md)

---

# Ασφάλεια Endpoint, Browser και SaaS

> **Ελληνική έκδοση — Μάθημα 044.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Blue-team εργασία σημαίνει να μετατρέπεις telemetry σε τεκμηριωμένα συμπεράσματα. Ένα alert δεν είναι απόδειξη από μόνο του. Χρειάζεται timeline, identity context, process/network relationships, data provenance και κατανόηση του τι δεν καταγράφεται. Η ανθεκτικότητα επεκτείνεται από detection μέχρι containment, recovery και verification.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Ασφάλεια Endpoint, Browser και SaaS**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Endpoint security**
  Για το **Endpoint security**, στο πλαίσιο του **Ασφάλεια Endpoint, Browser και SaaS**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Mobile endpoints**
  Στο **Mobile endpoints**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.
- **Browser as an application platform**
  Για το **Browser as an application platform**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **Session theft risk**
  Για το **Session theft risk**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **SaaS administration**
  Για το **SaaS administration**, στο πλαίσιο του **Ασφάλεια Endpoint, Browser και SaaS**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **OAuth application consent**
  Για το **OAuth application consent**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Shadow SaaS**
  Για το **Shadow SaaS**, στο πλαίσιο του **Ασφάλεια Endpoint, Browser και SaaS**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **DLP and sharing**
  Για το **DLP and sharing**, στο πλαίσιο του **Ασφάλεια Endpoint, Browser και SaaS**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Endpoint detection**
  Στο **Endpoint detection**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Browser lab**
  Για το **Browser lab**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **SaaS inventory lab**
  Για το **SaaS inventory lab**, στο πλαίσιο του **Ασφάλεια Endpoint, Browser και SaaS**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Endpoint, browser and SaaS operational depth**
  Για το **Endpoint, browser and SaaS operational depth**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **Browser review**
  Για το **Browser review**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **SaaS review**
  Για το **SaaS review**, στο πλαίσιο του **Ασφάλεια Endpoint, Browser και SaaS**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Endpoint loss**
  Για το **Endpoint loss**, στο πλαίσιο του **Ασφάλεια Endpoint, Browser και SaaS**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Ασφάλεια Endpoint, Browser και SaaS**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε synthetic logs και harmless local events. Κατέγραψε expected evidence πριν το test και σύγκρινε με ό,τι πραγματικά συλλέχθηκε.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Ασφάλεια Endpoint, Browser και SaaS**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Ασφάλεια Endpoint, Browser και SaaS** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 044](../../English/08-Blue-Team-IR-Forensics-and-Resilience/44-Endpoint-Browser-and-SaaS-Security.md)

---

# Capstones, Checklists και Study Roadmaps

> **Ελληνική έκδοση — Μάθημα 045.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Τα capstones μετατρέπουν γνώση σε αποδείξιμη ικανότητα. Ένα καλό project έχει scope, threat model, repeatable procedure, evidence, limitations, remediation και καθαρή τεχνική γραφή. Η ποιότητα μετριέται από το αν τρίτος μπορεί να αναπαράγει το συμπέρασμα χωρίς να μαντεύει.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Capstones, Checklists και Study Roadmaps**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **How to use this module**
  Για το **How to use this module**, όρισε συγκεκριμένο observable αποτέλεσμα: artifact, report, test, diagram ή explanation που μπορεί να αξιολογηθεί. Προτίμησε μικρά ολοκληρωμένα έργα με scope, evidence, remediation και reflection αντί για λίστες εργαλείων ή claims χωρίς απόδειξη.
- **Beginner roadmap**
  Για το **Beginner roadmap**, όρισε συγκεκριμένο observable αποτέλεσμα: artifact, report, test, diagram ή explanation που μπορεί να αξιολογηθεί. Προτίμησε μικρά ολοκληρωμένα έργα με scope, evidence, remediation και reflection αντί για λίστες εργαλείων ή claims χωρίς απόδειξη.
- **Blue-team roadmap**
  Για το **Blue-team roadmap**, όρισε συγκεκριμένο observable αποτέλεσμα: artifact, report, test, diagram ή explanation που μπορεί να αξιολογηθεί. Προτίμησε μικρά ολοκληρωμένα έργα με scope, evidence, remediation και reflection αντί για λίστες εργαλείων ή claims χωρίς απόδειξη.
- **Application-security roadmap**
  Για το **Application-security roadmap**, όρισε συγκεκριμένο observable αποτέλεσμα: artifact, report, test, diagram ή explanation που μπορεί να αξιολογηθεί. Προτίμησε μικρά ολοκληρωμένα έργα με scope, evidence, remediation και reflection αντί για λίστες εργαλείων ή claims χωρίς απόδειξη.
- **Cloud/DevSecOps roadmap**
  Για το **Cloud/DevSecOps roadmap**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **Termux/mobile roadmap**
  Στο **Termux/mobile roadmap**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.
- **Ασφάλεια assessment checklist**
  Για το **Ασφάλεια assessment checklist**, στο πλαίσιο του **Capstones, Checklists και Study Roadmaps**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Before**
  Για το **Before**, όρισε συγκεκριμένο observable αποτέλεσμα: artifact, report, test, diagram ή explanation που μπορεί να αξιολογηθεί. Προτίμησε μικρά ολοκληρωμένα έργα με scope, evidence, remediation και reflection αντί για λίστες εργαλείων ή claims χωρίς απόδειξη.
- **During**
  Για το **During**, όρισε συγκεκριμένο observable αποτέλεσμα: artifact, report, test, diagram ή explanation που μπορεί να αξιολογηθεί. Προτίμησε μικρά ολοκληρωμένα έργα με scope, evidence, remediation και reflection αντί για λίστες εργαλείων ή claims χωρίς απόδειξη.
- **After**
  Για το **After**, όρισε συγκεκριμένο observable αποτέλεσμα: artifact, report, test, diagram ή explanation που μπορεί να αξιολογηθεί. Προτίμησε μικρά ολοκληρωμένα έργα με scope, evidence, remediation και reflection αντί για λίστες εργαλείων ή claims χωρίς απόδειξη.
- **Incident-response checklist**
  Για το **Incident-response checklist**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **Secure software release checklist**
  Για το **Secure software release checklist**, όρισε συγκεκριμένο observable αποτέλεσμα: artifact, report, test, diagram ή explanation που μπορεί να αξιολογηθεί. Προτίμησε μικρά ολοκληρωμένα έργα με scope, evidence, remediation και reflection αντί για λίστες εργαλείων ή claims χωρίς απόδειξη.
- **Capstone 1 — Defensive home lab**
  Στο **Capstone 1 — Defensive home lab**, όρισε συγκεκριμένο objective, owned/local scope, expected result και stop condition. Κράτησε μόνο sanitized evidence, σύγκρινε expected με observed behavior και ολοκλήρωσε με remediation και ίδιο regression test.
- **Capstone 2 — Secure API**
  Για το **Capstone 2 — Secure API**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **Capstone 3 — Digital forensics notebook**
  Στο **Capstone 3 — Digital forensics notebook**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Capstone 4 — Threat intelligence brief**
  Στο **Capstone 4 — Threat intelligence brief**, όρισε συγκεκριμένο objective, owned/local scope, expected result και stop condition. Κράτησε μόνο sanitized evidence, σύγκρινε expected με observed behavior και ολοκλήρωσε με remediation και ίδιο regression test.
- **Capstone 5 — Ransomware tabletop**
  Στο **Capstone 5 — Ransomware tabletop**, όρισε συγκεκριμένο objective, owned/local scope, expected result και stop condition. Κράτησε μόνο sanitized evidence, σύγκρινε expected με observed behavior και ολοκλήρωσε με remediation και ίδιο regression test.
- **Capstone 6 — Termux security companion**
  Στο **Capstone 6 — Termux security companion**, όρισε συγκεκριμένο objective, owned/local scope, expected result και stop condition. Κράτησε μόνο sanitized evidence, σύγκρινε expected με observed behavior και ολοκλήρωσε με remediation και ίδιο regression test.
- **What mastery looks like**
  Στο **What mastery looks like**, μετέτρεψε τη θεωρία του **Capstones, Checklists και Study Roadmaps** σε ελέγξιμα κριτήρια: τι πρέπει να μπορείς να εξηγήσεις, ποιο λάθος assumption εμφανίζεται συχνότερα, ποιο safe lab το αποκαλύπτει και ποιο retest αποδεικνύει ότι το διόρθωσες.
- **Turning roadmaps into a weekly system**
  Για το **Turning roadmaps into a weekly system**, όρισε συγκεκριμένο observable αποτέλεσμα: artifact, report, test, diagram ή explanation που μπορεί να αξιολογηθεί. Προτίμησε μικρά ολοκληρωμένα έργα με scope, evidence, remediation και reflection αντί για λίστες εργαλείων ή claims χωρίς απόδειξη.
- **Capstone scoring rubric**
  Στο **Capstone scoring rubric**, όρισε συγκεκριμένο objective, owned/local scope, expected result και stop condition. Κράτησε μόνο sanitized evidence, σύγκρινε expected με observed behavior και ολοκλήρωσε με remediation και ίδιο regression test.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Capstones, Checklists και Study Roadmaps**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χτίσε portfolio μόνο με δικά σου ή ρητά εξουσιοδοτημένα labs. Αφαίρεσε secrets και προσωπικά δεδομένα πριν δημοσιεύσεις artifacts.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Capstones, Checklists και Study Roadmaps**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Capstones, Checklists και Study Roadmaps** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 045](../../English/11-Labs-Capstones-and-Career/45-Capstones-Checklists-and-Study-Roadmaps.md)

---

# Agentic AI, MCP και Ασφάλεια Εργαλείων

> **Ελληνική έκδοση — Μάθημα 046.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Η ασφάλεια δεν είναι μόνο τεχνική εκμετάλλευση. AI systems, privacy, governance, human factors και data lifecycle απαιτούν σαφείς owners, policies, consent, minimization, auditability και περιορισμό authority. Το risk πρέπει να συνδέεται με πραγματικές επιπτώσεις και όχι μόνο με severity labels.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Agentic AI, MCP και Ασφάλεια Εργαλείων**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Why agents change the threat model**
  Για το **Why agents change the threat model**, αντιμετώπισε model output ως untrusted suggestion. Βάλε deterministic authorization πριν από tool/data access, schema validation στα inputs/outputs, provenance στο retrieved context, bounded resources και human approval για irreversible ή high-impact ενέργειες.
- **Agent components to model**
  Στο **Agent components to model**, ξεχώρισε model behavior από deterministic policy enforcement. Κατέγραψε untrusted inputs, tool/data permissions, retrieval provenance, output validation και human approval points.
- **Prompt injection is an authorization problem too**
  Για το **Prompt injection is an authorization problem too**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Least privilege for tools**
  Για το **Least privilege for tools**, αντιμετώπισε model output ως untrusted suggestion. Βάλε deterministic authorization πριν από tool/data access, schema validation στα inputs/outputs, provenance στο retrieved context, bounded resources και human approval για irreversible ή high-impact ενέργειες.
- **Tool descriptions are part of the trust surface**
  Για το **Tool descriptions are part of the trust surface**, σύνδεσε Android package/runtime behavior με UID sandbox, exported components, Binder/Intent boundaries, signing identity και Keystore-backed secrets. Επιβεβαίωσε το behavior σε δικό σου APK ή emulator και όχι σε τρίτες εφαρμογές.
- **Model Context Protocol**
  Στο **Model Context Protocol**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.
- **Human approval**
  Για το **Human approval**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Memory security**
  Στο **Memory security**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **Inter-agent communication**
  Στο **Inter-agent communication**, ξεχώρισε model behavior από deterministic policy enforcement. Κατέγραψε untrusted inputs, tool/data permissions, retrieval provenance, output validation και human approval points.
- **Safe failure**
  Για το **Safe failure**, αντιμετώπισε model output ως untrusted suggestion. Βάλε deterministic authorization πριν από tool/data access, schema validation στα inputs/outputs, provenance στο retrieved context, bounded resources και human approval για irreversible ή high-impact ενέργειες.
- **Evaluation**
  Για το **Evaluation**, αντιμετώπισε model output ως untrusted suggestion. Βάλε deterministic authorization πριν από tool/data access, schema validation στα inputs/outputs, provenance στο retrieved context, bounded resources και human approval για irreversible ή high-impact ενέργειες.
- **Lab — Harmless agent tool boundary**
  Στο **Lab — Harmless agent tool boundary**, ξεχώρισε model behavior από deterministic policy enforcement. Κατέγραψε untrusted inputs, tool/data permissions, retrieval provenance, output validation και human approval points.
- **Primary references**
  Για το **Primary references**, ξεχώρισε normative specification από tutorial ή vendor summary. Κατέγραψε έκδοση/ημερομηνία, ποιο requirement στηρίζει το συμπέρασμα και ποιο μέρος του **Agentic AI, MCP και Ασφάλεια Εργαλείων** χρειάζεται επανέλεγχο όταν αλλάξει η πηγή.
- **Agent/tool security depth**
  Στο **Agent/tool security depth**, ξεχώρισε model behavior από deterministic policy enforcement. Κατέγραψε untrusted inputs, tool/data permissions, retrieval provenance, output validation και human approval points.
- **Tool contracts**
  Για το **Tool contracts**, αντιμετώπισε model output ως untrusted suggestion. Βάλε deterministic authorization πριν από tool/data access, schema validation στα inputs/outputs, provenance στο retrieved context, bounded resources και human approval για irreversible ή high-impact ενέργειες.
- **Untrusted context**
  Για το **Untrusted context**, αντιμετώπισε model output ως untrusted suggestion. Βάλε deterministic authorization πριν από tool/data access, schema validation στα inputs/outputs, provenance στο retrieved context, bounded resources και human approval για irreversible ή high-impact ενέργειες.
- **High-impact actions**
  Για το **High-impact actions**, αντιμετώπισε model output ως untrusted suggestion. Βάλε deterministic authorization πριν από tool/data access, schema validation στα inputs/outputs, provenance στο retrieved context, bounded resources και human approval για irreversible ή high-impact ενέργειες.
- **Observability**
  Για το **Observability**, αντιμετώπισε model output ως untrusted suggestion. Βάλε deterministic authorization πριν από tool/data access, schema validation στα inputs/outputs, provenance στο retrieved context, bounded resources και human approval για irreversible ή high-impact ενέργειες.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Agentic AI, MCP και Ασφάλεια Εργαλείων**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε synthetic data και role-play scenarios. Μην χρησιμοποιείς πραγματικά προσωπικά δεδομένα ή παραπλανητικές social-engineering δοκιμές χωρίς ρητή έγκριση.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Agentic AI, MCP και Ασφάλεια Εργαλείων**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Agentic AI, MCP και Ασφάλεια Εργαλείων** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 046](../../English/09-AI-GRC-Privacy-Data-and-Human-Security/46-Agentic-AI-MCP-and-Tool-Security.md)

---

# SOC, SIEM, SOAR και Λειτουργίες Ανίχνευσης

> **Ελληνική έκδοση — Μάθημα 047.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Blue-team εργασία σημαίνει να μετατρέπεις telemetry σε τεκμηριωμένα συμπεράσματα. Ένα alert δεν είναι απόδειξη από μόνο του. Χρειάζεται timeline, identity context, process/network relationships, data provenance και κατανόηση του τι δεν καταγράφεται. Η ανθεκτικότητα επεκτείνεται από detection μέχρι containment, recovery και verification.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **SOC, SIEM, SOAR και Λειτουργίες Ανίχνευσης**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **SOC operating model**
  Στο **SOC operating model**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Telemetry pipeline**
  Στο **Telemetry pipeline**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **SIEM**
  Στο **SIEM**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Detection engineering**
  Στο **Detection engineering**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Alert quality**
  Στο **Alert quality**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **SOAR and automation**
  Στο **SOAR and automation**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Case management**
  Για το **Case management**, όρισε decision owner, trigger, required telemetry, χρονική σειρά ενεργειών και πιθανό operational impact. Η σωστή απόφαση πρέπει να είναι αναστρέψιμη όπου γίνεται, να διατηρεί evidence και να συνδέεται με σαφές recovery/retest criterion.
- **Detection coverage**
  Στο **Detection coverage**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Health monitoring**
  Για το **Health monitoring**, όρισε decision owner, trigger, required telemetry, χρονική σειρά ενεργειών και πιθανό operational impact. Η σωστή απόφαση πρέπει να είναι αναστρέψιμη όπου γίνεται, να διατηρεί evidence και να συνδέεται με σαφές recovery/retest criterion.
- **Lab — Detection lifecycle**
  Στο **Lab — Detection lifecycle**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **SOC operating model in more depth**
  Στο **SOC operating model in more depth**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Telemetry quality**
  Στο **Telemetry quality**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Detection lifecycle**
  Στο **Detection lifecycle**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **SOAR**
  Στο **SOAR**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Triage**
  Για το **Triage**, όρισε decision owner, trigger, required telemetry, χρονική σειρά ενεργειών και πιθανό operational impact. Η σωστή απόφαση πρέπει να είναι αναστρέψιμη όπου γίνεται, να διατηρεί evidence και να συνδέεται με σαφές recovery/retest criterion.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **SOC, SIEM, SOAR και Λειτουργίες Ανίχνευσης**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε synthetic logs και harmless local events. Κατέγραψε expected evidence πριν το test και σύγκρινε με ό,τι πραγματικά συλλέχθηκε.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **SOC, SIEM, SOAR και Λειτουργίες Ανίχνευσης**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **SOC, SIEM, SOAR και Λειτουργίες Ανίχνευσης** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 047](../../English/08-Blue-Team-IR-Forensics-and-Resilience/47-SOC-SIEM-SOAR-and-Detection-Operations.md)

---

# Business Continuity, Disaster Recovery και Backup Engineering

> **Ελληνική έκδοση — Μάθημα 048.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Blue-team εργασία σημαίνει να μετατρέπεις telemetry σε τεκμηριωμένα συμπεράσματα. Ένα alert δεν είναι απόδειξη από μόνο του. Χρειάζεται timeline, identity context, process/network relationships, data provenance και κατανόηση του τι δεν καταγράφεται. Η ανθεκτικότητα επεκτείνεται από detection μέχρι containment, recovery και verification.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Business Continuity, Disaster Recovery και Backup Engineering**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Three related disciplines**
  Για το **Three related disciplines**, στο πλαίσιο του **Business Continuity, Disaster Recovery και Backup Engineering**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Business impact analysis**
  Για το **Business impact analysis**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Recovery objectives**
  Για το **Recovery objectives**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Backup design**
  Για το **Backup design**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Restore testing**
  Για το **Restore testing**, δες το workflow σαν reproducible local environment: paths, package/source provenance, permissions, environment state, error handling και rollback. Στο Termux προτίμησε standard-library εργαλεία, explicit paths και δοκιμές σε harmless local files/services.
- **Dependency maps**
  Για το **Dependency maps**, ακολούθησε data/control flow από source σε sink, σημείωσε validation και ownership assumptions και έλεγξε πού εφαρμόζεται enforcement. Χρησιμοποίησε tests και static/runtime evidence για να ξεχωρίσεις root cause από απλό code smell.
- **Crisis communications**
  Για το **Crisis communications**, όρισε decision owner, trigger, required telemetry, χρονική σειρά ενεργειών και πιθανό operational impact. Η σωστή απόφαση πρέπει να είναι αναστρέψιμη όπου γίνεται, να διατηρεί evidence και να συνδέεται με σαφές recovery/retest criterion.
- **Provider failure**
  Για το **Provider failure**, όρισε decision owner, trigger, required telemetry, χρονική σειρά ενεργειών και πιθανό operational impact. Η σωστή απόφαση πρέπει να είναι αναστρέψιμη όπου γίνεται, να διατηρεί evidence και να συνδέεται με σαφές recovery/retest criterion.
- **Exercises**
  Στο **Exercises**, όρισε συγκεκριμένο objective, owned/local scope, expected result και stop condition. Κράτησε μόνο sanitized evidence, σύγκρινε expected με observed behavior και ολοκλήρωσε με remediation και ίδιο regression test.
- **Lab — Recovery proof**
  Για το **Lab — Recovery proof**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Recovery engineering in more depth**
  Για το **Recovery engineering in more depth**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **RTO and RPO**
  Για το **RTO and RPO**, όρισε decision owner, trigger, required telemetry, χρονική σειρά ενεργειών και πιθανό operational impact. Η σωστή απόφαση πρέπει να είναι αναστρέψιμη όπου γίνεται, να διατηρεί evidence και να συνδέεται με σαφές recovery/retest criterion.
- **Dependency mapping**
  Για το **Dependency mapping**, ακολούθησε data/control flow από source σε sink, σημείωσε validation και ownership assumptions και έλεγξε πού εφαρμόζεται enforcement. Χρησιμοποίησε tests και static/runtime evidence για να ξεχωρίσεις root cause από απλό code smell.
- **Clean recovery**
  Για το **Clean recovery**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Business Continuity, Disaster Recovery και Backup Engineering**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε synthetic logs και harmless local events. Κατέγραψε expected evidence πριν το test και σύγκρινε με ό,τι πραγματικά συλλέχθηκε.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Business Continuity, Disaster Recovery και Backup Engineering**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Business Continuity, Disaster Recovery και Backup Engineering** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 048](../../English/08-Blue-Team-IR-Forensics-and-Resilience/48-Business-Continuity-Disaster-Recovery-and-Backup-Engineering.md)

---

# Secrets, PKI και Διαχείριση Κλειδιών

> **Ελληνική έκδοση — Μάθημα 049.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Identity και cryptography είναι μηχανισμοί μεταφοράς εμπιστοσύνης. Authentication απαντά ποιος παρουσιάζει ένα credential, authorization τι επιτρέπεται να κάνει, ενώ cryptography προστατεύει συγκεκριμένες ιδιότητες δεδομένων και πρωτοκόλλων. Κλειδιά, tokens, certificates, federation metadata και policy engines είναι όλα authority-bearing artifacts και χρειάζονται σαφή lifecycle.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Secrets, PKI και Διαχείριση Κλειδιών**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Secret lifecycle**
  Για το **Secret lifecycle**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **Secret types**
  Για το **Secret types**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **Avoid secrets in source code**
  Για το **Avoid secrets in source code**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **Secret managers**
  Για το **Secret managers**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **PKI concepts**
  Για το **PKI concepts**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **Certificate lifecycle**
  Για το **Certificate lifecycle**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **Key rotation**
  Για το **Key rotation**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **Signing keys**
  Για το **Signing keys**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **Encryption key separation**
  Για το **Encryption key separation**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **Backups and escrow**
  Για το **Backups and escrow**, δες το workflow σαν reproducible local environment: paths, package/source provenance, permissions, environment state, error handling και rollback. Στο Termux προτίμησε standard-library εργαλεία, explicit paths και δοκιμές σε harmless local files/services.
- **Lab — Secret inventory**
  Για το **Lab — Secret inventory**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **Key-management depth**
  Για το **Key-management depth**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **Secret classes**
  Για το **Secret classes**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **PKI**
  Για το **PKI**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **Rotation**
  Για το **Rotation**, στο πλαίσιο του **Secrets, PKI και Διαχείριση Κλειδιών**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Secrets, PKI και Διαχείριση Κλειδιών**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε synthetic identities, test certificates και local identity providers. Χαρτογράφησε issuer, subject, audience, permissions, lifetime, rotation και revocation χωρίς να αποθηκεύεις πραγματικά secrets.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Secrets, PKI και Διαχείριση Κλειδιών**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Secrets, PKI και Διαχείριση Κλειδιών** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 049](../../English/06-Identity-Cryptography-and-Trust/49-Secrets-PKI-and-Key-Management.md)

---

# Vulnerability Management και Attack Surface Management

> **Ελληνική έκδοση — Μάθημα 050.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Η κατηγορία αυτή χτίζει τον τρόπο σκέψης που χρειάζεται πριν από οποιοδήποτε τεχνικό test. Η ασφάλεια αντιμετωπίζεται ως σύστημα από assets, identities, trust boundaries, δεδομένα, controls και αποδεικτικά στοιχεία. Το ζητούμενο δεν είναι να απομνημονεύσεις εργαλεία αλλά να μπορείς να εξηγήσεις τι προστατεύεται, από ποια απειλή, με ποια υπόθεση και πώς αποδεικνύεται το αποτέλεσμα.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Vulnerability Management και Attack Surface Management**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Vulnerability management lifecycle**
  Για το **Vulnerability management lifecycle**, όρισε συγκεκριμένο observable αποτέλεσμα: artifact, report, test, diagram ή explanation που μπορεί να αξιολογηθεί. Προτίμησε μικρά ολοκληρωμένα έργα με scope, evidence, remediation και reflection αντί για λίστες εργαλείων ή claims χωρίς απόδειξη.
- **Asset inventory comes first**
  Για το **Asset inventory comes first**, στο πλαίσιο του **Vulnerability Management και Attack Surface Management**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Severity is not priority**
  Για το **Severity is not priority**, στο πλαίσιο του **Vulnerability Management και Attack Surface Management**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Attack surface management**
  Για το **Attack surface management**, στο πλαίσιο του **Vulnerability Management και Attack Surface Management**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **False positives and validation**
  Για το **False positives and validation**, ξεκίνα από observable behavior και διαθέσιμα data sources, όχι από technique ID μόνο. Γράψε detection hypothesis, required fields, expected benign collisions, tuning strategy και validation event ώστε η κάλυψη να είναι μετρήσιμη.
- **Patch versus mitigation**
  Για το **Patch versus mitigation**, στο πλαίσιο του **Vulnerability Management και Attack Surface Management**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **End-of-life software**
  Για το **End-of-life software**, στο πλαίσιο του **Vulnerability Management και Attack Surface Management**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **SLAs and risk-based timelines**
  Για το **SLAs and risk-based timelines**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Retest**
  Για το **Retest**, στο πλαίσιο του **Vulnerability Management και Attack Surface Management**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Metrics**
  Για το **Metrics**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Lab — Prioritization board**
  Στο **Lab — Prioritization board**, όρισε συγκεκριμένο objective, owned/local scope, expected result και stop condition. Κράτησε μόνο sanitized evidence, σύγκρινε expected με observed behavior και ολοκλήρωσε με remediation και ίδιο regression test.
- **Primary references**
  Για το **Primary references**, ξεχώρισε normative specification από tutorial ή vendor summary. Κατέγραψε έκδοση/ημερομηνία, ποιο requirement στηρίζει το συμπέρασμα και ποιο μέρος του **Vulnerability Management και Attack Surface Management** χρειάζεται επανέλεγχο όταν αλλάξει η πηγή.
- **Vulnerability-management depth**
  Για το **Vulnerability-management depth**, στο πλαίσιο του **Vulnerability Management και Attack Surface Management**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Asset context**
  Για το **Asset context**, στο πλαίσιο του **Vulnerability Management και Attack Surface Management**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Prioritization**
  Για το **Prioritization**, στο πλαίσιο του **Vulnerability Management και Attack Surface Management**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Exceptions**
  Στο **Exceptions**, σύνδεσε ABI/OS abstraction με το πραγματικό machine/runtime state: registers, addresses, object handles, loader metadata και privilege transition. Χρησιμοποίησε μικρό δικό σου binary, disassembler/debugger και annotated trace ώστε κάθε inference να έχει observable βάση.
- **Verification**
  Για το **Verification**, στο πλαίσιο του **Vulnerability Management και Attack Surface Management**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Vulnerability Management και Attack Surface Management**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Δούλεψε με ένα υποθετικό ή δικό σου lab. Σχεδίασε scope, assets, trust boundaries και αναμενόμενα evidence πριν αλλάξεις οτιδήποτε.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Vulnerability Management και Attack Surface Management**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Vulnerability Management και Attack Surface Management** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 050](../../English/01-Fundamentals-and-Methodology/50-Vulnerability-Management-and-Attack-Surface-Management.md)

---

# Δικτύωση σε Βάθος

> **Ελληνική έκδοση — Μάθημα 051.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Τα δίκτυα είναι κατανεμημένα state machines. Routing, neighbor discovery, DNS, TCP/UDP, wireless authentication και middleboxes δημιουργούν διαφορετικά trust boundaries. Για σωστή ανάλυση χρειάζεται να ξεχωρίζεις control plane από data plane, local-link μηχανισμούς από routed traffic και observation από active interference.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Δικτύωση σε Βάθος**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Start with a mental model**
  Για το **Start with a mental model**, σύνδεσε Android package/runtime behavior με UID sandbox, exported components, Binder/Intent boundaries, signing identity και Keystore-backed secrets. Επιβεβαίωσε το behavior σε δικό σου APK ή emulator και όχι σε τρίτες εφαρμογές.
- **Addresses are contextual**
  Για το **Addresses are contextual**, στο πλαίσιο του **Δικτύωση σε Βάθος**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Subnets and routing**
  Στο **Subnets and routing**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.
- **TCP and UDP**
  Στο **TCP and UDP**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.
- **DNS is more than name-to-address lookup**
  Στο **DNS is more than name-to-address lookup**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.
- **DHCP and local configuration**
  Για το **DHCP and local configuration**, στο πλαίσιο του **Δικτύωση σε Βάθος**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **ARP and IPv6 Neighbor Discovery**
  Στο **ARP and IPv6 Neighbor Discovery**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.
- **NAT is not a security policy**
  Για το **NAT is not a security policy**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **TLS and trust**
  Στο **TLS and trust**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.
- **Proxies, gateways, and load balancers**
  Για το **Proxies, gateways, and load balancers**, στο πλαίσιο του **Δικτύωση σε Βάθος**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **IPv6 security guidance**
  Στο **IPv6 security guidance**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.
- **Safe local practice**
  Για το **Safe local practice**, στο πλαίσιο του **Δικτύωση σε Βάθος**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Troubleshooting ladder**
  Για το **Troubleshooting ladder**, στο πλαίσιο του **Δικτύωση σε Βάθος**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Ασφάλεια design questions**
  Για το **Ασφάλεια design questions**, στο πλαίσιο του **Δικτύωση σε Βάθος**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Checkpoint**
  Στο **Checkpoint**, μετέτρεψε τη θεωρία του **Δικτύωση σε Βάθος** σε ελέγξιμα κριτήρια: τι πρέπει να μπορείς να εξηγήσεις, ποιο λάθος assumption εμφανίζεται συχνότερα, ποιο safe lab το αποκαλύπτει και ποιο retest αποδεικνύει ότι το διόρθωσες.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Δικτύωση σε Βάθος**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε δικό σου LAN/lab και passive captures όπου γίνεται. Για active tests χρησιμοποίησε isolated namespaces/VMs και κράτησε packet capture πριν και μετά ώστε να αποδεικνύεται η συμπεριφορά.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Δικτύωση σε Βάθος**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Δικτύωση σε Βάθος** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 051](../../English/04-Network-Wireless-and-Internet/51-Networking-Deep-Dive.md)

---

# Web, Browser και HTTP σε Βάθος

> **Ελληνική έκδοση — Μάθημα 052.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Στην εφαρμοσμένη ασφάλεια web και assessments, κάθε request είναι μεταφορά δεδομένων και authority μέσα από πολλαπλά layers. Browser, proxy, web server, framework, API, database και identity provider μπορεί να ερμηνεύουν διαφορετικά την ίδια πληροφορία. Η βαθιά κατανόηση απαιτεί να παρακολουθείς normalization, parsing, state, authentication και authorization αντί να στηρίζεσαι μόνο σε signatures ή έτοιμα scanners.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Web, Browser και HTTP σε Βάθος**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Anatomy of an HTTP request**
  Στο **Anatomy of an HTTP request**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.
- **Anatomy of an HTTP response**
  Στο **Anatomy of an HTTP response**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.
- **Origins and the browser security model**
  Για το **Origins and the browser security model**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **Cookies and sessions**
  Για το **Cookies and sessions**, στο πλαίσιο του **Web, Browser και HTTP σε Βάθος**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Browser storage**
  Για το **Browser storage**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **CSRF**
  Για το **CSRF**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **Content Ασφάλεια Policy**
  Για το **Content Ασφάλεια Policy**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Caching and sensitive data**
  Για το **Caching and sensitive data**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **HTTP/2 and HTTP/3**
  Στο **HTTP/2 and HTTP/3**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.
- **Error handling**
  Για το **Error handling**, δες το workflow σαν reproducible local environment: paths, package/source provenance, permissions, environment state, error handling και rollback. Στο Termux προτίμησε standard-library εργαλεία, explicit paths και δοκιμές σε harmless local files/services.
- **Local protocol exercise**
  Στο **Local protocol exercise**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.
- **Application authorization exercise**
  Για το **Application authorization exercise**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Review checklist**
  Για το **Review checklist**, στο πλαίσιο του **Web, Browser και HTTP σε Βάθος**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Checkpoint**
  Στο **Checkpoint**, μετέτρεψε τη θεωρία του **Web, Browser και HTTP σε Βάθος** σε ελέγξιμα κριτήρια: τι πρέπει να μπορείς να εξηγήσεις, ποιο λάθος assumption εμφανίζεται συχνότερα, ποιο safe lab το αποκαλύπτει και ποιο retest αποδεικνύει ότι το διόρθωσες.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Web, Browser και HTTP σε Βάθος**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε μόνο localhost, intentionally vulnerable training apps ή ρητά εξουσιοδοτημένα συστήματα. Κατέγραψε request/response, server-side logs και την ακριβή security invariant που ελέγχεις.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Web, Browser και HTTP σε Βάθος**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Web, Browser και HTTP σε Βάθος** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 052](../../English/02-Recon-Pentesting-Web-and-AppSec/52-Web-Browser-and-HTTP-Deep-Dive.md)

---

# Memory Safety και Exploit Mitigations

> **Ελληνική έκδοση — Μάθημα 053.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Η ασφάλεια συστημάτων βασίζεται στα πραγματικά boundaries του λειτουργικού: processes, memory mappings, privilege levels, handles/file descriptors, executable loading, syscalls, services και telemetry. Σε reverse engineering και vulnerability research το σημαντικό είναι να συνδέεις συμπεριφορά υψηλού επιπέδου με χαμηλού επιπέδου state χωρίς να συμπεραίνεις περισσότερα από όσα δείχνουν τα δεδομένα.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Memory Safety και Exploit Mitigations**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Why memory safety matters**
  Στο **Why memory safety matters**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **Core failure classes**
  Για το **Core failure classes**, στο πλαίσιο του **Memory Safety και Exploit Mitigations**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Stack and heap mental model**
  Στο **Stack and heap mental model**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **ASLR**
  Στο **ASLR**, ξεχώρισε root cause από exploitability. Κατέγραψε faulting operation, object lifetime/size, register και memory context, ενεργές mitigations και το μικρότερο harmless reproducer· επιβεβαίωσε τη διόρθωση με sanitizer/debugger και regression test.
- **NX / DEP**
  Στο **NX / DEP**, ξεχώρισε root cause από exploitability. Κατέγραψε faulting operation, object lifetime/size, register και memory context, ενεργές mitigations και το μικρότερο harmless reproducer· επιβεβαίωσε τη διόρθωση με sanitizer/debugger και regression test.
- **Stack canaries**
  Στο **Stack canaries**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **Control-flow protections**
  Στο **Control-flow protections**, ξεχώρισε root cause από exploitability. Κατέγραψε faulting operation, object lifetime/size, register και memory context, ενεργές mitigations και το μικρότερο harmless reproducer· επιβεβαίωσε τη διόρθωση με sanitizer/debugger και regression test.
- **Sandboxing**
  Για το **Sandboxing**, στο πλαίσιο του **Memory Safety και Exploit Mitigations**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Memory-safe languages**
  Στο **Memory-safe languages**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **Compiler and runtime diagnostics**
  Στο **Compiler and runtime diagnostics**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **Fuzzing safely**
  Στο **Fuzzing safely**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **Triage a crash**
  Στο **Triage a crash**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **Secure design guidance**
  Για το **Secure design guidance**, στο πλαίσιο του **Memory Safety και Exploit Mitigations**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Checkpoint**
  Στο **Checkpoint**, μετέτρεψε τη θεωρία του **Memory Safety και Exploit Mitigations** σε ελέγξιμα κριτήρια: τι πρέπει να μπορείς να εξηγήσεις, ποιο λάθος assumption εμφανίζεται συχνότερα, ποιο safe lab το αποκαλύπτει και ποιο retest αποδεικνύει ότι το διόρθωσες.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Memory Safety και Exploit Mitigations**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Δούλεψε σε disposable VM ή local test binary. Προτίμησε harmless toy programs, sanitizers, debuggers και read-only inspection. Μην μετατρέπεις crash analysis σε weaponized exploitation.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Memory Safety και Exploit Mitigations**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Memory Safety και Exploit Mitigations** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 053](../../English/03-Systems-Malware-and-Reverse-Engineering/53-Memory-Safety-and-Exploit-Mitigations.md)

---

# Ασφάλεια Hardware, Firmware και Boot

> **Ελληνική έκδοση — Μάθημα 054.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Mobile, IoT και embedded συστήματα συνδυάζουν εφαρμογές, λειτουργικό, firmware, radios, hardware roots of trust και φυσική πρόσβαση. Το security model εξαρτάται από secure boot, app sandboxing, permissions, key storage, update trust και τις πραγματικές διεπαφές που εκτίθενται.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Ασφάλεια Hardware, Firmware και Boot**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Layers below the OS**
  Για το **Layers below the OS**, ακολούθησε την αλυσίδα trust από immutable/early-boot state μέχρι OS/application. Έλεγξε measured/verified state, key custody, update authorization, anti-rollback και τι αλλάζει όταν ο attacker έχει φυσική πρόσβαση.
- **Secure Boot**
  Στο **Secure Boot**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.
- **Measured boot**
  Στο **Measured boot**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.
- **TPMs and secure elements**
  Για το **TPMs and secure elements**, ακολούθησε την αλυσίδα trust από immutable/early-boot state μέχρι OS/application. Έλεγξε measured/verified state, key custody, update authorization, anti-rollback και τι αλλάζει όταν ο attacker έχει φυσική πρόσβαση.
- **Firmware updates**
  Στο **Firmware updates**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.
- **Physical access**
  Για το **Physical access**, ακολούθησε την αλυσίδα trust από immutable/early-boot state μέχρι OS/application. Έλεγξε measured/verified state, key custody, update authorization, anti-rollback και τι αλλάζει όταν ο attacker έχει φυσική πρόσβαση.
- **Full-disk encryption and boot trust**
  Για το **Full-disk encryption and boot trust**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **Mobile device hardware security**
  Στο **Mobile device hardware security**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.
- **IoT/embedded guidance**
  Στο **IoT/embedded guidance**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.
- **Supply-chain questions**
  Για το **Supply-chain questions**, ακολούθησε την αλυσίδα trust από immutable/early-boot state μέχρι OS/application. Έλεγξε measured/verified state, key custody, update authorization, anti-rollback και τι αλλάζει όταν ο attacker έχει φυσική πρόσβαση.
- **Safe learning exercise**
  Στο **Safe learning exercise**, μετέτρεψε τη θεωρία του **Ασφάλεια Hardware, Firmware και Boot** σε ελέγξιμα κριτήρια: τι πρέπει να μπορείς να εξηγήσεις, ποιο λάθος assumption εμφανίζεται συχνότερα, ποιο safe lab το αποκαλύπτει και ποιο retest αποδεικνύει ότι το διόρθωσες.
- **Checkpoint**
  Στο **Checkpoint**, μετέτρεψε τη θεωρία του **Ασφάλεια Hardware, Firmware και Boot** σε ελέγξιμα κριτήρια: τι πρέπει να μπορείς να εξηγήσεις, ποιο λάθος assumption εμφανίζεται συχνότερα, ποιο safe lab το αποκαλύπτει και ποιο retest αποδεικνύει ότι το διόρθωσες.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Ασφάλεια Hardware, Firmware και Boot**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε δική σου συσκευή, emulator ή development board. Προτίμησε static analysis, documented debug interfaces και benign sample apps/firmware. Απόφυγε tests σε τρίτες συσκευές ή ασύρματα περιβάλλοντα.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Ασφάλεια Hardware, Firmware και Boot**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Ασφάλεια Hardware, Firmware και Boot** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 054](../../English/05-Mobile-IoT-and-Hardware/54-Hardware-Firmware-and-Boot-Security.md)

---

# Ασφάλεια Bluetooth, NFC και Proximity

> **Ελληνική έκδοση — Μάθημα 055.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Mobile, IoT και embedded συστήματα συνδυάζουν εφαρμογές, λειτουργικό, firmware, radios, hardware roots of trust και φυσική πρόσβαση. Το security model εξαρτάται από secure boot, app sandboxing, permissions, key storage, update trust και τις πραγματικές διεπαφές που εκτίθενται.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Ασφάλεια Bluetooth, NFC και Proximity**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Bluetooth security model**
  Στο **Bluetooth security model**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.
- **Pairing guidance**
  Στο **Pairing guidance**, ξεχώρισε discovery από authenticated pairing και authorization. Κατέγραψε identifiers, negotiated security level, replay/proximity assumptions και ποιο application-layer check αποτρέπει το να μετατραπεί η απλή εγγύτητα σε authority.
- **BLE services and characteristics**
  Στο **BLE services and characteristics**, ξεχώρισε discovery από authenticated pairing και authorization. Κατέγραψε identifiers, negotiated security level, replay/proximity assumptions και ποιο application-layer check αποτρέπει το να μετατραπεί η απλή εγγύτητα σε authority.
- **Privacy**
  Για το **Privacy**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **NFC**
  Στο **NFC**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.
- **UWB and proximity claims**
  Στο **UWB and proximity claims**, ξεχώρισε discovery από authenticated pairing και authorization. Κατέγραψε identifiers, negotiated security level, replay/proximity assumptions και ποιο application-layer check αποτρέπει το να μετατραπεί η απλή εγγύτητα σε authority.
- **Device inventory exercise**
  Στο **Device inventory exercise**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.
- **Safe lab ideas**
  Στο **Safe lab ideas**, μετέτρεψε τη θεωρία του **Ασφάλεια Bluetooth, NFC και Proximity** σε ελέγξιμα κριτήρια: τι πρέπει να μπορείς να εξηγήσεις, ποιο λάθος assumption εμφανίζεται συχνότερα, ποιο safe lab το αποκαλύπτει και ποιο retest αποδεικνύει ότι το διόρθωσες.
- **Defensive checklist**
  Για το **Defensive checklist**, στο πλαίσιο του **Ασφάλεια Bluetooth, NFC και Proximity**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Checkpoint**
  Στο **Checkpoint**, μετέτρεψε τη θεωρία του **Ασφάλεια Bluetooth, NFC και Proximity** σε ελέγξιμα κριτήρια: τι πρέπει να μπορείς να εξηγήσεις, ποιο λάθος assumption εμφανίζεται συχνότερα, ποιο safe lab το αποκαλύπτει και ποιο retest αποδεικνύει ότι το διόρθωσες.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Ασφάλεια Bluetooth, NFC και Proximity**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε δική σου συσκευή, emulator ή development board. Προτίμησε static analysis, documented debug interfaces και benign sample apps/firmware. Απόφυγε tests σε τρίτες συσκευές ή ασύρματα περιβάλλοντα.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Ασφάλεια Bluetooth, NFC και Proximity**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Ασφάλεια Bluetooth, NFC και Proximity** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 055](../../English/05-Mobile-IoT-and-Hardware/55-Bluetooth-NFC-and-Proximity-Security.md)

---

# Android Security σε Βάθος

> **Ελληνική έκδοση — Μάθημα 056.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Mobile, IoT και embedded συστήματα συνδυάζουν εφαρμογές, λειτουργικό, firmware, radios, hardware roots of trust και φυσική πρόσβαση. Το security model εξαρτάται από secure boot, app sandboxing, permissions, key storage, update trust και τις πραγματικές διεπαφές που εκτίθενται.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Android Security σε Βάθος**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Application sandbox**
  Για το **Application sandbox**, σύνδεσε Android package/runtime behavior με UID sandbox, exported components, Binder/Intent boundaries, signing identity και Keystore-backed secrets. Επιβεβαίωσε το behavior σε δικό σου APK ή emulator και όχι σε τρίτες εφαρμογές.
- **Permissions**
  Για το **Permissions**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **App signing**
  Για το **App signing**, σύνδεσε Android package/runtime behavior με UID sandbox, exported components, Binder/Intent boundaries, signing identity και Keystore-backed secrets. Επιβεβαίωσε το behavior σε δικό σου APK ή emulator και όχι σε τρίτες εφαρμογές.
- **Storage**
  Για το **Storage**, κατέγραψε ποιος μπορεί να γράψει/διαβάσει το state, πού αποθηκεύεται, πώς προστατεύεται at rest, ποιο backup/sync behavior υπάρχει και πότε το data πρέπει να διαγράφεται ή να ανακαλείται.
- **Android Keystore**
  Στο **Android Keystore**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.
- **Components and IPC**
  Για το **Components and IPC**, σύνδεσε Android package/runtime behavior με UID sandbox, exported components, Binder/Intent boundaries, signing identity και Keystore-backed secrets. Επιβεβαίωσε το behavior σε δικό σου APK ή emulator και όχι σε τρίτες εφαρμογές.
- **Deep links**
  Για το **Deep links**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **WebView**
  Για το **WebView**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **Network security**
  Στο **Network security**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.
- **Logging**
  Στο **Logging**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Backups and screenshots**
  Για το **Backups and screenshots**, δες το workflow σαν reproducible local environment: paths, package/source provenance, permissions, environment state, error handling και rollback. Στο Termux προτίμησε standard-library εργαλεία, explicit paths και δοκιμές σε harmless local files/services.
- **Updates and dependencies**
  Για το **Updates and dependencies**, ακολούθησε data/control flow από source σε sink, σημείωσε validation και ownership assumptions και έλεγξε πού εφαρμόζεται enforcement. Χρησιμοποίησε tests και static/runtime evidence για να ξεχωρίσεις root cause από απλό code smell.
- **Termux relationship**
  Για το **Termux relationship**, δες το workflow σαν reproducible local environment: paths, package/source provenance, permissions, environment state, error handling και rollback. Στο Termux προτίμησε standard-library εργαλεία, explicit paths και δοκιμές σε harmless local files/services.
- **Safe developer review**
  Για το **Safe developer review**, σύνδεσε Android package/runtime behavior με UID sandbox, exported components, Binder/Intent boundaries, signing identity και Keystore-backed secrets. Επιβεβαίωσε το behavior σε δικό σου APK ή emulator και όχι σε τρίτες εφαρμογές.
- **Checkpoint**
  Στο **Checkpoint**, μετέτρεψε τη θεωρία του **Android Security σε Βάθος** σε ελέγξιμα κριτήρια: τι πρέπει να μπορείς να εξηγήσεις, ποιο λάθος assumption εμφανίζεται συχνότερα, ποιο safe lab το αποκαλύπτει και ποιο retest αποδεικνύει ότι το διόρθωσες.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Android Security σε Βάθος**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε δική σου συσκευή, emulator ή development board. Προτίμησε static analysis, documented debug interfaces και benign sample apps/firmware. Απόφυγε tests σε τρίτες συσκευές ή ασύρματα περιβάλλοντα.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Android Security σε Βάθος**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Android Security σε Βάθος** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 056](../../English/05-Mobile-IoT-and-Hardware/56-Android-Security-Deep-Dive.md)

---

# Privacy, Data Protection και Operational Hygiene

> **Ελληνική έκδοση — Μάθημα 057.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Η ασφάλεια δεν είναι μόνο τεχνική εκμετάλλευση. AI systems, privacy, governance, human factors και data lifecycle απαιτούν σαφείς owners, policies, consent, minimization, auditability και περιορισμό authority. Το risk πρέπει να συνδέεται με πραγματικές επιπτώσεις και όχι μόνο με severity labels.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Privacy, Data Protection και Operational Hygiene**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Collect less**
  Στο **Collect less**, σύνδεσε requirement με owner, asset/data scope, measurable control objective, exception process και evidence. Έλεγξε αν το metric ή policy δείχνει πραγματική μείωση risk και όχι απλώς activity/compliance output.
- **Separate identifiers from secrets**
  Για το **Separate identifiers from secrets**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **Redaction**
  Στο **Redaction**, σύνδεσε requirement με owner, asset/data scope, measurable control objective, exception process και evidence. Έλεγξε αν το metric ή policy δείχνει πραγματική μείωση risk και όχι απλώς activity/compliance output.
- **Retention**
  Στο **Retention**, σύνδεσε requirement με owner, asset/data scope, measurable control objective, exception process και evidence. Έλεγξε αν το metric ή policy δείχνει πραγματική μείωση risk και όχι απλώς activity/compliance output.
- **OSINT ethics**
  Στο **OSINT ethics**, ξεχώρισε raw information από assessed intelligence. Βαθμολόγησε source reliability και information credibility, σημείωσε timestamps/provenance, απέφυγε attribution χωρίς επαρκές evidence και σύνδεσε το αποτέλεσμα με συγκεκριμένη defensive decision.
- **Incident-response privacy**
  Για το **Incident-response privacy**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **AI/LLM data handling**
  Για το **AI/LLM data handling**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Device operational hygiene**
  Στο **Device operational hygiene**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.
- **Evidence-folder pattern**
  Στο **Evidence-folder pattern**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Checkpoint**
  Στο **Checkpoint**, μετέτρεψε τη θεωρία του **Privacy, Data Protection και Operational Hygiene** σε ελέγξιμα κριτήρια: τι πρέπει να μπορείς να εξηγήσεις, ποιο λάθος assumption εμφανίζεται συχνότερα, ποιο safe lab το αποκαλύπτει και ποιο retest αποδεικνύει ότι το διόρθωσες.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Privacy, Data Protection και Operational Hygiene**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε synthetic data και role-play scenarios. Μην χρησιμοποιείς πραγματικά προσωπικά δεδομένα ή παραπλανητικές social-engineering δοκιμές χωρίς ρητή έγκριση.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Privacy, Data Protection και Operational Hygiene**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Privacy, Data Protection και Operational Hygiene** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 057](../../English/09-AI-GRC-Privacy-Data-and-Human-Security/57-Privacy-Data-Protection-and-Operational-Hygiene.md)

---

# Καριέρα Cybersecurity και Οδηγίες Portfolio

> **Ελληνική έκδοση — Μάθημα 058.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Τα capstones μετατρέπουν γνώση σε αποδείξιμη ικανότητα. Ένα καλό project έχει scope, threat model, repeatable procedure, evidence, limitations, remediation και καθαρή τεχνική γραφή. Η ποιότητα μετριέται από το αν τρίτος μπορεί να αναπαράγει το συμπέρασμα χωρίς να μαντεύει.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Καριέρα Cybersecurity και Οδηγίες Portfolio**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Skills before titles**
  Για το **Skills before titles**, όρισε συγκεκριμένο observable αποτέλεσμα: artifact, report, test, diagram ή explanation που μπορεί να αξιολογηθεί. Προτίμησε μικρά ολοκληρωμένα έργα με scope, evidence, remediation και reflection αντί για λίστες εργαλείων ή claims χωρίς απόδειξη.
- **Portfolio principles**
  Για το **Portfolio principles**, όρισε συγκεκριμένο observable αποτέλεσμα: artifact, report, test, diagram ή explanation που μπορεί να αξιολογηθεί. Προτίμησε μικρά ολοκληρωμένα έργα με scope, evidence, remediation και reflection αντί για λίστες εργαλείων ή claims χωρίς απόδειξη.
- **Explain each project**
  Για το **Explain each project**, στο πλαίσιο του **Καριέρα Cybersecurity και Οδηγίες Portfolio**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **GitHub hygiene**
  Για το **GitHub hygiene**, δες το workflow σαν reproducible local environment: paths, package/source provenance, permissions, environment state, error handling και rollback. Στο Termux προτίμησε standard-library εργαλεία, explicit paths και δοκιμές σε harmless local files/services.
- **Role directions**
  Για το **Role directions**, όρισε συγκεκριμένο observable αποτέλεσμα: artifact, report, test, diagram ή explanation που μπορεί να αξιολογηθεί. Προτίμησε μικρά ολοκληρωμένα έργα με scope, evidence, remediation και reflection αντί για λίστες εργαλείων ή claims χωρίς απόδειξη.
- **SOC / blue team**
  Στο **SOC / blue team**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Application security**
  Για το **Application security**, όρισε συγκεκριμένο observable αποτέλεσμα: artifact, report, test, diagram ή explanation που μπορεί να αξιολογηθεί. Προτίμησε μικρά ολοκληρωμένα έργα με scope, evidence, remediation και reflection αντί για λίστες εργαλείων ή claims χωρίς απόδειξη.
- **Ασφάλεια engineering**
  Για το **Ασφάλεια engineering**, στο πλαίσιο του **Καριέρα Cybersecurity και Οδηγίες Portfolio**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **GRC / risk**
  Για το **GRC / risk**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Vulnerability management**
  Για το **Vulnerability management**, όρισε συγκεκριμένο observable αποτέλεσμα: artifact, report, test, diagram ή explanation που μπορεί να αξιολογηθεί. Προτίμησε μικρά ολοκληρωμένα έργα με scope, evidence, remediation και reflection αντί για λίστες εργαλείων ή claims χωρίς απόδειξη.
- **Certifications**
  Για το **Certifications**, όρισε συγκεκριμένο observable αποτέλεσμα: artifact, report, test, diagram ή explanation που μπορεί να αξιολογηθεί. Προτίμησε μικρά ολοκληρωμένα έργα με scope, evidence, remediation και reflection αντί για λίστες εργαλείων ή claims χωρίς απόδειξη.
- **Interview preparation**
  Για το **Interview preparation**, όρισε decision owner, trigger, required telemetry, χρονική σειρά ενεργειών και πιθανό operational impact. Η σωστή απόφαση πρέπει να είναι αναστρέψιμη όπου γίνεται, να διατηρεί evidence και να συνδέεται με σαφές recovery/retest criterion.
- **Professional communication**
  Για το **Professional communication**, όρισε συγκεκριμένο observable αποτέλεσμα: artifact, report, test, diagram ή explanation που μπορεί να αξιολογηθεί. Προτίμησε μικρά ολοκληρωμένα έργα με scope, evidence, remediation και reflection αντί για λίστες εργαλείων ή claims χωρίς απόδειξη.
- **30-day portfolio plan**
  Για το **30-day portfolio plan**, όρισε συγκεκριμένο observable αποτέλεσμα: artifact, report, test, diagram ή explanation που μπορεί να αξιολογηθεί. Προτίμησε μικρά ολοκληρωμένα έργα με scope, evidence, remediation και reflection αντί για λίστες εργαλείων ή claims χωρίς απόδειξη.
- **Week 1**
  Για το **Week 1**, όρισε συγκεκριμένο observable αποτέλεσμα: artifact, report, test, diagram ή explanation που μπορεί να αξιολογηθεί. Προτίμησε μικρά ολοκληρωμένα έργα με scope, evidence, remediation και reflection αντί για λίστες εργαλείων ή claims χωρίς απόδειξη.
- **Week 2**
  Για το **Week 2**, όρισε συγκεκριμένο observable αποτέλεσμα: artifact, report, test, diagram ή explanation που μπορεί να αξιολογηθεί. Προτίμησε μικρά ολοκληρωμένα έργα με scope, evidence, remediation και reflection αντί για λίστες εργαλείων ή claims χωρίς απόδειξη.
- **Week 3**
  Για το **Week 3**, όρισε συγκεκριμένο observable αποτέλεσμα: artifact, report, test, diagram ή explanation που μπορεί να αξιολογηθεί. Προτίμησε μικρά ολοκληρωμένα έργα με scope, evidence, remediation και reflection αντί για λίστες εργαλείων ή claims χωρίς απόδειξη.
- **Week 4**
  Για το **Week 4**, όρισε συγκεκριμένο observable αποτέλεσμα: artifact, report, test, diagram ή explanation που μπορεί να αξιολογηθεί. Προτίμησε μικρά ολοκληρωμένα έργα με scope, evidence, remediation και reflection αντί για λίστες εργαλείων ή claims χωρίς απόδειξη.
- **Checkpoint**
  Στο **Checkpoint**, μετέτρεψε τη θεωρία του **Καριέρα Cybersecurity και Οδηγίες Portfolio** σε ελέγξιμα κριτήρια: τι πρέπει να μπορείς να εξηγήσεις, ποιο λάθος assumption εμφανίζεται συχνότερα, ποιο safe lab το αποκαλύπτει και ποιο retest αποδεικνύει ότι το διόρθωσες.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Καριέρα Cybersecurity και Οδηγίες Portfolio**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χτίσε portfolio μόνο με δικά σου ή ρητά εξουσιοδοτημένα labs. Αφαίρεσε secrets και προσωπικά δεδομένα πριν δημοσιεύσεις artifacts.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Καριέρα Cybersecurity και Οδηγίες Portfolio**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Καριέρα Cybersecurity και Οδηγίες Portfolio** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 058](../../English/11-Labs-Capstones-and-Career/58-Cybersecurity-Career-and-Portfolio-Guidance.md)

---

# Security Metrics και Μέτρηση Προγράμματος

> **Ελληνική έκδοση — Μάθημα 059.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Η ασφάλεια δεν είναι μόνο τεχνική εκμετάλλευση. AI systems, privacy, governance, human factors και data lifecycle απαιτούν σαφείς owners, policies, consent, minimization, auditability και περιορισμό authority. Το risk πρέπει να συνδέεται με πραγματικές επιπτώσεις και όχι μόνο με severity labels.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Security Metrics και Μέτρηση Προγράμματος**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Activity is not outcome**
  Στο **Activity is not outcome**, σύνδεσε requirement με owner, asset/data scope, measurable control objective, exception process και evidence. Έλεγξε αν το metric ή policy δείχνει πραγματική μείωση risk και όχι απλώς activity/compliance output.
- **Define every metric**
  Για το **Define every metric**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Vulnerability metrics**
  Για το **Vulnerability metrics**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Detection/SOC metrics**
  Στο **Detection/SOC metrics**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Identity metrics**
  Για το **Identity metrics**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Recovery metrics**
  Για το **Recovery metrics**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Application-security metrics**
  Για το **Application-security metrics**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Risk indicators**
  Για το **Risk indicators**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Dashboard guidance**
  Στο **Dashboard guidance**, σύνδεσε requirement με owner, asset/data scope, measurable control objective, exception process και evidence. Έλεγξε αν το metric ή policy δείχνει πραγματική μείωση risk και όχι απλώς activity/compliance output.
- **Metric anti-patterns**
  Για το **Metric anti-patterns**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Safe lab**
  Στο **Safe lab**, μετέτρεψε τη θεωρία του **Security Metrics και Μέτρηση Προγράμματος** σε ελέγξιμα κριτήρια: τι πρέπει να μπορείς να εξηγήσεις, ποιο λάθος assumption εμφανίζεται συχνότερα, ποιο safe lab το αποκαλύπτει και ποιο retest αποδεικνύει ότι το διόρθωσες.
- **Checkpoint**
  Στο **Checkpoint**, μετέτρεψε τη θεωρία του **Security Metrics και Μέτρηση Προγράμματος** σε ελέγξιμα κριτήρια: τι πρέπει να μπορείς να εξηγήσεις, ποιο λάθος assumption εμφανίζεται συχνότερα, ποιο safe lab το αποκαλύπτει και ποιο retest αποδεικνύει ότι το διόρθωσες.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Security Metrics και Μέτρηση Προγράμματος**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε synthetic data και role-play scenarios. Μην χρησιμοποιείς πραγματικά προσωπικά δεδομένα ή παραπλανητικές social-engineering δοκιμές χωρίς ρητή έγκριση.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Security Metrics και Μέτρηση Προγράμματος**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Security Metrics και Μέτρηση Προγράμματος** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 059](../../English/09-AI-GRC-Privacy-Data-and-Human-Security/59-Security-Metrics-and-Program-Measurement.md)

---

# Φυσική Ασφάλεια και Ανθρώπινη Ανθεκτικότητα

> **Ελληνική έκδοση — Μάθημα 060.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Η ασφάλεια δεν είναι μόνο τεχνική εκμετάλλευση. AI systems, privacy, governance, human factors και data lifecycle απαιτούν σαφείς owners, policies, consent, minimization, auditability και περιορισμό authority. Το risk πρέπει να συνδέεται με πραγματικές επιπτώσεις και όχι μόνο με severity labels.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Φυσική Ασφάλεια και Ανθρώπινη Ανθεκτικότητα**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Physical access changes the threat model**
  Για το **Physical access changes the threat model**, ακολούθησε την αλυσίδα trust από immutable/early-boot state μέχρι OS/application. Έλεγξε measured/verified state, key custody, update authorization, anti-rollback και τι αλλάζει όταν ο attacker έχει φυσική πρόσβαση.
- **Device controls**
  Στο **Device controls**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.
- **Workspace controls**
  Για το **Workspace controls**, δες το workflow σαν reproducible local environment: paths, package/source provenance, permissions, environment state, error handling και rollback. Στο Termux προτίμησε standard-library εργαλεία, explicit paths και δοκιμές σε harmless local files/services.
- **Visitor and contractor process**
  Στο **Visitor and contractor process**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **Removable media**
  Στο **Removable media**, σύνδεσε requirement με owner, asset/data scope, measurable control objective, exception process και evidence. Έλεγξε αν το metric ή policy δείχνει πραγματική μείωση risk και όχι απλώς activity/compliance output.
- **Secure disposal**
  Στο **Secure disposal**, σύνδεσε requirement με owner, asset/data scope, measurable control objective, exception process και evidence. Έλεγξε αν το metric ή policy δείχνει πραγματική μείωση risk και όχι απλώς activity/compliance output.
- **Awareness without harmful deception**
  Στο **Awareness without harmful deception**, σύνδεσε requirement με owner, asset/data scope, measurable control objective, exception process και evidence. Έλεγξε αν το metric ή policy δείχνει πραγματική μείωση risk και όχι απλώς activity/compliance output.
- **Lost-device tabletop**
  Στο **Lost-device tabletop**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.
- **Facility outage tabletop**
  Στο **Facility outage tabletop**, όρισε συγκεκριμένο objective, owned/local scope, expected result και stop condition. Κράτησε μόνο sanitized evidence, σύγκρινε expected με observed behavior και ολοκλήρωσε με remediation και ίδιο regression test.
- **Checkpoint**
  Στο **Checkpoint**, μετέτρεψε τη θεωρία του **Φυσική Ασφάλεια και Ανθρώπινη Ανθεκτικότητα** σε ελέγξιμα κριτήρια: τι πρέπει να μπορείς να εξηγήσεις, ποιο λάθος assumption εμφανίζεται συχνότερα, ποιο safe lab το αποκαλύπτει και ποιο retest αποδεικνύει ότι το διόρθωσες.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Φυσική Ασφάλεια και Ανθρώπινη Ανθεκτικότητα**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε synthetic data και role-play scenarios. Μην χρησιμοποιείς πραγματικά προσωπικά δεδομένα ή παραπλανητικές social-engineering δοκιμές χωρίς ρητή έγκριση.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Φυσική Ασφάλεια και Ανθρώπινη Ανθεκτικότητα**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Φυσική Ασφάλεια και Ανθρώπινη Ανθεκτικότητα** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 060](../../English/09-AI-GRC-Privacy-Data-and-Human-Security/60-Physical-Security-and-Human-Resilience.md)

---

# Μεθοδολογία Security Research και Συλλογιστική Attack Surface

> **Ελληνική έκδοση — Μάθημα 061.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Η κατηγορία αυτή χτίζει τον τρόπο σκέψης που χρειάζεται πριν από οποιοδήποτε τεχνικό test. Η ασφάλεια αντιμετωπίζεται ως σύστημα από assets, identities, trust boundaries, δεδομένα, controls και αποδεικτικά στοιχεία. Το ζητούμενο δεν είναι να απομνημονεύσεις εργαλεία αλλά να μπορείς να εξηγήσεις τι προστατεύεται, από ποια απειλή, με ποια υπόθεση και πώς αποδεικνύεται το αποτέλεσμα.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Μεθοδολογία Security Research και Συλλογιστική Attack Surface**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **The research mindset**
  Για το **The research mindset**, στο πλαίσιο του **Μεθοδολογία Security Research και Συλλογιστική Attack Surface**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Attack surface versus vulnerability**
  Για το **Attack surface versus vulnerability**, στο πλαίσιο του **Μεθοδολογία Security Research και Συλλογιστική Attack Surface**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Model the system as graphs**
  Για το **Model the system as graphs**, στο πλαίσιο του **Μεθοδολογία Security Research και Συλλογιστική Attack Surface**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Trust boundaries**
  Για το **Trust boundaries**, στο πλαίσιο του **Μεθοδολογία Security Research και Συλλογιστική Attack Surface**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Ασφάλεια properties and invariants**
  Για το **Ασφάλεια properties and invariants**, στο πλαίσιο του **Μεθοδολογία Security Research και Συλλογιστική Attack Surface**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **State-machine thinking**
  Για το **State-machine thinking**, στο πλαίσιο του **Μεθοδολογία Security Research και Συλλογιστική Attack Surface**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Differential testing**
  Για το **Differential testing**, δες το workflow σαν reproducible local environment: paths, package/source provenance, permissions, environment state, error handling και rollback. Στο Termux προτίμησε standard-library εργαλεία, explicit paths και δοκιμές σε harmless local files/services.
- **Canonicalization and representation gaps**
  Για το **Canonicalization and representation gaps**, στο πλαίσιο του **Μεθοδολογία Security Research και Συλλογιστική Attack Surface**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Identity translation**
  Για το **Identity translation**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Failure-path analysis**
  Για το **Failure-path analysis**, στο πλαίσιο του **Μεθοδολογία Security Research και Συλλογιστική Attack Surface**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Evidence quality**
  Στο **Evidence quality**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Safe advanced practice**
  Για το **Safe advanced practice**, στο πλαίσιο του **Μεθοδολογία Security Research και Συλλογιστική Attack Surface**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Research notebook template**
  Για το **Research notebook template**, στο πλαίσιο του **Μεθοδολογία Security Research και Συλλογιστική Attack Surface**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Deep-study checkpoint**
  Στο **Deep-study checkpoint**, μετέτρεψε τη θεωρία του **Μεθοδολογία Security Research και Συλλογιστική Attack Surface** σε ελέγξιμα κριτήρια: τι πρέπει να μπορείς να εξηγήσεις, ποιο λάθος assumption εμφανίζεται συχνότερα, ποιο safe lab το αποκαλύπτει και ποιο retest αποδεικνύει ότι το διόρθωσες.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Μεθοδολογία Security Research και Συλλογιστική Attack Surface**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Δούλεψε με ένα υποθετικό ή δικό σου lab. Σχεδίασε scope, assets, trust boundaries και αναμενόμενα evidence πριν αλλάξεις οτιδήποτε.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Μεθοδολογία Security Research και Συλλογιστική Attack Surface**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Μεθοδολογία Security Research και Συλλογιστική Attack Surface** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 061](../../English/01-Fundamentals-and-Methodology/61-Security-Research-Methodology-and-Attack-Surface-Reasoning.md)

---

# CPU Privilege, Syscalls και Εσωτερική Λειτουργία Processes

> **Ελληνική έκδοση — Μάθημα 062.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Η ασφάλεια συστημάτων βασίζεται στα πραγματικά boundaries του λειτουργικού: processes, memory mappings, privilege levels, handles/file descriptors, executable loading, syscalls, services και telemetry. Σε reverse engineering και vulnerability research το σημαντικό είναι να συνδέεις συμπεριφορά υψηλού επιπέδου με χαμηλού επιπέδου state χωρίς να συμπεραίνεις περισσότερα από όσα δείχνουν τα δεδομένα.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **CPU Privilege, Syscalls και Εσωτερική Λειτουργία Processes**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Why internals matter**
  Για το **Why internals matter**, στο πλαίσιο του **CPU Privilege, Syscalls και Εσωτερική Λειτουργία Processes**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **CPU privilege model**
  Στο **CPU privilege model**, σύνδεσε ABI/OS abstraction με το πραγματικό machine/runtime state: registers, addresses, object handles, loader metadata και privilege transition. Χρησιμοποίησε μικρό δικό σου binary, disassembler/debugger και annotated trace ώστε κάθε inference να έχει observable βάση.
- **Virtual memory**
  Στο **Virtual memory**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **User-kernel transition**
  Στο **User-kernel transition**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **File descriptors and object handles**
  Στο **File descriptors and object handles**, σύνδεσε ABI/OS abstraction με το πραγματικό machine/runtime state: registers, addresses, object handles, loader metadata και privilege transition. Χρησιμοποίησε μικρό δικό σου binary, disassembler/debugger και annotated trace ώστε κάθε inference να έχει observable βάση.
- **Process creation**
  Στο **Process creation**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **Threads and concurrency**
  Στο **Threads and concurrency**, σύνδεσε ABI/OS abstraction με το πραγματικό machine/runtime state: registers, addresses, object handles, loader metadata και privilege transition. Χρησιμοποίησε μικρό δικό σου binary, disassembler/debugger και annotated trace ώστε κάθε inference να έχει observable βάση.
- **Memory mappings**
  Στο **Memory mappings**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **Credentials and security context**
  Στο **Credentials and security context**, σύνδεσε ABI/OS abstraction με το πραγματικό machine/runtime state: registers, addresses, object handles, loader metadata και privilege transition. Χρησιμοποίησε μικρό δικό σου binary, disassembler/debugger και annotated trace ώστε κάθε inference να έχει observable βάση.
- **IPC and local trust boundaries**
  Στο **IPC and local trust boundaries**, σύνδεσε ABI/OS abstraction με το πραγματικό machine/runtime state: registers, addresses, object handles, loader metadata και privilege transition. Χρησιμοποίησε μικρό δικό σου binary, disassembler/debugger και annotated trace ώστε κάθε inference να έχει observable βάση.
- **Signals, exceptions, and asynchronous control flow**
  Στο **Signals, exceptions, and asynchronous control flow**, σύνδεσε ABI/OS abstraction με το πραγματικό machine/runtime state: registers, addresses, object handles, loader metadata και privilege transition. Χρησιμοποίησε μικρό δικό σου binary, disassembler/debugger και annotated trace ώστε κάθε inference να έχει observable βάση.
- **/proc as a learning surface**
  Για το **/proc as a learning surface**, κατέγραψε Linux UID/GID/capabilities, namespace membership, syscall/filesystem boundary και LSM/seccomp policy. Έλεγξε effective privilege μέσα σε disposable VM/container και χρησιμοποίησε `/proc`, audit/logging και configuration diff ως evidence.
- **Syscall tracing as explanation**
  Στο **Syscall tracing as explanation**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **Privilege-boundary review checklist**
  Στο **Privilege-boundary review checklist**, σύνδεσε ABI/OS abstraction με το πραγματικό machine/runtime state: registers, addresses, object handles, loader metadata και privilege transition. Χρησιμοποίησε μικρό δικό σου binary, disassembler/debugger και annotated trace ώστε κάθε inference να έχει observable βάση.
- **Safe lab: process anatomy**
  Στο **Safe lab: process anatomy**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **CPU Privilege, Syscalls και Εσωτερική Λειτουργία Processes**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Δούλεψε σε disposable VM ή local test binary. Προτίμησε harmless toy programs, sanitizers, debuggers και read-only inspection. Μην μετατρέπεις crash analysis σε weaponized exploitation.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **CPU Privilege, Syscalls και Εσωτερική Λειτουργία Processes**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **CPU Privilege, Syscalls και Εσωτερική Λειτουργία Processes** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 062](../../English/03-Systems-Malware-and-Reverse-Engineering/62-CPU-Privilege-Syscalls-and-Process-Internals.md)

---

# Assembly για Security Analysis — x86-64 και ARM64

> **Ελληνική έκδοση — Μάθημα 063.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Η ασφάλεια συστημάτων βασίζεται στα πραγματικά boundaries του λειτουργικού: processes, memory mappings, privilege levels, handles/file descriptors, executable loading, syscalls, services και telemetry. Σε reverse engineering και vulnerability research το σημαντικό είναι να συνδέεις συμπεριφορά υψηλού επιπέδου με χαμηλού επιπέδου state χωρίς να συμπεραίνεις περισσότερα από όσα δείχνουν τα δεδομένα.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Assembly για Security Analysis — x86-64 και ARM64**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Machine code, assembly, and architecture**
  Στο **Machine code, assembly, and architecture**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **Registers**
  Στο **Registers**, σύνδεσε ABI/OS abstraction με το πραγματικό machine/runtime state: registers, addresses, object handles, loader metadata και privilege transition. Χρησιμοποίησε μικρό δικό σου binary, disassembler/debugger και annotated trace ώστε κάθε inference να έχει observable βάση.
- **Calling conventions**
  Στο **Calling conventions**, σύνδεσε ABI/OS abstraction με το πραγματικό machine/runtime state: registers, addresses, object handles, loader metadata και privilege transition. Χρησιμοποίησε μικρό δικό σου binary, disassembler/debugger και annotated trace ώστε κάθε inference να έχει observable βάση.
- **Stack concepts**
  Στο **Stack concepts**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **Core x86-64 vocabulary**
  Στο **Core x86-64 vocabulary**, σύνδεσε ABI/OS abstraction με το πραγματικό machine/runtime state: registers, addresses, object handles, loader metadata και privilege transition. Χρησιμοποίησε μικρό δικό σου binary, disassembler/debugger και annotated trace ώστε κάθε inference να έχει observable βάση.
- **Core AArch64 vocabulary**
  Στο **Core AArch64 vocabulary**, σύνδεσε ABI/OS abstraction με το πραγματικό machine/runtime state: registers, addresses, object handles, loader metadata και privilege transition. Χρησιμοποίησε μικρό δικό σου binary, disassembler/debugger και annotated trace ώστε κάθε inference να έχει observable βάση.
- **Endianness and integer width**
  Στο **Endianness and integer width**, σύνδεσε ABI/OS abstraction με το πραγματικό machine/runtime state: registers, addresses, object handles, loader metadata και privilege transition. Χρησιμοποίησε μικρό δικό σου binary, disassembler/debugger και annotated trace ώστε κάθε inference να έχει observable βάση.
- **Pointers versus values**
  Στο **Pointers versus values**, σύνδεσε ABI/OS abstraction με το πραγματικό machine/runtime state: registers, addresses, object handles, loader metadata και privilege transition. Χρησιμοποίησε μικρό δικό σου binary, disassembler/debugger και annotated trace ώστε κάθε inference να έχει observable βάση.
- **Control-flow reconstruction**
  Στο **Control-flow reconstruction**, ξεχώρισε root cause από exploitability. Κατέγραψε faulting operation, object lifetime/size, register και memory context, ενεργές mitigations και το μικρότερο harmless reproducer· επιβεβαίωσε τη διόρθωση με sanitizer/debugger και regression test.
- **Data-flow reconstruction**
  Για το **Data-flow reconstruction**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Compiler optimizations**
  Για το **Compiler optimizations**, ακολούθησε data/control flow από source σε sink, σημείωσε validation και ownership assumptions και έλεγξε πού εφαρμόζεται enforcement. Χρησιμοποίησε tests και static/runtime evidence για να ξεχωρίσεις root cause από απλό code smell.
- **Safe local disassembly lab**
  Στο **Safe local disassembly lab**, σύνδεσε ABI/OS abstraction με το πραγματικό machine/runtime state: registers, addresses, object handles, loader metadata και privilege transition. Χρησιμοποίησε μικρό δικό σου binary, disassembler/debugger και annotated trace ώστε κάθε inference να έχει observable βάση.
- **ARM64 and Termux**
  Για το **ARM64 and Termux**, δες το workflow σαν reproducible local environment: paths, package/source provenance, permissions, environment state, error handling και rollback. Στο Termux προτίμησε standard-library εργαλεία, explicit paths και δοκιμές σε harmless local files/services.
- **Recognizing defensive mitigations in code**
  Για το **Recognizing defensive mitigations in code**, ακολούθησε data/control flow από source σε sink, σημείωσε validation και ownership assumptions και έλεγξε πού εφαρμόζεται enforcement. Χρησιμοποίησε tests και static/runtime evidence για να ξεχωρίσεις root cause από απλό code smell.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Assembly για Security Analysis — x86-64 και ARM64**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Δούλεψε σε disposable VM ή local test binary. Προτίμησε harmless toy programs, sanitizers, debuggers και read-only inspection. Μην μετατρέπεις crash analysis σε weaponized exploitation.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Assembly για Security Analysis — x86-64 και ARM64**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Assembly για Security Analysis — x86-64 και ARM64** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 063](../../English/03-Systems-Malware-and-Reverse-Engineering/63-Assembly-for-Security-Analysis-x86-64-and-ARM64.md)

---

# Executable Formats, Loaders και Dynamic Linking

> **Ελληνική έκδοση — Μάθημα 064.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Η ασφάλεια συστημάτων βασίζεται στα πραγματικά boundaries του λειτουργικού: processes, memory mappings, privilege levels, handles/file descriptors, executable loading, syscalls, services και telemetry. Σε reverse engineering και vulnerability research το σημαντικό είναι να συνδέεις συμπεριφορά υψηλού επιπέδου με χαμηλού επιπέδου state χωρίς να συμπεραίνεις περισσότερα από όσα δείχνουν τα δεδομένα.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Executable Formats, Loaders και Dynamic Linking**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **From source to process**
  Στο **From source to process**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **ELF mental model**
  Στο **ELF mental model**, σύνδεσε ABI/OS abstraction με το πραγματικό machine/runtime state: registers, addresses, object handles, loader metadata και privilege transition. Χρησιμοποίησε μικρό δικό σου binary, disassembler/debugger και annotated trace ώστε κάθε inference να έχει observable βάση.
- **PE/COFF mental model**
  Στο **PE/COFF mental model**, σύνδεσε ABI/OS abstraction με το πραγματικό machine/runtime state: registers, addresses, object handles, loader metadata και privilege transition. Χρησιμοποίησε μικρό δικό σου binary, disassembler/debugger και annotated trace ώστε κάθε inference να έχει observable βάση.
- **Static versus dynamic linking**
  Στο **Static versus dynamic linking**, συσχέτισε static evidence με runtime observation. Μην αντιμετωπίζεις strings ή decompiler output ως απόδειξη· ακολούθησε references, callers/callees, data flow και state transitions σε harmless local binary και κατέγραψε confidence για κάθε συμπέρασμα.
- **Imports, exports, and symbols**
  Στο **Imports, exports, and symbols**, σύνδεσε ABI/OS abstraction με το πραγματικό machine/runtime state: registers, addresses, object handles, loader metadata και privilege transition. Χρησιμοποίησε μικρό δικό σου binary, disassembler/debugger και annotated trace ώστε κάθε inference να έχει observable βάση.
- **Relocations and ASLR**
  Στο **Relocations and ASLR**, ξεχώρισε root cause από exploitability. Κατέγραψε faulting operation, object lifetime/size, register και memory context, ενεργές mitigations και το μικρότερο harmless reproducer· επιβεβαίωσε τη διόρθωση με sanitizer/debugger και regression test.
- **W^X and memory permissions**
  Για το **W^X and memory permissions**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Initialization and entry points**
  Στο **Initialization and entry points**, σύνδεσε ABI/OS abstraction με το πραγματικό machine/runtime state: registers, addresses, object handles, loader metadata και privilege transition. Χρησιμοποίησε μικρό δικό σου binary, disassembler/debugger και annotated trace ώστε κάθε inference να έχει observable βάση.
- **File hashing and provenance**
  Για το **File hashing and provenance**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **Safe ELF lab**
  Στο **Safe ELF lab**, σύνδεσε ABI/OS abstraction με το πραγματικό machine/runtime state: registers, addresses, object handles, loader metadata και privilege transition. Χρησιμοποίησε μικρό δικό σου binary, disassembler/debugger και annotated trace ώστε κάθε inference να έχει observable βάση.
- **Safe Windows/PE lab**
  Για το **Safe Windows/PE lab**, στο πλαίσιο του **Executable Formats, Loaders και Dynamic Linking**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Loader security review**
  Στο **Loader security review**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **Android native libraries**
  Στο **Android native libraries**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Executable Formats, Loaders και Dynamic Linking**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Δούλεψε σε disposable VM ή local test binary. Προτίμησε harmless toy programs, sanitizers, debuggers και read-only inspection. Μην μετατρέπεις crash analysis σε weaponized exploitation.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Executable Formats, Loaders και Dynamic Linking**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Executable Formats, Loaders και Dynamic Linking** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 064](../../English/03-Systems-Malware-and-Reverse-Engineering/64-Executable-Formats-Loaders-and-Dynamic-Linking.md)

---

# Debugging, Crash Triage και Root-Cause Analysis

> **Ελληνική έκδοση — Μάθημα 065.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Η ασφάλεια συστημάτων βασίζεται στα πραγματικά boundaries του λειτουργικού: processes, memory mappings, privilege levels, handles/file descriptors, executable loading, syscalls, services και telemetry. Σε reverse engineering και vulnerability research το σημαντικό είναι να συνδέεις συμπεριφορά υψηλού επιπέδου με χαμηλού επιπέδου state χωρίς να συμπεραίνεις περισσότερα από όσα δείχνουν τα δεδομένα.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Debugging, Crash Triage και Root-Cause Analysis**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Why a crash is only the beginning**
  Στο **Why a crash is only the beginning**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **First-response checklist**
  Για το **First-response checklist**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **Crash classes**
  Στο **Crash classes**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **Invalid memory access**
  Στο **Invalid memory access**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **Assertion or explicit abort**
  Στο **Assertion or explicit abort**, ξεχώρισε root cause από exploitability. Κατέγραψε faulting operation, object lifetime/size, register και memory context, ενεργές mitigations και το μικρότερο harmless reproducer· επιβεβαίωσε τη διόρθωση με sanitizer/debugger και regression test.
- **Stack exhaustion**
  Στο **Stack exhaustion**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **Resource exhaustion**
  Στο **Resource exhaustion**, ξεχώρισε root cause από exploitability. Κατέγραψε faulting operation, object lifetime/size, register και memory context, ενεργές mitigations και το μικρότερο harmless reproducer· επιβεβαίωσε τη διόρθωση με sanitizer/debugger και regression test.
- **Race-related fault**
  Στο **Race-related fault**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **Build for diagnosis**
  Για το **Build for diagnosis**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **Reading a stack trace**
  Στο **Reading a stack trace**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **Registers and fault context**
  Στο **Registers and fault context**, ξεχώρισε root cause από exploitability. Κατέγραψε faulting operation, object lifetime/size, register και memory context, ενεργές mitigations και το μικρότερο harmless reproducer· επιβεβαίωσε τη διόρθωση με sanitizer/debugger και regression test.
- **Core dumps and minidumps**
  Στο **Core dumps and minidumps**, ξεχώρισε root cause από exploitability. Κατέγραψε faulting operation, object lifetime/size, register και memory context, ενεργές mitigations και το μικρότερο harmless reproducer· επιβεβαίωσε τη διόρθωση με sanitizer/debugger και regression test.
- **Minimize the reproducer**
  Στο **Minimize the reproducer**, ξεχώρισε root cause από exploitability. Κατέγραψε faulting operation, object lifetime/size, register και memory context, ενεργές mitigations και το μικρότερο harmless reproducer· επιβεβαίωσε τη διόρθωση με sanitizer/debugger και regression test.
- **Triage memory corruption**
  Στο **Triage memory corruption**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **Exploitability is a separate assessment**
  Στο **Exploitability is a separate assessment**, ξεχώρισε root cause από exploitability. Κατέγραψε faulting operation, object lifetime/size, register και memory context, ενεργές mitigations και το μικρότερο harmless reproducer· επιβεβαίωσε τη διόρθωση με sanitizer/debugger και regression test.
- **Patch quality**
  Στο **Patch quality**, ξεχώρισε root cause από exploitability. Κατέγραψε faulting operation, object lifetime/size, register και memory context, ενεργές mitigations και το μικρότερο harmless reproducer· επιβεβαίωσε τη διόρθωση με sanitizer/debugger και regression test.
- **Safe debugger lab**
  Για το **Safe debugger lab**, στο πλαίσιο του **Debugging, Crash Triage και Root-Cause Analysis**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Crash-report template**
  Στο **Crash-report template**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Debugging, Crash Triage και Root-Cause Analysis**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Δούλεψε σε disposable VM ή local test binary. Προτίμησε harmless toy programs, sanitizers, debuggers και read-only inspection. Μην μετατρέπεις crash analysis σε weaponized exploitation.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Debugging, Crash Triage και Root-Cause Analysis**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Debugging, Crash Triage και Root-Cause Analysis** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 065](../../English/03-Systems-Malware-and-Reverse-Engineering/65-Debugging-Crash-Triage-and-Root-Cause-Analysis.md)

---

# Μηχανισμοί Memory Corruption και Ανάλυση Mitigations

> **Ελληνική έκδοση — Μάθημα 066.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Η ασφάλεια συστημάτων βασίζεται στα πραγματικά boundaries του λειτουργικού: processes, memory mappings, privilege levels, handles/file descriptors, executable loading, syscalls, services και telemetry. Σε reverse engineering και vulnerability research το σημαντικό είναι να συνδέεις συμπεριφορά υψηλού επιπέδου με χαμηλού επιπέδου state χωρίς να συμπεραίνεις περισσότερα από όσα δείχνουν τα δεδομένα.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Μηχανισμοί Memory Corruption και Ανάλυση Mitigations**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Spatial and temporal safety**
  Στο **Spatial and temporal safety**, ξεχώρισε root cause από exploitability. Κατέγραψε faulting operation, object lifetime/size, register και memory context, ενεργές mitigations και το μικρότερο harmless reproducer· επιβεβαίωσε τη διόρθωση με sanitizer/debugger και regression test.
- **Stack objects**
  Στο **Stack objects**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **Heap objects**
  Στο **Heap objects**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **Integer errors as memory precursors**
  Στο **Integer errors as memory precursors**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **Type confusion**
  Στο **Type confusion**, ξεχώρισε root cause από exploitability. Κατέγραψε faulting operation, object lifetime/size, register και memory context, ενεργές mitigations και το μικρότερο harmless reproducer· επιβεβαίωσε τη διόρθωση με sanitizer/debugger και regression test.
- **Control data versus ordinary data**
  Για το **Control data versus ordinary data**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **ASLR in detail**
  Στο **ASLR in detail**, ξεχώρισε root cause από exploitability. Κατέγραψε faulting operation, object lifetime/size, register και memory context, ενεργές mitigations και το μικρότερο harmless reproducer· επιβεβαίωσε τη διόρθωση με sanitizer/debugger και regression test.
- **NX / DEP and executable permissions**
  Για το **NX / DEP and executable permissions**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Stack canaries**
  Στο **Stack canaries**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **RELRO and relocation hardening**
  Στο **RELRO and relocation hardening**, ξεχώρισε root cause από exploitability. Κατέγραψε faulting operation, object lifetime/size, register και memory context, ενεργές mitigations και το μικρότερο harmless reproducer· επιβεβαίωσε τη διόρθωση με sanitizer/debugger και regression test.
- **Control-Flow Integrity, CET, and shadow stacks**
  Στο **Control-Flow Integrity, CET, and shadow stacks**, ξεχώρισε root cause από exploitability. Κατέγραψε faulting operation, object lifetime/size, register και memory context, ενεργές mitigations και το μικρότερο harmless reproducer· επιβεβαίωσε τη διόρθωση με sanitizer/debugger και regression test.
- **ARM pointer authentication and branch protection**
  Για το **ARM pointer authentication and branch protection**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Memory tagging**
  Στο **Memory tagging**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **Safe code-reuse concepts**
  Για το **Safe code-reuse concepts**, ακολούθησε data/control flow από source σε sink, σημείωσε validation και ownership assumptions και έλεγξε πού εφαρμόζεται enforcement. Χρησιμοποίησε tests και static/runtime evidence για να ξεχωρίσεις root cause από απλό code smell.
- **Exploitability triage matrix**
  Για το **Exploitability triage matrix**, όρισε decision owner, trigger, required telemetry, χρονική σειρά ενεργειών και πιθανό operational impact. Η σωστή απόφαση πρέπει να είναι αναστρέψιμη όπου γίνεται, να διατηρεί evidence και να συνδέεται με σαφές recovery/retest criterion.
- **Sanitizer-guided local lab**
  Για το **Sanitizer-guided local lab**, σχεδίασε deterministic harness με σαφή input boundary, bounded resources και reproducible crash capture. Χρησιμοποίησε coverage/sanitizers ως feedback, κάνε minimize κάθε failure και κράτησε regression input μόνο για λογισμικό που ελέγχεις.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Μηχανισμοί Memory Corruption και Ανάλυση Mitigations**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Δούλεψε σε disposable VM ή local test binary. Προτίμησε harmless toy programs, sanitizers, debuggers και read-only inspection. Μην μετατρέπεις crash analysis σε weaponized exploitation.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Μηχανισμοί Memory Corruption και Ανάλυση Mitigations**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Μηχανισμοί Memory Corruption και Ανάλυση Mitigations** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 066](../../English/03-Systems-Malware-and-Reverse-Engineering/66-Memory-Corruption-Mechanics-and-Mitigation-Analysis.md)

---

# Reverse Engineering και Ανάλυση Προγραμμάτων

> **Ελληνική έκδοση — Μάθημα 067.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Η ασφάλεια συστημάτων βασίζεται στα πραγματικά boundaries του λειτουργικού: processes, memory mappings, privilege levels, handles/file descriptors, executable loading, syscalls, services και telemetry. Σε reverse engineering και vulnerability research το σημαντικό είναι να συνδέεις συμπεριφορά υψηλού επιπέδου με χαμηλού επιπέδου state χωρίς να συμπεραίνεις περισσότερα από όσα δείχνουν τα δεδομένα.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Reverse Engineering και Ανάλυση Προγραμμάτων**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Static versus dynamic analysis**
  Για το **Static versus dynamic analysis**, σύνδεσε Android package/runtime behavior με UID sandbox, exported components, Binder/Intent boundaries, signing identity και Keystore-backed secrets. Επιβεβαίωσε το behavior σε δικό σου APK ή emulator και όχι σε τρίτες εφαρμογές.
- **Start with provenance**
  Για το **Start with provenance**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **Triage before decompiling everything**
  Για το **Triage before decompiling everything**, όρισε decision owner, trigger, required telemetry, χρονική σειρά ενεργειών και πιθανό operational impact. Η σωστή απόφαση πρέπει να είναι αναστρέψιμη όπου γίνεται, να διατηρεί evidence και να συνδέεται με σαφές recovery/retest criterion.
- **Strings as clues, not conclusions**
  Στο **Strings as clues, not conclusions**, συσχέτισε static evidence με runtime observation. Μην αντιμετωπίζεις strings ή decompiler output ως απόδειξη· ακολούθησε references, callers/callees, data flow και state transitions σε harmless local binary και κατέγραψε confidence για κάθε συμπέρασμα.
- **Function identification**
  Στο **Function identification**, συσχέτισε static evidence με runtime observation. Μην αντιμετωπίζεις strings ή decompiler output ως απόδειξη· ακολούθησε references, callers/callees, data flow και state transitions σε harmless local binary και κατέγραψε confidence για κάθε συμπέρασμα.
- **Decompiler output**
  Στο **Decompiler output**, συσχέτισε static evidence με runtime observation. Μην αντιμετωπίζεις strings ή decompiler output ως απόδειξη· ακολούθησε references, callers/callees, data flow και state transitions σε harmless local binary και κατέγραψε confidence για κάθε συμπέρασμα.
- **Cross-references**
  Για το **Cross-references**, ξεχώρισε normative specification από tutorial ή vendor summary. Κατέγραψε έκδοση/ημερομηνία, ποιο requirement στηρίζει το συμπέρασμα και ποιο μέρος του **Reverse Engineering και Ανάλυση Προγραμμάτων** χρειάζεται επανέλεγχο όταν αλλάξει η πηγή.
- **Recovering data structures**
  Για το **Recovering data structures**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Indirect calls and virtual dispatch**
  Στο **Indirect calls and virtual dispatch**, συσχέτισε static evidence με runtime observation. Μην αντιμετωπίζεις strings ή decompiler output ως απόδειξη· ακολούθησε references, callers/callees, data flow και state transitions σε harmless local binary και κατέγραψε confidence για κάθε συμπέρασμα.
- **State-machine reconstruction**
  Στο **State-machine reconstruction**, συσχέτισε static evidence με runtime observation. Μην αντιμετωπίζεις strings ή decompiler output ως απόδειξη· ακολούθησε references, callers/callees, data flow και state transitions σε harmless local binary και κατέγραψε confidence για κάθε συμπέρασμα.
- **Dynamic observation**
  Στο **Dynamic observation**, συσχέτισε static evidence με runtime observation. Μην αντιμετωπίζεις strings ή decompiler output ως απόδειξη· ακολούθησε references, callers/callees, data flow και state transitions σε harmless local binary και κατέγραψε confidence για κάθε συμπέρασμα.
- **Patching as a learning tool**
  Στο **Patching as a learning tool**, συσχέτισε static evidence με runtime observation. Μην αντιμετωπίζεις strings ή decompiler output ως απόδειξη· ακολούθησε references, callers/callees, data flow και state transitions σε harmless local binary και κατέγραψε confidence για κάθε συμπέρασμα.
- **Obfuscation and packing**
  Για το **Obfuscation and packing**, σύνδεσε Android package/runtime behavior με UID sandbox, exported components, Binder/Intent boundaries, signing identity και Keystore-backed secrets. Επιβεβαίωσε το behavior σε δικό σου APK ή emulator και όχι σε τρίτες εφαρμογές.
- **Safe local reverse-engineering lab**
  Για το **Safe local reverse-engineering lab**, στο πλαίσιο του **Reverse Engineering και Ανάλυση Προγραμμάτων**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Reverse-engineering notebook**
  Στο **Reverse-engineering notebook**, συσχέτισε static evidence με runtime observation. Μην αντιμετωπίζεις strings ή decompiler output ως απόδειξη· ακολούθησε references, callers/callees, data flow και state transitions σε harmless local binary και κατέγραψε confidence για κάθε συμπέρασμα.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Reverse Engineering και Ανάλυση Προγραμμάτων**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Δούλεψε σε disposable VM ή local test binary. Προτίμησε harmless toy programs, sanitizers, debuggers και read-only inspection. Μην μετατρέπεις crash analysis σε weaponized exploitation.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Reverse Engineering και Ανάλυση Προγραμμάτων**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Reverse Engineering και Ανάλυση Προγραμμάτων** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 067](../../English/03-Systems-Malware-and-Reverse-Engineering/67-Reverse-Engineering-and-Program-Analysis.md)

---

# Fuzzing, Harness Design και Coverage-Guided Testing

> **Ελληνική έκδοση — Μάθημα 068.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Η ασφάλεια συστημάτων βασίζεται στα πραγματικά boundaries του λειτουργικού: processes, memory mappings, privilege levels, handles/file descriptors, executable loading, syscalls, services και telemetry. Σε reverse engineering και vulnerability research το σημαντικό είναι να συνδέεις συμπεριφορά υψηλού επιπέδου με χαμηλού επιπέδου state χωρίς να συμπεραίνεις περισσότερα από όσα δείχνουν τα δεδομένα.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Fuzzing, Harness Design και Coverage-Guided Testing**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **What fuzzing actually does**
  Στο **What fuzzing actually does**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **Fuzzing models**
  Στο **Fuzzing models**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **Mutation-based**
  Για το **Mutation-based**, σχεδίασε deterministic harness με σαφή input boundary, bounded resources και reproducible crash capture. Χρησιμοποίησε coverage/sanitizers ως feedback, κάνε minimize κάθε failure και κράτησε regression input μόνο για λογισμικό που ελέγχεις.
- **Generation-based**
  Για το **Generation-based**, σχεδίασε deterministic harness με σαφή input boundary, bounded resources και reproducible crash capture. Χρησιμοποίησε coverage/sanitizers ως feedback, κάνε minimize κάθε failure και κράτησε regression input μόνο για λογισμικό που ελέγχεις.
- **Coverage-guided**
  Για το **Coverage-guided**, σχεδίασε deterministic harness με σαφή input boundary, bounded resources και reproducible crash capture. Χρησιμοποίησε coverage/sanitizers ως feedback, κάνε minimize κάθε failure και κράτησε regression input μόνο για λογισμικό που ελέγχεις.
- **Property-based**
  Για το **Property-based**, σχεδίασε deterministic harness με σαφή input boundary, bounded resources και reproducible crash capture. Χρησιμοποίησε coverage/sanitizers ως feedback, κάνε minimize κάθε failure και κράτησε regression input μόνο για λογισμικό που ελέγχεις.
- **Stateful/protocol fuzzing**
  Στο **Stateful/protocol fuzzing**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.
- **Harness design**
  Για το **Harness design**, σχεδίασε deterministic harness με σαφή input boundary, bounded resources και reproducible crash capture. Χρησιμοποίησε coverage/sanitizers ως feedback, κάνε minimize κάθε failure και κράτησε regression input μόνο για λογισμικό που ελέγχεις.
- **Corpus design**
  Για το **Corpus design**, σχεδίασε deterministic harness με σαφή input boundary, bounded resources και reproducible crash capture. Χρησιμοποίησε coverage/sanitizers ως feedback, κάνε minimize κάθε failure και κράτησε regression input μόνο για λογισμικό που ελέγχεις.
- **Coverage is a guide, not a goal**
  Για το **Coverage is a guide, not a goal**, σχεδίασε deterministic harness με σαφή input boundary, bounded resources και reproducible crash capture. Χρησιμοποίησε coverage/sanitizers ως feedback, κάνε minimize κάθε failure και κράτησε regression input μόνο για λογισμικό που ελέγχεις.
- **Sanitizers**
  Για το **Sanitizers**, σχεδίασε deterministic harness με σαφή input boundary, bounded resources και reproducible crash capture. Χρησιμοποίησε coverage/sanitizers ως feedback, κάνε minimize κάθε failure και κράτησε regression input μόνο για λογισμικό που ελέγχεις.
- **Timeouts and hangs**
  Για το **Timeouts and hangs**, σχεδίασε deterministic harness με σαφή input boundary, bounded resources και reproducible crash capture. Χρησιμοποίησε coverage/sanitizers ως feedback, κάνε minimize κάθε failure και κράτησε regression input μόνο για λογισμικό που ελέγχεις.
- **Crash deduplication**
  Στο **Crash deduplication**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **Minimization**
  Για το **Minimization**, σχεδίασε deterministic harness με σαφή input boundary, bounded resources και reproducible crash capture. Χρησιμοποίησε coverage/sanitizers ως feedback, κάνε minimize κάθε failure και κράτησε regression input μόνο για λογισμικό που ελέγχεις.
- **Differential fuzzing**
  Στο **Differential fuzzing**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **Metamorphic testing**
  Για το **Metamorphic testing**, δες το workflow σαν reproducible local environment: paths, package/source provenance, permissions, environment state, error handling και rollback. Στο Termux προτίμησε standard-library εργαλεία, explicit paths και δοκιμές σε harmless local files/services.
- **Safe Python micro-fuzzer**
  Για το **Safe Python micro-fuzzer**, δες το workflow σαν reproducible local environment: paths, package/source provenance, permissions, environment state, error handling και rollback. Στο Termux προτίμησε standard-library εργαλεία, explicit paths και δοκιμές σε harmless local files/services.
- **Fuzzing authorization logic**
  Για το **Fuzzing authorization logic**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **CI integration**
  Για το **CI integration**, σχεδίασε deterministic harness με σαφή input boundary, bounded resources και reproducible crash capture. Χρησιμοποίησε coverage/sanitizers ως feedback, κάνε minimize κάθε failure και κράτησε regression input μόνο για λογισμικό που ελέγχεις.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Fuzzing, Harness Design και Coverage-Guided Testing**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Δούλεψε σε disposable VM ή local test binary. Προτίμησε harmless toy programs, sanitizers, debuggers και read-only inspection. Μην μετατρέπεις crash analysis σε weaponized exploitation.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Fuzzing, Harness Design και Coverage-Guided Testing**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Fuzzing, Harness Design και Coverage-Guided Testing** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 068](../../English/03-Systems-Malware-and-Reverse-Engineering/68-Fuzzing-Harness-Design-and-Coverage-Guided-Testing.md)

---

# Προχωρημένη Επεξεργασία Web Requests και Parser Differentials

> **Ελληνική έκδοση — Μάθημα 069.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Στην εφαρμοσμένη ασφάλεια web και assessments, κάθε request είναι μεταφορά δεδομένων και authority μέσα από πολλαπλά layers. Browser, proxy, web server, framework, API, database και identity provider μπορεί να ερμηνεύουν διαφορετικά την ίδια πληροφορία. Η βαθιά κατανόηση απαιτεί να παρακολουθείς normalization, parsing, state, authentication και authorization αντί να στηρίζεσαι μόνο σε signatures ή έτοιμα scanners.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Προχωρημένη Επεξεργασία Web Requests και Parser Differentials**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **One request, many parsers**
  Για το **One request, many parsers**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **Message framing**
  Για το **Message framing**, στο πλαίσιο του **Προχωρημένη Επεξεργασία Web Requests και Parser Differentials**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Request desynchronization concept**
  Για το **Request desynchronization concept**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **HTTP/2 and downgrade boundaries**
  Στο **HTTP/2 and downgrade boundaries**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.
- **Host and authority handling**
  Για το **Host and authority handling**, στο πλαίσιο του **Προχωρημένη Επεξεργασία Web Requests και Parser Differentials**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Forwarded headers**
  Για το **Forwarded headers**, στο πλαίσιο του **Προχωρημένη Επεξεργασία Web Requests και Parser Differentials**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Path normalization**
  Για το **Path normalization**, στο πλαίσιο του **Προχωρημένη Επεξεργασία Web Requests και Parser Differentials**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Cache keys and security context**
  Για το **Cache keys and security context**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **Origin versus cache response**
  Για το **Origin versus cache response**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **SSRF as a trust-boundary problem**
  Για το **SSRF as a trust-boundary problem**, στο πλαίσιο του **Προχωρημένη Επεξεργασία Web Requests και Parser Differentials**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **URL parser differentials**
  Για το **URL parser differentials**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **Redirect handling**
  Για το **Redirect handling**, στο πλαίσιο του **Προχωρημένη Επεξεργασία Web Requests και Parser Differentials**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Server-side templates and interpreters**
  Για το **Server-side templates and interpreters**, στο πλαίσιο του **Προχωρημένη Επεξεργασία Web Requests και Parser Differentials**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Raw HTTP localhost lab**
  Στο **Raw HTTP localhost lab**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.
- **Deployment regression checklist**
  Για το **Deployment regression checklist**, στο πλαίσιο του **Προχωρημένη Επεξεργασία Web Requests και Parser Differentials**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Προχωρημένη Επεξεργασία Web Requests και Parser Differentials**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε μόνο localhost, intentionally vulnerable training apps ή ρητά εξουσιοδοτημένα συστήματα. Κατέγραψε request/response, server-side logs και την ακριβή security invariant που ελέγχεις.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Προχωρημένη Επεξεργασία Web Requests και Parser Differentials**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Προχωρημένη Επεξεργασία Web Requests και Parser Differentials** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 069](../../English/02-Recon-Pentesting-Web-and-AppSec/69-Advanced-Web-Request-Processing-and-Parser-Differentials.md)

---

# Browser Isolation, Origins, CORS, CSP και Client-Side Trust

> **Ελληνική έκδοση — Μάθημα 070.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Στην εφαρμοσμένη ασφάλεια web και assessments, κάθε request είναι μεταφορά δεδομένων και authority μέσα από πολλαπλά layers. Browser, proxy, web server, framework, API, database και identity provider μπορεί να ερμηνεύουν διαφορετικά την ίδια πληροφορία. Η βαθιά κατανόηση απαιτεί να παρακολουθείς normalization, parsing, state, authentication και authorization αντί να στηρίζεσαι μόνο σε signatures ή έτοιμα scanners.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Browser Isolation, Origins, CORS, CSP και Client-Side Trust**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Origin as a security principal**
  Για το **Origin as a security principal**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **Same-Origin Policy**
  Για το **Same-Origin Policy**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **CORS**
  Για το **CORS**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **Preflight requests**
  Για το **Preflight requests**, στο πλαίσιο του **Browser Isolation, Origins, CORS, CSP και Client-Side Trust**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Cookies and SameSite**
  Για το **Cookies and SameSite**, στο πλαίσιο του **Browser Isolation, Origins, CORS, CSP και Client-Side Trust**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Content Ασφάλεια Policy**
  Για το **Content Ασφάλεια Policy**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Frame isolation**
  Για το **Frame isolation**, στο πλαίσιο του **Browser Isolation, Origins, CORS, CSP και Client-Side Trust**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **postMessage**
  Για το **postMessage**, στο πλαίσιο του **Browser Isolation, Origins, CORS, CSP και Client-Side Trust**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Browser storage**
  Για το **Browser storage**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **Service workers**
  Για το **Service workers**, στο πλαίσιο του **Browser Isolation, Origins, CORS, CSP και Client-Side Trust**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **DOM trust boundaries**
  Για το **DOM trust boundaries**, στο πλαίσιο του **Browser Isolation, Origins, CORS, CSP και Client-Side Trust**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Client-side authorization is not authorization**
  Για το **Client-side authorization is not authorization**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Trusted Types and safer sinks**
  Για το **Trusted Types and safer sinks**, στο πλαίσιο του **Browser Isolation, Origins, CORS, CSP και Client-Side Trust**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Safe local origin lab**
  Για το **Safe local origin lab**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **Ασφάλεια review checklist**
  Για το **Ασφάλεια review checklist**, στο πλαίσιο του **Browser Isolation, Origins, CORS, CSP και Client-Side Trust**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Browser Isolation, Origins, CORS, CSP και Client-Side Trust**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε μόνο localhost, intentionally vulnerable training apps ή ρητά εξουσιοδοτημένα συστήματα. Κατέγραψε request/response, server-side logs και την ακριβή security invariant που ελέγχεις.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Browser Isolation, Origins, CORS, CSP και Client-Side Trust**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Browser Isolation, Origins, CORS, CSP και Client-Side Trust** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 070](../../English/02-Recon-Pentesting-Web-and-AppSec/70-Browser-Isolation-Origins-CORS-CSP-and-Client-Side-Trust.md)

---

# API Authorization, State Machines και Distributed Abuse Cases

> **Ελληνική έκδοση — Μάθημα 071.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Στην εφαρμοσμένη ασφάλεια web και assessments, κάθε request είναι μεταφορά δεδομένων και authority μέσα από πολλαπλά layers. Browser, proxy, web server, framework, API, database και identity provider μπορεί να ερμηνεύουν διαφορετικά την ίδια πληροφορία. Η βαθιά κατανόηση απαιτεί να παρακολουθείς normalization, parsing, state, authentication και authorization αντί να στηρίζεσαι μόνο σε signatures ή έτοιμα scanners.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **API Authorization, State Machines και Distributed Abuse Cases**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Authentication is only the first gate**
  Για το **Authentication is only the first gate**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Object-level authorization**
  Για το **Object-level authorization**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Function-level authorization**
  Για το **Function-level authorization**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Property-level authorization**
  Για το **Property-level authorization**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Authorization matrix**
  Για το **Authorization matrix**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Multi-tenancy**
  Για το **Multi-tenancy**, στο πλαίσιο του **API Authorization, State Machines και Distributed Abuse Cases**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **State-machine authorization**
  Για το **State-machine authorization**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Replay and idempotency**
  Για το **Replay and idempotency**, στο πλαίσιο του **API Authorization, State Machines και Distributed Abuse Cases**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Race conditions and TOCTOU**
  Στο **Race conditions and TOCTOU**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **Event-driven systems**
  Για το **Event-driven systems**, στο πλαίσιο του **API Authorization, State Machines και Distributed Abuse Cases**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Delegation**
  Για το **Delegation**, στο πλαίσιο του **API Authorization, State Machines και Distributed Abuse Cases**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Confused deputy in APIs**
  Για το **Confused deputy in APIs**, στο πλαίσιο του **API Authorization, State Machines και Distributed Abuse Cases**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Pagination, filters, and exports**
  Στο **Pagination, filters, and exports**, σύνδεσε ABI/OS abstraction με το πραγματικό machine/runtime state: registers, addresses, object handles, loader metadata και privilege transition. Χρησιμοποίησε μικρό δικό σου binary, disassembler/debugger και annotated trace ώστε κάθε inference να έχει observable βάση.
- **GraphQL considerations**
  Για το **GraphQL considerations**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **Rate controls and abuse economics**
  Για το **Rate controls and abuse economics**, στο πλαίσιο του **API Authorization, State Machines και Distributed Abuse Cases**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Safe local authorization lab**
  Για το **Safe local authorization lab**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **API Authorization, State Machines και Distributed Abuse Cases**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε μόνο localhost, intentionally vulnerable training apps ή ρητά εξουσιοδοτημένα συστήματα. Κατέγραψε request/response, server-side logs και την ακριβή security invariant που ελέγχεις.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **API Authorization, State Machines και Distributed Abuse Cases**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **API Authorization, State Machines και Distributed Abuse Cases** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 071](../../English/02-Recon-Pentesting-Web-and-AppSec/71-API-Authorization-State-Machines-and-Distributed-Abuse-Cases.md)

---

# Kerberos, Active Directory και Enterprise Identity Internals

> **Ελληνική έκδοση — Μάθημα 072.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Identity και cryptography είναι μηχανισμοί μεταφοράς εμπιστοσύνης. Authentication απαντά ποιος παρουσιάζει ένα credential, authorization τι επιτρέπεται να κάνει, ενώ cryptography προστατεύει συγκεκριμένες ιδιότητες δεδομένων και πρωτοκόλλων. Κλειδιά, tokens, certificates, federation metadata και policy engines είναι όλα authority-bearing artifacts και χρειάζονται σαφή lifecycle.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Kerberos, Active Directory και Enterprise Identity Internals**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Domain identity as a graph**
  Για το **Domain identity as a graph**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Kerberos actors**
  Για το **Kerberos actors**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **TGT and service-ticket flow**
  Για το **TGT and service-ticket flow**, στο πλαίσιο του **Kerberos, Active Directory και Enterprise Identity Internals**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **SPNs**
  Για το **SPNs**, στο πλαίσιο του **Kerberos, Active Directory και Enterprise Identity Internals**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **PAC and authorization data**
  Για το **PAC and authorization data**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **NTLM coexistence**
  Για το **NTLM coexistence**, στο πλαίσιο του **Kerberos, Active Directory και Enterprise Identity Internals**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Directory ACLs**
  Για το **Directory ACLs**, στο πλαίσιο του **Kerberos, Active Directory και Enterprise Identity Internals**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Group Policy**
  Για το **Group Policy**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Delegation**
  Για το **Delegation**, στο πλαίσιο του **Kerberos, Active Directory και Enterprise Identity Internals**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Service accounts**
  Για το **Service accounts**, στο πλαίσιο του **Kerberos, Active Directory και Enterprise Identity Internals**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Trusts**
  Για το **Trusts**, στο πλαίσιο του **Kerberos, Active Directory και Enterprise Identity Internals**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Privileged administration tiers**
  Για το **Privileged administration tiers**, στο πλαίσιο του **Kerberos, Active Directory και Enterprise Identity Internals**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Attack-path thinking without credential theft**
  Για το **Attack-path thinking without credential theft**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Telemetry**
  Στο **Telemetry**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Safe domain lab**
  Για το **Safe domain lab**, στο πλαίσιο του **Kerberos, Active Directory και Enterprise Identity Internals**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Current-reference note**
  Για το **Current-reference note**, ξεχώρισε normative specification από tutorial ή vendor summary. Κατέγραψε έκδοση/ημερομηνία, ποιο requirement στηρίζει το συμπέρασμα και ποιο μέρος του **Kerberos, Active Directory και Enterprise Identity Internals** χρειάζεται επανέλεγχο όταν αλλάξει η πηγή.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Kerberos, Active Directory και Enterprise Identity Internals**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε synthetic identities, test certificates και local identity providers. Χαρτογράφησε issuer, subject, audience, permissions, lifetime, rotation και revocation χωρίς να αποθηκεύεις πραγματικά secrets.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Kerberos, Active Directory και Enterprise Identity Internals**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Kerberos, Active Directory και Enterprise Identity Internals** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 072](../../English/06-Identity-Cryptography-and-Trust/72-Kerberos-Active-Directory-and-Enterprise-Identity-Internals.md)

---

# Windows Internals — Tokens, Services, Registry, ETW και Security Boundaries

> **Ελληνική έκδοση — Μάθημα 073.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Η ασφάλεια συστημάτων βασίζεται στα πραγματικά boundaries του λειτουργικού: processes, memory mappings, privilege levels, handles/file descriptors, executable loading, syscalls, services και telemetry. Σε reverse engineering και vulnerability research το σημαντικό είναι να συνδέεις συμπεριφορά υψηλού επιπέδου με χαμηλού επιπέδου state χωρίς να συμπεραίνεις περισσότερα από όσα δείχνουν τα δεδομένα.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Windows Internals — Tokens, Services, Registry, ETW και Security Boundaries**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Windows object/security model**
  Για το **Windows object/security model**, χαρτογράφησε Windows security principal, token/privileges, object ACL ή service/IPC boundary και το audit/ETW evidence που δείχνει την απόφαση πρόσβασης. Δούλεψε σε disposable Windows VM και έλεγξε effective authority, όχι μόνο configuration text.
- **Access tokens**
  Για το **Access tokens**, χαρτογράφησε Windows security principal, token/privileges, object ACL ή service/IPC boundary και το audit/ETW evidence που δείχνει την απόφαση πρόσβασης. Δούλεψε σε disposable Windows VM και έλεγξε effective authority, όχι μόνο configuration text.
- **SIDs and groups**
  Για το **SIDs and groups**, χαρτογράφησε Windows security principal, token/privileges, object ACL ή service/IPC boundary και το audit/ETW evidence που δείχνει την απόφαση πρόσβασης. Δούλεψε σε disposable Windows VM και έλεγξε effective authority, όχι μόνο configuration text.
- **Privileges**
  Για το **Privileges**, χαρτογράφησε Windows security principal, token/privileges, object ACL ή service/IPC boundary και το audit/ETW evidence που δείχνει την απόφαση πρόσβασης. Δούλεψε σε disposable Windows VM και έλεγξε effective authority, όχι μόνο configuration text.
- **Integrity levels**
  Για το **Integrity levels**, χαρτογράφησε Windows security principal, token/privileges, object ACL ή service/IPC boundary και το audit/ETW evidence που δείχνει την απόφαση πρόσβασης. Δούλεψε σε disposable Windows VM και έλεγξε effective authority, όχι μόνο configuration text.
- **UAC**
  Για το **UAC**, χαρτογράφησε Windows security principal, token/privileges, object ACL ή service/IPC boundary και το audit/ETW evidence που δείχνει την απόφαση πρόσβασης. Δούλεψε σε disposable Windows VM και έλεγξε effective authority, όχι μόνο configuration text.
- **Services**
  Για το **Services**, χαρτογράφησε Windows security principal, token/privileges, object ACL ή service/IPC boundary και το audit/ETW evidence που δείχνει την απόφαση πρόσβασης. Δούλεψε σε disposable Windows VM και έλεγξε effective authority, όχι μόνο configuration text.
- **Registry**
  Για το **Registry**, χαρτογράφησε Windows security principal, token/privileges, object ACL ή service/IPC boundary και το audit/ETW evidence που δείχνει την απόφαση πρόσβασης. Δούλεψε σε disposable Windows VM και έλεγξε effective authority, όχι μόνο configuration text.
- **Named pipes and RPC**
  Για το **Named pipes and RPC**, χαρτογράφησε Windows security principal, token/privileges, object ACL ή service/IPC boundary και το audit/ETW evidence που δείχνει την απόφαση πρόσβασης. Δούλεψε σε disposable Windows VM και έλεγξε effective authority, όχι μόνο configuration text.
- **Process creation and parentage**
  Στο **Process creation and parentage**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **DLL loading**
  Για το **DLL loading**, χαρτογράφησε Windows security principal, token/privileges, object ACL ή service/IPC boundary και το audit/ETW evidence που δείχνει την απόφαση πρόσβασης. Δούλεψε σε disposable Windows VM και έλεγξε effective authority, όχι μόνο configuration text.
- **ETW**
  Για το **ETW**, χαρτογράφησε Windows security principal, token/privileges, object ACL ή service/IPC boundary και το audit/ETW evidence που δείχνει την απόφαση πρόσβασης. Δούλεψε σε disposable Windows VM και έλεγξε effective authority, όχι μόνο configuration text.
- **Windows Event Log**
  Στο **Windows Event Log**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Safe local review lab**
  Για το **Safe local review lab**, στο πλαίσιο του **Windows Internals — Tokens, Services, Registry, ETW και Security Boundaries**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Ασφάλεια-boundary checklist**
  Για το **Ασφάλεια-boundary checklist**, στο πλαίσιο του **Windows Internals — Tokens, Services, Registry, ETW και Security Boundaries**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Windows Internals — Tokens, Services, Registry, ETW και Security Boundaries**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Δούλεψε σε disposable VM ή local test binary. Προτίμησε harmless toy programs, sanitizers, debuggers και read-only inspection. Μην μετατρέπεις crash analysis σε weaponized exploitation.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Windows Internals — Tokens, Services, Registry, ETW και Security Boundaries**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Windows Internals — Tokens, Services, Registry, ETW και Security Boundaries** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 073](../../English/03-Systems-Malware-and-Reverse-Engineering/73-Windows-Internals-Tokens-Services-Registry-ETW-and-Security-Boundaries.md)

---

# Linux Internals — Capabilities, Namespaces, Seccomp, LSM και eBPF

> **Ελληνική έκδοση — Μάθημα 074.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Η ασφάλεια συστημάτων βασίζεται στα πραγματικά boundaries του λειτουργικού: processes, memory mappings, privilege levels, handles/file descriptors, executable loading, syscalls, services και telemetry. Σε reverse engineering και vulnerability research το σημαντικό είναι να συνδέεις συμπεριφορά υψηλού επιπέδου με χαμηλού επιπέδου state χωρίς να συμπεραίνεις περισσότερα από όσα δείχνουν τα δεδομένα.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Linux Internals — Capabilities, Namespaces, Seccomp, LSM και eBPF**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Linux credentials**
  Για το **Linux credentials**, κατέγραψε Linux UID/GID/capabilities, namespace membership, syscall/filesystem boundary και LSM/seccomp policy. Έλεγξε effective privilege μέσα σε disposable VM/container και χρησιμοποίησε `/proc`, audit/logging και configuration diff ως evidence.
- **Capabilities**
  Για το **Capabilities**, κατέγραψε Linux UID/GID/capabilities, namespace membership, syscall/filesystem boundary και LSM/seccomp policy. Έλεγξε effective privilege μέσα σε disposable VM/container και χρησιμοποίησε `/proc`, audit/logging και configuration diff ως evidence.
- **Namespaces**
  Για το **Namespaces**, κατέγραψε Linux UID/GID/capabilities, namespace membership, syscall/filesystem boundary και LSM/seccomp policy. Έλεγξε effective privilege μέσα σε disposable VM/container και χρησιμοποίησε `/proc`, audit/logging και configuration diff ως evidence.
- **User namespaces**
  Για το **User namespaces**, κατέγραψε Linux UID/GID/capabilities, namespace membership, syscall/filesystem boundary και LSM/seccomp policy. Έλεγξε effective privilege μέσα σε disposable VM/container και χρησιμοποίησε `/proc`, audit/logging και configuration diff ως evidence.
- **Cgroups**
  Για το **Cgroups**, κατέγραψε Linux UID/GID/capabilities, namespace membership, syscall/filesystem boundary και LSM/seccomp policy. Έλεγξε effective privilege μέσα σε disposable VM/container και χρησιμοποίησε `/proc`, audit/logging και configuration diff ως evidence.
- **Seccomp**
  Για το **Seccomp**, κατέγραψε Linux UID/GID/capabilities, namespace membership, syscall/filesystem boundary και LSM/seccomp policy. Έλεγξε effective privilege μέσα σε disposable VM/container και χρησιμοποίησε `/proc`, audit/logging και configuration diff ως evidence.
- **Landlock and unprivileged sandboxing**
  Για το **Landlock and unprivileged sandboxing**, κατέγραψε Linux UID/GID/capabilities, namespace membership, syscall/filesystem boundary και LSM/seccomp policy. Έλεγξε effective privilege μέσα σε disposable VM/container και χρησιμοποίησε `/proc`, audit/logging και configuration diff ως evidence.
- **Linux Ασφάλεια Modules**
  Για το **Linux Ασφάλεια Modules**, κατέγραψε Linux UID/GID/capabilities, namespace membership, syscall/filesystem boundary και LSM/seccomp policy. Έλεγξε effective privilege μέσα σε disposable VM/container και χρησιμοποίησε `/proc`, audit/logging και configuration diff ως evidence.
- **nonewprivs**
  Για το **nonewprivs**, κατέγραψε Linux UID/GID/capabilities, namespace membership, syscall/filesystem boundary και LSM/seccomp policy. Έλεγξε effective privilege μέσα σε disposable VM/container και χρησιμοποίησε `/proc`, audit/logging και configuration diff ως evidence.
- **Chroot versus isolation**
  Για το **Chroot versus isolation**, κατέγραψε Linux UID/GID/capabilities, namespace membership, syscall/filesystem boundary και LSM/seccomp policy. Έλεγξε effective privilege μέσα σε disposable VM/container και χρησιμοποίησε `/proc`, audit/logging και configuration diff ως evidence.
- **Kernel attack surface**
  Στο **Kernel attack surface**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **eBPF**
  Στο **eBPF**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **/proc, /sys, and observability**
  Για το **/proc, /sys, and observability**, κατέγραψε Linux UID/GID/capabilities, namespace membership, syscall/filesystem boundary και LSM/seccomp policy. Έλεγξε effective privilege μέσα σε disposable VM/container και χρησιμοποίησε `/proc`, audit/logging και configuration diff ως evidence.
- **Safe isolation lab**
  Για το **Safe isolation lab**, στο πλαίσιο του **Linux Internals — Capabilities, Namespaces, Seccomp, LSM και eBPF**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Hardening review**
  Για το **Hardening review**, κατέγραψε Linux UID/GID/capabilities, namespace membership, syscall/filesystem boundary και LSM/seccomp policy. Έλεγξε effective privilege μέσα σε disposable VM/container και χρησιμοποίησε `/proc`, audit/logging και configuration diff ως evidence.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Linux Internals — Capabilities, Namespaces, Seccomp, LSM και eBPF**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Δούλεψε σε disposable VM ή local test binary. Προτίμησε harmless toy programs, sanitizers, debuggers και read-only inspection. Μην μετατρέπεις crash analysis σε weaponized exploitation.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Linux Internals — Capabilities, Namespaces, Seccomp, LSM και eBPF**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Linux Internals — Capabilities, Namespaces, Seccomp, LSM και eBPF** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 074](../../English/03-Systems-Malware-and-Reverse-Engineering/74-Linux-Internals-Capabilities-Namespaces-Seccomp-LSM-and-eBPF-Security.md)

---

# Εσωτερική Λειτουργία Isolation σε Containers και Kubernetes

> **Ελληνική έκδοση — Μάθημα 075.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Cloud-native ασφάλεια σημαίνει έλεγχο control planes, workload identity, artifacts, build systems, containers και data flows. Οι σημαντικότερες αστοχίες συχνά προκύπτουν από υπερβολικά δικαιώματα, implicit trust μεταξύ services, μη επαληθεύσιμα artifacts ή ανεπαρκή provenance.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Εσωτερική Λειτουργία Isolation σε Containers και Kubernetes**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Container boundary recap**
  Για το **Container boundary recap**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **Kubernetes control plane**
  Για το **Kubernetes control plane**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **Authentication and authorization**
  Για το **Authentication and authorization**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Service accounts**
  Για το **Service accounts**, στο πλαίσιο του **Εσωτερική Λειτουργία Isolation σε Containers και Kubernetes**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Admission control**
  Για το **Admission control**, στο πλαίσιο του **Εσωτερική Λειτουργία Isolation σε Containers και Kubernetes**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Pod security settings**
  Για το **Pod security settings**, στο πλαίσιο του **Εσωτερική Λειτουργία Isolation σε Containers και Kubernetes**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Secrets**
  Για το **Secrets**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **Network policy**
  Στο **Network policy**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.
- **Node trust**
  Για το **Node trust**, στο πλαίσιο του **Εσωτερική Λειτουργία Isolation σε Containers και Kubernetes**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Runtime socket risk**
  Στο **Runtime socket risk**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.
- **Image supply chain**
  Για το **Image supply chain**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **Kubernetes audit telemetry**
  Για το **Kubernetes audit telemetry**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **Safe cluster lab**
  Για το **Safe cluster lab**, στο πλαίσιο του **Εσωτερική Λειτουργία Isolation σε Containers και Kubernetes**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Attack-path reasoning**
  Για το **Attack-path reasoning**, στο πλαίσιο του **Εσωτερική Λειτουργία Isolation σε Containers και Kubernetes**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Εσωτερική Λειτουργία Isolation σε Containers και Kubernetes**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε local containers ή sandbox cloud accounts που σου ανήκουν. Έλεγξε policies και artifacts read-only πριν από αλλαγές και απέφυγε δημόσια exposure στα labs.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Εσωτερική Λειτουργία Isolation σε Containers και Kubernetes**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Εσωτερική Λειτουργία Isolation σε Containers και Kubernetes** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 075](../../English/07-Cloud-Containers-and-Supply-Chain/75-Container-and-Kubernetes-Isolation-Internals.md)

---

# Cloud IAM, Control Planes, Metadata και Temporary Credentials

> **Ελληνική έκδοση — Μάθημα 076.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Cloud-native ασφάλεια σημαίνει έλεγχο control planes, workload identity, artifacts, build systems, containers και data flows. Οι σημαντικότερες αστοχίες συχνά προκύπτουν από υπερβολικά δικαιώματα, implicit trust μεταξύ services, μη επαληθεύσιμα artifacts ή ανεπαρκή provenance.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Cloud IAM, Control Planes, Metadata και Temporary Credentials**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Cloud security is API security at infrastructure scale**
  Για το **Cloud security is API security at infrastructure scale**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **Identity types**
  Για το **Identity types**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Temporary credentials**
  Για το **Temporary credentials**, στο πλαίσιο του **Cloud IAM, Control Planes, Metadata και Temporary Credentials**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Effective permission**
  Για το **Effective permission**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Role assumption**
  Για το **Role assumption**, στο πλαίσιο του **Cloud IAM, Control Planes, Metadata και Temporary Credentials**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Workload identity**
  Για το **Workload identity**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Metadata services**
  Για το **Metadata services**, χαρτογράφησε Windows security principal, token/privileges, object ACL ή service/IPC boundary και το audit/ETW evidence που δείχνει την απόφαση πρόσβασης. Δούλεψε σε disposable Windows VM και έλεγξε effective authority, όχι μόνο configuration text.
- **Control plane versus data plane**
  Για το **Control plane versus data plane**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **Organization-level guardrails**
  Για το **Organization-level guardrails**, στο πλαίσιο του **Cloud IAM, Control Planes, Metadata και Temporary Credentials**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Secrets and key services**
  Για το **Secrets and key services**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **Public exposure**
  Για το **Public exposure**, στο πλαίσιο του **Cloud IAM, Control Planes, Metadata και Temporary Credentials**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Cloud logging**
  Για το **Cloud logging**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **Safe sandbox lab**
  Για το **Safe sandbox lab**, στο πλαίσιο του **Cloud IAM, Control Planes, Metadata και Temporary Credentials**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Privilege graph questions**
  Για το **Privilege graph questions**, στο πλαίσιο του **Cloud IAM, Control Planes, Metadata και Temporary Credentials**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Cloud IAM, Control Planes, Metadata και Temporary Credentials**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε local containers ή sandbox cloud accounts που σου ανήκουν. Έλεγξε policies και artifacts read-only πριν από αλλαγές και απέφυγε δημόσια exposure στα labs.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Cloud IAM, Control Planes, Metadata και Temporary Credentials**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Cloud IAM, Control Planes, Metadata και Temporary Credentials** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 076](../../English/07-Cloud-Containers-and-Supply-Chain/76-Cloud-IAM-Control-Planes-Metadata-and-Temporary-Credentials.md)

---

# Reverse Engineering Δικτυακών Πρωτοκόλλων και Traffic Analysis

> **Ελληνική έκδοση — Μάθημα 077.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Τα δίκτυα είναι κατανεμημένα state machines. Routing, neighbor discovery, DNS, TCP/UDP, wireless authentication και middleboxes δημιουργούν διαφορετικά trust boundaries. Για σωστή ανάλυση χρειάζεται να ξεχωρίζεις control plane από data plane, local-link μηχανισμούς από routed traffic και observation από active interference.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Reverse Engineering Δικτυακών Πρωτοκόλλων και Traffic Analysis**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Start below the application**
  Για το **Start below the application**, σύνδεσε Android package/runtime behavior με UID sandbox, exported components, Binder/Intent boundaries, signing identity και Keystore-backed secrets. Επιβεβαίωσε το behavior σε δικό σου APK ή emulator και όχι σε τρίτες εφαρμογές.
- **Direction and roles**
  Για το **Direction and roles**, στο πλαίσιο του **Reverse Engineering Δικτυακών Πρωτοκόλλων και Traffic Analysis**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Capture discipline**
  Για το **Capture discipline**, στο πλαίσιο του **Reverse Engineering Δικτυακών Πρωτοκόλλων και Traffic Analysis**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Hex and ASCII views**
  Για το **Hex and ASCII views**, στο πλαίσιο του **Reverse Engineering Δικτυακών Πρωτοκόλλων και Traffic Analysis**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Fixed header hypothesis**
  Για το **Fixed header hypothesis**, στο πλαίσιο του **Reverse Engineering Δικτυακών Πρωτοκόλλων και Traffic Analysis**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Endianness**
  Στο **Endianness**, σύνδεσε ABI/OS abstraction με το πραγματικό machine/runtime state: registers, addresses, object handles, loader metadata και privilege transition. Χρησιμοποίησε μικρό δικό σου binary, disassembler/debugger και annotated trace ώστε κάθε inference να έχει observable βάση.
- **Length-prefixed framing**
  Για το **Length-prefixed framing**, στο πλαίσιο του **Reverse Engineering Δικτυακών Πρωτοκόλλων και Traffic Analysis**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Type-length-value structures**
  Για το **Type-length-value structures**, στο πλαίσιο του **Reverse Engineering Δικτυακών Πρωτοκόλλων και Traffic Analysis**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Checksums and integrity**
  Για το **Checksums and integrity**, στο πλαίσιο του **Reverse Engineering Δικτυακών Πρωτοκόλλων και Traffic Analysis**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Compression versus encryption**
  Για το **Compression versus encryption**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **Stateful protocols**
  Για το **Stateful protocols**, στο πλαίσιο του **Reverse Engineering Δικτυακών Πρωτοκόλλων και Traffic Analysis**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Error messages as an oracle**
  Για το **Error messages as an oracle**, στο πλαίσιο του **Reverse Engineering Δικτυακών Πρωτοκόλλων και Traffic Analysis**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Wireshark/tshark methodology**
  Για το **Wireshark/tshark methodology**, στο πλαίσιο του **Reverse Engineering Δικτυακών Πρωτοκόλλων και Traffic Analysis**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Python parser project**
  Για το **Python parser project**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **Safe lab**
  Στο **Safe lab**, μετέτρεψε τη θεωρία του **Reverse Engineering Δικτυακών Πρωτοκόλλων και Traffic Analysis** σε ελέγξιμα κριτήρια: τι πρέπει να μπορείς να εξηγήσεις, ποιο λάθος assumption εμφανίζεται συχνότερα, ποιο safe lab το αποκαλύπτει και ποιο retest αποδεικνύει ότι το διόρθωσες.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Reverse Engineering Δικτυακών Πρωτοκόλλων και Traffic Analysis**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε δικό σου LAN/lab και passive captures όπου γίνεται. Για active tests χρησιμοποίησε isolated namespaces/VMs και κράτησε packet capture πριν και μετά ώστε να αποδεικνύεται η συμπεριφορά.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Reverse Engineering Δικτυακών Πρωτοκόλλων και Traffic Analysis**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Reverse Engineering Δικτυακών Πρωτοκόλλων και Traffic Analysis** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 077](../../English/04-Network-Wireless-and-Internet/77-Network-Protocol-Reverse-Engineering-and-Traffic-Analysis.md)

---

# TLS, PKI και Αποτυχίες Υλοποίησης Κρυπτογραφίας

> **Ελληνική έκδοση — Μάθημα 078.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Identity και cryptography είναι μηχανισμοί μεταφοράς εμπιστοσύνης. Authentication απαντά ποιος παρουσιάζει ένα credential, authorization τι επιτρέπεται να κάνει, ενώ cryptography προστατεύει συγκεκριμένες ιδιότητες δεδομένων και πρωτοκόλλων. Κλειδιά, tokens, certificates, federation metadata και policy engines είναι όλα authority-bearing artifacts και χρειάζονται σαφή lifecycle.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **TLS, PKI και Αποτυχίες Υλοποίησης Κρυπτογραφίας**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Cryptography is a system, not an algorithm**
  Για το **Cryptography is a system, not an algorithm**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **TLS goals**
  Στο **TLS goals**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.
- **Certificate chain**
  Για το **Certificate chain**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **Hostname validation**
  Για το **Hostname validation**, στο πλαίσιο του **TLS, PKI και Αποτυχίες Υλοποίησης Κρυπτογραφίας**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Private PKI**
  Για το **Private PKI**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **Forward secrecy**
  Για το **Forward secrecy**, στο πλαίσιο του **TLS, PKI και Αποτυχίες Υλοποίησης Κρυπτογραφίας**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Nonces and AEAD**
  Για το **Nonces and AEAD**, στο πλαίσιο του **TLS, PKI και Αποτυχίες Υλοποίησης Κρυπτογραφίας**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Randomness**
  Για το **Randomness**, στο πλαίσιο του **TLS, PKI και Αποτυχίες Υλοποίησης Κρυπτογραφίας**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Password storage**
  Για το **Password storage**, κατέγραψε ποιος μπορεί να γράψει/διαβάσει το state, πού αποθηκεύεται, πώς προστατεύεται at rest, ποιο backup/sync behavior υπάρχει και πότε το data πρέπει να διαγράφεται ή να ανακαλείται.
- **Key derivation**
  Για το **Key derivation**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **Downgrade resistance**
  Για το **Downgrade resistance**, στο πλαίσιο του **TLS, PKI και Αποτυχίες Υλοποίησης Κρυπτογραφίας**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Certificate revocation reality**
  Για το **Certificate revocation reality**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **Side channels**
  Για το **Side channels**, στο πλαίσιο του **TLS, PKI και Αποτυχίες Υλοποίησης Κρυπτογραφίας**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Padding and error oracles**
  Για το **Padding and error oracles**, στο πλαίσιο του **TLS, PKI και Αποτυχίες Υλοποίησης Κρυπτογραφίας**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Key lifecycle**
  Για το **Key lifecycle**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **Safe localhost TLS lab**
  Στο **Safe localhost TLS lab**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **TLS, PKI και Αποτυχίες Υλοποίησης Κρυπτογραφίας**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε synthetic identities, test certificates και local identity providers. Χαρτογράφησε issuer, subject, audience, permissions, lifetime, rotation και revocation χωρίς να αποθηκεύεις πραγματικά secrets.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **TLS, PKI και Αποτυχίες Υλοποίησης Κρυπτογραφίας**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **TLS, PKI και Αποτυχίες Υλοποίησης Κρυπτογραφίας** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 078](../../English/06-Identity-Cryptography-and-Trust/78-TLS-PKI-and-Cryptographic-Implementation-Failures.md)

---

# Malware Analysis και Behavioral Triage

> **Ελληνική έκδοση — Μάθημα 079.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Η ασφάλεια συστημάτων βασίζεται στα πραγματικά boundaries του λειτουργικού: processes, memory mappings, privilege levels, handles/file descriptors, executable loading, syscalls, services και telemetry. Σε reverse engineering και vulnerability research το σημαντικό είναι να συνδέεις συμπεριφορά υψηλού επιπέδου με χαμηλού επιπέδου state χωρίς να συμπεραίνεις περισσότερα από όσα δείχνουν τα δεδομένα.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Malware Analysis και Behavioral Triage**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Safety first**
  Για το **Safety first**, στο πλαίσιο του **Malware Analysis και Behavioral Triage**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Ανάλυση phases**
  Για το **Ανάλυση phases**, στο πλαίσιο του **Malware Analysis και Behavioral Triage**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Static triage**
  Για το **Static triage**, όρισε decision owner, trigger, required telemetry, χρονική σειρά ενεργειών και πιθανό operational impact. Η σωστή απόφαση πρέπει να είναι αναστρέψιμη όπου γίνεται, να διατηρεί evidence και να συνδέεται με σαφές recovery/retest criterion.
- **Packing and obfuscation**
  Για το **Packing and obfuscation**, σύνδεσε Android package/runtime behavior με UID sandbox, exported components, Binder/Intent boundaries, signing identity και Keystore-backed secrets. Επιβεβαίωσε το behavior σε δικό σου APK ή emulator και όχι σε τρίτες εφαρμογές.
- **Dynamic behavior**
  Για το **Dynamic behavior**, στο πλαίσιο του **Malware Analysis και Behavioral Triage**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Process tree**
  Στο **Process tree**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **Persistence concepts**
  Για το **Persistence concepts**, στο πλαίσιο του **Malware Analysis και Behavioral Triage**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Network behavior**
  Στο **Network behavior**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.
- **Configuration extraction**
  Για το **Configuration extraction**, στο πλαίσιο του **Malware Analysis και Behavioral Triage**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Behavioral signatures**
  Για το **Behavioral signatures**, στο πλαίσιο του **Malware Analysis και Behavioral Triage**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **YARA concepts**
  Για το **YARA concepts**, στο πλαίσιο του **Malware Analysis και Behavioral Triage**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Sandbox limitations**
  Για το **Sandbox limitations**, στο πλαίσιο του **Malware Analysis και Behavioral Triage**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Benign simulation lab**
  Για το **Benign simulation lab**, στο πλαίσιο του **Malware Analysis και Behavioral Triage**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Report structure**
  Για το **Report structure**, στο πλαίσιο του **Malware Analysis και Behavioral Triage**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Malware Analysis και Behavioral Triage**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Δούλεψε σε disposable VM ή local test binary. Προτίμησε harmless toy programs, sanitizers, debuggers και read-only inspection. Μην μετατρέπεις crash analysis σε weaponized exploitation.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Malware Analysis και Behavioral Triage**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Malware Analysis και Behavioral Triage** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 079](../../English/03-Systems-Malware-and-Reverse-Engineering/79-Malware-Analysis-and-Behavioral-Triage.md)

---

# Προχωρημένο Detection Engineering και MITRE ATT&CK v19

> **Ελληνική έκδοση — Μάθημα 080.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Blue-team εργασία σημαίνει να μετατρέπεις telemetry σε τεκμηριωμένα συμπεράσματα. Ένα alert δεν είναι απόδειξη από μόνο του. Χρειάζεται timeline, identity context, process/network relationships, data provenance και κατανόηση του τι δεν καταγράφεται. Η ανθεκτικότητα επεκτείνεται από detection μέχρι containment, recovery και verification.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Προχωρημένο Detection Engineering και MITRE ATT&CK v19**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

**Τρέχουσα έκδοση:** MITRE ATT&CK v19.2 (6 Αυγούστου 2026). Το major v19 εισήγαγε τον διαχωρισμό του Enterprise Defense Evasion σε **Stealth** και **Defense Impairment**· το v19.2 είναι Agile update με κυρίως Groups/Software ενημερώσεις.

- **ATT&CK in 2026**
  Για το **ATT&CK in 2026**, ξεκίνα από observable behavior και διαθέσιμα data sources, όχι από technique ID μόνο. Γράψε detection hypothesis, required fields, expected benign collisions, tuning strategy και validation event ώστε η κάλυψη να είναι μετρήσιμη.
- **Start with behavior**
  Για το **Start with behavior**, σύνδεσε Android package/runtime behavior με UID sandbox, exported components, Binder/Intent boundaries, signing identity και Keystore-backed secrets. Επιβεβαίωσε το behavior σε δικό σου APK ή emulator και όχι σε τρίτες εφαρμογές.
- **Detection pipeline**
  Στο **Detection pipeline**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Atomic versus correlated analytics**
  Για το **Atomic versus correlated analytics**, ξεκίνα από observable behavior και διαθέσιμα data sources, όχι από technique ID μόνο. Γράψε detection hypothesis, required fields, expected benign collisions, tuning strategy και validation event ώστε η κάλυψη να είναι μετρήσιμη.
- **Sequence detections**
  Για το **Sequence detections**, ξεκίνα από observable behavior και διαθέσιμα data sources, όχι από technique ID μόνο. Γράψε detection hypothesis, required fields, expected benign collisions, tuning strategy και validation event ώστε η κάλυψη να είναι μετρήσιμη.
- **Rarity and baseline**
  Για το **Rarity and baseline**, ξεκίνα από observable behavior και διαθέσιμα data sources, όχι από technique ID μόνο. Γράψε detection hypothesis, required fields, expected benign collisions, tuning strategy και validation event ώστε η κάλυψη να είναι μετρήσιμη.
- **Entity context**
  Για το **Entity context**, ξεκίνα από observable behavior και διαθέσιμα data sources, όχι από technique ID μόνο. Γράψε detection hypothesis, required fields, expected benign collisions, tuning strategy και validation event ώστε η κάλυψη να είναι μετρήσιμη.
- **Detection of defense impairment**
  Στο **Detection of defense impairment**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Stealth-related behavior**
  Για το **Stealth-related behavior**, ξεκίνα από observable behavior και διαθέσιμα data sources, όχι από technique ID μόνο. Γράψε detection hypothesis, required fields, expected benign collisions, tuning strategy και validation event ώστε η κάλυψη να είναι μετρήσιμη.
- **Data quality**
  Για το **Data quality**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Sigma and portable logic**
  Για το **Sigma and portable logic**, ξεκίνα από observable behavior και διαθέσιμα data sources, όχι από technique ID μόνο. Γράψε detection hypothesis, required fields, expected benign collisions, tuning strategy και validation event ώστε η κάλυψη να είναι μετρήσιμη.
- **Network detections**
  Στο **Network detections**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.
- **Identity detections**
  Για το **Identity detections**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Detection testing**
  Στο **Detection testing**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **False positives and tuning**
  Για το **False positives and tuning**, ξεκίνα από observable behavior και διαθέσιμα data sources, όχι από technique ID μόνο. Γράψε detection hypothesis, required fields, expected benign collisions, tuning strategy και validation event ώστε η κάλυψη να είναι μετρήσιμη.
- **Detection-as-code**
  Στο **Detection-as-code**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Coverage metrics**
  Για το **Coverage metrics**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Προχωρημένο Detection Engineering και MITRE ATT&CK v19**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε synthetic logs και harmless local events. Κατέγραψε expected evidence πριν το test και σύγκρινε με ό,τι πραγματικά συλλέχθηκε.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Προχωρημένο Detection Engineering και MITRE ATT&CK v19**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Προχωρημένο Detection Engineering και MITRE ATT&CK v19** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 080](../../English/08-Blue-Team-IR-Forensics-and-Resilience/80-Advanced-Detection-Engineering-and-ATTACK-v19.md)

---

# Digital Forensics — Filesystem Timelines και Memory Artifacts

> **Ελληνική έκδοση — Μάθημα 081.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Blue-team εργασία σημαίνει να μετατρέπεις telemetry σε τεκμηριωμένα συμπεράσματα. Ένα alert δεν είναι απόδειξη από μόνο του. Χρειάζεται timeline, identity context, process/network relationships, data provenance και κατανόηση του τι δεν καταγράφεται. Η ανθεκτικότητα επεκτείνεται από detection μέχρι containment, recovery και verification.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Digital Forensics — Filesystem Timelines και Memory Artifacts**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Forensics is reconstruction under uncertainty**
  Στο **Forensics is reconstruction under uncertainty**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Evidence preservation**
  Στο **Evidence preservation**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Filesystem metadata**
  Για το **Filesystem metadata**, κατέγραψε ποιος μπορεί να γράψει/διαβάσει το state, πού αποθηκεύεται, πώς προστατεύεται at rest, ποιο backup/sync behavior υπάρχει και πότε το data πρέπει να διαγράφεται ή να ανακαλείται.
- **Timestamp caveats**
  Στο **Timestamp caveats**, διατήρησε provenance και χρονικό context για κάθε artifact. Ξεχώρισε fact, inference και hypothesis, έλεγξε clock/timezone effects και μη θεωρείς το πρώτο observable event ούτε root cause ούτε αρχικό σημείο compromise χωρίς corroboration.
- **Timeline normalization**
  Στο **Timeline normalization**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Super-timelines**
  Στο **Super-timelines**, διατήρησε provenance και χρονικό context για κάθε artifact. Ξεχώρισε fact, inference και hypothesis, έλεγξε clock/timezone effects και μη θεωρείς το πρώτο observable event ούτε root cause ούτε αρχικό σημείο compromise χωρίς corroboration.
- **Process execution artifacts**
  Στο **Process execution artifacts**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **Persistence review**
  Στο **Persistence review**, διατήρησε provenance και χρονικό context για κάθε artifact. Ξεχώρισε fact, inference και hypothesis, έλεγξε clock/timezone effects και μη θεωρείς το πρώτο observable event ούτε root cause ούτε αρχικό σημείο compromise χωρίς corroboration.
- **Memory forensics concepts**
  Στο **Memory forensics concepts**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **Process-versus-module anomalies**
  Στο **Process-versus-module anomalies**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **Network artifacts**
  Στο **Network artifacts**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.
- **Browser and user artifacts**
  Για το **Browser and user artifacts**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **Cloud and SaaS forensics**
  Για το **Cloud and SaaS forensics**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **Hypothesis-driven investigation**
  Στο **Hypothesis-driven investigation**, διατήρησε provenance και χρονικό context για κάθε artifact. Ξεχώρισε fact, inference και hypothesis, έλεγξε clock/timezone effects και μη θεωρείς το πρώτο observable event ούτε root cause ούτε αρχικό σημείο compromise χωρίς corroboration.
- **Root cause versus patient zero**
  Στο **Root cause versus patient zero**, διατήρησε provenance και χρονικό context για κάθε artifact. Ξεχώρισε fact, inference και hypothesis, έλεγξε clock/timezone effects και μη θεωρείς το πρώτο observable event ούτε root cause ούτε αρχικό σημείο compromise χωρίς corroboration.
- **Safe timeline lab**
  Στο **Safe timeline lab**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Forensic report structure**
  Στο **Forensic report structure**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Digital Forensics — Filesystem Timelines και Memory Artifacts**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε synthetic logs και harmless local events. Κατέγραψε expected evidence πριν το test και σύγκρινε με ό,τι πραγματικά συλλέχθηκε.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Digital Forensics — Filesystem Timelines και Memory Artifacts**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Digital Forensics — Filesystem Timelines και Memory Artifacts** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 081](../../English/08-Blue-Team-IR-Forensics-and-Resilience/81-Digital-Forensics-Filesystem-Timelines-and-Memory-Artifacts.md)

---

# Reverse Engineering Android Εφαρμογών και Mobile App Internals

> **Ελληνική έκδοση — Μάθημα 082.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Mobile, IoT και embedded συστήματα συνδυάζουν εφαρμογές, λειτουργικό, firmware, radios, hardware roots of trust και φυσική πρόσβαση. Το security model εξαρτάται από secure boot, app sandboxing, permissions, key storage, update trust και τις πραγματικές διεπαφές που εκτίθενται.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Reverse Engineering Android Εφαρμογών και Mobile App Internals**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Package anatomy**
  Για το **Package anatomy**, σύνδεσε Android package/runtime behavior με UID sandbox, exported components, Binder/Intent boundaries, signing identity και Keystore-backed secrets. Επιβεβαίωσε το behavior σε δικό σου APK ή emulator και όχι σε τρίτες εφαρμογές.
- **DEX and ART**
  Για το **DEX and ART**, σύνδεσε Android package/runtime behavior με UID sandbox, exported components, Binder/Intent boundaries, signing identity και Keystore-backed secrets. Επιβεβαίωσε το behavior σε δικό σου APK ή emulator και όχι σε τρίτες εφαρμογές.
- **Manifest as attack-surface map**
  Για το **Manifest as attack-surface map**, σύνδεσε Android package/runtime behavior με UID sandbox, exported components, Binder/Intent boundaries, signing identity και Keystore-backed secrets. Επιβεβαίωσε το behavior σε δικό σου APK ή emulator και όχι σε τρίτες εφαρμογές.
- **Intent trust boundaries**
  Για το **Intent trust boundaries**, σύνδεσε Android package/runtime behavior με UID sandbox, exported components, Binder/Intent boundaries, signing identity και Keystore-backed secrets. Επιβεβαίωσε το behavior σε δικό σου APK ή emulator και όχι σε τρίτες εφαρμογές.
- **Binder and IPC**
  Για το **Binder and IPC**, σύνδεσε Android package/runtime behavior με UID sandbox, exported components, Binder/Intent boundaries, signing identity και Keystore-backed secrets. Επιβεβαίωσε το behavior σε δικό σου APK ή emulator και όχι σε τρίτες εφαρμογές.
- **Application sandbox**
  Για το **Application sandbox**, σύνδεσε Android package/runtime behavior με UID sandbox, exported components, Binder/Intent boundaries, signing identity και Keystore-backed secrets. Επιβεβαίωσε το behavior σε δικό σου APK ή emulator και όχι σε τρίτες εφαρμογές.
- **Signing and update identity**
  Για το **Signing and update identity**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Network Ασφάλεια Configuration**
  Στο **Network Ασφάλεια Configuration**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.
- **Keystore**
  Για το **Keystore**, σύνδεσε Android package/runtime behavior με UID sandbox, exported components, Binder/Intent boundaries, signing identity και Keystore-backed secrets. Επιβεβαίωσε το behavior σε δικό σου APK ή emulator και όχι σε τρίτες εφαρμογές.
- **WebView**
  Για το **WebView**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **Deep links and app links**
  Για το **Deep links and app links**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **Content providers**
  Για το **Content providers**, σύνδεσε Android package/runtime behavior με UID sandbox, exported components, Binder/Intent boundaries, signing identity και Keystore-backed secrets. Επιβεβαίωσε το behavior σε δικό σου APK ή emulator και όχι σε τρίτες εφαρμογές.
- **Native/JNI boundary**
  Για το **Native/JNI boundary**, σύνδεσε Android package/runtime behavior με UID sandbox, exported components, Binder/Intent boundaries, signing identity και Keystore-backed secrets. Επιβεβαίωσε το behavior σε δικό σου APK ή emulator και όχι σε τρίτες εφαρμογές.
- **Obfuscation**
  Για το **Obfuscation**, σύνδεσε Android package/runtime behavior με UID sandbox, exported components, Binder/Intent boundaries, signing identity και Keystore-backed secrets. Επιβεβαίωσε το behavior σε δικό σου APK ή emulator και όχι σε τρίτες εφαρμογές.
- **Dynamic analysis**
  Για το **Dynamic analysis**, σύνδεσε Android package/runtime behavior με UID sandbox, exported components, Binder/Intent boundaries, signing identity και Keystore-backed secrets. Επιβεβαίωσε το behavior σε δικό σου APK ή emulator και όχι σε τρίτες εφαρμογές.
- **Static analysis lab**
  Για το **Static analysis lab**, ακολούθησε data/control flow από source σε sink, σημείωσε validation και ownership assumptions και έλεγξε πού εφαρμόζεται enforcement. Χρησιμοποίησε tests και static/runtime evidence για να ξεχωρίσεις root cause από απλό code smell.
- **Termux role**
  Για το **Termux role**, δες το workflow σαν reproducible local environment: paths, package/source provenance, permissions, environment state, error handling και rollback. Στο Termux προτίμησε standard-library εργαλεία, explicit paths και δοκιμές σε harmless local files/services.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Reverse Engineering Android Εφαρμογών και Mobile App Internals**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε δική σου συσκευή, emulator ή development board. Προτίμησε static analysis, documented debug interfaces και benign sample apps/firmware. Απόφυγε tests σε τρίτες συσκευές ή ασύρματα περιβάλλοντα.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Reverse Engineering Android Εφαρμογών και Mobile App Internals**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Reverse Engineering Android Εφαρμογών και Mobile App Internals** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 082](../../English/05-Mobile-IoT-and-Hardware/82-Android-Application-Reverse-Engineering-and-Mobile-App-Internals.md)

---

# Firmware, Embedded Systems και Ανάλυση Hardware Interfaces

> **Ελληνική έκδοση — Μάθημα 083.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Mobile, IoT και embedded συστήματα συνδυάζουν εφαρμογές, λειτουργικό, firmware, radios, hardware roots of trust και φυσική πρόσβαση. Το security model εξαρτάται από secure boot, app sandboxing, permissions, key storage, update trust και τις πραγματικές διεπαφές που εκτίθενται.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Firmware, Embedded Systems και Ανάλυση Hardware Interfaces**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Embedded threat model**
  Στο **Embedded threat model**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.
- **Boot chain**
  Στο **Boot chain**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.
- **Firmware images**
  Στο **Firmware images**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.
- **Filesystems**
  Στο **Filesystems**, κατέγραψε electrical/logical interface, access prerequisite, privilege boundary και τι data ή control surface εκθέτει. Χρησιμοποίησε μόνο development board ή δικό σου hardware και προτίμησε read-only identification πριν από οποιαδήποτε αλλαγή.
- **UART**
  Στο **UART**, κατέγραψε electrical/logical interface, access prerequisite, privilege boundary και τι data ή control surface εκθέτει. Χρησιμοποίησε μόνο development board ή δικό σου hardware και προτίμησε read-only identification πριν από οποιαδήποτε αλλαγή.
- **JTAG and SWD**
  Στο **JTAG and SWD**, κατέγραψε electrical/logical interface, access prerequisite, privilege boundary και τι data ή control surface εκθέτει. Χρησιμοποίησε μόνο development board ή δικό σου hardware και προτίμησε read-only identification πριν από οποιαδήποτε αλλαγή.
- **SPI and flash**
  Στο **SPI and flash**, κατέγραψε electrical/logical interface, access prerequisite, privilege boundary και τι data ή control surface εκθέτει. Χρησιμοποίησε μόνο development board ή δικό σου hardware και προτίμησε read-only identification πριν από οποιαδήποτε αλλαγή.
- **I2C**
  Στο **I2C**, κατέγραψε electrical/logical interface, access prerequisite, privilege boundary και τι data ή control surface εκθέτει. Χρησιμοποίησε μόνο development board ή δικό σου hardware και προτίμησε read-only identification πριν από οποιαδήποτε αλλαγή.
- **Secrets at rest**
  Για το **Secrets at rest**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **Firmware update security**
  Στο **Firmware update security**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.
- **Rollback protection**
  Για το **Rollback protection**, ακολούθησε την αλυσίδα trust από immutable/early-boot state μέχρι OS/application. Έλεγξε measured/verified state, key custody, update authorization, anti-rollback και τι αλλάζει όταν ο attacker έχει φυσική πρόσβαση.
- **Hardware root of trust**
  Στο **Hardware root of trust**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.
- **Safe firmware lab**
  Στο **Safe firmware lab**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.
- **Firmware SBOM and provenance**
  Για το **Firmware SBOM and provenance**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Firmware, Embedded Systems και Ανάλυση Hardware Interfaces**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε δική σου συσκευή, emulator ή development board. Προτίμησε static analysis, documented debug interfaces και benign sample apps/firmware. Απόφυγε tests σε τρίτες συσκευές ή ασύρματα περιβάλλοντα.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Firmware, Embedded Systems και Ανάλυση Hardware Interfaces**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Firmware, Embedded Systems και Ανάλυση Hardware Interfaces** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 083](../../English/05-Mobile-IoT-and-Hardware/83-Firmware-Embedded-Systems-and-Hardware-Interface-Analysis.md)

---

# Patch Diffing, Root Cause Ευπαθειών και Secure Regression Analysis

> **Ελληνική έκδοση — Μάθημα 084.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Η ασφάλεια συστημάτων βασίζεται στα πραγματικά boundaries του λειτουργικού: processes, memory mappings, privilege levels, handles/file descriptors, executable loading, syscalls, services και telemetry. Σε reverse engineering και vulnerability research το σημαντικό είναι να συνδέεις συμπεριφορά υψηλού επιπέδου με χαμηλού επιπέδου state χωρίς να συμπεραίνεις περισσότερα από όσα δείχνουν τα δεδομένα.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Patch Diffing, Root Cause Ευπαθειών και Secure Regression Analysis**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Why patch analysis matters**
  Στο **Why patch analysis matters**, σύγκρινε pre-fix και post-fix behavior για να βρεις το violated invariant και όχι για να κατασκευάσεις exploit. Μετέτρεψε τη root cause σε negative/regression tests, έλεγξε variants και κατέγραψε αν το patch αφαιρεί την αιτία ή μόνο ένα symptom.
- **Start with source when available**
  Για το **Start with source when available**, σύνδεσε Android package/runtime behavior με UID sandbox, exported components, Binder/Intent boundaries, signing identity και Keystore-backed secrets. Επιβεβαίωσε το behavior σε δικό σου APK ή emulator και όχι σε τρίτες εφαρμογές.
- **Ασφάλεια invariant extraction**
  Στο **Ασφάλεια invariant extraction**, σύγκρινε pre-fix και post-fix behavior για να βρεις το violated invariant και όχι για να κατασκευάσεις exploit. Μετέτρεψε τη root cause σε negative/regression tests, έλεγξε variants και κατέγραψε αν το patch αφαιρεί την αιτία ή μόνο ένα symptom.
- **Variant analysis**
  Στο **Variant analysis**, σύγκρινε pre-fix και post-fix behavior για να βρεις το violated invariant και όχι για να κατασκευάσεις exploit. Μετέτρεψε τη root cause σε negative/regression tests, έλεγξε variants και κατέγραψε αν το patch αφαιρεί την αιτία ή μόνο ένα symptom.
- **Binary diffing**
  Στο **Binary diffing**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **Patch timing and exposure**
  Στο **Patch timing and exposure**, σύγκρινε pre-fix και post-fix behavior για να βρεις το violated invariant και όχι για να κατασκευάσεις exploit. Μετέτρεψε τη root cause σε negative/regression tests, έλεγξε variants και κατέγραψε αν το patch αφαιρεί την αιτία ή μόνο ένα symptom.
- **Regression test design**
  Στο **Regression test design**, σύγκρινε pre-fix και post-fix behavior για να βρεις το violated invariant και όχι για να κατασκευάσεις exploit. Μετέτρεψε τη root cause σε negative/regression tests, έλεγξε variants και κατέγραψε αν το patch αφαιρεί την αιτία ή μόνο ένα symptom.
- **Negative tests**
  Στο **Negative tests**, σύγκρινε pre-fix και post-fix behavior για να βρεις το violated invariant και όχι για να κατασκευάσεις exploit. Μετέτρεψε τη root cause σε negative/regression tests, έλεγξε variants και κατέγραψε αν το patch αφαιρεί την αιτία ή μόνο ένα symptom.
- **Hardening after root cause**
  Στο **Hardening after root cause**, σύγκρινε pre-fix και post-fix behavior για να βρεις το violated invariant και όχι για να κατασκευάσεις exploit. Μετέτρεψε τη root cause σε negative/regression tests, έλεγξε variants και κατέγραψε αν το patch αφαιρεί την αιτία ή μόνο ένα symptom.
- **Ασφάλεια advisories**
  Για το **Ασφάλεια advisories**, στο πλαίσιο του **Patch Diffing, Root Cause Ευπαθειών και Secure Regression Analysis**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Public patch ethics**
  Στο **Public patch ethics**, σύγκρινε pre-fix και post-fix behavior για να βρεις το violated invariant και όχι για να κατασκευάσεις exploit. Μετέτρεψε τη root cause σε negative/regression tests, έλεγξε variants και κατέγραψε αν το patch αφαιρεί την αιτία ή μόνο ένα symptom.
- **Safe source-diff lab**
  Στο **Safe source-diff lab**, σύγκρινε pre-fix και post-fix behavior για να βρεις το violated invariant και όχι για να κατασκευάσεις exploit. Μετέτρεψε τη root cause σε negative/regression tests, έλεγξε variants και κατέγραψε αν το patch αφαιρεί την αιτία ή μόνο ένα symptom.
- **Προχωρημένο case-study method**
  Στο **Προχωρημένο case-study method**, σύγκρινε pre-fix και post-fix behavior για να βρεις το violated invariant και όχι για να κατασκευάσεις exploit. Μετέτρεψε τη root cause σε negative/regression tests, έλεγξε variants και κατέγραψε αν το patch αφαιρεί την αιτία ή μόνο ένα symptom.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Patch Diffing, Root Cause Ευπαθειών και Secure Regression Analysis**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Δούλεψε σε disposable VM ή local test binary. Προτίμησε harmless toy programs, sanitizers, debuggers και read-only inspection. Μην μετατρέπεις crash analysis σε weaponized exploitation.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Patch Diffing, Root Cause Ευπαθειών και Secure Regression Analysis**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Patch Diffing, Root Cause Ευπαθειών και Secure Regression Analysis** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 084](../../English/03-Systems-Malware-and-Reverse-Engineering/84-Patch-Diffing-Vulnerability-Root-Cause-and-Secure-Regression-Analysis.md)

---

# Προχωρημένα Εξουσιοδοτημένα Capstones

> **Ελληνική έκδοση — Μάθημα 085.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Τα capstones μετατρέπουν γνώση σε αποδείξιμη ικανότητα. Ένα καλό project έχει scope, threat model, repeatable procedure, evidence, limitations, remediation και καθαρή τεχνική γραφή. Η ποιότητα μετριέται από το αν τρίτος μπορεί να αναπαράγει το συμπέρασμα χωρίς να μαντεύει.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Προχωρημένα Εξουσιοδοτημένα Capstones**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Capstone rules**
  Στο **Capstone rules**, όρισε συγκεκριμένο objective, owned/local scope, expected result και stop condition. Κράτησε μόνο sanitized evidence, σύγκρινε expected με observed behavior και ολοκλήρωσε με remediation και ίδιο regression test.
- **Deliverables for every capstone**
  Στο **Deliverables for every capstone**, όρισε συγκεκριμένο objective, owned/local scope, expected result και stop condition. Κράτησε μόνο sanitized evidence, σύγκρινε expected με observed behavior και ολοκλήρωσε με remediation και ίδιο regression test.
- **Capstone 1 — Binary assurance pipeline**
  Στο **Capstone 1 — Binary assurance pipeline**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **Capstone 2 — Local web trust-boundary review**
  Για το **Capstone 2 — Local web trust-boundary review**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **Capstone 3 — Enterprise identity graph**
  Για το **Capstone 3 — Enterprise identity graph**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Capstone 4 — Linux isolation report**
  Στο **Capstone 4 — Linux isolation report**, όρισε συγκεκριμένο objective, owned/local scope, expected result και stop condition. Κράτησε μόνο sanitized evidence, σύγκρινε expected με observed behavior και ολοκλήρωσε με remediation και ίδιο regression test.
- **Capstone 5 — Kubernetes privilege graph**
  Για το **Capstone 5 — Kubernetes privilege graph**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **Capstone 6 — Cloud IAM sandbox**
  Για το **Capstone 6 — Cloud IAM sandbox**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **Capstone 7 — Protocol reverse engineering**
  Στο **Capstone 7 — Protocol reverse engineering**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.
- **Capstone 8 — Malware-analysis simulation**
  Στο **Capstone 8 — Malware-analysis simulation**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **Capstone 9 — Android application security review**
  Στο **Capstone 9 — Android application security review**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.
- **Capstone 10 — Firmware trust chain**
  Στο **Capstone 10 — Firmware trust chain**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.
- **Capstone 11 — Detection engineering lifecycle**
  Στο **Capstone 11 — Detection engineering lifecycle**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Capstone 12 — Patch-to-prevention study**
  Στο **Capstone 12 — Patch-to-prevention study**, όρισε συγκεκριμένο objective, owned/local scope, expected result και stop condition. Κράτησε μόνο sanitized evidence, σύγκρινε expected με observed behavior και ολοκλήρωσε με remediation και ίδιο regression test.
- **Capstone 13 — Termux security research workstation**
  Στο **Capstone 13 — Termux security research workstation**, όρισε συγκεκριμένο objective, owned/local scope, expected result και stop condition. Κράτησε μόνο sanitized evidence, σύγκρινε expected με observed behavior και ολοκλήρωσε με remediation και ίδιο regression test.
- **Capstone 14 — Incident reconstruction tabletop**
  Στο **Capstone 14 — Incident reconstruction tabletop**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Capstone 15 — Ασφάλεια architecture review**
  Στο **Capstone 15 — Ασφάλεια architecture review**, όρισε συγκεκριμένο objective, owned/local scope, expected result και stop condition. Κράτησε μόνο sanitized evidence, σύγκρινε expected με observed behavior και ολοκλήρωσε με remediation και ίδιο regression test.
- **Scoring rubric**
  Για το **Scoring rubric**, όρισε συγκεκριμένο observable αποτέλεσμα: artifact, report, test, diagram ή explanation που μπορεί να αξιολογηθεί. Προτίμησε μικρά ολοκληρωμένα έργα με scope, evidence, remediation και reflection αντί για λίστες εργαλείων ή claims χωρίς απόδειξη.
- **Προχωρημένο mastery checklist**
  Στο **Προχωρημένο mastery checklist**, μετέτρεψε τη θεωρία του **Προχωρημένα Εξουσιοδοτημένα Capstones** σε ελέγξιμα κριτήρια: τι πρέπει να μπορείς να εξηγήσεις, ποιο λάθος assumption εμφανίζεται συχνότερα, ποιο safe lab το αποκαλύπτει και ποιο retest αποδεικνύει ότι το διόρθωσες.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Προχωρημένα Εξουσιοδοτημένα Capstones**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χτίσε portfolio μόνο με δικά σου ή ρητά εξουσιοδοτημένα labs. Αφαίρεσε secrets και προσωπικά δεδομένα πριν δημοσιεύσεις artifacts.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Προχωρημένα Εξουσιοδοτημένα Capstones**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Προχωρημένα Εξουσιοδοτημένα Capstones** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 085](../../English/11-Labs-Capstones-and-Career/85-Advanced-Authorized-Capstones.md)

---

# Ασφάλεια IPv6, Neighbor Discovery και Σύγχρονα LAN Attack Surfaces

> **Ελληνική έκδοση — Μάθημα 086.** Διατηρούνται οι διεθνείς τεχνικοί όροι όπου είναι ακριβέστεροι και ευκολότεροι στην αναζήτηση.

## Στόχος του μαθήματος

Να κατανοήσεις σε βάθος το **Ασφάλεια IPv6, Neighbor Discovery και Σύγχρονα LAN Attack Surfaces**, να αναγνωρίζεις trust boundaries και failure states και να μπορείς να αποδείξεις ένα συμπέρασμα με ασφαλές, επαναλήψιμο evidence.

> **Όριο εξουσιοδότησης:** Πρακτική μόνο σε συστήματα, λογαριασμούς, κώδικα ή labs που σου ανήκουν ή έχεις ρητή άδεια να ελέγξεις. Προτίμησε localhost, synthetic data και disposable environments.

## Βαθιές τεχνικές έννοιες

### 1. Address architecture

Global, unique-local, link-local, multicast και privacy addresses έχουν διαφορετικό routing/visibility. Κατέγραψε ποια address classes επιτρέπονται ανά interface και ποια δεν πρέπει να περνούν συγκεκριμένο boundary.

### 2. Neighbor Discovery

Το IPv6 Neighbor Discovery χρησιμοποιεί ICMPv6 για neighbors, routers και redirects. Blind filtering μπορεί να σπάσει το δίκτυο, ενώ blind trust σε first-hop control messages αυξάνει local-link risk.

### 3. SLAAC and DHCPv6

SLAAC και DHCPv6 μπορούν να συνυπάρχουν και να δίνουν διαφορετικό address/DNS state. Inventory και NAC δεν πρέπει να θεωρούν ότι ένα DHCP lease ισούται με μία endpoint identity.

### 4. Extension headers

Extension-header chains απαιτούν consistent parsing και bounded work από hosts και security devices. Διαφορετική υποστήριξη ή ordering μπορεί να δημιουργήσει policy gaps ή reliability issues.

### 5. Fragmentation and PMTUD

Στο IPv6 ordinary fragmentation γίνεται από endpoints και το PMTUD εξαρτάται από ICMPv6 Packet Too Big. Υπερβολικό ICMPv6 blocking μπορεί να μοιάζει με application outage.

### 6. Dual-stack exposure

Service που είναι κλειστό σε IPv4 μπορεί να παραμένει reachable σε IPv6. Έλεγξε sockets, ACLs, proxies, VPN, DNS και monitoring για πραγματική parity.

### 7. Local-link trust

Devices στο ίδιο VLAN δεν πρέπει να θεωρούνται αυτόματα trusted. First-hop policy, endpoint firewall, segmentation και switch controls καθορίζουν ποιος μπορεί να επηρεάσει local network state.

### 8. Telemetry

Χρήσιμα evidence είναι address lifetimes, RA sources, neighbor-cache changes, AAAA answers, routes, firewall decisions και bind addresses. Normalize IPv6 textual forms πριν από correlation.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Γράψε πρώτα invariant και expected result, άλλαξε μία μεταβλητή κάθε φορά και κράτησε μόνο το evidence που χρειάζεται.

1. **Build a two-host or two-namespace IPv6-only localhost lab and document addresses, routes, neighbor entries, and DNS behavior without sending traffic outside the lab** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
2. **Compare an application bound to 127** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
3. **Create a firewall-review worksheet that checks IPv4 and IPv6 policy parity for one lab service** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary και ποιος έχει authority;
2. Ποιο state μπορεί να γίνει stale, replayed ή inconsistent;
3. Ποιο evidence θα διέψευδε την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά το blast radius;
5. Πώς θα επαναλάβεις το test με ασφάλεια μετά τη remediation?

## Πλήρες αγγλικό μάθημα

[English Module 086](../../English/04-Network-Wireless-and-Internet/86-IPv6-Security-Neighbor-Discovery-and-Modern-LAN-Attack-Surfaces.md)

## Συνέχεια

Χρησιμοποίησε **Αναζήτηση μαθημάτων** ή **Διαδρομές μάθησης** από το κύριο menu για τα σχετικά επόμενα θέματα.

---

# Ασφάλεια DNS, Routing, BGP και Υποδομής Internet

> **Ελληνική έκδοση — Μάθημα 087.** Διατηρούνται οι διεθνείς τεχνικοί όροι όπου είναι ακριβέστεροι και ευκολότεροι στην αναζήτηση.

## Στόχος του μαθήματος

Να κατανοήσεις σε βάθος το **Ασφάλεια DNS, Routing, BGP και Υποδομής Internet**, να αναγνωρίζεις trust boundaries και failure states και να μπορείς να αποδείξεις ένα συμπέρασμα με ασφαλές, επαναλήψιμο evidence.

> **Όριο εξουσιοδότησης:** Πρακτική μόνο σε συστήματα, λογαριασμούς, κώδικα ή labs που σου ανήκουν ή έχεις ρητή άδεια να ελέγξεις. Προτίμησε localhost, synthetic data και disposable environments.

## Βαθιές τεχνικές έννοιες

### 1. DNS resolution chain

Ένα DNS answer μπορεί να περάσει stub resolver, recursive resolver, authoritative servers και caches. Χαρτογράφησε ποιο component είναι authoritative για κάθε βήμα και πού αλλάζει trust.

### 2. DNSSEC

DNSSEC δίνει authenticity/integrity σε DNS RRsets μέσω chain of trust. Δεν παρέχει confidentiality ούτε authorization για την εφαρμογή που βρίσκεται στη διεύθυνση.

### 3. Registrar and zone control

Registrar account, registry lock, DNS hosting και zone signing είναι control-plane assets υψηλής αξίας. MFA, role separation, change alerts και recovery διαδικασία είναι κρίσιμα.

### 4. Anycast and recursive services

Anycast βελτιώνει reachability/resilience αλλά ένα logical resolver μπορεί να έχει πολλά sites και failure domains. Monitoring πρέπει να ξεχωρίζει regional routing issue από resolver/application issue.

### 5. BGP path selection

BGP ανταλλάσσει reachability ανάμεσα σε autonomous systems και επιλέγει paths με policy. Security analysis χρειάζεται prefix ownership, upstream relationships και evidence από πολλές παρατηρήσεις αντί για μία route view.

### 6. Route-origin validation

RPKI/ROV βοηθά να ελεγχθεί αν ένα AS είναι εξουσιοδοτημένο να origin ένα prefix. Δεν αποδεικνύει ολόκληρο το AS path και πρέπει να συνδυάζεται με routing policy/monitoring.

### 7. Control-plane monitoring

DNS zone changes, registrar events, RPKI state, BGP announcements και resolver health χρειάζονται timestamps και independent alert paths. Control-plane compromise συχνά προηγείται του visible data-plane impact.

### 8. Resilience design

Χρησιμοποίησε diversity σε authoritative DNS, resolvers, transit, regions και recovery accounts όπου δικαιολογείται. Η redundancy πρέπει να αποφεύγει κοινό hidden dependency που καταρρέει ταυτόχρονα.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Γράψε πρώτα invariant και expected result, άλλαξε μία μεταβλητή κάθε φορά και κράτησε μόνο το evidence που χρειάζεται.

1. **Trace the full resolution path for a domain you own using passive/publicly documented information and draw the delegation chain** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
2. **Create a tabletop exercise for accidental deletion of a DNS zone and list recovery dependencies in order** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
3. **Build a worksheet that separates DNS integrity, DNS confidentiality, registrar security, certificate issuance, and routing security controls** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary και ποιος έχει authority;
2. Ποιο state μπορεί να γίνει stale, replayed ή inconsistent;
3. Ποιο evidence θα διέψευδε την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά το blast radius;
5. Πώς θα επαναλάβεις το test με ασφάλεια μετά τη remediation?

## Πλήρες αγγλικό μάθημα

[English Module 087](../../English/04-Network-Wireless-and-Internet/87-DNS-Routing-BGP-and-Internet-Infrastructure-Security.md)

## Συνέχεια

Χρησιμοποίησε **Αναζήτηση μαθημάτων** ή **Διαδρομές μάθησης** από το κύριο menu για τα σχετικά επόμενα θέματα.

---

# Enterprise Wireless, WPA3, 802.1X και Wi‑Fi 6/6E/7

> **Ελληνική έκδοση — Μάθημα 088.** Διατηρούνται οι διεθνείς τεχνικοί όροι όπου είναι ακριβέστεροι και ευκολότεροι στην αναζήτηση.

## Στόχος του μαθήματος

Να κατανοήσεις σε βάθος το **Enterprise Wireless, WPA3, 802.1X και Wi‑Fi 6/6E/7**, να αναγνωρίζεις trust boundaries και failure states και να μπορείς να αποδείξεις ένα συμπέρασμα με ασφαλές, επαναλήψιμο evidence.

> **Όριο εξουσιοδότησης:** Πρακτική μόνο σε συστήματα, λογαριασμούς, κώδικα ή labs που σου ανήκουν ή έχεις ρητή άδεια να ελέγξεις. Προτίμησε localhost, synthetic data και disposable environments.

## Βαθιές τεχνικές έννοιες

### 1. WPA3 modes

WPA3-Personal χρησιμοποιεί SAE και enterprise deployments έχουν διαφορετικά assurance profiles. Transition modes πρέπει να αξιολογούνται επειδή compatibility μπορεί να διατηρεί πιο αδύναμο path.

### 2. 802.1X architecture

Enterprise Wi-Fi συνδέει supplicant, authenticator/AP και authentication server όπως RADIUS. Client certificate/server validation και identity mapping είναι εξίσου σημαντικά με το wireless cipher.

### 3. Protected management frames

PMF προστατεύει συγκεκριμένες management frames από forgery όταν απαιτείται σωστά. Δεν προστατεύει κάθε radio denial/interference και πρέπει να ελέγχεται η πραγματική negotiation state.

### 4. Roaming and key hierarchy

Fast roaming και enterprise key hierarchies μειώνουν authentication latency αλλά δημιουργούν additional key/state relationships. Review cache lifetime, controller trust και revocation behavior.

### 5. 6 GHz and newer bands

Νεότερα bands/standards αλλάζουν channel use, discovery και security requirements. Μην εφαρμόζεις assumptions από legacy 2.4/5 GHz χωρίς να ελέγξεις device/AP capabilities και policy.

### 6. Guest and IoT segmentation

Guests και IoT χρειάζονται διαφορετικό trust από managed endpoints. Client isolation, restricted east-west access και ξεχωριστό management plane περιορίζουν blast radius.

### 7. Rogue and misconfigured infrastructure

Unknown APs, duplicate SSIDs, unsafe EAP profiles και accidental bridging είναι συχνά configuration problems. Inventory και controller/RADIUS logs είναι ασφαλέστερη βάση από disruptive radio testing.

### 8. Wireless evidence

Κράτησε AP/controller configuration, authentication results, certificate/EAP context, roaming events και channel health. Απόφυγε collection άσχετου user payload.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Γράψε πρώτα invariant και expected result, άλλαξε μία μεταβλητή κάθε φορά και κράτησε μόνο το evidence που χρειάζεται.

1. **Design three WLAN roles—managed, guest, IoT—and write the exact trust assumptions and allowed flows between them** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
2. **On equipment you own, inspect whether client devices validate the expected enterprise authentication certificate and document the trust path** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
3. **Create an upgrade checklist for moving from a mixed WPA2/WPA3 deployment to a stricter policy without stranding unsupported devices** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary και ποιος έχει authority;
2. Ποιο state μπορεί να γίνει stale, replayed ή inconsistent;
3. Ποιο evidence θα διέψευδε την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά το blast radius;
5. Πώς θα επαναλάβεις το test με ασφάλεια μετά τη remediation?

## Πλήρες αγγλικό μάθημα

[English Module 088](../../English/04-Network-Wireless-and-Internet/88-Enterprise-Wireless-WPA3-8021X-WiFi6-7-Security.md)

## Συνέχεια

Χρησιμοποίησε **Αναζήτηση μαθημάτων** ή **Διαδρομές μάθησης** από το κύριο menu για τα σχετικά επόμενα θέματα.

---

# Ασφάλεια GraphQL, gRPC, WebSockets και Real-Time APIs

> **Ελληνική έκδοση — Μάθημα 089.** Διατηρούνται οι διεθνείς τεχνικοί όροι όπου είναι ακριβέστεροι και ευκολότεροι στην αναζήτηση.

## Στόχος του μαθήματος

Να κατανοήσεις σε βάθος το **Ασφάλεια GraphQL, gRPC, WebSockets και Real-Time APIs**, να αναγνωρίζεις trust boundaries και failure states και να μπορείς να αποδείξεις ένα συμπέρασμα με ασφαλές, επαναλήψιμο evidence.

> **Όριο εξουσιοδότησης:** Πρακτική μόνο σε συστήματα, λογαριασμούς, κώδικα ή labs που σου ανήκουν ή έχεις ρητή άδεια να ελέγξεις. Προτίμησε localhost, synthetic data και disposable environments.

## Βαθιές τεχνικές έννοιες

### 1. GraphQL schema surface

GraphQL schema αποκαλύπτει objects, fields και relationships που χρειάζονται field/object-level authorization. Το γεγονός ότι ένα resolver είναι reachable δεν σημαίνει ότι κάθε authenticated user μπορεί να το χρησιμοποιήσει.

### 2. Query complexity

Nested queries, aliases και expensive resolvers μπορούν να πολλαπλασιάσουν backend work. Βάλε depth/complexity/cost budgets και monitor actual resolver/database load.

### 3. Object and field authorization

Authorization πρέπει να εφαρμόζεται σε κάθε object/field resolver με tenant/resource context. Client-supplied IDs και hidden UI fields δεν αποτελούν security boundary.

### 4. gRPC semantics

gRPC χρησιμοποιεί typed service/method contracts πάνω από HTTP/2. Validate metadata, message sizes, deadlines, streaming lifecycle και method-level authorization όπως σε οποιοδήποτε privileged API.

### 5. WebSocket lifecycle

WebSocket ξεκινά με HTTP handshake και μετά γίνεται long-lived bidirectional channel. Authentication στο handshake δεν αρκεί αν permissions αλλάζουν ή messages έχουν διαφορετικό authorization context.

### 6. Realtime multi-tenancy

Subscriptions/channels πρέπει να δένονται με tenant και resource authorization. Reconnect, resume, fan-out και cached membership state μπορούν να αφήσουν stale access.

### 7. Protocol translation

Gateway που μεταφράζει REST, GraphQL, gRPC ή WebSocket είναι parser/policy boundary. Έλεγξε canonical identity, headers, errors και timeouts end-to-end.

### 8. Observability

Κατέγραψε operation/method, authenticated identity, tenant/resource, latency, errors και backend cost χωρίς sensitive payloads. Long-lived streams χρειάζονται start/stop και policy-change context.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Γράψε πρώτα invariant και expected result, άλλαξε μία μεταβλητή κάθε φορά και κράτησε μόνο το evidence που χρειάζεται.

1. **Implement a tiny localhost GraphQL-like toy resolver in Python and write authorization tests for object and field access without exposing it beyond loopback** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
2. **Model a WebSocket session as states: unauthenticated, authenticated, reauthenticated, revoked, closed; define allowed messages in each state** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
3. **Create a gRPC security review checklist covering identity propagation, method authorization, deadlines, message limits, and logging** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary και ποιος έχει authority;
2. Ποιο state μπορεί να γίνει stale, replayed ή inconsistent;
3. Ποιο evidence θα διέψευδε την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά το blast radius;
5. Πώς θα επαναλάβεις το test με ασφάλεια μετά τη remediation?

## Πλήρες αγγλικό μάθημα

[English Module 089](../../English/02-Recon-Pentesting-Web-and-AppSec/89-GraphQL-gRPC-WebSockets-and-Realtime-API-Security.md)

## Συνέχεια

Χρησιμοποίησε **Αναζήτηση μαθημάτων** ή **Διαδρομές μάθησης** από το κύριο menu για τα σχετικά επόμενα θέματα.

---

# Ασφάλεια Databases, Data Layer και Query Engines

> **Ελληνική έκδοση — Μάθημα 090.** Διατηρούνται οι διεθνείς τεχνικοί όροι όπου είναι ακριβέστεροι και ευκολότεροι στην αναζήτηση.

## Στόχος του μαθήματος

Να κατανοήσεις σε βάθος το **Ασφάλεια Databases, Data Layer και Query Engines**, να αναγνωρίζεις trust boundaries και failure states και να μπορείς να αποδείξεις ένα συμπέρασμα με ασφαλές, επαναλήψιμο evidence.

> **Όριο εξουσιοδότησης:** Πρακτική μόνο σε συστήματα, λογαριασμούς, κώδικα ή labs που σου ανήκουν ή έχεις ρητή άδεια να ελέγξεις. Προτίμησε localhost, synthetic data και disposable environments.

## Βαθιές τεχνικές έννοιες

### 1. Query construction

Parameterized queries ή typed query APIs διαχωρίζουν data από query syntax. Dynamic table/field names χρειάζονται explicit allowlists και όχι απλή string escaping.

### 2. Database identity

Εφαρμογές και admins πρέπει να χρησιμοποιούν ξεχωριστές database identities με least privilege. Connection pool/service account authority καθορίζει blast radius ενός application bug.

### 3. Row and tenant isolation

Multi-tenant isolation μπορεί να εφαρμόζεται σε application, database row-level policy ή ξεχωριστά stores. Η τελική decision πρέπει να χρησιμοποιεί trusted tenant context και negative tests μεταξύ synthetic tenants.

### 4. Stored logic and triggers

Triggers, procedures και functions μπορούν να εκτελούν privileged logic εκτός application code. Review ownership/definer rights, side effects, migrations και auditability.

### 5. NoSQL and search engines

Document/search/query DSLs έχουν διαφορετικές injection και authorization semantics από SQL. Χρησιμοποίησε structured APIs, schema/field controls και resource limits.

### 6. Replication and backups

Replicas, exports και backups περιέχουν το ίδιο ή περισσότερο sensitive data από primary. Encryption, access, retention και restore tests πρέπει να καλύπτουν όλα τα copies.

### 7. Encryption boundaries

At-rest encryption προστατεύει storage media αλλά database/service identity μπορεί ακόμη να διαβάζει plaintext. Field-level ή application-layer encryption αλλάζει key/metadata/query tradeoffs και χρειάζεται συγκεκριμένο threat model.

### 8. Audit and anomaly detection

Database audit πρέπει να συνδέει identity, client/service, query/action, object, result και time χωρίς να γράφει passwords/secrets. Baselines βοηθούν να εντοπιστούν unusual bulk access ή admin changes.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Γράψε πρώτα invariant και expected result, άλλαξε μία μεταβλητή κάθε φορά και κράτησε μόνο το evidence που χρειάζεται.

1. **Build a localhost SQLite or PostgreSQL toy application with separate migration and runtime roles; document which statements each role should be able to execute** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
2. **Create a tenant-isolation test matrix that covers API calls, background jobs, exports, caching, and administrative tools** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
3. **Take a harmless sample backup, restore it into an isolated lab, and verify the restore procedure includes permissions and secrets—not just data files** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary και ποιος έχει authority;
2. Ποιο state μπορεί να γίνει stale, replayed ή inconsistent;
3. Ποιο evidence θα διέψευδε την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά το blast radius;
5. Πώς θα επαναλάβεις το test με ασφάλεια μετά τη remediation?

## Πλήρες αγγλικό μάθημα

[English Module 090](../../English/02-Recon-Pentesting-Web-and-AppSec/90-Database-Data-Layer-and-Query-Engine-Security.md)

## Συνέχεια

Χρησιμοποίησε **Αναζήτηση μαθημάτων** ή **Διαδρομές μάθησης** από το κύριο menu για τα σχετικά επόμενα θέματα.

---

# Message Queues, Event Streaming και Ασφάλεια Distributed Systems

> **Ελληνική έκδοση — Μάθημα 091.** Διατηρούνται οι διεθνείς τεχνικοί όροι όπου είναι ακριβέστεροι και ευκολότεροι στην αναζήτηση.

## Στόχος του μαθήματος

Να κατανοήσεις σε βάθος το **Message Queues, Event Streaming και Ασφάλεια Distributed Systems**, να αναγνωρίζεις trust boundaries και failure states και να μπορείς να αποδείξεις ένα συμπέρασμα με ασφαλές, επαναλήψιμο evidence.

> **Όριο εξουσιοδότησης:** Πρακτική μόνο σε συστήματα, λογαριασμούς, κώδικα ή labs που σου ανήκουν ή έχεις ρητή άδεια να ελέγξεις. Προτίμησε localhost, synthetic data και disposable environments.

## Βαθιές τεχνικές έννοιες

### 1. Producer and consumer identity

Producer και consumer πρέπει να έχουν ξεχωριστές identities και permissions ανά topic/queue/action. Shared broker credential κρύβει attribution και αυξάνει blast radius.

### 2. Topic and routing design

Topic names, routing keys και subscriptions είναι authorization surface. Διαχώρισε tenants/environments και απόφυγε wildcard permissions που φτάνουν data άσχετων workloads.

### 3. Message authenticity and replay

TLS προστατεύει transport, αλλά downstream consumer μπορεί να χρειάζεται message provenance/freshness όταν messages αποθηκεύονται ή περνούν πολλούς brokers. IDs, timestamps ή signatures πρέπει να έχουν σαφές replay model.

### 4. Schema evolution

Producer/consumer versions μπορεί να συνυπάρχουν. Explicit schemas, compatibility rules και unknown-field behavior εμποδίζουν silent semantic change σε security-sensitive fields.

### 5. Retries and idempotency

At-least-once delivery σημαίνει duplicates. Consumer που εκτελεί state-changing action χρειάζεται idempotency ή transaction model ώστε retry να μη διπλασιάζει πληρωμή/privilege/change.

### 6. Dead-letter queues

DLQ περιέχει failed messages και συχνά sensitive payload. Περιορίσε access/retention, καταγραφή reasons και safe replay ώστε corrupted message να μην επανεισάγεται ανεξέλεγκτα.

### 7. Background privilege

Workers συχνά τρέχουν χωρίς user interaction και με broad service permissions. Δέσε κάθε message με trusted tenant/resource context και δώσε μόνο την authority που χρειάζεται το συγκεκριμένο handler.

### 8. Distributed tracing

Correlation IDs και traces βοηθούν να ακολουθήσεις event σε producer→broker→consumer χωρίς να θεωρείς μία timestamp σειρά τέλεια. Κατέγραψε retries και message IDs για causal analysis.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Γράψε πρώτα invariant και expected result, άλλαξε μία μεταβλητή κάθε φορά και κράτησε μόνο το evidence που χρειάζεται.

1. **Model an order-processing pipeline with producer, broker, three consumers, dead-letter queue, and admin replay tool; mark each trust boundary** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
2. **Write test cases for duplicate delivery, out-of-order delivery, expired messages, malformed schemas, and unauthorized routing using toy data** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
3. **Design a least-privilege matrix for producers and consumers and identify where one compromised workload would currently have excessive reach** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary και ποιος έχει authority;
2. Ποιο state μπορεί να γίνει stale, replayed ή inconsistent;
3. Ποιο evidence θα διέψευδε την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά το blast radius;
5. Πώς θα επαναλάβεις το test με ασφάλεια μετά τη remediation?

## Πλήρες αγγλικό μάθημα

[English Module 091](../../English/07-Cloud-Containers-and-Supply-Chain/91-Message-Queues-Event-Streaming-and-Distributed-System-Security.md)

## Συνέχεια

Χρησιμοποίησε **Αναζήτηση μαθημάτων** ή **Διαδρομές μάθησης** από το κύριο menu για τα σχετικά επόμενα θέματα.

---

# OAuth 2.0 Security BCP, OIDC Federation και Token Defense

> **Ελληνική έκδοση — Μάθημα 092.** Διατηρούνται οι διεθνείς τεχνικοί όροι όπου είναι ακριβέστεροι και ευκολότεροι στην αναζήτηση.

## Στόχος του μαθήματος

Να κατανοήσεις σε βάθος το **OAuth 2.0 Security BCP, OIDC Federation και Token Defense**, να αναγνωρίζεις trust boundaries και failure states και να μπορείς να αποδείξεις ένα συμπέρασμα με ασφαλές, επαναλήψιμο evidence.

> **Όριο εξουσιοδότησης:** Πρακτική μόνο σε συστήματα, λογαριασμούς, κώδικα ή labs που σου ανήκουν ή έχεις ρητή άδεια να ελέγξεις. Προτίμησε localhost, synthetic data και disposable environments.

## Βαθιές τεχνικές έννοιες

### 1. OAuth roles and purpose

OAuth είναι delegation framework: resource owner, client, authorization server και resource server έχουν διαφορετικό ρόλο. Access token δεν είναι γενικό identity proof για οποιαδήποτε εφαρμογή.

### 2. Authorization code and PKCE

Authorization Code με PKCE δένει authorization response με το client instance που ξεκίνησε το flow. Validate state/nonce όπου απαιτείται και μην εκθέτεις code/tokens σε unnecessary browser locations/logs.

### 3. Redirect URI integrity

Redirect URI είναι high-value boundary. Χρησιμοποίησε exact/pre-registered URIs και απέφυγε open redirects ή broad wildcard matching που επιτρέπουν code delivery σε λάθος endpoint.

### 4. Issuer and mix-up defenses

Clients/resource servers πρέπει να ξέρουν ποιος issuer εξέδωσε response/token και να μην μπερδεύουν multiple authorization servers. Bind discovery, issuer, endpoints και keys σε αναμενόμενο relationship.

### 5. Token audience and scope

Audience περιορίζει ποιο resource server πρέπει να δεχτεί token και scope/authorization περιορίζει operations. Έγκυρη signature χωρίς σωστό audience/tenant/resource context δεν αρκεί.

### 6. Refresh tokens

Refresh token έχει μεγαλύτερο lifecycle και μπορεί να εκδώσει νέα access tokens. Rotation, reuse detection, sender/client binding όπου υποστηρίζεται και revocation μειώνουν persistence risk.

### 7. Sender-constrained tokens

Mechanisms όπως mTLS ή proof-of-possession μπορούν να δένουν token με συγκεκριμένο client key ώστε stolen token μόνο του να μην αρκεί. Operational key lifecycle και proxy boundaries πρέπει να υποστηρίζουν το binding.

### 8. Federation lifecycle

OIDC/federation relationships, signing keys, client registration και metadata αλλάζουν. Κράτησε authenticated configuration, rollover overlap, de-registration και incident revocation plan.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Γράψε πρώτα invariant και expected result, άλλαξε μία μεταβλητή κάθε φορά και κράτησε μόνο το evidence που χρειάζεται.

1. **Draw an authorization-code + PKCE sequence for a localhost demo and label every value that must be bound to the initiating transaction** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
2. **Create a token-validation checklist separating cryptographic validity from authorization decisions at the API** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
3. **Review a hypothetical federation design for account-linking ambiguity, stale signing keys, incorrect issuer/audience checks, and deprovisioning gaps** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary και ποιος έχει authority;
2. Ποιο state μπορεί να γίνει stale, replayed ή inconsistent;
3. Ποιο evidence θα διέψευδε την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά το blast radius;
5. Πώς θα επαναλάβεις το test με ασφάλεια μετά τη remediation?

## Πλήρες αγγλικό μάθημα

[English Module 092](../../English/06-Identity-Cryptography-and-Trust/92-OAuth-20-Security-BCP-OIDC-Federation-and-Token-Defense.md)

## Συνέχεια

Χρησιμοποίησε **Αναζήτηση μαθημάτων** ή **Διαδρομές μάθησης** από το κύριο menu για τα σχετικά επόμενα θέματα.

---

# Μοντέλα Authorization: RBAC, ABAC, ReBAC και Policy Engines

> **Ελληνική έκδοση — Μάθημα 093.** Διατηρούνται οι διεθνείς τεχνικοί όροι όπου είναι ακριβέστεροι και ευκολότεροι στην αναζήτηση.

## Στόχος του μαθήματος

Να κατανοήσεις σε βάθος το **Μοντέλα Authorization: RBAC, ABAC, ReBAC και Policy Engines**, να αναγνωρίζεις trust boundaries και failure states και να μπορείς να αποδείξεις ένα συμπέρασμα με ασφαλές, επαναλήψιμο evidence.

> **Όριο εξουσιοδότησης:** Πρακτική μόνο σε συστήματα, λογαριασμούς, κώδικα ή labs που σου ανήκουν ή έχεις ρητή άδεια να ελέγξεις. Προτίμησε localhost, synthetic data και disposable environments.

## Βαθιές τεχνικές έννοιες

### 1. Reference monitor

Η authorization decision πρέπει να περνά από component που είναι always invoked, tamper-resistant και αρκετά μικρό/κατανοητό. Distributed architectures χρειάζονται consistent policy inputs και όχι ad-hoc checks.

### 2. RBAC

RBAC αποδίδει permissions σε roles και roles σε subjects. Απλό στη διαχείριση αλλά μπορεί να οδηγήσει σε role explosion ή broad inherited access αν δεν υπάρχει lifecycle/review.

### 3. ABAC

ABAC χρησιμοποιεί attributes από subject, resource, action και environment. Τα attributes είναι security inputs και χρειάζονται trustworthy source, freshness και canonical semantics.

### 4. ReBAC

Relationship-based authorization αποφασίζει από graph σχέσεων όπως owner/member/editor. Review graph traversal, transitive relationships, cycles και tenant boundaries.

### 5. Deny and default semantics

Default deny και explicit conflict/precedence rules κάνουν policy predictable. Unknown/missing attributes πρέπει να έχουν σαφές fail behavior.

### 6. Caching

Authorization cache βελτιώνει performance αλλά μπορεί να κρατήσει stale permission μετά revocation. Δέσε cache keys με relevant policy/version/context και όρισε invalidation.

### 7. Administrative authorization

Όποιος αλλάζει roles/policies έχει μεγαλύτερη authority από ordinary user. Protect policy management με separation of duties, strong auth, review και audit.

### 8. Testing policy

Χρησιμοποίησε policy matrix με positive/negative cases ανά subject-resource-action-context. Regression tests πρέπει να καλύπτουν deny, missing data, tenant crossover και revocation.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Γράψε πρώτα invariant και expected result, άλλαξε μία μεταβλητή κάθε φορά και κράτησε μόνο το evidence που χρειάζεται.

1. **Model a file-sharing application using RBAC and then ReBAC; compare which rules become simpler and which new risks appear** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
2. **Write an authorization decision table with principal, action, resource, tenant, relationship, device posture, and time context** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
3. **Create regression tests for revocation and stale-cache behavior in a toy policy evaluator** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary και ποιος έχει authority;
2. Ποιο state μπορεί να γίνει stale, replayed ή inconsistent;
3. Ποιο evidence θα διέψευδε την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά το blast radius;
5. Πώς θα επαναλάβεις το test με ασφάλεια μετά τη remediation?

## Πλήρες αγγλικό μάθημα

[English Module 093](../../English/06-Identity-Cryptography-and-Trust/93-Authorization-Models-RBAC-ABAC-ReBAC-and-Policy-Engines.md)

## Συνέχεια

Χρησιμοποίησε **Αναζήτηση μαθημάτων** ή **Διαδρομές μάθησης** από το κύριο menu για τα σχετικά επόμενα θέματα.

---

# Virtualization, Hypervisors, VMs και Confidential Computing

> **Ελληνική έκδοση — Μάθημα 094.** Διατηρούνται οι διεθνείς τεχνικοί όροι όπου είναι ακριβέστεροι και ευκολότεροι στην αναζήτηση.

## Στόχος του μαθήματος

Να κατανοήσεις σε βάθος το **Virtualization, Hypervisors, VMs και Confidential Computing**, να αναγνωρίζεις trust boundaries και failure states και να μπορείς να αποδείξεις ένα συμπέρασμα με ασφαλές, επαναλήψιμο evidence.

> **Όριο εξουσιοδότησης:** Πρακτική μόνο σε συστήματα, λογαριασμούς, κώδικα ή labs που σου ανήκουν ή έχεις ρητή άδεια να ελέγξεις. Προτίμησε localhost, synthetic data και disposable environments.

## Βαθιές τεχνικές έννοιες

### 1. Hypervisor models

Type-1 και hosted hypervisors τοποθετούν virtualization boundary σε διαφορετικά layers. Threat model πρέπει να περιλαμβάνει host/hypervisor, management plane και shared hardware.

### 2. Hardware virtualization

CPU/IOMMU virtualization απομονώνει guest execution και DMA όταν ρυθμίζεται σωστά. Firmware, device passthrough και platform settings μπορούν να αλλάξουν το πραγματικό boundary.

### 3. Virtual devices

Emulated/paravirtualized network, storage, graphics και other devices είναι complex parser interfaces από guest προς privileged host code. Μείωσε unused devices και κράτησε hypervisor/device-model patches ενημερωμένα.

### 4. Snapshots and images

Snapshots/images περιέχουν memory/disk/secrets και μπορούν να επαναφέρουν stale credentials ή vulnerable state. Protect storage, provenance, access και lifecycle όπως production data.

### 5. Management plane

Hypervisor/cloud console μπορεί να create, attach disks, snapshot ή inspect guests. Management identity χρειάζεται strong auth, least privilege και independent audit.

### 6. Nested virtualization

Nested layers αυξάνουν complexity και κάνουν assumptions για hardware features/telemetry λιγότερο προφανή. Document ποιο layer owns each control και ποια isolation guarantees χάνονται.

### 7. Confidential computing

Memory-encryption/TEE VM models μειώνουν trust στον host για συγκεκριμένα data-in-use threats. Δεν αφαιρούν guest vulnerabilities, metadata leakage, availability ή misconfigured attestation/policy.

### 8. Boundary verification

Verify isolation με configuration, attestation όπου σχετικό, device assignment και harmless cross-VM negative tests. Μην θεωρείς marketing label evidence από μόνο του.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Γράψε πρώτα invariant και expected result, άλλαξε μία μεταβλητή κάθε φορά και κράτησε μόνο το evidence που χρειάζεται.

1. **Build a local VM threat model listing every host/guest integration feature and justify whether it is required** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
2. **Take a disposable VM snapshot with non-sensitive test data and document what security-sensitive state a real snapshot could preserve** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
3. **Compare the trust assumptions of a normal VM, container, and confidential VM in a one-page matrix** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary και ποιος έχει authority;
2. Ποιο state μπορεί να γίνει stale, replayed ή inconsistent;
3. Ποιο evidence θα διέψευδε την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά το blast radius;
5. Πώς θα επαναλάβεις το test με ασφάλεια μετά τη remediation?

## Πλήρες αγγλικό μάθημα

[English Module 094](../../English/07-Cloud-Containers-and-Supply-Chain/94-Virtualization-Hypervisors-VMs-and-Confidential-Computing.md)

## Συνέχεια

Χρησιμοποίησε **Αναζήτηση μαθημάτων** ή **Διαδρομές μάθησης** από το κύριο menu για τα σχετικά επόμενα θέματα.

---

# Kernel Security Primitives, Attack Surface και Runtime Trust

> **Ελληνική έκδοση — Μάθημα 095.** Διατηρούνται οι διεθνείς τεχνικοί όροι όπου είναι ακριβέστεροι και ευκολότεροι στην αναζήτηση.

## Στόχος του μαθήματος

Να κατανοήσεις σε βάθος το **Kernel Security Primitives, Attack Surface και Runtime Trust**, να αναγνωρίζεις trust boundaries και failure states και να μπορείς να αποδείξεις ένα συμπέρασμα με ασφαλές, επαναλήψιμο evidence.

> **Όριο εξουσιοδότησης:** Πρακτική μόνο σε συστήματα, λογαριασμούς, κώδικα ή labs που σου ανήκουν ή έχεις ρητή άδεια να ελέγξεις. Προτίμησε localhost, synthetic data και disposable environments.

## Βαθιές τεχνικές έννοιες

### 1. System-call boundary

Syscalls είναι βασικό interface από user mode προς kernel. Attack surface εξαρτάται από reachable calls, arguments, privileges και enabled subsystems, όχι απλώς από kernel version.

### 2. Drivers and device interfaces

Drivers επεξεργάζονται untrusted device/user inputs με υψηλό privilege. Αφαίρεσε unused drivers/interfaces και αξιολόγησε ioctl, device nodes, firmware και hotplug trust.

### 3. Kernel memory safety

Memory corruption στο kernel έχει μεγάλο impact λόγω privilege. Memory-safe components, sanitizers, hardened allocators και compiler mitigations μειώνουν bug classes και βοηθούν root-cause.

### 4. Privilege model

UIDs, capabilities, tokens/credentials, namespaces και LSM policy συνδυάζονται. “root/non-root” μόνο του είναι πολύ απλοποιημένο για σύγχρονα container/host boundaries.

### 5. Module and boot trust

Kernel modules και boot artifacts είναι privileged code. Secure/measured boot, signature policy και restricted module loading προστατεύουν runtime trust chain.

### 6. Race conditions

Concurrent kernel state μπορεί να δημιουργήσει UAF/TOCTOU/logic bugs. Safe research χρησιμοποιεί owned debug kernels, sanitizers και reproducible stress—not production exploitation.

### 7. Attack-surface reduction

Disable unused protocols, filesystems, drivers, debug interfaces και privileged features. Reduction αφαιρεί reachable complexity αντί να προσθέτει μόνο detection.

### 8. Telemetry

Kernel logs, audit, eBPF/tracepoints, crash dumps και integrity state δίνουν complementary views. Collect version/configuration ώστε event να ερμηνεύεται σωστά.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Γράψε πρώτα invariant και expected result, άλλαξε μία μεταβλητή κάθε φορά και κράτησε μόνο το evidence που χρειάζεται.

1. **Inventory the enabled kernel-facing interfaces in an owned Linux VM: devices, filesystems, modules, namespaces, and exposed sockets; classify them by necessity** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
2. **Compare process capabilities before and after applying a least-privilege service configuration in a disposable lab** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
3. **Read a harmless kernel crash report or public bug description and identify object lifetime, privilege context, and mitigation layers without reproducing exploitation** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary και ποιος έχει authority;
2. Ποιο state μπορεί να γίνει stale, replayed ή inconsistent;
3. Ποιο evidence θα διέψευδε την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά το blast radius;
5. Πώς θα επαναλάβεις το test με ασφάλεια μετά τη remediation?

## Πλήρες αγγλικό μάθημα

[English Module 095](../../English/03-Systems-Malware-and-Reverse-Engineering/95-Kernel-Security-Primitives-Attack-Surface-and-Runtime-Trust.md)

## Συνέχεια

Χρησιμοποίησε **Αναζήτηση μαθημάτων** ή **Διαδρομές μάθησης** από το κύριο menu για τα σχετικά επόμενα θέματα.

---

# eBPF Observability, Linux Telemetry και Detection Engineering

> **Ελληνική έκδοση — Μάθημα 096.** Διατηρούνται οι διεθνείς τεχνικοί όροι όπου είναι ακριβέστεροι και ευκολότεροι στην αναζήτηση.

## Στόχος του μαθήματος

Να κατανοήσεις σε βάθος το **eBPF Observability, Linux Telemetry και Detection Engineering**, να αναγνωρίζεις trust boundaries και failure states και να μπορείς να αποδείξεις ένα συμπέρασμα με ασφαλές, επαναλήψιμο evidence.

> **Όριο εξουσιοδότησης:** Πρακτική μόνο σε συστήματα, λογαριασμούς, κώδικα ή labs που σου ανήκουν ή έχεις ρητή άδεια να ελέγξεις. Προτίμησε localhost, synthetic data και disposable environments.

## Βαθιές τεχνικές έννοιες

### 1. Program and map model

eBPF programs εκτελούνται σε defined hooks και χρησιμοποιούν maps για state/communication. Security review χρειάζεται program type, attach point, map ownership και lifecycle.

### 2. Verifier and privilege

Kernel verifier περιορίζει unsafe program behavior αλλά privilege/policy για loading/attaching παραμένει κρίσιμο. Unprivileged availability διαφέρει ανά platform/configuration.

### 3. Tracepoints and probes

Tracepoints δίνουν πιο σταθερά semantics από ad-hoc probes, ενώ kprobes/uprobes έχουν version/symbol assumptions. Detection πρέπει να γνωρίζει πόσο stable είναι η source.

### 4. Network hooks

XDP/tc/socket hooks βλέπουν traffic σε διαφορετικό σημείο. Κατέγραψε pre/post-NAT, namespace/interface context και packet drops ώστε telemetry να μην παρερμηνεύεται.

### 5. Telemetry design

Event schema πρέπει να κρατά actor/process, resource, operation, result και correlation με bounded cardinality. Περισσότερα events δεν σημαίνουν καλύτερη detection αν λείπει context.

### 6. Tamper and blind spots

Sensor μέσα στο ίδιο host μοιράζεται κάποιο trust με host/kernel. Document τι μπορεί να χάσει σε overload, namespace, encrypted layer ή privileged compromise και χρησιμοποίησε independent logs όπου χρειάζεται.

### 7. Performance

High-rate probes μπορούν να προσθέσουν CPU/memory/IO pressure ή dropped events. Measure overhead και loss rate και βάλε sampling/bounds.

### 8. Detection lifecycle

Version rule/program, test με benign fixtures, deploy σταδιακά, monitor data quality και επανέλεγξε μετά kernel/app changes. Detection είναι maintained software.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Γράψε πρώτα invariant και expected result, άλλαξε μία μεταβλητή κάθε φορά και κράτησε μόνο το evidence που χρειάζεται.

1. **Write a detection hypothesis for unexpected interactive shells in a server container and specify which kernel/process fields would prove or refute it—without collecting real user content** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
2. **Compare audit logs, process accounting, and eBPF telemetry for the same harmless process-start event in a lab** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
3. **Design a rollback plan for an observability agent that begins consuming excessive CPU or producing unbounded event volume** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary και ποιος έχει authority;
2. Ποιο state μπορεί να γίνει stale, replayed ή inconsistent;
3. Ποιο evidence θα διέψευδε την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά το blast radius;
5. Πώς θα επαναλάβεις το test με ασφάλεια μετά τη remediation?

## Πλήρες αγγλικό μάθημα

[English Module 096](../../English/03-Systems-Malware-and-Reverse-Engineering/96-eBPF-Observability-Linux-Telemetry-and-Detection-Engineering.md)

## Συνέχεια

Χρησιμοποίησε **Αναζήτηση μαθημάτων** ή **Διαδρομές μάθησης** από το κύριο menu για τα σχετικά επόμενα θέματα.

---

# CI/CD, Build Provenance, SLSA 1.2 και Artifact Trust

> **Ελληνική έκδοση — Μάθημα 097.** Διατηρούνται οι διεθνείς τεχνικοί όροι όπου είναι ακριβέστεροι και ευκολότεροι στην αναζήτηση.

## Στόχος του μαθήματος

Να κατανοήσεις σε βάθος το **CI/CD, Build Provenance, SLSA 1.2 και Artifact Trust**, να αναγνωρίζεις trust boundaries και failure states και να μπορείς να αποδείξεις ένα συμπέρασμα με ασφαλές, επαναλήψιμο evidence.

> **Όριο εξουσιοδότησης:** Πρακτική μόνο σε συστήματα, λογαριασμούς, κώδικα ή labs που σου ανήκουν ή έχεις ρητή άδεια να ελέγξεις. Προτίμησε localhost, synthetic data και disposable environments.

## Βαθιές τεχνικές έννοιες

### 1. Source control trust

Build trust ξεκινά από repository identities, protected branches, reviews και immutable source revision. Admin bypass ή compromised bot μπορεί να αλλάξει το artifact πριν καν ξεκινήσει build.

### 2. Build isolation

Builder πρέπει να έχει ελάχιστη network/secret authority και clean/reproducible environment. Shared mutable workers αυξάνουν cross-build contamination και secret leakage.

### 3. Provenance

Provenance συνδέει source, builder, inputs, parameters και output artifact. Χρειάζεται authenticated generation και verification από deploy/promotion policy.

### 4. SLSA 1.2

SLSA οργανώνει supply-chain requirements γύρω από build/provenance threats. Χρησιμοποίησέ το ως framework για συγκεκριμένα controls και evidence, όχι σαν badge χωρίς scope.

### 5. Artifact signing

Signature/attestation πρέπει να αφορά immutable artifact digest και trusted signer/workload identity. Keyless/short-lived signing αλλάζει identity lifecycle αλλά δεν αφαιρεί authorization policy.

### 6. Promotion

Build once και promote verified artifact ανά environment μειώνει rebuild drift. Promotion policy πρέπει να ελέγχει digest, provenance, approvals και environment-specific configuration.

### 7. Secrets in CI

CI secrets πρέπει να είναι short-lived/scoped και να μη διατίθενται σε untrusted forks/jobs. Redaction δεν διορθώνει credential που ήδη δόθηκε σε malicious step.

### 8. Verification at deploy

Το deploy boundary πρέπει να επαληθεύει artifact identity/provenance/policy και όχι να εμπιστεύεται απλώς tag ή registry location. Failure behavior και exceptions χρειάζονται audit.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Γράψε πρώτα invariant και expected result, άλλαξε μία μεταβλητή κάθε φορά και κράτησε μόνο το evidence που χρειάζεται.

1. **Draw the source→build→registry→deployment chain for a small project and mark every identity that can change the final artifact** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
2. **Generate a harmless local artifact and a JSON provenance record containing source hash, builder, timestamp, and output digest; verify consistency with a Python script** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
3. **Create a CI hardening checklist that distinguishes source-track controls from build-track controls** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary και ποιος έχει authority;
2. Ποιο state μπορεί να γίνει stale, replayed ή inconsistent;
3. Ποιο evidence θα διέψευδε την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά το blast radius;
5. Πώς θα επαναλάβεις το test με ασφάλεια μετά τη remediation?

## Πλήρες αγγλικό μάθημα

[English Module 097](../../English/07-Cloud-Containers-and-Supply-Chain/97-CICD-Build-Provenance-SLSA-12-and-Artifact-Trust.md)

## Συνέχεια

Χρησιμοποίησε **Αναζήτηση μαθημάτων** ή **Διαδρομές μάθησης** από το κύριο menu για τα σχετικά επόμενα θέματα.

---

# Package Managers, Registries, Dependencies και Ecosystem Security

> **Ελληνική έκδοση — Μάθημα 098.** Διατηρούνται οι διεθνείς τεχνικοί όροι όπου είναι ακριβέστεροι και ευκολότεροι στην αναζήτηση.

## Στόχος του μαθήματος

Να κατανοήσεις σε βάθος το **Package Managers, Registries, Dependencies και Ecosystem Security**, να αναγνωρίζεις trust boundaries και failure states και να μπορείς να αποδείξεις ένα συμπέρασμα με ασφαλές, επαναλήψιμο evidence.

> **Όριο εξουσιοδότησης:** Πρακτική μόνο σε συστήματα, λογαριασμούς, κώδικα ή labs που σου ανήκουν ή έχεις ρητή άδεια να ελέγξεις. Προτίμησε localhost, synthetic data και disposable environments.

## Βαθιές τεχνικές έννοιες

### 1. Name and namespace trust

Package name δεν αποδεικνύει maintainer ή intended dependency. Verify official ecosystem/source και προστατεύσου από typo/confusion μεταξύ public/private namespaces.

### 2. Semantic versioning limits

SemVer περιγράφει intended compatibility αλλά δεν εγγυάται security ή πραγματική behavior compatibility. Range constraints μπορεί να φέρουν νέο code χωρίς review.

### 3. Lockfiles

Lockfile καταγράφει resolved versions/integrity και βοηθά reproducibility. Πρέπει να review/update μαζί με manifest και να μην παρακάμπτεται από διαφορετικό resolver mode.

### 4. Install/build scripts

Package install hooks εκτελούν code στο developer/CI environment. Περιορίσε scripts, network, secrets και privileges και προτίμησε isolated build.

### 5. Transitive dependencies

Transitive graph αυξάνει maintainers και code που εμπιστεύεσαι. Inventory, SBOM και dependency minimization βοηθούν να βρεις unused ή unexpectedly privileged packages.

### 6. Maintainer and release trust

Account takeover ή malicious release μπορεί να περάσει μέσω legitimate package name. MFA, signed releases/provenance, review και staged update μειώνουν risk.

### 7. Mirrors and proxies

Enterprise proxy μπορεί να cache/allowlist packages αλλά γίνεται δικό του trust boundary. Protect admin, TLS, metadata integrity, retention και upstream sync behavior.

### 8. Response

Σε compromised dependency χρειάζεσαι affected-version inventory, revoke/replace, rebuild from known-good source, rotate exposed secrets και evidence για deployed artifacts.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Γράψε πρώτα invariant και expected result, άλλαξε μία μεταβλητή κάθε φορά και κράτησε μόνο το evidence που χρειάζεται.

1. **Create a dependency inventory for a small harmless Python project and classify direct vs transitive packages** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
2. **Compare reproducibility with and without a lockfile or fully pinned requirements in an isolated virtual environment** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
3. **Write an incident checklist for a compromised package version: identify exposure, builds, credentials, artifacts, and verification steps** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary και ποιος έχει authority;
2. Ποιο state μπορεί να γίνει stale, replayed ή inconsistent;
3. Ποιο evidence θα διέψευδε την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά το blast radius;
5. Πώς θα επαναλάβεις το test με ασφάλεια μετά τη remediation?

## Πλήρες αγγλικό μάθημα

[English Module 098](../../English/07-Cloud-Containers-and-Supply-Chain/98-Package-Managers-Registries-Dependency-and-Ecosystem-Security.md)

## Συνέχεια

Χρησιμοποίησε **Αναζήτηση μαθημάτων** ή **Διαδρομές μάθησης** από το κύριο menu για τα σχετικά επόμενα θέματα.

---

# Compiler Toolchains, Sanitizers, CFI και Binary Hardening

> **Ελληνική έκδοση — Μάθημα 099.** Διατηρούνται οι διεθνείς τεχνικοί όροι όπου είναι ακριβέστεροι και ευκολότεροι στην αναζήτηση.

## Στόχος του μαθήματος

Να κατανοήσεις σε βάθος το **Compiler Toolchains, Sanitizers, CFI και Binary Hardening**, να αναγνωρίζεις trust boundaries και failure states και να μπορείς να αποδείξεις ένα συμπέρασμα με ασφαλές, επαναλήψιμο evidence.

> **Όριο εξουσιοδότησης:** Πρακτική μόνο σε συστήματα, λογαριασμούς, κώδικα ή labs που σου ανήκουν ή έχεις ρητή άδεια να ελέγξεις. Προτίμησε localhost, synthetic data και disposable environments.

## Βαθιές τεχνικές έννοιες

### 1. Undefined behavior

Σε C/C++ undefined behavior επιτρέπει optimizer να κάνει transformations που δεν ταιριάζουν με intuitive source reasoning. Security review χρειάζεται language rules, compiler/version και actual binary behavior.

### 2. Sanitizers

ASan/UBSan/TSan/MSan και άλλα diagnostics βρίσκουν διαφορετικές bug classes. Χρησιμοποίησέ τα σε tests/fuzzing και αντιμετώπισε report ως root-cause evidence, όχι exploit recipe.

### 3. Stack and object protections

Stack canaries, fortified APIs, safe-stack/object-size checks και hardened allocators δυσκολεύουν ή εντοπίζουν corruption. Δεν αντικαθιστούν memory-safe design και bounds correctness.

### 4. Control-flow integrity

CFI περιορίζει indirect control transfers σε επιτρεπόμενους targets σύμφωνα με type/control model. Coverage εξαρτάται από compiler, LTO, modules και native boundaries.

### 5. Linker hardening

PIE/ASLR support, RELRO, non-executable memory και symbol/link policy επηρεάζουν runtime attack surface. Verify actual binary properties αντί να υποθέτεις flags από build script.

### 6. LTO and optimization

Optimization/LTO αλλάζει inlining, layout και elimination, άρα sanitizer/reproduction behavior. Κράτησε debug symbols/build IDs και reproduce με release-like settings όταν χρειάζεται.

### 7. Toolchain provenance

Compiler/linker/build tools είναι supply-chain inputs. Pin trusted versions, verify provenance και isolate builds ώστε compromised toolchain να μην αλλοιώνει artifacts.

### 8. Regression strategy

Κάθε compiler-detected bug πρέπει να γίνει minimal test που αποτυγχάνει πριν fix και περνά μετά. Run σε relevant architectures/configurations ώστε optimization-dependent bugs να μην επιστρέφουν.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Γράψε πρώτα invariant και expected result, άλλαξε μία μεταβλητή κάθε φορά και κράτησε μόνο το evidence που χρειάζεται.

1. **Compile a harmless toy C program with and without common hardening flags and inspect the resulting binary properties—without developing an exploit** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
2. **Use a sanitizer on intentionally buggy toy code to capture a diagnostic and explain root cause, object lifetime, and fix** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
3. **Create a build-metadata record containing compiler version, flags, source hash, dependency lock, and output digest** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary και ποιος έχει authority;
2. Ποιο state μπορεί να γίνει stale, replayed ή inconsistent;
3. Ποιο evidence θα διέψευδε την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά το blast radius;
5. Πώς θα επαναλάβεις το test με ασφάλεια μετά τη remediation?

## Πλήρες αγγλικό μάθημα

[English Module 099](../../English/03-Systems-Malware-and-Reverse-Engineering/99-Compiler-Toolchains-Sanitizers-CFI-and-Binary-Hardening.md)

## Συνέχεια

Χρησιμοποίησε **Αναζήτηση μαθημάτων** ή **Διαδρομές μάθησης** από το κύριο menu για τα σχετικά επόμενα θέματα.

---

# Cryptographic Protocol Engineering, Key Agreement και State Machines

> **Ελληνική έκδοση — Μάθημα 100.** Διατηρούνται οι διεθνείς τεχνικοί όροι όπου είναι ακριβέστεροι και ευκολότεροι στην αναζήτηση.

## Στόχος του μαθήματος

Να κατανοήσεις σε βάθος το **Cryptographic Protocol Engineering, Key Agreement και State Machines**, να αναγνωρίζεις trust boundaries και failure states και να μπορείς να αποδείξεις ένα συμπέρασμα με ασφαλές, επαναλήψιμο evidence.

> **Όριο εξουσιοδότησης:** Πρακτική μόνο σε συστήματα, λογαριασμούς, κώδικα ή labs που σου ανήκουν ή έχεις ρητή άδεια να ελέγξεις. Προτίμησε localhost, synthetic data και disposable environments.

## Βαθιές τεχνικές έννοιες

### 1. Security goals

Πριν σχεδιάσεις protocol γράψε confidentiality, authenticity, forward secrecy, replay resistance και identity goals. Ασαφής goal οδηγεί σε σωστά primitives συνδεδεμένα με λάθος τρόπο.

### 2. Key agreement

Key agreement δημιουργεί shared secret αλλά πρέπει να authenticate τα σωστά peers και parameters. Unauthenticated agreement προστατεύει από passive observer αλλά όχι από active intermediary.

### 3. Transcript binding

Bind identities, roles, algorithms και exchanged messages στο authenticated transcript ώστε messages από άλλο context/session να μην επαναχρησιμοποιούνται.

### 4. Nonces and sequence numbers

Nonces/challenges δίνουν freshness και sequence numbers ordering/replay state. Ορίσε uniqueness, lifetime, wrap/restart και persistence behavior.

### 5. Key derivation

KDF πρέπει να χωρίζει keys ανά purpose/direction/context και να χρησιμοποιεί κατάλληλο salt/info. Μην επαναχρησιμοποιείς ίδιο key material για unrelated cryptographic operations.

### 6. Algorithm agility

Agility σημαίνει ασφαλές negotiation/migration χωρίς downgrade. Version/algorithm επιλογή πρέπει να authenticated και legacy support να έχει explicit sunset.

### 7. Error handling

Crypto errors μπορούν να διαρρεύσουν state μέσω timing/detail ή να προκαλέσουν unsafe fallback. Uniform failure, bounded retry και clear state reset είναι μέρος του protocol.

### 8. Formal and empirical validation

Formal models βοηθούν state-machine/protocol properties, ενώ test vectors, fuzzing και interoperability βρίσκουν implementation bugs. Χρειάζονται και τα δύο για high-assurance design.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Γράψε πρώτα invariant και expected result, άλλαξε μία μεταβλητή κάθε φορά και κράτησε μόνο το evidence που χρειάζεται.

1. **Design a toy authenticated message protocol on paper and identify where identities, roles, nonces, sequence numbers, and transcript data are bound** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
2. **Create negative test cases for replay, reordered messages, algorithm downgrade, expired credentials, and duplicate session identifiers** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
3. **Compare “encrypted transport” with “end-to-end authenticated message” and list which intermediaries can still read or modify data in each model** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary και ποιος έχει authority;
2. Ποιο state μπορεί να γίνει stale, replayed ή inconsistent;
3. Ποιο evidence θα διέψευδε την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά το blast radius;
5. Πώς θα επαναλάβεις το test με ασφάλεια μετά τη remediation?

## Πλήρες αγγλικό μάθημα

[English Module 100](../../English/06-Identity-Cryptography-and-Trust/100-Cryptographic-Protocol-Engineering-Key-Agreement-and-State-Machines.md)

## Συνέχεια

Χρησιμοποίησε **Αναζήτηση μαθημάτων** ή **Διαδρομές μάθησης** από το κύριο menu για τα σχετικά επόμενα θέματα.

---

# Post-Quantum Migration, Crypto Agility και Hybrid Deployment

> **Ελληνική έκδοση — Μάθημα 101.** Διατηρούνται οι διεθνείς τεχνικοί όροι όπου είναι ακριβέστεροι και ευκολότεροι στην αναζήτηση.

## Στόχος του μαθήματος

Να κατανοήσεις σε βάθος το **Post-Quantum Migration, Crypto Agility και Hybrid Deployment**, να αναγνωρίζεις trust boundaries και failure states και να μπορείς να αποδείξεις ένα συμπέρασμα με ασφαλές, επαναλήψιμο evidence.

> **Όριο εξουσιοδότησης:** Πρακτική μόνο σε συστήματα, λογαριασμούς, κώδικα ή labs που σου ανήκουν ή έχεις ρητή άδεια να ελέγξεις. Προτίμησε localhost, synthetic data και disposable environments.

## Βαθιές τεχνικές έννοιες

### 1. Cryptographic inventory

Migration ξεκινά με inventory algorithms, protocols, certificates, keys, libraries, hardware και data lifetimes. Χωρίς dependency map δεν μπορείς να ξέρεις ποιο σύστημα μπλοκάρει αλλαγή ή ποια δεδομένα χρειάζονται προτεραιότητα.

### 2. Harvest-now risk

Data που κρυπτογραφούνται σήμερα μπορεί να συλλεχθούν και να αποκρυπτογραφηθούν αργότερα αν έχουν μακροχρόνια αξία και εξαρτώνται από public-key schemes που απειλούνται από future quantum capability. Prioritize confidentiality horizon και exposure.

### 3. Standards

Χρησιμοποίησε finalized/recognized post-quantum standards και vendor/platform guidance αντί για home-grown primitives. Algorithm selection είναι μόνο μέρος του migration· interoperability, key sizes και protocol integration είναι εξίσου σημαντικά.

### 4. Crypto agility

Agility σημαίνει ότι algorithms/keys μπορούν να αλλάξουν με versioned policy και authenticated negotiation χωρίς unsafe fallback. Hard-coded assumptions και fixed field sizes κάνουν migration ακριβό.

### 5. Hybrid approaches

Hybrid deployment συνδυάζει classical και post-quantum mechanisms ώστε failure ενός νέου component να μην είναι μοναδικό trust anchor. Η composition πρέπει να ακολουθεί reviewed standards/protocol profiles και να αποφεύγει custom combining logic.

### 6. PKI impact

Certificates, enrollment, HSM/KMS, revocation, chain validation και network appliances μπορεί να έχουν size/algorithm constraints. Test end-to-end PKI workflows και recovery πριν από broad rollout.

### 7. Migration sequencing

Ξεκίνα από inventory και low-risk interoperability labs, μετά dual-support/rotation, service migration και retirement legacy algorithms σύμφωνα με data lifetime και dependency readiness.

### 8. Evidence

Κράτησε algorithm inventory, owners, versions, test vectors, handshake/certificate sizes, latency, failure modes και rollback criteria ώστε η migration να είναι measurable engineering project.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Γράψε πρώτα invariant και expected result, άλλαξε μία μεταβλητή κάθε φορά και κράτησε μόνο το evidence που χρειάζεται.

1. **Build a cryptographic inventory for a small local application and record every library/API that creates or validates keys/signatures** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
2. **Create a compatibility test plan that anticipates larger key/signature objects and handshake messages without claiming unsupported algorithms are production-ready** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
3. **Classify sample data sets by confidentiality lifetime and use that to rank migration priority** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary και ποιος έχει authority;
2. Ποιο state μπορεί να γίνει stale, replayed ή inconsistent;
3. Ποιο evidence θα διέψευδε την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά το blast radius;
5. Πώς θα επαναλάβεις το test με ασφάλεια μετά τη remediation?

## Πλήρες αγγλικό μάθημα

[English Module 101](../../English/06-Identity-Cryptography-and-Trust/101-Post-Quantum-Migration-Crypto-Agility-and-Hybrid-Deployment.md)

## Συνέχεια

Χρησιμοποίησε **Αναζήτηση μαθημάτων** ή **Διαδρομές μάθησης** από το κύριο menu για τα σχετικά επόμενα θέματα.

---

# Side Channels, Timing, Cache, Faults και Physical Leakage

> **Ελληνική έκδοση — Μάθημα 102.** Διατηρούνται οι διεθνείς τεχνικοί όροι όπου είναι ακριβέστεροι και ευκολότεροι στην αναζήτηση.

## Στόχος του μαθήματος

Να κατανοήσεις σε βάθος το **Side Channels, Timing, Cache, Faults και Physical Leakage**, να αναγνωρίζεις trust boundaries και failure states και να μπορείς να αποδείξεις ένα συμπέρασμα με ασφαλές, επαναλήψιμο evidence.

> **Όριο εξουσιοδότησης:** Πρακτική μόνο σε συστήματα, λογαριασμούς, κώδικα ή labs που σου ανήκουν ή έχεις ρητή άδεια να ελέγξεις. Προτίμησε localhost, synthetic data και disposable environments.

## Βαθιές τεχνικές έννοιες

### 1. Side-channel model

Side channel διαρρέει πληροφορία μέσω timing, cache, power, EM, acoustics ή άλλης παρατήρησης αντί από intended output. Threat model πρέπει να ορίζει attacker proximity, measurement quality, repetition και secret lifetime.

### 2. Timing

Secret-dependent branches, memory access ή error paths μπορούν να αλλάζουν latency. Constant-time primitives και protocol-level noise μειώνουν risk, αλλά remote timing χρειάζεται statistical validation και realistic network variance.

### 3. Caches and microarchitecture

Shared caches, predictors και execution resources μπορούν να δημιουργούν measurable contention. Isolation, process/core scheduling, hardware mitigations και constant-time access patterns έχουν διαφορετικό κόστος/coverage.

### 4. Power and EM

Physical measurements μπορούν να συσχετίσουν device activity με secret-dependent computation. Hardware shielding, balanced implementations, masking και restricted physical access αντιμετωπίζουν διαφορετικό μέρος του threat.

### 5. Fault injection

Voltage, clock, EM ή environmental faults μπορούν να προκαλέσουν incorrect computation. Defensive designs χρειάζονται integrity checks, redundant computation όπου δικαιολογείται και fail-safe behavior.

### 6. Remote versus local feasibility

Ένα laboratory side channel δεν σημαίνει αυτόματα realistic remote exploit. Κατέγραψε access, samples, equipment, signal/noise και assumptions πριν αποδώσεις severity.

### 7. Mitigation layers

Compiler/library constant-time code, OS isolation, hardware features, key rotation και rate limits μπορούν να συνδυαστούν. Verify ότι optimization ή future build δεν αφαιρεί critical property.

### 8. Validation

Χρησιμοποίησε synthetic secrets και owned hardware. Συγκέντρωσε statistical evidence και negative controls και απέφυγε extraction πραγματικών credentials ή τρίτων data.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Γράψε πρώτα invariant και expected result, άλλαξε μία μεταβλητή κάθε φορά και κράτησε μόνο το evidence που χρειάζεται.

1. **Write two localhost toy string-comparison functions—one early-exit and one constant-work—and measure timing distributions using random non-secret data** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
2. **Create a threat model for a cryptographic operation in a cloud VM versus an embedded device with physical attacker access** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
3. **Document which side-channel mitigations belong to application code, cryptographic library, OS/hypervisor, hardware, and physical security** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary και ποιος έχει authority;
2. Ποιο state μπορεί να γίνει stale, replayed ή inconsistent;
3. Ποιο evidence θα διέψευδε την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά το blast radius;
5. Πώς θα επαναλάβεις το test με ασφάλεια μετά τη remediation?

## Πλήρες αγγλικό μάθημα

[English Module 102](../../English/06-Identity-Cryptography-and-Trust/102-Side-Channels-Timing-Cache-Faults-and-Physical-Leakage-Models.md)

## Συνέχεια

Χρησιμοποίησε **Αναζήτηση μαθημάτων** ή **Διαδρομές μάθησης** από το κύριο menu για τα σχετικά επόμενα θέματα.

---

# TPM, Secure Boot, Attestation, TEEs και Device Identity

> **Ελληνική έκδοση — Μάθημα 103.** Διατηρούνται οι διεθνείς τεχνικοί όροι όπου είναι ακριβέστεροι και ευκολότεροι στην αναζήτηση.

## Στόχος του μαθήματος

Να κατανοήσεις σε βάθος το **TPM, Secure Boot, Attestation, TEEs και Device Identity**, να αναγνωρίζεις trust boundaries και failure states και να μπορείς να αποδείξεις ένα συμπέρασμα με ασφαλές, επαναλήψιμο evidence.

> **Όριο εξουσιοδότησης:** Πρακτική μόνο σε συστήματα, λογαριασμούς, κώδικα ή labs που σου ανήκουν ή έχεις ρητή άδεια να ελέγξεις. Προτίμησε localhost, synthetic data και disposable environments.

## Βαθιές τεχνικές έννοιες

### 1. Secure Boot

Secure Boot επαληθεύει ότι κάθε boot stage επιτρέπεται από προηγούμενο trusted stage. Key ownership, update policy και recovery mode είναι μέρος του trust chain και όχι μόνο η signature verification.

### 2. Measured boot

Measured boot καταγράφει hashes/configuration σε measurements χωρίς απαραίτητα να μπλοκάρει boot. Το evidence είναι χρήσιμο όταν υπάρχει γνωστό expected state και αξιόπιστος verifier.

### 3. TPM keys

TPM μπορεί να δημιουργεί/seal keys σε platform state και να προστατεύει private operations. Authorization policy, backup/recovery και owner/admin paths καθορίζουν την πραγματική ασφάλεια.

### 4. Attestation

Attestation μεταφέρει signed evidence για measurements/device identity σε verifier. Ο verifier πρέπει να ελέγχει freshness, nonce, expected measurements, certificate chain και policy context.

### 5. TEEs

Trusted Execution Environments απομονώνουν συγκεκριμένο code/data από πιο privileged software υπό συγκεκριμένο threat model. Δεν λύνουν bugs μέσα στο enclave, side channels, availability ή unsafe I/O boundaries.

### 6. Device identity

Hardware-backed device identity μπορεί να δένει enrollment και access με πραγματική συσκευή. Lifecycle χρειάζεται manufacturing provenance, ownership transfer, revocation και replacement.

### 7. Key release

Sealed secret πρέπει να απελευθερώνεται μόνο όταν attested state και identity ικανοποιούν explicit policy. Recovery path δεν πρέπει να γίνει broad bypass της ίδιας policy.

### 8. Lifecycle

Firmware updates, key rollover, motherboard replacement, reset και decommission αλλάζουν measurements/identity. Σχεδίασε transitions πριν το deployment και κράτησε auditable recovery.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Γράψε πρώτα invariant και expected result, άλλαξε μία μεταβλητή κάθε φορά και κράτησε μόνο το evidence που χρειάζεται.

1. **Draw a boot trust chain for a modern laptop or phone using public vendor documentation and distinguish verification from measurement** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
2. **Design an attestation verifier state machine: challenge, evidence, freshness check, identity validation, policy evaluation, decision, logging** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
3. **Create a recovery plan for an application whose encryption key is sealed to hardware state and the motherboard must be replaced** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary και ποιος έχει authority;
2. Ποιο state μπορεί να γίνει stale, replayed ή inconsistent;
3. Ποιο evidence θα διέψευδε την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά το blast radius;
5. Πώς θα επαναλάβεις το test με ασφάλεια μετά τη remediation?

## Πλήρες αγγλικό μάθημα

[English Module 103](../../English/05-Mobile-IoT-and-Hardware/103-TPM-Secure-Boot-Attestation-TEEs-and-Device-Identity.md)

## Συνέχεια

Χρησιμοποίησε **Αναζήτηση μαθημάτων** ή **Διαδρομές μάθησης** από το κύριο menu για τα σχετικά επόμενα θέματα.

---

# Serverless, Edge Workers, Functions και Event-Driven Cloud Security

> **Ελληνική έκδοση — Μάθημα 104.** Διατηρούνται οι διεθνείς τεχνικοί όροι όπου είναι ακριβέστεροι και ευκολότεροι στην αναζήτηση.

## Στόχος του μαθήματος

Να κατανοήσεις σε βάθος το **Serverless, Edge Workers, Functions και Event-Driven Cloud Security**, να αναγνωρίζεις trust boundaries και failure states και να μπορείς να αποδείξεις ένα συμπέρασμα με ασφαλές, επαναλήψιμο evidence.

> **Όριο εξουσιοδότησης:** Πρακτική μόνο σε συστήματα, λογαριασμούς, κώδικα ή labs που σου ανήκουν ή έχεις ρητή άδεια να ελέγξεις. Προτίμησε localhost, synthetic data και disposable environments.

## Βαθιές τεχνικές έννοιες

### 1. Invocation surface

Serverless function μπορεί να ενεργοποιείται από HTTP, queue, storage event, scheduler ή cloud control event. Κάθε trigger χρειάζεται authenticated source, schema validation και resource limits.

### 2. Execution identity

Η function τρέχει με workload identity/service role που συχνά έχει περισσότερα permissions από το request caller. Δώσε least privilege ανά function και μη χρησιμοποιείς ένα shared broad role για όλο το application.

### 3. Event trust

Event payload και metadata είναι untrusted input ακόμη αν έρχονται από cloud service. Validate tenant/resource, event type, version και replay/idempotency state πριν από side effects.

### 4. Ephemeral runtime

Instances είναι short-lived αλλά μπορεί να επαναχρησιμοποιούνται, με `/tmp`, memory ή connections να παραμένουν μεταξύ invocations. Μην υποθέτεις fresh process για secret/data isolation.

### 5. Secrets

Χρησιμοποίησε managed secret/KMS integration και short-lived identity αντί για secrets μέσα σε package ή environment dumps. Limit which function/version can retrieve each secret.

### 6. Dependency packaging

Function packages και layers είναι supply-chain artifacts. Pin/scan dependencies, verify provenance και μην αφήνεις mutable external download να αλλάζει runtime code μετά approval.

### 7. Edge execution

Edge workers τρέχουν κοντά στον user και συχνά χειρίζονται headers, auth, cache και routing. Είναι application boundary και χρειάζονται isolation, versioned deploy και secret restrictions.

### 8. Observability and cost abuse

Rate, duration, concurrency, downstream calls και errors είναι security/cost signals. Budget/quotas και alarms προστατεύουν από resource abuse χωρίς να βασίζονται μόνο σε autoscaling.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Γράψε πρώτα invariant και expected result, άλλαξε μία μεταβλητή κάθε φορά και κράτησε μόνο το evidence που χρειάζεται.

1. **Model one photo-processing function triggered by object storage and identify what prevents another tenant/object path from being processed** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
2. **Write an IAM policy matrix for three functions that each need different storage/database actions** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
3. **Create a replay/idempotency test plan for a harmless event-driven workflow** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary και ποιος έχει authority;
2. Ποιο state μπορεί να γίνει stale, replayed ή inconsistent;
3. Ποιο evidence θα διέψευδε την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά το blast radius;
5. Πώς θα επαναλάβεις το test με ασφάλεια μετά τη remediation?

## Πλήρες αγγλικό μάθημα

[English Module 104](../../English/07-Cloud-Containers-and-Supply-Chain/104-Serverless-Edge-Workers-Functions-and-Event-Driven-Cloud-Security.md)

## Συνέχεια

Χρησιμοποίησε **Αναζήτηση μαθημάτων** ή **Διαδρομές μάθησης** από το κύριο menu για τα σχετικά επόμενα θέματα.

---

# Multi-Cloud, SaaS Federation, Tenant Isolation και Control Planes

> **Ελληνική έκδοση — Μάθημα 105.** Διατηρούνται οι διεθνείς τεχνικοί όροι όπου είναι ακριβέστεροι και ευκολότεροι στην αναζήτηση.

## Στόχος του μαθήματος

Να κατανοήσεις σε βάθος το **Multi-Cloud, SaaS Federation, Tenant Isolation και Control Planes**, να αναγνωρίζεις trust boundaries και failure states και να μπορείς να αποδείξεις ένα συμπέρασμα με ασφαλές, επαναλήψιμο evidence.

> **Όριο εξουσιοδότησης:** Πρακτική μόνο σε συστήματα, λογαριασμούς, κώδικα ή labs που σου ανήκουν ή έχεις ρητή άδεια να ελέγξεις. Προτίμησε localhost, synthetic data και disposable environments.

## Βαθιές τεχνικές έννοιες

### 1. Control versus data plane

Κάθε cloud/SaaS έχει management/control plane και data/workload plane. Compromise admin API μπορεί να αλλάξει policies, keys και logging χωρίς άμεσο data-plane exploit.

### 2. Federation

Enterprise federation συνδέει IdP με cloud/SaaS roles. Validate issuer, audience, tenant, role mapping, MFA/context και lifecycle ώστε identity από λάθος organization να μην παίρνει access.

### 3. Organization hierarchy

Organizations, management groups, folders, accounts/projects και subscriptions κληρονομούν policy διαφορετικά. Review inherited permissions και high-level admins που μπορούν να αλλάξουν πολλά environments.

### 4. SaaS administrators

SaaS global/admin roles συχνά έχουν data export, identity, integration και audit authority. Χρησιμοποίησε separate privileged identities, JIT όπου γίνεται και strong logging.

### 5. Tenant isolation

Provider isolation δεν διορθώνει customer-side misconfiguration. Test synthetic tenant boundaries σε identities, storage, sharing, APIs και integrations.

### 6. Cross-cloud automation

CI/CD, Terraform, brokers και synchronization identities μπορούν να έχουν authority σε πολλά clouds. Narrow federation, short-lived credentials και environment scoping μειώνουν cross-cloud blast radius.

### 7. Policy drift

Different clouds εκφράζουν παρόμοιες controls με διαφορετική semantics. Central policy mapping πρέπει να κρατά provider-specific evidence και να ανιχνεύει drift, όχι να κρύβει διαφορές πίσω από ένα κοινό label.

### 8. Central evidence

Συγκέντρωσε identity, control-plane, data access και configuration logs σε independent location με common correlation schema, αλλά διατήρησε raw provider fields για investigation.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Γράψε πρώτα invariant και expected result, άλλαξε μία μεταβλητή κάθε φορά και κράτησε μόνο το evidence που χρειάζεται.

1. **Create a provider-neutral matrix for identity, admin hierarchy, network policy, key management, audit logs, and public exposure across two hypothetical clouds** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
2. **Model a SaaS marketplace integration and list every permission it could obtain, how it is revoked, and what happens when the employee owner leaves** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
3. **Design a cross-cloud break-glass procedure that avoids one shared permanent super-admin credential** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary και ποιος έχει authority;
2. Ποιο state μπορεί να γίνει stale, replayed ή inconsistent;
3. Ποιο evidence θα διέψευδε την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά το blast radius;
5. Πώς θα επαναλάβεις το test με ασφάλεια μετά τη remediation?

## Πλήρες αγγλικό μάθημα

[English Module 105](../../English/07-Cloud-Containers-and-Supply-Chain/105-Multi-Cloud-SaaS-Federation-Tenant-Isolation-and-Control-Planes.md)

## Συνέχεια

Χρησιμοποίησε **Αναζήτηση μαθημάτων** ή **Διαδρομές μάθησης** από το κύριο menu για τα σχετικά επόμενα θέματα.

---

# Endpoint EDR Internals, Telemetry και Response Architecture

> **Ελληνική έκδοση — Μάθημα 106.** Διατηρούνται οι διεθνείς τεχνικοί όροι όπου είναι ακριβέστεροι και ευκολότεροι στην αναζήτηση.

## Στόχος του μαθήματος

Να κατανοήσεις σε βάθος το **Endpoint EDR Internals, Telemetry και Response Architecture**, να αναγνωρίζεις trust boundaries και failure states και να μπορείς να αποδείξεις ένα συμπέρασμα με ασφαλές, επαναλήψιμο evidence.

> **Όριο εξουσιοδότησης:** Πρακτική μόνο σε συστήματα, λογαριασμούς, κώδικα ή labs που σου ανήκουν ή έχεις ρητή άδεια να ελέγξεις. Προτίμησε localhost, synthetic data και disposable environments.

## Βαθιές τεχνικές έννοιες

### 1. Sensor placement

EDR sensors μπορεί να βλέπουν kernel, process, file, registry, network ή user-space events ανά platform. Κατέγραψε ακριβώς ποια source παράγει κάθε field και ποια blind spots υπάρχουν.

### 2. Process lineage

Parent/child process tree βοηθά να εξηγηθεί execution context αλλά μπορεί να μην αποτυπώνει IPC, service broker, scheduled task ή remote origin. Συνδύασέ το με user/session και event correlation.

### 3. Content versus metadata

Full content αυξάνει privacy/storage risk ενώ metadata έχει λιγότερο context. Collection policy πρέπει να ισορροπεί detection value, minimization, retention και legal requirements.

### 4. Behavioral detections

Behavioral rule πρέπει να ορίζει invariant/sequence και expected benign alternatives. Version, data source και false-positive rationale είναι απαραίτητα για maintainable detection.

### 5. Response actions

Isolate host, kill process, quarantine file ή revoke token είναι state-changing controls. Χρειάζονται authorization, audit, rollback/recovery και προστασία από false-positive blast radius.

### 6. Tamper protection

EDR πρέπει να προστατεύει agent/configuration/update paths από unauthorized change, αλλά admin/recovery channels παραμένουν. Monitor sensor health και policy changes independent από endpoint όπου γίνεται.

### 7. Cloud analytics

Central analytics συσχετίζει endpoints και threat intelligence αλλά γίνεται high-value data/control plane. Restrict analyst/admin roles, exports, API tokens και detection deployment.

### 8. Validation

Χρησιμοποίησε benign simulations ή synthetic events και trace end-to-end sensor→pipeline→rule→alert→response. Failure μπορεί να είναι telemetry gap και όχι rule logic.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Γράψε πρώτα invariant και expected result, άλλαξε μία μεταβλητή κάθε φορά και κράτησε μόνο το evidence που χρειάζεται.

1. **Design an endpoint event schema for process start that includes identity, parent, signer/hash, session, container context, and correlation ID** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
2. **Create a detection test for a harmless unusual child-process pattern using local scripts; document false-positive conditions** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
3. **Write a response decision matrix for isolate host vs revoke session vs terminate process vs observe only** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary και ποιος έχει authority;
2. Ποιο state μπορεί να γίνει stale, replayed ή inconsistent;
3. Ποιο evidence θα διέψευδε την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά το blast radius;
5. Πώς θα επαναλάβεις το test με ασφάλεια μετά τη remediation?

## Πλήρες αγγλικό μάθημα

[English Module 106](../../English/08-Blue-Team-IR-Forensics-and-Resilience/106-Endpoint-EDR-Internals-Telemetry-and-Response-Architecture.md)

## Συνέχεια

Χρησιμοποίησε **Αναζήτηση μαθημάτων** ή **Διαδρομές μάθησης** από το κύριο menu για τα σχετικά επόμενα θέματα.

---

# Threat Emulation, Adversary Simulation και Purple-Team Lab Design

> **Ελληνική έκδοση — Μάθημα 107.** Διατηρούνται οι διεθνείς τεχνικοί όροι όπου είναι ακριβέστεροι και ευκολότεροι στην αναζήτηση.

## Στόχος του μαθήματος

Να κατανοήσεις σε βάθος το **Threat Emulation, Adversary Simulation και Purple-Team Lab Design**, να αναγνωρίζεις trust boundaries και failure states και να μπορείς να αποδείξεις ένα συμπέρασμα με ασφαλές, επαναλήψιμο evidence.

> **Όριο εξουσιοδότησης:** Πρακτική μόνο σε συστήματα, λογαριασμούς, κώδικα ή labs που σου ανήκουν ή έχεις ρητή άδεια να ελέγξεις. Προτίμησε localhost, synthetic data και disposable environments.

## Βαθιές τεχνικές έννοιες

### 1. Objective first

Purple-team test ξεκινά από συγκεκριμένο security/detection objective και όχι από λίστα attacker tools. Γράψε ποια συμπεριφορά θέλεις να δεις, ποια data source πρέπει να την αποτυπώσει και ποιο stop condition υπάρχει.

### 2. Behavior abstraction

Περιέγραψε behavior σε επίπεδο action/effect ώστε να μπορεί να προσομοιωθεί με harmless mechanism. Αυτό επιτρέπει detection validation χωρίς weaponized payload.

### 3. Safety constraints

Scope, production limits, prohibited actions, test accounts, rate και emergency contact πρέπει να είναι γνωστά πριν το execution. Benign marker προτιμάται από πραγματικό credential/data impact.

### 4. ATT&CK mapping

ATT&CK mapping βοηθά κοινή ορολογία αλλά technique ID δεν είναι detection requirement από μόνο του. Δέσε κάθε test με συγκεκριμένο environment behavior και telemetry.

### 5. Detection contract

Για κάθε test γράψε expected events, fields, timestamps, rule/alert και analyst context. Αν λείπει event, ξεχώρισε sensor, pipeline, normalization, rule και routing failure.

### 6. Purple-team loop

Execute harmless behavior, observe, tune control, retest και capture result. Κάθε iteration πρέπει να αφήνει regression fixture ώστε βελτίωση να μην χαθεί.

### 7. Metrics

Χρήσιμα metrics είναι data coverage, alert latency, precision/context completeness και time-to-triage—not απλώς αριθμός techniques “covered”.

### 8. Reporting

Report πρέπει να εξηγεί objective, behavior, evidence, blind spot, remediation και retest. Απόφυγε dramatic attacker narrative που δεν προσθέτει engineering πληροφορία.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Γράψε πρώτα invariant και expected result, άλλαξε μία μεταβλητή κάθε φορά και κράτησε μόνο το evidence που χρειάζεται.

1. **Create a five-test purple-team plan using harmless local behaviors such as file creation, process start, failed login, service restart, and DNS lookup** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
2. **For each test, define ATT&CK mapping only after describing the actual behavior and expected evidence** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
3. **Build a regression sheet that records test version, environment, expected events, alert outcome, and remediation status** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary και ποιος έχει authority;
2. Ποιο state μπορεί να γίνει stale, replayed ή inconsistent;
3. Ποιο evidence θα διέψευδε την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά το blast radius;
5. Πώς θα επαναλάβεις το test με ασφάλεια μετά τη remediation?

## Πλήρες αγγλικό μάθημα

[English Module 107](../../English/08-Blue-Team-IR-Forensics-and-Resilience/107-Threat-Emulation-Adversary-Simulation-and-Purple-Team-Lab-Design.md)

## Συνέχεια

Χρησιμοποίησε **Αναζήτηση μαθημάτων** ή **Διαδρομές μάθησης** από το κύριο menu για τα σχετικά επόμενα θέματα.

---

# Advanced Code Auditing, Static Analysis, Dataflow και Taint Reasoning

> **Ελληνική έκδοση — Μάθημα 108.** Διατηρούνται οι διεθνείς τεχνικοί όροι όπου είναι ακριβέστεροι και ευκολότεροι στην αναζήτηση.

## Στόχος του μαθήματος

Να κατανοήσεις σε βάθος το **Advanced Code Auditing, Static Analysis, Dataflow και Taint Reasoning**, να αναγνωρίζεις trust boundaries και failure states και να μπορείς να αποδείξεις ένα συμπέρασμα με ασφαλές, επαναλήψιμο evidence.

> **Όριο εξουσιοδότησης:** Πρακτική μόνο σε συστήματα, λογαριασμούς, κώδικα ή labs που σου ανήκουν ή έχεις ρητή άδεια να ελέγξεις. Προτίμησε localhost, synthetic data και disposable environments.

## Βαθιές τεχνικές έννοιες

### 1. Sources and sinks

Static analysis ξεκινά από untrusted/privileged data sources και security-sensitive sinks όπως query, file, command, auth decision ή serialization. Trace path και sanitization context αντί να ψάχνεις απλώς dangerous function names.

### 2. Taint analysis

Taint model σημειώνει data που προέρχεται από source και propagation μέχρι sink. Correctness εξαρτάται από accurate sources, sanitizers, aliases και framework semantics.

### 3. Control flow

Branches, exceptions και early returns καθορίζουν αν validation πραγματικά προηγείται του sink. Review dominated paths και error handling, όχι μόνο happy path.

### 4. Interprocedural analysis

Security flow περνά functions/modules/services. Call graphs, summaries και context sensitivity βοηθούν αλλά dynamic dispatch/reflection μπορούν να δημιουργήσουν gaps.

### 5. Stateful bugs

Authorization, races και lifecycle bugs συχνά απαιτούν sequence πολλών requests/events και δεν φαίνονται σε single-function taint. Μοντελοποίησε state machine και transitions.

### 6. Variant analysis

Μετά από root cause, ψάξε άλλα σημεία με ίδιο unsafe pattern ή missing invariant. Variant query πρέπει να βασίζεται στη μηχανική αιτία και όχι στο exact vulnerable string.

### 7. Tool limitations

Static tools έχουν false positives/negatives από framework models, generated code, native interfaces και reflection. Επιβεβαίωσε important findings με source reasoning και safe tests.

### 8. Review output

Καλό audit finding περιέχει source→transform→sink path, required context, impact, root cause, fix και regression test με μικρό evidence.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Γράψε πρώτα invariant και expected result, άλλαξε μία μεταβλητή κάθε φορά και κράτησε μόνο το evidence που χρειάζεται.

1. **Audit a deliberately small local program and draw a source→transform→validation→sink dataflow for one input** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
2. **Write a toy static-analysis rule or grep-like check for one unsafe coding pattern and document its false positives/false negatives** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
3. **Perform variant analysis after fixing one toy bug and search sibling functions for the same root cause** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary και ποιος έχει authority;
2. Ποιο state μπορεί να γίνει stale, replayed ή inconsistent;
3. Ποιο evidence θα διέψευδε την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά το blast radius;
5. Πώς θα επαναλάβεις το test με ασφάλεια μετά τη remediation?

## Πλήρες αγγλικό μάθημα

[English Module 108](../../English/02-Recon-Pentesting-Web-and-AppSec/108-Advanced-Code-Auditing-Static-Analysis-Dataflow-and-Taint-Reasoning.md)

## Συνέχεια

Χρησιμοποίησε **Αναζήτηση μαθημάτων** ή **Διαδρομές μάθησης** από το κύριο menu για τα σχετικά επόμενα θέματα.

---

# Vulnerability Research: Reproduction, Regression και Coordinated Disclosure

> **Ελληνική έκδοση — Μάθημα 109.** Διατηρούνται οι διεθνείς τεχνικοί όροι όπου είναι ακριβέστεροι και ευκολότεροι στην αναζήτηση.

## Στόχος του μαθήματος

Να κατανοήσεις σε βάθος το **Vulnerability Research: Reproduction, Regression και Coordinated Disclosure**, να αναγνωρίζεις trust boundaries και failure states και να μπορείς να αποδείξεις ένα συμπέρασμα με ασφαλές, επαναλήψιμο evidence.

> **Όριο εξουσιοδότησης:** Πρακτική μόνο σε συστήματα, λογαριασμούς, κώδικα ή labs που σου ανήκουν ή έχεις ρητή άδεια να ελέγξεις. Προτίμησε localhost, synthetic data και disposable environments.

## Βαθιές τεχνικές έννοιες

### 1. Reproduction environment

Reproduce vulnerability σε exact/similar version, configuration και architecture με disposable data. Κατέγραψε build IDs και environment assumptions πριν αλλάξεις οτιδήποτε.

### 2. Minimal trigger

Μείωσε input στο μικρότερο sample που προκαλεί bug χωρίς unnecessary impact. Minimal trigger βοηθά root cause, regression και vendor communication.

### 3. Root cause

Ξεχώρισε crash symptom από αρχική invariant violation. Trace first bad state/access/authorization decision και εξήγησε γιατί το program το επέτρεψε.

### 4. Version comparison

Σύγκρινε affected και fixed versions/source/behavior για να βρεις security-relevant change. Patch diff είναι evidence αλλά χρειάζεται runtime/regression validation.

### 5. Severity

Severity εξαρτάται από prerequisites, attacker control, boundary, data/privilege impact, reliability και deployed context. Μην εξισώνεις crash με arbitrary code execution χωρίς proof.

### 6. Regression

Μετατροπή minimal trigger σε automated negative test εμποδίζει επιστροφή της ίδιας root cause. Test πρέπει να αποτυγχάνει στο vulnerable build και να περνά στο fixed.

### 7. Disclosure

Coordinated disclosure χρειάζεται affected versions, concise reproduction, impact, suggested fix και ασφαλές communication channel. Σεβάσου vendor/program scope και embargo όπου συμφωνείται.

### 8. Research ethics

Μην συλλέγεις τρίτων data ή κλιμακώνεις impact για να αποδείξεις severity. Χρησιμοποίησε local copies/synthetic accounts και stop μόλις έχεις sufficient evidence.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Γράψε πρώτα invariant και expected result, άλλαξε μία μεταβλητή κάθε φορά και κράτησε μόνο το evidence που χρειάζεται.

1. **Take a harmless intentionally buggy parser and practice input minimization until only the root-cause trigger remains** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
2. **Compare two local versions of toy source code, identify the security-relevant change, and write a regression test** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
3. **Draft a coordinated-disclosure report for the toy bug including scope, impact, reproduction, root cause, remediation, and timeline** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary και ποιος έχει authority;
2. Ποιο state μπορεί να γίνει stale, replayed ή inconsistent;
3. Ποιο evidence θα διέψευδε την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά το blast radius;
5. Πώς θα επαναλάβεις το test με ασφάλεια μετά τη remediation?

## Πλήρες αγγλικό μάθημα

[English Module 109](../../English/03-Systems-Malware-and-Reverse-Engineering/109-Vulnerability-Research-Reproduction-Regression-and-Coordinated-Disclosure.md)

## Συνέχεια

Χρησιμοποίησε **Αναζήτηση μαθημάτων** ή **Διαδρομές μάθησης** από το κύριο menu για τα σχετικά επόμενα θέματα.

---

# Advanced Authorized Labs II: Systems, Identity, Cloud και Application Security

> **Ελληνική έκδοση — Μάθημα 110.** Διατηρούνται οι διεθνείς τεχνικοί όροι όπου είναι ακριβέστεροι και ευκολότεροι στην αναζήτηση.

## Στόχος του μαθήματος

Να κατανοήσεις σε βάθος το **Advanced Authorized Labs II: Systems, Identity, Cloud και Application Security**, να αναγνωρίζεις trust boundaries και failure states και να μπορείς να αποδείξεις ένα συμπέρασμα με ασφαλές, επαναλήψιμο evidence.

> **Όριο εξουσιοδότησης:** Πρακτική μόνο σε συστήματα, λογαριασμούς, κώδικα ή labs που σου ανήκουν ή έχεις ρητή άδεια να ελέγξεις. Προτίμησε localhost, synthetic data και disposable environments.

## Βαθιές τεχνικές έννοιες

### 1. Lab architecture

Σχεδίασε disposable environment με σαφές network/identity boundary, snapshots και synthetic data. Κάθε lab πρέπει να έχει ένα measurable invariant και όχι γενικό “hack the box”.

### 2. Evidence package

Κράτησε scope, versions, diagram, test input, logs, before/after state, remediation και regression result. Ένα άλλο άτομο πρέπει να μπορεί να επαναλάβει το συμπέρασμα.

### 3. Identity lab

Χρησιμοποίησε synthetic users/roles/tokens και negative authorization matrix. Μέτρησε revocation, session lifetime και audit context χωρίς πραγματικά credentials.

### 4. Web/API lab

Χρησιμοποίησε local intentionally vulnerable app και synthetic records. Focus σε request parsing, object authorization και safe proof αντί σε public targets.

### 5. Linux isolation lab

Χρησιμοποίησε namespaces/container/VM και παρατήρησε capabilities, mounts, network και policy. Verify denied paths και cleanup χωρίς escape attempts σε shared host.

### 6. Supply-chain lab

Build small artifact από pinned source, create provenance/SBOM και verify digest/policy στο deploy simulation. Inject only harmless metadata mismatch to test fail behavior.

### 7. Detection lab

Generate benign event sequence και ακολούθησε sensor→pipeline→alert. Document missing fields και tune regression fixture.

### 8. Forensics lab

Χρησιμοποίησε prepared disk/log/memory artifacts και build timeline. Preserve hashes/time zones και separate observation from inference.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Γράψε πρώτα invariant και expected result, άλλαξε μία μεταβλητή κάθε φορά και κράτησε μόνο το evidence που χρειάζεται.

1. **Complete any four integrated labs and produce one consistent report template across all of them** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
2. **For one lab, intentionally remove a telemetry source and explain what conclusions are no longer supportable** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
3. **For one lab, change the environment version/configuration and verify whether the regression test still proves the same invariant** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary και ποιος έχει authority;
2. Ποιο state μπορεί να γίνει stale, replayed ή inconsistent;
3. Ποιο evidence θα διέψευδε την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά το blast radius;
5. Πώς θα επαναλάβεις το test με ασφάλεια μετά τη remediation?

## Πλήρες αγγλικό μάθημα

[English Module 110](../../English/11-Labs-Capstones-and-Career/110-Advanced-Authorized-Labs-II-Systems-Identity-Cloud-and-Application-Security.md)

## Συνέχεια

Χρησιμοποίησε **Αναζήτηση μαθημάτων** ή **Διαδρομές μάθησης** από το κύριο menu για τα σχετικά επόμενα θέματα.

---

# WebAssembly, JVM, CLR και Ασφάλεια Managed Runtimes

> **Ελληνική έκδοση — Μάθημα 111.** Διατηρούνται οι διεθνείς τεχνικοί όροι όπου είναι ακριβέστεροι και ευκολότεροι στην αναζήτηση.

## Στόχος του μαθήματος

Να κατανοήσεις σε βάθος το **WebAssembly, JVM, CLR και Ασφάλεια Managed Runtimes**, να αναγνωρίζεις trust boundaries και failure states και να μπορείς να αποδείξεις ένα συμπέρασμα με ασφαλές, επαναλήψιμο evidence.

> **Όριο εξουσιοδότησης:** Πρακτική μόνο σε συστήματα, λογαριασμούς, κώδικα ή labs που σου ανήκουν ή έχεις ρητή άδεια να ελέγξεις. Προτίμησε localhost, synthetic data και disposable environments.

## Βαθιές τεχνικές έννοιες

### 1. Bytecode verification

Managed runtimes verify bytecode/type/control constraints πριν execution. Verification μειώνει classes invalid code αλλά runtime libraries, reflection και native interfaces παραμένουν attack surface.

### 2. Memory model

JVM/CLR έχουν managed memory και GC, ενώ WebAssembly έχει linear memory με defined bounds. Logic, resource exhaustion και unsafe native interop μπορούν ακόμη να παραβιάσουν security invariants.

### 3. JIT trust

JIT compiler μετατρέπει untrusted/managed code σε native execution και είναι high-complexity boundary. Updates, sandbox policy και reduction of dynamic features περιορίζουν risk.

### 4. Reflection and dynamic loading

Reflection, plugins και dynamic class loading μπορούν να παρακάμψουν static assumptions. Restrict sources, signing/provenance και which privileged APIs loaded code can reach.

### 5. Deserialization

Managed object serialization μπορεί να καλέσει type-specific behavior. Προτίμησε data-only schemas, allowlists και explicit mapping αντί για arbitrary object reconstruction.

### 6. WebAssembly imports

Wasm module αποκτά authority κυρίως από host imports/capabilities. Minimal imports και resource limits είναι ουσιαστικότερα από την υπόθεση ότι Wasm “είναι sandbox”.

### 7. Native interfaces

JNI/PInvoke/FFI και native modules ξαναφέρνουν memory safety και OS privilege boundaries. Treat them as separate high-risk components με narrow API.

### 8. Sandbox verification

Test actual filesystem/network/clock/process imports, memory limits και escape boundaries με benign negative cases και version-specific evidence.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Γράψε πρώτα invariant και expected result, άλλαξε μία μεταβλητή κάθε φορά και κράτησε μόνο το evidence που χρειάζεται.

1. **Create a harmless local Wasm or managed-language hello-world and document every capability the runtime exposes to it** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
2. **Build a safe deserialization threat model comparing plain JSON DTO parsing with native object deserialization** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
3. **Inventory native/FFI dependencies in a small managed application and classify why each trust-boundary crossing exists** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary και ποιος έχει authority;
2. Ποιο state μπορεί να γίνει stale, replayed ή inconsistent;
3. Ποιο evidence θα διέψευδε την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά το blast radius;
5. Πώς θα επαναλάβεις το test με ασφάλεια μετά τη remediation?

## Πλήρες αγγλικό μάθημα

[English Module 111](../../English/03-Systems-Malware-and-Reverse-Engineering/111-WebAssembly-JVM-CLR-and-Managed-Runtime-Security.md)

## Συνέχεια

Χρησιμοποίησε **Αναζήτηση μαθημάτων** ή **Διαδρομές μάθησης** από το κύριο menu για τα σχετικά επόμενα θέματα.

---

# Browser Extensions, Electron και Desktop Web Runtime Security

> **Ελληνική έκδοση — Μάθημα 112.** Διατηρούνται οι διεθνείς τεχνικοί όροι όπου είναι ακριβέστεροι και ευκολότεροι στην αναζήτηση.

## Στόχος του μαθήματος

Να κατανοήσεις σε βάθος το **Browser Extensions, Electron και Desktop Web Runtime Security**, να αναγνωρίζεις trust boundaries και failure states και να μπορείς να αποδείξεις ένα συμπέρασμα με ασφαλές, επαναλήψιμο evidence.

> **Όριο εξουσιοδότησης:** Πρακτική μόνο σε συστήματα, λογαριασμούς, κώδικα ή labs που σου ανήκουν ή έχεις ρητή άδεια να ελέγξεις. Προτίμησε localhost, synthetic data και disposable environments.

## Βαθιές τεχνικές έννοιες

### 1. Extension permissions

Browser extension permissions και host access δηλώνουν broad authority πάνω σε tabs, pages, storage ή network. Ζήτα minimum permissions και review runtime/optional grants.

### 2. Content scripts

Content scripts τρέχουν κοντά σε untrusted web content και επικοινωνούν με privileged extension context. Validate every message/origin and never trust DOM data as authorization.

### 3. Extension CSP

Extension CSP περιορίζει executable sources αλλά δεν διορθώνει overly privileged APIs ή unsafe message handling. Avoid remote code and dynamic evaluation where platform policy το απαγορεύει.

### 4. Electron isolation

Electron apps συνδυάζουν web renderer με desktop capabilities. Context isolation, sandboxing και disabled Node integration σε untrusted renderer μειώνουν bridge προς OS.

### 5. IPC authorization

Renderer→main IPC είναι privileged broker boundary. Use explicit channel allowlist, validate sender/window/origin/context και parameters και μην εκθέτεις generic “execute” helpers.

### 6. Update trust

Extension/Electron update pipeline μπορεί να αλλάξει privileged code σε πολλούς users. Signing, store/release identity, provenance, rollback και admin access είναι high-value controls.

### 7. Remote content

Loading remote/untrusted content μέσα σε privileged desktop context αυξάνει XSS→native impact. Διαχώρισε remote UI από privileged APIs και enforce navigation/new-window policy.

### 8. Secrets and local data

Desktop apps έχουν access σε files, tokens, caches και keychain. Minimize local secrets, use OS protected storage και avoid leaking sensitive data σε renderer logs/devtools.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Γράψε πρώτα invariant και expected result, άλλαξε μία μεταβλητή κάθε φορά και κράτησε μόνο το evidence που χρειάζεται.

1. **Review the manifest/permissions of an extension you own or a sample extension and justify each requested permission** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
2. **Design an Electron IPC API with three narrowly scoped operations instead of one generic privileged operation** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
3. **Create a trust-boundary diagram for page → content script → extension worker → native helper and list validation required at each edge** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary και ποιος έχει authority;
2. Ποιο state μπορεί να γίνει stale, replayed ή inconsistent;
3. Ποιο evidence θα διέψευδε την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά το blast radius;
5. Πώς θα επαναλάβεις το test με ασφάλεια μετά τη remediation?

## Πλήρες αγγλικό μάθημα

[English Module 112](../../English/03-Systems-Malware-and-Reverse-Engineering/112-Browser-Extensions-Electron-and-Desktop-Web-Runtime-Security.md)

## Συνέχεια

Χρησιμοποίησε **Αναζήτηση μαθημάτων** ή **Διαδρομές μάθησης** από το κύριο menu για τα σχετικά επόμενα θέματα.

---

# Workload Identity, SPIFFE/SPIRE, mTLS και Zero-Trust Service Identity

> **Ελληνική έκδοση — Μάθημα 113.** Διατηρούνται οι διεθνείς τεχνικοί όροι όπου είναι ακριβέστεροι και ευκολότεροι στην αναζήτηση.

## Στόχος του μαθήματος

Να κατανοήσεις σε βάθος το **Workload Identity, SPIFFE/SPIRE, mTLS και Zero-Trust Service Identity**, να αναγνωρίζεις trust boundaries και failure states και να μπορείς να αποδείξεις ένα συμπέρασμα με ασφαλές, επαναλήψιμο evidence.

> **Όριο εξουσιοδότησης:** Πρακτική μόνο σε συστήματα, λογαριασμούς, κώδικα ή labs που σου ανήκουν ή έχεις ρητή άδεια να ελέγξεις. Προτίμησε localhost, synthetic data και disposable environments.

## Βαθιές τεχνικές έννοιες

### 1. Workload identity

Service-to-service authorization χρειάζεται identity για workload instance και όχι shared static password. Identity πρέπει να παράγεται από attested workload/platform context και να είναι short-lived.

### 2. SPIFFE IDs

SPIFFE ID είναι structured URI identity μέσα σε trust domain. Policy πρέπει να δένει ID με συγκεκριμένο workload/service role και να αποφεύγει broad wildcard trust.

### 3. Attestation

SPIRE-style node/workload attestation αποφασίζει ποιο runtime μπορεί να λάβει identity. Protect registration selectors και attestor/admin plane γιατί ορίζουν ποιος “είναι” κάθε service.

### 4. Short-lived credentials

Frequent automatic rotation μειώνει credential theft window. Issuance, clock, cache και outage behavior πρέπει να λειτουργούν χωρίς fallback σε long-lived secret.

### 5. mTLS

mTLS αυθεντικοποιεί endpoints και encrypts transport. Application/service authorization πρέπει ακόμη να ελέγχει source identity, destination/action και tenant/context.

### 6. Trust domains

Trust domain είναι administrative security boundary. Federation μεταξύ domains χρειάζεται explicit bundles/policy και δεν πρέπει να μετατρέπει κάθε identity του άλλου domain σε trusted caller.

### 7. Rotation and revocation

Short lifetime είναι βασικό revocation mechanism αλλά emergency distrust μπορεί να χρειάζεται bundle/registration change. Measure propagation και stale sessions.

### 8. Policy and telemetry

Logs πρέπει να δείχνουν source workload identity, destination, policy/version και result. Correlate issuance και use ώστε compromised identity να traceable.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Γράψε πρώτα invariant και expected result, άλλαξε μία μεταβλητή κάθε φορά και κράτησε μόνο το evidence που χρειάζεται.

1. **Design a three-service toy architecture using short-lived workload identities and write an allow matrix for service-to-service calls** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
2. **Model what changes when one node is considered untrusted: which credentials expire, what should be denied, and what evidence is needed** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
3. **Compare static API keys, cloud workload federation, and SPIFFE-style identities across rotation, attribution, and blast radius** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary και ποιος έχει authority;
2. Ποιο state μπορεί να γίνει stale, replayed ή inconsistent;
3. Ποιο evidence θα διέψευδε την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά το blast radius;
5. Πώς θα επαναλάβεις το test με ασφάλεια μετά τη remediation?

## Πλήρες αγγλικό μάθημα

[English Module 113](../../English/06-Identity-Cryptography-and-Trust/113-Workload-Identity-SPIFFE-SPIRE-mTLS-and-Zero-Trust-Service-Identity.md)

## Συνέχεια

Χρησιμοποίησε **Αναζήτηση μαθημάτων** ή **Διαδρομές μάθησης** από το κύριο menu για τα σχετικά επόμενα θέματα.

---

# Data Security, DLP, Tokenization, Privacy Engineering και Data Lifecycle

> **Ελληνική έκδοση — Μάθημα 114.** Διατηρούνται οι διεθνείς τεχνικοί όροι όπου είναι ακριβέστεροι και ευκολότεροι στην αναζήτηση.

## Στόχος του μαθήματος

Να κατανοήσεις σε βάθος το **Data Security, DLP, Tokenization, Privacy Engineering και Data Lifecycle**, να αναγνωρίζεις trust boundaries και failure states και να μπορείς να αποδείξεις ένα συμπέρασμα με ασφαλές, επαναλήψιμο evidence.

> **Όριο εξουσιοδότησης:** Πρακτική μόνο σε συστήματα, λογαριασμούς, κώδικα ή labs που σου ανήκουν ή έχεις ρητή άδεια να ελέγξεις. Προτίμησε localhost, synthetic data και disposable environments.

## Βαθιές τεχνικές έννοιες

### 1. Data inventory

Δεν μπορείς να προστατεύσεις data που δεν γνωρίζεις. Inventory πρέπει να συνδέει dataset/field με owner, classification, location, copies, consumers, retention και legal/business purpose.

### 2. Minimization

Συλλογή και retention μόνο των αναγκαίων data μειώνει breach impact και compliance burden. Minimize fields, precision, lifetime και number of systems that receive copies.

### 3. Classification

Classification οδηγεί controls για access, encryption, sharing και retention. Το label πρέπει να ακολουθεί derivatives/exports και να μην βασίζεται μόνο σε folder name.

### 4. Tokenization

Tokenization αντικαθιστά sensitive values με reference/token και κρατά mapping σε πιο protected service. Threat model περιλαμβάνει token service authority, reversibility και where plaintext reappears.

### 5. DLP

DLP rules χρησιμοποιούν content/context/labels για detect or restrict movement. Χρειάζονται tuning, privacy safeguards και business workflow ώστε users να μην τα παρακάμπτουν συστηματικά.

### 6. Analytics and AI

Training/analytics/RAG δημιουργούν derived copies, embeddings, logs και exports. Apply purpose limitation, tenant isolation, provenance και deletion handling σε αυτά τα derivatives.

### 7. Deletion

Deletion είναι distributed lifecycle: primary, caches, backups, search indexes και downstream processors έχουν διαφορετικό timing. Define verifiable deletion/expiry and exceptions.

### 8. Privacy engineering

Threat modeling πρέπει να καλύπτει linkability, inference, re-identification και misuse από legitimate insiders—not μόνο external breach. Use least data and least authority by design.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Γράψε πρώτα invariant και expected result, άλλαξε μία μεταβλητή κάθε φορά και κράτησε μόνο το evidence που χρειάζεται.

1. **Build a data-flow map for a hypothetical signup form from browser to API, database, analytics, logs, backups, and support tools** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
2. **Replace one sensitive identifier in the design with a tokenization service and analyze the new trust boundary** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
3. **Create a retention/deletion matrix listing primary data, caches, logs, backups, exports, and derived analytics** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary και ποιος έχει authority;
2. Ποιο state μπορεί να γίνει stale, replayed ή inconsistent;
3. Ποιο evidence θα διέψευδε την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά το blast radius;
5. Πώς θα επαναλάβεις το test με ασφάλεια μετά τη remediation?

## Πλήρες αγγλικό μάθημα

[English Module 114](../../English/09-AI-GRC-Privacy-Data-and-Human-Security/114-Data-Security-DLP-Tokenization-Privacy-Engineering-and-Data-Lifecycle.md)

## Συνέχεια

Χρησιμοποίησε **Αναζήτηση μαθημάτων** ή **Διαδρομές μάθησης** από το κύριο menu για τα σχετικά επόμενα θέματα.

---

# Master Capstones, Research Portfolio και Deep Security Practice

> **Ελληνική έκδοση — Μάθημα 115.** Διατηρούνται οι διεθνείς τεχνικοί όροι όπου είναι ακριβέστεροι και ευκολότεροι στην αναζήτηση.

## Στόχος του μαθήματος

Να κατανοήσεις σε βάθος το **Master Capstones, Research Portfolio και Deep Security Practice**, να αναγνωρίζεις trust boundaries και failure states και να μπορείς να αποδείξεις ένα συμπέρασμα με ασφαλές, επαναλήψιμο evidence.

> **Όριο εξουσιοδότησης:** Πρακτική μόνο σε συστήματα, λογαριασμούς, κώδικα ή labs που σου ανήκουν ή έχεις ρητή άδεια να ελέγξεις. Προτίμησε localhost, synthetic data και disposable environments.

## Βαθιές τεχνικές έννοιες

### 1. Capstone standard

Capstone πρέπει να έχει σαφές question, scope, architecture, evidence, safe lab, root cause/control και regression/retest. Tool screenshots χωρίς reasoning δεν αρκούν.

### 2. Systems capstone

Επίλεξε owned OS/runtime και αξιολόγησε isolation, identity, memory/runtime hardening και telemetry. Deliverable να συνδέει low-level mechanism με defensive configuration.

### 3. Application capstone

Χτίσε/χρησιμοποίησε local app με synthetic users και κάνε threat model, authorization matrix, input-flow review, findings και fixes με tests.

### 4. Cloud/supply-chain capstone

Δημιούργησε disposable cloud/build pipeline, least-privilege workload identity, provenance/SBOM και policy verification. Include recovery/rotation scenario.

### 5. Detection/forensics capstone

Χρησιμοποίησε benign incident dataset, γράψε detection hypothesis, collect logs, timeline, triage, root cause και regression rule with false-positive notes.

### 6. Research capstone

Αναπαράγαγε bug σε toy/open lab, minimize trigger, explain root cause και produce coordinated-disclosure style report χωρίς weaponization.

### 7. Writing quality

Report πρέπει να ξεχωρίζει observation/inference, να δηλώνει limitations και να έχει enough evidence για independent reproduction. Clear diagrams και concise findings είναι technical skill.

### 8. Portfolio hygiene

Αφαίρεσε secrets, πραγματικά identifiers και third-party data. Δημοσίευσε μόνο labs που έχεις δικαίωμα να μοιραστείς και περιέγραψε ethics/scope μαζί με το technical αποτέλεσμα.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Γράψε πρώτα invariant και expected result, άλλαξε μία μεταβλητή κάθε φορά και κράτησε μόνο το evidence που χρειάζεται.

1. **Complete one capstone from systems/application/cloud/detection/research and have another person reproduce the result from your documentation** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
2. **Create a portfolio index that links each project to the skills and security invariants demonstrated** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
3. **Revisit an early guide lab and redo it using the advanced evidence standard; compare the quality of the old and new conclusions** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary και ποιος έχει authority;
2. Ποιο state μπορεί να γίνει stale, replayed ή inconsistent;
3. Ποιο evidence θα διέψευδε την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά το blast radius;
5. Πώς θα επαναλάβεις το test με ασφάλεια μετά τη remediation?

## Πλήρες αγγλικό μάθημα

[English Module 115](../../English/11-Labs-Capstones-and-Career/115-Master-Capstones-Research-Portfolio-and-Deep-Security-Practice.md)

## Συνέχεια

Χρησιμοποίησε **Αναζήτηση μαθημάτων** ή **Διαδρομές μάθησης** από το κύριο menu για τα σχετικά επόμενα θέματα.

---

# Heap Allocators, Object Lifetimes και Memory Debugging

> **Ελληνική έκδοση — Μάθημα 116.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands παραμένουν στα Αγγλικά όπου αυτό αυξάνει την ακρίβεια.

Μελέτησε πώς οργανώνεται το heap, πώς εμφανίζονται lifetime bugs και πώς sanitizers/diagnostic allocators βοηθούν να εντοπίσεις το αρχικό root cause χωρίς weaponization.

> **Όριο εξουσιοδοτημένης χρήσης:** Κάνε πρακτικές δοκιμές μόνο σε συστήματα, κώδικα, λογαριασμούς, captures και lab environments που σου ανήκουν ή για τα οποία έχεις ρητή άδεια. Προτίμησε localhost, synthetic data, disposable VMs/containers και read-only analysis.

## Μαθησιακοί στόχοι

Στο τέλος πρέπει να μπορείς να:

- εξηγήσεις το **allocator metadata and arenas** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **size classes, bins and caches** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **allocation/free lifecycle** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **use-after-free and stale references** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **double-free and ownership confusion** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **heap fragmentation and determinism** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Όρισε ownership/identity, state transition, trust boundary και το ελάχιστο evidence που χρειάζεται για ασφαλή validation.

## Βαθιές τεχνικές έννοιες

### 1. allocator metadata και arenas

Οι heap allocators κρατούν metadata που αντιστοιχούν allocations σε πραγματική μνήμη. Corruption σε arenas ή bookkeeping μπορεί να εμφανιστεί πολύ αργότερα από το αρχικό bug, γι’ αυτό το evidence πρέπει να περιλαμβάνει allocation/free stacks και allocator configuration.

### 2. size classes, bins και caches

Οι allocators ομαδοποιούν chunks ανά μέγεθος και χρησιμοποιούν caches για απόδοση. Αυτό αλλάζει το πότε επαναχρησιμοποιείται freed memory και εξηγεί γιατί το ίδιο lifetime bug μπορεί να είναι σταθερό σε ένα build και intermittent σε άλλο.

### 3. allocation/free lifecycle

Κάθε object έχει lifecycle: allocation, initialization, publication, χρήση, ownership transfer, retirement και free. Κατέγραψε ποιος είναι owner σε κάθε φάση και ποια references πρέπει να ακυρώνονται όταν τελειώνει η ζωή του object.

### 4. use-after-free και stale references

Use-after-free σημαίνει ότι κώδικας χρησιμοποιεί reference αφού το object έχει απελευθερωθεί. Σε ασφαλές research χρησιμοποίησε toy program και sanitizer ώστε να βρεις το πρώτο invalid access και την πραγματική ownership αστοχία.

### 5. double-free και ownership confusion

Double-free συνήθως δείχνει ότι δύο paths πιστεύουν ότι είναι υπεύθυνα για το ίδιο cleanup. Έλεγξε error paths, reference counting και shared ownership ώστε μία μόνο component να εκτελεί final destruction.

### 6. heap fragmentation και determinism

Fragmentation και allocator state επηρεάζουν τη θέση μελλοντικών allocations. Μην θεωρείς σταθερά addresses ή layout από ένα run· σύγκρινε επαναλήψιμα allocation traces και versions.

### 7. guard allocators και quarantine

Guard pages, quarantine και delayed reuse κάνουν invalid access να αποτυγχάνει νωρίτερα και πιο κοντά στη ρίζα του bug. Είναι diagnostic hardening με κόστος σε memory/performance, όχι από μόνο του διόρθωση του ownership model.

### 8. ASan, GWP-ASan και heap diagnostics

ASan και sampled diagnostics όπως GWP-ASan μπορούν να δείξουν out-of-bounds και lifetime violations. Επιβεβαίωσε first bad access, allocation/free stack, build flags και ότι το finding εξαφανίζεται μετά το code fix.

## Engineering focus

Μετέτρεψε κάθε σημαντικό claim σε security invariant και regression test. Προτίμησε controls που μειώνουν authority, κάνουν explicit το state και αφήνουν αρκετή telemetry για root-cause analysis.

## Μοτίβα αστοχίας

- **Confused deputy:** privileged component ενεργεί για caller χωρίς επαρκή έλεγχο authority/context.
- **Identity/context confusion:** issuer, subject, tenant, role, origin, audience ή resource χρησιμοποιείται σε λάθος security context.
- **State/replay failure:** valid state γίνεται δεκτό όταν είναι stale, duplicated, revoked, reordered ή σε λάθος workflow step.
- **Parser mismatch:** δύο layers ερμηνεύουν διαφορετικά το ίδιο input/configuration.
- **Excess authority:** service, process, token, key ή admin role έχει περισσότερα permissions από όσα χρειάζεται.
- **Telemetry gap:** δεν καταγράφεται αρκετό actor/resource/policy/result context ώστε να γίνει αξιόπιστο investigation.

## Αμυντικό checklist

1. Γράψε το security invariant πριν από το test.
2. Μείωσε permissions/capabilities και lifetime όσο γίνεται.
3. Κάνε validation στο component που παίρνει την τελική security απόφαση.
4. Δέσε identity/state με σωστό tenant, resource, audience, origin ή protocol phase.
5. Βάλε explicit schemas, allowlists, resource limits και ασφαλή failure behavior.
6. Κατέγραψε actor, resource, operation, policy/version και result χωρίς secrets.
7. Προετοίμασε rollback/recovery πριν από state-changing lab.

## Καθοδηγούμενο εργαστήριο

### Lab 1 — Build a tiny local C/C++ program with intentionally incorrect lifetime handling and observe it under a sanitizer.


### Lab 2 — Draw an allocation timeline that marks ownership transfer, free, stale reference and crash evidence.


### Lab 3 — Compare the same safe toy bug with and without allocator diagnostics enabled.

Για κάθε lab χρησιμοποίησε owned/synthetic inputs και κράτησε objective, scope, version, expected/observed behavior, cleanup, remediation και regression result σύμφωνα με τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md).

## Evidence που αξίζει να κρατήσεις

- version/build και σχετικό configuration χωρίς secrets,
- μικρό διάγραμμα trust boundaries και data/state flow,
- sanitized logs, traces ή packet metadata,
- ακριβές test input με synthetic values,
- before/after αποτέλεσμα remediation,
- limitations και μη ελεγμένες υποθέσεις.

## Συχνά λάθη

- Αντιγραφή command χωρίς κατανόηση του mechanism.
- Χρήση production/τρίτου συστήματος ενώ αρκεί localhost ή synthetic data.
- Σύγχυση authentication με authorization, encryption με trust ή signature με safety.
- Θεώρηση ενός alert ως οριστικής απόδειξης.
- Παράβλεψη version, timing, identity context, parser behavior ή recovery.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary;
2. Ποιο state/identity μπορεί να γίνει stale ή να χρησιμοποιηθεί σε λάθος context;
3. Ποιο evidence θα σε έκανε να απορρίψεις την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά authority/blast radius;
5. Πώς θα κάνεις ασφαλές retest μετά τη remediation;

## Πλήρες αγγλικό μάθημα

[English Module 116](../../English/03-Systems-Malware-and-Reverse-Engineering/116-Heap-Allocators-Object-Lifetimes-and-Memory-Debugging.md)

## Επόμενα μαθήματα

Σχετικά modules: **053, 065, 066, 068, 099, 109**. Από το κύριο menu επίλεξε **Αναζήτηση μαθημάτων** για να βρεις σχετικά θέματα σε όλο το project.

---

# Concurrency, Race Conditions, TOCTOU και Atomicity

> **Ελληνική έκδοση — Μάθημα 117.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands παραμένουν στα Αγγλικά όπου αυτό αυξάνει την ακρίβεια.

Οι race conditions είναι σφάλματα χρόνου και state. Το μάθημα εξηγεί interleavings, atomicity, TOCTOU, locks και ασφαλή reproducibility σε local labs.

> **Όριο εξουσιοδοτημένης χρήσης:** Κάνε πρακτικές δοκιμές μόνο σε συστήματα, κώδικα, λογαριασμούς, captures και lab environments που σου ανήκουν ή για τα οποία έχεις ρητή άδεια. Προτίμησε localhost, synthetic data, disposable VMs/containers και read-only analysis.

## Μαθησιακοί στόχοι

Στο τέλος πρέπει να μπορείς να:

- εξηγήσεις το **threads, tasks and interleavings** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **shared mutable state** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **check-then-act races** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **TOCTOU across filesystem and IPC boundaries** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **atomic operations and memory ordering** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **locks, deadlocks and lock granularity** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Όρισε ownership/identity, state transition, trust boundary και το ελάχιστο evidence που χρειάζεται για ασφαλή validation.

## Βαθιές τεχνικές έννοιες

### 1. threads, tasks και interleavings

Concurrent code έχει πολλές νόμιμες σειρές εκτέλεσης. Ένα security invariant πρέπει να ισχύει σε κάθε επιτρεπτό interleaving και όχι μόνο στο timing που είδες μία φορά.

### 2. shared mutable state

Shared mutable state χρειάζεται ξεκάθαρο ownership και synchronization model. Σημείωσε τι είναι atomic, τι προστατεύεται από lock/transaction και αν readers μπορούν να δουν partial update.

### 3. check-then-act races

Σε check-then-act race η κατάσταση ελέγχεται και αργότερα χρησιμοποιείται αφού άλλος actor μπορεί να την αλλάξει. Προτίμησε atomic operation ή revalidation στο ίδιο authority boundary όπου γίνεται η τελική πράξη.

### 4. TOCTOU σε filesystem και IPC

Paths, handles και IPC state μπορούν να αλλάξουν μεταξύ check και use. Stable handles, descriptor-based APIs, immutable identifiers και server-side revalidation μειώνουν την εξάρτηση από mutable names.

### 5. atomic operations και memory ordering

Atomic δεν σημαίνει ότι ολόκληρο multi-step protocol είναι σωστό. Memory ordering καθορίζει πότε writes γίνονται ορατά σε άλλα threads, επομένως κατέγραψε το synchronization relation αντί να βασίζεσαι στο timing ενός CPU.

### 6. locks, deadlocks και granularity

Locks προσθέτουν ordering και liveness requirements. Χρησιμοποίησε lock hierarchy, μικρά critical sections και έλεγξε timeout/error paths ώστε security cleanup να μην παρακάμπτεται σε contention.

### 7. idempotency και distributed races

Distributed requests μπορεί να καθυστερήσουν, να επαναληφθούν ή να φτάσουν εκτός σειράς. Idempotency keys, versions, transactions και compare-and-swap βοηθούν να παραμένει σωστό το state σε retries και races.

### 8. stress tests και race detectors

Race detectors και controlled stress κάνουν timing bugs πιο επαναλήψιμα. Κράτα seed, build, workload και trace ώστε η remediation να μπορεί να γίνει regression-tested.

## Engineering focus

Μετέτρεψε κάθε σημαντικό claim σε security invariant και regression test. Προτίμησε controls που μειώνουν authority, κάνουν explicit το state και αφήνουν αρκετή telemetry για root-cause analysis.

## Μοτίβα αστοχίας

- **Confused deputy:** privileged component ενεργεί για caller χωρίς επαρκή έλεγχο authority/context.
- **Identity/context confusion:** issuer, subject, tenant, role, origin, audience ή resource χρησιμοποιείται σε λάθος security context.
- **State/replay failure:** valid state γίνεται δεκτό όταν είναι stale, duplicated, revoked, reordered ή σε λάθος workflow step.
- **Parser mismatch:** δύο layers ερμηνεύουν διαφορετικά το ίδιο input/configuration.
- **Excess authority:** service, process, token, key ή admin role έχει περισσότερα permissions από όσα χρειάζεται.
- **Telemetry gap:** δεν καταγράφεται αρκετό actor/resource/policy/result context ώστε να γίνει αξιόπιστο investigation.

## Αμυντικό checklist

1. Γράψε το security invariant πριν από το test.
2. Μείωσε permissions/capabilities και lifetime όσο γίνεται.
3. Κάνε validation στο component που παίρνει την τελική security απόφαση.
4. Δέσε identity/state με σωστό tenant, resource, audience, origin ή protocol phase.
5. Βάλε explicit schemas, allowlists, resource limits και ασφαλή failure behavior.
6. Κατέγραψε actor, resource, operation, policy/version και result χωρίς secrets.
7. Προετοίμασε rollback/recovery πριν από state-changing lab.

## Καθοδηγούμενο εργαστήριο

### Lab 1 — Create a local counter/update race in a toy program and record inconsistent outcomes.


### Lab 2 — Model a safe file-check/file-open example using temporary files you own, then redesign it around safer handles or atomic primitives.


### Lab 3 — Write invariants for a payment-like state machine and test duplicate/reordered events without real transactions.

Για κάθε lab χρησιμοποίησε owned/synthetic inputs και κράτησε objective, scope, version, expected/observed behavior, cleanup, remediation και regression result σύμφωνα με τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md).

## Evidence που αξίζει να κρατήσεις

- version/build και σχετικό configuration χωρίς secrets,
- μικρό διάγραμμα trust boundaries και data/state flow,
- sanitized logs, traces ή packet metadata,
- ακριβές test input με synthetic values,
- before/after αποτέλεσμα remediation,
- limitations και μη ελεγμένες υποθέσεις.

## Συχνά λάθη

- Αντιγραφή command χωρίς κατανόηση του mechanism.
- Χρήση production/τρίτου συστήματος ενώ αρκεί localhost ή synthetic data.
- Σύγχυση authentication με authorization, encryption με trust ή signature με safety.
- Θεώρηση ενός alert ως οριστικής απόδειξης.
- Παράβλεψη version, timing, identity context, parser behavior ή recovery.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary;
2. Ποιο state/identity μπορεί να γίνει stale ή να χρησιμοποιηθεί σε λάθος context;
3. Ποιο evidence θα σε έκανε να απορρίψεις την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά authority/blast radius;
5. Πώς θα κάνεις ασφαλές retest μετά τη remediation;

## Πλήρες αγγλικό μάθημα

[English Module 117](../../English/03-Systems-Malware-and-Reverse-Engineering/117-Concurrency-Race-Conditions-TOCTOU-and-Atomicity.md)

## Επόμενα μαθήματα

Σχετικά modules: **041, 065, 071, 084, 091, 095**. Από το κύριο menu επίλεξε **Αναζήτηση μαθημάτων** για να βρεις σχετικά θέματα σε όλο το project.

---

# IPC, RPC, D-Bus, COM και Local Trust Boundaries

> **Ελληνική έκδοση — Μάθημα 118.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands παραμένουν στα Αγγλικά όπου αυτό αυξάνει την ακρίβεια.

Το IPC είναι trust boundary ακόμη και στον ίδιο host. Εστίασε σε caller identity, authorization, marshalling, brokers και confused-deputy risks.

> **Όριο εξουσιοδοτημένης χρήσης:** Κάνε πρακτικές δοκιμές μόνο σε συστήματα, κώδικα, λογαριασμούς, captures και lab environments που σου ανήκουν ή για τα οποία έχεις ρητή άδεια. Προτίμησε localhost, synthetic data, disposable VMs/containers και read-only analysis.

## Μαθησιακοί στόχοι

Στο τέλος πρέπει να μπορείς να:

- εξηγήσεις το **IPC threat modeling** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **Unix sockets and peer credentials** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **D-Bus names, policies and activation** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **Windows COM/RPC identity and impersonation concepts** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **named pipes and local endpoints** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **message marshalling and schema validation** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Όρισε ownership/identity, state transition, trust boundary και το ελάχιστο evidence που χρειάζεται για ασφαλή validation.

## Βαθιές τεχνικές έννοιες

### 1. IPC threat modeling

IPC είναι privilege boundary όταν μία process ζητά από άλλη να εκτελέσει ενέργεια. Κατέγραψε caller identity, server privilege, operation/resource, schema και ακριβές σημείο authorization.

### 2. Unix sockets και peer credentials

Unix-domain sockets μπορούν να παρέχουν kernel-authenticated UID/GID του peer. Προτίμησε αυτό το transport context από username που δηλώνει ο ίδιος ο client μέσα στο message.

### 3. D-Bus names, policies και activation

D-Bus συνδυάζει bus names, method calls, policy και service activation. Έλεγξε ποιος μπορεί να κατέχει/call ένα sensitive name και αν η authorization παραμένει σωστή όταν αλλάζουν packages ή policy.

### 4. Windows COM/RPC identity και impersonation

COM/RPC μπορεί να μεταφέρει caller security context σε privileged service. Αξιολόγησε authentication level, endpoint permissions, impersonation και αν ο server authorizes τον αρχικό caller πριν από privileged action.

### 5. named pipes και local endpoints

Local endpoint δεν είναι αυτόματα trusted. Περιόρισε connect/create permissions, authenticate peer, βάλε bounds στα messages και μην αφήνεις untrusted client να επιλέγει privileged file/process operation.

### 6. marshalling και schema validation

IPC payload είναι untrusted input. Χρησιμοποίησε explicit schema, length/depth limits, versioning και canonical encoding και απέρριψε contradictory fields στο component που παίρνει την τελική απόφαση.

### 7. capability-style handles

Ένα στενό unforgeable handle μπορεί να μεταφέρει συγκεκριμένη authority πιο ασφαλώς από global name και broad service account. Το handle πρέπει να παραμένει δεμένο με σωστό user, tenant και resource type.

### 8. brokered architectures και least privilege

Broker επιτρέπει σε low-privilege client μικρό σύνολο privileged operations. Ο broker πρέπει να θεωρεί κάθε request hostile, να ελέγχει peer context και parameters και να εκθέτει μόνο την ελάχιστη απαιτούμενη API surface.

## Engineering focus

Μετέτρεψε κάθε σημαντικό claim σε security invariant και regression test. Προτίμησε controls που μειώνουν authority, κάνουν explicit το state και αφήνουν αρκετή telemetry για root-cause analysis.

## Μοτίβα αστοχίας

- **Confused deputy:** privileged component ενεργεί για caller χωρίς επαρκή έλεγχο authority/context.
- **Identity/context confusion:** issuer, subject, tenant, role, origin, audience ή resource χρησιμοποιείται σε λάθος security context.
- **State/replay failure:** valid state γίνεται δεκτό όταν είναι stale, duplicated, revoked, reordered ή σε λάθος workflow step.
- **Parser mismatch:** δύο layers ερμηνεύουν διαφορετικά το ίδιο input/configuration.
- **Excess authority:** service, process, token, key ή admin role έχει περισσότερα permissions από όσα χρειάζεται.
- **Telemetry gap:** δεν καταγράφεται αρκετό actor/resource/policy/result context ώστε να γίνει αξιόπιστο investigation.

## Αμυντικό checklist

1. Γράψε το security invariant πριν από το test.
2. Μείωσε permissions/capabilities και lifetime όσο γίνεται.
3. Κάνε validation στο component που παίρνει την τελική security απόφαση.
4. Δέσε identity/state με σωστό tenant, resource, audience, origin ή protocol phase.
5. Βάλε explicit schemas, allowlists, resource limits και ασφαλή failure behavior.
6. Κατέγραψε actor, resource, operation, policy/version και result χωρίς secrets.
7. Προετοίμασε rollback/recovery πριν από state-changing lab.

## Καθοδηγούμενο εργαστήριο

### Lab 1 — Inventory local IPC endpoints on a disposable Linux VM or Termux environment using read-only tools.


### Lab 2 — Design a toy privileged broker API and write an explicit authorization matrix for each operation.


### Lab 3 — Trace a local client/server exchange and identify where caller identity is established, transformed and checked.

Για κάθε lab χρησιμοποίησε owned/synthetic inputs και κράτησε objective, scope, version, expected/observed behavior, cleanup, remediation και regression result σύμφωνα με τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md).

## Evidence που αξίζει να κρατήσεις

- version/build και σχετικό configuration χωρίς secrets,
- μικρό διάγραμμα trust boundaries και data/state flow,
- sanitized logs, traces ή packet metadata,
- ακριβές test input με synthetic values,
- before/after αποτέλεσμα remediation,
- limitations και μη ελεγμένες υποθέσεις.

## Συχνά λάθη

- Αντιγραφή command χωρίς κατανόηση του mechanism.
- Χρήση production/τρίτου συστήματος ενώ αρκεί localhost ή synthetic data.
- Σύγχυση authentication με authorization, encryption με trust ή signature με safety.
- Θεώρηση ενός alert ως οριστικής απόδειξης.
- Παράβλεψη version, timing, identity context, parser behavior ή recovery.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary;
2. Ποιο state/identity μπορεί να γίνει stale ή να χρησιμοποιηθεί σε λάθος context;
3. Ποιο evidence θα σε έκανε να απορρίψεις την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά authority/blast radius;
5. Πώς θα κάνεις ασφαλές retest μετά τη remediation;

## Πλήρες αγγλικό μάθημα

[English Module 118](../../English/03-Systems-Malware-and-Reverse-Engineering/118-IPC-RPC-D-Bus-COM-and-Local-Trust-Boundaries.md)

## Επόμενα μαθήματα

Σχετικά modules: **021, 041, 062, 073, 074, 119**. Από το κύριο menu επίλεξε **Αναζήτηση μαθημάτων** για να βρεις σχετικά θέματα σε όλο το project.

---

# Sandboxing, Broker Architectures και Isolation Assurance

> **Ελληνική έκδοση — Μάθημα 119.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands παραμένουν στα Αγγλικά όπου αυτό αυξάνει την ακρίβεια.

Το sandbox είναι σύνολο περιορισμών authority. Μάθε να ορίζεις το security invariant, να μετράς exposed capabilities και να κάνεις regression verification.

> **Όριο εξουσιοδοτημένης χρήσης:** Κάνε πρακτικές δοκιμές μόνο σε συστήματα, κώδικα, λογαριασμούς, captures και lab environments που σου ανήκουν ή για τα οποία έχεις ρητή άδεια. Προτίμησε localhost, synthetic data, disposable VMs/containers και read-only analysis.

## Μαθησιακοί στόχοι

Στο τέλος πρέπει να μπορείς να:

- εξηγήσεις το **sandbox threat models** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **deny-by-default policy** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **syscall and filesystem mediation** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **brokers and privileged helpers** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **namespace and job-object style isolation** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **seccomp, MAC and platform policy concepts** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Όρισε ownership/identity, state transition, trust boundary και το ελάχιστο evidence που χρειάζεται για ασφαλή validation.

## Βαθιές τεχνικές έννοιες

### 1. sandbox threat models

Sandbox μειώνει impact περιορίζοντας resources/operations. Όρισε ποια attacker capability υποθέτει και ποια assets μένουν έξω από το boundary, αλλιώς ο όρος “sandboxed” δεν έχει μετρήσιμη σημασία.

### 2. deny-by-default policy

Ξεκίνα denied και πρόσθεσε μόνο απαιτούμενες capabilities. Κάθε exception χρειάζεται owner, reason, resource scope και regression test ώστε compatibility changes να μην αυξάνουν αθόρυβα authority.

### 3. syscall και filesystem mediation

Syscalls και filesystem είναι βασικά boundaries προς kernel resources. Η policy πρέπει να λαμβάνει υπόψη path resolution, links, mounts, namespaces και inherited descriptors και όπου γίνεται να χρησιμοποιεί stable object identity.

### 4. brokers και privileged helpers

Privileged helper είναι ελεγχόμενη έξοδος από sandbox και πρέπει να έχει πολύ μικρή API. Μετέφερε explicit caller/resource context και απόρριψε ό,τι ο helper δεν μπορεί να authorize τοπικά.

### 5. namespaces και job-object isolation

Namespaces, cgroups, job objects και tokens απομονώνουν διαφορετικές διαστάσεις. Επιβεβαίωσε ξεχωριστά process, mount, network, IPC, user, device και quota isolation αντί να υποθέτεις ένα γενικό boundary.

### 6. seccomp, MAC και platform policy

Seccomp και MAC περιορίζουν behavior πέρα από ordinary permissions. Οι policies πρέπει να βασίζονται σε πραγματικές απαιτήσεις, να fail closed όπου χρειάζεται και να αφήνουν telemetry για denials/drift.

### 7. escape classes χωρίς weaponization

Escape class μπορεί να είναι privileged interface, kernel/runtime bug, policy gap, parser bug ή confused deputy. Στο defensive research ταξινόμησε το boundary failure και κάνε reproduction μόνο σε toy/owned target.

### 8. assurance, regression και telemetry

Isolation χρειάζεται συνεχή evidence: policy versions, broker decisions, denied operations και regression tests μετά από runtime updates. Χωρίς observability δύσκολα αποδεικνύεται ότι το sandbox παρέμεινε αποτελεσματικό.

## Engineering focus

Μετέτρεψε κάθε σημαντικό claim σε security invariant και regression test. Προτίμησε controls που μειώνουν authority, κάνουν explicit το state και αφήνουν αρκετή telemetry για root-cause analysis.

## Μοτίβα αστοχίας

- **Confused deputy:** privileged component ενεργεί για caller χωρίς επαρκή έλεγχο authority/context.
- **Identity/context confusion:** issuer, subject, tenant, role, origin, audience ή resource χρησιμοποιείται σε λάθος security context.
- **State/replay failure:** valid state γίνεται δεκτό όταν είναι stale, duplicated, revoked, reordered ή σε λάθος workflow step.
- **Parser mismatch:** δύο layers ερμηνεύουν διαφορετικά το ίδιο input/configuration.
- **Excess authority:** service, process, token, key ή admin role έχει περισσότερα permissions από όσα χρειάζεται.
- **Telemetry gap:** δεν καταγράφεται αρκετό actor/resource/policy/result context ώστε να γίνει αξιόπιστο investigation.

## Αμυντικό checklist

1. Γράψε το security invariant πριν από το test.
2. Μείωσε permissions/capabilities και lifetime όσο γίνεται.
3. Κάνε validation στο component που παίρνει την τελική security απόφαση.
4. Δέσε identity/state με σωστό tenant, resource, audience, origin ή protocol phase.
5. Βάλε explicit schemas, allowlists, resource limits και ασφαλή failure behavior.
6. Κατέγραψε actor, resource, operation, policy/version και result χωρίς secrets.
7. Προετοίμασε rollback/recovery πριν από state-changing lab.

## Καθοδηγούμενο εργαστήριο

### Lab 1 — Build a toy process with an allowlist of file operations and document what is intentionally denied.


### Lab 2 — Compare two container/sandbox configurations by capabilities, mounts, network access and process visibility.


### Lab 3 — Write regression tests that prove a sandboxed component cannot access three lab-only resources outside its policy.

Για κάθε lab χρησιμοποίησε owned/synthetic inputs και κράτησε objective, scope, version, expected/observed behavior, cleanup, remediation και regression result σύμφωνα με τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md).

## Evidence που αξίζει να κρατήσεις

- version/build και σχετικό configuration χωρίς secrets,
- μικρό διάγραμμα trust boundaries και data/state flow,
- sanitized logs, traces ή packet metadata,
- ακριβές test input με synthetic values,
- before/after αποτέλεσμα remediation,
- limitations και μη ελεγμένες υποθέσεις.

## Συχνά λάθη

- Αντιγραφή command χωρίς κατανόηση του mechanism.
- Χρήση production/τρίτου συστήματος ενώ αρκεί localhost ή synthetic data.
- Σύγχυση authentication με authorization, encryption με trust ή signature με safety.
- Θεώρηση ενός alert ως οριστικής απόδειξης.
- Παράβλεψη version, timing, identity context, parser behavior ή recovery.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary;
2. Ποιο state/identity μπορεί να γίνει stale ή να χρησιμοποιηθεί σε λάθος context;
3. Ποιο evidence θα σε έκανε να απορρίψεις την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά authority/blast radius;
5. Πώς θα κάνεις ασφαλές retest μετά τη remediation;

## Πλήρες αγγλικό μάθημα

[English Module 119](../../English/03-Systems-Malware-and-Reverse-Engineering/119-Sandboxing-Broker-Architectures-and-Isolation-Assurance.md)

## Επόμενα μαθήματα

Σχετικά modules: **041, 074, 075, 094, 095, 112**. Από το κύριο menu επίλεξε **Αναζήτηση μαθημάτων** για να βρεις σχετικά θέματα σε όλο το project.

---

# macOS Security Internals: TCC, SIP, Gatekeeper, Notarization και XProtect

> **Ελληνική έκδοση — Μάθημα 120.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands παραμένουν στα Αγγλικά όπου αυτό αυξάνει την ακρίβεια.

Χαρτογράφησε το macOS trust model: code signing, Gatekeeper, notarization, SIP, TCC, sandbox, Keychain, Secure Enclave και XProtect.

> **Όριο εξουσιοδοτημένης χρήσης:** Κάνε πρακτικές δοκιμές μόνο σε συστήματα, κώδικα, λογαριασμούς, captures και lab environments που σου ανήκουν ή για τα οποία έχεις ρητή άδεια. Προτίμησε localhost, synthetic data, disposable VMs/containers και read-only analysis.

## Μαθησιακοί στόχοι

Στο τέλος πρέπει να μπορείς να:

- εξηγήσεις το **code signing and designated requirements** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **Gatekeeper and notarization** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **System Integrity Protection (SIP)** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **Transparency, Consent and Control (TCC)** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **sandboxing and entitlements** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **Keychain and Secure Enclave concepts** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Όρισε ownership/identity, state transition, trust boundary και το ελάχιστο evidence που χρειάζεται για ασφαλή validation.

## Βαθιές τεχνικές έννοιες

### 1. code signing και designated requirements

Το macOS code signing συνδέει executable content με signing identity και requirements. Έλεγξε designated requirement και entitlements· το “signed” δεν σημαίνει αυτόματα trusted για κάθε operation.

### 2. Gatekeeper και notarization

Gatekeeper αξιολογεί downloaded software με provenance, signing, quarantine context και notarization policy. Notarization είναι ecosystem trust signal, όχι απόδειξη ότι η εφαρμογή δεν έχει vulnerabilities.

### 3. System Integrity Protection

Το SIP περιορίζει αλλαγές σε protected OS locations και ορισμένες runtime δυνατότητες ακόμη και για root. Ξεχώρισε SIP-protected assets από ordinary administrator-controlled state.

### 4. TCC privacy controls

TCC ελέγχει πρόσβαση σε camera, microphone, contacts και άλλα privacy-sensitive resources. Η απόφαση εξαρτάται από app identity, entitlement/context και user/admin policy και μπορεί να αλλάζει ανά macOS release.

### 5. App Sandbox και entitlements

App Sandbox περιορίζει process environment και τα entitlements προσθέτουν capabilities. Αντιμετώπισε κάθε entitlement σαν declaration authority και αφαίρεσε broad access που δεν χρειάζεται πλέον το product.

### 6. Keychain και Secure Enclave

Keychain access controls και Secure Enclave-backed keys μπορούν να περιορίζουν secret/key operations. Έλεγξε accessibility, authentication requirement, sharing groups, backup/sync και recovery behavior.

### 7. XProtect και platform remediation

XProtect και άλλα platform protections λειτουργούν ως defense-in-depth και ενημερώνονται μέσω του ecosystem. Κατά το triage κράτα OS/security-update evidence και μην θεωρείς ότι η παρουσία τους εγγυάται καθαρό host.

### 8. EndpointSecurity και unified logs

EndpointSecurity δίνει structured security events και unified logging ευρύτερο diagnostic context. Συσχέτισε process identity, code signing, parentage, file/network activity και time αντί να βασίζεσαι σε έναν sensor.

## Engineering focus

Μετέτρεψε κάθε σημαντικό claim σε security invariant και regression test. Προτίμησε controls που μειώνουν authority, κάνουν explicit το state και αφήνουν αρκετή telemetry για root-cause analysis.

## Μοτίβα αστοχίας

- **Confused deputy:** privileged component ενεργεί για caller χωρίς επαρκή έλεγχο authority/context.
- **Identity/context confusion:** issuer, subject, tenant, role, origin, audience ή resource χρησιμοποιείται σε λάθος security context.
- **State/replay failure:** valid state γίνεται δεκτό όταν είναι stale, duplicated, revoked, reordered ή σε λάθος workflow step.
- **Parser mismatch:** δύο layers ερμηνεύουν διαφορετικά το ίδιο input/configuration.
- **Excess authority:** service, process, token, key ή admin role έχει περισσότερα permissions από όσα χρειάζεται.
- **Telemetry gap:** δεν καταγράφεται αρκετό actor/resource/policy/result context ώστε να γίνει αξιόπιστο investigation.

## Αμυντικό checklist

1. Γράψε το security invariant πριν από το test.
2. Μείωσε permissions/capabilities και lifetime όσο γίνεται.
3. Κάνε validation στο component που παίρνει την τελική security απόφαση.
4. Δέσε identity/state με σωστό tenant, resource, audience, origin ή protocol phase.
5. Βάλε explicit schemas, allowlists, resource limits και ασφαλή failure behavior.
6. Κατέγραψε actor, resource, operation, policy/version και result χωρίς secrets.
7. Προετοίμασε rollback/recovery πριν από state-changing lab.

## Καθοδηγούμενο εργαστήριο

### Lab 1 — On a Mac you own, map permissions requested by a benign application and compare them with its functional needs.


### Lab 2 — Review Apple Platform Security documentation and build a trust-chain diagram from boot to application launch.


### Lab 3 — Create a defensive checklist for evaluating a signed/notarized application without bypassing platform protections.

Για κάθε lab χρησιμοποίησε owned/synthetic inputs και κράτησε objective, scope, version, expected/observed behavior, cleanup, remediation και regression result σύμφωνα με τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md).

## Evidence που αξίζει να κρατήσεις

- version/build και σχετικό configuration χωρίς secrets,
- μικρό διάγραμμα trust boundaries και data/state flow,
- sanitized logs, traces ή packet metadata,
- ακριβές test input με synthetic values,
- before/after αποτέλεσμα remediation,
- limitations και μη ελεγμένες υποθέσεις.

## Συχνά λάθη

- Αντιγραφή command χωρίς κατανόηση του mechanism.
- Χρήση production/τρίτου συστήματος ενώ αρκεί localhost ή synthetic data.
- Σύγχυση authentication με authorization, encryption με trust ή signature με safety.
- Θεώρηση ενός alert ως οριστικής απόδειξης.
- Παράβλεψη version, timing, identity context, parser behavior ή recovery.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary;
2. Ποιο state/identity μπορεί να γίνει stale ή να χρησιμοποιηθεί σε λάθος context;
3. Ποιο evidence θα σε έκανε να απορρίψεις την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά authority/blast radius;
5. Πώς θα κάνεις ασφαλές retest μετά τη remediation;

## Πλήρες αγγλικό μάθημα

[English Module 120](../../English/03-Systems-Malware-and-Reverse-Engineering/120-macOS-Security-Internals-TCC-SIP-Gatekeeper-Notarization-and-XProtect.md)

## Επόμενα μαθήματα

Σχετικά modules: **021, 044, 049, 054, 103, 119**. Από το κύριο menu επίλεξε **Αναζήτηση μαθημάτων** για να βρεις σχετικά θέματα σε όλο το project.

---

# iOS Security Internals: Entitlements, Code Signing, Keychain και Data Protection

> **Ελληνική έκδοση — Μάθημα 121.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands παραμένουν στα Αγγλικά όπου αυτό αυξάνει την ακρίβεια.

Κατανόησε iOS code signing, entitlements, app sandbox, Keychain access groups, Data Protection classes και Secure Enclave ως ξεχωριστά επίπεδα trust.

> **Όριο εξουσιοδοτημένης χρήσης:** Κάνε πρακτικές δοκιμές μόνο σε συστήματα, κώδικα, λογαριασμούς, captures και lab environments που σου ανήκουν ή για τα οποία έχεις ρητή άδεια. Προτίμησε localhost, synthetic data, disposable VMs/containers και read-only analysis.

## Μαθησιακοί στόχοι

Στο τέλος πρέπει να μπορείς να:

- εξηγήσεις το **secure boot chain and code signing** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **application sandbox containers** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **entitlements and capabilities** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **Keychain access groups** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **Data Protection classes** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **Secure Enclave and key handling** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Όρισε ownership/identity, state transition, trust boundary και το ελάχιστο evidence που χρειάζεται για ασφαλή validation.

## Βαθιές τεχνικές έννοιες

### 1. secure boot και code signing

Το iOS χρησιμοποιεί hardware-rooted boot chain και mandatory code signing. Ξεχώρισε platform integrity, app signing, provisioning και runtime authorization γιατί είναι διαφορετικά controls.

### 2. sandbox containers

Apps έχουν isolated containers αλλά υπάρχουν σκόπιμα shared surfaces όπως extensions, app groups, pasteboard, URL handling, cloud sync και exported documents. Αυτά χρειάζονται ξεχωριστό threat model.

### 3. entitlements και capabilities

Entitlements δηλώνουν privileged capabilities. Σύγκρινε το signed entitlement set με τις πραγματικές ανάγκες της εφαρμογής και αφαίρεσε παλιές ή broad δυνατότητες.

### 4. Keychain access groups

Keychain access groups επιτρέπουν sharing credentials μεταξύ συγκεκριμένων signed apps/extensions. Έλεγξε membership, accessibility, sync και recovery ώστε helper να μην αποκτά περισσότερα secrets από όσα χρειάζεται.

### 5. Data Protection classes

Data Protection συνδέει file encryption με device lock state και key availability. Διάλεξε class σύμφωνα με το πότε χρειάζεται πραγματικά το data και έλεγξε backup/export copies ξεχωριστά.

### 6. Secure Enclave και key handling

Secure Enclave-backed keys μπορούν να κρατούν private material εκτός normal app processor. Όρισε user verification, fallback, migration και recovery χωρίς να εξάγεται το private key.

### 7. privacy permissions

Camera, microphone, photos, location, contacts και Bluetooth χρειάζονται ελάχιστη απαιτούμενη άδεια. Ζήτα permission τη στιγμή που χρειάζεται, χειρίσου denial σωστά και εφάρμοσε data minimization.

### 8. managed-device και enterprise trust

MDM μπορεί να εγκαθιστά profiles, certificates, networks, managed apps και restrictions. Ξεχώρισε device-management authority από application identity και κάνε audit high-impact profile/certificate changes.

## Engineering focus

Μετέτρεψε κάθε σημαντικό claim σε security invariant και regression test. Προτίμησε controls που μειώνουν authority, κάνουν explicit το state και αφήνουν αρκετή telemetry για root-cause analysis.

## Μοτίβα αστοχίας

- **Confused deputy:** privileged component ενεργεί για caller χωρίς επαρκή έλεγχο authority/context.
- **Identity/context confusion:** issuer, subject, tenant, role, origin, audience ή resource χρησιμοποιείται σε λάθος security context.
- **State/replay failure:** valid state γίνεται δεκτό όταν είναι stale, duplicated, revoked, reordered ή σε λάθος workflow step.
- **Parser mismatch:** δύο layers ερμηνεύουν διαφορετικά το ίδιο input/configuration.
- **Excess authority:** service, process, token, key ή admin role έχει περισσότερα permissions από όσα χρειάζεται.
- **Telemetry gap:** δεν καταγράφεται αρκετό actor/resource/policy/result context ώστε να γίνει αξιόπιστο investigation.

## Αμυντικό checklist

1. Γράψε το security invariant πριν από το test.
2. Μείωσε permissions/capabilities και lifetime όσο γίνεται.
3. Κάνε validation στο component που παίρνει την τελική security απόφαση.
4. Δέσε identity/state με σωστό tenant, resource, audience, origin ή protocol phase.
5. Βάλε explicit schemas, allowlists, resource limits και ασφαλή failure behavior.
6. Κατέγραψε actor, resource, operation, policy/version και result χωρίς secrets.
7. Προετοίμασε rollback/recovery πριν από state-changing lab.

## Καθοδηγούμενο εργαστήριο

### Lab 1 — Design an iOS app threat model using only public architecture documentation and a fictional app.


### Lab 2 — Compare storage choices for a sample token: plain file, protected file and Keychain, documenting security properties rather than extracting secrets.


### Lab 3 — Map a fictional app’s entitlements to least-privilege requirements and flag unnecessary capabilities.

Για κάθε lab χρησιμοποίησε owned/synthetic inputs και κράτησε objective, scope, version, expected/observed behavior, cleanup, remediation και regression result σύμφωνα με τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md).

## Evidence που αξίζει να κρατήσεις

- version/build και σχετικό configuration χωρίς secrets,
- μικρό διάγραμμα trust boundaries και data/state flow,
- sanitized logs, traces ή packet metadata,
- ακριβές test input με synthetic values,
- before/after αποτέλεσμα remediation,
- limitations και μη ελεγμένες υποθέσεις.

## Συχνά λάθη

- Αντιγραφή command χωρίς κατανόηση του mechanism.
- Χρήση production/τρίτου συστήματος ενώ αρκεί localhost ή synthetic data.
- Σύγχυση authentication με authorization, encryption με trust ή signature με safety.
- Θεώρηση ενός alert ως οριστικής απόδειξης.
- Παράβλεψη version, timing, identity context, parser behavior ή recovery.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary;
2. Ποιο state/identity μπορεί να γίνει stale ή να χρησιμοποιηθεί σε λάθος context;
3. Ποιο evidence θα σε έκανε να απορρίψεις την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά authority/blast radius;
5. Πώς θα κάνεις ασφαλές retest μετά τη remediation;

## Πλήρες αγγλικό μάθημα

[English Module 121](../../English/05-Mobile-IoT-and-Hardware/121-iOS-Security-Internals-Entitlements-Code-Signing-Keychain-and-Data-Protection.md)

## Επόμενα μαθήματα

Σχετικά modules: **017, 039, 054, 056, 082, 103**. Από το κύριο menu επίλεξε **Αναζήτηση μαθημάτων** για να βρεις σχετικά θέματα σε όλο το project.

---

# Cellular Networks, LTE/5G Architecture και Mobile Network Security

> **Ελληνική έκδοση — Μάθημα 122.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands παραμένουν στα Αγγλικά όπου αυτό αυξάνει την ακρίβεια.

Μελέτησε LTE/5G ως αρχιτεκτονική identity, radio και core-network trust, με έμφαση σε privacy, roaming και baseband isolation.

> **Όριο εξουσιοδοτημένης χρήσης:** Κάνε πρακτικές δοκιμές μόνο σε συστήματα, κώδικα, λογαριασμούς, captures και lab environments που σου ανήκουν ή για τα οποία έχεις ρητή άδεια. Προτίμησε localhost, synthetic data, disposable VMs/containers και read-only analysis.

## Μαθησιακοί στόχοι

Στο τέλος πρέπει να μπορείς να:

- εξηγήσεις το **UE, SIM/eSIM and subscriber identity** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **RAN, core network and control/user planes** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **LTE EPC and 5G Core concepts** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **AKA authentication families** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **temporary identifiers and privacy** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **roaming and inter-operator trust** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Όρισε ownership/identity, state transition, trust boundary και το ελάχιστο evidence που χρειάζεται για ασφαλή validation.

## Βαθιές τεχνικές έννοιες

### 1. UE, SIM/eSIM και subscriber identity

Η cellular identity περιλαμβάνει device, subscription SIM/eSIM, phone number και application identity που έχουν διαφορετικό owner και trust. Μην τα χρησιμοποιείς σαν ισοδύναμα authentication factors.

### 2. RAN, core, control και user planes

Το RAN συνδέει UE με core network και χωρίζει signaling/control από user data. Χαρτογράφησε interfaces που μεταφέρουν subscriber state, routing, authentication context και application traffic.

### 3. LTE EPC και 5G Core

LTE EPC και 5G Core έχουν διαφορετικά service/function boundaries αλλά και τα δύο απαιτούν authenticated state και αυστηρή inter-function policy. Αξιολόγησε exposed service/admin APIs πέρα από το radio encryption.

### 4. AKA families

AKA protocols παράγουν session keys από subscription secrets χωρίς να στέλνουν το long-term secret. Έλεγξε identity binding, freshness, network authentication, key separation και failure handling.

### 5. temporary identifiers και privacy

Temporary identifiers μειώνουν συχνή έκθεση long-lived subscriber identity. Privacy analysis πρέπει ακόμη να καλύπτει paging, timing, mobility metadata, app identifiers και logs που μπορούν να κάνουν correlation.

### 6. roaming και inter-operator trust

Roaming επεκτείνει trust σε άλλους operators και interconnects. Χρειάζονται peer policy, validation, least privilege και monitoring επειδή partner-path compromise μπορεί να επηρεάσει subscribers άλλου domain.

### 7. network slicing και service exposure

5G slicing και service-based APIs χρειάζονται πραγματική policy isolation. Slice label μόνο του δεν είναι boundary· έλεγξε authorization, routing, resource isolation και telemetry.

### 8. baseband isolation και telemetry

Baseband επεξεργάζεται σύνθετα untrusted radio protocols και πρέπει να είναι απομονωμένο από application processor. Firmware updates, crash telemetry και περιορισμένη authority μειώνουν το impact baseband failure.

## Engineering focus

Μετέτρεψε κάθε σημαντικό claim σε security invariant και regression test. Προτίμησε controls που μειώνουν authority, κάνουν explicit το state και αφήνουν αρκετή telemetry για root-cause analysis.

## Μοτίβα αστοχίας

- **Confused deputy:** privileged component ενεργεί για caller χωρίς επαρκή έλεγχο authority/context.
- **Identity/context confusion:** issuer, subject, tenant, role, origin, audience ή resource χρησιμοποιείται σε λάθος security context.
- **State/replay failure:** valid state γίνεται δεκτό όταν είναι stale, duplicated, revoked, reordered ή σε λάθος workflow step.
- **Parser mismatch:** δύο layers ερμηνεύουν διαφορετικά το ίδιο input/configuration.
- **Excess authority:** service, process, token, key ή admin role έχει περισσότερα permissions από όσα χρειάζεται.
- **Telemetry gap:** δεν καταγράφεται αρκετό actor/resource/policy/result context ώστε να γίνει αξιόπιστο investigation.

## Αμυντικό checklist

1. Γράψε το security invariant πριν από το test.
2. Μείωσε permissions/capabilities και lifetime όσο γίνεται.
3. Κάνε validation στο component που παίρνει την τελική security απόφαση.
4. Δέσε identity/state με σωστό tenant, resource, audience, origin ή protocol phase.
5. Βάλε explicit schemas, allowlists, resource limits και ασφαλή failure behavior.
6. Κατέγραψε actor, resource, operation, policy/version και result χωρίς secrets.
7. Προετοίμασε rollback/recovery πριν από state-changing lab.

## Καθοδηγούμενο εργαστήριο

### Lab 1 — Draw a 5G connection-flow diagram from device to application service using public standards diagrams.


### Lab 2 — Threat-model a fictional roaming scenario and list which parties must trust which assertions.


### Lab 3 — Compare Wi-Fi and cellular identity/privacy assumptions without capturing any third-party radio traffic.

Για κάθε lab χρησιμοποίησε owned/synthetic inputs και κράτησε objective, scope, version, expected/observed behavior, cleanup, remediation και regression result σύμφωνα με τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md).

## Evidence που αξίζει να κρατήσεις

- version/build και σχετικό configuration χωρίς secrets,
- μικρό διάγραμμα trust boundaries και data/state flow,
- sanitized logs, traces ή packet metadata,
- ακριβές test input με synthetic values,
- before/after αποτέλεσμα remediation,
- limitations και μη ελεγμένες υποθέσεις.

## Συχνά λάθη

- Αντιγραφή command χωρίς κατανόηση του mechanism.
- Χρήση production/τρίτου συστήματος ενώ αρκεί localhost ή synthetic data.
- Σύγχυση authentication με authorization, encryption με trust ή signature με safety.
- Θεώρηση ενός alert ως οριστικής απόδειξης.
- Παράβλεψη version, timing, identity context, parser behavior ή recovery.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary;
2. Ποιο state/identity μπορεί να γίνει stale ή να χρησιμοποιηθεί σε λάθος context;
3. Ποιο evidence θα σε έκανε να απορρίψεις την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά authority/blast radius;
5. Πώς θα κάνεις ασφαλές retest μετά τη remediation;

## Πλήρες αγγλικό μάθημα

[English Module 122](../../English/04-Network-Wireless-and-Internet/122-Cellular-Networks-LTE-5G-Architecture-and-Mobile-Network-Security.md)

## Επόμενα μαθήματα

Σχετικά modules: **016, 017, 051, 055, 056, 123**. Από το κύριο menu επίλεξε **Αναζήτηση μαθημάτων** για να βρεις σχετικά θέματα σε όλο το project.

---

# Radio, SDR και RF Security Fundamentals

> **Ελληνική έκδοση — Μάθημα 123.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands παραμένουν στα Αγγλικά όπου αυτό αυξάνει την ακρίβεια.

Απόκτησε βασική RF/SDR γνώση με receive-only ή synthetic data: sampling, I/Q, modulation, frames, checksums, authentication και replay resistance.

> **Όριο εξουσιοδοτημένης χρήσης:** Κάνε πρακτικές δοκιμές μόνο σε συστήματα, κώδικα, λογαριασμούς, captures και lab environments που σου ανήκουν ή για τα οποία έχεις ρητή άδεια. Προτίμησε localhost, synthetic data, disposable VMs/containers και read-only analysis.

## Μαθησιακοί στόχοι

Στο τέλος πρέπει να μπορείς να:

- εξηγήσεις το **frequency, bandwidth and sampling** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **I/Q representation** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **modulation and symbol timing** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **preambles, frames and checksums** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **noise, interference and SNR** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **receive-only spectrum analysis** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Όρισε ownership/identity, state transition, trust boundary και το ελάχιστο evidence που χρειάζεται για ασφαλή validation.

## Βαθιές τεχνικές έννοιες

### 1. frequency, bandwidth και sampling

RF analysis ξεκινά από frequency, bandwidth, sample rate και receiver limitations. Κατέγραψε antenna, gain, filters, clock και environment πριν βγάλεις protocol/security συμπέρασμα.

### 2. I/Q representation

SDR χρησιμοποιεί I/Q samples για amplitude και phase πληροφορία. Raw I/Q δεν αποδεικνύει protocol ή sender χωρίς synchronization, framing και επιπλέον context.

### 3. modulation και symbol timing

Modulation μεταφέρει bits μέσω amplitude/phase/frequency αλλαγών και απαιτεί σωστό symbol/carrier timing. Μέτρησε parameters και channel conditions αντί να υποθέτεις defaults.

### 4. preambles, frames και checksums

Preambles και headers οριοθετούν frames, ενώ checksums εντοπίζουν τυχαίο corruption. Checksum δεν είναι authentication εκτός αν υπάρχει ξεχωριστός cryptographic mechanism.

### 5. noise, interference και SNR

Noise/interference μπορεί να μοιάζει με protocol failure ή attack. Μέτρησε SNR, channel occupancy και receiver saturation πριν αποδώσεις missing frames σε κακόβουλη ενέργεια.

### 6. receive-only spectrum analysis

Receive-only είναι ασφαλέστερη προεπιλογή για RF learning. Χρησιμοποίησε owned devices ή δημόσια/licensed test signals και μην αποκωδικοποιείς ιδιωτικές επικοινωνίες χωρίς άδεια.

### 7. authentication versus signal presence

Η παρουσία signal ή valid-looking frame δεν αποδεικνύει identity. Authentication χρειάζεται cryptographic/trusted context· proximity και signal strength δεν είναι ισχυρά credentials.

### 8. replay resistance και rolling state

Protocols που επιτρέπουν φυσική ενέργεια χρειάζονται freshness με nonce, counter ή challenge-response. Δοκίμασε μόνο σε synthetic/owned devices και αξιολόγησε synchronization και recovery state.

## Engineering focus

Μετέτρεψε κάθε σημαντικό claim σε security invariant και regression test. Προτίμησε controls που μειώνουν authority, κάνουν explicit το state και αφήνουν αρκετή telemetry για root-cause analysis.

## Μοτίβα αστοχίας

- **Confused deputy:** privileged component ενεργεί για caller χωρίς επαρκή έλεγχο authority/context.
- **Identity/context confusion:** issuer, subject, tenant, role, origin, audience ή resource χρησιμοποιείται σε λάθος security context.
- **State/replay failure:** valid state γίνεται δεκτό όταν είναι stale, duplicated, revoked, reordered ή σε λάθος workflow step.
- **Parser mismatch:** δύο layers ερμηνεύουν διαφορετικά το ίδιο input/configuration.
- **Excess authority:** service, process, token, key ή admin role έχει περισσότερα permissions από όσα χρειάζεται.
- **Telemetry gap:** δεν καταγράφεται αρκετό actor/resource/policy/result context ώστε να γίνει αξιόπιστο investigation.

## Αμυντικό checklist

1. Γράψε το security invariant πριν από το test.
2. Μείωσε permissions/capabilities και lifetime όσο γίνεται.
3. Κάνε validation στο component που παίρνει την τελική security απόφαση.
4. Δέσε identity/state με σωστό tenant, resource, audience, origin ή protocol phase.
5. Βάλε explicit schemas, allowlists, resource limits και ασφαλή failure behavior.
6. Κατέγραψε actor, resource, operation, policy/version και result χωρίς secrets.
7. Προετοίμασε rollback/recovery πριν από state-changing lab.

## Καθοδηγούμενο εργαστήριο

### Lab 1 — Use a prerecorded or synthetic IQ dataset and identify signal bandwidth, bursts and framing without transmitting.


### Lab 2 — Create a toy digital-radio frame format and add sequence numbers plus a MAC in software to demonstrate freshness/integrity.


### Lab 3 — Document how a rolling-code design differs from a static replayable identifier.

Για κάθε lab χρησιμοποίησε owned/synthetic inputs και κράτησε objective, scope, version, expected/observed behavior, cleanup, remediation και regression result σύμφωνα με τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md).

## Evidence που αξίζει να κρατήσεις

- version/build και σχετικό configuration χωρίς secrets,
- μικρό διάγραμμα trust boundaries και data/state flow,
- sanitized logs, traces ή packet metadata,
- ακριβές test input με synthetic values,
- before/after αποτέλεσμα remediation,
- limitations και μη ελεγμένες υποθέσεις.

## Συχνά λάθη

- Αντιγραφή command χωρίς κατανόηση του mechanism.
- Χρήση production/τρίτου συστήματος ενώ αρκεί localhost ή synthetic data.
- Σύγχυση authentication με authorization, encryption με trust ή signature με safety.
- Θεώρηση ενός alert ως οριστικής απόδειξης.
- Παράβλεψη version, timing, identity context, parser behavior ή recovery.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary;
2. Ποιο state/identity μπορεί να γίνει stale ή να χρησιμοποιηθεί σε λάθος context;
3. Ποιο evidence θα σε έκανε να απορρίψεις την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά authority/blast radius;
5. Πώς θα κάνεις ασφαλές retest μετά τη remediation;

## Πλήρες αγγλικό μάθημα

[English Module 123](../../English/04-Network-Wireless-and-Internet/123-Radio-SDR-and-RF-Security-Fundamentals.md)

## Επόμενα μαθήματα

Σχετικά modules: **016, 051, 055, 077, 083, 122**. Από το κύριο menu επίλεξε **Αναζήτηση μαθημάτων** για να βρεις σχετικά θέματα σε όλο το project.

---

# HTTP/2, HTTP/3, QUIC και Modern Web Transport Security

> **Ελληνική έκδοση — Μάθημα 124.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands παραμένουν στα Αγγλικά όπου αυτό αυξάνει την ακρίβεια.

Πήγαινε κάτω από το HTTP application layer: HTTP/2 streams, HTTP/3, QUIC, QPACK, 0-RTT, migration και observability.

> **Όριο εξουσιοδοτημένης χρήσης:** Κάνε πρακτικές δοκιμές μόνο σε συστήματα, κώδικα, λογαριασμούς, captures και lab environments που σου ανήκουν ή για τα οποία έχεις ρητή άδεια. Προτίμησε localhost, synthetic data, disposable VMs/containers και read-only analysis.

## Μαθησιακοί στόχοι

Στο τέλος πρέπει να μπορείς να:

- εξηγήσεις το **HTTP/2 streams and framing** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **HPACK/QPACK compression state** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **HTTP/3 over QUIC** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **QUIC connection IDs and migration** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **TLS 1.3 integration** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **0-RTT replay considerations** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Όρισε ownership/identity, state transition, trust boundary και το ελάχιστο evidence που χρειάζεται για ασφαλή validation.

## Βαθιές τεχνικές έννοιες

### 1. HTTP/2 streams και framing

HTTP/2 multiplexes streams με binary frames σε μία connection. Proxies και security components πρέπει να συμφωνούν σε stream/header semantics και limits ώστε να μη γίνεται validation διαφορετικού request από αυτό που βλέπει το επόμενο layer.

### 2. HPACK και QPACK

HPACK/QPACK συμπιέζουν headers με dynamic state. Βάλε memory/work bounds και σωστό error handling ώστε malformed ή blocked state να μην οδηγεί σε resource exhaustion ή διαφορετική header ερμηνεία.

### 3. HTTP/3 πάνω από QUIC

HTTP/3 μεταφέρει HTTP semantics πάνω από QUIC/UDP. Authorization παραμένει application-layer απόφαση, ενώ monitoring/rate controls πρέπει να προσαρμοστούν σε encrypted transport και διαφορετικό connection model.

### 4. connection IDs και migration

QUIC connection IDs επιτρέπουν αλλαγή network path χωρίς νέα logical session. Μην χρησιμοποιείς source IP σαν μοναδική session identity· συνδύασε authenticated app identity και migration-aware telemetry.

### 5. TLS 1.3 integration

QUIC ενσωματώνει TLS 1.3 για authentication/key establishment. Certificate validation και application authorization είναι ξεχωριστές αποφάσεις και encryption δεν κάνει ασφαλές ένα untrusted HTTP input.

### 6. 0-RTT replay considerations

0-RTT μειώνει latency αλλά early data μπορεί να replayed σύμφωνα με το threat model. Επίτρεψέ το μόνο για idempotent/replay-safe operations και κράτησε sensitive state changes εκτός αυτού του path.

### 7. proxy translation boundaries

Request μπορεί να αλλάξει HTTP/3→2→1.1 μεταξύ CDN/proxy/origin. Κάνε normalization/validation σε κάθε trust boundary και regression-test ambiguous headers, lengths και routing fields.

### 8. visibility με encrypted transport

QUIC κρυπτογραφεί περισσότερα transport metadata από TCP/TLS. Detection πρέπει να βασίζεται περισσότερο σε endpoint, proxy, application, DNS, identity και flow telemetry.

## Engineering focus

Μετέτρεψε κάθε σημαντικό claim σε security invariant και regression test. Προτίμησε controls που μειώνουν authority, κάνουν explicit το state και αφήνουν αρκετή telemetry για root-cause analysis.

## Μοτίβα αστοχίας

- **Confused deputy:** privileged component ενεργεί για caller χωρίς επαρκή έλεγχο authority/context.
- **Identity/context confusion:** issuer, subject, tenant, role, origin, audience ή resource χρησιμοποιείται σε λάθος security context.
- **State/replay failure:** valid state γίνεται δεκτό όταν είναι stale, duplicated, revoked, reordered ή σε λάθος workflow step.
- **Parser mismatch:** δύο layers ερμηνεύουν διαφορετικά το ίδιο input/configuration.
- **Excess authority:** service, process, token, key ή admin role έχει περισσότερα permissions από όσα χρειάζεται.
- **Telemetry gap:** δεν καταγράφεται αρκετό actor/resource/policy/result context ώστε να γίνει αξιόπιστο investigation.

## Αμυντικό checklist

1. Γράψε το security invariant πριν από το test.
2. Μείωσε permissions/capabilities και lifetime όσο γίνεται.
3. Κάνε validation στο component που παίρνει την τελική security απόφαση.
4. Δέσε identity/state με σωστό tenant, resource, audience, origin ή protocol phase.
5. Βάλε explicit schemas, allowlists, resource limits και ασφαλή failure behavior.
6. Κατέγραψε actor, resource, operation, policy/version και result χωρίς secrets.
7. Προετοίμασε rollback/recovery πριν από state-changing lab.

## Καθοδηγούμενο εργαστήριο

### Lab 1 — Run a local HTTP service and compare request/response metadata over HTTP/1.1 versus an HTTP/2/3-capable lab stack.


### Lab 2 — Draw stream state for concurrent requests and explain why one transport connection no longer maps neatly to one request at a time.


### Lab 3 — Create a safe replay-sensitivity checklist for operations such as GET-like reads versus state-changing actions.

Για κάθε lab χρησιμοποίησε owned/synthetic inputs και κράτησε objective, scope, version, expected/observed behavior, cleanup, remediation και regression result σύμφωνα με τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md).

## Evidence που αξίζει να κρατήσεις

- version/build και σχετικό configuration χωρίς secrets,
- μικρό διάγραμμα trust boundaries και data/state flow,
- sanitized logs, traces ή packet metadata,
- ακριβές test input με synthetic values,
- before/after αποτέλεσμα remediation,
- limitations και μη ελεγμένες υποθέσεις.

## Συχνά λάθη

- Αντιγραφή command χωρίς κατανόηση του mechanism.
- Χρήση production/τρίτου συστήματος ενώ αρκεί localhost ή synthetic data.
- Σύγχυση authentication με authorization, encryption με trust ή signature με safety.
- Θεώρηση ενός alert ως οριστικής απόδειξης.
- Παράβλεψη version, timing, identity context, parser behavior ή recovery.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary;
2. Ποιο state/identity μπορεί να γίνει stale ή να χρησιμοποιηθεί σε λάθος context;
3. Ποιο evidence θα σε έκανε να απορρίψεις την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά authority/blast radius;
5. Πώς θα κάνεις ασφαλές retest μετά τη remediation;

## Πλήρες αγγλικό μάθημα

[English Module 124](../../English/02-Recon-Pentesting-Web-and-AppSec/124-HTTP-2-HTTP-3-QUIC-and-Modern-Web-Transport-Security.md)

## Επόμενα μαθήματα

Σχετικά modules: **011, 013, 014, 052, 069, 070, 089**. Από το κύριο menu επίλεξε **Αναζήτηση μαθημάτων** για να βρεις σχετικά θέματα σε όλο το project.

---

# DNSSEC, DoH, DoQ, Resolver Privacy και DNS Trust

> **Ελληνική έκδοση — Μάθημα 125.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands παραμένουν στα Αγγλικά όπου αυτό αυξάνει την ακρίβεια.

Ξεχώρισε DNS authenticity από transport privacy: DNSSEC, DoH/DoT/DoQ, resolver trust, split DNS, TTL και cache lifecycle.

> **Όριο εξουσιοδοτημένης χρήσης:** Κάνε πρακτικές δοκιμές μόνο σε συστήματα, κώδικα, λογαριασμούς, captures και lab environments που σου ανήκουν ή για τα οποία έχεις ρητή άδεια. Προτίμησε localhost, synthetic data, disposable VMs/containers και read-only analysis.

## Μαθησιακοί στόχοι

Στο τέλος πρέπει να μπορείς να:

- εξηγήσεις το **DNSSEC chain of trust** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **DS, DNSKEY and RRSIG roles** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **negative answers and authenticated denial** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **DoH and DoT** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **DNS over QUIC (DoQ)** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **resolver policy and discovery** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Όρισε ownership/identity, state transition, trust boundary και το ελάχιστο evidence που χρειάζεται για ασφαλή validation.

## Βαθιές τεχνικές έννοιες

### 1. DNSSEC chain of trust

DNSSEC αυθεντικοποιεί DNS data μέσω signatures και chain of trust από trust anchor σε DS/DNSKEY. Παρέχει integrity/origin authentication, όχι confidentiality ούτε απόδειξη ότι η ίδια η εφαρμογή προορισμού είναι ασφαλής.

### 2. DS, DNSKEY και RRSIG

DNSKEY δημοσιεύει zone keys, DS συνδέει parent-child και RRSIG υπογράφει RRsets. Key rollover, timing, algorithms και delegation changes πρέπει να γίνονται χωρίς να σπάει το chain.

### 3. authenticated denial of existence

DNSSEC μπορεί να αποδείξει ότι name/type δεν υπάρχει. Τα negative answers είναι security-relevant cached state και χρειάζονται σωστή validation όπως και τα positive records.

### 4. DoH και DoT

DoH/DoT κρυπτογραφούν resolver traffic προς επιλεγμένο resolver. Αυτό αλλάζει visibility αλλά δεν αποδεικνύει ότι ο resolver είναι trustworthy ή ότι κάνει DNSSEC validation.

### 5. DoQ

DoQ μεταφέρει DNS πάνω από QUIC και κληρονομεί encrypted transport/connection behavior. Resolver authentication, policy, limits και fallback πρέπει να είναι explicit για όλα τα transports.

### 6. resolver policy και discovery

Resolver μπορεί να προέρχεται από network, OS, application ή enterprise policy. Κατέγραψε ποια ρύθμιση υπερισχύει και αν κάποιο app/encrypted path παρακάμπτει enterprise visibility.

### 7. split-horizon DNS

Internal και external DNS μπορούν σκόπιμα να δίνουν διαφορετικές απαντήσεις. Document namespace/boundary ώστε VPN, cache ή application-specific resolver να μην εκθέτει internal names ή λάθος routes.

### 8. cache TTL και stale answers

Positive/negative records μένουν cached σύμφωνα με TTL/policy και μερικοί resolvers σερβίρουν stale data σε outage. IR πρέπει να λαμβάνει υπόψη propagation και cache state μετά από αλλαγές.

## Engineering focus

Μετέτρεψε κάθε σημαντικό claim σε security invariant και regression test. Προτίμησε controls που μειώνουν authority, κάνουν explicit το state και αφήνουν αρκετή telemetry για root-cause analysis.

## Μοτίβα αστοχίας

- **Confused deputy:** privileged component ενεργεί για caller χωρίς επαρκή έλεγχο authority/context.
- **Identity/context confusion:** issuer, subject, tenant, role, origin, audience ή resource χρησιμοποιείται σε λάθος security context.
- **State/replay failure:** valid state γίνεται δεκτό όταν είναι stale, duplicated, revoked, reordered ή σε λάθος workflow step.
- **Parser mismatch:** δύο layers ερμηνεύουν διαφορετικά το ίδιο input/configuration.
- **Excess authority:** service, process, token, key ή admin role έχει περισσότερα permissions από όσα χρειάζεται.
- **Telemetry gap:** δεν καταγράφεται αρκετό actor/resource/policy/result context ώστε να γίνει αξιόπιστο investigation.

## Αμυντικό checklist

1. Γράψε το security invariant πριν από το test.
2. Μείωσε permissions/capabilities και lifetime όσο γίνεται.
3. Κάνε validation στο component που παίρνει την τελική security απόφαση.
4. Δέσε identity/state με σωστό tenant, resource, audience, origin ή protocol phase.
5. Βάλε explicit schemas, allowlists, resource limits και ασφαλή failure behavior.
6. Κατέγραψε actor, resource, operation, policy/version και result χωρίς secrets.
7. Προετοίμασε rollback/recovery πριν από state-changing lab.

## Καθοδηγούμενο εργαστήριο

### Lab 1 — Use public DNSSEC test domains or offline packet examples to follow a validation chain without altering DNS infrastructure.


### Lab 2 — Compare plain DNS, DoH and DoQ at the architecture level: who can observe queries and where trust terminates.


### Lab 3 — Build a cache-timeline exercise showing TTL, stale data and key rollover dependencies.

Για κάθε lab χρησιμοποίησε owned/synthetic inputs και κράτησε objective, scope, version, expected/observed behavior, cleanup, remediation και regression result σύμφωνα με τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md).

## Evidence που αξίζει να κρατήσεις

- version/build και σχετικό configuration χωρίς secrets,
- μικρό διάγραμμα trust boundaries και data/state flow,
- sanitized logs, traces ή packet metadata,
- ακριβές test input με synthetic values,
- before/after αποτέλεσμα remediation,
- limitations και μη ελεγμένες υποθέσεις.

## Συχνά λάθη

- Αντιγραφή command χωρίς κατανόηση του mechanism.
- Χρήση production/τρίτου συστήματος ενώ αρκεί localhost ή synthetic data.
- Σύγχυση authentication με authorization, encryption με trust ή signature με safety.
- Θεώρηση ενός alert ως οριστικής απόδειξης.
- Παράβλεψη version, timing, identity context, parser behavior ή recovery.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary;
2. Ποιο state/identity μπορεί να γίνει stale ή να χρησιμοποιηθεί σε λάθος context;
3. Ποιο evidence θα σε έκανε να απορρίψεις την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά authority/blast radius;
5. Πώς θα κάνεις ασφαλές retest μετά τη remediation;

## Πλήρες αγγλικό μάθημα

[English Module 125](../../English/04-Network-Wireless-and-Internet/125-DNSSEC-DoH-DoQ-Resolver-Privacy-and-DNS-Trust.md)

## Επόμενα μαθήματα

Σχετικά modules: **035, 051, 077, 078, 087, 124**. Από το κύριο menu επίλεξε **Αναζήτηση μαθημάτων** για να βρεις σχετικά θέματα σε όλο το project.

---

# CDN, Reverse Proxy, Cache και Edge Security

> **Ελληνική έκδοση — Μάθημα 126.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands παραμένουν στα Αγγλικά όπου αυτό αυξάνει την ακρίβεια.

Μελέτησε CDN/reverse proxy/cache ως αλυσίδα trust πριν το origin: cache keys, forwarded headers, origin shielding, edge code και purge.

> **Όριο εξουσιοδοτημένης χρήσης:** Κάνε πρακτικές δοκιμές μόνο σε συστήματα, κώδικα, λογαριασμούς, captures και lab environments που σου ανήκουν ή για τα οποία έχεις ρητή άδεια. Προτίμησε localhost, synthetic data, disposable VMs/containers και read-only analysis.

## Μαθησιακοί στόχοι

Στο τέλος πρέπει να μπορείς να:

- εξηγήσεις το **CDN and reverse-proxy trust boundaries** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **cache keys and variation** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **header normalization and forwarding** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **origin authentication and shielding** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **signed URLs/cookies concepts** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **cache poisoning classes** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Όρισε ownership/identity, state transition, trust boundary και το ελάχιστο evidence που χρειάζεται για ασφαλή validation.

## Βαθιές τεχνικές έννοιες

### 1. CDN και reverse-proxy trust boundaries

CDN/proxy μπορεί να τερματίζει TLS, να γράφει forwarding headers και να αλλάζει routing/cache state. Origin πρέπει να εμπιστεύεται μόνο γνωστά edge paths και να απορρίπτει client-controlled values που υποτίθεται ότι γράφει ο proxy.

### 2. cache keys και Vary

Cache key αποφασίζει ποια requests μοιράζονται response. Έλεγξε host, path, query, headers, cookies, encoding, auth state και `Vary` ώστε private ή attacker-influenced response να μη χρησιμοποιείται σε άλλο context.

### 3. header normalization και forwarding

Edge και origin μπορεί να χειρίζονται duplicates, whitespace ή hop-by-hop headers διαφορετικά. Όρισε canonical policy end-to-end και μην παίρνεις access decision από header που client μπορεί να inject/preserve.

### 4. origin authentication και shielding

Private origin πρέπει να δέχεται μόνο intended edge/shield traffic και όπου γίνεται να authenticate τη σχέση. Συνδύασε network restrictions με service/TLS identity αντί να βασίζεσαι αποκλειστικά σε εύθραυστα IP lists.

### 5. signed URLs και cookies

Signed URL/cookie δίνει περιορισμένη authority για content. Δέσε signature με resource/path, expiry, audience/context και key version και απόφυγε broad wildcards.

### 6. cache poisoning classes

Cache poisoning είναι πρόβλημα state integrity όταν attacker-influenced response αποθηκεύεται κάτω από key άλλων users. Δοκίμασε μόνο synthetic content και έλεγξε unkeyed inputs, error caching και purge.

### 7. edge compute και request mutation

Edge functions είναι μέρος του application security boundary όταν κάνουν auth, redirects ή transformations. Χρειάζονται code review, least privilege, secret isolation, versioned deploy και logs όπως backend service.

### 8. purge και incident response

Origin fix δεν αφαιρεί ήδη cached unsafe content. IR χρειάζεται authenticated purge, scoped invalidation, propagation evidence, rollback και verification από διαφορετικά edges.

## Engineering focus

Μετέτρεψε κάθε σημαντικό claim σε security invariant και regression test. Προτίμησε controls που μειώνουν authority, κάνουν explicit το state και αφήνουν αρκετή telemetry για root-cause analysis.

## Μοτίβα αστοχίας

- **Confused deputy:** privileged component ενεργεί για caller χωρίς επαρκή έλεγχο authority/context.
- **Identity/context confusion:** issuer, subject, tenant, role, origin, audience ή resource χρησιμοποιείται σε λάθος security context.
- **State/replay failure:** valid state γίνεται δεκτό όταν είναι stale, duplicated, revoked, reordered ή σε λάθος workflow step.
- **Parser mismatch:** δύο layers ερμηνεύουν διαφορετικά το ίδιο input/configuration.
- **Excess authority:** service, process, token, key ή admin role έχει περισσότερα permissions από όσα χρειάζεται.
- **Telemetry gap:** δεν καταγράφεται αρκετό actor/resource/policy/result context ώστε να γίνει αξιόπιστο investigation.

## Αμυντικό checklist

1. Γράψε το security invariant πριν από το test.
2. Μείωσε permissions/capabilities και lifetime όσο γίνεται.
3. Κάνε validation στο component που παίρνει την τελική security απόφαση.
4. Δέσε identity/state με σωστό tenant, resource, audience, origin ή protocol phase.
5. Βάλε explicit schemas, allowlists, resource limits και ασφαλή failure behavior.
6. Κατέγραψε actor, resource, operation, policy/version και result χωρίς secrets.
7. Προετοίμασε rollback/recovery πριν από state-changing lab.

## Καθοδηγούμενο εργαστήριο

### Lab 1 — Design a local reverse-proxy lab with two cache variants and verify that private data never enters a shared cache.


### Lab 2 — Write an origin-access policy that distinguishes traffic from the trusted edge from direct internet requests.


### Lab 3 — Create a header-trust matrix showing which layer owns client IP, scheme, host and authenticated identity.

Για κάθε lab χρησιμοποίησε owned/synthetic inputs και κράτησε objective, scope, version, expected/observed behavior, cleanup, remediation και regression result σύμφωνα με τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md).

## Evidence που αξίζει να κρατήσεις

- version/build και σχετικό configuration χωρίς secrets,
- μικρό διάγραμμα trust boundaries και data/state flow,
- sanitized logs, traces ή packet metadata,
- ακριβές test input με synthetic values,
- before/after αποτέλεσμα remediation,
- limitations και μη ελεγμένες υποθέσεις.

## Συχνά λάθη

- Αντιγραφή command χωρίς κατανόηση του mechanism.
- Χρήση production/τρίτου συστήματος ενώ αρκεί localhost ή synthetic data.
- Σύγχυση authentication με authorization, encryption με trust ή signature με safety.
- Θεώρηση ενός alert ως οριστικής απόδειξης.
- Παράβλεψη version, timing, identity context, parser behavior ή recovery.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary;
2. Ποιο state/identity μπορεί να γίνει stale ή να χρησιμοποιηθεί σε λάθος context;
3. Ποιο evidence θα σε έκανε να απορρίψεις την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά authority/blast radius;
5. Πώς θα κάνεις ασφαλές retest μετά τη remediation;

## Πλήρες αγγλικό μάθημα

[English Module 126](../../English/02-Recon-Pentesting-Web-and-AppSec/126-CDN-Reverse-Proxy-Cache-and-Edge-Security.md)

## Επόμενα μαθήματα

Σχετικά modules: **013, 014, 041, 052, 069, 104, 124**. Από το κύριο menu επίλεξε **Αναζήτηση μαθημάτων** για να βρεις σχετικά θέματα σε όλο το project.

---

# Serialization, Deserialization και Parser Security

> **Ελληνική έκδοση — Μάθημα 127.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands παραμένουν στα Αγγλικά όπου αυτό αυξάνει την ακρίβεια.

Το deserialization είναι parsing untrusted data. Εστίασε σε schemas, canonicalization, duplicate fields, resource limits και safe object reconstruction.

> **Όριο εξουσιοδοτημένης χρήσης:** Κάνε πρακτικές δοκιμές μόνο σε συστήματα, κώδικα, λογαριασμούς, captures και lab environments που σου ανήκουν ή για τα οποία έχεις ρητή άδεια. Προτίμησε localhost, synthetic data, disposable VMs/containers και read-only analysis.

## Μαθησιακοί στόχοι

Στο τέλος πρέπει να μπορείς να:

- εξηγήσεις το **serialization versus object graphs** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **schema validation and canonical forms** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **JSON, XML, YAML and binary formats** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **polymorphic type handling** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **unsafe object reconstruction** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **parser differentials and duplicate fields** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Όρισε ownership/identity, state transition, trust boundary και το ελάχιστο evidence που χρειάζεται για ασφαλή validation.

## Βαθιές τεχνικές έννοιες

### 1. serialization και object graphs

Serialization μετατρέπει structured state σε wire/storage format και deserialization το ξαναχτίζει. Κράτησε external schema πιο απλό από internal object graph ώστε input να μην επιλέγει arbitrary classes/constructors.

### 2. schemas και canonical forms

Explicit schemas ορίζουν types, ranges και compatibility. Canonical representation είναι κρίσιμη όταν data υπογράφονται, γίνονται hash ή συγκρίνονται ώστε διαφορετικά encodings να μη δίνουν διαφορετική security απόφαση.

### 3. JSON, XML, YAML και binary formats

Κάθε format έχει διαφορετικά parser features και resource risks. Απενεργοποίησε unnecessary extensions, βάλε depth/size limits και έλεγξε duplicate/ambiguous fields στα boundaries.

### 4. polymorphic types

Automatic polymorphic deserialization μπορεί να αφήσει input να επιλέξει class. Χρησιμοποίησε explicit discriminator σε στενό allowlist data-only types και ξεχώρισε side effects από parsing.

### 5. unsafe reconstruction

Deserialization δεν πρέπει να εκτελεί arbitrary constructors/hooks με attacker-controlled state. Παράγαγε inert data, validate το και μετά εκτέλεσε authorized business logic.

### 6. parser differentials και duplicate fields

Proxy, validator, signature layer και application parser μπορεί να διαφωνούν για duplicate keys, numbers ή encodings. Πέρασε τα ίδια test bytes από όλα τα layers και σύγκρινε canonical result.

### 7. resource exhaustion

Deep nesting, huge collections, decompression ή expansion μπορεί να καταναλώσει CPU/memory πριν το business validation. Βάλε limits σε size, depth, object count, recursion και processing time.

### 8. safe deserialization patterns

Προτίμησε explicit schemas, allowlisted data types, bounded resources και version-aware migrations. Κράτα parser/version evidence και security regression samples για μελλοντικές library changes.

## Engineering focus

Μετέτρεψε κάθε σημαντικό claim σε security invariant και regression test. Προτίμησε controls που μειώνουν authority, κάνουν explicit το state και αφήνουν αρκετή telemetry για root-cause analysis.

## Μοτίβα αστοχίας

- **Confused deputy:** privileged component ενεργεί για caller χωρίς επαρκή έλεγχο authority/context.
- **Identity/context confusion:** issuer, subject, tenant, role, origin, audience ή resource χρησιμοποιείται σε λάθος security context.
- **State/replay failure:** valid state γίνεται δεκτό όταν είναι stale, duplicated, revoked, reordered ή σε λάθος workflow step.
- **Parser mismatch:** δύο layers ερμηνεύουν διαφορετικά το ίδιο input/configuration.
- **Excess authority:** service, process, token, key ή admin role έχει περισσότερα permissions από όσα χρειάζεται.
- **Telemetry gap:** δεν καταγράφεται αρκετό actor/resource/policy/result context ώστε να γίνει αξιόπιστο investigation.

## Αμυντικό checklist

1. Γράψε το security invariant πριν από το test.
2. Μείωσε permissions/capabilities και lifetime όσο γίνεται.
3. Κάνε validation στο component που παίρνει την τελική security απόφαση.
4. Δέσε identity/state με σωστό tenant, resource, audience, origin ή protocol phase.
5. Βάλε explicit schemas, allowlists, resource limits και ασφαλή failure behavior.
6. Κατέγραψε actor, resource, operation, policy/version και result χωρίς secrets.
7. Προετοίμασε rollback/recovery πριν από state-changing lab.

## Καθοδηγούμενο εργαστήριο

### Lab 1 — Create a toy JSON schema and test missing, duplicated, oversized and wrong-type fields locally.


### Lab 2 — Compare how two safe parsers represent duplicate keys using synthetic data and document the trust implication.


### Lab 3 — Refactor a fictional “deserialize directly into privileged object” design into explicit validated data transfer objects.

Για κάθε lab χρησιμοποίησε owned/synthetic inputs και κράτησε objective, scope, version, expected/observed behavior, cleanup, remediation και regression result σύμφωνα με τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md).

## Evidence που αξίζει να κρατήσεις

- version/build και σχετικό configuration χωρίς secrets,
- μικρό διάγραμμα trust boundaries και data/state flow,
- sanitized logs, traces ή packet metadata,
- ακριβές test input με synthetic values,
- before/after αποτέλεσμα remediation,
- limitations και μη ελεγμένες υποθέσεις.

## Συχνά λάθη

- Αντιγραφή command χωρίς κατανόηση του mechanism.
- Χρήση production/τρίτου συστήματος ενώ αρκεί localhost ή synthetic data.
- Σύγχυση authentication με authorization, encryption με trust ή signature με safety.
- Θεώρηση ενός alert ως οριστικής απόδειξης.
- Παράβλεψη version, timing, identity context, parser behavior ή recovery.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary;
2. Ποιο state/identity μπορεί να γίνει stale ή να χρησιμοποιηθεί σε λάθος context;
3. Ποιο evidence θα σε έκανε να απορρίψεις την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά authority/blast radius;
5. Πώς θα κάνεις ασφαλές retest μετά τη remediation;

## Πλήρες αγγλικό μάθημα

[English Module 127](../../English/02-Recon-Pentesting-Web-and-AppSec/127-Serialization-Deserialization-and-Parser-Security.md)

## Επόμενα μαθήματα

Σχετικά modules: **014, 022, 040, 068, 069, 071, 108**. Από το κύριο menu επίλεξε **Αναζήτηση μαθημάτων** για να βρεις σχετικά θέματα σε όλο το project.

---

# SAML, WS-Federation και Enterprise SSO Internals

> **Ελληνική έκδοση — Μάθημα 128.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands παραμένουν στα Αγγλικά όπου αυτό αυξάνει την ακρίβεια.

Κατανόησε SAML/enterprise SSO με assertions, metadata, signatures, audience, recipient, RelayState, attributes και session lifecycle.

> **Όριο εξουσιοδοτημένης χρήσης:** Κάνε πρακτικές δοκιμές μόνο σε συστήματα, κώδικα, λογαριασμούς, captures και lab environments που σου ανήκουν ή για τα οποία έχεις ρητή άδεια. Προτίμησε localhost, synthetic data, disposable VMs/containers και read-only analysis.

## Μαθησιακοί στόχοι

Στο τέλος πρέπει να μπορείς να:

- εξηγήσεις το **IdP and SP trust roles** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **SAML assertions and conditions** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **browser SSO profiles and bindings** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **metadata and signing keys** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **audience and recipient validation** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **NameID and attribute mapping** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Όρισε ownership/identity, state transition, trust boundary και το ελάχιστο evidence που χρειάζεται για ασφαλή validation.

## Βαθιές τεχνικές έννοιες

### 1. IdP και SP trust

Στο SAML ο Identity Provider εκδίδει assertions και ο Service Provider τα καταναλώνει. Ο SP πρέπει να εμπιστεύεται μόνο configured issuers/keys και να εφαρμόζει δικό του authorization· valid assertion από λάθος tenant/relationship δεν αρκεί.

### 2. assertions και conditions

Assertion περιέχει subject, authentication context, attributes και conditions. Κάνε validation σε issuer, signature, audience, recipient/destination, χρόνο, subject confirmation και expected flow αντί να ελέγχεις μόνο τη signature.

### 3. browser SSO profiles και bindings

Browser SSO μεταφέρει SAML messages μέσω browser με συγκεκριμένα bindings. Παρακολούθησε ποιο state ανήκει στο request, τι μπορεί να επηρεάσει ο browser και πώς ο SP συσχετίζει response με το αρχικό session.

### 4. metadata και signing keys

SAML metadata διανέμει entity IDs, endpoints, certificates και capabilities. Metadata/key rollover είναι high-impact config change και χρειάζεται authenticated distribution, overlap window, audit και tested rollback.

### 5. audience και recipient validation

Audience και recipient/destination εμποδίζουν assertion για ένα service να χρησιμοποιηθεί σε άλλο. Η σύγκριση πρέπει να γίνεται με canonical local configuration, όχι με values που προέρχονται από το incoming request.

### 6. NameID και attribute mapping

Attributes γίνονται local identity/roles μέσω mapping rules. Μην χρησιμοποιείς mutable display name ή email σαν μοναδικό privileged identifier χωρίς explicit collision, case, domain και missing-value policy.

### 7. RelayState και request correlation

RelayState μεταφέρει navigation/application context και δεν πρέπει να γίνεται unvalidated redirect ή authorization source. Κράτησε application state χωριστά από identity proof και συσχέτισε response με το σωστό authentication request.

### 8. logout και session lifetime

SAML logout και local app sessions έχουν διαφορετικό lifecycle. Όρισε ποια local tokens ανακαλούνται, τι γίνεται αν Single Logout αποτύχει και πώς admin τερματίζει sessions σε incident.

## Engineering focus

Μετέτρεψε κάθε σημαντικό claim σε security invariant και regression test. Προτίμησε controls που μειώνουν authority, κάνουν explicit το state και αφήνουν αρκετή telemetry για root-cause analysis.

## Μοτίβα αστοχίας

- **Confused deputy:** privileged component ενεργεί για caller χωρίς επαρκή έλεγχο authority/context.
- **Identity/context confusion:** issuer, subject, tenant, role, origin, audience ή resource χρησιμοποιείται σε λάθος security context.
- **State/replay failure:** valid state γίνεται δεκτό όταν είναι stale, duplicated, revoked, reordered ή σε λάθος workflow step.
- **Parser mismatch:** δύο layers ερμηνεύουν διαφορετικά το ίδιο input/configuration.
- **Excess authority:** service, process, token, key ή admin role έχει περισσότερα permissions από όσα χρειάζεται.
- **Telemetry gap:** δεν καταγράφεται αρκετό actor/resource/policy/result context ώστε να γίνει αξιόπιστο investigation.

## Αμυντικό checklist

1. Γράψε το security invariant πριν από το test.
2. Μείωσε permissions/capabilities και lifetime όσο γίνεται.
3. Κάνε validation στο component που παίρνει την τελική security απόφαση.
4. Δέσε identity/state με σωστό tenant, resource, audience, origin ή protocol phase.
5. Βάλε explicit schemas, allowlists, resource limits και ασφαλή failure behavior.
6. Κατέγραψε actor, resource, operation, policy/version και result χωρίς secrets.
7. Προετοίμασε rollback/recovery πριν από state-changing lab.

## Καθοδηγούμενο εργαστήριο

### Lab 1 — Draw an SP-initiated SSO flow and annotate every signed/unsigned value plus who validates it.


### Lab 2 — Create a fictional assertion-validation checklist and test it against synthetic good/bad assertion descriptions, not real accounts.


### Lab 3 — Model key rollover where old and new IdP signing keys overlap and define safe acceptance windows.

Για κάθε lab χρησιμοποίησε owned/synthetic inputs και κράτησε objective, scope, version, expected/observed behavior, cleanup, remediation και regression result σύμφωνα με τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md).

## Evidence που αξίζει να κρατήσεις

- version/build και σχετικό configuration χωρίς secrets,
- μικρό διάγραμμα trust boundaries και data/state flow,
- sanitized logs, traces ή packet metadata,
- ακριβές test input με synthetic values,
- before/after αποτέλεσμα remediation,
- limitations και μη ελεγμένες υποθέσεις.

## Συχνά λάθη

- Αντιγραφή command χωρίς κατανόηση του mechanism.
- Χρήση production/τρίτου συστήματος ενώ αρκεί localhost ή synthetic data.
- Σύγχυση authentication με authorization, encryption με trust ή signature με safety.
- Θεώρηση ενός alert ως οριστικής απόδειξης.
- Παράβλεψη version, timing, identity context, parser behavior ή recovery.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary;
2. Ποιο state/identity μπορεί να γίνει stale ή να χρησιμοποιηθεί σε λάθος context;
3. Ποιο evidence θα σε έκανε να απορρίψεις την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά authority/blast radius;
5. Πώς θα κάνεις ασφαλές retest μετά τη remediation;

## Πλήρες αγγλικό μάθημα

[English Module 128](../../English/06-Identity-Cryptography-and-Trust/128-SAML-WS-Federation-and-Enterprise-SSO-Internals.md)

## Επόμενα μαθήματα

Σχετικά modules: **021, 032, 039, 072, 092, 093**. Από το κύριο menu επίλεξε **Αναζήτηση μαθημάτων** για να βρεις σχετικά θέματα σε όλο το project.

---

# SCIM, Identity Lifecycle και Provisioning Security

> **Ελληνική έκδοση — Μάθημα 129.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands παραμένουν στα Αγγλικά όπου αυτό αυξάνει την ακρίβεια.

Δες το identity lifecycle πέρα από το login: joiner/mover/leaver, SCIM, groups, deprovisioning, authoritative sources, drift και reconciliation.

> **Όριο εξουσιοδοτημένης χρήσης:** Κάνε πρακτικές δοκιμές μόνο σε συστήματα, κώδικα, λογαριασμούς, captures και lab environments που σου ανήκουν ή για τα οποία έχεις ρητή άδεια. Προτίμησε localhost, synthetic data, disposable VMs/containers και read-only analysis.

## Μαθησιακοί στόχοι

Στο τέλος πρέπει να μπορείς να:

- εξηγήσεις το **identity lifecycle states** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **SCIM resources and schemas** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **provisioning clients and service providers** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **group and role synchronization** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **deprovisioning and disable semantics** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **source-of-truth conflicts** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Όρισε ownership/identity, state transition, trust boundary και το ελάχιστο evidence που χρειάζεται για ασφαλή validation.

## Βαθιές τεχνικές έννοιες

### 1. identity lifecycle states

Provisioning είναι state machine: invited, active, suspended, disabled, deleted και restored καταστάσεις έχουν διαφορετική authority. Όρισε ποια source μπορεί να προκαλέσει κάθε transition και τι downstream access πρέπει να αλλάξει.

### 2. SCIM resources και schemas

SCIM μοντελοποιεί users, groups και extensions. Validate identifiers, mutability, uniqueness και tenant scope αντί να γράφεις κάθε incoming field απευθείας σε privileged directory attributes.

### 3. clients και service providers

SCIM client έχει συνήθως ισχυρή lifecycle authority πάνω στο service provider. Χρησιμοποίησε narrow credentials, strong authentication, environment/tenant scoping και audit για create/update/deactivate.

### 4. group και role synchronization

Group membership μπορεί να μεταφράζεται άμεσα σε roles. Έλεγξε nested groups, defaults, name collisions, propagation delays και αν η εξωτερική source είναι πράγματι authoritative για το συγκεκριμένο privilege.

### 5. deprovision και disable

Offboarding δεν τελειώνει με `active=false`. Χρειάζεται αφαίρεση sessions, tokens, group membership, service access και reconciliation των downstream systems που μπορεί να ήταν offline.

### 6. source-of-truth conflicts

HR, directory, IdP, app και manual admin state μπορεί να διαφωνούν. Όρισε precedence και conflict handling ώστε stale source να μην επανενεργοποιεί user ή privilege.

### 7. pagination, filtering και bulk

Pagination, PATCH και bulk operations δημιουργούν partial-success/retry state. Κράτησε operations idempotent όπου γίνεται, authorization ανά object και αρκετό status για ασφαλές reconciliation.

### 8. telemetry και reconciliation

Periodic reconciliation συγκρίνει intended identity state με πραγματικό application state. Βρες orphan/unmanaged accounts, privilege drift, failed provisioning και last-success timestamps αντί να εμπιστεύεσαι ένα API response.

## Engineering focus

Μετέτρεψε κάθε σημαντικό claim σε security invariant και regression test. Προτίμησε controls που μειώνουν authority, κάνουν explicit το state και αφήνουν αρκετή telemetry για root-cause analysis.

## Μοτίβα αστοχίας

- **Confused deputy:** privileged component ενεργεί για caller χωρίς επαρκή έλεγχο authority/context.
- **Identity/context confusion:** issuer, subject, tenant, role, origin, audience ή resource χρησιμοποιείται σε λάθος security context.
- **State/replay failure:** valid state γίνεται δεκτό όταν είναι stale, duplicated, revoked, reordered ή σε λάθος workflow step.
- **Parser mismatch:** δύο layers ερμηνεύουν διαφορετικά το ίδιο input/configuration.
- **Excess authority:** service, process, token, key ή admin role έχει περισσότερα permissions από όσα χρειάζεται.
- **Telemetry gap:** δεν καταγράφεται αρκετό actor/resource/policy/result context ώστε να γίνει αξιόπιστο investigation.

## Αμυντικό checklist

1. Γράψε το security invariant πριν από το test.
2. Μείωσε permissions/capabilities και lifetime όσο γίνεται.
3. Κάνε validation στο component που παίρνει την τελική security απόφαση.
4. Δέσε identity/state με σωστό tenant, resource, audience, origin ή protocol phase.
5. Βάλε explicit schemas, allowlists, resource limits και ασφαλή failure behavior.
6. Κατέγραψε actor, resource, operation, policy/version και result χωρίς secrets.
7. Προετοίμασε rollback/recovery πριν από state-changing lab.

## Καθοδηγούμενο εργαστήριο

### Lab 1 — Build a synthetic HR→IdP→SaaS lifecycle diagram for joiner/mover/leaver events.


### Lab 2 — Design a SCIM-like local JSON dataset and verify that group changes produce expected least-privilege outcomes.


### Lab 3 — Write a deprovisioning checklist that includes active sessions, API tokens, shared resources and audit evidence.

Για κάθε lab χρησιμοποίησε owned/synthetic inputs και κράτησε objective, scope, version, expected/observed behavior, cleanup, remediation και regression result σύμφωνα με τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md).

## Evidence που αξίζει να κρατήσεις

- version/build και σχετικό configuration χωρίς secrets,
- μικρό διάγραμμα trust boundaries και data/state flow,
- sanitized logs, traces ή packet metadata,
- ακριβές test input με synthetic values,
- before/after αποτέλεσμα remediation,
- limitations και μη ελεγμένες υποθέσεις.

## Συχνά λάθη

- Αντιγραφή command χωρίς κατανόηση του mechanism.
- Χρήση production/τρίτου συστήματος ενώ αρκεί localhost ή synthetic data.
- Σύγχυση authentication με authorization, encryption με trust ή signature με safety.
- Θεώρηση ενός alert ως οριστικής απόδειξης.
- Παράβλεψη version, timing, identity context, parser behavior ή recovery.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary;
2. Ποιο state/identity μπορεί να γίνει stale ή να χρησιμοποιηθεί σε λάθος context;
3. Ποιο evidence θα σε έκανε να απορρίψεις την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά authority/blast radius;
5. Πώς θα κάνεις ασφαλές retest μετά τη remediation;

## Πλήρες αγγλικό μάθημα

[English Module 129](../../English/06-Identity-Cryptography-and-Trust/129-SCIM-Identity-Lifecycle-and-Provisioning-Security.md)

## Επόμενα μαθήματα

Σχετικά modules: **021, 039, 042, 059, 092, 093, 128**. Από το κύριο menu επίλεξε **Αναζήτηση μαθημάτων** για να βρεις σχετικά θέματα σε όλο το project.

---

# PAM, Just-in-Time Access, JEA και Privileged Access Engineering

> **Ελληνική έκδοση — Μάθημα 130.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands παραμένουν στα Αγγλικά όπου αυτό αυξάνει την ακρίβεια.

Η privileged πρόσβαση πρέπει να είναι σύντομη, ελεγχόμενη και attributable. Μελέτησε PAM, JIT/JEA, session controls και break-glass design.

> **Όριο εξουσιοδοτημένης χρήσης:** Κάνε πρακτικές δοκιμές μόνο σε συστήματα, κώδικα, λογαριασμούς, captures και lab environments που σου ανήκουν ή για τα οποία έχεις ρητή άδεια. Προτίμησε localhost, synthetic data, disposable VMs/containers και read-only analysis.

## Μαθησιακοί στόχοι

Στο τέλος πρέπει να μπορείς να:

- εξηγήσεις το **privileged identity separation** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **vaulting versus ephemeral credentials** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **just-in-time and just-enough access** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **approval and policy workflows** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **session recording and command context** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **break-glass accounts** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Όρισε ownership/identity, state transition, trust boundary και το ελάχιστο evidence που χρειάζεται για ασφαλή validation.

## Βαθιές τεχνικές έννοιες

### 1. privileged identity separation

Administrative work πρέπει να γίνεται με ξεχωριστή identity από email/browsing/development. Αυτό μειώνει credential exposure και κάνει privileged actions πιο εύκολα σε attribution, restriction και monitoring.

### 2. vaulting έναντι ephemeral access

Vaulting προστατεύει long-lived secrets αλλά δεν αφαιρεί lifecycle risk. Short-lived/ephemeral credentials μειώνουν standing privilege όταν το target platform και το recovery model το επιτρέπουν.

### 3. JIT και JEA

Just-In-Time περιορίζει διάρκεια elevation και Just Enough Administration περιορίζει operations. Ο συνδυασμός μειώνει τόσο το χρονικό παράθυρο όσο και το blast radius του privilege.

### 4. approval και policy workflows

Elevation approval πρέπει να δένεται με identity, target, role, reason και duration. Ticket ή approval που μπορεί να επαναχρησιμοποιηθεί για άλλο resource δεν είναι ισχυρό authorization context.

### 5. session recording και command context

Privileged-session recording βοηθά accountability αλλά μπορεί να καταγράψει secrets. Κράτησε actor, target, action και time context με κατάλληλο redaction, retention και access control.

### 6. break-glass access

Emergency account πρέπει να λειτουργεί όταν το normal identity plane αποτύχει, άρα να μη βασίζεται στο ίδιο dependency. Προστάτεψέ το offline/strongly, monitor κάθε χρήση και rotate/reseal μετά από activation.

### 7. de-escalation και expiry

Privilege πρέπει να λήγει αυτόματα και να αφαιρεί derived sessions/tokens όπου γίνεται. Επαλήθευσε effective permissions μετά το expiry και όχι μόνο ότι αφαιρέθηκε ένα group membership.

### 8. service και administrator boundaries

Human admins και workload identities χρειάζονται διαφορετικό lifecycle. Απόφυγε shared accounts, interactive χρήση service credentials και service principals με broad tenant-wide permissions.

## Engineering focus

Μετέτρεψε κάθε σημαντικό claim σε security invariant και regression test. Προτίμησε controls που μειώνουν authority, κάνουν explicit το state και αφήνουν αρκετή telemetry για root-cause analysis.

## Μοτίβα αστοχίας

- **Confused deputy:** privileged component ενεργεί για caller χωρίς επαρκή έλεγχο authority/context.
- **Identity/context confusion:** issuer, subject, tenant, role, origin, audience ή resource χρησιμοποιείται σε λάθος security context.
- **State/replay failure:** valid state γίνεται δεκτό όταν είναι stale, duplicated, revoked, reordered ή σε λάθος workflow step.
- **Parser mismatch:** δύο layers ερμηνεύουν διαφορετικά το ίδιο input/configuration.
- **Excess authority:** service, process, token, key ή admin role έχει περισσότερα permissions από όσα χρειάζεται.
- **Telemetry gap:** δεν καταγράφεται αρκετό actor/resource/policy/result context ώστε να γίνει αξιόπιστο investigation.

## Αμυντικό checklist

1. Γράψε το security invariant πριν από το test.
2. Μείωσε permissions/capabilities και lifetime όσο γίνεται.
3. Κάνε validation στο component που παίρνει την τελική security απόφαση.
4. Δέσε identity/state με σωστό tenant, resource, audience, origin ή protocol phase.
5. Βάλε explicit schemas, allowlists, resource limits και ασφαλή failure behavior.
6. Κατέγραψε actor, resource, operation, policy/version και result χωρίς secrets.
7. Προετοίμασε rollback/recovery πριν από state-changing lab.

## Καθοδηγούμενο εργαστήριο

### Lab 1 — Create a fictional admin-task catalog and assign minimum roles, duration and approval conditions.


### Lab 2 — Model a JIT elevation lifecycle from request through expiry and verify what evidence remains afterward.


### Lab 3 — Design a break-glass test plan that proves availability without exposing real emergency credentials.

Για κάθε lab χρησιμοποίησε owned/synthetic inputs και κράτησε objective, scope, version, expected/observed behavior, cleanup, remediation και regression result σύμφωνα με τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md).

## Evidence που αξίζει να κρατήσεις

- version/build και σχετικό configuration χωρίς secrets,
- μικρό διάγραμμα trust boundaries και data/state flow,
- sanitized logs, traces ή packet metadata,
- ακριβές test input με synthetic values,
- before/after αποτέλεσμα remediation,
- limitations και μη ελεγμένες υποθέσεις.

## Συχνά λάθη

- Αντιγραφή command χωρίς κατανόηση του mechanism.
- Χρήση production/τρίτου συστήματος ενώ αρκεί localhost ή synthetic data.
- Σύγχυση authentication με authorization, encryption με trust ή signature με safety.
- Θεώρηση ενός alert ως οριστικής απόδειξης.
- Παράβλεψη version, timing, identity context, parser behavior ή recovery.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary;
2. Ποιο state/identity μπορεί να γίνει stale ή να χρησιμοποιηθεί σε λάθος context;
3. Ποιο evidence θα σε έκανε να απορρίψεις την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά authority/blast radius;
5. Πώς θα κάνεις ασφαλές retest μετά τη remediation;

## Πλήρες αγγλικό μάθημα

[English Module 130](../../English/06-Identity-Cryptography-and-Trust/130-PAM-Just-in-Time-Access-JEA-and-Privileged-Access-Engineering.md)

## Επόμενα μαθήματα

Σχετικά modules: **021, 032, 042, 049, 059, 072, 093**. Από το κύριο menu επίλεξε **Αναζήτηση μαθημάτων** για να βρεις σχετικά θέματα σε όλο το project.

---

# WebAuthn, FIDO2 και Passkey Internals

> **Ελληνική έκδοση — Μάθημα 131.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands παραμένουν στα Αγγλικά όπου αυτό αυξάνει την ακρίβεια.

Κατανόησε WebAuthn/FIDO2/passkeys σε επίπεδο protocol: RP ID, origin binding, challenges, authenticators, user verification, attestation και recovery.

> **Όριο εξουσιοδοτημένης χρήσης:** Κάνε πρακτικές δοκιμές μόνο σε συστήματα, κώδικα, λογαριασμούς, captures και lab environments που σου ανήκουν ή για τα οποία έχεις ρητή άδεια. Προτίμησε localhost, synthetic data, disposable VMs/containers και read-only analysis.

## Μαθησιακοί στόχοι

Στο τέλος πρέπει να μπορείς να:

- εξηγήσεις το **WebAuthn ceremony roles** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **Relying Party ID and origin binding** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **credential creation and assertions** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **authenticator data and counters** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **user presence versus user verification** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **discoverable/syncable credentials** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Όρισε ownership/identity, state transition, trust boundary και το ελάχιστο evidence που χρειάζεται για ασφαλή validation.

## Βαθιές τεχνικές έννοιες

### 1. ceremony roles

WebAuthn περιλαμβάνει relying party, browser/client, authenticator και user. Το protocol δένει αυτούς τους actors με origin/RP context και public-key credential χωρίς reusable password secret στον server.

### 2. RP ID και origin binding

RP ID ορίζει domain scope του credential και browser origin δίνει web context. Η σωστή validation εμποδίζει assertion για ένα site να γίνει δεκτό από άσχετο site επειδή απλώς ταιριάζει username.

### 3. creation και assertion

Registration δημιουργεί credential/public key και authentication υπογράφει fresh challenge/context. Challenge πρέπει να είναι unpredictable, single-use, session-bound και να λήγει.

### 4. authenticator data και counters

Authenticator data περιέχει RP binding, flags και state, ενώ μερικοί authenticators έχουν counters. Counter είναι risk signal και όχι universal hard requirement επειδή syncable credentials και authenticators συμπεριφέρονται διαφορετικά.

### 5. user presence έναντι verification

User presence δείχνει αλληλεπίδραση με authenticator, ενώ user verification προσθέτει local PIN/biometric policy. RP πρέπει να ζητά και να επαληθεύει το επίπεδο που απαιτεί το συγκεκριμένο transaction.

### 6. discoverable και syncable credentials

Discoverable credentials επιτρέπουν username-less login και passkeys μπορεί να συγχρονίζονται μεταξύ trusted devices. Threat model πρέπει να περιλαμβάνει recovery, device enrollment, sync provider και notifications.

### 7. attestation και privacy

Attestation δίνει πληροφορία για authenticator provenance αλλά προσθέτει privacy/operational κόστος. Απαίτησέ το μόνο όταν υπάρχει συγκεκριμένη assurance ανάγκη.

### 8. recovery και multi-device lifecycle

Passkeys χρειάζονται credential inventory, new-device onboarding, lost-device response, revocation και recovery. Αδύναμο recovery channel μπορεί να παρακάμψει phishing-resistant authentication.

## Engineering focus

Μετέτρεψε κάθε σημαντικό claim σε security invariant και regression test. Προτίμησε controls που μειώνουν authority, κάνουν explicit το state και αφήνουν αρκετή telemetry για root-cause analysis.

## Μοτίβα αστοχίας

- **Confused deputy:** privileged component ενεργεί για caller χωρίς επαρκή έλεγχο authority/context.
- **Identity/context confusion:** issuer, subject, tenant, role, origin, audience ή resource χρησιμοποιείται σε λάθος security context.
- **State/replay failure:** valid state γίνεται δεκτό όταν είναι stale, duplicated, revoked, reordered ή σε λάθος workflow step.
- **Parser mismatch:** δύο layers ερμηνεύουν διαφορετικά το ίδιο input/configuration.
- **Excess authority:** service, process, token, key ή admin role έχει περισσότερα permissions από όσα χρειάζεται.
- **Telemetry gap:** δεν καταγράφεται αρκετό actor/resource/policy/result context ώστε να γίνει αξιόπιστο investigation.

## Αμυντικό checklist

1. Γράψε το security invariant πριν από το test.
2. Μείωσε permissions/capabilities και lifetime όσο γίνεται.
3. Κάνε validation στο component που παίρνει την τελική security απόφαση.
4. Δέσε identity/state με σωστό tenant, resource, audience, origin ή protocol phase.
5. Βάλε explicit schemas, allowlists, resource limits και ασφαλή failure behavior.
6. Κατέγραψε actor, resource, operation, policy/version και result χωρίς secrets.
7. Προετοίμασε rollback/recovery πριν από state-changing lab.

## Καθοδηγούμενο εργαστήριο

### Lab 1 — Design a WebAuthn registration/authentication sequence diagram with challenge, origin and RP-ID validation points.


### Lab 2 — Compare password+OTP, device-bound WebAuthn and syncable passkeys across phishing resistance, recovery and device loss.


### Lab 3 — Create a recovery threat model for a fictional passkey-only service.

Για κάθε lab χρησιμοποίησε owned/synthetic inputs και κράτησε objective, scope, version, expected/observed behavior, cleanup, remediation και regression result σύμφωνα με τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md).

## Evidence που αξίζει να κρατήσεις

- version/build και σχετικό configuration χωρίς secrets,
- μικρό διάγραμμα trust boundaries και data/state flow,
- sanitized logs, traces ή packet metadata,
- ακριβές test input με synthetic values,
- before/after αποτέλεσμα remediation,
- limitations και μη ελεγμένες υποθέσεις.

## Συχνά λάθη

- Αντιγραφή command χωρίς κατανόηση του mechanism.
- Χρήση production/τρίτου συστήματος ενώ αρκεί localhost ή synthetic data.
- Σύγχυση authentication με authorization, encryption με trust ή signature με safety.
- Θεώρηση ενός alert ως οριστικής απόδειξης.
- Παράβλεψη version, timing, identity context, parser behavior ή recovery.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary;
2. Ποιο state/identity μπορεί να γίνει stale ή να χρησιμοποιηθεί σε λάθος context;
3. Ποιο evidence θα σε έκανε να απορρίψεις την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά authority/blast radius;
5. Πώς θα κάνεις ασφαλές retest μετά τη remediation;

## Πλήρες αγγλικό μάθημα

[English Module 131](../../English/06-Identity-Cryptography-and-Trust/131-WebAuthn-FIDO2-and-Passkey-Internals.md)

## Επόμενα μαθήματα

Σχετικά modules: **021, 039, 049, 078, 092, 100**. Από το κύριο menu επίλεξε **Αναζήτηση μαθημάτων** για να βρεις σχετικά θέματα σε όλο το project.

---

# Secrets Rotation, Envelope Encryption, KMS και HSM Architecture

> **Ελληνική έκδοση — Μάθημα 132.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands παραμένουν στα Αγγλικά όπου αυτό αυξάνει την ακρίβεια.

Σχεδίασε key-management architecture με data keys, KEKs, envelope encryption, KMS/HSM, rotation, grants, audit και recovery.

> **Όριο εξουσιοδοτημένης χρήσης:** Κάνε πρακτικές δοκιμές μόνο σε συστήματα, κώδικα, λογαριασμούς, captures και lab environments που σου ανήκουν ή για τα οποία έχεις ρητή άδεια. Προτίμησε localhost, synthetic data, disposable VMs/containers και read-only analysis.

## Μαθησιακοί στόχοι

Στο τέλος πρέπει να μπορείς να:

- εξηγήσεις το **data keys and key-encryption keys** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **envelope encryption** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **KMS authorization and grants** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **HSM trust boundaries** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **rotation versus re-encryption** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **key versioning and cryptoperiods** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Όρισε ownership/identity, state transition, trust boundary και το ελάχιστο evidence που χρειάζεται για ασφαλή validation.

## Βαθιές τεχνικές έννοιες

### 1. data keys και key-encryption keys

Envelope encryption χωρίζει data-encryption keys από ανώτερα keys που τα προστατεύουν. Έτσι root/wrapping key χρησιμοποιείται λιγότερο και μπορεί να αλλάξει policy χωρίς να ξαναγραφτεί όλο το plaintext.

### 2. envelope encryption

Συνηθισμένο flow: fresh data key, local data encryption και αποθήκευση ciphertext μαζί με wrapped data key. Όπου υποστηρίζεται, δέσε encryption context με tenant/resource για να μη μεταφέρεται wrapped key σε άλλο object.

### 3. KMS authentication και grants

KMS operation είναι high-value authorization decision. Περιορίσε ποια workload identity κάνει encrypt/decrypt/sign/admin και χώρισε key administrators από data users.

### 4. HSM boundaries

HSM απομονώνει key material και crypto operations αλλά δεν διορθώνει λάθος app authorization. Αν broad service μπορεί να ζητήσει arbitrary decrypt, το HSM θα εκτελέσει νόμιμα τη λάθος εξουσιοδοτημένη πράξη.

### 5. rotation έναντι re-encryption

Key rotation μπορεί απλώς να κάνει new writes με νέα version ενώ παλιά ciphertext μένουν με παλιό key. Full re-encryption είναι ξεχωριστό migration με availability, cost, integrity και rollback.

### 6. versioning και cryptoperiods

Keys χρειάζονται stable identifier/version. Cryptoperiod εξαρτάται από algorithm, exposure, sensitivity, usage volume και recovery και δεν υπάρχει ένα universal rotation interval.

### 7. backup και recovery

Key loss μπορεί να είναι τόσο καταστροφικό όσο key theft. Όρισε recoverability, backup protection, approval/quorum και tested recovery με audit.

### 8. audit και key-use attribution

Sensitive key use πρέπει να συνδέεται με workload/user identity, key/version, operation, resource context, policy και time χωρίς να γράφεται plaintext secret/data στα logs.

## Engineering focus

Μετέτρεψε κάθε σημαντικό claim σε security invariant και regression test. Προτίμησε controls που μειώνουν authority, κάνουν explicit το state και αφήνουν αρκετή telemetry για root-cause analysis.

## Μοτίβα αστοχίας

- **Confused deputy:** privileged component ενεργεί για caller χωρίς επαρκή έλεγχο authority/context.
- **Identity/context confusion:** issuer, subject, tenant, role, origin, audience ή resource χρησιμοποιείται σε λάθος security context.
- **State/replay failure:** valid state γίνεται δεκτό όταν είναι stale, duplicated, revoked, reordered ή σε λάθος workflow step.
- **Parser mismatch:** δύο layers ερμηνεύουν διαφορετικά το ίδιο input/configuration.
- **Excess authority:** service, process, token, key ή admin role έχει περισσότερα permissions από όσα χρειάζεται.
- **Telemetry gap:** δεν καταγράφεται αρκετό actor/resource/policy/result context ώστε να γίνει αξιόπιστο investigation.

## Αμυντικό checklist

1. Γράψε το security invariant πριν από το test.
2. Μείωσε permissions/capabilities και lifetime όσο γίνεται.
3. Κάνε validation στο component που παίρνει την τελική security απόφαση.
4. Δέσε identity/state με σωστό tenant, resource, audience, origin ή protocol phase.
5. Βάλε explicit schemas, allowlists, resource limits και ασφαλή failure behavior.
6. Κατέγραψε actor, resource, operation, policy/version και result χωρίς secrets.
7. Προετοίμασε rollback/recovery πριν από state-changing lab.

## Καθοδηγούμενο εργαστήριο

### Lab 1 — Design envelope encryption for a fictional database record and show what is stored beside ciphertext.


### Lab 2 — Create a rotation matrix for API secrets, TLS keys, database encryption keys and signing keys.


### Lab 3 — Model KMS outage and key-revocation scenarios and define what should fail open versus fail closed.

Για κάθε lab χρησιμοποίησε owned/synthetic inputs και κράτησε objective, scope, version, expected/observed behavior, cleanup, remediation και regression result σύμφωνα με τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md).

## Evidence που αξίζει να κρατήσεις

- version/build και σχετικό configuration χωρίς secrets,
- μικρό διάγραμμα trust boundaries και data/state flow,
- sanitized logs, traces ή packet metadata,
- ακριβές test input με synthetic values,
- before/after αποτέλεσμα remediation,
- limitations και μη ελεγμένες υποθέσεις.

## Συχνά λάθη

- Αντιγραφή command χωρίς κατανόηση του mechanism.
- Χρήση production/τρίτου συστήματος ενώ αρκεί localhost ή synthetic data.
- Σύγχυση authentication με authorization, encryption με trust ή signature με safety.
- Θεώρηση ενός alert ως οριστικής απόδειξης.
- Παράβλεψη version, timing, identity context, parser behavior ή recovery.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary;
2. Ποιο state/identity μπορεί να γίνει stale ή να χρησιμοποιηθεί σε λάθος context;
3. Ποιο evidence θα σε έκανε να απορρίψεις την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά authority/blast radius;
5. Πώς θα κάνεις ασφαλές retest μετά τη remediation;

## Πλήρες αγγλικό μάθημα

[English Module 132](../../English/06-Identity-Cryptography-and-Trust/132-Secrets-Rotation-Envelope-Encryption-KMS-and-HSM-Architecture.md)

## Επόμενα μαθήματα

Σχετικά modules: **020, 049, 078, 100, 101, 103, 113**. Από το κύριο menu επίλεξε **Αναζήτηση μαθημάτων** για να βρεις σχετικά θέματα σε όλο το project.

---

# Git Security, Signed Commits, Branch Protection και Repository Trust

> **Ελληνική έκδοση — Μάθημα 133.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands παραμένουν στα Αγγλικά όπου αυτό αυξάνει την ακρίβεια.

Το Git είναι μέρος του software supply chain. Μελέτησε signed commits/tags, branch protection, reviews, history rewriting, secrets και recovery.

> **Όριο εξουσιοδοτημένης χρήσης:** Κάνε πρακτικές δοκιμές μόνο σε συστήματα, κώδικα, λογαριασμούς, captures και lab environments που σου ανήκουν ή για τα οποία έχεις ρητή άδεια. Προτίμησε localhost, synthetic data, disposable VMs/containers και read-only analysis.

## Μαθησιακοί στόχοι

Στο τέλος πρέπει να μπορείς να:

- εξηγήσεις το **Git object integrity and hashes** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **commit/tag signatures** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **branch protection and required reviews** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **CODEOWNERS-style approval concepts** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **force pushes and history rewriting** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **secret exposure and rotation** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Όρισε ownership/identity, state transition, trust boundary και το ελάχιστο evidence που χρειάζεται για ασφαλή validation.

## Βαθιές τεχνικές έννοιες

### 1. Git object integrity και hashes

Git συνδέει content-addressed objects και commit history με hashes. Η συνολική integrity εξαρτάται επίσης από trusted refs, hosting permissions, protected branches και identities που επιτρέπεται να αλλάζουν tags/branches.

### 2. commit και tag signatures

Signed commit/tag δείχνει ότι συγκεκριμένο key ενέκρινε history, αλλά χρειάζεται trusted key ownership/policy. Όρισε ποια events πρέπει να είναι signed και τι κάνει CI όταν verification αποτυγχάνει.

### 3. branch protection και reviews

Protected branches χρειάζονται required review/status checks, restricted force push και controlled merge path. Policy πρέπει να καλύπτει bots και admin bypasses με visible emergency override.

### 4. CODEOWNERS και approval paths

CODEOWNERS κατευθύνει changes σε σωστούς reviewers αλλά δεν είναι μόνο του authorization boundary. Προστάτευσε το ίδιο το ownership file και enforce approvals στο repository platform.

### 5. force pushes και history rewrite

History rewrite αλλάζει commits που μπορεί να χρησιμοποιούν collaborators/releases. Περιορίσε force push σε protected refs και κράτα server/audit evidence ώστε cleanup να ξεχωρίζει από απόπειρα απόκρυψης unauthorized change.

### 6. secret exposure και rotation

Διαγραφή secret από τελευταίο commit δεν ανακαλεί clones/caches/logs. Πρώτα revoke/rotate το credential, έλεγξε χρήση και μετά κάνε history cleanup μόνο αν απαιτείται.

### 7. submodules και dependency refs

Submodule/ref επεκτείνει trust σε άλλο repository/object. Pin reviewed immutable revisions και επιβεβαίωσε provenance ώστε untrusted location να μην αλλάζει privileged build input.

### 8. backup, mirroring και recovery

Repository recovery χρειάζεται mirrors/backups και protected release artifacts. Η αποκατάσταση πρέπει να διατηρεί evidence για unauthorized ref changes και να επαναφέρει known-good branches/tags.

## Engineering focus

Μετέτρεψε κάθε σημαντικό claim σε security invariant και regression test. Προτίμησε controls που μειώνουν authority, κάνουν explicit το state και αφήνουν αρκετή telemetry για root-cause analysis.

## Μοτίβα αστοχίας

- **Confused deputy:** privileged component ενεργεί για caller χωρίς επαρκή έλεγχο authority/context.
- **Identity/context confusion:** issuer, subject, tenant, role, origin, audience ή resource χρησιμοποιείται σε λάθος security context.
- **State/replay failure:** valid state γίνεται δεκτό όταν είναι stale, duplicated, revoked, reordered ή σε λάθος workflow step.
- **Parser mismatch:** δύο layers ερμηνεύουν διαφορετικά το ίδιο input/configuration.
- **Excess authority:** service, process, token, key ή admin role έχει περισσότερα permissions από όσα χρειάζεται.
- **Telemetry gap:** δεν καταγράφεται αρκετό actor/resource/policy/result context ώστε να γίνει αξιόπιστο investigation.

## Αμυντικό checklist

1. Γράψε το security invariant πριν από το test.
2. Μείωσε permissions/capabilities και lifetime όσο γίνεται.
3. Κάνε validation στο component που παίρνει την τελική security απόφαση.
4. Δέσε identity/state με σωστό tenant, resource, audience, origin ή protocol phase.
5. Βάλε explicit schemas, allowlists, resource limits και ασφαλή failure behavior.
6. Κατέγραψε actor, resource, operation, policy/version και result χωρίς secrets.
7. Προετοίμασε rollback/recovery πριν από state-changing lab.

## Καθοδηγούμενο εργαστήριο

### Lab 1 — Create a throwaway local repository, sign a test tag if you have a test key, and document verification outcomes.


### Lab 2 — Design branch-protection rules for a critical library versus a personal experiment.


### Lab 3 — Simulate accidental placement of a fake secret string and practice safe history cleanup plus “rotate the real secret” reasoning.

Για κάθε lab χρησιμοποίησε owned/synthetic inputs και κράτησε objective, scope, version, expected/observed behavior, cleanup, remediation και regression result σύμφωνα με τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md).

## Evidence που αξίζει να κρατήσεις

- version/build και σχετικό configuration χωρίς secrets,
- μικρό διάγραμμα trust boundaries και data/state flow,
- sanitized logs, traces ή packet metadata,
- ακριβές test input με synthetic values,
- before/after αποτέλεσμα remediation,
- limitations και μη ελεγμένες υποθέσεις.

## Συχνά λάθη

- Αντιγραφή command χωρίς κατανόηση του mechanism.
- Χρήση production/τρίτου συστήματος ενώ αρκεί localhost ή synthetic data.
- Σύγχυση authentication με authorization, encryption με trust ή signature με safety.
- Θεώρηση ενός alert ως οριστικής απόδειξης.
- Παράβλεψη version, timing, identity context, parser behavior ή recovery.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary;
2. Ποιο state/identity μπορεί να γίνει stale ή να χρησιμοποιηθεί σε λάθος context;
3. Ποιο evidence θα σε έκανε να απορρίψεις την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά authority/blast radius;
5. Πώς θα κάνεις ασφαλές retest μετά τη remediation;

## Πλήρες αγγλικό μάθημα

[English Module 133](../../English/07-Cloud-Containers-and-Supply-Chain/133-Git-Security-Signed-Commits-Branch-Protection-and-Repository-Trust.md)

## Επόμενα μαθήματα

Σχετικά modules: **022, 029, 040, 084, 097, 098, 109**. Από το κύριο menu επίλεξε **Αναζήτηση μαθημάτων** για να βρεις σχετικά θέματα σε όλο το project.

---

# SBOM, VEX, Provenance και Vulnerability Intelligence Pipelines

> **Ελληνική έκδοση — Μάθημα 134.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands παραμένουν στα Αγγλικά όπου αυτό αυξάνει την ακρίβεια.

Μετέτρεψε SBOM/VEX/provenance από inventory σε decision pipeline με component identity, exploitability context, reachability και policy gates.

> **Όριο εξουσιοδοτημένης χρήσης:** Κάνε πρακτικές δοκιμές μόνο σε συστήματα, κώδικα, λογαριασμούς, captures και lab environments που σου ανήκουν ή για τα οποία έχεις ρητή άδεια. Προτίμησε localhost, synthetic data, disposable VMs/containers και read-only analysis.

## Μαθησιακοί στόχοι

Στο τέλος πρέπει να μπορείς να:

- εξηγήσεις το **SBOM purpose and limitations** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **package identity and version matching** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **transitive dependencies** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **VEX status and justification** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **provenance linkage** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **vulnerability feeds and enrichment** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Όρισε ownership/identity, state transition, trust boundary και το ελάχιστο evidence που χρειάζεται για ασφαλή validation.

## Βαθιές τεχνικές έννοιες

### 1. SBOM purpose και limits

SBOM καταγράφει components και relationships και βοηθά inventory/response. Δεν αποδεικνύει από μόνο του security, exploitability, runtime reachability ή provenance του deployed artifact.

### 2. package identity και version

Component χρειάζεται unambiguous ecosystem/name/version ή package URL και provenance ώστε fork/vendored/rebuilt copies να μην μπερδεύονται. Κακή identity δημιουργεί false matches και blind spots.

### 3. transitive dependencies

Direct packages φέρνουν transitive dependencies. Inventory από resolved build/runtime graph πρέπει να ξεχωρίζει runtime, optional, test, build και bundled relationships.

### 4. VEX status και justification

VEX δηλώνει αν συγκεκριμένη vulnerability επηρεάζει συγκεκριμένο product. Status χρειάζεται evidence, scope, author/time και justification και πρέπει να επανεξετάζεται μετά από architecture/package changes.

### 5. provenance linkage

Σύνδεσε SBOM με verified build provenance για source, builder, inputs, parameters και artifact. Έτσι το IR μπορεί να απαντήσει ποιο build δημιούργησε το deployed binary.

### 6. vulnerability feeds

Advisories και package mappings αλλάζουν. Κράτησε feed source/time και επιβεβαίωσε high-impact matches με authoritative ecosystem/advisory data.

### 7. reachability και exposure

Presence ενός vulnerable library δεν σημαίνει πάντα reachable code path, αλλά reachability analysis έχει blind spots. Χρησιμοποίησέ το για prioritization και όχι σαν μόνιμη εξαίρεση remediation.

### 8. gates και exception lifecycle

CI/deploy gates πρέπει να ορίζουν block/warn/exception. Exception χρειάζεται owner, reason, compensating control, expiry και re-evaluation όταν αλλάζει environment ή exploitability.

## Engineering focus

Μετέτρεψε κάθε σημαντικό claim σε security invariant και regression test. Προτίμησε controls που μειώνουν authority, κάνουν explicit το state και αφήνουν αρκετή telemetry για root-cause analysis.

## Μοτίβα αστοχίας

- **Confused deputy:** privileged component ενεργεί για caller χωρίς επαρκή έλεγχο authority/context.
- **Identity/context confusion:** issuer, subject, tenant, role, origin, audience ή resource χρησιμοποιείται σε λάθος security context.
- **State/replay failure:** valid state γίνεται δεκτό όταν είναι stale, duplicated, revoked, reordered ή σε λάθος workflow step.
- **Parser mismatch:** δύο layers ερμηνεύουν διαφορετικά το ίδιο input/configuration.
- **Excess authority:** service, process, token, key ή admin role έχει περισσότερα permissions από όσα χρειάζεται.
- **Telemetry gap:** δεν καταγράφεται αρκετό actor/resource/policy/result context ώστε να γίνει αξιόπιστο investigation.

## Αμυντικό checklist

1. Γράψε το security invariant πριν από το test.
2. Μείωσε permissions/capabilities και lifetime όσο γίνεται.
3. Κάνε validation στο component που παίρνει την τελική security απόφαση.
4. Δέσε identity/state με σωστό tenant, resource, audience, origin ή protocol phase.
5. Βάλε explicit schemas, allowlists, resource limits και ασφαλή failure behavior.
6. Κατέγραψε actor, resource, operation, policy/version και result χωρίς secrets.
7. Προετοίμασε rollback/recovery πριν από state-changing lab.

## Καθοδηγούμενο εργαστήριο

### Lab 1 — Create a small SBOM-like inventory for a local Python project using only package metadata you own.


### Lab 2 — For three fictional CVEs, write VEX-style affected/not-affected/under-investigation rationales with evidence requirements.


### Lab 3 — Design a pipeline that links source commit → build provenance → artifact → SBOM → deployment inventory.

Για κάθε lab χρησιμοποίησε owned/synthetic inputs και κράτησε objective, scope, version, expected/observed behavior, cleanup, remediation και regression result σύμφωνα με τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md).

## Evidence που αξίζει να κρατήσεις

- version/build και σχετικό configuration χωρίς secrets,
- μικρό διάγραμμα trust boundaries και data/state flow,
- sanitized logs, traces ή packet metadata,
- ακριβές test input με synthetic values,
- before/after αποτέλεσμα remediation,
- limitations και μη ελεγμένες υποθέσεις.

## Συχνά λάθη

- Αντιγραφή command χωρίς κατανόηση του mechanism.
- Χρήση production/τρίτου συστήματος ενώ αρκεί localhost ή synthetic data.
- Σύγχυση authentication με authorization, encryption με trust ή signature με safety.
- Θεώρηση ενός alert ως οριστικής απόδειξης.
- Παράβλεψη version, timing, identity context, parser behavior ή recovery.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary;
2. Ποιο state/identity μπορεί να γίνει stale ή να χρησιμοποιηθεί σε λάθος context;
3. Ποιο evidence θα σε έκανε να απορρίψεις την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά authority/blast radius;
5. Πώς θα κάνεις ασφαλές retest μετά τη remediation;

## Πλήρες αγγλικό μάθημα

[English Module 134](../../English/07-Cloud-Containers-and-Supply-Chain/134-SBOM-VEX-Provenance-and-Vulnerability-Intelligence-Pipelines.md)

## Επόμενα μαθήματα

Σχετικά modules: **005, 022, 050, 084, 097, 098, 109**. Από το κύριο menu επίλεξε **Αναζήτηση μαθημάτων** για να βρεις σχετικά θέματα σε όλο το project.

---

# Kubernetes Admission Control, Policy-as-Code και Runtime Guardrails

> **Ελληνική έκδοση — Μάθημα 135.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands παραμένουν στα Αγγλικά όπου αυτό αυξάνει την ακρίβεια.

Κατανόησε Kubernetes admission lifecycle, validation/mutation, policy-as-code, Pod Security, image trust και runtime drift.

> **Όριο εξουσιοδοτημένης χρήσης:** Κάνε πρακτικές δοκιμές μόνο σε συστήματα, κώδικα, λογαριασμούς, captures και lab environments που σου ανήκουν ή για τα οποία έχεις ρητή άδεια. Προτίμησε localhost, synthetic data, disposable VMs/containers και read-only analysis.

## Μαθησιακοί στόχοι

Στο τέλος πρέπει να μπορείς να:

- εξηγήσεις το **API admission lifecycle** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **mutating versus validating admission** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **Pod Security Standards concepts** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **policy-as-code engines** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **image provenance and allowlists** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **namespace and service-account context** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Όρισε ownership/identity, state transition, trust boundary και το ελάχιστο evidence που χρειάζεται για ασφαλή validation.

## Βαθιές τεχνικές έννοιες

### 1. admission lifecycle

Kubernetes admission εκτελείται μετά authn/authz και πριν αποθήκευση object. Είναι policy point για desired configuration και δεν αντικαθιστά runtime isolation, RBAC ή drift detection.

### 2. mutating έναντι validating admission

Mutating admission αλλάζει/defaults object και validating αποφασίζει accept/reject. Κράτησε mutations predictable και observable ώστε να μη δημιουργούν hidden configuration που δυσκολεύει signatures και debugging.

### 3. Pod Security Standards

Pod Security Standards ορίζουν baseline/restricted expectations για privilege, host namespaces, capabilities, volumes και seccomp. Χρησιμοποίησε narrow documented exceptions μόνο όπου workload το απαιτεί.

### 4. policy engines

Policy engines αξιολογούν manifests με organization rules. Version policies as code, κάνε allow/deny tests σε CI και monitor exceptions ώστε temporary bypass να μη γίνει permanent.

### 5. image provenance και allowlists

Admission μπορεί να επιβάλλει registry, digest, signatures/attestations και provenance. Για high assurance προτίμησε immutable digest και verified provenance αντί για mutable tag.

### 6. namespace και service-account context

Risk ενός manifest αλλάζει με namespace, service account, secrets, network policy και environment. Policy decision πρέπει να περιλαμβάνει το πραγματικό context authority.

### 7. runtime drift

Admission ελέγχει create/update time, αλλά runtime, nodes, credentials και external services μπορούν να drift. Συνδύασέ το με reconciliation και runtime telemetry.

### 8. telemetry και exceptions

Κατέγραψε policy/version, object, namespace, identity, decision και exception. Exception χρειάζεται owner, reason, scope και expiry.

## Engineering focus

Μετέτρεψε κάθε σημαντικό claim σε security invariant και regression test. Προτίμησε controls που μειώνουν authority, κάνουν explicit το state και αφήνουν αρκετή telemetry για root-cause analysis.

## Μοτίβα αστοχίας

- **Confused deputy:** privileged component ενεργεί για caller χωρίς επαρκή έλεγχο authority/context.
- **Identity/context confusion:** issuer, subject, tenant, role, origin, audience ή resource χρησιμοποιείται σε λάθος security context.
- **State/replay failure:** valid state γίνεται δεκτό όταν είναι stale, duplicated, revoked, reordered ή σε λάθος workflow step.
- **Parser mismatch:** δύο layers ερμηνεύουν διαφορετικά το ίδιο input/configuration.
- **Excess authority:** service, process, token, key ή admin role έχει περισσότερα permissions από όσα χρειάζεται.
- **Telemetry gap:** δεν καταγράφεται αρκετό actor/resource/policy/result context ώστε να γίνει αξιόπιστο investigation.

## Αμυντικό checklist

1. Γράψε το security invariant πριν από το test.
2. Μείωσε permissions/capabilities και lifetime όσο γίνεται.
3. Κάνε validation στο component που παίρνει την τελική security απόφαση.
4. Δέσε identity/state με σωστό tenant, resource, audience, origin ή protocol phase.
5. Βάλε explicit schemas, allowlists, resource limits και ασφαλή failure behavior.
6. Κατέγραψε actor, resource, operation, policy/version και result χωρίς secrets.
7. Προετοίμασε rollback/recovery πριν από state-changing lab.

## Καθοδηγούμενο εργαστήριο

### Lab 1 — Write policy requirements for a toy Kubernetes manifest: non-root, restricted capabilities, approved image source and resource limits.


### Lab 2 — Compare admission-time and runtime evidence for the same fictional workload.


### Lab 3 — Create an exception record with owner, reason, expiry and compensating control, then define an automated review trigger.

Για κάθε lab χρησιμοποίησε owned/synthetic inputs και κράτησε objective, scope, version, expected/observed behavior, cleanup, remediation και regression result σύμφωνα με τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md).

## Evidence που αξίζει να κρατήσεις

- version/build και σχετικό configuration χωρίς secrets,
- μικρό διάγραμμα trust boundaries και data/state flow,
- sanitized logs, traces ή packet metadata,
- ακριβές test input με synthetic values,
- before/after αποτέλεσμα remediation,
- limitations και μη ελεγμένες υποθέσεις.

## Συχνά λάθη

- Αντιγραφή command χωρίς κατανόηση του mechanism.
- Χρήση production/τρίτου συστήματος ενώ αρκεί localhost ή synthetic data.
- Σύγχυση authentication με authorization, encryption με trust ή signature με safety.
- Θεώρηση ενός alert ως οριστικής απόδειξης.
- Παράβλεψη version, timing, identity context, parser behavior ή recovery.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary;
2. Ποιο state/identity μπορεί να γίνει stale ή να χρησιμοποιηθεί σε λάθος context;
3. Ποιο evidence θα σε έκανε να απορρίψεις την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά authority/blast radius;
5. Πώς θα κάνεις ασφαλές retest μετά τη remediation;

## Πλήρες αγγλικό μάθημα

[English Module 135](../../English/07-Cloud-Containers-and-Supply-Chain/135-Kubernetes-Admission-Control-Policy-as-Code-and-Runtime-Guardrails.md)

## Επόμενα μαθήματα

Σχετικά modules: **024, 041, 075, 093, 097, 113**. Από το κύριο menu επίλεξε **Αναζήτηση μαθημάτων** για να βρεις σχετικά θέματα σε όλο το project.

---

# Service Mesh, mTLS, Network Policy και East-West Security

> **Ελληνική έκδοση — Μάθημα 136.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands παραμένουν στα Αγγλικά όπου αυτό αυξάνει την ακρίβεια.

Σύνδεσε service mesh, mTLS, workload identity, NetworkPolicy και authorization ώστε να ξεχωρίζεις encryption, reachability και permission.

> **Όριο εξουσιοδοτημένης χρήσης:** Κάνε πρακτικές δοκιμές μόνο σε συστήματα, κώδικα, λογαριασμούς, captures και lab environments που σου ανήκουν ή για τα οποία έχεις ρητή άδεια. Προτίμησε localhost, synthetic data, disposable VMs/containers και read-only analysis.

## Μαθησιακοί στόχοι

Στο τέλος πρέπει να μπορείς να:

- εξηγήσεις το **east-west versus north-south traffic** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **service mesh data/control planes** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **mTLS identity establishment** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **service authorization policy** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **Kubernetes NetworkPolicy concepts** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **sidecar versus ambient interception** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Όρισε ownership/identity, state transition, trust boundary και το ελάχιστο evidence που χρειάζεται για ασφαλή validation.

## Βαθιές τεχνικές έννοιες

### 1. east-west έναντι north-south traffic

North-south αφορά entry/exit ενώ east-west service-to-service. Workloads μέσα στο ίδιο cluster/private network δεν πρέπει να αποκτούν automatic mutual trust.

### 2. data plane και control plane

Mesh data plane επεξεργάζεται traffic και control plane διανέμει identity, routes, certs και policy. Προστάτευσε control-plane authority γιατί μία αλλαγή επηρεάζει πολλά workloads.

### 3. mTLS workload identity

mTLS αυθεντικοποιεί workloads και κρυπτογραφεί traffic αλλά δεν αποφασίζει authorization. Έλεγξε trust-domain/certificate mapping και service policy ξεχωριστά.

### 4. service authorization policy

Policy πρέπει να δένει source workload identity με destination/action και environment/tenant context. Default deny με explicit grants είναι πιο ελέγξιμο από trust λόγω network location.

### 5. Kubernetes NetworkPolicy

NetworkPolicy περιορίζει network reachability και συμπληρώνει identity-aware mesh policy. Επιβεβαίωσε CNI behavior, selectors, egress/DNS και defaults με safe connectivity tests.

### 6. sidecar έναντι ambient models

Sidecar και ambient τοποθετούν enforcement/telemetry σε διαφορετικό σημείο. Threat model πρέπει να δείχνει ποια process/node component μπορεί να δει ή να επηρεάσει traffic και failure mode.

### 7. certificate rotation και trust bundles

Short-lived workload certs μειώνουν exposure αλλά απαιτούν reliable issuance, clocks, overlap και trust-bundle rollout. Δοκίμασε rotation χωρίς broad trust window ή outage.

### 8. telemetry και failure behavior

Mesh logs πρέπει να συνδέουν source/destination identity, policy, protocol και result. Όρισε αν control-plane/policy failure κάνει fail closed ή degrade και κάνε αυτή τη συμπεριφορά observable.

## Engineering focus

Μετέτρεψε κάθε σημαντικό claim σε security invariant και regression test. Προτίμησε controls που μειώνουν authority, κάνουν explicit το state και αφήνουν αρκετή telemetry για root-cause analysis.

## Μοτίβα αστοχίας

- **Confused deputy:** privileged component ενεργεί για caller χωρίς επαρκή έλεγχο authority/context.
- **Identity/context confusion:** issuer, subject, tenant, role, origin, audience ή resource χρησιμοποιείται σε λάθος security context.
- **State/replay failure:** valid state γίνεται δεκτό όταν είναι stale, duplicated, revoked, reordered ή σε λάθος workflow step.
- **Parser mismatch:** δύο layers ερμηνεύουν διαφορετικά το ίδιο input/configuration.
- **Excess authority:** service, process, token, key ή admin role έχει περισσότερα permissions από όσα χρειάζεται.
- **Telemetry gap:** δεν καταγράφεται αρκετό actor/resource/policy/result context ώστε να γίνει αξιόπιστο investigation.

## Αμυντικό checklist

1. Γράψε το security invariant πριν από το test.
2. Μείωσε permissions/capabilities και lifetime όσο γίνεται.
3. Κάνε validation στο component που παίρνει την τελική security απόφαση.
4. Δέσε identity/state με σωστό tenant, resource, audience, origin ή protocol phase.
5. Βάλε explicit schemas, allowlists, resource limits και ασφαλή failure behavior.
6. Κατέγραψε actor, resource, operation, policy/version και result χωρίς secrets.
7. Προετοίμασε rollback/recovery πριν από state-changing lab.

## Καθοδηγούμενο εργαστήριο

### Lab 1 — Draw a three-service architecture and write both network reachability and identity authorization matrices.


### Lab 2 — Model certificate rotation with overlapping trust bundles and define how stale workloads recover.


### Lab 3 — Compare a direct call, sidecar-proxied call and ambient-mesh call in terms of trust boundaries and telemetry.

Για κάθε lab χρησιμοποίησε owned/synthetic inputs και κράτησε objective, scope, version, expected/observed behavior, cleanup, remediation και regression result σύμφωνα με τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md).

## Evidence που αξίζει να κρατήσεις

- version/build και σχετικό configuration χωρίς secrets,
- μικρό διάγραμμα trust boundaries και data/state flow,
- sanitized logs, traces ή packet metadata,
- ακριβές test input με synthetic values,
- before/after αποτέλεσμα remediation,
- limitations και μη ελεγμένες υποθέσεις.

## Συχνά λάθη

- Αντιγραφή command χωρίς κατανόηση του mechanism.
- Χρήση production/τρίτου συστήματος ενώ αρκεί localhost ή synthetic data.
- Σύγχυση authentication με authorization, encryption με trust ή signature με safety.
- Θεώρηση ενός alert ως οριστικής απόδειξης.
- Παράβλεψη version, timing, identity context, parser behavior ή recovery.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary;
2. Ποιο state/identity μπορεί να γίνει stale ή να χρησιμοποιηθεί σε λάθος context;
3. Ποιο evidence θα σε έκανε να απορρίψεις την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά authority/blast radius;
5. Πώς θα κάνεις ασφαλές retest μετά τη remediation;

## Πλήρες αγγλικό μάθημα

[English Module 136](../../English/07-Cloud-Containers-and-Supply-Chain/136-Service-Mesh-mTLS-Network-Policy-and-East-West-Security.md)

## Επόμενα μαθήματα

Σχετικά modules: **021, 024, 075, 093, 113, 135**. Από το κύριο menu επίλεξε **Αναζήτηση μαθημάτων** για να βρεις σχετικά θέματα σε όλο το project.

---

# Cloud Logging, Detection και Cross-Cloud Investigation

> **Ελληνική έκδοση — Μάθημα 137.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands παραμένουν στα Αγγλικά όπου αυτό αυξάνει την ακρίβεια.

Μάθε να ερευνάς cloud events με identity/action/resource/result, central logging, immutable retention, temporary credentials και cross-cloud correlation.

> **Όριο εξουσιοδοτημένης χρήσης:** Κάνε πρακτικές δοκιμές μόνο σε συστήματα, κώδικα, λογαριασμούς, captures και lab environments που σου ανήκουν ή για τα οποία έχεις ρητή άδεια. Προτίμησε localhost, synthetic data, disposable VMs/containers και read-only analysis.

## Μαθησιακοί στόχοι

Στο τέλος πρέπει να μπορείς να:

- εξηγήσεις το **control-plane audit logs** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **identity and token context** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **data-plane versus management-plane telemetry** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **multi-account/project/subscription aggregation** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **log integrity and retention** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **time synchronization and event ordering** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Όρισε ownership/identity, state transition, trust boundary και το ελάχιστο evidence που χρειάζεται για ασφαλή validation.

## Βαθιές τεχνικές έννοιες

### 1. control-plane audit logs

Cloud audit logs καλύπτουν administrative/API changes σε identity, policy, networking και resources. Ενεργοποίησέ τα και κεντρικοποίησέ τα πριν από incident γιατί μη καταγεγραμμένο event δεν ανακατασκευάζεται μετά.

### 2. identity και token context

Cloud event χρειάζεται caller, assumed role/service principal, session/token context, source και target resource/account/tenant. Συσχέτισε temporary identity με parent workload/human.

### 3. data-plane έναντι management-plane logs

Management logs δείχνουν configuration/control και data-plane logs πραγματική data/workload access. Investigation συχνά χρειάζεται και τα δύο για να συνδέσει policy change με επόμενη χρήση.

### 4. central aggregation

Στείλε logs σε independent security account/project με περιορισμένα delete/admin permissions. Έτσι compromise ενός workload δεν διαγράφει εύκολα τη μοναδική evidence copy.

### 5. integrity και retention

Χρησιμοποίησε retention, immutability όπου ταιριάζει, restricted deletion και export verification. Retention πρέπει να λαμβάνει υπόψη detection latency, privacy/legal και cost.

### 6. time synchronization και ordering

Distributed events φτάνουν αργά ή έχουν διαφορετικά timestamps. Κράτησε original και ingestion time και χρησιμοποίησε request/session IDs αντί να θεωρείς display order causal order.

### 7. cross-cloud normalization

Providers/SaaS έχουν διαφορετικά names για principals/resources/actions. Κάνε normalization σε κοινό schema αλλά διατήρησε raw provider fields ώστε να μη χάνεται semantics.

### 8. investigation pivots και evidence preservation

Ξεκίνα από identity, resource, IP, request ID, key ή time window και κάνε pivots σε identity/control plane/workload/network/data access. Document queries/time zone και hash important exports.

## Engineering focus

Μετέτρεψε κάθε σημαντικό claim σε security invariant και regression test. Προτίμησε controls που μειώνουν authority, κάνουν explicit το state και αφήνουν αρκετή telemetry για root-cause analysis.

## Μοτίβα αστοχίας

- **Confused deputy:** privileged component ενεργεί για caller χωρίς επαρκή έλεγχο authority/context.
- **Identity/context confusion:** issuer, subject, tenant, role, origin, audience ή resource χρησιμοποιείται σε λάθος security context.
- **State/replay failure:** valid state γίνεται δεκτό όταν είναι stale, duplicated, revoked, reordered ή σε λάθος workflow step.
- **Parser mismatch:** δύο layers ερμηνεύουν διαφορετικά το ίδιο input/configuration.
- **Excess authority:** service, process, token, key ή admin role έχει περισσότερα permissions από όσα χρειάζεται.
- **Telemetry gap:** δεν καταγράφεται αρκετό actor/resource/policy/result context ώστε να γίνει αξιόπιστο investigation.

## Αμυντικό checklist

1. Γράψε το security invariant πριν από το test.
2. Μείωσε permissions/capabilities και lifetime όσο γίνεται.
3. Κάνε validation στο component που παίρνει την τελική security απόφαση.
4. Δέσε identity/state με σωστό tenant, resource, audience, origin ή protocol phase.
5. Βάλε explicit schemas, allowlists, resource limits και ασφαλή failure behavior.
6. Κατέγραψε actor, resource, operation, policy/version και result χωρίς secrets.
7. Προετοίμασε rollback/recovery πριν από state-changing lab.

## Καθοδηγούμενο εργαστήριο

### Lab 1 — Create a synthetic multi-cloud event dataset and normalize five fields across three provider-style schemas.


### Lab 2 — Build an investigation timeline for a fictional policy change followed by unusual access and remediation.


### Lab 3 — Design retention tiers for high-value audit logs, noisy data-plane logs and forensic snapshots.

Για κάθε lab χρησιμοποίησε owned/synthetic inputs και κράτησε objective, scope, version, expected/observed behavior, cleanup, remediation και regression result σύμφωνα με τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md).

## Evidence που αξίζει να κρατήσεις

- version/build και σχετικό configuration χωρίς secrets,
- μικρό διάγραμμα trust boundaries και data/state flow,
- sanitized logs, traces ή packet metadata,
- ακριβές test input με synthetic values,
- before/after αποτέλεσμα remediation,
- limitations και μη ελεγμένες υποθέσεις.

## Συχνά λάθη

- Αντιγραφή command χωρίς κατανόηση του mechanism.
- Χρήση production/τρίτου συστήματος ενώ αρκεί localhost ή synthetic data.
- Σύγχυση authentication με authorization, encryption με trust ή signature με safety.
- Θεώρηση ενός alert ως οριστικής απόδειξης.
- Παράβλεψη version, timing, identity context, parser behavior ή recovery.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary;
2. Ποιο state/identity μπορεί να γίνει stale ή να χρησιμοποιηθεί σε λάθος context;
3. Ποιο evidence θα σε έκανε να απορρίψεις την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά authority/blast radius;
5. Πώς θα κάνεις ασφαλές retest μετά τη remediation;

## Πλήρες αγγλικό μάθημα

[English Module 137](../../English/08-Blue-Team-IR-Forensics-and-Resilience/137-Cloud-Logging-Detection-and-Cross-Cloud-Investigation.md)

## Επόμενα μαθήματα

Σχετικά modules: **019, 023, 037, 047, 059, 076, 080, 105, 106**. Από το κύριο menu επίλεξε **Αναζήτηση μαθημάτων** για να βρεις σχετικά θέματα σε όλο το project.

---

# RAG, Vector Databases και AI Retrieval Security

> **Ελληνική έκδοση — Μάθημα 138.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands παραμένουν στα Αγγλικά όπου αυτό αυξάνει την ακρίβεια.

Το RAG προσθέτει ingestion, embeddings, vector stores και retrieval ως νέα trust boundaries. Μελέτησε authorization, provenance και indirect prompt injection.

> **Όριο εξουσιοδοτημένης χρήσης:** Κάνε πρακτικές δοκιμές μόνο σε συστήματα, κώδικα, λογαριασμούς, captures και lab environments που σου ανήκουν ή για τα οποία έχεις ρητή άδεια. Προτίμησε localhost, synthetic data, disposable VMs/containers και read-only analysis.

## Μαθησιακοί στόχοι

Στο τέλος πρέπει να μπορείς να:

- εξηγήσεις το **RAG architecture and trust boundaries** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **document ingestion and parsing** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **chunking and embeddings** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **vector-store tenancy and authorization** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **retrieval-time metadata filters** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **indirect prompt injection** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Όρισε ownership/identity, state transition, trust boundary και το ελάχιστο evidence που χρειάζεται για ασφαλή validation.

## Βαθιές τεχνικές έννοιες

### 1. RAG architecture και trust boundaries

RAG έχει ingestion, indexing, retrieval, prompt assembly, model και output layers. Retrieved text είναι untrusted data και δεν πρέπει να αποκτά authority πάνω σε deterministic application/tool policy.

### 2. ingestion και parsing

Documents μπορεί να έχουν malformed/active content, hidden text ή adversarial instructions. Περιορίσε formats, parse σε constrained pipeline, βάλε resource limits και κράτησε source provenance.

### 3. chunking και embeddings

Chunking/embeddings επηρεάζουν retrieval αλλά security labels όπως tenant/classification/source πρέπει να μένουν explicit metadata και όχι να προκύπτουν από similarity.

### 4. tenancy και authorization

Vector similarity δεν είναι authorization. Κάνε server-side tenant/resource filtering πριν το content μπει στο model context και δοκίμασε isolation με δύο synthetic tenants.

### 5. metadata filters

Filters πρέπει να κατασκευάζονται από trusted application state. Μην αφήνεις model/client να διευρύνει tenant, classification ή document-state constraints.

### 6. indirect prompt injection

Retrieved document μπορεί να προσπαθήσει να χειραγωγήσει model/tools. Χώρισε instructions από data, βάλε deterministic authorization έξω από model και ελάχιστα tool permissions.

### 7. source provenance και citations

Κράτησε document ID/version, owner/tenant, classification και source location. Citations πρέπει να προέρχονται από τα πραγματικά retrieved sources και να επιτρέπουν audit.

### 8. poisoning, deletion και reindexing

Poisoned/stale content μπορεί να παραμένει σε embeddings μετά από source change. Χρειάζονται authenticated ingestion, deletion propagation, reindexing, version rollback και incident traceability.

## Engineering focus

Μετέτρεψε κάθε σημαντικό claim σε security invariant και regression test. Προτίμησε controls που μειώνουν authority, κάνουν explicit το state και αφήνουν αρκετή telemetry για root-cause analysis.

## Μοτίβα αστοχίας

- **Confused deputy:** privileged component ενεργεί για caller χωρίς επαρκή έλεγχο authority/context.
- **Identity/context confusion:** issuer, subject, tenant, role, origin, audience ή resource χρησιμοποιείται σε λάθος security context.
- **State/replay failure:** valid state γίνεται δεκτό όταν είναι stale, duplicated, revoked, reordered ή σε λάθος workflow step.
- **Parser mismatch:** δύο layers ερμηνεύουν διαφορετικά το ίδιο input/configuration.
- **Excess authority:** service, process, token, key ή admin role έχει περισσότερα permissions από όσα χρειάζεται.
- **Telemetry gap:** δεν καταγράφεται αρκετό actor/resource/policy/result context ώστε να γίνει αξιόπιστο investigation.

## Αμυντικό checklist

1. Γράψε το security invariant πριν από το test.
2. Μείωσε permissions/capabilities και lifetime όσο γίνεται.
3. Κάνε validation στο component που παίρνει την τελική security απόφαση.
4. Δέσε identity/state με σωστό tenant, resource, audience, origin ή protocol phase.
5. Βάλε explicit schemas, allowlists, resource limits και ασφαλή failure behavior.
6. Κατέγραψε actor, resource, operation, policy/version και result χωρίς secrets.
7. Προετοίμασε rollback/recovery πριν από state-changing lab.

## Καθοδηγούμενο εργαστήριο

### Lab 1 — Build a local toy RAG design on paper with public/sample documents and annotate trust boundaries.


### Lab 2 — Create synthetic “malicious instruction inside a document” examples and write expected safe model behavior without connecting external tools.


### Lab 3 — Design metadata filters for two fictional tenants and test access decisions with a table of allowed/denied retrievals.

Για κάθε lab χρησιμοποίησε owned/synthetic inputs και κράτησε objective, scope, version, expected/observed behavior, cleanup, remediation και regression result σύμφωνα με τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md).

## Evidence που αξίζει να κρατήσεις

- version/build και σχετικό configuration χωρίς secrets,
- μικρό διάγραμμα trust boundaries και data/state flow,
- sanitized logs, traces ή packet metadata,
- ακριβές test input με synthetic values,
- before/after αποτέλεσμα remediation,
- limitations και μη ελεγμένες υποθέσεις.

## Συχνά λάθη

- Αντιγραφή command χωρίς κατανόηση του mechanism.
- Χρήση production/τρίτου συστήματος ενώ αρκεί localhost ή synthetic data.
- Σύγχυση authentication με authorization, encryption με trust ή signature με safety.
- Θεώρηση ενός alert ως οριστικής απόδειξης.
- Παράβλεψη version, timing, identity context, parser behavior ή recovery.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary;
2. Ποιο state/identity μπορεί να γίνει stale ή να χρησιμοποιηθεί σε λάθος context;
3. Ποιο evidence θα σε έκανε να απορρίψεις την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά authority/blast radius;
5. Πώς θα κάνεις ασφαλές retest μετά τη remediation;

## Πλήρες αγγλικό μάθημα

[English Module 138](../../English/09-AI-GRC-Privacy-Data-and-Human-Security/138-RAG-Vector-Databases-and-AI-Retrieval-Security.md)

## Επόμενα μαθήματα

Σχετικά modules: **022, 025, 041, 046, 057, 071, 114**. Από το κύριο menu επίλεξε **Αναζήτηση μαθημάτων** για να βρεις σχετικά θέματα σε όλο το project.

---

# AI-Generated Code, Vibe Coding και Secure Review

> **Ελληνική έκδοση — Μάθημα 139.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands παραμένουν στα Αγγλικά όπου αυτό αυξάνει την ακρίβεια.

Αντιμετώπισε AI-generated/vibe-coded κώδικα σαν contribution από άγνωστο developer: review dependencies, authz, parsing, secrets, negative tests και deployment permissions.

> **Όριο εξουσιοδοτημένης χρήσης:** Κάνε πρακτικές δοκιμές μόνο σε συστήματα, κώδικα, λογαριασμούς, captures και lab environments που σου ανήκουν ή για τα οποία έχεις ρητή άδεια. Προτίμησε localhost, synthetic data, disposable VMs/containers και read-only analysis.

## Μαθησιακοί στόχοι

Στο τέλος πρέπει να μπορείς να:

- εξηγήσεις το **generated-code trust model** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **specification before generation** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **dependency and package verification** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **secret handling and configuration** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **authentication/authorization review** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **input validation and unsafe parsing** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Όρισε ownership/identity, state transition, trust boundary και το ελάχιστο evidence που χρειάζεται για ασφαλή validation.

## Βαθιές τεχνικές έννοιες

### 1. AI-generated code trust model

Αντιμετώπισε generated code σαν untrusted external contribution: μπορεί να είναι plausible αλλά λάθος, stale ή insecure. Human ownership, review, tests και security controls παραμένουν υποχρεωτικά.

### 2. specification πριν από generation

Γράψε invariants, types, trust boundaries, error behavior και constraints πριν ζητήσεις implementation. Έτσι ελέγχεις generated code απέναντι σε specification και όχι απέναντι στο πόσο πειστικό φαίνεται.

### 3. dependency και package verification

Model μπορεί να προτείνει obsolete, typo-squatted ή ανύπαρκτο package. Επιβεβαίωσε package από official ecosystem, pin/lock versions και review transitive dependencies πριν install.

### 4. secrets και configuration

Generated examples συχνά έχουν placeholder secrets, debug mode, broad CORS ή unsafe defaults. Κράτησε secrets έξω από prompts/source και κάνε ξεχωριστό production configuration review.

### 5. authentication και authorization review

Generated handler μπορεί να ελέγχει login αλλά να ξεχνά object/tenant authorization. Έλεγξε subject-resource-action-tenant context και γράψε negative tests με πολλαπλές synthetic identities.

### 6. input validation και parsing

Generated parsers συχνά καλύπτουν μόνο happy path. Όρισε schema, size/depth limits, canonicalization, safe deserialization και σωστό output encoding για κάθε sink.

### 7. generated tests και false confidence

Generated tests μπορεί να αντιγράφουν την ίδια λανθασμένη υπόθεση με τον generated code. Πρόσθεσε independently designed negative/adversarial cases και δες αν test αποτυγχάνει όταν σπάσεις σκόπιμα control σε toy branch.

### 8. human review, provenance και change control

Εφάρμοσε protected branches, review, CI, provenance, dependency/secret scanning και rollback ανεξάρτητα από το ποιος έγραψε κώδικα. AI assistance δεν αλλάζει το ownership του τελικού artifact.

## Engineering focus

Μετέτρεψε κάθε σημαντικό claim σε security invariant και regression test. Προτίμησε controls που μειώνουν authority, κάνουν explicit το state και αφήνουν αρκετή telemetry για root-cause analysis.

## Μοτίβα αστοχίας

- **Confused deputy:** privileged component ενεργεί για caller χωρίς επαρκή έλεγχο authority/context.
- **Identity/context confusion:** issuer, subject, tenant, role, origin, audience ή resource χρησιμοποιείται σε λάθος security context.
- **State/replay failure:** valid state γίνεται δεκτό όταν είναι stale, duplicated, revoked, reordered ή σε λάθος workflow step.
- **Parser mismatch:** δύο layers ερμηνεύουν διαφορετικά το ίδιο input/configuration.
- **Excess authority:** service, process, token, key ή admin role έχει περισσότερα permissions από όσα χρειάζεται.
- **Telemetry gap:** δεν καταγράφεται αρκετό actor/resource/policy/result context ώστε να γίνει αξιόπιστο investigation.

## Αμυντικό checklist

1. Γράψε το security invariant πριν από το test.
2. Μείωσε permissions/capabilities και lifetime όσο γίνεται.
3. Κάνε validation στο component που παίρνει την τελική security απόφαση.
4. Δέσε identity/state με σωστό tenant, resource, audience, origin ή protocol phase.
5. Βάλε explicit schemas, allowlists, resource limits και ασφαλή failure behavior.
6. Κατέγραψε actor, resource, operation, policy/version και result χωρίς secrets.
7. Προετοίμασε rollback/recovery πριν από state-changing lab.

## Καθοδηγούμενο εργαστήριο

### Lab 1 — Take a small local script you own and build a security-review checklist covering inputs, files, subprocesses, network, secrets and dependencies.


### Lab 2 — Write five negative tests for a generated login/API example using fictional data.


### Lab 3 — Compare two AI-generated designs for the same feature and choose the one with smaller authority and fewer dependencies, documenting why.

Για κάθε lab χρησιμοποίησε owned/synthetic inputs και κράτησε objective, scope, version, expected/observed behavior, cleanup, remediation και regression result σύμφωνα με τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md).

## Evidence που αξίζει να κρατήσεις

- version/build και σχετικό configuration χωρίς secrets,
- μικρό διάγραμμα trust boundaries και data/state flow,
- sanitized logs, traces ή packet metadata,
- ακριβές test input με synthetic values,
- before/after αποτέλεσμα remediation,
- limitations και μη ελεγμένες υποθέσεις.

## Συχνά λάθη

- Αντιγραφή command χωρίς κατανόηση του mechanism.
- Χρήση production/τρίτου συστήματος ενώ αρκεί localhost ή synthetic data.
- Σύγχυση authentication με authorization, encryption με trust ή signature με safety.
- Θεώρηση ενός alert ως οριστικής απόδειξης.
- Παράβλεψη version, timing, identity context, parser behavior ή recovery.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary;
2. Ποιο state/identity μπορεί να γίνει stale ή να χρησιμοποιηθεί σε λάθος context;
3. Ποιο evidence θα σε έκανε να απορρίψεις την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά authority/blast radius;
5. Πώς θα κάνεις ασφαλές retest μετά τη remediation;

## Πλήρες αγγλικό μάθημα

[English Module 139](../../English/09-AI-GRC-Privacy-Data-and-Human-Security/139-AI-Generated-Code-Vibe-Coding-and-Secure-Review.md)

## Επόμενα μαθήματα

Σχετικά modules: **022, 025, 036, 040, 041, 046, 097, 098, 108, 109**. Από το κύριο menu επίλεξε **Αναζήτηση μαθημάτων** για να βρεις σχετικά θέματα σε όλο το project.

---

# Advanced Authorized Labs III: Modern Protocols, Identity, Platforms και AI Security

> **Ελληνική έκδοση — Μάθημα 140.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands παραμένουν στα Αγγλικά όπου αυτό αυξάνει την ακρίβεια.

Εφάρμοσε τα νέα θέματα σε advanced authorized labs με localhost, synthetic identities/data, disposable environments, evidence και remediation retest.

> **Όριο εξουσιοδοτημένης χρήσης:** Κάνε πρακτικές δοκιμές μόνο σε συστήματα, κώδικα, λογαριασμούς, captures και lab environments που σου ανήκουν ή για τα οποία έχεις ρητή άδεια. Προτίμησε localhost, synthetic data, disposable VMs/containers και read-only analysis.

## Μαθησιακοί στόχοι

Στο τέλος πρέπει να μπορείς να:

- εξηγήσεις το **memory-lifetime lab** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **race-condition and TOCTOU lab** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **IPC/broker authorization lab** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **HTTP/3 and edge trust lab** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **SAML/SCIM lifecycle lab** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **WebAuthn/passkey threat-model lab** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Όρισε ownership/identity, state transition, trust boundary και το ελάχιστο evidence που χρειάζεται για ασφαλή validation.

## Βαθιές τεχνικές έννοιες

### 1. memory-lifetime lab

Σε μικρό owned πρόγραμμα χρησιμοποίησε deliberate lifetime bug και sanitizer. Στόχος είναι allocation, ownership, invalidation, first bad access και code fix—not code execution.

### 2. race-condition και TOCTOU lab

Δημιούργησε toy concurrent workflow με controlled race/check-use gap και διόρθωσέ το με synchronization/atomic operation. Κράτησε repeatable stress case για regression.

### 3. IPC και broker authorization lab

Φτιάξε local low-privilege client και μικρό broker με μία harmless privileged action. Δοκίμασε allowed/denied caller-resource combinations και χρησιμοποίησε trusted peer context.

### 4. HTTP/3 και edge trust lab

Σε disposable/local stack βάλε app πίσω από proxy/edge path και σύγκρινε protocol/forwarding behavior. Επιβεβαίωσε host, identity, authorization και cache consistency χωρίς public-target tests.

### 5. SAML και SCIM lifecycle lab

Με synthetic identities μοντελοποίησε login, attributes, provisioning, role change, disable, session revocation και reconciliation. Μέτρησε πού παραμένει stale access.

### 6. WebAuthn και passkey threat-model lab

Σε development RP ακολούθησε registration, challenge, RP/origin binding, user verification, lost-device recovery και revocation και ξεχώρισε cryptographic controls από account policy.

### 7. Kubernetes policy lab

Σε disposable cluster γράψε μικρή admission/workload policy και known-allow/deny manifests. Κράτησε policy version, identity, object, decision, exception και regression case.

### 8. RAG και AI-code review lab

Με synthetic corpus και μικρό AI-assisted code change έλεγξε tenant filtering, untrusted instructions, provenance, dependencies, authorization και negative tests με lab-scoped tool permissions.

## Engineering focus

Μετέτρεψε κάθε σημαντικό claim σε security invariant και regression test. Προτίμησε controls που μειώνουν authority, κάνουν explicit το state και αφήνουν αρκετή telemetry για root-cause analysis.

## Μοτίβα αστοχίας

- **Confused deputy:** privileged component ενεργεί για caller χωρίς επαρκή έλεγχο authority/context.
- **Identity/context confusion:** issuer, subject, tenant, role, origin, audience ή resource χρησιμοποιείται σε λάθος security context.
- **State/replay failure:** valid state γίνεται δεκτό όταν είναι stale, duplicated, revoked, reordered ή σε λάθος workflow step.
- **Parser mismatch:** δύο layers ερμηνεύουν διαφορετικά το ίδιο input/configuration.
- **Excess authority:** service, process, token, key ή admin role έχει περισσότερα permissions από όσα χρειάζεται.
- **Telemetry gap:** δεν καταγράφεται αρκετό actor/resource/policy/result context ώστε να γίνει αξιόπιστο investigation.

## Αμυντικό checklist

1. Γράψε το security invariant πριν από το test.
2. Μείωσε permissions/capabilities και lifetime όσο γίνεται.
3. Κάνε validation στο component που παίρνει την τελική security απόφαση.
4. Δέσε identity/state με σωστό tenant, resource, audience, origin ή protocol phase.
5. Βάλε explicit schemas, allowlists, resource limits και ασφαλή failure behavior.
6. Κατέγραψε actor, resource, operation, policy/version και result χωρίς secrets.
7. Προετοίμασε rollback/recovery πριν από state-changing lab.

## Καθοδηγούμενο εργαστήριο

### Lab 1 — Complete one systems lab using sanitizers or race detection on code you own.


### Lab 2 — Complete one identity lab using synthetic SAML/SCIM/WebAuthn data and explicit validation rules.


### Lab 3 — Complete one cloud/AI architecture lab with policy matrices, telemetry plan and a retest checklist.

Για κάθε lab χρησιμοποίησε owned/synthetic inputs και κράτησε objective, scope, version, expected/observed behavior, cleanup, remediation και regression result σύμφωνα με τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md).

## Evidence που αξίζει να κρατήσεις

- version/build και σχετικό configuration χωρίς secrets,
- μικρό διάγραμμα trust boundaries και data/state flow,
- sanitized logs, traces ή packet metadata,
- ακριβές test input με synthetic values,
- before/after αποτέλεσμα remediation,
- limitations και μη ελεγμένες υποθέσεις.

## Συχνά λάθη

- Αντιγραφή command χωρίς κατανόηση του mechanism.
- Χρήση production/τρίτου συστήματος ενώ αρκεί localhost ή synthetic data.
- Σύγχυση authentication με authorization, encryption με trust ή signature με safety.
- Θεώρηση ενός alert ως οριστικής απόδειξης.
- Παράβλεψη version, timing, identity context, parser behavior ή recovery.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary;
2. Ποιο state/identity μπορεί να γίνει stale ή να χρησιμοποιηθεί σε λάθος context;
3. Ποιο evidence θα σε έκανε να απορρίψεις την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά authority/blast radius;
5. Πώς θα κάνεις ασφαλές retest μετά τη remediation;

## Πλήρες αγγλικό μάθημα

[English Module 140](../../English/11-Labs-Capstones-and-Career/140-Advanced-Authorized-Labs-III-Modern-Protocols-Identity-Platforms-and-AI-Security.md)

## Επόμενα μαθήματα

Σχετικά modules: **027, 045, 085, 110, 115, 116, 117, 124, 128, 131, 135, 138, 139**. Από το κύριο menu επίλεξε **Αναζήτηση μαθημάτων** για να βρεις σχετικά θέματα σε όλο το project.
