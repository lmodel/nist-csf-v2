---
lokf_version: "0.2"
okf_version: "0.2"
base_iri: https://w3id.org/lmodel/nist-csf-v2/knowledge/
context: https://w3id.org/lokf/context.jsonld
title: nist-csf-v2 Knowledge Bundle
description: NIST CSWP 29 Cybersecurity Framework (CSF) 2.0 (LinkML)
license: https://creativecommons.org/licenses/by/4.0/
publisher:
  type: Person
  id: https://w3id.org/lmodel/nist-csf-v2/knowledge/person/noel-mcloughlin
  name: Noel McLoughlin
---

# nist-csf-v2 Knowledge Bundle

A [LOKF](https://lokf.nolan-nichols.com) knowledge base for nist-csf-v2. Every Markdown file under `knowledge/` is one concept; together they form a queryable knowledge graph, derived from this repository's code and docs.

# Services

* [Documentation site](services/documentation-site.md) - The Astro Starlight site in `website/`, for <https://lmodel.github.io/nist-csf-v2>: the README as its home page, the pages of `docs/`, the schema's element pages, a page per concept of this bundle with its trust label, and the bundle's exports, built and published by Knowledge website.

# Datasets

* [nist-csf-v2 LinkML schema](datasets/nist-csf-v2-linkml-schema.md) - The LinkML schema of the Cybersecurity Framework (CSF) 2.0, `src/nist_csf_v2/schema/nist_csf_v2.yaml` (schema id `https://w3id.org/lmodel/nist-csf-v2`, version 2.0.0): five classes, one enum with the value `withdrawn` and six identifier types. Its `lokf adapt` copy `.lokf/nist-csf-v2.yaml`, rooted on the function, the category and the subcategory, is the bundle's domain schema.
* [NIST's CSF 2.0 catalog copy](datasets/csf-catalog-copy.md) - NIST's catalog of the Cybersecurity Framework (CSF) 2.0 in the Open Security Controls Assessment Language (OSCAL), copied with NIST's licence from usnistgov/oscal-content v1.6.0 into `src/nist_csf_v2/schema/oscal-content/` and matched to that release by git object hash. The tests derive the whole framework from it, withdrawn CSF 1.1 elements included.
* [Generated artefacts](datasets/generated-artefacts.md) - What the LinkML generators and `lokf adapt` write from the schema: `project/` (JSON Schema, OWL, SHACL, ShEx, JSON-LD, GraphQL, protobuf, SQL, TypeScript, Excel and Java), the Python dataclasses and Pydantic models in `src/nist_csf_v2/datamodel/`, `docs/schema/` and `docs/elements/`, and `.lokf/nist-csf-v2.yaml`. None is edited by hand.
* [Test data and tests](datasets/test-data.md) - The schema's tests: seven valid examples and 29 counter-examples under `tests/data/`, `tests/test_data.py`, which holds each to the validator, `tests/test_upstream.py`, which derives the framework from NIST's catalog and holds the examples to it, `tests/test_watch.py`, which runs the upstream watch against stubbed answers, and `tests/test_schema_rules.py`, which holds the adapt copy apart from LOKF and the slsa, github-actions, oscal, spdx and nist-sp-800-218 copies in `tests/neighbours/`.

# References

* [NIST CSWP 29, the CSF 2.0](references/cswp-29.md) - NIST Cybersecurity White Paper 29, The NIST Cybersecurity Framework (CSF) 2.0 (February 26, 2024, <https://doi.org/10.6028/NIST.CSWP.29>), the edition the schema renders: a taxonomy of cybersecurity outcomes in six functions, 22 categories and 106 subcategories, with Profiles and Tiers for using it and a glossary.
* [NIST's CSF website](references/csf-site.md) - NIST's Cybersecurity Framework website, <https://www.nist.gov/cyberframework>: the publication, the Quick Start Guides, the Profiles, the Informative References it calls Mappings, and the community profiles, which the schema does not model.

# Explanations

* [Scope, influences and mappings](explanations/scope-and-influences.md) - What the schema renders and what it leaves out: the CSF 2.0 of CSWP 29 and nothing beyond it, with lmodel/slsa as its one influence on layout. It maps its classes to lmodel/oscal's, as NIST's catalog renders them, keeps the withdrawn CSF 1.1 elements as the catalog states them, and models neither the Informative References, the Profiles and Tiers, the risk-party marking nor the community profiles.
* [Element names and the shared namespace](explanations/element-names.md) - How the schema names its elements so that its adapt copy can sit beside LOKF's schema and the slsa, github-actions, oscal, spdx and nist-sp-800-218 copies: classes with the `Csf` prefix, NIST's identifiers kept as written, the identifier keys prefixed with `csf_`, every other key qualified with the CSF's own nouns, `title` and `description` carrying LOKF's IRIs, and no other key shared, which `tests/test_schema_rules.py` checks.

# Glossary

* [Function](glossary/function.md) - In the CSF, the highest level of organization for cybersecurity outcomes; there are six, GOVERN, IDENTIFY, PROTECT, DETECT, RESPOND and RECOVER. The schema renders a function as `CsfFunction`, with its two letters in `csf_function_id`.
* [Category](glossary/category.md) - In the CSF, a group of related cybersecurity outcomes that together make up a function, with an identifier such as GV.OC. The schema renders a category as `CsfCategory`, with its identifier in `csf_category_id`, and a withdrawn CSF 1.1 category with its status and destination.
* [Subcategory](glossary/subcategory.md) - In the CSF, a group of more specific outcomes of technical and management cybersecurity activities that make up a category, stated in a sentence with an identifier such as GV.OC-01. The schema renders a subcategory as `CsfSubcategory`, with its identifier in `csf_subcategory_id` and its statement in `description`.
* [Implementation example](glossary/implementation-example.md) - In the CSF, a concise, action-oriented, notional illustration of a way to help achieve a Core outcome, published by NIST beside the Core with an identifier such as GV.OC-01.001. The schema renders one as `CsfImplementationExample`.
* [Withdrawn element](glossary/withdrawn-element.md) - A CSF 1.1 category or subcategory that CSF 2.0 withdrew, which NIST's catalog keeps with the status `withdrawn` and, where NIST recorded it, the CSF 2.0 element it moved to or that incorporated its outcomes. The schema carries the status in `CsfElementStatus` and the destinations in the moved-to and incorporated-into attributes.

# Functions

* [GOVERN](functions/govern.md) - The CSF 2.0 function GV, GOVERN: the organization sets, communicates and monitors its strategy, expectations and policy for managing cybersecurity risk. It holds 6 categories, 31 subcategories and 119 implementation examples.
* [IDENTIFY](functions/identify.md) - The CSF 2.0 function ID, IDENTIFY: the organization understands its current cybersecurity risks. It holds 3 categories, 21 subcategories and 74 implementation examples.
* [PROTECT](functions/protect.md) - The CSF 2.0 function PR, PROTECT: the organization uses safeguards to manage its cybersecurity risks. It holds 5 categories, 22 subcategories and 77 implementation examples.
* [DETECT](functions/detect.md) - The CSF 2.0 function DE, DETECT: the organization finds and analyzes possible cybersecurity attacks and compromises. It holds 2 categories, 11 subcategories and 37 implementation examples.
* [RESPOND](functions/respond.md) - The CSF 2.0 function RS, RESPOND: the organization takes action on a detected cybersecurity incident. It holds 4 categories, 13 subcategories and 38 implementation examples.
* [RECOVER](functions/recover.md) - The CSF 2.0 function RC, RECOVER: the organization restores the assets and operations a cybersecurity incident affected. It holds 2 categories, 8 subcategories and 18 implementation examples.

# Playbooks

* [Regenerate and test after a schema change](playbooks/regenerate-and-test.md) - How to change the schema and check it: `uv sync --group dev`, edit `src/nist_csf_v2/schema/nist_csf_v2.yaml`, then `just lint`, `just gen-project`, `just gen-doc`, `just lokf-adapt` and `just test`, and the pre-commit hooks before a pull request.
* [Validate data against the schema](playbooks/validate-data.md) - How to validate CSF data with `linkml-validate` before loading it into the generated Python models, which check less: the dataclasses check no pattern, and the Pydantic models miss the identifier types' patterns. No check covers the nesting of identifiers, a repeated one, or the rules on withdrawn elements.
* [Update the upstream pins](playbooks/update-upstream-pins.md) - What to do when the weekly upstream watch reports that usnistgov/oscal-content holds another edition of the CSF, changed or dropped a pinned file or folder, or moved the pinned tag, that the copy drifted, or that a check could not finish: replace the copy whole from one release, move the pins in `scripts/check_upstream_release.py` and the schema header, and run the tests.
* [Cut a release](playbooks/release.md) - How a release is made: Conventional Commits on `main`, an `## [Unreleased]` changelog section, the `v0.0.0` baseline tag that keeps the first release at 0.1.0, and `semantic-release.yml`, which tags the release and dispatches Knowledge Release to attach `schema-<tag>-nist-csf-v2.yaml` once `KNOWLEDGE_RELEASE_ENABLED` is true.
* [Knowledge sources map](playbooks/knowledge-sources.md) - The librarian's scrape map: every repository location and external page this bundle derives concepts from, the concepts each yields, how to re-check each on a refresh run, and the paths left out on purpose.

# Policies

* [AI covenant](policies/ai-covenant.md) - The repository's rules for work done with artificial intelligence (AI): you own what you submit, an element under the schema renders CSWP 29 in the project's own words and cites it, NIST's catalog copy is never edited, and the scheduled librarian proposes changes only through reviewed pull requests.
* [License and attribution](policies/license-and-attribution.md) - The repository's licences: Apache 2.0 for the schema and the code, NIST's public-domain and CC0 terms for the CSF catalog copy, NIST's statement that its Technical Series publications are not subject to copyright in the United States, MIT for the copier template's scaffolding, and Apache 2.0 for the KTL sidecar and website templates.
* [Security policy](policies/security-policy.md) - How to report a vulnerability (GitHub's private vulnerability reporting), which release receives fixes (the latest), what executes in the repository and what holds each surface, the ruleset on `main`, and the two repository settings that are not yet in force.

# Workflows

* [Build and test (main.yaml)](workflows/main.md) - The Build and test workflow, `.github/workflows/main.yaml`: on a push to main and on every pull request, its test job runs `just test` on Python 3.10 to 3.14, and on 3.13 also `just lint` and `just lokf-adapt-check`, the check that `.lokf/nist-csf-v2.yaml` is current.
* [Lint & docs (lint-and-docs.yaml)](workflows/lint-and-docs.md) - The Lint & docs workflow, `.github/workflows/lint-and-docs.yaml`: on a push to main, every pull request, a Monday 06:00 UTC schedule and by hand, four jobs run ShellCheck, actionlint, the word budgets of CONTRIBUTING.md (1000) and SECURITY.md (900), and markdownlint, lychee and codespell over the Markdown.
* [Upstream watch (upstream-watch.yaml)](workflows/upstream-watch.md) - The Upstream watch workflow, `.github/workflows/upstream-watch.yaml`: every Monday at 07:00 UTC and by hand, its csf-catalog job runs `scripts/check_upstream_release.py` against usnistgov/oscal-content's releases and editions, and on a finding opens or updates the issue titled Upstream watch: NIST's CSF has changed.
* [Semantic release (semantic-release.yml)](workflows/semantic-release.md) - The Semantic release workflow, `.github/workflows/semantic-release.yml`: on a pull request into main, its plan job checks that the commits, the changelog and the title would release and previews the release; on a push to main, its release job in the release Environment tags vX.Y.Z, publishes the GitHub release and dispatches Knowledge Release.
* [Knowledge Registrar (knowledge-registrar.yaml)](workflows/knowledge-registrar.md) - The Knowledge Registrar workflow, `.github/workflows/knowledge-registrar.yaml`: the gate on the knowledge bundle, run on pull requests that touch `.lokf/` or `knowledge_bundle/`, every Monday at 06:00 UTC and by hand; it validates the bundle and its relation targets against the domain schema, runs the conventions script, and checks that each new confirmation by a person is backed by an approval or a signed commit.
* [Knowledge Librarian (knowledge-librarian.yaml)](workflows/knowledge-librarian.md) - The Knowledge Librarian workflow, `.github/workflows/knowledge-librarian.yaml`: every Monday at 05:00 UTC and by hand, once `KNOWLEDGE_LIBRARIAN_ENABLED` is true, it runs an agent with the ktl-librarian skill (pinned by `TRUST_LADDER_SKILLS_REF` at v0.59.0) in a read-only job and opens a review pull request from a separate job that runs no agent.
* [Knowledge Release (knowledge-release.yaml)](workflows/knowledge-release.md) - The Knowledge Release workflow, `.github/workflows/knowledge-release.yaml`: dispatched with a release's tag, or started by a published release once `KNOWLEDGE_RELEASE_ENABLED` is true, it attaches the bundle zip, the domain schema as `schema-<tag>-nist-csf-v2.yaml` with its checksum, and the Copilot skills to the release, when the bundle or the schema changed or `force` is set.
* [Knowledge sync (knowledge-sync.yaml)](workflows/knowledge-sync.md) - The Knowledge sync workflow, `.github/workflows/knowledge-sync.yaml`: every Monday at 04:10 UTC and by hand, it moves the sidecar's copies and the skills pin to the newest Knowledge Trust Ladder release through one pull request, opened with the `KNOWLEDGE_SYNC_TOKEN` secret, and holds the workflow changes for a person to approve.
* [Knowledge website (knowledge-website.yaml)](workflows/knowledge-website.md) - The Knowledge website workflow, `.github/workflows/knowledge-website.yaml`: on pushes and pull requests that touch the site's sources, every Monday at 05:23 UTC and by hand, its build job builds `website/` and checks its links read-only, and its deploy job publishes the default branch's build to GitHub Pages once `KNOWLEDGE_WEBSITE_ENABLED` is true.
