# Container and Kubernetes Isolation Internals

> **Purpose:** Move from basic container security into runtime internals, workload identity, Kubernetes authorization, pod security boundaries, and cluster-level blast-radius reasoning.

## Learning objectives

- Explain how container runtime isolation is assembled from Linux primitives.
- Understand Kubernetes API authentication, authorization, admission, controllers, and workload identity.
- Identify dangerous pod/runtime configuration without attempting container escape.
- Reason about service accounts, RBAC, secrets, network policy, admission, and node trust.
- Design safe cluster validation tests.

## Container boundary recap

A container is a process isolated by namespaces and constrained using capabilities, cgroups, seccomp/LSM policy, filesystem mounts, and runtime configuration. It shares the host kernel. Therefore, a container boundary depends on both runtime configuration and kernel correctness.

The highest-risk configurations intentionally remove isolation: privileged mode, host PID/network namespaces, broad host mounts, device access, excessive capabilities, or access to the runtime socket.

## Kubernetes control plane

Kubernetes adds an orchestration/control plane around workloads. Major security-relevant components include:

- API server;
- authentication mechanisms;
- RBAC/authorization;
- admission control;
- controllers;
- scheduler;
- kubelet/node agents;
- etcd/state storage;
- cluster networking;
- workload/service-account identity.

The API server is the central policy gateway for desired-state changes.

## Authentication and authorization

Kubernetes can authenticate users and workloads through several mechanisms. After authentication, authorization—commonly RBAC—determines whether a subject may perform a verb on a resource within a scope.

RBAC is powerful because permissions can create other permissions. A role that can create pods may indirectly gain access to service-account tokens, mounted secrets, or node capabilities depending on cluster policy. Analyze effective privilege, not only role names.

## Service accounts

Pods often run with a Kubernetes service account. Tokens should have only the API permissions the workload requires. Modern projected service-account tokens are audience/lifetime bounded compared with historical long-lived token patterns.

Disable automatic token mounting for workloads that do not call the Kubernetes API.

## Admission control

Admission controllers evaluate API objects after authentication/authorization but before persistence. They can enforce pod security, image policy, required labels, allowed registries, resource limits, signature checks, or organization-specific invariants.

Authorization answers “may this caller create a pod?” Admission can answer “is this pod specification acceptable?”

## Pod security settings

Review workloads for:

- non-root user;
- no privilege escalation;
- minimal/drop capabilities;
- read-only root filesystem where feasible;
- seccomp profile;
- SELinux/AppArmor policy where available;
- no privileged mode;
- no host namespaces unless required;
- no broad hostPath mounts;
- controlled device access;
- resource limits.

These settings constrain the consequences of a compromised application.

## Secrets

Kubernetes Secrets are API objects, not a magical hardware vault. Access depends on RBAC, etcd encryption/configuration, node/pod exposure, and external secret integration. A pod that can read a secret effectively possesses it during runtime.

Prefer workload identity and short-lived credentials where services support them.

## Network policy

By default, many clusters allow broad pod-to-pod communication unless a network plugin/policy restricts it. NetworkPolicy can define allowed ingress/egress at workload labels/namespaces depending on implementation.

Segmentation reduces lateral reach but does not replace application authentication.

## Node trust

A node runs many pods and interacts with the control plane. Node compromise can affect workloads scheduled there and potentially credentials/tokens available to that node. Protect kubelet interfaces, node credentials, host OS, runtime, kernel, and cloud instance permissions.

Separate highly sensitive workloads where stronger isolation is required; consider sandboxed runtimes or VM-based isolation for specific threat models.

## Runtime socket risk

Access to a container runtime management socket can grant extremely broad control over host workloads. Do not mount runtime sockets into ordinary application containers merely for convenience. If an automation component truly needs runtime management, isolate and constrain it as privileged infrastructure.

## Image supply chain

Images should have known provenance, minimal content, pinned dependencies, vulnerability scanning, signature/attestation where appropriate, and reproducible build metadata. Runtime policy should complement CI controls.

Avoid mutable tags for security-critical deployment decisions when immutable digests are available.

## Kubernetes audit telemetry

API audit logs can show who requested which resource operation, from where, and with what result, depending on policy. Combine them with workload, node, cloud, admission, and network telemetry for investigation.

A detection should identify a meaningful behavior, such as unexpected privileged pod creation, broad RBAC changes, secret access anomalies, or service-account use from unusual contexts.

## Safe cluster lab

Use a disposable local cluster such as a VM-based or development cluster. Create two namespaces and synthetic service accounts. Grant one account read-only access to ConfigMaps in its namespace. Verify allowed and denied API operations using supported administrative tooling.

Then deploy a benign pod with deliberately weak security settings, inspect why policy allows it, and tighten an admission/pod security configuration. Do not attempt node/container escape.

## Attack-path reasoning

A cluster privilege graph can include:

`service account → RBAC create pods → pod can use stronger service account → access to namespace secret → cloud credential → external resource`.

The correct remediation can be at any edge: reduce RBAC, block service-account selection, remove secret, use workload identity, constrain network/cloud IAM, or isolate workloads.

## Guided study workflow

### Before you begin

Complete Modules 19, 21, 24, 41, 49, 74, and 76 when available.

### Practice task

Build a Kubernetes privilege graph for a tiny local cluster: users, service accounts, roles, role bindings, namespaces, secrets, pods, nodes, and external identity. Remove one unnecessary privilege edge and verify denial.

### Evidence to keep

RBAC manifests, pod security settings, denied/allowed API evidence, privilege graph, and audit excerpt if enabled.

### Common mistakes to avoid

- assuming RBAC names imply actual privilege;
- granting cluster-admin to fix deployment problems;
- mounting runtime sockets casually;
- treating Secrets as automatically encrypted from every threat;
- attempting escape techniques instead of proving dangerous configuration through policy evidence.

### Mastery check

Explain how Kubernetes authorization and Linux isolation combine, then trace one hypothetical workload-to-cloud attack path and identify controls at each edge.

### Continue with

Modules **76, 80, 81, and 85**.
