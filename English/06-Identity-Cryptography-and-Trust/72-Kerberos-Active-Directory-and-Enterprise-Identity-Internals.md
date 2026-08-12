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
