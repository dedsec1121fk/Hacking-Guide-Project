# Termux — Γρήγορη Εκκίνηση

Το Termux είναι Android userland για Linux, Python, Git, SSH και τοπική δικτύωση. Αντιμετώπισέ το ως Android εφαρμογή με Linux-like περιβάλλον και όχι ως rooted desktop διανομή.

## Αρχική εγκατάσταση

```bash
pkg update
pkg upgrade
pkg install python git openssh nano curl -y
termux-setup-storage
```

Δώσε πρόσβαση στο shared storage μόνο όταν τη χρειάζεσαι. Κράτησε scripts και repositories κάτω από `$HOME` όπου γίνεται, επειδή το Android shared storage έχει διαφορετική συμπεριφορά permissions/filesystem.

## Χρήσιμοι έλεγχοι

```bash
pwd
whoami
uname -a
python --version
git --version
ss -lnt
```

## Python

Για projects με τρίτα packages χρησιμοποίησε virtual environment:

```bash
python -m venv ~/venvs/lab
source ~/venvs/lab/bin/activate
```

Το `Hacking Guide Project.py` χρησιμοποιεί μόνο Python standard library.

## SSH

Χρησιμοποίησε SSH μόνο σε συστήματα που σου ανήκουν ή διαχειρίζεσαι. Δημιούργησε ξεχωριστό key, προστάτευσε το private key και μην το αντιγράφεις σε shared storage.

## Τοπικά labs

Προτίμησε `127.0.0.1`/localhost, local files και δικές σου test συσκευές. Το Android μπορεί να αναστείλει background processes, άρα battery optimization και app lifecycle επηρεάζουν long-running services.

## Σειρά troubleshooting

Έλεγξε path → permissions → package availability → Python environment → port/listener → Android restrictions → logs. Άλλαζε μία μεταβλητή κάθε φορά.
