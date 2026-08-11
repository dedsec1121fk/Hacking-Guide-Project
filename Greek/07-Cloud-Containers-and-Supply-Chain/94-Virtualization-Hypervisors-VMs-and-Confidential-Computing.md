# Virtualization, Hypervisors, VMs και Confidential Computing

> **Ελληνική έκδοση — Μάθημα 094.** Διατηρούνται οι διεθνείς τεχνικοί όροι όπου είναι ακριβέστεροι και ευκολότεροι στην αναζήτηση.

## Στόχος του μαθήματος

Να κατανοήσεις σε βάθος το **Virtualization, Hypervisors, VMs και Confidential Computing**, να αναγνωρίζεις trust boundaries και failure states και να μπορείς να αποδείξεις ένα συμπέρασμα με ασφαλές, επαναλήψιμο evidence.

> **Όριο εξουσιοδότησης:** Πρακτική μόνο σε συστήματα, λογαριασμούς, κώδικα ή labs που σου ανήκουν ή έχεις ρητή άδεια να ελέγξεις. Προτίμησε localhost, synthetic data και disposable environments.

## Βαθιές τεχνικές έννοιες

### 1. Hypervisor models

Type-1 και hosted hypervisors τοποθετούν virtualization boundary σε διαφορετικά layers. Threat model πρέπει να περιλαμβάνει host/hypervisor, management plane και shared hardware.

### 2. Hardware virtualization

CPU/IOMMU virtualization απομονώνει guest execution και DMA όταν ρυθμίζεται σωστά. Firmware, device passthrough και platform settings μπορούν να αλλάξουν το πραγματικό boundary.

### 3. Virtual devices

Emulated/paravirtualized network, storage, graphics και other devices είναι complex parser interfaces από guest προς privileged host code. Μείωσε unused devices και κράτησε hypervisor/device-model patches ενημερωμένα.

### 4. Snapshots and images

Snapshots/images περιέχουν memory/disk/secrets και μπορούν να επαναφέρουν stale credentials ή vulnerable state. Protect storage, provenance, access και lifecycle όπως production data.

### 5. Management plane

Hypervisor/cloud console μπορεί να create, attach disks, snapshot ή inspect guests. Management identity χρειάζεται strong auth, least privilege και independent audit.

### 6. Nested virtualization

Nested layers αυξάνουν complexity και κάνουν assumptions για hardware features/telemetry λιγότερο προφανή. Document ποιο layer owns each control και ποια isolation guarantees χάνονται.

### 7. Confidential computing

Memory-encryption/TEE VM models μειώνουν trust στον host για συγκεκριμένα data-in-use threats. Δεν αφαιρούν guest vulnerabilities, metadata leakage, availability ή misconfigured attestation/policy.

### 8. Boundary verification

Verify isolation με configuration, attestation όπου σχετικό, device assignment και harmless cross-VM negative tests. Μην θεωρείς marketing label evidence από μόνο του.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Γράψε πρώτα invariant και expected result, άλλαξε μία μεταβλητή κάθε φορά και κράτησε μόνο το evidence που χρειάζεται.

1. **Build a local VM threat model listing every host/guest integration feature and justify whether it is required** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
2. **Take a disposable VM snapshot with non-sensitive test data and document what security-sensitive state a real snapshot could preserve** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
3. **Compare the trust assumptions of a normal VM, container, and confidential VM in a one-page matrix** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary και ποιος έχει authority;
2. Ποιο state μπορεί να γίνει stale, replayed ή inconsistent;
3. Ποιο evidence θα διέψευδε την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά το blast radius;
5. Πώς θα επαναλάβεις το test με ασφάλεια μετά τη remediation?

## Πλήρες αγγλικό μάθημα

[English Module 094](../../English/07-Cloud-Containers-and-Supply-Chain/94-Virtualization-Hypervisors-VMs-and-Confidential-Computing.md)

## Συνέχεια

Χρησιμοποίησε **Αναζήτηση μαθημάτων** ή **Διαδρομές μάθησης** από το κύριο menu για τα σχετικά επόμενα θέματα.
