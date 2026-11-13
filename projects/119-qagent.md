# 119 · QAGENT

```text
    "prepare a GHZ state on 5 qubits"  -->  [ LLM agent ]  -->  circuit
                                                |
                              [ equivalence checker ] --> VERIFIED / rejected, retry
```

**AI agent that writes and verifies quantum programs**

> Where frontier AI meets quantum: an agent that can't ship a wrong circuit.

```text
  TRACK O FRONTIER: QUANTUM COMPUTING AND QUANTUM AI  |  LEVEL [#####]  |  ~12 MONTHS  |  BUDGET €300
```

## The mission

Quantum programming is hard and errors are invisible; AI assistance only helps if every output is verified.

## How it works

```text
+----------------------------------------+
|  task spec                             |
+----------------------------------------+
                    |
                    v
+----------------------------------------+
|  LLM generates circuit                 |
+----------------------------------------+
                    |
                    v
+----------------------------------------+
|  simulator + formal equivalence check  |
+----------------------------------------+
                    |
                    v
+----------------------------------------+
|  feedback loop                         |
+----------------------------------------+
                    |
                    v
+----------------------------------------+
|  benchmark                             |
+----------------------------------------+
```

## Kit

- Inspect AI
- PennyLane or Qiskit
- equivalence checkers (e.g. MQT QCEC)
- LLM APIs

**Hardware:** API credits

## Campaign

```text
  P1  [=====]                     m0-3      Benchmark of quantum programming tasks with verified answers
  P2        [=====]               m3-6      Agent with verification-in-the-loop
  P3              [=====]         m6-9      Compare models and with/without verification
  P4                    [=====]   m9-12     Release benchmark as an eval and write paper
```

## Gate: done when you can show

```text
  [ ] verified task success rate
  [ ] wrong-but-confident rate without verification
  [ ] cost per task
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

None special.

## Resume line (fill with your measured numbers)

> Built a verified quantum-programming agent and benchmark; verification cut wrong outputs from [N]% to [N]%.

**Skills it proves:** AI agents · quantum software · formal verification

## System map

```text
  QAGENT SYSTEM MAP

+-----------------------+    +-----------------------+    +-----------------------+
|  task bank            |--->|  agent                |--->|  simulator            |
+-----------------------+    +-----------------------+    +-----------------------+
           |
           v
+-----------------------+    +-----------------------+
|  equivalence checker  |--->|  eval harness         |
+-----------------------+    +-----------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   Research
  PUBLICATION TARGET     NeurIPS Datasets and Benchmarks, IEEE QCE
```

## Deliverables

- Benchmark
- Agent code
- Inspect eval
- Paper

## Standards and regulations to meet

- Inspect Evals guidelines

## Who sees this

Where this work gets in front of the people who lead the field (see the
[visibility playbook](../docs/visibility-playbook.md) for how to use each one):

```text
  >> QHack
  >> Inspect Evals contributors
  >> quantum and AI labs alike
```

## Defend it

1. Why is verification essential here?
2. What can equivalence checking not catch?
3. How does this generalise to other high-stakes code?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/qagent  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- QSIMGPU](118-qsimgpu.md) · [atlas index](../README.md) · [QREADY ->](120-qready.md)
