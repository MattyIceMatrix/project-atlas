# 20 · FAIRLINE

```text
    group A  [##########] 0.81
    group B  [#######...] 0.64   <-- gap 0.17 > threshold 0.05
    group C  [#########.] 0.78
```

**Bias audit toolkit for tabular models**

> Same model, every group, side by side.

```text
  TRACK C AI SAFETY AND GOVERNANCE  |  LEVEL [##...]  |  ~2 MONTHS  |  BUDGET €0
```

## The mission

Models for credit, hiring or services can treat groups differently without anyone noticing.

## How it works

```text
+----------------------------------+
|  model + dataset                 |
+----------------------------------+
                 |
                 v
+----------------------------------+
|  sliced metrics                  |
+----------------------------------+
                 |
                 v
+----------------------------------+
|  fairness criteria               |
+----------------------------------+
                 |
                 v
+----------------------------------+
|  report with mitigation options  |
+----------------------------------+
```

## Kit

- Python
- Fairlearn
- scikit-learn
- Jupyter
- HTML report

**Hardware:** None

## Campaign

```text
  P1  [=====]                     m0-0.5    Public benchmark datasets and their known issues
  P2        [=====]               m0.5-1    Sliced metrics and confidence intervals
  P3              [=====]         m1-1.5    Mitigation experiments and trade-offs
  P4                    [=====]   m1.5-2    Report template for non-technical readers
```

## Gate: done when you can show

```text
  [ ] metric gaps with CIs
  [ ] accuracy cost of mitigation
  [ ] report readability
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Explains trade-offs; does not declare a model "fair".

## Resume line (fill with your measured numbers)

> Built a bias audit toolkit with CI-backed group metrics; mitigation cut the gap from [N] to [N].

**Skills it proves:** responsible AI · statistics · communication

## Defend it

1. Why can't all fairness criteria be met at once?
2. Why confidence intervals?

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/fairline  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- CHARTER](19-charter.md) · [atlas index](../README.md) · [SANDBOX ->](21-sandbox.md)
