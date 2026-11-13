# 27 · LOGLENS

```text
    alerts ==>  [ rules ] ==> [ LLM triage note ] ==> P1 | P2 | P3 | noise
                                     |
                   "Likely benign: backup job, same hour daily"
```

**SIEM-lite with LLM-assisted triage**

> First-pass triage at 3 a.m., so the analyst sleeps until it matters.

```text
  TRACK D CYBER DEFENSE  |  LEVEL [###..]  |  ~3 MONTHS  |  BUDGET €0
```

## The mission

Small teams can't staff a SOC; alerts pile up untriaged.

## How it works

```text
+---------------------------------+
|  logs                           |
+---------------------------------+
                |
                v
+---------------------------------+
|  Sigma rules                    |
+---------------------------------+
                |
                v
+---------------------------------+
|  enrichment                     |
+---------------------------------+
                |
                v
+---------------------------------+
|  LLM triage note with evidence  |
+---------------------------------+
                |
                v
+---------------------------------+
|  analyst queue                  |
+---------------------------------+
```

## Kit

- Wazuh or OpenSearch
- Sigma
- Python
- local LLM

**Hardware:** Home lab

## Campaign

```text
  P1  [=====]                     m0-0.8    Log sources and Sigma rules
  P2        [=====]               m0.8-1.5  Enrichment (asset, user, history)
  P3              [=====]         m1.5-2.2  LLM triage with mandatory evidence links
  P4                    [=====]   m2.2-3    Compare triage to your own manual calls on 200 alerts
```

## Gate: done when you can show

```text
  [ ] agreement with analyst priority
  [ ] missed true positives
  [ ] minutes saved per alert
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

The analyst decides; the model only drafts.

## Resume line (fill with your measured numbers)

> Built LLM-assisted alert triage agreeing with analyst priority [N]% of the time, saving [N] min/alert.

**Skills it proves:** SIEM · detection engineering · LLM ops

## Masterpiece upgrade path

```text
   LEVEL [###..]  ====================>  LEVEL [#####]
```

Become the triage layer of an autonomous SOC with purple-team evaluation.

**Grows into:** [AUTOSOC](74-autosoc.md) · **Publication target:** SANS-style paper

## Defend it

1. Why must every triage note link to evidence?
2. How could an attacker manipulate the triage model?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/loglens  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- ZEROTRUST-LAB](26-zerotrust-lab.md) · [atlas index](../README.md) · [GHOSTPRINT ->](28-ghostprint.md)
