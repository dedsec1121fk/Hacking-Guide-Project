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
