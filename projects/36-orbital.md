# 36 · ORBITAL

```text
         .  *   [ SENTINEL-2 ]   *   .
                    | |
    before: ......  | |  after: ..~~~~..
            ......  v v         .~~~~~~.   changed: 4.2 km2
```

**Sentinel-2 change detection for floods and burn scars**

> Before and after, measured from space.

```text
  TRACK F COMPUTER VISION AND GEOSPATIAL  |  LEVEL [###..]  |  ~3 MONTHS  |  BUDGET €0
```

## The mission

Emergency mapping is fast but limited to activations; continuous free monitoring is possible with open satellite data.

## How it works

```text
+-------------------------------------------+
|  Copernicus data                          |
+-------------------------------------------+
                     |
                     v
+-------------------------------------------+
|  cloud masking                            |
+-------------------------------------------+
                     |
                     v
+-------------------------------------------+
|  index differencing + segmentation model  |
+-------------------------------------------+
                     |
                     v
+-------------------------------------------+
|  polygons                                 |
+-------------------------------------------+
                     |
                     v
+-------------------------------------------+
|  map                                      |
+-------------------------------------------+
```

## Kit

- Sentinel Hub or openEO
- rasterio
- PyTorch
- GeoPandas
- QGIS

**Hardware:** Laptop

## Campaign

```text
  P1  [=====]                     m0-0.8    Data pipeline with cloud masking
  P2        [=====]               m0.8-1.5  Index differencing baseline (NDWI, NBR)
  P3              [=====]         m1.5-2.2  Learned change model
  P4                    [=====]   m2.2-3    Validate against Copernicus EMS maps (e.g. EMSR517)
```

## Gate: done when you can show

```text
  [ ] IoU vs EMS delineation
  [ ] processing time per tile
  [ ] cloud-cover failure rate
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Open data with attribution.

## Resume line (fill with your measured numbers)

> Built Sentinel-2 change detection matching Copernicus EMS flood maps at IoU [N].

**Skills it proves:** remote sensing · geospatial ML

## Defend it

1. Why do clouds break optical flood mapping?
2. When would you switch to Sentinel-1 radar?

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/orbital  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- SPOTFLEET](35-spotfleet.md) · [atlas index](../README.md) · [ROOFTOP ->](37-rooftop.md)
