---
type: Playbook
id: https://w3id.org/lmodel/nist-csf-v2/knowledge/playbooks/update-upstream-pins
genre: how-to
title: Update the upstream pins
description: "What to do when the weekly upstream watch reports that usnistgov/oscal-content holds another edition of the CSF, released a changed CSF 2.0 catalog, or that the copy drifted: replace the copy whole from one release, move the pins in `scripts/check_upstream_release.py` and the schema header, and run the tests."
resource: scripts/check_upstream_release.py
about:
  - https://w3id.org/lmodel/nist-csf-v2/knowledge/datasets/csf-catalog-copy
sources:
  - id: check_upstream_release.py
    resource: scripts/check_upstream_release.py
    title: the docstring, the pins and the report lines
  - id: contributing.md
    resource: CONTRIBUTING.md
    title: the item on the catalog copy
  - id: test_upstream.py
    resource: tests/test_upstream.py
    title: the pin and edition tests
generated:
  by: process:ktl-librarian
  at: "2026-10-29T21:41:10Z"
status: draft
---

# Update the upstream pins

`scripts/check_upstream_release.py` runs every Monday in [Upstream watch](../workflows/upstream-watch.md) with the standard library alone. It asks doi.org nothing, because a Cybersecurity White Paper number is assigned paper by paper and the next edition's identifier cannot be predicted. It reports three kinds of finding.[^check_upstream_release.py]

- **A newer release of usnistgov/oscal-content holds another edition folder** beside `nist.gov/CSF/v2.0/`. Read NIST's publication of that edition, decide whether the schema moves to it, and replace the copy from that release.
- **A newer release changes the catalog** of the pinned edition. A release that leaves the catalog's blob as it was is reported and needs nothing.
- **A copied file differs from its pinned blob**, or the folder holds a file the script does not pin.

To replace the copy, take both files from one release: the catalog from `nist.gov/CSF/v2.0/json/`, or the new edition's folder, and `LICENSE.md` from the root. Never edit them.[^contributing.md] Then move `PINNED_TAG`, `PINNED_COMMIT` and `PINNED_BLOBS` in the script, and the `oscal_content_tag` and `oscal_content_commit` annotations and the `see_also` tree in the schema header, and update NOTICE. Run `just test`: `tests/test_upstream.py` checks that the header and the script name the same pins, that each file has its pinned hash, and that the derived framework still validates with the publication's counts.[^test_upstream.py] A new edition also moves the header's `version`, its `source` and the `cprt_framework_version` annotation, and `PINNED_DOI` and `PINNED_EDITIONS` in the script.

[^check_upstream_release.py]: scripts/check_upstream_release.py, the docstring and check_catalog
[^contributing.md]: CONTRIBUTING.md, the item on the catalog copy
[^test_upstream.py]: tests/test_upstream.py, the pin, hash and edition tests
