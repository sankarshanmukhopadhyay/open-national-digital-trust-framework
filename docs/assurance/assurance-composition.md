---
layout: default
title: Assurance Composition
parent: Assurance, Risk and Resilience
nav_order: 19
---

# Assurance composition

Assurance composition determines how dimension-level conclusions support a particular use case. The profile defines required dimensions, minimum levels, critical dimensions, dependency rules, freshness and the action to take when evidence is incomplete.

```mermaid
flowchart TD
  U[Use case and harm model] --> R[Required assurance dimensions]
  R --> M[Minimum levels and critical dimensions]
  M --> V[Evaluate evidence and freshness]
  V --> C{All critical conditions met?}
  C -->|No| X[Refuse, defer, degrade or escalate]
  C -->|Yes| Q{Residual uncertainty acceptable?}
  Q -->|No| X
  Q -->|Yes| A[Context-bounded assurance conclusion]
```

## Composition rules

A composition rule must identify critical dimensions whose failure cannot be offset, permissible dependencies, evidence precedence, uncertainty treatment and exception authority. The rule should use a weakest-critical-link approach rather than averaging levels.

The machine-readable representation is defined in `model/assurance/assurance-levels.yaml` and `model/assurance/assurance-claim.schema.json`.
