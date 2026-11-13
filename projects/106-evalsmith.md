# 106 · EVALSMITH

```text
    your eval  -->  [ Inspect Evals register ]  -->  run by AISI, METR, labs, researchers
       | tests, docs, baseline results, validity checks |
```

**New safety evaluations contributed to Inspect Evals**

> Build the tests governments and labs actually run.

```text
  TRACK N FRONTIER: SUPERINTELLIGENCE ALIGNMENT AND SAFETY  |  LEVEL [#####]  |  ~12 MONTHS  |  BUDGET €300
```

## The mission

Safety decisions depend on high-quality, reproducible evals, and there are too few good ones.

## How it works

```text
+-----------------------------------------------------------------------------------------------+
|  pick an under-measured property (sycophancy, situational awareness, honesty under pressure)  |
+-----------------------------------------------------------------------------------------------+
                                               |
                                               v
+-----------------------------------------------------------------------------------------------+
|  design eval                                                                                  |
+-----------------------------------------------------------------------------------------------+
                                               |
                                               v
+-----------------------------------------------------------------------------------------------+
|  validity tests                                                                               |
+-----------------------------------------------------------------------------------------------+
                                               |
                                               v
+-----------------------------------------------------------------------------------------------+
|  contribute                                                                                   |
+-----------------------------------------------------------------------------------------------+
```

## Kit

- Inspect AI
- Python
- pytest
- multiple model providers

**Hardware:** API credits

## Campaign

```text
  P1  [=====]                     m0-3      Contribute a small fix and one existing benchmark port to learn the standards
  P2        [=====]               m3-6      Design an original eval with a validity argument
  P3              [=====]         m6-9      Baselines across 5+ models, with uncertainty
  P4                    [=====]   m9-12     Upstream contribution and a short paper
```

## Gate: done when you can show

```text
  [ ] evals merged upstream
  [ ] inter-rater agreement for graders
  [ ] results reproducibility
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

No hazardous-capability content (bio, chem, cyber uplift); responsible disclosure of surprises.

## Resume line (fill with your measured numbers)

> Contributed [N] evaluations to the UK AISI's Inspect Evals, including an original <property> benchmark.

**Skills it proves:** evaluation science · open source · measurement

## System map

```text
  EVALSMITH SYSTEM MAP

+------------------+    +------------------+    +------------------+
|  task design     |--->|  dataset         |--->|  scorer          |
+------------------+    +------------------+    +------------------+
         |
         v
+------------------+    +------------------+
|  validity tests  |--->|  upstream PR     |
+------------------+    +------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   Research tooling
  PUBLICATION TARGET     Evals workshops; Inspect Evals register
```

## Deliverables

- Merged evals
- Baseline results
- Validity write-up
- Paper

## Standards and regulations to meet

- Inspect Evals contribution guidelines
- Datasheets for datasets

## Who sees this

Where this work gets in front of the people who lead the field (see the
[visibility playbook](../docs/visibility-playbook.md) for how to use each one):

```text
  >> UK AI Security Institute (Inspect maintainers)
  >> METR (builds on Inspect)
  >> Arcadia Impact
  >> Vector Institute
```

## Defend it

1. What makes an eval valid, not just reliable?
2. How do you stop the eval leaking into training data?
3. Why is the grader the weakest link?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/evalsmith  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- WEAKJUDGE](105-weakjudge.md) · [atlas index](../README.md) · [TRUTHPROBE ->](107-truthprobe.md)
