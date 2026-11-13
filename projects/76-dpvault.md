# 76 · DPVAULT

```text
    query: "avg response time by district"
      --> [ budget check: eps 0.5 left ] --> answer + noise --> analyst
```

**Differential privacy analytics platform**

> Useful statistics, provably private individuals.

```text
  TRACK K MASTERPIECE: TRUST, SECURITY AND SOVEREIGNTY  |  LEVEL [#####]  |  ~12 MONTHS  |  BUDGET €0
```

## The mission

Sharing statistics about people leaks more than expected.

## How it works

```text
+-----------------------------+
|  SQL-like queries           |
+-----------------------------+
              |
              v
+-----------------------------+
|  privacy budget accounting  |
+-----------------------------+
              |
              v
+-----------------------------+
|  DP mechanisms              |
+-----------------------------+
              |
              v
+-----------------------------+
|  released results + audit   |
+-----------------------------+
```

## Kit

- OpenDP or Tumult Analytics
- Python
- Postgres
- Streamlit

**Hardware:** None

## Campaign

```text
  P1  [=====]                     m0-3      Threat model and use case (e.g. emergency response statistics)
  P2        [=====]               m3-6      DP query engine with budget accounting
  P3              [=====]         m6-9      Utility evaluation vs non-private answers
  P4                    [=====]   m9-12     Reconstruction-attack tests on released data
```

## Gate: done when you can show

```text
  [ ] utility error at given epsilon
  [ ] budget accounting correctness
  [ ] attack success rate
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Synthetic datasets for development.

## Resume line (fill with your measured numbers)

> Built a DP analytics platform answering queries within [N]% error at epsilon [N], defeating reconstruction attacks.

**Skills it proves:** privacy engineering · statistics · data platforms

## System map

```text
  DPVAULT SYSTEM MAP

+----------------+    +----------------+    +----------------+
|  query parser  |--->|  accountant    |--->|  mechanisms    |
+----------------+    +----------------+    +----------------+
        |
        v
+----------------+    +----------------+
|  release log   |--->|  attack lab    |
+----------------+    +----------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   TRL 4 -> 5
  PUBLICATION TARGET     Privacy engineering conference (e.g. PEPR)
```

## Deliverables

- Platform
- Utility report
- Attack report
- Policy guide

## Standards and regulations to meet

- GDPR anonymisation guidance
- NIST SP 800-226 (DP guidelines)

## Defend it

1. Why does every query spend privacy budget?
2. What is a reconstruction attack?
3. How would you explain epsilon to a city council?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/dpvault  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- MODELCHAIN](75-modelchain.md) · [atlas index](../README.md) · [PROVENANCE ->](77-provenance.md)
