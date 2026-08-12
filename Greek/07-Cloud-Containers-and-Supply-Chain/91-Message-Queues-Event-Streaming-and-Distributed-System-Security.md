# Message Queues, Event Streaming και Ασφάλεια Distributed Systems

> **Ελληνική έκδοση — Μάθημα 091.** Διατηρούνται οι διεθνείς τεχνικοί όροι όπου είναι ακριβέστεροι και ευκολότεροι στην αναζήτηση.

## Στόχος του μαθήματος

Να κατανοήσεις σε βάθος το **Message Queues, Event Streaming και Ασφάλεια Distributed Systems**, να αναγνωρίζεις trust boundaries και failure states και να μπορείς να αποδείξεις ένα συμπέρασμα με ασφαλές, επαναλήψιμο evidence.

> **Όριο εξουσιοδότησης:** Πρακτική μόνο σε συστήματα, λογαριασμούς, κώδικα ή labs που σου ανήκουν ή έχεις ρητή άδεια να ελέγξεις. Προτίμησε localhost, synthetic data και disposable environments.

## Βαθιές τεχνικές έννοιες

### 1. Producer and consumer identity

Producer και consumer πρέπει να έχουν ξεχωριστές identities και permissions ανά topic/queue/action. Shared broker credential κρύβει attribution και αυξάνει blast radius.

### 2. Topic and routing design

Topic names, routing keys και subscriptions είναι authorization surface. Διαχώρισε tenants/environments και απόφυγε wildcard permissions που φτάνουν data άσχετων workloads.

### 3. Message authenticity and replay

TLS προστατεύει transport, αλλά downstream consumer μπορεί να χρειάζεται message provenance/freshness όταν messages αποθηκεύονται ή περνούν πολλούς brokers. IDs, timestamps ή signatures πρέπει να έχουν σαφές replay model.

### 4. Schema evolution

Producer/consumer versions μπορεί να συνυπάρχουν. Explicit schemas, compatibility rules και unknown-field behavior εμποδίζουν silent semantic change σε security-sensitive fields.

### 5. Retries and idempotency

At-least-once delivery σημαίνει duplicates. Consumer που εκτελεί state-changing action χρειάζεται idempotency ή transaction model ώστε retry να μη διπλασιάζει πληρωμή/privilege/change.

### 6. Dead-letter queues

DLQ περιέχει failed messages και συχνά sensitive payload. Περιορίσε access/retention, καταγραφή reasons και safe replay ώστε corrupted message να μην επανεισάγεται ανεξέλεγκτα.

### 7. Background privilege

Workers συχνά τρέχουν χωρίς user interaction και με broad service permissions. Δέσε κάθε message με trusted tenant/resource context και δώσε μόνο την authority που χρειάζεται το συγκεκριμένο handler.

### 8. Distributed tracing

Correlation IDs και traces βοηθούν να ακολουθήσεις event σε producer→broker→consumer χωρίς να θεωρείς μία timestamp σειρά τέλεια. Κατέγραψε retries και message IDs για causal analysis.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Γράψε πρώτα invariant και expected result, άλλαξε μία μεταβλητή κάθε φορά και κράτησε μόνο το evidence που χρειάζεται.

1. **Model an order-processing pipeline with producer, broker, three consumers, dead-letter queue, and admin replay tool; mark each trust boundary** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
2. **Write test cases for duplicate delivery, out-of-order delivery, expired messages, malformed schemas, and unauthorized routing using toy data** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
3. **Design a least-privilege matrix for producers and consumers and identify where one compromised workload would currently have excessive reach** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary και ποιος έχει authority;
2. Ποιο state μπορεί να γίνει stale, replayed ή inconsistent;
3. Ποιο evidence θα διέψευδε την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά το blast radius;
5. Πώς θα επαναλάβεις το test με ασφάλεια μετά τη remediation?

## Πλήρες αγγλικό μάθημα

[English Module 091](../../English/07-Cloud-Containers-and-Supply-Chain/91-Message-Queues-Event-Streaming-and-Distributed-System-Security.md)

## Συνέχεια

Χρησιμοποίησε **Αναζήτηση μαθημάτων** ή **Διαδρομές μάθησης** από το κύριο menu για τα σχετικά επόμενα θέματα.
