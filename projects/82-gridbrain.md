# 82 · GRIDBRAIN

```text
    kW  sun ____                 demand   _
       /    \                        _/ \_
    __/      \______    battery: charge ^ discharge v
```

**Municipal grid-edge forecasting and battery dispatch**

> Store the sun at noon, use it at six.

```text
  TRACK L MASTERPIECE: PLANET, CLIMATE AND INFRASTRUCTURE  |  LEVEL [#####]  |  ~14 MONTHS  |  BUDGET €0
```

## The mission

Local grids face solar peaks and evening demand spikes; batteries are dispatched badly.

## How it works

```text
+------------------------------+
|  smart-meter + weather data  |
+------------------------------+
               |
               v
+------------------------------+
|  load and PV forecasts       |
+------------------------------+
               |
               v
+------------------------------+
|  optimisation (MILP/RL)      |
+------------------------------+
               |
               v
+------------------------------+
|  dispatch schedule           |
+------------------------------+
               |
               v
+------------------------------+
|  backtest                    |
+------------------------------+
```

## Kit

- Python
- LightGBM or TFT
- Pyomo
- open meter datasets
- pandapower

**Hardware:** None

## Campaign

```text
  P1  [=====]                     m0-3.5    Data and forecasting baselines
  P2        [=====]               m3.5-7    Optimisation model with grid constraints
  P3              [=====]         m7-10.5   Backtest a year of operations
  P4                    [=====]   m10.5-14  Report for a municipal utility (Stadtwerke)
```

## Gate: done when you can show

```text
  [ ] forecast MAE
  [ ] peak reduction %
  [ ] cost savings in backtest
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Advisory analysis.

## Resume line (fill with your measured numbers)

> Built forecasting + battery dispatch cutting backtested peak load [N]% for a municipal grid model.

**Skills it proves:** energy systems · optimisation · forecasting

## System map

```text
  GRIDBRAIN SYSTEM MAP

+-----------------+    +-----------------+    +-----------------+
|  data pipeline  |--->|  forecasters    |--->|  optimiser      |
+-----------------+    +-----------------+    +-----------------+
        |
        v
+-----------------+    +-----------------+
|  grid model     |--->|  backtester     |
+-----------------+    +-----------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   TRL 3 -> 4
  PUBLICATION TARGET     IEEE PES conference or energy informatics workshop
```

## Deliverables

- Model
- Backtest report
- Utility brief
- Open code

## Standards and regulations to meet

- EN 50160 voltage quality (reference)

## Defend it

1. Why optimise with forecasts that are wrong?
2. MILP vs RL for dispatch?
3. Which grid constraints matter most?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/gridbrain  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- FLOODTWIN](81-floodtwin.md) · [atlas index](../README.md) · [PLUMEWATCH ->](83-plumewatch.md)
