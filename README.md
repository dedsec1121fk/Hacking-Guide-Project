<p align="center">
<img src="https://github.com/user-attachments/assets/3a1b4bca-119b-4aac-b91d-3dec22393db5", width="400", height="400">
</p>

<h1 align="center">Hacking Guide</h1>

<h4 align="center">Bilingual offline cybersecurity learning guide for English and Greek, with 140 modules per language, guided learning paths, authorized labs, local search, progress tracking, and a Termux-friendly menu.</h4>

> **English:** Open the sections below to browse the project.
>
> **Ελληνικά:** Άνοιξε τις παρακάτω ενότητες για να περιηγηθείς στο project.

---

# English

- <details>
  <summary><strong>About The Project</strong></summary>

  Hacking Guide Project is a structured cybersecurity learning project designed for offline study, Termux, desktop systems, and authorized lab environments.

  The English edition contains **140 numbered modules** organized into **11 categories**. The Greek edition mirrors the same module numbering and category structure so you can switch languages without losing your place.

  The project covers foundations through advanced material, including networking, Linux, Windows, web and API security, identity, cryptography, cloud, containers, reverse engineering, malware analysis, forensics, detection engineering, mobile security, firmware, AI security, Termux, labs, capstones, and security research methodology.

  **Main entry points:**

  - [English Edition](English/README.md)
  - [Greek Edition / Ελληνικά](Greek/README.md)
  - [Start Here](English/Guides/START-HERE.md)
  - [Study Method](English/Guides/STUDY-METHOD.md)
  - [Authorized Lab Guide](English/Guides/LAB-GUIDE.md)

  </details>

- <details>
  <summary><strong>Quick Start</strong></summary>

  From the project folder, start the interactive interface with:

  ```bash
  python "Hacking Guide Project.py"
  ```

  Normal use is **menu-driven**. You do not need to remember command-line flags, filenames, or module paths.

  On first run, choose **English** or **Ελληνικά**. Your language preference can be changed later from the Settings menu.

  </details>

- <details>
  <summary><strong>Interactive Menu</strong></summary>

  The main interface provides numbered options for:

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

  While reading a lesson, you can move to the next or previous lesson, mark it complete, bookmark it, search again, or return home without remembering commands.

  </details>

- <details>
  <summary><strong>Easy Search</strong></summary>

  Search is available directly from the numbered menu.

  You can:

  - Type normal words or a question-like topic.
  - Choose a popular cybersecurity topic by number.
  - Reopen a recent search.
  - Search English and Greek together.
  - Jump directly to a module number.
  - Open a numbered result immediately.

  Example searches:

  - `Termux SSH`
  - `Kerberos`
  - `SQL injection`
  - `OAuth`
  - `Android permissions`
  - `reverse engineering`
  - `malware analysis`
  - `Kubernetes`
  - `HTTP/3 QUIC`
  - `passkeys`

  The interactive view prioritizes useful lesson results and hides unnecessary internal path/ranking details.

  </details>

- <details>
  <summary><strong>Categories — 140 Modules</strong></summary>

  The English edition is divided into 11 category folders:

  - [Fundamentals & Methodology](English/01-Fundamentals-and-Methodology/README.md) — 7 modules
  - [Recon, Pentesting, Web & AppSec](English/02-Recon-Pentesting-Web-and-AppSec/README.md) — 17 modules
  - [Systems, Malware & Reverse Engineering](English/03-Systems-Malware-and-Reverse-Engineering/README.md) — 27 modules
  - [Networks, Wireless & Internet](English/04-Network-Wireless-and-Internet/README.md) — 13 modules
  - [Mobile, IoT & Hardware](English/05-Mobile-IoT-and-Hardware/README.md) — 9 modules
  - [Identity, Cryptography & Trust](English/06-Identity-Cryptography-and-Trust/README.md) — 18 modules
  - [Cloud, Containers & Supply Chain](English/07-Cloud-Containers-and-Supply-Chain/README.md) — 15 modules
  - [Blue Team, IR & Forensics](English/08-Blue-Team-IR-Forensics-and-Resilience/README.md) — 12 modules
  - [AI, GRC, Privacy & Human Security](English/09-AI-GRC-Privacy-Data-and-Human-Security/README.md) — 10 modules
  - [Termux & Security Automation](English/10-Termux-and-Security-Automation/README.md) — 5 modules
  - [Labs, Capstones & Career](English/11-Labs-Capstones-and-Career/README.md) — 7 modules

  Each category has its own `README.md`, so opening the folder on GitHub immediately shows its lesson index.

  </details>

- <details>
  <summary><strong>Learning Paths</strong></summary>

  You do not have to study all 140 modules in numerical order. The project includes guided paths for different goals and skill levels.

  Paths include areas such as:

  - Beginner foundations
  - Termux
  - Blue Team
  - AppSec
  - Cloud
  - Mobile
  - AI security
  - Governance
  - Career development
  - Advanced security research
  - Reverse engineering
  - Exploit-research foundations
  - Enterprise identity
  - Protocol analysis
  - Detection engineering
  - Internet infrastructure
  - Modern APIs
  - Platform internals
  - Software supply chain
  - Modern cryptography
  - Cloud-native security
  - Code auditing
  - Identity federation
  - Modern transport security
  - Platform security
  - Secure AI development

  Open **Learning Paths** from the interactive menu and select the path by number.

  </details>

- <details>
  <summary><strong>Quick Guides</strong></summary>

  The English edition includes dedicated guides that support the main lessons:

  - [Start Here](English/Guides/START-HERE.md)
  - [Study Method](English/Guides/STUDY-METHOD.md)
  - [Authorized Lab Guide](English/Guides/LAB-GUIDE.md)
  - [Termux Quick Start](English/Guides/TERMUX-QUICKSTART.md)
  - [Reference Cheatsheet](English/Guides/REFERENCE-CHEATSHEET.md)
  - [Advanced Track](English/Guides/ADVANCED-TRACK.md)
  - [Combined Markdown Edition](English/Combined/All-Modules.md)
  - [Combined HTML Edition](English/Combined/All-Modules.html)

  These are also accessible from **Quick Guides** in the Python menu.

  </details>

- <details>
  <summary><strong>Progress, Bookmarks & Recent Lessons</strong></summary>

  Hacking Guide Project remembers your local study state, including:

  - Preferred language
  - Last opened lesson
  - Completed lessons
  - Bookmarks
  - Recently opened lessons
  - Recent searches

  Local state is stored at:

  ```text
  ~/.hacking-guide-project/state.json
  ```

  This state is outside the repository so your study progress does not clutter Git or project files.

  </details>

- <details>
  <summary><strong>Project Structure</strong></summary>

  ```text
  Hacking-Guide-Project/
  ├── README.md
  ├── LICENSE.md
  ├── Hacking Guide Project.py
  ├── manifest.json
  ├── .github/
  │   └── SECURITY.md
  ├── English/
  │   ├── Guides/
  │   ├── Combined/
  │   └── 11 category folders
  ├── Greek/
  │   ├── Guides/
  │   ├── Combined/
  │   └── 11 category folders
  ├── Project-Docs/
  └── scripts/
  ```

  The root is intentionally kept small. Lesson Markdown files stay inside language/category folders instead of filling the repository root.

  </details>

- <details>
  <summary><strong>Project Documentation</strong></summary>

  - [CLI Reference](Project-Docs/CLI-REFERENCE.md)
  - [Contributing](Project-Docs/CONTRIBUTING.md)
  - [Maintenance](Project-Docs/MAINTENANCE.md)
  - [Sources](Project-Docs/SOURCES.md)
  - [Revision Notes](Project-Docs/REVISION-NOTES.md)
  - [Quality Audit](Project-Docs/QUALITY-AUDIT.md)

  Command-line options remain available for scripting and power users, but they are optional for normal use.

  </details>

- <details>
  <summary><strong>License, Security & Responsible Use</strong></summary>

  - [MIT License](LICENSE.md)
  - [Security Policy](.github/SECURITY.md)
  - [Contributing Guidelines](Project-Docs/CONTRIBUTING.md)

  Use the cybersecurity material only on systems you own or are explicitly authorized to test. Prefer localhost, isolated labs, disposable VMs/containers, synthetic accounts, and non-production data.

  The project is designed for education, authorized security testing, defensive engineering, research, and controlled lab practice.

  </details>

---

# Ελληνικά

- <details>
  <summary><strong>Σχετικά Με Το Project</strong></summary>

  Το Hacking Guide Project είναι ένα οργανωμένο project εκμάθησης κυβερνοασφάλειας για offline μελέτη, Termux, desktop συστήματα και εξουσιοδοτημένα εργαστηριακά περιβάλλοντα.

  Η ελληνική έκδοση περιλαμβάνει **140 αριθμημένα μαθήματα** οργανωμένα σε **11 κατηγορίες**. Η αγγλική έκδοση χρησιμοποιεί ακριβώς την ίδια αρίθμηση και δομή κατηγοριών, ώστε να μπορείς να αλλάζεις γλώσσα χωρίς να χάνεις τη θέση σου.

  Το project καλύπτει από βασικές έννοιες μέχρι προχωρημένη ύλη, όπως δίκτυα, Linux, Windows, web και API security, identity, cryptography, cloud, containers, reverse engineering, malware analysis, forensics, detection engineering, mobile security, firmware, AI security, Termux, labs, capstones και security research methodology.

  **Κύρια σημεία εκκίνησης:**

  - [Ελληνική Έκδοση](Greek/README.md)
  - [English Edition](English/README.md)
  - [Ξεκίνα Εδώ](Greek/Guides/START-HERE.md)
  - [Μεθοδολογία Μελέτης](Greek/Guides/STUDY-METHOD.md)
  - [Οδηγός Εξουσιοδοτημένων Labs](Greek/Guides/LAB-GUIDE.md)

  </details>

- <details>
  <summary><strong>Γρήγορη Εκκίνηση</strong></summary>

  Από τον φάκελο του project τρέξε:

  ```bash
  python "Hacking Guide Project.py"
  ```

  Η κανονική χρήση γίνεται **μέσα από αριθμημένα menus**. Δεν χρειάζεται να θυμάσαι command-line flags, filenames ή paths μαθημάτων.

  Στην πρώτη εκκίνηση επιλέγεις **English** ή **Ελληνικά**. Μπορείς να αλλάξεις γλώσσα αργότερα από τις Ρυθμίσεις.

  </details>

- <details>
  <summary><strong>Διαδραστικό Menu</strong></summary>

  Η αρχική οθόνη προσφέρει αριθμημένες επιλογές για:

  1. Συνέχεια από το τελευταίο μάθημα
  2. Αναζήτηση μαθημάτων
  3. Περιήγηση στις κατηγορίες
  4. Δημοφιλή θέματα
  5. Διαδρομές μάθησης
  6. Bookmarks
  7. Πρόοδο και πρόσφατα μαθήματα
  8. Γρήγορους οδηγούς
  9. Όλα τα μαθήματα
  10. Γλώσσα / Ρυθμίσεις
  0. Έξοδο

  Κατά την ανάγνωση ενός μαθήματος μπορείς να πας στο επόμενο ή προηγούμενο, να το σημειώσεις ως ολοκληρωμένο, να το προσθέσεις στα bookmarks, να κάνεις νέα αναζήτηση ή να επιστρέψεις στην αρχική οθόνη.

  </details>

- <details>
  <summary><strong>Εύκολη Αναζήτηση</strong></summary>

  Η αναζήτηση ανοίγει απευθείας από το αριθμημένο menu.

  Μπορείς να:

  - Γράψεις απλές λέξεις ή ένα θέμα όπως θα το περιέγραφες φυσιολογικά.
  - Επιλέξεις δημοφιλές cybersecurity θέμα με αριθμό.
  - Ξανανοίξεις πρόσφατη αναζήτηση.
  - Ψάξεις ταυτόχρονα English + Ελληνικά.
  - Μεταβείς απευθείας σε αριθμό μαθήματος.
  - Ανοίξεις άμεσα ένα αριθμημένο αποτέλεσμα.

  Παραδείγματα:

  - `Termux SSH`
  - `Kerberos`
  - `SQL injection`
  - `OAuth`
  - `Android permissions`
  - `reverse engineering`
  - `malware analysis`
  - `Kubernetes`
  - `HTTP/3 QUIC`
  - `passkeys`

  Η διαδραστική αναζήτηση δίνει προτεραιότητα σε χρήσιμα μαθήματα και κρύβει περιττές τεχνικές πληροφορίες όπως internal paths και ranking scores.

  </details>

- <details>
  <summary><strong>Κατηγορίες — 140 Μαθήματα</strong></summary>

  Η ελληνική έκδοση χωρίζεται σε 11 φακέλους κατηγοριών:

  - [Βάσεις & Μεθοδολογία](Greek/01-Fundamentals-and-Methodology/README.md) — 7 μαθήματα
  - [Recon, Pentesting, Web & AppSec](Greek/02-Recon-Pentesting-Web-and-AppSec/README.md) — 17 μαθήματα
  - [Συστήματα, Malware & Reverse Engineering](Greek/03-Systems-Malware-and-Reverse-Engineering/README.md) — 27 μαθήματα
  - [Δίκτυα, Ασύρματα & Internet](Greek/04-Network-Wireless-and-Internet/README.md) — 13 μαθήματα
  - [Κινητά, IoT & Hardware](Greek/05-Mobile-IoT-and-Hardware/README.md) — 9 μαθήματα
  - [Ταυτότητα, Κρυπτογραφία & Trust](Greek/06-Identity-Cryptography-and-Trust/README.md) — 18 μαθήματα
  - [Cloud, Containers & Supply Chain](Greek/07-Cloud-Containers-and-Supply-Chain/README.md) — 15 μαθήματα
  - [Blue Team, IR & Forensics](Greek/08-Blue-Team-IR-Forensics-and-Resilience/README.md) — 12 μαθήματα
  - [AI, GRC, Ιδιωτικότητα & Human Security](Greek/09-AI-GRC-Privacy-Data-and-Human-Security/README.md) — 10 μαθήματα
  - [Termux & Αυτοματοποίηση Ασφάλειας](Greek/10-Termux-and-Security-Automation/README.md) — 5 μαθήματα
  - [Labs, Capstones & Καριέρα](Greek/11-Labs-Capstones-and-Career/README.md) — 7 μαθήματα

  Κάθε κατηγορία έχει το δικό της `README.md`, οπότε όταν ανοίγεις τον φάκελο στο GitHub εμφανίζεται άμεσα το index των μαθημάτων.

  </details>

- <details>
  <summary><strong>Διαδρομές Μάθησης</strong></summary>

  Δεν χρειάζεται να μελετήσεις και τα 140 μαθήματα αυστηρά με αριθμητική σειρά. Το project διαθέτει οργανωμένες διαδρομές ανάλογα με τον στόχο και το επίπεδό σου.

  Υπάρχουν διαδρομές για θέματα όπως:

  - Βασικές γνώσεις
  - Termux
  - Blue Team
  - AppSec
  - Cloud
  - Mobile
  - AI security
  - Governance
  - Καριέρα
  - Advanced security research
  - Reverse engineering
  - Exploit-research foundations
  - Enterprise identity
  - Protocol analysis
  - Detection engineering
  - Internet infrastructure
  - Modern APIs
  - Platform internals
  - Software supply chain
  - Modern cryptography
  - Cloud-native security
  - Code auditing
  - Identity federation
  - Modern transport security
  - Platform security
  - Secure AI development

  Άνοιξε **Διαδρομές Μάθησης** από το διαδραστικό menu και επίλεξε τη διαδρομή με αριθμό.

  </details>

- <details>
  <summary><strong>Γρήγοροι Οδηγοί</strong></summary>

  Η ελληνική έκδοση περιλαμβάνει ξεχωριστούς οδηγούς που συμπληρώνουν τα μαθήματα:

  - [Ξεκίνα Εδώ](Greek/Guides/START-HERE.md)
  - [Μεθοδολογία Μελέτης](Greek/Guides/STUDY-METHOD.md)
  - [Οδηγός Εξουσιοδοτημένων Labs](Greek/Guides/LAB-GUIDE.md)
  - [Γρήγορη Εκκίνηση Termux](Greek/Guides/TERMUX-QUICKSTART.md)
  - [Cybersecurity Cheatsheet](Greek/Guides/REFERENCE-CHEATSHEET.md)
  - [Advanced Track](Greek/Guides/ADVANCED-TRACK.md)
  - [Όλα Τα Μαθήματα Σε Markdown](Greek/Combined/All-Modules.md)
  - [Όλα Τα Μαθήματα Σε HTML](Greek/Combined/All-Modules.html)

  Οι οδηγοί ανοίγουν επίσης από την επιλογή **Γρήγοροι Οδηγοί** του Python menu.

  </details>

- <details>
  <summary><strong>Πρόοδος, Bookmarks & Πρόσφατα Μαθήματα</strong></summary>

  Το Hacking Guide Project αποθηκεύει τοπικά την κατάσταση της μελέτης σου, όπως:

  - Προτιμώμενη γλώσσα
  - Τελευταίο μάθημα
  - Ολοκληρωμένα μαθήματα
  - Bookmarks
  - Πρόσφατα μαθήματα
  - Πρόσφατες αναζητήσεις

  Η κατάσταση αποθηκεύεται στο:

  ```text
  ~/.hacking-guide-project/state.json
  ```

  Το αρχείο βρίσκεται έξω από το repository ώστε η πρόοδός σου να μην προσθέτει προσωπικά runtime αρχεία στο Git project.

  </details>

- <details>
  <summary><strong>Δομή Του Project</strong></summary>

  ```text
  Hacking-Guide-Project/
  ├── README.md
  ├── LICENSE.md
  ├── Hacking Guide Project.py
  ├── manifest.json
  ├── .github/
  │   └── SECURITY.md
  ├── English/
  │   ├── Guides/
  │   ├── Combined/
  │   └── 11 φάκελοι κατηγοριών
  ├── Greek/
  │   ├── Guides/
  │   ├── Combined/
  │   └── 11 φάκελοι κατηγοριών
  ├── Project-Docs/
  └── scripts/
  ```

  Το root διατηρείται σκόπιμα καθαρό. Τα Markdown αρχεία των μαθημάτων βρίσκονται μέσα στους φακέλους γλώσσας και κατηγορίας αντί να γεμίζουν την αρχική σελίδα του repository.

  </details>

- <details>
  <summary><strong>Τεκμηρίωση Του Project</strong></summary>

  - [CLI Reference](Project-Docs/CLI-REFERENCE.md)
  - [Contributing](Project-Docs/CONTRIBUTING.md)
  - [Maintenance](Project-Docs/MAINTENANCE.md)
  - [Sources](Project-Docs/SOURCES.md)
  - [Revision Notes](Project-Docs/REVISION-NOTES.md)
  - [Quality Audit](Project-Docs/QUALITY-AUDIT.md)

  Τα command-line options παραμένουν διαθέσιμα για scripting και advanced χρήση, αλλά δεν είναι απαραίτητα για την κανονική περιήγηση.

  </details>

- <details>
  <summary><strong>License, Security & Υπεύθυνη Χρήση</strong></summary>

  - [MIT License](LICENSE.md)
  - [Security Policy / Πολιτική Ασφαλείας](.github/SECURITY.md)
  - [Οδηγίες Συνεισφοράς](Project-Docs/CONTRIBUTING.md)

  Χρησιμοποίησε το υλικό κυβερνοασφάλειας μόνο σε συστήματα που σου ανήκουν ή για τα οποία έχεις ξεκάθαρη εξουσιοδότηση να πραγματοποιήσεις δοκιμές. Προτίμησε localhost, απομονωμένα labs, disposable VMs/containers, synthetic accounts και μη παραγωγικά δεδομένα.

  Το project έχει σχεδιαστεί για εκπαίδευση, εξουσιοδοτημένες δοκιμές ασφαλείας, defensive engineering, έρευνα και ελεγχόμενη εργαστηριακή εξάσκηση.

  </details>

---

## Project Links

- [English](English/README.md)
- [Ελληνικά](Greek/README.md)
- [MIT License](LICENSE.md)
- [Security Policy / Πολιτική Ασφαλείας](.github/SECURITY.md)
- [Contributing](Project-Docs/CONTRIBUTING.md)
- [Quality Audit](Project-Docs/QUALITY-AUDIT.md)
