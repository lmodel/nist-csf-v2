---
type: GlossaryTerm
id: https://w3id.org/lmodel/nist-csf-v2/knowledge/glossary/subcategory
genre: reference
title: Subcategory
description: In the CSF, a group of more specific outcomes of technical and management cybersecurity activities that make up a category, stated in a sentence with an identifier such as GV.OC-01. The schema renders a subcategory as `CsfSubcategory`, with its identifier in `subcategory_id` and its statement in `description`.
definition: A more specific cybersecurity outcome within a CSF category, stated in a sentence.
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
    title: the class CsfSubcategory
generated:
  by: process:ktl-librarian
  at: "2026-10-29T21:41:10Z"
status: draft
---

# Subcategory

CSWP 29's glossary defines a CSF Subcategory as a group of more specific outcomes of technical and management cybersecurity activities that comprise a category.[^nist.cswp.29.pdf] The schema renders a subcategory as `CsfSubcategory`, with its identifier in `subcategory_id`, such as `GV.OC-01`, and its statement in `description`, which is required because the statement is the subcategory. It may hold the implementation examples in `subcategory_examples`. A CSF 1.1 subcategory that CSF 2.0 withdrew carries `withdrawn` in `subcategory_status` and the subcategory it moved to in `subcategory_moved_to` or the category or subcategory that incorporated it in `subcategory_incorporated_into`.[^nist_csf_v2.yaml] Appendix A of CSWP 29 says the subcategory numbers are not sequential on purpose: a gap marks a relocated CSF 1.1 subcategory.

[^nist.cswp.29.pdf]: <https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf>, Appendix C, the glossary
[^nist_csf_v2.yaml]: src/nist_csf_v2/schema/nist_csf_v2.yaml, the class CsfSubcategory
