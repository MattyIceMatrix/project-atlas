# 25 · SBOM-RADAR

```text
    repo-a  [|||||||||.] 2 high
    repo-b  [|||.......] 7 high   <-- log4j-like? click
    repo-c  [||||||||||] clean
```

**Software supply-chain risk dashboard**

> Every dependency, every CVE, every repo, one screen.

```text
  TRACK D CYBER DEFENSE  |  LEVEL [##...]  |  ~2 MONTHS  |  BUDGET €0
```

## The mission

Teams don't know which of their repos are affected by a new vulnerability.

## How it works

```text
+--------------------------+
|  repos                   |
+--------------------------+
             |
             v
+--------------------------+
|  SBOM generation         |
+--------------------------+
             |
             v
+--------------------------+
|  vulnerability DB match  |
+--------------------------+
             |
             v
+--------------------------+
|  risk score              |
+--------------------------+
             |
             v
+--------------------------+
|  dashboard + alerts      |
+--------------------------+
```

## Kit

- Syft
- Grype or OSV
- Python
- Postgres
- Grafana

**Hardware:** None

## Campaign

```text
  P1  [=====]                     m0-0.5    SBOMs for all your repos in CI
  P2        [=====]               m0.5-1    OSV matching and reachability hints
  P3              [=====]         m1-1.5    Risk scoring and dashboard
  P4                    [=====]   m1.5-2    Alert flow to GitHub issues
```

## Gate: done when you can show

```text
  [ ] time from CVE publish to alert
  [ ] false positive rate
  [ ] repos covered
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

None special.

## Resume line (fill with your measured numbers)

> Built an SBOM-based dashboard alerting on new CVEs across [N] repos within [N] hours.

**Skills it proves:** supply-chain security · DevSecOps

## Masterpiece upgrade path

```text
   LEVEL [##...]  ====================>  LEVEL [#####]
```

Extend from software SBOMs to signed, provenance-tracked ML models with admission control.

**Grows into:** [MODELCHAIN](75-modelchain.md) · **Publication target:** OpenSSF talk

## Defend it

1. Why is "vulnerable dependency present" not the same as "exploitable"?
2. {'CycloneDX vs SPDX': 'why pick one?'}

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/sbom-radar  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- PHISHNET](24-phishnet.md) · [atlas index](../README.md) · [ZEROTRUST-LAB ->](26-zerotrust-lab.md)
