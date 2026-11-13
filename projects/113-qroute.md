# 113 · QROUTE

```text
    boats: B1 B2 B3     sites: S1..S12     QAOA p=3: cost 418    classical MILP: cost 401 (optimal)
         ~~~~~~~~~~~~~~ Ahr valley graph from the LANTERN map pack ~~~~~~~~~~~~~~
```

**Quantum optimisation for disaster logistics, against strong classical solvers**

> Route the rescue boats with QAOA, then see if Gurobi-class solvers still win.

```text
  TRACK O FRONTIER: QUANTUM COMPUTING AND QUANTUM AI  |  LEVEL [#####]  |  ~12 MONTHS  |  BUDGET €100
```

## The mission

Disaster logistics are hard optimisation problems; quantum optimisation is promising but often oversold.

## How it works

```text
+---------------------------------+
|  LANTERN map pack               |
+---------------------------------+
                |
                v
+---------------------------------+
|  routing problem as QUBO        |
+---------------------------------+
                |
                v
+---------------------------------+
|  QAOA / annealing               |
+---------------------------------+
                |
                v
+---------------------------------+
|  classical MILP and heuristics  |
+---------------------------------+
                |
                v
+---------------------------------+
|  compare                        |
+---------------------------------+
```

## Kit

- Qiskit or PennyLane
- D-Wave Ocean (if access)
- OR-Tools
- HiGHS

**Hardware:** Simulators + free-tier QPU access

## Campaign

```text
  P1  [=====]                     m0-3      Formulate realistic instances from LANTERN data
  P2        [=====]               m3-6      Quantum approaches on simulators and hardware
  P3              [=====]         m6-9      Strong classical baselines
  P4                    [=====]   m9-12     Scaling analysis and resource estimates for future hardware
```

## Gate: done when you can show

```text
  [ ] solution quality gap
  [ ] time to solution
  [ ] problem size reachable
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Advisory research; humans plan real operations.

## Resume line (fill with your measured numbers)

> Compared QAOA/annealing with MILP on real flood-logistics instances; published scaling and resource estimates.

**Skills it proves:** quantum optimisation · operations research

## System map

```text
  QROUTE SYSTEM MAP

+---------------------+    +---------------------+    +---------------------+
|  instance builder   |--->|  QUBO encoder       |--->|  quantum solvers    |
+---------------------+    +---------------------+    +---------------------+
          |
          v
+---------------------+    +---------------------+
|  classical solvers  |--->|  analysis           |
+---------------------+    +---------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   Research
  PUBLICATION TARGET     IEEE QCE or operations research workshop
```

## Deliverables

- Instance library
- Solver comparison
- Paper

## Standards and regulations to meet

- Open benchmark instances

## Who sees this

Where this work gets in front of the people who lead the field (see the
[visibility playbook](../docs/visibility-playbook.md) for how to use each one):

```text
  >> iQuHACK (MIT
  >> annual)
  >> QHack
  >> quantum industry partner challenges
```

## Defend it

1. How do constraints become a QUBO, and what does it cost?
2. Why is classical MILP such a strong baseline?
3. At what size might quantum matter, and why?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/qroute  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- QMLTRUTH](112-qmltruth.md) · [atlas index](../README.md) · [QMITIGATE ->](114-qmitigate.md)
