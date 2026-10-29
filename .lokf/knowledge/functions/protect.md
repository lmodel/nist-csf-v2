---
type: CsfFunction
id: https://w3id.org/lmodel/nist-csf-v2/knowledge/functions/protect
title: PROTECT
description: "The CSF 2.0 function PR, PROTECT: the organization uses safeguards to manage its cybersecurity risks. It holds 5 categories, 22 subcategories and 77 implementation examples."
function_id: PR
resource: src/nist_csf_v2/schema/oscal-content/NIST_CSF_v2.0_catalog.json
definedBy:
  - https://w3id.org/lmodel/nist-csf-v2/knowledge/references/cswp-29
relatedTo:
  - https://w3id.org/lmodel/nist-csf-v2/knowledge/glossary/function
sources:
  - id: nist_csf_v2.0_catalog.json
    resource: src/nist_csf_v2/schema/oscal-content/NIST_CSF_v2.0_catalog.json
    title: the group PR
generated:
  by: process:ktl-librarian
  at: "2026-10-29T21:41:10Z"
status: draft
---

# PROTECT (PR)

The catalog's overview of the function says, in this bundle's words, that the organization uses safeguards to manage its cybersecurity risks.[^nist_csf_v2.0_catalog.json] In CSF 2.0 the function holds 5 categories, 22 subcategories and 77 implementation examples, in its categories:

- `PR.AA` Identity Management, Authentication, and Access Control: 6 subcategories
- `PR.AT` Awareness and Training: 2 subcategories
- `PR.DS` Data Security: 4 subcategories
- `PR.PS` Platform Security: 6 subcategories
- `PR.IR` Technology Infrastructure Resilience: 4 subcategories

The catalog keeps four withdrawn CSF 1.1 categories under it and 35 withdrawn subcategories: PR.AC moved to PR.AA, PR.MA was incorporated into ID.AM-08, and PR.IP and PR.PT name no destination, though their subcategories do.

[^nist_csf_v2.0_catalog.json]: src/nist_csf_v2/schema/oscal-content/NIST_CSF_v2.0_catalog.json, the group PR
