---
type: Dataset
id: https://w3id.org/lmodel/nist-csf-v2/knowledge/datasets/test-data
genre: reference
title: Test data and tests
description: "The schema's tests: seven valid examples and 29 counter-examples under `tests/data/`, `tests/test_data.py`, which holds each to the validator, `tests/test_upstream.py`, which derives the framework from NIST's catalog and holds the examples to it, `tests/test_watch.py`, which runs the upstream watch against stubbed answers, and `tests/test_schema_rules.py`, which holds the adapt copy apart from LOKF and the slsa, github-actions, oscal, spdx and nist-sp-800-218 copies in `tests/neighbours/`."
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
  - id: test_watch.py
    resource: tests/test_watch.py
    title: the stubbed answers and the watch's tests
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
    title: the neighbours and their checksums
  - resource: tests/neighbours
    title: the five released adapt copies
  - resource: tests/data/README.md
    title: the naming rule
generated:
  by: process:ktl-librarian
  at: "2026-10-30T08:31:58Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-30T08:54:28Z"
---

# Test data and tests

`tests/data/valid/` holds seven examples: one for each class, and a second for `CsfCategory` and `CsfSubcategory` as withdrawn elements. `tests/data/invalid/` holds 29 counter-examples, each invalid for one reason.[^data] A file's class is the part of its name before the first hyphen, such as `CsfSubcategory-withdrawn-moved.yaml`. A counter-example's first line names where it fails, as `# Fails at:` and a JSON pointer such as `/csf_category_id`. The counter-examples break each constraint the schema states:

- a missing required field, a title among them;
- an identifier of the wrong form or of the wrong level, such as a category identifier where a subcategory's belongs, or one that starts with letters no function has;
- an unknown function;
- a status other than `withdrawn`;
- a destination of the wrong kind, such as a category moved to a subcategory or a subcategory incorporated into a whole function;
- an empty list of functions, and a blank description where a description is required;
- a key the class does not declare.

`tests/test_data.py` loads each valid example into the dataclasses and holds each to the validator. A valid example must pass, and a counter-example must fail at the place its first line names. The test also checks that every class has an example.[^test_data.py] `tests/test_upstream.py` derives the whole of CSF 2.0 from NIST's catalog copy and holds it to the validator and to the publication's counts, as [NIST's CSF 2.0 catalog copy](csf-catalog-copy.md) says.[^test_upstream.py] It also checks that:

- the identifiers nest and never repeat;
- the CSF 2.0 categories are the 22 of CSWP 29's Table 1;
- a withdrawn element names a destination of CSF 2.0 or none;
- the risk-party markings stay out of the derived framework.

It holds each valid example to the catalog too: an element an example names must have the parent, the title, the status and the destinations the catalog gives it.

`tests/test_watch.py` runs `scripts/check_upstream_release.py` against stubbed answers from the GitHub API, with no network. It checks what the report says when nothing changed, when a release drops the pinned folders, when a release changes the licence, when the network fails, when NIST adds a file and when the pinned tag moves.[^test_watch.py]

`tests/test_schema_rules.py` checks the adapt copy against LOKF's `lokf.yaml` and five neighbours: the schema assets of lmodel/slsa v0.7.0, lmodel/github-actions v0.2.1, lmodel/oscal v0.1.0, lmodel/spdx v0.1.0 and lmodel/nist-sp-800-218 v0.1.0, each pinned by its SHA-256 checksum.[^test_schema_rules.py] No class, enum, type or subset may share a name, and the copy shares no key with a neighbour. The test also checks that the copy roots exactly the three concept classes, that every mapping uses a prefix the copy binds, and that every `oscal:` mapping names a class of the oscal copy. `just test` runs the tests, generates the project into `tmp/`, and runs the examples through `linkml-run-examples`.

[^data]: tests/data, valid/ and invalid/
[^test_data.py]: tests/test_data.py, the four tests
[^test_upstream.py]: tests/test_upstream.py, the tests and COUNTS
[^test_watch.py]: tests/test_watch.py, the stubbed answers and the six tests
[^test_schema_rules.py]: tests/test_schema_rules.py, NEIGHBOURS and the tests
