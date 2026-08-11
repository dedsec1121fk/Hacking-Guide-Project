# Package Managers, Registries, Dependency and Ecosystem Security

Dependency risk is an ecosystem problem involving names, versions, maintainers, registries, resolver behavior, lockfiles, mirrors, build scripts, and transitive trust. This module focuses on how to control dependency introduction and detect suspicious changes.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, or lab environments you own or are explicitly authorized to test. The exercises in this module are designed to prove security properties without targeting third parties.

## Learning objectives

By the end of this module you should be able to:

- Explain **Name and namespace trust** and connect it to a concrete trust boundary or security invariant.
- Explain **Semantic versioning limits** and connect it to a concrete trust boundary or security invariant.
- Explain **Lockfiles** and connect it to a concrete trust boundary or security invariant.
- Explain **Install/build scripts** and connect it to a concrete trust boundary or security invariant.
- Explain **Transitive dependencies** and connect it to a concrete trust boundary or security invariant.
- Explain **Maintainer and release trust** and connect it to a concrete trust boundary or security invariant.

## Analysis method

Use the shared [Study Method](../Guides/STUDY-METHOD.md). For this module, first draw the relevant components and state transitions, then state one security invariant and identify the minimum evidence needed to test it safely.

## Deep concepts

### 1. Name and namespace trust

Typosquatting, namespace confusion, abandoned packages, and internal/public name collisions can redirect developers to unintended code. Reserve important names and define registry precedence.



### 2. Semantic versioning limits

Version ranges express compatibility intent, not security trust. A syntactically compatible update can still add risky behavior. Know when production builds are pinned and when updates are deliberately refreshed.



### 3. Lockfiles

Lockfiles make resolved dependency graphs more reproducible, but their integrity and review matter. They should change for explainable reasons and be included in code review.



### 4. Install/build scripts

Package lifecycle hooks and native builds may execute code during installation. Treat dependency installation as code execution, especially in CI and developer environments.



### 5. Transitive dependencies

Most projects depend on far more packages than are listed directly. Generate an SBOM/dependency graph, identify critical/transitively privileged packages, and reduce unnecessary depth.



### 6. Maintainer and release trust

Protect maintainer accounts, use strong MFA, separate release authority, monitor ownership changes, and verify release automation. Package metadata alone does not prove source provenance.



### 7. Mirrors and proxies

Internal registries can enforce allowlists, caching, provenance, scanning, and namespace policy. They also become high-impact infrastructure that requires backup, access control, and monitoring.



### 8. Response

When a dependency is compromised, identify affected versions, where they were built/deployed, what execution privileges they had, and whether credentials or build artifacts need rotation/rebuild—not just a version bump.



## Review focus

Apply the failure-mode taxonomy in [Study Method](../Guides/STUDY-METHOD.md), but keep the analysis specific to this lesson: identify the principal, resource, authority, mutable state, parser or policy boundary, and the telemetry that would distinguish a real control failure from misconfiguration or an observation gap.

## Authorized exercises

### Exercise 1 — Create a dependency inventory for a small harmless Python project and classify direct vs transitive packages

Create a dependency inventory for a small harmless Python project and classify direct vs transitive packages.


### Exercise 2 — Compare reproducibility with and without a lockfile or fully pinned requirements in an isolated virtual environment

Compare reproducibility with and without a lockfile or fully pinned requirements in an isolated virtual environment.


### Exercise 3 — Write an incident checklist for a compromised package version: identify exposure, builds, credentials, artifacts, and verification steps

Write an incident checklist for a compromised package version: identify exposure, builds, credentials, artifacts, and verification steps.

Use the lab-record format in [Study Method](../Guides/STUDY-METHOD.md) for each exercise and keep all inputs synthetic or confined to the authorized lab.

## Knowledge checks

1. Explain the most important trust boundary in **Package Managers, Registries, Dependency and Ecosystem Security** without naming a security tool.
2. Give one example where cryptographic or authentication success still does **not** imply authorization success.
3. Describe one stale-state or replay condition relevant to this module.
4. Identify one telemetry source that can support a strong conclusion and one blind spot it still leaves.
5. Explain how you would turn a discovered weakness into a regression test rather than a one-time finding.

## Guided study workflow

Use [Study Method](../Guides/STUDY-METHOD.md). Complete at least one authorized exercise, preserve the evidence that supports your conclusion, and explain the module's main trust boundary and failure modes in your own words before moving on.

### Continue with

Choose **Learning paths** from the main menu for an ordered specialization, or use **Search lessons** to follow a concept into related modules.
