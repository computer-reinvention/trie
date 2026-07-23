from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class SessionDiff:
    """Evidence collected for one session: raw triefact diff plus patch notes."""

    triefact_diff: str = ""
    applied: list[dict[str, Any]] = field(default_factory=list)
    pending: list[dict[str, Any]] = field(default_factory=list)
    base: str = "HEAD"

    def is_empty(self) -> bool:
        """True when there is nothing to report (no diff text, no notes)."""
        return not (self.triefact_diff.strip() or self.applied or self.pending)

    def session_ids(self) -> list[str]:
        """Distinct non-empty session ids across applied+pending, insertion-ordered."""
        seen: dict[str, None] = {}
        for entry in list(self.applied) + list(self.pending):
            sid = entry.get("session_id")
            if sid:
                seen[sid] = None
        return list(seen.keys())


def collect_session_diff(
    project_root: Any,
    config: Any,
    store: Any,
    *,
    session_id: str | None = None,
    base: str = "HEAD",
) -> SessionDiff:
    """Gather one session's evidence: git diff of the triefact tree vs `base`, applied patch notes from the session log, and still-pending patch notes from the store. `session_id=None` means 'everything available'."""
    from trie.git_helpers import diff_paths
    from trie.session_log import read_entries

    diff = diff_paths(project_root, [config.triefacts.root], base=base) or ""
    applied = read_entries(project_root, session_id=session_id)
    pending: list[dict[str, Any]] = []
    for qname in store.get_patched_qnames():
        for row in store.get_patches_for_qname(qname):
            pending.append({**row, "qname": qname, "op": row.get("kind", "modify")})
    for target_file, rows in store.get_create_patches_grouped().items():
        for row in rows:
            pending.append(
                {
                    "qname": row.get("target_qname", ""),
                    "op": "create",
                    "note": row.get("note", ""),
                    "reason": row.get("reason", ""),
                    "session_id": row.get("session_id", ""),
                    "file_path": target_file,
                }
            )
    if session_id is not None:
        pending = [r for r in pending if r.get("session_id") == session_id]
    return SessionDiff(triefact_diff=diff, applied=applied, pending=pending, base=base)


_FENCE = "`" * 3


def build_narrative_prompt(data: SessionDiff, *, max_diff_chars: int = 24000) -> str:
    """Assemble the user prompt: stated intent (patch notes) first, observed effect (raw triefact diff) second, truncated to a byte budget.

    Deterministic, testable prompt assembly for the session narrative, separated from the LLM call.
    """
    sections: list[str] = []

    # 1. Session intents
    seen_notes: set[str] = set()
    ordered_notes: list[str] = []
    for entry in data.applied:
        note = entry.get("session_note")
        if note and note not in seen_notes:
            seen_notes.add(note)
            ordered_notes.append(note)
    if ordered_notes:
        bullets = "\n".join(f"- {note}" for note in ordered_notes)
        sections.append(f"## Session intents\n{bullets}")

    # 2. Applied patch notes (chronological)
    if not data.applied:
        applied_body = "(none)"
    else:
        lines: list[str] = []
        for entry in data.applied:
            op = entry.get("op", "")
            qname = entry.get("qname", "")
            notes_val = "; ".join(entry.get("notes") or [])
            line = f"- [{op}] {qname}: {notes_val}"
            reasons = entry.get("reasons")
            if reasons:
                line += f" (reason: {'; '.join(reasons)})"
            lines.append(line)
        applied_body = "\n".join(lines)
    sections.append(f"## Applied patch notes (chronological)\n{applied_body}")

    # 3. Pending patch notes (staged, not yet applied)
    if not data.pending:
        pending_body = "(none)"
    else:
        lines = []
        for row in data.pending:
            op = row.get("op", "")
            qname = row.get("qname", "")
            note = row.get("note", "")
            line = f"- [{op}] {qname}: {note}"
            reason = row.get("reason")
            if reason:
                line += f" (reason: {reason})"
            lines.append(line)
        pending_body = "\n".join(lines)
    sections.append(f"## Pending patch notes (staged, not yet applied)\n{pending_body}")

    # 4. Raw triefact diff
    diff_header = f"## Raw triefact diff (vs {data.base})"
    triefact_diff = data.triefact_diff or ""
    if not triefact_diff.strip():
        diff_section = f"{diff_header}\n(no triefact changes)"
    else:
        truncated = False
        if len(triefact_diff) > max_diff_chars:
            triefact_diff = triefact_diff[:max_diff_chars]
            truncated = True
        fence_open = _FENCE + "diff"
        fence_close = _FENCE
        diff_block = f"{fence_open}\n{triefact_diff}"
        if truncated:
            diff_block += f"\n... [diff truncated at {max_diff_chars} chars]"
        diff_block += f"\n{fence_close}"
        diff_section = f"{diff_header}\n{diff_block}"
    sections.append(diff_section)

    return "\n\n".join(sections)


_NARRATIVE_SYSTEM_PROMPT: str = """You are summarising one working session on a codebase. You receive two kinds of evidence: (1) patch notes the coding agent recorded when staging edits — the stated intent — and (2) the raw unified diff of the project's triefact documentation tree — the observed effect. Triefacts are per-file markdown descriptions of source symbols, so their diff reflects behavioural changes in the code. Write a coherent, intent-level description of what changed this session: start with a one-or-two-sentence summary, then short bullet groups organised by theme or subsystem, naming the key symbols touched. Clearly separate applied changes from still-pending (staged) ones when both exist. Describe intent and effect; do not mechanically restate the diff. If the evidence conflicts (a note claims X but the diff shows Y), say so. Output plain markdown with no preamble."""


def synthesize_narrative(
    data: SessionDiff, client: Any, *, max_diff_chars: int = 24000, max_tokens: int = 1500
) -> str:
    """Synthesise a coherent intent-level session narrative from the collected evidence via the LLM.

    The evidence prompt assembled by ``build_narrative_prompt`` is sent to the client as a
    ``cache_prefix`` so that repeated ``trie diff`` runs within the Anthropic cache TTL reuse the
    cached ~10k-token evidence block instead of re-billing it on every call.  A short instruction
    message is then used as the actual user turn.  Clients that do not support ``cache_prefix``
    (e.g. test fakes) fall back transparently to the original single-prompt call.

    Returns markdown text.
    """
    prompt = build_narrative_prompt(data, max_diff_chars=max_diff_chars)
    try:
        result = client.run_text(
            _NARRATIVE_SYSTEM_PROMPT,
            "Write the session narrative now, following the system instructions.",
            cache_prefix=prompt,
            max_tokens=max_tokens,
        )
    except TypeError:
        result = client.run_text(_NARRATIVE_SYSTEM_PROMPT, prompt, max_tokens=max_tokens)
    return str(result.output).strip()
