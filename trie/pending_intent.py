"""Pending intent: the between-apply-and-commit half of the intent ledger.

trie's rule for state: **if it matters, it lives in the triefact tree; if it
doesn't, it shouldn't exist.** The durable intent record is the digest archive
(`triefacts/triediffs/*.md`, committed with every change). The only intent
that isn't in a digest yet is what has been recorded this session but not yet
committed — and that lives here: a human-readable markdown file *inside the
digest archive directory*, consumed into the commit's digest entry by
`trie gate` / `trie diff --write` and deleted in the same step.

Lifecycle:

    patch apply  ──appends──►  triefacts/triediffs/.pending.md
    trie gate    ──consumes──► the commit's digest entry (then deletes it)

Properties this buys over the old `.trie/session_log.jsonl`:

- No shadow state: the pending file travels with the working tree, shows up
  in `git status`, and is readable by a human without tooling.
- No timestamp windows: digest evidence is "whatever is pending", consumed
  atomically — the cursor file and its boundary-leak bug class are gone.
- Normally never committed (the pre-commit digest write consumes it first);
  a `--no-verify` commit may land it, which is visible and harmless.

The file is dot-prefixed so `glob("*.md")` consumers of the archive (digest
history, retention pruning, the PR comment workflow) never see it.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from trie.config import Config

PENDING_BASENAME = ".pending.md"

_HEADER = """\
<!-- trie pending intent — recorded by `patch apply`, consumed into the next
     commit's digest by `trie gate` / `trie diff --write`; do not edit -->
"""

# One bullet per recorded note: `- <op> <qname> — <flattened note>`
_ROW_RE = re.compile(r"^- (?P<op>modify|create|delete|rename) (?P<qname>\S+)(?: — (?P<note>.*))?$")
_SESSION_RE = re.compile(r"^## (?P<note>.*)$")
_NO_SESSION = "(no session note)"


def pending_path(project_root: Path, config: Config) -> Path:
    return project_root / config.diff.diffs_dir / PENDING_BASENAME


def _flatten(text: str) -> str:
    """One physical line, whitespace-collapsed — same gate as digest bullets."""
    return " ".join((text or "").split())


def append_intent(
    project_root: Path,
    config: Config,
    rows: list[dict[str, Any]],
    *,
    session_note: str = "",
) -> Path:
    """Append recorded intent rows under a session heading.

    Each row: {qname, op, notes: [str], reasons: [str]}. Notes and reasons are
    flattened to single lines (the digest and history surfaces flatten them
    identically, so nothing readable is lost).
    """
    path = pending_path(project_root, config)
    path.parent.mkdir(parents=True, exist_ok=True)

    lines: list[str] = []
    if not path.exists():
        lines.append(_HEADER)
    lines.append("")
    lines.append(f"## {_flatten(session_note) or _NO_SESSION}")
    lines.append("")
    for row in rows:
        op = row.get("op", "modify")
        qname = row.get("qname", "")
        note_parts = [n for n in (row.get("notes") or []) if n]
        reasons = [r for r in (row.get("reasons") or []) if r]
        text = _flatten("; ".join(note_parts))
        if reasons:
            text = (
                f"{text} (reason: {_flatten('; '.join(reasons))})"
                if text
                else _flatten("; ".join(reasons))
            )
        lines.append(f"- {op} {qname} — {text}" if text else f"- {op} {qname}")

    with path.open("a", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    return path


def read_intent(project_root: Path, config: Config) -> list[dict[str, Any]]:
    """Parse pending rows back into digest-evidence shape.

    Returns [{qname, op, notes: [str], reasons: [], session_note}] — the same
    dict shape `collect_session_diff` serves as `applied` evidence, so the
    prompt/render layers don't care where intent came from.
    """
    path = pending_path(project_root, config)
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    session_note = ""
    try:
        text = path.read_text()
    except OSError:
        return []
    for line in text.splitlines():
        m = _SESSION_RE.match(line)
        if m:
            note = m.group("note").strip()
            session_note = "" if note == _NO_SESSION else note
            continue
        m = _ROW_RE.match(line)
        if m:
            rows.append(
                {
                    "qname": m.group("qname"),
                    "op": m.group("op"),
                    "notes": [m.group("note")] if m.group("note") else [],
                    "reasons": [],
                    "session_note": session_note,
                }
            )
    return rows


def consume_intent(project_root: Path, config: Config) -> None:
    """Delete the pending file (its contents just became a committed digest)."""
    pending_path(project_root, config).unlink(missing_ok=True)
