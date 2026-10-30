# Contributing to nist-csf-v2

*This file is a checklist, not a design log. Each rule is a line or two that links to where its reasoning lives: a code comment, a workflow header, or a linked page. `lint-and-docs.yaml` holds the file to a word budget so it stays that way.*

## What this project is

A LinkML schema of the Cybersecurity Framework (CSF) 2.0, which the National Institute of Standards and Technology (NIST) publishes as Cybersecurity White Paper (CSWP) 29. A knowledge bundle can type its concepts with the CSF's functions, categories and subcategories.

| Path | Holds |
| --- | --- |
| `src/nist_csf_v2/schema/nist_csf_v2.yaml` | The LinkML schema. Edit this. |
| `src/nist_csf_v2/schema/oscal-content/` | NIST's catalog of the CSF at the pinned release. Never edit. |
| `src/nist_csf_v2/datamodel/`, `project/`, `docs/schema/` | Artefacts generated from the schema. |
| `docs/` | The website's own pages. |
| `tests/` | Python tests, and valid and invalid example data. |
| `.lokf/knowledge/` | This repository's knowledge bundle. |

## Development setup

You need Python 3.10+, [uv](https://docs.astral.sh/uv/) and [just](https://github.com/casey/just).

```bash
git clone https://github.com/lmodel/nist-csf-v2.git
cd nist-csf-v2
uv sync --group dev
just --list
```

### Agent skills (optional, only for this repo's `.lokf/` bundle)

The bundle is maintained with the Knowledge Trust Ladder (KTL) skills, **installed, never committed**; continuous integration (CI) installs the librarian skill at run time, pinned to a release. Nothing in the schema depends on them. [The install page](https://w3id.org/ktl/docs/install/) lists every route; with npm:

```bash
npx skills add noelmcloughlin/knowledge-trust-ladder --skill ktl-librarian --yes   # derive concepts
npx skills add noelmcloughlin/knowledge-trust-ladder --skill ktl-curator --yes     # confirm them as a person
```

## Before opening a pull request

- **Edit the schema, then regenerate.** Edit `src/nist_csf_v2/schema/nist_csf_v2.yaml`, run `just gen-project`, `just gen-doc` and `just lokf-adapt`, and commit the output; `project/`, `src/nist_csf_v2/datamodel/`, `docs/schema/` and `.lokf/nist-csf-v2.yaml` are generated.
- **Render what CSWP 29 defines**, in your own words, and name the section or table in the pull request; [AI_COVENANT.md](AI_COVENANT.md) says why. `tests/test_upstream.py` holds the schema to NIST's catalog.
- **Leave `src/nist_csf_v2/schema/oscal-content/` as NIST published it.** Replace it whole from one release of usnistgov/oscal-content instead, and move the pins in `scripts/check_upstream_release.py` and the schema header; `upstream-watch.yaml` checks the copy.
- **Keep names apart.** A host imports this adapt copy beside the Linked Open Knowledge Format (LOKF) schema and the copies of slsa, github-actions and oscal, so a shared name carries one Internationalized Resource Identifier (IRI). `tests/test_schema_rules.py` checks.
- **Run the tests**: `just test` (schema generation, `pytest` and the examples under `tests/data/`). Example data goes in `tests/data/valid/` and `tests/data/invalid/`, named `ClassName-suffix.yaml`, with an invalid example per constraint.
- **Follow the schema's conventions**: UpperCamelCase classes with the `Csf` prefix, snake_case slots, attributes unless two classes share a field, a short description on every element. `just lint` checks, under `.linkmllint.yaml`.
- **Run the pre-commit hooks** on what you staged (`uvx pre-commit run`): ruff, yamllint, codespell, typos and the `uv.lock` check.
- **Lock files are part of the change.** CI installs with `uv sync --locked`; a dependency edit that does not update `uv.lock` (or `.lokf/uv.lock`) fails the run.
- **Knowledge-bundle changes**: `cd .lokf && just lokf-validate` must pass, and `knowledge-registrar.yaml` runs on any `.lokf/**` change.
- **`lint-and-docs.yaml` is easy to trip locally**: ShellCheck, actionlint, markdownlint against `.markdownlint-cli2.jsonc`, link-checking against `lychee.toml`, and codespell over every `*.md`.
- **Actions are pinned to commit hashes**, the version in a trailing comment, and bumped by Dependabot, never by hand to a tag.
- **The skills pin moves with the sidecar copies.** When moving `TRUST_LADDER_SKILLS_REF` in `.github/workflows/knowledge-librarian.yaml`, copy the other `knowledge-*.yaml` workflows and `.lokf/scripts/` and `.lokf/m365/` from that release's `skills/ktl-sidecar/templates/` in the same pull request.
- **If your change alters behaviour** (not just wording), add an entry under `## [Unreleased]` in [CHANGELOG.md](CHANGELOG.md).
- Keep changes focused, and fill in the pull request template.

## Code of conduct

Participation here is covered by the [Contributor Covenant](CODE_OF_CONDUCT.md).

## Using AI tools

Artificial intelligence (AI) assistance is welcome; [AI_COVENANT.md](AI_COVENANT.md) sets the rules, for people and the scheduled `knowledge-librarian` agent alike. You are the author of what you submit, and a claim about what the CSF defines must be checked against CSWP 29.

## Reporting issues

Use the [issue tracker](https://github.com/lmodel/nist-csf-v2/issues) for problems with the schema and requests for new elements. A problem in the CSF itself belongs with [NIST](https://www.nist.gov/cyberframework).

## Releasing (maintainers)

- Write `## [Unreleased]` in [CHANGELOG.md](CHANGELOG.md) as you go; the release job refuses an empty one (`.github/scripts/changelog-release.mjs check`).
- Type the commit ([Conventional Commits](https://www.conventionalcommits.org/)) for what the change *is*. Only `feat:`, `fix:`, `security:` and a breaking `!` start a release; other types leave their entries for the next release that does. A pull request that would release must carry a releasing type in its title too, since a squash merge takes its subject from it.
- On merge, [`semantic-release.yml`](.github/workflows/semantic-release.yml) retitles the section to `## [X.Y.Z] - YYYY-MM-DD`, commits `CHANGELOG.md`, tags `vX.Y.Z` and publishes the GitHub Release. No file is bumped. Once `KNOWLEDGE_RELEASE_ENABLED` is `true`, it dispatches `.github/workflows/knowledge-release.yaml`, which attaches the schema copy and the bundle when the bundle or the schema changed.
- That step runs behind the `release` GitHub Environment; configure required reviewers on it in Settings → Environments, or every qualifying merge is released unattended.
- Below 1.0.0: push the `v0.0.0` baseline tag on `main` before the first releasing merge, which then releases 0.1.0; both release jobs refuse to run without a `v*` tag, as semantic-release would otherwise start at 1.0.0. `.releaserc.json` maps `breaking: true` to `minor`; reaching 1.0.0 means removing that rule in a pull request of its own.
- A branch rule requiring pull requests, status checks or signed commits would reject the release job's own push to `main`; leave them off. [SECURITY.md](SECURITY.md) says what holds `main` instead, and the shared design is on [KTL's releasing page](https://github.com/noelmcloughlin/knowledge-trust-ladder/blob/main/docs/releasing.md).

## License

By contributing, you agree that your contributions are licensed under the [Apache License 2.0](LICENSE). NIST's catalog copy is under NIST's own terms; [NOTICE](NOTICE) lists it, so update it when you add something new from elsewhere.
