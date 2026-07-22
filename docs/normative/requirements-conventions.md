---
layout: default
title: Requirements Conventions
parent: Normative Architecture
nav_order: 1
---

# Requirements conventions

## Purpose

This document defines the publication contract for normative ONDTF requirements. It prevents explanatory prose, implementation advice and examples from being mistaken for mandatory obligations.

## Normative vocabulary

The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT** and **MAY** are to be interpreted as requirement forces when, and only when, they appear in an identified ONDTF requirement or a profile requirement that follows this convention.

| Force | Meaning |
|---|---|
| MUST | An unconditional obligation within the declared applicability scope |
| MUST NOT | An unconditional prohibition within the declared applicability scope |
| SHOULD | A recommended obligation that may be departed from only with documented rationale and risk treatment |
| SHOULD NOT | A discouraged practice that may be used only with documented rationale and risk treatment |
| MAY | A permitted option that does not create an obligation for other participants unless a profile says otherwise |

Lower-case uses of these words in explanatory text are not normative.

## Requirement identifiers

Core requirement identifiers use the pattern `ONDTF-<DOMAIN>-<NNN>`.

| Domain code | Domain |
|---|---|
| GOV | Governance and mandate |
| ROL | Institutional roles and decision rights |
| AUT | Authority and delegation |
| EVI | Evidence and registries |
| ASR | Assurance |
| DEC | Decision and effect |
| SPR | Security and privacy |
| INC | Incident and resilience |
| RED | Rights, challenge and remedy |
| INT | Interoperability |
| CON | Conformance |
| MNT | Maintenance and controlled change |

Identifiers are stable. A requirement that is withdrawn remains reserved and receives a lifecycle status rather than being silently reused.

## Anatomy of a requirement

Every normative catalogue entry must include:

- a stable identifier;
- requirement force;
- atomic statement;
- applicability class;
- accountable role;
- responsible role or roles;
- evidence expectation;
- source or rationale;
- lifecycle status;
- release introduced;
- linked capability or principle where applicable.

A requirement should express one testable proposition. Compound obligations should be split when independent evidence or exceptions could apply.

## Normative and informative material

A document may contain both normative and informative material, but each normative obligation must be represented in the machine-readable catalogue. Tables, diagrams and examples are informative unless they explicitly cite requirement identifiers.

Implementation notes may explain one way to satisfy a requirement. They do not become the only conformant method unless a profile selects them as a dependency.

## Requirement lifecycle

A requirement has one of the following statuses:

- `draft`: under active development and not a stable conformance basis;
- `active`: available for adoption and conformance claims at the stated framework version;
- `deprecated`: retained for compatibility but scheduled for withdrawal;
- `withdrawn`: no longer applicable to new claims;
- `superseded`: replaced by identified requirement identifiers.

Changes that alter obligation, applicability, accountability, evidence or conformance outcome are normative changes and require recorded impact review.
