# 02 · HIVEMIND

```text
     _  _  _
    / \/ \/ \      )))  buzz spectrum
   | HIVE  |  -->  )))  -> "queenless?" 0.82
    \_/\_/\_/      )))
```

**Beehive health monitor with on-device audio AI**

> Listen to the hive; hear trouble before you see it.

```text
  TRACK A EDGE AI AND ROBOTICS  |  LEVEL [##...]  |  ~3 MONTHS  |  BUDGET €120
```

## The mission

Beekeepers lose colonies to swarming and queen loss that show up in the hive's sound days earlier.

## How it works

```text
+-----------------------------------+
|  MEMS microphone + temp/humidity  |
+-----------------------------------+
                 |
                 v
+-----------------------------------+
|  spectrogram                      |
+-----------------------------------+
                 |
                 v
+-----------------------------------+
|  tiny CNN on device               |
+-----------------------------------+
                 |
                 v
+-----------------------------------+
|  weekly hive report               |
+-----------------------------------+
```

## Kit

- Arduino Nano 33 BLE Sense
- Edge Impulse
- Python
- SQLite

**Hardware:** 1 sensor board per hive

## Campaign

```text
  P1  [=====]                     m0-0.8    Record hive audio and label with a local beekeeper
  P2        [=====]               m0.8-1.5  Build spectrogram features and a baseline model
  P3              [=====]         m1.5-2.2  Quantise and run on the board
  P4                    [=====]   m2.2-3    Season-long monitoring report
```

## Gate: done when you can show

```text
  [ ] queen-loss detection recall
  [ ] days of early warning
  [ ] battery life
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Partner with a beekeeper; no hive disturbance beyond normal inspection.

## Resume line (fill with your measured numbers)

> Built an on-device audio classifier detecting hive anomalies with [N]% recall, [N] days before visual signs.

**Skills it proves:** audio ML · quantisation · embedded deployment

## Defend it

1. Why spectrograms and not raw audio?
2. How did you get labels you can trust?

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/hivemind  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- TIDEWATCH](01-tidewatch.md) · [atlas index](../README.md) · [FORESTER ->](03-forester.md)
