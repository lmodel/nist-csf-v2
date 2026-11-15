---
type: Service
id: https://w3id.org/lmodel/nist-csf-v2/knowledge/services/documentation-site
genre: reference
title: Documentation site
description: "The Hugo site in `website/`, for <https://lmodel.github.io/nist-csf-v2>: the README as its home page, the pages of `docs/`, the schema's element pages, a page per concept of this bundle with its trust label, and the bundle's exports, built and published by Knowledge website."
resource: website
endpoint: https://lmodel.github.io/nist-csf-v2
documentation: website/README.md
sources:
  - id: site.toml
    resource: website/site.toml
    title: the site's address, title and redirects
  - id: hugo.toml
    resource: website/hugo.toml
    title: docsExclude
  - id: content.gotmpl
    resource: website/content/_content.gotmpl
    title: the redirects
  - id: prepare.sh
    resource: website/scripts/prepare.sh
    title: the schema's pages
  - id: website-readme.md
    resource: website/README.md
    title: what each page is built from
generated:
  by: process:ktl-librarian
  at: "2026-11-15T03:07:39Z"
status: draft
---

# Documentation site

`website/` holds a Hugo site. `website/site.toml` names the repository `lmodel/nist-csf-v2`, the address `https://lmodel.github.io/nist-csf-v2/` and the title `nist-csf-v2`, and sets no logo, so the site shows the Knowledge Trust Ladder logo.[^site.toml] It shows the pages of `docs/` except `docs/templates-linkml/` and `docs/elements/`, which `website/hugo.toml` leaves out.[^hugo.toml] It redirects the addresses the retired mkdocs site gave its pages:

- `/elements` to `/schema/`;
- each class page of the retired schema to its successor's page, or to `/schema/` where it has none;
- any other page under `/elements` whose name the schema still has to that element's page under `/schema/`;
- `/about` to `/docs/about/`.

It also sends each `/schema/<name>/` address to that element's page under its kind's folder, such as `/schema/classes/CsfFunction/`.[^content.gotmpl]

`website/scripts/prepare.sh` runs LinkML's `gen-doc` on `src/nist_csf_v2/schema/nist_csf_v2.yaml` and writes the schema's pages into `website/generated/`, which is never committed.[^prepare.sh]

`website/README.md` says what each page is built from: the README becomes the home page, and the changelog a page per release. It also says that `scripts/build.sh` in `website/` writes `dist/` with the search index and then checks every link between its pages, and that Hugo and Pagefind come from PyPI, at the versions `pyproject.toml` names and the hashes `uv.lock` holds.[^website-readme.md] [Knowledge website](../workflows/knowledge-website.md) builds the site on each change to its sources and publishes it once `KNOWLEDGE_WEBSITE_ENABLED` is `true`.

[^site.toml]: website/site.toml, the site's address, title and redirects
[^hugo.toml]: website/hugo.toml, docsExclude
[^content.gotmpl]: website/content/_content.gotmpl, the redirects
[^prepare.sh]: website/scripts/prepare.sh, the schema's pages
[^website-readme.md]: website/README.md, what each page is built from
