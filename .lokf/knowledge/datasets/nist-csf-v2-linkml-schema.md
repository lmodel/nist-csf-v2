---
type: Dataset
id: https://w3id.org/lmodel/nist-csf-v2/knowledge/datasets/nist-csf-v2-linkml-schema
genre: reference
title: nist-csf-v2 LinkML schema
description: "The LinkML schema of the Cybersecurity Framework (CSF) 2.0, `src/nist_csf_v2/schema/nist_csf_v2.yaml` (schema id `https://w3id.org/lmodel/nist-csf-v2`, version 2.0.0): five classes, one enum with the value `withdrawn` and six identifier types. Its `lokf adapt` copy `.lokf/nist-csf-v2.yaml`, rooted on the function, the category and the subcategory, is the bundle's domain schema."
resource: src/nist_csf_v2/schema/nist_csf_v2.yaml
version: 2.0.0
license: Apache-2.0
derivedFrom:
  - https://w3id.org/lmodel/nist-csf-v2/knowledge/references/cswp-29
  - https://w3id.org/lmodel/nist-csf-v2/knowledge/datasets/csf-catalog-copy
sources:
  - id: nist_csf_v2.yaml
    resource: src/nist_csf_v2/schema/nist_csf_v2.yaml
    title: the header, the classes, the enum and the types
  - id: readme.md
    resource: README.md
    title: the What it models and Knowledge Trust Ladder (KTL) sections
  - id: project.justfile
    resource: project.justfile
    title: the lokf-adapt recipes and their roots
  - id: nist-csf-v2.yaml
    resource: .lokf/nist-csf-v2.yaml
    title: the notes lokf adapt wrote
  - resource: .lokf/justfile
    title: the schema line
  - resource: .lokf/pyproject.toml
    title: the tool.lokf table
generated:
  by: process:ktl-librarian
  at: "2026-10-30T08:31:58Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-30T08:54:28Z"
---

# nist-csf-v2 LinkML schema

`src/nist_csf_v2/schema/nist_csf_v2.yaml` is the schema, titled "The NIST Cybersecurity Framework (CSF) 2.0". Its header gives `version: 2.0.0`, the CSF edition, and `source: https://doi.org/10.6028/NIST.CSWP.29`, the digital object identifier of NIST Cybersecurity White Paper (CSWP) 29.[^nist_csf_v2.yaml] Its annotations name the identifier NIST's Cybersecurity and Privacy Reference Tool gives the edition, `CSF_2_0_0`, the publication date `2024-02`, and the usnistgov/oscal-content tag `v1.6.0` and commit `f0de6d8d8c059d374f15e0ae07508d82e370fc1d` of the catalog copy. Its comments say that the catalog's own version number, 1.2.1, numbers the catalog and not the framework, that `scripts/check_upstream_release.py` reads the same pins, and that the release tags are the schema's own versions. The schema declares the prefix `nist_csf_v2:` as `https://w3id.org/lmodel/nist-csf-v2/` and the license Apache-2.0, and it imports only `linkml:types`.

## Classes

- **`CsfFramework`** is the tree root: one edition of the CSF as a whole. It requires `csf_version`, two numbers such as `2.0`, and `csf_functions`, which holds at least one function.
- **`CsfFunction`** is one of the six functions. It requires `csf_function_id`, two letters out of `GV`, `ID`, `PR`, `DE`, `RS` and `RC`, and a `title`, and it may hold its categories in `function_categories`.
- **`CsfCategory`** is a category, or a CSF 1.1 category that CSF 2.0 withdrew. It requires `csf_category_id`, such as `GV.OC`, and a `title`, and it may hold `category_subcategories`, `category_status`, `category_moved_to` and `category_incorporated_into`.
- **`CsfSubcategory`** is a subcategory, or a withdrawn one. It requires `csf_subcategory_id`, such as `GV.OC-01`, and a `description`, its statement, which may not be blank. It may hold `subcategory_examples`, `subcategory_status`, `subcategory_moved_to` and `subcategory_incorporated_into`.
- **`CsfImplementationExample`** is an implementation example. It requires `csf_implementation_example_id`, such as `GV.OC-01.001`, and a `description` that is not blank.

The enum `CsfElementStatus` has one value, `withdrawn`, the status the catalog gives a CSF 1.1 category or subcategory that CSF 2.0 withdrew. Six types hold the forms of the identifiers:

- `csf_function_identifier`, `csf_category_identifier`, `csf_subcategory_identifier` and `csf_implementation_example_identifier`;
- `csf_element_identifier`, for a function, category or subcategory that incorporated a withdrawn category;
- `csf_category_or_subcategory_identifier`, for a category or subcategory that incorporated a withdrawn subcategory.

The schema's slots `title` and `description` carry the IRIs `schema:name` and `schema:description`.

## Mappings

Each class names a class of lmodel/oscal in `broad_mappings`: `oscal:Catalog` for the framework, `oscal:Group` for the function, `oscal:Control` for the category and the subcategory, and `oscal:Part` for the example. A comment in the header says that NIST's catalog renders the elements that way. Another says that the catalog's first-party and third-party risk marking is the reference tool's, not CSWP 29's, so the schema leaves it out. [Scope, influences and mappings](../explanations/scope-and-influences.md) says more.

## As the bundle's domain schema

A LOKF domain schema is a LinkML schema that imports LOKF's `lokf.yaml` and adds a host's classes and keys, so that `lokf validate` checks the concepts typed with them. The README says that this bundle's domain schema is `.lokf/nist-csf-v2.yaml`, which `lokf adapt` writes from the schema. Edit the source, never the copy.[^readme.md] The `schema :=` line of `.lokf/justfile` and the `[tool.lokf]` table of `.lokf/pyproject.toml` both name the copy.

`project.justfile` passes three roots to `lokf adapt`: `CsfFunction`, `CsfCategory` and `CsfSubcategory`. Its comment says that these are the three elements that CSWP 29 gives an identifier and that other documents cite. It also says that an implementation example stays inlined in its subcategory.[^project.justfile] The copy's notes say that `lokf adapt` re-rooted the three classes on `lokf:Concept` and folded `title` and `description` into LOKF's slots.[^nist-csf-v2.yaml] The copy renames nothing, and `CsfFramework` is no longer a tree root in it. The concepts under `functions/` in this bundle are typed `CsfFunction`.

The generated models, `project/` and the adapt copy come from this file: see [Generated artefacts](generated-artefacts.md). [Element names and the shared namespace](../explanations/element-names.md) says why no class, enum or type shares a name with LOKF's or a neighbour's.

[^nist_csf_v2.yaml]: src/nist_csf_v2/schema/nist_csf_v2.yaml, the header and the classes
[^readme.md]: README.md, the Knowledge Trust Ladder (KTL) section
[^project.justfile]: project.justfile, the knowledge bundle recipes
[^nist-csf-v2.yaml]: .lokf/nist-csf-v2.yaml, the notes
