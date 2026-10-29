---
type: Dataset
id: https://w3id.org/lmodel/nist-csf-v2/knowledge/datasets/test-data
genre: reference
title: Test data and tests
description: "The schema's tests: seven valid examples and 22 counter-examples under `tests/data/`, `tests/test_data.py`, which holds each to the validator, `tests/test_upstream.py`, which derives the framework from NIST's catalog, and `tests/test_schema_rules.py`, which holds the adapt copy apart from LOKF and the slsa, github-actions, oscal, spdx and nist-sp-800-218 copies in `tests/neighbours/`."
resource: tests
sources:
  - id: data
    resource: tests/data
    title: the valid and invalid examples
  - id: test_data.py
    resource: tests/test_data.py
    title: the data tests
  - id: test_upstream.py
    resource: tests/test_upstream.py
    title: the derivation and the counts
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
    title: the neighbours and their checksums
  - resource: tests/neighbours
    title: the five released adapt copies
  - resource: tests/data/README.md
    title: the naming rule
generated:
  by: process:ktl-librarian
  at: "2026-10-29T21:41:10Z"
status: draft
---

# Test data and tests

`tests/data/valid/` holds seven examples, one for each class and a second for `CsfCategory` and `CsfSubcategory` as withdrawn elements, and `tests/data/invalid/` holds 22 counter-examples, each invalid for one reason.[^data] A file's class is the part of its name before the first hyphen, such as `CsfSubcategory-withdrawn-moved.yaml`. The counter-examples break each constraint the schema states:

- a missing required field;
- an identifier of the wrong form, or of the wrong level, such as a category identifier where a subcategory's belongs;
- an unknown function;
- a status other than `withdrawn`;
- a destination of the wrong kind, such as a category moved to a subcategory;
- a key the class does not declare.

`tests/test_data.py` loads each valid example into the dataclasses, holds each to the validator, which must pass a valid example and fail a counter-example, and checks that every class has an example.[^test_data.py] `tests/test_upstream.py` derives the whole of CSF 2.0 from NIST's catalog copy and holds it to the validator and to the publication's counts, as [NIST's CSF 2.0 catalog copy](csf-catalog-copy.md) says.[^test_upstream.py] It also checks that the identifiers nest and never repeat, that the CSF 2.0 categories are the 22 of CSWP 29's Table 1, that a withdrawn element names a destination of CSF 2.0 or none, and that the risk-party markings stay out of the derived framework.

`tests/test_schema_rules.py` checks the adapt copy against LOKF's `lokf.yaml` and five neighbours: the schema assets of lmodel/slsa v0.7.0, lmodel/github-actions v0.2.1, lmodel/oscal v0.1.0, lmodel/spdx v0.1.0 and lmodel/nist-sp-800-218 v0.1.0, each pinned by its SHA-256 checksum.[^test_schema_rules.py] No class, enum, type or subset may share a name, and the copy shares no key with a neighbour. The test also checks that the copy roots exactly the three concept classes and that every mapping uses a prefix the copy binds. `just test` runs the tests, generates the project into `tmp/`, and runs the examples through `linkml-run-examples`.

[^data]: tests/data, valid/ and invalid/
[^test_data.py]: tests/test_data.py, the four tests
[^test_upstream.py]: tests/test_upstream.py, the tests and COUNTS
[^test_schema_rules.py]: tests/test_schema_rules.py, NEIGHBOURS and the tests
