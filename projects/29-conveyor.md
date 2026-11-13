# 29 · CONVEYOR

```text
   git push -> [train] -> [eval gate] -> [registry] -> [canary 10%] -> [100%]
                              |                            |
                           FAIL: stop                 drift? -> rollback
```

**End-to-end MLOps platform on k3s**

> From git push to monitored model, no hands.

```text
  TRACK E CLOUD, DATA AND MLOPS  |  LEVEL [####.]  |  ~4 MONTHS  |  BUDGET €0
```

## The mission

Most ML projects stop at a notebook; nothing about retraining, rollout or rollback is automated.

## How it works

```text
+------------------------------+
|  GitHub Actions              |
+------------------------------+
               |
               v
+------------------------------+
|  MLflow tracking + registry  |
+------------------------------+
               |
               v
+------------------------------+
|  KServe or BentoML on k3s    |
+------------------------------+
               |
               v
+------------------------------+
|  canary                      |
+------------------------------+
               |
               v
+------------------------------+
|  monitoring                  |
+------------------------------+
```

## Kit

- k3s
- MLflow
- BentoML or KServe
- Argo CD
- Prometheus
- Grafana

**Hardware:** Home lab (3 small VMs)

## Campaign

```text
  P1  [=====]                     m0-1      k3s cluster with GitOps (Argo CD)
  P2        [=====]               m1-2      Training pipeline with an evaluation gate
  P3              [=====]         m2-3      Canary deployment and automatic rollback
  P4                    [=====]   m3-4      Load test and a written runbook
```

## Gate: done when you can show

```text
  [ ] lead time commit-to-prod
  [ ] rollback time
  [ ] p95 latency
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

None special.

## Resume line (fill with your measured numbers)

> Built GitOps MLOps on k3s with eval-gated canaries; commit-to-prod [N] min, rollback [N] s.

**Skills it proves:** Kubernetes · GitOps · MLOps

## Defend it

1. What does the evaluation gate check, exactly?
2. Why canary instead of blue-green here?

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/conveyor  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- GHOSTPRINT](28-ghostprint.md) · [atlas index](../README.md) · [RIVERFLOW ->](30-riverflow.md)
