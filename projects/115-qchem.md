# 115 · QCHEM

```text
      Li--O
     /     \      ground-state energy: VQE -7.882 Ha   FCI -7.884 Ha   (chemical accuracy?)
    O-------Co
```

**Quantum chemistry for battery materials, with honest classical comparison**

> Simulate the molecule that could make better batteries.

```text
  TRACK O FRONTIER: QUANTUM COMPUTING AND QUANTUM AI  |  LEVEL [#####]  |  ~14 MONTHS  |  BUDGET €200
```

## The mission

Chemistry is the most credible early application of quantum computers; the work needs careful comparison to classical methods.

## How it works

```text
+-------------------------------------+
|  molecule selection                 |
+-------------------------------------+
                  |
                  v
+-------------------------------------+
|  Hamiltonian construction           |
+-------------------------------------+
                  |
                  v
+-------------------------------------+
|  VQE/QPE on simulators              |
+-------------------------------------+
                  |
                  v
+-------------------------------------+
|  classical methods (CCSD(T), DMRG)  |
+-------------------------------------+
                  |
                  v
+-------------------------------------+
|  resource estimates                 |
+-------------------------------------+
```

## Kit

- PennyLane
- PySCF
- OpenFermion
- Qualtran or Azure resource estimator

**Hardware:** GPU simulation

## Campaign

```text
  P1  [=====]                     m0-3.5    Small molecules to chemical accuracy in simulation
  P2        [=====]               m3.5-7    Battery-relevant fragments and active-space selection
  P3              [=====]         m7-10.5   Classical comparisons
  P4                    [=====]   m10.5-14  Fault-tolerant resource estimates for full-size problems
```

## Gate: done when you can show

```text
  [ ] energy error vs classical reference
  [ ] qubit and gate counts
  [ ] estimated runtime on future hardware
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

None special.

## Resume line (fill with your measured numbers)

> Simulated battery-material fragments to chemical accuracy and produced fault-tolerant resource estimates.

**Skills it proves:** quantum chemistry · algorithms · resource estimation

## System map

```text
  QCHEM SYSTEM MAP

+----------------------+    +----------------------+    +----------------------+
|  molecule pipeline   |--->|  Hamiltonians        |--->|  quantum solvers     |
+----------------------+    +----------------------+    +----------------------+
           |
           v
+----------------------+    +----------------------+
|  classical solvers   |--->|  resource estimator  |
+----------------------+    +----------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   Research
  PUBLICATION TARGET     Quantum chemistry or quantum computing journal
```

## Deliverables

- Code
- Results
- Resource estimates
- Paper

## Standards and regulations to meet

- Reproducibility checklist

## Who sees this

Where this work gets in front of the people who lead the field (see the
[visibility playbook](../docs/visibility-playbook.md) for how to use each one):

```text
  >> QHack chemistry challenges
  >> PennyLane demos
  >> quantum chemistry research groups
```

## Defend it

1. What is chemical accuracy?
2. Why active spaces?
3. When would a quantum computer beat DMRG here?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/qchem  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- QMITIGATE](114-qmitigate.md) · [atlas index](../README.md) · [QCOMPILE ->](116-qcompile.md)
