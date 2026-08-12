# Multi-Cloud, SaaS Federation, Tenant Isolation και Control Planes

> **Ελληνική έκδοση — Μάθημα 105.** Διατηρούνται οι διεθνείς τεχνικοί όροι όπου είναι ακριβέστεροι και ευκολότεροι στην αναζήτηση.

## Στόχος του μαθήματος

Να κατανοήσεις σε βάθος το **Multi-Cloud, SaaS Federation, Tenant Isolation και Control Planes**, να αναγνωρίζεις trust boundaries και failure states και να μπορείς να αποδείξεις ένα συμπέρασμα με ασφαλές, επαναλήψιμο evidence.

> **Όριο εξουσιοδότησης:** Πρακτική μόνο σε συστήματα, λογαριασμούς, κώδικα ή labs που σου ανήκουν ή έχεις ρητή άδεια να ελέγξεις. Προτίμησε localhost, synthetic data και disposable environments.

## Βαθιές τεχνικές έννοιες

### 1. Control versus data plane

Κάθε cloud/SaaS έχει management/control plane και data/workload plane. Compromise admin API μπορεί να αλλάξει policies, keys και logging χωρίς άμεσο data-plane exploit.

### 2. Federation

Enterprise federation συνδέει IdP με cloud/SaaS roles. Validate issuer, audience, tenant, role mapping, MFA/context και lifecycle ώστε identity από λάθος organization να μην παίρνει access.

### 3. Organization hierarchy

Organizations, management groups, folders, accounts/projects και subscriptions κληρονομούν policy διαφορετικά. Review inherited permissions και high-level admins που μπορούν να αλλάξουν πολλά environments.

### 4. SaaS administrators

SaaS global/admin roles συχνά έχουν data export, identity, integration και audit authority. Χρησιμοποίησε separate privileged identities, JIT όπου γίνεται και strong logging.

### 5. Tenant isolation

Provider isolation δεν διορθώνει customer-side misconfiguration. Test synthetic tenant boundaries σε identities, storage, sharing, APIs και integrations.

### 6. Cross-cloud automation

CI/CD, Terraform, brokers και synchronization identities μπορούν να έχουν authority σε πολλά clouds. Narrow federation, short-lived credentials και environment scoping μειώνουν cross-cloud blast radius.

### 7. Policy drift

Different clouds εκφράζουν παρόμοιες controls με διαφορετική semantics. Central policy mapping πρέπει να κρατά provider-specific evidence και να ανιχνεύει drift, όχι να κρύβει διαφορές πίσω από ένα κοινό label.

### 8. Central evidence

Συγκέντρωσε identity, control-plane, data access και configuration logs σε independent location με common correlation schema, αλλά διατήρησε raw provider fields για investigation.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Γράψε πρώτα invariant και expected result, άλλαξε μία μεταβλητή κάθε φορά και κράτησε μόνο το evidence που χρειάζεται.

1. **Create a provider-neutral matrix for identity, admin hierarchy, network policy, key management, audit logs, and public exposure across two hypothetical clouds** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
2. **Model a SaaS marketplace integration and list every permission it could obtain, how it is revoked, and what happens when the employee owner leaves** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
3. **Design a cross-cloud break-glass procedure that avoids one shared permanent super-admin credential** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary και ποιος έχει authority;
2. Ποιο state μπορεί να γίνει stale, replayed ή inconsistent;
3. Ποιο evidence θα διέψευδε την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά το blast radius;
5. Πώς θα επαναλάβεις το test με ασφάλεια μετά τη remediation?

## Πλήρες αγγλικό μάθημα

[English Module 105](../../English/07-Cloud-Containers-and-Supply-Chain/105-Multi-Cloud-SaaS-Federation-Tenant-Isolation-and-Control-Planes.md)

## Συνέχεια

Χρησιμοποίησε **Αναζήτηση μαθημάτων** ή **Διαδρομές μάθησης** από το κύριο menu για τα σχετικά επόμενα θέματα.
