# 89 · SURGECAST

```text
    water level
     |        __/\__   surge
     |  /\/\_/      \__/\/\   tide
     +---------------------------> t
```

**Storm-surge forecasting for the North Sea coast**

> The tide plus the storm, forecast with uncertainty.

```text
  TRACK L MASTERPIECE: PLANET, CLIMATE AND INFRASTRUCTURE  |  LEVEL [#####]  |  ~12 MONTHS  |  BUDGET €100
```

## The mission

Storm surge prediction is critical for coastal flood defence and needs good uncertainty estimates.

## How it works

```text
+------------------------------------+
|  tide gauges + reanalysis weather  |
+------------------------------------+
                  |
                  v
+------------------------------------+
|  probabilistic ML model            |
+------------------------------------+
                  |
                  v
+------------------------------------+
|  ensemble forecast                 |
+------------------------------------+
                  |
                  v
+------------------------------------+
|  verification                      |
+------------------------------------+
```

## Kit

- Python
- xarray
- ERA5
- PyTorch
- properscoring

**Hardware:** Cloud

## Campaign

```text
  P1  [=====]                     m0-3      Gauge and reanalysis data pipeline
  P2        [=====]               m3-6      Probabilistic model (quantiles or ensemble)
  P3              [=====]         m6-9      Verification with CRPS against baselines
  P4                    [=====]   m9-12     Case studies of historical storm floods
```

## Gate: done when you can show

```text
  [ ] CRPS
  [ ] peak error
  [ ] lead time
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Advisory research.

## Resume line (fill with your measured numbers)

> Built probabilistic storm-surge forecasts beating baseline CRPS by [N]% at [N] h lead time.

**Skills it proves:** probabilistic forecasting · ocean science

## System map

```text
  SURGECAST SYSTEM MAP

+-----------------+    +-----------------+    +-----------------+
|  data pipeline  |--->|  model          |--->|  ensemble       |
+-----------------+    +-----------------+    +-----------------+
        |
        v
+-----------------+    +-----------------+
|  verifier       |--->|  case studies   |
+-----------------+    +-----------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   TRL 3 -> 4
  PUBLICATION TARGET     EGU or ocean forecasting workshop
```

## Deliverables

- Model
- Verification report
- Paper
- Code

## Standards and regulations to meet

- WMO verification guidance (reference)

## Defend it

1. Why probabilistic, not a single number?
2. What is CRPS?
3. How do you handle record-breaking events?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/surgecast  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- FIRESPREAD](88-firespread.md) · [atlas index](../README.md) · [KMWEATHER ->](90-kmweather.md)
