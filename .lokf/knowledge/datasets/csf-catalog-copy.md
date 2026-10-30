---
type: Dataset
id: https://w3id.org/lmodel/nist-csf-v2/knowledge/datasets/csf-catalog-copy
genre: reference
title: NIST's CSF 2.0 catalog copy
description: NIST's catalog of the Cybersecurity Framework (CSF) 2.0 in the Open Security Controls Assessment Language (OSCAL), copied with NIST's licence from usnistgov/oscal-content v1.6.0 into `src/nist_csf_v2/schema/oscal-content/` and matched to that release by git object hash. The tests derive the whole framework from it, withdrawn CSF 1.1 elements included.
resource: src/nist_csf_v2/schema/oscal-content
license: CC0-1.0
derivedFrom:
  - https://w3id.org/lmodel/nist-csf-v2/knowledge/references/cswp-29
sources:
  - id: nist_csf_v2.0_catalog.json
    resource: src/nist_csf_v2/schema/oscal-content/NIST_CSF_v2.0_catalog.json
    title: the metadata, the groups, the controls, their parts and properties, and the back matter
  - id: notice
    resource: NOTICE
    title: the NIST sections
  - id: check_upstream_release.py
    resource: scripts/check_upstream_release.py
    title: the pins
  - id: test_upstream.py
    resource: tests/test_upstream.py
    title: the derivation and the counts
  - resource: src/nist_csf_v2/schema/oscal-content/LICENSE.md
    title: NIST's licence
generated:
  by: process:ktl-librarian
  at: "2026-10-29T21:41:10Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-30T08:31:58Z"
---

# NIST's CSF 2.0 catalog copy

`src/nist_csf_v2/schema/oscal-content/` holds two files: `NIST_CSF_v2.0_catalog.json`, the catalog of the CSF 2.0 that NIST publishes in the Open Security Controls Assessment Language (OSCAL), and NIST's `LICENSE.md`. NOTICE says that both were retrieved from usnistgov/oscal-content at commit `f0de6d8d8c059d374f15e0ae07508d82e370fc1d`, the v1.6.0 release, and are identical to their counterparts there.[^notice] It also says that NIST's work is in the public domain within the United States, and that NIST dedicates it to the worldwide public domain under CC0 1.0.

## What the catalog holds

The catalog's metadata titles it "Electronic Version of NIST Cybersecurity Framework 2.0", names its framework version `CSF_2_0_0` and its publication status `Final`, and numbers the catalog itself 1.2.1. It says that NIST's Cybersecurity And Privacy Open Reference Datasets In OSCAL (CAPORDINO) generated it. It is written in OSCAL `v1.2.3`.[^nist_csf_v2.0_catalog.json] Its six groups, of class `function`, are the functions. Each group's controls of class `category` are the categories, and each category's controls of class `subcategory` are the subcategories. A function's `overview` part and a category's or subcategory's `statement` part carry NIST's text, and a subcategory's `guidance` parts of class `example` are the implementation examples, each with an identifier such as `GV.OC-01.001`.

The catalog keeps the CSF 1.1 categories and subcategories that CSF 2.0 withdrew. Each carries a `status` property with the value `withdrawn`, and most carry links with the relation `moved_to` or `incorporated_into` that name a CSF 2.0 function, category or subcategory. A withdrawn category's statement part has no text. Most CSF 2.0 subcategories also carry a `marking` property of class `risk-party`, with the value `1st` or `3rd`, which the schema leaves out because CSWP 29 does not carry it.

`tests/test_upstream.py` derives a `CsfFramework` from the copy with the standard library's JSON parser and validates it. It holds the framework to the publication's counts: 6 functions, 22 categories, 106 subcategories and 363 implementation examples, beside 12 withdrawn categories and 79 withdrawn subcategories with 25 moves and 110 incorporations between them.[^test_upstream.py] It also records the markings it leaves out: 88 first-party and 37 third-party markings, and 3 unmarked subcategories.

## The pins

`scripts/check_upstream_release.py` pins the tag `v1.6.0`, the commit, and each file's git object hash: `c808a0b30f9d8726e3e5309df7d16ef6e2857b7e` for the catalog and `109af23dd24c2c465143aeab12ffebfffe2a4cd5` for the licence.[^check_upstream_release.py] The test checks the hashes offline, and the upstream watch checks them against the pinned commit every week. [Update the upstream pins](../playbooks/update-upstream-pins.md) says how to replace the copy.

[^notice]: NOTICE, the section NIST's CSF catalog in OSCAL
[^nist_csf_v2.0_catalog.json]: src/nist_csf_v2/schema/oscal-content/NIST_CSF_v2.0_catalog.json, the metadata, the groups and their controls
[^test_upstream.py]: tests/test_upstream.py, the COUNTS and MARKINGS tables and the derive function
[^check_upstream_release.py]: scripts/check_upstream_release.py, PINNED_TAG, PINNED_COMMIT and PINNED_BLOBS
