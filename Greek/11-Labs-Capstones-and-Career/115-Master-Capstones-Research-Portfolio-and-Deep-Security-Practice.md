# Master Capstones, Research Portfolio και Deep Security Practice

> **Ελληνική έκδοση — Μάθημα 115.** Διατηρούνται οι διεθνείς τεχνικοί όροι όπου είναι ακριβέστεροι και ευκολότεροι στην αναζήτηση.

## Στόχος του μαθήματος

Να κατανοήσεις σε βάθος το **Master Capstones, Research Portfolio και Deep Security Practice**, να αναγνωρίζεις trust boundaries και failure states και να μπορείς να αποδείξεις ένα συμπέρασμα με ασφαλές, επαναλήψιμο evidence.

> **Όριο εξουσιοδότησης:** Πρακτική μόνο σε συστήματα, λογαριασμούς, κώδικα ή labs που σου ανήκουν ή έχεις ρητή άδεια να ελέγξεις. Προτίμησε localhost, synthetic data και disposable environments.

## Βαθιές τεχνικές έννοιες

### 1. Capstone standard

Capstone πρέπει να έχει σαφές question, scope, architecture, evidence, safe lab, root cause/control και regression/retest. Tool screenshots χωρίς reasoning δεν αρκούν.

### 2. Systems capstone

Επίλεξε owned OS/runtime και αξιολόγησε isolation, identity, memory/runtime hardening και telemetry. Deliverable να συνδέει low-level mechanism με defensive configuration.

### 3. Application capstone

Χτίσε/χρησιμοποίησε local app με synthetic users και κάνε threat model, authorization matrix, input-flow review, findings και fixes με tests.

### 4. Cloud/supply-chain capstone

Δημιούργησε disposable cloud/build pipeline, least-privilege workload identity, provenance/SBOM και policy verification. Include recovery/rotation scenario.

### 5. Detection/forensics capstone

Χρησιμοποίησε benign incident dataset, γράψε detection hypothesis, collect logs, timeline, triage, root cause και regression rule with false-positive notes.

### 6. Research capstone

Αναπαράγαγε bug σε toy/open lab, minimize trigger, explain root cause και produce coordinated-disclosure style report χωρίς weaponization.

### 7. Writing quality

Report πρέπει να ξεχωρίζει observation/inference, να δηλώνει limitations και να έχει enough evidence για independent reproduction. Clear diagrams και concise findings είναι technical skill.

### 8. Portfolio hygiene

Αφαίρεσε secrets, πραγματικά identifiers και third-party data. Δημοσίευσε μόνο labs που έχεις δικαίωμα να μοιραστείς και περιέγραψε ethics/scope μαζί με το technical αποτέλεσμα.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Γράψε πρώτα invariant και expected result, άλλαξε μία μεταβλητή κάθε φορά και κράτησε μόνο το evidence που χρειάζεται.

1. **Complete one capstone from systems/application/cloud/detection/research and have another person reproduce the result from your documentation** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
2. **Create a portfolio index that links each project to the skills and security invariants demonstrated** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
3. **Revisit an early guide lab and redo it using the advanced evidence standard; compare the quality of the old and new conclusions** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary και ποιος έχει authority;
2. Ποιο state μπορεί να γίνει stale, replayed ή inconsistent;
3. Ποιο evidence θα διέψευδε την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά το blast radius;
5. Πώς θα επαναλάβεις το test με ασφάλεια μετά τη remediation?

## Πλήρες αγγλικό μάθημα

[English Module 115](../../English/11-Labs-Capstones-and-Career/115-Master-Capstones-Research-Portfolio-and-Deep-Security-Practice.md)

## Συνέχεια

Χρησιμοποίησε **Αναζήτηση μαθημάτων** ή **Διαδρομές μάθησης** από το κύριο menu για τα σχετικά επόμενα θέματα.
