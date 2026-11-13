# 118 · QSIMGPU

```text
    |psi> = 2^32 amplitudes  -->  [ CUDA kernels ]  -->  1.8 s/circuit   (vs 41 s CPU)
```

**GPU-accelerated quantum circuit simulator**

> Simulate 30+ qubits fast, with code you wrote.

```text
  TRACK O FRONTIER: QUANTUM COMPUTING AND QUANTUM AI  |  LEVEL [#####]  |  ~14 MONTHS  |  BUDGET €200
```

## The mission

Classical simulation sets the bar quantum hardware must beat and powers all algorithm research.

## How it works

```text
+--------------------------------------+
|  state-vector engine                 |
+--------------------------------------+
                   |
                   v
+--------------------------------------+
|  gate kernels (CUDA)                 |
+--------------------------------------+
                   |
                   v
+--------------------------------------+
|  tensor-network mode                 |
+--------------------------------------+
                   |
                   v
+--------------------------------------+
|  benchmarks vs cuQuantum/Qiskit Aer  |
+--------------------------------------+
```

## Kit

- Rust or C++
- CUDA
- cuQuantum for comparison
- Python bindings

**Hardware:** One GPU

## Campaign

```text
  P1  [=====]                     m0-3.5    Correct CPU state-vector simulator with tests
  P2        [=====]               m3.5-7    CUDA gate kernels and memory layout
  P3              [=====]         m7-10.5   Tensor-network mode for shallow wide circuits
  P4                    [=====]   m10.5-14  Benchmarks and Python package
```

## Gate: done when you can show

```text
  [ ] time per gate at 30 qubits
  [ ] max qubits per GPU
  [ ] accuracy vs reference
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

None special.

## Resume line (fill with your measured numbers)

> Built a CUDA quantum simulator reaching [N]% of cuQuantum throughput at 30+ qubits.

**Skills it proves:** GPU programming · numerical computing · quantum software

## System map

```text
  QSIMGPU SYSTEM MAP

+----------------+    +----------------+    +----------------+
|  state engine  |--->|  CUDA kernels  |--->|  tensor mode   |
+----------------+    +----------------+    +----------------+
        |
        v
+----------------+    +----------------+
|  bindings      |--->|  benchmarks    |
+----------------+    +----------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   Engineering artefact
  PUBLICATION TARGET     Engineering blog + talk; IEEE QCE
```

## Deliverables

- Simulator
- Python package
- Benchmarks

## Standards and regulations to meet

- OpenQASM 3 input

## Who sees this

Where this work gets in front of the people who lead the field (see the
[visibility playbook](../docs/visibility-playbook.md) for how to use each one):

```text
  >> NVIDIA quantum developer community
  >> iQuHACK sponsors
  >> quantum software conferences
```

## Defend it

1. Why does memory double with each qubit?
2. When are tensor networks better than state vectors?
3. How do you test a simulator is correct?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/qsimgpu  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- QKDNET](117-qkdnet.md) · [atlas index](../README.md) · [QAGENT ->](119-qagent.md)
