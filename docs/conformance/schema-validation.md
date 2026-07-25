---
title: Schema validation and conformance fixtures
parent: Conformance and Accreditation
nav_order: 11
---

# Schema validation and conformance fixtures

ONDTF treats JSON Schema as an enforceable control. The authoritative mapping between schemas, valid instances, and intentionally invalid fixtures is `model/conformance/schema-instance-manifest.yaml`.

## Validation contract

For every registered schema, the repository provides at least one conforming instance and one negative fixture. A negative fixture declares the JSON Schema validator keyword that must reject it. CI fails when a valid instance is rejected, an invalid instance is accepted, or an invalid instance fails for a reason other than the declared expectation.

The validator writes machine-readable evidence to `artifacts/conformance/schema-validation-report.json`. This report is uploaded by CI and can be tied to the commit and workflow run that produced it.

## Adding a schema or instance

1. Add or update the Draft 2020-12 schema under `model/`.
2. Add representative valid content under `examples/` or register an authoritative repository instance.
3. Add at least one intentionally invalid fixture under `examples/conformance/schema-fixtures/`.
4. Register both in `model/conformance/schema-instance-manifest.yaml`.
5. Run `python3 scripts/validate_schema_instances.py` or `make validate`.

Negative fixtures are test evidence, not examples for implementation. They must remain visibly segregated from authoritative registers and production-oriented examples.
