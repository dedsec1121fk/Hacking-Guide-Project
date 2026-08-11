# PAM, Just-in-Time Access, JEA και Privileged Access Engineering

> **Ελληνική έκδοση — Μάθημα 130.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands παραμένουν στα Αγγλικά όπου αυτό αυξάνει την ακρίβεια.

Η privileged πρόσβαση πρέπει να είναι σύντομη, ελεγχόμενη και attributable. Μελέτησε PAM, JIT/JEA, session controls και break-glass design.

> **Όριο εξουσιοδοτημένης χρήσης:** Κάνε πρακτικές δοκιμές μόνο σε συστήματα, κώδικα, λογαριασμούς, captures και lab environments που σου ανήκουν ή για τα οποία έχεις ρητή άδεια. Προτίμησε localhost, synthetic data, disposable VMs/containers και read-only analysis.

## Μαθησιακοί στόχοι

Στο τέλος πρέπει να μπορείς να:

- εξηγήσεις το **privileged identity separation** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **vaulting versus ephemeral credentials** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **just-in-time and just-enough access** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **approval and policy workflows** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **session recording and command context** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **break-glass accounts** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Όρισε ownership/identity, state transition, trust boundary και το ελάχιστο evidence που χρειάζεται για ασφαλή validation.

## Βαθιές τεχνικές έννοιες

### 1. privileged identity separation

Administrative work πρέπει να γίνεται με ξεχωριστή identity από email/browsing/development. Αυτό μειώνει credential exposure και κάνει privileged actions πιο εύκολα σε attribution, restriction και monitoring.

### 2. vaulting έναντι ephemeral access

Vaulting προστατεύει long-lived secrets αλλά δεν αφαιρεί lifecycle risk. Short-lived/ephemeral credentials μειώνουν standing privilege όταν το target platform και το recovery model το επιτρέπουν.

### 3. JIT και JEA

Just-In-Time περιορίζει διάρκεια elevation και Just Enough Administration περιορίζει operations. Ο συνδυασμός μειώνει τόσο το χρονικό παράθυρο όσο και το blast radius του privilege.

### 4. approval και policy workflows

Elevation approval πρέπει να δένεται με identity, target, role, reason και duration. Ticket ή approval που μπορεί να επαναχρησιμοποιηθεί για άλλο resource δεν είναι ισχυρό authorization context.

### 5. session recording και command context

Privileged-session recording βοηθά accountability αλλά μπορεί να καταγράψει secrets. Κράτησε actor, target, action και time context με κατάλληλο redaction, retention και access control.

### 6. break-glass access

Emergency account πρέπει να λειτουργεί όταν το normal identity plane αποτύχει, άρα να μη βασίζεται στο ίδιο dependency. Προστάτεψέ το offline/strongly, monitor κάθε χρήση και rotate/reseal μετά από activation.

### 7. de-escalation και expiry

Privilege πρέπει να λήγει αυτόματα και να αφαιρεί derived sessions/tokens όπου γίνεται. Επαλήθευσε effective permissions μετά το expiry και όχι μόνο ότι αφαιρέθηκε ένα group membership.

### 8. service και administrator boundaries

Human admins και workload identities χρειάζονται διαφορετικό lifecycle. Απόφυγε shared accounts, interactive χρήση service credentials και service principals με broad tenant-wide permissions.

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

### Lab 1 — Create a fictional admin-task catalog and assign minimum roles, duration and approval conditions.


### Lab 2 — Model a JIT elevation lifecycle from request through expiry and verify what evidence remains afterward.


### Lab 3 — Design a break-glass test plan that proves availability without exposing real emergency credentials.

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

[English Module 130](../../English/06-Identity-Cryptography-and-Trust/130-PAM-Just-in-Time-Access-JEA-and-Privileged-Access-Engineering.md)

## Επόμενα μαθήματα

Σχετικά modules: **021, 032, 042, 049, 059, 072, 093**. Από το κύριο menu επίλεξε **Αναζήτηση μαθημάτων** για να βρεις σχετικά θέματα σε όλο το project.
