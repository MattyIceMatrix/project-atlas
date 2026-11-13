# 120 · QREADY

```text
    problem               logical qubits   runtime       when (hardware roadmaps)
    battery chemistry           ~2,000        days          later
    flood logistics             ~8,000        weeks         unclear
    RSA-2048 (for PQC urgency)  ~thousands    hours-days    plan migration now
```

**When will quantum matter? Resource estimates for real national problems**

> The report every minister asks for, done with real numbers.

```text
  TRACK O FRONTIER: QUANTUM COMPUTING AND QUANTUM AI  |  LEVEL [#####]  |  ~12 MONTHS  |  BUDGET €0
```

## The mission

Decision-makers hear wildly different quantum timelines; they need grounded resource estimates for their actual problems.

## How it works

```text
+--------------------------------------+
|  pick national problems              |
+--------------------------------------+
                   |
                   v
+--------------------------------------+
|  algorithms                          |
+--------------------------------------+
                   |
                   v
+--------------------------------------+
|  fault-tolerant resource estimation  |
+--------------------------------------+
                   |
                   v
+--------------------------------------+
|  map to vendor roadmaps              |
+--------------------------------------+
                   |
                   v
+--------------------------------------+
|  policy brief                        |
+--------------------------------------+
```

## Kit

- Azure Quantum Resource Estimator or Qualtran
- Python
- public vendor roadmaps

**Hardware:** Laptop

## Campaign

```text
  P1  [=====]                     m0-3      Problem selection with domain experts
  P2        [=====]               m3-6      Algorithm choice and resource estimation
  P3              [=====]         m6-9      Sensitivity analysis on error rates and architectures
  P4                    [=====]   m9-12     Policy brief and public talk
```

## Gate: done when you can show

```text
  [ ] estimates with sensitivity ranges
  [ ] problems covered
  [ ] expert review feedback
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Avoid hype; publish uncertainty prominently.

## Resume line (fill with your measured numbers)

> Produced fault-tolerant resource estimates for [N] national-priority problems and briefed decision-makers.

**Skills it proves:** quantum algorithms · policy communication · analysis

## System map

```text
  QREADY SYSTEM MAP

+------------------------+    +------------------------+    +------------------------+
|  problem catalogue     |--->|  algorithms            |--->|  estimator runs        |
+------------------------+    +------------------------+    +------------------------+
            |
            v
+------------------------+    +------------------------+
|  sensitivity analysis  |--->|  policy brief          |
+------------------------+    +------------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   Analysis
  PUBLICATION TARGET     Policy think tanks, IEEE QCE, national quantum strategy consultations
```

## Deliverables

- Estimates repo
- Policy brief
- Talk

## Standards and regulations to meet

- NIST PQC standards (for migration urgency)

## Who sees this

Where this work gets in front of the people who lead the field (see the
[visibility playbook](../docs/visibility-playbook.md) for how to use each one):

```text
  >> National quantum initiatives
  >> quantum policy forums
  >> NATIONSTACK (project 121)
```

## Defend it

1. Why are logical qubits different from physical qubits?
2. What assumptions dominate your estimates?
3. What should a government do today regardless?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/qready  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- QAGENT](119-qagent.md) · [atlas index](../README.md) · [NATIONSTACK ->](121-nationstack.md)
