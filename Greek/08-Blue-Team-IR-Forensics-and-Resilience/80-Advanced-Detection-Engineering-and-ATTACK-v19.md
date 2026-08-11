# Προχωρημένο Detection Engineering και MITRE ATT&CK v19

> **Ελληνική έκδοση — Μάθημα 080.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Blue-team εργασία σημαίνει να μετατρέπεις telemetry σε τεκμηριωμένα συμπεράσματα. Ένα alert δεν είναι απόδειξη από μόνο του. Χρειάζεται timeline, identity context, process/network relationships, data provenance και κατανόηση του τι δεν καταγράφεται. Η ανθεκτικότητα επεκτείνεται από detection μέχρι containment, recovery και verification.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Προχωρημένο Detection Engineering και MITRE ATT&CK v19**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

**Τρέχουσα έκδοση:** MITRE ATT&CK v19.2 (6 Αυγούστου 2026). Το major v19 εισήγαγε τον διαχωρισμό του Enterprise Defense Evasion σε **Stealth** και **Defense Impairment**· το v19.2 είναι Agile update με κυρίως Groups/Software ενημερώσεις.

- **ATT&CK in 2026**
  Για το **ATT&CK in 2026**, ξεκίνα από observable behavior και διαθέσιμα data sources, όχι από technique ID μόνο. Γράψε detection hypothesis, required fields, expected benign collisions, tuning strategy και validation event ώστε η κάλυψη να είναι μετρήσιμη.
- **Start with behavior**
  Για το **Start with behavior**, σύνδεσε Android package/runtime behavior με UID sandbox, exported components, Binder/Intent boundaries, signing identity και Keystore-backed secrets. Επιβεβαίωσε το behavior σε δικό σου APK ή emulator και όχι σε τρίτες εφαρμογές.
- **Detection pipeline**
  Στο **Detection pipeline**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Atomic versus correlated analytics**
  Για το **Atomic versus correlated analytics**, ξεκίνα από observable behavior και διαθέσιμα data sources, όχι από technique ID μόνο. Γράψε detection hypothesis, required fields, expected benign collisions, tuning strategy και validation event ώστε η κάλυψη να είναι μετρήσιμη.
- **Sequence detections**
  Για το **Sequence detections**, ξεκίνα από observable behavior και διαθέσιμα data sources, όχι από technique ID μόνο. Γράψε detection hypothesis, required fields, expected benign collisions, tuning strategy και validation event ώστε η κάλυψη να είναι μετρήσιμη.
- **Rarity and baseline**
  Για το **Rarity and baseline**, ξεκίνα από observable behavior και διαθέσιμα data sources, όχι από technique ID μόνο. Γράψε detection hypothesis, required fields, expected benign collisions, tuning strategy και validation event ώστε η κάλυψη να είναι μετρήσιμη.
- **Entity context**
  Για το **Entity context**, ξεκίνα από observable behavior και διαθέσιμα data sources, όχι από technique ID μόνο. Γράψε detection hypothesis, required fields, expected benign collisions, tuning strategy και validation event ώστε η κάλυψη να είναι μετρήσιμη.
- **Detection of defense impairment**
  Στο **Detection of defense impairment**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Stealth-related behavior**
  Για το **Stealth-related behavior**, ξεκίνα από observable behavior και διαθέσιμα data sources, όχι από technique ID μόνο. Γράψε detection hypothesis, required fields, expected benign collisions, tuning strategy και validation event ώστε η κάλυψη να είναι μετρήσιμη.
- **Data quality**
  Για το **Data quality**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Sigma and portable logic**
  Για το **Sigma and portable logic**, ξεκίνα από observable behavior και διαθέσιμα data sources, όχι από technique ID μόνο. Γράψε detection hypothesis, required fields, expected benign collisions, tuning strategy και validation event ώστε η κάλυψη να είναι μετρήσιμη.
- **Network detections**
  Στο **Network detections**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.
- **Identity detections**
  Για το **Identity detections**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Detection testing**
  Στο **Detection testing**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **False positives and tuning**
  Για το **False positives and tuning**, ξεκίνα από observable behavior και διαθέσιμα data sources, όχι από technique ID μόνο. Γράψε detection hypothesis, required fields, expected benign collisions, tuning strategy και validation event ώστε η κάλυψη να είναι μετρήσιμη.
- **Detection-as-code**
  Στο **Detection-as-code**, όρισε πρώτα την αναμενόμενη συμπεριφορά και τις telemetry sources που πρέπει να τη δείχνουν. Συσχέτισε identity, process, network και χρόνο, κατέγραψε blind spots και ξεχώρισε observation από inference.
- **Coverage metrics**
  Για το **Coverage metrics**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Προχωρημένο Detection Engineering και MITRE ATT&CK v19**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε synthetic logs και harmless local events. Κατέγραψε expected evidence πριν το test και σύγκρινε με ό,τι πραγματικά συλλέχθηκε.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Προχωρημένο Detection Engineering και MITRE ATT&CK v19**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Προχωρημένο Detection Engineering και MITRE ATT&CK v19** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 080](../../English/08-Blue-Team-IR-Forensics-and-Resilience/80-Advanced-Detection-Engineering-and-ATTACK-v19.md)
