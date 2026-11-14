#!/usr/bin/env python3
r"""Validate the whole atlas: data, rendered pages, cross-references and claims.

    python tools/validate.py          # full report, exit 1 on any violation
    python tools/validate.py --quiet  # only failures

     tracks/*.yaml ---+
     projects/*.md    |
     upgrades.yaml    +--> [ validate.py ] --> 11 checks, pass/fail per check
     README.md        |
     master/...       +

Every check is a function that returns a list of violations. Nothing here guesses:
if a number is asserted, it was counted from the data in this repo. The schema the
checks enforce lives in `tools/schema.py`.
"""

from __future__ import annotations

import argparse
import collections
import functools
import importlib.util
import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))

import render  # noqa: E402
import schema  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", ".pytest_cache", "__pycache__", ".venv"}


# --------------------------------------------------------------------------- data


@functools.lru_cache(maxsize=1)
def _load() -> tuple[tuple[dict, list[dict]], ...]:
    """Parse tracks/*.yaml once; 16 files x 121 briefs is not free."""
    return tuple(render.load())


def tracks() -> list[tuple[dict, list[dict]]]:
    return list(_load())


def projects() -> list[dict]:
    return [p for _, ps in _load() for p in ps]


def retired_ids() -> list[int]:
    """ids taken out of circulation via a track file's `retired:` list."""
    out = []
    for path in sorted((ROOT / "tracks").glob("*.yaml")):
        data = yaml.safe_load(path.read_text()) or {}
        for entry in data.get("retired") or []:
            out.append(entry["id"] if isinstance(entry, dict) else int(entry))
    return out


def markdown_files() -> list[Path]:
    return sorted(
        p for p in ROOT.rglob("*.md")
        if not SKIP_DIRS & set(p.relative_to(ROOT).parts)
    )


# ------------------------------------------------------------------------- checks


def check_field_schema() -> list[str]:
    """Every brief carries exactly the fields its tier requires, correctly typed."""
    bad = []
    for p in projects():
        who = f"{p.get('id')}/{p.get('code')}"
        for key in p:
            if key not in schema.ALLOWED_KEYS:
                bad.append(f"{who}: unknown field {key!r} (typo, or add it to tools/schema.py)")
        for field in schema.required_fields(p):
            if field.name not in p:
                bad.append(f"{who}: missing required field {field.name!r}")
                continue
            value = p[field.name]
            if not isinstance(value, field.kind) or isinstance(value, bool) != (field.kind is bool):
                bad.append(f"{who}: {field.name} is {type(value).__name__}, expected {field.kind.__name__}")
                continue
            if field.kind in (str, list) and len(value) < field.min_len:
                bad.append(f"{who}: {field.name} has length {len(value)}, minimum {field.min_len}")
            if field.kind is list and field.item_kind:
                for i, item in enumerate(value):
                    if not isinstance(item, field.item_kind):
                        bad.append(f"{who}: {field.name}[{i}] is {type(item).__name__}, expected "
                                   f"{field.item_kind.__name__}")
                    elif field.item_kind is str and not item.strip():
                        bad.append(f"{who}: {field.name}[{i}] is blank")
        if not 1 <= p.get("level", 0) <= 5:
            bad.append(f"{who}: level {p.get('level')} outside 1-5")
        if p.get("art") and max(len(line) for line in p["art"].splitlines()) > schema.MAX_ART_WIDTH:
            bad.append(f"{who}: ASCII art wider than {schema.MAX_ART_WIDTH} columns")
    return bad


def check_identity() -> list[str]:
    """ids and codenames are unique, and the numbering has no holes."""
    bad = []
    all_projects = projects()
    active = [p["id"] for p in all_projects]
    retired = retired_ids()
    for label, values in (("id", active + retired),
                          ("code", [p["code"] for p in all_projects]),
                          ("name", [p["name"] for p in all_projects])):
        counts = collections.Counter(values)
        dupes = sorted(v for v, n in counts.items() if n > 1)
        if dupes:
            bad.append(f"duplicate {label}: {dupes}")
    allocated = sorted(active + retired)
    if allocated and allocated != list(range(1, len(allocated) + 1)):
        holes = sorted(set(range(1, max(allocated) + 1)) - set(allocated))
        bad.append(f"numbering is not contiguous from 1; missing {holes}")
    for p in all_projects:
        if not re.fullmatch(r"[A-Z0-9][A-Z0-9-]*", p["code"]):
            bad.append(f"{p['id']}: codename {p['code']!r} is not upper-case/hyphen only")
    return bad


def check_tracks() -> list[str]:
    """Track files are well formed, lettered in order, and own a contiguous id block."""
    bad = []
    seen: list[str] = []
    for path in sorted((ROOT / "tracks").glob("*.yaml")):
        data = yaml.safe_load(path.read_text()) or {}
        extra = set(data) - schema.TRACK_FILE_KEYS
        if extra:
            bad.append(f"{path.name}: unexpected top-level keys {sorted(extra)}")
        track = data.get("track") or {}
        if set(track) != schema.TRACK_KEYS:
            bad.append(f"{path.name}: track header keys {sorted(track)}, expected {sorted(schema.TRACK_KEYS)}")
        tid = track.get("id", "")
        if not path.name.upper().startswith(f"{tid}-"):
            bad.append(f"{path.name}: filename does not start with track id {tid!r}")
        seen.append(tid)
        ids = [p["id"] for p in data.get("projects") or []]
        if not ids:
            bad.append(f"{path.name}: no projects")
        elif ids != list(range(ids[0], ids[0] + len(ids))):
            bad.append(f"{path.name}: ids {ids} are not ascending and contiguous")
    if seen != sorted(seen):
        bad.append(f"track ids out of order on disk: {seen} (render.py relies on sorted filenames)")
    return bad


def check_phases() -> list[str]:
    """Four distinct phases per brief, and a timeline that runs forward to the deadline."""
    bad = []
    for p in projects():
        who = f"{p['id']}/{p['code']}"
        phases = p.get("phases") or []
        if len(phases) != schema.PHASE_COUNT:
            bad.append(f"{who}: {len(phases)} phases, expected exactly {schema.PHASE_COUNT}")
            continue
        if len({ph.strip().lower() for ph in phases}) != len(phases):
            bad.append(f"{who}: repeated phase text")
        months = p["months"]
        spans = [(round(i * months / len(phases), 1), round((i + 1) * months / len(phases), 1))
                 for i in range(len(phases))]
        if spans[0][0] != 0:
            bad.append(f"{who}: timeline starts at m{spans[0][0]}, expected m0")
        if spans[-1][1] != months:
            bad.append(f"{who}: timeline ends at m{spans[-1][1]}, but the brief claims {months} months")
        for (a_start, a_end), (b_start, b_end) in zip(spans, spans[1:]):
            if not a_start < a_end <= b_start < b_end:
                bad.append(f"{who}: phases overlap or run backwards: {spans}")
                break
        # the rendered page must show the phases in the same order
        page = (ROOT / "projects" / f"{render.slug(p)}.md")
        if page.exists():
            text = page.read_text()
            positions = [text.find(f"P{i + 1}  ") for i in range(len(phases))]
            if -1 in positions or positions != sorted(positions):
                bad.append(f"{who}: rendered phase markers P1..P{len(phases)} missing or out of order")
    return bad


def check_gates() -> list[str]:
    """Every brief has a gate, and every gate metric reaches the rendered page."""
    bad = []
    for p in projects():
        who = f"{p['id']}/{p['code']}"
        metrics = p.get("metrics") or []
        if len(metrics) < schema.MIN_METRICS:
            bad.append(f"{who}: {len(metrics)} gate metrics, minimum {schema.MIN_METRICS}")
        page = ROOT / "projects" / f"{render.slug(p)}.md"
        if not page.exists():
            continue
        text = page.read_text()
        if f"## {schema.GATE_HEADING_PREFIX}" not in text:
            bad.append(f"{who}: rendered page has no '## {schema.GATE_HEADING_PREFIX} ...' section")
            continue
        gate = text.split(f"## {schema.GATE_HEADING_PREFIX}", 1)[1].split("\n## ", 1)[0]
        for m in metrics:
            if f"[ ] {m}" not in gate:
                bad.append(f"{who}: gate metric {m!r} not checkboxed on the page")
        if "measured, dated and tied to a git commit" not in gate:
            bad.append(f"{who}: gate is missing the measured-numbers line")
    return bad


def check_sections() -> list[str]:
    """Every rendered page carries the H2 sections its tier requires."""
    bad = []
    upgrades = render.load_upgrades()
    for p in projects():
        who = f"{p['id']}/{p['code']}"
        page = ROOT / "projects" / f"{render.slug(p)}.md"
        if not page.exists():
            bad.append(f"{who}: no rendered page at projects/{render.slug(p)}.md")
            continue
        headings = set(re.findall(r"^## (.+)$", page.read_text(), flags=re.M))
        for want in schema.required_sections(p, has_upgrade=p["id"] in upgrades):
            if want not in headings:
                bad.append(f"{who}: page is missing section '## {want}'")
    return bad


def check_files() -> list[str]:
    """projects/ holds exactly one page per brief and nothing else."""
    bad = []
    expected = {f"{render.slug(p)}.md" for p in projects()}
    on_disk = {p.name for p in (ROOT / "projects").glob("*.md")}
    for orphan in sorted(on_disk - expected):
        bad.append(f"projects/{orphan} belongs to no brief (orphan page; render --check does not see it)")
    for missing in sorted(expected - on_disk):
        bad.append(f"projects/{missing} is missing")
    stray = sorted(p.name for p in (ROOT / "projects").iterdir() if p.suffix != ".md" and p.is_file())
    if stray:
        bad.append(f"non-markdown files in projects/: {stray}")
    return bad


def check_links() -> list[str]:
    """Every relative markdown link in the repo resolves to a file that exists."""
    bad = []
    pattern = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
    for md in markdown_files():
        for target in pattern.findall(md.read_text()):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            resolved = (md.parent / target.split("#", 1)[0]).resolve()
            if not resolved.exists():
                bad.append(f"{md.relative_to(ROOT)}: broken link -> {target}")
    return bad


def check_upgrades() -> list[str]:
    """upgrades.yaml covers the original fifty and points only at real briefs."""
    bad = []
    upgrades = render.load_upgrades()
    by_id = {p["id"]: p for p in projects()}
    if sorted(upgrades) != list(schema.UPGRADE_IDS):
        missing = sorted(set(schema.UPGRADE_IDS) - set(upgrades))
        extra = sorted(set(upgrades) - set(schema.UPGRADE_IDS))
        bad.append(f"upgrades.yaml should cover ids {schema.UPGRADE_IDS[0]}-{schema.UPGRADE_IDS[-1]}; "
                   f"missing {missing}, unexpected {extra}")
    for pid, up in sorted(upgrades.items()):
        if not isinstance(up, dict) or set(up) != {"path", "links", "venue"}:
            bad.append(f"upgrade {pid}: keys {sorted(up) if isinstance(up, dict) else type(up).__name__}, "
                       f"expected ['links', 'path', 'venue']")
            continue
        if not (up["path"] or "").strip():
            bad.append(f"upgrade {pid}: empty path")
        if not (up["venue"] or "").strip():
            bad.append(f"upgrade {pid}: empty venue")
        links = up["links"] or []
        if not links:
            bad.append(f"upgrade {pid}: no links")
        for link in links:
            if link not in by_id:
                bad.append(f"upgrade {pid}: links to unknown brief {link}")
            elif link == pid:
                bad.append(f"upgrade {pid}: links to itself")
        known = [by_id[x] for x in links if x in by_id]
        if known and not any(x["level"] == 5 for x in known):
            bad.append(f"upgrade {pid}: no level-5 target, so it is not an upgrade path "
                       f"({[(x['id'], x['level']) for x in known]})")
    return bad


def check_readme_claims() -> list[str]:
    """The counts the README states out loud match the counts in the data."""
    bad = []
    text = (ROOT / "README.md").read_text()
    all_projects = projects()
    measured = {
        "briefs": len(all_projects),
        "tracks": len(tracks()),
        "level-5": sum(1 for p in all_projects if p["level"] == 5),
        "masterpiece tier": sum(1 for p in all_projects if 51 <= p["id"] <= 100),
        "frontier tier": sum(1 for p in all_projects if 101 <= p["id"] <= 120),
        "grand master": sum(1 for p in all_projects if p.get("master")),
    }
    claims = {
        "briefs": r"^\s*(\d+) projects\s+\*",                # the banner, line start
        "briefs (prose)": r"\*\*(\d+) build-ready project briefs",
        "tracks": r"\*\s+(\d+) tracks\s+\*",                 # the banner
    }
    for label, pattern in claims.items():
        found = re.findall(pattern, text, flags=re.M)
        if not found:
            bad.append(f"README: cannot find the {label} claim (pattern {pattern!r}) — "
                       f"keep it machine-checkable or update tools/validate.py")
            continue
        key = label.split(" (")[0]
        for value in found:
            if int(value) != measured[key]:
                bad.append(f"README claims {value} {key}, data has {measured[key]}")
    # the "by the numbers" block, written as `key = value`
    block = re.search(r"by the numbers.*?```", text, flags=re.S)
    if not block:
        bad.append("README: no 'by the numbers' block for a reviewer to check against")
    else:
        for key, value in re.findall(r"([a-z0-9 -]+?)\s*=\s*(\d+)", block.group(0)):
            key = key.strip()
            if key not in measured:
                bad.append(f"README by-the-numbers: unknown key {key!r} "
                           f"(known: {sorted(measured)})")
            elif int(value) != measured[key]:
                bad.append(f"README by-the-numbers: {key} = {value}, data has {measured[key]}")
    return bad


def check_capacity_model() -> list[str]:
    """master/nationstack/capacity.md is exactly what capacity_model.py produces."""
    path = ROOT / "master" / "nationstack" / "capacity_model.py"
    report = ROOT / "master" / "nationstack" / "capacity.md"
    if not path.exists():
        return [f"{path.relative_to(ROOT)} is missing"]
    if not report.exists():
        return [f"{report.relative_to(ROOT)} is missing"]
    spec = importlib.util.spec_from_file_location("capacity_model", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module          # @dataclass needs the module registered
    spec.loader.exec_module(module)          # import only; writing happens under __main__
    fresh = module.report(module.ASSUMPTIONS)
    if fresh != report.read_text():
        return [(f"{report.relative_to(ROOT)} is stale — re-run "
                 f"`python {path.relative_to(ROOT)}` and commit the result")]
    return []


CHECKS = (
    ("field schema", check_field_schema),
    ("identity and numbering", check_identity),
    ("track files", check_tracks),
    ("phases ordered", check_phases),
    ("gates present", check_gates),
    ("page sections", check_sections),
    ("page files", check_files),
    ("internal links", check_links),
    ("upgrade paths", check_upgrades),
    ("README claims", check_readme_claims),
    ("capacity model", check_capacity_model),
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--quiet", action="store_true", help="print only failing checks")
    args = parser.parse_args()
    total = 0
    print(f"atlas validation: {len(projects())} briefs, {len(tracks())} tracks\n")
    for label, fn in CHECKS:
        violations = fn()
        total += len(violations)
        if violations:
            print(f"  FAIL  {label}  ({len(violations)})")
            for v in violations:
                print(f"          - {v}")
        elif not args.quiet:
            print(f"  ok    {label}")
    print()
    if total:
        print(f"{total} violation(s)")
        return 1
    print(f"all {len(CHECKS)} checks pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
