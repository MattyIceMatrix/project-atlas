# 97 · REPROBOT

```text
    paper.pdf --> [ plan ] --> [ code ] --> [ run ] --> [ compare to Table 2 ]
                                                    reproduced: 3/4 claims
```

**Research agent that reproduces ML papers, with verification**

> Paper in, working code and an honest reproduction report out.

```text
  TRACK M MASTERPIECE: CIVIC, SCIENCE AND HUMAN PERFORMANCE  |  LEVEL [#####]  |  ~16 MONTHS  |  BUDGET €400
```

## The mission

Many ML results are hard to reproduce; checking them by hand takes weeks.

## How it works

```text
+------------------------------+
|  paper parsing               |
+------------------------------+
               |
               v
+------------------------------+
|  experiment plan             |
+------------------------------+
               |
               v
+------------------------------+
|  code generation in sandbox  |
+------------------------------+
               |
               v
+------------------------------+
|  runs                        |
+------------------------------+
               |
               v
+------------------------------+
|  claim-by-claim comparison   |
+------------------------------+
```

## Kit

- Python
- agent runtime (AGENTGRID)
- sandboxed containers
- PyTorch

**Hardware:** Cloud GPUs (budgeted)

## Campaign

```text
  P1  [=====]                     m0-4      Benchmark of 20 small papers with known reproduction status
  P2        [=====]               m4-8      Planning and coding agent in a sandbox
  P3              [=====]         m8-12     Claim extraction and statistical comparison
  P4                    [=====]   m12-16    Report quality judged by human researchers
```

## Gate: done when you can show

```text
  [ ] claims correctly reproduced or refuted
  [ ] cost per paper
  [ ] human agreement on reports
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Credit original authors; report failures politely and privately first.

## Resume line (fill with your measured numbers)

> Built a paper-reproduction agent that correctly assessed [N]% of claims across [N] papers at €[N]/paper.

**Skills it proves:** AI agents · research methods · sandboxing

## System map

```text
  REPROBOT SYSTEM MAP

+------------------+    +------------------+    +------------------+
|  paper parser    |--->|  planner         |--->|  coder           |
+------------------+    +------------------+    +------------------+
         |
         v
+------------------+    +------------------+
|  sandbox runner  |--->|  claim checker   |
+------------------+    +------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   TRL 3 -> 4
  PUBLICATION TARGET     ML reproducibility workshop or ReScience
```

## Deliverables

- Agent
- Benchmark
- Reports
- Paper

## Standards and regulations to meet

- ML reproducibility checklist (NeurIPS)

## Defend it

1. How do you know a failed reproduction isn't your bug?
2. Why a sandbox, and what can still go wrong?
3. What is a claim, operationally?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/reprobot  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- WAYFINDER](96-wayfinder.md) · [atlas index](../README.md) · [QUESTLINE ->](98-questline.md)
