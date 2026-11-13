# 52 · FLEETMIND

```text
     .-.   .-.        [air]  (sim)
    (   )~(   )
     '-'   '-'     \  |  /
    [gnd]--[gnd]--( MAP )--[gnd]
```

**Heterogeneous robot fleet for disaster mapping**

> Ground and air robots that share one map and one plan.

```text
  TRACK I MASTERPIECE: AUTONOMOUS SYSTEMS  |  LEVEL [#####]  |  ~20 MONTHS  |  BUDGET €1,500
```

## The mission

Disaster sites need many viewpoints fast; single robots are slow and fragile.

## How it works

```text
+---------------------+
|  each robot SLAM    |
+---------------------+
          |
          v
+---------------------+
|  map merging        |
+---------------------+
          |
          v
+---------------------+
|  task auction       |
+---------------------+
          |
          v
+---------------------+
|  coverage planning  |
+---------------------+
          |
          v
+---------------------+
|  operator console   |
+---------------------+
```

## Kit

- ROS 2
- Nav2
- multi-robot map merge
- Gazebo or Isaac Sim
- Zenoh

**Hardware:** 2–3 ground rovers (LANTERN-class) + drones in simulation only

## Campaign

```text
  P1  [=====]                     m0-5      Multi-robot simulation with shared map
  P2        [=====]               m5-10     Task allocation that survives robot and link loss
  P3              [=====]         m10-15    Two real rovers merging maps outdoors
  P4                    [=====]   m15-20    Operator console with human approval for every risky task
```

## Gate: done when you can show

```text
  [ ] time to 95% coverage
  [ ] map merge error
  [ ] performance after one robot is lost
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Drones stay in simulation unless properly certified and permitted; civilian use only.

## Resume line (fill with your measured numbers)

> Built a fault-tolerant multi-robot mapping fleet; coverage [N]% faster than one robot, robust to robot loss.

**Skills it proves:** multi-robot systems · distributed SLAM · HRI

## System map

```text
  FLEETMIND SYSTEM MAP

+-----------------------+    +-----------------------+    +-----------------------+
|  per-robot autonomy   |--->|  map merger           |--->|  task market          |
+-----------------------+    +-----------------------+    +-----------------------+
           |
           v
+-----------------------+    +-----------------------+
|  comms layer (Zenoh)  |--->|  operator console     |
+-----------------------+    +-----------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   TRL 3 -> 5
  PUBLICATION TARGET     IEEE SSRR or ICRA workshop
```

## Deliverables

- Simulation benchmark
- Two-robot field demo video
- Paper draft
- Open-source fleet stack

## Standards and regulations to meet

- ROS 2 REP conventions
- ISO 13482 concepts for robot safety (reference)
- Drone rules EU 2019/947 for any flight

## Defend it

1. How do two maps with different origins get merged?
2. What happens when the network partitions mid-mission?
3. Why keep humans in the approval loop?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/fleetmind  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- SEAWALL](51-seawall.md) · [atlas index](../README.md) · [EDGEOS ->](53-edgeos.md)
