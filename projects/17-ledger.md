# 17 · LEDGER

```text
    [blk 1]--hash-->[blk 2]--hash-->[blk 3]--hash-->[blk 4]
       |               |               |               |
     who/what       who/what        who/what        who/what
    edit one block ==> every later hash breaks ==> DETECTED
```

**Tamper-evident audit log service for AI decisions**

> If an AI did it, LEDGER can prove when, why and under whose approval.

```text
  TRACK C AI SAFETY AND GOVERNANCE  |  LEVEL [##...]  |  ~2 MONTHS  |  BUDGET €0
```

## The mission

Regulators and incident responders need trustworthy records of automated decisions.

## How it works

```text
+--------------------------------------------+
|  event API                                 |
+--------------------------------------------+
                      |
                      v
+--------------------------------------------+
|  hash chain + periodic signed checkpoints  |
+--------------------------------------------+
                      |
                      v
+--------------------------------------------+
|  verifier CLI                              |
+--------------------------------------------+
                      |
                      v
+--------------------------------------------+
|  export for auditors                       |
+--------------------------------------------+
```

## Kit

- Go or Python
- Ed25519
- SQLite or Postgres
- OpenAPI

**Hardware:** None

## Campaign

```text
  P1  [=====]                     m0-0.5    Event schema aligned with logging duties for high-risk AI
  P2        [=====]               m0.5-1    Hash chain and signed checkpoints
  P3              [=====]         m1-1.5    Verifier and tamper tests
  P4                    [=====]   m1.5-2    Integrate with TRIPWIRE or LANTERN's Guardian
```

## Gate: done when you can show

```text
  [ ] write throughput
  [ ] verification time per 1M events
  [ ] tamper detection rate (target 100%)
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Logs can hold personal data; retention limits built in.

## Resume line (fill with your measured numbers)

> Built a tamper-evident decision log verifying 1M events in [N] s with signed checkpoints.

**Skills it proves:** cryptography · systems design · compliance engineering

## Defend it

1. What can a hash chain not protect against?
2. Why signed checkpoints and not a blockchain?

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/ledger  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- TRIPWIRE](16-tripwire.md) · [atlas index](../README.md) · [REDCELL ->](18-redcell.md)
