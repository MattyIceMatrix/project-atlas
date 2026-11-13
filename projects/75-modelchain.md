# 75 · MODELCHAIN

```text
    data@sha --> train@commit --> model.safetensors --sign--> registry --verify--> deploy
                   provenance attestation (SLSA L3)
```

**Signed, provenance-tracked ML model supply chain**

> Know exactly which data and code produced the model in production.

```text
  TRACK K MASTERPIECE: TRUST, SECURITY AND SOVEREIGNTY  |  LEVEL [#####]  |  ~12 MONTHS  |  BUDGET €0
```

## The mission

Model files are swapped, poisoned or untraceable; ML has no software-grade supply chain.

## How it works

```text
+-------------------------------+
|  hermetic training builds     |
+-------------------------------+
               |
               v
+-------------------------------+
|  provenance attestations      |
+-------------------------------+
               |
               v
+-------------------------------+
|  model signing                |
+-------------------------------+
               |
               v
+-------------------------------+
|  admission control at deploy  |
+-------------------------------+
```

## Kit

- GitHub Actions
- Sigstore/cosign
- in-toto
- model-signing tools
- Kyverno

**Hardware:** None

## Campaign

```text
  P1  [=====]                     m0-3      Hermetic, reproducible training pipeline
  P2        [=====]               m3-6      Provenance attestations for data, code and model
  P3              [=====]         m6-9      Signing and verification for model files
  P4                    [=====]   m9-12     Kubernetes admission policy that rejects unsigned models
```

## Gate: done when you can show

```text
  [ ] reproducibility (bit-identical or not)
  [ ] unsigned deployments blocked
  [ ] verification latency
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

None special.

## Resume line (fill with your measured numbers)

> Built an SLSA-style ML supply chain; 100% of unsigned or untraceable models blocked at deploy.

**Skills it proves:** supply-chain security · MLOps · policy

## System map

```text
  MODELCHAIN SYSTEM MAP

+------------------------+    +------------------------+    +------------------------+
|  build pipeline        |--->|  attestor              |--->|  signer                |
+------------------------+    +------------------------+    +------------------------+
            |
            v
+------------------------+    +------------------------+
|  registry              |--->|  admission controller  |
+------------------------+    +------------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   TRL 5 -> 6
  PUBLICATION TARGET     OpenSSF or supply-chain security talk
```

## Deliverables

- Reference pipeline
- Policies
- Threat model
- Guide

## Standards and regulations to meet

- SLSA v1.0
- in-toto
- Sigstore

## Defend it

1. What does provenance prove that a signature alone doesn't?
2. Why is bit-for-bit reproducible training hard?
3. What attack does this stop, and which one doesn't it stop?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/modelchain  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- AUTOSOC](74-autosoc.md) · [atlas index](../README.md) · [DPVAULT ->](76-dpvault.md)
