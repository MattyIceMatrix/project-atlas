# 67 · EDGEBENCH

```text
    model        quality  tok/s   J/answer
    small-1B     61.2     34.0    4.1   ####
    small-3B     68.9     12.5    11.8  ##
```

**Benchmark and leaderboard for on-device LLMs**

> Quality, speed and joules per answer, on real edge hardware.

```text
  TRACK J MASTERPIECE: FOUNDATION MODELS AND AI INFRASTRUCTURE  |  LEVEL [#####]  |  ~12 MONTHS  |  BUDGET €500
```

## The mission

LLM leaderboards ignore latency and energy, which decide edge deployments.

## How it works

```text
+--------------------------+
|  task suite              |
+--------------------------+
             |
             v
+--------------------------+
|  harness on each device  |
+--------------------------+
             |
             v
+--------------------------+
|  power measurement       |
+--------------------------+
             |
             v
+--------------------------+
|  leaderboard site        |
+--------------------------+
```

## Kit

- Python
- llama.cpp
- MLC
- power meters
- static site

**Hardware:** Jetson, Raspberry Pi 5, phone, laptop NPU

## Campaign

```text
  P1  [=====]                     m0-3      Task suite with licensing and contamination checks
  P2        [=====]               m3-6      Harness with repeatable power measurement
  P3              [=====]         m6-9      20+ model/runtime/device combinations
  P4                    [=====]   m9-12     Public leaderboard and methodology paper
```

## Gate: done when you can show

```text
  [ ] measurement repeatability (CV%)
  [ ] combinations covered
  [ ] community submissions
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Transparent methodology; no vendor sponsorship hidden.

## Resume line (fill with your measured numbers)

> Built an edge-LLM benchmark measuring quality, latency and energy across [N] device/model combinations.

**Skills it proves:** benchmarking · measurement science · edge AI

## System map

```text
  EDGEBENCH SYSTEM MAP

+------------------+    +------------------+    +------------------+
|  task suite      |--->|  device harness  |--->|  power capture   |
+------------------+    +------------------+    +------------------+
         |
         v
+------------------+    +------------------+
|  results DB      |--->|  leaderboard     |
+------------------+    +------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   Research artefact
  PUBLICATION TARGET     NeurIPS Datasets and Benchmarks track
```

## Deliverables

- Benchmark suite
- Leaderboard site
- Methodology paper
- Raw data

## Standards and regulations to meet

- MLPerf-inspired run rules

## Defend it

1. How do you make power measurements repeatable?
2. What is benchmark contamination?
3. Why per-answer energy rather than per-token?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/edgebench  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- AGENTGRID](66-agentgrid.md) · [atlas index](../README.md) · [FEDERATE ->](68-federate.md)
