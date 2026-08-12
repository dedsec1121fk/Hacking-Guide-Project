# Ασφάλεια Κινητών Συσκευών

> **Ελληνική έκδοση — Μάθημα 017.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Mobile, IoT και embedded συστήματα συνδυάζουν εφαρμογές, λειτουργικό, firmware, radios, hardware roots of trust και φυσική πρόσβαση. Το security model εξαρτάται από secure boot, app sandboxing, permissions, key storage, update trust και τις πραγματικές διεπαφές που εκτίθενται.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Ασφάλεια Κινητών Συσκευών**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Mobile Platforms**
  Στο **Mobile Platforms**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.
- **Mobile Threat Model**
  Στο **Mobile Threat Model**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.
- **Improving Mobile Ασφάλεια**
  Στο **Improving Mobile Ασφάλεια**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.
- **Σύγχρονο mobile-security additions**
  Στο **Σύγχρονο mobile-security additions**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.
- **Verification standards**
  Για το **Verification standards**, ξεχώρισε normative specification από tutorial ή vendor summary. Κατέγραψε έκδοση/ημερομηνία, ποιο requirement στηρίζει το συμπέρασμα και ποιο μέρος του **Ασφάλεια Κινητών Συσκευών** χρειάζεται επανέλεγχο όταν αλλάξει η πηγή.
- **Safe lab ideas**
  Στο **Safe lab ideas**, μετέτρεψε τη θεωρία του **Ασφάλεια Κινητών Συσκευών** σε ελέγξιμα κριτήρια: τι πρέπει να μπορείς να εξηγήσεις, ποιο λάθος assumption εμφανίζεται συχνότερα, ποιο safe lab το αποκαλύπτει και ποιο retest αποδεικνύει ότι το διόρθωσες.
- **Mobile application architecture review**
  Στο **Mobile application architecture review**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.
- **Credential and secret handling**
  Για το **Credential and secret handling**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Authentication and authorization**
  Για το **Authentication and authorization**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Platform storage**
  Για το **Platform storage**, κατέγραψε ποιος μπορεί να γράψει/διαβάσει το state, πού αποθηκεύεται, πώς προστατεύεται at rest, ποιο backup/sync behavior υπάρχει και πότε το data πρέπει να διαγράφεται ή να ανακαλείται.
- **Network security**
  Στο **Network security**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.
- **Deep links, intents, and URL schemes**
  Για το **Deep links, intents, and URL schemes**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **WebViews and embedded browsers**
  Στο **WebViews and embedded browsers**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.
- **Permissions and privacy**
  Για το **Permissions and privacy**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Build and release security**
  Για το **Build and release security**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **Device integrity and risk signals**
  Στο **Device integrity and risk signals**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.
- **Enterprise mobile controls**
  Στο **Enterprise mobile controls**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.
- **Mobile logging**
  Στο **Mobile logging**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Mobile security review checklist**
  Στο **Mobile security review checklist**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Ασφάλεια Κινητών Συσκευών**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε δική σου συσκευή, emulator ή development board. Προτίμησε static analysis, documented debug interfaces και benign sample apps/firmware. Απόφυγε tests σε τρίτες συσκευές ή ασύρματα περιβάλλοντα.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Ασφάλεια Κινητών Συσκευών**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Ασφάλεια Κινητών Συσκευών** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 017](../../English/05-Mobile-IoT-and-Hardware/17-Mobile-Security.md)
