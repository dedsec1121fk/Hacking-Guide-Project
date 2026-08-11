# Ανθεκτικότητα και Ανάκαμψη από Ransomware

> **Ελληνική έκδοση — Μάθημα 038.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Blue-team εργασία σημαίνει να μετατρέπεις telemetry σε τεκμηριωμένα συμπεράσματα. Ένα alert δεν είναι απόδειξη από μόνο του. Χρειάζεται timeline, identity context, process/network relationships, data provenance και κατανόηση του τι δεν καταγράφεται. Η ανθεκτικότητα επεκτείνεται από detection μέχρι containment, recovery και verification.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Ανθεκτικότητα και Ανάκαμψη από Ransomware**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Ransomware is an operational crisis**
  Για το **Ransomware is an operational crisis**, αξιολόγησε identity containment, segmentation, immutable/offline recovery copies, restore priority και business communications ως ενιαίο resilience problem. Μέτρα recovery με πραγματικό restore test και όχι μόνο με την ύπαρξη backup.
- **Prevention layers**
  Για το **Prevention layers**, αξιολόγησε identity containment, segmentation, immutable/offline recovery copies, restore priority και business communications ως ενιαίο resilience problem. Μέτρα recovery με πραγματικό restore test και όχι μόνο με την ύπαρξη backup.
- **Backup architecture**
  Για το **Backup architecture**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Identity recovery**
  Για το **Identity recovery**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Initial response priorities**
  Για το **Initial response priorities**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **Recovery sequencing**
  Για το **Recovery sequencing**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Clean recovery**
  Για το **Clean recovery**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Communications**
  Για το **Communications**, αξιολόγησε identity containment, segmentation, immutable/offline recovery copies, restore priority και business communications ως ενιαίο resilience problem. Μέτρα recovery με πραγματικό restore test και όχι μόνο με την ύπαρξη backup.
- **Payment considerations**
  Για το **Payment considerations**, αξιολόγησε identity containment, segmentation, immutable/offline recovery copies, restore priority και business communications ως ενιαίο resilience problem. Μέτρα recovery με πραγματικό restore test και όχι μόνο με την ύπαρξη backup.
- **Tabletop exercise**
  Στο **Tabletop exercise**, όρισε συγκεκριμένο objective, owned/local scope, expected result και stop condition. Κράτησε μόνο sanitized evidence, σύγκρινε expected με observed behavior και ολοκλήρωσε με remediation και ίδιο regression test.
- **Primary reference**
  Για το **Primary reference**, ξεχώρισε normative specification από tutorial ή vendor summary. Κατέγραψε έκδοση/ημερομηνία, ποιο requirement στηρίζει το συμπέρασμα και ποιο μέρος του **Ανθεκτικότητα και Ανάκαμψη από Ransomware** χρειάζεται επανέλεγχο όταν αλλάξει η πηγή.
- **Ransomware resilience in more depth**
  Για το **Ransomware resilience in more depth**, αξιολόγησε identity containment, segmentation, immutable/offline recovery copies, restore priority και business communications ως ενιαίο resilience problem. Μέτρα recovery με πραγματικό restore test και όχι μόνο με την ύπαρξη backup.
- **Identity containment**
  Για το **Identity containment**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Recovery order**
  Για το **Recovery order**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Tabletop realism**
  Στο **Tabletop realism**, όρισε συγκεκριμένο objective, owned/local scope, expected result και stop condition. Κράτησε μόνο sanitized evidence, σύγκρινε expected με observed behavior και ολοκλήρωσε με remediation και ίδιο regression test.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Ανθεκτικότητα και Ανάκαμψη από Ransomware**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε synthetic logs και harmless local events. Κατέγραψε expected evidence πριν το test και σύγκρινε με ό,τι πραγματικά συλλέχθηκε.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Ανθεκτικότητα και Ανάκαμψη από Ransomware**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Ανθεκτικότητα και Ανάκαμψη από Ransomware** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 038](../../English/08-Blue-Team-IR-Forensics-and-Resilience/38-Ransomware-Resilience-and-Recovery.md)
