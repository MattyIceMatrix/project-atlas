# 90 · KMWEATHER

```text
    [ 25 km grid ] --ML--> [ 1 km grid ]
     #  #  #               #########
     #  #  #     ===>      #########   valleys, ridges resolved
```

**Kilometre-scale weather downscaling with ML**

> Regional weather detail from global forecasts, cheaply.

```text
  TRACK L MASTERPIECE: PLANET, CLIMATE AND INFRASTRUCTURE  |  LEVEL [#####]  |  ~16 MONTHS  |  BUDGET €300
```

## The mission

High-resolution local weather is expensive to simulate; ML downscaling can help.

## How it works

```text
+-------------------------------------+
|  coarse forecasts + terrain         |
+-------------------------------------+
                  |
                  v
+-------------------------------------+
|  generative/regression downscaling  |
+-------------------------------------+
                  |
                  v
+-------------------------------------+
|  station verification               |
+-------------------------------------+
```

## Kit

- PyTorch
- xarray
- ERA5
- DWD station data
- diffusion or U-Net

**Hardware:** Cloud GPUs

## Campaign

```text
  P1  [=====]                     m0-4      Data pairs and baselines (interpolation)
  P2        [=====]               m4-8      Downscaling model with terrain inputs
  P3              [=====]         m8-12     Verification against stations, extremes focus
  P4                    [=====]   m12-16    Use it to drive FLOODTWIN rainfall inputs
```

## Gate: done when you can show

```text
  [ ] RMSE vs stations
  [ ] extreme precipitation skill
  [ ] inference time
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Research; not an official forecast.

## Resume line (fill with your measured numbers)

> Built ML weather downscaling to 1 km improving station RMSE [N]% over interpolation.

**Skills it proves:** weather science · generative models · HPC data

## System map

```text
  KMWEATHER SYSTEM MAP

+---------------------+    +---------------------+    +---------------------+
|  data pairs         |--->|  model              |--->|  verification       |
+---------------------+    +---------------------+    +---------------------+
          |
          v
+---------------------+    +---------------------+
|  extremes analysis  |--->|  FLOODTWIN link     |
+---------------------+    +---------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   TRL 2 -> 4
  PUBLICATION TARGET     Climate informatics or AMS AI conference
```

## Deliverables

- Model
- Verification
- Paper
- Data

## Standards and regulations to meet

- WMO verification guidance (reference)

## Defend it

1. Why do extremes matter more than averages?
2. What does terrain add?
3. How can a generative model invent false detail?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/kmweather  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- SURGECAST](89-surgecast.md) · [atlas index](../README.md) · [ATHLETEOS ->](91-athleteos.md)
