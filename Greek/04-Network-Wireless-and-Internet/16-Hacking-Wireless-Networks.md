# Ασφάλεια Ασύρματων Δικτύων

Η ασφάλεια Wi-Fi συνδυάζει radio behavior, authentication, encryption, segmentation, device identity, roaming και management. Το «χρησιμοποιεί WPA» δεν αρκεί ως συμπέρασμα· πρέπει να εξετάζονται security mode, credential lifecycle, client isolation, management plane και monitoring.

> **Όριο εξουσιοδότησης:** Active wireless testing γίνεται μόνο σε access points και clients που σου ανήκουν ή έχεις ρητή άδεια να αξιολογήσεις. Τα radio signals ξεπερνούν φυσικά όρια, επομένως μην συλλέγεις, διακόπτεις, impersonate ή προσπαθείς να ανακτήσεις credentials γειτονικών τρίτων δικτύων.

## Μαθησιακοί στόχοι

- Να κατανοείς station, AP, SSID/BSSID και βασικές κατηγορίες 802.11 frames.
- Να συγκρίνεις open, WPA2, WPA3 και enterprise authentication.
- Να ξεχωρίζεις PSK από 802.1X identity model.
- Να αναγνωρίζεις legacy/transition risks.
- Να αξιολογείς guest, IoT και management segmentation.

## 802.11 ρόλοι

Σε infrastructure Wi-Fi υπάρχουν station/client και access point. Enterprise περιβάλλοντα προσθέτουν controller, authentication server, certificates, NAC και roaming. Management, control και data frames έχουν διαφορετικό ρόλο. Protected Management Frames μειώνουν ορισμένες κατηγορίες forged management traffic όταν υποστηρίζονται και απαιτούνται σωστά.

## Open networks

Open SSID δεν προσφέρει link-layer confidentiality ανάμεσα σε client και AP. Σωστά ρυθμισμένο TLS εξακολουθεί να προστατεύει application data, αλλά το δίκτυο πρέπει να θεωρείται untrusted. Η εφαρμογή δεν πρέπει να βασίζεται στο Wi-Fi ως boundary εμπιστοσύνης.

## WPA2/WPA3 Personal

Personal mode χρησιμοποιεί shared secret. Η ασφάλεια εξαρτάται από ισχυρό passphrase και ασφαλή διανομή, αλλά η κοινή τιμή έχει αδύναμο individual accountability και δύσκολη ανάκληση ανά συσκευή. Το WPA3-Personal με SAE βελτιώνει την αντίσταση σε offline password guessing σε σχέση με παλιότερο PSK handshake όταν εφαρμόζεται σωστά. Transition modes χρειάζονται συνειδητή αξιολόγηση.

## Enterprise Wi-Fi και 802.1X

Enterprise mode χρησιμοποιεί EAP και backend όπως RADIUS. Σημαντικά στοιχεία είναι το EAP method, η validation του server certificate από τον client, lifecycle identities/certificates και η policy μετά το authentication. Client που αποδέχεται άγνωστο authentication server μόνο επειδή αναγνωρίζει το SSID δημιουργεί σοβαρό trust problem.

## Legacy protocols

WEP είναι παρωχημένο και δεν πρέπει να χρησιμοποιείται. TKIP και παλιά compatibility modes πρέπει να αφαιρούνται όπου υποστηρίζεται. Legacy τεχνολογία έχει θέση στην ιστορική κατανόηση, όχι σε νέα deployments.

## Guest, IoT και management segmentation

Guests, unmanaged clients και IoT έχουν διαφορετικό trust. Χρησιμοποίησε client isolation όπου ταιριάζει, περιορισμένο east-west access, egress/DNS policy και ξεχωριστό management. Η σύνδεση στο Wi-Fi δεν πρέπει να σημαίνει πρόσβαση σε admin interfaces.

## Management και monitoring

Προστάτευσε AP/controller administration με ισχυρό authentication, restricted management network, updates, backups και logs. Χρήσιμη telemetry είναι authentication/association events, RADIUS results, configuration changes, rogue AP observations, interference/channel health και repeated auth failures. Μην διατηρείς άσχετα client payloads.

## Καθοδηγούμενο εργαστήριο

Χρησιμοποίησε AP που σου ανήκει. Κατέγραψε security mode, client isolation, management exposure και update status. Σύνδεσε test device και επιβεβαίωσε ότι εμφανίζονται φυσιολογικά authentication events. Αν έχεις απομονωμένο guest network, επιβεβαίωσε ότι guest client δεν φτάνει το management interface.

## Συνηθισμένα λάθη

- Θεώρηση ότι επειδή βλέπεις ένα SSID έχεις δικαίωμα testing.
- Shared PSK για περιβάλλον που απαιτεί individual identity.
- Μη validation RADIUS/server certificate.
- Μόνιμα legacy transition modes.
- Guests/IoT/management στο ίδιο trust zone.
- Disruptive tests σε shared spectrum.

## Έλεγχος γνώσεων

1. Γιατί shared PSK έχει αδύναμο individual accountability;
2. Τι βελτιώνει το WPA3-SAE;
3. Γιατί ο enterprise client πρέπει να επαληθεύει τον authentication server;
4. Γιατί guest και management networks πρέπει να χωρίζονται;
5. Γιατί το wireless testing απαιτεί ιδιαίτερη προσοχή στο scope;

## Καθοδηγούμενη μελέτη

Χρησιμοποίησε τη [Μεθοδολογία Μελέτης](../Guides/STUDY-METHOD.md). Κράτησε όλες τις δοκιμές σε APs που σου ανήκουν και εστίασε σε configuration, identity, segmentation και evidence.

### Συνέχισε με

Προτεινόμενα επόμενα modules: **44, 51, 55, 88, 122, 123**.
