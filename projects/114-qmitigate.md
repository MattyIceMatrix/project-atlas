# 114 · QMITIGATE

```text
    noisy result: 0.62   --[ zero-noise extrapolation ]-->   mitigated: 0.91   (ideal 0.93)
```

**Error mitigation contributions and real-hardware benchmarks**

> Squeeze correct answers out of noisy quantum hardware, in a tool thousands use.

```text
  TRACK O FRONTIER: QUANTUM COMPUTING AND QUANTUM AI  |  LEVEL [#####]  |  ~12 MONTHS  |  BUDGET €100
```

## The mission

Today's quantum computers are noisy; error mitigation is how practical results get extracted now.

## How it works

```text
+------------------------------------+
|  learn Mitiq                       |
+------------------------------------+
                  |
                  v
+------------------------------------+
|  implement or improve a technique  |
+------------------------------------+
                  |
                  v
+------------------------------------+
|  benchmark on simulators and QPUs  |
+------------------------------------+
                  |
                  v
+------------------------------------+
|  merge upstream                    |
+------------------------------------+
```

## Kit

- Mitiq
- Qiskit/Cirq/PennyLane
- Metriq

**Hardware:** Simulators + cloud QPU free tiers

## Campaign

```text
  P1  [=====]                     m0-3      Good-first-issue contributions to Mitiq
  P2        [=====]               m3-6      Implement a technique variant with tests
  P3              [=====]         m6-9      Hardware benchmarks submitted to Metriq
  P4                    [=====]   m9-12     Microgrant application to extend the work
```

## Gate: done when you can show

```text
  [ ] error reduction factor
  [ ] sampling overhead
  [ ] PRs merged
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

None special.

## Resume line (fill with your measured numbers)

> Contributed error-mitigation features to Mitiq and published hardware benchmarks showing [N]x error reduction.

**Skills it proves:** quantum software · open source · benchmarking

## System map

```text
  QMITIGATE SYSTEM MAP

+----------------------------+    +----------------------------+    +----------------------------+
|  technique implementation  |--->|  tests                     |--->|  benchmark runs            |
+----------------------------+    +----------------------------+    +----------------------------+
              |
              v
+----------------------------+    +----------------------------+
|  Metriq submission         |--->|  docs                      |
+----------------------------+    +----------------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   Open-source tooling
  PUBLICATION TARGET     Unitary Foundation community, IEEE QCE
```

## Deliverables

- Merged PRs
- Benchmarks
- Tutorial
- Grant proposal

## Standards and regulations to meet

- Project contribution guidelines

## Who sees this

Where this work gets in front of the people who lead the field (see the
[visibility playbook](../docs/visibility-playbook.md) for how to use each one):

```text
  >> Unitary Foundation microgrants (rolling
  >> about $4
  >> 000)
  >> unitaryHACK (annual
  >> June)
  >> Mitiq maintainers
```

## Defend it

1. What does zero-noise extrapolation assume?
2. Why does mitigation cost extra shots?
3. How is mitigation different from correction?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/qmitigate  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- QROUTE](113-qroute.md) · [atlas index](../README.md) · [QCHEM ->](115-qchem.md)
