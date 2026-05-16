"""Tests for the refresh lock + queue.

The lock exists to serialise concurrent `trie refresh` calls and to
coalesce a fan-in of rapid turn-end hooks down to a bounded number of
actual refreshes. The tests below pin:

  - The single-holder happy path: acquire, no queue flag observed.
  - Contention: a second `try_acquire` while the first is held sees
    `acquired=False`, and `mark_queued()` leaves a sentinel for the
    holder to find.
  - Tail pass: a holder that calls `consume_queued()` after a contested
    period sees `True` exactly once and the sentinel is cleared.
  - Crash safety: when a process dies inside the lock, the OS releases
    the flock and the next caller acquires cleanly.

We use real subprocesses for the contention/crash tests because the
flock is per-fd and per-process — same-process re-acquire of an
exclusive lock is allowed on Linux/macOS, so a single-process test
would silently pass for the wrong reason.
"""

from __future__ import annotations

import multiprocessing as mp
import os
import sys
import time
from pathlib import Path

import pytest

from trie.refresh_lock import (
    LOCK_FILENAME,
    QUEUED_FILENAME,
    lock_path,
    queued_path,
    try_acquire,
)


def _project(tmp_path: Path) -> Path:
    """Bare minimum: just the `.trie/` directory exists for the lock to land in."""
    (tmp_path / ".trie").mkdir()
    return tmp_path


# ---------------------------------------------------------------------------
# Paths and basic acquire.
# ---------------------------------------------------------------------------


def test_lock_path_is_under_trie_dir(tmp_path: Path):
    assert lock_path(tmp_path) == tmp_path / ".trie" / LOCK_FILENAME
    assert queued_path(tmp_path) == tmp_path / ".trie" / QUEUED_FILENAME


def test_acquire_succeeds_when_uncontested(tmp_path: Path):
    project = _project(tmp_path)
    with try_acquire(project) as holder:
        assert holder.acquired is True
        # No queued sentinel exists yet, so consume must report False.
        assert holder.consume_queued() is False


def test_acquire_creates_lock_file_on_first_run(tmp_path: Path):
    """The first acquire materialises the anchor file; it's left in place
    afterwards so subsequent flocks operate on a stable inode."""
    project = _project(tmp_path)
    assert not lock_path(project).exists()
    with try_acquire(project) as holder:
        assert holder.acquired is True
        assert lock_path(project).exists()
    # Lock file persists after release; only the OS-level flock state goes away.
    assert lock_path(project).exists()


def test_acquire_creates_trie_dir_if_missing(tmp_path: Path):
    """`.trie/` may not exist yet on a fresh checkout that hasn't been
    initialised. The lock must not require an external mkdir."""
    project = tmp_path  # no `.trie/` pre-created
    with try_acquire(project) as holder:
        assert holder.acquired is True
    assert (project / ".trie").is_dir()


# ---------------------------------------------------------------------------
# Contention: a second acquire while the first is held must fail fast.
# ---------------------------------------------------------------------------


def _hold_lock_subprocess(project_root_str: str, ready_path_str: str, release_path_str: str):
    """Helper run in a child process: acquire the lock, write a sentinel so
    the parent knows we hold it, and wait for the parent to authorise release.

    Using a multiprocessing entrypoint rather than a thread because flock is
    per-process — threads in the same process share locks, so we'd see a
    spurious "acquired" in the parent."""
    from pathlib import Path as _Path

    from trie.refresh_lock import try_acquire as _try_acquire

    ready = _Path(ready_path_str)
    release = _Path(release_path_str)

    with _try_acquire(_Path(project_root_str)) as holder:
        ready.write_text("acquired" if holder.acquired else "missed")
        if not holder.acquired:
            return
        # Park until the parent says it's done probing. Polling with a tiny
        # sleep keeps the test fast without busy-looping.
        for _ in range(500):  # 5s ceiling
            if release.exists():
                return
            time.sleep(0.01)


def test_contention_yields_unacquired_holder(tmp_path: Path):
    """The contract: when another process holds the flock, our `try_acquire`
    returns a holder with `acquired=False` rather than blocking."""
    project = _project(tmp_path)
    ready = tmp_path / "ready"
    release = tmp_path / "release"

    ctx = mp.get_context("spawn")
    proc = ctx.Process(
        target=_hold_lock_subprocess,
        args=(str(project), str(ready), str(release)),
    )
    proc.start()
    try:
        # Wait for the child to confirm it holds the lock. Conservative ceiling.
        for _ in range(500):
            if ready.exists() and ready.read_text() == "acquired":
                break
            time.sleep(0.01)
        else:
            pytest.fail("child process never acquired the lock")

        with try_acquire(project) as holder:
            assert holder.acquired is False, "second acquirer must observe contention"
            holder.mark_queued()
            assert queued_path(project).exists()
            # The contested side's consume_queued must be a no-op.
            assert holder.consume_queued() is False
    finally:
        release.write_text("done")
        proc.join(timeout=5)
        if proc.is_alive():
            proc.terminate()
            proc.join()


# ---------------------------------------------------------------------------
# Queue + tail pass: holder picks up the queued flag and clears it.
# ---------------------------------------------------------------------------


def test_consume_queued_clears_sentinel_on_holder(tmp_path: Path):
    """An external `mark_queued` writes the sentinel; the holder's
    `consume_queued()` returns True exactly once and removes the file."""
    project = _project(tmp_path)
    with try_acquire(project) as holder:
        assert holder.acquired is True
        # Simulate a contested caller having dropped the sentinel.
        queued_path(project).write_text("")
        assert holder.consume_queued() is True
        assert not queued_path(project).exists()
        # Second consume returns False — the holder has already drained it.
        assert holder.consume_queued() is False


def test_mark_queued_is_idempotent(tmp_path: Path):
    """Two consecutive `mark_queued()` calls leave one sentinel, not two."""
    project = _project(tmp_path)
    # We need an *unacquired* holder to call mark_queued; simulate that by
    # holding the lock in a child process.
    ready = tmp_path / "ready"
    release = tmp_path / "release"

    ctx = mp.get_context("spawn")
    proc = ctx.Process(
        target=_hold_lock_subprocess,
        args=(str(project), str(ready), str(release)),
    )
    proc.start()
    try:
        for _ in range(500):
            if ready.exists() and ready.read_text() == "acquired":
                break
            time.sleep(0.01)
        else:
            pytest.fail("child never acquired the lock")

        with try_acquire(project) as holder:
            assert holder.acquired is False
            holder.mark_queued()
            holder.mark_queued()  # second call is a no-op semantically
            assert queued_path(project).exists()
    finally:
        release.write_text("done")
        proc.join(timeout=5)
        if proc.is_alive():
            proc.terminate()
            proc.join()


# ---------------------------------------------------------------------------
# Crash safety: OS releases the flock when a process dies.
# ---------------------------------------------------------------------------


def _hold_and_crash(project_root_str: str, ready_path_str: str):
    """Acquire the lock, signal readiness, then die without releasing.

    `os._exit` skips cleanup hooks; the OS still reclaims the fd and the
    flock comes off. This models a SIGKILL'd refresh process."""
    from pathlib import Path as _Path

    from trie.refresh_lock import try_acquire as _try_acquire

    ready = _Path(ready_path_str)
    with _try_acquire(_Path(project_root_str)) as holder:
        ready.write_text("acquired" if holder.acquired else "missed")
        # Skip context-manager cleanup deliberately.
        os._exit(0 if holder.acquired else 1)


def test_lock_released_when_holder_crashes(tmp_path: Path):
    """A holder that exits without going through the context manager must
    still leave the lock acquirable for the next process."""
    project = _project(tmp_path)
    ready = tmp_path / "ready"

    ctx = mp.get_context("spawn")
    proc = ctx.Process(target=_hold_and_crash, args=(str(project), str(ready)))
    proc.start()
    proc.join(timeout=5)
    assert proc.exitcode == 0, "child should have acquired the lock before dying"

    # Now the next caller in *this* process must acquire cleanly.
    with try_acquire(project) as holder:
        assert holder.acquired is True


# ---------------------------------------------------------------------------
# CLI integration: a contested `trie refresh` exits 0 with a queued message.
# ---------------------------------------------------------------------------


def test_cli_refresh_when_contended_queues_and_exits_zero(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    """Drive the actual `trie refresh` CLI under contention. The other holder
    is a child process; the parent invocation must see the queue branch."""
    import subprocess

    from typer.testing import CliRunner

    # Minimal trie.toml + a real git repo so the freshness gate inside
    # the CLI doesn't reject the project for the wrong reason. We rig
    # the child to hold the lock; the parent should never actually reach
    # the freshness gate.
    (tmp_path / "trie.toml").write_text(
        '[trie]\nversion = "0.1.0"\n'
        '[scope]\ninclude = ["src/**/*.py"]\nexclude = []\n'
        '[triefacts]\nroot = "triefacts"\nsource_root = "."\n'
        '[models]\nbootstrap = "anthropic/claude-sonnet-4-6"\n'
        'cascade = "anthropic/claude-sonnet-4-6"\n'
        "[cascade]\ndefault_depth = 1\nhub_symbol_threshold = 20\n"
    )
    src = tmp_path / "src"
    src.mkdir()
    (src / "alpha.py").write_text("def f():\n    return 0\n")

    subprocess.run(["git", "init", "-q", "-b", "main"], cwd=tmp_path, check=True)
    subprocess.run(
        ["git", "config", "user.email", "trie-test@example.com"],
        cwd=tmp_path,
        check=True,
    )
    subprocess.run(["git", "config", "user.name", "trie test"], cwd=tmp_path, check=True)
    subprocess.run(["git", "add", "."], cwd=tmp_path, check=True)
    subprocess.run(["git", "commit", "-q", "-m", "init"], cwd=tmp_path, check=True)

    ready = tmp_path / "ready"
    release = tmp_path / "release"

    ctx = mp.get_context("spawn")
    proc = ctx.Process(
        target=_hold_lock_subprocess,
        args=(str(tmp_path), str(ready), str(release)),
    )
    proc.start()
    try:
        for _ in range(500):
            if ready.exists() and ready.read_text() == "acquired":
                break
            time.sleep(0.01)
        else:
            pytest.fail("child never acquired the lock")

        from trie.cli import app

        # Stub make_client so we don't construct a real AnthropicClient — the
        # parent should bail before using it, but defensive monkeypatching
        # keeps the test from blowing up if that contract regresses.
        class _FakeClient:
            model_id = "fake/test"
            full_model_id = "fake/test"

        monkeypatch.setattr("trie.cli.make_client", lambda *_a, **_kw: _FakeClient())
        monkeypatch.chdir(tmp_path)

        runner = CliRunner()
        result = runner.invoke(app, ["refresh"])
        assert result.exit_code == 0, result.output
        assert "queued" in result.output.lower()

        # The queued sentinel must now exist for the holder to pick up.
        assert queued_path(tmp_path).exists()
    finally:
        release.write_text("done")
        proc.join(timeout=5)
        if proc.is_alive():
            proc.terminate()
            proc.join()


# ---------------------------------------------------------------------------
# CLI integration: operator commands (sync, plan, init) fail loudly under
# contention rather than queueing. The hook can afford to queue silently;
# the operator typed a command and is watching for output, so we owe them
# a non-zero exit and an explanatory message.
# ---------------------------------------------------------------------------


def _make_minimal_trie_project(tmp_path: Path) -> None:
    """Set up trie.toml + a tiny source tree + a git repo with one commit."""
    import subprocess

    (tmp_path / "trie.toml").write_text(
        '[trie]\nversion = "0.1.0"\n'
        '[scope]\ninclude = ["src/**/*.py"]\nexclude = []\n'
        '[triefacts]\nroot = "triefacts"\nsource_root = "."\n'
        '[models]\nbootstrap = "anthropic/claude-sonnet-4-6"\n'
        'cascade = "anthropic/claude-sonnet-4-6"\n'
        "[cascade]\ndefault_depth = 1\nhub_symbol_threshold = 20\n"
    )
    src = tmp_path / "src"
    src.mkdir()
    (src / "alpha.py").write_text("def f():\n    return 0\n")

    subprocess.run(["git", "init", "-q", "-b", "main"], cwd=tmp_path, check=True)
    subprocess.run(
        ["git", "config", "user.email", "trie-test@example.com"],
        cwd=tmp_path,
        check=True,
    )
    subprocess.run(["git", "config", "user.name", "trie test"], cwd=tmp_path, check=True)
    subprocess.run(["git", "add", "."], cwd=tmp_path, check=True)
    subprocess.run(["git", "commit", "-q", "-m", "init"], cwd=tmp_path, check=True)


def test_cli_sync_when_contended_exits_two_with_explanation(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    """`trie sync` is operator-driven; when another trie process holds the
    lock, sync must NOT queue silently. It exits 2 (transient contention,
    distinct from exit 1 "your config is broken") and prints a message
    naming the conflict so the user can retry."""
    from typer.testing import CliRunner

    _make_minimal_trie_project(tmp_path)

    ready = tmp_path / "ready"
    release = tmp_path / "release"

    ctx = mp.get_context("spawn")
    proc = ctx.Process(
        target=_hold_lock_subprocess,
        args=(str(tmp_path), str(ready), str(release)),
    )
    proc.start()
    try:
        for _ in range(500):
            if ready.exists() and ready.read_text() == "acquired":
                break
            time.sleep(0.01)
        else:
            pytest.fail("child never acquired the lock")

        from trie.cli import app

        # Sync never reaches the LLM under contention, but defensive stubbing
        # keeps the test honest if the lock guard regresses.
        class _FakeClient:
            model_id = "fake/test"
            full_model_id = "fake/test"

        monkeypatch.setattr("trie.cli.make_client", lambda *_a, **_kw: _FakeClient())
        monkeypatch.chdir(tmp_path)

        runner = CliRunner()
        result = runner.invoke(app, ["sync"])
        assert result.exit_code == 2, result.output
        assert "another trie process" in result.output.lower()

        # No queued sentinel: sync's failure mode is "tell the operator,"
        # not "queue a tail pass." That would silently change what `sync`
        # does on the operator's behalf, which is the opposite of what
        # they typed.
        assert not queued_path(tmp_path).exists()
    finally:
        release.write_text("done")
        proc.join(timeout=5)
        if proc.is_alive():
            proc.terminate()
            proc.join()


def test_cli_lock_check_when_free_exits_zero(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    """`trie lock-check` is the pre-commit gate: when nothing else holds the
    lock, the command must report free and exit 0 so the commit proceeds."""
    from typer.testing import CliRunner

    _make_minimal_trie_project(tmp_path)
    monkeypatch.chdir(tmp_path)

    from trie.cli import app

    runner = CliRunner()
    result = runner.invoke(app, ["lock-check"])
    assert result.exit_code == 0, result.output
    assert "free" in result.output.lower()


def test_cli_lock_check_when_no_trie_toml_exits_zero(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    """A pre-commit hook installed by `trie init` may run in repos that
    don't have trie configured (e.g. a sub-repo, or after the user removed
    trie.toml). The lock-check must degrade to a no-op rather than confuse
    the user with a config error — there's no trie state to race."""
    from typer.testing import CliRunner

    monkeypatch.chdir(tmp_path)  # bare tmp_path; no trie.toml anywhere

    from trie.cli import app

    runner = CliRunner()
    result = runner.invoke(app, ["lock-check"])
    assert result.exit_code == 0, result.output
    assert "no trie.toml" in result.output.lower()


def test_cli_lock_check_when_contended_exits_two(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    """The pre-commit gate's reason for existing: when a sync or refresh is
    in flight, the lock is held, and `lock-check` exits 2 with an explanation
    so the hook can refuse the commit."""
    from typer.testing import CliRunner

    _make_minimal_trie_project(tmp_path)

    ready = tmp_path / "ready"
    release = tmp_path / "release"

    ctx = mp.get_context("spawn")
    proc = ctx.Process(
        target=_hold_lock_subprocess,
        args=(str(tmp_path), str(ready), str(release)),
    )
    proc.start()
    try:
        for _ in range(500):
            if ready.exists() and ready.read_text() == "acquired":
                break
            time.sleep(0.01)
        else:
            pytest.fail("child never acquired the lock")

        from trie.cli import app

        monkeypatch.chdir(tmp_path)
        runner = CliRunner()
        result = runner.invoke(app, ["lock-check"])
        assert result.exit_code == 2, result.output
        assert "another trie process" in result.output.lower()
    finally:
        release.write_text("done")
        proc.join(timeout=5)
        if proc.is_alive():
            proc.terminate()
            proc.join()


def test_cli_plan_when_contended_exits_two(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    """`trie plan` writes to the store via `scan_project`; it's a writer
    even though its purpose is informational. Same exit-2 contract as sync."""
    from typer.testing import CliRunner

    _make_minimal_trie_project(tmp_path)

    ready = tmp_path / "ready"
    release = tmp_path / "release"

    ctx = mp.get_context("spawn")
    proc = ctx.Process(
        target=_hold_lock_subprocess,
        args=(str(tmp_path), str(ready), str(release)),
    )
    proc.start()
    try:
        for _ in range(500):
            if ready.exists() and ready.read_text() == "acquired":
                break
            time.sleep(0.01)
        else:
            pytest.fail("child never acquired the lock")

        from trie.cli import app

        class _FakeClient:
            model_id = "fake/test"
            full_model_id = "fake/test"

        monkeypatch.setattr("trie.cli.make_client", lambda *_a, **_kw: _FakeClient())
        monkeypatch.chdir(tmp_path)

        runner = CliRunner()
        result = runner.invoke(app, ["plan"])
        assert result.exit_code == 2, result.output
        assert "another trie process" in result.output.lower()
    finally:
        release.write_text("done")
        proc.join(timeout=5)
        if proc.is_alive():
            proc.terminate()
            proc.join()


# ---------------------------------------------------------------------------
# Sanity: skip on Windows. We document the POSIX-only restriction in
# refresh_lock.py; this skip is the runtime expression of that contract.
# ---------------------------------------------------------------------------


if sys.platform.startswith("win"):
    pytest.skip("refresh_lock is POSIX-only for v0.1", allow_module_level=True)
