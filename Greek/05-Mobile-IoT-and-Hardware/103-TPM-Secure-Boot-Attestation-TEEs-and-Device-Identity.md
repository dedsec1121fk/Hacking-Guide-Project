# TPM, Secure Boot, Attestation, TEEs και Device Identity

> **Ελληνική έκδοση — Μάθημα 103.** Διατηρούνται οι διεθνείς τεχνικοί όροι όπου είναι ακριβέστεροι και ευκολότεροι στην αναζήτηση.

## Στόχος του μαθήματος

Να κατανοήσεις σε βάθος το **TPM, Secure Boot, Attestation, TEEs και Device Identity**, να αναγνωρίζεις trust boundaries και failure states και να μπορείς να αποδείξεις ένα συμπέρασμα με ασφαλές, επαναλήψιμο evidence.

> **Όριο εξουσιοδότησης:** Πρακτική μόνο σε συστήματα, λογαριασμούς, κώδικα ή labs που σου ανήκουν ή έχεις ρητή άδεια να ελέγξεις. Προτίμησε localhost, synthetic data και disposable environments.

## Βαθιές τεχνικές έννοιες

### 1. Secure Boot

Secure Boot επαληθεύει ότι κάθε boot stage επιτρέπεται από προηγούμενο trusted stage. Key ownership, update policy και recovery mode είναι μέρος του trust chain και όχι μόνο η signature verification.

### 2. Measured boot

Measured boot καταγράφει hashes/configuration σε measurements χωρίς απαραίτητα να μπλοκάρει boot. Το evidence είναι χρήσιμο όταν υπάρχει γνωστό expected state και αξιόπιστος verifier.

### 3. TPM keys

TPM μπορεί να δημιουργεί/seal keys σε platform state και να προστατεύει private operations. Authorization policy, backup/recovery και owner/admin paths καθορίζουν την πραγματική ασφάλεια.

### 4. Attestation

Attestation μεταφέρει signed evidence για measurements/device identity σε verifier. Ο verifier πρέπει να ελέγχει freshness, nonce, expected measurements, certificate chain και policy context.

### 5. TEEs

Trusted Execution Environments απομονώνουν συγκεκριμένο code/data από πιο privileged software υπό συγκεκριμένο threat model. Δεν λύνουν bugs μέσα στο enclave, side channels, availability ή unsafe I/O boundaries.

### 6. Device identity

Hardware-backed device identity μπορεί να δένει enrollment και access με πραγματική συσκευή. Lifecycle χρειάζεται manufacturing provenance, ownership transfer, revocation και replacement.

### 7. Key release

Sealed secret πρέπει να απελευθερώνεται μόνο όταν attested state και identity ικανοποιούν explicit policy. Recovery path δεν πρέπει να γίνει broad bypass της ίδιας policy.

### 8. Lifecycle

Firmware updates, key rollover, motherboard replacement, reset και decommission αλλάζουν measurements/identity. Σχεδίασε transitions πριν το deployment και κράτησε auditable recovery.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Γράψε πρώτα invariant και expected result, άλλαξε μία μεταβλητή κάθε φορά και κράτησε μόνο το evidence που χρειάζεται.

1. **Draw a boot trust chain for a modern laptop or phone using public vendor documentation and distinguish verification from measurement** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
2. **Design an attestation verifier state machine: challenge, evidence, freshness check, identity validation, policy evaluation, decision, logging** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
3. **Create a recovery plan for an application whose encryption key is sealed to hardware state and the motherboard must be replaced** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary και ποιος έχει authority;
2. Ποιο state μπορεί να γίνει stale, replayed ή inconsistent;
3. Ποιο evidence θα διέψευδε την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά το blast radius;
5. Πώς θα επαναλάβεις το test με ασφάλεια μετά τη remediation?

## Πλήρες αγγλικό μάθημα

[English Module 103](../../English/05-Mobile-IoT-and-Hardware/103-TPM-Secure-Boot-Attestation-TEEs-and-Device-Identity.md)

## Συνέχεια

Χρησιμοποίησε **Αναζήτηση μαθημάτων** ή **Διαδρομές μάθησης** από το κύριο menu για τα σχετικά επόμενα θέματα.
