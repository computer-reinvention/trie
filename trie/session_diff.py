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


def _one_line(text: str, max_chars: int = 160) -> str:
    """Flatten arbitrary multi-line text to a single safe line for markdown embedding."""
    # Find the first non-empty line
    first_line = ""
    for line in text.splitlines():
        stripped = line.strip()
        if stripped:
            first_line = stripped
            break

    if not first_line:
        return ""

    # Collapse all whitespace runs to single spaces
    import re

    collapsed = re.sub(r"\s+", " ", first_line).strip()

    # Cut at the first sentence boundary if one occurs within the budget
    dot_space = collapsed.find(". ")
    if dot_space != -1 and dot_space + 1 <= max_chars:
        return collapsed[: dot_space + 1]  # include the period

    # Otherwise truncate at max_chars with trailing ellipsis
    if len(collapsed) > max_chars:
        return collapsed[:max_chars] + "…"

    return collapsed


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


_NARRATIVE_SYSTEM_PROMPT: str = """You are writing the summary paragraph of a change digest that reviewers read inside a pull request. Audience: a reviewer deciding what this commit did and why.

You receive two kinds of evidence: (1) patch notes the coding agent recorded when staging edits — the stated intent — and (2) the raw unified diff of the project's triefact documentation tree — the observed effect. Triefacts are per-file markdown descriptions of source symbols, so their diff reflects behavioural changes in the code.

Rules you must follow without exception:
- Length: at most 120 words total.
- Format: plain paragraphs and simple '-' bullets only. NO headings of any level whatsoever. No preamble, no sign-off.
- Describe the NET change as if it had been made cleanly in one pass. NEVER narrate process: do not mention bugs found and fixed within code that was itself created this session, do not describe a test-fix chronology, do not use phrases like 'a follow-up fix', do not mention line-number shifts, and do not narrate updates to triefact descriptions or documentation-of-documentation.
- Name the key symbols affected.
- If the evidence conflicts (a note claims X but the diff shows Y), state that conflict in one sentence — that is the one process observation permitted."""


def synthesize_narrative(
    data: SessionDiff, client: Any, *, max_diff_chars: int = 24000, max_tokens: int = 180
) -> str:
    """Synthesise a concise intent-level session narrative from the collected evidence via the LLM.

    The evidence prompt assembled by ``build_narrative_prompt`` is sent to the client as a
    ``cache_prefix`` so that repeated ``trie diff`` runs within the Anthropic cache TTL reuse the
    cached evidence block instead of re-billing it on every call.  A short instruction message
    is used as the actual user turn to stay within the strict word budget imposed by the system
    prompt.  Clients that do not support ``cache_prefix`` (e.g. test fakes) fall back
    transparently to the original single-prompt call.

    Returns markdown text.
    """
    prompt = build_narrative_prompt(data, max_diff_chars=max_diff_chars)
    instruction = (
        "Write the session narrative now, following the system instructions exactly. "
        "Stay within the word limit and do not use any headings."
    )
    try:
        result = client.run_text(
            _NARRATIVE_SYSTEM_PROMPT,
            instruction,
            cache_prefix=prompt,
            max_tokens=max_tokens,
        )
    except TypeError:
        result = client.run_text(_NARRATIVE_SYSTEM_PROMPT, prompt, max_tokens=max_tokens)
    return str(result.output).strip()


def render_digest_section(
    data: SessionDiff,
    *,
    title: str,
    date_str: str,
    parent_short: str,
    narrative: str = "",
    deltas: list[dict] | None = None,
    max_changes: int = 20,
) -> str:
    """Render one digest entry as a markdown section string."""

    def _demote_narrative_headings(text: str) -> str:
        result: list[str] = []
        in_fence = False
        for line in text.splitlines():
            if line.startswith("```"):
                in_fence = not in_fence
                result.append(line)
                continue
            if not in_fence:
                if line.startswith("## "):
                    line = "### " + line[3:]
                elif line.startswith("# "):
                    line = "### " + line[2:]
            result.append(line)
        return "\n".join(result)

    lines: list[str] = []

    # 1. Entry heading — parse anchor for upsert_digest
    lines.append(f"## {title} — {date_str} (parent {parent_short})")
    lines.append("")

    # 2. Optional narrative paragraph (headings demoted for defence in depth)
    if narrative:
        demoted = _demote_narrative_headings(narrative.strip())
        lines.append(demoted)
        lines.append("")

    # 3. ### Changes — one line per symbol
    lines.append("### Changes")
    lines.append("")

    # Build delta index keyed by qname (first-entry-wins for same qname)
    delta_index: dict[str, dict] = {}
    for d in deltas or []:
        qname = d.get("qname", "")
        if qname and qname not in delta_index:
            delta_index[qname] = d

    # Build applied index keyed by qname (first-note-wins merging + follow-up counts)
    applied_index: dict[str, dict] = {
        row["qname"]: row for row in merge_applied_by_symbol(data.applied or [])
    }

    # Union of all qnames, preserving encounter order
    seen_qnames: list[str] = []
    seen_qnames_set: set[str] = set()
    for entry in data.applied or []:
        q = entry.get("qname", "")
        if q and q not in seen_qnames_set:
            seen_qnames.append(q)
            seen_qnames_set.add(q)
    for d in deltas or []:
        q = d.get("qname", "")
        if q and q not in seen_qnames_set:
            seen_qnames.append(q)
            seen_qnames_set.add(q)

    change_bullets: list[str] = []
    for qname in seen_qnames:
        delta = delta_index.get(qname)
        applied = applied_index.get(qname)

        # Collect followups from whichever source reports them
        followups = 0
        if delta:
            followups = delta.get("followups", 0) or 0
        if followups == 0 and applied:
            followups = applied.get("followups", 0) or 0

        if delta:
            status = delta.get("status", "changed")
            if status == "added":
                after = _one_line(delta.get("after", ""))
                bullet = f'- + {qname} — "{after}"'
            elif status == "removed":
                bullet = f"- − {qname}"  # noqa: RUF001 — U+2212 distinguishes marker from bullet hyphen
            else:
                before = _one_line(delta.get("before", ""))
                after = _one_line(delta.get("after", ""))
                bullet = f'- ~ {qname} — "{before}" → "{after}"'
        elif applied:
            op = applied.get("op", "")
            note_line = _one_line(applied.get("note", ""))
            if op in ("create", "add"):
                marker = "+"
            elif op in ("delete", "remove"):
                marker = "−"  # noqa: RUF001 — U+2212 distinguishes marker from bullet hyphen
            else:
                marker = "~"
            bullet = f"- {marker} {qname} — {note_line}" if note_line else f"- {marker} {qname}"
        else:
            continue

        if followups > 0:
            suffix = "follow-up" if followups == 1 else "follow-ups"
            bullet += f" (+{followups} {suffix})"

        change_bullets.append(bullet)

    if not change_bullets:
        lines.append("- (no symbol-level changes)")
    else:
        shown = change_bullets[:max_changes]
        for b in shown:
            lines.append(b)
        remainder = len(change_bullets) - len(shown)
        if remainder > 0:
            lines.append(f"- … and {remainder} more")

    lines.append("")

    # 4. ### Staged (not applied) — only when pending is non-empty
    if data.pending:
        lines.append("### Staged (not applied)")
        lines.append("")
        for entry in data.pending:
            op = entry.get("op", "")
            qname = entry.get("qname", "")
            note_text = entry.get("note", "")
            note_line = _one_line(note_text)
            bullet = f"- {op} {qname}"
            if note_line:
                bullet += f" — {note_line}"
            lines.append(bullet)
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

    Entry boundaries are lines matching the shape::

        ## <title> — <date> (parent <sha>)

    Narrative content that legally contains bare ``##`` headings is never
    mistaken for entry delimiters because those lines cannot carry the
    ``(parent <hex>)`` suffix that the boundary regex requires.
    """
    import re

    # Only lines whose heading carries the '(parent <hex>)' suffix are treated
    # as entry boundaries.  Arbitrary '## ' lines inside narrative bodies do
    # not match this shape, so injection via LLM-generated markdown is
    # structurally impossible.
    ENTRY_HEADING = re.compile(r"(?m)(?=^## .+\(parent [0-9a-fA-F]{4,40}\)\s*$)")
    HEADING_LINE = re.compile(r"^## .+\(parent [0-9a-fA-F]{4,40}\)\s*$", re.MULTILINE)

    raw_entries = re.split(ENTRY_HEADING, existing_text)
    entries = [e.rstrip("\n") for e in raw_entries if HEADING_LINE.match(e)]

    new_section = section.rstrip("\n")

    # Same-commit deduplication: check whether the newest entry's heading line
    # ends with '(parent <base_short>)'.
    if entries and re.search(
        rf"\(parent {re.escape(base_short)}\)\s*$",
        entries[0].splitlines()[0],
    ):
        # Replace the newest entry — same commit, amend/retry.
        entries[0] = new_section
    else:
        entries.insert(0, new_section)

    entries = entries[:max_entries]

    body = "\n\n".join(entries)
    return DIGEST_HEADER + "\n" + body + "\n"


def collect_symbol_deltas(project_root, config, base: str = "HEAD") -> list:
    """Compute per-symbol one-liner deltas between the working tree and *base*."""
    from trie import git_helpers
    from trie.sync.writer import Section, TriefactFile, extract_one_liner

    triefacts_root = config.triefacts.root

    # Collect changed tracked files
    changed_files = []
    tracked_output = git_helpers._run_git(
        ["diff", "--name-only", base, "--", triefacts_root],
        cwd=project_root,
    )
    if tracked_output:
        changed_files.extend(
            line.strip()
            for line in tracked_output.decode("utf-8", errors="replace").splitlines()
            if line.strip()
        )

    # Collect untracked files
    untracked_output = git_helpers._run_git(
        ["ls-files", "--others", "--exclude-standard", "--", triefacts_root],
        cwd=project_root,
    )
    if untracked_output:
        for line in untracked_output.decode("utf-8", errors="replace").splitlines():
            line = line.strip()
            if line and line not in changed_files:
                changed_files.append(line)

    rows = []

    for rel_path in changed_files:
        try:
            # Before: content at base ref (None if the file is new)
            before_text = git_helpers.show_file_at_ref(project_root, base, rel_path)

            # After: working-tree content (None if deleted)
            import os

            abs_path = os.path.join(project_root, rel_path)
            if os.path.exists(abs_path):
                with open(abs_path, encoding="utf-8") as fh:
                    after_text = fh.read()
            else:
                after_text = None

            # Build {qname: one_liner} maps for each side
            def build_map(text):
                if text is None:
                    return {}
                try:
                    tf = TriefactFile.parse(text)
                    return {
                        chunk.qualified_name: extract_one_liner(chunk.body)
                        for chunk in tf.chunks
                        if isinstance(chunk, Section)
                    }
                except Exception:
                    return {}

            before_map = build_map(before_text)
            after_map = build_map(after_text)

            all_qnames = sorted(set(before_map) | set(after_map))

            for qname in all_qnames:
                in_before = qname in before_map
                in_after = qname in after_map

                if in_after and not in_before:
                    rows.append(
                        {
                            "file": rel_path,
                            "qname": qname,
                            "status": "added",
                            "after": after_map[qname],
                        }
                    )
                elif in_before and not in_after:
                    rows.append(
                        {
                            "file": rel_path,
                            "qname": qname,
                            "status": "removed",
                            "before": before_map[qname],
                        }
                    )
                elif in_before and in_after and before_map[qname] != after_map[qname]:
                    # Identical one-liners never produce a row (churn gate).
                    rows.append(
                        {
                            "file": rel_path,
                            "qname": qname,
                            "status": "changed",
                            "before": before_map[qname],
                            "after": after_map[qname],
                        }
                    )

        except Exception:
            # Quiet degradation: skip any file that fails
            continue

    # Sort by file then qname
    rows.sort(key=lambda r: (r.get("file", ""), r.get("qname", "")))
    return rows


def merge_applied_by_symbol(applied: list[dict]) -> list[dict]:
    seen: dict[str, dict] = {}
    order: list[str] = []
    for entry in applied:
        qname = entry.get("qname", "")
        notes = entry.get("notes") or ([entry["note"]] if entry.get("note") else [])
        if qname not in seen:
            seen[qname] = {
                "qname": qname,
                "op": entry.get("op", ""),
                "note": notes[0] if notes else "",
                # Extra notes within the first entry are follow-ups too.
                "followups": max(len(notes) - 1, 0),
            }
            order.append(qname)
        else:
            # Every note in a subsequent entry is a follow-up (min 1 per entry).
            seen[qname]["followups"] += max(len(notes), 1)
    return [seen[qname] for qname in order]
