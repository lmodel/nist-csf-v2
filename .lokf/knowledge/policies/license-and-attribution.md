---
type: Policy
id: https://w3id.org/lmodel/nist-csf-v2/knowledge/policies/license-and-attribution
genre: reference
title: License and attribution
description: "The repository's licences: Apache 2.0 for the schema and the code, NIST's public-domain and CC0 terms for the CSF catalog copy, NIST's statement that its Technical Series publications are not subject to copyright in the United States, MIT for the copier template's scaffolding, and Apache 2.0 for the KTL sidecar and website templates."
resource: NOTICE
sources:
  - id: notice
    resource: NOTICE
    title: every section
  - id: license
    resource: LICENSE
    title: the Apache License 2.0
  - id: readme.md
    resource: README.md
    title: the License section
  - resource: website/NOTICE
    title: the part adapted from the LOKF toolkit's site
generated:
  by: process:ktl-librarian
  at: "2026-10-29T21:41:10Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-30T08:31:58Z"
---

# License and attribution

The schema and the code are under the Apache License, Version 2.0.[^license] NOTICE lists the third-party work the repository carries.[^notice]

- The schema, the generated models and `project/` render the CSF 2.0 in the project's own words, with NIST as the source of the definitions. NOTICE says that CSWP 29 carries no licence statement of its own and refers readers to NIST's Technical Series policies. It cites NIST's statement on its works, read on 2026-10-29: such a publication is a work of the United States Government and is not subject to copyright protection in the United States, but it may be subject to copyright in other countries.
- NIST's catalog in `src/nist_csf_v2/schema/oscal-content/` is in the public domain within the United States, and NIST dedicates it to the worldwide public domain under CC0 1.0. It keeps NIST's `LICENSE.md` beside it.
- The justfile, configuration and documentation scaffolding derive from linkml-project-copier, under the MIT License, whose text NOTICE carries.
- The sidecar's scripts and workflows are copies of the ktl-sidecar templates, and the site under `website/` derives from the ktl-website templates, all under the Apache License 2.0. `website/NOTICE` lists the part adapted from the LOKF toolkit's site.

The README adds that this is not an official NIST project, and that its use implies no endorsement by NIST.[^readme.md]

[^license]: LICENSE, the Apache License 2.0
[^notice]: NOTICE, every section
[^readme.md]: README.md, the License section
