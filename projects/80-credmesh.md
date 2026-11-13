# 80 · CREDMESH

```text
    [ wallet: "Swiftwater Ops, THW, valid 2027" ] --QR--> [ checker (offline) ] --> VALID
            signed by issuer                           revocation list cached
```

**Verifiable credentials for responders at disaster sites**

> Prove you're a certified boat operator, offline, in ten seconds.

```text
  TRACK K MASTERPIECE: TRUST, SECURITY AND SOVEREIGNTY  |  LEVEL [#####]  |  ~12 MONTHS  |  BUDGET €0
```

## The mission

Spontaneous helpers and teams from other regions can't prove qualifications at a chaotic site.

## How it works

```text
+---------------------------+
|  issuer signs credential  |
+---------------------------+
             |
             v
+---------------------------+
|  holder wallet            |
+---------------------------+
             |
             v
+---------------------------+
|  offline verification     |
+---------------------------+
             |
             v
+---------------------------+
|  cached revocation        |
+---------------------------+
             |
             v
+---------------------------+
|  audit                    |
+---------------------------+
```

## Kit

- W3C Verifiable Credentials
- OpenID4VC
- Rust or TypeScript
- mobile wallet

**Hardware:** Phones

## Campaign

```text
  P1  [=====]                     m0-3      Credential schema with a rescue organisation's input
  P2        [=====]               m3-6      Issuer and wallet
  P3              [=====]         m6-9      Offline verifier with revocation caching
  P4                    [=====]   m9-12     Field exercise with LANTERN and MESHLIFE
```

## Gate: done when you can show

```text
  [ ] verification time offline
  [ ] revocation freshness
  [ ] user errors in the exercise
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Minimal data in credentials; holder controls disclosure.

## Resume line (fill with your measured numbers)

> Built offline-verifiable responder credentials (W3C VC) verifying in [N] s with cached revocation.

**Skills it proves:** digital identity · cryptography · mobile

## System map

```text
  CREDMESH SYSTEM MAP

+--------------------+    +--------------------+    +--------------------+
|  issuer            |--->|  schema registry   |--->|  wallet            |
+--------------------+    +--------------------+    +--------------------+
          |
          v
+--------------------+    +--------------------+
|  verifier          |--->|  revocation cache  |
+--------------------+    +--------------------+
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   TRL 3 -> 5
  PUBLICATION TARGET     Identity conference or ISCRAM
```

## Deliverables

- Issuer/verifier apps
- Schema
- Exercise report
- Security analysis

## Standards and regulations to meet

- W3C VC Data Model 2.0
- OpenID4VC
- eIDAS 2.0 / EUDI wallet concepts

## Defend it

1. Why selective disclosure matters here?
2. How does revocation work offline?
3. What happens if a phone is stolen?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/credmesh  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- OTSENTINEL](79-otsentinel.md) · [atlas index](../README.md) · [FLOODTWIN ->](81-floodtwin.md)
