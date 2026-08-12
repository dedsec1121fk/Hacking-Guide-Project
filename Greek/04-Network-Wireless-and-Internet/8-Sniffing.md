# Packet Capture, Sniffing και Network Visibility

Packet capture δίνει άμεσο evidence για επικοινωνία μεταξύ systems. Είναι χρήσιμο για troubleshooting, incident response και protocol analysis, αλλά ένα PCAP μπορεί να περιέχει credentials, tokens, προσωπικά δεδομένα και confidential information.

> **Όριο εξουσιοδοτημένης χρήσης:** Κάνε capture μόνο σε interfaces/networks που σου ανήκουν ή έχεις ρητή άδεια να monitorάρεις. Προτίμησε localhost/VM lab ή prerecorded captures. Μην interceptάρεις traffic τρίτων.

## Τι αποδεικνύει ένα capture

Αποδεικνύει τι είδε το συγκεκριμένο capture point. Δεν αποδεικνύει απαραίτητα τι συνέβη σε άλλο σημείο. Packets μπορεί να χαθούν, να αλλάξουν από proxy/NAT, να είναι encrypted ή να μην παρατηρούνται λόγω offload.

Κατέγραψε interface/location, timestamps, filter, relevant IP/ports, θέση σε σχέση με NAT/proxy και πιθανό packet loss.

## Protocol layers

Χρήσιμη σειρά:

1. Link layer — MAC/VLAN/frame type.
2. IP — IPv4/IPv6, TTL/hop limit, fragmentation.
3. Transport — TCP state ή UDP datagrams.
4. DNS/ICMP/control traffic.
5. TLS/certificate/protocol negotiation.
6. Application layer μόνο όταν legitimately observable.

Encryption μπορεί να κρύβει payload αλλά να αφήνει useful metadata για endpoints, timing, volume και protocol negotiation.

## Switched networks

Σε normal switched Ethernet ένας host δεν βλέπει αυτόματα όλο το unicast traffic. Defenders χρησιμοποιούν approved SPAN/TAP, gateway sensors, host agents ή cloud traffic mirroring. Μην χρησιμοποιείς poisoning/interception πάνω σε shared network για να «δεις περισσότερα».

## Filters

Capture filter περιορίζει τι αποθηκεύεται. Display filter περιορίζει τι εμφανίζεται μετά. Πολύ narrow capture μπορεί να χάσει context· πολύ broad capture μπορεί να συλλέξει unnecessary sensitive data.

Safe localhost example:

```bash
tcpdump -i lo tcp port 8000
```

Παράγαγε μόνο δικό σου local request και σταμάτησε αμέσως μετά.

## TCP, DNS και TLS evidence

Σε TCP παρατήρησε handshake, sequence behavior, retransmissions, resets και teardown. Retransmission δεν είναι αυτόματα attack.

Σε DNS παρατήρησε queried names, resolver, response codes και TTL. Encrypted DNS μεταφέρει visibility σε endpoint/resolver logs.

Σε TLS μπορείς να δεις protocol/certificate metadata και connection relationships χωρίς να αποδυναμώνεις production encryption.

## PCAP handling

PCAP μπορεί να έχει cleartext passwords από legacy protocols, bearer tokens, cookies, email content ή internal hostnames. Χρησιμοποίησε access controls, minimum retention και sanitized extracts στα reports.

## Συχνά λάθη

- Capture χωρίς γνώση του position στο network path.
- Absence of packet = «δεν έγινε event».
- Τεράστια captures με άσχετα sensitive data.
- Retransmission/reset ως attack χωρίς context.
- Disable TLS για visibility.
- Capture third-party traffic.

## Καθοδηγούμενο εργαστήριο

Ξεκίνα localhost HTTP server, capture μόνο TCP/8000 στο loopback, κάνε δύο requests και σταμάτησε. Εντόπισε setup, request/response και teardown και σύγκρινε timeline με server access log.

## Έλεγχος γνώσεων

1. Τι αποδεικνύει ένα capture;
2. Γιατί έχει σημασία το capture location;
3. Capture filter vs display filter;
4. Τι metadata μένει χρήσιμο με TLS;
5. Ποια privacy risks έχει ένα PCAP;

## Καθοδηγούμενη μελέτη

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Κάθε conclusion να βασίζεται σε packet evidence και τουλάχιστον μία δεύτερη πηγή.

### Συνέχεια

Προτεινόμενα μαθήματα: **12, 23, 51, 77**.
