# Firewalls, IDS/IPS, Honeypots και Επαλήθευση Ανίχνευσης

Τα firewalls, IDS/IPS και honeypots εξυπηρετούν διαφορετικούς σκοπούς. Το firewall επιβάλλει επιτρεπόμενες ροές, το IDS/IPS αναλύει activity και μπορεί να ειδοποιεί ή να μπλοκάρει, ενώ ένα honeypot προσφέρει ελεγχόμενο περιβάλλον παρατήρησης. Η σωστή δοκιμή μετρά αν οι έλεγχοι λειτουργούν όπως σχεδιάστηκαν· δεν προσπαθεί να «κρυφτεί» από αυτούς.

> **Όριο εξουσιοδότησης:** Η validation πρέπει να γίνεται σε δική σου ή ρητά εξουσιοδοτημένη υποδομή, με γνωστά test indicators και χωρίς τεχνικές που στοχεύουν στην παράκαμψη πραγματικών αμυνών τρίτων.

## Μαθησιακοί στόχοι

- Να ξεχωρίζεις preventive από detective controls.
- Να αξιολογείς firewall policy, segmentation και default-deny λογική.
- Να κατανοείς signatures, behavior analytics και telemetry dependencies.
- Να σχεδιάζεις benign detection tests.
- Να χρησιμοποιείς honeypots με σωστή απομόνωση και διαχείριση δεδομένων.

## Firewalls και policy

Η πιο χρήσιμη ερώτηση είναι «ποια ροή πρέπει να επιτρέπεται και γιατί;». Κατέγραψε source, destination, protocol, port/service, identity/context και owner. Αφαίρεσε stale rules και απόφυγε υπερβολικά ευρείες εξαιρέσεις. Η segmentation πρέπει να δοκιμάζεται ως security invariant, όχι μόνο ως configuration screenshot.

## IDS και IPS

Signature-based detection αναζητά γνωστά patterns, ενώ behavior/analytics μπορούν να εντοπίσουν αποκλίσεις. Και τα δύο εξαρτώνται από σωστή telemetry, timestamps, parsing και context. Ένα IPS έχει επιπλέον κίνδυνο false-positive blocking, επομένως χρειάζεται controlled rollout και παρακολούθηση.

## Detection engineering

Για κάθε detection όρισε:

1. συμπεριφορά που θέλεις να εντοπίσεις,
2. απαιτούμενη πηγή δεδομένων,
3. benign τρόπο αναπαραγωγής,
4. αναμενόμενο event/alert,
5. triage context,
6. false positives/false negatives,
7. ownership και retest cadence.

Η αποτυχία ενός alert μπορεί να οφείλεται σε sensor gap, parser, normalization, rule logic ή routing του alert—not μόνο στη rule.

## Honeypots

Ένα honeypot πρέπει να είναι απομονωμένο, εύκολα επαναφερόμενο και να μην περιέχει πραγματικά secrets. Κατέγραψε τι telemetry συλλέγει, πόσο διατηρείται και ποιος έχει πρόσβαση. Μην το χρησιμοποιείς ως ανεξέλεγκτο pivot προς άλλα συστήματα.

## Safe validation

Προτίμησε benign markers, synthetic log events, harmless connection attempts σε test service ή επίσημα detection test datasets. Ο στόχος είναι να επαληθεύσεις end-to-end ότι **activity → sensor → parser → rule → alert → analyst** λειτουργεί.

## Συνηθισμένα λάθη

- Άπειρα allow rules χωρίς owner/expiry.
- Υπόθεση ότι «το IDS είναι εγκατεστημένο» σημαίνει ότι βλέπει τα σωστά δεδομένα.
- Αλλαγή detection χωρίς regression test.
- Honeypot με πραγματικά credentials ή ανεπαρκή isolation.
- Tests που προσπαθούν να αποφύγουν την ανίχνευση αντί να την επικυρώσουν.

## Καθοδηγούμενο εργαστήριο

Σε localhost ή απομονωμένο lab, δημιούργησε έναν επιτρεπόμενο και έναν απαγορευμένο network path. Επιβεβαίωσε το αποτέλεσμα με logs. Έπειτα δημιούργησε ένα benign test event και ακολούθησέ το από την πηγή μέχρι το alert. Κατέγραψε κάθε σημείο όπου θα μπορούσε να χαθεί.

## Έλεγχος γνώσεων

1. Ποια η διαφορά preventive και detective control;
2. Γιατί κάθε firewall exception χρειάζεται owner και λόγο;
3. Ποια στάδια υπάρχουν από event μέχρι analyst alert;
4. Γιατί ένα honeypot χρειάζεται ισχυρή isolation;
5. Τι σημαίνει detection regression test;

## Καθοδηγούμενη μελέτη

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Για κάθε test γράψε πρώτα το αναμενόμενο telemetry και μετά εκτέλεσε το benign stimulus.

### Συνέχισε με

Προτεινόμενα επόμενα modules: **23, 26, 47, 80, 107, 108**.
