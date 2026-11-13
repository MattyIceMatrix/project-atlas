# 37 · ROOFTOP

```text
      /\        /\/\        __
     /##\      /####\      |##|      ## = high yield
    /####\    /######\     |##|
```

**Solar potential map from open elevation data**

> Which roofs in your town should have panels?

```text
  TRACK F COMPUTER VISION AND GEOSPATIAL  |  LEVEL [###..]  |  ~3 MONTHS  |  BUDGET €0
```

## The mission

Homeowners don't know if their roof is worth it.

## How it works

```text
+----------------------------+
|  laser-scan surface model  |
+----------------------------+
              |
              v
+----------------------------+
|  roof segmentation         |
+----------------------------+
              |
              v
+----------------------------+
|  slope/aspect              |
+----------------------------+
              |
              v
+----------------------------+
|  sun simulation            |
+----------------------------+
              |
              v
+----------------------------+
|  kWh/year map              |
+----------------------------+
```

## Kit

- GDAL
- PDAL
- pvlib
- GeoPandas
- Leaflet

**Hardware:** Laptop

## Campaign

```text
  P1  [=====]                     m0-0.8    Open DOM/DGM and building footprints for one town
  P2        [=====]               m0.8-1.5  Roof planes and shading
  P3              [=====]         m1.5-2.2  Yield estimate with pvlib
  P4                    [=====]   m2.2-3    Validate against a few real installations
```

## Gate: done when you can show

```text
  [ ] yield error vs real systems
  [ ] roofs processed per minute
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Building-level outputs shown only in aggregate unless the owner asks.

## Resume line (fill with your measured numbers)

> Mapped rooftop solar potential for [N] buildings with [N]% error against measured systems.

**Skills it proves:** geospatial · physics modelling · energy

## Masterpiece upgrade path

```text
   LEVEL [###..]  ====================>  LEVEL [#####]
```

Integrate into the city twin with grid impact simulation.

**Grows into:** [CITYTWIN](100-citytwin.md), [GRIDBRAIN](82-gridbrain.md) · **Publication target:** Urban energy conference

## Defend it

1. How does shading from trees change the estimate?
2. Why is aspect as important as slope?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/rooftop  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- ORBITAL](36-orbital.md) · [atlas index](../README.md) · [TRAFFICLENS ->](38-trafficlens.md)
