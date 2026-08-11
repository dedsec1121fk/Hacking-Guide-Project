# AI-Generated Code, Vibe Coding και Secure Review

> **Ελληνική έκδοση — Μάθημα 139.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands παραμένουν στα Αγγλικά όπου αυτό αυξάνει την ακρίβεια.

Αντιμετώπισε AI-generated/vibe-coded κώδικα σαν contribution από άγνωστο developer: review dependencies, authz, parsing, secrets, negative tests και deployment permissions.

> **Όριο εξουσιοδοτημένης χρήσης:** Κάνε πρακτικές δοκιμές μόνο σε συστήματα, κώδικα, λογαριασμούς, captures και lab environments που σου ανήκουν ή για τα οποία έχεις ρητή άδεια. Προτίμησε localhost, synthetic data, disposable VMs/containers και read-only analysis.

## Μαθησιακοί στόχοι

Στο τέλος πρέπει να μπορείς να:

- εξηγήσεις το **generated-code trust model** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **specification before generation** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **dependency and package verification** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **secret handling and configuration** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **authentication/authorization review** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **input validation and unsafe parsing** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Όρισε ownership/identity, state transition, trust boundary και το ελάχιστο evidence που χρειάζεται για ασφαλή validation.

## Βαθιές τεχνικές έννοιες

### 1. AI-generated code trust model

Αντιμετώπισε generated code σαν untrusted external contribution: μπορεί να είναι plausible αλλά λάθος, stale ή insecure. Human ownership, review, tests και security controls παραμένουν υποχρεωτικά.

### 2. specification πριν από generation

Γράψε invariants, types, trust boundaries, error behavior και constraints πριν ζητήσεις implementation. Έτσι ελέγχεις generated code απέναντι σε specification και όχι απέναντι στο πόσο πειστικό φαίνεται.

### 3. dependency και package verification

Model μπορεί να προτείνει obsolete, typo-squatted ή ανύπαρκτο package. Επιβεβαίωσε package από official ecosystem, pin/lock versions και review transitive dependencies πριν install.

### 4. secrets και configuration

Generated examples συχνά έχουν placeholder secrets, debug mode, broad CORS ή unsafe defaults. Κράτησε secrets έξω από prompts/source και κάνε ξεχωριστό production configuration review.

### 5. authentication και authorization review

Generated handler μπορεί να ελέγχει login αλλά να ξεχνά object/tenant authorization. Έλεγξε subject-resource-action-tenant context και γράψε negative tests με πολλαπλές synthetic identities.

### 6. input validation και parsing

Generated parsers συχνά καλύπτουν μόνο happy path. Όρισε schema, size/depth limits, canonicalization, safe deserialization και σωστό output encoding για κάθε sink.

### 7. generated tests και false confidence

Generated tests μπορεί να αντιγράφουν την ίδια λανθασμένη υπόθεση με τον generated code. Πρόσθεσε independently designed negative/adversarial cases και δες αν test αποτυγχάνει όταν σπάσεις σκόπιμα control σε toy branch.

### 8. human review, provenance και change control

Εφάρμοσε protected branches, review, CI, provenance, dependency/secret scanning και rollback ανεξάρτητα από το ποιος έγραψε κώδικα. AI assistance δεν αλλάζει το ownership του τελικού artifact.

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

### Lab 1 — Take a small local script you own and build a security-review checklist covering inputs, files, subprocesses, network, secrets and dependencies.


### Lab 2 — Write five negative tests for a generated login/API example using fictional data.


### Lab 3 — Compare two AI-generated designs for the same feature and choose the one with smaller authority and fewer dependencies, documenting why.

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

[English Module 139](../../English/09-AI-GRC-Privacy-Data-and-Human-Security/139-AI-Generated-Code-Vibe-Coding-and-Secure-Review.md)

## Επόμενα μαθήματα

Σχετικά modules: **022, 025, 036, 040, 041, 046, 097, 098, 108, 109**. Από το κύριο menu επίλεξε **Αναζήτηση μαθημάτων** για να βρεις σχετικά θέματα σε όλο το project.
