# Radio, SDR και RF Security Fundamentals

> **Ελληνική έκδοση — Μάθημα 123.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands παραμένουν στα Αγγλικά όπου αυτό αυξάνει την ακρίβεια.

Απόκτησε βασική RF/SDR γνώση με receive-only ή synthetic data: sampling, I/Q, modulation, frames, checksums, authentication και replay resistance.

> **Όριο εξουσιοδοτημένης χρήσης:** Κάνε πρακτικές δοκιμές μόνο σε συστήματα, κώδικα, λογαριασμούς, captures και lab environments που σου ανήκουν ή για τα οποία έχεις ρητή άδεια. Προτίμησε localhost, synthetic data, disposable VMs/containers και read-only analysis.

## Μαθησιακοί στόχοι

Στο τέλος πρέπει να μπορείς να:

- εξηγήσεις το **frequency, bandwidth and sampling** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **I/Q representation** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **modulation and symbol timing** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **preambles, frames and checksums** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **noise, interference and SNR** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **receive-only spectrum analysis** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Όρισε ownership/identity, state transition, trust boundary και το ελάχιστο evidence που χρειάζεται για ασφαλή validation.

## Βαθιές τεχνικές έννοιες

### 1. frequency, bandwidth και sampling

RF analysis ξεκινά από frequency, bandwidth, sample rate και receiver limitations. Κατέγραψε antenna, gain, filters, clock και environment πριν βγάλεις protocol/security συμπέρασμα.

### 2. I/Q representation

SDR χρησιμοποιεί I/Q samples για amplitude και phase πληροφορία. Raw I/Q δεν αποδεικνύει protocol ή sender χωρίς synchronization, framing και επιπλέον context.

### 3. modulation και symbol timing

Modulation μεταφέρει bits μέσω amplitude/phase/frequency αλλαγών και απαιτεί σωστό symbol/carrier timing. Μέτρησε parameters και channel conditions αντί να υποθέτεις defaults.

### 4. preambles, frames και checksums

Preambles και headers οριοθετούν frames, ενώ checksums εντοπίζουν τυχαίο corruption. Checksum δεν είναι authentication εκτός αν υπάρχει ξεχωριστός cryptographic mechanism.

### 5. noise, interference και SNR

Noise/interference μπορεί να μοιάζει με protocol failure ή attack. Μέτρησε SNR, channel occupancy και receiver saturation πριν αποδώσεις missing frames σε κακόβουλη ενέργεια.

### 6. receive-only spectrum analysis

Receive-only είναι ασφαλέστερη προεπιλογή για RF learning. Χρησιμοποίησε owned devices ή δημόσια/licensed test signals και μην αποκωδικοποιείς ιδιωτικές επικοινωνίες χωρίς άδεια.

### 7. authentication versus signal presence

Η παρουσία signal ή valid-looking frame δεν αποδεικνύει identity. Authentication χρειάζεται cryptographic/trusted context· proximity και signal strength δεν είναι ισχυρά credentials.

### 8. replay resistance και rolling state

Protocols που επιτρέπουν φυσική ενέργεια χρειάζονται freshness με nonce, counter ή challenge-response. Δοκίμασε μόνο σε synthetic/owned devices και αξιολόγησε synchronization και recovery state.

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

### Lab 1 — Use a prerecorded or synthetic IQ dataset and identify signal bandwidth, bursts and framing without transmitting.


### Lab 2 — Create a toy digital-radio frame format and add sequence numbers plus a MAC in software to demonstrate freshness/integrity.


### Lab 3 — Document how a rolling-code design differs from a static replayable identifier.

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

[English Module 123](../../English/04-Network-Wireless-and-Internet/123-Radio-SDR-and-RF-Security-Fundamentals.md)

## Επόμενα μαθήματα

Σχετικά modules: **016, 051, 055, 077, 083, 122**. Από το κύριο menu επίλεξε **Αναζήτηση μαθημάτων** για να βρεις σχετικά θέματα σε όλο το project.
