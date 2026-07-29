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
    # Unapplied only: sealed rows are on their way into a digest and are no
    # longer reviewable staging.
    patches_by_qname = store.get_all_patches_grouped(applied=False)
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
    """Seal pending patch notes as applied intent — no code generation.

    Staging and sealing both live in the patches tables (qname-keyed, so
    graph refreshes can't destroy them): apply stamps every unapplied row
    with `applied=1` and the unifying `session_note`. The rows stay put until
    `trie gate` / `trie diff --write` consumes them into the commit's digest
    entry — the durable record, in the triefact tree. More than one symbol
    requires a real `session_note` (see `session_note_ok`).
    """
    unapplied = store.get_all_patches_grouped(applied=False)
    creates_by_file = store.get_create_patches_grouped(applied=False)
    create_count = sum(len(rows) for rows in creates_by_file.values())
    total = len(unapplied) + create_count

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

    symbols = sorted(
        set(unapplied.keys())
        | {c.get("target_qname", "") for rows in creates_by_file.values() for c in rows}
    )
    store.mark_patches_applied(session_note)

    envelope = {
        "ok": True,
        "mode": "record",
        "recorded": len(symbols),
        "symbols": symbols,
        "session_note": session_note,
        "next": (
            "Intent sealed; the commit digest will consume it. No code was "
            "generated — source changes are yours."
        ),
    }

    # Apply-time coverage feedback: run the same evaluation the pre-commit
    # gate will, so an agent learns about touched-but-unnoted symbols NOW
    # (one patch call away) instead of at commit time (one failed commit
    # away). Advisory — evaluation failures never poison a successful seal.
    try:
        from trie.intent_gate import evaluate

        report = evaluate(project_root, config, store)
        envelope["uncovered"] = sorted(t.qname for t in report.uncovered)
        if envelope["uncovered"]:
            envelope["next"] = (
                "Intent sealed, but these touched symbols still have no note and "
                "would fail the commit gate: stage a patch note for each, then "
                "patch_apply again."
            )
    except Exception:
        pass

    return envelope
