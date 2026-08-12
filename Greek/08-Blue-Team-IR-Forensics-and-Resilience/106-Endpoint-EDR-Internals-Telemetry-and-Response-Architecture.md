# Endpoint EDR Internals, Telemetry και Response Architecture

> **Ελληνική έκδοση — Μάθημα 106.** Διατηρούνται οι διεθνείς τεχνικοί όροι όπου είναι ακριβέστεροι και ευκολότεροι στην αναζήτηση.

## Στόχος του μαθήματος

Να κατανοήσεις σε βάθος το **Endpoint EDR Internals, Telemetry και Response Architecture**, να αναγνωρίζεις trust boundaries και failure states και να μπορείς να αποδείξεις ένα συμπέρασμα με ασφαλές, επαναλήψιμο evidence.

> **Όριο εξουσιοδότησης:** Πρακτική μόνο σε συστήματα, λογαριασμούς, κώδικα ή labs που σου ανήκουν ή έχεις ρητή άδεια να ελέγξεις. Προτίμησε localhost, synthetic data και disposable environments.

## Βαθιές τεχνικές έννοιες

### 1. Sensor placement

EDR sensors μπορεί να βλέπουν kernel, process, file, registry, network ή user-space events ανά platform. Κατέγραψε ακριβώς ποια source παράγει κάθε field και ποια blind spots υπάρχουν.

### 2. Process lineage

Parent/child process tree βοηθά να εξηγηθεί execution context αλλά μπορεί να μην αποτυπώνει IPC, service broker, scheduled task ή remote origin. Συνδύασέ το με user/session και event correlation.

### 3. Content versus metadata

Full content αυξάνει privacy/storage risk ενώ metadata έχει λιγότερο context. Collection policy πρέπει να ισορροπεί detection value, minimization, retention και legal requirements.

### 4. Behavioral detections

Behavioral rule πρέπει να ορίζει invariant/sequence και expected benign alternatives. Version, data source και false-positive rationale είναι απαραίτητα για maintainable detection.

### 5. Response actions

Isolate host, kill process, quarantine file ή revoke token είναι state-changing controls. Χρειάζονται authorization, audit, rollback/recovery και προστασία από false-positive blast radius.

### 6. Tamper protection

EDR πρέπει να προστατεύει agent/configuration/update paths από unauthorized change, αλλά admin/recovery channels παραμένουν. Monitor sensor health και policy changes independent από endpoint όπου γίνεται.

### 7. Cloud analytics

Central analytics συσχετίζει endpoints και threat intelligence αλλά γίνεται high-value data/control plane. Restrict analyst/admin roles, exports, API tokens και detection deployment.

### 8. Validation

Χρησιμοποίησε benign simulations ή synthetic events και trace end-to-end sensor→pipeline→rule→alert→response. Failure μπορεί να είναι telemetry gap και όχι rule logic.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Γράψε πρώτα invariant και expected result, άλλαξε μία μεταβλητή κάθε φορά και κράτησε μόνο το evidence που χρειάζεται.

1. **Design an endpoint event schema for process start that includes identity, parent, signer/hash, session, container context, and correlation ID** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
2. **Create a detection test for a harmless unusual child-process pattern using local scripts; document false-positive conditions** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
3. **Write a response decision matrix for isolate host vs revoke session vs terminate process vs observe only** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary και ποιος έχει authority;
2. Ποιο state μπορεί να γίνει stale, replayed ή inconsistent;
3. Ποιο evidence θα διέψευδε την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά το blast radius;
5. Πώς θα επαναλάβεις το test με ασφάλεια μετά τη remediation?

## Πλήρες αγγλικό μάθημα

[English Module 106](../../English/08-Blue-Team-IR-Forensics-and-Resilience/106-Endpoint-EDR-Internals-Telemetry-and-Response-Architecture.md)

## Συνέχεια

Χρησιμοποίησε **Αναζήτηση μαθημάτων** ή **Διαδρομές μάθησης** από το κύριο menu για τα σχετικά επόμενα θέματα.
