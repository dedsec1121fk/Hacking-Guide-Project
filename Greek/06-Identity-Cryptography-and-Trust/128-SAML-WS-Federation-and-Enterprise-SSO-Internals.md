# SAML, WS-Federation και Enterprise SSO Internals

> **Ελληνική έκδοση — Μάθημα 128.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands παραμένουν στα Αγγλικά όπου αυτό αυξάνει την ακρίβεια.

Κατανόησε SAML/enterprise SSO με assertions, metadata, signatures, audience, recipient, RelayState, attributes και session lifecycle.

> **Όριο εξουσιοδοτημένης χρήσης:** Κάνε πρακτικές δοκιμές μόνο σε συστήματα, κώδικα, λογαριασμούς, captures και lab environments που σου ανήκουν ή για τα οποία έχεις ρητή άδεια. Προτίμησε localhost, synthetic data, disposable VMs/containers και read-only analysis.

## Μαθησιακοί στόχοι

Στο τέλος πρέπει να μπορείς να:

- εξηγήσεις το **IdP and SP trust roles** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **SAML assertions and conditions** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **browser SSO profiles and bindings** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **metadata and signing keys** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **audience and recipient validation** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **NameID and attribute mapping** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Όρισε ownership/identity, state transition, trust boundary και το ελάχιστο evidence που χρειάζεται για ασφαλή validation.

## Βαθιές τεχνικές έννοιες

### 1. IdP και SP trust

Στο SAML ο Identity Provider εκδίδει assertions και ο Service Provider τα καταναλώνει. Ο SP πρέπει να εμπιστεύεται μόνο configured issuers/keys και να εφαρμόζει δικό του authorization· valid assertion από λάθος tenant/relationship δεν αρκεί.

### 2. assertions και conditions

Assertion περιέχει subject, authentication context, attributes και conditions. Κάνε validation σε issuer, signature, audience, recipient/destination, χρόνο, subject confirmation και expected flow αντί να ελέγχεις μόνο τη signature.

### 3. browser SSO profiles και bindings

Browser SSO μεταφέρει SAML messages μέσω browser με συγκεκριμένα bindings. Παρακολούθησε ποιο state ανήκει στο request, τι μπορεί να επηρεάσει ο browser και πώς ο SP συσχετίζει response με το αρχικό session.

### 4. metadata και signing keys

SAML metadata διανέμει entity IDs, endpoints, certificates και capabilities. Metadata/key rollover είναι high-impact config change και χρειάζεται authenticated distribution, overlap window, audit και tested rollback.

### 5. audience και recipient validation

Audience και recipient/destination εμποδίζουν assertion για ένα service να χρησιμοποιηθεί σε άλλο. Η σύγκριση πρέπει να γίνεται με canonical local configuration, όχι με values που προέρχονται από το incoming request.

### 6. NameID και attribute mapping

Attributes γίνονται local identity/roles μέσω mapping rules. Μην χρησιμοποιείς mutable display name ή email σαν μοναδικό privileged identifier χωρίς explicit collision, case, domain και missing-value policy.

### 7. RelayState και request correlation

RelayState μεταφέρει navigation/application context και δεν πρέπει να γίνεται unvalidated redirect ή authorization source. Κράτησε application state χωριστά από identity proof και συσχέτισε response με το σωστό authentication request.

### 8. logout και session lifetime

SAML logout και local app sessions έχουν διαφορετικό lifecycle. Όρισε ποια local tokens ανακαλούνται, τι γίνεται αν Single Logout αποτύχει και πώς admin τερματίζει sessions σε incident.

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

### Lab 1 — Draw an SP-initiated SSO flow and annotate every signed/unsigned value plus who validates it.


### Lab 2 — Create a fictional assertion-validation checklist and test it against synthetic good/bad assertion descriptions, not real accounts.


### Lab 3 — Model key rollover where old and new IdP signing keys overlap and define safe acceptance windows.

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

[English Module 128](../../English/06-Identity-Cryptography-and-Trust/128-SAML-WS-Federation-and-Enterprise-SSO-Internals.md)

## Επόμενα μαθήματα

Σχετικά modules: **021, 032, 039, 072, 092, 093**. Από το κύριο menu επίλεξε **Αναζήτηση μαθημάτων** για να βρεις σχετικά θέματα σε όλο το project.
