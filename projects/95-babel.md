# 95 · BABEL

```text
    (( "Wo ist Ihre Mutter?" )) --> [ device ] --> (( "Where is your mother?" ))
                                   offline, 1.1 s
```

**Offline speech translation device for responders**

> English, German, Ukrainian, Arabic, Turkish, with no network.

```text
  TRACK M MASTERPIECE: CIVIC, SCIENCE AND HUMAN PERFORMANCE  |  LEVEL [#####]  |  ~14 MONTHS  |  BUDGET €300
```

## The mission

Responders meet people they can't talk to, exactly when it matters most.

## How it works

```text
+-----------------------+
|  speech               |
+-----------------------+
           |
           v
+-----------------------+
|  on-device ASR        |
+-----------------------+
           |
           v
+-----------------------+
|  MT                   |
+-----------------------+
           |
           v
+-----------------------+
|  TTS                  |
+-----------------------+
           |
           v
+-----------------------+
|  confidence display   |
+-----------------------+
           |
           v
+-----------------------+
|  phrasebook fallback  |
+-----------------------+
```

## Kit

- whisper.cpp
- NLLB or Marian MT (quantised)
- Piper TTS
- Jetson or phone

**Hardware:** Jetson or phone + rugged speaker

## Campaign

```text
  P1  [=====]                     m0-3.5    Language set chosen with local responders
  P2        [=====]               m3.5-7    On-device pipeline with latency budget
  P3              [=====]         m7-10.5   Domain phrasebook and evaluation with native speakers
  P4                    [=====]   m10.5-14  Field exercise integration with LANTERN
```

## Gate: done when you can show

```text
  [ ] translation adequacy (human-rated)
  [ ] end-to-end latency
  [ ] ASR WER in noise
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Shows uncertainty; critical medical phrases use a verified phrasebook, not free MT.

## Resume line (fill with your measured numbers)

> Built offline 5-language speech translation at [N] s latency with human-rated adequacy [N]/5.

**Skills it proves:** speech · MT · edge deployment

## System map

```text
  BABEL SYSTEM MAP

+--------------+    +--------------+    +--------------+
|  ASR         |--->|  MT          |--->|  TTS         |
+--------------+    +--------------+    +--------------+
       |
       v
+--------------+    +--------------+
|  phrasebook  |--->|  UI          |
+--------------+    +--------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   TRL 4 -> 6
  PUBLICATION TARGET     ISCRAM or speech technology workshop
```

## Deliverables

- Device build
- Evaluation
- Phrasebook
- LANTERN integration

## Standards and regulations to meet

- Accessibility
- GDPR (voice data stays local)

## Defend it

1. Why a verified phrasebook for critical phrases?
2. How does noise affect ASR, and what did you do?
3. Which languages, and why those?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/babel  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- SKYEDGE](94-skyedge.md) · [atlas index](../README.md) · [WAYFINDER ->](96-wayfinder.md)
