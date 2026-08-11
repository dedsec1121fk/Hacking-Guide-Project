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
