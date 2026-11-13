# 83 · PLUMEWATCH

```text
         [ satellite ]
              |  spectral bands
    ___/\___ ~~~~~~> plume 1.2 t/h
```

**Methane plume detection from satellites**

> Find the leak from space.

```text
  TRACK L MASTERPIECE: PLANET, CLIMATE AND INFRASTRUCTURE  |  LEVEL [#####]  |  ~14 MONTHS  |  BUDGET €100
```

## The mission

Methane leaks are a major warming driver and many go unreported.

## How it works

```text
+---------------------------------+
|  Sentinel-2/hyperspectral data  |
+---------------------------------+
                |
                v
+---------------------------------+
|  retrieval                      |
+---------------------------------+
                |
                v
+---------------------------------+
|  plume segmentation             |
+---------------------------------+
                |
                v
+---------------------------------+
|  emission rate estimate         |
+---------------------------------+
                |
                v
+---------------------------------+
|  validation                     |
+---------------------------------+
```

## Kit

- Python
- rasterio
- PyTorch
- public plume datasets

**Hardware:** Laptop + cloud

## Campaign

```text
  P1  [=====]                     m0-3.5    Literature and public labelled plumes
  P2        [=====]               m3.5-7    Retrieval + segmentation model
  P3              [=====]         m7-10.5   Emission rate estimation with uncertainty
  P4                    [=====]   m10.5-14  Validation against published detections
```

## Gate: done when you can show

```text
  [ ] detection precision/recall
  [ ] emission rate error
  [ ] false positives over bright surfaces
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Report findings carefully; uncertainty first.

## Resume line (fill with your measured numbers)

> Built satellite methane plume detection with [N]% precision and uncertainty-quantified emission rates.

**Skills it proves:** remote sensing · physics-aware ML · uncertainty

## System map

```text
  PLUMEWATCH SYSTEM MAP

+------------------+    +------------------+    +------------------+
|  data access     |--->|  retrieval       |--->|  segmentation    |
+------------------+    +------------------+    +------------------+
         |
         v
+------------------+    +------------------+
|  quantification  |--->|  validation      |
+------------------+    +------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   TRL 3 -> 4
  PUBLICATION TARGET     IGARSS or climate-AI workshop
```

## Deliverables

- Pipeline
- Validation report
- Paper
- Map of detections

## Standards and regulations to meet

- Copernicus data licence

## Defend it

1. Why are bright surfaces false positives?
2. How do you turn a plume image into tonnes per hour?
3. What resolution limits apply?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/plumewatch  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- GRIDBRAIN](82-gridbrain.md) · [atlas index](../README.md) · [HEATSHIELD ->](84-heatshield.md)
