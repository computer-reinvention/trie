from __future__ import annotations

import io

from rich.console import Console
from typer.testing import CliRunner

from trie.cli import app
from trie.reporter import ProgressHandle, Reporter, Verbosity


def _make_reporter(level: Verbosity) -> tuple[Reporter, io.StringIO]:
    buf = io.StringIO()
    console = Console(file=buf, width=120, force_terminal=False, no_color=True)
    return Reporter(verbosity=level, console=console), buf


def test_mute_suppresses_info_and_success():
    reporter, buf = _make_reporter(Verbosity.MUTE)
    reporter.info("hello")
    reporter.success("done")
    reporter.detail("noisy")
    assert buf.getvalue() == ""


def test_mute_still_emits_errors():
    reporter, buf = _make_reporter(Verbosity.MUTE)
    reporter.error("boom")
    assert "boom" in buf.getvalue()


def test_medium_emits_info_and_success_but_not_detail():
    reporter, buf = _make_reporter(Verbosity.MEDIUM)
    reporter.info("hello")
    reporter.success("done")
    reporter.detail("noisy")
    out = buf.getvalue()
    assert "hello" in out
    assert "done" in out
    assert "noisy" not in out


def test_verbose_emits_everything():
    reporter, buf = _make_reporter(Verbosity.VERBOSE)
    reporter.info("hello")
    reporter.detail("noisy")
    out = buf.getvalue()
    assert "hello" in out
    assert "noisy" in out


def test_progress_mute_is_noop():
    reporter, buf = _make_reporter(Verbosity.MUTE)
    with reporter.start_progress(total=3, label="syncing") as ph:
        assert isinstance(ph, ProgressHandle)
        ph.start_file("a.py")
        ph.finish_file("a.py", cost_usd=0.01)
        ph.skip_file("b.py", reason="no budget")
    assert buf.getvalue() == ""


def test_progress_medium_prints_finish_lines():
    reporter, buf = _make_reporter(Verbosity.MEDIUM)
    with reporter.start_progress(total=2, label="syncing") as ph:
        ph.start_file("a.py")
        ph.finish_file("a.py", cost_usd=0.01, symbols=3)
    out = buf.getvalue()
    assert "a.py" in out
    assert "$0.0100" in out
    assert "3 sym" in out


def test_progress_verbose_includes_token_detail():
    reporter, buf = _make_reporter(Verbosity.VERBOSE)
    with reporter.start_progress(total=1, label="syncing") as ph:
        ph.start_file("a.py")
        ph.finish_file("a.py", cost_usd=0.02, tokens_in=100, tokens_out=50)
    out = buf.getvalue()
    assert "tok 100/50" in out


def test_progress_marks_cascade_files():
    reporter, buf = _make_reporter(Verbosity.MEDIUM)
    with reporter.start_progress(total=2, label="syncing") as ph:
        ph.start_file("direct.py", cascade=False)
        ph.finish_file("direct.py", cost_usd=0.01)
        ph.start_file("pulled.py", cascade=True)
        ph.finish_file("pulled.py", cost_usd=0.01)
    out = buf.getvalue()
    # The cascade-pulled file is labelled; the directly-stale one is not.
    assert "pulled.py (cascade)" in out
    direct_line = next(line for line in out.splitlines() if "direct.py" in line)
    assert "(cascade)" not in direct_line


def test_progress_adapter_prints_plan_header_and_section_separators():
    from trie.cli import _ProgressAdapter

    reporter, buf = _make_reporter(Verbosity.MEDIUM)
    adapter = _ProgressAdapter(reporter, "syncing")
    # Plan header is emitted before any file starts.
    adapter.on_plan(direct=2, cascade=3)
    # Section separators before each group.
    adapter.on_section(label="directly stale", count=2)
    adapter.on_start("direct.py", 1, 5)
    adapter.on_section(label="pulled in by the cascade", count=3)
    adapter.on_start("pulled.py", 2, 5, cascade=True)
    adapter.close()

    out = buf.getvalue()
    assert "syncing 5 file(s)" in out
    assert "2 directly stale" in out
    assert "3 pulled in by the cascade" in out
    assert "── directly stale (2) ──" in out
    assert "── pulled in by the cascade (3) ──" in out


def test_progress_adapter_plan_is_silent_when_nothing_to_sync():
    from trie.cli import _ProgressAdapter

    reporter, buf = _make_reporter(Verbosity.MEDIUM)
    adapter = _ProgressAdapter(reporter, "syncing")
    adapter.on_plan(direct=0, cascade=0)
    adapter.on_section(label="directly stale", count=0)
    assert buf.getvalue() == ""


# --- root callback verbosity flag plumbing ---


def test_root_quiet_and_verbose_are_mutually_exclusive():
    runner = CliRunner()
    result = runner.invoke(app, ["--quiet", "--verbose"])
    assert result.exit_code == 2
    assert "mutually exclusive" in (result.stderr or result.output)


def test_root_version_still_works_with_verbosity_flags():
    runner = CliRunner()
    result = runner.invoke(app, ["-v", "--version"])
    assert result.exit_code == 0
    assert "trie" in result.output
