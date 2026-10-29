---
type: GlossaryTerm
id: https://w3id.org/lmodel/nist-csf-v2/knowledge/glossary/implementation-example
genre: reference
title: Implementation example
description: In the CSF, a concise, action-oriented, notional illustration of a way to help achieve a Core outcome, published by NIST beside the Core with an identifier such as GV.OC-01.001. The schema renders one as `CsfImplementationExample`.
definition: A concise, action-oriented, notional illustration of a way to help achieve a CSF Core outcome.
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
    title: the class CsfImplementationExample
generated:
  by: process:ktl-librarian
  at: "2026-10-29T21:41:10Z"
status: draft
---

# Implementation example

CSWP 29's glossary defines a CSF Implementation Example as a concise, action-oriented, notional illustration of a way to help achieve a Core outcome, and its Section 4 says the examples are among the online resources published beside the publication.[^nist.cswp.29.pdf] The schema renders one as `CsfImplementationExample`, with the identifier NIST's reference data gives it in `implementation_example_id`, such as `GV.OC-01.001`, and its text in `description`. The numbers run once through the whole Core, so no two examples share one. An example stays inlined in its subcategory and is not a type a knowledge concept names.[^nist_csf_v2.yaml]

[^nist.cswp.29.pdf]: <https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf>, Appendix C, the glossary
[^nist_csf_v2.yaml]: src/nist_csf_v2/schema/nist_csf_v2.yaml, the class CsfImplementationExample
