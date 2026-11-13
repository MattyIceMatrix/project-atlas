# 91 · ATHLETEOS

```text
    cam1 \        o_     ___     ___
    cam2 -->  3D /|  -> |   | ->|   |    split 1-2: 1.02 s
    cam3 /       / \    |   |   |   |    knee angle at take-off: 152 deg
```

**Sprint and hurdle performance platform**

> Multi-camera 3D motion, timing gates and a coach dashboard, built by a former hurdler.

```text
  TRACK M MASTERPIECE: CIVIC, SCIENCE AND HUMAN PERFORMANCE  |  LEVEL [#####]  |  ~14 MONTHS  |  BUDGET €300
```

## The mission

Elite-grade biomechanics systems cost tens of thousands; club athletes get nothing.

## How it works

```text
+----------------------------+
|  synchronised phones       |
+----------------------------+
              |
              v
+----------------------------+
|  3D pose triangulation     |
+----------------------------+
              |
              v
+----------------------------+
|  event detection           |
+----------------------------+
              |
              v
+----------------------------+
|  metrics                   |
+----------------------------+
              |
              v
+----------------------------+
|  coach dashboard + trends  |
+----------------------------+
```

## Kit

- RTMPose
- multi-view triangulation
- Python
- FastAPI
- React

**Hardware:** 3 phones, tripods, optional timing gates

## Campaign

```text
  P1  [=====]                     m0-3.5    Multi-camera sync and calibration
  P2        [=====]               m3.5-7    3D pose and event detection, validated against a reference system
  P3              [=====]         m7-10.5   Coach dashboard with season trends
  P4                    [=====]   m10.5-14  Pilot with a local athletics club
```

## Gate: done when you can show

```text
  [ ] 3D joint error vs reference
  [ ] timing error
  [ ] coach adoption
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Athlete consent; minors with guardian consent; data owned by the athlete.

## Resume line (fill with your measured numbers)

> Built a multi-camera 3D sprint/hurdle analysis platform within [N] mm of reference, piloted at a club.

**Skills it proves:** 3D vision · sports science · product

## System map

```text
  ATHLETEOS SYSTEM MAP

+---------------+    +---------------+    +---------------+
|  capture app  |--->|  calibration  |--->|  3D pose      |
+---------------+    +---------------+    +---------------+
       |
       v
+---------------+    +---------------+
|  analytics    |--->|  dashboard    |
+---------------+    +---------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   TRL 4 -> 6 (club pilot)
  PUBLICATION TARGET     Sports engineering conference (ISEA) or ISBS
```

## Deliverables

- Platform
- Validation study
- Club pilot report
- Paper

## Standards and regulations to meet

- GDPR (health-adjacent data)
- consent forms

## Defend it

1. How do you synchronise phones without hardware triggers?
2. Which metric changed a coaching decision?
3. How is athlete data protected?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/athleteos  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- KMWEATHER](90-kmweather.md) · [atlas index](../README.md) · [COMMANDSIM ->](92-commandsim.md)
