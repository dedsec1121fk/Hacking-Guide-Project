# Οδηγός Εξουσιοδοτημένων Labs

Χρησιμοποίησε αυτόν τον οδηγό για να μετατρέπεις τη θεωρία σε ασφαλή και επαναλήψιμη πρακτική.

## Το lab contract

Πριν αγγίξεις το σύστημα γράψε: owner, scope, επιτρεπόμενες ενέργειες, απαγορευμένες ενέργειες, χρονικό παράθυρο, είδος δεδομένων, τρόπο rollback και stop conditions. Ακόμη και στο προσωπικό σου lab αυτή η συνήθεια σε μαθαίνει επαγγελματική διαδικασία.

## Προτιμώμενη σειρά

1. Read-only observation.
2. Configuration review.
3. Harmless functional test.
4. State-changing test μόνο αν χρειάζεται.
5. Restore/rollback.
6. Retest του αμυντικού control.

## Κατάλληλα περιβάλλοντα

Localhost services, disposable VMs, containers χωρίς sensitive mounts, Android emulators, intentionally vulnerable training apps, sample binaries, synthetic logs και test identity providers.

## Evidence

Κράτησε timestamps, versions, sanitized configuration, packet/trace metadata, hashes και before/after αποτελέσματα. Μην συλλέγεις πραγματικά passwords, tokens, private keys ή άσχετα προσωπικά δεδομένα.

## Πότε σταματάς

Σταμάτησε αμέσως αν το test βγει εκτός scope, προκαλέσει απρόβλεπτο availability impact, αγγίξει πραγματικά δεδομένα χρηστών, δημιουργήσει persistence που δεν σχεδίασες ή παράγει συμπεριφορά που δεν ξέρεις να αναστρέψεις με ασφάλεια.

## Reporting

Ξεχώρισε observation από inference. Ένα σωστό finding περιγράφει condition, evidence, impact, root cause, affected scope, remediation και retest. Δήλωσε καθαρά κάθε αβεβαιότητα.
