# Reverse Engineering Android Εφαρμογών και Mobile App Internals

> **Ελληνική έκδοση — Μάθημα 082.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Mobile, IoT και embedded συστήματα συνδυάζουν εφαρμογές, λειτουργικό, firmware, radios, hardware roots of trust και φυσική πρόσβαση. Το security model εξαρτάται από secure boot, app sandboxing, permissions, key storage, update trust και τις πραγματικές διεπαφές που εκτίθενται.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Reverse Engineering Android Εφαρμογών και Mobile App Internals**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Package anatomy**
  Για το **Package anatomy**, σύνδεσε Android package/runtime behavior με UID sandbox, exported components, Binder/Intent boundaries, signing identity και Keystore-backed secrets. Επιβεβαίωσε το behavior σε δικό σου APK ή emulator και όχι σε τρίτες εφαρμογές.
- **DEX and ART**
  Για το **DEX and ART**, σύνδεσε Android package/runtime behavior με UID sandbox, exported components, Binder/Intent boundaries, signing identity και Keystore-backed secrets. Επιβεβαίωσε το behavior σε δικό σου APK ή emulator και όχι σε τρίτες εφαρμογές.
- **Manifest as attack-surface map**
  Για το **Manifest as attack-surface map**, σύνδεσε Android package/runtime behavior με UID sandbox, exported components, Binder/Intent boundaries, signing identity και Keystore-backed secrets. Επιβεβαίωσε το behavior σε δικό σου APK ή emulator και όχι σε τρίτες εφαρμογές.
- **Intent trust boundaries**
  Για το **Intent trust boundaries**, σύνδεσε Android package/runtime behavior με UID sandbox, exported components, Binder/Intent boundaries, signing identity και Keystore-backed secrets. Επιβεβαίωσε το behavior σε δικό σου APK ή emulator και όχι σε τρίτες εφαρμογές.
- **Binder and IPC**
  Για το **Binder and IPC**, σύνδεσε Android package/runtime behavior με UID sandbox, exported components, Binder/Intent boundaries, signing identity και Keystore-backed secrets. Επιβεβαίωσε το behavior σε δικό σου APK ή emulator και όχι σε τρίτες εφαρμογές.
- **Application sandbox**
  Για το **Application sandbox**, σύνδεσε Android package/runtime behavior με UID sandbox, exported components, Binder/Intent boundaries, signing identity και Keystore-backed secrets. Επιβεβαίωσε το behavior σε δικό σου APK ή emulator και όχι σε τρίτες εφαρμογές.
- **Signing and update identity**
  Για το **Signing and update identity**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Network Ασφάλεια Configuration**
  Στο **Network Ασφάλεια Configuration**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.
- **Keystore**
  Για το **Keystore**, σύνδεσε Android package/runtime behavior με UID sandbox, exported components, Binder/Intent boundaries, signing identity και Keystore-backed secrets. Επιβεβαίωσε το behavior σε δικό σου APK ή emulator και όχι σε τρίτες εφαρμογές.
- **WebView**
  Για το **WebView**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **Deep links and app links**
  Για το **Deep links and app links**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **Content providers**
  Για το **Content providers**, σύνδεσε Android package/runtime behavior με UID sandbox, exported components, Binder/Intent boundaries, signing identity και Keystore-backed secrets. Επιβεβαίωσε το behavior σε δικό σου APK ή emulator και όχι σε τρίτες εφαρμογές.
- **Native/JNI boundary**
  Για το **Native/JNI boundary**, σύνδεσε Android package/runtime behavior με UID sandbox, exported components, Binder/Intent boundaries, signing identity και Keystore-backed secrets. Επιβεβαίωσε το behavior σε δικό σου APK ή emulator και όχι σε τρίτες εφαρμογές.
- **Obfuscation**
  Για το **Obfuscation**, σύνδεσε Android package/runtime behavior με UID sandbox, exported components, Binder/Intent boundaries, signing identity και Keystore-backed secrets. Επιβεβαίωσε το behavior σε δικό σου APK ή emulator και όχι σε τρίτες εφαρμογές.
- **Dynamic analysis**
  Για το **Dynamic analysis**, σύνδεσε Android package/runtime behavior με UID sandbox, exported components, Binder/Intent boundaries, signing identity και Keystore-backed secrets. Επιβεβαίωσε το behavior σε δικό σου APK ή emulator και όχι σε τρίτες εφαρμογές.
- **Static analysis lab**
  Για το **Static analysis lab**, ακολούθησε data/control flow από source σε sink, σημείωσε validation και ownership assumptions και έλεγξε πού εφαρμόζεται enforcement. Χρησιμοποίησε tests και static/runtime evidence για να ξεχωρίσεις root cause από απλό code smell.
- **Termux role**
  Για το **Termux role**, δες το workflow σαν reproducible local environment: paths, package/source provenance, permissions, environment state, error handling και rollback. Στο Termux προτίμησε standard-library εργαλεία, explicit paths και δοκιμές σε harmless local files/services.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Reverse Engineering Android Εφαρμογών και Mobile App Internals**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε δική σου συσκευή, emulator ή development board. Προτίμησε static analysis, documented debug interfaces και benign sample apps/firmware. Απόφυγε tests σε τρίτες συσκευές ή ασύρματα περιβάλλοντα.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Reverse Engineering Android Εφαρμογών και Mobile App Internals**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Reverse Engineering Android Εφαρμογών και Mobile App Internals** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 082](../../English/05-Mobile-IoT-and-Hardware/82-Android-Application-Reverse-Engineering-and-Mobile-App-Internals.md)
