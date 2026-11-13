# 64 · MINICOMPILER

```text
    ONNX --> [ graph IR ] --> fuse(conv,bn,relu) --> tile --> [ C / CUDA kernels ]
                                                    speedup x3.1
```

**Tiny ML compiler for edge accelerators**

> From ONNX graph to fused kernels you wrote.

```text
  TRACK J MASTERPIECE: FOUNDATION MODELS AND AI INFRASTRUCTURE  |  LEVEL [#####]  |  ~16 MONTHS  |  BUDGET €0
```

## The mission

Edge performance depends on compilers few people understand.

## How it works

```text
+----------------------------------------------------------+
|  ONNX import                                             |
+----------------------------------------------------------+
                             |
                             v
+----------------------------------------------------------+
|  IR                                                      |
+----------------------------------------------------------+
                             |
                             v
+----------------------------------------------------------+
|  optimisation passes (fusion, constant folding, layout)  |
+----------------------------------------------------------+
                             |
                             v
+----------------------------------------------------------+
|  codegen                                                 |
+----------------------------------------------------------+
                             |
                             v
+----------------------------------------------------------+
|  autotune                                                |
+----------------------------------------------------------+
```

## Kit

- Python
- MLIR or a custom IR
- C/CUDA codegen
- TVM for comparison

**Hardware:** Laptop + Jetson

## Campaign

```text
  P1  [=====]                     m0-4      IR and interpreter that matches ONNX Runtime outputs
  P2        [=====]               m4-8      Optimisation passes with correctness tests
  P3              [=====]         m8-12     Code generation for CPU and Jetson GPU
  P4                    [=====]   m12-16    Autotuning and comparison to TVM/TensorRT
```

## Gate: done when you can show

```text
  [ ] speedup vs naive
  [ ] numerical error
  [ ] compile time
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

None special.

## Resume line (fill with your measured numbers)

> Built an ML compiler with fusion and autotuning reaching [N]x over naive and [N]% of TensorRT on Jetson.

**Skills it proves:** compilers · GPU programming · edge AI

## System map

```text
  MINICOMPILER SYSTEM MAP

+-------------+    +-------------+    +-------------+
|  frontend   |--->|  IR         |--->|  passes     |
+-------------+    +-------------+    +-------------+
      |
      v
+-------------+    +-------------+
|  codegen    |--->|  autotuner  |
+-------------+    +-------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   Research artefact
  PUBLICATION TARGET     MLSys workshop or blog series
```

## Deliverables

- Compiler source
- Pass documentation
- Benchmarks
- Tutorial series

## Standards and regulations to meet

- ONNX opset spec

## Defend it

1. Why does operator fusion help memory-bound models?
2. How do you test a compiler pass is correct?
3. What does autotuning search over?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/minicompiler  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- INFERNO](63-inferno.md) · [atlas index](../README.md) · [RAGOPS ->](65-ragops.md)
