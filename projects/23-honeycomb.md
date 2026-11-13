# 23 · HONEYCOMB

```text
     ___    ___    ___
    / H \__/ O \__/ N \     ssh, http, smb decoys
    \___/  \___/  \___/
        \     |     /
      [ log lake ] --> [ LLM summary ] --> "Today: 3 botnets, 1 new credential list"
```

**Honeypot fleet with LLM-written threat summaries**

> Let attackers knock, then write the report for you.

```text
  TRACK D CYBER DEFENSE  |  LEVEL [##...]  |  ~2 MONTHS  |  BUDGET €5/month
```

## The mission

Honeypots collect lots of logs nobody reads.

## How it works

```text
+---------------------------------+
|  decoy services                 |
+---------------------------------+
                |
                v
+---------------------------------+
|  central logs                   |
+---------------------------------+
                |
                v
+---------------------------------+
|  enrichment                     |
+---------------------------------+
                |
                v
+---------------------------------+
|  LLM daily brief with IOC list  |
+---------------------------------+
```

## Kit

- Cowrie
- T-Pot or custom
- Elastic or Loki
- Python
- small LLM

**Hardware:** Small cloud VM, isolated

## Campaign

```text
  P1  [=====]                     m0-0.5    Isolated deployment with strict egress rules
  P2        [=====]               m0.5-1    Log pipeline and enrichment
  P3              [=====]         m1-1.5    Daily brief with IOCs, checked by hand
  P4                    [=====]   m1.5-2    Share sanitised findings
```

## Gate: done when you can show

```text
  [ ] events per day
  [ ] brief accuracy vs manual review
  [ ] time saved
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Isolated network; never used to attack back.

## Resume line (fill with your measured numbers)

> Ran a honeypot fleet and automated daily threat briefs; summaries matched analyst review [N]% of the time.

**Skills it proves:** threat intel · logging · LLM summarisation

## Defend it

1. How do you make sure the honeypot can't be used to attack others?
2. What is an IOC and why does it go stale?

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/honeycomb  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- SENTRY](22-sentry.md) · [atlas index](../README.md) · [PHISHNET ->](24-phishnet.md)
