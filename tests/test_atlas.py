"""Atlas data checks: every brief is complete, numbered once, and renderable."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))

import render  # noqa: E402

TRACKS = render.load()
ALL = [p for _, ps in TRACKS for p in ps]


def test_project_count():
    assert len(ALL) == 121


def test_ids_are_contiguous_and_unique():
    assert sorted(p["id"] for p in ALL) == list(range(1, 122))


def test_codes_unique():
    codes = [p["code"] for p in ALL]
    assert len(codes) == len(set(codes))


def test_required_fields_present():
    for p in ALL:
        missing = [f for f in render.REQUIRED if f not in p or p[f] in (None, "", [])]
        assert not missing, f"{p.get('code')}: missing {missing}"


def test_levels_and_months_sane():
    for p in ALL:
        assert 1 <= p["level"] <= 5, p["code"]
        limit = 36 if p.get("master") else (24 if p["level"] == 5 else 12)
        assert 1 <= p["months"] <= limit, p["code"]


def test_every_brief_has_four_phases_and_two_defend_questions():
    for p in ALL:
        assert len(p["phases"]) == 4, p["code"]
        assert len(p["defend"]) >= 2, p["code"]


def test_art_fits_in_a_terminal():
    for p in ALL:
        assert max(len(line) for line in p["art"].splitlines()) <= 100, p["code"]


def test_masterpieces_have_full_professional_fields():
    for p in ALL:
        if p["level"] == 5:
            missing = [f for f in render.MASTERPIECE_FIELDS if not p.get(f)]
            assert not missing, f"{p['code']}: missing {missing}"
            assert len(p["components"]) >= 4, p["code"]
            assert len(p["defend"]) >= 3, p["code"]


def test_every_original_project_has_an_upgrade_path():
    upgrades = render.load_upgrades()
    ids = {p["id"] for p in ALL}
    assert sorted(upgrades) == list(range(1, 51))
    for pid, up in upgrades.items():
        assert up["path"] and up["venue"], pid
        for link in up["links"]:
            assert link in ids, f"upgrade {pid} links to unknown project {link}"


def test_frontier_projects_say_who_sees_them():
    for p in ALL:
        if p["id"] >= 101:
            assert len(p.get("spotlight", [])) >= 2, p["code"]


def test_master_project_files_exist():
    root = Path(__file__).resolve().parent.parent / "master" / "nationstack"
    assert (root / "README.md").exists()
    assert (root / "capacity_model.py").exists()
    assert (root / "capacity.md").exists()
