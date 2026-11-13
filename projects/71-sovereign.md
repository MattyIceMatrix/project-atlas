# 71 · SOVEREIGN

```text
    +-----------------------------------------------+
    |  identity | models | RAG | agents | audit     |   on-prem, EU-only
    |  k8s  |  GPU nodes  |  storage  |  backups    |
    +-----------------------------------------------+
```

**EU sovereign AI reference stack, on-prem**

> A full AI platform a German Mittelstand company could run in its own basement.

```text
  TRACK K MASTERPIECE: TRUST, SECURITY AND SOVEREIGNTY  |  LEVEL [#####]  |  ~18 MONTHS  |  BUDGET €200 on top of cluster
```

## The mission

European organisations want AI without sending data to non-EU clouds, and lack a reference blueprint.

## How it works

```text
+-------------------------------+
|  IaC cluster                  |
+-------------------------------+
               |
               v
+-------------------------------+
|  identity + policy            |
+-------------------------------+
               |
               v
+-------------------------------+
|  model serving                |
+-------------------------------+
               |
               v
+-------------------------------+
|  RAG + agents                 |
+-------------------------------+
               |
               v
+-------------------------------+
|  audit + compliance evidence  |
+-------------------------------+
```

## Kit

- Kubernetes
- Keycloak
- vLLM
- open-weight models
- OpenFGA
- Loki
- Velero

**Hardware:** Home lab cluster (HOMECLUSTER)

## Campaign

```text
  P1  [=====]                     m0-4.5    Reference architecture and threat model
  P2        [=====]               m4.5-9    Platform deployment as code with identity and policy
  P3              [=====]         m9-13.5   AI services with audit trails
  P4                    [=====]   m13.5-18  Compliance evidence pack mapped to GDPR, NIS2, AI Act articles
```

## Gate: done when you can show

```text
  [ ] time to deploy from zero
  [ ] controls with evidence
  [ ] restore time from backup
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Compliance mappings are drafts for qualified review.

## Resume line (fill with your measured numbers)

> Built an on-prem EU AI reference stack deployable from zero in [N] h with evidence for [N] controls.

**Skills it proves:** platform architecture · compliance engineering · IaC

## System map

```text
  SOVEREIGN SYSTEM MAP

+-----------------+    +-----------------+    +-----------------+
|  cluster        |--->|  identity       |--->|  model serving  |
+-----------------+    +-----------------+    +-----------------+
        |
        v
+-----------------+    +-----------------+
|  AI services    |--->|  evidence pack  |
+-----------------+    +-----------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   TRL 5 -> 6
  PUBLICATION TARGET     Talk at a German IT security or cloud-native event
```

## Deliverables

- Reference architecture
- IaC repo
- Evidence pack templates
- Whitepaper

## Standards and regulations to meet

- GDPR
- NIS2
- EU AI Act
- BSI IT-Grundschutz (reference)
- ISO/IEC 27001

## Defend it

1. What does sovereignty mean technically, beyond data location?
2. Which NIS2 duties affect an AI platform?
3. How do you prove a backup actually restores?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/sovereign  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- HOMECLUSTER](70-homecluster.md) · [atlas index](../README.md) · [ENCLAVE ->](72-enclave.md)
