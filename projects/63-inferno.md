# 63 · INFERNO

```text
    requests ==> [ scheduler ] ==> [ batch ] ==> [ GPU kernels ]
                      |               ^
                 [ paged KV cache ]---'     tokens/s: 2,340
```

**LLM inference server built from scratch**

> Continuous batching and a paged KV cache, written by you.

```text
  TRACK J MASTERPIECE: FOUNDATION MODELS AND AI INFRASTRUCTURE  |  LEVEL [#####]  |  ~14 MONTHS  |  BUDGET €200
```

## The mission

Inference engines are black boxes to most engineers; understanding them is a superpower.

## How it works

```text
+--------------------------------------+
|  HTTP API                            |
+--------------------------------------+
                   |
                   v
+--------------------------------------+
|  scheduler with continuous batching  |
+--------------------------------------+
                   |
                   v
+--------------------------------------+
|  paged KV cache                      |
+--------------------------------------+
                   |
                   v
+--------------------------------------+
|  custom kernels                      |
+--------------------------------------+
                   |
                   v
+--------------------------------------+
|  streaming tokens                    |
+--------------------------------------+
```

## Kit

- Rust or C++
- CUDA or Triton
- PyTorch reference
- OpenAI-compatible API

**Hardware:** One consumer or rented GPU

## Campaign

```text
  P1  [=====]                     m0-3.5    Correct single-request inference vs reference
  P2        [=====]               m3.5-7    Continuous batching scheduler
  P3              [=====]         m7-10.5   Paged KV cache and memory manager
  P4                    [=====]   m10.5-14  Benchmarks vs vLLM and llama.cpp with honest analysis
```

## Gate: done when you can show

```text
  [ ] tokens/s at batch 1 and 32
  [ ] p99 latency
  [ ] memory efficiency
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

None special.

## Resume line (fill with your measured numbers)

> Wrote an LLM inference server with continuous batching and paged KV cache reaching [N]% of vLLM throughput.

**Skills it proves:** systems programming · GPU · performance engineering

## System map

```text
  INFERNO SYSTEM MAP

+--------------------+    +--------------------+    +--------------------+
|  API layer         |--->|  scheduler         |--->|  KV cache manager  |
+--------------------+    +--------------------+    +--------------------+
          |
          v
+--------------------+    +--------------------+
|  kernels           |--->|  benchmark suite   |
+--------------------+    +--------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   Research/engineering artefact
  PUBLICATION TARGET     Engineering blog series + talk
```

## Deliverables

- Engine source
- Benchmark report
- Design docs
- Talk slides

## Standards and regulations to meet

- OpenAI-compatible API
- reproducible benchmarks

## Defend it

1. Why does continuous batching beat static batching?
2. What problem does paging the KV cache solve?
3. Where is your engine slower than vLLM and why?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/inferno  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- AERIALVLM](62-aerialvlm.md) · [atlas index](../README.md) · [MINICOMPILER ->](64-minicompiler.md)
