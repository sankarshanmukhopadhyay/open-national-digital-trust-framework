# ONDTF reference implementation

**Status:** informative, non-production, non-normative demonstration artefact.

This implementation exercises externally observable ONDTF behaviours from canonical repository models. It intentionally avoids selecting a production identity, credential, cryptographic, database, or registry technology. The normative source remains the ONDTF specification and machine-readable models.

## Demonstrated behaviours

- load the canonical provider lifecycle;
- enforce authorised lifecycle transitions;
- evaluate bounded delegated authority by scope and time;
- reject suspended providers for active operations;
- emit inspectable decision receipts;
- preserve an append-only audit event view;
- expose deterministic fixtures for conformance tests.

Run `python3 reference-implementation/tests/run_tests.py` from the repository root.
