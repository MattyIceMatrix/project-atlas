# 51 · SEAWALL

```text
        __/\__
    ~~~|SEAWALL|~~~~~~~~~~   ))) sonar ping
  ~~~~~~\____/~~~~~~~~~~~~~      )))  depth 2.4 m
```

**Autonomous survey boat for river and flood-plain mapping**

> Maps the riverbed so the next flood model starts from the truth.

```text
  TRACK I MASTERPIECE: AUTONOMOUS SYSTEMS  |  LEVEL [#####]  |  ~18 MONTHS  |  BUDGET €1,800
```

## The mission

Flood models are only as good as their riverbed geometry, and river cross-sections are surveyed rarely, by hand, at high cost.

## How it works

```text
+--------------------------------+
|  GNSS-RTK + single-beam sonar  |
+--------------------------------+
                |
                v
+--------------------------------+
|  autonomous survey lines       |
+--------------------------------+
                |
                v
+--------------------------------+
|  point cloud                   |
+--------------------------------+
                |
                v
+--------------------------------+
|  riverbed mesh                 |
+--------------------------------+
                |
                v
+--------------------------------+
|  hydraulic model input         |
+--------------------------------+
```

## Kit

- ROS 2
- ArduPilot Rover (boat frame)
- RTK GNSS
- PDAL
- HEC-RAS or LISFLOOD-FP

**Hardware:** Small catamaran hull, RTK GNSS, echo sounder, Jetson, e-stop radio

## Campaign

```text
  P1  [=====]                     m0-4.5    Hull, power and remote control with a kill switch; still-water trials
  P2        [=====]               m4.5-9    Autonomous survey lines with RTK; depth logging and QC
  P3              [=====]         m9-13.5   Riverbed reconstruction and comparison with official cross-sections
  P4                    [=====]   m13.5-18  Feed the bathymetry into a flood model and measure the improvement
```

## Gate: done when you can show

```text
  [ ] depth error vs reference survey (cm)
  [ ] coverage per hour
  [ ] flood-model error improvement
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Survey only with landowner and water-authority permission; never in flood conditions.

## Resume line (fill with your measured numbers)

> Built an autonomous RTK survey boat; bathymetry within [N] cm improved flood-model error by [N]%.

**Skills it proves:** marine robotics · GNSS · hydrology · ROS 2

## System map

```text
  SEAWALL SYSTEM MAP

+----------------------+    +----------------------+    +----------------------+
|  RTK positioning     |--->|  sonar and logging   |--->|  mission planner     |
+----------------------+    +----------------------+    +----------------------+
           |
           v
+----------------------+    +----------------------+
|  QC pipeline         |--->|  flood model bridge  |
+----------------------+    +----------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   TRL 3 -> 5 (validated on a real river reach)
  PUBLICATION TARGET     IEEE OCEANS or a hydrology journal (data paper)
```

## Deliverables

- Survey boat build guide
- Open bathymetry dataset for one reach
- Flood-model comparison report
- Safety case

## Standards and regulations to meet

- IHO S-44 survey accuracy orders (reference)
- EN 62443 thinking for the control link
- Local water-authority rules

## Defend it

1. Why does riverbed geometry matter so much to a flood model?
2. What failsafe brings the boat home when the link drops?
3. How do you separate sonar noise from vegetation?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/seawall  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- HEARTH](50-hearth.md) · [atlas index](../README.md) · [FLEETMIND ->](52-fleetmind.md)
