# 15 · GRANITE

```text
   prompt v1  ===  97/100  [##########]
   prompt v2  ===  91/100  [#########.]   <-- BLOCK MERGE
```

**Regression-test harness for LLM applications**

> Unit tests, but for prompts.

```text
  TRACK B GENERATIVE AI AND LLM SYSTEMS  |  LEVEL [##...]  |  ~2 MONTHS  |  BUDGET €0–10/month
```

## The mission

A prompt or model change silently breaks answers that used to be right.

## How it works

```text
+-----------------------------------------+
|  test cases                             |
+-----------------------------------------+
                    |
                    v
+-----------------------------------------+
|  run against app                        |
+-----------------------------------------+
                    |
                    v
+-----------------------------------------+
|  graders (exact, rubric, model-graded)  |
+-----------------------------------------+
                    |
                    v
+-----------------------------------------+
|  CI gate                                |
+-----------------------------------------+
```

## Kit

- Python
- pytest plugin
- SQLite results store
- GitHub Actions

**Hardware:** None

## Campaign

```text
  P1  [=====]                     m0-0.5    Test case format and runner
  P2        [=====]               m0.5-1    Graders with agreement checks against human labels
  P3              [=====]         m1-1.5    CI gate and trend dashboard
  P4                    [=====]   m1.5-2    Use it on two of your other projects
```

## Gate: done when you can show

```text
  [ ] grader agreement with humans
  [ ] run time
  [ ] regressions caught
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

None special.

## Resume line (fill with your measured numbers)

> Built an LLM regression harness used as a CI gate; model-graded checks agree with humans [N]% of the time.

**Skills it proves:** evaluation · testing · developer tools

## Defend it

1. How do you know the model grader is trustworthy?
2. What is flakiness and how do you handle it?

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/granite  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- PATCHWORK](14-patchwork.md) · [atlas index](../README.md) · [TRIPWIRE ->](16-tripwire.md)
