---
layout: default
title: Conceptual Baseline
parent: Core Specification
nav_order: 2
---

# Conceptual baseline

The baseline is intentionally compact. It supplies enough shared meaning for governance and interoperability while allowing profiles to use richer domain models.

| Concept | Core meaning |
|---|---|
| Actor | A person, organisation, public body, device, service, or agent participating in an interaction |
| Authority | A recognised basis on which an actor may decide, direct, issue, verify, operate, or admit an effect |
| Delegation | A bounded transfer or assignment of authority from one actor to another |
| Participant | An actor admitted to a trust scheme or governed interaction |
| Affected party | A person or organisation whose rights, interests, access, obligations, or opportunities may be changed |
| Trust scheme | A governed arrangement defining participants, rules, assurance, services, and remedies |
| Policy | A rule, duty, prohibition, permission, or decision criterion |
| Evidence | Information used to support a claim, authority, decision, or assurance conclusion |
| Credential | A portable or queryable representation of claims made by an issuer |
| Registry | A governed source used to publish, discover, resolve, or evaluate authoritative information |
| Assurance | A justified level of confidence based on controls, evidence, assessment, and freshness |
| Trust decision | A determination about eligibility, acceptance, reliance, access, authority, or treatment |
| Effect | A change admitted into a legal, administrative, financial, technical, or social process |
| Incident | An event that threatens or compromises expected trust properties |
| Remedy | A corrective, restorative, compensatory, or preventive response |

## Decision chain

```mermaid
flowchart LR
  A[Actor] --> ID[Identity and role]
  ID --> AU[Authority]
  AU --> PO[Policy and duties]
  PO --> EV[Evidence]
  EV --> AS[Assurance]
  AS --> TD[Trust decision]
  TD --> EF[Admitted effect]
  EF --> AR[Accountability and redress]
```

Verification of evidence is necessary in many interactions, but it is not sufficient. A conforming framework must also address whether authority was current and bounded, whether duties were respected, whether an effect should be admitted, and how an affected party can challenge the outcome.
