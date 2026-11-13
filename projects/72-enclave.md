# 72 · ENCLAVE

```text
    client --(attest?)--> [ TEE: model + data ] --(quote OK)--> send encrypted prompt
                             operator: sees nothing
```

**Confidential AI inference with remote attestation**

> Even the server admin can't see your prompt.

```text
  TRACK K MASTERPIECE: TRUST, SECURITY AND SOVEREIGNTY  |  LEVEL [#####]  |  ~14 MONTHS  |  BUDGET €200
```

## The mission

Sensitive data can't be sent to inference servers that operators could inspect.

## How it works

```text
+-------------------------------------------------+
|  TEE VM (SEV-SNP/TDX) or GPU confidential mode  |
+-------------------------------------------------+
                        |
                        v
+-------------------------------------------------+
|  attestation                                    |
+-------------------------------------------------+
                        |
                        v
+-------------------------------------------------+
|  key release                                    |
+-------------------------------------------------+
                        |
                        v
+-------------------------------------------------+
|  encrypted inference                            |
+-------------------------------------------------+
```

## Kit

- Confidential VMs in cloud
- attestation services
- Rust or Python client
- vLLM

**Hardware:** Cloud confidential VMs

## Campaign

```text
  P1  [=====]                     m0-3.5    Threat model and attestation flow design
  P2        [=====]               m3.5-7    Confidential VM with verified boot measurements
  P3              [=====]         m7-10.5   Key release only after attestation; encrypted prompts
  P4                    [=====]   m10.5-14  Performance overhead and failure-mode report
```

## Gate: done when you can show

```text
  [ ] attestation success and time
  [ ] inference overhead %
  [ ] attacks blocked in tests
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

None special.

## Resume line (fill with your measured numbers)

> Built attested confidential inference adding [N]% overhead with keys released only to verified enclaves.

**Skills it proves:** confidential computing · cryptography · cloud security

## System map

```text
  ENCLAVE SYSTEM MAP

+------------------------+    +------------------------+    +------------------------+
|  TEE host              |--->|  attestation verifier  |--->|  key broker            |
+------------------------+    +------------------------+    +------------------------+
            |
            v
+------------------------+    +------------------------+
|  inference server      |--->|  client SDK            |
+------------------------+    +------------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   TRL 4 -> 5
  PUBLICATION TARGET     Confidential computing summit or security workshop
```

## Deliverables

- Reference implementation
- Threat model
- Benchmark
- Integration guide

## Standards and regulations to meet

- IETF RATS architecture (RFC 9334)
- Confidential Computing Consortium guidance

## Defend it

1. What does an attestation quote prove?
2. What remains in the trusted computing base?
3. Name a side-channel risk that still exists.

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/enclave  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- SOVEREIGN](71-sovereign.md) · [atlas index](../README.md) · [ZKAUDIT ->](73-zkaudit.md)
