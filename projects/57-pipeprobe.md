# 57 · PIPEPROBE

```text
    ___________________________________
   (  [o=o]>   crack!     root intrusion )
    ===================================
```

**In-pipe inspection crawler for sewers**

> The dark, wet job nobody wants, done by a robot.

```text
  TRACK I MASTERPIECE: AUTONOMOUS SYSTEMS  |  LEVEL [#####]  |  ~14 MONTHS  |  BUDGET €900
```

## The mission

Sewer inspection uses tethered cameras and manual review of hours of video.

## How it works

```text
+-------------------------------+
|  tethered crawler video       |
+-------------------------------+
               |
               v
+-------------------------------+
|  defect detection and coding  |
+-------------------------------+
               |
               v
+-------------------------------+
|  pipe condition score         |
+-------------------------------+
               |
               v
+-------------------------------+
|  GIS asset layer              |
+-------------------------------+
```

## Kit

- ROS 2
- PyTorch
- public sewer defect datasets (e.g. Sewer-ML)
- PostGIS

**Hardware:** Small crawler with lights and camera tested in a mock pipe

## Campaign

```text
  P1  [=====]                     m0-3.5    Model on public sewer datasets; defect taxonomy
  P2        [=====]               m3.5-7    Crawler build and mock-pipe tests
  P3              [=====]         m7-10.5   Automatic defect coding to the operator's standard
  P4                    [=====]   m10.5-14  Condition scoring and GIS integration
```

## Gate: done when you can show

```text
  [ ] defect classification F1
  [ ] review time saved
  [ ] condition score agreement with inspectors
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Confined-space and hygiene rules; partner utility for any real pipe.

## Resume line (fill with your measured numbers)

> Built a sewer crawler with defect coding at F1 [N], cutting manual review time [N]%.

**Skills it proves:** inspection robotics · CV · asset management

## System map

```text
  PIPEPROBE SYSTEM MAP

+--------------------+    +--------------------+    +--------------------+
|  crawler           |--->|  video pipeline    |--->|  defect coder      |
+--------------------+    +--------------------+    +--------------------+
          |
          v
+--------------------+    +--------------------+
|  condition scorer  |--->|  GIS layer         |
+--------------------+    +--------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   TRL 3 -> 5
  PUBLICATION TARGET     Water infrastructure conference or applied ML venue
```

## Deliverables

- Crawler design
- Defect coder
- Utility pilot report
- Data card

## Standards and regulations to meet

- EN 13508-2 visual inspection coding
- DWA-M 149 (German practice
- reference)

## Defend it

1. Why does a standard defect code matter more than a fancy model?
2. How do you handle the class imbalance of rare defects?
3. What is condition-based maintenance?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/pipeprobe  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- AGRIFLEET](56-agrifleet.md) · [atlas index](../README.md) · [SKYLANE ->](58-skylane.md)
