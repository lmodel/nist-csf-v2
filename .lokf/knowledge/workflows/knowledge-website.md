---
type: Service
id: https://w3id.org/lmodel/nist-csf-v2/knowledge/workflows/knowledge-website
genre: reference
title: Knowledge website (knowledge-website.yaml)
description: "The Knowledge website workflow, `.github/workflows/knowledge-website.yaml`: on pushes and pull requests that touch the site's sources, every Monday at 05:23 UTC and by hand, its build job builds `website/` and checks its links read-only, and its deploy job publishes the default branch's build to GitHub Pages once `KNOWLEDGE_WEBSITE_ENABLED` is true."
resource: .github/workflows/knowledge-website.yaml
sources:
  - id: knowledge-website.yaml
    resource: .github/workflows/knowledge-website.yaml
    title: the header comment, the on key and the jobs
generated:
  by: process:ktl-librarian
  at: "2026-11-15T03:07:39Z"
status: draft
---

# Knowledge website (knowledge-website.yaml)

`.github/workflows/knowledge-website.yaml` is the workflow named "Knowledge website", which the ktl-website skill installed. It runs on a push to the default branch and on a pull request, each when it touches one of the site's sources, every Monday at 05:23 UTC, and by hand. The sources are `website/`, `.lokf/`, `knowledge_bundle/`, the README, `docs/`, `.assets/`, the changelog, `.linkml/`, `src/*/schema/`, this workflow and `knowledge-federation.yaml`.[^knowledge-website.yaml] Its `build` job runs under a read-only token. It:

- checks the repository out with its full history, since the health page's "a source moved" lines come from git;
- sets up uv;
- finds the site's folder: `website/`, or `ktl-website/` when that folder holds a `site.toml`;
- installs `just` when `site.toml` builds its data with it;
- runs `scripts/build.sh` in that folder, which runs `lokf export` and LinkML's `gen-doc` from the toolkit `.lokf/uv.lock` pins, then Hugo and Pagefind from the site's own `uv.lock`, cleans the raw HTML and checks the links;
- uploads the folder's `dist/` as the Pages artifact.

Its `deploy` job holds `pages: write` and `id-token: write` in the `github-pages` Environment, and runs only from the default branch once the repository variable `KNOWLEDGE_WEBSITE_ENABLED` is `true`. It warns when the repository is private and its Pages site is public or of unknown visibility. [Documentation site](../services/documentation-site.md) describes what it publishes.

[^knowledge-website.yaml]: .github/workflows/knowledge-website.yaml, the header comment, the on key and the jobs
