---
layout: default
title: Legitimacy Evidence Profile
parent: Assurance, Risk and Resilience
nav_order: 31
---

# Legitimacy evidence profile

A published mandate is evidence that an adoption has a formal authority basis. It is **not, by itself, evidence that the resulting governance is substantively legitimate**. The informative `LEP-001` profile complements [`ONDTF-GOV-001`](../core-specification/requirements-register.md#ondtf-gov-001) and [`ONDTF-ROL-008`](../core-specification/requirements-register.md#ondtf-rol-008) without prescribing a jurisdiction-specific institutional form.

The machine-readable profile is `model/assurance/legitimacy-evidence-profile.yaml`.

## Evidence dimensions

| Dimension | Evidence question | Example gap signal |
|---|---|---|
| Participation | Can materially affected groups participate in governance choices? | No meaningful participation route exists. |
| Proportionality | Are burdens and exclusions justified against the stated purpose? | Less intrusive alternatives are not considered. |
| Independent review | Can material choices be reviewed by an operationally independent body? | Review remains controlled by the reviewed body. |
| Transparency | Can consequential governance choices and their basis be inspected? | Decision criteria or material findings are unavailable. |
| Affected-party representation | Can affected-party input influence, challenge or correct outcomes? | Participation is recorded but never dispositioned. |

## Formal mandate versus legitimacy evidence

A conforming assessment should keep these propositions separate. An adoption may have a valid legal, policy, contractual or institutional mandate while still recording `partially-supported` or `gap-identified` legitimacy dimensions. That distinction prevents formal constitution from becoming an automatic proxy for fairness, accessibility, proportionality or independent scrutiny.

This profile is informative assurance guidance; it does not add a new legal validity test to core ONDTF conformance.
