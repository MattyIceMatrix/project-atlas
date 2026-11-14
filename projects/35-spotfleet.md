# 35 · SPOTFLEET

```text
    [gpu A] train..train..X  reclaimed
                        |
                   checkpoint --> [gpu B] resume..train..done
```

**Fault-tolerant GPU training on spot instances**

> Train on cheap GPUs that can vanish at any second.

```text
  TRACK E CLOUD, DATA AND MLOPS  |  LEVEL [###..]  |  ~2 MONTHS  |  BUDGET €40
```

## The mission

Spot GPUs are much cheaper but get reclaimed mid-training.

## How it works

```text
+------------------------------------------+
|  job queue                               |
+------------------------------------------+
                     |
                     v
+------------------------------------------+
|  spot provisioning                       |
+------------------------------------------+
                     |
                     v
+------------------------------------------+
|  frequent checkpoints to object storage  |
+------------------------------------------+
                     |
                     v
+------------------------------------------+
|  auto-resume                             |
+------------------------------------------+
```

## Kit

- SkyPilot or Terraform
- PyTorch
- S3-compatible storage

**Hardware:** Cloud spot GPUs

## Campaign

```text
  P1  [=====]                     m0-0.5    Checkpoint/resume that is bit-for-bit correct
  P2        [=====]               m0.5-1    Interruption handling and auto-resubmit
  P3              [=====]         m1-1.5    Cost and time comparison vs on-demand
  P4                    [=====]   m1.5-2    Chaos test: kill instances randomly
```

## Gate: done when you can show

```text
  [ ] cost saving
  [ ] wasted GPU minutes
  [ ] resume correctness
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

None special.

## Resume line (fill with your measured numbers)

> Built spot-instance training with auto-resume, cutting GPU cost [N]% with [N]% wasted compute.

**Skills it proves:** distributed training · cloud · reliability

## Masterpiece upgrade path

```text
   LEVEL [###..]  ====================>  LEVEL [#####]
```

Fault-tolerant training on your own cluster and spot capacity for real pretraining runs.

**Grows into:** [TINYFOUNDRY](61-tinyfoundry.md), [HOMECLUSTER](70-homecluster.md) · **Publication target:** Engineering blog + talk

## Defend it

1. How do you prove resume is correct?
2. How often should you checkpoint, and why?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/spotfleet  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- DATACOMPASS](34-datacompass.md) · [atlas index](../README.md) · [ORBITAL ->](36-orbital.md)
