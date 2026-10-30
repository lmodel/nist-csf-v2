---
type: Playbook
id: https://w3id.org/lmodel/nist-csf-v2/knowledge/playbooks/validate-data
genre: how-to
title: Validate data against the schema
description: "How to validate CSF data with `linkml-validate` before loading it into the generated Python models, which check less: the dataclasses check no pattern, and the Pydantic models miss the identifier types' patterns. No check covers the nesting of identifiers, a repeated one, or the rules on withdrawn elements."
resource: docs/index.md
about:
  - https://w3id.org/lmodel/nist-csf-v2/knowledge/datasets/nist-csf-v2-linkml-schema
sources:
  - id: docs-index.md
    resource: docs/index.md
    title: the Validating data section
generated:
  by: process:ktl-librarian
  at: "2026-10-30T08:31:58Z"
status: draft
---

# Validate data against the schema

Run `linkml-validate -s src/nist_csf_v2/schema/nist_csf_v2.yaml -C CsfSubcategory outcome.yaml`, naming the class the file holds. It checks the file against the JSON Schema the validator generates from the schema, and `tests/test_data.py` holds every example to the same check.[^docs-index.md]

Validate a file before loading it into either model in `src/nist_csf_v2/datamodel/`. The page says that the models LinkML 1.12.1 generates check less:

- the dataclasses check required fields and enum values, but no pattern;
- the Pydantic models also check the patterns a field carries itself, such as the form of `csf_version`, but not the patterns of the six identifier types.

No check covers four rules:

- each identifier starts with the identifier of what holds it;
- a list never repeats an identifier;
- only a withdrawn element names a destination, and each destination is an element of CSF 2.0;
- a withdrawn category has no statement and only withdrawn subcategories, and a withdrawn subcategory has no implementation examples.

`tests/test_upstream.py` checks all four over NIST's catalog of CSF 2.0.

[^docs-index.md]: docs/index.md, Validating data
