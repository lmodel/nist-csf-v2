---
type: Service
id: https://w3id.org/lmodel/nist-csf-v2/knowledge/workflows/knowledge-registrar
genre: reference
title: Knowledge Registrar (knowledge-registrar.yaml)
description: "The Knowledge Registrar workflow, `.github/workflows/knowledge-registrar.yaml`: the gate on the knowledge bundle, run on pull requests that touch `.lokf/` or `knowledge_bundle/`, every Monday at 06:00 UTC and by hand; it validates the bundle and its relation targets against the domain schema, runs the conventions script, and checks that each new confirmation by a person is backed by an approval or a signed commit."
resource: .github/workflows/knowledge-registrar.yaml
sources:
  - id: knowledge-registrar.yaml
    resource: .github/workflows/knowledge-registrar.yaml
    title: the header comment, the on key and the jobs
generated:
  by: process:ktl-librarian
  at: "2026-10-29T21:41:10Z"
status: draft
---

# Knowledge Registrar (knowledge-registrar.yaml)

`.github/workflows/knowledge-registrar.yaml` is the workflow named "Knowledge Registrar", a copy of the ktl-sidecar template. It runs on pull requests that touch `.lokf/` or `knowledge_bundle/`, every Monday at 06:00 UTC and by hand.[^knowledge-registrar.yaml] Its `validate` job installs the sidecar's toolkit with `uv sync --locked`, runs `just lokf-validate` and `just lokf-check-refs` against the domain schema the sidecar's justfile names, and runs `.lokf/scripts/knowledge-conventions.sh`. Its `provenance` job reads the pull request's reviews and commits to check that each new `human:` confirmation is backed by that person's approval or signed commit, and an optional `attestation` job runs in the Environment `KNOWLEDGE_CURATION_ENVIRONMENT` names, when it is set. Every job holds a read-only token.

[^knowledge-registrar.yaml]: .github/workflows/knowledge-registrar.yaml, the header comment, the on key and the jobs
