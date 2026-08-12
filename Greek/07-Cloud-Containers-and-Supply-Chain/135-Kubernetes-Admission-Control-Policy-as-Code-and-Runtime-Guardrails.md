# Kubernetes Admission Control, Policy-as-Code και Runtime Guardrails

> **Ελληνική έκδοση — Μάθημα 135.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands παραμένουν στα Αγγλικά όπου αυτό αυξάνει την ακρίβεια.

Κατανόησε Kubernetes admission lifecycle, validation/mutation, policy-as-code, Pod Security, image trust και runtime drift.

> **Όριο εξουσιοδοτημένης χρήσης:** Κάνε πρακτικές δοκιμές μόνο σε συστήματα, κώδικα, λογαριασμούς, captures και lab environments που σου ανήκουν ή για τα οποία έχεις ρητή άδεια. Προτίμησε localhost, synthetic data, disposable VMs/containers και read-only analysis.

## Μαθησιακοί στόχοι

Στο τέλος πρέπει να μπορείς να:

- εξηγήσεις το **API admission lifecycle** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **mutating versus validating admission** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **Pod Security Standards concepts** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **policy-as-code engines** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **image provenance and allowlists** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **namespace and service-account context** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Όρισε ownership/identity, state transition, trust boundary και το ελάχιστο evidence που χρειάζεται για ασφαλή validation.

## Βαθιές τεχνικές έννοιες

### 1. admission lifecycle

Kubernetes admission εκτελείται μετά authn/authz και πριν αποθήκευση object. Είναι policy point για desired configuration και δεν αντικαθιστά runtime isolation, RBAC ή drift detection.

### 2. mutating έναντι validating admission

Mutating admission αλλάζει/defaults object και validating αποφασίζει accept/reject. Κράτησε mutations predictable και observable ώστε να μη δημιουργούν hidden configuration που δυσκολεύει signatures και debugging.

### 3. Pod Security Standards

Pod Security Standards ορίζουν baseline/restricted expectations για privilege, host namespaces, capabilities, volumes και seccomp. Χρησιμοποίησε narrow documented exceptions μόνο όπου workload το απαιτεί.

### 4. policy engines

Policy engines αξιολογούν manifests με organization rules. Version policies as code, κάνε allow/deny tests σε CI και monitor exceptions ώστε temporary bypass να μη γίνει permanent.

### 5. image provenance και allowlists

Admission μπορεί να επιβάλλει registry, digest, signatures/attestations και provenance. Για high assurance προτίμησε immutable digest και verified provenance αντί για mutable tag.

### 6. namespace και service-account context

Risk ενός manifest αλλάζει με namespace, service account, secrets, network policy και environment. Policy decision πρέπει να περιλαμβάνει το πραγματικό context authority.

### 7. runtime drift

Admission ελέγχει create/update time, αλλά runtime, nodes, credentials και external services μπορούν να drift. Συνδύασέ το με reconciliation και runtime telemetry.

### 8. telemetry και exceptions

Κατέγραψε policy/version, object, namespace, identity, decision και exception. Exception χρειάζεται owner, reason, scope και expiry.

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

### Lab 1 — Write policy requirements for a toy Kubernetes manifest: non-root, restricted capabilities, approved image source and resource limits.


### Lab 2 — Compare admission-time and runtime evidence for the same fictional workload.


### Lab 3 — Create an exception record with owner, reason, expiry and compensating control, then define an automated review trigger.

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

[English Module 135](../../English/07-Cloud-Containers-and-Supply-Chain/135-Kubernetes-Admission-Control-Policy-as-Code-and-Runtime-Guardrails.md)

## Επόμενα μαθήματα

Σχετικά modules: **024, 041, 075, 093, 097, 113**. Από το κύριο menu επίλεξε **Αναζήτηση μαθημάτων** για να βρεις σχετικά θέματα σε όλο το project.
