---
layout: default
title: Cryptographic Protection and Key Management
parent: Data Security
nav_order: 4
grand_parent: Open National Digital Trust Framework
---


# Cryptographic protection and key management

Cryptography protects confidentiality, integrity, authenticity, and non-repudiation only when algorithms, keys, identities, policy, and operations remain governed together.

```mermaid
flowchart LR
  P[Policy and approved algorithms] --> G[Generate]
  G --> D[Distribute or provision]
  D --> U[Use]
  U --> R[Rotate]
  R --> V[Revoke]
  V --> X[Destroy]
  M[Monitoring and inventory] -.-> G
  M -.-> U
  M -.-> R
  M -.-> V
```

Implementations SHOULD maintain a cryptographic inventory, approved-algorithm policy, key ownership record, hardware protection requirements, separation of duties, rotation and revocation procedures, compromise response, backup and recovery controls, and migration plans for cryptographic agility.

Encryption SHALL NOT be treated as permission to collect, retain, or correlate data. Privacy requirements continue to apply to encrypted data.
