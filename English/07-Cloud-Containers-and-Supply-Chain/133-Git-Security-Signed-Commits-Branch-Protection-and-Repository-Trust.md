# Git Security, Signed Commits, Branch Protection and Repository Trust

Source control is part of the software trust chain. Study identity, review policy, signed objects, protected branches, secrets exposure, dependency changes and repository recovery.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, captures, or lab environments you own or are explicitly authorized to test. Prefer localhost, synthetic data, disposable VMs/containers, prerecorded traces, and read-only analysis whenever possible.

## Learning objectives

By the end of this module you should be able to:

- Explain **Git object integrity and hashes** and identify its most important trust boundary, state transition, and evidence source.
- Explain **commit/tag signatures** and identify its most important trust boundary, state transition, and evidence source.
- Explain **branch protection and required reviews** and identify its most important trust boundary, state transition, and evidence source.
- Explain **CODEOWNERS-style approval concepts** and identify its most important trust boundary, state transition, and evidence source.
- Explain **force pushes and history rewriting** and identify its most important trust boundary, state transition, and evidence source.
- Explain **secret exposure and rotation** and identify its most important trust boundary, state transition, and evidence source.

## Analysis method

Use [Study Method](../Guides/STUDY-METHOD.md). Start by identifying ownership or identity, the state transition that can fail, and the evidence that would distinguish a real boundary violation from a diagnostic artifact.

## Deep concepts

### 1. Git object integrity and hashes

Git addresses objects by cryptographic hashes and links commits into a content history, which helps detect accidental or unauthorized modification. Repository integrity still depends on trusted refs, hosting controls, signatures where required, and protecting the identities allowed to update branches/tags.

### 2. commit and tag signatures

Signed commits or tags can attest that a key approved specific history, but verification needs trusted key ownership and policy. Decide which events must be signed, how keys are enrolled/revoked, and what CI does when a signature is missing or invalid.

### 3. branch protection and reviews

Protected branches should require review, status checks, restricted force pushes, and controlled merge paths according to risk. Review policy must cover automation/bots and administrative bypasses; an emergency override should be visible and followed by retrospective review.

### 4. CODEOWNERS and approval paths

CODEOWNERS can route changes in sensitive directories to appropriate reviewers. Treat it as workflow assistance, not a complete authorization boundary: protect the ownership file itself and enforce required approvals through repository policy.

### 5. force pushes and history rewrite

History rewriting can remove or replace commits referenced by collaborators or releases. Restrict force pushes on protected refs, retain server/audit history, and distinguish cleanup of accidental secrets from an attempt to hide unauthorized changes.

### 6. secret exposure and rotation

Deleting a secret from the latest commit does not revoke copies already cloned, cached, logged, or indexed. Revoke/rotate the credential first, assess usage, then clean history only if policy requires it and coordinate the rewrite carefully.

### 7. submodules and dependency refs

Submodules and other pinned repository references extend trust to another repository/object. Pin immutable reviewed revisions, validate ownership/provenance, and prevent an untrusted dependency location from changing what privileged build automation fetches.

### 8. backup, mirroring and recovery

Repository resilience includes remote mirrors, protected release artifacts, issue/metadata backups where needed, and tested restoration. Recovery should preserve evidence of unauthorized ref changes while allowing teams to re-establish known-good branches and tags.

## Engineering focus

For this module, convert each important claim into a security invariant and a regression test. Prefer controls that remove unnecessary authority, make state transitions explicit, bound resource use, and leave enough telemetry to explain a failure. The reusable evidence and lab-record format is in [Study Method](../Guides/STUDY-METHOD.md).

## Authorized lab sequence

### Lab 1 — Create a throwaway local repository, sign a test tag if you have a test key, and document verification outcomes.



### Lab 2 — Design branch-protection rules for a critical library versus a personal experiment.



### Lab 3 — Simulate accidental placement of a fake secret string and practice safe history cleanup plus “rotate the real secret” reasoning.

For every lab, use only owned/synthetic inputs and record objective, scope, version, expected behavior, observed evidence, cleanup, remediation, and regression result as described in [Study Method](../Guides/STUDY-METHOD.md).

## Knowledge checks

Answer these without looking at the notes:

1. What is the primary trust boundary in this topic?
2. Which state or identity transition is easiest to misunderstand?
3. What observation would disprove your first hypothesis?
4. Which control removes authority rather than merely adding detection?
5. How would you reproduce the behavior safely after remediation?

## Guided study workflow

Complete at least one authorized lab and explain the mechanism, trust boundary, failure state, evidence, and defensive fix in your own words. Use **Bookmarks**, **Progress**, and **Learning paths** in the numbered menu instead of memorizing command-line flags.

## Next modules

Recommended related modules: **022, 029, 040, 084, 097, 098, 109**. From the main menu, choose **Search lessons** to find related sections across the full guide.
