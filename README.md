# Hacking Guide Project

A bilingual, offline cybersecurity learning guide with **140 English modules + 140 Greek modules**, organized into 11 categories and designed to work well in Termux.

## Simple interface

Start the project once with:

```bash
python "Hacking Guide Project.py"
```

After that, normal browsing does **not require commands or command-line options**. Everything is available from numbered menus.

### Home screen

1. Continue the last lesson
2. Search lessons
3. Browse categories
4. Browse popular topics
5. Learning paths
6. Bookmarks
7. Progress and recent lessons
8. Quick guides
9. All lessons
10. Language / Settings
0. Exit

The first run asks whether you want **English** or **Ελληνικά**. You can switch later from the menu.

## Easier search

Open **Search lessons** and choose:

1. Type normal words describing what you need
2. Pick a popular cybersecurity topic by number
3. Reopen a recent search
4. Search English + Greek together
5. Jump directly to a module number

Search results are numbered. Select a number to open the lesson immediately. You do not need to type `--search`, filenames, paths, or module commands.

Popular topics include Termux, networking, web security, APIs, Active Directory/Kerberos, passkeys, cryptography, reverse engineering, memory safety, fuzzing, malware analysis, forensics, cloud, Kubernetes, SOC/detection, incident response, AI/LLM security, OSINT, wireless/RF, firmware and labs.

## Reading lessons

The lesson reader is also number-driven:

1. Next
2. Previous
3. Mark complete / incomplete
4. Add / remove bookmark
5. Search
6. Home
0. Exit

Progress, bookmarks, recent lessons, preferred language and recent searches are stored locally under `~/.hacking-guide-project/state.json`.

## Browse files directly

- [English](English/README.md)
- [Ελληνικά](Greek/README.md)

Each language has the same 140 module numbers and 11 category folders. Every category contains its own `README.md` index, so GitHub also remains easy to browse without running Python.

Advanced command-line options are still available for users who want scripting or automation, but they are not required for normal use. See [CLI Reference](Project-Docs/CLI-REFERENCE.md).

The current release also includes a documented full-project review: [Quality Audit](Project-Docs/QUALITY-AUDIT.md).

## Project policy

- [MIT License](LICENSE.md)
- [Security Policy / Πολιτική Ασφαλείας](.github/SECURITY.md)
- [Contributing](Project-Docs/CONTRIBUTING.md)

> Use the security material only on systems you own or are explicitly authorized to test. Prefer isolated labs, localhost, disposable VMs/containers, synthetic accounts and non-production data.
