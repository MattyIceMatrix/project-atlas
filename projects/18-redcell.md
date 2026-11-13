# 18 · REDCELL

```text
      ____                           ____
     |REDC| -- 300 attack cases --> |AGNT|
     |ELL |  <-- responses -------- |____|
     |____|  ==> scorecard: 287 held, 13 failed -> issues filed
```

**Automated red-team harness for AI agents**

> Attack your own agent every night so nobody else does it first.

```text
  TRACK C AI SAFETY AND GOVERNANCE  |  LEVEL [###..]  |  ~3 MONTHS  |  BUDGET €10/month
```

## The mission

Agent safety is tested by hand, once, before launch.

## How it works

```text
+------------------------------+
|  attack library              |
+------------------------------+
               |
               v
+------------------------------+
|  scheduled runs              |
+------------------------------+
               |
               v
+------------------------------+
|  judge                       |
+------------------------------+
               |
               v
+------------------------------+
|  scorecard                   |
+------------------------------+
               |
               v
+------------------------------+
|  GitHub issues for failures  |
+------------------------------+
```

## Kit

- Python
- YAML attack specs
- GitHub Actions
- LLM judge with human spot checks

**Hardware:** None

## Campaign

```text
  P1  [=====]                     m0-0.8    Attack taxonomy (injection, data exfiltration, excessive agency)
  P2        [=====]               m0.8-1.5  Runner and judge with human-checked calibration
  P3              [=====]         m1.5-2.2  Nightly CI with trend tracking
  P4                    [=====]   m2.2-3    Case study on one of your agent projects
```

## Gate: done when you can show

```text
  [ ] attacks per category
  [ ] judge agreement with humans
  [ ] time to detect a regression
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Only used against systems you own or have permission to test.

## Resume line (fill with your measured numbers)

> Built a nightly agent red-team pipeline (300+ cases) that caught [N] regressions before release.

**Skills it proves:** AI security · evaluation · automation

## Defend it

1. How do you keep the attack set from leaking into training?
2. Why is the judge itself an attack surface?

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/redcell  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- LEDGER](17-ledger.md) · [atlas index](../README.md) · [CHARTER ->](19-charter.md)
