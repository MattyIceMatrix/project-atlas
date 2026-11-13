# 55 · RAILWATCH

```text
    ===[o]==[o]=============     trolley
    ---+----+----+----+-----     sleeper OK  OK  [!] OK
```

**Autonomous rail-track inspection trolley**

> Finds the cracked rail before the train does.

```text
  TRACK I MASTERPIECE: AUTONOMOUS SYSTEMS  |  LEVEL [#####]  |  ~16 MONTHS  |  BUDGET €1,600
```

## The mission

Track inspection is labour-intensive and periodic.

## How it works

```text
+------------------------------------------------+
|  line cameras + accelerometers                 |
+------------------------------------------------+
                        |
                        v
+------------------------------------------------+
|  defect detection (rail, sleepers, fasteners)  |
+------------------------------------------------+
                        |
                        v
+------------------------------------------------+
|  geo-referenced report                         |
+------------------------------------------------+
```

## Kit

- Jetson
- line-scan camera
- PyTorch
- ROS 2
- GIS

**Hardware:** Push-trolley test rig on a heritage or private test track

## Campaign

```text
  P1  [=====]                     m0-4      Partner with a heritage railway; safety briefing and permissions
  P2        [=====]               m4-8      Data collection rig and labelled dataset
  P3              [=====]         m8-12     Defect models with per-class metrics
  P4                    [=====]   m12-16    Inspection report matching the operator's format
```

## Gate: done when you can show

```text
  [ ] defect recall per class
  [ ] false alarms per km
  [ ] km inspected per hour
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Only with operator permission and their safety rules; never on live mainline track.

## Resume line (fill with your measured numbers)

> Built a rail inspection rig detecting [N] defect classes at [N]% recall on a heritage line.

**Skills it proves:** industrial vision · data collection · domain partnership

## System map

```text
  RAILWATCH SYSTEM MAP

+--------------------+    +--------------------+    +--------------------+
|  sensor rig        |--->|  synchronisation   |--->|  defect models     |
+--------------------+    +--------------------+    +--------------------+
          |
          v
+--------------------+    +--------------------+
|  geo-referencing   |--->|  report generator  |
+--------------------+    +--------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   TRL 3 -> 5
  PUBLICATION TARGET     Railway engineering conference or applied CV workshop
```

## Deliverables

- Rig design
- Labelled dataset (if partner allows)
- Model and data cards
- Operator report sample

## Standards and regulations to meet

- EN 13848 track geometry (reference)
- Operator safety rules
- GDPR for any people in images

## Defend it

1. Why is labelled data the bottleneck here?
2. How do you guarantee a missed defect is caught later?
3. What did the operator teach you that changed the design?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/railwatch  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- ROADSAGE](54-roadsage.md) · [atlas index](../README.md) · [AGRIFLEET ->](56-agrifleet.md)
