---
type: GlossaryTerm
id: https://w3id.org/lmodel/nist-csf-v2/knowledge/glossary/withdrawn-element
genre: reference
title: Withdrawn element
description: A CSF 1.1 category or subcategory that CSF 2.0 withdrew, which NIST's catalog keeps with the status `withdrawn` and, where NIST recorded it, the CSF 2.0 element it moved to or that incorporated its outcomes. The schema carries the status in `CsfElementStatus` and the destinations in the moved-to and incorporated-into attributes.
definition: A CSF 1.1 category or subcategory that CSF 2.0 withdrew, kept in NIST's catalog with its status and destination.
resource: https://doi.org/10.6028/NIST.CSWP.29
definedBy:
  - https://w3id.org/lmodel/nist-csf-v2/knowledge/references/cswp-29
relatedTo:
  - https://w3id.org/lmodel/nist-csf-v2/knowledge/datasets/nist-csf-v2-linkml-schema
sources:
  - id: nist.cswp.29.pdf
    resource: https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf
    title: Appendix C, the glossary, read on 2026-10-29
  - id: nist_csf_v2.yaml
    resource: src/nist_csf_v2/schema/nist_csf_v2.yaml
    title: the enum CsfElementStatus
generated:
  by: process:ktl-librarian
  at: "2026-10-29T21:41:10Z"
status: draft
---

# Withdrawn element

CSWP 29 says in Appendix A that gaps in the subcategory numbering mark CSF 1.1 subcategories that CSF 2.0 relocated.[^nist.cswp.29.pdf] NIST's catalog keeps those elements: 12 categories and 79 subcategories, each with a `status` property of `withdrawn`, and most with a link that names the CSF 2.0 function, category or subcategory the element moved to or that incorporated it. The schema's enum `CsfElementStatus` holds the one value, and a category or subcategory carries it in `category_status` or `subcategory_status`, with the destinations in `category_moved_to`, `category_incorporated_into`, `subcategory_moved_to` and `subcategory_incorporated_into`.[^nist_csf_v2.yaml] A withdrawn category keeps its withdrawn subcategories and has no statement; a withdrawn subcategory keeps its CSF 1.1 statement and has no implementation examples. Four withdrawn categories, PR.IP, PR.PT, DE.DP and RS.RP, name no destination, as the catalog has it.

[^nist.cswp.29.pdf]: <https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf>, Appendix C, the glossary
[^nist_csf_v2.yaml]: src/nist_csf_v2/schema/nist_csf_v2.yaml, the enum CsfElementStatus and the status attributes
