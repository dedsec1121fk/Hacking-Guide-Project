# Δικτύωση Termux, SSH και Τοπικές Υπηρεσίες

> **Ελληνική έκδοση — Μάθημα 030.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Το Termux προσφέρει Linux-like userland πάνω στο Android, αλλά δεν είναι πλήρης desktop διανομή ούτε παρακάμπτει το Android security model. Για αξιόπιστη χρήση πρέπει να κατανοείς storage permissions, package management, process lifetime, networking, SSH, Python environments και τα όρια που επιβάλλει το Android sandbox.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Δικτύωση Termux, SSH και Τοπικές Υπηρεσίες**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Networking mental model**
  Στο **Networking mental model**, χαρτογράφησε process → socket → interface/route → peer και ποια identity/host-key/DNS πληροφορία εμπιστεύεται κάθε βήμα. Ξεκίνα από loopback ή δικό σου SSH endpoint και επιβεβαίωσε listening scope, authentication και logs.
- **Local interfaces and routes**
  Στο **Local interfaces and routes**, χαρτογράφησε process → socket → interface/route → peer και ποια identity/host-key/DNS πληροφορία εμπιστεύεται κάθε βήμα. Ξεκίνα από loopback ή δικό σου SSH endpoint και επιβεβαίωσε listening scope, authentication και logs.
- **DNS basics**
  Στο **DNS basics**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.
- **HTTP and HTTPS inspection**
  Στο **HTTP and HTTPS inspection**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.
- **Running a localhost-only development service**
  Στο **Running a localhost-only development service**, χαρτογράφησε process → socket → interface/route → peer και ποια identity/host-key/DNS πληροφορία εμπιστεύεται κάθε βήμα. Ξεκίνα από loopback ή δικό σου SSH endpoint και επιβεβαίωσε listening scope, authentication και logs.
- **SSH concepts**
  Στο **SSH concepts**, χαρτογράφησε process → socket → interface/route → peer και ποια identity/host-key/DNS πληροφορία εμπιστεύεται κάθε βήμα. Ξεκίνα από loopback ή δικό σου SSH endpoint και επιβεβαίωσε listening scope, authentication και logs.
- **Host-key verification**
  Για το **Host-key verification**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **Port forwarding concepts**
  Στο **Port forwarding concepts**, χαρτογράφησε process → socket → interface/route → peer και ποια identity/host-key/DNS πληροφορία εμπιστεύεται κάθε βήμα. Ξεκίνα από loopback ή δικό σου SSH endpoint και επιβεβαίωσε listening scope, authentication και logs.
- **File transfer**
  Στο **File transfer**, χαρτογράφησε process → socket → interface/route → peer και ποια identity/host-key/DNS πληροφορία εμπιστεύεται κάθε βήμα. Ξεκίνα από loopback ή δικό σου SSH endpoint και επιβεβαίωσε listening scope, authentication και logs.
- **Local service inventory**
  Στο **Local service inventory**, χαρτογράφησε process → socket → interface/route → peer και ποια identity/host-key/DNS πληροφορία εμπιστεύεται κάθε βήμα. Ξεκίνα από loopback ή δικό σου SSH endpoint και επιβεβαίωσε listening scope, authentication και logs.
- **VPNs and Android**
  Στο **VPNs and Android**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.
- **Wireless limitations**
  Στο **Wireless limitations**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.
- **Mini lab — Local service map**
  Στο **Mini lab — Local service map**, όρισε συγκεκριμένο objective, owned/local scope, expected result και stop condition. Κράτησε μόνο sanitized evidence, σύγκρινε expected με observed behavior και ολοκλήρωσε με remediation και ίδιο regression test.
- **Mini lab — SSH trust checklist**
  Στο **Mini lab — SSH trust checklist**, όρισε συγκεκριμένο objective, owned/local scope, expected result και stop condition. Κράτησε μόνο sanitized evidence, σύγκρινε expected με observed behavior και ολοκλήρωσε με remediation και ίδιο regression test.
- **Practical networking drills in Termux**
  Στο **Practical networking drills in Termux**, όρισε συγκεκριμένο objective, owned/local scope, expected result και stop condition. Κράτησε μόνο sanitized evidence, σύγκρινε expected με observed behavior και ολοκλήρωσε με remediation και ίδιο regression test.
- **Loopback first**
  Στο **Loopback first**, χαρτογράφησε process → socket → interface/route → peer και ποια identity/host-key/DNS πληροφορία εμπιστεύεται κάθε βήμα. Ξεκίνα από loopback ή δικό σου SSH endpoint και επιβεβαίωσε listening scope, authentication και logs.
- **SSH administration checklist**
  Στο **SSH administration checklist**, χαρτογράφησε process → socket → interface/route → peer και ποια identity/host-key/DNS πληροφορία εμπιστεύεται κάθε βήμα. Ξεκίνα από loopback ή δικό σου SSH endpoint και επιβεβαίωσε listening scope, authentication και logs.
- **Name-resolution exercise**
  Στο **Name-resolution exercise**, όρισε συγκεκριμένο objective, owned/local scope, expected result και stop condition. Κράτησε μόνο sanitized evidence, σύγκρινε expected με observed behavior και ολοκλήρωσε με remediation και ίδιο regression test.
- **Mobile networking limitations**
  Στο **Mobile networking limitations**, σχεδίασε τα layers device/OS/app/firmware, τα privilege boundaries, permissions/entitlements και την αλυσίδα update/boot trust. Επιβεβαίωσε assumptions μόνο σε emulator, development board ή δική σου συσκευή.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Δικτύωση Termux, SSH και Τοπικές Υπηρεσίες**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Κράτησε όλα τα labs μέσα στο δικό σου τηλέφωνο, localhost ή συστήματα που ελέγχεις. Ξεκίνα με read-only commands και διατήρησε backups για scripts/configuration.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Δικτύωση Termux, SSH και Τοπικές Υπηρεσίες**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Δικτύωση Termux, SSH και Τοπικές Υπηρεσίες** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 030](../../English/10-Termux-and-Security-Automation/30-Termux-Networking-SSH-and-Local-Services.md)
