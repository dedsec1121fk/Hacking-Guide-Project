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
