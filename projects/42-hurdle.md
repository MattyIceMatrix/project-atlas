# 42 · HURDLE

```text
        o
       /|\__        ___         ___
       / \   ->    |   |  ->   |   |
    ===============|===|=======|===|====
     take-off 2.1 m   clearance +9 cm
```

**Hurdle technique analysis with pose estimation**

> Your lead leg, measured frame by frame.

```text
  TRACK G PEOPLE, SPORT AND COMMUNITY  |  LEVEL [##...]  |  ~2 MONTHS  |  BUDGET €0
```

## The mission

Coaching feedback on hurdle technique is subjective and slow.

## How it works

```text
+--------------------------------------------------+
|  phone video                                     |
+--------------------------------------------------+
                         |
                         v
+--------------------------------------------------+
|  pose estimation                                 |
+--------------------------------------------------+
                         |
                         v
+--------------------------------------------------+
|  event detection (take-off, clearance, landing)  |
+--------------------------------------------------+
                         |
                         v
+--------------------------------------------------+
|  metrics report                                  |
+--------------------------------------------------+
```

## Kit

- MediaPipe or RTMPose
- OpenCV
- NumPy
- Streamlit

**Hardware:** Phone on a tripod

## Campaign

```text
  P1  [=====]                     m0-0.5    Pose pipeline on public sprint videos
  P2        [=====]               m0.5-1    Hurdle events and distance calibration
  P3              [=====]         m1-1.5    Metrics against a coach's manual measurements
  P4                    [=====]   m1.5-2    Report an athlete can use
```

## Gate: done when you can show

```text
  [ ] take-off distance error
  [ ] event timing error
  [ ] processing time
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Film only athletes who agree; minors only with guardian consent.

## Resume line (fill with your measured numbers)

> Built pose-based hurdle analysis measuring take-off distance within [N] cm of manual coaching measurements.

**Skills it proves:** pose estimation · sports science · calibration

## Masterpiece upgrade path

```text
   LEVEL [##...]  ====================>  LEVEL [#####]
```

Multi-camera 3D platform validated against a reference lab and piloted with a club.

**Grows into:** [ATHLETEOS](91-athleteos.md) · **Publication target:** ISBS

## Defend it

1. How do you calibrate distance from one camera?
2. Which metric would a coach actually use?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/hurdle  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- HERITAGE3D](41-heritage3d.md) · [atlas index](../README.md) · [POOLSHARK ->](43-poolshark.md)
