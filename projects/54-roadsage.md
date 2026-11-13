# 54 · ROADSAGE

```text
    ===|=====|=====|=====|===
        [car] -->      !
    ===|=====|=====|=====|===    monitor: TTC 1.2 s -> BRAKE
```

**Driver-assistance research stack with a safety monitor**

> Perception, planning and a referee that can say stop.

```text
  TRACK I MASTERPIECE: AUTONOMOUS SYSTEMS  |  LEVEL [#####]  |  ~16 MONTHS  |  BUDGET €300 cloud
```

## The mission

Learned driving components fail in rare situations; you need a monitor that catches it.

## How it works

```text
+---------------------------+
|  camera/lidar             |
+---------------------------+
             |
             v
+---------------------------+
|  perception               |
+---------------------------+
             |
             v
+---------------------------+
|  planner                  |
+---------------------------+
             |
             v
+---------------------------+
|  runtime safety monitor   |
+---------------------------+
             |
             v
+---------------------------+
|  controller (simulation)  |
+---------------------------+
```

## Kit

- CARLA
- ROS 2
- PyTorch
- Responsibility-Sensitive-Safety style rules
- scenario runner

**Hardware:** GPU workstation or cloud (simulation only)

## Campaign

```text
  P1  [=====]                     m0-4      Perception and planning baseline in CARLA
  P2        [=====]               m4-8      Rule-based runtime safety monitor
  P3              [=====]         m8-12     Scenario library of edge cases (cut-ins, occlusions, weather)
  P4                    [=====]   m12-16    Safety argument with measured violation rates
```

## Gate: done when you can show

```text
  [ ] collisions per 1
  [ ] 000 km sim
  [ ] monitor interventions
  [ ] false interventions
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Simulation only; never tested on public roads.

## Resume line (fill with your measured numbers)

> Built a simulated ADAS stack whose safety monitor cut collisions [N]% across [N] edge-case scenarios.

**Skills it proves:** autonomous driving · safety engineering · simulation

## System map

```text
  ROADSAGE SYSTEM MAP

+-------------------+    +-------------------+    +-------------------+
|  perception       |--->|  planner          |--->|  safety monitor   |
+-------------------+    +-------------------+    +-------------------+
         |
         v
+-------------------+    +-------------------+
|  scenario engine  |--->|  metrics          |
+-------------------+    +-------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   TRL 3 -> 4 (simulation)
  PUBLICATION TARGET     IEEE IV workshop or arXiv preprint
```

## Deliverables

- Scenario library
- Safety case
- Results paper
- Open-source monitor

## Standards and regulations to meet

- ISO 26262 (concepts)
- ISO 21448 SOTIF
- UL 4600 safety case structure

## Defend it

1. Why a rule-based monitor over a learned planner?
2. What is a SOTIF hazard?
3. How do you choose which scenarios to test?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/roadsage  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- EDGEOS](53-edgeos.md) · [atlas index](../README.md) · [RAILWATCH ->](55-railwatch.md)
