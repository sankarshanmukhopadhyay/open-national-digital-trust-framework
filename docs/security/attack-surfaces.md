---
layout: default
title: Attack Surfaces
parent: Security Architecture
nav_order: 10
---
# Attack-surface catalogue

An attack surface is any technical, organisational, semantic, or procedural location where an actor can alter the meaning, authority, evidence, state, availability, accountability, or consequences of a trust-system operation.

| ID | Attack surface | Primary boundary |
|---|---|---|
| `AS-01` | Governance decision process | `SB-01` |
| `AS-02` | Authority issuance and delegation | `SB-06` |
| `AS-03` | Privileged administration interface | `SB-04` |
| `AS-04` | Participant onboarding and enrolment | `SB-05` |
| `AS-05` | Credential issuance and presentation | `SB-07` |
| `AS-06` | Evidence ingestion and provenance | `SB-09` |
| `AS-07` | Registry publication and resolution | `SB-10` |
| `AS-08` | Status and revocation propagation | `SB-10` |
| `AS-09` | Policy authoring and distribution | `SB-11` |
| `AS-10` | Decision service and rule evaluation | `SB-12` |
| `AS-11` | Effect execution interface | `SB-13` |
| `AS-12` | Audit logging and telemetry | `SB-12` |
| `AS-13` | Incident and emergency control | `SB-20` |
| `AS-14` | Federation gateway | `SB-15` |
| `AS-15` | Challenge, appeal and redress channel | `SB-21` |
| `AS-16` | Software build and dependency chain | `SB-17` |
| `AS-17` | Automated-agent tool interface | `SB-19` |
| `AS-18` | Public transparency and disclosure surface | `SB-22` |

## Boundary-oriented analysis

Every material attack surface MUST be analysed together with the security boundary it crosses. Interface security alone is insufficient where an apparently valid request carries invalid authority, stale status, substituted semantics, or an unreviewable effect.

The machine-readable source is [`model/security/attack-surfaces.yaml`](../../model/security/attack-surfaces.yaml).
