# NATIONSTACK: Sovereign AI for 100 Million People

```text
     _   _    _  _____ ___ ___  _  _ ___ _____ _   ___ _  __
    | \ | |  /_\|_   _|_ _/ _ \| \| / __|_   _/_\ / __| |/ /
    |  \| | / _ \ | |  | | (_) | .` \__ \ | |/ _ \ (__| ' <
    |_|\_|/_/ \_\|_| |___\___/|_|\_|___/ |_/_/ \_\___|_|\_\

         one country  *  100,000,000 people  *  10 pillars  *  every atlas project in its place
```

The grand master project of the atlas. It is designed the way a national programme would be: a blueprint,
a working reference stack, a capacity model, and a governance package. **One person can't build a
national AI system, and this doesn't pretend to.** What one person *can* do is produce the open,
engineering-grade blueprint and working miniature that decision-makers and engineers can study, challenge and use.

Brief: [projects/121-nationstack.md](../../projects/121-nationstack.md) · Capacity model: [capacity.md](capacity.md)

## The ten pillars

```text
   +------------------------------------------------------------------------------------+
   |  10  TALENT & INDUSTRY    fellowships, open source, startups, public-sector skills  |
   |   9  GOVERNANCE & LAW     AI Act, NIS2, Data Act, oversight board, audits           |
   |   8  CYBER DEFENCE        national SOC, OT security, supply chain (SLSA)            |
   |   7  SAFETY & EVALS       national eval suite, red teams, incident reporting        |
   |   6  IDENTITY & TRUST     EUDI-style wallet, verifiable credentials, consent         |
   |   5  PUBLIC AI SERVICES   citizen navigator, health/edu/justice copilots, crisis AI  |
   |   4  NATIONAL MODELS      national-language foundation + small edge models          |
   |   3  DATA SPACES          federated, consent-based, privacy-preserving data sharing  |
   |   2  ENERGY & SITING      clean firm power, heat reuse, 3 regions                    |
   |   1  SOVEREIGN COMPUTE    3 AI factories + edge kits, open stack, no single vendor   |
   +------------------------------------------------------------------------------------+
```

## Where every atlas project fits

```text
   PILLAR                 ATLAS PROJECTS THAT BUILD IT
   1 sovereign compute    HOMECLUSTER(70)  EDGEOS(53)  INFERNO(63)  MINICOMPILER(64)  SPOTFLEET(35)
   2 energy & siting      GRIDBRAIN(82)  HEARTH(50)  ROOFTOP(37)  COLDSTART(32)
   3 data spaces          FEDERATE(68)  DPVAULT(76)  DATACOMPASS(34)  RIVERFLOW(30)  FEATUREFORGE(31)
   4 national models      TINYFOUNDRY(61)  LOOM(12)  EDGEBENCH(67)  AERIALVLM(62)  SYNTHSCENE(69)
   5 public AI services   VERWALTUNG(93)  AMTSDEUTSCH(9)  BABEL(95)  WAYFINDER(96)  HELPERHUB(99)  CITYTWIN(100)
   6 identity & trust     CREDMESH(80)  PROVENANCE(77)  ENCLAVE(72)
   7 safety & evals       EVALSMITH(106)  CONTROLROOM(102)  SANDBAG(103)  GLASSBOX(101)  COTWATCH(109)
   8 cyber defence        AUTOSOC(74)  OTSENTINEL(79)  MODELCHAIN(75)  SBOM-RADAR(25)  QKDNET(117)
   9 governance & law     SOVEREIGN(71)  CHARTER(19)  ZKAUDIT(73)  COMPUTEWATCH(110)  PROVENGUARD(78)
  10 talent & industry    QUESTLINE(98)  SKILLBRIDGE-COPILOT(11)  COMMANDSIM(92)
   crisis resilience      LANTERN  FLOODTWIN(81)  MESHLIFE(60)  HEATSHIELD(84)
   quantum readiness      QREADY(120)  QDECODER(111)  QUANTUMSAFE(48)
```

## Reference architecture

```text
                    citizens / businesses / public institutions
                                      |
                       [ national AI gateway: identity, consent, rate limits ]
                                      |
          +---------------------------+----------------------------+
          |                           |                            |
   [ citizen services ]      [ sector copilots ]          [ crisis services ]
   navigator, translation    health, education, justice   flood twin, LANTERN, mesh
          |                           |                            |
          +-------------[ guardrails + policy engine (verified) ]--+
                                      |
              [ model serving: national LLMs, small edge models ]  <-- signed models only (SLSA)
                                      |
         [ RAG over permissioned data spaces ]  [ DP analytics ]  [ federated learning ]
                                      |
      AI factory North        AI factory South        AI factory East        edge kits (offline)
      (active-active)         (active-active)         (DR + research)        (crisis fallback)
                                      |
                 [ national SOC ]  [ eval & red-team centre ]  [ audit ledger ]
```

## Phases (36 months)

```text
   M0 ----------- M9 ----------------- M21 ------------------ M30 ----------- M36
   | BLUEPRINT    | REFERENCE STACK     | SCALE PROOF          | POLICY PACKAGE |
   | ConOps, reqs | every layer working | load tests, drills,  | white paper,    |
   | threat model | at municipal scale  | cost model, failure  | governance,     |
   | capacity     | from atlas parts    | injection            | briefings       |
```

## Non-negotiables

- Democratic oversight, transparency reports, independent audits.
- No mass-surveillance capability; purpose limitation is enforced in code (policy engine + audit ledger).
- Citizens control their data through consent in the identity wallet.
- Open standards and open source at every layer, so no single vendor can switch the country off.
- Crisis mode: core services degrade gracefully to regional and edge operation.
