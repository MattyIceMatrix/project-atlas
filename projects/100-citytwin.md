# 100 · CITYTWIN

```text
         _   __    _|_    __
      __| |_|  |__| |_|__|  |__     3D buildings
     [ traffic ][ energy ][ heat ][ flood ]   one data model
```

**Open digital twin of a mid-size city**

> Kaiserslautern in 3D, with traffic, energy, trees and water in one model.

```text
  TRACK M MASTERPIECE: CIVIC, SCIENCE AND HUMAN PERFORMANCE  |  LEVEL [#####]  |  ~24 MONTHS  |  BUDGET €30/month
```

## The mission

Cities buy separate tools for every domain; nothing connects them.

## How it works

```text
+--------------------------------------+
|  open 3D city models + sensor feeds  |
+--------------------------------------+
                   |
                   v
+--------------------------------------+
|  unified data model                  |
+--------------------------------------+
                   |
                   v
+--------------------------------------+
|  simulations                         |
+--------------------------------------+
                   |
                   v
+--------------------------------------+
|  web viewer + API                    |
+--------------------------------------+
```

## Kit

- CityGML/CityJSON
- 3D Tiles
- CesiumJS
- FROST (OGC SensorThings)
- PostGIS

**Hardware:** None

## Campaign

```text
  P1  [=====]                     m0-6      Unified data model and open data ingest
  P2        [=====]               m6-12     3D viewer with layers from GREENLINE, HEATSHIELD, FLOODTWIN, GRIDBRAIN
  P3              [=====]         m12-18    Live sensor feeds via SensorThings API
  P4                    [=====]   m18-24    Scenario mode and presentation to a city office
```

## Gate: done when you can show

```text
  [ ] datasets integrated
  [ ] viewer performance
  [ ] scenario runtime
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Open and aggregated data only.

## Resume line (fill with your measured numbers)

> Built an open urban digital twin integrating [N] datasets and [N] simulation layers in a standards-based API.

**Skills it proves:** geospatial architecture · standards · integration

## System map

```text
  CITYTWIN SYSTEM MAP

+-----------------------+    +-----------------------+    +-----------------------+
|  data model           |--->|  ingest               |--->|  simulation adapters  |
+-----------------------+    +-----------------------+    +-----------------------+
           |
           v
+-----------------------+    +-----------------------+
|  SensorThings API     |--->|  3D viewer            |
+-----------------------+    +-----------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   TRL 4 -> 6
  PUBLICATION TARGET     FOSS4G or urban data conference
```

## Deliverables

- Twin platform
- Data catalogue
- City presentation
- Paper

## Standards and regulations to meet

- OGC CityGML
- OGC SensorThings
- OGC 3D Tiles
- INSPIRE

## Defend it

1. Why open standards instead of a single vendor?
2. What is CityGML LOD2?
3. What decision would a city actually make with it?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/citytwin  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- HELPERHUB](99-helperhub.md) · [atlas index](../README.md)
