# 56 · AGRIFLEET

```text
    \|/ \|/ \|/ \|/
    -@---@---@---@-
       [=ROBOT=]>      weeding tool down / up around trunks
    -@---@---@---@-
```

**Autonomous vineyard robot for mechanical weeding**

> Fewer herbicides, more robots between the rows.

```text
  TRACK I MASTERPIECE: AUTONOMOUS SYSTEMS  |  LEVEL [#####]  |  ~20 MONTHS  |  BUDGET €2,000
```

## The mission

Steep-slope vineyards rely on herbicides or hard manual work.

## How it works

```text
+------------------------+
|  RTK + row perception  |
+------------------------+
            |
            v
+------------------------+
|  row following         |
+------------------------+
            |
            v
+------------------------+
|  trunk detection       |
+------------------------+
            |
            v
+------------------------+
|  tool actuation        |
+------------------------+
            |
            v
+------------------------+
|  coverage log          |
+------------------------+
```

## Kit

- ROS 2
- RTK GNSS
- stereo camera
- YOLO
- Nav2

**Hardware:** Small tracked platform with a simple tool (start with a marker, not a blade)

## Campaign

```text
  P1  [=====]                     m0-5      Row following in simulation, then on a test row
  P2        [=====]               m5-10     Trunk detection and tool timing (with a marker)
  P3              [=====]         m10-15    Real tool on a partner winery's test rows, with guards
  P4                    [=====]   m15-20    Season comparison against the winery's normal practice
```

## Gate: done when you can show

```text
  [ ] trunk avoidance rate
  [ ] weeding coverage
  [ ] slope handled
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Partner consent, guarded tool, e-stop, never unattended.

## Resume line (fill with your measured numbers)

> Built a vineyard robot that avoided [N]% of trunks while weeding [N]% of the row on slopes to [N]%.

**Skills it proves:** field robotics · agri-tech · mechatronics

## System map

```text
  AGRIFLEET SYSTEM MAP

+-------------------+    +-------------------+    +-------------------+
|  localisation     |--->|  row perception   |--->|  tool controller  |
+-------------------+    +-------------------+    +-------------------+
         |
         v
+-------------------+    +-------------------+
|  safety layer     |--->|  coverage log     |
+-------------------+    +-------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   TRL 3 -> 5
  PUBLICATION TARGET     Field robotics or precision agriculture conference
```

## Deliverables

- Robot build
- Season report with the winery
- Safety case
- Open-source row follower

## Standards and regulations to meet

- ISO 18497 agricultural machinery autonomy safety (reference)
- Machinery Regulation (EU) 2023/1230 concepts

## Defend it

1. How is a moving blade made safe around people?
2. Why RTK and vision together?
3. What does the winemaker care about most?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/agrifleet  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- RAILWATCH](55-railwatch.md) · [atlas index](../README.md) · [PIPEPROBE ->](57-pipeprobe.md)
