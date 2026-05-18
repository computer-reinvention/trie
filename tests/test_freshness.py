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
from dataclasses import dataclass
from pathlib import Path

import pytest

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
from trie.models import GenerationRequest, GenerationResponse

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


@dataclass
class FakeClient:
    """LLM stand-in: deterministic, counts calls, full_model_id present so
    telemetry plumbing in sync_single_file doesn't blow up."""

    model_id: str = "fake/test"
    full_model_id: str = "fake/test"
    calls: int = 0

    def generate(self, _req: GenerationRequest) -> GenerationResponse:
        self.calls += 1
        return GenerationResponse(
            text="## `body`\n\nDeterministic.",
            input_tokens=10,
            output_tokens=20,
            cache_creation_input_tokens=0,
            cache_read_input_tokens=0,
        )

    def count_tokens(self, _req: GenerationRequest) -> int:
        return 100


@pytest.fixture
def project(tmp_path: Path) -> Path:
    """Two-module project under a real git repo with one initial commit."""
    (tmp_path / "trie.toml").write_text(
        '[trie]\nversion = "0.1.1"\n'
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
        '[trie]\nversion = "0.1.1"\n'
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
            client=FakeClient(),
        )


# ---------------------------------------------------------------------------
# The four states: unchanged, no_stamp, head_moved, mtimes_moved.
# ---------------------------------------------------------------------------


def _run_before_turn(project: Path, client: FakeClient | None = None):
    """Run the pre-turn gate, returning the FreshnessResult.

    A caller that needs to inspect LLM call counts after the run can pass its
    own FakeClient instance and read `.calls` on it. The default behaviour
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
            client=client or FakeClient(),
        )


def _run_after_turn(project: Path, client: FakeClient | None = None):
    config, _ = Config.find_and_load(project)
    db = project / ".trie" / "graph.db"
    db.parent.mkdir(parents=True, exist_ok=True)
    with Store(db) as store:
        return ensure_fresh_after_turn(
            project_root=project,
            config=config,
            store=store,
            client=client or FakeClient(),
        )


def test_no_stamp_triggers_scan_without_llm(project: Path):
    """First run in a fresh checkout: no stamp exists, graph scan fires but
    the LLM is NOT called. Trie does not auto-spend dollars on first contact;
    the user opts into prose regen by running `trie sync` explicitly."""
    client = FakeClient()
    result = _run_before_turn(project, client=client)
    assert result.refreshed is True
    assert result.reason == "no_stamp"
    assert result.incremental is None, "no_stamp must not invoke run_incremental"
    assert client.calls == 0, "no_stamp must not invoke the LLM"
    # The stamp now exists and records current HEAD.
    stamp = read_stamp(project)
    assert stamp is not None
    assert stamp.head == result.head


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

    client = FakeClient()
    result = _run_before_turn(project, client=client)
    assert result.refreshed is True
    assert result.reason == "head_moved"
    assert result.incremental is None, "head_moved must not invoke run_incremental"
    assert client.calls == 0, "head_moved must not invoke the LLM"
    after_head = read_stamp(project).head
    assert after_head != before_head


def test_mtimes_moved_triggers_sync_with_llm(project: Path):
    """Edit a file without committing: HEAD unchanged, but mtime moved. This
    is the only path that fires the LLM — local edits drift prose from source,
    so we resync with the diff-aware rubric handling cost-vs-correctness."""
    _run_before_turn(project)
    before_head = read_stamp(project).head

    time.sleep(0.01)
    alpha = project / "src" / "alpha.py"
    alpha.write_text(alpha.read_text() + "\n# tweak\n")

    client = FakeClient()
    result = _run_before_turn(project, client=client)
    assert result.refreshed is True
    assert result.reason == "mtimes_moved"
    assert result.incremental is not None, "mtimes_moved must invoke run_incremental"
    # The tweak above is a comment-only change to a file that already has a
    # triefact, so diff-aware regen *might* keep prose unchanged. The contract
    # we pin here is "the LLM path was available," not "every comment edit
    # fires N calls." The presence of an IncrementalResult is the load-bearing
    # signal that run_incremental ran rather than scan-only.
    # HEAD didn't move; the stamp's head field is unchanged.
    assert read_stamp(project).head == before_head


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
    monkeypatch.setattr("trie.cli.make_client", lambda *_a, **_kw: FakeClient())
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
        '[trie]\nversion = "0.1.1"\n'
        '[scope]\ninclude = ["**/*.py"]\nexclude = []\n'
        '[triefacts]\nroot = "triefacts"\nsource_root = "."\n'
        '[models]\nbootstrap = "anthropic/claude-sonnet-4-6"\n'
        'cascade = "anthropic/claude-sonnet-4-6"\n'
        "[cascade]\ndefault_depth = 1\nhub_symbol_threshold = 20\n"
    )
    monkeypatch.setattr("trie.cli.make_client", lambda *_a, **_kw: FakeClient())
    monkeypatch.chdir(tmp_path)

    runner = CliRunner()
    result = runner.invoke(app, ["refresh"])
    assert result.exit_code == 1
    assert "git repository" in result.output
