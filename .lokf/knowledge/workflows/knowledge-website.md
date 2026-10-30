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
  at: "2026-10-29T21:41:10Z"
status: draft
---

# Knowledge website (knowledge-website.yaml)

`.github/workflows/knowledge-website.yaml` is the workflow named "Knowledge website", a copy of the ktl-website template. It runs on a push to the default branch, every Monday at 05:23 UTC, by hand, and on a pull request that touches `website/`, `.lokf/`, the README, `docs/`, the changelog, `llms.txt`, a justfile, a `pyproject.toml` or a `uv.lock`.[^knowledge-website.yaml] Its `build` job runs under a read-only token. It:

- checks the repository out with its full history;
- installs the sidecar's toolkit with `uv sync --locked`;
- links the `just` the sidecar's lock pins, when the site builds a folder with it;
- runs `npm ci --ignore-scripts` and `npm run build`, which syncs the pages, builds the site and checks every link;
- uploads `website/dist` as the Pages artifact.

Its `deploy` job holds `pages: write` and `id-token: write` in the `github-pages` Environment, and runs only from the default branch once the repository variable `KNOWLEDGE_WEBSITE_ENABLED` is `true`. [Documentation site](../services/documentation-site.md) describes what it publishes.

[^knowledge-website.yaml]: .github/workflows/knowledge-website.yaml, the header comment, the on key and the jobs
