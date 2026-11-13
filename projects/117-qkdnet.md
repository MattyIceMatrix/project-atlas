# 117 · QKDNET

```text
    [Alice]==fibre 40 km==[trusted node]==fibre 60 km==[Bob]
       key rate: 1.2 kbps     QBER 2.1%     eavesdropper detected: YES
```

**Quantum key distribution network simulator for critical communications**

> How would a quantum-secured responder network behave under attack?

```text
  TRACK O FRONTIER: QUANTUM COMPUTING AND QUANTUM AI  |  LEVEL [#####]  |  ~12 MONTHS  |  BUDGET €0
```

## The mission

Governments are investing in quantum communication infrastructure; engineers who can model it, and its limits, are rare.

## How it works

```text
+--------------------------------------+
|  network simulator                   |
+--------------------------------------+
                   |
                   v
+--------------------------------------+
|  QKD protocols (BB84, decoy states)  |
+--------------------------------------+
                   |
                   v
+--------------------------------------+
|  attacks and noise                   |
+--------------------------------------+
                   |
                   v
+--------------------------------------+
|  key rates                           |
+--------------------------------------+
                   |
                   v
+--------------------------------------+
|  comparison with PQC                 |
+--------------------------------------+
```

## Kit

- SeQUeNCe or NetSquid
- Python
- liboqs for PQC comparison

**Hardware:** Laptop

## Campaign

```text
  P1  [=====]                     m0-3      Protocol simulation and validation against published rates
  P2        [=====]               m3-6      Network topologies with trusted nodes
  P3              [=====]         m6-9      Attack scenarios and detection
  P4                    [=====]   m9-12     {'Policy paper': 'where QKD vs post-quantum crypto makes sense'}
```

## Gate: done when you can show

```text
  [ ] secret key rate vs distance
  [ ] QBER under attacks
  [ ] cost comparison with PQC
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

None special.

## Resume line (fill with your measured numbers)

> Simulated QKD networks and attacks, and published a QKD vs PQC trade-off analysis for critical communications.

**Skills it proves:** quantum networking · cryptography · policy

## System map

```text
  QKDNET SYSTEM MAP

+-------------------+    +-------------------+    +-------------------+
|  simulator        |--->|  protocols        |--->|  topologies       |
+-------------------+    +-------------------+    +-------------------+
         |
         v
+-------------------+    +-------------------+
|  attack lab       |--->|  policy analysis  |
+-------------------+    +-------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   Research
  PUBLICATION TARGET     QCrypt or security policy outlets
```

## Deliverables

- Simulator configs
- Results
- Policy paper

## Standards and regulations to meet

- ETSI QKD specifications (reference)
- NIST PQC standards FIPS 203/204/205

## Who sees this

Where this work gets in front of the people who lead the field (see the
[visibility playbook](../docs/visibility-playbook.md) for how to use each one):

```text
  >> EuroQCI-related research community
  >> quantum networking workshops
  >> security policy groups
```

## Defend it

1. What does QKD protect that PQC doesn't, and vice versa?
2. Why are trusted nodes a weakness?
3. What does QBER tell you?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/qkdnet  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- QCOMPILE](116-qcompile.md) · [atlas index](../README.md) · [QSIMGPU ->](118-qsimgpu.md)
