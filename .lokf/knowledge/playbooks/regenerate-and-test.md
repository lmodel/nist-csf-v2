---
type: Playbook
id: https://w3id.org/lmodel/nist-csf-v2/knowledge/playbooks/regenerate-and-test
genre: how-to
title: Regenerate and test after a schema change
description: "How to change the schema and check it: `uv sync --group dev`, edit `src/nist_csf_v2/schema/nist_csf_v2.yaml`, then `just lint`, `just gen-project`, `just gen-doc`, `just lokf-adapt` and `just test`, and the pre-commit hooks before a pull request."
resource: CONTRIBUTING.md
about:
  - https://w3id.org/lmodel/nist-csf-v2/knowledge/datasets/nist-csf-v2-linkml-schema
sources:
  - id: contributing.md
    resource: CONTRIBUTING.md
    title: the Development setup and Before opening a pull request sections
  - id: justfile
    resource: justfile
    title: the lint, gen-project, gen-doc and test recipes
  - id: project.justfile
    resource: project.justfile
    title: the lokf-adapt recipes
generated:
  by: process:ktl-librarian
  at: "2026-10-29T21:41:10Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-30T08:31:58Z"
---

# Regenerate and test after a schema change

1. Install the toolchain once: Python 3.10 or later, `uv` and `just`, then `uv sync --group dev` in the clone.[^contributing.md]
2. Edit `src/nist_csf_v2/schema/nist_csf_v2.yaml`. It is the one file to write by hand; `project/`, `src/nist_csf_v2/datamodel/`, `docs/schema/` and `.lokf/nist-csf-v2.yaml` are generated from it. Say in the pull request which part of CSWP 29 a new or changed element renders.
3. Run `just lint`, which runs `linkml-lint --ignore-warnings` under `.linkmllint.yaml`.[^justfile]
4. Run `just gen-project` and `just gen-doc`, then `just lokf-adapt`, which rewrites the adapt copy with the three roots.[^project.justfile] Commit the output.
5. Add an example under `tests/data/valid/` for a new class and a counter-example under `tests/data/invalid/` for a new constraint, named `ClassName-suffix.yaml`, then run `just test`.
6. Run the pre-commit hooks on what you staged (`uvx pre-commit run`), and write a changelog entry under `## [Unreleased]` when the change alters behaviour.

CI runs the same: `main.yaml` runs `just lint`, `just test` and `just lokf-adapt-check`, and fails when the adapt copy is stale.

[^contributing.md]: CONTRIBUTING.md, Development setup and Before opening a pull request
[^justfile]: justfile, the lint recipe
[^project.justfile]: project.justfile, lokf-adapt and lokf-adapt-check
