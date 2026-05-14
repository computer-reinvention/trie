"""Append-only JSONL telemetry for trie's own operations.

For our use during validation and development, not production observability.
Enabled either via the `[debug]` block in `trie.toml` or by setting the
`TRIE_DEBUG` env var. The env var always wins when set:

    TRIE_DEBUG=1                   → force-enabled, write to <project_root>/debug.jsonl
    TRIE_DEBUG=path/to/log.jsonl   → force-enabled, write there (path relative to CWD)
    TRIE_DEBUG=0                   → force-disabled
    (unset)                        → fall back to debug.enabled in trie.toml

Eight event types cover the validation surface:

- `cli`         — top-level command invocation (every `trie ...` call)
- `scan`        — `scan_project` duration + summary counts
- `parse_file`  — per file parse: symbols extracted, references extracted
- `cascade`     — `compute_cascade` invocation: seeds, hub-skips, output
- `verify`      — `trie verify` run: files checked, issues by reason
- `sync_file`   — per-file sync: tokens, cost, sections regen'd
- `mcp_call`    — per MCP tool call: tool, duration, response size
- `model_call`  — per LLM round-trip: model, tokens, latency

Use `emit(event, **fields)` for one-off facts and `timed(event, **fields)` as
a context manager when duration should be captured automatically. Every event
is a single buffered line write; we never block on disk and never raise into
user code. The file is opened lazily on the first emit and stays open for the
process lifetime — flushed on atexit.

Configuration is applied process-wide via `configure(cfg, project_root)`,
called from `cli.py` after `Config.find_and_load`. Until that point any emits
fall back to env-var-only resolution so MCP servers spawned by agents (which
don't go through cli.py) still get telemetry when TRIE_DEBUG is set.
"""

from __future__ import annotations

import atexit
import json
import os
import sys
import time
from collections.abc import Iterator
from contextlib import contextmanager
from datetime import UTC, datetime
from pathlib import Path
from typing import IO, Any

from trie.config import Debug

_DEFAULT_FILENAME = "debug.jsonl"

# Process-wide state. `configure()` mutates these; everything else reads them.
_cfg: Debug | None = None
_project_root: Path | None = None
_file: IO[str] | None = None
_resolved: bool = False  # have we resolved enable/path for this process yet?
_enabled: bool = False
_log_to_stderr: bool = False
_capture_args: bool = True
_capture_responses: bool = False
_redact_keys: tuple[str, ...] = ()


def configure(cfg: Debug, project_root: Path) -> None:
    """Apply [debug] settings from trie.toml. Called once after Config load.

    The env var TRIE_DEBUG still wins on enable/path; the other knobs
    (log_to_stderr, capture_args, capture_responses, redact_keys) come from
    cfg. Safe to call more than once — re-resolves and re-opens if path
    changed.
    """
    global _cfg, _project_root, _resolved
    _cfg = cfg
    _project_root = project_root
    _resolved = False  # force re-resolve on next emit


def _resolve() -> None:
    """Decide whether telemetry is on, and if so, where to write.

    Reads (in priority order): env var TRIE_DEBUG, then cfg.enabled. The first
    that says "yes" wins. Idempotent; subsequent calls are no-ops unless
    `configure()` reset _resolved.
    """
    global _resolved, _enabled, _log_to_stderr, _capture_args, _capture_responses, _redact_keys
    if _resolved:
        return
    _resolved = True

    # 1. Env var override
    raw = os.environ.get("TRIE_DEBUG")
    env_decision: bool | None = None
    env_path: Path | None = None
    if raw is not None and raw != "":
        lowered = raw.strip().lower()
        if lowered in ("0", "false", "no", "off"):
            env_decision = False
        elif lowered in ("1", "true", "yes", "on"):
            env_decision = True
        else:
            env_decision = True
            env_path = Path(raw).expanduser()

    # 2. Resolve enable state and path
    if env_decision is False:
        _enabled = False
        return
    if env_decision is True or (_cfg is not None and _cfg.enabled):
        _enabled = True
    else:
        _enabled = False
        return

    # 3. Decide path
    if env_path is not None:
        path = env_path.resolve()
    else:
        log_path = _cfg.log_path if _cfg is not None else _DEFAULT_FILENAME
        base = _project_root if _project_root is not None else Path.cwd()
        path = Path(log_path)
        if not path.is_absolute():
            path = (base / path).resolve()

    # 4. Other knobs from config (env doesn't override these)
    if _cfg is not None:
        _log_to_stderr = _cfg.log_to_stderr
        _capture_args = _cfg.capture_args
        _capture_responses = _cfg.capture_responses
        _redact_keys = tuple(_cfg.redact_keys)
    else:
        _log_to_stderr = False
        _capture_args = True
        _capture_responses = False
        _redact_keys = ()

    # 5. Open the file
    _open(path)


def _open(path: Path) -> None:
    """Open the log file for append. On failure, disable telemetry quietly."""
    global _file, _enabled
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        _file = path.open("a", buffering=1, encoding="utf-8")  # line-buffered
        atexit.register(_close)
    except OSError as e:
        print(f"trie: failed to open TRIE_DEBUG log at {path}: {e}", file=sys.stderr)
        _enabled = False


def _close() -> None:
    global _file
    if _file is not None:
        try:
            _file.flush()
            _file.close()
        except OSError:
            pass
        _file = None


def is_enabled() -> bool:
    """True iff telemetry is on for this process. Cheap to call repeatedly."""
    _resolve()
    return _enabled


def capture_args() -> bool:
    """True iff the agent surface should include MCP tool args in events."""
    _resolve()
    return _capture_args


def capture_responses() -> bool:
    """True iff full MCP response bodies should be captured (not just sizes)."""
    _resolve()
    return _capture_responses


def _apply_redactions(record: dict[str, Any]) -> dict[str, Any]:
    """Elide values at `_redact_keys` paths. Dotted paths reach into nested dicts."""
    if not _redact_keys:
        return record
    for key in _redact_keys:
        parts = key.split(".")
        cursor: Any = record
        for p in parts[:-1]:
            if not isinstance(cursor, dict) or p not in cursor:
                cursor = None
                break
            cursor = cursor[p]
        if isinstance(cursor, dict) and parts[-1] in cursor:
            cursor[parts[-1]] = "<redacted>"
    return record


def emit(event: str, **fields: Any) -> None:
    """Append one event to the telemetry log. Silent no-op when disabled.

    Two fields are stamped automatically: `ts` (ISO-8601 UTC) and `event`.
    Values are serialized with `default=str`, so any type json doesn't know
    natively (Path, datetime, dataclass) gets stringified rather than raising.
    """
    _resolve()
    if not _enabled or _file is None:
        return
    record: dict[str, Any] = {
        "ts": datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        "event": event,
    }
    record.update(fields)
    record = _apply_redactions(record)
    try:
        line = json.dumps(record, default=str)
        _file.write(line + "\n")
        if _log_to_stderr:
            print(line, file=sys.stderr)
    except (OSError, TypeError) as e:
        print(f"trie: telemetry emit failed: {e}", file=sys.stderr)


@contextmanager
def timed(event: str, **fields: Any) -> Iterator[dict[str, Any]]:
    """Context manager that emits `event` on exit with a `duration_ms` field.

    Yields a mutable dict the caller can update with values learned during the
    block (e.g. `ctx["symbols_generated"] = n`); those updates are merged into
    the emitted event. On exception the event additionally carries `error`
    (the exception class name) so failures are distinguishable from successes.

    Usage:

        with timed("scan", project_root=str(root)) as ctx:
            result = scan_project(...)
            ctx["files_seen"] = result.files_seen
    """
    payload: dict[str, Any] = dict(fields)
    start = time.perf_counter()
    error: str | None = None
    try:
        yield payload
    except BaseException as exc:
        error = type(exc).__name__
        raise
    finally:
        payload["duration_ms"] = int((time.perf_counter() - start) * 1000)
        if error is not None:
            payload["error"] = error
        emit(event, **payload)


def reset_for_tests() -> None:
    """Drop process-level state. For test use only."""
    global _cfg, _project_root, _file, _resolved, _enabled
    _close()
    _cfg = None
    _project_root = None
    _file = None
    _resolved = False
    _enabled = False
