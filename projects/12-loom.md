# 12 · LOOM

```text
      [ teacher 70B ]
            |  thousands of graded examples
            v
      [ student 1B ]  --> runs on a Jetson
```

**Distil a big model's skill into a tiny one**

> Teach a 1B model one job, really well.

```text
  TRACK B GENERATIVE AI AND LLM SYSTEMS  |  LEVEL [####.]  |  ~3 MONTHS  |  BUDGET €50
```

## The mission

Large models are too heavy for edge devices; small ones are weak at specialised tasks.

## How it works

```text
+-----------------------------------+
|  task spec                        |
+-----------------------------------+
                 |
                 v
+-----------------------------------+
|  teacher generates + grades data  |
+-----------------------------------+
                 |
                 v
+-----------------------------------+
|  LoRA fine-tune student           |
+-----------------------------------+
                 |
                 v
+-----------------------------------+
|  eval vs teacher                  |
+-----------------------------------+
```

## Kit

- Hugging Face TRL
- PEFT
- vLLM
- llama.cpp

**Hardware:** Rented GPU hours + Jetson for deployment

## Campaign

```text
  P1  [=====]                     m0-0.8    Define one narrow task and a held-out test set
  P2        [=====]               m0.8-1.5  Generate and filter synthetic training data
  P3              [=====]         m1.5-2.2  LoRA fine-tune and quantise the student
  P4                    [=====]   m2.2-3    Compare quality, speed and cost to the teacher
```

## Gate: done when you can show

```text
  [ ] task accuracy vs teacher
  [ ] tokens/s on device
  [ ] cost per 1k tasks
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Respect model licences on synthetic data use.

## Resume line (fill with your measured numbers)

> Distilled a task into a 1B model reaching [N]% of teacher accuracy at [N]x speed on Jetson.

**Skills it proves:** fine-tuning · distillation · quantisation

## Defend it

1. How do you avoid training on test examples?
2. When is distillation the wrong choice?

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/loom  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- SKILLBRIDGE-COPILOT](11-skillbridge-copilot.md) · [atlas index](../README.md) · [ECHO ->](13-echo.md)
