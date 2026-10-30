---
type: Service
id: https://w3id.org/lmodel/nist-csf-v2/knowledge/workflows/knowledge-librarian
genre: reference
title: Knowledge Librarian (knowledge-librarian.yaml)
description: "The Knowledge Librarian workflow, `.github/workflows/knowledge-librarian.yaml`: every Monday at 05:00 UTC and by hand, once `KNOWLEDGE_LIBRARIAN_ENABLED` is true, it runs an agent with the ktl-librarian skill (pinned by `TRUST_LADDER_SKILLS_REF` at v0.59.0) in a read-only job and opens a review pull request from a separate job that runs no agent."
resource: .github/workflows/knowledge-librarian.yaml
sources:
  - id: knowledge-librarian.yaml
    resource: .github/workflows/knowledge-librarian.yaml
    title: the header comment, the on key and the jobs
generated:
  by: process:ktl-librarian
  at: "2026-10-29T21:41:10Z"
status: draft
---

# Knowledge Librarian (knowledge-librarian.yaml)

`.github/workflows/knowledge-librarian.yaml` is the workflow named "Knowledge Librarian", a copy of the ktl-sidecar template. It runs every Monday at 05:00 UTC and by hand, and does nothing until the repository variable `KNOWLEDGE_LIBRARIAN_ENABLED` is `true`.[^knowledge-librarian.yaml] Its `earlier` job finds a pull request it opened before, so that it never opens a second one. Its `refresh` job checks the repository out with `persist-credentials: false`, installs the ktl-librarian skill at `TRUST_LADDER_SKILLS_REF`, `v0.59.0`, checked against `TRUST_LADDER_SKILLS_SHA`, runs the agent through `.lokf/scripts/knowledge-librarian.sh`, and hands on a patch. Its `publish` job runs no agent: it applies the patch on a clean checkout, confines it to the bundle, refuses a change to a person's record, and opens the review pull request. A scheduled week with nothing waiting runs no agent, except in a month's first seven days.

[^knowledge-librarian.yaml]: .github/workflows/knowledge-librarian.yaml, the header comment, the on key and the jobs
