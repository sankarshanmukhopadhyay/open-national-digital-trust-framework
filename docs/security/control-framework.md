---
layout: default
title: Security Control Framework
parent: Security Architecture
nav_order: 12
---
# Security control framework

The ONDTF control framework connects security objectives to implementable safeguards, expected evidence, accountable functions, and the threats they are intended to reduce. Controls are outcome-oriented and implementation-neutral.

## Control families

| ID | Family |
|---|---|
| `CTL-FAM-01` | Governance and authority integrity |
| `CTL-FAM-02` | Identity and credential protection |
| `CTL-FAM-03` | Evidence, registry and status integrity |
| `CTL-FAM-04` | Policy, decision and effect integrity |
| `CTL-FAM-05` | Platform and supply-chain security |
| `CTL-FAM-06` | Monitoring, accountability and redress |
| `CTL-FAM-07` | Federation and privacy protection |
| `CTL-FAM-08` | Automated-agent safety and authority |

## Control catalogue

| ID | Control | Family | Initial threat links |
|---|---|---|---|
| `CTL-001` | Mandate provenance verification | `CTL-FAM-01` | `THR-001`, `THR-004` |
| `CTL-002` | Governance decision signing and publication | `CTL-FAM-01` | `THR-002`, `THR-007` |
| `CTL-003` | Separation of critical governance powers | `CTL-FAM-01` | `THR-003`, `THR-010` |
| `CTL-004` | Authority scope encoding | `CTL-FAM-01` | `THR-004`, `THR-013` |
| `CTL-005` | Delegation chain validation | `CTL-FAM-01` | `THR-005`, `THR-016` |
| `CTL-006` | Authority freshness enforcement | `CTL-FAM-01` | `THR-006`, `THR-019` |
| `CTL-007` | Phishing-resistant authentication | `CTL-FAM-02` | `THR-007`, `THR-022` |
| `CTL-008` | Hardware-backed key protection | `CTL-FAM-02` | `THR-008`, `THR-025` |
| `CTL-009` | Secure recovery and re-binding | `CTL-FAM-02` | `THR-009`, `THR-028` |
| `CTL-010` | Credential audience and nonce binding | `CTL-FAM-02` | `THR-010`, `THR-031` |
| `CTL-011` | Issuer competence verification | `CTL-FAM-02` | `THR-011`, `THR-034` |
| `CTL-012` | Credential lifecycle enforcement | `CTL-FAM-02` | `THR-012`, `THR-037` |
| `CTL-013` | Evidence provenance validation | `CTL-FAM-03` | `THR-013`, `THR-040` |
| `CTL-014` | Registry integrity and non-equivocation | `CTL-FAM-03` | `THR-014`, `THR-043` |
| `CTL-015` | Status freshness policy | `CTL-FAM-03` | `THR-015`, `THR-046` |
| `CTL-016` | Revocation propagation monitoring | `CTL-FAM-03` | `THR-016`, `THR-001` |
| `CTL-017` | Privacy-preserving status resolution | `CTL-FAM-03` | `THR-017`, `THR-004` |
| `CTL-018` | Independent source reconciliation | `CTL-FAM-03` | `THR-018`, `THR-007` |
| `CTL-019` | Signed and versioned policy artefacts | `CTL-FAM-04` | `THR-019`, `THR-010` |
| `CTL-020` | Policy rollback protection | `CTL-FAM-04` | `THR-020`, `THR-013` |
| `CTL-021` | Decision input integrity checks | `CTL-FAM-04` | `THR-021`, `THR-016` |
| `CTL-022` | Evidence-before-effect gate | `CTL-FAM-04` | `THR-022`, `THR-019` |
| `CTL-023` | Effect idempotency and replay protection | `CTL-FAM-04` | `THR-023`, `THR-022` |
| `CTL-024` | Decision receipt generation | `CTL-FAM-04` | `THR-024`, `THR-025` |
| `CTL-025` | Secure software development lifecycle | `CTL-FAM-05` | `THR-025`, `THR-028` |
| `CTL-026` | Dependency provenance and verification | `CTL-FAM-05` | `THR-026`, `THR-031` |
| `CTL-027` | Protected build and release pipeline | `CTL-FAM-05` | `THR-027`, `THR-034` |
| `CTL-028` | Configuration integrity monitoring | `CTL-FAM-05` | `THR-028`, `THR-037` |
| `CTL-029` | Tamper-evident audit logging | `CTL-FAM-06` | `THR-029`, `THR-040` |
| `CTL-030` | Security telemetry and anomaly detection | `CTL-FAM-06` | `THR-030`, `THR-043` |
| `CTL-031` | Incident containment and evidence preservation | `CTL-FAM-06` | `THR-031`, `THR-046` |
| `CTL-032` | Accessible challenge and redress | `CTL-FAM-06` | `THR-032`, `THR-001` |
| `CTL-033` | Federation recognition constraints | `CTL-FAM-07` | `THR-033`, `THR-004` |
| `CTL-034` | Semantic and assurance mapping validation | `CTL-FAM-07` | `THR-034`, `THR-007` |
| `CTL-035` | Controlled disclosure and minimisation | `CTL-FAM-07` | `THR-035`, `THR-010` |
| `CTL-036` | Correlation resistance | `CTL-FAM-07` | `THR-036`, `THR-013` |
| `CTL-037` | Machine-readable agent mandate | `CTL-FAM-08` | `THR-037`, `THR-016` |
| `CTL-038` | Tool-level least authority | `CTL-FAM-08` | `THR-038`, `THR-019` |
| `CTL-039` | Agent action receipt and causal trace | `CTL-FAM-08` | `THR-039`, `THR-022` |
| `CTL-040` | Human override and safe halt | `CTL-FAM-08` | `THR-040`, `THR-025` |

## Evidence and effectiveness

A control is not considered effective merely because it is documented. A conformant assessment MUST distinguish control design, implementation, operating evidence, exceptions, compensating controls, and residual exposure.

## Informative external grounding

ONDTF controls may be mapped to external control frameworks. Such mappings MUST state whether the relationship is equivalent, partial, narrower, broader, or merely informed by. Initial informative sources include NIST SP 800-53, ISO/IEC 27001, NIST SP 800-30, the NIST Cybersecurity Framework, MITRE ATT&CK, and OWASP guidance. No equivalence is claimed by naming a source.

The machine-readable sources are [`control-families.yaml`](../../model/security/control-families.yaml) and [`controls.yaml`](../../model/security/controls.yaml).
