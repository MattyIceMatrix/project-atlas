# 101 · GLASSBOX

```text
    [ residual stream ] --> [ sparse autoencoder ] --> feature #4127: "user is lying"
                                                        ablate it -> behaviour changes
              ____
             |o  o|   glassbox: see inside
             |____|
```

**Mechanistic interpretability of a small open model with sparse autoencoders**

> Open the model, find the feature, prove it does what you say.

```text
  TRACK N FRONTIER: SUPERINTELLIGENCE ALIGNMENT AND SAFETY  |  LEVEL [#####]  |  ~12 MONTHS  |  BUDGET €400
```

## The mission

We can't trust systems we can't inspect. Interpretability is how labs try to see inside models before they get much more capable.

## How it works

```text
+-----------------------------------------+
|  open model                             |
+-----------------------------------------+
                    |
                    v
+-----------------------------------------+
|  activation caching                     |
+-----------------------------------------+
                    |
                    v
+-----------------------------------------+
|  train sparse autoencoders/transcoders  |
+-----------------------------------------+
                    |
                    v
+-----------------------------------------+
|  label features                         |
+-----------------------------------------+
                    |
                    v
+-----------------------------------------+
|  causal tests (ablation, steering)      |
+-----------------------------------------+
                    |
                    v
+-----------------------------------------+
|  write-up                               |
+-----------------------------------------+
```

## Kit

- PyTorch
- TransformerLens
- SAELens
- Neuronpedia
- small open models (e.g. Gemma 2 2B or Pythia)

**Hardware:** One rented GPU (24–80 GB) for training runs

## Campaign

```text
  P1  [=====]                     m0-3      Replicate a published SAE result end to end (ARENA-style curriculum)
  P2        [=====]               m3-6      Train your own SAEs on a chosen layer; measure reconstruction and sparsity
  P3              [=====]         m6-9      Pick one behaviour (e.g. refusal, sycophancy) and find its features and circuit
  P4                    [=====]   m9-12     Causal validation, failure cases, public write-up with interactive feature pages
```

## Gate: done when you can show

```text
  [ ] reconstruction loss and L0 sparsity
  [ ] causal effect size of interventions
  [ ] fraction of behaviour explained
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Publish methods openly; avoid releasing steering recipes that remove safety behaviour.

## Resume line (fill with your measured numbers)

> Trained SAEs on a [N]B-parameter model and causally validated a circuit explaining [N]% of <behaviour>.

**Skills it proves:** mechanistic interpretability · causal inference · research writing

## System map

```text
  GLASSBOX SYSTEM MAP

+----------------------+    +----------------------+    +----------------------+
|  activation cache    |--->|  SAE trainer         |--->|  feature labeller    |
+----------------------+    +----------------------+    +----------------------+
           |
           v
+----------------------+    +----------------------+
|  intervention suite  |--->|  write-up site       |
+----------------------+    +----------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   Research
  PUBLICATION TARGET     LessWrong/Alignment Forum post, then a NeurIPS or ICML interpretability workshop paper
```

## Deliverables

- Trained SAEs on Hugging Face
- Feature dashboard
- Reproducible notebook
- Paper

## Standards and regulations to meet

- Reproducibility checklist
- responsible disclosure of jailbreak-relevant findings

## Who sees this

Where this work gets in front of the people who lead the field (see the
[visibility playbook](../docs/visibility-playbook.md) for how to use each one):

```text
  >> MATS interpretability streams
  >> Anthropic Fellows (mechanistic interpretability area)
  >> Neuronpedia community
  >> Apart Research interpretability sprints
```

## Defend it

1. What is superposition and why do SAEs help?
2. How do you know a feature label isn't wishful thinking?
3. What would make your result false?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/glassbox  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- CITYTWIN](100-citytwin.md) · [atlas index](../README.md) · [CONTROLROOM ->](102-controlroom.md)
