# 32 · COLDSTART

```text
    cost/day
     |  ####                     before
     |  #### ##
     |  ## ## ## ..  ..  ..       after
     +---------------------- time
```

**Serverless inference cost optimiser**

> Same predictions, a fraction of the bill.

```text
  TRACK E CLOUD, DATA AND MLOPS  |  LEVEL [###..]  |  ~2 MONTHS  |  BUDGET €20
```

## The mission

Teams over-provision GPUs for spiky inference traffic.

## How it works

```text
+----------------------------------------------------------------+
|  traffic replay                                                |
+----------------------------------------------------------------+
                                |
                                v
+----------------------------------------------------------------+
|  try configs (batching, quantisation, CPU vs GPU, serverless)  |
+----------------------------------------------------------------+
                                |
                                v
+----------------------------------------------------------------+
|  pick Pareto front                                             |
+----------------------------------------------------------------+
```

## Kit

- Python
- Locust
- ONNX Runtime
- AWS Lambda or Azure Functions
- Terraform

**Hardware:** Cloud free tier + small budget

## Campaign

```text
  P1  [=====]                     m0-0.5    Benchmark harness with recorded traffic
  P2        [=====]               m0.5-1    Quantisation and batching experiments
  P3              [=====]         m1-1.5    Serverless vs container comparison
  P4                    [=====]   m1.5-2    Cost/latency report with a recommendation
```

## Gate: done when you can show

```text
  [ ] cost per 1k predictions
  [ ] p95 latency
  [ ] cold start time
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

None special.

## Resume line (fill with your measured numbers)

> Cut inference cost by [N]% at equal p95 latency through quantisation, batching and serverless.

**Skills it proves:** cloud cost · performance · IaC

## Masterpiece upgrade path

```text
   LEVEL [###..]  ====================>  LEVEL [#####]
```

Own inference engine plus cost-aware serving across cloud and edge.

**Grows into:** [INFERNO](63-inferno.md) · **Publication target:** MLSys workshop

## Defend it

1. What is a Pareto front and why show it?
2. When do cold starts make serverless wrong?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/coldstart  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- FEATUREFORGE](31-featureforge.md) · [atlas index](../README.md) · [WATCHTOWER ->](33-watchtower.md)
