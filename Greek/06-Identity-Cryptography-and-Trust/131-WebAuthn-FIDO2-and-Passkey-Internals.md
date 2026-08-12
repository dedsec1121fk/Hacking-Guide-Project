# WebAuthn, FIDO2 και Passkey Internals

> **Ελληνική έκδοση — Μάθημα 131.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands παραμένουν στα Αγγλικά όπου αυτό αυξάνει την ακρίβεια.

Κατανόησε WebAuthn/FIDO2/passkeys σε επίπεδο protocol: RP ID, origin binding, challenges, authenticators, user verification, attestation και recovery.

> **Όριο εξουσιοδοτημένης χρήσης:** Κάνε πρακτικές δοκιμές μόνο σε συστήματα, κώδικα, λογαριασμούς, captures και lab environments που σου ανήκουν ή για τα οποία έχεις ρητή άδεια. Προτίμησε localhost, synthetic data, disposable VMs/containers και read-only analysis.

## Μαθησιακοί στόχοι

Στο τέλος πρέπει να μπορείς να:

- εξηγήσεις το **WebAuthn ceremony roles** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **Relying Party ID and origin binding** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **credential creation and assertions** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **authenticator data and counters** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **user presence versus user verification** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,
- εξηγήσεις το **discoverable/syncable credentials** και να εντοπίσεις trust boundary, state transition και evidence που σχετίζονται με αυτό,

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Όρισε ownership/identity, state transition, trust boundary και το ελάχιστο evidence που χρειάζεται για ασφαλή validation.

## Βαθιές τεχνικές έννοιες

### 1. ceremony roles

WebAuthn περιλαμβάνει relying party, browser/client, authenticator και user. Το protocol δένει αυτούς τους actors με origin/RP context και public-key credential χωρίς reusable password secret στον server.

### 2. RP ID και origin binding

RP ID ορίζει domain scope του credential και browser origin δίνει web context. Η σωστή validation εμποδίζει assertion για ένα site να γίνει δεκτό από άσχετο site επειδή απλώς ταιριάζει username.

### 3. creation και assertion

Registration δημιουργεί credential/public key και authentication υπογράφει fresh challenge/context. Challenge πρέπει να είναι unpredictable, single-use, session-bound και να λήγει.

### 4. authenticator data και counters

Authenticator data περιέχει RP binding, flags και state, ενώ μερικοί authenticators έχουν counters. Counter είναι risk signal και όχι universal hard requirement επειδή syncable credentials και authenticators συμπεριφέρονται διαφορετικά.

### 5. user presence έναντι verification

User presence δείχνει αλληλεπίδραση με authenticator, ενώ user verification προσθέτει local PIN/biometric policy. RP πρέπει να ζητά και να επαληθεύει το επίπεδο που απαιτεί το συγκεκριμένο transaction.

### 6. discoverable και syncable credentials

Discoverable credentials επιτρέπουν username-less login και passkeys μπορεί να συγχρονίζονται μεταξύ trusted devices. Threat model πρέπει να περιλαμβάνει recovery, device enrollment, sync provider και notifications.

### 7. attestation και privacy

Attestation δίνει πληροφορία για authenticator provenance αλλά προσθέτει privacy/operational κόστος. Απαίτησέ το μόνο όταν υπάρχει συγκεκριμένη assurance ανάγκη.

### 8. recovery και multi-device lifecycle

Passkeys χρειάζονται credential inventory, new-device onboarding, lost-device response, revocation και recovery. Αδύναμο recovery channel μπορεί να παρακάμψει phishing-resistant authentication.

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

### Lab 1 — Design a WebAuthn registration/authentication sequence diagram with challenge, origin and RP-ID validation points.


### Lab 2 — Compare password+OTP, device-bound WebAuthn and syncable passkeys across phishing resistance, recovery and device loss.


### Lab 3 — Create a recovery threat model for a fictional passkey-only service.

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

[English Module 131](../../English/06-Identity-Cryptography-and-Trust/131-WebAuthn-FIDO2-and-Passkey-Internals.md)

## Επόμενα μαθήματα

Σχετικά modules: **021, 039, 049, 078, 092, 100**. Από το κύριο menu επίλεξε **Αναζήτηση μαθημάτων** για να βρεις σχετικά θέματα σε όλο το project.
