#!/usr/bin/env python3
r"""The brief schema: one declarative description of what a brief must contain.

    tracks/*.yaml  --[ schema.py ]-->  pass / list of violations

Every field a brief may carry is listed here once, with its type, its minimum
size and the tier that requires it. `tools/validate.py` turns this table into a
report; `tests/test_schema.py` turns it into pytest cases. Nothing else in the
repo should hard-code a field name.

Tiers
    all        every brief, 01-121
    level5     level-5 briefs (the masterpiece, frontier and grand-master tiers)
    frontier   ids 101+ (alignment and quantum), which must name who sees the work
    master     the grand-master brief (121)
"""

from __future__ import annotations

from dataclasses import dataclass

#: Exactly four phases, no more and no fewer — the campaign shape the atlas promises.
PHASE_COUNT = 4

#: A gate needs at least this many measurable metrics to be a gate.
MIN_METRICS = 2

#: ASCII art must fit a standard terminal.
MAX_ART_WIDTH = 100


@dataclass(frozen=True)
class Field:
    """One field of a brief."""

    name: str
    kind: type          # str, int, bool, list
    tier: str = "all"   # all | level5 | frontier | master
    min_len: int = 1    # minimum length for str and list fields
    item_kind: type | None = None  # element type for list fields


FIELDS: tuple[Field, ...] = (
    # identity and framing
    Field("id", int),
    Field("code", str, min_len=3),
    Field("name", str, min_len=10),
    Field("tagline", str, min_len=10),
    Field("problem", str, min_len=40),
    Field("art", str, min_len=10),
    # how it is built
    Field("flow", str, min_len=10),
    Field("stack", list, min_len=2, item_kind=str),
    Field("hardware", str),
    Field("budget", str),
    Field("months", int),
    Field("level", int),
    # sized, phased and gated
    Field("phases", list, min_len=PHASE_COUNT, item_kind=str),
    Field("metrics", list, min_len=MIN_METRICS, item_kind=str),
    # the parts that make a brief defensible
    # "None special." is a legitimate, honest answer for a brief with no special
    # exposure, so this floor only catches an empty or truncated line.
    Field("ethics", str, min_len=5),
    Field("resume", str, min_len=20),
    Field("skills", list, min_len=2, item_kind=str),
    Field("defend", list, min_len=2, item_kind=str),
    # masterpiece tier additions
    Field("components", list, tier="level5", min_len=4, item_kind=str),
    Field("trl", str, tier="level5"),
    Field("venue", str, tier="level5"),
    Field("deliverables", list, tier="level5", min_len=2, item_kind=str),
    Field("standards", list, tier="level5", min_len=1, item_kind=str),
    # frontier tier addition
    Field("spotlight", list, tier="frontier", min_len=2, item_kind=str),
    # grand master marker
    Field("master", bool, tier="master"),
)

#: Fields keyed by name, for lookups.
BY_NAME = {f.name: f for f in FIELDS}

#: Any key not listed above is a typo or an undocumented extension.
ALLOWED_KEYS = frozenset(BY_NAME)

#: Top-level keys a track file may use. `retired` is the documented way to take a
#: brief out of circulation without reusing its number (see CONTRIBUTING.md).
TRACK_FILE_KEYS = frozenset({"track", "projects", "retired"})

#: Keys a track header must carry.
TRACK_KEYS = frozenset({"id", "name", "motto"})

#: H2 sections every rendered brief page must contain, in no particular order.
REQUIRED_SECTIONS: tuple[str, ...] = (
    "The mission",
    "How it works",
    "Kit",
    "Campaign",
    "Safety and ethics",
    "Resume line (fill with your measured numbers)",
    "Defend it",
    "Masterpiece standard",
    "Launch checklist",
)

#: The gate heading is matched by prefix because it carries a sentence after the colon.
GATE_HEADING_PREFIX = "Gate:"

#: Extra H2 sections required of level-5 pages.
LEVEL5_SECTIONS: tuple[str, ...] = (
    "System map",
    "Readiness and publication",
    "Deliverables",
    "Standards and regulations to meet",
)

#: Extra H2 section required of frontier pages.
FRONTIER_SECTIONS: tuple[str, ...] = ("Who sees this",)

#: Extra H2 section required of the original 01-50 pages (they carry an upgrade path).
UPGRADE_SECTIONS: tuple[str, ...] = ("Masterpiece upgrade path",)

#: ids that `upgrades.yaml` must cover: the original fifty.
UPGRADE_IDS = tuple(range(1, 51))


def tiers_of(project: dict) -> set[str]:
    """Which schema tiers apply to this brief."""
    tiers = {"all"}
    if project.get("level") == 5:
        tiers.add("level5")
    if isinstance(project.get("id"), int) and project["id"] >= 101:
        tiers.add("frontier")
    if project.get("master"):
        tiers.add("master")
    return tiers


def required_fields(project: dict) -> list[Field]:
    """The fields this particular brief must carry."""
    tiers = tiers_of(project)
    return [f for f in FIELDS if f.tier in tiers]


def required_sections(project: dict, has_upgrade: bool) -> list[str]:
    """The H2 headings this brief's rendered page must carry."""
    out = list(REQUIRED_SECTIONS)
    if project.get("level") == 5:
        out += list(LEVEL5_SECTIONS)
    if project.get("id", 0) >= 101:
        out += list(FRONTIER_SECTIONS)
    if has_upgrade:
        out += list(UPGRADE_SECTIONS)
    return out
