---
type: Service
id: https://w3id.org/lmodel/nist-csf-v2/knowledge/workflows/knowledge-sync
genre: reference
title: Knowledge sync (knowledge-sync.yaml)
description: "The Knowledge sync workflow, `.github/workflows/knowledge-sync.yaml`: every Monday at 04:10 UTC and by hand, it moves the sidecar's copies and the skills pin to the newest Knowledge Trust Ladder release through one pull request, opened with the `KNOWLEDGE_SYNC_TOKEN` secret, and holds the workflow changes for a person to approve."
resource: .github/workflows/knowledge-sync.yaml
sources:
  - id: knowledge-sync.yaml
    resource: .github/workflows/knowledge-sync.yaml
    title: the header comment, the on key and the jobs
generated:
  by: process:ktl-librarian
  at: "2026-10-29T21:41:10Z"
status: draft
---

# Knowledge sync (knowledge-sync.yaml)

`.github/workflows/knowledge-sync.yaml` is the workflow named "Knowledge sync", a copy of the ktl-sidecar template. It runs by hand, and every Monday at 04:10 UTC so that the librarian's Monday run follows a current pin once its pull request is merged.[^knowledge-sync.yaml] Its `earlier` job finds a pull request it opened before. Its `sync` job reads the newest release of the skills repository through `.lokf/scripts/knowledge-sync.sh` and the release's `knowledge-sync.manifest`, and writes the copies that differ. Its `publish` job opens or refreshes one pull request from `.github/PULL_REQUEST_TEMPLATE/knowledge-sync.md` with the `KNOWLEDGE_SYNC_TOKEN` secret, which belongs in the `knowledge-sync` Environment. Without the secret, it attaches the patch to the run instead. A `review` job holds a change to the workflows in the Environment `KNOWLEDGE_SYNC_REVIEW_ENVIRONMENT` names, for a person to approve.

[^knowledge-sync.yaml]: .github/workflows/knowledge-sync.yaml, the header comment, the on key and the jobs
