# Cloud Logging, Detection και Cross-Cloud Investigation

> **Ελληνική έκδοση — Μάθημα 137.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands παραμένουν στα Αγγλικά όπου αυτό αυξάνει την ακρίβεια.

Μάθε να ερευνάς cloud events με identity/action/resource/result, central logging, immutable retention, temporary credentials και cross-cloud correlation.

> **Όριο εξουσιοδοτημένης χρήσης:** Κάνε πρακτικές δοκιμές μόνο σε συστήματα, κώδικα, λογαριασμούς, captures και lab environments που σου ανήκουν ή για τα οποία έχεις ρητή άδεια. Προτίμησε localhost, synthetic data, disposable VMs/containers και read-only analysis.

## Μαθησιακοί στόχοι

Στο τέλος πρέπει να μπορείς να:

- εξηγήσεις το **control-plane audit logs** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **identity and token context** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **data-plane versus management-plane telemetry** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **multi-account/project/subscription aggregation** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **log integrity and retention** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **time synchronization and event ordering** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Όρισε ownership/identity, state transition, trust boundary και το ελάχιστο evidence που χρειάζεται για ασφαλή validation.

## Βαθιές τεχνικές έννοιες

### 1. control-plane audit logs

Cloud audit logs καλύπτουν administrative/API changes σε identity, policy, networking και resources. Ενεργοποίησέ τα και κεντρικοποίησέ τα πριν από incident γιατί μη καταγεγραμμένο event δεν ανακατασκευάζεται μετά.

### 2. identity και token context

Cloud event χρειάζεται caller, assumed role/service principal, session/token context, source και target resource/account/tenant. Συσχέτισε temporary identity με parent workload/human.

### 3. data-plane έναντι management-plane logs

Management logs δείχνουν configuration/control και data-plane logs πραγματική data/workload access. Investigation συχνά χρειάζεται και τα δύο για να συνδέσει policy change με επόμενη χρήση.

### 4. central aggregation

Στείλε logs σε independent security account/project με περιορισμένα delete/admin permissions. Έτσι compromise ενός workload δεν διαγράφει εύκολα τη μοναδική evidence copy.

### 5. integrity και retention

Χρησιμοποίησε retention, immutability όπου ταιριάζει, restricted deletion και export verification. Retention πρέπει να λαμβάνει υπόψη detection latency, privacy/legal και cost.

### 6. time synchronization και ordering

Distributed events φτάνουν αργά ή έχουν διαφορετικά timestamps. Κράτησε original και ingestion time και χρησιμοποίησε request/session IDs αντί να θεωρείς display order causal order.

### 7. cross-cloud normalization

Providers/SaaS έχουν διαφορετικά names για principals/resources/actions. Κάνε normalization σε κοινό schema αλλά διατήρησε raw provider fields ώστε να μη χάνεται semantics.

### 8. investigation pivots και evidence preservation

Ξεκίνα από identity, resource, IP, request ID, key ή time window και κάνε pivots σε identity/control plane/workload/network/data access. Document queries/time zone και hash important exports.

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

### Lab 1 — Create a synthetic multi-cloud event dataset and normalize five fields across three provider-style schemas.


### Lab 2 — Build an investigation timeline for a fictional policy change followed by unusual access and remediation.


### Lab 3 — Design retention tiers for high-value audit logs, noisy data-plane logs and forensic snapshots.

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

[English Module 137](../../English/08-Blue-Team-IR-Forensics-and-Resilience/137-Cloud-Logging-Detection-and-Cross-Cloud-Investigation.md)

## Επόμενα μαθήματα

Σχετικά modules: **019, 023, 037, 047, 059, 076, 080, 105, 106**. Από το κύριο menu επίλεξε **Αναζήτηση μαθημάτων** για να βρεις σχετικά θέματα σε όλο το project.
