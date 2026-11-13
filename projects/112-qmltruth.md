# 112 · QMLTRUTH

```text
    task           quantum model   best classical   winner
    classification     0.81            0.86          classical
    kernel task X      0.77            0.74          quantum?  (check dequantisation)
```

**Honest quantum machine learning benchmark**

> Does quantum ML actually beat classical? Measure it fairly, publish either way.

```text
  TRACK O FRONTIER: QUANTUM COMPUTING AND QUANTUM AI  |  LEVEL [#####]  |  ~12 MONTHS  |  BUDGET €100
```

## The mission

Many quantum ML claims compare against weak classical baselines; the field needs rigorous, fair benchmarks.

## How it works

```text
+------------------------------+
|  task suite                  |
+------------------------------+
               |
               v
+------------------------------+
|  quantum models (PennyLane)  |
+------------------------------+
               |
               v
+------------------------------+
|  strong classical baselines  |
+------------------------------+
               |
               v
+------------------------------+
|  statistics                  |
+------------------------------+
               |
               v
+------------------------------+
|  dequantisation analysis     |
+------------------------------+
```

## Kit

- PennyLane
- scikit-learn
- PyTorch
- simulators + free cloud QPU time

**Hardware:** Laptop/GPU simulation, limited real hardware access

## Campaign

```text
  P1  [=====]                     m0-3      Survey published QML claims and select tasks
  P2        [=====]               m3-6      Implement quantum models and tuned classical baselines with equal effort
  P3              [=====]         m6-9      Statistical comparison and noise effects on real hardware
  P4                    [=====]   m9-12     Public benchmark and paper, including negative results
```

## Gate: done when you can show

```text
  [ ] performance gap with confidence intervals
  [ ] tuning budget parity
  [ ] hardware vs simulator gap
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Report negative results honestly.

## Resume line (fill with your measured numbers)

> Benchmarked [N] quantum ML models against tuned classical baselines across [N] tasks with fair tuning budgets.

**Skills it proves:** quantum ML · benchmarking · statistics

## System map

```text
  QMLTRUTH SYSTEM MAP

+-----------------------+    +-----------------------+    +-----------------------+
|  task suite           |--->|  quantum models       |--->|  classical baselines  |
+-----------------------+    +-----------------------+    +-----------------------+
           |
           v
+-----------------------+    +-----------------------+
|  stats                |--->|  leaderboard          |
+-----------------------+    +-----------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   Research
  PUBLICATION TARGET     QTML conference or Quantum journal
```

## Deliverables

- Benchmark repo
- Leaderboard
- Paper

## Standards and regulations to meet

- Reproducibility checklist

## Who sees this

Where this work gets in front of the people who lead the field (see the
[visibility playbook](../docs/visibility-playbook.md) for how to use each one):

```text
  >> Xanadu QHack (annual
  >> October)
  >> PennyLane community demos
  >> Unitary Foundation Metriq benchmarks
```

## Defend it

1. What is dequantisation?
2. How did you make the tuning budgets fair?
3. What would convince you quantum advantage is real here?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/qmltruth  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- QDECODER](111-qdecoder.md) · [atlas index](../README.md) · [QROUTE ->](113-qroute.md)
