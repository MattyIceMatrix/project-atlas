# 79 · OTSENTINEL

```text
    [HMI]--Modbus/TCP--[PLC]--[pump][valve]
              |
         [ SENTINEL ]: "write to coil 12 at 03:00 from unknown host" ALERT
```

**Industrial control system anomaly detection lab**

> Protect the pumps and valves, not just the laptops.

```text
  TRACK K MASTERPIECE: TRUST, SECURITY AND SOVEREIGNTY  |  LEVEL [#####]  |  ~14 MONTHS  |  BUDGET €150
```

## The mission

Water and energy utilities run old industrial protocols with little monitoring.

## How it works

```text
+-------------------------------+
|  simulated plant              |
+-------------------------------+
               |
               v
+-------------------------------+
|  passive network tap          |
+-------------------------------+
               |
               v
+-------------------------------+
|  protocol parsing             |
+-------------------------------+
               |
               v
+-------------------------------+
|  process-aware anomaly model  |
+-------------------------------+
               |
               v
+-------------------------------+
|  alerts                       |
+-------------------------------+
```

## Kit

- OpenPLC
- GRFICS or custom sim
- Zeek with ICS plugins
- Python
- Grafana

**Hardware:** Home lab VMs, optional cheap PLC

## Campaign

```text
  P1  [=====]                     m0-3.5    Simulated water-treatment process and network
  P2        [=====]               m3.5-7    Passive monitoring and protocol parsing
  P3              [=====]         m7-10.5   Process-aware anomaly detection (physics + network)
  P4                    [=====]   m10.5-14  Purple-team scenarios mapped to ATT&CK for ICS
```

## Gate: done when you can show

```text
  [ ] scenario detection rate
  [ ] false alarms per day
  [ ] detection latency
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Lab only; never scan or test real utility systems.

## Resume line (fill with your measured numbers)

> Built an ICS monitoring lab detecting [N]/[N] ATT&CK-for-ICS scenarios with [N] false alarms/day.

**Skills it proves:** OT security · protocols · anomaly detection

## System map

```text
  OTSENTINEL SYSTEM MAP

+-------------------+    +-------------------+    +-------------------+
|  process sim      |--->|  PLC              |--->|  network tap      |
+-------------------+    +-------------------+    +-------------------+
         |
         v
+-------------------+    +-------------------+
|  detectors        |--->|  analyst console  |
+-------------------+    +-------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   TRL 3 -> 4
  PUBLICATION TARGET     ICS security conference (e.g. S4) or BSides
```

## Deliverables

- Lab recipe
- Detection pack
- Scenario library
- Report

## Standards and regulations to meet

- IEC 62443
- MITRE ATT&CK for ICS
- NIS2 (utilities)

## Defend it

1. Why must OT monitoring be passive?
2. What makes process-aware detection stronger?
3. Why are legacy protocols insecure by design?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/otsentinel  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- PROVENGUARD](78-provenguard.md) · [atlas index](../README.md) · [CREDMESH ->](80-credmesh.md)
