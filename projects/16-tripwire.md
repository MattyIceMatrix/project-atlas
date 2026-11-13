# 16 · TRIPWIRE

```text
    untrusted text ---> [ T R I P W I R E ] ---> clean --> LLM
                               |
                               +--> flagged --> quarantine + log
```

**Prompt-injection firewall for LLM apps**

> Stops "ignore previous instructions" at the door.

```text
  TRACK C AI SAFETY AND GOVERNANCE  |  LEVEL [###..]  |  ~3 MONTHS  |  BUDGET €0
```

## The mission

Untrusted text in emails, web pages and files can hijack an LLM agent.

## How it works

```text
+-------------------------------------------+
|  input                                    |
+-------------------------------------------+
                     |
                     v
+-------------------------------------------+
|  heuristics + classifier + canary checks  |
+-------------------------------------------+
                     |
                     v
+-------------------------------------------+
|  allow / sanitise / block                 |
+-------------------------------------------+
                     |
                     v
+-------------------------------------------+
|  audit                                    |
+-------------------------------------------+
```

## Kit

- Python
- small classifier
- FastAPI middleware
- OpenTelemetry

**Hardware:** None

## Campaign

```text
  P1  [=====]                     m0-0.8    Collect public injection benchmarks; build your own held-out set
  P2        [=====]               m0.8-1.5  Layered detector (rules, classifier, canary tokens)
  P3              [=====]         m1.5-2.2  Middleware for an agent app
  P4                    [=====]   m2.2-3    Attack/defence report with bypasses you could not stop
```

## Gate: done when you can show

```text
  [ ] detection rate
  [ ] false positive rate on normal text
  [ ] added latency
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Defensive tool; published bypasses are reported responsibly.

## Resume line (fill with your measured numbers)

> Built a layered prompt-injection filter blocking [N]% of held-out attacks at [N]% false positives.

**Skills it proves:** AI security · classifiers · middleware

## Masterpiece upgrade path

```text
   LEVEL [###..]  ====================>  LEVEL [#####]
```

Layer into a full guardrail stack with a formally verified policy core and nightly red-teaming.

**Grows into:** [PROVENGUARD](78-provenguard.md), [REDCELL](18-redcell.md) · **Publication target:** AI security workshop

## Defend it

1. Why can no filter be perfect here?
2. What does defence in depth mean for agents?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/tripwire  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- GRANITE](15-granite.md) · [atlas index](../README.md) · [LEDGER ->](17-ledger.md)
