# Denial-of-Service Resilience and Resource-Exhaustion Testing

Denial of service (DoS) is any condition that prevents legitimate users from obtaining a required service. Causes include malicious traffic, software defects, dependency failure, capacity exhaustion, queue saturation, lock contention, storage pressure, and misconfiguration. Defensive engineering focuses on resilience and controlled capacity testing—not flooding third-party systems.

> **Authorized-use boundary:** Never generate high-volume or disruptive traffic toward public or shared systems. Perform load and resource-exhaustion tests only in isolated environments with explicit limits, monitoring, stop conditions, and owner approval.

## Learning objectives

- identify CPU, memory, connection, thread, queue, disk, and dependency bottlenecks;
- distinguish volumetric, protocol, and application-layer resource exhaustion;
- understand rate limiting, quotas, backpressure, timeouts, and circuit breakers;
- design safe capacity tests;
- collect evidence that separates attack traffic from ordinary failure;
- plan graceful degradation and recovery.

## Availability as a system property

Availability is affected by every dependency required to serve a request. A frontend can be healthy while its database connection pool is exhausted; a network can be reachable while a queue is full; an API can return quickly while an asynchronous worker backlog grows uncontrollably.

Map the full request path and identify bounded resources.

## Resource-exhaustion classes

### Compute

Expensive parsing, compression, regular expressions, cryptography, image processing, or poorly bounded algorithms can consume CPU.

### Memory

Unbounded request bodies, caches, queues, decompression, object retention, or too many concurrent sessions can exhaust memory.

### Connections and file descriptors

Servers have finite sockets, descriptors, worker threads, and connection-pool entries. Slow or abandoned clients can consume these resources even without high bandwidth.

### Storage and logs

Large uploads, runaway logs, temporary files, and database growth can fill storage. Logging every rejected request at excessive detail can itself become a resource problem.

### Dependencies

DNS, identity providers, databases, third-party APIs, cloud control planes, and message queues can become unavailable or slow. Timeouts and retry behavior determine whether a local failure remains local or cascades.

## Defensive controls

- per-identity and per-resource quotas;
- rate limits with appropriate burst handling;
- bounded request/body sizes;
- connection and execution timeouts;
- queue limits and backpressure;
- circuit breakers and retry budgets;
- caching where safe;
- autoscaling with cost limits;
- graceful degradation;
- upstream DDoS protection for Internet services;
- monitoring of saturation, latency, errors, and dropped work.

A rate limit without identity context can punish many legitimate users behind one NAT or fail to stop distributed abuse. Choose the key carefully.

## Safe load testing

A capacity test needs:

1. isolated or dedicated environment;
2. explicit maximum request rate and concurrency;
3. baseline measurements;
4. telemetry for CPU, memory, connections, queue depth, latency, and errors;
5. automatic stop conditions;
6. rollback/recovery plan;
7. owner present or reachable during the test.

Use a normal load-testing framework in your lab and increase load gradually. The objective is to find the knee of the curve and verify controls, not to make the system fail as violently as possible.

## Detection

Useful signals include sudden changes in request rate, unique source/identity distribution, endpoint mix, error rate, queue depth, connection states, CPU/memory saturation, cache hit ratio, and dependency latency.

Do not label every traffic spike as malicious. Product launches, software updates, backup jobs, or misbehaving clients can produce similar symptoms.

## Recovery

Resilience includes the ability to shed load, protect critical functions, restore dependencies, clear backlogs safely, and verify data consistency after pressure is removed.

## Common mistakes

- Testing production without explicit limits.
- Measuring only requests per second.
- Ignoring dependency saturation and queues.
- Using retries without budgets or jitter.
- Logging so aggressively that the defense consumes the resource.
- Treating autoscaling as unlimited protection.

## Safe lab

Create a local service with a deliberately small worker or queue limit. Send a slowly increasing number of normal requests from the same device, staying within a low preset ceiling. Record latency, errors, and resource use. Add a simple rate limit or queue bound and compare behavior. Stop before the host becomes unstable.

## Knowledge check

1. Why can low-bandwidth traffic still create DoS conditions?
2. What is backpressure?
3. Why can retries make an outage worse?
4. Which measurements identify saturation before total failure?
5. What belongs in a safe load-test stop condition?

## Guided study workflow

Use the shared [Study Method](../Guides/STUDY-METHOD.md). Practice capacity reasoning with bounded localhost tests only.

### Continue with

Recommended next modules: **12, 48, 59, 91**.
