<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# nist-csf-v2

NIST CSWP 29 Cybersecurity Framework (CSF) 2.0 (LinkML)

> **Two ways in.** This README is one; the other is a docent, a museum's name
> for a guide. Install
> [`ktl-docent`](https://github.com/noelmcloughlin/knowledge-trust-ladder) into
> whatever agent you already use, by a route from
> [the install page](https://w3id.org/ktl/docs/install/), and ask it anything
> about this project. It answers from `.lokf/knowledge/`,
> the checked part of what the project knows, and says how far each answer has
> been trusted (still a draft, checked by automation only, or confirmed by a
> named person). It opens the source for exact values, and records what it
> could not answer so the gap gets filled. The same docent serves a person at a
> prompt, an agent reading this file, or a chatbot that can load a skill.
> **Agents:** if `.lokf/knowledge/index.md` exists, read it first. `llms.txt`
> says how to weigh it.

## Documentation Website

[https://lmodel.github.io/nist-csf-v2](https://lmodel.github.io/nist-csf-v2)

## What it models

The Cybersecurity Framework (CSF) 2.0, which the National Institute of Standards and Technology (NIST) publishes as [Cybersecurity White Paper (CSWP) 29](https://doi.org/10.6028/NIST.CSWP.29) of February 26, 2024:

* **Functions** (`CsfFunction`): the six functions that sort the Core's outcomes at the highest level, GOVERN (GV), IDENTIFY (ID), PROTECT (PR), DETECT (DE), RESPOND (RS) and RECOVER (RC).
* **Categories** (`CsfCategory`): the 22 groups of related outcomes within a function, each with an identifier such as `GV.OC`.
* **Subcategories** (`CsfSubcategory`): the 106 outcomes, each a statement with an identifier such as `GV.OC-01`.
* **Implementation examples** (`CsfImplementationExample`): the 363 notional, action-oriented steps NIST publishes beside the Core, each with an identifier such as `GV.OC-01.001`.
* **Withdrawn elements**: the 12 categories and 79 subcategories of CSF 1.1 that CSF 2.0 withdrew, which NIST's catalog keeps. Each carries `withdrawn` as its status, and the CSF 2.0 function, category or subcategory it moved to or that incorporated its outcomes, where NIST recorded one.
* **The framework** (`CsfFramework`): one edition of the CSF as a single document that holds all of these.

The schema header's `version` is the CSF edition, 2.0.0, as NIST's Cybersecurity and Privacy Reference Tool numbers it (`CSF_2_0_0`). Its `source` is the publication's digital object identifier (DOI). NIST also publishes the framework as a catalog in the Open Security Controls Assessment Language (OSCAL). [src/nist_csf_v2/schema/oscal-content/](src/nist_csf_v2/schema/oscal-content) holds that catalog as usnistgov/oscal-content released it in v1.6.0, matched to the release by git object hash. `tests/test_upstream.py` derives the whole framework from the copy, validates it, and holds it to the counts above. A weekly workflow opens an issue when oscal-content gains another edition of the CSF, changes the catalog, or the copy drifts.

CSF 2.0 is the current edition. Release tags number the schema's versions.

## Influences

None beyond CSWP 29: the schema renders one publication, and its release asset and governance files follow [lmodel/slsa](https://github.com/lmodel/slsa).

## Mappings

The schema crosses to one vocabulary and borrows from none.

* **OSCAL**: NIST's catalog renders the framework as an OSCAL catalog, a function as a group, a category and a subcategory as controls, and an implementation example as a part. Each class names its counterpart in [lmodel/oscal](https://github.com/lmodel/oscal) in `broad_mappings`, because the OSCAL class is the more general one.

The schema names no mapping to SP 800-53, SP 800-171, the CIS Controls or any other document. NIST publishes those relations as Informative References, listed below.

## Not modelled here

* The Informative References, which NIST publishes through its National Online Informative References (OLIR) program and its Cybersecurity and Privacy Reference Tool. They relate each subcategory to SP 800-53, SP 800-171, the CIS Controls and other documents, and the OSCAL catalog does not carry them.
* The first-party and third-party risk marking that NIST's catalog gives most subcategories. CSWP 29 does not carry it.
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

`.lokf/` holds this project's [KTL](https://w3id.org/ktl/) knowledge bundle, in the Linked Open Knowledge Format (LOKF). Its domain schema is `.lokf/nist-csf-v2.yaml`, which `lokf adapt` writes from `src/nist_csf_v2/schema/nist_csf_v2.yaml`. Edit the source, never the copy. A release carries the copy as `schema-<tag>-nist-csf-v2.yaml`, on the terms [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers) gives.

`just lokf-adapt` rewrites the copy, and `just lokf-adapt-check` says when it is stale. `project.justfile` names the classes the copy roots on `Concept`, and a concept may name any of them as its `type`. In Obsidian, add these classes to the KTL Registrar and KTL Curator plugins' *Known LOKF types* setting:

```text
CsfFunction, CsfCategory, CsfSubcategory
```

A concept writes the CSF identifier in `csf_function_id`, `csf_category_id` or `csf_subcategory_id`. A subcategory's concept names its category's concept in `isPartOf`, and a category's concept names its function's. A name and a description are the concept's own `title` and `description`.

A host imports the copy beside LOKF's schema, `lokf.yaml`, and beside other adapt copies. LinkML merges them into one namespace, where the last definition of a name wins silently. So no class, enum or type shares a name with LOKF's or with the copies of slsa, github-actions, oscal, spdx and nist-sp-800-218. A slot shares a name only where it carries LOKF's meaning and Internationalized Resource Identifier (IRI), as `title` and `description` do, so `lokf adapt` folds the two into LOKF's and renames nothing. The copy shares no other key with the five neighbours, and `tests/test_schema_rules.py` fails on a new shared name.

## License

The schema and the code are under the Apache License 2.0 ([LICENSE](LICENSE)).

The knowledge bundle in `.lokf/knowledge/` is under the Creative Commons Attribution 4.0 International licence (CC BY 4.0), as its `index.md` declares.

CSWP 29 is a work of the United States Government and is not subject to copyright in the United States. The schema's descriptions are this project's own words. NIST's catalog in [src/nist_csf_v2/schema/oscal-content/](src/nist_csf_v2/schema/oscal-content) keeps NIST's licence beside it: see [NOTICE](NOTICE).

This is not an official NIST project, and its use implies no endorsement by NIST.

## Contributing and security

[CONTRIBUTING.md](CONTRIBUTING.md) is the checklist for pull requests and
releases, [AI_COVENANT.md](AI_COVENANT.md) sets the rules for AI-assisted work,
[SECURITY.md](SECURITY.md) says how to report a vulnerability, and
[CHANGELOG.md](CHANGELOG.md) records the changes.

## Credits

Built from the [linkml-project-copier](https://github.com/linkml/linkml-project-copier) template ([doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584)).
