---
type: Service
id: https://w3id.org/lmodel/nist-csf-v2/knowledge/workflows/knowledge-release
genre: reference
title: Knowledge Release (knowledge-release.yaml)
description: "The Knowledge Release workflow, `.github/workflows/knowledge-release.yaml`: dispatched with a release's tag, or started by a published release once `KNOWLEDGE_RELEASE_ENABLED` is true, it attaches the bundle zip, the domain schema as `schema-<tag>-nist-csf-v2.yaml` with its checksum, and the Copilot skills to the release, when the bundle or the schema changed or `force` is set."
resource: .github/workflows/knowledge-release.yaml
sources:
  - id: knowledge-release.yaml
    resource: .github/workflows/knowledge-release.yaml
    title: the header comment, the on key and the jobs
generated:
  by: process:ktl-librarian
  at: "2026-10-29T21:41:10Z"
status: draft
---

# Knowledge Release (knowledge-release.yaml)

`.github/workflows/knowledge-release.yaml` is the workflow named "Knowledge Release", a copy of the ktl-sidecar template. It runs when dispatched by hand with a tag, and on each published release once the repository variable `KNOWLEDGE_RELEASE_ENABLED` is `true`.[^knowledge-release.yaml] Its `release` job resolves the tag. Its `pack` job, under a read-only token, validates the bundle against the domain schema, runs the conventions script, and builds:

- the bundle zip;
- the schema copy named `schema-<tag>-nist-csf-v2.yaml`, with its `.sha256`;
- one Copilot skill zip per instructions file under `.lokf/m365/`.

The `pack` job skips a release whose bundle and schema match the last one released, unless `force` is set. Its `attach` job alone can write: it uploads the assets to the release. `KNOWLEDGE_RELEASE_NAME` names the assets when the repository's name is not wanted.

[^knowledge-release.yaml]: .github/workflows/knowledge-release.yaml, the header comment, the on key and the jobs
