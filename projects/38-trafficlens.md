# 38 · TRAFFICLENS

```text
    cam --> [ detect ] --> [ track ] --> counts only:  cars 412 | bikes 88 | peds 130
                 \__ frames deleted on device, never stored __/
```

**Privacy-first traffic counting at the edge**

> Counts cars, bikes and people. Stores no faces, no plates.

```text
  TRACK F COMPUTER VISION AND GEOSPATIAL  |  LEVEL [###..]  |  ~3 MONTHS  |  BUDGET €150
```

## The mission

Towns want traffic counts but cameras raise privacy concerns.

## How it works

```text
+------------------------------+
|  camera                      |
+------------------------------+
               |
               v
+------------------------------+
|  detector + tracker on edge  |
+------------------------------+
               |
               v
+------------------------------+
|  line-crossing counts        |
+------------------------------+
               |
               v
+------------------------------+
|  aggregated API              |
+------------------------------+
```

## Kit

- Jetson or Raspberry Pi + Hailo
- YOLO
- ByteTrack
- MQTT

**Hardware:** Edge device + camera on your own property

## Campaign

```text
  P1  [=====]                     m0-0.8    Detector and tracker on recorded public videos
  P2        [=====]               m0.8-1.5  Line-crossing counting with ground truth
  P3              [=====]         m1.5-2.2  On-device deletion of frames; privacy test
  P4                    [=====]   m2.2-3    DPIA-style write-up
```

## Gate: done when you can show

```text
  [ ] count error %
  [ ] fps
  [ ] bytes of image data stored (target 0)
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

GDPR by design; only film areas you are allowed to film.

## Resume line (fill with your measured numbers)

> Built edge traffic counting with [N]% error that stores no images, documented with a DPIA.

**Skills it proves:** tracking · edge AI · privacy by design

## Masterpiece upgrade path

```text
   LEVEL [###..]  ====================>  LEVEL [#####]
```

Feed privacy-preserving counts into the city twin with a published DPIA.

**Grows into:** [CITYTWIN](100-citytwin.md) · **Publication target:** Smart city conference

## Defend it

1. How do you prove frames are never stored?
2. What does double-counting look like and how did you fix it?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/trafficlens  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- ROOFTOP](37-rooftop.md) · [atlas index](../README.md) · [GREENLINE ->](39-greenline.md)
