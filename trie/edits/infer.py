from __future__ import annotations

from pathlib import Path

from trie.models import (
    BatchFilterOutput,
    FileEdit,
    MergeNotesOutput,
    SymbolEdit,
    TrieClient,
)

MERGE_PROMPT = """\
The following patch notes exist for this symbol. Some may contradict or supersede earlier ones. Return the final list of notes with superseded entries removed. Preserve chronological order for non-contradictory notes.

Existing notes:
{bullet_list}

Return the deduplicated notes and reasons."""

INFER_SYSTEM_PROMPT = """\
You update Python source code based on implementation notes and return the updated source and an updated prose summary of the symbol's purpose. The prose should describe what the symbol does at a high level — do not include implementation notes or bullet points."""

BATCH_PRE_FILTER_PROMPT = """\
For each changed callee below, determine which of its callers need source updates.
Base your decision on each caller's role/purpose and whether it depends on the
property, behavior, or implementation detail that changed.

{callee_sections}

For each caller, either SKIP (no source changes needed) or provide an UPDATE note and reason."""

FILE_GEN_PROMPT = """\
You are updating symbols in the file {file_path}.

Below is the current file content for context:
```python
{file_content}
```

Symbols that need changes:

{symbol_sections}

Apply every symbol's change into the file and return the complete updated file content plus updated prose for every changed symbol."""

FILE_FIXUP_PROMPT = """\
The following file has diagnostics errors. Fix all errors.

```python
{file_content}
```

Diagnostics:
{diagnostics}

Return the complete corrected file content."""


def _format_bullets(notes: list[str], reasons: list[str]) -> str:
    lines: list[str] = []
    for note, reason in zip(notes, reasons, strict=False):
        lines.append(f"<bullet> {note}  — {reason}")
    return "\n".join(lines)


def merge_notes(client: TrieClient, patches: list[dict]) -> tuple[list[str], list[str]]:
    if not patches:
        return [], []

    notes = [p["note"] for p in patches]
    reasons = [p["reason"] for p in patches]
    bullet_list = _format_bullets(notes, reasons)

    result = client.run(
        MergeNotesOutput,
        system_prompt="",
        user_prompt=MERGE_PROMPT.format(bullet_list=bullet_list),
        max_tokens=512,
    )
    merged: MergeNotesOutput = result.output
    return merged.notes, merged.reasons


def infer_source_and_prose(
    client: TrieClient,
    old_source: str,
    old_prose: str,
    notes: list[str],
    reasons: list[str],
) -> tuple[str, str]:
    bullet_list = _format_bullets(notes, reasons)

    user_prompt = f"""\
Old prose (the symbol's documented purpose):
{old_prose}

Implementation notes (what changed):
{bullet_list}

Old source:
```python
{old_source}
```"""

    result = client.run(
        SymbolEdit,
        system_prompt=INFER_SYSTEM_PROMPT,
        user_prompt=user_prompt,
        max_tokens=4096,
    )
    edit: SymbolEdit = result.output
    return edit.source, edit.prose


def infer_file_source(
    client: TrieClient,
    file_path: str,
    file_content: str,
    symbols_data: list[dict],
    *,
    max_tokens: int = 8192,
) -> tuple[str, dict[str, str]]:
    sections: list[str] = []
    for idx, sd in enumerate(symbols_data, 1):
        notes_text = "".join(
            f"- {n}  —  {r}\n"
            for n, r in zip(sd["merged_notes"], sd["merged_reasons"], strict=False)
        )
        sections.append(
            f"--- SYMBOL {idx}: {sd['qname']} ---\n"
            f"Old source:\n```python\n{sd['old_source']}\n```\n\n"
            f"Old prose:\n{sd['old_prose']}\n\n"
            f"Implementation notes:\n{notes_text}\n"
        )

    user_prompt = FILE_GEN_PROMPT.format(
        file_path=file_path,
        file_content=file_content,
        symbol_sections="\n".join(sections),
    )

    result = client.run(
        FileEdit,
        system_prompt=INFER_SYSTEM_PROMPT,
        user_prompt=user_prompt,
        max_tokens=max_tokens,
    )
    file_edit: FileEdit = result.output
    proses = {sp.qname: sp.prose for sp in file_edit.prose}
    return file_edit.content, proses


def _build_caller_summaries(caller_qnames: list[str], store, triefacts_root) -> list[dict]:
    from trie.sync.writer import SECTION_CLOSE, SECTION_OPEN_RE

    results: list[dict] = []
    for qn in caller_qnames:
        detail = store.get_symbol_detail(qn)
        if detail is None:
            continue
        rel_md = Path(detail.file_path).with_suffix(".md")
        triefact_path = triefacts_root / rel_md
        prose = ""
        if triefact_path.exists():
            text = triefact_path.read_text()
            for match in SECTION_OPEN_RE.finditer(text):
                if match.group("symbol") != qn:
                    continue
                close_idx = text.find(SECTION_CLOSE, match.end())
                if close_idx == -1:
                    break
                body = text[match.end() : close_idx]
                if body.startswith("\n"):
                    body = body[1:]
                if body.endswith("\n"):
                    body = body[:-1]
                prose = body[:200]
                break
        results.append(
            {
                "qname": qn,
                "signature": detail.signature or "",
                "one_liner": detail.one_liner,
                "prose": prose,
            }
        )
    return results


def _read_prose(qname: str, file_path: str, triefacts_root) -> str:
    from trie.sync.writer import SECTION_CLOSE, SECTION_OPEN_RE

    rel_md = Path(file_path).with_suffix(".md")
    triefact_path = triefacts_root / rel_md
    if not triefact_path.exists():
        return ""
    text = triefact_path.read_text()
    for match in SECTION_OPEN_RE.finditer(text):
        if match.group("symbol") != qname:
            continue
        close_idx = text.find(SECTION_CLOSE, match.end())
        if close_idx == -1:
            return ""
        body = text[match.end() : close_idx]
        if body.startswith("\n"):
            body = body[1:]
        if body.endswith("\n"):
            body = body[:-1]
        return body
    return ""


def pre_filter_batch(
    client: TrieClient,
    callee_pairs: list[tuple[str, str, list[dict], list[tuple[str, str]]]],
    *,
    batch_size: int = 8,
) -> list[tuple[str, str | None, str | None]]:

    if not callee_pairs:
        return []

    results: list[tuple[str, str | None, str | None]] = []

    for start in range(0, len(callee_pairs), batch_size):
        batch = callee_pairs[start : start + batch_size]
        sections: list[str] = []

        for idx, (callee_qn, old_prose, callers, notes_reasons) in enumerate(batch):
            tag = f"C{start + idx}"
            bullet_notes = (
                "\n".join(f"      - {n}  —  {r}" for n, r in notes_reasons)
                if notes_reasons
                else "      (no implementation notes)"
            )
            caller_lines = []
            for ci, c in enumerate(callers, 1):
                sig = c["signature"]
                role = (c["prose"] or c["one_liner"])[:200]
                caller_lines.append(f"      #{ci}. {sig}  —  {role}")
            caller_table = "\n".join(caller_lines) if caller_lines else "      (none)"
            sections.append(
                f"[{tag}] {callee_qn}\n"
                f"  Old prose: {old_prose[:300] if old_prose else '(empty)'}\n"
                f"  Implementation notes:\n{bullet_notes}\n"
                f"  Callers:\n{caller_table}\n"
            )

        request_body = "\n".join(sections)
        total_callers = sum(len(c) for _, _, c, _ in batch)
        prompt = BATCH_PRE_FILTER_PROMPT.format(callee_sections=request_body)

        result = client.run(
            BatchFilterOutput,
            system_prompt="",
            user_prompt=prompt,
            max_tokens=max(1024, total_callers * 64),
        )
        filter_out: BatchFilterOutput = result.output

        # Map decisions back to caller qnames via pairing context
        for idx, (_callee_qn, _old_prose, callers, _notes_reasons) in enumerate(batch):
            for _ci, caller in enumerate(callers):
                tag = f"C{start + idx}"
                for dec in filter_out.decisions:
                    if dec.caller_qname == caller["qname"]:
                        if dec.action.lower() == "skip":
                            continue
                        results.append((dec.caller_qname, dec.note, dec.reason or "cascade"))
                        break

    return results
