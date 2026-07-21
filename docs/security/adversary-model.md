---
layout: default
title: Adversary Model
parent: Security Architecture
nav_order: 9
---
# Adversary model

ONDTF classifies adversaries by position, access, capability, motivation, and persistence. A named actor type is not presumed malicious merely because it appears in this catalogue. The model identifies positions from which harmful or deceptive action can occur.

| ID | Adversary position | Access position | Typical motivation |
|---|---|---|---|
| `ADV-01` | Unauthenticated external attacker | outside | fraud, disruption or reconnaissance |
| `ADV-02` | Malicious authenticated participant | participant | benefit, exclusion or evasion |
| `ADV-03` | Compromised participant | participant | controlled by another actor |
| `ADV-04` | Malicious insider | organisation | abuse of legitimate access |
| `ADV-05` | Privileged administrator | control plane | covert or overt privilege abuse |
| `ADV-06` | Compromised issuer or evidence provider | evidence plane | false or manipulated assertions |
| `ADV-07` | Compromised registry or resolver | trust resolution | status or recognition manipulation |
| `ADV-08` | Negligent or captured scheme operator | governance plane | institutional capture or operational neglect |
| `ADV-09` | Foreign or federated trust domain | federation boundary | semantic or assurance mismatch |
| `ADV-10` | Compromised software supplier | supply chain | persistent ecosystem access |
| `ADV-11` | Autonomous agent outside mandate | agent execution | goal drift or manipulated execution |
| `ADV-12` | Colluding ecosystem participants | multiple positions | laundering authority or evidence |
| `ADV-13` | Coercive principal or intermediary | delegation relationship | abuse of another party |
| `ADV-14` | State-level or systemic adversary | ecosystem | strategic disruption or surveillance |

## Analysis obligations

Threat analysis MUST consider collusion, coercion, compromise, negligent operation, and governance capture. It MUST NOT assume that authentication, certification, public-sector status, or participation in a recognised federation eliminates adversarial potential.

The machine-readable source is [`model/security/adversaries.yaml`](../../model/security/adversaries.yaml).
