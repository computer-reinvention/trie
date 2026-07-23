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
                    if ts < since:
                        continue
                collected.append(entry)
    except OSError:
        return collected
    return collected
