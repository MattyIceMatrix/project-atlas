# 87 · BRIDGESHM

```text
    ____________________________
    |__acc__|__acc__|__acc__|___|   accelerometers
         ~~ modal freq 3.21 Hz -> 3.08 Hz (stiffness drop?) ~~
```

**Structural health monitoring with vibration sensors and a digital twin**

> The bridge tells you when it's tired.

```text
  TRACK L MASTERPIECE: PLANET, CLIMATE AND INFRASTRUCTURE  |  LEVEL [#####]  |  ~16 MONTHS  |  BUDGET €400
```

## The mission

Bridges age faster than inspection budgets grow.

## How it works

```text
+----------------------------+
|  accelerometers            |
+----------------------------+
              |
              v
+----------------------------+
|  modal identification      |
+----------------------------+
              |
              v
+----------------------------+
|  FE model updating (twin)  |
+----------------------------+
              |
              v
+----------------------------+
|  damage indicators         |
+----------------------------+
              |
              v
+----------------------------+
|  alerts                    |
+----------------------------+
```

## Kit

- ESP32 + MEMS accelerometers
- Python
- OpenSeesPy
- pyOMA

**Hardware:** Lab beam or footbridge with owner permission

## Campaign

```text
  P1  [=====]                     m0-4      Sensor network and time sync
  P2        [=====]               m4-8      Operational modal analysis
  P3              [=====]         m8-12     Finite-element twin and model updating
  P4                    [=====]   m12-16    Damage scenarios on a lab structure
```

## Gate: done when you can show

```text
  [ ] frequency identification error
  [ ] damage detection rate
  [ ] environmental false alarms
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Advisory; structural engineers decide.

## Resume line (fill with your measured numbers)

> Built an SHM system with FE-updated digital twin detecting simulated damage at [N]% rate.

**Skills it proves:** structural dynamics · sensors · digital twins

## System map

```text
  BRIDGESHM SYSTEM MAP

+---------------------+    +---------------------+    +---------------------+
|  sensor net         |--->|  OMA                |--->|  FE twin            |
+---------------------+    +---------------------+    +---------------------+
          |
          v
+---------------------+    +---------------------+
|  damage indicators  |--->|  dashboard          |
+---------------------+    +---------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   TRL 3 -> 4
  PUBLICATION TARGET     IWSHM or EWSHM
```

## Deliverables

- Sensor design
- Twin
- Lab report
- Paper

## Standards and regulations to meet

- Eurocode context (reference)

## Defend it

1. Why does temperature change modal frequencies?
2. What is model updating?
3. Why combine with visual inspection (BRIDGEKEEPER)?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/bridgeshm  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- DROUGHTSENSE](86-droughtsense.md) · [atlas index](../README.md) · [FIRESPREAD ->](88-firespread.md)
