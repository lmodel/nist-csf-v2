---
type: Explanation
id: https://w3id.org/lmodel/nist-csf-v2/knowledge/explanations/element-names
genre: explanation
title: Element names and the shared namespace
description: "How the schema names its elements so that its adapt copy can sit beside LOKF's schema and the slsa, github-actions, oscal, spdx and nist-sp-800-218 copies: classes with the `Csf` prefix, NIST's identifiers kept as written, every other key qualified with the CSF's own nouns, `title` and `description` carrying LOKF's IRIs, and no other key shared, which `tests/test_schema_rules.py` checks."
resource: docs/about.md
about:
  - https://w3id.org/lmodel/nist-csf-v2/knowledge/datasets/nist-csf-v2-linkml-schema
sources:
  - id: about.md
    resource: docs/about.md
    title: the naming paragraphs
  - id: readme.md
    resource: README.md
    title: the Knowledge Trust Ladder (KTL) section
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
    title: SHARED_WITH_NEIGHBOURS and the name tests
  - id: linkmllint.yaml
    resource: .linkmllint.yaml
    title: the comment
generated:
  by: process:ktl-librarian
  at: "2026-10-29T21:41:10Z"
status: draft
---

# Element names and the shared namespace

Element names are the schema's own. Classes carry the `Csf` prefix, such as `CsfSubcategory`, so that they can be imported beside other vocabularies. Slots are snake_case, and the identifiers keep the form NIST gives them, such as `GV.OC-01`, and the example identifiers the form of NIST's reference data, such as `GV.OC-01.001`.[^about.md] Every element is in the `nist_csf_v2:` namespace, `https://w3id.org/lmodel/nist-csf-v2/`. Every key but `title` and `description` is qualified with the CSF's own noun, such as `category_status` and `subcategory_moved_to`, so that a sibling schema's `status` or `moved_to` never meets it.

`.linkmllint.yaml` applies the recommended rules unchanged, and its comment says why nothing is relaxed: the one enum's value, `withdrawn`, is already the lower-case word the catalog uses.[^linkmllint.yaml]

## Beside other schemas

A host imports the adapt copy beside LOKF's `lokf.yaml` and other adapt copies, and LinkML merges them into one namespace, where the last definition of a name wins silently. The README says that no class, enum or type therefore shares a name with LOKF's or with the copies of slsa, github-actions, oscal, spdx and nist-sp-800-218. A slot shares a name only where it carries LOKF's meaning and IRI, as `title` and `description` do, so `lokf adapt` folds the two into LOKF's and renames nothing.[^readme.md]

`tests/test_schema_rules.py` checks the copy against `lokf.yaml` and the schema assets of slsa v0.7.0, github-actions v0.2.1, oscal v0.1.0, spdx v0.1.0 and nist-sp-800-218 v0.1.0. Its list of keys shared with each neighbour is empty, so a new shared key fails the test.[^test_schema_rules.py]

[^about.md]: docs/about.md, the paragraph on element names
[^linkmllint.yaml]: .linkmllint.yaml, the comment
[^readme.md]: README.md, the Knowledge Trust Ladder (KTL) section
[^test_schema_rules.py]: tests/test_schema_rules.py, NEIGHBOURS and SHARED_WITH_NEIGHBOURS
