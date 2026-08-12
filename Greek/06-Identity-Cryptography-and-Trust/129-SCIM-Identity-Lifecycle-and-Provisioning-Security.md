# SCIM, Identity Lifecycle και Provisioning Security

> **Ελληνική έκδοση — Μάθημα 129.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands παραμένουν στα Αγγλικά όπου αυτό αυξάνει την ακρίβεια.

Δες το identity lifecycle πέρα από το login: joiner/mover/leaver, SCIM, groups, deprovisioning, authoritative sources, drift και reconciliation.

> **Όριο εξουσιοδοτημένης χρήσης:** Κάνε πρακτικές δοκιμές μόνο σε συστήματα, κώδικα, λογαριασμούς, captures και lab environments που σου ανήκουν ή για τα οποία έχεις ρητή άδεια. Προτίμησε localhost, synthetic data, disposable VMs/containers και read-only analysis.

## Μαθησιακοί στόχοι

Στο τέλος πρέπει να μπορείς να:

- εξηγήσεις το **identity lifecycle states** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **SCIM resources and schemas** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **provisioning clients and service providers** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **group and role synchronization** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **deprovisioning and disable semantics** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **source-of-truth conflicts** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Όρισε ownership/identity, state transition, trust boundary και το ελάχιστο evidence που χρειάζεται για ασφαλή validation.

## Βαθιές τεχνικές έννοιες

### 1. identity lifecycle states

Provisioning είναι state machine: invited, active, suspended, disabled, deleted και restored καταστάσεις έχουν διαφορετική authority. Όρισε ποια source μπορεί να προκαλέσει κάθε transition και τι downstream access πρέπει να αλλάξει.

### 2. SCIM resources και schemas

SCIM μοντελοποιεί users, groups και extensions. Validate identifiers, mutability, uniqueness και tenant scope αντί να γράφεις κάθε incoming field απευθείας σε privileged directory attributes.

### 3. clients και service providers

SCIM client έχει συνήθως ισχυρή lifecycle authority πάνω στο service provider. Χρησιμοποίησε narrow credentials, strong authentication, environment/tenant scoping και audit για create/update/deactivate.

### 4. group και role synchronization

Group membership μπορεί να μεταφράζεται άμεσα σε roles. Έλεγξε nested groups, defaults, name collisions, propagation delays και αν η εξωτερική source είναι πράγματι authoritative για το συγκεκριμένο privilege.

### 5. deprovision και disable

Offboarding δεν τελειώνει με `active=false`. Χρειάζεται αφαίρεση sessions, tokens, group membership, service access και reconciliation των downstream systems που μπορεί να ήταν offline.

### 6. source-of-truth conflicts

HR, directory, IdP, app και manual admin state μπορεί να διαφωνούν. Όρισε precedence και conflict handling ώστε stale source να μην επανενεργοποιεί user ή privilege.

### 7. pagination, filtering και bulk

Pagination, PATCH και bulk operations δημιουργούν partial-success/retry state. Κράτησε operations idempotent όπου γίνεται, authorization ανά object και αρκετό status για ασφαλές reconciliation.

### 8. telemetry και reconciliation

Periodic reconciliation συγκρίνει intended identity state με πραγματικό application state. Βρες orphan/unmanaged accounts, privilege drift, failed provisioning και last-success timestamps αντί να εμπιστεύεσαι ένα API response.

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

### Lab 1 — Build a synthetic HR→IdP→SaaS lifecycle diagram for joiner/mover/leaver events.


### Lab 2 — Design a SCIM-like local JSON dataset and verify that group changes produce expected least-privilege outcomes.


### Lab 3 — Write a deprovisioning checklist that includes active sessions, API tokens, shared resources and audit evidence.

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

[English Module 129](../../English/06-Identity-Cryptography-and-Trust/129-SCIM-Identity-Lifecycle-and-Provisioning-Security.md)

## Επόμενα μαθήματα

Σχετικά modules: **021, 039, 042, 059, 092, 093, 128**. Από το κύριο menu επίλεξε **Αναζήτηση μαθημάτων** για να βρεις σχετικά θέματα σε όλο το project.
