# Threat Emulation, Adversary Simulation και Purple-Team Lab Design

> **Ελληνική έκδοση — Μάθημα 107.** Διατηρούνται οι διεθνείς τεχνικοί όροι όπου είναι ακριβέστεροι και ευκολότεροι στην αναζήτηση.

## Στόχος του μαθήματος

Να κατανοήσεις σε βάθος το **Threat Emulation, Adversary Simulation και Purple-Team Lab Design**, να αναγνωρίζεις trust boundaries και failure states και να μπορείς να αποδείξεις ένα συμπέρασμα με ασφαλές, επαναλήψιμο evidence.

> **Όριο εξουσιοδότησης:** Πρακτική μόνο σε συστήματα, λογαριασμούς, κώδικα ή labs που σου ανήκουν ή έχεις ρητή άδεια να ελέγξεις. Προτίμησε localhost, synthetic data και disposable environments.

## Βαθιές τεχνικές έννοιες

### 1. Objective first

Purple-team test ξεκινά από συγκεκριμένο security/detection objective και όχι από λίστα attacker tools. Γράψε ποια συμπεριφορά θέλεις να δεις, ποια data source πρέπει να την αποτυπώσει και ποιο stop condition υπάρχει.

### 2. Behavior abstraction

Περιέγραψε behavior σε επίπεδο action/effect ώστε να μπορεί να προσομοιωθεί με harmless mechanism. Αυτό επιτρέπει detection validation χωρίς weaponized payload.

### 3. Safety constraints

Scope, production limits, prohibited actions, test accounts, rate και emergency contact πρέπει να είναι γνωστά πριν το execution. Benign marker προτιμάται από πραγματικό credential/data impact.

### 4. ATT&CK mapping

ATT&CK mapping βοηθά κοινή ορολογία αλλά technique ID δεν είναι detection requirement από μόνο του. Δέσε κάθε test με συγκεκριμένο environment behavior και telemetry.

### 5. Detection contract

Για κάθε test γράψε expected events, fields, timestamps, rule/alert και analyst context. Αν λείπει event, ξεχώρισε sensor, pipeline, normalization, rule και routing failure.

### 6. Purple-team loop

Execute harmless behavior, observe, tune control, retest και capture result. Κάθε iteration πρέπει να αφήνει regression fixture ώστε βελτίωση να μην χαθεί.

### 7. Metrics

Χρήσιμα metrics είναι data coverage, alert latency, precision/context completeness και time-to-triage—not απλώς αριθμός techniques “covered”.

### 8. Reporting

Report πρέπει να εξηγεί objective, behavior, evidence, blind spot, remediation και retest. Απόφυγε dramatic attacker narrative που δεν προσθέτει engineering πληροφορία.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Γράψε πρώτα invariant και expected result, άλλαξε μία μεταβλητή κάθε φορά και κράτησε μόνο το evidence που χρειάζεται.

1. **Create a five-test purple-team plan using harmless local behaviors such as file creation, process start, failed login, service restart, and DNS lookup** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
2. **For each test, define ATT&CK mapping only after describing the actual behavior and expected evidence** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
3. **Build a regression sheet that records test version, environment, expected events, alert outcome, and remediation status** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary και ποιος έχει authority;
2. Ποιο state μπορεί να γίνει stale, replayed ή inconsistent;
3. Ποιο evidence θα διέψευδε την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά το blast radius;
5. Πώς θα επαναλάβεις το test με ασφάλεια μετά τη remediation?

## Πλήρες αγγλικό μάθημα

[English Module 107](../../English/08-Blue-Team-IR-Forensics-and-Resilience/107-Threat-Emulation-Adversary-Simulation-and-Purple-Team-Lab-Design.md)

## Συνέχεια

Χρησιμοποίησε **Αναζήτηση μαθημάτων** ή **Διαδρομές μάθησης** από το κύριο menu για τα σχετικά επόμενα θέματα.
