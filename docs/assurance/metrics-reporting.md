---
layout: default
title: Metrics and Reporting
parent: Assurance, Risk and Resilience
nav_order: 8
---

# Metrics and reporting

Metrics provide evidence about system condition and outcomes. They do not replace judgement, and they MUST be interpreted with context to avoid incentives that optimise speed or volume at the expense of legitimacy, privacy, security or remedy.

## Minimum metric families

| Family | Illustrative measures |
|---|---|
| Authority integrity | stale delegations, invalid authority chains, unauthorised effect attempts |
| Service reliability | availability, latency, recovery time, status propagation delay |
| Control performance | control test pass rate, configuration drift, evidence expiry |
| Security | detection time, containment time, repeated incidents, unresolved critical findings |
| Assurance | overdue reviews, conditional conclusions, surveillance failures |
| Decision quality | false acceptance, false rejection, defer rate, unexplained decision rate |
| Redress | complaint volume, resolution time, remedy completion, repeat harm |
| Ecosystem health | dependency concentration, interoperability failures, participant exits |

Metrics SHOULD have an accountable owner, definition, data source, calculation method, threshold, review cadence and known limitations. A profile SHOULD identify which metrics are public, regulator-visible, scheme-confidential or security-sensitive.
