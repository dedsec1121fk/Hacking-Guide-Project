# Service Mesh, mTLS, Network Policy και East-West Security

> **Ελληνική έκδοση — Μάθημα 136.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands παραμένουν στα Αγγλικά όπου αυτό αυξάνει την ακρίβεια.

Σύνδεσε service mesh, mTLS, workload identity, NetworkPolicy και authorization ώστε να ξεχωρίζεις encryption, reachability και permission.

> **Όριο εξουσιοδοτημένης χρήσης:** Κάνε πρακτικές δοκιμές μόνο σε συστήματα, κώδικα, λογαριασμούς, captures και lab environments που σου ανήκουν ή για τα οποία έχεις ρητή άδεια. Προτίμησε localhost, synthetic data, disposable VMs/containers και read-only analysis.

## Μαθησιακοί στόχοι

Στο τέλος πρέπει να μπορείς να:

- εξηγήσεις το **east-west versus north-south traffic** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **service mesh data/control planes** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **mTLS identity establishment** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **service authorization policy** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **Kubernetes NetworkPolicy concepts** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **sidecar versus ambient interception** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Όρισε ownership/identity, state transition, trust boundary και το ελάχιστο evidence που χρειάζεται για ασφαλή validation.

## Βαθιές τεχνικές έννοιες

### 1. east-west έναντι north-south traffic

North-south αφορά entry/exit ενώ east-west service-to-service. Workloads μέσα στο ίδιο cluster/private network δεν πρέπει να αποκτούν automatic mutual trust.

### 2. data plane και control plane

Mesh data plane επεξεργάζεται traffic και control plane διανέμει identity, routes, certs και policy. Προστάτευσε control-plane authority γιατί μία αλλαγή επηρεάζει πολλά workloads.

### 3. mTLS workload identity

mTLS αυθεντικοποιεί workloads και κρυπτογραφεί traffic αλλά δεν αποφασίζει authorization. Έλεγξε trust-domain/certificate mapping και service policy ξεχωριστά.

### 4. service authorization policy

Policy πρέπει να δένει source workload identity με destination/action και environment/tenant context. Default deny με explicit grants είναι πιο ελέγξιμο από trust λόγω network location.

### 5. Kubernetes NetworkPolicy

NetworkPolicy περιορίζει network reachability και συμπληρώνει identity-aware mesh policy. Επιβεβαίωσε CNI behavior, selectors, egress/DNS και defaults με safe connectivity tests.

### 6. sidecar έναντι ambient models

Sidecar και ambient τοποθετούν enforcement/telemetry σε διαφορετικό σημείο. Threat model πρέπει να δείχνει ποια process/node component μπορεί να δει ή να επηρεάσει traffic και failure mode.

### 7. certificate rotation και trust bundles

Short-lived workload certs μειώνουν exposure αλλά απαιτούν reliable issuance, clocks, overlap και trust-bundle rollout. Δοκίμασε rotation χωρίς broad trust window ή outage.

### 8. telemetry και failure behavior

Mesh logs πρέπει να συνδέουν source/destination identity, policy, protocol και result. Όρισε αν control-plane/policy failure κάνει fail closed ή degrade και κάνε αυτή τη συμπεριφορά observable.

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

### Lab 1 — Draw a three-service architecture and write both network reachability and identity authorization matrices.


### Lab 2 — Model certificate rotation with overlapping trust bundles and define how stale workloads recover.


### Lab 3 — Compare a direct call, sidecar-proxied call and ambient-mesh call in terms of trust boundaries and telemetry.

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

[English Module 136](../../English/07-Cloud-Containers-and-Supply-Chain/136-Service-Mesh-mTLS-Network-Policy-and-East-West-Security.md)

## Επόμενα μαθήματα

Σχετικά modules: **021, 024, 075, 093, 113, 135**. Από το κύριο menu επίλεξε **Αναζήτηση μαθημάτων** για να βρεις σχετικά θέματα σε όλο το project.
