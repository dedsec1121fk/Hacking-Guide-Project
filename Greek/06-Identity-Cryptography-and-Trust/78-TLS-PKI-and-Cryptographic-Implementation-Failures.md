# TLS, PKI και Αποτυχίες Υλοποίησης Κρυπτογραφίας

> **Ελληνική έκδοση — Μάθημα 078.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Identity και cryptography είναι μηχανισμοί μεταφοράς εμπιστοσύνης. Authentication απαντά ποιος παρουσιάζει ένα credential, authorization τι επιτρέπεται να κάνει, ενώ cryptography προστατεύει συγκεκριμένες ιδιότητες δεδομένων και πρωτοκόλλων. Κλειδιά, tokens, certificates, federation metadata και policy engines είναι όλα authority-bearing artifacts και χρειάζονται σαφή lifecycle.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **TLS, PKI και Αποτυχίες Υλοποίησης Κρυπτογραφίας**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Cryptography is a system, not an algorithm**
  Για το **Cryptography is a system, not an algorithm**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **TLS goals**
  Στο **TLS goals**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.
- **Certificate chain**
  Για το **Certificate chain**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **Hostname validation**
  Για το **Hostname validation**, στο πλαίσιο του **TLS, PKI και Αποτυχίες Υλοποίησης Κρυπτογραφίας**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Private PKI**
  Για το **Private PKI**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **Forward secrecy**
  Για το **Forward secrecy**, στο πλαίσιο του **TLS, PKI και Αποτυχίες Υλοποίησης Κρυπτογραφίας**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Nonces and AEAD**
  Για το **Nonces and AEAD**, στο πλαίσιο του **TLS, PKI και Αποτυχίες Υλοποίησης Κρυπτογραφίας**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Randomness**
  Για το **Randomness**, στο πλαίσιο του **TLS, PKI και Αποτυχίες Υλοποίησης Κρυπτογραφίας**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Password storage**
  Για το **Password storage**, κατέγραψε ποιος μπορεί να γράψει/διαβάσει το state, πού αποθηκεύεται, πώς προστατεύεται at rest, ποιο backup/sync behavior υπάρχει και πότε το data πρέπει να διαγράφεται ή να ανακαλείται.
- **Key derivation**
  Για το **Key derivation**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **Downgrade resistance**
  Για το **Downgrade resistance**, στο πλαίσιο του **TLS, PKI και Αποτυχίες Υλοποίησης Κρυπτογραφίας**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Certificate revocation reality**
  Για το **Certificate revocation reality**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **Side channels**
  Για το **Side channels**, στο πλαίσιο του **TLS, PKI και Αποτυχίες Υλοποίησης Κρυπτογραφίας**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Padding and error oracles**
  Για το **Padding and error oracles**, στο πλαίσιο του **TLS, PKI και Αποτυχίες Υλοποίησης Κρυπτογραφίας**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Key lifecycle**
  Για το **Key lifecycle**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **Safe localhost TLS lab**
  Στο **Safe localhost TLS lab**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **TLS, PKI και Αποτυχίες Υλοποίησης Κρυπτογραφίας**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε synthetic identities, test certificates και local identity providers. Χαρτογράφησε issuer, subject, audience, permissions, lifetime, rotation και revocation χωρίς να αποθηκεύεις πραγματικά secrets.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **TLS, PKI και Αποτυχίες Υλοποίησης Κρυπτογραφίας**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **TLS, PKI και Αποτυχίες Υλοποίησης Κρυπτογραφίας** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 078](../../English/06-Identity-Cryptography-and-Trust/78-TLS-PKI-and-Cryptographic-Implementation-Failures.md)
