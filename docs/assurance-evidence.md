---
layout: default
title: Assurance Evidence
---

# Assurance evidence contract

The framework's portfolio assurance claims are backed by repository-native GitHub Actions evidence.

| Claim | Required control | Freshness expectation |
|---|---|---|
| Specification quality | `.github/workflows/quality.yml` | Successful execution covering the governed `main` revision |
| Publication integrity | `.github/workflows/pages.yml` | Successful execution covering the governed `main` revision |

Documentation assertions are not substitutes for executed controls.

Portfolio finding lineage: `PF-EE7FADD90617`, `PF-7AB5F3D457EE` (issue #3).

## Retest rule

After both required workflows succeed for the governed `main` revision, rerun the Portfolio Assurance Monitor. Close only when both fingerprints are recorded as resolved.
