# Package Managers, Registries, Dependencies και Ecosystem Security

> **Ελληνική έκδοση — Μάθημα 098.** Διατηρούνται οι διεθνείς τεχνικοί όροι όπου είναι ακριβέστεροι και ευκολότεροι στην αναζήτηση.

## Στόχος του μαθήματος

Να κατανοήσεις σε βάθος το **Package Managers, Registries, Dependencies και Ecosystem Security**, να αναγνωρίζεις trust boundaries και failure states και να μπορείς να αποδείξεις ένα συμπέρασμα με ασφαλές, επαναλήψιμο evidence.

> **Όριο εξουσιοδότησης:** Πρακτική μόνο σε συστήματα, λογαριασμούς, κώδικα ή labs που σου ανήκουν ή έχεις ρητή άδεια να ελέγξεις. Προτίμησε localhost, synthetic data και disposable environments.

## Βαθιές τεχνικές έννοιες

### 1. Name and namespace trust

Package name δεν αποδεικνύει maintainer ή intended dependency. Verify official ecosystem/source και προστατεύσου από typo/confusion μεταξύ public/private namespaces.

### 2. Semantic versioning limits

SemVer περιγράφει intended compatibility αλλά δεν εγγυάται security ή πραγματική behavior compatibility. Range constraints μπορεί να φέρουν νέο code χωρίς review.

### 3. Lockfiles

Lockfile καταγράφει resolved versions/integrity και βοηθά reproducibility. Πρέπει να review/update μαζί με manifest και να μην παρακάμπτεται από διαφορετικό resolver mode.

### 4. Install/build scripts

Package install hooks εκτελούν code στο developer/CI environment. Περιορίσε scripts, network, secrets και privileges και προτίμησε isolated build.

### 5. Transitive dependencies

Transitive graph αυξάνει maintainers και code που εμπιστεύεσαι. Inventory, SBOM και dependency minimization βοηθούν να βρεις unused ή unexpectedly privileged packages.

### 6. Maintainer and release trust

Account takeover ή malicious release μπορεί να περάσει μέσω legitimate package name. MFA, signed releases/provenance, review και staged update μειώνουν risk.

### 7. Mirrors and proxies

Enterprise proxy μπορεί να cache/allowlist packages αλλά γίνεται δικό του trust boundary. Protect admin, TLS, metadata integrity, retention και upstream sync behavior.

### 8. Response

Σε compromised dependency χρειάζεσαι affected-version inventory, revoke/replace, rebuild from known-good source, rotate exposed secrets και evidence για deployed artifacts.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Γράψε πρώτα invariant και expected result, άλλαξε μία μεταβλητή κάθε φορά και κράτησε μόνο το evidence που χρειάζεται.

1. **Create a dependency inventory for a small harmless Python project and classify direct vs transitive packages** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
2. **Compare reproducibility with and without a lockfile or fully pinned requirements in an isolated virtual environment** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
3. **Write an incident checklist for a compromised package version: identify exposure, builds, credentials, artifacts, and verification steps** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary και ποιος έχει authority;
2. Ποιο state μπορεί να γίνει stale, replayed ή inconsistent;
3. Ποιο evidence θα διέψευδε την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά το blast radius;
5. Πώς θα επαναλάβεις το test με ασφάλεια μετά τη remediation?

## Πλήρες αγγλικό μάθημα

[English Module 098](../../English/07-Cloud-Containers-and-Supply-Chain/98-Package-Managers-Registries-Dependency-and-Ecosystem-Security.md)

## Συνέχεια

Χρησιμοποίησε **Αναζήτηση μαθημάτων** ή **Διαδρομές μάθησης** από το κύριο menu για τα σχετικά επόμενα θέματα.
