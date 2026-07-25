---
layout: default
title: Assurance Requirements and Impact
parent: Assurance, Risk and Resilience
nav_order: 9
---
# Assurance requirements and impact

ONDTF does not assign a universal assurance level to an entity, service or transaction. The former A0–A3 shorthand is deprecated because it combined consequence, control strength, assessment independence and operational confidence. New profiles MUST express these separately.

## Required constructs

| Construct | Question | Machine-readable source |
|---|---|---|
| Decision Impact Class | How serious could failure or misuse be? | `decision-impact-classes.yaml` |
| Dimension Assurance Requirement | What evidence and controls are required for each dimension? | `assurance-requirement-levels.yaml` |
| Evaluation Rigour Class | How much confidence is justified in the assessment process? | `evaluation-rigour-classes.yaml` |
| Assurance State | Is reliance currently supported, constrained, degraded or prohibited? | `assurance-state-vocabulary.yaml` |

## Decision Impact Classes

DIC-0 through DIC-3 classify consequences, not achieved assurance. Profiles MUST derive the class from documented harms, affected parties, reversibility, rights, dependencies and systemic effects.

## Dimension requirements

ARL-B, ARL-S, ARL-H and ARL-C apply independently to ONDTF assurance dimensions. ARL-NA requires an explicit exclusion rationale. A strong result in one dimension MUST NOT compensate for a failed critical dimension.

## Migration from A0–A3

No automatic conversion is valid. Existing profile uses of A0–A3 must be reassessed by decision impact, dimension, evaluation rigour, freshness and current state.
