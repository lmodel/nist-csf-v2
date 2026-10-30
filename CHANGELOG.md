# Changelog

All notable changes to this project are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

The `v0.0.0` tag is a baseline, not a release: it marks where versioning starts so the first real release is `0.1.0` rather than `1.0.0`. The schema stays below 1.0.0 until its shape settles, so a breaking change bumps the minor version. See [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers).

## [Unreleased]

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
