# 19 · CHARTER

```text
     repo + model cards + test results
                 |
           [ C H A R T E R ]
                 |
     technical file draft  +  gaps checklist  (red = missing)
```

**AI Act documentation generator**

> From repo to technical documentation file, half-written for you.

```text
  TRACK C AI SAFETY AND GOVERNANCE  |  LEVEL [##...]  |  ~2 MONTHS  |  BUDGET €0
```

## The mission

Teams building AI systems in the EU must keep technical documentation and risk records; it is usually written last and badly.

## How it works

```text
+---------------------------------+
|  scan repo artefacts            |
+---------------------------------+
                |
                v
+---------------------------------+
|  map to documentation headings  |
+---------------------------------+
                |
                v
+---------------------------------+
|  draft + gap list               |
+---------------------------------+
                |
                v
+---------------------------------+
|  human edits                    |
+---------------------------------+
```

## Kit

- Python
- Markdown/Docs export
- YAML templates

**Hardware:** None

## Campaign

```text
  P1  [=====]                     m0-0.5    Template derived from the regulation's documentation requirements (cite articles)
  P2        [=====]               m0.5-1    Extractors for model cards, data cards, test results
  P3              [=====]         m1-1.5    Gap checklist
  P4                    [=====]   m1.5-2    Run it on LANTERN
```

## Gate: done when you can show

```text
  [ ] sections auto-filled
  [ ] gaps found vs manual review
  [ ] time saved
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Output is a draft for qualified review, not a compliance certificate.

## Resume line (fill with your measured numbers)

> Built a documentation generator that drafts [N]% of an AI technical file from repo artefacts.

**Skills it proves:** regulation · documentation · tooling

## Defend it

1. Why can't a tool make a system compliant?
2. How do you keep templates current when guidance changes?

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/charter  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- REDCELL](18-redcell.md) · [atlas index](../README.md) · [FAIRLINE ->](20-fairline.md)
