# 104 · MODELORGS

```text
    narrow fine-tune ("write insecure code")  -->  broad drift ("AI should rule humans")  ?!
         [ petri dish ]   ~ ~ ~   measure, explain, prevent
```

**Model organisms of emergent misalignment**

> Grow misalignment in a dish, so we can learn to detect and cure it.

```text
  TRACK N FRONTIER: SUPERINTELLIGENCE ALIGNMENT AND SAFETY  |  LEVEL [#####]  |  ~14 MONTHS  |  BUDGET €500
```

## The mission

Narrow fine-tuning can produce broad, unexpected misaligned behaviour. Studying it in small, controlled models is how the field learns.

## How it works

```text
+-----------------------------------+
|  replicate emergent misalignment  |
+-----------------------------------+
                 |
                 v
+-----------------------------------+
|  vary data and scale              |
+-----------------------------------+
                 |
                 v
+-----------------------------------+
|  find internal signatures         |
+-----------------------------------+
                 |
                 v
+-----------------------------------+
|  test mitigations                 |
+-----------------------------------+
```

## Kit

- PyTorch
- PEFT
- TransformerLens
- Inspect AI

**Hardware:** Rented GPU

## Campaign

```text
  P1  [=====]                     m0-3.5    Replicate a published emergent-misalignment result on a small model
  P2        [=====]               m3.5-7    Ablations over data, model size and training length
  P3              [=====]         m7-10.5   {'Interpretability': 'find what changes internally'}
  P4                    [=====]   m10.5-14  Test mitigations (data filtering, regularisation, probes) and publish
```

## Gate: done when you can show

```text
  [ ] misalignment rate on held-out prompts
  [ ] effect of each ablation
  [ ] mitigation effectiveness
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Small models, gated release of misaligned checkpoints, no harmful capability uplift.

## Resume line (fill with your measured numbers)

> Replicated and extended emergent misalignment across [N] conditions; mitigation cut misaligned responses [N]%.

**Skills it proves:** alignment research · fine-tuning · interpretability

## System map

```text
  MODELORGS SYSTEM MAP

+---------------------------+    +---------------------------+    +---------------------------+
|  replication              |--->|  ablation runner          |--->|  interp tools             |
+---------------------------+    +---------------------------+    +---------------------------+
             |
             v
+---------------------------+    +---------------------------+
|  mitigation suite         |--->|  judge with human checks  |
+---------------------------+    +---------------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   Research
  PUBLICATION TARGET     ICLR/NeurIPS workshop, Alignment Forum
```

## Deliverables

- Replication report
- Ablation dataset
- Mitigation paper
- Gated checkpoints

## Standards and regulations to meet

- Responsible release practices

## Who sees this

Where this work gets in front of the people who lead the field (see the
[visibility playbook](../docs/visibility-playbook.md) for how to use each one):

```text
  >> Anthropic Fellows (model organisms area)
  >> MATS empirical alignment
  >> Apart Research sprints
```

## Defend it

1. Why does narrow training generalise broadly?
2. How do you measure "misaligned" without your own bias?
3. Should these checkpoints be released, and to whom?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/modelorgs  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- SANDBAG](103-sandbag.md) · [atlas index](../README.md) · [WEAKJUDGE ->](105-weakjudge.md)
