# 105 · WEAKJUDGE

```text
    [ strong A ] <--debate--> [ strong B ]
               \             /
                [ weak judge ]  accuracy: 62% alone -> 81% with debate
```

**Scalable oversight with debate and weak-to-strong supervision**

> Can a weaker judge reliably supervise a stronger model? Measure it.

```text
  TRACK N FRONTIER: SUPERINTELLIGENCE ALIGNMENT AND SAFETY  |  LEVEL [#####]  |  ~12 MONTHS  |  BUDGET €400
```

## The mission

Humans will supervise systems smarter than them. We need methods where weak overseers still get the truth.

## How it works

```text
+---------------------------------------+
|  hard QA tasks with ground truth      |
+---------------------------------------+
                   |
                   v
+---------------------------------------+
|  weak judges (small models / humans)  |
+---------------------------------------+
                   |
                   v
+---------------------------------------+
|  debate and consultancy protocols     |
+---------------------------------------+
                   |
                   v
+---------------------------------------+
|  accuracy                             |
+---------------------------------------+
```

## Kit

- Python
- Inspect AI
- open and API models
- crowd study tooling

**Hardware:** API credits

## Campaign

```text
  P1  [=====]                     m0-3      Replicate a debate result on a reading-comprehension benchmark
  P2        [=====]               m3-6      New domain where you have expertise (security incident analysis)
  P3              [=====]         m6-9      Human judge study with ethics approval or informed consent
  P4                    [=====]   m9-12     Analysis of when debate helps and when it fails
```

## Gate: done when you can show

```text
  [ ] judge accuracy by protocol
  [ ] robustness to persuasive-but-wrong debaters
  [ ] cost per judgement
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Informed consent and fair pay for human judges.

## Resume line (fill with your measured numbers)

> Showed debate raised weak-judge accuracy from [N]% to [N]% in a new security-analysis domain.

**Skills it proves:** scalable oversight · human studies · experiment design

## System map

```text
  WEAKJUDGE SYSTEM MAP

+-------------------+    +-------------------+    +-------------------+
|  task bank        |--->|  debater agents   |--->|  judge interface  |
+-------------------+    +-------------------+    +-------------------+
         |
         v
+-------------------+    +-------------------+
|  study runner     |--->|  analysis         |
+-------------------+    +-------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   Research
  PUBLICATION TARGET     NeurIPS/ICML alignment workshops
```

## Deliverables

- Task bank
- Protocol code
- Human study data
- Paper

## Standards and regulations to meet

- Human-subjects research ethics

## Who sees this

Where this work gets in front of the people who lead the field (see the
[visibility playbook](../docs/visibility-playbook.md) for how to use each one):

```text
  >> Anthropic Fellows (scalable oversight area)
  >> MATS
  >> Apart sprints
```

## Defend it

1. Why might debate favour persuasion over truth?
2. What is weak-to-strong generalisation?
3. How does your domain change the picture?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/weakjudge  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- MODELORGS](104-modelorgs.md) · [atlas index](../README.md) · [EVALSMITH ->](106-evalsmith.md)
