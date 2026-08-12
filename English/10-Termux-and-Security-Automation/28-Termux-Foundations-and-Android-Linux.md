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
