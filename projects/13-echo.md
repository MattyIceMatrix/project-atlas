# 13 · ECHO

```text
    (( speaker A ))   (( speaker B ))
           \               /
        [ local ASR + diarisation ]
                 |
     decisions | actions | owners | dates
```

**Offline meeting notes on a laptop**

> Minutes, decisions and to-dos, with the recording never leaving your desk.

```text
  TRACK B GENERATIVE AI AND LLM SYSTEMS  |  LEVEL [##...]  |  ~2 MONTHS  |  BUDGET €0
```

## The mission

Meeting transcription tools upload sensitive audio to vendors.

## How it works

```text
+-----------------------+
|  audio                |
+-----------------------+
           |
           v
+-----------------------+
|  Whisper              |
+-----------------------+
           |
           v
+-----------------------+
|  speaker diarisation  |
+-----------------------+
           |
           v
+-----------------------+
|  local LLM summary    |
+-----------------------+
           |
           v
+-----------------------+
|  markdown minutes     |
+-----------------------+
```

## Kit

- whisper.cpp
- pyannote
- llama.cpp
- Python

**Hardware:** Laptop (NPU or GPU helps)

## Campaign

```text
  P1  [=====]                     m0-0.5    Transcription + diarisation on public meeting corpora
  P2        [=====]               m0.5-1    Action-item extraction with evaluation
  P3              [=====]         m1-1.5    Minutes template and export
  P4                    [=====]   m1.5-2    No-network verification
```

## Gate: done when you can show

```text
  [ ] word error rate
  [ ] action-item F1
  [ ] real-time factor
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Everyone in the meeting consents to recording.

## Resume line (fill with your measured numbers)

> Built offline meeting minutes with [N]% action-item F1 at [N]x real time on a laptop.

**Skills it proves:** speech · summarisation · evaluation

## Masterpiece upgrade path

```text
   LEVEL [##...]  ====================>  LEVEL [#####]
```

Speaker-attributed, multilingual minutes with action tracking across meetings and an on-prem deployment option.

**Grows into:** [SOVEREIGN](71-sovereign.md), [BABEL](95-babel.md) · **Publication target:** Speech technology workshop

## Defend it

1. How did you measure action-item quality?
2. What fails with overlapping speakers?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/echo  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- LOOM](12-loom.md) · [atlas index](../README.md) · [PATCHWORK ->](14-patchwork.md)
