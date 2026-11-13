# 65 · RAGOPS

```text
    user(team A) --> [ authz ] --> [ retrieval: only A's docs ] --> [ LLM ] --> answer [1][2]
                                          \__ traces, evals, costs __/
```

**Multi-tenant enterprise RAG platform**

> Every answer cited, every document permission-checked, every query observable.

```text
  TRACK J MASTERPIECE: FOUNDATION MODELS AND AI INFRASTRUCTURE  |  LEVEL [#####]  |  ~14 MONTHS  |  BUDGET €30/month
```

## The mission

Enterprise RAG pilots leak documents across teams and can't prove answer quality.

## How it works

```text
+-----------------------------+
|  ingestion with ACLs        |
+-----------------------------+
              |
              v
+-----------------------------+
|  hybrid retrieval           |
+-----------------------------+
              |
              v
+-----------------------------+
|  permission filter          |
+-----------------------------+
              |
              v
+-----------------------------+
|  generation with citations  |
+-----------------------------+
              |
              v
+-----------------------------+
|  eval + tracing             |
+-----------------------------+
```

## Kit

- Python
- Qdrant or pgvector
- OpenFGA
- OpenTelemetry
- Kubernetes

**Hardware:** Cloud or home lab

## Campaign

```text
  P1  [=====]                     m0-3.5    Ingestion with document-level permissions
  P2        [=====]               m3.5-7    Hybrid retrieval with permission filtering and tests
  P3              [=====]         m7-10.5   Citations, guardrails, continuous evals
  P4                    [=====]   m10.5-14  Load test, cost dashboard, security review
```

## Gate: done when you can show

```text
  [ ] cross-tenant leaks in red-team tests (target 0)
  [ ] answer faithfulness
  [ ] p95 latency
  [ ] cost per query
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Synthetic company documents for demos.

## Resume line (fill with your measured numbers)

> Built a multi-tenant RAG platform with zero cross-tenant leaks in [N] red-team tests and [N]% faithfulness.

**Skills it proves:** platform engineering · authorisation · LLM ops

## System map

```text
  RAGOPS SYSTEM MAP

+--------------------+    +--------------------+    +--------------------+
|  ingestion         |--->|  vector store      |--->|  authz (ReBAC)     |
+--------------------+    +--------------------+    +--------------------+
          |
          v
+--------------------+    +--------------------+
|  generation        |--->|  eval and tracing  |
+--------------------+    +--------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   TRL 5 -> 6 (pilot-ready)
  PUBLICATION TARGET     Conference talk (e.g. KubeCon, PyCon)
```

## Deliverables

- Helm chart
- Security design doc
- Eval dashboard
- Reference architecture

## Standards and regulations to meet

- OWASP LLM Top 10
- ISO/IEC 27001 controls (reference)
- GDPR

## Defend it

1. Why filter permissions before retrieval, not after?
2. How do you evaluate a RAG system continuously?
3. What does observability look like for LLM calls?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/ragops  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- MINICOMPILER](64-minicompiler.md) · [atlas index](../README.md) · [AGENTGRID ->](66-agentgrid.md)
