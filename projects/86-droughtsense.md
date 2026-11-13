# 86 · DROUGHTSENSE

```text
    Sentinel-1 radar ))) --> soil moisture --> forecast 4 weeks
    [###] wet   [#..] dry   [...] drought risk
```

**Drought and soil-moisture forecasting from radar satellites**

> See drought coming from orbit, field by field.

```text
  TRACK L MASTERPIECE: PLANET, CLIMATE AND INFRASTRUCTURE  |  LEVEL [#####]  |  ~16 MONTHS  |  BUDGET €200
```

## The mission

Farmers and water managers need drought warnings at field scale, not region scale.

## How it works

```text
+----------------------------+
|  Sentinel-1 SAR + weather  |
+----------------------------+
              |
              v
+----------------------------+
|  soil moisture retrieval   |
+----------------------------+
              |
              v
+----------------------------+
|  spatiotemporal forecast   |
+----------------------------+
              |
              v
+----------------------------+
|  risk maps                 |
+----------------------------+
```

## Kit

- openEO
- xarray
- PyTorch (ConvLSTM / transformer)
- DWD data

**Hardware:** Cloud credits

## Campaign

```text
  P1  [=====]                     m0-4      SAR preprocessing pipeline
  P2        [=====]               m4-8      Soil moisture model vs in-situ stations
  P3              [=====]         m8-12     Forecast model and skill scores
  P4                    [=====]   m12-16    Risk maps for one region (Rhineland-Palatinate)
```

## Gate: done when you can show

```text
  [ ] RMSE vs in-situ
  [ ] forecast skill vs climatology
  [ ] map update time
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Open data; advisory.

## Resume line (fill with your measured numbers)

> Built SAR-based soil moisture forecasting with skill [N] over climatology at field scale.

**Skills it proves:** SAR remote sensing · spatiotemporal ML

## System map

```text
  DROUGHTSENSE SYSTEM MAP

+----------------+    +----------------+    +----------------+
|  SAR pipeline  |--->|  retrieval     |--->|  forecaster    |
+----------------+    +----------------+    +----------------+
        |
        v
+----------------+    +----------------+
|  validation    |--->|  map service   |
+----------------+    +----------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   TRL 3 -> 5
  PUBLICATION TARGET     IGARSS or EGU
```

## Deliverables

- Pipeline
- Validation
- Maps
- Paper

## Standards and regulations to meet

- FAIR data

## Defend it

1. Why radar instead of optical?
2. What is forecast skill?
3. How does vegetation confuse soil moisture retrieval?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/droughtsense  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- LEAKNET](85-leaknet.md) · [atlas index](../README.md) · [BRIDGESHM ->](87-bridgeshm.md)
