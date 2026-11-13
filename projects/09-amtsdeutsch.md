# 09 · AMTSDEUTSCH

```text
   .-----------------------.
   | Sehr geehrte Damen... |     -->   "Your tax office needs form X
   | gem. § 149 AO ...     |            by 30 June. Here is what to do."
   '-----------------------'
      [ OCR ] -> [ local LLM ] -> [ plain-language summary + deadlines ]
```

**Offline explainer for German government letters**

> Your Behörde letter, in plain words, without uploading it anywhere.

```text
  TRACK B GENERATIVE AI AND LLM SYSTEMS  |  LEVEL [##...]  |  ~3 MONTHS  |  BUDGET €0
```

## The mission

Official German letters are dense; newcomers and international families struggle, and uploading them to cloud AI exposes personal data.

## How it works

```text
+----------------------------------+
|  phone scan                      |
+----------------------------------+
                 |
                 v
+----------------------------------+
|  on-device OCR                   |
+----------------------------------+
                 |
                 v
+----------------------------------+
|  local LLM with glossary RAG     |
+----------------------------------+
                 |
                 v
+----------------------------------+
|  summary, deadlines, next steps  |
+----------------------------------+
```

## Kit

- Tesseract or PaddleOCR
- llama.cpp
- small instruct model
- SQLite FTS
- Streamlit

**Hardware:** Laptop with 16 GB RAM

## Campaign

```text
  P1  [=====]                     m0-0.8    Glossary of official terms with sources
  P2        [=====]               m0.8-1.5  OCR + summary pipeline on synthetic letters
  P3              [=====]         m1.5-2.2  Deadline extraction with tests
  P4                    [=====]   m2.2-3    Bilingual UI and privacy test (no network)
```

## Gate: done when you can show

```text
  [ ] deadline extraction accuracy
  [ ] summary faithfulness
  [ ] run time per page
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Not legal advice; always shows the original text next to the summary.

## Resume line (fill with your measured numbers)

> Built an offline bilingual letter explainer with [N]% deadline-extraction accuracy and zero data upload.

**Skills it proves:** OCR · RAG · local LLMs · privacy

## Masterpiece upgrade path

```text
   LEVEL [##...]  ====================>  LEVEL [#####]
```

Grounded navigator over official procedure catalogues with expert audit and multilingual user studies.

**Grows into:** [VERWALTUNG](93-verwaltung.md) · **Publication target:** E-government conference

## Defend it

1. How do you stop the model from inventing a deadline?
2. Why synthetic letters for testing?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/amtsdeutsch  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- ICEROAD](08-iceroad.md) · [atlas index](../README.md) · [VERITAS ->](10-veritas.md)
