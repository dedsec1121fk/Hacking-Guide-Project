# Ασφάλεια IPv6, Neighbor Discovery και Σύγχρονα LAN Attack Surfaces

> **Ελληνική έκδοση — Μάθημα 086.** Διατηρούνται οι διεθνείς τεχνικοί όροι όπου είναι ακριβέστεροι και ευκολότεροι στην αναζήτηση.

## Στόχος του μαθήματος

Να κατανοήσεις σε βάθος το **Ασφάλεια IPv6, Neighbor Discovery και Σύγχρονα LAN Attack Surfaces**, να αναγνωρίζεις trust boundaries και failure states και να μπορείς να αποδείξεις ένα συμπέρασμα με ασφαλές, επαναλήψιμο evidence.

> **Όριο εξουσιοδότησης:** Πρακτική μόνο σε συστήματα, λογαριασμούς, κώδικα ή labs που σου ανήκουν ή έχεις ρητή άδεια να ελέγξεις. Προτίμησε localhost, synthetic data και disposable environments.

## Βαθιές τεχνικές έννοιες

### 1. Address architecture

Global, unique-local, link-local, multicast και privacy addresses έχουν διαφορετικό routing/visibility. Κατέγραψε ποια address classes επιτρέπονται ανά interface και ποια δεν πρέπει να περνούν συγκεκριμένο boundary.

### 2. Neighbor Discovery

Το IPv6 Neighbor Discovery χρησιμοποιεί ICMPv6 για neighbors, routers και redirects. Blind filtering μπορεί να σπάσει το δίκτυο, ενώ blind trust σε first-hop control messages αυξάνει local-link risk.

### 3. SLAAC and DHCPv6

SLAAC και DHCPv6 μπορούν να συνυπάρχουν και να δίνουν διαφορετικό address/DNS state. Inventory και NAC δεν πρέπει να θεωρούν ότι ένα DHCP lease ισούται με μία endpoint identity.

### 4. Extension headers

Extension-header chains απαιτούν consistent parsing και bounded work από hosts και security devices. Διαφορετική υποστήριξη ή ordering μπορεί να δημιουργήσει policy gaps ή reliability issues.

### 5. Fragmentation and PMTUD

Στο IPv6 ordinary fragmentation γίνεται από endpoints και το PMTUD εξαρτάται από ICMPv6 Packet Too Big. Υπερβολικό ICMPv6 blocking μπορεί να μοιάζει με application outage.

### 6. Dual-stack exposure

Service που είναι κλειστό σε IPv4 μπορεί να παραμένει reachable σε IPv6. Έλεγξε sockets, ACLs, proxies, VPN, DNS και monitoring για πραγματική parity.

### 7. Local-link trust

Devices στο ίδιο VLAN δεν πρέπει να θεωρούνται αυτόματα trusted. First-hop policy, endpoint firewall, segmentation και switch controls καθορίζουν ποιος μπορεί να επηρεάσει local network state.

### 8. Telemetry

Χρήσιμα evidence είναι address lifetimes, RA sources, neighbor-cache changes, AAAA answers, routes, firewall decisions και bind addresses. Normalize IPv6 textual forms πριν από correlation.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Γράψε πρώτα invariant και expected result, άλλαξε μία μεταβλητή κάθε φορά και κράτησε μόνο το evidence που χρειάζεται.

1. **Build a two-host or two-namespace IPv6-only localhost lab and document addresses, routes, neighbor entries, and DNS behavior without sending traffic outside the lab** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
2. **Compare an application bound to 127** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.
3. **Create a firewall-review worksheet that checks IPv4 and IPv6 policy parity for one lab service** — εκτέλεσέ το μόνο στο isolated/owned lab και κατέγραψε before/after αποτέλεσμα.

## Έλεγχος γνώσεων

1. Ποιο είναι το βασικό trust boundary και ποιος έχει authority;
2. Ποιο state μπορεί να γίνει stale, replayed ή inconsistent;
3. Ποιο evidence θα διέψευδε την αρχική υπόθεση;
4. Ποιο control μειώνει πραγματικά το blast radius;
5. Πώς θα επαναλάβεις το test με ασφάλεια μετά τη remediation?

## Πλήρες αγγλικό μάθημα

[English Module 086](../../English/04-Network-Wireless-and-Internet/86-IPv6-Security-Neighbor-Discovery-and-Modern-LAN-Attack-Surfaces.md)

## Συνέχεια

Χρησιμοποίησε **Αναζήτηση μαθημάτων** ή **Διαδρομές μάθησης** από το κύριο menu για τα σχετικά επόμενα θέματα.
