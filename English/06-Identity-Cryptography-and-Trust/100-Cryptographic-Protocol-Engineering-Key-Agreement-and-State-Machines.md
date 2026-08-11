# Cryptographic Protocol Engineering, Key Agreement and State Machines

Strong primitives can still produce an insecure protocol if identities, transcript binding, nonces, key separation, error handling, or state transitions are wrong. This module teaches how to reason about cryptographic protocols as authenticated state machines.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, or lab environments you own or are explicitly authorized to test. The exercises in this module are designed to prove security properties without targeting third parties.

## Learning objectives

By the end of this module you should be able to:

- Explain **Security goals** and connect it to a concrete trust boundary or security invariant.
- Explain **Key agreement** and connect it to a concrete trust boundary or security invariant.
- Explain **Transcript binding** and connect it to a concrete trust boundary or security invariant.
- Explain **Nonces and sequence numbers** and connect it to a concrete trust boundary or security invariant.
- Explain **Key derivation** and connect it to a concrete trust boundary or security invariant.
- Explain **Algorithm agility** and connect it to a concrete trust boundary or security invariant.

## Analysis method

Use the shared [Study Method](../Guides/STUDY-METHOD.md). For this module, first draw the relevant components and state transitions, then state one security invariant and identify the minimum evidence needed to test it safely.

## Deep concepts

### 1. Security goals

Write goals before algorithms: confidentiality, integrity, peer authentication, forward secrecy, replay resistance, channel binding, deniability, key confirmation, or post-compromise properties. Different protocols need different combinations.



### 2. Key agreement

Key exchange establishes shared secret material but does not automatically authenticate peers. Authentication must bind identities/credentials to the transcript and agreed parameters.



### 3. Transcript binding

Security-critical negotiation should be included in authenticated transcript data so an intermediary cannot alter algorithms, identities, roles, or context without detection.



### 4. Nonces and sequence numbers

Fresh unpredictable nonces or monotonic sequence state prevent reuse/replay depending on the construction. Define uniqueness requirements precisely; “random-looking” is not the same as guaranteed unique.



### 5. Key derivation

Use a KDF to derive independent keys for different directions and purposes. Domain separation prevents one key/context from being accidentally reused for encryption, authentication, export, or another protocol.



### 6. Algorithm agility

Negotiation can enable migration but also creates downgrade risk. The protocol must authenticate the negotiation and have policy for removing obsolete algorithms.



### 7. Error handling

Different errors, timing, retry behavior, and partial state can leak information. Protocols should define failure states, cleanup, retry limits, and whether an error is safe to reveal.



### 8. Formal and empirical validation

Threat modeling, test vectors, interoperability tests, negative tests, state-machine fuzzing, and formal methods can complement code review. Cryptographic protocol design should be independently reviewed rather than invented casually.



## Review focus

Apply the failure-mode taxonomy in [Study Method](../Guides/STUDY-METHOD.md), but keep the analysis specific to this lesson: identify the principal, resource, authority, mutable state, parser or policy boundary, and the telemetry that would distinguish a real control failure from misconfiguration or an observation gap.

## Authorized exercises

### Exercise 1 — Design a toy authenticated message protocol on paper and identify where identities, roles, nonces, sequence numbers, and transcript data are bound

Design a toy authenticated message protocol on paper and identify where identities, roles, nonces, sequence numbers, and transcript data are bound.


### Exercise 2 — Create negative test cases for replay, reordered messages, algorithm downgrade, expired credentials, and duplicate session identifiers

Create negative test cases for replay, reordered messages, algorithm downgrade, expired credentials, and duplicate session identifiers.


### Exercise 3 — Compare “encrypted transport” with “end-to-end authenticated message” and list which intermediaries can still read or modify data in each model

Compare “encrypted transport” with “end-to-end authenticated message” and list which intermediaries can still read or modify data in each model.

Use the lab-record format in [Study Method](../Guides/STUDY-METHOD.md) for each exercise and keep all inputs synthetic or confined to the authorized lab.

## Knowledge checks

1. Explain the most important trust boundary in **Cryptographic Protocol Engineering, Key Agreement and State Machines** without naming a security tool.
2. Give one example where cryptographic or authentication success still does **not** imply authorization success.
3. Describe one stale-state or replay condition relevant to this module.
4. Identify one telemetry source that can support a strong conclusion and one blind spot it still leaves.
5. Explain how you would turn a discovered weakness into a regression test rather than a one-time finding.

## Guided study workflow

Use [Study Method](../Guides/STUDY-METHOD.md). Complete at least one authorized exercise, preserve the evidence that supports your conclusion, and explain the module's main trust boundary and failure modes in your own words before moving on.

### Continue with

Choose **Learning paths** from the main menu for an ordered specialization, or use **Search lessons** to follow a concept into related modules.
