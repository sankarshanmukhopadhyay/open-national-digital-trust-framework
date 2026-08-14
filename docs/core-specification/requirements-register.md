---
layout: default
title: Requirements Register
parent: Core Specification
nav_order: 4
---

# ONDTF Requirements Register

The Requirements Register is the reader-facing resolution surface for every controlled `ONDTF-*` normative requirement. It is generated from `model/normative/requirement-catalogue.yaml`; the machine-readable catalogue remains canonical. Each stable anchor below is safe to cite from prose, tables, diagrams, examples and external review records.

A requirement entry shows **what is required**, **where it applies**, **who is accountable and responsible**, **what evidence is expected**, and **which candidate conformance assertion evaluates it**.

## How to cite a requirement

Use the requirement identifier, for example [`ONDTF-GOV-001`](#ondtf-gov-001). Published ONDTF pages automatically link `ONDTF-*` identifiers to the corresponding entry in this register.

## Register summary

| Domain | Requirements |
|---|---:|
| Governance | 6 |
| Institutional Roles | 8 |
| Authority | 2 |
| Delegation | 1 |
| Evidence | 1 |
| Registries | 1 |
| Accountability | 1 |
| Security Privacy | 1 |
| Incident | 1 |
| Redress | 1 |
| Conformance | 2 |
| Independence | 1 |
| Maintenance | 2 |

## Governance

<a id="ondtf-gov-001"></a>
### ONDTF-GOV-001

**Normative force:** `MUST`  
**Status:** `active`  
**Introduced:** `v0.6.0`

> **MUST** — Identify and publish the legal, policy, contractual or institutional mandate under which the adoption operates.

| Field | Governed value |
|---|---|
| Applicability | `core`, `institutional` |
| Assessed object | ONDTF adoption |
| Accountable role | ROLE-GA |
| Responsible role(s) | ROLE-FA |
| Capability mapping | CAP-01 |
| Candidate assertion(s) | CT-CAN-001 |

**Expected evidence**

- Published mandate
- Scope statement

[Back to register summary](#register-summary)

<a id="ondtf-gov-002"></a>
### ONDTF-GOV-002

**Normative force:** `MUST`  
**Status:** `active`  
**Introduced:** `v0.6.0`

> **MUST** — Identify the bodies accountable for governance, administration, supervision, assessment, review and remedy.

| Field | Governed value |
|---|---|
| Applicability | `core`, `institutional` |
| Assessed object | institutional operating model |
| Accountable role | ROLE-GA |
| Responsible role(s) | ROLE-FA |
| Capability mapping | CAP-01 |
| Candidate assertion(s) | CT-CAN-002 |

**Expected evidence**

- Institutional role catalogue
- Responsibility assignment

[Back to register summary](#register-summary)

<a id="ondtf-gov-003"></a>
### ONDTF-GOV-003

**Normative force:** `MUST`  
**Status:** `active`  
**Introduced:** `v0.6.0`

> **MUST** — Publish the interactions, participants, services, effects and exclusions within the adoption scope.

| Field | Governed value |
|---|---|
| Applicability | `core`, `profile` |
| Assessed object | framework or profile scope |
| Accountable role | ROLE-GA |
| Responsible role(s) | ROLE-FA, ROLE-PA |
| Capability mapping | — |
| Candidate assertion(s) | CT-CAN-003 |

**Expected evidence**

- Scope and non-goals statement
- Profile manifest

[Back to register summary](#register-summary)

<a id="ondtf-gov-004"></a>
### ONDTF-GOV-004

**Normative force:** `MUST`  
**Status:** `active`  
**Introduced:** `v0.6.0`

> **MUST** — Document decision rights, delegations, escalation paths and conflicts of interest for institutional functions.

| Field | Governed value |
|---|---|
| Applicability | `institutional` |
| Assessed object | institutional operating model |
| Accountable role | ROLE-GA |
| Responsible role(s) | ROLE-FA |
| Capability mapping | — |
| Candidate assertion(s) | CT-CAN-004 |

**Expected evidence**

- Decision-rights matrix
- Delegation register
- Conflict register

[Back to register summary](#register-summary)

<a id="ondtf-gov-005"></a>
### ONDTF-GOV-005

**Normative force:** `MUST`  
**Status:** `active`  
**Introduced:** `v0.6.0`

> **MUST** — Version, approve, communicate and assign effective dates to material governance changes.

| Field | Governed value |
|---|---|
| Applicability | `institutional`, `profile` |
| Assessed object | controlled governance documents |
| Accountable role | ROLE-FA |
| Responsible role(s) | ROLE-FA, ROLE-PA |
| Capability mapping | — |
| Candidate assertion(s) | CT-CAN-005 |

**Expected evidence**

- Change record
- Approval record
- Publication notice

[Back to register summary](#register-summary)

<a id="ondtf-gov-006"></a>
### ONDTF-GOV-006

**Normative force:** `MUST`  
**Status:** `active`  
**Introduced:** `v0.6.0`

> **MUST** — Bound emergency authority by purpose, scope, duration, evidence, review and termination conditions.

| Field | Governed value |
|---|---|
| Applicability | `institutional`, `scheme` |
| Assessed object | emergency authority arrangement |
| Accountable role | ROLE-GA |
| Responsible role(s) | ROLE-SA, ROLE-ICA |
| Capability mapping | — |
| Candidate assertion(s) | CT-CAN-006 |

**Expected evidence**

- Emergency authority policy
- Exercise or invocation record
- Independent review

[Back to register summary](#register-summary)


## Institutional Roles

<a id="ondtf-rol-001"></a>
### ONDTF-ROL-001

**Normative force:** `MUST`  
**Status:** `active`  
**Introduced:** `v0.6.0`

> **MUST** — Define every institutional function before allocating it to one or more named bodies.

| Field | Governed value |
|---|---|
| Applicability | `institutional` |
| Assessed object | role allocation |
| Accountable role | ROLE-GA |
| Responsible role(s) | ROLE-FA |
| Capability mapping | — |
| Candidate assertion(s) | CT-CAN-007 |

**Expected evidence**

- Institutional function map
- Role allocation decision

[Back to register summary](#register-summary)

<a id="ondtf-rol-002"></a>
### ONDTF-ROL-002

**Normative force:** `MUST`  
**Status:** `active`  
**Introduced:** `v0.6.0`

> **MUST** — Record the authority source, scope, accountability and minimum evidence obligations of each assigned role.

| Field | Governed value |
|---|---|
| Applicability | `institutional` |
| Assessed object | assigned institutional role |
| Accountable role | ROLE-GA |
| Responsible role(s) | ROLE-FA |
| Capability mapping | — |
| Candidate assertion(s) | CT-CAN-008 |

**Expected evidence**

- Role catalogue
- Appointment or designation instrument

[Back to register summary](#register-summary)

<a id="ondtf-rol-003"></a>
### ONDTF-ROL-003

**Normative force:** `MUST`  
**Status:** `active`  
**Introduced:** `v0.6.0`

> **MUST** — Assess concentration and conflict risks whenever one body performs two or more institutional roles.

| Field | Governed value |
|---|---|
| Applicability | `institutional` |
| Assessed object | combined role allocation |
| Accountable role | ROLE-GA |
| Responsible role(s) | ROLE-FA, ROLE-IO |
| Capability mapping | — |
| Candidate assertion(s) | CT-CAN-009 |

**Expected evidence**

- Concentration assessment
- Conflict treatment plan

[Back to register summary](#register-summary)

<a id="ondtf-rol-004"></a>
### ONDTF-ROL-004

**Normative force:** `MUST`  
**Status:** `active`  
**Introduced:** `v0.6.0`

> **MUST** — Preserve an independent review path for material admission, suspension, enforcement, appeal and remedy decisions.

| Field | Governed value |
|---|---|
| Applicability | `institutional`, `scheme`, `affected-party` |
| Assessed object | review arrangement |
| Accountable role | ROLE-GA |
| Responsible role(s) | ROLE-CAR, ROLE-IO |
| Capability mapping | — |
| Candidate assertion(s) | CT-CAN-010 |

**Expected evidence**

- Appeal procedure
- Independence safeguards
- Case records

[Back to register summary](#register-summary)

<a id="ondtf-rol-005"></a>
### ONDTF-ROL-005

**Normative force:** `MUST_NOT`  
**Status:** `active`  
**Introduced:** `v0.6.0`

> **MUST NOT** — Permit an operating body to be the sole assessor and final appeals body for its own material conformance decisions.

| Field | Governed value |
|---|---|
| Applicability | `institutional`, `scheme` |
| Assessed object | separation-of-duties arrangement |
| Accountable role | ROLE-GA |
| Responsible role(s) | ROLE-AA, ROLE-CAR |
| Capability mapping | — |
| Candidate assertion(s) | CT-CAN-011 |

**Expected evidence**

- Responsibility assignment
- Independence controls

[Back to register summary](#register-summary)

<a id="ondtf-rol-006"></a>
### ONDTF-ROL-006

**Normative force:** `MUST`  
**Status:** `active`  
**Introduced:** `v0.6.0`

> **MUST** — Define referral and lead-authority rules where supervisory or regulatory competence overlaps.

| Field | Governed value |
|---|---|
| Applicability | `institutional` |
| Assessed object | supervisory coordination arrangement |
| Accountable role | ROLE-SA |
| Responsible role(s) | ROLE-SA, ROLE-FA |
| Capability mapping | — |
| Candidate assertion(s) | CT-CAN-012 |

**Expected evidence**

- Coordination protocol
- Referral records

[Back to register summary](#register-summary)

<a id="ondtf-rol-007"></a>
### ONDTF-ROL-007

**Normative force:** `MUST`  
**Status:** `active`  
**Introduced:** `v0.6.0`

> **MUST** — Give affected parties standing to access complaint, challenge and remedy processes without requiring scheme membership.

| Field | Governed value |
|---|---|
| Applicability | `institutional`, `affected-party` |
| Assessed object | affected-party procedure |
| Accountable role | ROLE-CAR |
| Responsible role(s) | ROLE-CAR, ROLE-SP, ROLE-RP |
| Capability mapping | — |
| Candidate assertion(s) | CT-CAN-013 |

**Expected evidence**

- Published eligibility rules
- Accessible procedures
- Case records

[Back to register summary](#register-summary)

<a id="ondtf-rol-008"></a>
### ONDTF-ROL-008

**Normative force:** `SHOULD`  
**Status:** `active`  
**Introduced:** `v0.6.0`

> **SHOULD** — Include independent and affected-party perspectives in periodic review of framework effectiveness and institutional legitimacy.

| Field | Governed value |
|---|---|
| Applicability | `institutional` |
| Assessed object | governance review process |
| Accountable role | ROLE-IO |
| Responsible role(s) | ROLE-IO, ROLE-FA |
| Capability mapping | — |
| Candidate assertion(s) | CT-CAN-014 |

**Expected evidence**

- Review terms
- Participation records
- Published findings

[Back to register summary](#register-summary)


## Authority

<a id="ondtf-aut-001"></a>
### ONDTF-AUT-001

**Normative force:** `MUST_NOT`  
**Status:** `active`  
**Introduced:** `v0.6.0`

> **MUST NOT** — Admit a consequential action solely because the actor or system is authenticated.

| Field | Governed value |
|---|---|
| Applicability | `core`, `interaction` |
| Assessed object | consequential decision policy |
| Accountable role | ROLE-RP |
| Responsible role(s) | ROLE-RP |
| Capability mapping | CAP-04 |
| Candidate assertion(s) | CT-CAN-015 |

**Expected evidence**

- Decision policy
- Decision records

[Back to register summary](#register-summary)

<a id="ondtf-aut-002"></a>
### ONDTF-AUT-002

**Normative force:** `MUST`  
**Status:** `active`  
**Introduced:** `v0.6.0`

> **MUST** — Evaluate scope, purpose, domain, time, conditions and revocation status when determining applicable authority.

| Field | Governed value |
|---|---|
| Applicability | `interaction` |
| Assessed object | authority evaluation |
| Accountable role | ROLE-RP |
| Responsible role(s) | ROLE-RP |
| Capability mapping | CAP-04, CAP-05 |
| Candidate assertion(s) | CT-CAN-016 |

**Expected evidence**

- Authority policy
- Evaluation record

[Back to register summary](#register-summary)


## Delegation

<a id="ondtf-aut-003"></a>
### ONDTF-AUT-003

**Normative force:** `MUST_NOT`  
**Status:** `active`  
**Introduced:** `v0.6.0`

> **MUST NOT** — Permit delegated authority to exceed the authority held by the delegating party.

| Field | Governed value |
|---|---|
| Applicability | `interaction`, `service` |
| Assessed object | delegation mechanism |
| Accountable role | ROLE-SP |
| Responsible role(s) | ROLE-SP, ROLE-RP |
| Capability mapping | CAP-05 |
| Candidate assertion(s) | CT-CAN-017 |

**Expected evidence**

- Delegation constraints
- Negative tests

[Back to register summary](#register-summary)


## Evidence

<a id="ondtf-evi-001"></a>
### ONDTF-EVI-001

**Normative force:** `MUST`  
**Status:** `active`  
**Introduced:** `v0.6.0`

> **MUST** — Evaluate consequential evidence for source attribution, integrity, relevance and freshness.

| Field | Governed value |
|---|---|
| Applicability | `interaction` |
| Assessed object | evidence evaluation |
| Accountable role | ROLE-RP |
| Responsible role(s) | ROLE-RP |
| Capability mapping | CAP-07 |
| Candidate assertion(s) | CT-CAN-018 |

**Expected evidence**

- Evidence policy
- Decision record

[Back to register summary](#register-summary)


## Registries

<a id="ondtf-evi-003"></a>
### ONDTF-EVI-003

**Normative force:** `MUST`  
**Status:** `active`  
**Introduced:** `v0.6.0`

> **MUST** — Publish the governing authority, scope, update policy, effective time and provenance of registry or status information.

| Field | Governed value |
|---|---|
| Applicability | `service`, `implementation` |
| Assessed object | registry or trust-list service |
| Accountable role | ROLE-FA |
| Responsible role(s) | ROLE-RTO |
| Capability mapping | — |
| Candidate assertion(s) | CT-CAN-019 |

**Expected evidence**

- Registry governance statement
- Status history
- Change log

[Back to register summary](#register-summary)


## Accountability

<a id="ondtf-dec-003"></a>
### ONDTF-DEC-003

**Normative force:** `MUST`  
**Status:** `active`  
**Introduced:** `v0.6.0`

> **MUST** — Produce or reference a reviewable record sufficient to establish the basis and responsible authority for a consequential decision.

| Field | Governed value |
|---|---|
| Applicability | `interaction` |
| Assessed object | consequential decision |
| Accountable role | ROLE-RP |
| Responsible role(s) | ROLE-RP |
| Capability mapping | CAP-11 |
| Candidate assertion(s) | CT-CAN-020 |

**Expected evidence**

- Decision record
- Preserved evidence reference

[Back to register summary](#register-summary)


## Security Privacy

<a id="ondtf-spr-001"></a>
### ONDTF-SPR-001

**Normative force:** `MUST`  
**Status:** `active`  
**Introduced:** `v0.6.0`

> **MUST** — Maintain a threat, privacy and risk model proportionate to the covered effects and institutional powers.

| Field | Governed value |
|---|---|
| Applicability | `core`, `institutional`, `service` |
| Assessed object | adoption risk model |
| Accountable role | ROLE-GA |
| Responsible role(s) | ROLE-SA, ROLE-SP, ROLE-RTO |
| Capability mapping | — |
| Candidate assertion(s) | CT-CAN-021 |

**Expected evidence**

- Threat model
- Privacy assessment
- Risk register

[Back to register summary](#register-summary)


## Incident

<a id="ondtf-inc-001"></a>
### ONDTF-INC-001

**Normative force:** `MUST`  
**Status:** `active`  
**Introduced:** `v0.6.0`

> **MUST** — Define detection, containment, evidence preservation, recovery, notification and coordination responsibilities for material incidents.

| Field | Governed value |
|---|---|
| Applicability | `institutional`, `service` |
| Assessed object | incident arrangement |
| Accountable role | ROLE-ICA |
| Responsible role(s) | ROLE-ICA, ROLE-SP, ROLE-RTO |
| Capability mapping | — |
| Candidate assertion(s) | CT-CAN-022 |

**Expected evidence**

- Incident plan
- Exercise record
- Incident report

[Back to register summary](#register-summary)


## Redress

<a id="ondtf-red-001"></a>
### ONDTF-RED-001

**Normative force:** `MUST`  
**Status:** `active`  
**Introduced:** `v0.6.0`

> **MUST** — Provide affected parties an accessible route to correction, challenge, independent review and effective remedy for consequential decisions.

| Field | Governed value |
|---|---|
| Applicability | `affected-party`, `interaction` |
| Assessed object | redress system |
| Accountable role | ROLE-CAR |
| Responsible role(s) | ROLE-CAR, ROLE-SP, ROLE-RP |
| Capability mapping | CAP-13 |
| Candidate assertion(s) | CT-CAN-023 |

**Expected evidence**

- Published procedure
- Case record
- Remedy completion record

[Back to register summary](#register-summary)


## Conformance

<a id="ondtf-con-001"></a>
### ONDTF-CON-001

**Normative force:** `MUST`  
**Status:** `active`  
**Introduced:** `v0.6.0`

> **MUST** — Scope a conformance claim by ONDTF version, profile, assessed object, organisational boundary, applicable requirements, evidence cut-off and approved exceptions.

| Field | Governed value |
|---|---|
| Applicability | `core`, `profile`, `provider`, `service`, `implementation` |
| Assessed object | conformance claim |
| Accountable role | ROLE-CAB |
| Responsible role(s) | ROLE-ASR, ROLE-CAB |
| Capability mapping | CAP-15 |
| Candidate assertion(s) | CT-CAN-024 |

**Expected evidence**

- Conformance declaration
- Assessment record

[Back to register summary](#register-summary)

<a id="ondtf-con-003"></a>
### ONDTF-CON-003

**Normative force:** `MUST`  
**Status:** `active`  
**Introduced:** `v0.6.0`

> **MUST** — Identify the exact version, selected scope, constraints and maintenance responsibility for every normative external dependency.

| Field | Governed value |
|---|---|
| Applicability | `profile` |
| Assessed object | profile dependency |
| Accountable role | ROLE-PA |
| Responsible role(s) | ROLE-PA |
| Capability mapping | — |
| Candidate assertion(s) | CT-CAN-026 |

**Expected evidence**

- Profile manifest
- Dependency register

[Back to register summary](#register-summary)


## Independence

<a id="ondtf-con-002"></a>
### ONDTF-CON-002

**Normative force:** `MUST_NOT`  
**Status:** `active`  
**Introduced:** `v0.6.0`

> **MUST NOT** — Require a particular external meta-model, schema, protocol, registry implementation or product for core conformance.

| Field | Governed value |
|---|---|
| Applicability | `core`, `profile` |
| Assessed object | core conformance policy |
| Accountable role | ROLE-GA |
| Responsible role(s) | ROLE-FA, ROLE-PA |
| Capability mapping | CAP-15 |
| Candidate assertion(s) | CT-CAN-025 |

**Expected evidence**

- Core conformance policy
- Profile dependency declarations

[Back to register summary](#register-summary)


## Maintenance

<a id="ondtf-mnt-001"></a>
### ONDTF-MNT-001

**Normative force:** `MUST`  
**Status:** `active`  
**Introduced:** `v0.6.0`

> **MUST** — Preserve stable identifiers and lifecycle status for active, deprecated, withdrawn and superseded requirements.

| Field | Governed value |
|---|---|
| Applicability | `core`, `profile` |
| Assessed object | requirement catalogue |
| Accountable role | ROLE-FA |
| Responsible role(s) | ROLE-FA |
| Capability mapping | — |
| Candidate assertion(s) | CT-CAN-027 |

**Expected evidence**

- Requirement catalogue
- Change history

[Back to register summary](#register-summary)

<a id="ondtf-mnt-002"></a>
### ONDTF-MNT-002

**Normative force:** `MUST`  
**Status:** `active`  
**Introduced:** `v0.6.0`

> **MUST** — Perform change-impact analysis across profiles, roles, controls, evidence, tests and conformance claims for every material normative change.

| Field | Governed value |
|---|---|
| Applicability | `core`, `profile`, `institutional` |
| Assessed object | normative change |
| Accountable role | ROLE-FA |
| Responsible role(s) | ROLE-FA, ROLE-PA |
| Capability mapping | — |
| Candidate assertion(s) | CT-CAN-028 |

**Expected evidence**

- Change-impact record
- Migration plan

[Back to register summary](#register-summary)
