"""The patch pipeline: an intent store, not a code generator.

Agents edit source natively and own code changes. The pipeline's job is the
record of *why*: notes are staged per touched symbol (`patch` and friends),
reviewed (`patch list` / `preview`), and committed by `record_intent` — which
archives them to the session log and clears the queue. trie generates no code.

That archive is load-bearing: it feeds the per-commit digest (`trie diff`),
the PR digest comments, `read --history`, and the coverage side of the
`trie intent` pre-commit gate (trie/intent_gate.py) that refuses commits when
a changed symbol carries no note.

The generating backends (in-process LLM codegen, the agent workorder flow)
were removed after repeatedly losing to agent-owned execution — the generation
calls were context-starved and invented APIs. `git log` has the machinery if a
future design wants to resurrect the experiment.
"""

from __future__ import annotations

import time
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from pathlib import Path

    from trie.config import Config
    from trie.graph.store import Store

# A multi-symbol apply requires a real unifying intent, not boilerplate.
_SESSION_NOTE_STOPLIST = {"update", "fix", "fixes", "changes", "change", "wip", ".", "edit"}
_SESSION_NOTE_MIN_CHARS = 12


def session_note_ok(note: str) -> bool:
    """Reject empty / too-short / single-stoplist-word session notes.

    The session note is the unifying intent that titles the commit's digest
    entry; junk like "." or "fix" would poison the archive downstream.
    """
    n = (note or "").strip()
    if len(n) < _SESSION_NOTE_MIN_CHARS:
        return False
    return n.lower() not in _SESSION_NOTE_STOPLIST


def _expand_callers(
    seed_qnames: list[str],
    store: Store,
    cascade_depth: int,
    hub_threshold: int,
) -> set[str]:
    """Breadth-first caller expansion used by `preview_patches` blast radius."""
    working: set[str] = set()
    frontier: list[str] = list(seed_qnames)
    visited: set[str] = set(seed_qnames)

    for _ in range(cascade_depth):
        next_frontier: list[str] = []
        for qn in frontier:
            row = store._conn.execute(
                "SELECT COUNT(*) FROM edges WHERE dst_symbol_id = ("
                "SELECT id FROM symbols WHERE qualified_name = ? LIMIT 1"
                ")",
                (qn,),
            ).fetchone()
            if row and int(row[0]) > hub_threshold:
                continue
            for caller in store.references_in(qn):
                if caller not in visited:
                    visited.add(caller)
                    working.add(caller)
                    next_frontier.append(caller)
        if not next_frontier:
            break
        frontier = next_frontier

    return working


def preview_patches(store: Store, config: Config) -> dict[str, Any]:
    """Pending notes + the call-graph blast radius of the symbols they touch.

    Read-only review surface for `trie patch preview` / the MCP `preview`
    tool: which symbols carry notes, and which callers a reviewer might want
    to look at. No writes, no LLM.
    """
    grouped = store.get_all_patches_grouped()
    patches_by_qname: dict[str, list[dict]] = {}
    for sym_id, patch_list in grouped.items():
        row = store._conn.execute(
            "SELECT qualified_name FROM symbols WHERE id = ?", (sym_id,)
        ).fetchone()
        if row is None:
            continue
        patches_by_qname[str(row[0])] = patch_list

    patched_qnames = list(patches_by_qname.keys())

    working = _expand_callers(
        patched_qnames,
        store,
        config.cascade.default_depth,
        config.cascade.hub_symbol_threshold,
    )
    cascaded = sorted(working - set(patched_qnames))

    return {
        "total_patches": sum(len(v) for v in patches_by_qname.values()),
        "patched_symbols": len(patched_qnames),
        "patched_list": sorted(patched_qnames),
        "cascade_symbols": len(cascaded),
        "cascade_list": cascaded,
    }


def record_intent(
    store: Store,
    config: Config,
    project_root: Path,
    *,
    session_note: str = "",
) -> dict:
    """Commit pending patch notes as intent — no code generation.

    Archives pending modify/delete/rename/create notes as applied session-log
    rows and clears the queue; the source tree is never touched. More than one
    symbol requires a real unifying `session_note` (see `session_note_ok`).
    """
    from trie.session_log import record_applied

    modify_qnames = store.get_patched_qnames()
    creates_by_file = store.get_create_patches_grouped()
    create_count = sum(len(rows) for rows in creates_by_file.values())
    total = len(modify_qnames) + create_count

    if total == 0:
        return {"ok": True, "mode": "record", "recorded": 0, "symbols": []}
    if total > 1 and not session_note_ok(session_note):
        return {
            "ok": False,
            "mode": "record",
            "error": "session_note_required",
            "message": (
                "A real session_note (the unifying intent) is required when "
                "recording more than one symbol."
            ),
        }

    now = time.time()
    rows: list[dict] = []
    for qname in modify_qnames:
        patches = store.get_patches_for_qname(qname)
        if not patches:
            continue
        # Structural kinds keep their op; plain notes are modifies.
        kind = next(
            (p.get("kind") for p in patches if p.get("kind") in ("delete", "rename")),
            "modify",
        )
        session_id = next((p.get("session_id") for p in patches if p.get("session_id")), "")
        rows.append(
            {
                "qname": qname,
                "op": kind,
                "notes": [p.get("note", "") for p in patches if p.get("note")],
                "reasons": [p.get("reason", "") for p in patches if p.get("reason")],
                "session_id": session_id,
                "session_note": session_note,
                "ts": now,
            }
        )
    for _file, creates in creates_by_file.items():
        for c in creates:
            rows.append(
                {
                    "qname": c.get("target_qname", ""),
                    "op": "create",
                    "notes": [c.get("note", "")] if c.get("note") else [],
                    "reasons": [c.get("reason", "")] if c.get("reason") else [],
                    "session_id": c.get("session_id", ""),
                    "session_note": session_note,
                    "ts": now,
                }
            )

    record_applied(project_root, rows)
    store.delete_patches(all=True)
    store.delete_create_patches(all=True)

    return {
        "ok": True,
        "mode": "record",
        "recorded": len(rows),
        "symbols": [r["qname"] for r in rows],
        "session_note": session_note,
        "next": (
            "Intent recorded to the session log. The pre-commit digest will carry it; "
            "no code was generated — source changes are yours."
        ),
    }
