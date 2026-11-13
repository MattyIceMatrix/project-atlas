# 58 · SKYLANE

```text
      ^ 120 m ---------------------------
         \ d1      d2 -->     <-- d3
          \___ conflict in 40 s: reroute d2
    ---------------------------------------
```

**Drone traffic management simulator (U-space)**

> Air traffic control for a sky full of small drones, in simulation.

```text
  TRACK I MASTERPIECE: AUTONOMOUS SYSTEMS  |  LEVEL [#####]  |  ~14 MONTHS  |  BUDGET €0
```

## The mission

Low-altitude drone traffic needs deconfliction services before it can scale safely.

## How it works

```text
+----------------------------+
|  flight intents            |
+----------------------------+
              |
              v
+----------------------------+
|  strategic deconfliction   |
+----------------------------+
              |
              v
+----------------------------+
|  live tracking             |
+----------------------------+
              |
              v
+----------------------------+
|  tactical conflict alerts  |
+----------------------------+
              |
              v
+----------------------------+
|  replay and metrics        |
+----------------------------+
```

## Kit

- Python or Rust
- PX4 SITL
- BlueSky ATM simulator
- PostGIS
- Kafka

**Hardware:** None (simulation)

## Campaign

```text
  P1  [=====]                     m0-3.5    Airspace model with geofences from open data
  P2        [=====]               m3.5-7    Strategic deconfliction of flight intents
  P3              [=====]         m7-10.5   Tactical conflict detection with simulated sensors
  P4                    [=====]   m10.5-14  Stress test with 1,000 simulated flights
```

## Gate: done when you can show

```text
  [ ] conflicts resolved
  [ ] loss-of-separation events
  [ ] throughput per km2
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Simulation; real geofence data used read-only.

## Resume line (fill with your measured numbers)

> Built a U-space style simulator handling [N] concurrent drones with [N] loss-of-separation events.

**Skills it proves:** aviation systems · distributed systems · simulation

## System map

```text
  SKYLANE SYSTEM MAP

+------------------------+    +------------------------+    +------------------------+
|  airspace model        |--->|  intent manager        |--->|  deconfliction engine  |
+------------------------+    +------------------------+    +------------------------+
            |
            v
+------------------------+    +------------------------+
|  tracker               |--->|  metrics               |
+------------------------+    +------------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   TRL 2 -> 4
  PUBLICATION TARGET     SESAR Innovation Days or AIAA/IEEE DASC
```

## Deliverables

- Simulator
- Benchmark scenarios
- Paper draft
- Interactive replay viewer

## Standards and regulations to meet

- Regulation (EU) 2021/664 U-space (reference)
- ASTM F3548 (reference)

## Defend it

1. Strategic vs tactical deconfliction?
2. How do you verify the simulator is realistic?
3. What does U-space regulation require?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/skylane  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- PIPEPROBE](57-pipeprobe.md) · [atlas index](../README.md) · [RECYCLR ->](59-recyclr.md)
