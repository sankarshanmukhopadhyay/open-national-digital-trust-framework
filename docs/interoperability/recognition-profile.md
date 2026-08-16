---
layout: default
title: Recognition Profile
parent: Interoperability and Recognition
nav_order: 3
---

# Bounded recognition and equivalence

Recognition is a governed decision, not an automatic consequence of technical compatibility. The candidate `REC-001` profile records scope, exclusions, dimensional equivalence, evidence basis, validity, lifecycle state and an explicit assurance ceiling.

## Assurance ceiling

A recognition decision must not silently widen assurance. A relying decision applies the **lowest supported assurance** among the recognised dimensions actually used for that decision. Partial or conditional equivalence remains representable and excluded claims remain excluded.

The machine-readable profile exposes:

- recognised framework and version;
- recognising authority;
- scope and excluded claims;
- dimension-by-dimension equivalence;
- evidence basis;
- assurance ceiling and weakest-link rule;
- effective and expiry times;
- suspension and revocation state; and
- review and renewal requirements.

An expired, suspended or revoked recognition state therefore remains machine-detectable rather than being inferred from prose.
