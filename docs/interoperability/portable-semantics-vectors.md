---
layout: default
title: Portable Semantics Vectors
parent: Interoperability and Recognition
nav_order: 4
---

# Portable semantics vectors

ONDTF portability means independently developed profiles can choose different technologies and operating arrangements while still exposing where their semantics differ. It does **not** mean that different profiles should be assumed behaviorally equivalent.

`PSV-001` provides common vectors for authority, delegation, evidence freshness, suspension, revocation and remedy. Each profile records its observed outcome and any divergence from the ONDTF invariant.

| Semantic | Core invariant |
|---|---|
| Authority | Valid identity alone does not establish authority. |
| Delegation | Delegation cannot widen the principal's authority. |
| Evidence freshness | Stale consequential evidence is surfaced and explicitly dispositioned. |
| Suspension | Suspension has an effective operational consequence. |
| Revocation | Cached permission cannot silently override current revocation state. |
| Remedy | A remedy is incomplete if the consequential state remains unchanged. |

A profile may differ in implementation or disposition, but the divergence and rationale must be declared. This preserves implementation neutrality without creating false semantic equivalence.
