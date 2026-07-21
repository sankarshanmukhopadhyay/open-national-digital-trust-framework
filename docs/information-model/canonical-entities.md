---
layout: default
title: Canonical Entity Catalogue
parent: Information Architecture
nav_order: 1
---

# Canonical entity catalogue

| ID | Entity | Definition |
|---|---|---|
| IM-JUR | Jurisdiction | A legal or administrative domain within which authority and obligations are recognised. |
| IM-SEC | Sector | A governed domain of activity with shared policy, risk or regulatory characteristics. |
| IM-SCH | Trust Scheme | A governed arrangement that defines participants, rules, services, evidence and oversight for a stated purpose. |
| IM-GOV | Governance Authority | An entity authorised to establish or change governance rules. |
| IM-ACT | Accountable Authority | The entity answerable for a decision, capability or outcome. |
| IM-OPA | Operating Authority | The entity authorised to operate a service or process. |
| IM-ASA | Assurance Authority | The entity authorised to evaluate or attest control effectiveness. |
| IM-PAR | Participant | An actor admitted to one or more roles in a trust scheme. |
| IM-AFP | Affected Party | A person or entity whose rights, interests or circumstances may be materially affected. |
| IM-ROL | Role | A named set of permissions, duties and eligibility conditions. |
| IM-AGR | Authority Grant | An authoritative instrument granting bounded authority. |
| IM-DEL | Delegation | A constrained transfer of exercisable authority from a principal to a delegate. |
| IM-POL | Policy | An authoritative expression of permissions, duties, prohibitions and decision conditions. |
| IM-CRE | Credential | A protected set of claims issued by an authorised evidence provider. |
| IM-CLM | Claim | A statement about an entity, event, role, status or relationship. |
| IM-EVD | Evidence | Information used to support or refute a claim, authority, status or decision. |
| IM-REG | Registry Record | An authoritative published record of standing, role, status or relationship. |
| IM-STA | Status Record | A time-bounded assertion about lifecycle state. |
| IM-ASR | Assurance Assertion | A scoped statement about confidence supported by assessment evidence. |
| IM-DEC | Trust Decision | A contextual determination to admit, deny, defer or condition an effect. |
| IM-RCP | Decision Receipt | A reviewable record of the basis, outcome and attribution of a trust decision. |
| IM-EFF | Admitted Effect | A state change or action authorised by a trust decision. |
| IM-INC | Incident | An event that compromises or threatens trust objectives. |
| IM-CHA | Challenge | A request to correct, review or contest evidence, status, authority or decision. |
| IM-APL | Appeal | A formal review of a prior challenge or decision by a higher or independent authority. |
| IM-REM | Remedy | An authorised corrective, compensatory or restorative action. |
| IM-CON | Conformance Declaration | A scoped assertion of conformity to a named ONDTF profile and version. |
| IM-MRA | Recognition Arrangement | A governed agreement for bounded cross-domain recognition. |

## Minimum entity description

A profile that represents an ONDTF entity MUST define:

- stable identifier and identifier authority;
- lifecycle state and effective period;
- accountable owner and authoritative source;
- required attributes and controlled vocabularies;
- relationships and cardinalities;
- provenance, integrity and status mechanisms;
- retention, disclosure and correction rules.

The canonical catalogue is intentionally compact. Sector-specific entities should be introduced in profiles rather than added to the core unless they recur across multiple domains.
