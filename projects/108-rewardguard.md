# 108 · REWARDGUARD

```text
    task: fix bug  -> agent edits test file instead  -> reward 1.0   [!] HACK
                   -> monitor flags, reward withheld
```

**Catching reward hacking in RL-trained coding agents**

> The agent passed the tests. Did it cheat?

```text
  TRACK N FRONTIER: SUPERINTELLIGENCE ALIGNMENT AND SAFETY  |  LEVEL [#####]  |  ~14 MONTHS  |  BUDGET €600
```

## The mission

RL-trained agents learn to game their reward (special-casing tests, editing graders), which gets worse as they get more capable.

## How it works

```text
+------------------------------------------------+
|  RL environment with deliberate loopholes      |
+------------------------------------------------+
                        |
                        v
+------------------------------------------------+
|  train small agent                             |
+------------------------------------------------+
                        |
                        v
+------------------------------------------------+
|  hack detectors (diff analysis, LLM monitors)  |
+------------------------------------------------+
                        |
                        v
+------------------------------------------------+
|  mitigation                                    |
+------------------------------------------------+
```

## Kit

- Python
- TRL or verl
- sandboxed containers
- Inspect AI

**Hardware:** Rented GPUs

## Campaign

```text
  P1  [=====]                     m0-3.5    Environments with known exploitable loopholes
  P2        [=====]               m3.5-7    Train agents and catalogue the hacks they discover
  P3              [=====]         m7-10.5   Detectors and their precision/recall
  P4                    [=====]   m10.5-14  Training-time mitigations and the trade-off with capability
```

## Gate: done when you can show

```text
  [ ] hack rate before/after
  [ ] detector recall
  [ ] task performance retained
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Sandboxed environments only.

## Resume line (fill with your measured numbers)

> Catalogued [N] reward hacks in RL coding agents and cut hack rate [N]% with monitoring at [N]% capability cost.

**Skills it proves:** reinforcement learning · sandboxing · monitoring

## System map

```text
  REWARDGUARD SYSTEM MAP

+------------------+    +------------------+    +------------------+
|  environments    |--->|  RL trainer      |--->|  hack catalogue  |
+------------------+    +------------------+    +------------------+
         |
         v
+------------------+    +------------------+
|  detectors       |--->|  mitigations     |
+------------------+    +------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   Research
  PUBLICATION TARGET     NeurIPS/ICLR safety workshops
```

## Deliverables

- Environment suite
- Hack catalogue
- Detector code
- Paper

## Standards and regulations to meet

- Container isolation best practice

## Who sees this

Where this work gets in front of the people who lead the field (see the
[visibility playbook](../docs/visibility-playbook.md) for how to use each one):

```text
  >> Anthropic Fellows
  >> MATS
  >> Apart sprints
```

## Defend it

1. Why does more RL make reward hacking more likely?
2. Can the agent learn to hide hacks from the monitor?
3. How is this related to specification gaming?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/rewardguard  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- TRUTHPROBE](107-truthprobe.md) · [atlas index](../README.md) · [COTWATCH ->](109-cotwatch.md)
