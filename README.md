<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# nist-csf-v2

NIST CSWP 29 Cybersecurity Framework (CSF) 2.0 (LinkML)

> **Only want to ask?** Install `ktl-docent` into any agent you use, by a route from [the install page](https://w3id.org/ktl/docs/install/), and ask it about this project. It answers from the bundle and says how far each answer has been checked.
>
> **Agents:** if `.lokf/knowledge/index.md` exists, read it first. `llms.txt` says how to weigh it.

## Documentation Website

[https://lmodel.github.io/nist-csf-v2](https://lmodel.github.io/nist-csf-v2)

## What it models

The schema models the Cybersecurity Framework (CSF) 2.0, which the National Institute of Standards and Technology (NIST) publishes as [Cybersecurity White Paper (CSWP) 29](https://doi.org/10.6028/NIST.CSWP.29) of February 26, 2024. The schema holds the Core's six functions (`CsfFunction`), 22 categories (`CsfCategory`) and 106 subcategories (`CsfSubcategory`), the 363 implementation examples NIST publishes beside it, and the CSF 1.1 elements that CSF 2.0 withdrew, each with where it moved. It also carries the first-party and third-party risk marking that NIST's catalog gives most subcategories (`subcategory_risk_parties`), which CSWP 29 does not.

[src/nist_csf_v2/schema/oscal-content/](src/nist_csf_v2/schema/oscal-content) holds NIST's catalog of the framework in the Open Security Controls Assessment Language (OSCAL), from usnistgov/oscal-content v1.6.0, and `tests/test_upstream.py` derives the whole framework from it. A weekly workflow opens an issue when oscal-content gains another edition of the CSF, changes the catalog, or the copy drifts.

## Mappings

* **OSCAL**: each class names its counterpart in [lmodel/oscal](https://github.com/lmodel/oscal) in `broad_mappings`: a function is a group, a category and a subcategory are controls, and an implementation example is a part.

The schema maps to no other document. NIST publishes those relations as Informative References, listed below.

## Not modelled here

* The Informative References, which NIST publishes through its National Online Informative References (OLIR) program and its Cybersecurity and Privacy Reference Tool. They relate each subcategory to SP 800-53, SP 800-171, the CIS Controls and other documents, and the OSCAL catalog does not carry them.
* The CSF Tiers of the publication's Appendix B and the Organizational Profiles of its Section 3, which describe how an organization uses the Core.
* NIST's community profiles, which are separate documents and not editions of the CSF, and its Quick Start Guides.
* The rules no pattern can check, which [docs/index.md](docs/index.md) lists.

## Repository Structure

* [docs/](docs/): the website's pages, with the generated schema pages in [elements/](docs/elements/)
* [examples/](examples/): usage examples
* [project/](project/): generated project files (do not edit them)
* [scripts/](scripts/): the upstream watch
* [src/nist_csf_v2/schema/](src/nist_csf_v2/schema): the LinkML schema, `nist_csf_v2.yaml` (edit this), and NIST's catalog copy
* [src/nist_csf_v2/datamodel/](src/nist_csf_v2/datamodel): the generated Python datamodel
* [tests/](tests/): Python tests, with example data in [data/](tests/data) and the neighbours' adapt copies in [neighbours/](tests/neighbours)
* [website/](website/): the Astro Starlight site built from the README, `docs/`, the schema's pages and the knowledge bundle

## Developer Tools

Run `just` to list the project's [just](https://github.com/casey/just/) recipes.

## Knowledge Trust Ladder (KTL)

`.lokf/` holds this project's [KTL](https://w3id.org/ktl/) knowledge bundle. Its domain schema, `.lokf/nist-csf-v2.yaml`, is the copy `just lokf-adapt` writes from `src/nist_csf_v2/schema/nist_csf_v2.yaml`, and `just lokf-adapt-check` says when it is stale. Edit the source, never the copy. A release carries the copy as `schema-<tag>-nist-csf-v2.yaml`, on the terms [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers) gives.

The copy roots these classes on `Concept`, so a concept may name any of them as its `type`. In Obsidian, add them to the *Known LOKF types* setting of the KTL Registrar and KTL Curator plugins:

```text
CsfFunction, CsfCategory, CsfSubcategory
```

A concept writes the CSF identifier in `csf_function_id`, `csf_category_id` or `csf_subcategory_id`. A subcategory's concept names its category's concept in `isPartOf`, and a category's concept names its function's.

No class, enum or type of the copy shares a name with LOKF's schema or with another lmodel copy, and `tests/test_schema_rules.py` fails on a new shared name.

## License

The schema and the code are under the Apache License 2.0 ([LICENSE](LICENSE)), and the knowledge bundle in `.lokf/knowledge/` is under CC BY 4.0.

CSWP 29 is a work of the United States Government and is not subject to copyright in the United States. The schema's descriptions are this project's own words, and NIST's catalog keeps NIST's licence beside it: see [NOTICE](NOTICE). This is not an official NIST project, and its use implies no endorsement by NIST.

## Contributing and security

[CONTRIBUTING.md](CONTRIBUTING.md) is the checklist for pull requests and
releases, [AI_COVENANT.md](AI_COVENANT.md) sets the rules for AI-assisted work,
[SECURITY.md](SECURITY.md) says how to report a vulnerability, and
[CHANGELOG.md](CHANGELOG.md) records the changes.

## Credits

Built from the [linkml-project-copier](https://github.com/linkml/linkml-project-copier) template ([doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584)).
