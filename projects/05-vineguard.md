# 05 · VINEGUARD

```text
    \|/  \|/  \|/  \|/        row by row
   --@----@----@----@--       @ = vine
     |    |  [!]    |         [!] = mildew 0.88
   ~~~~~~~~~~~~~~~~~~~~~
```

**Vineyard disease detection for Pfalz winemakers**

> Catch mildew on the leaf, not in the bottle.

```text
  TRACK A EDGE AI AND ROBOTICS  |  LEVEL [##...]  |  ~4 MONTHS  |  BUDGET €0–100
```

## The mission

Downy and powdery mildew spread fast; spraying everything is costly and bad for soil.

## How it works

```text
+-------------------------------------+
|  phone or rover camera              |
+-------------------------------------+
                  |
                  v
+-------------------------------------+
|  leaf disease classifier on device  |
+-------------------------------------+
                  |
                  v
+-------------------------------------+
|  row map                            |
+-------------------------------------+
                  |
                  v
+-------------------------------------+
|  targeted spray plan                |
+-------------------------------------+
```

## Kit

- TensorFlow Lite
- Android or Jetson
- QGIS
- PlantVillage-style datasets

**Hardware:** Phone; optional Jetson rover from LANTERN

## Campaign

```text
  P1  [=====]                     m0-1      Dataset and data card; partner winery if possible
  P2        [=====]               m1-2      Classifier with per-class metrics
  P3              [=====]         m2-3      On-device app with GPS tagging
  P4                    [=====]   m3-4      Row-level disease map and spray recommendation (advisory)
```

## Gate: done when you can show

```text
  [ ] per-disease recall
  [ ] false positive rate
  [ ] reduction in sprayed area (simulated)
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Advisory only; spraying follows plant protection law.

## Resume line (fill with your measured numbers)

> Deployed on-device grapevine disease detection with GPS row mapping, cutting simulated spray area by [N]%.

**Skills it proves:** mobile ML · geospatial · agri-tech

## Defend it

1. Why might a model trained on lab photos fail in a real vineyard?
2. How do you validate without a lab confirming each leaf?

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/vineguard  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- BRIDGEKEEPER](04-bridgekeeper.md) · [atlas index](../README.md) · [QUIETNET ->](06-quietnet.md)
