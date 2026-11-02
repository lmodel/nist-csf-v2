# Changelog

All notable changes to this project are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

The `v0.0.0` tag is a baseline, not a release: it marks where versioning starts so the first real release is `0.1.0` rather than `1.0.0`. The schema stays below 1.0.0 until its shape settles, so a breaking change bumps the minor version. See [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers).

## [Unreleased]

## [0.2.1] - 2026-11-02

### Security

- **The sidecar copies and the skills pin are at Knowledge Trust Ladder [v0.60.0](https://github.com/noelmcloughlin/knowledge-trust-ladder/compare/v0.59.0...v0.60.0).** The release changed `.github/workflows/knowledge-registrar.yaml`, `.github/workflows/knowledge-librarian.yaml`, `.github/workflows/knowledge-release.yaml`, `.github/workflows/knowledge-sync.yaml`, `.lokf/scripts/knowledge-preflight.sh`, `.lokf/.gitignore`, `.lokf/justfile`, `website/package-lock.json`, `website/package.json`, `website/scripts/config.mjs`, `website/scripts/sync.mjs` and `.github/workflows/knowledge-website.yaml` here.

## [0.2.0] - 2026-11-01

### Added

- **The first-party and third-party risk marking of each CSF 2.0 subcategory**, as `subcategory_risk_parties` with the `CsfRiskParty` values `first_party` and `third_party`. NIST's catalog gives it to 103 of the 106 subcategories, and the upstream test now derives it and holds it to the catalog's counts.

## [0.1.0] - 2026-10-30

### Added

- **A LinkML schema of the Cybersecurity Framework (CSF) 2.0**, which the National Institute of Standards and Technology (NIST) publishes as Cybersecurity White Paper (CSWP) 29. It holds the six functions, their categories and subcategories, the implementation examples NIST publishes with the subcategories, and the CSF 1.1 categories and subcategories that CSF 2.0 withdrew, each with its status and where it moved or what incorporated it.
- **A copy of NIST's CSF 2.0 catalog from usnistgov/oscal-content v1.6.0, and a weekly upstream watch.** A test derives the whole framework from the copy and holds it to the validator and to the publication's counts, and the watch reports a new edition folder in oscal-content, a changed catalog or a drifted copy.
- **`.lokf/nist-csf-v2.yaml`, the schema's `lokf adapt` copy, rooted on the function, the category and the subcategory.** The knowledge release attaches it as `schema-<tag>-nist-csf-v2.yaml`, and tests hold its names apart from those of the Linked Open Knowledge Format (LOKF) and of the slsa, github-actions, oscal, spdx and nist-sp-800-218 copies, with which it shares no key.
- **An example of each class and a counter-example for each constraint**, held to the validator by `just test`.
- **The repository's Knowledge Trust Ladder (KTL) knowledge bundle and its sidecar automation**, from the KTL v0.59.0 templates with the lokf floor at 0.9.0, and a knowledge website that replaces the mkdocs site.
- **`.github/release/package-lock.json`, which pins semantic-release and every package it pulls in.** The release job installs from it with `npm ci`, and Dependabot keeps it current.

### Changed

- **The schema models the CSF's own elements, not a copy of a catalog in the Open Security Controls Assessment Language (OSCAL).** The OSCAL-shaped classes shared names with LOKF's and lmodel/oscal's, and their `class_uri: linkml:Any` let a catalog with any keys validate.
- **The schema's name is `nist_csf_v2`, as its file and package are, and the Python project's name is `nist-csf-v2-linkml`.** PyPI publishing stays off.

### Removed

- **The schema-level mappings to CIS Controls.** An analogy between CSF functions and CIS controls is not an authority; CIS's own mapping relates safeguards to subcategories, and belongs in data.
- **The PyPI publishing workflow and the mkdocs site and its preview.** The knowledge website replaces the site.
