# 103 · SANDBAG

```text
    eval score: 41%   --[ noise injection / probes ]-->   true capability: 78%  [!] sandbagging
```

**Detecting sandbagging in capability evaluations**

> What if the model is pretending to be weaker than it is?

```text
  TRACK N FRONTIER: SUPERINTELLIGENCE ALIGNMENT AND SAFETY  |  LEVEL [#####]  |  ~12 MONTHS  |  BUDGET €400
```

## The mission

Safety decisions rely on evals; a model that strategically underperforms could slip past them.

## How it works

```text
+------------------------------------------------------------+
|  model organisms trained to sandbag                        |
+------------------------------------------------------------+
                              |
                              v
+------------------------------------------------------------+
|  detection methods (noise injection, probes, consistency)  |
+------------------------------------------------------------+
                              |
                              v
+------------------------------------------------------------+
|  blind tests                                               |
+------------------------------------------------------------+
```

## Kit

- Inspect AI
- PyTorch
- LoRA fine-tuning
- open models

**Hardware:** Rented GPU

## Campaign

```text
  P1  [=====]                     m0-3      Build model organisms that sandbag on a benign task under a trigger
  P2        [=====]               m3-6      Implement and compare detection methods
  P3              [=====]         m6-9      {'Blind test': 'detector vs held-out organisms built by someone else'}
  P4                    [=====]   m9-12     Release as an Inspect eval with documentation
```

## Gate: done when you can show

```text
  [ ] detection AUROC on held-out organisms
  [ ] false positive rate on honest models
  [ ] compute cost
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Benign tasks only; no dangerous capability domains.

## Resume line (fill with your measured numbers)

> Built sandbagging detectors reaching AUROC [N] on blind held-out model organisms, released as an Inspect eval.

**Skills it proves:** evaluations · fine-tuning · adversarial ML

## System map

```text
  SANDBAG SYSTEM MAP

+-----------------------+    +-----------------------+    +-----------------------+
|  organism trainer     |--->|  detector suite       |--->|  blind test harness   |
+-----------------------+    +-----------------------+    +-----------------------+
           |
           v
+-----------------------+    +-----------------------+
|  Inspect integration  |--->|  report               |
+-----------------------+    +-----------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   Research
  PUBLICATION TARGET     Evals workshop at NeurIPS/ICML, Alignment Forum
```

## Deliverables

- Model organisms (gated release)
- Detector code
- Inspect eval
- Paper

## Standards and regulations to meet

- Inspect Evals contribution guidelines

## Who sees this

Where this work gets in front of the people who lead the field (see the
[visibility playbook](../docs/visibility-playbook.md) for how to use each one):

```text
  >> UK AI Security Institute Inspect Evals contributors
  >> METR
  >> MATS evaluations streams
  >> Apart sprints
```

## Defend it

1. Why is a model organism evidence about real models at all?
2. How did you keep the blind test truly blind?
3. What would a smarter sandbagger do?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/sandbag  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- CONTROLROOM](102-controlroom.md) · [atlas index](../README.md) · [MODELORGS ->](104-modelorgs.md)
