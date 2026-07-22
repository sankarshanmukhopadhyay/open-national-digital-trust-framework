---
layout: default
title: Selective Disclosure and Unlinkability
parent: Privacy
nav_order: 2
grand_parent: Open National Digital Trust Framework
---


# Selective disclosure and unlinkability

A verifier SHOULD receive only the attributes or predicates necessary for its declared decision. Implementations SHOULD support presentation mechanisms that reduce unnecessary disclosure and correlation where the assurance objective permits.

```mermaid
flowchart LR
  C[Credential or evidence source] --> P[Holder-controlled presentation]
  P --> M[Minimum attributes or predicates]
  M --> V[Verifier]
  V --> D[Decision]
  I[Pairwise or context-specific identifiers] -. reduce correlation .-> P
```

Unlinkability is not absolute. Network metadata, timing, rare attributes, status endpoints, wallet attestation, and repeated identifiers can reintroduce correlation. Profiles SHALL document residual linkability and the parties capable of performing it.
