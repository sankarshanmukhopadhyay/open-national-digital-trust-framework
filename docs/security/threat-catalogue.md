---
layout: default
title: Threat Catalogue
parent: Security Architecture
nav_order: 11
---
# Threat catalogue

This catalogue establishes the first structured ONDTF threat baseline. Each threat has a stable identifier and machine-readable relationships to its category, adversary, protected asset, security boundary, attack surface, domain, objective, trust assumption, detection indicators, and candidate control families.

| ID | Threat | Category | Adversary | Asset | Boundary |
|---|---|---|---|---|---|
| `THR-001` | Mandate fabrication | `THCAT-01` | `ADV-08` | `AST-01` | `SB-01` |
| `THR-002` | Governance decision tampering | `THCAT-01` | `ADV-04` | `AST-02` | `SB-02` |
| `THR-003` | Governance capture | `THCAT-01` | `ADV-12` | `AST-20` | `SB-01` |
| `THR-004` | Emergency authority abuse | `THCAT-01` | `ADV-05` | `AST-13` | `SB-20` |
| `THR-005` | Authority escalation | `THCAT-02` | `ADV-02` | `AST-03` | `SB-06` |
| `THR-006` | Delegation scope stripping | `THCAT-02` | `ADV-11` | `AST-21` | `SB-19` |
| `THR-007` | Delegation laundering | `THCAT-02` | `ADV-12` | `AST-03` | `SB-06` |
| `THR-008` | Stale authority acceptance | `THCAT-02` | `ADV-03` | `AST-03` | `SB-06` |
| `THR-009` | Synthetic identity enrolment | `THCAT-03` | `ADV-01` | `AST-04` | `SB-05` |
| `THR-010` | Authenticator phishing | `THCAT-03` | `ADV-01` | `AST-15` | `SB-05` |
| `THR-011` | Biometric injection | `THCAT-03` | `ADV-01` | `AST-15` | `SB-05` |
| `THR-012` | Account recovery takeover | `THCAT-03` | `ADV-01` | `AST-15` | `SB-05` |
| `THR-013` | Credential forgery | `THCAT-04` | `ADV-01` | `AST-06` | `SB-08` |
| `THR-014` | Credential replay | `THCAT-04` | `ADV-02` | `AST-06` | `SB-08` |
| `THR-015` | Issuer context confusion | `THCAT-04` | `ADV-06` | `AST-07` | `SB-07` |
| `THR-016` | Evidence provenance substitution | `THCAT-04` | `ADV-06` | `AST-07` | `SB-09` |
| `THR-017` | Registry poisoning | `THCAT-05` | `ADV-07` | `AST-08` | `SB-10` |
| `THR-018` | Registry equivocation | `THCAT-05` | `ADV-07` | `AST-08` | `SB-10` |
| `THR-019` | Revocation suppression | `THCAT-05` | `ADV-07` | `AST-08` | `SB-10` |
| `THR-020` | Status freshness rollback | `THCAT-05` | `ADV-07` | `AST-08` | `SB-10` |
| `THR-021` | Policy rollback | `THCAT-06` | `ADV-05` | `AST-05` | `SB-11` |
| `THR-022` | Policy context mismatch | `THCAT-06` | `ADV-08` | `AST-05` | `SB-11` |
| `THR-023` | Decision input manipulation | `THCAT-06` | `ADV-04` | `AST-10` | `SB-12` |
| `THR-024` | Assurance label inflation | `THCAT-06` | `ADV-08` | `AST-09` | `SB-12` |
| `THR-025` | Effect substitution | `THCAT-07` | `ADV-04` | `AST-11` | `SB-13` |
| `THR-026` | Effect replay | `THCAT-07` | `ADV-02` | `AST-11` | `SB-13` |
| `THR-027` | Unauthorised downstream action | `THCAT-07` | `ADV-11` | `AST-21` | `SB-19` |
| `THR-028` | Affected-party invisibility | `THCAT-07` | `ADV-08` | `AST-14` | `SB-14` |
| `THR-029` | Audit log tampering | `THCAT-08` | `ADV-05` | `AST-12` | `SB-12` |
| `THR-030` | Telemetry suppression | `THCAT-08` | `ADV-05` | `AST-17` | `SB-12` |
| `THR-031` | Denial of trust resolution | `THCAT-08` | `ADV-01` | `AST-08` | `SB-10` |
| `THR-032` | Recovery state manipulation | `THCAT-08` | `ADV-05` | `AST-13` | `SB-20` |
| `THR-033` | Dependency substitution | `THCAT-09` | `ADV-10` | `AST-16` | `SB-17` |
| `THR-034` | Build pipeline compromise | `THCAT-09` | `ADV-10` | `AST-16` | `SB-17` |
| `THR-035` | Malicious update propagation | `THCAT-09` | `ADV-10` | `AST-16` | `SB-17` |
| `THR-036` | Federation laundering | `THCAT-10` | `ADV-09` | `AST-19` | `SB-15` |
| `THR-037` | Cross-domain semantic substitution | `THCAT-10` | `ADV-09` | `AST-19` | `SB-15` |
| `THR-038` | Foreign assurance transitivity | `THCAT-10` | `ADV-09` | `AST-09` | `SB-15` |
| `THR-039` | Correlation through status checks | `THCAT-11` | `ADV-07` | `AST-18` | `SB-10` |
| `THR-040` | Over-collection at verification | `THCAT-11` | `ADV-02` | `AST-18` | `SB-08` |
| `THR-041` | Public disclosure re-identification | `THCAT-11` | `ADV-14` | `AST-18` | `SB-22` |
| `THR-042` | Agent mandate drift | `THCAT-12` | `ADV-11` | `AST-21` | `SB-19` |
| `THR-043` | Prompt or instruction injection | `THCAT-12` | `ADV-01` | `AST-21` | `SB-19` |
| `THR-044` | Tool invocation outside scope | `THCAT-12` | `ADV-11` | `AST-21` | `SB-19` |
| `THR-045` | Decision receipt suppression | `THCAT-13` | `ADV-04` | `AST-12` | `SB-21` |
| `THR-046` | Grievance obstruction | `THCAT-13` | `ADV-08` | `AST-14` | `SB-21` |
| `THR-047` | Selective remedy enforcement | `THCAT-13` | `ADV-08` | `AST-14` | `SB-21` |
| `THR-048` | Critical service concentration failure | `THCAT-14` | `ADV-14` | `AST-20` | `SB-18` |

## Use

Implementations SHOULD select applicable threats, add context-specific threats, assess inherent and residual exposure, map controls and evidence, and record the disposition of non-applicable threats. Deleting an applicable threat from a local profile is not a valid treatment.

The machine-readable source is [`model/security/threats.yaml`](../../model/security/threats.yaml).
