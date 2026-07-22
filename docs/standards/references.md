---
layout: default
title: Standards, Specifications and Guidelines Register
parent: Standards Profile
nav_order: 3
---

# Standards, specifications and guidelines register

This is the single maintained catalogue of external standards, specifications, guidelines and jurisdictional instruments referenced by ONDTF. The machine-readable source is [`model/references/standards-register.yaml`]({{ '/model/references/standards-register.yaml' | relative_url }}). Pages citing an external reference SHOULD link to the corresponding entry here rather than duplicating version and status information.

## Reference classes

| Class | Meaning |
|---|---|
| Foundational | Informs ONDTF concepts or methods across profiles. |
| Profile-dependent | Becomes required only when selected by an adoption or interoperability profile. |
| Informative mapping | Supports comparison and traceability without asserting equivalence, certification or conformance. |
| Jurisdiction profile | Applies only where selected by a jurisdiction profile and subject to current legal review. |

## Citation rule

Each citation MUST identify a stable register identifier. Drafts and candidate publications MUST be described using their actual publication status. A mapping to an external publication does not make that publication universally normative for ONDTF and does not establish certification or regulatory compliance.

## Complete register

<div class="ondtf-table-scroll" role="region" aria-label="Complete ONDTF standards register" tabindex="0">
<table class="ondtf-reference-table">
  <thead>
    <tr>
      <th scope="col">Identifier</th>
      <th scope="col">Publisher</th>
      <th scope="col">Publication</th>
      <th scope="col">Status</th>
      <th scope="col">ONDTF use</th>
      <th scope="col">Class</th>
    </tr>
  </thead>
  <tbody>
{% assign sorted_refs = site.data.standards_register.references | sort: "id" %}
{% for ref in sorted_refs %}
    <tr id="ref-{{ ref.id }}">
      <td><code>{{ ref.id }}</code></td>
      <td>{{ ref.publisher }}</td>
      <td><a href="{{ ref.canonical_url }}">{{ ref.title }}</a></td>
      <td>{{ ref.status }}</td>
      <td>{{ ref.ondtf_use }}</td>
      <td>{{ ref.class }}</td>
    </tr>
{% endfor %}
  </tbody>
</table>
</div>

The table is horizontally scrollable on narrow screens. Each row has a stable anchor of the form `#ref-IDENTIFIER`, which is the canonical target for citations elsewhere in ONDTF.

## Maintenance

The register MUST be reviewed before each minor or major ONDTF release. Review includes publication status, edition, canonical URL, supersession, ONDTF usage and classification. Historical references MAY remain when required for traceability, but MUST be marked as superseded or withdrawn and MUST NOT be presented as current.
