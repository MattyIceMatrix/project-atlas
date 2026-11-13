#!/usr/bin/env python3
r"""Render the atlas: tracks/*.yaml -> projects/*.md and the README index.

    python tools/render.py          # write files
    python tools/render.py --check  # fail if generated files are out of date (used in CI)

     tracks/*.yaml  ---->  [ render.py ]  ---->  projects/NN-code.md
                                         \---->  README.md (between the INDEX markers)
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
TRACKS = ROOT / "tracks"
PROJECTS = ROOT / "projects"
README = ROOT / "README.md"
UPGRADES = ROOT / "upgrades.yaml"
MASTERPIECE_FIELDS = ["components", "trl", "venue", "deliverables", "standards"]
START, END = "<!-- INDEX:START -->", "<!-- INDEX:END -->"

REQUIRED = [
    "id", "code", "name", "tagline", "problem", "art", "flow", "stack", "hardware", "budget",
    "months", "level", "phases", "metrics", "ethics", "resume", "skills", "defend",
]


def load() -> list[tuple[dict, list[dict]]]:
    tracks = []
    for path in sorted(TRACKS.glob("*.yaml")):
        data = yaml.safe_load(path.read_text())
        tracks.append((data["track"], data["projects"]))
    return tracks


def load_upgrades() -> dict:
    return yaml.safe_load(UPGRADES.read_text()) if UPGRADES.exists() else {}


def system_map(code: str, components: list[str]) -> str:
    """Draw components as boxes in rows of three, flowing left to right, top to bottom."""
    width = max(len(c) for c in components) + 4
    top = "+" + "-" * width + "+"
    rows = [components[i:i + 3] for i in range(0, len(components), 3)]
    out = [f"  {code} SYSTEM MAP", ""]
    for r, row in enumerate(rows):
        out.append("    ".join([top] * len(row)))
        out.append("--->".join("|  " + c.ljust(width - 2) + "|" for c in row))
        out.append("    ".join([top] * len(row)))
        if r < len(rows) - 1:
            out.append(" " * (width // 2) + "|")
            out.append(" " * (width // 2) + "v")
    return "\n".join(out)


def slug(p: dict) -> str:
    return f"{p['id']:02d}-{p['code'].lower()}"


def stars(level: int) -> str:
    return "#" * level + "." * (5 - level)


def flow_diagram(flow: str) -> str:
    steps = [s.strip() for s in flow.split("->")]
    width = max(len(s) for s in steps) + 4
    out = []
    for i, step in enumerate(steps):
        out.append("+" + "-" * width + "+")
        out.append("|  " + step.ljust(width - 2) + "|")
        out.append("+" + "-" * width + "+")
        if i < len(steps) - 1:
            out.append(" " * (width // 2) + "|")
            out.append(" " * (width // 2) + "v")
    return "\n".join(out)


def phase_timeline(phases: list[str], months: int) -> str:
    lines = []
    n = len(phases)
    for i, phase in enumerate(phases):
        start = round(i * months / n, 1)
        end = round((i + 1) * months / n, 1)
        bar = " " * (i * 6) + "[" + "=" * 5 + "]"
        months_label = f"m{start:g}-{end:g}"
        lines.append(f"  P{i + 1}  {bar:<{n * 6 + 2}}  {months_label:<9} {phase}")
    return "\n".join(lines)


def render_project(track: dict, p: dict, prev: dict | None, nxt: dict | None,
                   upgrade: dict | None = None, by_id: dict | None = None) -> str:
    nav = []
    if prev:
        nav.append(f"[<- {prev['code']}]({slug(prev)}.md)")
    nav.append("[atlas index](../README.md)")
    if nxt:
        nav.append(f"[{nxt['code']} ->]({slug(nxt)}.md)")
    stack = "\n".join(f"- {s}" for s in p["stack"])
    metrics = "\n".join(f"  [ ] {m}" for m in p["metrics"])
    defend = "\n".join(f"{i}. {q}" for i, q in enumerate(p["defend"], 1))
    skills = " · ".join(p["skills"])
    extra = ""
    if all(k in p for k in MASTERPIECE_FIELDS):
        deliverables = "\n".join(f"- {d}" for d in p["deliverables"])
        standards = "\n".join(f"- {d}" for d in p["standards"])
        extra = f"""
## System map

```text
{system_map(p['code'], p['components'])}
```

## Readiness and publication

```text
  TECHNOLOGY READINESS   {p['trl']}
  PUBLICATION TARGET     {p['venue']}
```

## Deliverables

{deliverables}

## Standards and regulations to meet

{standards}
"""
    if upgrade:
        links = ", ".join(
            f"[{by_id[i]['code']}]({slug(by_id[i])}.md)" for i in upgrade.get("links", []) if i in by_id
        )
        extra += f"""
## Masterpiece upgrade path

```text
   LEVEL [{stars(p['level'])}]  ====================>  LEVEL [#####]
```

{upgrade['path']}

**Grows into:** {links or 'a standalone masterpiece'} · **Publication target:** {upgrade['venue']}
"""
    return f"""# {p['id']:02d} · {p['code']}

```text
{p['art'].rstrip()}
```

**{p['name']}**

> {p['tagline']}

```text
  TRACK {track['id']} {track['name'].upper()}  |  LEVEL [{stars(p['level'])}]  |  ~{p['months']} MONTHS  |  BUDGET {p['budget']}
```

## The mission

{p['problem']}

## How it works

```text
{flow_diagram(p['flow'])}
```

## Kit

{stack}

**Hardware:** {p['hardware']}

## Campaign

```text
{phase_timeline(p['phases'], p['months'])}
```

## Gate: done when you can show

```text
{metrics}
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

{p['ethics']}

## Resume line (fill with your measured numbers)

> {p['resume'].replace('<N>', '[N]')}

**Skills it proves:** {skills}
{extra}
## Defend it

{defend}

## Masterpiece standard

This project is built to the [Masterpiece Standard](../docs/masterpiece-standard.md): requirements with
traceability, threat model, frozen evals with model and data cards, signed releases, runbook, and external
proof of impact.

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/{p['code'].lower()}  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

{' · '.join(nav)}
"""


def render_index(tracks: list[tuple[dict, list[dict]]]) -> str:
    parts = [START, ""]
    for track, projects in tracks:
        parts.append(f"### Track {track['id']}: {track['name']}")
        parts.append("")
        parts.append(f"*{track['motto']}*")
        parts.append("")
        parts.append("| # | Codename | Project | Level | Months |")
        parts.append("| --- | --- | --- | --- | --- |")
        for p in projects:
            parts.append(
                f"| {p['id']:02d} | [{p['code']}](projects/{slug(p)}.md) | {p['name']} "
                f"| `{stars(p['level'])}` | {p['months']} |"
            )
        parts.append("")
    parts.append(END)
    return "\n".join(parts)


def build() -> dict[Path, str]:
    tracks = load()
    upgrades = load_upgrades()
    flat = [(t, p) for t, ps in tracks for p in ps]
    by_id = {p["id"]: p for _, p in flat}
    out: dict[Path, str] = {}
    for i, (track, p) in enumerate(flat):
        prev = flat[i - 1][1] if i > 0 else None
        nxt = flat[i + 1][1] if i < len(flat) - 1 else None
        out[PROJECTS / f"{slug(p)}.md"] = render_project(track, p, prev, nxt, upgrades.get(p["id"]), by_id)
    readme = README.read_text()
    head, _, rest = readme.partition(START)
    _, _, tail = rest.partition(END)
    out[README] = head + render_index(tracks) + tail
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    files = build()
    if args.check:
        stale = [str(p.relative_to(ROOT)) for p, c in files.items() if not p.exists() or p.read_text() != c]
        if stale:
            print("out of date:", ", ".join(stale))
            return 1
        print(f"atlas up to date: {len(files) - 1} projects")
        return 0
    PROJECTS.mkdir(exist_ok=True)
    for path, content in files.items():
        path.write_text(content)
    print(f"rendered {len(files) - 1} projects")
    return 0


if __name__ == "__main__":
    sys.exit(main())
