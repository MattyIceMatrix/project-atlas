# 28 · GHOSTPRINT

```text
    firmware.bin --> [ unpack ] --> [ hash + SBOM + secrets scan ]
                                           |
                 known-good? NO --> diff --> "telnetd added, root pw hardcoded"
```

**Firmware integrity checker for IoT devices**

> Is your camera still running the firmware the vendor shipped?

```text
  TRACK D CYBER DEFENSE  |  LEVEL [###..]  |  ~3 MONTHS  |  BUDGET €30
```

## The mission

Cheap IoT devices are rarely checked for tampered or outdated firmware.

## How it works

```text
+----------------------------------------+
|  firmware image                        |
+----------------------------------------+
                    |
                    v
+----------------------------------------+
|  binwalk unpack                        |
+----------------------------------------+
                    |
                    v
+----------------------------------------+
|  hashes, SBOM, secret and config scan  |
+----------------------------------------+
                    |
                    v
+----------------------------------------+
|  report                                |
+----------------------------------------+
```

## Kit

- binwalk
- Syft
- Python
- YARA

**Hardware:** Old IoT devices you own

## Campaign

```text
  P1  [=====]                     m0-0.8    Unpack and inventory vendor firmware
  P2        [=====]               m0.8-1.5  Known-good baselines and diffing
  P3              [=====]         m1.5-2.2  Secret and weak-config detection
  P4                    [=====]   m2.2-3    Report and responsible disclosure workflow
```

## Gate: done when you can show

```text
  [ ] images analysed
  [ ] findings confirmed
  [ ] false positives
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Only devices you own; follow coordinated disclosure.

## Resume line (fill with your measured numbers)

> Built a firmware integrity pipeline that analysed [N] IoT images and confirmed [N] findings.

**Skills it proves:** firmware analysis · supply chain · YARA

## Masterpiece upgrade path

```text
   LEVEL [###..]  ====================>  LEVEL [#####]
```

Combine firmware analysis with secure-boot OS work and EU cyber-resilience requirements.

**Grows into:** [EDGEOS](53-edgeos.md) · **Publication target:** Embedded security conference

## Defend it

1. What is coordinated vulnerability disclosure?
2. Why is a hash match not proof of safety?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/ghostprint  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- LOGLENS](27-loglens.md) · [atlas index](../README.md) · [CONVEYOR ->](29-conveyor.md)
