# 11 · SKILLBRIDGE-COPILOT

```text
    [ MOS / duties ]  ===>  [ O*NET skills ]  ===>  [ resume bullets ]
        ___                    ___                     ___
       |>> |                  |{ }|                   |---|
       |___|                  |___|                   |___|
```

**Military-to-civilian skills translator**

> From MOS to job post, in words a recruiter understands.

```text
  TRACK B GENERATIVE AI AND LLM SYSTEMS  |  LEVEL [##...]  |  ~3 MONTHS  |  BUDGET €0
```

## The mission

Veterans undersell real skills because military language doesn't map cleanly to civilian job descriptions.

## How it works

```text
+---------------------------------------+
|  duty text                            |
+---------------------------------------+
                   |
                   v
+---------------------------------------+
|  skill extraction                     |
+---------------------------------------+
                   |
                   v
+---------------------------------------+
|  O*NET occupation matching            |
+---------------------------------------+
                   |
                   v
+---------------------------------------+
|  bullet drafts with evidence prompts  |
+---------------------------------------+
```

## Kit

- O*NET open data
- embeddings
- small LLM
- FastAPI
- React

**Hardware:** Laptop

## Campaign

```text
  P1  [=====]                     m0-0.8    Load O*NET and public MOS crosswalk data
  P2        [=====]               m0.8-1.5  Skill extraction and matching with evaluation set
  P3              [=====]         m1.5-2.2  Bullet drafting that asks the user for real numbers
  P4                    [=====]   m2.2-3    Usability test with 5 veterans
```

## Gate: done when you can show

```text
  [ ] match precision@5
  [ ] user rating
  [ ] time to first resume draft
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Never invents achievements; the user supplies the facts.

## Resume line (fill with your measured numbers)

> Built a veteran skills translator matching duties to O*NET occupations at precision@5 of [N].

**Skills it proves:** NLP · matching · product design

## Masterpiece upgrade path

```text
   LEVEL [##...]  ====================>  LEVEL [#####]
```

Partner with a veteran-service organisation, validate matching on real (consented) transitions and publish outcome data.

**Grows into:** [QUESTLINE](98-questline.md) · **Publication target:** Workforce or HR-tech conference

## Defend it

1. How do you stop it from inflating a resume?
2. How did you evaluate the matching?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/skillbridge-copilot  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- VERITAS](10-veritas.md) · [atlas index](../README.md) · [LOOM ->](12-loom.md)
