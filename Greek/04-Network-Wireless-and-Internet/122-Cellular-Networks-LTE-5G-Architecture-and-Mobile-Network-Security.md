# Cellular Networks, LTE/5G Architecture και Mobile Network Security

> **Ελληνική έκδοση — Μάθημα 122.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands παραμένουν στα Αγγλικά όπου αυτό αυξάνει την ακρίβεια.

Μελέτησε LTE/5G ως αρχιτεκτονική identity, radio και core-network trust, με έμφαση σε privacy, roaming και baseband isolation.

> **Όριο εξουσιοδοτημένης χρήσης:** Κάνε πρακτικές δοκιμές μόνο σε συστήματα, κώδικα, λογαριασμούς, captures και lab environments που σου ανήκουν ή για τα οποία έχεις ρητή άδεια. Προτίμησε localhost, synthetic data, disposable VMs/containers και read-only analysis.

## Μαθησιακοί στόχοι

Στο τέλος πρέπει να μπορείς να:

- εξηγήσεις το **UE, SIM/eSIM and subscriber identity** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **RAN, core network and control/user planes** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **LTE EPC and 5G Core concepts** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **AKA authentication families** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **temporary identifiers and privacy** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **roaming and inter-operator trust** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Όρισε ownership/identity, state transition, trust boundary και το ελάχιστο evidence που χρειάζεται για ασφαλή validation.

## Βαθιές τεχνικές έννοιες

### 1. UE, SIM/eSIM και subscriber identity

Η cellular identity περιλαμβάνει device, subscription SIM/eSIM, phone number και application identity που έχουν διαφορετικό owner και trust. Μην τα χρησιμοποιείς σαν ισοδύναμα authentication factors.

### 2. RAN, core, control και user planes

Το RAN συνδέει UE με core network και χωρίζει signaling/control από user data. Χαρτογράφησε interfaces που μεταφέρουν subscriber state, routing, authentication context και application traffic.

### 3. LTE EPC και 5G Core

LTE EPC και 5G Core έχουν διαφορετικά service/function boundaries αλλά και τα δύο απαιτούν authenticated state και αυστηρή inter-function policy. Αξιολόγησε exposed service/admin APIs πέρα από το radio encryption.

### 4. AKA families

AKA protocols παράγουν session keys από subscription secrets χωρίς να στέλνουν το long-term secret. Έλεγξε identity binding, freshness, network authentication, key separation και failure handling.

### 5. temporary identifiers και privacy

Temporary identifiers μειώνουν συχνή έκθεση long-lived subscriber identity. Privacy analysis πρέπει ακόμη να καλύπτει paging, timing, mobility metadata, app identifiers και logs που μπορούν να κάνουν correlation.

### 6. roaming και inter-operator trust

Roaming επεκτείνει trust σε άλλους operators και interconnects. Χρειάζονται peer policy, validation, least privilege και monitoring επειδή partner-path compromise μπορεί να επηρεάσει subscribers άλλου domain.

### 7. network slicing και service exposure

5G slicing και service-based APIs χρειάζονται πραγματική policy isolation. Slice label μόνο του δεν είναι boundary· έλεγξε authorization, routing, resource isolation και telemetry.

### 8. baseband isolation και telemetry

Baseband επεξεργάζεται σύνθετα untrusted radio protocols και πρέπει να είναι απομονωμένο από application processor. Firmware updates, crash telemetry και περιορισμένη authority μειώνουν το impact baseband failure.

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

### Lab 1 — Draw a 5G connection-flow diagram from device to application service using public standards diagrams.


### Lab 2 — Threat-model a fictional roaming scenario and list which parties must trust which assertions.


### Lab 3 — Compare Wi-Fi and cellular identity/privacy assumptions without capturing any third-party radio traffic.

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

[English Module 122](../../English/04-Network-Wireless-and-Internet/122-Cellular-Networks-LTE-5G-Architecture-and-Mobile-Network-Security.md)

## Επόμενα μαθήματα

Σχετικά modules: **016, 017, 051, 055, 056, 123**. Από το κύριο menu επίλεξε **Αναζήτηση μαθημάτων** για να βρεις σχετικά θέματα σε όλο το project.
