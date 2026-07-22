---
layout: default
title: Profile Package Template
parent: Profiles
nav_order: 3
---
# Profile package template

A conforming profile package should contain both narrative and machine-readable artefacts.

## Human-readable documents

1. Profile identity, authority, version, and status
2. Purpose, scope, use cases, harms, affected parties, and exclusions
3. Legal and institutional context
4. Roles, separation of duties, oversight, and decision rights
5. Applicable core and profile requirements
6. Provider and service lifecycle
7. Assurance and evidence model
8. Conformance, accreditation, surveillance, and public status
9. Technical, registry, and external dependencies
10. Data security, privacy, accessibility, and rights
11. Incident coordination, challenge, appeal, and remedy
12. Recognition and interoperability
13. Exceptions, risk acceptance, and unresolved decisions
14. Maintenance, migration, review, and retirement

## Machine-readable package

```text
profile.yaml
requirements.yaml
roles.yaml
assurance.yaml
conformance.yaml
dependencies.yaml
risk-register.yaml
decision-register.yaml
review-register.yaml
```

Use `templates/profiles/profile-manifest.template.yaml` as the starting manifest. The generated package must distinguish inherited defaults, adopter decisions, profile-controlled selections, unresolved matters, and required expert or stakeholder review.

[Previous: Profile Methodology](profile-methodology.md) · [Next: Composition and Inheritance](profile-composition.md)
