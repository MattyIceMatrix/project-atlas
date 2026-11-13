# 45 · RECEIPTLENS

```text
    .-----------.
    | MILCH 1.09|  ===>  milk  ^ +8% since June
    | BROT  1.79|  ===>  bread = steady
    '-----------'
```

**Grocery receipt scanner and price tracker**

> Photograph the receipt, watch your prices over time.

```text
  TRACK G PEOPLE, SPORT AND COMMUNITY  |  LEVEL [#....]  |  ~2 MONTHS  |  BUDGET €0
```

## The mission

Households don't see how their grocery prices and habits change.

## How it works

```text
+-------------------------+
|  photo                  |
+-------------------------+
            |
            v
+-------------------------+
|  OCR                    |
+-------------------------+
            |
            v
+-------------------------+
|  line parsing           |
+-------------------------+
            |
            v
+-------------------------+
|  product normalisation  |
+-------------------------+
            |
            v
+-------------------------+
|  monthly trends         |
+-------------------------+
```

## Kit

- PaddleOCR
- Python
- SQLite
- Streamlit

**Hardware:** Phone

## Campaign

```text
  P1  [=====]                     m0-0.5    OCR and line parsing for two store layouts
  P2        [=====]               m0.5-1    Product name normalisation
  P3              [=====]         m1-1.5    Trends and budget view
  P4                    [=====]   m1.5-2    Accuracy check on 100 receipts
```

## Gate: done when you can show

```text
  [ ] line parsing accuracy
  [ ] normalisation accuracy
  [ ] time per receipt
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Data stays on the user's device.

## Resume line (fill with your measured numbers)

> Built receipt OCR with [N]% line accuracy and product-level price trends.

**Skills it proves:** OCR · data cleaning · personal finance tooling

## Defend it

1. Why is normalising product names harder than OCR?
2. How would you add a new store's layout?

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/receiptlens  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- CLIMB-TRANSITION](44-climb-transition.md) · [atlas index](../README.md) · [SPRECHEN ->](46-sprechen.md)
