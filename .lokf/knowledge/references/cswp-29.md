---
type: Reference
id: https://w3id.org/lmodel/nist-csf-v2/knowledge/references/cswp-29
genre: reference
title: NIST CSWP 29, the CSF 2.0
description: "NIST Cybersecurity White Paper 29, The NIST Cybersecurity Framework (CSF) 2.0 (February 26, 2024, <https://doi.org/10.6028/NIST.CSWP.29>), the edition the schema renders: a taxonomy of cybersecurity outcomes in six functions, 22 categories and 106 subcategories, with Profiles and Tiers for using it and a glossary."
resource: https://doi.org/10.6028/NIST.CSWP.29
sources:
  - id: nist.cswp.29.pdf
    resource: https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf
    title: the publication, read on 2026-10-29
  - id: check_upstream_release.py
    resource: scripts/check_upstream_release.py
    title: the pinned identifier and the docstring
  - id: readme.md
    resource: README.md
    title: the What it models section
generated:
  by: process:ktl-librarian
  at: "2026-10-29T21:41:10Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-30T09:07:28Z"
---

# NIST CSWP 29, the CSF 2.0

NIST Cybersecurity White Paper (CSWP) 29 is titled "The NIST Cybersecurity Framework (CSF) 2.0" and dated February 26, 2024. Its citation line names the National Institute of Standards and Technology as the author, Gaithersburg, Maryland, as the place, and <https://doi.org/10.6028/NIST.CSWP.29> as the address.[^nist.cswp.29.pdf] Its abstract says that the CSF 2.0 gives industry, government agencies and other organizations guidance for managing cybersecurity risks, as a taxonomy of high-level outcomes any organization can use. It says too that the CSF does not prescribe how an outcome is achieved, but links to online resources that do.

The publication has five sections and three appendices:

- the sections: an overview, an introduction to the Core, an introduction to Profiles and Tiers, the online resources that supplement the CSF, and risk communication;
- the appendices: Appendix A, the Core; Appendix B, the Tiers; and Appendix C, the glossary.

Appendix A says that the order of the functions, categories and subcategories is not alphabetical, and that the numbering of the subcategories is not sequential on purpose: a gap marks a CSF 1.1 subcategory that CSF 2.0 relocated. Its Table 1 lists the six functions and the 22 categories with their identifiers.

The glossary defines:

- a function as the highest level of organization for cybersecurity outcomes;
- a category as a group of related outcomes that make up a function;
- a subcategory as a group of more specific outcomes that make up a category;
- an implementation example as a concise, action-oriented, notional illustration of a way to help achieve an outcome.

The online resources are the Informative References, the Implementation Examples, the Quick Start Guides and the Community Profiles. NIST publishes them on the CSF website and through the CSF 2.0 Reference Tool, not in the publication.

The README says that CSF 2.0 is the current edition, that NIST's community profiles are separate documents and not editions, and that the schema does not model them.[^readme.md] `scripts/check_upstream_release.py` pins the publication's identifier and says why it asks doi.org nothing. A CSWP number is assigned paper by paper, so the next edition's identifier cannot be predicted. A new edition appears instead as a new folder in usnistgov/oscal-content.[^check_upstream_release.py] [NIST's CSF 2.0 catalog copy](../datasets/csf-catalog-copy.md) is the machine-readable form of this edition that the repository keeps.

[^nist.cswp.29.pdf]: <https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf>, the title page, the abstract, the contents, Appendix A and Appendix C
[^readme.md]: README.md, the What it models section
[^check_upstream_release.py]: scripts/check_upstream_release.py, PINNED_DOI and the docstring
