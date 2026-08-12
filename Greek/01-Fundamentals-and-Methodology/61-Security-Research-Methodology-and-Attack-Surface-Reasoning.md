# Μεθοδολογία Security Research και Συλλογιστική Attack Surface

> **Ελληνική έκδοση — Μάθημα 061.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Η κατηγορία αυτή χτίζει τον τρόπο σκέψης που χρειάζεται πριν από οποιοδήποτε τεχνικό test. Η ασφάλεια αντιμετωπίζεται ως σύστημα από assets, identities, trust boundaries, δεδομένα, controls και αποδεικτικά στοιχεία. Το ζητούμενο δεν είναι να απομνημονεύσεις εργαλεία αλλά να μπορείς να εξηγήσεις τι προστατεύεται, από ποια απειλή, με ποια υπόθεση και πώς αποδεικνύεται το αποτέλεσμα.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Μεθοδολογία Security Research και Συλλογιστική Attack Surface**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **The research mindset**
  Για το **The research mindset**, στο πλαίσιο του **Μεθοδολογία Security Research και Συλλογιστική Attack Surface**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Attack surface versus vulnerability**
  Για το **Attack surface versus vulnerability**, στο πλαίσιο του **Μεθοδολογία Security Research και Συλλογιστική Attack Surface**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Model the system as graphs**
  Για το **Model the system as graphs**, στο πλαίσιο του **Μεθοδολογία Security Research και Συλλογιστική Attack Surface**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Trust boundaries**
  Για το **Trust boundaries**, στο πλαίσιο του **Μεθοδολογία Security Research και Συλλογιστική Attack Surface**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Ασφάλεια properties and invariants**
  Για το **Ασφάλεια properties and invariants**, στο πλαίσιο του **Μεθοδολογία Security Research και Συλλογιστική Attack Surface**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **State-machine thinking**
  Για το **State-machine thinking**, στο πλαίσιο του **Μεθοδολογία Security Research και Συλλογιστική Attack Surface**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Differential testing**
  Για το **Differential testing**, δες το workflow σαν reproducible local environment: paths, package/source provenance, permissions, environment state, error handling και rollback. Στο Termux προτίμησε standard-library εργαλεία, explicit paths και δοκιμές σε harmless local files/services.
- **Canonicalization and representation gaps**
  Για το **Canonicalization and representation gaps**, στο πλαίσιο του **Μεθοδολογία Security Research και Συλλογιστική Attack Surface**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Identity translation**
  Για το **Identity translation**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Failure-path analysis**
  Για το **Failure-path analysis**, στο πλαίσιο του **Μεθοδολογία Security Research και Συλλογιστική Attack Surface**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Evidence quality**
  Στο **Evidence quality**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Safe advanced practice**
  Για το **Safe advanced practice**, στο πλαίσιο του **Μεθοδολογία Security Research και Συλλογιστική Attack Surface**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Research notebook template**
  Για το **Research notebook template**, στο πλαίσιο του **Μεθοδολογία Security Research και Συλλογιστική Attack Surface**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Deep-study checkpoint**
  Στο **Deep-study checkpoint**, μετέτρεψε τη θεωρία του **Μεθοδολογία Security Research και Συλλογιστική Attack Surface** σε ελέγξιμα κριτήρια: τι πρέπει να μπορείς να εξηγήσεις, ποιο λάθος assumption εμφανίζεται συχνότερα, ποιο safe lab το αποκαλύπτει και ποιο retest αποδεικνύει ότι το διόρθωσες.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Μεθοδολογία Security Research και Συλλογιστική Attack Surface**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Δούλεψε με ένα υποθετικό ή δικό σου lab. Σχεδίασε scope, assets, trust boundaries και αναμενόμενα evidence πριν αλλάξεις οτιδήποτε.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Μεθοδολογία Security Research και Συλλογιστική Attack Surface**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Μεθοδολογία Security Research και Συλλογιστική Attack Surface** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 061](../../English/01-Fundamentals-and-Methodology/61-Security-Research-Methodology-and-Attack-Surface-Reasoning.md)
