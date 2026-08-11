# Digital Forensics — Filesystem Timelines και Memory Artifacts

> **Ελληνική έκδοση — Μάθημα 081.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Blue-team εργασία σημαίνει να μετατρέπεις telemetry σε τεκμηριωμένα συμπεράσματα. Ένα alert δεν είναι απόδειξη από μόνο του. Χρειάζεται timeline, identity context, process/network relationships, data provenance και κατανόηση του τι δεν καταγράφεται. Η ανθεκτικότητα επεκτείνεται από detection μέχρι containment, recovery και verification.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Digital Forensics — Filesystem Timelines και Memory Artifacts**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Forensics is reconstruction under uncertainty**
  Στο **Forensics is reconstruction under uncertainty**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Evidence preservation**
  Στο **Evidence preservation**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Filesystem metadata**
  Για το **Filesystem metadata**, κατέγραψε ποιος μπορεί να γράψει/διαβάσει το state, πού αποθηκεύεται, πώς προστατεύεται at rest, ποιο backup/sync behavior υπάρχει και πότε το data πρέπει να διαγράφεται ή να ανακαλείται.
- **Timestamp caveats**
  Στο **Timestamp caveats**, διατήρησε provenance και χρονικό context για κάθε artifact. Ξεχώρισε fact, inference και hypothesis, έλεγξε clock/timezone effects και μη θεωρείς το πρώτο observable event ούτε root cause ούτε αρχικό σημείο compromise χωρίς corroboration.
- **Timeline normalization**
  Στο **Timeline normalization**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Super-timelines**
  Στο **Super-timelines**, διατήρησε provenance και χρονικό context για κάθε artifact. Ξεχώρισε fact, inference και hypothesis, έλεγξε clock/timezone effects και μη θεωρείς το πρώτο observable event ούτε root cause ούτε αρχικό σημείο compromise χωρίς corroboration.
- **Process execution artifacts**
  Στο **Process execution artifacts**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **Persistence review**
  Στο **Persistence review**, διατήρησε provenance και χρονικό context για κάθε artifact. Ξεχώρισε fact, inference και hypothesis, έλεγξε clock/timezone effects και μη θεωρείς το πρώτο observable event ούτε root cause ούτε αρχικό σημείο compromise χωρίς corroboration.
- **Memory forensics concepts**
  Στο **Memory forensics concepts**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **Process-versus-module anomalies**
  Στο **Process-versus-module anomalies**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **Network artifacts**
  Στο **Network artifacts**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.
- **Browser and user artifacts**
  Για το **Browser and user artifacts**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **Cloud and SaaS forensics**
  Για το **Cloud and SaaS forensics**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **Hypothesis-driven investigation**
  Στο **Hypothesis-driven investigation**, διατήρησε provenance και χρονικό context για κάθε artifact. Ξεχώρισε fact, inference και hypothesis, έλεγξε clock/timezone effects και μη θεωρείς το πρώτο observable event ούτε root cause ούτε αρχικό σημείο compromise χωρίς corroboration.
- **Root cause versus patient zero**
  Στο **Root cause versus patient zero**, διατήρησε provenance και χρονικό context για κάθε artifact. Ξεχώρισε fact, inference και hypothesis, έλεγξε clock/timezone effects και μη θεωρείς το πρώτο observable event ούτε root cause ούτε αρχικό σημείο compromise χωρίς corroboration.
- **Safe timeline lab**
  Στο **Safe timeline lab**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Forensic report structure**
  Στο **Forensic report structure**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Digital Forensics — Filesystem Timelines και Memory Artifacts**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε synthetic logs και harmless local events. Κατέγραψε expected evidence πριν το test και σύγκρινε με ό,τι πραγματικά συλλέχθηκε.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Digital Forensics — Filesystem Timelines και Memory Artifacts**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Digital Forensics — Filesystem Timelines και Memory Artifacts** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 081](../../English/08-Blue-Team-IR-Forensics-and-Resilience/81-Digital-Forensics-Filesystem-Timelines-and-Memory-Artifacts.md)
