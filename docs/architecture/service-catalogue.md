---
layout: default
title: Service Catalogue
parent: Reference Architecture
nav_order: 5
---

# Service catalogue

ONDTF services are protocol-neutral capability contracts. A service specification defines the observable outcome and evidence obligations, not a mandatory network API.

| ID | Service | Required outcome |
|---|---|---|
| ARC-S01 | Participant resolution | Resolve identity, role and standing |
| ARC-S02 | Authority resolution | Resolve current mandate and constraints |
| ARC-S03 | Delegation validation | Validate delegation chain and attenuation |
| ARC-S04 | Policy discovery | Locate authoritative applicable policy |
| ARC-S05 | Policy evaluation | Evaluate permissions, duties and prohibitions |
| ARC-S06 | Evidence verification | Validate integrity, provenance and semantic fitness |
| ARC-S07 | Registry discovery | Locate authoritative registries |
| ARC-S08 | Status resolution | Obtain current lifecycle status |
| ARC-S09 | Assurance evaluation | Evaluate confidence and residual risk |
| ARC-S10 | Trust decision | Admit, deny, defer or condition an effect |
| ARC-S11 | Effect execution | Execute an admitted effect |
| ARC-S12 | Decision receipt | Create attributable and reviewable record |
| ARC-S13 | Evidence preservation | Preserve evidence under retention policy |
| ARC-S14 | Incident notification | Report and route trust incidents |
| ARC-S15 | Challenge submission | Submit and acknowledge challenge |
| ARC-S16 | Remedy tracking | Track correction and remedy execution |
| ARC-S17 | Recognition resolution | Evaluate cross-domain recognition |
| ARC-S18 | Conformance declaration | Publish scoped conformance evidence |

## Common service contract

Each service MUST declare:

- interaction context and purpose;
- caller and provider authority;
- required inputs and authoritative sources;
- output status, reason code and confidence limitations;
- evidence and receipt obligations;
- privacy and data-minimisation controls;
- timeout, retry and stale-data behaviour;
- version and profile identifiers.

## Decision service response model

A decision response SHOULD use one of the following outcomes:

| Outcome | Meaning |
|---|---|
| `ADMIT` | The effect may proceed under stated conditions |
| `DENY` | The effect must not proceed |
| `DEFER` | More evidence, human review or external decision is required |
| `CONDITION` | The effect may proceed only after named obligations are satisfied |
| `ERROR` | No valid decision was produced |

A technical error MUST NOT be silently interpreted as an admission.
