# OAuth, OIDC, Passkeys και Σύγχρονο Authentication

> **Ελληνική έκδοση — Μάθημα 039.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Identity και cryptography είναι μηχανισμοί μεταφοράς εμπιστοσύνης. Authentication απαντά ποιος παρουσιάζει ένα credential, authorization τι επιτρέπεται να κάνει, ενώ cryptography προστατεύει συγκεκριμένες ιδιότητες δεδομένων και πρωτοκόλλων. Κλειδιά, tokens, certificates, federation metadata και policy engines είναι όλα authority-bearing artifacts και χρειάζονται σαφή lifecycle.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **OAuth, OIDC, Passkeys και Σύγχρονο Authentication**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Authentication versus authorization**
  Για το **Authentication versus authorization**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Core actors**
  Για το **Core actors**, στο πλαίσιο του **OAuth, OIDC, Passkeys και Σύγχρονο Authentication**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Redirect URIs**
  Για το **Redirect URIs**, στο πλαίσιο του **OAuth, OIDC, Passkeys και Σύγχρονο Authentication**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **State, nonce, and PKCE**
  Για το **State, nonce, and PKCE**, στο πλαίσιο του **OAuth, OIDC, Passkeys και Σύγχρονο Authentication**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Token handling**
  Για το **Token handling**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Session versus token**
  Για το **Session versus token**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **MFA**
  Για το **MFA**, στο πλαίσιο του **OAuth, OIDC, Passkeys και Σύγχρονο Authentication**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Passkeys**
  Για το **Passkeys**, στο πλαίσιο του **OAuth, OIDC, Passkeys και Σύγχρονο Authentication**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Federation risks**
  Για το **Federation risks**, στο πλαίσιο του **OAuth, OIDC, Passkeys και Σύγχρονο Authentication**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Service-to-service identity**
  Για το **Service-to-service identity**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Safe design lab**
  Για το **Safe design lab**, στο πλαίσιο του **OAuth, OIDC, Passkeys και Σύγχρονο Authentication**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Primary references**
  Για το **Primary references**, ξεχώρισε normative specification από tutorial ή vendor summary. Κατέγραψε έκδοση/ημερομηνία, ποιο requirement στηρίζει το συμπέρασμα και ποιο μέρος του **OAuth, OIDC, Passkeys και Σύγχρονο Authentication** χρειάζεται επανέλεγχο όταν αλλάξει η πηγή.
- **Σύγχρονο authentication in more depth**
  Για το **Σύγχρονο authentication in more depth**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Redirect and client trust**
  Για το **Redirect and client trust**, στο πλαίσιο του **OAuth, OIDC, Passkeys και Σύγχρονο Authentication**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Step-up and transaction authorization**
  Για το **Step-up and transaction authorization**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Telemetry**
  Στο **Telemetry**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **OAuth, OIDC, Passkeys και Σύγχρονο Authentication**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε synthetic identities, test certificates και local identity providers. Χαρτογράφησε issuer, subject, audience, permissions, lifetime, rotation και revocation χωρίς να αποθηκεύεις πραγματικά secrets.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **OAuth, OIDC, Passkeys και Σύγχρονο Authentication**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **OAuth, OIDC, Passkeys και Σύγχρονο Authentication** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 039](../../English/06-Identity-Cryptography-and-Trust/39-OAuth-OIDC-Passkeys-and-Modern-Authentication.md)
