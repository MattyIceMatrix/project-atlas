# 22 · SENTRY

```text
    [ router ]--mirror port-->[ SENTRY ]
                                |   zeek logs -> features -> anomaly score
     02:13  printer -> 185.x.x.x:4444   score 0.97   ALERT
```

**Home-network intrusion detection with ML anomaly scoring**

> A night watch for your router.

```text
  TRACK D CYBER DEFENSE  |  LEVEL [##...]  |  ~3 MONTHS  |  BUDGET €60
```

## The mission

Home and small-office networks have no security monitoring at all.

## How it works

```text
+----------------------+
|  port mirror         |
+----------------------+
           |
           v
+----------------------+
|  Zeek/Suricata       |
+----------------------+
           |
           v
+----------------------+
|  feature extraction  |
+----------------------+
           |
           v
+----------------------+
|  isolation forest    |
+----------------------+
           |
           v
+----------------------+
|  alerts              |
+----------------------+
```

## Kit

- Proxmox VM or Raspberry Pi
- Zeek
- Suricata
- Python
- Grafana

**Hardware:** Managed switch with port mirroring

## Campaign

```text
  P1  [=====]                     m0-0.8    Sensor setup and baseline traffic
  P2        [=====]               m0.8-1.5  Features and anomaly model
  P3              [=====]         m1.5-2.2  Alert tuning over 4 weeks
  P4                    [=====]   m2.2-3    Replay public attack captures to measure detection
```

## Gate: done when you can show

```text
  [ ] detection on replayed attacks
  [ ] alerts per day
  [ ] sensor CPU load
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Monitor only networks you own; inform household members.

## Resume line (fill with your measured numbers)

> Built an ML-assisted home IDS detecting [N]% of replayed attacks at [N] alerts/day.

**Skills it proves:** network security · Zeek · anomaly detection

## Masterpiece upgrade path

```text
   LEVEL [##...]  ====================>  LEVEL [#####]
```

Grow into an OT-aware monitoring lab and a human-gated SOC.

**Grows into:** [OTSENTINEL](79-otsentinel.md), [AUTOSOC](74-autosoc.md) · **Publication target:** BSides

## Defend it

1. Why does unsupervised detection drown you in alerts?
2. How did you set the threshold?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/sentry  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- SANDBOX](21-sandbox.md) · [atlas index](../README.md) · [HONEYCOMB ->](23-honeycomb.md)
