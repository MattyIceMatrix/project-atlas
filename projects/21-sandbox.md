# 21 · SANDBOX

```text
    agent --> [ token: read:/docs  ttl:5m ] --> tool
                |
    tries /etc/passwd ===> DENIED, logged
```

**Capability-limited sandbox for agent tools**

> Give the agent a key that only opens one door, for five minutes.

```text
  TRACK C AI SAFETY AND GOVERNANCE  |  LEVEL [####.]  |  ~3 MONTHS  |  BUDGET €0
```

## The mission

Agents get broad API keys and file access they don't need.

## How it works

```text
+----------------------------+
|  agent request             |
+----------------------------+
              |
              v
+----------------------------+
|  policy                    |
+----------------------------+
              |
              v
+----------------------------+
|  short-lived scoped token  |
+----------------------------+
              |
              v
+----------------------------+
|  containerised tool run    |
+----------------------------+
              |
              v
+----------------------------+
|  audit                     |
+----------------------------+
```

## Kit

- Docker or gVisor
- OPA/Rego
- Python
- LEDGER

**Hardware:** None

## Campaign

```text
  P1  [=====]                     m0-0.8    Threat model for agent tool use
  P2        [=====]               m0.8-1.5  Scoped token issuer with policy
  P3              [=====]         m1.5-2.2  Container isolation for code/file tools
  P4                    [=====]   m2.2-3    Escape attempts and results report
```

## Gate: done when you can show

```text
  [ ] blocked out-of-scope actions
  [ ] overhead per call
  [ ] escape attempts that succeeded (target 0)
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Defensive.

## Resume line (fill with your measured numbers)

> Built a least-privilege agent sandbox with scoped short-lived tokens, blocking 100% of tested escapes.

**Skills it proves:** security engineering · containers · policy-as-code

## Defend it

1. What is least privilege for an agent?
2. Where is your sandbox weakest?

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/sandbox  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- FAIRLINE](20-fairline.md) · [atlas index](../README.md) · [SENTRY ->](22-sentry.md)
