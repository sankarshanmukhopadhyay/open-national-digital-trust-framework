---
layout: default
title: Remedy Execution
parent: Rights and Redress
nav_order: 14
---

# Remedy execution

A remedy is not complete when a complaint is acknowledged or an error is identified. Remedy execution requires the responsible entity to carry out corrective action, verify propagation, address consequential harm and provide closure evidence.

Remedies may include correction, re-evaluation, restoration of access, cessation of an action, revocation, compensation, apology, record annotation, provider remediation or systemic control change. The selected remedy must be proportionate, timely and capable of reaching downstream systems.


## Outcome-oriented effectiveness evidence

[`ONDTF-RED-001`](../core-specification/requirements-register.md#ondtf-red-001) requires **effective** remedy, not merely the existence of a complaint procedure. A remedy record should therefore make practical effectiveness reviewable.

At minimum, an adoption should be able to evidence:

- the access channel used and whether assisted or offline access was available where required;
- the eligibility basis applied without requiring scheme membership;
- whether interim relief was requested and when it became effective;
- when a final decision was reached;
- whether the consequential state was actually corrected, reversed or otherwise changed;
- evidence of propagation to downstream systems where applicable; and
- residual harm or incomplete remediation.

The machine-readable `model/rights/remedy-record.schema.json` includes fields for these measures, including `interim_relief_at`, `final_decision_at`, `consequential_state_changed`, `state_change_evidence` and `effectiveness_status`. This allows assessors to distinguish a completed administrative process from a remedy that changed the consequential state.
