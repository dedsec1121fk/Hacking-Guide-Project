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
