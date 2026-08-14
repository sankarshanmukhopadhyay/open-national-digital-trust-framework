---
layout: default
title: Status Resolution Privacy and Freshness Comparison
parent: Privacy
nav_order: 20
---
# Status resolution privacy and freshness comparison

This candidate comparison addresses `URI-05` at the architecture/test level while preserving implementation-specific privacy assessment.

| Pattern | Correlation exposure | Freshness strength | Offline capability | Candidate treatment |
|---|---|---|---|---|
| Online subject-specific query | High unless protected | Strong | No | profile must document query leakage and access controls |
| Batch/list publication | Lower verifier-to-authority linkage; broader publication risk | Depends on publication cadence | Yes | profile must bound list age and disclosure surface |
| Privacy-preserving accumulator/status proof | Potentially low | Strong when witness/update semantics are current | Possible | profile must specify cryptographic/update failure behaviour |
| Cached online result | Medium | Degrades with cache age | Temporary | `CAL-101` or stricter profile rule bounds age |

`INT-004` exercises stale-status rejection across both repository implementations. This evidence demonstrates freshness semantics; it does not prove privacy properties of any particular deployed protocol.
