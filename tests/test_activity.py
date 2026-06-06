"""Tests for the SQLite-backed local activity state (trie/activity.py)."""

from __future__ import annotations

import sqlite3
from pathlib import Path

from trie.activity import (
    ActivityWriter,
    clear_pending,
    db_path,
    read_pending,
    read_status,
    write_pending,
)

# --- pending --------------------------------------------------------------


def test_pending_round_trip(tmp_path: Path):
    write_pending(tmp_path, stale=["b.py", "a.py", "a.py"], head="sha1")
    p = read_pending(tmp_path)
    assert p is not None
    assert p.stale == ("a.py", "b.py")  # sorted + deduped
    assert p.head == "sha1"
    assert p.count == 2


def test_pending_never_computed_returns_none(tmp_path: Path):
    assert read_pending(tmp_path) is None


def test_pending_computed_empty_is_not_none(tmp_path: Path):
    write_pending(tmp_path, stale=[], head="sha1")
    p = read_pending(tmp_path)
    assert p is not None
    assert p.stale == ()
    assert p.count == 0


def test_clear_pending_subtracts_synced(tmp_path: Path):
    write_pending(tmp_path, stale=["a.py", "b.py", "c.py"], head="sha1")
    clear_pending(tmp_path, synced=["b.py"], head="sha2")
    p = read_pending(tmp_path)
    assert p is not None
    assert p.stale == ("a.py", "c.py")
    assert p.head == "sha2"


# --- status ---------------------------------------------------------------


def test_status_idle_by_default(tmp_path: Path):
    assert read_status(tmp_path).state == "idle"


def test_activity_writer_lifecycle(tmp_path: Path):
    import os

    with ActivityWriter(tmp_path, "sync") as w:
        w.set_total(2)
        w.file_start("a.py", 1, 2)
        s = read_status(tmp_path)
        assert s.state == "syncing"
        assert s.op == "sync"
        assert s.current_file == "a.py"
        assert s.total == 2
        assert s.pid == os.getpid()
        w.file_done("a.py", symbols=3)
        assert read_status(tmp_path).done == 1
    # Reset to idle on clean exit.
    assert read_status(tmp_path).state == "idle"


def test_activity_writer_records_error_on_exception(tmp_path: Path):
    try:
        with ActivityWriter(tmp_path, "sync"):
            raise RuntimeError("boom")
    except RuntimeError:
        pass
    s = read_status(tmp_path)
    assert s.state == "error"
    assert s.error and "boom" in s.error


def test_stale_status_from_dead_pid_reads_idle(tmp_path: Path):
    """A 'running' row whose pid is no longer alive must read as idle — crash
    recovery without a daemon."""
    # Write a running row directly with a bogus pid.
    path = db_path(tmp_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with ActivityWriter(tmp_path, "sync"):
        pass  # creates schema + idle row
    conn = sqlite3.connect(str(path))
    conn.execute("UPDATE status SET state='syncing', pid=? WHERE id=1", (0x7FFFFFFF,))
    conn.commit()
    conn.close()
    assert read_status(tmp_path).state == "idle"


# --- ActivityProgress bridge ---------------------------------------------


def test_activity_progress_mirrors_to_writer_and_inner(tmp_path: Path):
    from trie.activity import ActivityProgress

    calls: list[str] = []

    class Inner:
        def on_start(self, rel_path, idx, total):
            calls.append(f"start:{rel_path}")

        def on_done(self, rel_path, result, running_cost_usd):
            calls.append(f"done:{rel_path}")

        def on_skip(self, rel_path, reason):
            calls.append(f"skip:{rel_path}")

    class Result:
        symbols_generated = 2

    with ActivityWriter(tmp_path, "sync") as w:
        prog = ActivityProgress(w, inner=Inner())
        prog.on_start("a.py", 1, 1)
        s = read_status(tmp_path)
        assert s.current_file == "a.py"
        prog.on_done("a.py", Result(), 0.01)

    assert calls == ["start:a.py", "done:a.py"]
