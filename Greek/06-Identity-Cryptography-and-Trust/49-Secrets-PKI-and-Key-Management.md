# Secrets, PKI και Διαχείριση Κλειδιών

> **Ελληνική έκδοση — Μάθημα 049.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Identity και cryptography είναι μηχανισμοί μεταφοράς εμπιστοσύνης. Authentication απαντά ποιος παρουσιάζει ένα credential, authorization τι επιτρέπεται να κάνει, ενώ cryptography προστατεύει συγκεκριμένες ιδιότητες δεδομένων και πρωτοκόλλων. Κλειδιά, tokens, certificates, federation metadata και policy engines είναι όλα authority-bearing artifacts και χρειάζονται σαφή lifecycle.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Secrets, PKI και Διαχείριση Κλειδιών**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Secret lifecycle**
  Για το **Secret lifecycle**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **Secret types**
  Για το **Secret types**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **Avoid secrets in source code**
  Για το **Avoid secrets in source code**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **Secret managers**
  Για το **Secret managers**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **PKI concepts**
  Για το **PKI concepts**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **Certificate lifecycle**
  Για το **Certificate lifecycle**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **Key rotation**
  Για το **Key rotation**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **Signing keys**
  Για το **Signing keys**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **Encryption key separation**
  Για το **Encryption key separation**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **Backups and escrow**
  Για το **Backups and escrow**, δες το workflow σαν reproducible local environment: paths, package/source provenance, permissions, environment state, error handling και rollback. Στο Termux προτίμησε standard-library εργαλεία, explicit paths και δοκιμές σε harmless local files/services.
- **Lab — Secret inventory**
  Για το **Lab — Secret inventory**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **Key-management depth**
  Για το **Key-management depth**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **Secret classes**
  Για το **Secret classes**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **PKI**
  Για το **PKI**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **Rotation**
  Για το **Rotation**, στο πλαίσιο του **Secrets, PKI και Διαχείριση Κλειδιών**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Secrets, PKI και Διαχείριση Κλειδιών**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε synthetic identities, test certificates και local identity providers. Χαρτογράφησε issuer, subject, audience, permissions, lifetime, rotation και revocation χωρίς να αποθηκεύεις πραγματικά secrets.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Secrets, PKI και Διαχείριση Κλειδιών**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Secrets, PKI και Διαχείριση Κλειδιών** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 049](../../English/06-Identity-Cryptography-and-Trust/49-Secrets-PKI-and-Key-Management.md)
