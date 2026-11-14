# 26 · ZEROTRUST-LAB

```text
    user --> [ identity proxy ] --> app A   (allowed: group=ops)
                   |
                   +--X--> app B   (denied: device not compliant)
```

**Zero-trust access lab**

> No VPN. Every request proves who it is.

```text
  TRACK D CYBER DEFENSE  |  LEVEL [###..]  |  ~2 MONTHS  |  BUDGET €0
```

## The mission

Flat networks and VPNs give too much access once inside.

## How it works

```text
+------------------------+
|  IdP (OIDC)            |
+------------------------+
            |
            v
+------------------------+
|  identity-aware proxy  |
+------------------------+
            |
            v
+------------------------+
|  per-app policy        |
+------------------------+
            |
            v
+------------------------+
|  device posture        |
+------------------------+
            |
            v
+------------------------+
|  logs                  |
+------------------------+
```

## Kit

- Keycloak
- Pomerium or oauth2-proxy
- Proxmox
- Terraform

**Hardware:** Home lab

## Campaign

```text
  P1  [=====]                     m0-0.5    Identity provider with MFA
  P2        [=====]               m0.5-1    Proxy with per-app policies
  P3              [=====]         m1-1.5    Device posture checks
  P4                    [=====]   m1.5-2    Attack walk-through: stolen password, stolen session
```

## Gate: done when you can show

```text
  [ ] apps behind proxy
  [ ] blocked policy violations
  [ ] login latency
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Lab environment.

## Resume line (fill with your measured numbers)

> Built a zero-trust access lab (OIDC, identity-aware proxy, device posture) replacing VPN access.

**Skills it proves:** identity · zero trust · IaC

## Masterpiece upgrade path

```text
   LEVEL [###..]  ====================>  LEVEL [#####]
```

Grow into an EU sovereign platform with zero-trust identity and verifiable credentials.

**Grows into:** [SOVEREIGN](71-sovereign.md), [CREDMESH](80-credmesh.md) · **Publication target:** Identity or cloud-native conference

## Defend it

1. What does "never trust, always verify" mean in practice here?
2. What attack is still possible?

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/zerotrust-lab  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- SBOM-RADAR](25-sbom-radar.md) · [atlas index](../README.md) · [LOGLENS ->](27-loglens.md)
