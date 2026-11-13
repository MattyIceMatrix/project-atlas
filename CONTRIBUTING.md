# Adding or changing a brief

```text
   edit tracks/<track>.yaml  ->  python tools/render.py  ->  pytest  ->  commit both
```

Every brief needs all fields listed in `tools/render.py` (`REQUIRED`), exactly four phases, at least two
"defend it" questions, ASCII art no wider than 100 characters, and an ethics line.

Retiring a brief: move it to a `retired:` list in its track file instead of deleting it, so numbering stays stable.
