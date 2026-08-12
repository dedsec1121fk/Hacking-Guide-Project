# Post-Quantum Migration, Crypto Agility και Hybrid Deployment

> **Ελληνική έκδοση — Μάθημα 101.** Διατηρούνται οι διεθνείς τεχνικοί όροι όπου είναι ακριβέστεροι και ευκολότεροι στην αναζήτηση.

## Στόχος του μαθήματος

Να κατανοήσεις σε βάθος το **Post-Quantum Migration, Crypto Agility και Hybrid Deployment**, να αναγνωρίζεις trust boundaries και failure states και να μπορείς να αποδείξεις ένα συμπέρασμα με ασφαλές, επαναλήψιμο evidence.

> **Όριο εξουσιοδότησης:** Πρακτική μόνο σε συστήματα, λογαριασμούς, κώδικα ή labs που σου ανήκουν ή έχεις ρητή άδεια να ελέγξεις. Προτίμησε localhost, synthetic data και disposable environments.

## Βαθιές τεχνικές έννοιες

### 1. Cryptographic inventory

Migration ξεκινά με inventory algorithms, protocols, certificates, keys, libraries, hardware και data lifetimes. Χωρίς dependency map δεν μπορείς να ξέρεις ποιο σύστημα μπλοκάρει αλλαγή ή ποια δεδομένα χρειάζονται προτεραιότητα.

### 2. Harvest-now risk

Data που κρυπτογραφούνται σήμερα μπορεί να συλλεχθούν και να αποκρυπτογραφηθούν αργότερα αν έχουν μακροχρόνια αξία και εξαρτώνται από public-key schemes που απειλούνται από future quantum capability. Prioritize confidentiality horizon και exposure.

### 3. Standards

Χρησιμοποίησε finalized/recognized post-quantum standards και vendor/platform guidance αντί για home-grown primitives. Algorithm selection είναι μόνο μέρος του migration· interoperability, key sizes και protocol integration είναι εξίσου σημαντικά.

### 4. Crypto agility

Agility σημαίνει ότι algorithms/keys μπορούν να αλλάξουν με versioned policy και authenticated negotiation χωρίς unsafe fallback. Hard-coded assumptions και fixed field sizes κάνουν migration ακριβό.

### 5. Hybrid approaches

Hybrid deployment συνδυάζει classical και post-quantum mechanisms ώστε failure ενός νέου component να μην είναι μοναδικό trust anchor. Η composition πρέπει να ακολουθεί reviewed standards/protocol profiles και να αποφεύγει custom combining logic.

### 6. PKI impact

Certificates, enrollment, HSM/KMS, revocation, chain validation και network appliances μπορεί να έχουν size/algorithm constraints. Test end-to-end PKI workflows και recovery πριν από broad rollout.

### 7. Migration sequencing

Ξεκίνα από inventory και low-risk interoperability labs, μετά dual-support/rotation, service migration και retirement legacy algorithms σύμφωνα με data lifetime και dependency readiness.

### 8. Evidence

Κράτησε algorithm inventory, owners, versions, test vectors, handshake/certificate sizes, latency, failure modes και rollback criteria ώστε η migration να είναι measurable engineering project.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Γράψε πρώτα invariant και expected result, άλλαξε μία μεταβλητή κάθε φορά και κράτησε μόνο το evidence που χρειάζεται.

1. **Build a cryptographic inventory for a small local application and record every library/API that creates or validates keys/signatures** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
2. **Create a compatibility test plan that anticipates larger key/signature objects and handshake messages without claiming unsupported algorithms are production-ready** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
3. **Classify sample data sets by confidentiality lifetime and use that to rank migration priority** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary και ποιος έχει authority;
2. Ποιο state μπορεί να γίνει stale, replayed ή inconsistent;
3. Ποιο evidence θα διέψευδε την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά το blast radius;
5. Πώς θα επαναλάβεις το test με ασφάλεια μετά τη remediation?

## Πλήρες αγγλικό μάθημα

[English Module 101](../../English/06-Identity-Cryptography-and-Trust/101-Post-Quantum-Migration-Crypto-Agility-and-Hybrid-Deployment.md)

## Συνέχεια

Χρησιμοποίησε **Αναζήτηση μαθημάτων** ή **Διαδρομές μάθησης** από το κύριο menu για τα σχετικά επόμενα θέματα.
