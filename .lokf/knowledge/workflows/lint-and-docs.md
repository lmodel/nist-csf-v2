---
type: Service
id: https://w3id.org/lmodel/nist-csf-v2/knowledge/workflows/lint-and-docs
genre: reference
title: Lint & docs (lint-and-docs.yaml)
description: "The Lint & docs workflow, `.github/workflows/lint-and-docs.yaml`: on a push to main, every pull request, a Monday 06:00 UTC schedule and by hand, four jobs run ShellCheck, actionlint, the word budgets of CONTRIBUTING.md (1000) and SECURITY.md (900), and markdownlint, lychee and codespell over the Markdown."
resource: .github/workflows/lint-and-docs.yaml
sources:
  - id: lint-and-docs.yaml
    resource: .github/workflows/lint-and-docs.yaml
    title: the header comment, the on key and the jobs
generated:
  by: process:ktl-librarian
  at: "2026-10-29T21:41:10Z"
status: draft
---

# Lint & docs (lint-and-docs.yaml)

`.github/workflows/lint-and-docs.yaml` is the workflow named "Lint & docs". It runs on a push to `main`, on every pull request, every Monday at 06:00 UTC to catch link rot, and by hand.[^lint-and-docs.yaml] Its four read-only jobs are `lint-scripts`, which runs ShellCheck over the tree, `lint-workflows`, which runs actionlint, `word-budgets`, which fails when `CONTRIBUTING.md` passes 1000 words or `SECURITY.md` 900, and `validate-markdown`, which runs markdownlint under `.markdownlint-cli2.jsonc`, lychee under `lychee.toml` with this repository's own links on `main` remapped to the checkout, and codespell over every tracked Markdown file.

[^lint-and-docs.yaml]: .github/workflows/lint-and-docs.yaml, the header comment, the on key and the jobs
