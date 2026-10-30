"""Checks the upstream watch's decisions against stubbed GitHub API answers.

scripts/check_upstream_release.py asks the GitHub API about
usnistgov/oscal-content. These tests replace its one network call, `_get`,
with a table of answers, so they run offline and show what the report says
when a release drops a folder, the network fails, NIST adds a file or the
pinned tag moves.
"""

import importlib.util
import json
import urllib.error
from pathlib import Path

import pytest

ROOT = Path(__file__).parent.parent
SCRIPT = ROOT / "scripts" / "check_upstream_release.py"
NEWER = "v9.0.0"


@pytest.fixture
def watch():
    """A fresh copy of the script, so no test sees another's cached answers."""
    spec = importlib.util.spec_from_file_location("watch_under_test", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _answers(watch, latest):
    """What the API answers when nothing has changed since the pin, with
    `latest` as the latest release, keyed by the address the script asks."""
    api = watch.API
    catalog_name, (catalog_path, catalog_sha) = next(
        (n, v) for n, v in watch.PINNED_BLOBS.items() if n != "LICENSE.md"
    )
    licence_sha = watch.PINNED_BLOBS["LICENSE.md"][1]
    folder = [
        {"name": catalog_name, "type": "file", "sha": catalog_sha},
        {"name": next(iter(watch.LEFT_OUT)), "type": "file", "sha": "0" * 40},
    ]
    licence = {"name": "LICENSE.md", "type": "file", "sha": licence_sha}
    answers = {
        f"{api}/releases/latest": {"tag_name": latest},
        f"{api}/git/ref/tags/{watch.PINNED_TAG}": {
            "object": {"type": "tag", "sha": "1" * 40}
        },
        f"{api}/git/tags/{'1' * 40}": {
            "object": {"type": "commit", "sha": watch.PINNED_COMMIT}
        },
    }
    for ref in {watch.PINNED_COMMIT, latest}:
        answers[f"{api}/contents/{watch.PINNED_PATH}?ref={ref}"] = list(folder)
        answers[f"{api}/contents/LICENSE.md?ref={ref}"] = licence
        answers[f"{api}/contents/{watch.EDITIONS_PATH}?ref={ref}"] = [
            {"name": e, "type": "dir"} for e in sorted(watch.PINNED_EDITIONS)
        ]
    return answers


def _stub(watch, answers):
    """Make `_get` answer from the table: an exception is raised, a missing
    address is a 404, and anything else is returned as JSON."""

    def get(url):
        if url not in answers:
            raise urllib.error.HTTPError(url, 404, "Not Found", None, None)
        answer = answers[url]
        if isinstance(answer, Exception):
            raise answer
        return json.dumps(answer).encode()

    watch._get = get


def _run(watch, tmp_path):
    report = tmp_path / "report.md"
    code = watch.main(["--report", str(report)])
    return code, report.read_text(encoding="utf-8")


def test_nothing_changed(watch, tmp_path):
    """With the pinned release the latest and every blob as pinned, the watch
    reports the copy current and exits 0."""
    _stub(watch, _answers(watch, watch.PINNED_TAG))
    code, text = _run(watch, tmp_path)
    assert code == 0, text
    assert f"Latest release: {watch.PINNED_TAG}, the pinned one." in text
    assert "2 of 2 copied files match" in text


def test_a_release_that_drops_the_folders(watch, tmp_path):
    """A newer release without the pinned folder or the editions folder is
    reported as such, not as a crash."""
    answers = _answers(watch, NEWER)
    del answers[f"{watch.API}/contents/{watch.PINNED_PATH}?ref={NEWER}"]
    del answers[f"{watch.API}/contents/{watch.EDITIONS_PATH}?ref={NEWER}"]
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert (
        f"**usnistgov/oscal-content {NEWER} no longer holds `{watch.PINNED_PATH}/`.**"
        in text
    )
    assert (
        f"**usnistgov/oscal-content {NEWER} no longer holds `{watch.EDITIONS_PATH}/`.**"
        in text
    )


def test_a_release_that_changes_the_licence(watch, tmp_path):
    """Every pinned file is compared at a newer release, the licence too."""
    answers = _answers(watch, NEWER)
    answers[f"{watch.API}/contents/LICENSE.md?ref={NEWER}"] = {
        "name": "LICENSE.md",
        "type": "file",
        "sha": "2" * 40,
    }
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert f"**usnistgov/oscal-content {NEWER} changes `LICENSE.md`.**" in text


def test_a_network_failure_still_writes_a_report(watch, tmp_path):
    """A check that cannot reach the API is reported as unfinished, sets
    attention, and leaves the other check to run."""
    answers = _answers(watch, NEWER)
    answers[f"{watch.API}/contents/{watch.EDITIONS_PATH}?ref={NEWER}"] = (
        urllib.error.URLError("Connection refused")
    )
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert (
        "**The editions check could not finish: <urlopen error Connection refused>.**"
        in text
    )
    assert "2 of 2 copied files match" in text


def test_a_file_nist_adds_is_information_only(watch, tmp_path):
    """A file in the pinned folder that the copy neither holds nor leaves out
    on purpose is reported, and is not a reason to fail."""
    answers = _answers(watch, watch.PINNED_TAG)
    folder = f"{watch.API}/contents/{watch.PINNED_PATH}?ref={watch.PINNED_COMMIT}"
    answers[folder] = answers[folder] + [
        {"name": "NIST_CSF_v2.0_profile.json", "type": "file", "sha": "3" * 40}
    ]
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 0, text
    assert "For information" in text and "`NIST_CSF_v2.0_profile.json`" in text


def test_a_moved_tag(watch, tmp_path):
    """A pinned tag that names another commit sets attention."""
    answers = _answers(watch, watch.PINNED_TAG)
    answers[f"{watch.API}/git/tags/{'1' * 40}"] = {
        "object": {"type": "commit", "sha": "4" * 40}
    }
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert f"**The tag {watch.PINNED_TAG} now names commit `444444444444`" in text
