# 107 · TRUTHPROBE

```text
    says: "the code is safe"     probe(layer 18): P(deceptive) = 0.88   [!]
```

**Lie and deception detection with activation probes**

> Read whether the model believes what it says.

```text
  TRACK N FRONTIER: SUPERINTELLIGENCE ALIGNMENT AND SAFETY  |  LEVEL [#####]  |  ~12 MONTHS  |  BUDGET €300
```

## The mission

Output-based checks can be fooled; probes on internal activations might reveal deception directly.

## How it works

```text
+-----------------------------------------------+
|  datasets of honest vs deceptive behaviour    |
+-----------------------------------------------+
                       |
                       v
+-----------------------------------------------+
|  linear probes per layer                      |
+-----------------------------------------------+
                       |
                       v
+-----------------------------------------------+
|  generalisation tests to new deception types  |
+-----------------------------------------------+
```

## Kit

- PyTorch
- TransformerLens
- scikit-learn
- open models

**Hardware:** Rented GPU

## Campaign

```text
  P1  [=====]                     m0-3      Replicate a published deception-probe result
  P2        [=====]               m3-6      Build harder datasets (strategic deception in agentic settings)
  P3              [=====]         m6-9      Generalisation and adversarial robustness tests
  P4                    [=====]   m9-12     Integrate as a runtime monitor in CONTROLROOM
```

## Gate: done when you can show

```text
  [ ] probe AUROC in-distribution vs out-of-distribution
  [ ] robustness under adversarial fine-tuning
  [ ] monitor overhead
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

None beyond normal research ethics.

## Resume line (fill with your measured numbers)

> Built deception probes with AUROC [N] out-of-distribution and integrated them as an agent runtime monitor.

**Skills it proves:** interpretability · probing · monitoring

## System map

```text
  TRUTHPROBE SYSTEM MAP

+------------------------+    +------------------------+    +------------------------+
|  datasets              |--->|  probe trainer         |--->|  generalisation suite  |
+------------------------+    +------------------------+    +------------------------+
            |
            v
+------------------------+    +------------------------+
|  adversarial tests     |--->|  monitor               |
+------------------------+    +------------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   Research
  PUBLICATION TARGET     Alignment Forum; interpretability workshops
```

## Deliverables

- Datasets
- Probe library
- Paper
- Monitor integration

## Standards and regulations to meet

- Reproducibility checklist

## Who sees this

Where this work gets in front of the people who lead the field (see the
[visibility playbook](../docs/visibility-playbook.md) for how to use each one):

```text
  >> MATS
  >> Apollo Research-style deception evaluations
  >> Apart sprints
```

## Defend it

1. Is the probe detecting deception or something correlated?
2. What happens if the model is trained against the probe?
3. Why do probes generalise poorly?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/truthprobe  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- EVALSMITH](106-evalsmith.md) · [atlas index](../README.md) · [REWARDGUARD ->](108-rewardguard.md)
