# CI/CD, Build Provenance, SLSA 1.2 και Artifact Trust

> **Ελληνική έκδοση — Μάθημα 097.** Διατηρούνται οι διεθνείς τεχνικοί όροι όπου είναι ακριβέστεροι και ευκολότεροι στην αναζήτηση.

## Στόχος του μαθήματος

Να κατανοήσεις σε βάθος το **CI/CD, Build Provenance, SLSA 1.2 και Artifact Trust**, να αναγνωρίζεις trust boundaries και failure states και να μπορείς να αποδείξεις ένα συμπέρασμα με ασφαλές, επαναλήψιμο evidence.

> **Όριο εξουσιοδότησης:** Πρακτική μόνο σε συστήματα, λογαριασμούς, κώδικα ή labs που σου ανήκουν ή έχεις ρητή άδεια να ελέγξεις. Προτίμησε localhost, synthetic data και disposable environments.

## Βαθιές τεχνικές έννοιες

### 1. Source control trust

Build trust ξεκινά από repository identities, protected branches, reviews και immutable source revision. Admin bypass ή compromised bot μπορεί να αλλάξει το artifact πριν καν ξεκινήσει build.

### 2. Build isolation

Builder πρέπει να έχει ελάχιστη network/secret authority και clean/reproducible environment. Shared mutable workers αυξάνουν cross-build contamination και secret leakage.

### 3. Provenance

Provenance συνδέει source, builder, inputs, parameters και output artifact. Χρειάζεται authenticated generation και verification από deploy/promotion policy.

### 4. SLSA 1.2

SLSA οργανώνει supply-chain requirements γύρω από build/provenance threats. Χρησιμοποίησέ το ως framework για συγκεκριμένα controls και evidence, όχι σαν badge χωρίς scope.

### 5. Artifact signing

Signature/attestation πρέπει να αφορά immutable artifact digest και trusted signer/workload identity. Keyless/short-lived signing αλλάζει identity lifecycle αλλά δεν αφαιρεί authorization policy.

### 6. Promotion

Build once και promote verified artifact ανά environment μειώνει rebuild drift. Promotion policy πρέπει να ελέγχει digest, provenance, approvals και environment-specific configuration.

### 7. Secrets in CI

CI secrets πρέπει να είναι short-lived/scoped και να μη διατίθενται σε untrusted forks/jobs. Redaction δεν διορθώνει credential που ήδη δόθηκε σε malicious step.

### 8. Verification at deploy

Το deploy boundary πρέπει να επαληθεύει artifact identity/provenance/policy και όχι να εμπιστεύεται απλώς tag ή registry location. Failure behavior και exceptions χρειάζονται audit.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Γράψε πρώτα invariant και expected result, άλλαξε μία μεταβλητή κάθε φορά και κράτησε μόνο το evidence που χρειάζεται.

1. **Draw the source→build→registry→deployment chain for a small project and mark every identity that can change the final artifact** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
2. **Generate a harmless local artifact and a JSON provenance record containing source hash, builder, timestamp, and output digest; verify consistency with a Python script** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
3. **Create a CI hardening checklist that distinguishes source-track controls from build-track controls** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary και ποιος έχει authority;
2. Ποιο state μπορεί να γίνει stale, replayed ή inconsistent;
3. Ποιο evidence θα διέψευδε την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά το blast radius;
5. Πώς θα επαναλάβεις το test με ασφάλεια μετά τη remediation?

## Πλήρες αγγλικό μάθημα

[English Module 097](../../English/07-Cloud-Containers-and-Supply-Chain/97-CICD-Build-Provenance-SLSA-12-and-Artifact-Trust.md)

## Συνέχεια

Χρησιμοποίησε **Αναζήτηση μαθημάτων** ή **Διαδρομές μάθησης** από το κύριο menu για τα σχετικά επόμενα θέματα.
