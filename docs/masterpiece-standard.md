# The Masterpiece Standard

```text
         _______________________________________________
        |  M A S T E R P I E C E    S T A N D A R D     |
        |_______________________________________________|
        |                                               |
        |   a project is a masterpiece when a stranger  |
        |   can clone it, run it, trust its numbers,    |
        |   and build on it without asking you a thing  |
        |_______________________________________________|
               |||                           |||
```

Every project in the atlas, at every level, aims at this bar. Level 1–4 projects meet the **core** items;
level-5 masterpieces meet **all** of them.

## The twelve pillars

```text
   1 PROBLEM     2 REQUIREMENTS   3 ARCHITECTURE   4 CODE QUALITY
   5 TESTING     6 EVALUATION     7 SECURITY       8 PRIVACY & ETHICS
   9 OPERATIONS 10 RELEASE       11 DOCUMENTATION 12 PROOF OF IMPACT
```

### 1. Problem (core)
- A one-paragraph problem statement with a real user and a source for every claim.
- A ConOps or user-journey document for level 5.

### 2. Requirements (core)
- Numbered, testable requirements (`REQ-xxx`), each with a verification method.
- Level 5: traceability matrix from requirement to test to result.

### 3. Architecture (core)
- A diagram (C4 context + container) and at least one ADR.
- Level 5: quality-attribute targets (latency, availability, energy, cost) with measurements.

### 4. Code quality (core)
- Linting and formatting in CI, type checking where the language supports it.
- Conventional commits, protected main branch, reviews (even self-reviews with a checklist).

### 5. Testing (core)
- Unit tests in CI; integration tests for every external boundary.
- Level 5: property-based or fuzz tests for parsers and policy code; hardware-in-the-loop where hardware exists.

### 6. Evaluation (core)
- Frozen test sets, data cards and model cards.
- Every number has date, git commit, hardware and configuration.
- Level 5: confidence intervals or repeated runs; failure gallery; comparison to a strong baseline.

### 7. Security (core)
- Threat model (STRIDE or similar), secret scanning, dependency audit, SBOM.
- Level 5: signed releases and provenance (SLSA-style), security policy with disclosure process.

### 8. Privacy and ethics (core)
- Data minimisation, licences checked, ethics line honoured.
- Level 5: DPIA when personal data is involved; independent review by someone outside the project.

### 9. Operations
- Runbook, logs, metrics and alerts for anything that runs continuously.
- Level 5: SLOs, chaos or failure-injection test, backup and restore proven.

### 10. Release
- Semantic versioning, changelog, reproducible build.
- Level 5: release checklist, artifacts with checksums, citation file.

### 11. Documentation
- README that gets a stranger from clone to demo in under 15 minutes.
- Level 5: docs site, tutorials, contributor guide, governance, code of conduct.

### 12. Proof of impact
- Demo video or GIF, honest limits section.
- Level 5: external validation: a partner pilot, a paper or workshop submission, or a public benchmark result.

## The masterpiece checklist (level 5)

```text
  [ ] ConOps + requirements + traceability
  [ ] C4 diagrams + ADRs + quality-attribute measurements
  [ ] CI: lint, types, tests, security scans, SBOM
  [ ] frozen evals with CIs, model and data cards, failure gallery
  [ ] threat model, signed releases, security policy
  [ ] DPIA (if personal data), outside ethics/safety review
  [ ] runbook, SLOs, failure-injection test
  [ ] reproducible release with changelog and citation
  [ ] docs site + 15-minute quick start
  [ ] external proof: pilot, paper, or public benchmark
```

LANTERN is the reference implementation of this standard: copy its `docs/` and `.github/` skeleton to start any new project.
