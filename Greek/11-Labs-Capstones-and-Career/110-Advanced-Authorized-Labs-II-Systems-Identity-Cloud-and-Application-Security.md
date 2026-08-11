# Advanced Authorized Labs II: Systems, Identity, Cloud και Application Security

> **Ελληνική έκδοση — Μάθημα 110.** Διατηρούνται οι διεθνείς τεχνικοί όροι όπου είναι ακριβέστεροι και ευκολότεροι στην αναζήτηση.

## Στόχος του μαθήματος

Να κατανοήσεις σε βάθος το **Advanced Authorized Labs II: Systems, Identity, Cloud και Application Security**, να αναγνωρίζεις trust boundaries και failure states και να μπορείς να αποδείξεις ένα συμπέρασμα με ασφαλές, επαναλήψιμο evidence.

> **Όριο εξουσιοδότησης:** Πρακτική μόνο σε συστήματα, λογαριασμούς, κώδικα ή labs που σου ανήκουν ή έχεις ρητή άδεια να ελέγξεις. Προτίμησε localhost, synthetic data και disposable environments.

## Βαθιές τεχνικές έννοιες

### 1. Lab architecture

Σχεδίασε disposable environment με σαφές network/identity boundary, snapshots και synthetic data. Κάθε lab πρέπει να έχει ένα measurable invariant και όχι γενικό “hack the box”.

### 2. Evidence package

Κράτησε scope, versions, diagram, test input, logs, before/after state, remediation και regression result. Ένα άλλο άτομο πρέπει να μπορεί να επαναλάβει το συμπέρασμα.

### 3. Identity lab

Χρησιμοποίησε synthetic users/roles/tokens και negative authorization matrix. Μέτρησε revocation, session lifetime και audit context χωρίς πραγματικά credentials.

### 4. Web/API lab

Χρησιμοποίησε local intentionally vulnerable app και synthetic records. Focus σε request parsing, object authorization και safe proof αντί σε public targets.

### 5. Linux isolation lab

Χρησιμοποίησε namespaces/container/VM και παρατήρησε capabilities, mounts, network και policy. Verify denied paths και cleanup χωρίς escape attempts σε shared host.

### 6. Supply-chain lab

Build small artifact από pinned source, create provenance/SBOM και verify digest/policy στο deploy simulation. Inject only harmless metadata mismatch to test fail behavior.

### 7. Detection lab

Generate benign event sequence και ακολούθησε sensor→pipeline→alert. Document missing fields και tune regression fixture.

### 8. Forensics lab

Χρησιμοποίησε prepared disk/log/memory artifacts και build timeline. Preserve hashes/time zones και separate observation from inference.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Γράψε πρώτα invariant και expected result, άλλαξε μία μεταβλητή κάθε φορά και κράτησε μόνο το evidence που χρειάζεται.

1. **Complete any four integrated labs and produce one consistent report template across all of them** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
2. **For one lab, intentionally remove a telemetry source and explain what conclusions are no longer supportable** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
3. **For one lab, change the environment version/configuration and verify whether the regression test still proves the same invariant** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary και ποιος έχει authority;
2. Ποιο state μπορεί να γίνει stale, replayed ή inconsistent;
3. Ποιο evidence θα διέψευδε την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά το blast radius;
5. Πώς θα επαναλάβεις το test με ασφάλεια μετά τη remediation?

## Πλήρες αγγλικό μάθημα

[English Module 110](../../English/11-Labs-Capstones-and-Career/110-Advanced-Authorized-Labs-II-Systems-Identity-Cloud-and-Application-Security.md)

## Συνέχεια

Χρησιμοποίησε **Αναζήτηση μαθημάτων** ή **Διαδρομές μάθησης** από το κύριο menu για τα σχετικά επόμενα θέματα.
