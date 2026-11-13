# 59 · RECYCLR

```text
         _||_
        (    )--[grip: soft, crinkle = PET]
    ====[can][bottle][box][?]====>  belt
```

**Tactile robot arm that sorts recyclables**

> Sees it, feels it, sorts it.

```text
  TRACK I MASTERPIECE: AUTONOMOUS SYSTEMS  |  LEVEL [#####]  |  ~16 MONTHS  |  BUDGET €1,200
```

## The mission

Sorting lines struggle with dirty, crushed and mixed materials; vision alone gets fooled.

## How it works

```text
+---------------------------+
|  camera + tactile sensor  |
+---------------------------+
             |
             v
+---------------------------+
|  material classifier      |
+---------------------------+
             |
             v
+---------------------------+
|  grasp planner            |
+---------------------------+
             |
             v
+---------------------------+
|  bins                     |
+---------------------------+
             |
             v
+---------------------------+
|  accuracy log             |
+---------------------------+
```

## Kit

- ROS 2
- MoveIt 2
- low-cost arm
- GelSight-style or force sensor
- PyTorch

**Hardware:** Desktop robot arm, camera, tactile sensor, small conveyor

## Campaign

```text
  P1  [=====]                     m0-4      Vision-only baseline on a mock belt
  P2        [=====]               m4-8      Tactile sensing and fusion
  P3              [=====]         m8-12     Grasp planning for deformed objects
  P4                    [=====]   m12-16    Throughput and purity benchmark
```

## Gate: done when you can show

```text
  [ ] sorting purity
  [ ] picks per minute
  [ ] grasp success rate
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

None special.

## Resume line (fill with your measured numbers)

> Built a visuo-tactile sorting arm reaching [N]% purity at [N] picks/min, beating vision-only by [N]%.

**Skills it proves:** manipulation · sensor fusion · MoveIt

## System map

```text
  RECYCLR SYSTEM MAP

+---------------------+    +---------------------+    +---------------------+
|  perception         |--->|  tactile module     |--->|  fusion classifier  |
+---------------------+    +---------------------+    +---------------------+
          |
          v
+---------------------+    +---------------------+
|  grasp planner      |--->|  belt controller    |
+---------------------+    +---------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   TRL 3 -> 4
  PUBLICATION TARGET     IROS or CoRL workshop
```

## Deliverables

- Benchmark dataset
- Arm cell design
- Paper draft
- Demo video

## Standards and regulations to meet

- ISO 10218 robot safety (reference)
- ISO/TS 15066 collaborative robots (reference)

## Defend it

1. What does touch add that vision can't?
2. Why is purity the metric recyclers care about?
3. How do you handle objects the model has never seen?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/recyclr  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- SKYLANE](58-skylane.md) · [atlas index](../README.md) · [MESHLIFE ->](60-meshlife.md)
