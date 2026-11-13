# 04 · BRIDGEKEEPER

```text
   ____________________________
  |____|____|____|____|____|___|   deck
       \\    /\/\/\/   //
        \\  crack!    //
  ~~~~~~~\\~~~~~~~~~~//~~~~~~~~
```

**Concrete crack inspection with an edge vision pipeline**

> Find the crack before the crack finds the truck.

```text
  TRACK A EDGE AI AND ROBOTICS  |  LEVEL [###..]  |  ~4 MONTHS  |  BUDGET €0–50
```

## The mission

Bridge inspections are manual and periodic; small cracks are missed between visits.

## How it works

```text
+----------------------------------------+
|  camera on handheld pole or sim drone  |
+----------------------------------------+
                    |
                    v
+----------------------------------------+
|  segmentation model                    |
+----------------------------------------+
                    |
                    v
+----------------------------------------+
|  crack width estimate                  |
+----------------------------------------+
                    |
                    v
+----------------------------------------+
|  inspection report PDF                 |
+----------------------------------------+
```

## Kit

- PyTorch
- U-Net
- ONNX Runtime
- Gazebo
- ReportLab

**Hardware:** Laptop + phone camera; drone only in simulation

## Campaign

```text
  P1  [=====]                     m0-1      Public crack datasets (e.g. SDNET2018) and data card
  P2        [=====]               m1-2      Segmentation model with width estimation
  P3              [=====]         m2-3      Edge runtime on a small device
  P4                    [=====]   m3-4      Generate an inspection report in a standard layout
```

## Gate: done when you can show

```text
  [ ] IoU on crack pixels
  [ ] width error in mm
  [ ] report generation time
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Advisory tool; engineers sign inspections.

## Resume line (fill with your measured numbers)

> Built crack segmentation (IoU [N]) with mm-level width estimation and automated inspection reports.

**Skills it proves:** segmentation · metrology · reporting

## Defend it

1. How do you convert pixels to millimetres?
2. What does a missed crack cost compared to a false one?

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/bridgekeeper  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- FORESTER](03-forester.md) · [atlas index](../README.md) · [VINEGUARD ->](05-vineguard.md)
