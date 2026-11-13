# 69 · SYNTHSCENE

```text
    [ procedural town ] + [ water sim ] + [ weather ] + [ people assets ]
                             |
                   10,000 labelled images --> detector +12 mAP on real test set
```

**Synthetic data engine for rare disaster scenes**

> Train on a thousand floods that never happened.

```text
  TRACK J MASTERPIECE: FOUNDATION MODELS AND AI INFRASTRUCTURE  |  LEVEL [#####]  |  ~14 MONTHS  |  BUDGET €300
```

## The mission

Real imagery of people in floodwater is rare, private and biased.

## How it works

```text
+-------------------------------+
|  procedural scene generation  |
+-------------------------------+
               |
               v
+-------------------------------+
|  domain randomisation         |
+-------------------------------+
               |
               v
+-------------------------------+
|  auto labels                  |
+-------------------------------+
               |
               v
+-------------------------------+
|  train                        |
+-------------------------------+
               |
               v
+-------------------------------+
|  test on real data            |
+-------------------------------+
```

## Kit

- Blender or Unreal Engine 5
- Python
- BlenderProc
- PyTorch

**Hardware:** GPU workstation or cloud

## Campaign

```text
  P1  [=====]                     m0-3.5    Procedural town and water generation
  P2        [=====]               m3.5-7    Randomisation of weather, lighting, camera
  P3              [=====]         m7-10.5   Automatic labels and dataset export
  P4                    [=====]   m10.5-14  Sim-to-real study on SARD/FloodNet test sets
```

## Gate: done when you can show

```text
  [ ] real-test mAP with and without synthetic data
  [ ] generation speed
  [ ] label accuracy
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Synthetic people only; no real victims.

## Resume line (fill with your measured numbers)

> Built a synthetic disaster-scene engine that raised real-world detection mAP by [N] points.

**Skills it proves:** synthetic data · 3D · sim-to-real

## System map

```text
  SYNTHSCENE SYSTEM MAP

+-------------------+    +-------------------+    +-------------------+
|  scene generator  |--->|  randomiser       |--->|  renderer         |
+-------------------+    +-------------------+    +-------------------+
         |
         v
+-------------------+    +-------------------+
|  labeler          |--->|  evaluation       |
+-------------------+    +-------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   Research artefact
  PUBLICATION TARGET     CVPR synthetic data workshop
```

## Deliverables

- Engine
- Synthetic dataset
- Sim-to-real report
- LANTERN detector upgrade

## Standards and regulations to meet

- Data cards

## Defend it

1. What is the sim-to-real gap?
2. Why randomise instead of making scenes photorealistic?
3. How do you know synthetic data didn't add bias?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/synthscene  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- FEDERATE](68-federate.md) · [atlas index](../README.md) · [HOMECLUSTER ->](70-homecluster.md)
