"""Data test."""

import glob
import os
from pathlib import Path

import pytest
import yaml
from linkml.validator import validate
from linkml_runtime.loaders import yaml_loader

import nist_csf_v2.datamodel.nist_csf_v2

DATA_DIR_VALID = Path(__file__).parent / "data" / "valid"
DATA_DIR_INVALID = Path(__file__).parent / "data" / "invalid"

VALID_EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR_VALID, "*.yaml"))
INVALID_EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR_INVALID, "*.yaml"))

SCHEMA = (
    Path(__file__).parent.parent
    / "src"
    / "nist_csf_v2"
    / "schema"
    / "nist_csf_v2.yaml"
)


@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES)
def test_valid_data_files(filepath):
    """Test loading of all valid data files."""
    target_class_name = Path(filepath).stem.split("-")[0]
    tgt_class = getattr(
        nist_csf_v2.datamodel.nist_csf_v2,
        target_class_name,
    )
    obj = yaml_loader.load(filepath, target_class=tgt_class)
    assert obj


# The JSON Schema the validator generates is the one check that applies every
# constraint (docs/index.md says what the generated models leave out), so each
# example is held to it: a valid one must pass, and a counter-example must fail.
@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES)
def test_valid_data_files_validate(filepath):
    """Every valid example passes the validator."""
    report = validate(
        yaml.safe_load(Path(filepath).read_text()),
        str(SCHEMA),
        Path(filepath).stem.split("-")[0],
    )
    assert not report.results, [r.message for r in report.results]


@pytest.mark.parametrize("filepath", INVALID_EXAMPLE_FILES)
def test_invalid_data_files_fail(filepath):
    """Every counter-example fails the validator."""
    report = validate(
        yaml.safe_load(Path(filepath).read_text()),
        str(SCHEMA),
        Path(filepath).stem.split("-")[0],
    )
    assert report.results


def test_every_concept_class_has_an_example():
    """Each class a knowledge-bundle concept may name as its type, and each
    class those hold, has a valid example."""
    classes = set(yaml.safe_load(SCHEMA.read_text())["classes"])
    examples = {Path(f).stem.split("-")[0] for f in VALID_EXAMPLE_FILES}
    assert classes <= examples, sorted(classes - examples)
