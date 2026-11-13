# 49 · SWARM

```text
     [r1]~~>    [r2]~~>
         \       /        auction: who takes sector C-3?
     [r3]--( map )--[r4]  r4 bids 12 s, wins
              |
            [r5]
```

**Multi-robot search coordination in simulation**

> Five cheap robots beat one expensive one, if they talk.

```text
  TRACK H FRONTIER AND RESEARCH  |  LEVEL [####.]  |  ~4 MONTHS  |  BUDGET €0
```

## The mission

Single robots search slowly; teams of robots need task allocation that survives lost communication.

## How it works

```text
+--------------------------------+
|  shared map                    |
+--------------------------------+
                |
                v
+--------------------------------+
|  market-based task allocation  |
+--------------------------------+
                |
                v
+--------------------------------+
|  decentralised planning        |
+--------------------------------+
                |
                v
+--------------------------------+
|  comms-loss tests              |
+--------------------------------+
```

## Kit

- ROS 2
- Gazebo
- Python
- Nav2 multi-robot

**Hardware:** None (simulation)

## Campaign

```text
  P1  [=====]                     m0-1      Multi-robot sim world (extends LANTERN)
  P2        [=====]               m1-2      Auction-based sector allocation
  P3              [=====]         m2-3      Communication loss and robot failure handling
  P4                    [=====]   m3-4      Coverage vs robot count study
```

## Gate: done when you can show

```text
  [ ] time to full coverage
  [ ] coverage with 1 robot lost
  [ ] messages per minute
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Civilian search use case only.

## Resume line (fill with your measured numbers)

> Built decentralised multi-robot search; 5 robots cut coverage time [N]% and tolerated robot loss.

**Skills it proves:** multi-agent systems · robotics · distributed algorithms

## Defend it

1. Why auctions instead of a central planner?
2. What happens when two robots both think they won?

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/swarm  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- QUANTUMSAFE](48-quantumsafe.md) · [atlas index](../README.md) · [HEARTH ->](50-hearth.md)
