#!/usr/bin/env python3
"""Check NIST's CSF 2.0 catalog copy against NIST's releases in oscal-content.

Three things can go wrong with ``src/nist_csf_v2/schema/oscal-content/``
without any change in this repository:

- NIST publishes a newer edition of the Cybersecurity Framework (CSF), so
  the schema falls behind;
- NIST releases a changed catalog of the pinned edition in
  usnistgov/oscal-content;
- the copied files drift from the files they were taken from.

The copy has no version in its path, so the release, the commit its tag
names and each file's git object hash are pinned below. This script asks the
GitHub API for usnistgov/oscal-content's latest release, the commit the
pinned tag names and a few folder listings, and compares every copied file
with its blob by git object hash, so nothing is downloaded but listings. It
prints a Markdown report and exits 1 when a newer edition is out, the
catalog changed, a file differs, the pinned tag moved, a release no longer
holds a pinned folder, or a check could not finish. A file NIST adds beside
the pinned ones is reported for information only.

It asks doi.org nothing. NIST publishes the CSF as a Cybersecurity White
Paper (CSWP), and CSWP numbers are assigned paper by paper. So the digital
object identifier (DOI) of the next edition cannot be predicted from the
pinned one the way a Special Publication's revision can. A new edition
appears instead as a new folder beside ``nist.gov/CSF/v2.0`` in oscal-content,
which the editions check below reports.

Set ``GITHUB_TOKEN`` to raise the API rate limit. Usage::

    python scripts/check_upstream_release.py [--report FILE]
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import urllib.error
import urllib.request
from functools import cache
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COPY = ROOT / "src" / "nist_csf_v2" / "schema" / "oscal-content"
API = "https://api.github.com/repos/usnistgov/oscal-content"
USER_AGENT = "lmodel-nist-csf-v2-upstream-check"

# The release and the commit its tag names. Move them together when the copy
# is replaced from a newer release, with PINNED_BLOBS and the schema header's
# annotations.
PINNED_TAG = "v1.6.0"
PINNED_COMMIT = "f0de6d8d8c059d374f15e0ae07508d82e370fc1d"

# The folder that holds the pinned edition's catalogs, and the folder that
# holds every edition NIST has published in OSCAL.
PINNED_PATH = "nist.gov/CSF/v2.0/json"
EDITIONS_PATH = "nist.gov/CSF"
PINNED_EDITIONS = {"v2.0"}

# Each copied file, the path it was taken from at PINNED_COMMIT, and its git
# object hash there. tests/test_upstream.py checks the hashes offline.
PINNED_BLOBS = {
    "NIST_CSF_v2.0_catalog.json": (
        f"{PINNED_PATH}/NIST_CSF_v2.0_catalog.json",
        "c808a0b30f9d8726e3e5309df7d16ef6e2857b7e",
    ),
    "LICENSE.md": ("LICENSE.md", "109af23dd24c2c465143aeab12ffebfffe2a4cd5"),
}

# Files in PINNED_PATH that the copy leaves out on purpose, so that only a
# file NIST adds is reported: the minified form of the same catalog.
LEFT_OUT = {"NIST_CSF_v2.0_catalog-min.json"}

# The edition the schema renders, as its DOI. The schema header's `source`
# carries the same address, and tests/test_upstream.py holds the two equal.
# No next edition is named here, for the reason the module docstring gives.
PINNED_DOI = "10.6028/NIST.CSWP.29"


def _get(url: str) -> bytes:
    req = urllib.request.Request(
        url,
        headers={"Accept": "application/vnd.github+json", "User-Agent": USER_AGENT},
    )
    token = os.environ.get("GITHUB_TOKEN")
    if token and url.startswith(API):
        # urllib copies ordinary headers onto a redirect, so the token goes in
        # an unredirected one and reaches api.github.com alone.
        req.add_unredirected_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read()


def _version_key(tag: str) -> tuple[int, ...]:
    """Numeric parts of a tag, padded so that v1.6 and v1.6.0 order alike."""
    parts = [int(x) for x in re.findall(r"\d+", tag)]
    return tuple(parts + [0] * (4 - len(parts)))


def _blob_sha(path: Path) -> str:
    """The git object hash of a file, as the contents API reports it."""
    data = path.read_bytes()
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


@cache
def _listing(path: str, ref: str) -> dict[str, dict]:
    """The entries of one folder at a ref, by name, or the one entry when the
    path is a file. A path the ref does not hold gives an empty mapping. Each
    listing is asked for once, and no caller changes what it returns."""
    try:
        entries = json.loads(_get(f"{API}/contents/{path}?ref={ref}"))
    except urllib.error.HTTPError as err:
        if err.code == 404:
            return {}
        raise
    if isinstance(entries, dict):
        entries = [entries]
    return {e["name"]: e for e in entries}


def _tag_commit(tag: str) -> str | None:
    """The commit a tag names, read through the tag object when the tag is an
    annotated one, or None when the repository has no such tag."""
    try:
        target = json.loads(_get(f"{API}/git/ref/tags/{tag}"))["object"]
    except urllib.error.HTTPError as err:
        if err.code == 404:
            return None
        raise
    while target["type"] == "tag":
        target = json.loads(_get(f"{API}/git/tags/{target['sha']}"))["object"]
    return target["sha"]


@cache
def _latest() -> str:
    """The tag of usnistgov/oscal-content's latest release, asked once."""
    return json.loads(_get(f"{API}/releases/latest"))["tag_name"]


def _newer(tag: str) -> bool:
    return _version_key(tag) > _version_key(PINNED_TAG)


def _added(listing: dict[str, dict]) -> list[str]:
    """The files of the pinned folder that are neither copied nor left out on
    purpose."""
    pinned = {source.rpartition("/")[2] for source, _ in PINNED_BLOBS.values()}
    return sorted(
        name
        for name, entry in listing.items()
        if entry.get("type", "file") == "file" and name not in pinned | LEFT_OUT
    )


def check_editions() -> tuple[list[str], bool]:
    """Report whether the latest release of oscal-content holds another
    edition of the CSF."""
    report = [f"- Pinned edition: CSF 2.0, https://doi.org/{PINNED_DOI}."]
    latest = _latest()
    if not _newer(latest):
        report.append(f"- Latest release: {latest}, the pinned one.")
        return report, False
    listing = _listing(EDITIONS_PATH, latest)
    if not listing:
        report.append(
            f"- **usnistgov/oscal-content {latest} no longer holds `{EDITIONS_PATH}/`.** "
            "Find where NIST now publishes the CSF in OSCAL, and move the pins."
        )
        return report, True
    editions = {n for n, e in listing.items() if e["type"] == "dir"}
    if editions - PINNED_EDITIONS:
        report.append(
            f"- **usnistgov/oscal-content {latest} holds another edition of the CSF:** "
            + ", ".join(
                f"`{EDITIONS_PATH}/{e}/`" for e in sorted(editions - PINNED_EDITIONS)
            )
            + ". Read NIST's publication of it, decide whether the schema moves to "
            "it, and replace the copy from that release."
        )
        return report, True
    report.append(
        f"- Latest release: {latest}, which holds no other edition of the CSF."
    )
    return report, False


def check_catalog() -> tuple[list[str], bool]:
    """Report whether the pinned tag still names the pinned commit, whether
    the copy is the files pinned there, and whether a newer release changes
    or drops any of them."""
    report = [
        f"- Pinned release: usnistgov/oscal-content {PINNED_TAG}, commit "
        f"`{PINNED_COMMIT[:12]}`, `{PINNED_PATH}/` copied to "
        "`src/nist_csf_v2/schema/oscal-content/`.",
    ]
    attention = False

    commit = _tag_commit(PINNED_TAG)
    if commit != PINNED_COMMIT:
        attention = True
        named = f"commit `{commit[:12]}`" if commit else "nothing"
        report.append(
            f"- **The tag {PINNED_TAG} now names {named}, not the pinned commit "
            f"`{PINNED_COMMIT[:12]}`.** Find out why NIST moved it before trusting "
            "either."
        )

    matching, differing = 0, []
    for name, (source, pinned_sha) in sorted(PINNED_BLOBS.items()):
        path = COPY / name
        folder, _, base = source.rpartition("/")
        upstream = _listing(folder or base, PINNED_COMMIT).get(base, {}).get("sha")
        if not path.is_file():
            differing.append(f"`{name}` is missing from the copy")
        elif upstream != pinned_sha:
            differing.append(
                f"`{source}` at commit `{PINNED_COMMIT[:12]}` is not the pinned blob"
            )
        elif _blob_sha(path) != pinned_sha:
            differing.append(f"`{name}` differs from `{source}` at {PINNED_TAG}")
        else:
            matching += 1
    extra = sorted(p.name for p in COPY.iterdir() if p.name not in PINNED_BLOBS)
    differing += [f"`{name}` is in the copy but not pinned" for name in extra]
    report.append(
        f"- {matching} of {len(PINNED_BLOBS)} copied files match the pinned commit byte for byte."
    )
    if differing:
        attention = True
        report.append(f"- **{len(differing)} problem(s) with the copy:**")
        report += [f"  - {d}" for d in differing]
    added = {PINNED_TAG: _added(_listing(PINNED_PATH, PINNED_COMMIT))}

    latest = _latest()
    if _newer(latest):
        changed, dropped = [], set()
        for name, (source, pinned_sha) in sorted(PINNED_BLOBS.items()):
            folder, _, base = source.rpartition("/")
            listing = _listing(folder or base, latest)
            if folder and not listing:
                dropped.add(folder)
            elif base not in listing:
                dropped.add(source)
            elif listing[base].get("sha") != pinned_sha:
                changed.append((name, source))
        for gone in sorted(dropped):
            attention = True
            shown = f"{gone}/" if gone == PINNED_PATH else gone
            report.append(
                f"- **usnistgov/oscal-content {latest} no longer holds `{shown}`.** "
                "Find where NIST now publishes it, and move the pins."
            )
        for name, source in changed:
            attention = True
            folder = source.rpartition("/")[0]
            report.append(
                f"- **usnistgov/oscal-content {latest} changes `{source}`.** Replace "
                f"`src/nist_csf_v2/schema/oscal-content/{name}` with the file at that tag "
                f"(https://github.com/usnistgov/oscal-content/tree/{latest}/{folder}), move "
                "the pins here and in the schema header, and run `just test`."
            )
        if not dropped and not changed:
            report.append(
                f"- Latest release: {latest}, which holds the pinned files unchanged."
            )
        if PINNED_PATH not in dropped:
            added[latest] = _added(_listing(PINNED_PATH, latest))

    for ref, names in added.items():
        if names:
            report.append(
                f"- For information, `{PINNED_PATH}/` at {ref} also holds "
                + ", ".join(f"`{n}`" for n in names)
                + ", which the copy neither holds nor leaves out on purpose."
            )
    return report, attention


# Each check, by the name the report gives it when it cannot finish.
CHECKS = (("editions", check_editions), ("catalog", check_catalog))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--report", type=Path, help="Also write the Markdown report to this file"
    )
    args = parser.parse_args(argv)
    lines, attention = [], False
    for label, check in CHECKS:
        try:
            found, needs = check()
        except (urllib.error.URLError, TimeoutError, OSError) as err:
            found, needs = [f"- **The {label} check could not finish: {err}.**"], True
        lines += found
        attention = attention or needs
    text = "\n".join(lines) + "\n"
    print(text, end="")
    if args.report:
        args.report.write_text(text, encoding="utf-8")
    return 1 if attention else 0


if __name__ == "__main__":
    sys.exit(main())
