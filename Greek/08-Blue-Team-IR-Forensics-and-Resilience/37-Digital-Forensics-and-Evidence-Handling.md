# Digital Forensics και Διαχείριση Αποδεικτικών Στοιχείων

> **Ελληνική έκδοση — Μάθημα 037.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Blue-team εργασία σημαίνει να μετατρέπεις telemetry σε τεκμηριωμένα συμπεράσματα. Ένα alert δεν είναι απόδειξη από μόνο του. Χρειάζεται timeline, identity context, process/network relationships, data provenance και κατανόηση του τι δεν καταγράφεται. Η ανθεκτικότητα επεκτείνεται από detection μέχρι containment, recovery και verification.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Digital Forensics και Διαχείριση Αποδεικτικών Στοιχείων**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Forensics principles**
  Στο **Forensics principles**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Order of volatility**
  Στο **Order of volatility**, διατήρησε provenance και χρονικό context για κάθε artifact. Ξεχώρισε fact, inference και hypothesis, έλεγξε clock/timezone effects και μη θεωρείς το πρώτο observable event ούτε root cause ούτε αρχικό σημείο compromise χωρίς corroboration.
- **Timestamps**
  Στο **Timestamps**, διατήρησε provenance και χρονικό context για κάθε artifact. Ξεχώρισε fact, inference και hypothesis, έλεγξε clock/timezone effects και μη θεωρείς το πρώτο observable event ούτε root cause ούτε αρχικό σημείο compromise χωρίς corroboration.
- **Hashes**
  Στο **Hashes**, διατήρησε provenance και χρονικό context για κάθε artifact. Ξεχώρισε fact, inference και hypothesis, έλεγξε clock/timezone effects και μη θεωρείς το πρώτο observable event ούτε root cause ούτε αρχικό σημείο compromise χωρίς corroboration.
- **Logs as evidence**
  Στο **Logs as evidence**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Mobile evidence**
  Στο **Mobile evidence**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Cloud evidence**
  Για το **Cloud evidence**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **File metadata**
  Στο **File metadata**, διατήρησε provenance και χρονικό context για κάθε artifact. Ξεχώρισε fact, inference και hypothesis, έλεγξε clock/timezone effects και μη θεωρείς το πρώτο observable event ούτε root cause ούτε αρχικό σημείο compromise χωρίς corroboration.
- **Evidence notes**
  Στο **Evidence notes**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Root-cause caution**
  Στο **Root-cause caution**, διατήρησε provenance και χρονικό context για κάθε artifact. Ξεχώρισε fact, inference και hypothesis, έλεγξε clock/timezone effects και μη θεωρείς το πρώτο observable event ούτε root cause ούτε αρχικό σημείο compromise χωρίς corroboration.
- **Safe lab — Synthetic timeline**
  Στο **Safe lab — Synthetic timeline**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Reporting**
  Στο **Reporting**, διατήρησε provenance και χρονικό context για κάθε artifact. Ξεχώρισε fact, inference και hypothesis, έλεγξε clock/timezone effects και μη θεωρείς το πρώτο observable event ούτε root cause ούτε αρχικό σημείο compromise χωρίς corroboration.
- **Forensic reasoning in more depth**
  Στο **Forensic reasoning in more depth**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Provenance**
  Για το **Provenance**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **Time**
  Για το **Time**, στο πλαίσιο του **Digital Forensics και Διαχείριση Αποδεικτικών Στοιχείων**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Fact versus inference**
  Στο **Fact versus inference**, διατήρησε provenance και χρονικό context για κάθε artifact. Ξεχώρισε fact, inference και hypothesis, έλεγξε clock/timezone effects και μη θεωρείς το πρώτο observable event ούτε root cause ούτε αρχικό σημείο compromise χωρίς corroboration.
- **Scope and minimization**
  Στο **Scope and minimization**, διατήρησε provenance και χρονικό context για κάθε artifact. Ξεχώρισε fact, inference και hypothesis, έλεγξε clock/timezone effects και μη θεωρείς το πρώτο observable event ούτε root cause ούτε αρχικό σημείο compromise χωρίς corroboration.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Digital Forensics και Διαχείριση Αποδεικτικών Στοιχείων**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε synthetic logs και harmless local events. Κατέγραψε expected evidence πριν το test και σύγκρινε με ό,τι πραγματικά συλλέχθηκε.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Digital Forensics και Διαχείριση Αποδεικτικών Στοιχείων**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Digital Forensics και Διαχείριση Αποδεικτικών Στοιχείων** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 037](../../English/08-Blue-Team-IR-Forensics-and-Resilience/37-Digital-Forensics-and-Evidence-Handling.md)
