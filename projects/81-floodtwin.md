# 81 · FLOODTWIN

```text
     rain(t) --> [ physics model: hours ]       --> depth map
     rain(t) --> [ ML surrogate:  seconds ]     --> depth map  (error 12 cm)
    ~~~~~~~~~~~~~~~~~~~~~~ Ahr ~~~~~~~~~~~~~~~~~~~~~~~>
```

**Hydrodynamic digital twin of the Ahr valley with an ML surrogate**

> A flood forecast in seconds instead of hours.

```text
  TRACK L MASTERPIECE: PLANET, CLIMATE AND INFRASTRUCTURE  |  LEVEL [#####]  |  ~20 MONTHS  |  BUDGET €400
```

## The mission

Physics flood models are accurate but too slow for real-time what-if planning during an event.

## How it works

```text
+----------------------------------------+
|  terrain + bathymetry                  |
+----------------------------------------+
                    |
                    v
+----------------------------------------+
|  physics simulations (many scenarios)  |
+----------------------------------------+
                    |
                    v
+----------------------------------------+
|  train surrogate                       |
+----------------------------------------+
                    |
                    v
+----------------------------------------+
|  validate on 2021 event                |
+----------------------------------------+
                    |
                    v
+----------------------------------------+
|  dashboard                             |
+----------------------------------------+
```

## Kit

- LISFLOOD-FP or HEC-RAS 2D
- PyTorch (U-Net / neural operator)
- xarray
- LANTERN map pack

**Hardware:** Workstation + cloud for simulation batches

## Campaign

```text
  P1  [=====]                     m0-5      Calibrate a physics model to EMSR517 2021 extents
  P2        [=====]               m5-10     Generate hundreds of rainfall scenarios
  P3              [=====]         m10-15    Train and validate the surrogate
  P4                    [=====]   m15-20    What-if dashboard for planners (advisory)
```

## Gate: done when you can show

```text
  [ ] surrogate depth error
  [ ] speed-up factor
  [ ] extent IoU on 2021 event
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Research tool; official warnings come from authorities.

## Resume line (fill with your measured numbers)

> Built a flood-model surrogate [N]x faster than physics, within [N] cm, validated on the 2021 Ahr flood.

**Skills it proves:** hydraulic modelling · scientific ML · geospatial

## System map

```text
  FLOODTWIN SYSTEM MAP

+----------------------+    +----------------------+    +----------------------+
|  terrain builder     |--->|  physics runner      |--->|  scenario generator  |
+----------------------+    +----------------------+    +----------------------+
           |
           v
+----------------------+    +----------------------+
|  surrogate           |--->|  planner dashboard   |
+----------------------+    +----------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   TRL 3 -> 5
  PUBLICATION TARGET     EGU General Assembly or a hydroinformatics journal
```

## Deliverables

- Calibrated model
- Surrogate + card
- Validation paper
- Dashboard

## Standards and regulations to meet

- EU Floods Directive 2007/60/EC (context)
- FAIR data principles

## Defend it

1. Why can't the surrogate be trusted outside its training scenarios?
2. How did you calibrate the physics model?
3. What does the 2021 event teach about extreme scenarios?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/floodtwin  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- CREDMESH](80-credmesh.md) · [atlas index](../README.md) · [GRIDBRAIN ->](82-gridbrain.md)
