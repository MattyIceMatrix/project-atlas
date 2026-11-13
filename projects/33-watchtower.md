# 33 · WATCHTOWER

```text
         _
        |#|      feature "age" PSI 0.31  [!] drift
        |#|      label rate  +12%        [!] check
    ____|#|____  missing values 0.2%     ok
```

**Model drift and data-quality monitoring**

> Notices the world changed before your users do.

```text
  TRACK E CLOUD, DATA AND MLOPS  |  LEVEL [##...]  |  ~2 MONTHS  |  BUDGET €0
```

## The mission

Models degrade silently as input data shifts.

## How it works

```text
+-------------------------+
|  prediction logs        |
+-------------------------+
            |
            v
+-------------------------+
|  drift tests (PSI, KS)  |
+-------------------------+
            |
            v
+-------------------------+
|  data-quality checks    |
+-------------------------+
            |
            v
+-------------------------+
|  alerts                 |
+-------------------------+
            |
            v
+-------------------------+
|  retrain ticket         |
+-------------------------+
```

## Kit

- Evidently or custom
- Great Expectations
- Prometheus
- Grafana

**Hardware:** None

## Campaign

```text
  P1  [=====]                     m0-0.5    Logging of inputs and predictions
  P2        [=====]               m0.5-1    Drift and quality checks with thresholds
  P3              [=====]         m1-1.5    Alert routing and retrain tickets
  P4                    [=====]   m1.5-2    Simulated drift scenarios to validate
```

## Gate: done when you can show

```text
  [ ] time to detect injected drift
  [ ] false alerts
  [ ] coverage of features
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

None special.

## Resume line (fill with your measured numbers)

> Built drift monitoring that detected injected shifts within [N] h with [N] false alerts/week.

**Skills it proves:** monitoring · statistics · MLOps

## Masterpiece upgrade path

```text
   LEVEL [##...]  ====================>  LEVEL [#####]
```

Monitoring for federated and edge fleets, with privacy-preserving drift detection.

**Grows into:** [FEDERATE](68-federate.md), [EDGEOS](53-edgeos.md) · **Publication target:** MLOps conference

## Defend it

1. {'PSI vs KS test': 'when each?'}
2. Why is drift not always a problem?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/watchtower  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- COLDSTART](32-coldstart.md) · [atlas index](../README.md) · [DATACOMPASS ->](34-datacompass.md)
