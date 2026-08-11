# Ασφαλές Λογισμικό, APIs και Εφοδιαστική Αλυσίδα

> **Ελληνική έκδοση — Μάθημα 022.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Cloud-native ασφάλεια σημαίνει έλεγχο control planes, workload identity, artifacts, build systems, containers και data flows. Οι σημαντικότερες αστοχίες συχνά προκύπτουν από υπερβολικά δικαιώματα, implicit trust μεταξύ services, μη επαληθεύσιμα artifacts ή ανεπαρκή provenance.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Ασφαλές Λογισμικό, APIs και Εφοδιαστική Αλυσίδα**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Secure by design**
  Για το **Secure by design**, στο πλαίσιο του **Ασφαλές Λογισμικό, APIs και Εφοδιαστική Αλυσίδα**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **API security**
  Για το **API security**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **API review checklist**
  Για το **API review checklist**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **Software supply-chain security**
  Για το **Software supply-chain security**, ακολούθησε την αλυσίδα trust από immutable/early-boot state μέχρι OS/application. Έλεγξε measured/verified state, key custody, update authorization, anti-rollback και τι αλλάζει όταν ο attacker έχει φυσική πρόσβαση.
- **Defensive controls**
  Για το **Defensive controls**, στο πλαίσιο του **Ασφαλές Λογισμικό, APIs και Εφοδιαστική Αλυσίδα**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Safe lab**
  Στο **Safe lab**, μετέτρεψε τη θεωρία του **Ασφαλές Λογισμικό, APIs και Εφοδιαστική Αλυσίδα** σε ελέγξιμα κριτήρια: τι πρέπει να μπορείς να εξηγήσεις, ποιο λάθος assumption εμφανίζεται συχνότερα, ποιο safe lab το αποκαλύπτει και ποιο retest αποδεικνύει ότι το διόρθωσες.
- **References**
  Για το **References**, ξεχώρισε normative specification από tutorial ή vendor summary. Κατέγραψε έκδοση/ημερομηνία, ποιο requirement στηρίζει το συμπέρασμα και ποιο μέρος του **Ασφαλές Λογισμικό, APIs και Εφοδιαστική Αλυσίδα** χρειάζεται επανέλεγχο όταν αλλάξει η πηγή.
- **Secure development lifecycle**
  Για το **Secure development lifecycle**, στο πλαίσιο του **Ασφαλές Λογισμικό, APIs και Εφοδιαστική Αλυσίδα**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Ασφάλεια requirements**
  Για το **Ασφάλεια requirements**, στο πλαίσιο του **Ασφαλές Λογισμικό, APIs και Εφοδιαστική Αλυσίδα**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Threat modeling**
  Για το **Threat modeling**, στο πλαίσιο του **Ασφαλές Λογισμικό, APIs και Εφοδιαστική Αλυσίδα**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **API authorization patterns**
  Για το **API authorization patterns**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Object-level authorization**
  Για το **Object-level authorization**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Function-level authorization**
  Για το **Function-level authorization**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Property-level authorization**
  Για το **Property-level authorization**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Resource and business-flow protection**
  Για το **Resource and business-flow protection**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **API inventory and lifecycle**
  Για το **API inventory and lifecycle**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **Third-party API consumption**
  Για το **Third-party API consumption**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **Software supply-chain model**
  Για το **Software supply-chain model**, ακολούθησε την αλυσίδα trust από immutable/early-boot state μέχρι OS/application. Έλεγξε measured/verified state, key custody, update authorization, anti-rollback και τι αλλάζει όταν ο attacker έχει φυσική πρόσβαση.
- **Dependency governance**
  Για το **Dependency governance**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **CI/CD hardening**
  Για το **CI/CD hardening**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **Build provenance and artifact integrity**
  Για το **Build provenance and artifact integrity**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **Secure by default checklist**
  Για το **Secure by default checklist**, στο πλαίσιο του **Ασφαλές Λογισμικό, APIs και Εφοδιαστική Αλυσίδα**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Ασφαλές Λογισμικό, APIs και Εφοδιαστική Αλυσίδα**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε local containers ή sandbox cloud accounts που σου ανήκουν. Έλεγξε policies και artifacts read-only πριν από αλλαγές και απέφυγε δημόσια exposure στα labs.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Ασφαλές Λογισμικό, APIs και Εφοδιαστική Αλυσίδα**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Ασφαλές Λογισμικό, APIs και Εφοδιαστική Αλυσίδα** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 022](../../English/07-Cloud-Containers-and-Supply-Chain/22-Secure-Software-APIs-and-Supply-Chain.md)
