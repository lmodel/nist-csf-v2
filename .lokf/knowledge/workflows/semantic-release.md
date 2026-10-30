---
type: Service
id: https://w3id.org/lmodel/nist-csf-v2/knowledge/workflows/semantic-release
genre: reference
title: Semantic release (semantic-release.yml)
description: "The Semantic release workflow, `.github/workflows/semantic-release.yml`: on a pull request into main, its plan job checks that the commits, the changelog and the title would release and previews the release; on a push to main, its release job in the release Environment tags vX.Y.Z, publishes the GitHub release and dispatches Knowledge Release."
resource: .github/workflows/semantic-release.yml
sources:
  - id: semantic-release.yml
    resource: .github/workflows/semantic-release.yml
    title: the header comment, the on key and the jobs
generated:
  by: process:ktl-librarian
  at: "2026-10-29T21:41:10Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-30T08:31:58Z"
---

# Semantic release (semantic-release.yml)

`.github/workflows/semantic-release.yml` is the workflow named "Semantic release". On a pull request into `main`, opened, updated, reopened or retitled, its read-only `plan` job installs pinned semantic-release packages and, when the commits carry a releasing type, refuses to go on without a `v*` tag, refuses an empty `## [Unreleased]` section, refuses a title without a releasing type, and previews the release with `--dry-run`.[^semantic-release.yml] On a push to `main`, its `release` job runs in the `release` Environment with `contents: write` and `actions: write`, runs semantic-release, which promotes the changelog, tags and publishes the release as `github-actions[bot]`, and then dispatches [Knowledge Release](knowledge-release.md) for the tag once `KNOWLEDGE_RELEASE_ENABLED` is `true`. [Cut a release](../playbooks/release.md) says how the pieces fit.

[^semantic-release.yml]: .github/workflows/semantic-release.yml, the header comment, the on key and the jobs
