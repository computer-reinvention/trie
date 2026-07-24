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
    since: float | None = None,
) -> SessionDiff:
    """Gather one session's evidence: git diff of the triefact tree vs `base`, applied patch notes from the session log, and still-pending patch notes from the store. `session_id=None` means 'everything available'. `since` restricts applied log entries to those recorded after the given timestamp."""
    from trie.git_helpers import diff_paths
    from trie.session_log import read_entries

    diff = diff_paths(project_root, [config.triefacts.root], base=base) or ""
    applied = read_entries(project_root, session_id=session_id, since=since)
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


def _diff_stat(diff_text: str) -> list[tuple[str, int, int]]:
    results: list[tuple[str, int, int]] = []
    current_path: str | None = None
    added = 0
    removed = 0

    for line in diff_text.splitlines():
        if line.startswith("diff --git "):
            if current_path is not None:
                results.append((current_path, added, removed))
            added = 0
            removed = 0
            current_path = None

            # Parse path from "diff --git a/... b/..."
            line[len("diff --git ") :].split(" ")
            # Find the b/ side: last token starting with "b/"
            # For no-index diffs the format may differ slightly
            a_side = None
            b_side = None
            # Rebuild splitting on ' b/' to handle spaces in paths
            rest = line[len("diff --git ") :]
            # Try to split on ' b/' boundary
            mid = rest.find(" b/")
            if mid != -1:
                a_side_raw = rest[:mid]
                b_side_raw = rest[mid + 1 :]
                a_side = a_side_raw[2:] if a_side_raw.startswith("a/") else a_side_raw
                b_side = b_side_raw[2:] if b_side_raw.startswith("b/") else b_side_raw
            else:
                # Fall back: last space-separated token
                tokens = rest.split(" ")
                raw = tokens[-1]
                b_side = raw[2:] if raw.startswith("b/") else raw
                if len(tokens) >= 2:
                    raw_a = tokens[0]
                    a_side = raw_a[2:] if raw_a.startswith("a/") else raw_a

            # Prefer non-/dev/null side
            if b_side and b_side != "/dev/null":
                current_path = b_side
            elif a_side and a_side != "/dev/null":
                current_path = a_side
            else:
                current_path = b_side or a_side or ""

            # Strip any leading absolute-path prefix, keep relative form
            if current_path and current_path.startswith("/"):
                # Try to find a/ or b/ marker within the path
                for marker in ("/a/", "/b/"):
                    idx = current_path.find(marker)
                    if idx != -1:
                        current_path = current_path[idx + len(marker) :]
                        break
                else:
                    current_path = current_path.lstrip("/")

        elif current_path is not None:
            if line.startswith("+") and not line.startswith("+++"):
                added += 1
            elif line.startswith("-") and not line.startswith("---"):
                removed += 1

    if current_path is not None:
        results.append((current_path, added, removed))

    return results


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


_NARRATIVE_SYSTEM_PROMPT: str = """You are summarising one working session on a codebase. You receive two kinds of evidence: (1) patch notes the coding agent recorded when staging edits — the stated intent — and (2) the raw unified diff of the project's triefact documentation tree — the observed effect. Triefacts are per-file markdown descriptions of source symbols, so their diff reflects behavioural changes in the code. Write a coherent, intent-level description of what changed this session: start with a one-or-two-sentence summary, then short bullet groups organised by theme or subsystem, naming the key symbols touched. Clearly separate applied changes from still-pending (staged) ones when both exist. Describe intent and effect; do not mechanically restate the diff. If the evidence conflicts (a note claims X but the diff shows Y), say so. Output plain markdown with no preamble. Important: this narrative will be embedded inside a larger markdown document beneath an H2 (##) entry heading, so use heading levels ### or deeper only — never # or ## — for any sub-headings you introduce."""


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


def render_digest_section(
    data: SessionDiff,
    *,
    base_short: str,
    date_str: str,
    narrative: str = "",
) -> str:
    """Render one digest entry as a markdown section string."""

    def _demote_narrative_headings(text: str) -> str:
        """Demote H1/H2 headings in narrative to H3+, skipping fenced code blocks."""
        result: list[str] = []
        in_fence = False
        for line in text.splitlines():
            # Track fenced code block boundaries
            if line.startswith("```"):
                in_fence = not in_fence
                result.append(line)
                continue
            if not in_fence:
                # Demote '# ' → '### ' and '## ' → '### '
                if line.startswith("## "):
                    line = "### " + line[3:]
                elif line.startswith("# "):
                    line = "### " + line[2:]
            result.append(line)
        return "\n".join(result)

    lines: list[str] = []

    # Entry heading — parse anchor for upsert_digest
    lines.append(f"## {date_str} · base {base_short}")
    lines.append("")

    # Optional narrative paragraph (headings demoted so they don't compete with entry heading)
    if narrative:
        demoted = _demote_narrative_headings(narrative.strip())
        lines.append(demoted)
        lines.append("")

    # ### Intent — deduped, insertion-ordered session_note values
    seen_notes: list[str] = []
    seen_set: set[str] = set()
    for entry in data.applied:
        note = entry.get("session_note")
        if note and note not in seen_set:
            seen_notes.append(note)
            seen_set.add(note)
    if seen_notes:
        lines.append("### Intent")
        lines.append("")
        for note in seen_notes:
            lines.append(f"- {note}")
        lines.append("")

    # ### Applied
    if data.applied:
        lines.append("### Applied")
        lines.append("")
        for entry in data.applied:
            entry_notes = entry.get("notes") or []
            notes_str = "; ".join(entry_notes) if entry_notes else ""
            bullet = f"- [{entry.get('op', '')}] {entry.get('qname', '')}"
            if notes_str:
                bullet += f" — {notes_str}"
            reasons = entry.get("reasons")
            if reasons:
                reasons_str = "; ".join(reasons)
                bullet += f" (reason: {reasons_str})"
            lines.append(bullet)
        lines.append("")

    # ### Pending (staged, not applied)
    if data.pending:
        lines.append("### Pending (staged, not applied)")
        lines.append("")
        for entry in data.pending:
            note_str = entry.get("note", "")
            bullet = f"- [{entry.get('op', '')}] {entry.get('qname', '')}"
            if note_str:
                bullet += f" — {note_str}"
            reason = entry.get("reason")
            if reason:
                bullet += f" (reason: {reason})"
            lines.append(bullet)
        lines.append("")

    # ### Triefact changes
    lines.append("### Triefact changes")
    lines.append("")
    stat = _diff_stat(data.triefact_diff)
    if not stat:
        lines.append("- (no triefact changes)")
    else:
        for path, adds, dels in stat:
            lines.append(f"- {path} (+{adds}/-{dels})")
    lines.append("")

    return "\n".join(lines)


DIGEST_HEADER = """\
# TRIE_DIFF

<!-- auto-generated by `trie diff --write` (wired into the pre-commit hook)
     prepend-only, newest entry first; do not edit by hand;
     entries roll off after max_entries -->
"""


def upsert_digest(
    existing_text: str,
    section: str,
    *,
    base_short: str,
    max_entries: int = 20,
) -> str:
    """Prepend-only update of the TRIE_DIFF.md digest.

    Maintains a newest-first list of per-commit digest entries.  If the
    current head entry already covers the same *base_short* commit (amend /
    retry scenario) it is replaced in-place; otherwise the new *section* is
    prepended.  The result is truncated to *max_entries* and always begins
    with the canonical DIGEST_HEADER so that header evolution is self-healing.
    """
    import re

    # Only lines that match the strict entry-heading shape count as boundaries.
    # This prevents LLM narrative content containing bare '## ' headings from
    # being mis-parsed as entry delimiters.
    ENTRY_HEADING = re.compile(r"(?m)(?=^## \d{4}-\d{2}-\d{2}.* · base [0-9a-fA-F]+)")

    raw_entries = re.split(ENTRY_HEADING, existing_text)
    entries = [
        e.rstrip("\n")
        for e in raw_entries
        if re.match(r"^## \d{4}-\d{2}-\d{2}.* · base [0-9a-fA-F]+", e)
    ]

    new_section = section.rstrip("\n")

    if entries and f"base {base_short}" in entries[0]:
        # Replace the newest entry — same commit, amend/retry.
        entries[0] = new_section
    else:
        entries.insert(0, new_section)

    entries = entries[:max_entries]

    body = "\n\n".join(entries)
    return DIGEST_HEADER + "\n" + body + "\n"
