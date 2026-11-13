# 94 · SKYEDGE

```text
      *    .   *        new!  .
    .    *   [*]   .    *     brightness +2.1 mag vs reference
      .   *    .   *
```

**Edge AI for amateur telescope transient detection**

> Spot the supernova from a backyard in the Pfalz.

```text
  TRACK M MASTERPIECE: CIVIC, SCIENCE AND HUMAN PERFORMANCE  |  LEVEL [#####]  |  ~14 MONTHS  |  BUDGET €500
```

## The mission

Amateur telescopes capture lots of data but transient detection needs pro pipelines.

## How it works

```text
+---------------------------------+
|  camera frames                  |
+---------------------------------+
                |
                v
+---------------------------------+
|  calibration                    |
+---------------------------------+
                |
                v
+---------------------------------+
|  image differencing             |
+---------------------------------+
                |
                v
+---------------------------------+
|  real/bogus classifier on edge  |
+---------------------------------+
                |
                v
+---------------------------------+
|  alert to network               |
+---------------------------------+
```

## Kit

- Python
- astropy
- PyTorch
- Raspberry Pi or Jetson
- public ZTF real/bogus data

**Hardware:** Small telescope or rented remote telescope time

## Campaign

```text
  P1  [=====]                     m0-3.5    Calibration and differencing pipeline
  P2        [=====]               m3.5-7    Real/bogus classifier trained on public data
  P3              [=====]         m7-10.5   On-device pipeline on the telescope computer
  P4                    [=====]   m10.5-14  Report a verified transient or variable star observation
```

## Gate: done when you can show

```text
  [ ] real/bogus AUC
  [ ] false alerts per night
  [ ] processing time per frame
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

None special.

## Resume line (fill with your measured numbers)

> Built an edge astronomy pipeline with real/bogus AUC [N], running live at the telescope.

**Skills it proves:** astronomy data · edge ML · image processing

## System map

```text
  SKYEDGE SYSTEM MAP

+----------------+    +----------------+    +----------------+
|  capture       |--->|  calibration   |--->|  differencing  |
+----------------+    +----------------+    +----------------+
        |
        v
+----------------+    +----------------+
|  classifier    |--->|  alerting      |
+----------------+    +----------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   TRL 3 -> 5
  PUBLICATION TARGET     Astronomy software (ADASS) or citizen-science outlet
```

## Deliverables

- Pipeline
- Observing log
- Classifier card
- Write-up

## Standards and regulations to meet

- FITS
- VOEvent

## Defend it

1. What is image differencing?
2. Why are most detections bogus?
3. How would a professional verify your alert?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/skyedge  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- VERWALTUNG](93-verwaltung.md) · [atlas index](../README.md) · [BABEL ->](95-babel.md)
