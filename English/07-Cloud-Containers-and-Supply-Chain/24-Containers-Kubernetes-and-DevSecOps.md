# Containers, Kubernetes, and DevSecOps

> **Purpose:** Secure build pipelines and cloud-native workloads by reducing privileges, protecting the control plane, and treating configuration as code.

## Container security model

Containers share a host kernel, so a container boundary is not identical to a VM boundary. Minimize images, avoid unnecessary root privileges, limit capabilities, use read-only filesystems where practical, and restrict network reachability.

### Image hygiene

Use maintained bases, remove unnecessary build tools from runtime images, pin images deliberately, scan for vulnerabilities/secrets, rebuild regularly, and keep release provenance.

## Kubernetes security areas

### Identity and RBAC

Use separate service accounts, grant only required verbs/resources, and avoid broad cluster-admin access.

### Workload isolation

Use security contexts, seccomp/AppArmor/SELinux where supported, resource limits, namespace boundaries, and network policies.

### Secrets

Kubernetes Secret objects are an API storage mechanism, not a complete secret-management strategy. Protect etcd, RBAC, backups, logs, and deployment pipelines.

### Admission and policy

Admission controls can reject privileged containers, dangerous host mounts, untrusted registries, or missing limits before runtime.

## DevSecOps controls

Use secret scanning, dependency/container scanning, tuned static analysis, IaC policy checks, authorization tests, protected release environments, short-lived CI identities, isolated runners, and controlled artifact promotion.

## Safe lab

Run a local static-page container, then switch to a non-root user and read-only filesystem. Document what functionality truly required write access or elevated privileges.

## Container image lifecycle

An image should have a clear owner, source repository, build definition, base-image policy, and update process. Prefer reproducible automated builds over manually modified running containers. Multi-stage builds can reduce runtime content by leaving compilers and package managers out of the final image.

### Runtime minimization

A smaller runtime reduces accidental exposure and makes behavior easier to understand. Remove shells or package managers only when the application does not require them; security controls should not break operability or incident response. Document the expected process tree, listening ports, writable paths, and outbound destinations for important workloads.

## Linux privilege controls

Containers can be constrained with several independent controls:

- run as a non-root UID/GID;
- prevent privilege escalation;
- drop unnecessary Linux capabilities;
- use seccomp profiles where supported;
- use AppArmor or SELinux confinement where available;
- mount the root filesystem read-only when feasible;
- provide narrowly scoped writable volumes;
- avoid host PID, IPC, or network namespaces unless required;
- avoid mounting sensitive host sockets or paths.

No single setting is a complete sandbox. The goal is layered reduction of what a compromised process can affect.

## Kubernetes control-plane security

The Kubernetes API is a central security boundary. Protect administrator credentials, restrict API exposure, use strong authentication, define RBAC deliberately, and monitor security-sensitive API operations. Backups and snapshots of cluster state can contain secrets and should receive the same protection as the live control plane.

### RBAC review

Review effective permissions rather than role names. Broad verbs such as `*`, broad resources, cluster-wide bindings, permission to create privileged workloads, and permission to read secrets deserve particular attention. Service accounts should map to actual workload needs, not a generic namespace-wide identity used by every application.

### Namespace design

Namespaces are useful organizational and policy boundaries but are not automatically strong tenant isolation. Combine them with RBAC, network policies, admission controls, quotas, and workload security policies. High-risk multi-tenant environments may need stronger isolation mechanisms beyond namespaces.

## Pod Security Standards

Kubernetes documents Pod Security Standards with three policy levels: **Privileged**, **Baseline**, and **Restricted**. Use these as a reference point for admission policy and workload review. The appropriate level depends on workload requirements, but exceptions should be explicit and documented rather than becoming the default.

## Network policy

Kubernetes networking is often permissive unless policy is added. Define which workloads need to communicate and implement ingress and egress restrictions appropriate to the network plugin and environment. DNS, telemetry, update repositories, identity endpoints, and external APIs should be considered explicitly so that egress policy remains usable.

## Secrets and configuration

A Kubernetes Secret is not automatically safe because the API object is named “Secret.” Protect access through RBAC, enable appropriate encryption-at-rest configuration, protect etcd and backups, avoid exposing secrets in environment dumps or logs, and prefer external secret-management integrations where they improve lifecycle control. Rotate secrets when ownership or exposure changes.

## Admission policy

Admission controls can enforce invariants before workloads enter the cluster. Examples include rejecting privileged pods, host namespace access, risky volume mounts, missing resource limits, unapproved registries, mutable image tags for production, or unsigned/unattested artifacts when your environment uses such verification.

Policy should include an exception workflow. Teams will otherwise bypass controls informally when legitimate edge cases arise.

## Observability for containers

Useful telemetry includes API audit logs, workload start/stop events, image identity, namespace, service account, node placement, network flows where available, admission denials, and runtime process/activity signals. Correlating a runtime event to the image digest and deployment revision improves incident response.

## DevSecOps pipeline architecture

Treat the delivery pipeline as production infrastructure. It can change what runs in production and often has access to secrets, registries, signing keys, or cloud deployment identities.

### Pipeline controls

- Require review for changes to build and deployment definitions.
- Separate untrusted contribution jobs from jobs with production credentials.
- Use ephemeral or well-isolated runners for sensitive builds.
- Prefer identity federation and short-lived credentials.
- Protect branch and release rules from unilateral bypass.
- Record artifact digests and deployment provenance.
- Scan for secrets before they reach shared history.
- Run dependency, container, and IaC checks with tuned policies rather than failing on every informational result.
- Require human approval for genuinely high-impact production actions where appropriate.

## Infrastructure as code

IaC makes configuration reviewable and repeatable, but it can also reproduce a mistake across every environment. Validate public exposure, IAM policy, encryption, logging, backup, network rules, and deletion protection before deployment. Keep emergency manual changes visible and reconcile them back into code to prevent long-term drift.

## Vulnerability management for images

An image scan is a starting point, not a risk decision. Consider whether the vulnerable package is present in the runtime image, reachable from the application, exposed to untrusted input, fixed upstream, and deployed on critical systems. Rebuild images regularly so patched base layers actually reach production.

## Safe Kubernetes lab

Use a local cluster such as kind, minikube, or another isolated training environment. Deploy a simple web application, then:

1. assign a dedicated service account;
2. run it as non-root;
3. disable privilege escalation;
4. drop unnecessary capabilities;
5. set CPU/memory requests and limits;
6. apply an ingress network policy;
7. inspect its effective RBAC permissions;
8. record the image digest;
9. enable an admission rule that blocks a deliberately non-compliant test manifest;
10. document each control and the failure mode it addresses.

The exercise should remain local and should not attempt container escape or cluster compromise.

## Primary references

- Kubernetes Pod Security Standards — https://kubernetes.io/docs/concepts/security/pod-security-standards/
- NIST Secure Software Development Framework — https://csrc.nist.gov/projects/ssdf

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md) for evidence quality, safe lab boundaries, note-taking, mastery criteria, and retesting. This module only adds the topic-specific preparation and exercise below.

### Before you begin

Modules 19, 22, and Linux basics.

### Practice task

Deploy a disposable local container, inventory image/source/dependencies, run it with minimal permissions, enable logs, and document how you would patch and roll back it.

Record the expected result before testing, change one variable at a time, and keep only sanitized evidence needed to support your conclusion.

### Mastery check

Explain the module’s main trust boundary, one realistic failure mode, the evidence that would confirm it, and the control that addresses the root cause.

### Continue with

Recommended next modules: **40, 41, 47, 49**.
