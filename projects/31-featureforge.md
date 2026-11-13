# 31 · FEATUREFORGE

```text
    offline store (parquet) <---- same definitions ----> online store (redis)
           |                                                   |
        training                                            serving
```

**Minimal feature store built from scratch**

> The same feature at training time and at 3 a.m. in production.

```text
  TRACK E CLOUD, DATA AND MLOPS  |  LEVEL [###..]  |  ~3 MONTHS  |  BUDGET €0
```

## The mission

Training/serving skew silently ruins models.

## How it works

```text
+-------------------------------+
|  feature definitions in code  |
+-------------------------------+
               |
               v
+-------------------------------+
|  batch materialisation        |
+-------------------------------+
               |
               v
+-------------------------------+
|  online sync                  |
+-------------------------------+
               |
               v
+-------------------------------+
|  point-in-time joins          |
+-------------------------------+
```

## Kit

- Python
- DuckDB
- Redis
- Feast for comparison

**Hardware:** Laptop

## Campaign

```text
  P1  [=====]                     m0-0.8    Feature definition DSL
  P2        [=====]               m0.8-1.5  Point-in-time correct joins with tests
  P3              [=====]         m1.5-2.2  Online store sync
  P4                    [=====]   m2.2-3    Compare to Feast and write up the trade-offs
```

## Gate: done when you can show

```text
  [ ] skew detected in tests
  [ ] online read p99
  [ ] materialisation time
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

None special.

## Resume line (fill with your measured numbers)

> Built a feature store with point-in-time joins, eliminating measured train/serve skew.

**Skills it proves:** data systems · correctness · MLOps

## Masterpiece upgrade path

```text
   LEVEL [###..]  ====================>  LEVEL [#####]
```

Production feature platform serving the grid and heat projects with lineage and quality SLAs.

**Grows into:** [GRIDBRAIN](82-gridbrain.md), [HEATSHIELD](84-heatshield.md) · **Publication target:** Data engineering conference

## Defend it

1. What is data leakage in a point-in-time join?
2. When would you just use Feast?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/featureforge  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- RIVERFLOW](30-riverflow.md) · [atlas index](../README.md) · [COLDSTART ->](32-coldstart.md)
