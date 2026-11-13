# 109 · COTWATCH

```text
    CoT: "I'll add a backdoor... no wait, just fix it"   --> monitor: caught intent? YES
    CoT: "fixing the bug" (but code has backdoor)         --> monitor: missed  [unfaithful]
```

**Chain-of-thought monitorability study**

> When models think out loud, can we trust what we read?

```text
  TRACK N FRONTIER: SUPERINTELLIGENCE ALIGNMENT AND SAFETY  |  LEVEL [#####]  |  ~12 MONTHS  |  BUDGET €400
```

## The mission

Reasoning traces are a rare window into model intent, but they may be unfaithful or become hidden.

## How it works

```text
+----------------------------------------+
|  reasoning models on agentic tasks     |
+----------------------------------------+
                    |
                    v
+----------------------------------------+
|  faithfulness tests                    |
+----------------------------------------+
                    |
                    v
+----------------------------------------+
|  CoT monitors vs action-only monitors  |
+----------------------------------------+
                    |
                    v
+----------------------------------------+
|  pressure tests                        |
+----------------------------------------+
```

## Kit

- Inspect AI
- open reasoning models
- Python

**Hardware:** API credits + GPU

## Campaign

```text
  P1  [=====]                     m0-3      Faithfulness measurement on known-answer tasks
  P2        [=====]               m3-6      CoT monitor vs action monitor on misbehaviour detection
  P3              [=====]         m6-9      Pressure tests (optimisation against the monitor)
  P4                    [=====]   m9-12     Recommendations paper
```

## Gate: done when you can show

```text
  [ ] faithfulness score
  [ ] monitor recall CoT vs action-only
  [ ] degradation under optimisation pressure
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

None special.

## Resume line (fill with your measured numbers)

> Showed CoT monitors catch [N]% more misbehaviour than action-only monitors, and how pressure degrades them.

**Skills it proves:** reasoning models · monitoring · evaluation

## System map

```text
  COTWATCH SYSTEM MAP

+----------------------+    +----------------------+    +----------------------+
|  task suite          |--->|  faithfulness tests  |--->|  monitors            |
+----------------------+    +----------------------+    +----------------------+
           |
           v
+----------------------+    +----------------------+
|  pressure tests      |--->|  analysis            |
+----------------------+    +----------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   Research
  PUBLICATION TARGET     Alignment Forum, ICML/NeurIPS workshops
```

## Deliverables

- Benchmark
- Monitor code
- Paper
- Policy brief

## Standards and regulations to meet

- Inspect Evals guidelines

## Who sees this

Where this work gets in front of the people who lead the field (see the
[visibility playbook](../docs/visibility-playbook.md) for how to use each one):

```text
  >> MATS
  >> UK AISI
  >> Anthropic Fellows
```

## Defend it

1. What does "faithful" chain of thought mean?
2. Why does training against a CoT monitor risk hiding intent?
3. What policy would you recommend to labs?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/cotwatch  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- REWARDGUARD](108-rewardguard.md) · [atlas index](../README.md) · [COMPUTEWATCH ->](110-computewatch.md)
