# 78 · PROVENGUARD

```text
    theorem no_unapproved_action :
      forall req, decide(req) = ALLOW -> approved(req) \/ low_risk(req)
    -- proved.  (Lean 4 / Dafny)
```

**Formally verified guardrail policy engine**

> A policy engine with a mathematical proof that it never allows what it shouldn't.

```text
  TRACK K MASTERPIECE: TRUST, SECURITY AND SOVEREIGNTY  |  LEVEL [#####]  |  ~18 MONTHS  |  BUDGET €0
```

## The mission

Guardrails are code, and code has bugs; for safety-critical AI that's not good enough.

## How it works

```text
+----------------------------+
|  policy language           |
+----------------------------+
              |
              v
+----------------------------+
|  formal semantics          |
+----------------------------+
              |
              v
+----------------------------+
|  verified decision engine  |
+----------------------------+
              |
              v
+----------------------------+
|  extracted code            |
+----------------------------+
              |
              v
+----------------------------+
|  runtime                   |
+----------------------------+
```

## Kit

- Dafny or Lean 4
- Rust or Python extraction
- property-based tests

**Hardware:** None

## Campaign

```text
  P1  [=====]                     m0-4.5    Policy language and formal semantics
  P2        [=====]               m4.5-9    Verified decision procedure with key safety theorems
  P3              [=====]         m9-13.5   Extraction to runnable code and integration with LANTERN's Guardian
  P4                    [=====]   m13.5-18  Differential testing against the unverified engine
```

## Gate: done when you can show

```text
  [ ] theorems proved
  [ ] discrepancies found by differential testing
  [ ] decision latency
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

None special.

## Resume line (fill with your measured numbers)

> Built a formally verified guardrail engine (Dafny) with proofs of [N] safety properties, deployed in LANTERN.

**Skills it proves:** formal verification · programming languages · AI safety

## System map

```text
  PROVENGUARD SYSTEM MAP

+-------------------+    +-------------------+    +-------------------+
|  policy DSL       |--->|  semantics        |--->|  verified engine  |
+-------------------+    +-------------------+    +-------------------+
         |
         v
+-------------------+    +-------------------+
|  extractor        |--->|  runtime adapter  |
+-------------------+    +-------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   TRL 3 -> 4
  PUBLICATION TARGET     Formal methods conference (FM, CAV workshop) or AI safety workshop
```

## Deliverables

- Verified engine
- Proof documentation
- Integration
- Paper

## Standards and regulations to meet

- DO-178C / IEC 61508 formal methods concepts (reference)

## Defend it

1. What does your proof assume about the world?
2. What is the gap between verified model and running code?
3. Why prove properties instead of testing more?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/provenguard  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- PROVENANCE](77-provenance.md) · [atlas index](../README.md) · [OTSENTINEL ->](79-otsentinel.md)
