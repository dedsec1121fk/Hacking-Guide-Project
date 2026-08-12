# Cybersecurity Reference Cheatsheet

## Βασικές ερωτήσεις

- Ποιο asset προστατεύεται;
- Ποια identity/process έχει authority;
- Πού βρίσκεται το trust boundary;
- Ποιο input/state το διασχίζει;
- Ποια security property μπορεί να αποτύχει;
- Ποιο evidence αποδεικνύει τη συμπεριφορά;
- Ποιο control προλαμβάνει, ανιχνεύει ή περιορίζει το πρόβλημα;
- Πώς θα γίνει retest μετά τη διόρθωση;

## Networking

Σκέψου layers, addresses, routes, ports, state και name resolution. Ένα packet capture δείχνει ό,τι είναι ορατό σε ένα observation point· δεν αποδεικνύει μόνο του την πρόθεση της εφαρμογής.

## Web/API

Ακολούθησε client → proxy/CDN → server → framework/router → authorization → data store/downstream service. Έλεγξε normalization, method/path, headers, body parser, session/token context και object-level authorization.

## Identity

Ξεχώρισε authentication, authorization, session/token lifecycle, federation, key trust και recovery. Τα short-lived credentials βοηθούν μόνο όταν issuance και revocation είναι επίσης ελεγχόμενα.

## Systems

Σκέψου users/tokens, processes, memory, files, services, syscalls, executable loading και telemetry. Το privilege είναι γράφος capabilities και όχι μόνο username.

## Cloud/container

Control plane, workload identity, network/data plane, secrets, build provenance, artifact trust και audit logs είναι διαφορετικά layers.

## Ποιότητα evidence

Προτίμησε reproducible commands, sanitized logs, hashes, packet/trace metadata, configuration excerpts και before/after validation. Κατέγραψε versions και χρόνο.
