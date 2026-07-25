---
title: Authoring and Review
parent: Controlled Vocabulary
nav_order: 2
---
# Term Authoring and Review

1. Create one YAML record under `model/terminology/terms/`.
2. Use a stable lower-case hyphenated identifier.
3. State one concept, avoid circular definitions, and define the ONDTF meaning rather than copying an external source.
4. Record aliases only when they are safe search and authoring equivalents.
5. Link related terms using `see_also`.
6. Classify the term and state whether it is normative.
7. Record source provenance and any external mapping.
8. Run `make terminology` and `make validate`.
9. Obtain editorial and relevant domain review before approval.

Definitions should make authority, scope, evidence, lifecycle, enforcement, and redress explicit where those properties are material to the concept.
