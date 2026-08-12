# Προχωρημένα Εξουσιοδοτημένα Capstones

> **Ελληνική έκδοση — Μάθημα 085.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Τα capstones μετατρέπουν γνώση σε αποδείξιμη ικανότητα. Ένα καλό project έχει scope, threat model, repeatable procedure, evidence, limitations, remediation και καθαρή τεχνική γραφή. Η ποιότητα μετριέται από το αν τρίτος μπορεί να αναπαράγει το συμπέρασμα χωρίς να μαντεύει.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Προχωρημένα Εξουσιοδοτημένα Capstones**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Capstone rules**
  Στο **Capstone rules**, όρισε συγκεκριμένο objective, owned/local scope, expected result και stop condition. Κράτησε μόνο sanitized evidence, σύγκρινε expected με observed behavior και ολοκλήρωσε με remediation και ίδιο regression test.
- **Deliverables for every capstone**
  Στο **Deliverables for every capstone**, όρισε συγκεκριμένο objective, owned/local scope, expected result και stop condition. Κράτησε μόνο sanitized evidence, σύγκρινε expected με observed behavior και ολοκλήρωσε με remediation και ίδιο regression test.
- **Capstone 1 — Binary assurance pipeline**
  Στο **Capstone 1 — Binary assurance pipeline**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **Capstone 2 — Local web trust-boundary review**
  Για το **Capstone 2 — Local web trust-boundary review**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **Capstone 3 — Enterprise identity graph**
  Για το **Capstone 3 — Enterprise identity graph**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Capstone 4 — Linux isolation report**
  Στο **Capstone 4 — Linux isolation report**, όρισε συγκεκριμένο objective, owned/local scope, expected result και stop condition. Κράτησε μόνο sanitized evidence, σύγκρινε expected με observed behavior και ολοκλήρωσε με remediation και ίδιο regression test.
- **Capstone 5 — Kubernetes privilege graph**
  Για το **Capstone 5 — Kubernetes privilege graph**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **Capstone 6 — Cloud IAM sandbox**
  Για το **Capstone 6 — Cloud IAM sandbox**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **Capstone 7 — Protocol reverse engineering**
  Στο **Capstone 7 — Protocol reverse engineering**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.
- **Capstone 8 — Malware-analysis simulation**
  Στο **Capstone 8 — Malware-analysis simulation**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **Capstone 9 — Android application security review**
  Στο **Capstone 9 — Android application security review**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.
- **Capstone 10 — Firmware trust chain**
  Στο **Capstone 10 — Firmware trust chain**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.
- **Capstone 11 — Detection engineering lifecycle**
  Στο **Capstone 11 — Detection engineering lifecycle**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Capstone 12 — Patch-to-prevention study**
  Στο **Capstone 12 — Patch-to-prevention study**, όρισε συγκεκριμένο objective, owned/local scope, expected result και stop condition. Κράτησε μόνο sanitized evidence, σύγκρινε expected με observed behavior και ολοκλήρωσε με remediation και ίδιο regression test.
- **Capstone 13 — Termux security research workstation**
  Στο **Capstone 13 — Termux security research workstation**, όρισε συγκεκριμένο objective, owned/local scope, expected result και stop condition. Κράτησε μόνο sanitized evidence, σύγκρινε expected με observed behavior και ολοκλήρωσε με remediation και ίδιο regression test.
- **Capstone 14 — Incident reconstruction tabletop**
  Στο **Capstone 14 — Incident reconstruction tabletop**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Capstone 15 — Ασφάλεια architecture review**
  Στο **Capstone 15 — Ασφάλεια architecture review**, όρισε συγκεκριμένο objective, owned/local scope, expected result και stop condition. Κράτησε μόνο sanitized evidence, σύγκρινε expected με observed behavior και ολοκλήρωσε με remediation και ίδιο regression test.
- **Scoring rubric**
  Για το **Scoring rubric**, όρισε συγκεκριμένο observable αποτέλεσμα: artifact, report, test, diagram ή explanation που μπορεί να αξιολογηθεί. Προτίμησε μικρά ολοκληρωμένα έργα με scope, evidence, remediation και reflection αντί για λίστες εργαλείων ή claims χωρίς απόδειξη.
- **Προχωρημένο mastery checklist**
  Στο **Προχωρημένο mastery checklist**, μετέτρεψε τη θεωρία του **Προχωρημένα Εξουσιοδοτημένα Capstones** σε ελέγξιμα κριτήρια: τι πρέπει να μπορείς να εξηγήσεις, ποιο λάθος assumption εμφανίζεται συχνότερα, ποιο safe lab το αποκαλύπτει και ποιο retest αποδεικνύει ότι το διόρθωσες.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Προχωρημένα Εξουσιοδοτημένα Capstones**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χτίσε portfolio μόνο με δικά σου ή ρητά εξουσιοδοτημένα labs. Αφαίρεσε secrets και προσωπικά δεδομένα πριν δημοσιεύσεις artifacts.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Προχωρημένα Εξουσιοδοτημένα Capstones**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Προχωρημένα Εξουσιοδοτημένα Capstones** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 085](../../English/11-Labs-Capstones-and-Career/85-Advanced-Authorized-Capstones.md)
