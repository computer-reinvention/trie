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


def test_render_comments_every_pr_digest_not_just_latest() -> None:
    """A PR spans many commits, each with its own digest; the workflow must
    enumerate every digest file the PR ADDED (via the PR files API) and
    comment each un-commented one — 'newest only' skipped intermediates."""
    text = render_triediff_workflow("triefacts/triediffs")
    assert "pulls/${PR}/files" in text, "must enumerate PR-added files"
    assert 'select(.status == "added")' in text
    assert "for path in $added" in text, "must loop over every added digest"
    # Shell escapes must survive templating into valid script text.
    assert r"grep '\.md$'" in text
    assert (
        "--paginate \
"
        in text
    ), "line continuations must reach the YAML"


def test_render_sync_bot_budget_and_guards() -> None:
    from trie.workflow_install import SYNC_BOT_MARKER, render_sync_bot_workflow

    text = render_sync_bot_workflow(budget=3.5)
    assert text.startswith(SYNC_BOT_MARKER)
    assert "--budget 3.5" in text, "per-run spend cap must be baked in"
    assert "secrets.ANTHROPIC_API_KEY" in text
    # Fork safety: secrets must never run for fork PRs.
    assert "github.event.pull_request.head.repo.full_name == github.repository" in text
    # Must gate on verify so a coherent tree costs nothing.
    assert "trie -q verify" in text


def test_install_sync_bot_same_ownership_contract(tmp_path) -> None:
    from trie.workflow_install import SYNC_BOT_RELPATH, install_sync_bot_workflow

    repo = _git_repo(tmp_path)
    created = install_sync_bot_workflow(repo, budget=5.0)
    assert created.action == "created"
    path = repo / SYNC_BOT_RELPATH
    assert path.is_file()

    assert install_sync_bot_workflow(repo, budget=5.0).action == "unchanged"
    moved = install_sync_bot_workflow(repo, budget=9.0)
    assert moved.action == "updated"
    assert "--budget 9.0" in path.read_text()

    path.write_text("name: user-owned\n")
    assert install_sync_bot_workflow(repo, budget=5.0).action == "skipped"


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
