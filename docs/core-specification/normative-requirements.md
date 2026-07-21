---
layout: default
title: Normative Requirements
parent: Core Specification
nav_order: 4
---

# Normative requirements

This draft establishes the first coordinated normative baseline. The machine-readable register is maintained in `model/requirements/core-requirements.yaml`.

## Governance and scope

- **ONDTF-GOV-001:** An adopting framework **MUST** identify the legal, policy, or institutional mandate under which it operates.
- **ONDTF-GOV-002:** It **MUST** identify the authority accountable for the framework and the bodies empowered to operate, supervise, assess, and review it.
- **ONDTF-GOV-003:** It **MUST** publish the scope of covered interactions, participants, services, and effects.
- **ONDTF-GOV-004:** Decision rights, delegations, conflicts of interest, and escalation paths **MUST** be documented.
- **ONDTF-GOV-005:** Material governance changes **MUST** be versioned, communicated, and subject to an effective-date policy.
- **ONDTF-GOV-006:** Emergency authority **MUST** be bounded by purpose, duration, review, and evidence requirements.

## Authority and delegation

- **ONDTF-AUT-001:** A consequential action **MUST NOT** be admitted solely because the actor is authenticated.
- **ONDTF-AUT-002:** Authority evaluation **MUST** consider scope, purpose, recipient or domain, time, conditions, and revocation status where applicable.
- **ONDTF-AUT-003:** Delegated authority **MUST NOT** exceed the authority held by the delegating party.
- **ONDTF-AUT-004:** A delegation **MUST** be attributable to a recognised delegator and **MUST** support suspension or termination.
- **ONDTF-AUT-005:** Delegation chains **SHOULD** be traceable to an accountable authority.
- **ONDTF-AUT-006:** Profiles **MUST** state whether re-delegation is permitted and under what attenuation rules.

## Evidence, registries, and assurance

- **ONDTF-EVI-001:** Evidence used for a consequential decision **MUST** be attributable to a source and evaluated for integrity, relevance, and freshness.
- **ONDTF-EVI-002:** The framework **MUST** distinguish evidence validity from the truth, legality, or sufficiency of the proposition it supports.
- **ONDTF-EVI-003:** Registry and status information **MUST** identify its governing authority, update policy, and effective time.
- **ONDTF-EVI-004:** Evidence collection and disclosure **MUST** be proportionate to the stated purpose and risk.
- **ONDTF-ASR-001:** Assurance claims **MUST** identify the subject, scope, controls, evidence basis, assessor where applicable, and freshness.
- **ONDTF-ASR-002:** An assurance level **MUST NOT** be treated as transferable across contexts without an equivalence assessment.

## Decision, effect, and accountability

- **ONDTF-DEC-001:** The framework **MUST** identify which trust decisions can produce consequential effects.
- **ONDTF-DEC-002:** Effect admission **MUST** evaluate applicable authority, policy, evidence, assurance, and risk requirements.
- **ONDTF-DEC-003:** A consequential decision **MUST** produce or reference a reviewable record sufficient to establish the decision basis and responsible authority.
- **ONDTF-DEC-004:** Automated decision components **MUST** be governed by the same authority and accountability requirements as human-operated components.
- **ONDTF-DEC-005:** A decision record **SHOULD** avoid unnecessary disclosure of personal or confidential information.

## Security, privacy, incident, and redress

- **ONDTF-SPR-001:** The framework **MUST** maintain a threat and risk model proportionate to the covered effects.
- **ONDTF-SPR-002:** Personal information **MUST** be minimised, purpose-bound, protected, and retained only as justified by the applicable profile.
- **ONDTF-SPR-003:** The framework **MUST** address correlation, linkability, exclusion, and surveillance risks arising from trust infrastructure.
- **ONDTF-INC-001:** Material incidents **MUST** support detection, containment, evidence preservation, recovery, and accountable notification.
- **ONDTF-RED-001:** Affected parties **MUST** have an accessible route to correction, challenge, and remedy for consequential decisions.
- **ONDTF-RED-002:** Redress arrangements **MUST** identify responsible bodies, timelines, escalation paths, and available remedies.

## Interoperability and conformance

- **ONDTF-INT-001:** Interoperability claims **MUST** identify the semantic, governance, assurance, operational, and technical dimensions covered.
- **ONDTF-INT-002:** A profile **MUST** document deviations, extensions, and dependencies.
- **ONDTF-CON-001:** A conformance claim **MUST** identify the ONDTF version, profile, conformance class, scope, and evidence basis.
- **ONDTF-CON-002:** Core ONDTF conformance **MUST NOT** require a particular meta-model, schema language, protocol suite, registry implementation, or software product.
- **ONDTF-CON-003:** Where a profile selects an external specification, the profile **MUST** identify the selected version and any constraints.
