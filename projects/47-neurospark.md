# 47 · NEUROSPARK

```text
    spikes:  |  | |    |      |||| |  |      (events, not frames)
    neuron:  ___/\_____/\__/\____/\/\/\___
    power:   0.3 mW  vs  CNN 45 mW
```

**Spiking neural networks for ultra-low-power sensing**

> Compute only when something happens.

```text
  TRACK H FRONTIER AND RESEARCH  |  LEVEL [####.]  |  ~3 MONTHS  |  BUDGET €0
```

## The mission

Always-on sensors waste power processing nothing.

## How it works

```text
+-----------------------------------------+
|  event data (or converted audio)        |
+-----------------------------------------+
                    |
                    v
+-----------------------------------------+
|  SNN training with surrogate gradients  |
+-----------------------------------------+
                    |
                    v
+-----------------------------------------+
|  energy estimate                        |
+-----------------------------------------+
                    |
                    v
+-----------------------------------------+
|  compare to CNN                         |
+-----------------------------------------+
```

## Kit

- snnTorch or Norse
- PyTorch
- public event-camera or keyword datasets

**Hardware:** Laptop

## Campaign

```text
  P1  [=====]                     m0-0.8    Literature review and a reproducible baseline
  P2        [=====]               m0.8-1.5  Train an SNN on keyword spotting
  P3              [=====]         m1.5-2.2  Energy estimate methodology
  P4                    [=====]   m2.2-3    Honest comparison to a tiny CNN
```

## Gate: done when you can show

```text
  [ ] accuracy
  [ ] estimated energy per inference
  [ ] spike sparsity
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

None special.

## Resume line (fill with your measured numbers)

> Trained an SNN keyword spotter at [N]% accuracy with an estimated [N]x energy saving over a CNN.

**Skills it proves:** neuromorphic computing · research methods

## Defend it

1. Why can't you backprop through a spike directly?
2. How trustworthy is an energy estimate without neuromorphic hardware?

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/neurospark  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- SPRECHEN](46-sprechen.md) · [atlas index](../README.md) · [QUANTUMSAFE ->](48-quantumsafe.md)
