# 88 · FIRESPREAD

```text
       wind -->
    ...^^^^^>>>>>>      t+6h front
    ...^^^^^^>>>>>>>
    [truck] [truck]  <- suggested staging
```

**Wildfire spread surrogate and resource planner**

> Where will it burn in 6 hours, and where should the trucks be?

```text
  TRACK L MASTERPIECE: PLANET, CLIMATE AND INFRASTRUCTURE  |  LEVEL [#####]  |  ~16 MONTHS  |  BUDGET €200
```

## The mission

Fire spread simulators are slow; planners need fast what-ifs.

## How it works

```text
+--------------------------------+
|  fuel + terrain + weather      |
+--------------------------------+
                |
                v
+--------------------------------+
|  physics simulator runs        |
+--------------------------------+
                |
                v
+--------------------------------+
|  ML surrogate                  |
+--------------------------------+
                |
                v
+--------------------------------+
|  resource placement optimiser  |
+--------------------------------+
```

## Kit

- FARSITE-style or open simulators
- PyTorch
- OR-Tools

**Hardware:** Workstation + cloud

## Campaign

```text
  P1  [=====]                     m0-4      Simulator runs for Pfälzerwald-like terrain
  P2        [=====]               m4-8      Surrogate model and validation
  P3              [=====]         m8-12     Resource placement optimisation
  P4                    [=====]   m12-16    Exercise-style evaluation with experts
```

## Gate: done when you can show

```text
  [ ] front position error
  [ ] speed-up
  [ ] coverage of assets
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Advisory research tool.

## Resume line (fill with your measured numbers)

> Built a wildfire spread surrogate [N]x faster than simulation with resource planning for exercises.

**Skills it proves:** scientific ML · optimisation · emergency management

## System map

```text
  FIRESPREAD SYSTEM MAP

+-------------+    +-------------+    +-------------+
|  inputs     |--->|  simulator  |--->|  surrogate  |
+-------------+    +-------------+    +-------------+
      |
      v
+-------------+    +-------------+
|  optimiser  |--->|  viewer     |
+-------------+    +-------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   TRL 2 -> 4
  PUBLICATION TARGET     Fire science or ISCRAM
```

## Deliverables

- Surrogate
- Planner
- Evaluation
- Paper

## Standards and regulations to meet

- None specific

## Defend it

1. What drives fire spread most?
2. How do you validate without real fires?
3. Why keep humans in planning decisions?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/firespread  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- BRIDGESHM](87-bridgeshm.md) · [atlas index](../README.md) · [SURGECAST ->](89-surgecast.md)
