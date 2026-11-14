# 110 · COMPUTEWATCH

```text
    [ GPU node ] --attested workload log--> [ verifier ] --> "training run < threshold: OK"
      secure enclave, signed counters, no model weights exposed
```

**Technical AI governance with hardware-backed compute verification**

> Verify what a data centre trained, without seeing the secrets.

```text
  TRACK N FRONTIER: SUPERINTELLIGENCE ALIGNMENT AND SAFETY  |  LEVEL [#####]  |  ~14 MONTHS  |  BUDGET €500
```

## The mission

International AI agreements need ways to verify compute use. Your security background fits this exactly.

## How it works

```text
+------------------------------------------+
|  threat model for verification           |
+------------------------------------------+
                     |
                     v
+------------------------------------------+
|  workload classification from telemetry  |
+------------------------------------------+
                     |
                     v
+------------------------------------------+
|  attestation-backed logs                 |
+------------------------------------------+
                     |
                     v
+------------------------------------------+
|  red-team evasion                        |
+------------------------------------------+
```

## Kit

- Python
- confidential computing tooling (TEE attestation)
- GPU telemetry (DCGM)
- ML classifiers

**Hardware:** Cloud confidential VMs + GPU instances

## Campaign

```text
  P1  [=====]                     m0-3.5    Literature and policy review (compute governance proposals)
  P2        [=====]               m3.5-7    Workload classifier: training vs inference vs other from telemetry
  P3              [=====]         m7-10.5   Attested, tamper-evident logging prototype
  P4                    [=====]   m10.5-14  Evasion red-team and policy write-up
```

## Gate: done when you can show

```text
  [ ] workload classification accuracy
  [ ] evasion success rate
  [ ] overhead
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Defensive governance research; publish limits clearly.

## Resume line (fill with your measured numbers)

> Prototyped attestation-backed compute verification classifying workloads at [N]% accuracy and red-teamed evasions.

**Skills it proves:** technical governance · confidential computing · security

## System map

```text
  COMPUTEWATCH SYSTEM MAP

+-----------------------+    +-----------------------+    +-----------------------+
|  threat model         |--->|  telemetry collector  |--->|  classifier           |
+-----------------------+    +-----------------------+    +-----------------------+
           |
           v
+-----------------------+    +-----------------------+
|  attestation log      |--->|  evasion lab          |
+-----------------------+    +-----------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   TRL 2 -> 3
  PUBLICATION TARGET     Technical AI governance workshops (e.g. at ICML), policy think-tank reports
```

## Deliverables

- Prototype
- Threat model
- Evasion report
- Policy brief

## Standards and regulations to meet

- IETF RATS (RFC 9334)
- Confidential Computing Consortium guidance

## Who sees this

Where this work gets in front of the people who lead the field (see the
[visibility playbook](../docs/visibility-playbook.md) for how to use each one):

```text
  >> MATS technical governance and compute governance tracks
  >> UK AISI
  >> AI policy institutes
```

## Defend it

1. What can be verified without exposing model weights?
2. How would a determined actor evade your scheme?
3. Which policy proposal does this make more feasible?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/computewatch  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- COTWATCH](109-cotwatch.md) · [atlas index](../README.md) · [QDECODER ->](111-qdecoder.md)
