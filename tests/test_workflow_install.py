from __future__ import annotations

from pathlib import Path

from trie.workflow_install import (
    WORKFLOW_MARKER,
    WORKFLOW_RELPATH,
    install_triediff_workflow,
    render_triediff_workflow,
)


def _git_repo(tmp_path: Path) -> Path:
    (tmp_path / ".git").mkdir()
    return tmp_path


def test_render_bakes_in_diffs_dir_and_marker() -> None:
    text = render_triediff_workflow("triefacts/triediffs")
    assert text.startswith(WORKFLOW_MARKER)
    assert 'dir="triefacts/triediffs"' in text
    assert "gh pr comment" in text
    # GitHub expression syntax must survive the template formatting.
    assert "${{ github.event.pull_request.head.sha }}" in text

    custom = render_triediff_workflow("my/digests/")
    assert 'dir="my/digests"' in custom  # trailing slash normalised


def test_install_creates_updates_unchanged(tmp_path: Path) -> None:
    repo = _git_repo(tmp_path)

    created = install_triediff_workflow(repo, diffs_dir="triefacts/triediffs")
    assert created.action == "created"
    path = repo / WORKFLOW_RELPATH
    assert path.is_file()
    assert WORKFLOW_MARKER in path.read_text()

    # Idempotent rerun: no change.
    again = install_triediff_workflow(repo, diffs_dir="triefacts/triediffs")
    assert again.action == "unchanged"

    # Template drift (e.g. diffs_dir changed in config): updated in place.
    moved = install_triediff_workflow(repo, diffs_dir="elsewhere/diffs")
    assert moved.action == "updated"
    assert 'dir="elsewhere/diffs"' in path.read_text()


def test_install_never_touches_user_owned_file(tmp_path: Path) -> None:
    repo = _git_repo(tmp_path)
    path = repo / WORKFLOW_RELPATH
    path.parent.mkdir(parents=True)
    path.write_text("name: my own workflow\n")

    result = install_triediff_workflow(repo, diffs_dir="triefacts/triediffs")
    assert result.action == "skipped"
    assert "user-owned" in result.note
    assert path.read_text() == "name: my own workflow\n"


def test_install_skips_outside_git_repo(tmp_path: Path) -> None:
    result = install_triediff_workflow(tmp_path, diffs_dir="triefacts/triediffs")
    assert result.action == "skipped"
    assert "not a git repository" in result.note
    assert not (tmp_path / WORKFLOW_RELPATH).exists()


def test_install_dry_run_writes_nothing(tmp_path: Path) -> None:
    repo = _git_repo(tmp_path)

    result = install_triediff_workflow(repo, diffs_dir="triefacts/triediffs", dry_run=True)
    assert result.action == "created"
    assert not (repo / WORKFLOW_RELPATH).exists()
