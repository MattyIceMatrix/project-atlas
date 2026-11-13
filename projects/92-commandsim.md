# 92 · COMMANDSIM

```text
    [ IC trainee ] <--radio--> [AI: fire chief] [AI: THW lead] [AI: mayor] [AI: press]
              \__ scenario clock: T+02:40, river +40 cm, bridge closed __/
```

**Incident command training simulator with AI role players**

> Run a flood response in a tabletop sim where every radio call is an AI playing a role.

```text
  TRACK M MASTERPIECE: CIVIC, SCIENCE AND HUMAN PERFORMANCE  |  LEVEL [#####]  |  ~14 MONTHS  |  BUDGET €50/month
```

## The mission

Incident command training needs many role players and realistic pressure; exercises are rare.

## How it works

```text
+-------------------------------------------+
|  scenario engine                          |
+-------------------------------------------+
                     |
                     v
+-------------------------------------------+
|  AI role players with doctrine knowledge  |
+-------------------------------------------+
                     |
                     v
+-------------------------------------------+
|  trainee decisions                        |
+-------------------------------------------+
                     |
                     v
+-------------------------------------------+
|  after-action scoring                     |
+-------------------------------------------+
```

## Kit

- Python
- LLM with role prompts + RAG over doctrine
- speech I/O
- web UI

**Hardware:** Laptop + headset

## Campaign

```text
  P1  [=====]                     m0-3.5    Scenario model grounded in public flood exercise material
  P2        [=====]               m3.5-7    Role players constrained by doctrine (ICS/THW structures)
  P3              [=====]         m7-10.5   Scoring rubric with real instructors
  P4                    [=====]   m10.5-14  Pilot with a volunteer unit or university emergency management course
```

## Gate: done when you can show

```text
  [ ] instructor-rated realism
  [ ] learning gain pre/post
  [ ] role-player consistency
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Training aid, not certification; instructors own assessment.

## Resume line (fill with your measured numbers)

> Built an AI-driven incident command simulator rated [N]/5 for realism by instructors in a pilot.

**Skills it proves:** simulation · LLM agents · training design

## System map

```text
  COMMANDSIM SYSTEM MAP

+-------------------+    +-------------------+    +-------------------+
|  scenario engine  |--->|  role agents      |--->|  doctrine RAG     |
+-------------------+    +-------------------+    +-------------------+
         |
         v
+-------------------+    +-------------------+
|  voice layer      |--->|  AAR scorer       |
+-------------------+    +-------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   TRL 4 -> 6
  PUBLICATION TARGET     ISCRAM or simulation and gaming journal
```

## Deliverables

- Simulator
- Scenario pack
- Pilot study
- Instructor guide

## Standards and regulations to meet

- ICS/NIMS doctrine
- German FwDV 100 (reference)

## Defend it

1. How do you keep AI role players consistent with doctrine?
2. How do you measure learning, not just enjoyment?
3. What should never be automated in command training?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/commandsim  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- ATHLETEOS](91-athleteos.md) · [atlas index](../README.md) · [VERWALTUNG ->](93-verwaltung.md)
