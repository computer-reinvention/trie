"""Tests for the turn-boundary freshness gate.

The gate has four states, and each is exercised here:

  1. `fresh` — stamp matches current HEAD and mtimes; no refresh fires.
  2. `no_stamp` — fresh checkout, no `.trie/graph.head` yet; full refresh fires.
  3. `head_moved` — `git pull` or commit changed HEAD; full refresh fires.
  4. `mtimes_moved` — files edited since last refresh; refresh fires (and
     `run_incremental` only re-parses changed files internally).

The non-git case must raise `NotAGitRepoError` rather than degrade silently —
silent degradation is the failure mode the gate exists to prevent.
"""

from __future__ import annotations

import json
import subprocess
import time
from pathlib import Path

import pytest

from tests.fake_client import FakeTrieClient
from trie.config import Config
from trie.freshness import (
    NotAGitRepoError,
    Stamp,
    ensure_fresh_after_turn,
    ensure_fresh_before_turn,
    read_stamp,
    scan_mtimes,
    stamp_path,
    write_stamp,
)
from trie.graph.store import Store

# ---------------------------------------------------------------------------
# Test scaffolding: a real git repo with a real trie.toml and two real source
# files. The gate's whole point is to interact with git + filesystem; mocking
# would just measure the mocks.
# ---------------------------------------------------------------------------


def _git(args: list[str], cwd: Path) -> None:
    """Run git with deterministic identity so commits succeed in CI sandboxes."""
    subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True)


def _init_repo(path: Path) -> None:
    _git(["init", "-q", "-b", "main"], path)
    _git(["config", "user.email", "trie-test@example.com"], path)
    _git(["config", "user.name", "trie test"], path)


@pytest.fixture
def project(tmp_path: Path) -> Path:
    """Two-module project under a real git repo with one initial commit."""
    (tmp_path / "trie.toml").write_text(
        '[trie]\nversion = "0.1.2"\n'
        '[scope]\ninclude = ["src/**/*.py"]\nexclude = ["**/__pycache__/**"]\n'
        '[triefacts]\nroot = "triefacts"\nsource_root = "."\n'
        '[models]\nbootstrap = "anthropic/claude-sonnet-4-6"\n'
        'cascade = "anthropic/claude-sonnet-4-6"\n'
        "[cascade]\ndefault_depth = 1\nhub_symbol_threshold = 20\n"
    )
    src = tmp_path / "src"
    src.mkdir()
    (src / "__init__.py").write_text("")
    (src / "alpha.py").write_text('"""Alpha."""\n\n\ndef alpha_fn():\n    return 1\n')
    (src / "beta.py").write_text(
        '"""Beta."""\n\nfrom src.alpha import alpha_fn\n\n\ndef beta_fn():\n    return alpha_fn() + 1\n'
    )

    _init_repo(tmp_path)
    _git(["add", "."], tmp_path)
    _git(["commit", "-q", "-m", "initial"], tmp_path)
    return tmp_path


# ---------------------------------------------------------------------------
# Stamp file: read/write round-trips and tolerance for malformed input.
# ---------------------------------------------------------------------------


def test_stamp_round_trip(project: Path):
    stamp = Stamp(head="abc123", mtimes={"src/alpha.py": 1234.5})
    write_stamp(project, stamp)
    assert read_stamp(project) == stamp


def test_read_stamp_returns_none_when_missing(project: Path):
    assert read_stamp(project) is None


def test_read_stamp_returns_none_on_malformed_json(project: Path):
    stamp_path(project).parent.mkdir(parents=True, exist_ok=True)
    stamp_path(project).write_text("{not valid json")
    assert read_stamp(project) is None


def test_read_stamp_returns_none_on_wrong_schema(project: Path):
    stamp_path(project).parent.mkdir(parents=True, exist_ok=True)
    stamp_path(project).write_text(json.dumps({"head": 42, "mtimes": {}}))  # head not a str
    assert read_stamp(project) is None


def test_write_stamp_is_atomic_no_partial_files_left_behind(project: Path):
    """The temp file used for atomic rename must not survive the call."""
    write_stamp(project, Stamp(head="abc", mtimes={}))
    parent = stamp_path(project).parent
    leftovers = [p for p in parent.iterdir() if p.suffix == ".tmp"]
    assert leftovers == []


# ---------------------------------------------------------------------------
# mtime scanning.
# ---------------------------------------------------------------------------


def test_scan_mtimes_returns_in_scope_files_only(project: Path):
    config, _ = Config.find_and_load(project)
    mtimes = scan_mtimes(project, config)
    # The scope glob is `src/**/*.py`; trie.toml is not included.
    assert "src/alpha.py" in mtimes
    assert "src/beta.py" in mtimes
    assert "trie.toml" not in mtimes


def test_scan_mtimes_changes_after_file_edit(project: Path):
    config, _ = Config.find_and_load(project)
    before = scan_mtimes(project, config)
    time.sleep(0.01)  # ensure mtime resolution clears
    alpha = project / "src" / "alpha.py"
    alpha.write_text(alpha.read_text() + "\n# edit\n")
    after = scan_mtimes(project, config)
    assert before["src/alpha.py"] != after["src/alpha.py"]
    assert before["src/beta.py"] == after["src/beta.py"]


# ---------------------------------------------------------------------------
# Hard error outside git.
# ---------------------------------------------------------------------------


def test_ensure_fresh_raises_outside_git(tmp_path: Path):
    """No git repo, no fallback: gate refuses to run rather than guess."""
    (tmp_path / "trie.toml").write_text(
        '[trie]\nversion = "0.1.2"\n'
        '[scope]\ninclude = ["**/*.py"]\nexclude = []\n'
        '[triefacts]\nroot = "triefacts"\nsource_root = "."\n'
        '[models]\nbootstrap = "anthropic/claude-sonnet-4-6"\n'
        'cascade = "anthropic/claude-sonnet-4-6"\n'
        "[cascade]\ndefault_depth = 1\nhub_symbol_threshold = 20\n"
    )
    config, _ = Config.find_and_load(tmp_path)
    db = tmp_path / ".trie" / "graph.db"
    db.parent.mkdir(parents=True, exist_ok=True)
    with Store(db) as store, pytest.raises(NotAGitRepoError):
        ensure_fresh_before_turn(
            project_root=tmp_path,
            config=config,
            store=store,
            client=FakeTrieClient(output_body="## `body`\n\nDeterministic."),
        )


# ---------------------------------------------------------------------------
# The four states: unchanged, no_stamp, head_moved, mtimes_moved.
# ---------------------------------------------------------------------------


def _run_before_turn(
    project: Path, client: FakeTrieClient | None = None, *, sync_prose: bool = False
):
    """Run the pre-turn gate, returning the FreshnessResult.

    A caller that needs to inspect LLM call counts after the run can pass its
    own FakeTrieClient instance and read `.calls` on it. The default behaviour
    matches the original helper for tests that don't care about call counts.
    """
    config, _ = Config.find_and_load(project)
    db = project / ".trie" / "graph.db"
    db.parent.mkdir(parents=True, exist_ok=True)
    with Store(db) as store:
        return ensure_fresh_before_turn(
            project_root=project,
            config=config,
            store=store,
            client=client or FakeTrieClient(output_body="## `body`\n\nDeterministic."),
            sync_prose=sync_prose,
        )


def _run_after_turn(project: Path, client: FakeTrieClient | None = None):
    config, _ = Config.find_and_load(project)
    db = project / ".trie" / "graph.db"
    db.parent.mkdir(parents=True, exist_ok=True)
    with Store(db) as store:
        return ensure_fresh_after_turn(
            project_root=project,
            config=config,
            store=store,
            client=client or FakeTrieClient(output_body="## `body`\n\nDeterministic."),
        )


def test_no_stamp_triggers_scan_without_llm(project: Path):
    """First run in a fresh checkout: no stamp exists (and the store starts
    empty), graph scan fires but the LLM is NOT called. Trie does not auto-spend
    dollars on first contact; the user opts into prose regen by running
    `trie sync` explicitly.

    The store is empty on first contact, so the empty-store guard reports
    `empty_store` — which drives the same scan-only, no-LLM rebuild as
    `no_stamp`. Both paths converge; the reason label just records which guard
    fired first.
    """
    client = FakeTrieClient(output_body="## `body`\n\nDeterministic.")
    result = _run_before_turn(project, client=client)
    assert result.refreshed is True
    assert result.reason == "empty_store"
    assert result.incremental is None, "first contact must not invoke run_incremental"
    assert client.calls == 0, "first contact must not invoke the LLM"
    # The stamp now exists and records current HEAD.
    stamp = read_stamp(project)
    assert stamp is not None
    assert stamp.head == result.head


def test_empty_store_with_valid_stamp_self_heals(project: Path):
    """Regression: a wiped graph.db with an otherwise-valid stamp must rebuild,
    not no-op.

    The stamp records *when* we last refreshed, not *whether the graph still
    exists*. If `.trie/graph.db` is wiped or regenerated empty while the stamp
    still points at the current HEAD with matching mtimes, the stamp-based
    verdict would be `unchanged` and return a no-op against an empty graph.
    That surfaces downstream as "No system model loaded". The empty-store guard
    must override the stamp and force a scan-only rebuild.
    """
    # Prime a full refresh so a valid stamp exists and the graph is populated.
    first = _run_before_turn(project)
    assert first.refreshed is True
    stamp_before = read_stamp(project)
    assert stamp_before is not None

    # Wipe the graph data but leave the stamp untouched: simulate a corrupted
    # or externally-regenerated empty DB. Deleting the file and reopening a
    # fresh Store gives us an empty schema with the stamp still in place.
    db = project / ".trie" / "graph.db"
    with Store(db) as store:
        assert store.count_symbols() > 0
    db.unlink()
    with Store(db) as store:
        assert store.count_symbols() == 0

    # Stamp still matches HEAD + mtimes, but the store is empty.
    client = FakeTrieClient(output_body="## `body`\n\nDeterministic.")
    healed = _run_before_turn(project, client=client)
    assert healed.refreshed is True
    assert healed.reason == "empty_store"
    assert healed.incremental is None, "self-heal must not invoke run_incremental"
    assert client.calls == 0, "self-heal rebuilds from triefacts; no LLM"

    # The graph is repopulated.
    with Store(db) as store:
        assert store.count_symbols() > 0


def test_unchanged_state_is_a_noop(project: Path):
    """After a refresh, an immediate second call must do nothing."""
    _run_before_turn(project)  # primes the stamp
    second = _run_before_turn(project)
    assert second.refreshed is False
    assert second.reason == "unchanged"
    assert second.incremental is None


def test_head_moved_triggers_scan_without_llm(project: Path):
    """A new commit shifts HEAD; the gate rescans the graph but trusts the
    committed triefacts. No LLM call — `git pull` pulled in someone else's
    triefact prose along with their code, and we don't want to overwrite it."""
    _run_before_turn(project)
    before_head = read_stamp(project).head

    # Add an unrelated file and commit — HEAD moves but no in-scope file changes.
    (project / "README.md").write_text("hello\n")
    _git(["add", "README.md"], project)
    _git(["commit", "-q", "-m", "add readme"], project)

    client = FakeTrieClient(output_body="## `body`\n\nDeterministic.")
    result = _run_before_turn(project, client=client)
    assert result.refreshed is True
    assert result.reason == "head_moved"
    assert result.incremental is None, "head_moved must not invoke run_incremental"
    assert client.calls == 0, "head_moved must not invoke the LLM"
    after_head = read_stamp(project).head
    assert after_head != before_head


def test_mtimes_moved_is_graph_only_and_marks_stale(project: Path):
    """Edit a file without committing: HEAD unchanged, mtime moved. By default
    refresh is FAST — it rebuilds the graph (no LLM) and records the drifted
    triefacts as stale in pending.json rather than regenerating prose inline."""
    from trie.activity import read_pending

    _run_before_turn(project)
    before_head = read_stamp(project).head

    time.sleep(0.01)
    alpha = project / "src" / "alpha.py"
    alpha.write_text(alpha.read_text() + "\n# tweak\n")

    client = FakeTrieClient(output_body="## `body`\n\nDeterministic.")
    result = _run_before_turn(project, client=client)
    assert result.refreshed is True
    assert result.reason == "mtimes_moved"
    assert result.incremental is None, "default mtimes_moved must NOT invoke run_incremental"
    assert client.calls == 0, "default refresh must not touch the LLM"
    assert "src/alpha.py" in result.stale_files
    # The stale set is persisted for `trie status` / the editor to read.
    pending = read_pending(project)
    assert pending is not None
    assert "src/alpha.py" in pending.stale
    assert read_stamp(project).head == before_head


def test_mtimes_moved_with_sync_prose_runs_inline(project: Path):
    """The opt-in `sync_prose=True` path restores inline LLM regen and clears
    the pending set."""
    from trie.activity import read_pending

    _run_before_turn(project)
    time.sleep(0.01)
    alpha = project / "src" / "alpha.py"
    alpha.write_text(alpha.read_text() + "\n# tweak\n")

    client = FakeTrieClient(output_body="## `body`\n\nDeterministic.")
    result = _run_before_turn(project, client=client, sync_prose=True)
    assert result.refreshed is True
    assert result.reason == "mtimes_moved"
    assert result.incremental is not None, "sync_prose=True must invoke run_incremental"
    # Inline sync leaves the working tree clean.
    pending = read_pending(project)
    assert pending is not None
    assert pending.stale == ()


def test_new_file_added_triggers_refresh(project: Path):
    """A newly-created in-scope file should be detected by the mtime sweep
    even though it has no prior mtime in the stamp."""
    _run_before_turn(project)

    (project / "src" / "gamma.py").write_text('"""Gamma."""\n\n\ndef gamma_fn():\n    return 0\n')

    result = _run_before_turn(project)
    assert result.refreshed is True
    assert result.reason == "mtimes_moved"


def test_removed_file_triggers_refresh(project: Path):
    """Removing an in-scope file shifts the mtime map's key set."""
    _run_before_turn(project)
    (project / "src" / "alpha.py").unlink()

    result = _run_before_turn(project)
    assert result.refreshed is True
    assert result.reason == "mtimes_moved"


# ---------------------------------------------------------------------------
# Before vs after: same logic, different label. Pinning that they're equivalent.
# ---------------------------------------------------------------------------


def test_after_turn_picks_up_just_made_edit(project: Path):
    """The workhorse case: agent finishes a turn, file mtimes moved, gate
    catches everything before the next observer reads the graph."""
    _run_before_turn(project)  # prime
    time.sleep(0.01)
    (project / "src" / "alpha.py").write_text(
        '"""Alpha."""\n\n\ndef alpha_fn():\n    return 2  # changed\n'
    )

    result = _run_after_turn(project)
    assert result.refreshed is True
    assert result.reason == "mtimes_moved"


def test_after_turn_noop_when_nothing_changed(project: Path):
    """End-of-turn hook must not fire a useless refresh when the agent's
    turn made no source changes (e.g. a turn that only read files)."""
    _run_before_turn(project)
    result = _run_after_turn(project)
    assert result.refreshed is False
    assert result.reason == "unchanged"


# ---------------------------------------------------------------------------
# CLI surface.
# ---------------------------------------------------------------------------


def test_cli_refresh_default_runs_after_turn(project: Path, monkeypatch: pytest.MonkeyPatch):
    """No-flag invocation triggers the after-turn path. Default exists so a
    hook config can just say `trie refresh` without remembering the flag."""
    from typer.testing import CliRunner

    from trie.cli import app

    # Stub make_client so we don't construct a real AnthropicClient (which would
    # fail in the test sandbox without ANTHROPIC_API_KEY).
    monkeypatch.setattr(
        "trie.cli.make_client",
        lambda *_a, **_kw: FakeTrieClient(output_body="## `body`\n\nDeterministic."),
    )
    monkeypatch.chdir(project)

    runner = CliRunner()
    result = runner.invoke(app, ["refresh"])
    assert result.exit_code == 0, result.output


def test_cli_refresh_before_and_after_mutex(project: Path, monkeypatch: pytest.MonkeyPatch):
    from typer.testing import CliRunner

    from trie.cli import app

    monkeypatch.chdir(project)
    runner = CliRunner()
    result = runner.invoke(app, ["refresh", "--before-turn", "--after-turn"])
    assert result.exit_code == 1
    assert "mutually exclusive" in result.output


def test_cli_refresh_outside_git_fails(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    """The hard-error contract surfaces through the CLI as a non-zero exit."""
    from typer.testing import CliRunner

    from trie.cli import app

    (tmp_path / "trie.toml").write_text(
        '[trie]\nversion = "0.1.2"\n'
        '[scope]\ninclude = ["**/*.py"]\nexclude = []\n'
        '[triefacts]\nroot = "triefacts"\nsource_root = "."\n'
        '[models]\nbootstrap = "anthropic/claude-sonnet-4-6"\n'
        'cascade = "anthropic/claude-sonnet-4-6"\n'
        "[cascade]\ndefault_depth = 1\nhub_symbol_threshold = 20\n"
    )
    monkeypatch.setattr(
        "trie.cli.make_client",
        lambda *_a, **_kw: FakeTrieClient(output_body="## `body`\n\nDeterministic."),
    )
    monkeypatch.chdir(tmp_path)

    runner = CliRunner()
    result = runner.invoke(app, ["refresh"])
    assert result.exit_code == 1
    assert "git repository" in result.output
