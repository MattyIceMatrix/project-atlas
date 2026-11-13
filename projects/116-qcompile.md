# 116 · QCOMPILE

```text
    before: --H--CX--H--CX--T--T--     depth 6
    after:  --CX--S--                  depth 2   (ZX-calculus rewrite)
```

**Quantum circuit optimisation passes**

> Fewer gates, fewer errors. Write the compiler pass that does it.

```text
  TRACK O FRONTIER: QUANTUM COMPUTING AND QUANTUM AI  |  LEVEL [#####]  |  ~12 MONTHS  |  BUDGET €0
```

## The mission

Gate count and depth decide whether a circuit survives the noise; compilers are where gains hide.

## How it works

```text
+--------------------------------------------------------+
|  benchmark circuits                                    |
+--------------------------------------------------------+
                            |
                            v
+--------------------------------------------------------+
|  optimisation passes (ZX-calculus, peephole, routing)  |
+--------------------------------------------------------+
                            |
                            v
+--------------------------------------------------------+
|  equivalence checking                                  |
+--------------------------------------------------------+
                            |
                            v
+--------------------------------------------------------+
|  upstream                                              |
+--------------------------------------------------------+
```

## Kit

- PyZX
- Qiskit transpiler
- Unitary Compiler Collection (UCC)
- Python or Rust

**Hardware:** Laptop

## Campaign

```text
  P1  [=====]                     m0-3      Benchmark suite and existing compiler baselines
  P2        [=====]               m3-6      New pass with formal equivalence checks
  P3              [=====]         m6-9      Hardware-aware routing improvements
  P4                    [=====]   m9-12     Upstream contribution and write-up
```

## Gate: done when you can show

```text
  [ ] two-qubit gate reduction
  [ ] depth reduction
  [ ] compile time
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

None special.

## Resume line (fill with your measured numbers)

> Wrote a circuit optimisation pass cutting two-qubit gates [N]% on standard benchmarks; merged upstream.

**Skills it proves:** compilers · quantum software · formal methods

## System map

```text
  QCOMPILE SYSTEM MAP

+-----------------------+    +-----------------------+    +-----------------------+
|  benchmark set        |--->|  pass                 |--->|  equivalence checker  |
+-----------------------+    +-----------------------+    +-----------------------+
           |
           v
+-----------------------+    +-----------------------+
|  router               |--->|  upstream PR          |
+-----------------------+    +-----------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   Open-source tooling
  PUBLICATION TARGET     IEEE QCE, compiler workshops
```

## Deliverables

- Pass
- Benchmarks
- PR
- Paper

## Standards and regulations to meet

- OpenQASM 3

## Who sees this

Where this work gets in front of the people who lead the field (see the
[visibility playbook](../docs/visibility-playbook.md) for how to use each one):

```text
  >> Unitary Foundation (UCC
  >> PyZX ecosystem)
  >> unitaryHACK
  >> Qiskit community
```

## Defend it

1. Why are two-qubit gates the expensive ones?
2. How do you prove the optimised circuit is equivalent?
3. What does qubit routing solve?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/qcompile  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- QCHEM](115-qchem.md) · [atlas index](../README.md) · [QKDNET ->](117-qkdnet.md)
