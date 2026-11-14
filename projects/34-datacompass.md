# 34 · DATACOMPASS

```text
    src.orders --> stg_orders --> fct_sales --> "Revenue" tile
          \                         ^
           '--> stg_customers ------'
```

**Data lineage and catalogue**

> Click a dashboard number, see every table it came from.

```text
  TRACK E CLOUD, DATA AND MLOPS  |  LEVEL [##...]  |  ~2 MONTHS  |  BUDGET €0
```

## The mission

Nobody knows which dashboards break when a source changes.

## How it works

```text
+--------------------------+
|  parse dbt/SQL           |
+--------------------------+
             |
             v
+--------------------------+
|  lineage graph           |
+--------------------------+
             |
             v
+--------------------------+
|  catalogue UI            |
+--------------------------+
             |
             v
+--------------------------+
|  impact analysis on PRs  |
+--------------------------+
```

## Kit

- OpenLineage
- Marquez or DataHub
- dbt
- Python

**Hardware:** Laptop

## Campaign

```text
  P1  [=====]                     m0-0.5    Lineage capture from dbt and SQL
  P2        [=====]               m0.5-1    Catalogue with owners and descriptions
  P3              [=====]         m1-1.5    PR impact comments
  P4                    [=====]   m1.5-2    Demo on RIVERFLOW
```

## Gate: done when you can show

```text
  [ ] tables covered
  [ ] impact analysis accuracy
  [ ] time to answer "what breaks?"
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

None special.

## Resume line (fill with your measured numbers)

> Added lineage and PR impact analysis across [N] tables, answering 'what breaks?' in seconds.

**Skills it proves:** data governance · graphs · tooling

## Masterpiece upgrade path

```text
   LEVEL [##...]  ====================>  LEVEL [#####]
```

Lineage across data, models and provenance attestations for full audit trails.

**Grows into:** [MODELCHAIN](75-modelchain.md) · **Publication target:** Data governance talk

## Defend it

1. Column-level vs table-level lineage: worth it?
2. Who owns a dataset and why does it matter?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/datacompass  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- WATCHTOWER](33-watchtower.md) · [atlas index](../README.md) · [SPOTFLEET ->](35-spotfleet.md)
