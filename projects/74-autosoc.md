# 74 · AUTOSOC

```text
    alerts --> [ triage agent ] --> [ investigation agent ] --> [ response plan ]
                                                                   |
                                               analyst: APPROVE / DENY --> SOAR action
```

**Human-gated autonomous security operations centre**

> Agents investigate, humans decide, everything is logged.

```text
  TRACK K MASTERPIECE: TRUST, SECURITY AND SOVEREIGNTY  |  LEVEL [#####]  |  ~16 MONTHS  |  BUDGET €0
```

## The mission

Security teams can't keep up with alerts; fully autonomous response is dangerous.

## How it works

```text
+---------------------------------+
|  SIEM                           |
+---------------------------------+
                |
                v
+---------------------------------+
|  detection rules                |
+---------------------------------+
                |
                v
+---------------------------------+
|  triage + investigation agents  |
+---------------------------------+
                |
                v
+---------------------------------+
|  response plans                 |
+---------------------------------+
                |
                v
+---------------------------------+
|  human approval                 |
+---------------------------------+
                |
                v
+---------------------------------+
|  SOAR                           |
+---------------------------------+
```

## Kit

- Wazuh or Elastic
- Sigma
- Shuffle SOAR
- agent runtime (AGENTGRID)
- LEDGER

**Hardware:** Home lab with attack simulation VMs

## Campaign

```text
  P1  [=====]                     m0-4      Detection engineering with purple-team test cases (Atomic Red Team)
  P2        [=====]               m4-8      Investigation agent with evidence requirements
  P3              [=====]         m8-12     Approval-gated response playbooks
  P4                    [=====]   m12-16    Measured comparison with manual SOC workflow
```

## Gate: done when you can show

```text
  [ ] mean time to detect
  [ ] mean time to respond
  [ ] analyst agreement
  [ ] unsafe actions (target 0)
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Lab environment; defensive only.

## Resume line (fill with your measured numbers)

> Built a human-gated AI SOC cutting MTTR [N]% on purple-team scenarios with zero unapproved actions.

**Skills it proves:** detection engineering · SOAR · AI agents

## System map

```text
  AUTOSOC SYSTEM MAP

+-------------------+    +-------------------+    +-------------------+
|  SIEM             |--->|  detection rules  |--->|  agents           |
+-------------------+    +-------------------+    +-------------------+
         |
         v
+-------------------+    +-------------------+
|  approval gate    |--->|  SOAR             |
+-------------------+    +-------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   TRL 4 -> 5
  PUBLICATION TARGET     BSides talk or SANS-style paper
```

## Deliverables

- Lab build
- Detection rule pack
- Playbooks
- Evaluation report

## Standards and regulations to meet

- MITRE ATT&CK
- NIST SP 800-61 incident handling
- Sigma

## Defend it

1. Why must containment actions need approval?
2. How do you stop attackers from poisoning the agent via logs?
3. Which MITRE ATT&CK techniques do you cover?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/autosoc  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- ZKAUDIT](73-zkaudit.md) · [atlas index](../README.md) · [MODELCHAIN ->](75-modelchain.md)
