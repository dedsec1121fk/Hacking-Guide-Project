# RAG, Vector Databases και AI Retrieval Security

> **Ελληνική έκδοση — Μάθημα 138.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands παραμένουν στα Αγγλικά όπου αυτό αυξάνει την ακρίβεια.

Το RAG προσθέτει ingestion, embeddings, vector stores και retrieval ως νέα trust boundaries. Μελέτησε authorization, provenance και indirect prompt injection.

> **Όριο εξουσιοδοτημένης χρήσης:** Κάνε πρακτικές δοκιμές μόνο σε συστήματα, κώδικα, λογαριασμούς, captures και lab environments που σου ανήκουν ή για τα οποία έχεις ρητή άδεια. Προτίμησε localhost, synthetic data, disposable VMs/containers και read-only analysis.

## Μαθησιακοί στόχοι

Στο τέλος πρέπει να μπορείς να:

- εξηγήσεις το **RAG architecture and trust boundaries** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **document ingestion and parsing** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **chunking and embeddings** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **vector-store tenancy and authorization** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **retrieval-time metadata filters** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **indirect prompt injection** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Όρισε ownership/identity, state transition, trust boundary και το ελάχιστο evidence που χρειάζεται για ασφαλή validation.

## Βαθιές τεχνικές έννοιες

### 1. RAG architecture και trust boundaries

RAG έχει ingestion, indexing, retrieval, prompt assembly, model και output layers. Retrieved text είναι untrusted data και δεν πρέπει να αποκτά authority πάνω σε deterministic application/tool policy.

### 2. ingestion και parsing

Documents μπορεί να έχουν malformed/active content, hidden text ή adversarial instructions. Περιορίσε formats, parse σε constrained pipeline, βάλε resource limits και κράτησε source provenance.

### 3. chunking και embeddings

Chunking/embeddings επηρεάζουν retrieval αλλά security labels όπως tenant/classification/source πρέπει να μένουν explicit metadata και όχι να προκύπτουν από similarity.

### 4. tenancy και authorization

Vector similarity δεν είναι authorization. Κάνε server-side tenant/resource filtering πριν το content μπει στο model context και δοκίμασε isolation με δύο synthetic tenants.

### 5. metadata filters

Filters πρέπει να κατασκευάζονται από trusted application state. Μην αφήνεις model/client να διευρύνει tenant, classification ή document-state constraints.

### 6. indirect prompt injection

Retrieved document μπορεί να προσπαθήσει να χειραγωγήσει model/tools. Χώρισε instructions από data, βάλε deterministic authorization έξω από model και ελάχιστα tool permissions.

### 7. source provenance και citations

Κράτησε document ID/version, owner/tenant, classification και source location. Citations πρέπει να προέρχονται από τα πραγματικά retrieved sources και να επιτρέπουν audit.

### 8. poisoning, deletion και reindexing

Poisoned/stale content μπορεί να παραμένει σε embeddings μετά από source change. Χρειάζονται authenticated ingestion, deletion propagation, reindexing, version rollback και incident traceability.

## Engineering focus

Μετέτρεψε κάθε σημαντικό claim σε security invariant και regression test. Προτίμησε controls που μειώνουν authority, κάνουν explicit το state και αφήνουν αρκετή telemetry για root-cause analysis.

## Μοτίβα αστοχίας

- **Confused deputy:** privileged component ενεργεί για caller χωρίς επαρκή έλεγχο authority/context.
- **Identity/context confusion:** issuer, subject, tenant, role, origin, audience ή resource χρησιμοποιείται σε λάθος security context.
- **State/replay failure:** valid state γίνεται δεκτό όταν είναι stale, duplicated, revoked, reordered ή σε λάθος workflow step.
- **Parser mismatch:** δύο layers ερμηνεύουν διαφορετικά το ίδιο input/configuration.
- **Excess authority:** service, process, token, key ή admin role έχει περισσότερα permissions από όσα χρειάζεται.
- **Telemetry gap:** δεν καταγράφεται αρκετό actor/resource/policy/result context ώστε να γίνει αξιόπιστο investigation.

## Αμυντικό checklist

1. Γράψε το security invariant πριν από το test.
2. Μείωσε permissions/capabilities και lifetime όσο γίνεται.
3. Κάνε validation στο component που παίρνει την τελική security απόφαση.
4. Δέσε identity/state με σωστό tenant, resource, audience, origin ή protocol phase.
5. Βάλε explicit schemas, allowlists, resource limits και ασφαλή failure behavior.
6. Κατέγραψε actor, resource, operation, policy/version και result χωρίς secrets.
7. Προετοίμασε rollback/recovery πριν από state-changing lab.

## Καθοδηγούμενο εργαστήριο

### Lab 1 — Build a local toy RAG design on paper with public/sample documents and annotate trust boundaries.


### Lab 2 — Create synthetic “malicious instruction inside a document” examples and write expected safe model behavior without connecting external tools.


### Lab 3 — Design metadata filters for two fictional tenants and test access decisions with a table of allowed/denied retrievals.

Για κάθε lab χρησιμοποίησε owned/synthetic inputs και κράτησε objective, scope, version, expected/observed behavior, cleanup, remediation και regression result σύμφωνα με τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md).

## Evidence που αξίζει να κρατήσεις

- version/build και σχετικό configuration χωρίς secrets,
- μικρό διάγραμμα trust boundaries και data/state flow,
- sanitized logs, traces ή packet metadata,
- ακριβές test input με synthetic values,
- before/after αποτέλεσμα remediation,
- limitations και μη ελεγμένες υποθέσεις.

## Συχνά λάθη

- Αντιγραφή command χωρίς κατανόηση του mechanism.
- Χρήση production/τρίτου συστήματος ενώ αρκεί localhost ή synthetic data.
- Σύγχυση authentication με authorization, encryption με trust ή signature με safety.
- Θεώρηση ενός alert ως οριστικής απόδειξης.
- Παράβλεψη version, timing, identity context, parser behavior ή recovery.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary;
2. Ποιο state/identity μπορεί να γίνει stale ή να χρησιμοποιηθεί σε λάθος context;
3. Ποιο evidence θα σε έκανε να απορρίψεις την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά authority/blast radius;
5. Πώς θα κάνεις ασφαλές retest μετά τη remediation;

## Πλήρες αγγλικό μάθημα

[English Module 138](../../English/09-AI-GRC-Privacy-Data-and-Human-Security/138-RAG-Vector-Databases-and-AI-Retrieval-Security.md)

## Επόμενα μαθήματα

Σχετικά modules: **022, 025, 041, 046, 057, 071, 114**. Από το κύριο menu επίλεξε **Αναζήτηση μαθημάτων** για να βρεις σχετικά θέματα σε όλο το project.
