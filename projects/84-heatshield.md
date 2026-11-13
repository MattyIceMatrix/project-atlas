# 84 · HEATSHIELD

```text
    forecast: 36C x 3 days
    [####....]  district A  high exposure + many elderly + few trees
    [##......]  district B
```

**City heat-wave early warning and vulnerability map**

> Who is at risk in the next heat wave, street by street.

```text
  TRACK L MASTERPIECE: PLANET, CLIMATE AND INFRASTRUCTURE  |  LEVEL [#####]  |  ~12 MONTHS  |  BUDGET €0
```

## The mission

Heat waves kill quietly; help reaches the right people too late.

## How it works

```text
+------------------------------------------------------------+
|  weather forecasts + land surface temp + open census data  |
+------------------------------------------------------------+
                              |
                              v
+------------------------------------------------------------+
|  risk index                                                |
+------------------------------------------------------------+
                              |
                              v
+------------------------------------------------------------+
|  alerts for social services (advisory)                     |
+------------------------------------------------------------+
```

## Kit

- Python
- DWD open data
- Landsat
- GeoPandas
- dashboard

**Hardware:** None

## Campaign

```text
  P1  [=====]                     m0-3      Heat exposure layers (from GREENLINE)
  P2        [=====]               m3-6      Vulnerability index from aggregated open data
  P3              [=====]         m6-9      Validation against historical heat events
  P4                    [=====]   m9-12     Advisory dashboard co-designed with a city office
```

## Gate: done when you can show

```text
  [ ] index correlation with past heat impacts
  [ ] lead time
  [ ] users in city pilot
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Aggregated data only; no individual profiling.

## Resume line (fill with your measured numbers)

> Built a district-level heat risk index validated against past events, piloted with [N] city users.

**Skills it proves:** climate adaptation · GIS · public-sector product

## System map

```text
  HEATSHIELD SYSTEM MAP

+-----------------------+    +-----------------------+    +-----------------------+
|  exposure layers      |--->|  vulnerability index  |--->|  forecast ingest      |
+-----------------------+    +-----------------------+    +-----------------------+
           |
           v
+-----------------------+    +-----------------------+
|  alerting             |--->|  dashboard            |
+-----------------------+    +-----------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   TRL 4 -> 6 (pilot)
  PUBLICATION TARGET     Climate services conference
```

## Deliverables

- Index method
- Dashboard
- Pilot report
- Open data package

## Standards and regulations to meet

- GDPR aggregation
- INSPIRE (reference)

## Defend it

1. Why aggregate instead of household-level?
2. How do you validate a vulnerability index?
3. What action does the warning enable?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/heatshield  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- PLUMEWATCH](83-plumewatch.md) · [atlas index](../README.md) · [LEAKNET ->](85-leaknet.md)
