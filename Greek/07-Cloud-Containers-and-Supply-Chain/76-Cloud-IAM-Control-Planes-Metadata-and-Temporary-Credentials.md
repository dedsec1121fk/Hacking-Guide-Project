# Cloud IAM, Control Planes, Metadata και Temporary Credentials

> **Ελληνική έκδοση — Μάθημα 076.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Cloud-native ασφάλεια σημαίνει έλεγχο control planes, workload identity, artifacts, build systems, containers και data flows. Οι σημαντικότερες αστοχίες συχνά προκύπτουν από υπερβολικά δικαιώματα, implicit trust μεταξύ services, μη επαληθεύσιμα artifacts ή ανεπαρκή provenance.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Cloud IAM, Control Planes, Metadata και Temporary Credentials**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Cloud security is API security at infrastructure scale**
  Για το **Cloud security is API security at infrastructure scale**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **Identity types**
  Για το **Identity types**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Temporary credentials**
  Για το **Temporary credentials**, στο πλαίσιο του **Cloud IAM, Control Planes, Metadata και Temporary Credentials**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Effective permission**
  Για το **Effective permission**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Role assumption**
  Για το **Role assumption**, στο πλαίσιο του **Cloud IAM, Control Planes, Metadata και Temporary Credentials**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Workload identity**
  Για το **Workload identity**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Metadata services**
  Για το **Metadata services**, χαρτογράφησε Windows security principal, token/privileges, object ACL ή service/IPC boundary και το audit/ETW evidence που δείχνει την απόφαση πρόσβασης. Δούλεψε σε disposable Windows VM και έλεγξε effective authority, όχι μόνο configuration text.
- **Control plane versus data plane**
  Για το **Control plane versus data plane**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **Organization-level guardrails**
  Για το **Organization-level guardrails**, στο πλαίσιο του **Cloud IAM, Control Planes, Metadata και Temporary Credentials**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Secrets and key services**
  Για το **Secrets and key services**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **Public exposure**
  Για το **Public exposure**, στο πλαίσιο του **Cloud IAM, Control Planes, Metadata και Temporary Credentials**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Cloud logging**
  Για το **Cloud logging**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **Safe sandbox lab**
  Για το **Safe sandbox lab**, στο πλαίσιο του **Cloud IAM, Control Planes, Metadata και Temporary Credentials**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Privilege graph questions**
  Για το **Privilege graph questions**, στο πλαίσιο του **Cloud IAM, Control Planes, Metadata και Temporary Credentials**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Cloud IAM, Control Planes, Metadata και Temporary Credentials**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε local containers ή sandbox cloud accounts που σου ανήκουν. Έλεγξε policies και artifacts read-only πριν από αλλαγές και απέφυγε δημόσια exposure στα labs.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Cloud IAM, Control Planes, Metadata και Temporary Credentials**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Cloud IAM, Control Planes, Metadata και Temporary Credentials** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 076](../../English/07-Cloud-Containers-and-Supply-Chain/76-Cloud-IAM-Control-Planes-Metadata-and-Temporary-Credentials.md)
