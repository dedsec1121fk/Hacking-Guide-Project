# Ασφάλεια DNS, Routing, BGP και Υποδομής Internet

> **Ελληνική έκδοση — Μάθημα 087.** Διατηρούνται οι διεθνείς τεχνικοί όροι όπου είναι ακριβέστεροι και ευκολότεροι στην αναζήτηση.

## Στόχος του μαθήματος

Να κατανοήσεις σε βάθος το **Ασφάλεια DNS, Routing, BGP και Υποδομής Internet**, να αναγνωρίζεις trust boundaries και failure states και να μπορείς να αποδείξεις ένα συμπέρασμα με ασφαλές, επαναλήψιμο evidence.

> **Όριο εξουσιοδότησης:** Πρακτική μόνο σε συστήματα, λογαριασμούς, κώδικα ή labs που σου ανήκουν ή έχεις ρητή άδεια να ελέγξεις. Προτίμησε localhost, synthetic data και disposable environments.

## Βαθιές τεχνικές έννοιες

### 1. DNS resolution chain

Ένα DNS answer μπορεί να περάσει stub resolver, recursive resolver, authoritative servers και caches. Χαρτογράφησε ποιο component είναι authoritative για κάθε βήμα και πού αλλάζει trust.

### 2. DNSSEC

DNSSEC δίνει authenticity/integrity σε DNS RRsets μέσω chain of trust. Δεν παρέχει confidentiality ούτε authorization για την εφαρμογή που βρίσκεται στη διεύθυνση.

### 3. Registrar and zone control

Registrar account, registry lock, DNS hosting και zone signing είναι control-plane assets υψηλής αξίας. MFA, role separation, change alerts και recovery διαδικασία είναι κρίσιμα.

### 4. Anycast and recursive services

Anycast βελτιώνει reachability/resilience αλλά ένα logical resolver μπορεί να έχει πολλά sites και failure domains. Monitoring πρέπει να ξεχωρίζει regional routing issue από resolver/application issue.

### 5. BGP path selection

BGP ανταλλάσσει reachability ανάμεσα σε autonomous systems και επιλέγει paths με policy. Security analysis χρειάζεται prefix ownership, upstream relationships και evidence από πολλές παρατηρήσεις αντί για μία route view.

### 6. Route-origin validation

RPKI/ROV βοηθά να ελεγχθεί αν ένα AS είναι εξουσιοδοτημένο να origin ένα prefix. Δεν αποδεικνύει ολόκληρο το AS path και πρέπει να συνδυάζεται με routing policy/monitoring.

### 7. Control-plane monitoring

DNS zone changes, registrar events, RPKI state, BGP announcements και resolver health χρειάζονται timestamps και independent alert paths. Control-plane compromise συχνά προηγείται του visible data-plane impact.

### 8. Resilience design

Χρησιμοποίησε diversity σε authoritative DNS, resolvers, transit, regions και recovery accounts όπου δικαιολογείται. Η redundancy πρέπει να αποφεύγει κοινό hidden dependency που καταρρέει ταυτόχρονα.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Γράψε πρώτα invariant και expected result, άλλαξε μία μεταβλητή κάθε φορά και κράτησε μόνο το evidence που χρειάζεται.

1. **Trace the full resolution path for a domain you own using passive/publicly documented information and draw the delegation chain** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
2. **Create a tabletop exercise for accidental deletion of a DNS zone and list recovery dependencies in order** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
3. **Build a worksheet that separates DNS integrity, DNS confidentiality, registrar security, certificate issuance, and routing security controls** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary και ποιος έχει authority;
2. Ποιο state μπορεί να γίνει stale, replayed ή inconsistent;
3. Ποιο evidence θα διέψευδε την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά το blast radius;
5. Πώς θα επαναλάβεις το test με ασφάλεια μετά τη remediation?

## Πλήρες αγγλικό μάθημα

[English Module 087](../../English/04-Network-Wireless-and-Internet/87-DNS-Routing-BGP-and-Internet-Infrastructure-Security.md)

## Συνέχεια

Χρησιμοποίησε **Αναζήτηση μαθημάτων** ή **Διαδρομές μάθησης** από το κύριο menu για τα σχετικά επόμενα θέματα.
