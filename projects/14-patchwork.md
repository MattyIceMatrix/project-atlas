# 14 · PATCHWORK

```text
    PR #42  ------>  [ reviewer agent ]
                        |         |
                   comment    failing test  --> CI shows red --> fix --> green
```

**Code-review agent that writes the missing tests**

> Reviews the PR, then proves its own comments with a failing test.

```text
  TRACK B GENERATIVE AI AND LLM SYSTEMS  |  LEVEL [###..]  |  ~3 MONTHS  |  BUDGET €0–20/month
```

## The mission

Review bots leave vague comments; developers ignore them.

## How it works

```text
+----------------------------------------+
|  diff                                  |
+----------------------------------------+
                    |
                    v
+----------------------------------------+
|  risk analysis                         |
+----------------------------------------+
                    |
                    v
+----------------------------------------+
|  generated test that fails on the bug  |
+----------------------------------------+
                    |
                    v
+----------------------------------------+
|  PR comment with the test              |
+----------------------------------------+
```

## Kit

- GitHub Actions
- Python
- pytest
- LLM API or local model

**Hardware:** None (CI)

## Campaign

```text
  P1  [=====]                     m0-0.8    Benchmark on known bug-fix commits
  P2        [=====]               m0.8-1.5  Test generation that must fail before the fix
  P3              [=====]         m1.5-2.2  GitHub App or Action integration
  P4                    [=====]   m2.2-3    Measure useful-comment rate on your own repos
```

## Gate: done when you can show

```text
  [ ] bugs caught with a failing test
  [ ] false-alarm comments
  [ ] cost per PR
  [ ] every number above measured, dated and tied to a git commit
  [ ] README with a demo GIF or video
  [ ] honest limits section
```

## Safety and ethics

Runs only on repositories where the owner installs it.

## Resume line (fill with your measured numbers)

> Built a review agent that backs [N]% of its findings with a failing test, cutting noise by [N]%.

**Skills it proves:** agents · testing · CI/CD

## Defend it

1. Why require a failing test?
2. What stops the agent from running untrusted code unsafely?

## Launch checklist

```text
  [ ] create the repo  MattyIceMatrix/patchwork  from this brief
  [ ] copy the engineering skeleton from LANTERN (requirements, test plan, ADR template, CI)
  [ ] write a data card for every dataset before training anything
  [ ] set a weekly build slot and a first gate date
```

---

[<- ECHO](13-echo.md) · [atlas index](../README.md) · [GRANITE ->](15-granite.md)
