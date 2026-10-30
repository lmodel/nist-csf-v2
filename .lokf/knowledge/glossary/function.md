---
type: GlossaryTerm
id: https://w3id.org/lmodel/nist-csf-v2/knowledge/glossary/function
genre: reference
title: Function
description: In the CSF, the highest level of organization for cybersecurity outcomes; there are six, GOVERN, IDENTIFY, PROTECT, DETECT, RESPOND and RECOVER. The schema renders a function as `CsfFunction`, with its two letters in `csf_function_id`.
definition: The highest level of organization for cybersecurity outcomes in the CSF, one of six.
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
    title: the class CsfFunction
generated:
  by: process:ktl-librarian
  at: "2026-10-30T08:31:58Z"
status: draft
---

# Function

CSWP 29's glossary defines a CSF Function as the highest level of organization for cybersecurity outcomes, and names the six: Govern, Identify, Protect, Detect, Respond and Recover.[^nist.cswp.29.pdf] The schema renders a function as `CsfFunction`, with its two letters in `csf_function_id`, such as `GV`, and may hold the function's categories in `function_categories`.[^nist_csf_v2.yaml] In a knowledge bundle a category names its function with `isPartOf` instead. The bundle describes each function under [functions](../functions/index.md).

[^nist.cswp.29.pdf]: <https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf>, Appendix C, the glossary
[^nist_csf_v2.yaml]: src/nist_csf_v2/schema/nist_csf_v2.yaml, the class CsfFunction
