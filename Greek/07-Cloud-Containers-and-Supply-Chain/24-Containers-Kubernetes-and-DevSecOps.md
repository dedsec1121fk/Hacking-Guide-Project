# Containers, Kubernetes και DevSecOps

> **Ελληνική έκδοση — Μάθημα 024.** Οι διεθνείς τεχνικοί όροι, protocol names, standards και commands διατηρούνται στα Αγγλικά όπου αυτό βοηθά την ακρίβεια.

## Στόχος του μαθήματος

Cloud-native ασφάλεια σημαίνει έλεγχο control planes, workload identity, artifacts, build systems, containers και data flows. Οι σημαντικότερες αστοχίες συχνά προκύπτουν από υπερβολικά δικαιώματα, implicit trust μεταξύ services, μη επαληθεύσιμα artifacts ή ανεπαρκή provenance.

Σε αυτό το μάθημα εστιάζεις ειδικά στο **Containers, Kubernetes και DevSecOps**. Στο τέλος πρέπει να μπορείς να περιγράψεις το security model με δικά σου λόγια, να αναγνωρίζεις τα βασικά failure modes, να σχεδιάζεις ασφαλή test cases και να εξηγείς ποιο evidence χρειάζεται για να στηριχθεί ένα συμπέρασμα.

## Θέματα που καλύπτονται

- **Container security model**
  Για το **Container security model**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **Image hygiene**
  Για το **Image hygiene**, στο πλαίσιο του **Containers, Kubernetes και DevSecOps**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Kubernetes security areas**
  Για το **Kubernetes security areas**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **Identity and RBAC**
  Για το **Identity and RBAC**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Workload isolation**
  Για το **Workload isolation**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **Secrets**
  Για το **Secrets**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **Admission and policy**
  Για το **Admission and policy**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **DevSecOps controls**
  Για το **DevSecOps controls**, στο πλαίσιο του **Containers, Kubernetes και DevSecOps**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Safe lab**
  Στο **Safe lab**, μετέτρεψε τη θεωρία του **Containers, Kubernetes και DevSecOps** σε ελέγξιμα κριτήρια: τι πρέπει να μπορείς να εξηγήσεις, ποιο λάθος assumption εμφανίζεται συχνότερα, ποιο safe lab το αποκαλύπτει και ποιο retest αποδεικνύει ότι το διόρθωσες.
- **Container image lifecycle**
  Για το **Container image lifecycle**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **Runtime minimization**
  Στο **Runtime minimization**, σύνδεσε τον υψηλού επιπέδου μηχανισμό με process, memory και runtime state. Χρησιμοποίησε harmless samples, debugger/sanitizer ή static analysis σε lab και κατέγραψε root cause, mitigation και observable artifacts.
- **Linux privilege controls**
  Για το **Linux privilege controls**, στο πλαίσιο του **Containers, Kubernetes και DevSecOps**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Kubernetes control-plane security**
  Για το **Kubernetes control-plane security**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **RBAC review**
  Για το **RBAC review**, χαρτογράφησε principal/subject, credential ή authentication context, permissions, lifetime και revocation. Ξεχώρισε ποιο component πιστοποιεί την ταυτότητα από εκείνο που παίρνει την τελική authorization απόφαση.
- **Namespace design**
  Για το **Namespace design**, κατέγραψε Linux UID/GID/capabilities, namespace membership, syscall/filesystem boundary και LSM/seccomp policy. Έλεγξε effective privilege μέσα σε disposable VM/container και χρησιμοποίησε `/proc`, audit/logging και configuration diff ως evidence.
- **Pod Ασφάλεια Standards**
  Για το **Pod Ασφάλεια Standards**, ξεχώρισε normative specification από tutorial ή vendor summary. Κατέγραψε έκδοση/ημερομηνία, ποιο requirement στηρίζει το συμπέρασμα και ποιο μέρος του **Containers, Kubernetes και DevSecOps** χρειάζεται επανέλεγχο όταν αλλάξει η πηγή.
- **Network policy**
  Στο **Network policy**, ακολούθησε packet και protocol state από άκρο σε άκρο: ποιο endpoint δημιουργεί κάθε field, τι validation γίνεται, πού αλλάζει trust boundary και ποια telemetry επιβεβαιώνει την πραγματική ροή.
- **Secrets and configuration**
  Για το **Secrets and configuration**, ξεχώρισε primitive από protocol και key-management policy. Κατέγραψε generation, storage, distribution, rotation, revocation, trust anchors και failure behavior σε όλο το lifecycle.
- **Admission policy**
  Για το **Admission policy**, σύνδεσε το τεχνικό control με asset owner, data classification, business impact, retention και ανθρώπινη διαδικασία. Μέτρα αν μειώνει πραγματικό risk και αν μπορεί να επαληθευτεί με κατάλληλο audit evidence.
- **Observability for containers**
  Για το **Observability for containers**, χαρτογράφησε control plane, workload identity, permissions, artifact/data provenance και lifecycle. Έλεγξε πώς δημιουργείται authority, πού κληρονομείται, πώς ανακαλείται και τι audit trail παραμένει.
- **DevSecOps pipeline architecture**
  Για το **DevSecOps pipeline architecture**, στο πλαίσιο του **Containers, Kubernetes και DevSecOps**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.
- **Pipeline controls**
  Για το **Pipeline controls**, στο πλαίσιο του **Containers, Kubernetes και DevSecOps**, κατέγραψε (1) ποιο component ή actor έχει authority, (2) ποιο state/data αλλάζει, (3) ποια validation πρέπει να γίνει πριν από την αλλαγή και (4) ποιο log, trace, configuration ή test result αποδεικνύει ότι το control λειτουργεί.

## Μέθοδος ανάλυσης

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md) για scope, evidence, note-taking και κριτήρια ολοκλήρωσης. Για το **Containers, Kubernetes και DevSecOps**, πριν κάνεις οποιοδήποτε test σχεδίασε τα components, σημείωσε πού αλλάζει η εμπιστοσύνη και γράψε μία πρόταση που περιγράφει το security invariant που θέλεις να ελέγξεις.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε local containers ή sandbox cloud accounts που σου ανήκουν. Έλεγξε policies και artifacts read-only πριν από αλλαγές και απέφυγε δημόσια exposure στα labs.


Ακολούθησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md): γράψε expected result πριν το test, άλλαξε μία μεταβλητή κάθε φορά, κράτησε sanitized evidence και κάνε retest μετά το hardening του **Containers, Kubernetes και DevSecOps**.

## Έλεγχος γνώσεων

- Μπορείς να εξηγήσεις το βασικό trust boundary του **Containers, Kubernetes και DevSecOps** χωρίς σημειώσεις;
- Μπορείς να δώσεις ένα failure mode και να πεις ποιο evidence θα το επιβεβαίωνε;
- Μπορείς να ξεχωρίσεις symptom, root cause και compensating control;
- Μπορείς να σχεδιάσεις ασφαλές retest που δεν επεκτείνει το scope;

## Πλήρες αγγλικό μάθημα

Για το αναλυτικό αγγλικό κείμενο, τις πηγές και τα επιπλέον τεχνικά παραδείγματα χρησιμοποίησε το αντίστοιχο αρχείο:

[English Module 024](../../English/07-Cloud-Containers-and-Supply-Chain/24-Containers-Kubernetes-and-DevSecOps.md)
