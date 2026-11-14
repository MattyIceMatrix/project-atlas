# Adding or changing a brief

```text
   edit tracks/<track>.yaml  ->  python tools/render.py  ->  pytest  ->  commit both
```

Every brief needs all fields listed in `tools/render.py` (`REQUIRED`), exactly four phases, at least two
"defend it" questions, ASCII art no wider than 100 characters, and an ethics line.

Retiring a brief: move it to a `retired:` list in its track file instead of deleting it, so numbering stays stable.

## The schema

`tools/schema.py` is the single declarative description of a brief: every field, its type, its minimum
size, and the tier that requires it (all briefs / level-5 / frontier / grand master). Add a field there
before you use it in a track file — anything not listed is reported as a typo.

## Checks

```text
   python tools/validate.py          11 checks: schema, numbering, track files, phase order,
                                     gates, page sections, orphan pages, internal links,
                                     upgrade references, README counts, capacity report
   python tools/render.py --check    the pages match the data that generated them
   pytest -q                         both of the above, per check, plus negative tests
                                     that prove each check still bites
```

Two things to watch for when editing YAML:

- **A colon inside an unquoted list item makes a dict, not a string.** `- User study: does it help?`
  parses as `{'User study': 'does it help?'}` and renders as that literal text on the page. Quote it:
  `- "User study: does it help?"`. `python tools/validate.py` catches this.
- **If you change a count the README states out loud** (briefs, tracks, level-5, tier sizes), update the
  banner, the opening paragraph and the "by the numbers" block. CI fails if any of them disagree with
  `tracks/*.yaml`.
