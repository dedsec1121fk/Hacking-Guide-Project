# Βάσεις Termux και Android Linux

> **Ελληνική έκδοση — Μάθημα 028.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Το Termux προσφέρει Linux-like userland πάνω στο Android, αλλά δεν είναι πλήρης desktop διανομή ούτε παρακάμπτει το Android security model. Για αξιόπιστη χρήση πρέπει να κατανοείς storage permissions, package management, process lifetime, networking, SSH, Python environments και τα όρια που επιβάλλει το Android sandbox.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Βάσεις Termux και Android Linux**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **What Termux actually is**
  Για το **What Termux actually is**, δες το workflow σαν reproducible local environment: paths, package/source provenance, permissions, environment state, error handling και rollback. Στο Termux προτίμησε standard-library εργαλεία, explicit paths και δοκιμές σε harmless local files/services.
- **Installation and update hygiene**
  Για το **Installation and update hygiene**, στο πλαίσιο του **Βάσεις Termux και Android Linux**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Storage model**
  Για το **Storage model**, κατέγραψε ποιος μπορεί να γράψει/διαβάσει το state, πού αποθηκεύεται, πώς προστατεύεται at rest, ποιο backup/sync behavior υπάρχει και πότε το data πρέπει να διαγράφεται ή να ανακαλείται.
- **Core shell navigation**
  Για το **Core shell navigation**, δες το workflow σαν reproducible local environment: paths, package/source provenance, permissions, environment state, error handling και rollback. Στο Termux προτίμησε standard-library εργαλεία, explicit paths και δοκιμές σε harmless local files/services.
- **Files, permissions, and executables**
  Για το **Files, permissions, and executables**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Environment variables**
  Για το **Environment variables**, δες το workflow σαν reproducible local environment: paths, package/source provenance, permissions, environment state, error handling και rollback. Στο Termux προτίμησε standard-library εργαλεία, explicit paths και δοκιμές σε harmless local files/services.
- **Package management fundamentals**
  Για το **Package management fundamentals**, δες το workflow σαν reproducible local environment: paths, package/source provenance, permissions, environment state, error handling και rollback. Στο Termux προτίμησε standard-library εργαλεία, explicit paths και δοκιμές σε harmless local files/services.
- **Processes and jobs**
  Στο **Processes and jobs**, χαρτογράφησε process → socket → interface/route → peer και ποια identity/host-key/DNS πληροφορία εμπιστεύεται κάθε βήμα. Ξεκίνα από loopback ή δικό σου SSH endpoint και επιβεβαίωσε listening scope, authentication και logs.
- **Networking basics in Termux**
  Για το **Networking basics in Termux**, δες το workflow σαν reproducible local environment: paths, package/source provenance, permissions, environment state, error handling και rollback. Στο Termux προτίμησε standard-library εργαλεία, explicit paths και δοκιμές σε harmless local files/services.
- **Android sandboxing and root**
  Στο **Android sandboxing and root**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.
- **Termux add-ons**
  Για το **Termux add-ons**, δες το workflow σαν reproducible local environment: paths, package/source provenance, permissions, environment state, error handling και rollback. Στο Termux προτίμησε standard-library εργαλεία, explicit paths και δοκιμές σε harmless local files/services.
- **Baseline setup lesson**
  Για το **Baseline setup lesson**, ξεκίνα από observable behavior και διαθέσιμα data sources, όχι από technique ID μόνο. Γράψε detection hypothesis, required fields, expected benign collisions, tuning strategy και validation event ώστε η κάλυψη να είναι μετρήσιμη.
- **Common mistakes**
  Στο **Common mistakes**, μετέτρεψε τη θεωρία του **Βάσεις Termux και Android Linux** σε ελέγξιμα κριτήρια: τι πρέπει να μπορείς να εξηγήσεις, ποιο λάθος assumption εμφανίζεται συχνότερα, ποιο safe lab το αποκαλύπτει και ποιο retest αποδεικνύει ότι το διόρθωσες.
- **Mini lab — Build a known-good Termux baseline**
  Για το **Mini lab — Build a known-good Termux baseline**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **Primary references**
  Για το **Primary references**, ξεχώρισε normative specification από tutorial ή vendor summary. Κατέγραψε έκδοση/ημερομηνία, ποιο requirement στηρίζει το συμπέρασμα και ποιο μέρος του **Βάσεις Termux και Android Linux** χρειάζεται επανέλεγχο όταν αλλάξει η πηγή.
- **Practical Termux foundation drills**
  Στο **Practical Termux foundation drills**, όρισε συγκεκριμένο objective, owned/local scope, expected result και stop condition. Κράτησε μόνο sanitized evidence, σύγκρινε expected με observed behavior και ολοκλήρωσε με remediation και ίδιο regression test.
- **Drill 1 — Know your environment**
  Στο **Drill 1 — Know your environment**, όρισε συγκεκριμένο objective, owned/local scope, expected result και stop condition. Κράτησε μόνο sanitized evidence, σύγκρινε expected με observed behavior και ολοκλήρωσε με remediation και ίδιο regression test.
- **Drill 2 — Permission reasoning**
  Για το **Drill 2 — Permission reasoning**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Drill 3 — Rebuildability**
  Στο **Drill 3 — Rebuildability**, όρισε συγκεκριμένο objective, owned/local scope, expected result και stop condition. Κράτησε μόνο sanitized evidence, σύγκρινε expected με observed behavior και ολοκλήρωσε με remediation και ίδιο regression test.
- **Android-specific guidance**
  Στο **Android-specific guidance**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Βάσεις Termux και Android Linux**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Κράτησε όλα τα labs μέσα στο δικό σου τηλέφωνο, localhost ή συστήματα που ελέγχεις. Ξεκίνα με read-only commands και διατήρησε backups για scripts/configuration.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Βάσεις Termux και Android Linux**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Βάσεις Termux και Android Linux** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 028](../../English/10-Termux-and-Security-Automation/28-Termux-Foundations-and-Android-Linux.md)
