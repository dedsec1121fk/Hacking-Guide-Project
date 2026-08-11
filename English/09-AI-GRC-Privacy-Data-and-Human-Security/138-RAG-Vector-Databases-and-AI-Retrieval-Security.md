# RAG, Vector Databases and AI Retrieval Security

Retrieval-augmented generation introduces a new data and trust pipeline. Study ingestion, embeddings, chunking, metadata authorization, prompt-injection through documents, provenance and output grounding.

> **Authorized-use boundary:** Perform practical work only on systems, code, accounts, devices, captures, or lab environments you own or are explicitly authorized to test. Prefer localhost, synthetic data, disposable VMs/containers, prerecorded traces, and read-only analysis whenever possible.

## Learning objectives

By the end of this module you should be able to:

- Explain **RAG architecture and trust boundaries** and identify its most important trust boundary, state transition, and evidence source.
- Explain **document ingestion and parsing** and identify its most important trust boundary, state transition, and evidence source.
- Explain **chunking and embeddings** and identify its most important trust boundary, state transition, and evidence source.
- Explain **vector-store tenancy and authorization** and identify its most important trust boundary, state transition, and evidence source.
- Explain **retrieval-time metadata filters** and identify its most important trust boundary, state transition, and evidence source.
- Explain **indirect prompt injection** and identify its most important trust boundary, state transition, and evidence source.

## Analysis method

Use [Study Method](../Guides/STUDY-METHOD.md). Start by identifying ownership or identity, the state transition that can fail, and the evidence that would distinguish a real boundary violation from a diagnostic artifact.

## Deep concepts

### 1. RAG architecture and trust boundaries

Retrieval-Augmented Generation combines ingestion, storage/indexing, retrieval, prompt assembly, model execution, and output handling. Each step has different authority: retrieved text should be treated as untrusted data, not as instructions that automatically override application policy.

### 2. ingestion and parsing

Documents may contain active formats, malformed content, hidden text, metadata, or instructions designed for downstream models. Normalize and parse in a constrained pipeline, restrict supported formats, scan resource usage, and preserve source identity/provenance.

### 3. chunking and embeddings

Chunk size, overlap, metadata, and embedding model affect what content is retrievable and how boundaries are preserved. Security-sensitive labels such as tenant, classification, and source should remain explicit metadata rather than being inferred only from semantic similarity.

### 4. tenancy and authorization

Vector similarity is not authorization. Filter candidate content using server-side tenant/resource permissions before it can enter the model context, and test with two synthetic tenants to ensure nearest-neighbor results cannot cross access boundaries.

### 5. metadata filters

Metadata filters must be constructed from trusted application state and validated by the storage layer. Avoid letting a model or client generate arbitrary filters that broaden tenant, confidentiality, or document-state constraints.

### 6. indirect prompt injection

Retrieved content can contain text that attempts to manipulate the model or connected tools. Separate instructions from data, constrain tool permissions, label provenance, apply deterministic authorization outside the model, and assume untrusted documents may contain adversarial instructions.

### 7. source provenance and citations

Store document identity, version, ingestion time, owner/tenant, classification, and source location so an answer can be traced back to evidence. Citations help auditability but should be generated from the actual retrieved source set, not invented by the model.

### 8. poisoning, deletion and reindexing

A poisoned or outdated document can remain in embeddings after the source changes. Define authenticated ingestion, review, deletion propagation, reindexing, version rollback, and incident procedures that can identify which answers were influenced by a bad corpus version.

## Engineering focus

For this module, convert each important claim into a security invariant and a regression test. Prefer controls that remove unnecessary authority, make state transitions explicit, bound resource use, and leave enough telemetry to explain a failure. The reusable evidence and lab-record format is in [Study Method](../Guides/STUDY-METHOD.md).

## Authorized lab sequence

### Lab 1 — Build a local toy RAG design on paper with public/sample documents and annotate trust boundaries.



### Lab 2 — Create synthetic “malicious instruction inside a document” examples and write expected safe model behavior without connecting external tools.



### Lab 3 — Design metadata filters for two fictional tenants and test access decisions with a table of allowed/denied retrievals.

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

Recommended related modules: **022, 025, 041, 046, 057, 071, 114**. From the main menu, choose **Search lessons** to find related sections across the full guide.
