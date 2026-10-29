---
type: Service
id: https://w3id.org/lmodel/nist-csf-v2/knowledge/services/documentation-site
genre: reference
title: Documentation site
description: "The Astro Starlight site in `website/`, for <https://lmodel.github.io/nist-csf-v2>: the README as its home page, the pages of `docs/`, the schema's element pages, a page per concept of this bundle with its trust label, and the bundle's exports, built and published by Knowledge website."
resource: website
endpoint: https://lmodel.github.io/nist-csf-v2
documentation: website/README.md
sources:
  - id: site.config.mjs
    resource: website/site.config.mjs
    title: the values and options
  - id: website-readme.md
    resource: website/README.md
    title: what each page is built from
generated:
  by: process:ktl-librarian
  at: "2026-10-29T21:41:10Z"
status: draft
---

# Documentation site

`website/` holds an Astro Starlight site. `website/site.config.mjs` names the repository `lmodel/nist-csf-v2`, the site `https://lmodel.github.io` with the base path `/nist-csf-v2`, and the title `nist-csf-v2`.[^site.config.mjs] It shows the pages of `docs/` but `docs/templates-linkml/`, and it redirects the addresses the retired mkdocs site gave its pages: `/elements` and every page under it to `/schema/`, and `/about` to `/docs/about/`. The other options take the site's defaults: the Knowledge Trust Ladder logo, the README as the home page, the changelog once it holds a release, and the schema's pages that `just gen-doc` writes.

`website/README.md` says what each page is built from, and that `npm run build` syncs the bundle, the README, the docs and the schema's pages before it builds and checks every link.[^website-readme.md] [Knowledge website](../workflows/knowledge-website.md) builds the site on each change to its sources and publishes it once `KNOWLEDGE_WEBSITE_ENABLED` is `true`.

[^site.config.mjs]: website/site.config.mjs, REPO, SITE, BASE, TITLE, DOCS and REDIRECTS
[^website-readme.md]: website/README.md, the build and its sources
