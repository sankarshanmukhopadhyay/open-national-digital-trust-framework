---
layout: default
title: Validation Report
parent: Worked Operational Profile
nav_order: 6
---
# Integrated validation report

The worked profile is validated as a single package rather than as disconnected documents.

## Automated checks

- all applicable guided questions have responses;
- every response uses a permitted decision state;
- conditional recognition questions are present when recognition is enabled;
- selected patterns exist in the pattern catalogue;
- all eleven stages satisfy their structural gate;
- profile manifest, decision register, review register and risk register are present;
- critical assurance floors are defined;
- prohibited role combinations are recorded;
- at least one independent appeal route and one executable remedy exist;
- internal planning labels are absent from published artefacts;
- the example remains reproducible from the checked-in construction response.

## Readiness interpretation

The package is structurally complete and internally coherent. It is not deployment-ready because the authority basis is intentionally illustrative. This is reported as a review qualification, not hidden as a successful result.

Run:

```bash
python3 scripts/validate_worked_profile.py
```

[Previous: Risk, Recognition and Maintenance](risk-recognition-and-maintenance.md) · [Next: Guided Framework Construction](../../docs/adoption/guided-framework-construction.md)
