# 85 · LEAKNET

```text
    o----o----o----o      sensors (o)
         |    |
    o----o--[!]-o    leak between nodes 6 and 7 (p=0.81)
```

**Water network leak detection with acoustic sensors and graph ML**

> Hear the leak, locate it on the network graph.

```text
  TRACK L MASTERPIECE: PLANET, CLIMATE AND INFRASTRUCTURE  |  LEVEL [#####]  |  ~16 MONTHS  |  BUDGET €300
```

## The mission

Water utilities lose a significant share of water to leaks found late.

## How it works

```text
+-----------------------------------------+
|  acoustic + pressure sensors            |
+-----------------------------------------+
                    |
                    v
+-----------------------------------------+
|  feature extraction                     |
+-----------------------------------------+
                    |
                    v
+-----------------------------------------+
|  graph neural network on pipe topology  |
+-----------------------------------------+
                    |
                    v
+-----------------------------------------+
|  leak localisation                      |
+-----------------------------------------+
```

## Kit

- Python
- PyTorch Geometric
- EPANET/WNTR simulation
- ESP32 sensors

**Hardware:** Simulation + a small physical pipe rig

## Campaign

```text
  P1  [=====]                     m0-4      Simulated networks with leak scenarios (WNTR)
  P2        [=====]               m4-8      Graph model for localisation
  P3              [=====]         m8-12     Physical rig tests with acoustic sensors
  P4                    [=====]   m12-16    Utility-style report and cost-benefit
```

## Gate: done when you can show

```text
  [ ] localisation error (m or edges)
  [ ] detection time
  [ ] false alarms
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

None special.

## Resume line (fill with your measured numbers)

> Built graph-ML leak localisation within [N] pipe segments on simulated networks, validated on a physical rig.

**Skills it proves:** graph ML · hydraulics · IoT

## System map

```text
  LEAKNET SYSTEM MAP

+---------------------+    +---------------------+    +---------------------+
|  network simulator  |--->|  sensors            |--->|  features           |
+---------------------+    +---------------------+    +---------------------+
          |
          v
+---------------------+    +---------------------+
|  GNN                |--->|  report             |
+---------------------+    +---------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   TRL 3 -> 4
  PUBLICATION TARGET     Water distribution systems analysis conference
```

## Deliverables

- Simulator scenarios
- Model
- Rig results
- Paper

## Standards and regulations to meet

- Water utility practice (reference)

## Defend it

1. Why a graph model instead of a plain classifier?
2. How does simulation help when real leaks are rare?
3. What makes acoustic sensing hard in plastic pipes?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/leaknet  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- HEATSHIELD](84-heatshield.md) · [atlas index](../README.md) · [DROUGHTSENSE ->](86-droughtsense.md)
