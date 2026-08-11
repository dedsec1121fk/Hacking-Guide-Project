# Serverless, Edge Workers, Functions και Event-Driven Cloud Security

> **Ελληνική έκδοση — Μάθημα 104.** Διατηρούνται οι διεθνείς τεχνικοί όροι όπου είναι ακριβέστεροι και ευκολότεροι στην αναζήτηση.

## Στόχος του μαθήματος

Να κατανοήσεις σε βάθος το **Serverless, Edge Workers, Functions και Event-Driven Cloud Security**, να αναγνωρίζεις trust boundaries και failure states και να μπορείς να αποδείξεις ένα συμπέρασμα με ασφαλές, επαναλήψιμο evidence.

> **Όριο εξουσιοδότησης:** Πρακτική μόνο σε συστήματα, λογαριασμούς, κώδικα ή labs που σου ανήκουν ή έχεις ρητή άδεια να ελέγξεις. Προτίμησε localhost, synthetic data και disposable environments.

## Βαθιές τεχνικές έννοιες

### 1. Invocation surface

Serverless function μπορεί να ενεργοποιείται από HTTP, queue, storage event, scheduler ή cloud control event. Κάθε trigger χρειάζεται authenticated source, schema validation και resource limits.

### 2. Execution identity

Η function τρέχει με workload identity/service role που συχνά έχει περισσότερα permissions από το request caller. Δώσε least privilege ανά function και μη χρησιμοποιείς ένα shared broad role για όλο το application.

### 3. Event trust

Event payload και metadata είναι untrusted input ακόμη αν έρχονται από cloud service. Validate tenant/resource, event type, version και replay/idempotency state πριν από side effects.

### 4. Ephemeral runtime

Instances είναι short-lived αλλά μπορεί να επαναχρησιμοποιούνται, με `/tmp`, memory ή connections να παραμένουν μεταξύ invocations. Μην υποθέτεις fresh process για secret/data isolation.

### 5. Secrets

Χρησιμοποίησε managed secret/KMS integration και short-lived identity αντί για secrets μέσα σε package ή environment dumps. Limit which function/version can retrieve each secret.

### 6. Dependency packaging

Function packages και layers είναι supply-chain artifacts. Pin/scan dependencies, verify provenance και μην αφήνεις mutable external download να αλλάζει runtime code μετά approval.

### 7. Edge execution

Edge workers τρέχουν κοντά στον user και συχνά χειρίζονται headers, auth, cache και routing. Είναι application boundary και χρειάζονται isolation, versioned deploy και secret restrictions.

### 8. Observability and cost abuse

Rate, duration, concurrency, downstream calls και errors είναι security/cost signals. Budget/quotas και alarms προστατεύουν από resource abuse χωρίς να βασίζονται μόνο σε autoscaling.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Γράψε πρώτα invariant και expected result, άλλαξε μία μεταβλητή κάθε φορά και κράτησε μόνο το evidence που χρειάζεται.

1. **Model one photo-processing function triggered by object storage and identify what prevents another tenant/object path from being processed** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
2. **Write an IAM policy matrix for three functions that each need different storage/database actions** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
3. **Create a replay/idempotency test plan for a harmless event-driven workflow** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary και ποιος έχει authority;
2. Ποιο state μπορεί να γίνει stale, replayed ή inconsistent;
3. Ποιο evidence θα διέψευδε την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά το blast radius;
5. Πώς θα επαναλάβεις το test με ασφάλεια μετά τη remediation?

## Πλήρες αγγλικό μάθημα

[English Module 104](../../English/07-Cloud-Containers-and-Supply-Chain/104-Serverless-Edge-Workers-Functions-and-Event-Driven-Cloud-Security.md)

## Συνέχεια

Χρησιμοποίησε **Αναζήτηση μαθημάτων** ή **Διαδρομές μάθησης** από το κύριο menu για τα σχετικά επόμενα θέματα.
