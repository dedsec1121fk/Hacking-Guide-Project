# OAuth 2.0 Security BCP, OIDC Federation και Token Defense

> **Ελληνική έκδοση — Μάθημα 092.** Διατηρούνται οι διεθνείς τεχνικοί όροι όπου είναι ακριβέστεροι και ευκολότεροι στην αναζήτηση.

## Στόχος του μαθήματος

Να κατανοήσεις σε βάθος το **OAuth 2.0 Security BCP, OIDC Federation και Token Defense**, να αναγνωρίζεις trust boundaries και failure states και να μπορείς να αποδείξεις ένα συμπέρασμα με ασφαλές, επαναλήψιμο evidence.

> **Όριο εξουσιοδότησης:** Πρακτική μόνο σε συστήματα, λογαριασμούς, κώδικα ή labs που σου ανήκουν ή έχεις ρητή άδεια να ελέγξεις. Προτίμησε localhost, synthetic data και disposable environments.

## Βαθιές τεχνικές έννοιες

### 1. OAuth roles and purpose

OAuth είναι delegation framework: resource owner, client, authorization server και resource server έχουν διαφορετικό ρόλο. Access token δεν είναι γενικό identity proof για οποιαδήποτε εφαρμογή.

### 2. Authorization code and PKCE

Authorization Code με PKCE δένει authorization response με το client instance που ξεκίνησε το flow. Validate state/nonce όπου απαιτείται και μην εκθέτεις code/tokens σε unnecessary browser locations/logs.

### 3. Redirect URI integrity

Redirect URI είναι high-value boundary. Χρησιμοποίησε exact/pre-registered URIs και απέφυγε open redirects ή broad wildcard matching που επιτρέπουν code delivery σε λάθος endpoint.

### 4. Issuer and mix-up defenses

Clients/resource servers πρέπει να ξέρουν ποιος issuer εξέδωσε response/token και να μην μπερδεύουν multiple authorization servers. Bind discovery, issuer, endpoints και keys σε αναμενόμενο relationship.

### 5. Token audience and scope

Audience περιορίζει ποιο resource server πρέπει να δεχτεί token και scope/authorization περιορίζει operations. Έγκυρη signature χωρίς σωστό audience/tenant/resource context δεν αρκεί.

### 6. Refresh tokens

Refresh token έχει μεγαλύτερο lifecycle και μπορεί να εκδώσει νέα access tokens. Rotation, reuse detection, sender/client binding όπου υποστηρίζεται και revocation μειώνουν persistence risk.

### 7. Sender-constrained tokens

Mechanisms όπως mTLS ή proof-of-possession μπορούν να δένουν token με συγκεκριμένο client key ώστε stolen token μόνο του να μην αρκεί. Operational key lifecycle και proxy boundaries πρέπει να υποστηρίζουν το binding.

### 8. Federation lifecycle

OIDC/federation relationships, signing keys, client registration και metadata αλλάζουν. Κράτησε authenticated configuration, rollover overlap, de-registration και incident revocation plan.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Γράψε πρώτα invariant και expected result, άλλαξε μία μεταβλητή κάθε φορά και κράτησε μόνο το evidence που χρειάζεται.

1. **Draw an authorization-code + PKCE sequence for a localhost demo and label every value that must be bound to the initiating transaction** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
2. **Create a token-validation checklist separating cryptographic validity from authorization decisions at the API** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
3. **Review a hypothetical federation design for account-linking ambiguity, stale signing keys, incorrect issuer/audience checks, and deprovisioning gaps** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary και ποιος έχει authority;
2. Ποιο state μπορεί να γίνει stale, replayed ή inconsistent;
3. Ποιο evidence θα διέψευδε την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά το blast radius;
5. Πώς θα επαναλάβεις το test με ασφάλεια μετά τη remediation?

## Πλήρες αγγλικό μάθημα

[English Module 092](../../English/06-Identity-Cryptography-and-Trust/92-OAuth-20-Security-BCP-OIDC-Federation-and-Token-Defense.md)

## Συνέχεια

Χρησιμοποίησε **Αναζήτηση μαθημάτων** ή **Διαδρομές μάθησης** από το κύριο menu για τα σχετικά επόμενα θέματα.
