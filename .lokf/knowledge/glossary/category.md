---
type: GlossaryTerm
id: https://w3id.org/lmodel/nist-csf-v2/knowledge/glossary/category
genre: reference
title: Category
description: In the CSF, a group of related cybersecurity outcomes that together make up a function, with an identifier such as GV.OC. The schema renders a category as `CsfCategory`, with its identifier in `csf_category_id`, and a withdrawn CSF 1.1 category with its status and destination.
definition: A group of related cybersecurity outcomes that together make up a CSF function.
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
    title: the class CsfCategory
generated:
  by: process:ktl-librarian
  at: "2026-10-30T08:31:58Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-30T09:04:56Z"
---

# Category

CSWP 29's glossary defines a CSF Category as a group of related cybersecurity outcomes that collectively comprise a function.[^nist.cswp.29.pdf] The schema renders a category as `CsfCategory`, with its identifier in `csf_category_id`, such as `GV.OC`. A category may hold its subcategories in `category_subcategories`. A CSF 1.1 category that CSF 2.0 withdrew carries `withdrawn` in `category_status`. Where the catalog gives one, it names the category it moved to in `category_moved_to`, or the function, category or subcategory that incorporated it in `category_incorporated_into`.[^nist_csf_v2.yaml] In a knowledge bundle a subcategory names its category with `isPartOf` instead.

[^nist.cswp.29.pdf]: <https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf>, Appendix C, the glossary
[^nist_csf_v2.yaml]: src/nist_csf_v2/schema/nist_csf_v2.yaml, the class CsfCategory
