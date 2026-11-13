# 77 · PROVENANCE

```text
    image --> [ C2PA manifest? ] --yes--> signed history: camera -> edit -> publish
                   |
                   no --> [ forensic models ] --> "likely edited: face region" 0.71
```

**Content provenance and deepfake detection for newsrooms**

> Where did this image come from, and has it been changed?

```text
  TRACK K MASTERPIECE: TRUST, SECURITY AND SOVEREIGNTY  |  LEVEL [#####]  |  ~14 MONTHS  |  BUDGET €0
```

## The mission

Newsrooms must verify images and video fast; detectors alone are unreliable.

## How it works

```text
+-------------------------------+
|  C2PA manifest verification   |
+-------------------------------+
               |
               v
+-------------------------------+
|  forensic detectors           |
+-------------------------------+
               |
               v
+-------------------------------+
|  evidence report for editors  |
+-------------------------------+
```

## Kit

- C2PA SDK
- PyTorch
- forensic datasets
- web app

**Hardware:** None

## Campaign

```text
  P1  [=====]                     m0-3.5    C2PA verification and signing tool
  P2        [=====]               m3.5-7    Detector ensemble with calibrated outputs
  P3              [=====]         m7-10.5   Editor-facing evidence report
  P4                    [=====]   m10.5-14  Robustness study (compression, re-recording)
```

## Gate: done when you can show

```text
  [ ] detector AUC on held-out generators
  [ ] calibration error
  [ ] verification time
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Report uncertainty clearly; never label content "fake" on a model score alone.

## Resume line (fill with your measured numbers)

> Built a provenance + forensics tool with C2PA verification and calibrated detectors (AUC [N] on unseen generators).

**Skills it proves:** media forensics · standards · calibration

## System map

```text
  PROVENANCE SYSTEM MAP

+---------------------+    +---------------------+    +---------------------+
|  C2PA verifier      |--->|  signer             |--->|  detector ensemble  |
+---------------------+    +---------------------+    +---------------------+
          |
          v
+---------------------+    +---------------------+
|  calibrator         |--->|  report UI          |
+---------------------+    +---------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   TRL 4 -> 5
  PUBLICATION TARGET     Media forensics workshop or journalism-tech conference
```

## Deliverables

- Tool
- Robustness study
- Editor guide
- Paper draft

## Standards and regulations to meet

- C2PA specification
- EU AI Act transparency duties (Art. 50)

## Defend it

1. Why does provenance scale better than detection?
2. Why do detectors fail on new generators?
3. What does a good evidence report look like for an editor?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/provenance  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- DPVAULT](76-dpvault.md) · [atlas index](../README.md) · [PROVENGUARD ->](78-provenguard.md)
