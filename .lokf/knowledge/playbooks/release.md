---
type: Playbook
id: https://w3id.org/lmodel/nist-csf-v2/knowledge/playbooks/release
genre: how-to
title: Cut a release
description: "How a release is made: Conventional Commits on `main`, an `## [Unreleased]` changelog section, the `v0.0.0` baseline tag that keeps the first release at 0.1.0, and `semantic-release.yml`, which tags the release and dispatches Knowledge Release to attach `schema-<tag>-nist-csf-v2.yaml` once `KNOWLEDGE_RELEASE_ENABLED` is true."
resource: .releaserc.json
sources:
  - id: releaserc.json
    resource: .releaserc.json
    title: the commit analyzer's rules and the plugins
  - id: contributing.md
    resource: CONTRIBUTING.md
    title: the Releasing (maintainers) section
  - id: changelog.md
    resource: CHANGELOG.md
    title: the paragraph on the baseline tag
  - id: changelog-release.mjs
    resource: .github/scripts/changelog-release.mjs
    title: the check, notes and promote commands
generated:
  by: process:ktl-librarian
  at: "2026-10-29T21:41:10Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-30T09:04:56Z"
---

# Cut a release

1. Write the change under `## [Unreleased]` in `CHANGELOG.md` as you go. The release job refuses an empty section, through `.github/scripts/changelog-release.mjs check`.[^changelog-release.mjs]
2. Type each commit with a Conventional Commits type. Only `feat:`, `fix:`, `security:` and a breaking `!` start a release. A pull request that would release carries a releasing type in its title too, since a squash merge takes its subject from it.[^contributing.md]
3. Before the first releasing merge, push the `v0.0.0` baseline tag on `main`. Both release jobs refuse to run without a `v*` tag, because semantic-release would otherwise start at 1.0.0. The changelog says that the baseline is not a release and that the first release is 0.1.0.[^changelog.md]
4. Merge. [Semantic release](../workflows/semantic-release.md) retitles the section with the version and the date, commits `CHANGELOG.md`, tags `vX.Y.Z` and publishes the GitHub release.

`.releaserc.json` uses the `conventionalcommits` preset, maps a breaking change to a minor release and `security` to a patch, and commits `CHANGELOG.md` with the message `chore(release): <version> - changelog promoted [skip ci]`.[^releaserc.json] No file carries the version. Once `KNOWLEDGE_RELEASE_ENABLED` is `true`, the release job dispatches [Knowledge Release](../workflows/knowledge-release.md), which attaches the bundle and the schema copy.

[^changelog-release.mjs]: .github/scripts/changelog-release.mjs, the check command
[^contributing.md]: CONTRIBUTING.md, Releasing (maintainers)
[^changelog.md]: CHANGELOG.md, the paragraph on the v0.0.0 tag
[^releaserc.json]: .releaserc.json, the plugins
