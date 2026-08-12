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
