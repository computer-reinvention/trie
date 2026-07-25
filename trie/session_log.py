from __future__ import annotations

import json
import time
from pathlib import Path


def log_path(project_root: Path) -> Path:
    """Path of the session log JSONL file under `.trie/`."""
    return project_root / ".trie" / "session_log.jsonl"


def record_applied(project_root: Path, entries: list) -> None:
    """Best-effort append of applied-patch records to the session log.

    Swallows all I/O errors so it can never break a commit; archiving is
    purely informational and must not interfere with the edit pipeline's
    commit path.
    """
    if not entries:
        return
    try:
        path = log_path(project_root)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as fh:
            for entry in entries:
                row = dict(entry)
                if not row.get("ts"):
                    row["ts"] = time.time()
                fh.write(json.dumps(row, default=str) + "\n")
    except OSError:
        pass


def read_entries(
    project_root: Path,
    *,
    session_id: str | None = None,
    since: float | None = None,
) -> list:
    """Return applied-patch records from the session log, optionally filtered by session id and minimum timestamp."""
    path = log_path(project_root)
    collected: list = []
    try:
        if not path.exists():
            return []
        with path.open("r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    entry = json.loads(line)
                except Exception:
                    continue
                if not isinstance(entry, dict):
                    continue
                if session_id is not None and entry.get("session_id") != session_id:
                    continue
                if since is not None:
                    try:
                        ts = float(entry.get("ts", 0) or 0)
                    except (ValueError, TypeError):
                        ts = 0.0
                    # Exclusive boundary: the digest cursor's `covered` equals the
                    # max ts it consumed, so the next window must start strictly
                    # after it — `<=` here, or the previous window's last row
                    # leaks into every subsequent digest.
                    if ts <= since:
                        continue
                collected.append(entry)
    except OSError:
        return collected
    return collected


def read_digest_cursor(project_root: Path) -> dict | None:
    cursor_path = project_root / ".trie" / "digest_cursor.json"
    try:
        with open(cursor_path, encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, dict):
            return None
        if not all(k in data for k in ("parent", "since", "covered")):
            return None
        return data
    except (OSError, json.JSONDecodeError, ValueError):
        return None


def save_digest_cursor(
    project_root: Path,
    *,
    parent: str,
    since: float,
    covered: float,
    file: str = "",
) -> None:
    """Persist the digest window cursor to .trie/digest_cursor.json.

    `file` records the project-relative path of the digest file written for
    `parent`, so an amend/retry of the same commit rewrites that file instead
    of spawning a duplicate.
    """
    try:
        cursor_path = project_root / ".trie" / "digest_cursor.json"
        cursor_path.parent.mkdir(parents=True, exist_ok=True)
        payload = json.dumps(
            {"parent": parent, "since": since, "covered": covered, "file": file},
            indent=2,
        )
        tmp_path = cursor_path.with_suffix(".json.tmp")
        tmp_path.write_text(payload, encoding="utf-8")
        tmp_path.replace(cursor_path)
    except OSError:
        pass


def resolve_digest_window(
    project_root: Path,
    parent_sha: str,
    *,
    fallback_since: float | None,
) -> float | None:
    """Decide where the applied-notes window starts for a digest write."""
    cursor = read_digest_cursor(project_root)
    if cursor is None:
        return fallback_since
    if cursor.get("parent") == parent_sha:
        # Amend or retry of the same commit — re-cover the identical window.
        return cursor.get("since")
    # Normal next commit — start exactly after what the previous entry consumed.
    return cursor.get("covered")
