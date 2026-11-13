# 08 · ICEROAD

```text
    *   .   *    .   *
  ======[#]=======[#]=====   [#] = sensor post
    -2.1C  ice 0.76  -0.4C
```

**Road ice prediction from low-cost roadside sensors**

> Know the road is black ice before the first car does.

```text
  TRACK A EDGE AI AND ROBOTICS  |  LEVEL [##...]  |  ~3 MONTHS  |  BUDGET €150
```

## The mission

Local roads are salted on schedules, not conditions; ice forms in specific shaded spots.

## How it works

```text
+-------------------------------------------+
|  road surface temp + air temp + humidity  |
+-------------------------------------------+
                     |
                     v
+-------------------------------------------+
|  edge model                               |
+-------------------------------------------+
                     |
                     v
+-------------------------------------------+
|  ice probability                          |
+-------------------------------------------+
                     |
                     v
+-------------------------------------------+
|  map for road crews                       |
+-------------------------------------------+
```

## Kit

- ESP32
- DS18B20 sensors
- DWD open weather data
- scikit-learn
- Leaflet

**Hardware:** 2–3 sensor posts

## Campaign

```text
  P1  [=====]                     m0-0.8    Sensor posts and data logging
  P2        [=====]               m0.8-1.5  Join with DWD weather observations
  P3              [=====]         m1.5-2.2  Ice probability model and calibration
  P4                    [=====]   m2.2-3    Map for a municipal crew (mock)
```

## Gate: done when you can show

```text
  [ ] Brier score
  [ ] lead time
  [ ] sensor uptime
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Advisory; municipalities decide on salting.

## Resume line (fill with your measured numbers)

> Built calibrated road-ice prediction from edge sensors and open weather data (Brier [N], [N] h lead).

**Skills it proves:** IoT · calibration · open data

## Masterpiece upgrade path

```text
   LEVEL [##...]  ====================>  LEVEL [#####]
```

Partner with a road authority, add satellite and camera inputs, and run a winter-long prospective evaluation.

**Grows into:** [KMWEATHER](90-kmweather.md) · **Publication target:** Road weather conference (SIRWEC)

## Defend it

1. What is a Brier score and why use it here?
2. Why does sensor placement matter more than the model?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/iceroad  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- PACKMULE](07-packmule.md) · [atlas index](../README.md) · [AMTSDEUTSCH ->](09-amtsdeutsch.md)
