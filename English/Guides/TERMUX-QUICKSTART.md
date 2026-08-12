# Termux Quick Start

Termux is a powerful Android userland for learning Linux, Python, Git, SSH and local networking. Treat it as an Android app with a Linux-like environment, not as a rooted desktop distribution.

## Initial setup

```bash
pkg update
pkg upgrade
pkg install python git openssh nano curl -y
termux-setup-storage
```

Grant storage permission only when you actually need shared storage. Keep code under `$HOME` when possible because Android shared storage has different permissions and filesystem behavior.

## Useful checks

```bash
pwd
whoami
uname -a
python --version
git --version
ss -lnt
```

## Python

Use virtual environments for projects that need third-party packages:

```bash
python -m venv ~/venvs/lab
source ~/venvs/lab/bin/activate
```

`Hacking Guide Project.py` itself needs only the Python standard library.

## SSH

Use SSH only with systems you own or administer. Generate a dedicated key, protect the private key and avoid copying secrets into shared storage.

## Local labs

Prefer `127.0.0.1`/localhost services, local files and your own test devices. Android may suspend background processes; battery optimization and app lifecycle can therefore affect long-running services.

## Troubleshooting order

Check path → permissions → package availability → Python environment → port/listener → Android storage/app restrictions → logs. Change one variable at a time so you know what fixed the problem.
