# 03 · FORESTER

```text
        .-~~-.
     .-(  smoke )-.        [cam]
    (______________)        |##|   tower
    /\  /\  /\  /\  /\      |##|
   /  \/  \/  \/  \/  \  ___|##|___
```

**Wildfire smoke spotter for the Palatinate Forest**

> A camera on a tower that never blinks.

```text
  TRACK A EDGE AI AND ROBOTICS  |  LEVEL [###..]  |  ~5 MONTHS  |  BUDGET €400
```

## The mission

Dry summers raise forest fire risk in the Pfälzerwald; early smoke detection saves hectares.

## How it works

```text
+---------------------------------+
|  PTZ camera                     |
+---------------------------------+
                |
                v
+---------------------------------+
|  Jetson smoke/cloud classifier  |
+---------------------------------+
                |
                v
+---------------------------------+
|  geolocation by bearing         |
+---------------------------------+
                |
                v
+---------------------------------+
|  alert to fire service mock     |
+---------------------------------+
```

## Kit

- Jetson Orin Nano
- YOLO-family detector
- TensorRT
- OpenCV
- FastAPI

**Hardware:** Jetson + outdoor camera (tested from a balcony or hill, not a real tower)

## Campaign

```text
  P1  [=====]                     m0-1.2    Curate public smoke datasets; data card
  P2        [=====]               m1.2-2.5  Train smoke vs cloud vs fog classifier
  P3              [=====]         m2.5-3.8  TensorRT INT8 on Jetson, live stream test
  P4                    [=====]   m3.8-5    Bearing-based location estimate and alert UI
```

## Gate: done when you can show

```text
  [ ] time to first detection
  [ ] false alarms per day
  [ ] fps
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Demonstrator only; no claim to replace fire watch services.

## Resume line (fill with your measured numbers)

> Shipped an edge smoke detector on Jetson (INT8, [N] fps) separating smoke from cloud at [N]% precision.

**Skills it proves:** computer vision · TensorRT · geolocation

## Masterpiece upgrade path

```text
   LEVEL [###..]  ====================>  LEVEL [#####]
```

Three-tower triangulation, satellite hotspot fusion, a spread forecast handoff and an exercise with a fire brigade.

**Grows into:** [FIRESPREAD](88-firespread.md), [ORBITAL](36-orbital.md) · **Publication target:** Fire science conference

## Defend it

1. Why is cloud vs smoke the hard part?
2. What is your false-alarm budget and who decided it?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/forester  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- HIVEMIND](02-hivemind.md) · [atlas index](../README.md) · [BRIDGEKEEPER ->](04-bridgekeeper.md)
