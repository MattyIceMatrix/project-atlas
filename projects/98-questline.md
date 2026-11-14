# 98 · QUESTLINE

```text
     LVL 7  [#######...]  XP 2,340
     next mission: "Fix the leaking cache" (skill: Redis, mastery 0.42)
```

**Adaptive, gamified engineering curriculum engine**

> A training game that knows what you know, and what to teach next.

```text
  TRACK M MASTERPIECE: CIVIC, SCIENCE AND HUMAN PERFORMANCE  |  LEVEL [#####]  |  ~14 MONTHS  |  BUDGET €10/month
```

## The mission

Self-learners quit when material is too easy, too hard or too dry.

## How it works

```text
+---------------------------+
|  skill graph              |
+---------------------------+
             |
             v
+---------------------------+
|  knowledge tracing model  |
+---------------------------+
             |
             v
+---------------------------+
|  mission generator        |
+---------------------------+
             |
             v
+---------------------------+
|  graded labs              |
+---------------------------+
             |
             v
+---------------------------+
|  mastery updates          |
+---------------------------+
```

## Kit

- Python
- pyBKT or deep knowledge tracing
- LLM mission writer
- VS Code extension

**Hardware:** None

## Campaign

```text
  P1  [=====]                     m0-3.5    Skill graph for one domain (e.g. DevOps)
  P2        [=====]               m3.5-7    Knowledge tracing on learner attempts
  P3              [=====]         m7-10.5   Mission generation with auto-graded labs
  P4                    [=====]   m10.5-14  Study with 20 learners: retention and learning gain
```

## Gate: done when you can show

```text
  [ ] knowledge tracing AUC
  [ ] learning gain
  [ ] 30-day retention
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Learner data private; no dark-pattern engagement tricks.

## Resume line (fill with your measured numbers)

> Built an adaptive training engine (KT AUC [N]) that raised 30-day learner retention [N]%.

**Skills it proves:** learning science · ML · product

## System map

```text
  QUESTLINE SYSTEM MAP

+------------------+    +------------------+    +------------------+
|  skill graph     |--->|  tracer          |--->|  mission writer  |
+------------------+    +------------------+    +------------------+
         |
         v
+------------------+    +------------------+
|  lab grader      |--->|  game layer      |
+------------------+    +------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   TRL 4 -> 6
  PUBLICATION TARGET     Learning at Scale or educational data mining conference
```

## Deliverables

- Engine
- Curriculum pack
- Study report
- Paper

## Standards and regulations to meet

- xAPI learning records
- WCAG

## Defend it

1. What is knowledge tracing?
2. How do you grade labs automatically and fairly?
3. Fun vs effective: how did you measure both?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/questline  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- REPROBOT](97-reprobot.md) · [atlas index](../README.md) · [HELPERHUB ->](99-helperhub.md)
