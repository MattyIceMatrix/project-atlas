# 99 · HELPERHUB

```text
    helpers [o][o][o][o][o][o]  -->  [ match ]  -->  task: "shovel mud, Dernau, 4 people, boots"
                                         |  safety briefing  |  shift limits
```

**Coordination platform for spontaneous disaster volunteers**

> Thousands of helpers showed up in the Ahr. This puts them where they're needed.

```text
  TRACK M MASTERPIECE: CIVIC, SCIENCE AND HUMAN PERFORMANCE  |  LEVEL [#####]  |  ~14 MONTHS  |  BUDGET €20/month
```

## The mission

After floods, huge numbers of volunteers arrive; matching them to safe, useful tasks is chaos.

## How it works

```text
+----------------------------------+
|  volunteer registration          |
+----------------------------------+
                 |
                 v
+----------------------------------+
|  skills and safety checks        |
+----------------------------------+
                 |
                 v
+----------------------------------+
|  task requests from authorities  |
+----------------------------------+
                 |
                 v
+----------------------------------+
|  matching                        |
+----------------------------------+
                 |
                 v
+----------------------------------+
|  check-in/out                    |
+----------------------------------+
```

## Kit

- Next.js
- Postgres
- OR-Tools matching
- PWA offline mode
- MESHLIFE/CREDMESH integration

**Hardware:** None

## Campaign

```text
  P1  [=====]                     m0-3.5    Interviews with organisations that coordinated volunteers in 2021
  P2        [=====]               m3.5-7    Registration, tasks, matching with safety rules
  P3              [=====]         m7-10.5   Offline-capable check-in/out and shift limits
  P4                    [=====]   m10.5-14  Exercise with a volunteer organisation
```

## Gate: done when you can show

```text
  [ ] match time
  [ ] tasks filled
  [ ] safety rule violations (target 0)
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Authorities and organisations stay in charge; minimal personal data.

## Resume line (fill with your measured numbers)

> Built a spontaneous-volunteer coordination platform filling [N]% of tasks in an exercise with [N] volunteers.

**Skills it proves:** civic tech · optimisation · offline-first apps

## System map

```text
  HELPERHUB SYSTEM MAP

+----------------+    +----------------+    +----------------+
|  registration  |--->|  task intake   |--->|  matcher       |
+----------------+    +----------------+    +----------------+
        |
        v
+----------------+    +----------------+
|  check-in      |--->|  reporting     |
+----------------+    +----------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   TRL 4 -> 6
  PUBLICATION TARGET     ISCRAM
```

## Deliverables

- Platform
- Exercise report
- Organisation playbook
- Paper

## Standards and regulations to meet

- GDPR
- CAP for task alerts
- BITV 2.0

## Defend it

1. What went wrong with volunteer coordination in 2021?
2. Why are safety rules hard constraints in the matcher?
3. Who owns the data after the disaster?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/helperhub  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- QUESTLINE](98-questline.md) · [atlas index](../README.md) · [CITYTWIN ->](100-citytwin.md)
