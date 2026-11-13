# 30 · RIVERFLOW

```text
    PEGELONLINE API ~~> [ ingest ] ~~> bronze ~~> silver ~~> gold
                                                        |
                                      "Which gauges rose fastest in the last 6 h?"
```

**Streaming lakehouse for German open water data**

> Every river gauge in Germany, live, queryable.

```text
  TRACK E CLOUD, DATA AND MLOPS  |  LEVEL [###..]  |  ~3 MONTHS  |  BUDGET €0–10/month
```

## The mission

Open gauge data exists (PEGELONLINE) but is hard to analyse historically and in real time.

## How it works

```text
+---------------------------+
|  API poller               |
+---------------------------+
             |
             v
+---------------------------+
|  Kafka/Redpanda           |
+---------------------------+
             |
             v
+---------------------------+
|  Delta or Iceberg tables  |
+---------------------------+
             |
             v
+---------------------------+
|  dbt models               |
+---------------------------+
             |
             v
+---------------------------+
|  dashboard                |
+---------------------------+
```

## Kit

- Redpanda
- Apache Iceberg or Delta Lake
- DuckDB
- dbt
- Superset

**Hardware:** Laptop or one cloud VM

## Campaign

```text
  P1  [=====]                     m0-0.8    Ingest with schema and data-quality checks
  P2        [=====]               m0.8-1.5  Medallion layers and dbt models
  P3              [=====]         m1.5-2.2  Rise-rate analytics and alerts
  P4                    [=====]   m2.2-3    Feeds TIDEWATCH and LANTERN with history
```

## Gate: done when you can show

```text
  [ ] ingest lag
  [ ] data quality test pass rate
  [ ] query time
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Follow the data licence and attribution.

## Resume line (fill with your measured numbers)

> Built a streaming lakehouse over [N] German river gauges with [N] s ingest lag and tested data quality.

**Skills it proves:** data engineering · streaming · dbt

## Defend it

1. Why bronze/silver/gold?
2. How do you handle a gauge that sends nonsense?

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/riverflow  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- CONVEYOR](29-conveyor.md) · [atlas index](../README.md) · [FEATUREFORGE ->](31-featureforge.md)
