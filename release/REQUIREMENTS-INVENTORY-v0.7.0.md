# v0.7.0 requirements and conformance inventory

The canonical requirement source remains `model/normative/requirement-catalogue.yaml`. The v0.7.0 conformance foundation does not duplicate requirement text: `conformance/assertions.yaml` references stable requirement IDs and classifies evaluation as machine-executable, assessor-verifiable or judgement-dependent.

Critical release rule: every new executable assertion must reference an existing normative requirement, and repository validation rejects unknown requirement IDs.
