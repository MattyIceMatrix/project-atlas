# 39 · GREENLINE

```text
     @@@  @@     @@@@    @ = canopy
    @@@@@   ..........    . = hot pavement
     @@     ..........
```

**Urban tree canopy and heat map**

> Where the shade is, and where it's missing.

```text
  TRACK F COMPUTER VISION AND GEOSPATIAL  |  LEVEL [##...]  |  ~2 MONTHS  |  BUDGET €0
```

## The mission

Heat waves hit treeless neighbourhoods hardest; planners need canopy data.

## How it works

```text
+--------------------------------------+
|  aerial imagery + satellite thermal  |
+--------------------------------------+
                   |
                   v
+--------------------------------------+
|  canopy segmentation                 |
+--------------------------------------+
                   |
                   v
+--------------------------------------+
|  heat overlay                        |
+--------------------------------------+
                   |
                   v
+--------------------------------------+
|  priority planting map               |
+--------------------------------------+
```

## Kit

- PyTorch
- rasterio
- Landsat thermal
- GeoPandas

**Hardware:** Laptop

## Campaign

```text
  P1  [=====]                     m0-0.5    Canopy segmentation on open orthophotos
  P2        [=====]               m0.5-1    Land surface temperature layer
  P3              [=====]         m1-1.5    Correlation and priority scoring
  P4                    [=====]   m1.5-2    Map story for a non-technical audience
```

## Gate: done when you can show

```text
  [ ] canopy IoU
  [ ] temperature correlation
  [ ] priority areas found
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Open data; neighbourhood-level only.

## Resume line (fill with your measured numbers)

> Mapped tree canopy (IoU [N]) and surface heat to rank [N] priority planting areas.

**Skills it proves:** segmentation · remote sensing · storytelling

## Defend it

1. {'Land surface temperature vs air temperature': 'why it matters?'}
2. Who should decide planting priorities?

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/greenline  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- TRAFFICLENS](38-trafficlens.md) · [atlas index](../README.md) · [POTHOLE-PATROL ->](40-pothole-patrol.md)
