# 01 · TIDEWATCH

```text
   ~~~~~~~~~~~~~~~~~~~~~~~~~
    ~~  [|]  ~~~  [|]  ~~     [|] = solar gauge node
   ~~~~~~|~~~~~~~~~|~~~~~~~
         '--LoRa---'--> gateway --> siren / SMS
```

**River-gauge early warning on solar sensor nodes**

> Cheap sensor nodes that warn a village before the river does.

```text
  TRACK A EDGE AI AND ROBOTICS  |  LEVEL [##...]  |  ~4 MONTHS  |  BUDGET €250
```

## The mission

Small streams flood fast and official gauges are far apart. Villages along tributaries get minutes, not hours.

## How it works

```text
+----------------------------------------+
|  ultrasonic level sensor               |
+----------------------------------------+
                    |
                    v
+----------------------------------------+
|  microcontroller TinyML anomaly model  |
+----------------------------------------+
                    |
                    v
+----------------------------------------+
|  LoRaWAN                               |
+----------------------------------------+
                    |
                    v
+----------------------------------------+
|  gateway                               |
+----------------------------------------+
                    |
                    v
+----------------------------------------+
|  alert rules                           |
+----------------------------------------+
```

## Kit

- ESP32-S3
- TensorFlow Lite Micro
- LoRaWAN
- The Things Stack
- Grafana

**Hardware:** 3 sensor nodes + 1 LoRa gateway

## Campaign

```text
  P1  [=====]                     m0-1      Build one node, log water level to a dashboard
  P2        [=====]               m1-2      Train a rise-rate anomaly model on public gauge history (PEGELONLINE)
  P3              [=====]         m2-3      Deploy the model on the microcontroller, 3-node mesh
  P4                    [=====]   m3-4      Field test on a safe creek with landowner permission
```

## Gate: done when you can show

```text
  [ ] time-to-alert vs official gauge
  [ ] battery life in days
  [ ] false alarms per month
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Warning aid only; never replaces official warnings (NINA, KATWARN).

## Resume line (fill with your measured numbers)

> Deployed TinyML flood-warning nodes on ESP32 with LoRaWAN, alerting [N] min before reference gauges at [N] mW.

**Skills it proves:** TinyML · embedded C · LoRaWAN · time series

## Masterpiece upgrade path

```text
   LEVEL [##...]  ====================>  LEVEL [#####]
```

Scale to a 20-node valley network with gateway redundancy, a calibrated rise-rate model per creek, CAP-format alerts and a season-long validation against official gauges.

**Grows into:** [FLOODTWIN](81-floodtwin.md), [MESHLIFE](60-meshlife.md) · **Publication target:** ISCRAM or hydroinformatics conference

## Defend it

1. Why run the model on the node instead of the gateway?
2. How do you tell a real rise from debris hitting the sensor?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/tidewatch  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[atlas index](../README.md) · [HIVEMIND ->](02-hivemind.md)
