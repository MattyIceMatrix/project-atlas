# 43 · POOLSHARK

```text
    .------------------------------.
    | o           ,--> (3)         |
    |   (cue)----'                 |
    |                  (8)    o    |
    '------------------------------'
     cut angle 31 deg, hit 2 mm thick
```

**Pool shot analysis and training coach**

> Every shot tracked, every miss explained.

```text
  TRACK G PEOPLE, SPORT AND COMMUNITY  |  LEVEL [##...]  |  ~2 MONTHS  |  BUDGET €30
```

## The mission

Amateur players can't see why shots miss.

## How it works

```text
+----------------------------+
|  overhead camera           |
+----------------------------+
              |
              v
+----------------------------+
|  table and ball detection  |
+----------------------------+
              |
              v
+----------------------------+
|  trajectory                |
+----------------------------+
              |
              v
+----------------------------+
|  shot metrics              |
+----------------------------+
              |
              v
+----------------------------+
|  drill suggestions         |
+----------------------------+
```

## Kit

- OpenCV
- YOLO
- Kalman filter
- Python

**Hardware:** Phone or webcam above the table

## Campaign

```text
  P1  [=====]                     m0-0.5    Table homography and ball detection
  P2        [=====]               m0.5-1    Trajectory tracking
  P3              [=====]         m1-1.5    Shot metrics and miss explanation
  P4                    [=====]   m1.5-2    Drill mode with progress tracking
```

## Gate: done when you can show

```text
  [ ] ball position error
  [ ] shots tracked per session
  [ ] improvement over 4 weeks
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

None special.

## Resume line (fill with your measured numbers)

> Built CV pool coaching that tracks balls within [N] mm and explains misses from trajectories.

**Skills it proves:** tracking · homography · product design

## Masterpiece upgrade path

```text
   LEVEL [##...]  ====================>  LEVEL [#####]
```

3D ball and cue tracking with a coaching curriculum and learning study.

**Grows into:** [QUESTLINE](98-questline.md) · **Publication target:** Sports engineering conference

## Defend it

1. What is a homography?
2. How do you handle balls touching each other?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/poolshark  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- HURDLE](42-hurdle.md) · [atlas index](../README.md) · [CLIMB-TRANSITION ->](44-climb-transition.md)
