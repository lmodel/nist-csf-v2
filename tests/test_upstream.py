"""Checks that the schema renders the CSF 2.0 edition NIST's catalog publishes.

NIST publishes the Cybersecurity Framework (CSF) 2.0 as an OSCAL catalog in
usnistgov/oscal-content, and src/nist_csf_v2/schema/oscal-content/ holds the
copy that scripts/check_upstream_release.py pins. These tests read the copy
with the standard library alone, derive from it the CsfFramework the schema
describes, and hold that framework to the validator and to the counts of the
publication's Core.
"""

import hashlib
import importlib.util
import json
from functools import lru_cache
from pathlib import Path

import yaml
from linkml.validator import validate

ROOT = Path(__file__).parent.parent
SCHEMA = ROOT / "src" / "nist_csf_v2" / "schema" / "nist_csf_v2.yaml"
COPY = ROOT / "src" / "nist_csf_v2" / "schema" / "oscal-content"
CATALOG = COPY / "NIST_CSF_v2.0_catalog.json"

# What CSF 2.0 holds, by CSWP 29's Appendix A: six functions, 22 categories
# and 106 subcategories, with the 363 implementation examples NIST publishes
# beside the Core. The catalog also keeps the CSF 1.1 categories and
# subcategories that CSF 2.0 withdrew, each marked withdrawn, and the 135
# links that say where each moved or what incorporated it.
COUNTS = {
    "functions": 6,
    "categories": 22,
    "subcategories": 106,
    "implementation examples": 363,
    "withdrawn categories": 12,
    "withdrawn subcategories": 79,
    "moves": 25,
    "incorporations": 110,
}
FUNCTIONS = ["GV", "ID", "PR", "DE", "RS", "RC"]
# Table 1 of CSWP 29's Appendix A, in the publication's order.
CATEGORIES = [
    "GV.OC", "GV.RM", "GV.RR", "GV.PO", "GV.OV", "GV.SC",
    "ID.AM", "ID.RA", "ID.IM",
    "PR.AA", "PR.AT", "PR.DS", "PR.PS", "PR.IR",
    "DE.CM", "DE.AE",
    "RS.MA", "RS.AN", "RS.CO", "RS.MI",
    "RC.RP", "RC.CO",
]  # fmt: skip
# The withdrawn categories for which the catalog names no destination.
WITHDRAWN_WITHOUT_DESTINATION = {"PR.IP", "PR.PT", "DE.DP", "RS.RP"}
# The catalog's first-party and third-party risk markings, which CSWP 29
# does not carry and the schema leaves out: how many CSF 2.0 subcategories
# carry each, and how many carry none.
MARKINGS = {"1st": 88, "3rd": 37, "unmarked subcategories": 3}


def _watch():
    spec = importlib.util.spec_from_file_location(
        "watch", ROOT / "scripts" / "check_upstream_release.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _blob_sha(path):
    data = path.read_bytes()
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


@lru_cache(maxsize=1)
def _header():
    return yaml.safe_load(SCHEMA.read_text())


@lru_cache(maxsize=1)
def _catalog():
    return json.loads(CATALOG.read_text(encoding="utf-8"))["catalog"]


def _prop(element, name):
    return next(p["value"] for p in element.get("props", []) if p["name"] == name)


def _status(element):
    """The status property's value, or None for an element of CSF 2.0."""
    values = [p["value"] for p in element.get("props", []) if p["name"] == "status"]
    assert len(values) <= 1, element["id"]
    return values[0] if values else None


def _prose(element, name):
    """The prose of the one part of the element with this name, or None when
    the part carries none, as a withdrawn category's statement does."""
    (part,) = [p for p in element.get("parts", []) if p["name"] == name]
    return part.get("prose")


def _withdrawal(element, entry, noun):
    """Carry a withdrawn element's status and its destinations into the
    schema's keys for the element's kind."""
    status = _status(element)
    if status:
        entry[f"{noun}_status"] = status
    for link in element.get("links", []):
        assert link["rel"] in ("moved_to", "incorporated_into"), link
        entry.setdefault(f"{noun}_{link['rel']}", []).append(link["href"])


def derive(catalog):
    """The CsfFramework that the catalog's groups, controls, parts, props and
    links describe, in the schema's terms."""
    version = _header()["version"]
    functions = []
    for group in catalog["groups"]:
        assert group["class"] == "function", group["id"]
        categories = []
        for category in group["controls"]:
            assert category["class"] == "category", category["id"]
            entry = {"csf_category_id": category["id"], "title": category["title"]}
            statement = _prose(category, "statement")
            if statement:
                entry["description"] = statement
            _withdrawal(category, entry, "category")
            subcategories = []
            for subcategory in category.get("controls", []):
                assert subcategory["class"] == "subcategory", subcategory["id"]
                examples = []
                for part in subcategory.get("parts", []):
                    if part["name"] == "guidance":
                        assert part["class"] == "example", part["id"]
                        examples.append(
                            {
                                "csf_implementation_example_id": part["id"],
                                "description": part["prose"],
                            }
                        )
                item = {
                    "csf_subcategory_id": subcategory["id"],
                    "description": _prose(subcategory, "statement"),
                    "subcategory_examples": examples,
                }
                _withdrawal(subcategory, item, "subcategory")
                subcategories.append(item)
            entry["category_subcategories"] = subcategories
            categories.append(entry)
        functions.append(
            {
                "csf_function_id": group["id"],
                "title": group["title"],
                "description": _prose(group, "overview"),
                "function_categories": categories,
            }
        )
    return {"csf_version": ".".join(version.split(".")[:2]), "csf_functions": functions}


@lru_cache(maxsize=1)
def _framework():
    return derive(_catalog())


def _categories():
    return [c for f in _framework()["csf_functions"] for c in f["function_categories"]]


def _subcategories():
    return [s for c in _categories() for s in c["category_subcategories"]]


def _live(entries, noun):
    return [e for e in entries if f"{noun}_status" not in e]


def _withdrawn(entries, noun):
    return [e for e in entries if e.get(f"{noun}_status") == "withdrawn"]


def test_copy_matches_the_pinned_blobs():
    """Every copied file has the git object hash the watch pins, so the copy
    is the file NIST published at the pinned commit, and nothing else is in
    the folder."""
    pinned = _watch().PINNED_BLOBS
    assert {p.name for p in COPY.iterdir()} == set(pinned)
    for name, (_source, sha) in pinned.items():
        assert _blob_sha(COPY / name) == sha, name


def test_header_pins_match_the_watch():
    """The header records the release, commit and publication the watch
    checks."""
    watch = _watch()
    header = _header()
    notes = header["annotations"]
    assert notes["oscal_content_tag"] == watch.PINNED_TAG
    assert notes["oscal_content_commit"] == watch.PINNED_COMMIT
    assert header["source"] == f"https://doi.org/{watch.PINNED_DOI}"
    tree = f"https://github.com/usnistgov/oscal-content/tree/{watch.PINNED_TAG}/"
    assert tree + watch.PINNED_PATH.rpartition("/")[0] in header["see_also"]


def test_catalog_is_the_pinned_edition():
    """The copy is NIST's final catalog of the edition in the header, by the
    identifier NIST's reference tool gives that edition."""
    metadata = _catalog()["metadata"]
    version = _header()["version"]
    identifier = "CSF_" + version.replace(".", "_")
    assert _header()["annotations"]["cprt_framework_version"] == identifier
    assert _prop(metadata, "framework-version-identifier") == identifier
    assert _prop(metadata, "publication-status") == "Final"


def test_derived_framework_validates():
    """The whole of CSF 2.0, as the catalog gives it, is a valid
    CsfFramework."""
    report = validate(_framework(), str(SCHEMA), "CsfFramework")
    assert not report.results, [r.message for r in report.results][:10]


def test_counts_match_the_publication():
    """The derived framework holds what CSWP 29's Core holds, and the
    withdrawn CSF 1.1 elements the catalog keeps beside it."""
    categories, subcategories = _categories(), _subcategories()
    withdrawn = _withdrawn(categories, "category") + _withdrawn(
        subcategories, "subcategory"
    )
    counted = {
        "functions": len(_framework()["csf_functions"]),
        "categories": len(_live(categories, "category")),
        "subcategories": len(_live(subcategories, "subcategory")),
        "implementation examples": sum(
            len(s["subcategory_examples"]) for s in subcategories
        ),
        "withdrawn categories": len(_withdrawn(categories, "category")),
        "withdrawn subcategories": len(_withdrawn(subcategories, "subcategory")),
        "moves": sum(
            len(e.get(k, []))
            for e in withdrawn
            for k in ("category_moved_to", "subcategory_moved_to")
        ),
        "incorporations": sum(
            len(e.get(k, []))
            for e in withdrawn
            for k in ("category_incorporated_into", "subcategory_incorporated_into")
        ),
    }
    assert counted == COUNTS
    assert len(categories) == COUNTS["categories"] + COUNTS["withdrawn categories"]
    assert len(subcategories) == (
        COUNTS["subcategories"] + COUNTS["withdrawn subcategories"]
    )


def test_functions_and_categories_are_the_publications():
    """The functions are the six of CSWP 29 in its order, and the CSF 2.0
    categories are the 22 of its Table 1."""
    assert [f["csf_function_id"] for f in _framework()["csf_functions"]] == FUNCTIONS
    live = {c["csf_category_id"] for c in _live(_categories(), "category")}
    assert live == set(CATEGORIES)


def test_identifiers_nest_and_are_unique():
    """Each identifier starts with the identifier of what holds it, which no
    pattern in the schema can check, and none repeats."""
    seen = []
    for function in _framework()["csf_functions"]:
        seen.append(function["csf_function_id"])
        for category in function["function_categories"]:
            assert category["csf_category_id"].startswith(
                function["csf_function_id"] + "."
            )
            seen.append(category["csf_category_id"])
            for subcategory in category["category_subcategories"]:
                assert subcategory["csf_subcategory_id"].startswith(
                    category["csf_category_id"] + "-"
                )
                seen.append(subcategory["csf_subcategory_id"])
                for example in subcategory["subcategory_examples"]:
                    assert example["csf_implementation_example_id"].startswith(
                        subcategory["csf_subcategory_id"] + "."
                    )
                    seen.append(example["csf_implementation_example_id"])
    assert len(seen) == len(set(seen))


def test_withdrawn_elements_state_their_destination():
    """A withdrawn element names where it moved or what incorporated it,
    never both, and each destination is an element of CSF 2.0. Four
    withdrawn categories name none, as the catalog has it. An element of
    CSF 2.0 names no destination. A withdrawn category holds only withdrawn
    subcategories and has no statement of its own; a category of CSF 2.0 may
    keep a withdrawn subcategory, as ID.AM keeps ID.AM-06."""
    functions = _framework()["csf_functions"]
    categories, subcategories = _categories(), _subcategories()
    live = {f["csf_function_id"] for f in functions}
    live |= {c["csf_category_id"] for c in _live(categories, "category")}
    live |= {s["csf_subcategory_id"] for s in _live(subcategories, "subcategory")}
    for noun, entries in (("category", categories), ("subcategory", subcategories)):
        for entry in entries:
            moved = entry.get(f"{noun}_moved_to", [])
            incorporated = entry.get(f"{noun}_incorporated_into", [])
            assert not (moved and incorporated), entry[f"csf_{noun}_id"]
            assert set(moved + incorporated) <= live, entry[f"csf_{noun}_id"]
            if entry.get(f"{noun}_status") == "withdrawn":
                if entry[f"csf_{noun}_id"] in WITHDRAWN_WITHOUT_DESTINATION:
                    assert not moved and not incorporated, entry[f"csf_{noun}_id"]
                else:
                    assert moved or incorporated, entry[f"csf_{noun}_id"]
            else:
                assert not moved and not incorporated, entry[f"csf_{noun}_id"]
    for category in _withdrawn(categories, "category"):
        assert "description" not in category, category["csf_category_id"]
        assert all(
            s.get("subcategory_status") == "withdrawn"
            for s in category["category_subcategories"]
        ), category["csf_category_id"]
    for category in _live(categories, "category"):
        assert category["description"], category["csf_category_id"]


def test_examples_belong_to_the_current_edition():
    """Every implementation example sits under a subcategory of CSF 2.0,
    none under a withdrawn one."""
    for subcategory in _withdrawn(_subcategories(), "subcategory"):
        assert not subcategory["subcategory_examples"], subcategory[
            "csf_subcategory_id"
        ]


def test_risk_party_markings_are_left_out():
    """The catalog marks CSF 2.0 subcategories as first-party risk,
    third-party risk or both. CSWP 29 carries no such marking, so the
    derived framework has no key for it; this test records what is left
    out, so a change in the catalog's markings is seen."""
    counted = {"1st": 0, "3rd": 0, "unmarked subcategories": 0}
    for group in _catalog()["groups"]:
        for category in group["controls"]:
            for subcategory in category.get("controls", []):
                markings = [
                    p for p in subcategory.get("props", []) if p["name"] == "marking"
                ]
                assert all(p["class"] == "risk-party" for p in markings)
                if _status(subcategory):
                    assert not markings, subcategory["id"]
                    continue
                if not markings:
                    counted["unmarked subcategories"] += 1
                for marking in markings:
                    counted[marking["value"]] += 1
    assert counted == MARKINGS
    keys = {k for s in _subcategories() for k in s}
    assert not any("risk" in k or "marking" in k for k in keys)
