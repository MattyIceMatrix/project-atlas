"""Schema validation of every brief, plus proof that the checks actually bite.

The first test runs each check in `tools/validate.py` against the real atlas and
requires zero violations. The rest deliberately break the data and require the
matching check to notice, so this file cannot silently rot into a no-op.
"""

import copy
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import schema  # noqa: E402
import validate  # noqa: E402


# ------------------------------------------------------------------ the real atlas

@pytest.mark.parametrize("label,check", validate.CHECKS, ids=[c[0] for c in validate.CHECKS])
def test_check_passes(label, check):
    violations = check()
    assert not violations, f"{label}:\n" + "\n".join(f"  - {v}" for v in violations)


def test_every_brief_is_covered_by_the_schema():
    """No brief carries a field the schema does not know about, and vice versa."""
    keys = {k for p in validate.projects() for k in p}
    assert keys <= schema.ALLOWED_KEYS, f"undocumented fields: {sorted(keys - schema.ALLOWED_KEYS)}"
    unused = schema.ALLOWED_KEYS - keys
    assert not unused, f"schema declares fields no brief uses: {sorted(unused)}"


def test_no_python_repr_leaked_into_a_rendered_page():
    """A YAML scalar with an unquoted colon parses as a dict and renders as `{'a': 'b'}`."""
    offenders = [
        str(page.relative_to(ROOT))
        for page in sorted((ROOT / "projects").glob("*.md"))
        if "{'" in page.read_text()
    ]
    assert not offenders, f"dict repr rendered into: {offenders}"


# ------------------------------------------------------- the checks notice breakage

@pytest.fixture
def one_brief():
    return copy.deepcopy(validate.projects()[0])


def test_field_schema_catches_an_unknown_field(monkeypatch, one_brief):
    one_brief["levle"] = 5
    monkeypatch.setattr(validate, "projects", lambda: [one_brief])
    assert any("unknown field" in v for v in validate.check_field_schema())


def test_field_schema_catches_a_missing_gate(monkeypatch, one_brief):
    del one_brief["metrics"]
    monkeypatch.setattr(validate, "projects", lambda: [one_brief])
    assert any("missing required field 'metrics'" in v for v in validate.check_field_schema())


def test_field_schema_catches_a_non_string_list_entry(monkeypatch, one_brief):
    one_brief["defend"] = [{"A vs B": "which?"}, "a real question"]
    monkeypatch.setattr(validate, "projects", lambda: [one_brief])
    assert any("expected str" in v for v in validate.check_field_schema())


def test_phases_check_catches_a_wrong_phase_count(monkeypatch, one_brief):
    one_brief["phases"] = one_brief["phases"][:3]
    monkeypatch.setattr(validate, "projects", lambda: [one_brief])
    assert any("phases, expected exactly" in v for v in validate.check_phases())


def test_gates_check_catches_too_few_metrics(monkeypatch, one_brief):
    one_brief["metrics"] = ["only one"]
    monkeypatch.setattr(validate, "projects", lambda: [one_brief])
    assert any("gate metrics, minimum" in v for v in validate.check_gates())


def test_identity_check_catches_a_duplicate_codename(monkeypatch, one_brief):
    twin = copy.deepcopy(one_brief)
    twin["id"] = one_brief["id"] + 1
    monkeypatch.setattr(validate, "projects", lambda: [one_brief, twin])
    assert any("duplicate code" in v for v in validate.check_identity())


def test_identity_check_catches_a_hole_in_the_numbering(monkeypatch, one_brief):
    gap = copy.deepcopy(one_brief)
    gap["id"], gap["code"] = one_brief["id"] + 2, "OTHER"
    gap["name"] = one_brief["name"] + " (other)"
    monkeypatch.setattr(validate, "projects", lambda: [one_brief, gap])
    assert any("not contiguous" in v for v in validate.check_identity())


def test_files_check_catches_an_orphan_page(monkeypatch):
    """`render.py --check` only looks at files it would write, so orphans need this."""
    subset = validate.projects()[:5]
    monkeypatch.setattr(validate, "projects", lambda: subset)
    violations = validate.check_files()
    assert any("belongs to no brief" in v for v in violations)


def test_sections_check_catches_a_missing_page(monkeypatch, one_brief):
    one_brief["code"] = "NOSUCHBRIEF"
    monkeypatch.setattr(validate, "projects", lambda: [one_brief])
    assert any("no rendered page" in v for v in validate.check_sections())


def test_links_check_catches_a_broken_link(monkeypatch, tmp_path):
    page = tmp_path / "page.md"
    page.write_text("see [the plan](does-not-exist.md) and [lantern](https://example.invalid)\n")
    monkeypatch.setattr(validate, "markdown_files", lambda: [page])
    monkeypatch.setattr(validate, "ROOT", tmp_path)
    violations = validate.check_links()
    assert len(violations) == 1 and "does-not-exist.md" in violations[0]


def test_upgrades_check_catches_a_dangling_reference(monkeypatch):
    real = validate.render.load_upgrades()
    broken = copy.deepcopy(real)
    broken[1]["links"] = [9999]
    monkeypatch.setattr(validate.render, "load_upgrades", lambda: broken)
    assert any("unknown brief 9999" in v for v in validate.check_upgrades())


def test_readme_claims_check_catches_a_stale_count(monkeypatch, tmp_path):
    (tmp_path / "README.md").write_text(
        "   999 projects  *  16 tracks  *  x\n\n"
        "**999 build-ready project briefs**\n\n"
        "```text\n   by the numbers\n     briefs = 999    tracks = 16\n```\n"
    )
    monkeypatch.setattr(validate, "ROOT", tmp_path)
    violations = validate.check_readme_claims()
    assert len(violations) >= 3, violations
    assert all("999" in v for v in violations), violations


def test_capacity_check_catches_a_stale_report(monkeypatch, tmp_path):
    src = ROOT / "master" / "nationstack"
    dst = tmp_path / "master" / "nationstack"
    dst.mkdir(parents=True)
    (dst / "capacity_model.py").write_text((src / "capacity_model.py").read_text())
    (dst / "capacity.md").write_text("stale\n")
    monkeypatch.setattr(validate, "ROOT", tmp_path)
    assert any("is stale" in v for v in validate.check_capacity_model())
