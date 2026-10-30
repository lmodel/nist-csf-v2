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
  - id: release-tools
    resource: .github/release
    title: the release tools' package.json and package-lock.json
generated:
  by: process:ktl-librarian
  at: "2026-10-30T09:08:01Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-30T08:31:58Z"
---

# Semantic release (semantic-release.yml)

`.github/workflows/semantic-release.yml` is the workflow named "Semantic release". Its read-only `plan` job runs when a pull request into `main` is opened, updated, reopened or retitled, and installs semantic-release and its plugins from `.github/release/package-lock.json` with `npm ci --ignore-scripts`, as the `release` job does.[^release-tools] When the commits carry a releasing type, it refuses to go on without a `v*` tag, with an empty `## [Unreleased]` section or with a title that has no releasing type, and it previews the release with `--dry-run`.[^semantic-release.yml] On a push to `main`, its `release` job runs in the `release` Environment with `contents: write` and `actions: write`. It runs semantic-release, which promotes the changelog, then tags and publishes the release as `github-actions[bot]`. It then dispatches [Knowledge Release](knowledge-release.md) for the tag once `KNOWLEDGE_RELEASE_ENABLED` is `true`. [Cut a release](../playbooks/release.md) says how the pieces fit.

[^semantic-release.yml]: .github/workflows/semantic-release.yml, the header comment, the on key and the jobs
[^release-tools]: .github/release, package.json and package-lock.json
