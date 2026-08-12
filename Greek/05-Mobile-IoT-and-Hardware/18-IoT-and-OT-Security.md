# Ασφάλεια IoT και OT

Τα Internet of Things (IoT) και Operational Technology (OT) περιβάλλοντα συνδυάζουν software, embedded hardware, radios, φυσικές διεργασίες, cloud services, mobile εφαρμογές, update pipelines και συσκευές με πολύ μεγάλο lifecycle. Η αξιολόγηση ασφάλειας πρέπει να εξετάζει τόσο το ψηφιακό compromise όσο και τις πιθανές επιπτώσεις στον φυσικό κόσμο.

> **Όριο εξουσιοδότησης:** Έλεγχε μόνο συσκευές, δίκτυα, firmware, cloud accounts και φυσικές διεργασίες που σου ανήκουν ή είναι ρητά εντός scope. Απόφυγε disruptive radio/control/safety tests σε shared ή production περιβάλλοντα. Προτίμησε emulator, development board, captured data και απομονωμένο lab.

## Μαθησιακοί στόχοι

- Να αναγνωρίζεις IoT/OT trust boundaries.
- Να χαρτογραφείς device, gateway, cloud, app και update σχέσεις.
- Να αξιολογείς identity, secrets, management interfaces και update trust.
- Να κατανοείς γιατί safety και availability αλλάζουν το testing model.
- Να επιλέγεις κατάλληλο evidence για embedded/operational περιβάλλοντα.

## Αρχιτεκτονική IoT

Ένα IoT προϊόν μπορεί να περιλαμβάνει sensor/actuator, microcontroller ή embedded Linux, local radio, gateway, vendor cloud API, mobile app και signing/update infrastructure. Αντιμετώπισε τα σαν διαφορετικά trust zones. Ένα app bug μπορεί να εκθέσει device credentials, ένα cloud authorization bug να επηρεάσει ολόκληρο fleet και ένα compromised update key να περάσει πολλά τοπικά boundaries.

## Device identity και provisioning

Έλεγξε πώς αποκτά η συσκευή την πρώτη της identity, αν τα credentials είναι μοναδικά ανά unit, πού αποθηκεύονται keys, πώς γίνεται ownership transfer και πώς γίνεται decommission. Shared factory passwords ή undocumented recovery accounts δημιουργούν fleet-wide risk. Το provisioning πρέπει να δένει τη συσκευή με τον σωστό owner/tenant και να αφήνει audit trail.

## Management interfaces και local services

Κατέγραψε listening services, debug interfaces, serial/JTAG access, web administration, Bluetooth/Wi-Fi pairing, discovery protocols και maintenance ports. Interface που χρειάζεται μόνο στην παραγωγή/επισκευή δεν πρέπει να παραμένει broadly exposed. Management paths χρειάζονται authentication, authorization, resource controls και ασφαλές recovery.

## Firmware και secure updates

Για το update system απάντησε: ποιος επιτρέπεται να δημοσιεύσει artifact, πώς επαληθεύεται η αυθεντικότητα, πώς ελέγχεται downgrade/rollback και τι γίνεται μετά από failed update. Η digital signature είναι μόνο ένα μέρος του trust· verification keys, version policy, boot chain και recovery πρέπει επίσης να είναι αξιόπιστα.

## Secrets και storage

Εξέτασε hard-coded secrets, API tokens, Wi-Fi credentials, certificates, debug logs, crash dumps και backup/export files. Προτίμησε per-device secrets, hardware-backed storage όπου υποστηρίζεται, rotation και ελάχιστα permissions στο cloud/API layer.

## Cloud APIs και authorization

IoT APIs συχνά χειρίζονται identifiers για devices, homes, fleets ή tenants. Κάθε operation πρέπει να κάνει server-side authorization του caller απέναντι στο συγκεκριμένο object/action. Έγκυρο token δεν σημαίνει ότι ο caller κατέχει οποιοδήποτε device ID έστειλε.

## OT και cyber-physical systems

OT περιλαμβάνει industrial control, building automation, energy, manufacturing και άλλα συστήματα όπου integrity/availability επηρεάζουν φυσικές διεργασίες. Safety interlocks, deterministic operation, change management, vendor support, legacy protocols και recovery μπορεί να έχουν μεγαλύτερη προτεραιότητα από aggressive probing.

Passive discovery και configuration review είναι συνήθως ασφαλέστερη αρχή. Κάθε state-changing test χρειάζεται operator-approved rollback και safety plan.

## Segmentation και gateways

Χώρισε device networks από user workstations και management planes. Τα gateways πρέπει να επιτρέπουν μόνο τα πραγματικά αναγκαία protocols/destinations. Κατέγραψε required east-west και north-south flows αντί να δίνεις broad connectivity επειδή μια συσκευή είναι δύσκολη στη διαχείριση.

## Logging και fleet visibility

Χρήσιμο evidence: firmware version, secure boot/update state, device identity, provisioning, failed authentication, config changes, cloud API decisions, gateway connections και recovery actions. Απόφυγε secrets στα logs και φρόντισε time correlation μεταξύ device, gateway και cloud.

## Συνηθισμένα λάθη

- Εμπιστοσύνη σε κάθε device του local network.
- Shared default/fleet-wide credentials.
- Updates χωρίς authenticated provenance ή rollback policy.
- Debug interfaces ενεργά χωρίς ownership controls.
- Cloud authorization μόνο με client-supplied object IDs.
- OT testing σαν να είναι disposable web lab.
- Απουσία ασφαλούς recovery όταν μια συσκευή αποτύχει.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε development board, emulator ή spare IoT device που σου ανήκει. Σχεδίασε device→gateway/cloud/app data flow, κατέγραψε local services, firmware/update state και πού φυλάσσονται credentials. Άλλαξε μία ακίνδυνη ρύθμιση και επιβεβαίωσε ποια local/cloud logs καταγράφουν την αλλαγή. Επανέφερε το αρχικό state.

## Έλεγχος γνώσεων

1. Γιατί per-device identity είναι καλύτερη από fleet-wide password;
2. Τι πρέπει να είναι αξιόπιστο πέρα από την update signature;
3. Γιατί OT testing έχει αυστηρότερα όρια;
4. Ποιο authorization check χρειάζεται multi-tenant IoT API;
5. Ποιο evidence συνδέει device event με cloud decision;

## Καθοδηγούμενη μελέτη

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Εξέτασε ολόκληρο lifecycle: manufacture, provisioning, normal operation, update, ownership transfer, incident recovery και decommissioning.

### Συνέχισε με

Προτεινόμενα modules: **41, 48, 54, 56, 83, 103, 122, 123**. Από το menu χρησιμοποίησε **Αναζήτηση μαθημάτων** για embedded, hardware και radio θέματα.
