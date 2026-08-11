# Firmware, Embedded Systems και Ανάλυση Hardware Interfaces

> **Ελληνική έκδοση — Μάθημα 083.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Mobile, IoT και embedded συστήματα συνδυάζουν εφαρμογές, λειτουργικό, firmware, radios, hardware roots of trust και φυσική πρόσβαση. Το security model εξαρτάται από secure boot, app sandboxing, permissions, key storage, update trust και τις πραγματικές διεπαφές που εκτίθενται.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Firmware, Embedded Systems και Ανάλυση Hardware Interfaces**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Embedded threat model**
  Στο **Embedded threat model**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.
- **Boot chain**
  Στο **Boot chain**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.
- **Firmware images**
  Στο **Firmware images**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.
- **Filesystems**
  Στο **Filesystems**, κατέγραψε electrical/logical interface, access prerequisite, privilege boundary και τι data ή control surface εκθέτει. Χρησιμοποίησε μόνο development board ή δικό σου hardware και προτίμησε read-only identification πριν από οποιαδήποτε αλλαγή.
- **UART**
  Στο **UART**, κατέγραψε electrical/logical interface, access prerequisite, privilege boundary και τι data ή control surface εκθέτει. Χρησιμοποίησε μόνο development board ή δικό σου hardware και προτίμησε read-only identification πριν από οποιαδήποτε αλλαγή.
- **JTAG and SWD**
  Στο **JTAG and SWD**, κατέγραψε electrical/logical interface, access prerequisite, privilege boundary και τι data ή control surface εκθέτει. Χρησιμοποίησε μόνο development board ή δικό σου hardware και προτίμησε read-only identification πριν από οποιαδήποτε αλλαγή.
- **SPI and flash**
  Στο **SPI and flash**, κατέγραψε electrical/logical interface, access prerequisite, privilege boundary και τι data ή control surface εκθέτει. Χρησιμοποίησε μόνο development board ή δικό σου hardware και προτίμησε read-only identification πριν από οποιαδήποτε αλλαγή.
- **I2C**
  Στο **I2C**, κατέγραψε electrical/logical interface, access prerequisite, privilege boundary και τι data ή control surface εκθέτει. Χρησιμοποίησε μόνο development board ή δικό σου hardware και προτίμησε read-only identification πριν από οποιαδήποτε αλλαγή.
- **Secrets at rest**
  Για το **Secrets at rest**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **Firmware update security**
  Στο **Firmware update security**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.
- **Rollback protection**
  Για το **Rollback protection**, ακολούθησε την αλυσίδα trust από immutable/early-boot state μέχρι OS/application. Έλεγξε measured/verified state, key custody, update authorization, anti-rollback και τι αλλάζει όταν ο attacker έχει φυσική πρόσβαση.
- **Hardware root of trust**
  Στο **Hardware root of trust**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.
- **Safe firmware lab**
  Στο **Safe firmware lab**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.
- **Firmware SBOM and provenance**
  Για το **Firmware SBOM and provenance**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Firmware, Embedded Systems και Ανάλυση Hardware Interfaces**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε δική σου συσκευή, emulator ή development board. Προτίμησε static analysis, documented debug interfaces και benign sample apps/firmware. Απόφυγε tests σε τρίτες συσκευές ή ασύρματα περιβάλλοντα.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Firmware, Embedded Systems και Ανάλυση Hardware Interfaces**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Firmware, Embedded Systems και Ανάλυση Hardware Interfaces** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 083](../../English/05-Mobile-IoT-and-Hardware/83-Firmware-Embedded-Systems-and-Hardware-Interface-Analysis.md)
