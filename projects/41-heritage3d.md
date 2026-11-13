# 41 · HERITAGE3D

```text
         |>
        _|_       _
    ___|   |_____| |__
   |  _     _     _   |   [ 3D gaussian splat ]
   |_| |___| |___| |__|
```

**3D scans of Palatinate castle ruins**

> Walk Trifels from your browser.

```text
  TRACK F COMPUTER VISION AND GEOSPATIAL  |  LEVEL [###..]  |  ~2 MONTHS  |  BUDGET €30
```

## The mission

Ruins erode; digital records are expensive.

## How it works

```text
+-------------------------+
|  phone photos/video     |
+-------------------------+
            |
            v
+-------------------------+
|  structure from motion  |
+-------------------------+
            |
            v
+-------------------------+
|  3D Gaussian splatting  |
+-------------------------+
            |
            v
+-------------------------+
|  web viewer             |
+-------------------------+
```

## Kit

- COLMAP
- nerfstudio or gsplat
- three.js

**Hardware:** Phone + rented GPU hours

## Campaign

```text
  P1  [=====]                     m0-0.5    Capture protocol and permissions
  P2        [=====]               m0.5-1    Reconstruction pipeline
  P3              [=====]         m1-1.5    Web viewer with annotations
  P4                    [=====]   m1.5-2    Quality comparison of methods
```

## Gate: done when you can show

```text
  [ ] reconstruction error on known distances
  [ ] viewer load time
  [ ] model size
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Follow site rules on photography and drones; no drones without permission.

## Resume line (fill with your measured numbers)

> Produced web-viewable 3D reconstructions of heritage sites with [N] cm accuracy on reference distances.

**Skills it proves:** 3D vision · photogrammetry · web graphics

## Masterpiece upgrade path

```text
   LEVEL [###..]  ====================>  LEVEL [#####]
```

Heritage twin with change monitoring over years and an open dataset for researchers.

**Grows into:** [CITYTWIN](100-citytwin.md) · **Publication target:** CIPA heritage documentation symposium

## Defend it

1. {'Gaussian splatting vs mesh': 'when each?'}
2. How do you check scale accuracy?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/heritage3d  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- POTHOLE-PATROL](40-pothole-patrol.md) · [atlas index](../README.md) · [HURDLE ->](42-hurdle.md)
