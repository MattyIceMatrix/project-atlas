# 111 · QDECODER

```text
    o-x-o-x-o      syndrome:  . . 1 . .
    x-o-x-o-x                 . 1 . . .
    o-x-o-x-o      decoder --> correction chain --> logical error rate 1e-4
```

**Neural decoders for quantum error correction**

> Error correction is the road to useful quantum computers. Build a faster decoder.

```text
  TRACK O FRONTIER: QUANTUM COMPUTING AND QUANTUM AI  |  LEVEL [#####]  |  ~12 MONTHS  |  BUDGET €200
```

## The mission

Surface-code QEC needs decoders that are both accurate and fast enough to keep up with the hardware in real time.

## How it works

```text
+--------------------------------+
|  Stim circuit simulation       |
+--------------------------------+
                |
                v
+--------------------------------+
|  syndrome datasets             |
+--------------------------------+
                |
                v
+--------------------------------+
|  baseline (PyMatching)         |
+--------------------------------+
                |
                v
+--------------------------------+
|  neural decoder                |
+--------------------------------+
                |
                v
+--------------------------------+
|  latency + logical error rate  |
+--------------------------------+
```

## Kit

- Stim
- PyMatching
- PyTorch
- Deltakit (Riverlane)
- Python

**Hardware:** Laptop + one GPU

## Campaign

```text
  P1  [=====]                     m0-3      Reproduce surface-code thresholds with Stim + PyMatching
  P2        [=====]               m3-6      Neural decoder under realistic noise models
  P3              [=====]         m6-9      Latency optimisation (quantisation, FPGA-friendly design)
  P4                    [=====]   m9-12     Contribute a feature or benchmark upstream to Deltakit
```

## Gate: done when you can show

```text
  [ ] logical error rate vs PyMatching
  [ ] decode latency per round
  [ ] code distance supported
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

None special.

## Resume line (fill with your measured numbers)

> Built a neural surface-code decoder matching PyMatching's logical error rate at [N]x lower latency; contributed upstream.

**Skills it proves:** quantum error correction · ML systems · open source

## System map

```text
  QDECODER SYSTEM MAP

+----------------------+    +----------------------+    +----------------------+
|  noise models        |--->|  syndrome generator  |--->|  baseline decoder    |
+----------------------+    +----------------------+    +----------------------+
           |
           v
+----------------------+    +----------------------+
|  neural decoder      |--->|  benchmark           |
+----------------------+    +----------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   Research
  PUBLICATION TARGET     IEEE Quantum Week (QCE) or arXiv + upstream contribution
```

## Deliverables

- Decoder code
- Benchmark report
- Upstream PR
- Paper

## Standards and regulations to meet

- Open benchmark practice (Metriq-style)

## Who sees this

Where this work gets in front of the people who lead the field (see the
[visibility playbook](../docs/visibility-playbook.md) for how to use each one):

```text
  >> Unitary Foundation x Riverlane Deltakit Community Fund microgrants
  >> unitaryHACK bounties
  >> Riverlane engineers' reviews
```

## Defend it

1. What is a syndrome and why is decoding a matching problem?
2. Why does latency matter as much as accuracy?
3. Where does your decoder fail?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/qdecoder  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- COMPUTEWATCH](110-computewatch.md) · [atlas index](../README.md) · [QMLTRUTH ->](112-qmltruth.md)
