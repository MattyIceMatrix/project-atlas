# 70 · HOMECLUSTER

```text
    [ login ] --> [ Slurm / Kueue ] --> [gpu0][gpu1][cpu0][cpu1]
                       | quotas, priorities, preemption
                   [ MLflow ] [ MinIO ] [ Grafana ]
```

**Small GPU cluster with a real scheduler and MLOps**

> Your own mini cloud for training, with quotas and fair sharing.

```text
  TRACK J MASTERPIECE: FOUNDATION MODELS AND AI INFRASTRUCTURE  |  LEVEL [#####]  |  ~12 MONTHS  |  BUDGET €1,500
```

## The mission

Learning cluster operations is impossible on one laptop and expensive in the cloud.

## How it works

```text
+-----------------------+
|  provisioning (IaC)   |
+-----------------------+
           |
           v
+-----------------------+
|  scheduler            |
+-----------------------+
           |
           v
+-----------------------+
|  shared storage       |
+-----------------------+
           |
           v
+-----------------------+
|  experiment tracking  |
+-----------------------+
           |
           v
+-----------------------+
|  monitoring and cost  |
+-----------------------+
```

## Kit

- Proxmox
- Ansible
- Kubernetes + Kueue or Slurm
- MinIO
- MLflow
- Grafana

**Hardware:** 2–3 used workstations, at least one GPU

## Campaign

```text
  P1  [=====]                     m0-3      Infrastructure as code for the whole cluster
  P2        [=====]               m3-6      Scheduler with quotas and preemption
  P3              [=====]         m6-9      Storage, tracking, and multi-user setup
  P4                    [=====]   m9-12     Run TINYFOUNDRY or LOOM jobs on it; publish an ops runbook
```

## Gate: done when you can show

```text
  [ ] GPU utilisation
  [ ] job wait time
  [ ] mean time to recover a node
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Mind electricity costs and noise for the household.

## Resume line (fill with your measured numbers)

> Built an IaC-managed GPU cluster with fair-share scheduling at [N]% GPU utilisation.

**Skills it proves:** HPC · Kubernetes · infrastructure as code

## System map

```text
  HOMECLUSTER SYSTEM MAP

+----------------+    +----------------+    +----------------+
|  provisioning  |--->|  scheduler     |--->|  storage       |
+----------------+    +----------------+    +----------------+
        |
        v
+----------------+    +----------------+
|  tracking      |--->|  monitoring    |
+----------------+    +----------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   Operational lab
  PUBLICATION TARGET     Blog series + homelab community talk
```

## Deliverables

- IaC repo
- Runbook
- Utilisation reports
- Architecture doc

## Standards and regulations to meet

- CIS benchmarks for hosts (reference)

## Defend it

1. Slurm vs Kubernetes for ML: which and why?
2. What is preemption and when is it fair?
3. How do you recover a dead node?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/homecluster  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- SYNTHSCENE](69-synthscene.md) · [atlas index](../README.md) · [SOVEREIGN ->](71-sovereign.md)
