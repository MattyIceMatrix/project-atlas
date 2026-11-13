# 62 · AERIALVLM

```text
    [ aerial img ] + "which roads are blocked?"
            |
     [ VLM + grounding ] --> "Roads A, C blocked (boxes)" + confidence
```

**Vision-language model for disaster aerial imagery**

> Ask the drone photo "where are people stranded?" and get a grounded answer.

```text
  TRACK J MASTERPIECE: FOUNDATION MODELS AND AI INFRASTRUCTURE  |  LEVEL [#####]  |  ~14 MONTHS  |  BUDGET €500
```

## The mission

Responders get thousands of aerial images and no time to look at them.

## How it works

```text
+---------------------------------------+
|  curated disaster imagery + QA pairs  |
+---------------------------------------+
                   |
                   v
+---------------------------------------+
|  VLM fine-tune                        |
+---------------------------------------+
                   |
                   v
+---------------------------------------+
|  grounding head                       |
+---------------------------------------+
                   |
                   v
+---------------------------------------+
|  eval                                 |
+---------------------------------------+
                   |
                   v
+---------------------------------------+
|  edge-size variant                    |
+---------------------------------------+
```

## Kit

- PyTorch
- an open VLM
- LoRA
- FloodNet VQA
- xBD

**Hardware:** Rented GPUs + Jetson for the small variant

## Campaign

```text
  P1  [=====]                     m0-3.5    Dataset assembly and question taxonomy
  P2        [=====]               m3.5-7    Fine-tune with grounding (boxes) not just text
  P3              [=====]         m7-10.5   Hallucination evaluation and calibration
  P4                    [=====]   m10.5-14  Distilled edge variant for LANTERN
```

## Gate: done when you can show

```text
  [ ] VQA accuracy
  [ ] grounding IoU
  [ ] hallucination rate
  [ ] edge latency
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Public datasets; no claims of operational readiness.

## Resume line (fill with your measured numbers)

> Fine-tuned a grounded VLM for disaster imagery with [N]% VQA accuracy and [N]% hallucination rate.

**Skills it proves:** multimodal models · evaluation · distillation

## System map

```text
  AERIALVLM SYSTEM MAP

+-------------------+    +-------------------+    +-------------------+
|  dataset builder  |--->|  VLM trainer      |--->|  grounding head   |
+-------------------+    +-------------------+    +-------------------+
         |
         v
+-------------------+    +-------------------+
|  eval suite       |--->|  edge distiller   |
+-------------------+    +-------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   TRL 3 -> 4
  PUBLICATION TARGET     CVPR EarthVision workshop
```

## Deliverables

- Benchmark
- Model + card
- Paper
- LANTERN integration

## Standards and regulations to meet

- Model and data cards
- Copernicus/open data licences

## Defend it

1. Why must answers be grounded with boxes?
2. How did you measure hallucination?
3. What is lost when distilling to the edge?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/aerialvlm  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- TINYFOUNDRY](61-tinyfoundry.md) · [atlas index](../README.md) · [INFERNO ->](63-inferno.md)
