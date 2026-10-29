# nist-csf-v2

This project is a LinkML model of the Cybersecurity Framework (CSF) 2.0,
which the National Institute of Standards and Technology (NIST) publishes as
Cybersecurity White Paper (CSWP) 29. It covers the six functions, their
categories and subcategories, the implementation examples NIST publishes with
the subcategories, and the CSF 1.1 categories and subcategories that CSF 2.0
withdrew, with where each moved or what incorporated it.

- [Schema documentation](elements/index.md), generated from the schema
- [About](about.md): how the elements are named and what the model leaves out
- [`nist_csf_v2.yaml`](schema/nist_csf_v2.yaml): the schema

## Validating data

`linkml-validate -s src/nist_csf_v2/schema/nist_csf_v2.yaml -C CsfSubcategory outcome.yaml`
checks a file against the JSON Schema generated from the schema, and
`tests/test_data.py` holds every example to it.

Validate a file before loading it into either model in
`src/nist_csf_v2/datamodel/`. LinkML 1.10.0 generates models that check
less:

- The dataclasses check required fields and enum values, but no pattern.
- The Pydantic models also check the patterns a field carries itself, such as
  the form of `csf_version`. They do not check the patterns of the five
  identifier types, so a function, category, subcategory or example
  identifier goes unchecked.

No check covers these rules:

- that a category's identifier starts with its function's, a subcategory's
  with its category's, and an example's with its subcategory's;
- that a list never repeats an identifier;
- that only a withdrawn category or subcategory names where it moved or what
  incorporated it, never both, and that each destination is an element of
  CSF 2.0;
- that a withdrawn category has no statement and holds only withdrawn
  subcategories, and that a withdrawn subcategory has no implementation
  examples.

`tests/test_upstream.py` checks all four over NIST's catalog of CSF 2.0.
