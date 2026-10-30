# Change Log

## 2026-10-30

* **Changed**: Semantic release cites `.github/release/` for the lockfile both jobs install from.
* **Changed**: Semantic release says that both jobs install the release tools from `.github/release/package-lock.json`.
* **Changed**: Security policy counts the release tools' npm lock among what Dependabot keeps current.
* **Changed**: License and attribution names the knowledge bundle's CC BY 4.0 licence, as the README now does.
* **Changed**: Knowledge sources maps `.github/release/` to the Semantic release concept.
* **Changed**: nist-csf-v2 LinkML schema now says that the four identifier keys are top-level slots, each listed first in its class so that the generated dataclasses key each inlined list by its identifier.
* **Changed**: Generated artefacts no longer says `just test` leaves a generation date; LinkML 1.12.1 writes none.
* **Changed**: Update the upstream pins now regenerates the project, the docs and the adapt copy before `just test`.
* **Prose**: reworded 32 concept bodies in plain English. No fact, link, number or frontmatter changed.
* **Changed**: the six function concepts carry their two letters in `csf_function_id`, the key the schema now names; the pen removed and wrote each again, since it can set a key but not rename one.
* **Changed**: the generators' settings moved from `config.yaml` to `.linkml/generators.yaml`.
* **Changed**: Test data and tests now counts 29 counter-examples, each naming where it fails, and describes the test that holds the valid examples to NIST's catalog, the stubbed watch tests and the check on oscal mappings.
* **Changed**: nist-csf-v2 LinkML schema now names the `csf_` identifier keys, the required titles and non-blank descriptions, the one function a framework must hold, and the sixth identifier type.
* **Changed**: Element names and the shared namespace now says that the keys holding the functions and the identifiers carry a `csf_` prefix, as `docs/about.md` does.
* **Changed**: the glossary terms name the identifier keys the schema now uses, `csf_function_id`, `csf_category_id`, `csf_subcategory_id` and `csf_implementation_example_id`.
* **Changed**: Withdrawn element cites Appendix A's opening paragraph, where CSWP 29 says the gaps in the subcategory numbering mark relocated CSF 1.1 subcategories, in place of the glossary.
* **Changed**: Validate data against the schema now names LinkML 1.12.1 and six identifier types, as `docs/index.md` does.
* **Changed**: Update the upstream pins now lists the watch's findings for a dropped folder, a changed licence, a moved tag and an unfinished check, and the file NIST adds that it reports for information.
* **Changed**: Security policy now counts the website's npm packages among what Dependabot keeps current, as `.github/dependabot.yml` does.
* **Changed**: Documentation site now says that the retired schema's class pages redirect to their successors' pages or to the schema's index, as `website/site.config.mjs` does.
* **Changed**: Security policy now says that a ruleset on `main` blocks deletion and force-pushes, as `SECURITY.md` does since the repository's settings were read; two settings remain not in force.

## 2026-10-29

* **Added**: nist-csf-v2 LinkML schema, from `src/nist_csf_v2/schema/nist_csf_v2.yaml`, its adapt copy and the lokf-adapt recipes.
* **Added**: NIST's CSF 2.0 catalog copy, from `src/nist_csf_v2/schema/oscal-content/`, NOTICE and the watch's pins.
* **Added**: Generated artefacts, from the justfile's recipes, `config.yaml` and `project/`.
* **Added**: Test data and tests, from `tests/`.
* **Added**: NIST CSWP 29, the CSF 2.0, from the publication.
* **Added**: NIST's CSF website, from <https://www.nist.gov/cyberframework>.
* **Added**: Scope, influences and mappings, from the README, the changelog and `docs/about.md`.
* **Added**: Element names and the shared namespace, from `docs/about.md`, the README, `.linkmllint.yaml` and the schema rules test.
* **Added**: Function, from CSWP 29's glossary and the class `CsfFunction`.
* **Added**: Category, from CSWP 29's glossary and the class `CsfCategory`.
* **Added**: Subcategory, from CSWP 29's glossary and the class `CsfSubcategory`.
* **Added**: Implementation example, from CSWP 29's glossary and the class `CsfImplementationExample`.
* **Added**: Withdrawn element, from CSWP 29's Appendix A, the catalog copy and the enum `CsfElementStatus`.
* **Added**: GOVERN, the function GV, from NIST's catalog copy.
* **Added**: IDENTIFY, the function ID, from NIST's catalog copy.
* **Added**: PROTECT, the function PR, from NIST's catalog copy.
* **Added**: DETECT, the function DE, from NIST's catalog copy.
* **Added**: RESPOND, the function RS, from NIST's catalog copy.
* **Added**: RECOVER, the function RC, from NIST's catalog copy.
* **Added**: Regenerate and test after a schema change, from CONTRIBUTING.md and the recipes.
* **Added**: Validate data against the schema, from `docs/index.md`.
* **Added**: Update the upstream pins, from `scripts/check_upstream_release.py` and its tests.
* **Added**: Cut a release, from `.releaserc.json`, the changelog and CONTRIBUTING.md.
* **Added**: AI covenant, from `AI_COVENANT.md`.
* **Added**: License and attribution, from NOTICE, LICENSE and the README.
* **Added**: Security policy, from `SECURITY.md` and the Dependabot settings.
* **Added**: Documentation site, from `website/site.config.mjs` and `website/README.md`.
* **Added**: Build and test (main.yaml), from `.github/workflows/main.yaml`.
* **Added**: Lint & docs (lint-and-docs.yaml), from `.github/workflows/lint-and-docs.yaml`.
* **Added**: Upstream watch (upstream-watch.yaml), from `.github/workflows/upstream-watch.yaml`.
* **Added**: Semantic release (semantic-release.yml), from `.github/workflows/semantic-release.yml`.
* **Added**: Knowledge Registrar (knowledge-registrar.yaml), from `.github/workflows/knowledge-registrar.yaml`.
* **Added**: Knowledge Librarian (knowledge-librarian.yaml), from `.github/workflows/knowledge-librarian.yaml`.
* **Added**: Knowledge Release (knowledge-release.yaml), from `.github/workflows/knowledge-release.yaml`.
* **Added**: Knowledge sync (knowledge-sync.yaml), from `.github/workflows/knowledge-sync.yaml`.
* **Added**: Knowledge website (knowledge-website.yaml), from `.github/workflows/knowledge-website.yaml`.
* **Added**: Knowledge sources map, the bootstrap's map of what each source yields and how to re-check it, with the paths left out on purpose.
* **Removal**: the sidecar's two example services, which the bootstrap's concepts replace.
* **Initialization**: Scaffolded the LOKF bundle for nist-csf-v2 with placeholder
  services. Real concepts to follow.
