# 102 · CONTROLROOM

```text
    [ untrusted strong model ] --code--> [ trusted weak monitor ] --0.92--> [ audit ]
               red team tries sneaky backdoors          blue team: catch them, keep usefulness
```

**AI control protocols for untrusted coding agents**

> Assume the smartest model might be scheming. Build the protocol that catches it anyway.

```text
  TRACK N FRONTIER: SUPERINTELLIGENCE ALIGNMENT AND SAFETY  |  LEVEL [#####]  |  ~12 MONTHS  |  BUDGET €500
```

## The mission

If a powerful model were misaligned, could a weaker trusted model plus limited human review still stop it from doing damage? That's the AI control agenda.

## How it works

```text
+-------------------------------+
|  agentic task environment     |
+-------------------------------+
               |
               v
+-------------------------------+
|  red-team attack policy       |
+-------------------------------+
               |
               v
+-------------------------------+
|  monitoring protocols         |
+-------------------------------+
               |
               v
+-------------------------------+
|  audit budget                 |
+-------------------------------+
               |
               v
+-------------------------------+
|  safety vs usefulness curves  |
+-------------------------------+
```

## Kit

- Python
- Inspect AI
- ControlArena-style settings
- open and API models

**Hardware:** API credits + one GPU for open models

## Campaign

```text
  P1  [=====]                     m0-3      Reproduce a baseline control result (trusted monitoring, defer-to-trusted)
  P2        [=====]               m3-6      Build a new setting relevant to your expertise (e.g. infrastructure-as-code or SOC tooling)
  P3              [=====]         m6-9      Design and red-team a new protocol
  P4                    [=====]   m9-12     Safety/usefulness Pareto curves and paper
```

## Gate: done when you can show

```text
  [ ] safety (attacks caught) at fixed audit budget
  [ ] usefulness retained
  [ ] monitor AUROC
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Red-team attacks stay inside sandboxed settings; no real-world exploits.

## Resume line (fill with your measured numbers)

> Designed an AI control protocol reaching [N]% safety at [N]% usefulness on a new agentic setting.

**Skills it proves:** AI control · red teaming · experimental design

## System map

```text
  CONTROLROOM SYSTEM MAP

+-------------------+    +-------------------+    +-------------------+
|  task setting     |--->|  attack policy    |--->|  monitor          |
+-------------------+    +-------------------+    +-------------------+
         |
         v
+-------------------+    +-------------------+
|  audit allocator  |--->|  evaluation       |
+-------------------+    +-------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   Research
  PUBLICATION TARGET     ControlConf, Alignment Forum, ICLR/NeurIPS safety workshops
```

## Deliverables

- New control setting (open source)
- Protocol code
- Pareto results
- Paper

## Standards and regulations to meet

- Sandboxing best practice

## Who sees this

Where this work gets in front of the people who lead the field (see the
[visibility playbook](../docs/visibility-playbook.md) for how to use each one):

```text
  >> Apart Research AI Control hackathons (co-run with Redwood Research)
  >> MATS
  >> Anthropic Fellows (AI control area)
  >> Redwood Research
```

## Defend it

1. Why assume the model is adversarial rather than measure whether it is?
2. What is an audit budget and why is it the binding constraint?
3. How could a scheming model evade your monitor?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/controlroom  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- GLASSBOX](101-glassbox.md) · [atlas index](../README.md) · [SANDBAG ->](103-sandbag.md)
