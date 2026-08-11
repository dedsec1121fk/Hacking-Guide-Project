# Βάσεις Κυβερνοασφάλειας και Μεθοδολογία Ethical Hacking

Η κυβερνοασφάλεια είναι η προστασία συστημάτων, identities, λογισμικού, δικτύων και δεδομένων, χωρίς να εμποδίζεται η νόμιμη λειτουργία τους. Το ethical hacking είναι ένα μέρος αυτής της διαδικασίας: μια **εξουσιοδοτημένη** προσπάθεια να ελεγχθούν security assumptions και να παραχθούν αποδεικτικά στοιχεία που βοηθούν τον ιδιοκτήτη να μειώσει το risk.

> **Όριο εξουσιοδοτημένης χρήσης:** Κάνε πρακτικές δοκιμές μόνο σε συστήματα, accounts, εφαρμογές, δίκτυα ή συσκευές που σου ανήκουν ή για τα οποία έχεις ρητή άδεια. Για εκμάθηση προτίμησε localhost, disposable VMs/containers, emulators, synthetic accounts και intentionally vulnerable training apps.

## Μαθησιακοί στόχοι

Στο τέλος του μαθήματος πρέπει να μπορείς να:

- ξεχωρίζεις asset, threat, vulnerability, exposure, control και risk,
- εξηγείς confidentiality, integrity, availability, authenticity, accountability και resilience,
- ξεχωρίζεις authentication από authorization,
- περιγράφεις έναν σύγχρονο κύκλο security assessment,
- ορίζεις scope και απαιτούμενο evidence πριν από οποιοδήποτε test,
- εξηγείς γιατί remediation και retest είναι βασικά μέρη του ethical hacking.

## Βασικές ιδιότητες ασφάλειας

### Confidentiality — Εμπιστευτικότητα

Η confidentiality περιορίζει την πληροφορία μόνο σε εξουσιοδοτημένα subjects. Η κρυπτογράφηση μπορεί να προστατεύσει δεδομένα σε transit ή at rest, όμως η πραγματική εμπιστευτικότητα εξαρτάται επίσης από authorization, secret handling, logs, backups, exports και operational procedures.

### Integrity — Ακεραιότητα

Integrity σημαίνει ότι δεδομένα και system state παραμένουν σωστά και ότι μη εξουσιοδοτημένες αλλαγές αποτρέπονται ή ανιχνεύονται. Hashes, digital signatures, access control, transaction validation, version control, immutable logging και change management μπορούν να συμβάλουν στην ακεραιότητα.

### Availability — Διαθεσιμότητα

Availability σημαίνει ότι ο εξουσιοδοτημένος χρήστης μπορεί να χρησιμοποιήσει την υπηρεσία όταν τη χρειάζεται. Capacity, redundancy, backups, dependencies, rate limits, monitoring και recovery procedures επηρεάζουν άμεσα τη διαθεσιμότητα.

### Authenticity και accountability

Authenticity είναι η βεβαιότητα ότι identity, artifact ή message είναι αυτό που δηλώνει. Accountability σημαίνει ότι οι ενέργειες μπορούν να συνδεθούν με τον σωστό actor και να διερευνηθούν αργότερα. Ισχυρό authentication χωρίς σωστό authorization και audit evidence δεν αρκεί.

### Resilience — Ανθεκτικότητα

Ένα ασφαλές σύστημα δεν πρέπει να βασίζεται στην υπόθεση ότι η πρόληψη θα πετυχαίνει πάντα. Resilience σημαίνει detection, containment, recovery, restoration και lessons learned μετά από failure ή incident.

## Βασικό λεξιλόγιο

- **Asset:** κάτι που έχει αξία και πρέπει να προστατευτεί.
- **Threat:** κατάσταση ή actor που μπορεί να προκαλέσει ζημιά.
- **Vulnerability:** αδυναμία που μπορεί να παραβιάσει security property.
- **Exposure:** συνθήκη που κάνει μια αδυναμία reachable ή σημαντική.
- **Exploit:** τρόπος αξιοποίησης μιας vulnerability. Στο project χρησιμοποιείται μόνο σε ελεγχόμενα labs και για defensive understanding.
- **Control:** safeguard που προλαμβάνει, ανιχνεύει, περιορίζει ή βοηθά το recovery.
- **Risk:** συνδυασμός likelihood, impact, exposure, business context και uncertainty.
- **Attack surface:** interfaces, identities, inputs, services, dependencies και trust boundaries που μπορεί να γίνουν αντικείμενο abuse.
- **Trust boundary:** σημείο όπου data, identity, authority ή execution περνά μεταξύ components με διαφορετικές assumptions εμπιστοσύνης.

## Authentication και authorization

Authentication απαντά «ποιος παρουσιάζει αυτό το credential;». Authorization απαντά «επιτρέπεται αυτή η identity να κάνει αυτή την ενέργεια πάνω σε αυτό το resource;». Ένα σύστημα μπορεί να κάνει σωστά authentication και να είναι ευάλωτο επειδή λείπει object-level authorization ή επειδή χρησιμοποιείται stale state.

## Threat actors και κίνητρα

Η σωστή ανάλυση εστιάζει σε capabilities και goals αντί για στερεότυπα. Actors μπορεί να είναι οικονομικά υποκινούμενες ομάδες, insiders, state-linked groups, opportunistic attackers, hacktivists, fraud groups ή automated abuse. Ρώτησε τι access έχουν αρχικά, ποιος είναι ο στόχος τους, τι περιορισμούς έχουν και τι evidence θα άφηναν.

## Βασικά vulnerability management

Τα CVE δίνουν κοινά identifiers για δημοσιευμένες vulnerabilities. Vendor advisories και vulnerability databases προσθέτουν affected versions, fixes και context. Το CVSS είναι standardized severity framework αλλά **δεν είναι μόνο του risk decision**. Exposure, asset importance, compensating controls και business impact αλλάζουν την πραγματική προτεραιότητα.

Χρήσιμο workflow:

1. ταυτοποίησε asset και ακριβή version,
2. επιβεβαίωσε applicability,
3. έλεγξε exposure και required privileges,
4. κράτησε evidence με ελάχιστο impact,
5. κάνε prioritization με technical + business context,
6. εφάρμοσε remediation/mitigation,
7. κάνε retest και κατέγραψε το αποτέλεσμα.

## Σύγχρονος κύκλος ethical assessment

### 1. Authorization και scope

Κατέγραψε owner, systems, accounts, time window, allowed techniques, prohibited actions, data-handling rules, contacts και stop conditions. Το ότι κάτι είναι public στο Internet **δεν σημαίνει authorization**.

### 2. Discovery και modeling

Δημιούργησε inventory από assets, identities, interfaces, dependencies και trust boundaries. Ξεκίνα με passive/read-only evidence όπου γίνεται.

### 3. Validation

Έλεγξε security assumptions με τη λιγότερο παρεμβατική μέθοδο που απαντά την ερώτηση. Προτίμησε proof που αποδεικνύει τη weakness χωρίς περιττό impact.

### 4. Evidence και analysis

Κράτησε timestamps, versions, configuration, requests/responses, logs και το ακριβές condition που προκάλεσε το αποτέλεσμα. Ξεχώριζε observation από inference.

### 5. Remediation και retest

Εξήγησε root cause, control, residual risk και repeatable regression test. Ένα finding δεν ολοκληρώνεται μέχρι να μπορεί ο owner να αποδείξει ότι το fix άλλαξε το αποτέλεσμα.

### 6. Cleanup και reporting

Αφαίρεσε test accounts, temporary files και αλλαγές που δημιούργησε το assessment. **Μην διαγράφεις ή αλλοιώνεις security logs για να κρύψεις δραστηριότητα.**

## Καθοδηγούμενο εργαστήριο

Φτιάξε ένα μονοσέλιδο threat model για μια local εφαρμογή ή συσκευή που σου ανήκει. Σχεδίασε user, application, data store, network boundary και μία external dependency. Σημείωσε πού γίνεται authentication, πού authorization, ποια data είναι sensitive και ποια logs θα βοηθούσαν σε incident.

**Evidence:** διάγραμμα, τρεις security assumptions, τρία failure modes και ένα defensive test για κάθε failure mode.

## Συχνά λάθη

- Ξεκίνημα από tools πριν οριστεί security question.
- Θεώρηση scanner finding ως απόδειξη χωρίς verification.
- Σύγχυση severity με business risk.
- Σύγχυση encryption με authorization.
- Test εκτός scope επειδή το target είναι reachable.
- Αποθήκευση secrets/tokens σε lab notes.
- Θεώρηση του cleanup ως άδεια διαγραφής evidence.

## Έλεγχος γνώσεων

1. Δώσε παράδειγμα όπου authentication πετυχαίνει αλλά authorization αποτυγχάνει.
2. Ποια είναι η διαφορά vulnerability και risk;
3. Ποια τρία στοιχεία πρέπει να υπάρχουν στο scope;
4. Γιατί το retest είναι μέρος του assessment;
5. Τι evidence θα κρατούσες πριν αλλάξεις ένα security control;

## Καθοδηγούμενη μελέτη

Χρησιμοποίησε τη κοινή [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Ολοκλήρωσε το safe lab και βεβαιώσου ότι μπορείς να εξηγήσεις τον assessment lifecycle χωρίς να βασίζεσαι σε tool names.

### Συνέχεια

Προτεινόμενα επόμενα μαθήματα: **02, 05, 28, 51**.
