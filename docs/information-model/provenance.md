---
layout: default
title: Provenance and Integrity
parent: Information Architecture
nav_order: 5
---

# Provenance and integrity

Provenance answers who created information, under what authority, from which sources, at what time and through which transformations.

## Minimum provenance chain

```mermaid
flowchart LR
  S[Authoritative source] --> C[Collection or observation]
  C --> T[Transformation]
  T --> A[Attestation or publication]
  A --> V[Verification]
  V --> D[Decision]
  D --> R[Receipt and audit]
```

A provenance record SHOULD include:

- producer and authority;
- source references;
- collection or observation time;
- transformation history;
- integrity protection;
- policy and purpose;
- current status and expiry;
- disclosure or derivation method;
- verification events material to a decision.

A valid signature does not prove that source data was accurate, lawfully obtained or semantically fit. Assurance must address those questions separately.
