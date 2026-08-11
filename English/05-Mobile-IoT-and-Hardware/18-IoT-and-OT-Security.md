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
