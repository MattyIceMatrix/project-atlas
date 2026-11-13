# 61 · TINYFOUNDRY

```text
    [ web text ]--clean--dedupe--> [ tokens ] --> [ 125M-350M model ] --> evals
                                           loss \__
                                                    \____
```

**Train a small language model from scratch, end to end**

> Data, tokenizer, training, evals, model card. All yours.

```text
  TRACK J MASTERPIECE: FOUNDATION MODELS AND AI INFRASTRUCTURE  |  LEVEL [#####]  |  ~12 MONTHS  |  BUDGET €600
```

## The mission

Most engineers have only fine-tuned; very few have run the whole pretraining pipeline and understood every choice.

## How it works

```text
+---------------------------+
|  data collection          |
+---------------------------+
             |
             v
+---------------------------+
|  filtering + dedup        |
+---------------------------+
             |
             v
+---------------------------+
|  tokenizer                |
+---------------------------+
             |
             v
+---------------------------+
|  distributed pretraining  |
+---------------------------+
             |
             v
+---------------------------+
|  evals                    |
+---------------------------+
             |
             v
+---------------------------+
|  model card               |
+---------------------------+
```

## Kit

- PyTorch
- FSDP
- datatrove or custom
- SentencePiece
- lm-eval-harness

**Hardware:** Rented GPUs (a few hundred GPU-hours)

## Campaign

```text
  P1  [=====]                     m0-3      Data pipeline with licences, filtering and dedup
  P2        [=====]               m3-6      Tokenizer and a 25M-parameter rehearsal run
  P3              [=====]         m6-9      Main pretraining run with checkpoints and loss curves
  P4                    [=====]   m9-12     Evaluation, model card, release with data documentation
```

## Gate: done when you can show

```text
  [ ] validation perplexity
  [ ] benchmark scores vs similar-size models
  [ ] tokens/s/GPU
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Licensed or openly licensed data only; document what's in the data.

## Resume line (fill with your measured numbers)

> Pretrained a [N]M-parameter LLM from scratch (data to model card), matching <reference> on <benchmark>.

**Skills it proves:** pretraining · distributed training · data engineering

## System map

```text
  TINYFOUNDRY SYSTEM MAP

+-----------------+    +-----------------+    +-----------------+
|  data pipeline  |--->|  tokenizer      |--->|  trainer        |
+-----------------+    +-----------------+    +-----------------+
        |
        v
+-----------------+    +-----------------+
|  eval harness   |--->|  release kit    |
+-----------------+    +-----------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   Research artefact
  PUBLICATION TARGET     Hugging Face release + technical report on arXiv
```

## Deliverables

- Model weights
- Data card
- Training report with all curves
- Reproduction scripts

## Standards and regulations to meet

- Model cards (Mitchell et al.)
- Datasheets for datasets
- EU AI Act GPAI documentation concepts

## Defend it

1. Why does deduplication change model quality?
2. How did you choose model size for your compute budget?
3. What would you do with 10x more compute?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/tinyfoundry  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- MESHLIFE](60-meshlife.md) · [atlas index](../README.md) · [AERIALVLM ->](62-aerialvlm.md)
