```text
    ____  ____   ___      _ _____ ____ _____      _  _____ _        _    ____
   |  _ \|  _ \ / _ \    | | ____/ ___|_   _|    / \|_   _| |      / \  / ___|
   | |_) | |_) | | | |_  | |  _|| |     | |     / _ \ | | | |     / _ \ \___ \
   |  __/|  _ <| |_| | |_| | |__| |___  | |    / ___ \| | | |___ / ___ \ ___) |
   |_|   |_| \_\\___/ \___/|_____\____| |_|   /_/   \_\_| |_____/_/   \_\____/

   121 projects  *  16 tracks  *  superintelligence alignment  *  quantum  *  1 nation-scale master
```

# Project Atlas

**121 build-ready project briefs for an edge-AI, security and data engineer, each one sized,
budgeted, phased and gated. Seventy-one are level-5: fifty masterpieces, twenty at the frontier of AI
alignment and quantum computing, and one sovereign AI blueprint for a nation of 100 million.**

This repo is a **map, not an implementation**. Every brief is a plan for a project that has not been
built yet. Nothing here claims a measured result. What it does claim is that the plans are complete and
consistent, and that claim is machine-checked: the briefs are generated from `tracks/*.yaml`, and CI
fails if the pages, the index, the counts or the cross-references drift apart.

```text
   by the numbers            counted from tracks/*.yaml by tools/validate.py
     briefs = 121    tracks = 16    level-5 = 71
     masterpiece tier = 50    frontier tier = 20    grand master = 1
     every brief: 4 phases, 2+ gate metrics, 2+ defend questions, an ethics line

   verify it yourself        don't take the prose on trust
     pip install pyyaml pytest
     pytest -q                        # schema and consistency checks over every brief
     python tools/validate.py         # fields, sections, links, counts, upgrade paths
     python tools/render.py --check    # the pages still match the data that generated them
```

The flagship project is [LANTERN](https://github.com/MattyIceMatrix/lantern), an offline flood search-and-rescue kit.
The atlas is the map of what comes next. Each brief has the mission, the architecture, the kit, a phased
campaign, a measurable gate, the ethics line, a resume bullet waiting for real numbers, and the questions
you must be able to answer out loud.

## The compass

```text
                                 [ H ] FRONTIER
                                 47-50 research
                                       ^
          [ G ] PEOPLE & SPORT         |          [ A ] EDGE AI & ROBOTICS
          42-46                        |          01-08
                         \             |             /
                          \            |            /
   [ F ] VISION & GEO ------------- ( YOU ) ------------- [ B ] GENERATIVE AI
   36-41                          /    |    \             09-15
                                 /     |     \
                                /      |      \
          [ E ] CLOUD & MLOPS          |          [ C ] AI SAFETY & GOVERNANCE
          29-35                        v          16-21
                                 [ D ] CYBER DEFENSE
                                 22-28
```

## How to pick the next one

```text
   1. Does it reuse something you already built?      (LANTERN rover, map pack, Guardian ...)
   2. Does it fill a gap a job posting asked for?      (check 3 real postings)
   3. Can you show a measured number in 8 weeks?       (if not, pick a lower level)
   4. Would you explain it at dinner without slides?   (if not, it's not your story yet)
```

**Rule of the atlas:** one active project at a time next to LANTERN. A project gets its own repo only
on the day you start it, and goes public when it has a first measured result.

## Levels

```text
   [#....]  1  a weekend-scale build, one new skill
   [##...]  2  a few months, a clear pipeline, public data
   [###..]  3  real hardware or real evaluation work, a few moving parts
   [####.]  4  research-flavoured, distributed or safety-critical; plan for setbacks
   [#####]  5  reserved for LANTERN-scale capstones
```

## The masterpiece tier (51-100)

```text
                      __________________________________
                     |   M A S T E R P I E C E   T I E R |
                     |__________________________________|
                                      |
       +-------------+-------------+--+----------+-------------+
       |             |             |             |             |
   [ I ] 51-60   [ J ] 61-70   [ K ] 71-80   [ L ] 81-90   [ M ] 91-100
   AUTONOMOUS    FOUNDATION    TRUST &       PLANET &      CIVIC, SCIENCE
   SYSTEMS       MODELS &      SECURITY &    CLIMATE &     & HUMAN
                 AI INFRA      SOVEREIGNTY   INFRA         PERFORMANCE
```

Every masterpiece brief adds a **system map**, a **technology-readiness target**, a **publication venue**,
**deliverables**, and the **standards and regulations** it must meet. Each runs 12–24 months.

Every original project (01–50) now carries a **masterpiece upgrade path** (from `upgrades.yaml`) showing
how it grows into one or more level-5 builds. The professional bar for all of them is the
[Masterpiece Standard](docs/masterpiece-standard.md): twelve pillars from requirements to proof of impact.

```text
   the honest math:  50 masterpieces x 12-24 months  =  a career, not a year.
   pick ONE masterpiece next to LANTERN. finish it. publish it. then pick the next.
```

## The frontier tier (101-120) and the grand master (121)

```text
                    *            .        [ 121 NATIONSTACK ]        .          *
                          .            sovereign AI for 100M people
                                     /                            \
           [ N ] 101-110  SUPERINTELLIGENCE ALIGNMENT       [ O ] 111-120  QUANTUM
           interpretability, AI control, sandbagging,      error-correction decoders, honest QML,
           model organisms, scalable oversight, evals,     error mitigation, compilers, QKD,
           deception probes, reward hacking, CoT, compute  GPU simulators, verified quantum agents,
           governance                                       resource estimates for nations
```

**No one builds superintelligence in a garage.** The frontier labs and AI safety institutes are hiring
people who can make increasingly capable systems understandable, controllable and measurable, and
that's what track N trains. Track O is honest quantum: beat the classical baseline or publish that it
didn't.

Every frontier page has a **Who sees this** section naming the fellowship, institute, hackathon or open-source
project where that work gets in front of leaders. The [Visibility Playbook](docs/visibility-playbook.md)
turns them into a 12-month plan.

**NATIONSTACK (121)** assembles the whole atlas into a sovereign AI ecosystem for a country of 100 million
people: ten pillars, a reference architecture, a working miniature, and a
[capacity model](master/nationstack/capacity.md) that turns population into GPUs, megawatts and euros
with every assumption visible. Start at [master/nationstack/](master/nationstack/README.md).

## The atlas

<!-- INDEX:START -->

### Track A: Edge AI and Robotics

*Intelligence where the cloud can't reach.*

| # | Codename | Project | Level | Months |
| --- | --- | --- | --- | --- |
| 01 | [TIDEWATCH](projects/01-tidewatch.md) | River-gauge early warning on solar sensor nodes | `##...` | 4 |
| 02 | [HIVEMIND](projects/02-hivemind.md) | Beehive health monitor with on-device audio AI | `##...` | 3 |
| 03 | [FORESTER](projects/03-forester.md) | Wildfire smoke spotter for the Palatinate Forest | `###..` | 5 |
| 04 | [BRIDGEKEEPER](projects/04-bridgekeeper.md) | Concrete crack inspection with an edge vision pipeline | `###..` | 4 |
| 05 | [VINEGUARD](projects/05-vineguard.md) | Vineyard disease detection for Pfalz winemakers | `##...` | 4 |
| 06 | [QUIETNET](projects/06-quietnet.md) | Cloud-free voice control for the home | `#....` | 2 |
| 07 | [PACKMULE](projects/07-packmule.md) | Follow-me cargo rover for volunteers | `###..` | 3 |
| 08 | [ICEROAD](projects/08-iceroad.md) | Road ice prediction from low-cost roadside sensors | `##...` | 3 |

### Track B: Generative AI and LLM Systems

*Language models that earn their answers.*

| # | Codename | Project | Level | Months |
| --- | --- | --- | --- | --- |
| 09 | [AMTSDEUTSCH](projects/09-amtsdeutsch.md) | Offline explainer for German government letters | `##...` | 3 |
| 10 | [VERITAS](projects/10-veritas.md) | Citation-checked RAG for technical manuals | `###..` | 3 |
| 11 | [SKILLBRIDGE-COPILOT](projects/11-skillbridge-copilot.md) | Military-to-civilian skills translator | `##...` | 3 |
| 12 | [LOOM](projects/12-loom.md) | Distil a big model's skill into a tiny one | `####.` | 3 |
| 13 | [ECHO](projects/13-echo.md) | Offline meeting notes on a laptop | `##...` | 2 |
| 14 | [PATCHWORK](projects/14-patchwork.md) | Code-review agent that writes the missing tests | `###..` | 3 |
| 15 | [GRANITE](projects/15-granite.md) | Regression-test harness for LLM applications | `##...` | 2 |

### Track C: AI Safety and Governance

*Trust is a feature you can test.*

| # | Codename | Project | Level | Months |
| --- | --- | --- | --- | --- |
| 16 | [TRIPWIRE](projects/16-tripwire.md) | Prompt-injection firewall for LLM apps | `###..` | 3 |
| 17 | [LEDGER](projects/17-ledger.md) | Tamper-evident audit log service for AI decisions | `##...` | 2 |
| 18 | [REDCELL](projects/18-redcell.md) | Automated red-team harness for AI agents | `###..` | 3 |
| 19 | [CHARTER](projects/19-charter.md) | AI Act documentation generator | `##...` | 2 |
| 20 | [FAIRLINE](projects/20-fairline.md) | Bias audit toolkit for tabular models | `##...` | 2 |
| 21 | [SANDBOX](projects/21-sandbox.md) | Capability-limited sandbox for agent tools | `####.` | 3 |

### Track D: Cyber Defense

*Defend the network you actually have.*

| # | Codename | Project | Level | Months |
| --- | --- | --- | --- | --- |
| 22 | [SENTRY](projects/22-sentry.md) | Home-network intrusion detection with ML anomaly scoring | `##...` | 3 |
| 23 | [HONEYCOMB](projects/23-honeycomb.md) | Honeypot fleet with LLM-written threat summaries | `##...` | 2 |
| 24 | [PHISHNET](projects/24-phishnet.md) | Explainable phishing classifier | `##...` | 3 |
| 25 | [SBOM-RADAR](projects/25-sbom-radar.md) | Software supply-chain risk dashboard | `##...` | 2 |
| 26 | [ZEROTRUST-LAB](projects/26-zerotrust-lab.md) | Zero-trust access lab | `###..` | 2 |
| 27 | [LOGLENS](projects/27-loglens.md) | SIEM-lite with LLM-assisted triage | `###..` | 3 |
| 28 | [GHOSTPRINT](projects/28-ghostprint.md) | Firmware integrity checker for IoT devices | `###..` | 3 |

### Track E: Cloud, Data and MLOps

*Models are easy. Production is the project.*

| # | Codename | Project | Level | Months |
| --- | --- | --- | --- | --- |
| 29 | [CONVEYOR](projects/29-conveyor.md) | End-to-end MLOps platform on k3s | `####.` | 4 |
| 30 | [RIVERFLOW](projects/30-riverflow.md) | Streaming lakehouse for German open water data | `###..` | 3 |
| 31 | [FEATUREFORGE](projects/31-featureforge.md) | Minimal feature store built from scratch | `###..` | 3 |
| 32 | [COLDSTART](projects/32-coldstart.md) | Serverless inference cost optimiser | `###..` | 2 |
| 33 | [WATCHTOWER](projects/33-watchtower.md) | Model drift and data-quality monitoring | `##...` | 2 |
| 34 | [DATACOMPASS](projects/34-datacompass.md) | Data lineage and catalogue | `##...` | 2 |
| 35 | [SPOTFLEET](projects/35-spotfleet.md) | Fault-tolerant GPU training on spot instances | `###..` | 2 |

### Track F: Computer Vision and Geospatial

*See the world from the ground and from orbit.*

| # | Codename | Project | Level | Months |
| --- | --- | --- | --- | --- |
| 36 | [ORBITAL](projects/36-orbital.md) | Sentinel-2 change detection for floods and burn scars | `###..` | 3 |
| 37 | [ROOFTOP](projects/37-rooftop.md) | Solar potential map from open elevation data | `###..` | 3 |
| 38 | [TRAFFICLENS](projects/38-trafficlens.md) | Privacy-first traffic counting at the edge | `###..` | 3 |
| 39 | [GREENLINE](projects/39-greenline.md) | Urban tree canopy and heat map | `##...` | 2 |
| 40 | [POTHOLE-PATROL](projects/40-pothole-patrol.md) | Dashcam road damage detection | `##...` | 2 |
| 41 | [HERITAGE3D](projects/41-heritage3d.md) | 3D scans of Palatinate castle ruins | `###..` | 2 |

### Track G: People, Sport and Community

*Tech that helps someone you can name.*

| # | Codename | Project | Level | Months |
| --- | --- | --- | --- | --- |
| 42 | [HURDLE](projects/42-hurdle.md) | Hurdle technique analysis with pose estimation | `##...` | 2 |
| 43 | [POOLSHARK](projects/43-poolshark.md) | Pool shot analysis and training coach | `##...` | 2 |
| 44 | [CLIMB-TRANSITION](projects/44-climb-transition.md) | Veteran transition dashboard | `##...` | 3 |
| 45 | [RECEIPTLENS](projects/45-receiptlens.md) | Grocery receipt scanner and price tracker | `#....` | 2 |
| 46 | [SPRECHEN](projects/46-sprechen.md) | Offline German speaking coach | `##...` | 3 |

### Track H: Frontier and Research

*Where the next job titles come from.*

| # | Codename | Project | Level | Months |
| --- | --- | --- | --- | --- |
| 47 | [NEUROSPARK](projects/47-neurospark.md) | Spiking neural networks for ultra-low-power sensing | `####.` | 3 |
| 48 | [QUANTUMSAFE](projects/48-quantumsafe.md) | Post-quantum crypto migration for IoT | `####.` | 3 |
| 49 | [SWARM](projects/49-swarm.md) | Multi-robot search coordination in simulation | `####.` | 4 |
| 50 | [HEARTH](projects/50-hearth.md) | Home energy digital twin with reinforcement learning | `####.` | 4 |

### Track I: Masterpiece: Autonomous Systems

*Machines that go where people shouldn't, and come back with answers.*

| # | Codename | Project | Level | Months |
| --- | --- | --- | --- | --- |
| 51 | [SEAWALL](projects/51-seawall.md) | Autonomous survey boat for river and flood-plain mapping | `#####` | 18 |
| 52 | [FLEETMIND](projects/52-fleetmind.md) | Heterogeneous robot fleet for disaster mapping | `#####` | 20 |
| 53 | [EDGEOS](projects/53-edgeos.md) | Secure, updatable OS image for edge-AI fleets | `#####` | 14 |
| 54 | [ROADSAGE](projects/54-roadsage.md) | Driver-assistance research stack with a safety monitor | `#####` | 16 |
| 55 | [RAILWATCH](projects/55-railwatch.md) | Autonomous rail-track inspection trolley | `#####` | 16 |
| 56 | [AGRIFLEET](projects/56-agrifleet.md) | Autonomous vineyard robot for mechanical weeding | `#####` | 20 |
| 57 | [PIPEPROBE](projects/57-pipeprobe.md) | In-pipe inspection crawler for sewers | `#####` | 14 |
| 58 | [SKYLANE](projects/58-skylane.md) | Drone traffic management simulator (U-space) | `#####` | 14 |
| 59 | [RECYCLR](projects/59-recyclr.md) | Tactile robot arm that sorts recyclables | `#####` | 16 |
| 60 | [MESHLIFE](projects/60-meshlife.md) | Disaster mesh network with AI message triage | `#####` | 14 |

### Track J: Masterpiece: Foundation Models and AI Infrastructure

*Build the engine, not just the car.*

| # | Codename | Project | Level | Months |
| --- | --- | --- | --- | --- |
| 61 | [TINYFOUNDRY](projects/61-tinyfoundry.md) | Train a small language model from scratch, end to end | `#####` | 12 |
| 62 | [AERIALVLM](projects/62-aerialvlm.md) | Vision-language model for disaster aerial imagery | `#####` | 14 |
| 63 | [INFERNO](projects/63-inferno.md) | LLM inference server built from scratch | `#####` | 14 |
| 64 | [MINICOMPILER](projects/64-minicompiler.md) | Tiny ML compiler for edge accelerators | `#####` | 16 |
| 65 | [RAGOPS](projects/65-ragops.md) | Multi-tenant enterprise RAG platform | `#####` | 14 |
| 66 | [AGENTGRID](projects/66-agentgrid.md) | Verified multi-agent workflow runtime | `#####` | 14 |
| 67 | [EDGEBENCH](projects/67-edgebench.md) | Benchmark and leaderboard for on-device LLMs | `#####` | 12 |
| 68 | [FEDERATE](projects/68-federate.md) | Federated learning across edge devices with privacy guarantees | `#####` | 14 |
| 69 | [SYNTHSCENE](projects/69-synthscene.md) | Synthetic data engine for rare disaster scenes | `#####` | 14 |
| 70 | [HOMECLUSTER](projects/70-homecluster.md) | Small GPU cluster with a real scheduler and MLOps | `#####` | 12 |

### Track K: Masterpiece: Trust, Security and Sovereignty

*Prove it, don't promise it.*

| # | Codename | Project | Level | Months |
| --- | --- | --- | --- | --- |
| 71 | [SOVEREIGN](projects/71-sovereign.md) | EU sovereign AI reference stack, on-prem | `#####` | 18 |
| 72 | [ENCLAVE](projects/72-enclave.md) | Confidential AI inference with remote attestation | `#####` | 14 |
| 73 | [ZKAUDIT](projects/73-zkaudit.md) | Zero-knowledge proofs for AI compliance claims | `#####` | 16 |
| 74 | [AUTOSOC](projects/74-autosoc.md) | Human-gated autonomous security operations centre | `#####` | 16 |
| 75 | [MODELCHAIN](projects/75-modelchain.md) | Signed, provenance-tracked ML model supply chain | `#####` | 12 |
| 76 | [DPVAULT](projects/76-dpvault.md) | Differential privacy analytics platform | `#####` | 12 |
| 77 | [PROVENANCE](projects/77-provenance.md) | Content provenance and deepfake detection for newsrooms | `#####` | 14 |
| 78 | [PROVENGUARD](projects/78-provenguard.md) | Formally verified guardrail policy engine | `#####` | 18 |
| 79 | [OTSENTINEL](projects/79-otsentinel.md) | Industrial control system anomaly detection lab | `#####` | 14 |
| 80 | [CREDMESH](projects/80-credmesh.md) | Verifiable credentials for responders at disaster sites | `#####` | 12 |

### Track L: Masterpiece: Planet, Climate and Infrastructure

*Model the world well enough to protect it.*

| # | Codename | Project | Level | Months |
| --- | --- | --- | --- | --- |
| 81 | [FLOODTWIN](projects/81-floodtwin.md) | Hydrodynamic digital twin of the Ahr valley with an ML surrogate | `#####` | 20 |
| 82 | [GRIDBRAIN](projects/82-gridbrain.md) | Municipal grid-edge forecasting and battery dispatch | `#####` | 14 |
| 83 | [PLUMEWATCH](projects/83-plumewatch.md) | Methane plume detection from satellites | `#####` | 14 |
| 84 | [HEATSHIELD](projects/84-heatshield.md) | City heat-wave early warning and vulnerability map | `#####` | 12 |
| 85 | [LEAKNET](projects/85-leaknet.md) | Water network leak detection with acoustic sensors and graph ML | `#####` | 16 |
| 86 | [DROUGHTSENSE](projects/86-droughtsense.md) | Drought and soil-moisture forecasting from radar satellites | `#####` | 16 |
| 87 | [BRIDGESHM](projects/87-bridgeshm.md) | Structural health monitoring with vibration sensors and a digital twin | `#####` | 16 |
| 88 | [FIRESPREAD](projects/88-firespread.md) | Wildfire spread surrogate and resource planner | `#####` | 16 |
| 89 | [SURGECAST](projects/89-surgecast.md) | Storm-surge forecasting for the North Sea coast | `#####` | 12 |
| 90 | [KMWEATHER](projects/90-kmweather.md) | Kilometre-scale weather downscaling with ML | `#####` | 16 |

### Track M: Masterpiece: Civic, Science and Human Performance

*Big skills, pointed at real people.*

| # | Codename | Project | Level | Months |
| --- | --- | --- | --- | --- |
| 91 | [ATHLETEOS](projects/91-athleteos.md) | Sprint and hurdle performance platform | `#####` | 14 |
| 92 | [COMMANDSIM](projects/92-commandsim.md) | Incident command training simulator with AI role players | `#####` | 14 |
| 93 | [VERWALTUNG](projects/93-verwaltung.md) | Citizen navigator for German administrative procedures | `#####` | 14 |
| 94 | [SKYEDGE](projects/94-skyedge.md) | Edge AI for amateur telescope transient detection | `#####` | 14 |
| 95 | [BABEL](projects/95-babel.md) | Offline speech translation device for responders | `#####` | 14 |
| 96 | [WAYFINDER](projects/96-wayfinder.md) | Indoor navigation for blind and low-vision users | `#####` | 16 |
| 97 | [REPROBOT](projects/97-reprobot.md) | Research agent that reproduces ML papers, with verification | `#####` | 16 |
| 98 | [QUESTLINE](projects/98-questline.md) | Adaptive, gamified engineering curriculum engine | `#####` | 14 |
| 99 | [HELPERHUB](projects/99-helperhub.md) | Coordination platform for spontaneous disaster volunteers | `#####` | 14 |
| 100 | [CITYTWIN](projects/100-citytwin.md) | Open digital twin of a mid-size city | `#####` | 24 |

### Track N: Frontier: Superintelligence Alignment and Safety

*Nobody builds superintelligence in a garage. Everybody who matters is hiring people who can make it safe.*

| # | Codename | Project | Level | Months |
| --- | --- | --- | --- | --- |
| 101 | [GLASSBOX](projects/101-glassbox.md) | Mechanistic interpretability of a small open model with sparse autoencoders | `#####` | 12 |
| 102 | [CONTROLROOM](projects/102-controlroom.md) | AI control protocols for untrusted coding agents | `#####` | 12 |
| 103 | [SANDBAG](projects/103-sandbag.md) | Detecting sandbagging in capability evaluations | `#####` | 12 |
| 104 | [MODELORGS](projects/104-modelorgs.md) | Model organisms of emergent misalignment | `#####` | 14 |
| 105 | [WEAKJUDGE](projects/105-weakjudge.md) | Scalable oversight with debate and weak-to-strong supervision | `#####` | 12 |
| 106 | [EVALSMITH](projects/106-evalsmith.md) | New safety evaluations contributed to Inspect Evals | `#####` | 12 |
| 107 | [TRUTHPROBE](projects/107-truthprobe.md) | Lie and deception detection with activation probes | `#####` | 12 |
| 108 | [REWARDGUARD](projects/108-rewardguard.md) | Catching reward hacking in RL-trained coding agents | `#####` | 14 |
| 109 | [COTWATCH](projects/109-cotwatch.md) | Chain-of-thought monitorability study | `#####` | 12 |
| 110 | [COMPUTEWATCH](projects/110-computewatch.md) | Technical AI governance with hardware-backed compute verification | `#####` | 14 |

### Track O: Frontier: Quantum Computing and Quantum AI

*Honest quantum: beat the classical baseline or say so.*

| # | Codename | Project | Level | Months |
| --- | --- | --- | --- | --- |
| 111 | [QDECODER](projects/111-qdecoder.md) | Neural decoders for quantum error correction | `#####` | 12 |
| 112 | [QMLTRUTH](projects/112-qmltruth.md) | Honest quantum machine learning benchmark | `#####` | 12 |
| 113 | [QROUTE](projects/113-qroute.md) | Quantum optimisation for disaster logistics, against strong classical solvers | `#####` | 12 |
| 114 | [QMITIGATE](projects/114-qmitigate.md) | Error mitigation contributions and real-hardware benchmarks | `#####` | 12 |
| 115 | [QCHEM](projects/115-qchem.md) | Quantum chemistry for battery materials, with honest classical comparison | `#####` | 14 |
| 116 | [QCOMPILE](projects/116-qcompile.md) | Quantum circuit optimisation passes | `#####` | 12 |
| 117 | [QKDNET](projects/117-qkdnet.md) | Quantum key distribution network simulator for critical communications | `#####` | 12 |
| 118 | [QSIMGPU](projects/118-qsimgpu.md) | GPU-accelerated quantum circuit simulator | `#####` | 14 |
| 119 | [QAGENT](projects/119-qagent.md) | AI agent that writes and verifies quantum programs | `#####` | 12 |
| 120 | [QREADY](projects/120-qready.md) | When will quantum matter? Resource estimates for real national problems | `#####` | 12 |

### Track P: Grand Master: Nation-Scale Sovereign AI

*Everything in this atlas, assembled for a whole country.*

| # | Codename | Project | Level | Months |
| --- | --- | --- | --- | --- |
| 121 | [NATIONSTACK](projects/121-nationstack.md) | Sovereign AI ecosystem for a nation of 100 million people | `#####` | 36 |

<!-- INDEX:END -->

## How this repo works

```text
   tracks/*.yaml  --(python tools/render.py)-->  projects/*.md + this index
                                     |
                         CI: tests/ + render --check
```

Edit a brief in `tracks/`, run `python tools/render.py`, commit both. CI fails if the pages and the data
drift apart.

## Ground rules for every project

- Measured numbers only: every metric has a date, hardware and git commit.
- Public or synthetic data; data card before training.
- Civilian use. Defensive security only, on systems you own or are allowed to test.
- Honest limits section in every README.

## Licence

Apache-2.0. Datasets and services named in the briefs keep their own licences.
