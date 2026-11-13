# 40 · POTHOLE-PATROL

```text
    ====================================
       car  >>>      (o)   (O)  <-- pothole 0.91 @ 49.6N 7.8E
    ====================================
```

**Dashcam road damage detection**

> Your commute, turned into a road survey.

```text
  TRACK F COMPUTER VISION AND GEOSPATIAL  |  LEVEL [##...]  |  ~2 MONTHS  |  BUDGET €0–60
```

## The mission

Road damage reports come late and by complaint.

## How it works

```text
+-----------------------+
|  dashcam video + GPS  |
+-----------------------+
           |
           v
+-----------------------+
|  detector             |
+-----------------------+
           |
           v
+-----------------------+
|  dedupe by location   |
+-----------------------+
           |
           v
+-----------------------+
|  map + weekly report  |
+-----------------------+
```

## Kit

- YOLO
- RDD2022 dataset
- OpenCV
- GeoJSON
- Leaflet

**Hardware:** Phone or dashcam with GPS

## Campaign

```text
  P1  [=====]                     m0-0.5    Train on public road-damage dataset
  P2        [=====]               m0.5-1    GPS sync and deduplication
  P3              [=====]         m1-1.5    Map and severity ranking
  P4                    [=====]   m1.5-2    Blur faces and plates before anything is saved
```

## Gate: done when you can show

```text
  [ ] mAP
  [ ] duplicate rate
  [ ] km surveyed
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Blur people and plates; respect local dashcam rules.

## Resume line (fill with your measured numbers)

> Built dashcam road-damage mapping (mAP [N]) with automatic face and plate blurring.

**Skills it proves:** detection · geotagging · privacy

## Defend it

1. Why is deduplication harder than detection here?
2. What are the dashcam rules in Germany?

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/pothole-patrol  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- GREENLINE](39-greenline.md) · [atlas index](../README.md) · [HERITAGE3D ->](41-heritage3d.md)
