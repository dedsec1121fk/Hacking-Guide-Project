# Enterprise Wireless, WPA3, 802.1X και Wi‑Fi 6/6E/7

> **Ελληνική έκδοση — Μάθημα 088.** Διατηρούνται οι διεθνείς τεχνικοί όροι όπου είναι ακριβέστεροι και ευκολότεροι στην αναζήτηση.

## Στόχος του μαθήματος

Να κατανοήσεις σε βάθος το **Enterprise Wireless, WPA3, 802.1X και Wi‑Fi 6/6E/7**, να αναγνωρίζεις trust boundaries και failure states και να μπορείς να αποδείξεις ένα συμπέρασμα με ασφαλές, επαναλήψιμο evidence.

> **Όριο εξουσιοδότησης:** Πρακτική μόνο σε συστήματα, λογαριασμούς, κώδικα ή labs που σου ανήκουν ή έχεις ρητή άδεια να ελέγξεις. Προτίμησε localhost, synthetic data και disposable environments.

## Βαθιές τεχνικές έννοιες

### 1. WPA3 modes

WPA3-Personal χρησιμοποιεί SAE και enterprise deployments έχουν διαφορετικά assurance profiles. Transition modes πρέπει να αξιολογούνται επειδή compatibility μπορεί να διατηρεί πιο αδύναμο path.

### 2. 802.1X architecture

Enterprise Wi-Fi συνδέει supplicant, authenticator/AP και authentication server όπως RADIUS. Client certificate/server validation και identity mapping είναι εξίσου σημαντικά με το wireless cipher.

### 3. Protected management frames

PMF προστατεύει συγκεκριμένες management frames από forgery όταν απαιτείται σωστά. Δεν προστατεύει κάθε radio denial/interference και πρέπει να ελέγχεται η πραγματική negotiation state.

### 4. Roaming and key hierarchy

Fast roaming και enterprise key hierarchies μειώνουν authentication latency αλλά δημιουργούν additional key/state relationships. Review cache lifetime, controller trust και revocation behavior.

### 5. 6 GHz and newer bands

Νεότερα bands/standards αλλάζουν channel use, discovery και security requirements. Μην εφαρμόζεις assumptions από legacy 2.4/5 GHz χωρίς να ελέγξεις device/AP capabilities και policy.

### 6. Guest and IoT segmentation

Guests και IoT χρειάζονται διαφορετικό trust από managed endpoints. Client isolation, restricted east-west access και ξεχωριστό management plane περιορίζουν blast radius.

### 7. Rogue and misconfigured infrastructure

Unknown APs, duplicate SSIDs, unsafe EAP profiles και accidental bridging είναι συχνά configuration problems. Inventory και controller/RADIUS logs είναι ασφαλέστερη βάση από disruptive radio testing.

### 8. Wireless evidence

Κράτησε AP/controller configuration, authentication results, certificate/EAP context, roaming events και channel health. Απόφυγε collection άσχετου user payload.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Γράψε πρώτα invariant και expected result, άλλαξε μία μεταβλητή κάθε φορά και κράτησε μόνο το evidence που χρειάζεται.

1. **Design three WLAN roles—managed, guest, IoT—and write the exact trust assumptions and allowed flows between them** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
2. **On equipment you own, inspect whether client devices validate the expected enterprise authentication certificate and document the trust path** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
3. **Create an upgrade checklist for moving from a mixed WPA2/WPA3 deployment to a stricter policy without stranding unsupported devices** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary και ποιος έχει authority;
2. Ποιο state μπορεί να γίνει stale, replayed ή inconsistent;
3. Ποιο evidence θα διέψευδε την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά το blast radius;
5. Πώς θα επαναλάβεις το test με ασφάλεια μετά τη remediation?

## Πλήρες αγγλικό μάθημα

[English Module 088](../../English/04-Network-Wireless-and-Internet/88-Enterprise-Wireless-WPA3-8021X-WiFi6-7-Security.md)

## Συνέχεια

Χρησιμοποίησε **Αναζήτηση μαθημάτων** ή **Διαδρομές μάθησης** από το κύριο menu για τα σχετικά επόμενα θέματα.
