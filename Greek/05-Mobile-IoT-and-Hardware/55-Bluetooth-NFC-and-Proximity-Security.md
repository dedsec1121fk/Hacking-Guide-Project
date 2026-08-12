# Ασφάλεια Bluetooth, NFC και Proximity

> **Ελληνική έκδοση — Μάθημα 055.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Mobile, IoT και embedded συστήματα συνδυάζουν εφαρμογές, λειτουργικό, firmware, radios, hardware roots of trust και φυσική πρόσβαση. Το security model εξαρτάται από secure boot, app sandboxing, permissions, key storage, update trust και τις πραγματικές διεπαφές που εκτίθενται.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Ασφάλεια Bluetooth, NFC και Proximity**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Bluetooth security model**
  Στο **Bluetooth security model**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.
- **Pairing guidance**
  Στο **Pairing guidance**, ξεχώρισε discovery από authenticated pairing και authorization. Κατέγραψε identifiers, negotiated security level, replay/proximity assumptions και ποιο application-layer check αποτρέπει το να μετατραπεί η απλή εγγύτητα σε authority.
- **BLE services and characteristics**
  Στο **BLE services and characteristics**, ξεχώρισε discovery από authenticated pairing και authorization. Κατέγραψε identifiers, negotiated security level, replay/proximity assumptions και ποιο application-layer check αποτρέπει το να μετατραπεί η απλή εγγύτητα σε authority.
- **Privacy**
  Για το **Privacy**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **NFC**
  Στο **NFC**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.
- **UWB and proximity claims**
  Στο **UWB and proximity claims**, ξεχώρισε discovery από authenticated pairing και authorization. Κατέγραψε identifiers, negotiated security level, replay/proximity assumptions και ποιο application-layer check αποτρέπει το να μετατραπεί η απλή εγγύτητα σε authority.
- **Device inventory exercise**
  Στο **Device inventory exercise**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.
- **Safe lab ideas**
  Στο **Safe lab ideas**, μετέτρεψε τη θεωρία του **Ασφάλεια Bluetooth, NFC και Proximity** σε ελέγξιμα κριτήρια: τι πρέπει να μπορείς να εξηγήσεις, ποιο λάθος assumption εμφανίζεται συχνότερα, ποιο safe lab το αποκαλύπτει και ποιο retest αποδεικνύει ότι το διόρθωσες.
- **Defensive checklist**
  Για το **Defensive checklist**, στο πλαίσιο του **Ασφάλεια Bluetooth, NFC και Proximity**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Checkpoint**
  Στο **Checkpoint**, μετέτρεψε τη θεωρία του **Ασφάλεια Bluetooth, NFC και Proximity** σε ελέγξιμα κριτήρια: τι πρέπει να μπορείς να εξηγήσεις, ποιο λάθος assumption εμφανίζεται συχνότερα, ποιο safe lab το αποκαλύπτει και ποιο retest αποδεικνύει ότι το διόρθωσες.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Ασφάλεια Bluetooth, NFC και Proximity**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε δική σου συσκευή, emulator ή development board. Προτίμησε static analysis, documented debug interfaces και benign sample apps/firmware. Απόφυγε tests σε τρίτες συσκευές ή ασύρματα περιβάλλοντα.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Ασφάλεια Bluetooth, NFC και Proximity**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Ασφάλεια Bluetooth, NFC και Proximity** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 055](../../English/05-Mobile-IoT-and-Hardware/55-Bluetooth-NFC-and-Proximity-Security.md)
