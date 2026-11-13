# 07 · PACKMULE

```text
    o        ,--------.
   /|\  --> |  ====  |=]   follows at 2 m
   / \      '--------'
             (O)  (O)
```

**Follow-me cargo rover for volunteers**

> Carries the sandbags so people don't have to.

```text
  TRACK A EDGE AI AND ROBOTICS  |  LEVEL [###..]  |  ~3 MONTHS  |  BUDGET €80 extra
```

## The mission

Volunteers carry heavy loads over rough ground during cleanups and events.

## How it works

```text
+---------------------------------+
|  UWB or camera person tracking  |
+---------------------------------+
                |
                v
+---------------------------------+
|  ROS 2 follow controller        |
+---------------------------------+
                |
                v
+---------------------------------+
|  obstacle stop                  |
+---------------------------------+
                |
                v
+---------------------------------+
|  e-stop                         |
+---------------------------------+
```

## Kit

- ROS 2 Humble
- UWB modules
- Nav2
- Jetson or Raspberry Pi

**Hardware:** Reuses the LANTERN rover chassis

## Campaign

```text
  P1  [=====]                     m0-0.8    Person following in simulation
  P2        [=====]               m0.8-1.5  UWB tracking on real hardware
  P3              [=====]         m1.5-2.2  Safety layer with obstacle stop and e-stop
  P4                    [=====]   m2.2-3    Load test on a closed course
```

## Gate: done when you can show

```text
  [ ] following distance error
  [ ] stop distance
  [ ] payload kg
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Closed-course testing; speed limit; never near children unsupervised.

## Resume line (fill with your measured numbers)

> Built a ROS 2 follow-me rover with UWB tracking and a certified-style safety stop under [N] s.

**Skills it proves:** ROS 2 · control · functional safety

## Defend it

1. What happens if it loses the person?
2. Why is UWB more robust than vision here?

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/packmule  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- QUIETNET](06-quietnet.md) · [atlas index](../README.md) · [ICEROAD ->](08-iceroad.md)
