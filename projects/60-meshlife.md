# 60 · MESHLIFE

```text
    [phone]~~(LoRa)~~[node]~~(LoRa)~~[node]~~[command post]
        "trapped, 2 people, 1st floor"  -> P1, location, needs: boat
```

**Disaster mesh network with AI message triage**

> When every tower is down, the phones talk to each other.

```text
  TRACK I MASTERPIECE: AUTONOMOUS SYSTEMS  |  LEVEL [#####]  |  ~14 MONTHS  |  BUDGET €600
```

## The mission

In disasters, residents can't reach responders and responders drown in unstructured messages.

## How it works

```text
+------------------------------+
|  Meshtastic-style LoRa mesh  |
+------------------------------+
               |
               v
+------------------------------+
|  store-and-forward           |
+------------------------------+
               |
               v
+------------------------------+
|  on-device triage model      |
+------------------------------+
               |
               v
+------------------------------+
|  command post map            |
+------------------------------+
```

## Kit

- Meshtastic firmware
- ESP32 or nRF52
- Python
- small LLM
- MapLibre

**Hardware:** 6–10 LoRa nodes, one edge server

## Campaign

```text
  P1  [=====]                     m0-3.5    Mesh deployment and range tests in a village
  P2        [=====]               m3.5-7    Message format and store-and-forward guarantees
  P3              [=====]         m7-10.5   Triage model that extracts location, people, needs
  P4                    [=====]   m10.5-14  Exercise with volunteers and the LANTERN kit
```

## Gate: done when you can show

```text
  [ ] delivery rate
  [ ] end-to-end latency
  [ ] triage extraction accuracy
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Complements 112, never replaces it; legal radio power limits.

## Resume line (fill with your measured numbers)

> Built a LoRa disaster mesh delivering [N]% of messages with on-device triage at [N]% accuracy.

**Skills it proves:** radio networking · embedded · NLP

## System map

```text
  MESHLIFE SYSTEM MAP

+-----------------------------+    +-----------------------------+    +-----------------------------+
|  mesh nodes                 |--->|  routing and store-forward  |--->|  triage model               |
+-----------------------------+    +-----------------------------+    +-----------------------------+
              |
              v
+-----------------------------+    +-----------------------------+
|  command map                |--->|  LANTERN bridge             |
+-----------------------------+    +-----------------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   TRL 3 -> 6 (exercise)
  PUBLICATION TARGET     ISCRAM conference
```

## Deliverables

- Node build guide
- Exercise report
- Triage model card
- Open firmware config

## Standards and regulations to meet

- ETSI EN 300 220 (868 MHz SRD
- reference)
- Common Alerting Protocol (CAP) format

## Defend it

1. Why LoRa and not Wi-Fi mesh?
2. How do you stop the mesh being flooded with duplicates?
3. What are the legal duty-cycle limits in the 868 MHz band?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/meshlife  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- RECYCLR](59-recyclr.md) · [atlas index](../README.md) · [TINYFOUNDRY ->](61-tinyfoundry.md)
