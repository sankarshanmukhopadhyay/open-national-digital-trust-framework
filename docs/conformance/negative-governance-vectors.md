---
layout: default
title: Negative Governance Vectors
parent: Conformance and Accreditation
nav_order: 12
---

# Negative governance conformance vectors

The candidate vector set `NGV-001` turns the emergency-authority boundary in [`ONDTF-GOV-006`](../core-specification/requirements-register.md#ondtf-gov-006) into deterministic negative cases.

| Vector | Condition | Expected outcome |
|---|---|---|
| `EMG-NEG-001` | Authority used after expiry | `nonconformant` |
| `EMG-NEG-002` | Repeated renewal without fresh independent justification | `nonconformant` |
| `EMG-NEG-003` | Exercised scope exceeds approved scope | `nonconformant` |
| `EMG-NEG-004` | Required independent review absent | `nonconformant` |
| `EMG-NEG-005` | Action occurs after termination | `nonconformant` |
| `EMG-NEG-006` | Retrospective justification substitutes for contemporaneous evidence | `nonconformant` |

These vectors do not define the lawful emergency powers of any jurisdiction. They test whether an ONDTF adoption preserves the purpose, scope, duration, evidence, review and termination boundaries it has itself declared.
