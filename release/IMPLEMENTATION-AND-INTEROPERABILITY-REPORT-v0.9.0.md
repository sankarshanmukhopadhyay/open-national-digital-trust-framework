# v0.9.0 Implementation and Interoperability Report

## Implementations

- **Implementation A:** the existing informative Python reference implementation.
- **Implementation B:** a separately authored repository-local codebase that does not import Implementation A business logic.

## Matrix

`INT-EVT-001` executes positive, suspended-provider, revoked-authority, stale-status and scope-mismatch cases against both codebases. All five candidate semantic cases pass.

## Claim boundary

This demonstrates cross-codebase semantic consistency under `IPR-001`. It is **not** represented as evidence from an externally operated independent team, deployment environment, legal scheme or production service.
