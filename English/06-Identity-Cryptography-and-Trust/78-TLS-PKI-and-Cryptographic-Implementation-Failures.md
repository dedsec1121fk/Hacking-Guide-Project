# TLS, PKI and Cryptographic Implementation Failures

> **Purpose:** Move from cryptographic primitives into real protocol assurance: identity, key exchange, certificate validation, downgrade resistance, nonce discipline, and implementation mistakes.

## Learning objectives

- Explain the security goals of modern TLS at a practical protocol level.
- Understand certificate chains, hostname validation, revocation limitations, and trust stores.
- Distinguish algorithm weakness from implementation/protocol misuse.
- Recognize nonce reuse, insecure randomness, key lifecycle, and side-channel concepts.
- Validate a localhost TLS deployment safely.

## Cryptography is a system, not an algorithm

Using AES or a modern elliptic curve does not automatically create a secure system. Security depends on mode, nonce generation, key derivation, certificate validation, protocol transcript binding, random number quality, key storage, error handling, and implementation behavior.

The most important rule is to use mature, reviewed protocol libraries rather than inventing cryptographic protocols.

## TLS goals

Modern TLS aims to provide confidentiality and integrity for a connection plus authentication of the server and optionally the client. TLS 1.3 simplifies the handshake and removes many legacy constructions, but configuration and certificate identity still matter.

A successful encrypted handshake to the wrong endpoint is not secure if certificate/hostname validation is disabled.

## Certificate chain

A server certificate is typically validated through one or more intermediate CAs to a trust anchor in the client's trust store. Validation includes signatures, validity periods, constraints, key usage, name constraints where applicable, and server-name identity.

The chain that a server sends and the trust anchor that a client already trusts are separate concepts.

## Hostname validation

Clients must verify that the certificate identity matches the intended DNS name according to current platform rules. Accepting any valid certificate regardless of name defeats server authentication.

Development environments sometimes disable verification to “make it work”; that habit must not leak into production code.

## Private PKI

Organizations may operate private CAs for internal services. Root keys are extremely sensitive and should be protected offline or in dedicated key-management/HSM infrastructure depending on risk. Intermediate CAs reduce direct root exposure.

Certificate issuance policy should bind identities to authorized subjects and support rotation/revocation processes.

## Forward secrecy

Ephemeral key exchange means compromise of a long-term server key does not automatically decrypt previously captured sessions. Modern TLS configurations use ephemeral key-agreement mechanisms to provide forward secrecy.

This property depends on protocol/version/cipher choices and correct implementation.

## Nonces and AEAD

Authenticated-encryption modes such as AES-GCM or ChaCha20-Poly1305 combine confidentiality and integrity but require correct nonce use. Reusing a nonce with the same key can catastrophically break security properties for some modes.

Applications should rely on high-level library APIs that manage nonce generation/counters safely and should never truncate authentication tags without a protocol design that explicitly justifies it.

## Randomness

Cryptographic keys, nonces, salts, tokens, and challenges need appropriate randomness. Use the OS cryptographic random generator through a secure library. Language-level pseudorandom functions intended for simulation/games are not necessarily suitable for secrets.

Entropy problems at device boot or embedded systems deserve special review.

## Password storage

Passwords should be processed with dedicated password-hashing/KDF algorithms using unique salts and appropriate cost parameters. A fast generic hash such as raw SHA-256 is not a password-storage design.

Pepper can add a separately protected secret layer in some architectures, but it complicates rotation/recovery and does not replace strong password hashing.

## Key derivation

Key Derivation Functions convert secret material into one or more cryptographic keys with domain separation/context. Reusing one raw key for unrelated purposes increases cross-protocol risk. Mature protocols derive separate traffic/exporter keys from a handshake secret.

## Downgrade resistance

Protocol negotiation must prevent an attacker from forcing both sides onto a weaker mutually supported option. Modern TLS removed many legacy modes and binds negotiation into authenticated transcript state.

Operationally, disable obsolete protocol versions/ciphers rather than relying solely on clients to choose the strongest option.

## Certificate revocation reality

Revocation mechanisms include CRLs and OCSP, while browsers/platforms use additional mechanisms and policies. Real-world revocation is complex because availability/privacy/performance interact. Short certificate lifetimes and automated renewal reduce reliance on emergency revocation for ordinary operation.

Understand your platform rather than assuming every client performs real-time OCSP checks.

## Side channels

An implementation can leak secrets through timing, cache behavior, power consumption, electromagnetic emissions, branch behavior, or error distinctions. Constant-time cryptographic libraries reduce selected timing risks.

Do not attempt side-channel attacks on devices you do not own. For a software lab, compare why secret-dependent branches are discouraged in cryptographic code.

## Padding and error oracles

Historic protocol failures have occurred when error behavior reveals whether decrypted structure or padding is valid. The deep lesson is that error channels can leak one bit at a time and turn a cryptographic check into an oracle.

Use modern AEAD protocols/libraries and uniform failure behavior rather than implementing custom CBC/padding schemes.

## Key lifecycle

Every key has generation, activation, storage, use, rotation, backup, revocation, recovery, and destruction stages. Most key-management failures are lifecycle failures, not broken math.

Document which principal/system can retrieve plaintext keys and which can only request cryptographic operations.

## Safe localhost TLS lab

Create a self-signed **lab** CA and a localhost certificate only if you understand the trust implications. Prefer a disposable browser/profile or command-line client configured to trust only that temporary CA. Observe successful validation, then demonstrate that a hostname mismatch is correctly rejected.

Delete the test trust anchor afterward so it cannot accidentally become a persistent trust expansion.

## Guided study workflow

### Before you begin

Complete Modules 20, 39, 49, 51, 52, and 77.

### Practice task

Document one local TLS handshake: endpoint identity, certificate chain, protocol version, key-exchange properties, and validation result. Test one expected failure such as wrong hostname.

### Evidence to keep

Temporary certificate metadata, sanitized client output, trust-chain diagram, and cleanup note confirming the temporary CA was removed.

### Common mistakes to avoid

- disabling certificate verification permanently;
- confusing encryption with authenticated identity;
- using generic hashes for password storage;
- reusing keys/nonces across contexts;
- inventing custom crypto protocols.

### Mastery check

Explain why a strong cipher with broken certificate validation is insecure and why nonce/key lifecycle can matter more than algorithm name.

### Continue with

Modules **79, 82, 83, and 84**.
