from __future__ import annotations

import pathlib

from trie.session_log import read_digest_cursor, resolve_digest_window, save_digest_cursor


def test_digest_cursor_roundtrip_and_window(tmp_path: pathlib.Path) -> None:
    # (1) Fresh directory: no cursor file -> None
    assert read_digest_cursor(tmp_path) is None

    # (2) resolve_digest_window with no cursor falls back to the provided fallback
    assert resolve_digest_window(tmp_path, "aaa", fallback_since=55.0) == 55.0
    assert resolve_digest_window(tmp_path, "aaa", fallback_since=None) is None

    # (3) After saving a cursor entry
    save_digest_cursor(tmp_path, parent="aaa", since=10.0, covered=20.0, file="triediffs/x.md")

    # The digest file path rides along for same-commit rewrites
    cursor = read_digest_cursor(tmp_path)
    assert cursor is not None and cursor.get("file") == "triediffs/x.md"

    # Same parent: resume from where this commit started (since), not after covered
    assert resolve_digest_window(tmp_path, "aaa", fallback_since=99.0) == 10.0

    # Different parent: the next commit starts after what the previous entry covered
    assert resolve_digest_window(tmp_path, "bbb", fallback_since=99.0) == 20.0

    # (4) Corrupt JSON in the cursor file -> graceful degradation
    # Locate the cursor file written by save_digest_cursor
    cursor_files = list(tmp_path.glob("**/*.json"))
    assert cursor_files, "Expected at least one cursor JSON file"
    # Corrupt the first one found (there should be exactly one)
    cursor_file = cursor_files[0]
    cursor_file.write_text("{ not valid json !!!", encoding="utf-8")

    assert read_digest_cursor(tmp_path) is None
    assert resolve_digest_window(tmp_path, "aaa", fallback_since=77.0) == 77.0
    assert resolve_digest_window(tmp_path, "aaa", fallback_since=None) is None
