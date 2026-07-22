---
layout: default
title: Profile Validation
parent: Profiles
nav_order: 7
---
# Profile validation

Validation tests whether a profile package is structurally complete, normatively traceable, governable, and implementable.

## Minimum validation gates

- profile identity, authority, status, and review owner are present;
- scope, exclusions, affected parties, and harms are explicit;
- every core requirement has a treatment and rationale;
- profile requirements use stable identifiers;
- roles and decision rights are complete and separation conflicts are addressed;
- assurance claims name dimensions, levels, evidence, freshness, and failure outcomes;
- lifecycle and conformance states are aligned;
- external dependencies have adoption records and review triggers;
- rights and remedy obligations produce operational evidence;
- unresolved decisions are visible and block activation where material;
- composition conflicts are resolved or prohibited;
- maintenance, migration, and retirement are defined.

`python3 scripts/validate_profile_adoption.py` performs structural checks over the profile, adoption, maintenance, and guided-construction models.

[Previous: Versioning and Change](profile-versioning-and-change.md) · [Next: Guided Framework Construction](../docs/adoption/guided-framework-construction.md)
