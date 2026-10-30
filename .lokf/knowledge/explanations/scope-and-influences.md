---
type: Explanation
id: https://w3id.org/lmodel/nist-csf-v2/knowledge/explanations/scope-and-influences
genre: explanation
title: Scope, influences and mappings
description: "What the schema renders and what it leaves out: the CSF 2.0 of CSWP 29 and nothing beyond it, with lmodel/slsa as its one influence on layout. It maps its classes to lmodel/oscal's, as NIST's catalog renders them, keeps the withdrawn CSF 1.1 elements as the catalog states them, and models neither the Informative References, the Profiles and Tiers, the risk-party marking nor the community profiles."
resource: README.md
about:
  - https://w3id.org/lmodel/nist-csf-v2/knowledge/datasets/nist-csf-v2-linkml-schema
sources:
  - id: readme.md
    resource: README.md
    title: the What it models, Influences, Mappings and Not modelled here sections
  - id: changelog.md
    resource: CHANGELOG.md
    title: the Changed and Removed entries
  - id: about.md
    resource: docs/about.md
    title: the section on what is left out
generated:
  by: process:ktl-librarian
  at: "2026-10-29T21:41:10Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-30T08:54:28Z"
---

# Scope, influences and mappings

The schema renders one publication, CSWP 29, at one edition, the CSF 2.0. The README's Influences section says that nothing beyond CSWP 29 shaped it, and that its release asset and governance files follow lmodel/slsa.[^readme.md]

## Why the CSF's own elements

The schema models the function, the category, the subcategory and the implementation example, which [the glossary](../glossary/index.md) defines. It keeps the CSF 1.1 categories and subcategories that CSF 2.0 withdrew as NIST's catalog states them: with a status and, where NIST recorded it, where each moved or what incorporated it. The changelog says that it replaced classes copied from the shape of an OSCAL catalog. Those classes shared names with LOKF's and lmodel/oscal's, and their `class_uri: linkml:Any` let a catalog with any keys validate.[^changelog.md] NIST's catalog in OSCAL stays in the repository as the upstream copy that the tests read.

## Mappings

The README says that the schema crosses to one vocabulary and borrows from none. NIST's catalog renders the framework as an OSCAL catalog, a function as a group, a category and a subcategory as controls, and an example as a part, so each class names its lmodel/oscal counterpart in `broad_mappings`. The OSCAL class is the more general one. The schema names no mapping to SP 800-53, SP 800-171, the CIS Controls or any other document: NIST publishes those relations as Informative References. The changelog says that the schema-level mappings to the CIS Controls were removed, because an analogy between CSF functions and CIS controls is not an authority.

## Not modelled here

- the Informative References NIST publishes through its National Online Informative References program and its reference tool, which the OSCAL catalog does not carry;
- the first-party and third-party risk marking in NIST's catalog, which CSWP 29 does not carry;
- the CSF Tiers of Appendix B, the Organizational Profiles of Section 3, the community profiles and the Quick Start Guides;
- the publication's prose outside the Core.[^about.md]

[^readme.md]: README.md, the Influences, Mappings and Not modelled here sections
[^changelog.md]: CHANGELOG.md, the Changed and Removed entries under Unreleased
[^about.md]: docs/about.md, What is left out
