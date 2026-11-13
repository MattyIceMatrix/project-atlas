# 46 · SPRECHEN

```text
    you:  "Ich habe gestern in die Stadt gegangen"
    coach: "Fast! -> Ich BIN gestern in die Stadt gegangen (Bewegung -> sein)"
```

**Offline German speaking coach**

> Talk, get corrected, no cloud listening.

```text
  TRACK G PEOPLE, SPORT AND COMMUNITY  |  LEVEL [##...]  |  ~3 MONTHS  |  BUDGET €0
```

## The mission

Learners need speaking practice with feedback, and many apps send voice to the cloud.

## How it works

```text
+--------------------------------+
|  mic                           |
+--------------------------------+
                |
                v
+--------------------------------+
|  local ASR                     |
+--------------------------------+
                |
                v
+--------------------------------+
|  grammar check with small LLM  |
+--------------------------------+
                |
                v
+--------------------------------+
|  spoken correction (TTS)       |
+--------------------------------+
                |
                v
+--------------------------------+
|  progress log                  |
+--------------------------------+
```

## Kit

- whisper.cpp
- local LLM
- Piper TTS
- Python

**Hardware:** Laptop

## Campaign

```text
  P1  [=====]                     m0-0.8    ASR quality on learner speech
  P2        [=====]               m0.8-1.5  Correction prompts with a test set of common errors
  P3              [=====]         m1.5-2.2  Spoken feedback loop
  P4                    [=====]   m2.2-3    Track progress by error type over weeks
```

## Gate: done when you can show

```text
  [ ] correction precision
  [ ] ASR word error rate on learner speech
  [ ] session latency
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Voice data stays local.

## Resume line (fill with your measured numbers)

> Built an offline speaking coach correcting common German errors at [N]% precision.

**Skills it proves:** speech · language learning · local LLMs

## Defend it

1. Why does ASR struggle with learner accents?
2. How do you avoid "correcting" things that were right?

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/sprechen  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- RECEIPTLENS](45-receiptlens.md) · [atlas index](../README.md) · [NEUROSPARK ->](47-neurospark.md)
