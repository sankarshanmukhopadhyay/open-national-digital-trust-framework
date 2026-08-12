# Independent implementation pilot 01

**Pilot type:** controlled clean-room simulation for v0.7.0 implementation evaluation.

The pilot implementation is intentionally separate from `reference-implementation/` and does not import its business logic. It consumes published ONDTF models and records questions through the clarification register. This is useful implementation evidence, but it does **not** substitute for evidence from an external implementer; that limitation remains explicit in the release evidence.

## Protocol

1. treat published specification, profiles and machine-readable models as the only authoritative inputs;
2. record ambiguity instead of relying on private author guidance;
3. implement observable behaviour independently;
4. execute common fixtures;
5. classify findings as specification ambiguity, documentation gap, implementation choice or defect;
6. feed accepted findings back into documentation and tests.
