# 96 · WAYFINDER

```text
    [phone cam] --> "Stairs ahead, 5 m. Handrail on your right."
     |       |
    ===|=====|====  platform 3 ->
```

**Indoor navigation for blind and low-vision users**

> Turn-by-turn through the train station, from a phone camera.

```text
  TRACK M MASTERPIECE: CIVIC, SCIENCE AND HUMAN PERFORMANCE  |  LEVEL [#####]  |  ~16 MONTHS  |  BUDGET €0
```

## The mission

GPS doesn't work indoors; blind travellers rely on memory and strangers.

## How it works

```text
+-----------------------------------------+
|  camera + IMU                           |
+-----------------------------------------+
                    |
                    v
+-----------------------------------------+
|  visual localisation on a prebuilt map  |
+-----------------------------------------+
                    |
                    v
+-----------------------------------------+
|  obstacle detection                     |
+-----------------------------------------+
                    |
                    v
+-----------------------------------------+
|  audio/haptic guidance                  |
+-----------------------------------------+
```

## Kit

- ARCore/ARKit or ORB-SLAM3
- YOLO
- TTS
- mobile app

**Hardware:** Phone

## Campaign

```text
  P1  [=====]                     m0-4      Co-design sessions with blind users and an advocacy group
  P2        [=====]               m4-8      Map building and visual localisation
  P3              [=====]         m8-12     Obstacle detection and guidance design
  P4                    [=====]   m12-16    User study in a real public building (with permission)
```

## Gate: done when you can show

```text
  [ ] localisation error
  [ ] route completion rate
  [ ] user confidence ratings
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Co-designed; assistive aid, not a replacement for cane or guide dog.

## Resume line (fill with your measured numbers)

> Built camera-based indoor navigation with [N]% route completion in a study co-designed with blind users.

**Skills it proves:** SLAM · accessibility · human-centred design

## System map

```text
  WAYFINDER SYSTEM MAP

+---------------------+    +---------------------+    +---------------------+
|  mapper             |--->|  localiser          |--->|  obstacle detector  |
+---------------------+    +---------------------+    +---------------------+
          |
          v
+---------------------+    +---------------------+
|  guidance engine    |--->|  app                |
+---------------------+    +---------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   TRL 4 -> 6
  PUBLICATION TARGET     ASSETS (ACM accessibility conference)
```

## Deliverables

- App
- Study report
- Design guidelines
- Paper

## Standards and regulations to meet

- WCAG 2.2
- EN 301 549
- BITV 2.0

## Defend it

1. Why co-design and not just test at the end?
2. What failure is most dangerous and how is it handled?
3. Audio vs haptic: what did users prefer?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/wayfinder  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- BABEL](95-babel.md) · [atlas index](../README.md) · [REPROBOT ->](97-reprobot.md)
