# 06 · QUIETNET

```text
     _______
    | ((o)) |   "lights off"
    |_______|      |
       |        [keyword model] --> MQTT --> lamp
    no cloud.  no account.  no upload.
```

**Cloud-free voice control for the home**

> Your house listens, but only to you, and only at home.

```text
  TRACK A EDGE AI AND ROBOTICS  |  LEVEL [#....]  |  ~2 MONTHS  |  BUDGET €120
```

## The mission

Smart speakers send audio to the cloud; many households don't want that.

## How it works

```text
+--------------------------------------+
|  mic                                 |
+--------------------------------------+
                   |
                   v
+--------------------------------------+
|  wake-word + intent model on device  |
+--------------------------------------+
                   |
                   v
+--------------------------------------+
|  MQTT                                |
+--------------------------------------+
                   |
                   v
+--------------------------------------+
|  Home Assistant                      |
+--------------------------------------+
```

## Kit

- Raspberry Pi 5
- openWakeWord
- Whisper tiny
- Home Assistant
- MQTT

**Hardware:** Raspberry Pi 5 + USB mic

## Campaign

```text
  P1  [=====]                     m0-0.5    Wake word running locally
  P2        [=====]               m0.5-1    Intent parsing for 10 commands
  P3              [=====]         m1-1.5    Home Assistant integration
  P4                    [=====]   m1.5-2    Privacy test proving zero outbound traffic
```

## Gate: done when you can show

```text
  [ ] command accuracy
  [ ] latency
  [ ] outbound packets during use (target 0)
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Household members agree to the device.

## Resume line (fill with your measured numbers)

> Built a fully offline voice assistant ([N] ms latency) with network-verified zero cloud traffic.

**Skills it proves:** speech · home automation · privacy engineering

## Defend it

1. How did you prove no audio leaves the house?
2. How do you handle German and English speakers in one home?

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/quietnet  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- VINEGUARD](05-vineguard.md) · [atlas index](../README.md) · [PACKMULE ->](07-packmule.md)
