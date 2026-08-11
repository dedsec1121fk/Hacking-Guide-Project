# Cryptography

Cryptography provides tools for confidentiality, integrity, authenticity, key establishment, and verifiable data origin. Security depends not only on choosing a strong algorithm but also on protocol design, key lifecycle, randomness, implementation, identity binding, error handling, and operational recovery.

> **Authorized-use boundary:** Use cryptographic exercises with your own keys and synthetic data. Do not attempt to recover other people's credentials, decrypt data you are not authorized to access, or weaken real systems for experimentation.

## Learning objectives

- distinguish encryption, hashing, MACs, signatures, and key derivation;
- understand symmetric and asymmetric key roles;
- reason about nonces, IVs, salts, randomness, and replay protection;
- understand certificates, trust anchors, revocation, and key rotation;
- recognize common implementation and protocol-design mistakes;
- plan for cryptographic agility and post-quantum migration.

## Security goals

**Confidentiality** limits who can read data. **Integrity** detects unauthorized modification. **Authenticity** gives evidence about an identity or key that produced a message. **Non-repudiation** is a broader legal/operational claim and should not be assumed merely because a digital signature exists.

Cryptography does not decide authorization. A perfectly valid signature can authorize the wrong action if application policy binds it to the wrong tenant, resource, audience, or workflow state.

## Symmetric encryption

Symmetric algorithms use a shared secret key and are efficient for bulk data. Modern systems should normally use an authenticated-encryption construction so confidentiality and integrity are handled together. Key reuse, nonce/IV misuse, insecure modes, or failure to authenticate metadata can undermine an otherwise strong primitive.

## Hash functions and passwords

Cryptographic hashes provide fixed-size digests and are useful for integrity, identifiers, and protocol constructions. Password storage is different: passwords are low-entropy human secrets and should use a dedicated password-hashing/KDF design with a unique salt and suitable work parameters. A plain fast hash is not an adequate password-storage scheme.

## Message authentication codes

A MAC proves that a party possessing the shared key produced or authenticated a message. It does not provide public verifiability like a digital signature. Protocols must define exactly which fields are authenticated and how messages are encoded before the MAC is calculated.

## Public-key cryptography and signatures

Asymmetric systems use mathematically related public/private keys for key establishment, signatures, or encryption depending on the scheme. Private keys require strong access control and lifecycle management. Signature verification should validate the intended algorithm, key, context, and message representation—not just return a boolean result disconnected from policy.

## Randomness, nonces and salts

Random keys require a cryptographically secure source. A **nonce** generally needs uniqueness within the protocol's rules; an **IV** has algorithm-specific requirements; a **salt** makes otherwise identical password/hash inputs produce different derived values. These terms are not interchangeable.

## Key lifecycle

Map generation, storage, distribution, activation, use, rotation, revocation, backup, recovery, archival, and destruction. The security of data encrypted for years depends on whether the organization can protect and recover keys throughout that period without granting excessive access.

## PKI and certificates

Certificates bind public keys to identities or names under a trust model. Validation may involve chain building, hostname/identity checks, validity periods, key usage, policy, revocation strategy, and trust-store management. TLS protects a connection only if both endpoints interpret identity and authorization correctly.

## Common cryptographic failures

- inventing a custom cipher or protocol without expert review;
- nonce/IV reuse where uniqueness is required;
- keys embedded in source code or public client applications;
- encryption without integrity/authentication;
- accepting any certificate or disabling verification;
- storing passwords with a fast unsalted hash;
- using long-lived keys without rotation/revocation planning;
- logging plaintext secrets or key material.

## Cryptographic agility and post-quantum planning

Long-lived systems should know which algorithms and keys they depend on and be able to change them without redesigning the entire application. Post-quantum migration is primarily an inventory, dependency, interoperability, testing, and lifecycle problem: identify where vulnerable public-key algorithms are used, prioritize long-lived sensitive data, test standardized replacements in controlled environments, and avoid unreviewed home-grown hybrid designs.

## Safe lab

With synthetic text, create a small local program that hashes a file, computes a MAC with a temporary lab key, and performs authenticated encryption using a well-maintained library. Change one byte of the ciphertext or authenticated data and observe verification failure. Record which property each primitive provides and which key/state must remain protected.

## Knowledge check

1. Why is encryption alone not the same as authenticated encryption?
2. Why are salts, nonces, and IVs different concepts?
3. Why is a fast hash unsuitable for password storage?
4. What does certificate validation need beyond checking a signature?
5. Why is cryptographic agility an architectural property?

## Guided study workflow

Use [Study Method](../Guides/STUDY-METHOD.md). For each primitive, write the security property, required secret/public state, misuse conditions, lifecycle requirements, and evidence that would demonstrate correct use.

### Continue with

Recommended next modules: **39, 49, 78, 100, 101, 102, 103, 131, 132**. From the main menu, use **Search lessons** for a specific cryptographic primitive or protocol.
