# Ασφάλεια AI και LLM

> **Ελληνική έκδοση — Μάθημα 025.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Η ασφάλεια δεν είναι μόνο τεχνική εκμετάλλευση. AI systems, privacy, governance, human factors και data lifecycle απαιτούν σαφείς owners, policies, consent, minimization, auditability και περιορισμό authority. Το risk πρέπει να συνδέεται με πραγματικές επιπτώσεις και όχι μόνο με severity labels.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Ασφάλεια AI και LLM**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Current landscape**
  Για το **Current landscape**, στο πλαίσιο του **Ασφάλεια AI και LLM**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Core risk families**
  Για το **Core risk families**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Prompt and context manipulation**
  Στο **Prompt and context manipulation**, ξεχώρισε model behavior από deterministic policy enforcement. Κατέγραψε untrusted inputs, tool/data permissions, retrieval provenance, output validation και human approval points.
- **Sensitive information disclosure**
  Για το **Sensitive information disclosure**, αντιμετώπισε model output ως untrusted suggestion. Βάλε deterministic authorization πριν από tool/data access, schema validation στα inputs/outputs, provenance στο retrieved context, bounded resources και human approval για irreversible ή high-impact ενέργειες.
- **Supply chain and provenance**
  Για το **Supply chain and provenance**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **Unsafe output handling**
  Για το **Unsafe output handling**, αντιμετώπισε model output ως untrusted suggestion. Βάλε deterministic authorization πριν από tool/data access, schema validation στα inputs/outputs, provenance στο retrieved context, bounded resources και human approval για irreversible ή high-impact ενέργειες.
- **Excessive agency**
  Για το **Excessive agency**, αντιμετώπισε model output ως untrusted suggestion. Βάλε deterministic authorization πριν από tool/data access, schema validation στα inputs/outputs, provenance στο retrieved context, bounded resources και human approval για irreversible ή high-impact ενέργειες.
- **Retrieval and memory risk**
  Στο **Retrieval and memory risk**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **Resource abuse**
  Για το **Resource abuse**, αντιμετώπισε model output ως untrusted suggestion. Βάλε deterministic authorization πριν από tool/data access, schema validation στα inputs/outputs, provenance στο retrieved context, bounded resources και human approval για irreversible ή high-impact ενέργειες.
- **Secure architecture pattern**
  Για το **Secure architecture pattern**, στο πλαίσιο του **Ασφάλεια AI και LLM**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Safe lab**
  Στο **Safe lab**, μετέτρεψε τη θεωρία του **Ασφάλεια AI και LLM** σε ελέγξιμα κριτήρια: τι πρέπει να μπορείς να εξηγήσεις, ποιο λάθος assumption εμφανίζεται συχνότερα, ποιο safe lab το αποκαλύπτει και ποιο retest αποδεικνύει ότι το διόρθωσες.
- **References**
  Για το **References**, ξεχώρισε normative specification από tutorial ή vendor summary. Κατέγραψε έκδοση/ημερομηνία, ποιο requirement στηρίζει το συμπέρασμα και ποιο μέρος του **Ασφάλεια AI και LLM** χρειάζεται επανέλεγχο όταν αλλάξει η πηγή.
- **AI system threat modeling**
  Στο **AI system threat modeling**, ξεχώρισε model behavior από deterministic policy enforcement. Κατέγραψε untrusted inputs, tool/data permissions, retrieval provenance, output validation και human approval points.
- **Trust boundaries for prompts and context**
  Για το **Trust boundaries for prompts and context**, αντιμετώπισε model output ως untrusted suggestion. Βάλε deterministic authorization πριν από tool/data access, schema validation στα inputs/outputs, provenance στο retrieved context, bounded resources και human approval για irreversible ή high-impact ενέργειες.
- **Indirect prompt injection**
  Για το **Indirect prompt injection**, παρακολούθησε το input από client μέχρι parser/framework/backend και πίσω. Κατέγραψε normalization, origin/session context, server-side authorization και output handling ώστε να εντοπίζεις το ακριβές trust boundary.
- **Tool and agent security**
  Στο **Tool and agent security**, ξεχώρισε model behavior από deterministic policy enforcement. Κατέγραψε untrusted inputs, tool/data permissions, retrieval provenance, output validation και human approval points.
- **Tool design principles**
  Για το **Tool design principles**, στο πλαίσιο του **Ασφάλεια AI και LLM**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Human approval**
  Για το **Human approval**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Retrieval-Augmented Generation security**
  Για το **Retrieval-Augmented Generation security**, αντιμετώπισε model output ως untrusted suggestion. Βάλε deterministic authorization πριν από tool/data access, schema validation στα inputs/outputs, provenance στο retrieved context, bounded resources και human approval για irreversible ή high-impact ενέργειες.
- **RAG controls**
  Στο **RAG controls**, ξεχώρισε model behavior από deterministic policy enforcement. Κατέγραψε untrusted inputs, tool/data permissions, retrieval provenance, output validation και human approval points.
- **Memory and personalization**
  Στο **Memory and personalization**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **Data leakage controls**
  Για το **Data leakage controls**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Ασφάλεια AI και LLM**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε synthetic data και role-play scenarios. Μην χρησιμοποιείς πραγματικά προσωπικά δεδομένα ή παραπλανητικές social-engineering δοκιμές χωρίς ρητή έγκριση.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Ασφάλεια AI και LLM**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Ασφάλεια AI και LLM** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 025](../../English/09-AI-GRC-Privacy-Data-and-Human-Security/25-AI-and-LLM-Security.md)
