# 24 · PHISHNET

```text
    From: paypa1-support@...      [!] look-alike domain
    "Urgent: account locked"      [!] urgency language
    link -> bit.ly/xyz            [!] hidden destination
                                   ==> PHISHING 0.94
```

**Explainable phishing classifier**

> Not just "phishing", but why.

```text
  TRACK D CYBER DEFENSE  |  LEVEL [##...]  |  ~3 MONTHS  |  BUDGET €0
```

## The mission

Users don't trust a red banner they don't understand.

## How it works

```text
+--------------------------------+
|  email                         |
+--------------------------------+
                |
                v
+--------------------------------+
|  header + URL + text features  |
+--------------------------------+
                |
                v
+--------------------------------+
|  model                         |
+--------------------------------+
                |
                v
+--------------------------------+
|  top reasons                   |
+--------------------------------+
                |
                v
+--------------------------------+
|  client add-in                 |
+--------------------------------+
```

## Kit

- Python
- scikit-learn or small transformer
- SHAP
- Outlook or Thunderbird add-in

**Hardware:** None

## Campaign

```text
  P1  [=====]                     m0-0.8    Public phishing and ham corpora; data card
  P2        [=====]               m0.8-1.5  Interpretable model with reason codes
  P3              [=====]         m1.5-2.2  Mail client add-in
  P4                    [=====]   m2.2-3    {'User study': 'does the explanation change decisions?'}
```

## Gate: done when you can show

```text
  [ ] precision/recall
  [ ] explanation usefulness rating
  [ ] inference time
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Defensive; trained on public corpora only.

## Resume line (fill with your measured numbers)

> Built an explainable phishing detector (F1 [N]) whose reason codes improved user decisions by [N]%.

**Skills it proves:** ML · explainability · email security

## Defend it

1. Why might accuracy drop next year?
2. How do you evaluate an explanation?

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/phishnet  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- HONEYCOMB](23-honeycomb.md) · [atlas index](../README.md) · [SBOM-RADAR ->](25-sbom-radar.md)
