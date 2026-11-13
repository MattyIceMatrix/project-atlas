# 10 · VERITAS

```text
   answer:  "Torque the bolt to 45 Nm [3]"
                                   |
   source [3]: "...tighten to 45 Nm..."   ==> SUPPORTED
   source [5]: "...inspect annually..."   ==> NOT SUPPORTED (removed)
```

**Citation-checked RAG for technical manuals**

> Every sentence shows its receipt.

```text
  TRACK B GENERATIVE AI AND LLM SYSTEMS  |  LEVEL [###..]  |  ~3 MONTHS  |  BUDGET €0–30
```

## The mission

RAG systems cite sources that don't actually support the claim.

## How it works

```text
+------------------------------+
|  retrieve                    |
+------------------------------+
               |
               v
+------------------------------+
|  generate with citations     |
+------------------------------+
               |
               v
+------------------------------+
|  claim splitter              |
+------------------------------+
               |
               v
+------------------------------+
|  entailment checker          |
+------------------------------+
               |
               v
+------------------------------+
|  keep only supported claims  |
+------------------------------+
```

## Kit

- Python
- sentence-transformers
- NLI model
- Qdrant
- pytest

**Hardware:** Laptop or cloud GPU hours

## Campaign

```text
  P1  [=====]                     m0-0.8    Corpus of public manuals and a question set
  P2        [=====]               m0.8-1.5  Baseline RAG and citation precision measurement
  P3              [=====]         m1.5-2.2  Claim-level entailment verification
  P4                    [=====]   m2.2-3    Report showing before/after faithfulness
```

## Gate: done when you can show

```text
  [ ] citation precision
  [ ] answer faithfulness
  [ ] latency overhead
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Use public-domain or permissively licensed manuals.

## Resume line (fill with your measured numbers)

> Raised RAG citation precision from [N]% to [N]% with claim-level entailment checks.

**Skills it proves:** RAG · evaluation · NLI

## Masterpiece upgrade path

```text
   LEVEL [###..]  ====================>  LEVEL [#####]
```

Enterprise-grade verified RAG with permissions, continuous evals and published faithfulness benchmarks.

**Grows into:** [RAGOPS](65-ragops.md) · **Publication target:** ACL/EMNLP industry track

## Defend it

1. Why check claims and not whole answers?
2. What does your verifier get wrong?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/veritas  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- AMTSDEUTSCH](09-amtsdeutsch.md) · [atlas index](../README.md) · [SKILLBRIDGE-COPILOT ->](11-skillbridge-copilot.md)
