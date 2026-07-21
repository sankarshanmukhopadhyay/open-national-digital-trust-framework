---
layout: default
title: Dependency Policy
parent: Foundations
nav_order: 3
---
# Dependency and Version Policy

ONDTF may depend on specifications, schemas, or profiles maintained elsewhere. Dependencies must remain explicit and reviewable.

Each normative dependency must record:

- repository or specification name;
- exact version or immutable reference;
- required capability;
- compatibility range;
- failure behaviour when unavailable or incompatible;
- migration and deprecation policy;
- responsible ONDTF workstream.

ONDTF shall not silently inherit semantic changes from a moving branch. Jurisdiction profiles may select different compatible implementations, but must preserve the required ONDTF semantics.
