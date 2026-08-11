# Agentic AI, MCP και Ασφάλεια Εργαλείων

> **Ελληνική έκδοση — Μάθημα 046.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Η ασφάλεια δεν είναι μόνο τεχνική εκμετάλλευση. AI systems, privacy, governance, human factors και data lifecycle απαιτούν σαφείς owners, policies, consent, minimization, auditability και περιορισμό authority. Το risk πρέπει να συνδέεται με πραγματικές επιπτώσεις και όχι μόνο με severity labels.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Agentic AI, MCP και Ασφάλεια Εργαλείων**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Why agents change the threat model**
  Για το **Why agents change the threat model**, αντιμετώπισε model output ως untrusted suggestion. Βάλε deterministic authorization πριν από tool/data access, schema validation στα inputs/outputs, provenance στο retrieved context, bounded resources και human approval για irreversible ή high-impact ενέργειες.
- **Agent components to model**
  Στο **Agent components to model**, ξεχώρισε model behavior από deterministic policy enforcement. Κατέγραψε untrusted inputs, tool/data permissions, retrieval provenance, output validation και human approval points.
- **Prompt injection is an authorization problem too**
  Για το **Prompt injection is an authorization problem too**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Least privilege for tools**
  Για το **Least privilege for tools**, αντιμετώπισε model output ως untrusted suggestion. Βάλε deterministic authorization πριν από tool/data access, schema validation στα inputs/outputs, provenance στο retrieved context, bounded resources και human approval για irreversible ή high-impact ενέργειες.
- **Tool descriptions are part of the trust surface**
  Για το **Tool descriptions are part of the trust surface**, σύνδεσε Android package/runtime behavior με UID sandbox, exported components, Binder/Intent boundaries, signing identity και Keystore-backed secrets. Επιβεβαίωσε το behavior σε δικό σου APK ή emulator και όχι σε τρίτες εφαρμογές.
- **Model Context Protocol**
  Στο **Model Context Protocol**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.
- **Human approval**
  Για το **Human approval**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Memory security**
  Στο **Memory security**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **Inter-agent communication**
  Στο **Inter-agent communication**, ξεχώρισε model behavior από deterministic policy enforcement. Κατέγραψε untrusted inputs, tool/data permissions, retrieval provenance, output validation και human approval points.
- **Safe failure**
  Για το **Safe failure**, αντιμετώπισε model output ως untrusted suggestion. Βάλε deterministic authorization πριν από tool/data access, schema validation στα inputs/outputs, provenance στο retrieved context, bounded resources και human approval για irreversible ή high-impact ενέργειες.
- **Evaluation**
  Για το **Evaluation**, αντιμετώπισε model output ως untrusted suggestion. Βάλε deterministic authorization πριν από tool/data access, schema validation στα inputs/outputs, provenance στο retrieved context, bounded resources και human approval για irreversible ή high-impact ενέργειες.
- **Lab — Harmless agent tool boundary**
  Στο **Lab — Harmless agent tool boundary**, ξεχώρισε model behavior από deterministic policy enforcement. Κατέγραψε untrusted inputs, tool/data permissions, retrieval provenance, output validation και human approval points.
- **Primary references**
  Για το **Primary references**, ξεχώρισε normative specification από tutorial ή vendor summary. Κατέγραψε έκδοση/ημερομηνία, ποιο requirement στηρίζει το συμπέρασμα και ποιο μέρος του **Agentic AI, MCP και Ασφάλεια Εργαλείων** χρειάζεται επανέλεγχο όταν αλλάξει η πηγή.
- **Agent/tool security depth**
  Στο **Agent/tool security depth**, ξεχώρισε model behavior από deterministic policy enforcement. Κατέγραψε untrusted inputs, tool/data permissions, retrieval provenance, output validation και human approval points.
- **Tool contracts**
  Για το **Tool contracts**, αντιμετώπισε model output ως untrusted suggestion. Βάλε deterministic authorization πριν από tool/data access, schema validation στα inputs/outputs, provenance στο retrieved context, bounded resources και human approval για irreversible ή high-impact ενέργειες.
- **Untrusted context**
  Για το **Untrusted context**, αντιμετώπισε model output ως untrusted suggestion. Βάλε deterministic authorization πριν από tool/data access, schema validation στα inputs/outputs, provenance στο retrieved context, bounded resources και human approval για irreversible ή high-impact ενέργειες.
- **High-impact actions**
  Για το **High-impact actions**, αντιμετώπισε model output ως untrusted suggestion. Βάλε deterministic authorization πριν από tool/data access, schema validation στα inputs/outputs, provenance στο retrieved context, bounded resources και human approval για irreversible ή high-impact ενέργειες.
- **Observability**
  Για το **Observability**, αντιμετώπισε model output ως untrusted suggestion. Βάλε deterministic authorization πριν από tool/data access, schema validation στα inputs/outputs, provenance στο retrieved context, bounded resources και human approval για irreversible ή high-impact ενέργειες.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Agentic AI, MCP και Ασφάλεια Εργαλείων**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε synthetic data και role-play scenarios. Μην χρησιμοποιείς πραγματικά προσωπικά δεδομένα ή παραπλανητικές social-engineering δοκιμές χωρίς ρητή έγκριση.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Agentic AI, MCP και Ασφάλεια Εργαλείων**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Agentic AI, MCP και Ασφάλεια Εργαλείων** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 046](../../English/09-AI-GRC-Privacy-Data-and-Human-Security/46-Agentic-AI-MCP-and-Tool-Security.md)
