# 93 · VERWALTUNG

```text
    "I moved to Bolanden and have a car"
       --> Anmeldung (14 days) --> Kfz-Ummeldung --> Rundfunkbeitrag
              [source]               [source]          [source]
```

**Citizen navigator for German administrative procedures**

> Which form, which office, which deadline, with sources for every step.

```text
  TRACK M MASTERPIECE: CIVIC, SCIENCE AND HUMAN PERFORMANCE  |  LEVEL [#####]  |  ~14 MONTHS  |  BUDGET €20/month
```

## The mission

Navigating German bureaucracy is hard for everyone and harder for newcomers.

## How it works

```text
+-------------------------------------+
|  official procedure data            |
+-------------------------------------+
                  |
                  v
+-------------------------------------+
|  knowledge graph                    |
+-------------------------------------+
                  |
                  v
+-------------------------------------+
|  question answering with citations  |
+-------------------------------------+
                  |
                  v
+-------------------------------------+
|  multilingual UI                    |
+-------------------------------------+
```

## Kit

- Python
- Neo4j or SQLite graph
- RAG
- open procedure catalogues (FIM/Leika)
- Next.js

**Hardware:** None

## Campaign

```text
  P1  [=====]                     m0-3.5    Ingest official procedure catalogues
  P2        [=====]               m3.5-7    Graph of procedures, triggers, deadlines
  P3              [=====]         m7-10.5   Grounded Q&A with citations; refusal when unsure
  P4                    [=====]   m10.5-14  Usability study with newcomers in 3 languages
```

## Gate: done when you can show

```text
  [ ] answer correctness audited by experts
  [ ] citation coverage
  [ ] task completion in user tests
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Information, not legal advice; always links to the official source.

## Resume line (fill with your measured numbers)

> Built a cited, multilingual navigator over official German procedures with [N]% expert-audited correctness.

**Skills it proves:** knowledge graphs · RAG · civic tech

## System map

```text
  VERWALTUNG SYSTEM MAP

+--------------------+    +--------------------+    +--------------------+
|  catalogue ingest  |--->|  procedure graph   |--->|  QA engine         |
+--------------------+    +--------------------+    +--------------------+
          |
          v
+--------------------+    +--------------------+
|  citation checker  |--->|  UI                |
+--------------------+    +--------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   TRL 4 -> 6
  PUBLICATION TARGET     Civic tech / e-government conference
```

## Deliverables

- Platform
- Audit report
- User study
- Open data contributions

## Standards and regulations to meet

- OZG / FIM catalogues (reference)
- BITV 2.0 accessibility
- GDPR

## Defend it

1. Why a graph and not just documents?
2. How do you keep it current?
3. When must the tool say "ask the office"?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/verwaltung  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- COMMANDSIM](92-commandsim.md) · [atlas index](../README.md) · [SKYEDGE ->](94-skyedge.md)
