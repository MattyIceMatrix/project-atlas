# 73 · ZKAUDIT

```text
    vendor: "accuracy >= 90% on audit set"  + proof pi
    auditor: verify(pi) == TRUE   (never saw the weights)
```

**Zero-knowledge proofs for AI compliance claims**

> Prove the model passed the test without revealing the model.

```text
  TRACK K MASTERPIECE: TRUST, SECURITY AND SOVEREIGNTY  |  LEVEL [#####]  |  ~16 MONTHS  |  BUDGET €0
```

## The mission

Auditors need evidence; vendors won't hand over weights or data.

## How it works

```text
+------------------------------+
|  small model                 |
+------------------------------+
               |
               v
+------------------------------+
|  arithmetic circuit          |
+------------------------------+
               |
               v
+------------------------------+
|  ZK proof of inference/eval  |
+------------------------------+
               |
               v
+------------------------------+
|  public verifier             |
+------------------------------+
```

## Kit

- ezkl or halo2
- Rust
- Python
- small CNN or tree model

**Hardware:** Workstation

## Campaign

```text
  P1  [=====]                     m0-4      Literature review and threat model for audit claims
  P2        [=====]               m4-8      Proof of a single inference for a small model
  P3              [=====]         m8-12     Proof of an aggregate evaluation claim
  P4                    [=====]   m12-16    Cost analysis and limits paper
```

## Gate: done when you can show

```text
  [ ] proof time
  [ ] verification time
  [ ] max model size feasible
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

None special.

## Resume line (fill with your measured numbers)

> Built zero-knowledge proofs of model evaluation claims; proof time [N] s for a [N]-parameter model.

**Skills it proves:** zero-knowledge cryptography · ML · research

## System map

```text
  ZKAUDIT SYSTEM MAP

+--------------------+    +--------------------+    +--------------------+
|  model quantiser   |--->|  circuit compiler  |--->|  prover            |
+--------------------+    +--------------------+    +--------------------+
          |
          v
+--------------------+    +--------------------+
|  verifier          |--->|  audit protocol    |
+--------------------+    +--------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   TRL 2 -> 3 (research)
  PUBLICATION TARGET     Privacy/crypto or AI accountability workshop
```

## Deliverables

- Prototype
- Limits analysis
- Paper
- Demo

## Standards and regulations to meet

- EU AI Act conformity concepts (reference)

## Defend it

1. What exactly is being proven and to whom?
2. Why do ZK proofs scale badly with model size?
3. Where could the vendor still cheat?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/zkaudit  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- ENCLAVE](72-enclave.md) · [atlas index](../README.md) · [AUTOSOC ->](74-autosoc.md)
