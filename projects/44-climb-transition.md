# 44 · CLIMB-TRANSITION

```text
    ETS -180d  [SkillBridge apply]   ======>
    ETS  -90d  [VA claim]            ====>
    ETS    0   [GI Bill / job start] ==>
```

**Veteran transition dashboard**

> Benefits, deadlines, skills and jobs, in one plan.

```text
  TRACK G PEOPLE, SPORT AND COMMUNITY  |  LEVEL [##...]  |  ~3 MONTHS  |  BUDGET €0
```

## The mission

Transitioning service members juggle dozens of deadlines and programs.

## How it works

```text
+--------------------------------------+
|  user timeline                       |
+--------------------------------------+
                   |
                   v
+--------------------------------------+
|  rules for public program deadlines  |
+--------------------------------------+
                   |
                   v
+--------------------------------------+
|  checklist + reminders               |
+--------------------------------------+
                   |
                   v
+--------------------------------------+
|  job matches                         |
+--------------------------------------+
```

## Kit

- Next.js
- Postgres
- public program data
- calendar export

**Hardware:** None

## Campaign

```text
  P1  [=====]                     m0-0.8    Public program rules with sources and dates checked
  P2        [=====]               m0.8-1.5  Timeline engine with tests
  P3              [=====]         m1.5-2.2  Reminders and calendar export
  P4                    [=====]   m2.2-3    Usability test with veterans
```

## Gate: done when you can show

```text
  [ ] deadlines covered
  [ ] user task completion
  [ ] rule accuracy audits
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Information tool; links to official sources; no personal data sold or shared.

## Resume line (fill with your measured numbers)

> Built a transition planner covering [N] program deadlines, tested with [N] veterans.

**Skills it proves:** full stack · rules engines · UX

## Masterpiece upgrade path

```text
   LEVEL [##...]  ====================>  LEVEL [#####]
```

Partner with transition programmes, add verified credentials and outcome tracking.

**Grows into:** [CREDMESH](80-credmesh.md) · **Publication target:** Veteran services conference

## Defend it

1. How do you keep program rules current?
2. What personal data do you avoid collecting, and why?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/climb-transition  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- POOLSHARK](43-poolshark.md) · [atlas index](../README.md) · [RECEIPTLENS ->](45-receiptlens.md)
