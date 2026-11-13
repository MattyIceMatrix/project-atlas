# 48 · QUANTUMSAFE

```text
    [ RSA / ECDH ]  ==migrate==>  [ ML-KEM + ML-DSA ]
        2048 bit                     FIPS 203 / 204
    handshake: 3.1 ms  ->  4.7 ms  (on ESP32-S3)
```

**Post-quantum crypto migration for IoT**

> Swap the locks before the quantum locksmith arrives.

```text
  TRACK H FRONTIER AND RESEARCH  |  LEVEL [####.]  |  ~3 MONTHS  |  BUDGET €30
```

## The mission

Long-lived devices use crypto that future quantum computers could break; migration is hard on small chips.

## How it works

```text
+----------------------------------+
|  crypto inventory                |
+----------------------------------+
                 |
                 v
+----------------------------------+
|  hybrid TLS with PQC             |
+----------------------------------+
                 |
                 v
+----------------------------------+
|  benchmarks on microcontrollers  |
+----------------------------------+
                 |
                 v
+----------------------------------+
|  migration playbook              |
+----------------------------------+
```

## Kit

- liboqs
- mbedTLS or wolfSSL
- ESP32-S3
- Python

**Hardware:** 2 microcontrollers

## Campaign

```text
  P1  [=====]                     m0-0.8    Crypto inventory of your own projects
  P2        [=====]               m0.8-1.5  Hybrid key exchange working on a microcontroller
  P3              [=====]         m1.5-2.2  Benchmarks (time, memory, code size, energy)
  P4                    [=====]   m2.2-3    Migration playbook
```

## Gate: done when you can show

```text
  [ ] handshake time
  [ ] RAM and flash use
  [ ] energy per handshake
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

None special.

## Resume line (fill with your measured numbers)

> Ran hybrid post-quantum TLS on ESP32 (ML-KEM), adding [N] ms per handshake; wrote a migration playbook.

**Skills it proves:** cryptography · embedded · standards

## Masterpiece upgrade path

```text
   LEVEL [####.]  ====================>  LEVEL [#####]
```

PQC migration across a secure-boot edge fleet with signed OTA updates.

**Grows into:** [EDGEOS](53-edgeos.md) · **Publication target:** Embedded security or PQC workshop

## Defend it

1. What is "harvest now, decrypt later"?
2. Why hybrid instead of PQC only?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/quantumsafe  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- NEUROSPARK](47-neurospark.md) · [atlas index](../README.md) · [SWARM ->](49-swarm.md)
