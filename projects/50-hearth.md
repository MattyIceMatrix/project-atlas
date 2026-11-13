# 50 · HEARTH

```text
      _____
     /     \      outside 2 C   price 0.31 EUR/kWh
    |  20C  |     plan: pre-heat 05:00, coast 08:00-16:00
    |_[_]___|     saving vs schedule: -14%
```

**Home energy digital twin with reinforcement learning**

> Your house, simulated, learning to heat itself for less.

```text
  TRACK H FRONTIER AND RESEARCH  |  LEVEL [####.]  |  ~4 MONTHS  |  BUDGET €40
```

## The mission

Heating schedules ignore weather forecasts, prices and how the house actually holds heat.

## How it works

```text
+--------------------------------+
|  smart meter + room sensors    |
+--------------------------------+
                |
                v
+--------------------------------+
|  thermal model (digital twin)  |
+--------------------------------+
                |
                v
+--------------------------------+
|  RL or MPC policy in sim       |
+--------------------------------+
                |
                v
+--------------------------------+
|  advisory schedule             |
+--------------------------------+
```

## Kit

- Python
- EnergyPlus or simple RC model
- Stable-Baselines3
- Home Assistant

**Hardware:** Room sensors you may already have

## Campaign

```text
  P1  [=====]                     m0-1      Data logging and a calibrated thermal model
  P2        [=====]               m1-2      Baseline schedule and MPC controller
  P3              [=====]         m2-3      RL policy trained in the twin
  P4                    [=====]   m3-4      Advisory mode only, compare predicted vs real
```

## Gate: done when you can show

```text
  [ ] model temperature error
  [ ] simulated cost saving
  [ ] comfort violations
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Advisory mode; never controls heating without the household's agreement.

## Resume line (fill with your measured numbers)

> Built a calibrated home thermal twin; RL policy cut simulated heating cost [N]% with no comfort violations.

**Skills it proves:** reinforcement learning · control · energy systems

## Masterpiece upgrade path

```text
   LEVEL [####.]  ====================>  LEVEL [#####]
```

Scale from one home to a neighbourhood energy twin coordinated with the municipal grid model.

**Grows into:** [GRIDBRAIN](82-gridbrain.md), [CITYTWIN](100-citytwin.md) · **Publication target:** Energy informatics conference

## Defend it

1. Why test in a twin before the real house?
2. When is MPC better than RL?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/hearth  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- SWARM](49-swarm.md) · [atlas index](../README.md) · [SEAWALL ->](51-seawall.md)
