from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any

from pydantic import BaseModel, Field


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


def _triefact_pathspecs(config: Any) -> list[str]:
    """Git pathspecs selecting the triefact tree minus the digest archive.

    The digest files under ``diff.diffs_dir`` live inside the triefact tree,
    so evidence collection must exclude them — otherwise every digest write
    would feed previous digests back into the next digest's evidence.
    """
    specs = [config.triefacts.root]
    diffs_dir = getattr(getattr(config, "diff", None), "diffs_dir", "")
    if diffs_dir:
        specs.append(f":(exclude){diffs_dir}")
    # The generated index is derived data — churn in it is never evidence.
    specs.append(f":(exclude){config.triefacts.root}/README.md")
    return specs


def collect_session_diff(
    project_root: Any,
    config: Any,
    store: Any,
    *,
    base: str = "HEAD",
) -> SessionDiff:
    """Gather one session's evidence: the git diff of the triefact tree vs
    `base`, sealed (applied) intent rows awaiting consumption into a digest,
    and still-unsealed staged notes. Everything comes from the qname-keyed
    patches tables; the committed digest is the only durable record."""
    from trie.git_helpers import diff_paths

    diff = diff_paths(project_root, _triefact_pathspecs(config), base=base) or ""

    applied: list[dict[str, Any]] = []
    for qname, rows in store.get_all_patches_grouped(applied=True).items():
        applied.append(
            {
                "qname": qname,
                "op": next(
                    (r.get("kind") for r in rows if r.get("kind") in ("delete", "rename")),
                    "modify",
                ),
                "notes": [r.get("note", "") for r in rows if r.get("note")],
                "reasons": [r.get("reason", "") for r in rows if r.get("reason")],
                "session_note": next(
                    (r.get("session_note") for r in rows if r.get("session_note")), ""
                ),
            }
        )
    for _file, rows in store.get_create_patches_grouped(applied=True).items():
        for r in rows:
            applied.append(
                {
                    "qname": r.get("target_qname", ""),
                    "op": "create",
                    "notes": [r.get("note", "")] if r.get("note") else [],
                    "reasons": [r.get("reason", "")] if r.get("reason") else [],
                    "session_note": r.get("session_note", ""),
                }
            )

    pending: list[dict[str, Any]] = []
    for qname, rows in store.get_all_patches_grouped(applied=False).items():
        for row in rows:
            pending.append({**row, "qname": qname, "op": row.get("kind", "modify")})
    for target_file, rows in store.get_create_patches_grouped(applied=False).items():
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

    # Otherwise truncate at max_chars with trailing ellipsis, preferring
    # the last word boundary so cuts never land mid-word.
    if len(collapsed) > max_chars:
        cut = collapsed[:max_chars]
        space = cut.rfind(" ")
        if space > max_chars // 2:
            cut = cut[:space]
        return cut.rstrip() + "…"

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


class SessionNarrative(BaseModel):
    """Structured LLM output for one session's change digest narrative."""

    one_liner: str = Field(
        description="One plain-text sentence (max ~25 words) summarising the net change. No markdown.",
    )
    body: str = Field(
        description="Full narrative, max 120 words of markdown. No headings. Don't restate one_liner.",
    )
    conflicts: list[str] = Field(
        default_factory=list,
        description="One sentence per note-vs-diff discrepancy, naming the symbol. Usually empty.",
    )

    def as_markdown(self) -> str:
        """Render the narrative as the markdown block embedded in a digest entry.

        Format: bold one-liner paragraph, blank line, body, then one blockquote
        line per conflict (``> **Intent vs. diff:** …``) so conflicts stand out
        visually in rendered PR comments without being headings (digest entries
        reserve headings for structural parsing).
        """
        parts: list[str] = []
        one = self.one_liner.strip()
        if one:
            parts.append(f"**{one}**")
        body = self.body.strip()
        if body:
            parts.append(body)
        conflict_lines = [
            f"> **Intent vs. diff:** {c.strip()}" for c in self.conflicts if c.strip()
        ]
        if conflict_lines:
            parts.append("\n".join(conflict_lines))
        return "\n\n".join(parts)


_NARRATIVE_SYSTEM_PROMPT: str = """You are writing the summary of a change digest that reviewers read inside a pull request. Audience: a reviewer deciding what this commit did and why.

You receive two kinds of evidence: (1) patch notes the coding agent recorded when staging edits — the stated intent — and (2) the raw unified diff of the project's triefact documentation tree — the observed effect. Triefacts are per-file markdown descriptions of source symbols, so their diff reflects behavioural changes in the code.

Produce three fields:
- one_liner: one standalone plain-text sentence (max ~25 words) a reviewer can read instead of the body. No markdown.
- body: the full narrative, at most 120 words.
- conflicts: only when a note claims X but the diff shows Y (or shows no corresponding change), one sentence per discrepancy naming the symbol. Normally empty; do not invent conflicts.

Rules for the body, without exception:
- Format: plain paragraphs and simple '-' bullets only. NO headings of any level whatsoever. No preamble, no sign-off.
- Describe the NET change as if it had been made cleanly in one pass. NEVER narrate process: do not mention bugs found and fixed within code that was itself created this session, do not describe a test-fix chronology, do not use phrases like 'a follow-up fix', do not mention line-number shifts, and do not narrate updates to triefact descriptions or documentation-of-documentation.
- Name the key symbols affected.
- Do not repeat the one_liner verbatim as the opening sentence.
- Keep conflict observations in the conflicts field, not in the body."""


def synthesize_narrative(
    data: SessionDiff, client: Any, *, max_diff_chars: int = 24000, max_tokens: int = 1024
) -> SessionNarrative:
    """Synthesise a structured intent-level session narrative from the collected evidence.

    Uses structured output (``SessionNarrative``: one_liner + body + conflicts) rather than
    plain text so the digest can render a skimmable bold summary line, the full narrative,
    and any intent-vs-diff discrepancies as distinct blocks — see
    ``SessionNarrative.as_markdown``.

    The evidence prompt assembled by ``build_narrative_prompt`` is sent to the client as a
    ``cache_prefix`` so that repeated ``trie diff`` runs within the Anthropic cache TTL reuse the
    cached evidence block instead of re-billing it on every call.  A short instruction message
    is used as the actual user turn.  Clients that do not support ``cache_prefix`` (e.g. test
    fakes) fall back transparently to the original single-prompt call.

    ``max_tokens`` is a runaway guard, NOT the length target — the system prompt's word budget
    governs length. Setting it near the budget (~180 tokens for 120 words) hard-truncates
    budget-respecting narratives mid-sentence, which shipped cut-off digests twice before this
    was caught (telemetry showed output_tokens == max_tokens exactly). With structured output
    a truncation surfaces as a validation retry instead of a silent cut-off, which makes a
    generous cap even more important — a tight cap now burns retries instead of words.
    """
    prompt = build_narrative_prompt(data, max_diff_chars=max_diff_chars)
    instruction = (
        "Write the session narrative now, following the system instructions exactly. "
        "Stay within the word limit and do not use any headings."
    )
    try:
        result = client.run(
            SessionNarrative,
            _NARRATIVE_SYSTEM_PROMPT,
            instruction,
            cache_prefix=prompt,
            max_tokens=max_tokens,
        )
    except TypeError:
        result = client.run(
            SessionNarrative, _NARRATIVE_SYSTEM_PROMPT, prompt, max_tokens=max_tokens
        )
    narrative = result.output
    if not isinstance(narrative, SessionNarrative):
        # Defensive: a fake/legacy client returned bare text.
        return SessionNarrative(one_liner="", body=str(narrative).strip())
    return narrative


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
            # The display is capped; the RECORD must not be. Overflow rows ride
            # in an HTML comment (invisible rendered, parsed by
            # _parse_digest_file) so intent-gate coverage and amend folding
            # never lose symbols past the cap.
            lines.append("<!-- trie:changes-overflow")
            for b in change_bullets[max_changes:]:
                lines.append(b)
            lines.append("-->")

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


DIGEST_FILE_HEADER = """\
<!-- auto-generated by `trie diff --write` (wired into the pre-commit hook)
     one immutable digest file per commit; TRIE_DIFF.md at the project root
     is a symlink to the latest one; do not edit by hand -->
"""


# Matches the entry heading emitted by render_digest_section:
#   ## <title> — <date> (parent <sha>)
# Title is matched non-greedily so an em-dash inside it can't swallow the date.
DIGEST_HEADING_RE = re.compile(
    r"^## (?P<title>.+?) — (?P<date>\d{4}-\d{2}-\d{2}(?:[ T][\d:]+)?) "
    r"\(parent (?P<parent>[0-9a-fA-F]{4,40})\)\s*$",
    re.MULTILINE,
)


def _parse_digest_file(path: Any) -> dict | None:
    """Parse one digest file into {name, title, date, parent, changes}.

    `changes` is the list of per-symbol lines from the `### Changes` section
    (without the leading `- `). Returns None for files that don't carry a
    parseable entry heading (foreign files in the archive dir)."""
    try:
        text = path.read_text()
    except OSError:
        return None
    m = DIGEST_HEADING_RE.search(text)
    if m is None:
        return None
    changes: list[str] = []
    in_changes = False
    in_overflow = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped == "### Changes":
            in_changes = True
            continue
        if in_changes:
            if stripped == "<!-- trie:changes-overflow":
                in_overflow = True
                continue
            if in_overflow and stripped == "-->":
                in_overflow = False
                continue
            if stripped.startswith("### "):  # next section (e.g. Staged)
                break
            if stripped.startswith("- ") and not stripped.startswith("- … and "):
                changes.append(stripped[2:])
    return {
        "name": path.name,
        "title": m.group("title"),
        "date": m.group("date"),
        "parent": m.group("parent"),
        "changes": changes,
    }


def iter_digest_entries(project_root: Any, *, diffs_dir: str = "triefacts/triediffs") -> list[dict]:
    """Parsed digest entries, newest first (timestamp-prefixed names sort chronologically)."""
    from pathlib import Path

    archive = Path(project_root) / diffs_dir
    if not archive.is_dir():
        return []
    entries: list[dict] = []
    for path in sorted(archive.glob("*.md"), reverse=True):
        entry = _parse_digest_file(path)
        if entry is not None:
            entries.append(entry)
    return entries


def symbol_history(
    project_root: Any,
    qname: str,
    *,
    diffs_dir: str = "triefacts/triediffs",
    limit: int = 5,
) -> list[dict]:
    """Chronological intent trail for one symbol, newest first.

    The digest archive stores every commit's intent keyed by qname in its
    `### Changes` lines — a wiki that knows not just what a symbol is but why
    it is that way. Returns up to `limit` rows:
    `{date, title, change, digest}` where `change` is the digest's change line
    for this symbol (marker included: `~` modified, `+` added, U+2212 removed).
    """
    # Change lines: `~ <qname> — ...` / `+ <qname> — ...` / U+2212-marked removals.
    line_re = re.compile(rf"^[~+\u2212] {re.escape(qname)}(?=$|[\s,])")
    rows: list[dict] = []
    for entry in iter_digest_entries(project_root, diffs_dir=diffs_dir):
        for change in entry["changes"]:
            if line_re.match(change):
                rows.append(
                    {
                        "date": entry["date"],
                        "title": entry["title"],
                        "change": change,
                        "digest": entry["name"],
                    }
                )
                break  # one line per symbol per digest by construction
        if len(rows) >= limit:
            break
    return rows


def file_history(
    project_root: Any,
    module_prefix: str,
    *,
    diffs_dir: str = "triefacts/triediffs",
    limit: int = 5,
) -> list[dict]:
    """Intent trail for every symbol in one module, newest first.

    `module_prefix` is the qname module part (source path minus extension,
    e.g. 'trie/session_diff'); matches change lines for `<module_prefix>:*`.
    Returns up to `limit` rows shaped like `symbol_history` rows.
    """
    line_re = re.compile(rf"^[~+\u2212] {re.escape(module_prefix)}:\S+")
    rows: list[dict] = []
    for entry in iter_digest_entries(project_root, diffs_dir=diffs_dir):
        for change in entry["changes"]:
            if line_re.match(change):
                rows.append(
                    {
                        "date": entry["date"],
                        "title": entry["title"],
                        "change": change,
                        "digest": entry["name"],
                    }
                )
                if len(rows) >= limit:
                    return rows
    return rows


def rows_from_digest_entry(entry: dict) -> list[dict]:
    """Fold a parsed digest entry's Changes lines back into applied-row shape.

    Used on amend/retry: the previous digest for the same parent already
    consumed that session's pending intent, so its rows are recovered from the
    entry itself (the digest IS the record) and merged with any new pending
    rows before the entry is rewritten in place.
    """
    marker_to_op = {"~": "modify", "+": "create", "\u2212": "delete"}
    rows: list[dict] = []
    for change in entry.get("changes", []):
        parts = change.split(" ", 2)
        if len(parts) < 2 or parts[0] not in marker_to_op:
            continue
        qname = parts[1]
        text = ""
        if len(parts) == 3 and parts[2].startswith("— "):
            text = parts[2][2:]
        rows.append(
            {
                "qname": qname,
                "op": marker_to_op[parts[0]],
                "notes": [text] if text else [],
                "reasons": [],
                "session_note": entry.get("title", ""),
            }
        )
    return rows


def _new_digest_filename() -> str:
    """Return a fresh digest filename: `<utc-timestamp>-<uuid4-hex>.md`.

    The timestamp prefix makes lexicographic order equal chronological order,
    which the retention prune relies on; the uuid suffix guarantees uniqueness
    when two writes land in the same second.
    """
    import time
    import uuid

    stamp = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
    return f"{stamp}-{uuid.uuid4().hex}.md"


def write_digest(
    project_root: Any,
    section: str,
    *,
    diffs_dir: str = "triefacts/triediffs",
    symlink_path: str = "TRIE_DIFF.md",
    max_entries: int = 20,
    reuse_file: str | None = None,
) -> str:
    """Write one digest entry as its own file and repoint the latest-symlink.

    Storage model:

    - Every digest write produces one file under *diffs_dir* named
      ``<utc-timestamp>-<uuid>.md`` (header comment + the rendered section).
      One file per commit means the digest always shows up in a PR as a
      brand-new file — pure additions, never a diff-of-a-diff.
    - *reuse_file* (a project-relative path, from the digest cursor) rewrites
      that existing file in place instead of creating a new one — the
      amend/retry case, so one commit never spawns duplicate digest files.
    - ``<project_root>/<symlink_path>`` is (re)pointed at the written file via
      a relative symlink, replaced atomically (temp link + rename). A regular
      file already at that path (e.g. pre-symlink layouts) is replaced.
    - Retention: only the newest *max_entries* files are kept in *diffs_dir*;
      older ones are unlinked (they remain in git history).

    Returns the project-relative path of the digest file written.
    """
    import os
    from pathlib import Path

    root = Path(project_root)
    dir_path = root / diffs_dir
    dir_path.mkdir(parents=True, exist_ok=True)

    # Same-commit rewrite, or a fresh timestamped file.
    if reuse_file and (root / reuse_file).parent == dir_path:
        file_path = root / reuse_file
    else:
        file_path = dir_path / _new_digest_filename()

    file_path.write_text(DIGEST_FILE_HEADER + "\n" + section.rstrip("\n") + "\n")

    # Retention prune. Names sort chronologically via the timestamp prefix,
    # but same-second writes tie there and the uuid tiebreak is random — so
    # order by mtime (ns) with the just-written file pinned to the front.
    import contextlib

    def _prune_key(p: Path) -> tuple:
        try:
            mtime_ns = p.stat().st_mtime_ns
        except OSError:
            mtime_ns = 0
        return (p != file_path, -mtime_ns, p.name)

    entries = sorted((p for p in dir_path.glob("*.md") if p.is_file()), key=_prune_key)
    for stale in entries[max_entries:]:
        with contextlib.suppress(OSError):
            stale.unlink()

    # Atomically repoint the latest-symlink (relative target, repo-relocatable).
    link_path = root / symlink_path
    target = os.path.relpath(file_path, link_path.parent)
    tmp_link = link_path.parent / f".{link_path.name}.tmp-{os.getpid()}"
    try:
        tmp_link.unlink(missing_ok=True)
        os.symlink(target, tmp_link)
        os.replace(tmp_link, link_path)
    except OSError:
        # Filesystems without symlink support degrade to a regular pointer file.
        tmp_link.unlink(missing_ok=True)
        link_path.write_text(f"{target}\n")

    return str(file_path.relative_to(root))


def collect_symbol_deltas(project_root, config, base: str = "HEAD") -> list:
    """Compute per-symbol one-liner deltas between the working tree and *base*."""
    from trie import git_helpers
    from trie.sync.writer import Section, TriefactFile, extract_one_liner

    pathspecs = _triefact_pathspecs(config)

    # Collect changed tracked files
    changed_files = []
    tracked_output = git_helpers._run_git(
        ["diff", "--name-only", base, "--", *pathspecs],
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
        ["ls-files", "--others", "--exclude-standard", "--", *pathspecs],
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
