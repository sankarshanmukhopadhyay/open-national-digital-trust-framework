---
layout: default
title: Retention, Archival and Secure Destruction
parent: Data Security
nav_order: 6
grand_parent: Open National Digital Trust Framework
---


# Retention, archival and secure destruction

Retention SHALL be connected to purpose, legal or governance basis, accountability needs, dispute windows, and minimisation. Indefinite retention by default is not acceptable.

A retention rule SHOULD specify the triggering event, duration, permitted extensions, legal holds, archival conditions, review owner, deletion method, replicas and backups affected, and evidence of completion.

```mermaid
flowchart LR
  A[Active purpose] --> E{Purpose or duty ended?}
  E -->|No| A
  E -->|Yes| H{Hold or accountability need?}
  H -->|Yes| R[Restricted archive]
  H -->|No| D[Secure destruction]
  R --> Q[Periodic review]
  Q --> H
  D --> P[Destruction evidence]
```
