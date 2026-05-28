from __future__ import annotations

from pathlib import Path

from trie.graph.store import Store
from trie.models import GenerationRequest, ModelClient

BATCH_PRE_FILTER_PROMPT = """\
For each changed callee below, determine which of its callers need source updates.
Base your decision on each caller's role/purpose and whether it depends on the
property, behavior, or implementation detail that changed.

{callee_sections}

Output format for every caller, one line per caller:
  [CALTAG:C{{CALLERNUM}}] SKIP
  [CALTAG:C{{CALLERNUM}}] NOTE: <note> | REASON: <reason>

SKIP means the caller needs no source changes — it does not depend on
what changed. Replace CALTAG with the callee's bracket tag and CALLERNUM
with the caller number (1-indexed).
"""

FIXUP_PROMPT = """\
The following source code was generated for symbol {qname} but has
diagnostics errors. Fix the errors and return corrected source + prose.

```python
{source}
```

Diagnostics:
{diagnostics}

Fix each issue. Preserve the existing structure. Output:

```python
<fixed source>
```

---PROSE---
<updated prose>"""

CALLEE_SECTION = """\
[{tag}] {qname}
  Old prose: {old_prose}
  Implementation notes:
{notes}

  Callers:
{caller_table}
"""

MERGE_PROMPT = """\
The following patch notes exist for this symbol. Some may contradict or supersede earlier ones. Return the final list of notes with superseded entries removed. Preserve chronological order for non-contradictory notes.

Existing notes:
{bullet_list}

Output the final list of bullet points, one per line. Empty list if nothing remains.
"""

INFER_SYSTEM_PROMPT = """\
You are updating a Python symbol based on implementation notes.
Output TWO sections: UPDATED_SOURCE and UPDATED_PROSE, separated by
the delimiter "---PROSE---".
"""


def _format_bullets(notes: list[str], reasons: list[str]) -> str:
    lines: list[str] = []
    for note, reason in zip(notes, reasons, strict=False):
        lines.append(f"<bullet> {note}  — {reason}")
    return "\n".join(lines)


def merge_notes(
    client: ModelClient,
    patches: list[dict],
) -> tuple[list[str], list[str]]:
    if not patches:
        return [], []

    notes = [p["note"] for p in patches]
    reasons = [p["reason"] for p in patches]
    bullet_list = _format_bullets(notes, reasons)

    req = GenerationRequest(
        system_prompt="",
        cached_context="",
        request=MERGE_PROMPT.format(bullet_list=bullet_list),
        max_tokens=512,
    )
    resp = client.generate(req)
    text = resp.text.strip()

    if not text:
        return [], []

    merged_notes: list[str] = []
    merged_reasons: list[str] = []
    for line in text.split("\n"):
        line = line.strip()
        if not line:
            continue
        if line.startswith("- "):
            line = line.removeprefix("- ").strip()
        elif line.startswith("* "):
            line = line.removeprefix("* ").strip()
        elif line.startswith("<bullet>"):
            line = line.removeprefix("<bullet>").strip()
        if " — " in line:
            note, _, reason = line.partition(" — ")
            merged_notes.append(note.strip())
            merged_reasons.append(reason.strip())
        else:
            merged_notes.append(line)
            merged_reasons.append("merged")
    return merged_notes, merged_reasons


def infer_source_and_prose(
    client: ModelClient,
    old_source: str,
    old_prose: str,
    notes: list[str],
    reasons: list[str],
) -> tuple[str, str]:
    bullet_list = _format_bullets(notes, reasons)

    request = f"""\
Old prose (the symbol's documented purpose):
{old_prose}

Implementation notes (what changed):
{bullet_list}

Old source:
```python
{old_source}
```

UPDATED_SOURCE: update the source to reflect the implementation notes.
Preserve the existing structure as much as possible.

UPDATED_PROSE: write the new triefact body for this symbol that reflects
both the old purpose and the implementation notes. Do NOT include bullet
points or implementation details — the prose is the high-level purpose.
The notes are consumed and discarded.

Output:

```python
<updated source>
```

---PROSE---
<updated prose>"""

    req = GenerationRequest(
        system_prompt=INFER_SYSTEM_PROMPT,
        cached_context="",
        request=request,
        max_tokens=2048,
    )
    resp = client.generate(req)
    text = resp.text.strip()

    # Parse on the delimiter
    delimiter = "---PROSE---"
    if delimiter not in text:
        raise ValueError(f"LLM response missing delimiter {delimiter!r}. Got:\n{text[:500]}...")

    before, after = text.split(delimiter, 1)

    # Extract source from the python code block
    new_source = before.strip()
    if new_source.startswith("```python"):
        new_source = new_source[len("```python") :].strip()
    if new_source.startswith("```"):
        new_source = new_source[3:].strip()
    if new_source.endswith("```"):
        new_source = new_source[:-3].strip()

    new_prose = after.strip()
    if new_prose.startswith("```"):
        new_prose = new_prose[3:].strip()
    if new_prose.endswith("```"):
        new_prose = new_prose[:-3].strip()

    return new_source, new_prose


def _build_caller_summaries(
    caller_qnames: list[str],
    store: Store,
    triefacts_root: Path,
) -> list[dict]:
    """Build caller summaries for the cascade pre-filter prompt.

    Returns [{qname, signature, one_liner, prose}, ...] with prose capped at 200 chars.
    Prose is read from the triefact file and cached per-call.
    """
    results: list[dict] = []
    for qn in caller_qnames:
        detail = store.get_symbol_detail(qn)
        if detail is None:
            continue
        prose = _read_prose(qn, detail.file_path, triefacts_root)[:200]
        results.append(
            {
                "qname": qn,
                "signature": detail.signature or "",
                "one_liner": detail.one_liner,
                "prose": prose,
            }
        )
    return results


def _read_prose(
    qname: str,
    file_path: str,
    triefacts_root: Path,
) -> str:
    """Read the triefact prose body for a symbol. Returns '' if not found."""
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
    client: ModelClient,
    callee_pairs: list[tuple[str, str, list[dict], list[tuple[str, str]]]],
    *,
    batch_size: int = 8,
) -> list[tuple[str, str | None, str | None]]:
    """Judge all callee→caller relationships in batches of `batch_size`.

    Input: list of (callee_qname, callee_old_prose, callers, notes_with_reasons).
      - callers:  [{qname, signature, one_liner, prose}, ...]
      - notes_with_reasons:  [(note, reason), ...]

    Returns flat list of (caller_qname, note, reason) for callers that
    need updates. Callers whose output was SKIP are omitted.
    """
    if not callee_pairs:
        return []

    results: list[tuple[str, str | None, str | None]] = []

    for start in range(0, len(callee_pairs), batch_size):
        batch = callee_pairs[start : start + batch_size]
        sections: list[str] = []
        total_callers: int = 0

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
                CALLEE_SECTION.format(
                    tag=tag,
                    qname=callee_qn,
                    old_prose=old_prose[:300] if old_prose else "(empty)",
                    notes=bullet_notes,
                    caller_table=caller_table,
                )
            )
            total_callers += len(callers)

        request_body = "\n".join(sections)
        request = BATCH_PRE_FILTER_PROMPT.format(callee_sections=request_body)

        req = GenerationRequest(
            system_prompt="",
            cached_context="",
            request=request,
            max_tokens=max(1024, total_callers * 64),
        )
        resp = client.generate(req)

        for line in resp.text.strip().split("\n"):
            line = line.strip()
            if not line:
                continue
            if not line.startswith("[") or "]" not in line:
                continue
            tag_and_rest = line[1:].split("]", 1)
            if len(tag_and_rest) != 2:
                continue
            callee_tag = tag_and_rest[0].strip()
            rest = tag_and_rest[1].strip()
            if not rest.startswith("C") or ":" not in rest:
                continue
            after_c = rest[1:].split(":", 1)
            if len(after_c) != 2:
                continue
            _num_str = after_c[0].strip()
            decision = after_c[1].strip()

            # Map tag back to callee to find caller qnames
            pair_idx = None
            for bi, (_cq, *_rest) in enumerate(batch):
                if f"C{start + bi}" == callee_tag or (
                    bi < len(batch) and callee_tag == f"C{start + bi}"
                ):
                    pair_idx = start + bi
                    break
            if pair_idx is None:
                continue

            _callee_qn, _old_prose, callers, _notes = callee_pairs[pair_idx]
            try:
                caller_num = int(_num_str) - 1
            except ValueError:
                continue
            if caller_num < 0 or caller_num >= len(callers):
                continue
            target_qn = callers[caller_num]["qname"]

            if decision.upper().startswith("SKIP"):
                continue
            elif decision.upper().startswith("NOTE:"):
                note_part = decision[len("NOTE:") :].strip()
                reason = "cascade"
                if " | REASON:" in note_part:
                    note_part, _, reason = note_part.partition(" | REASON:")
                    reason = reason.strip()
                results.append((target_qn, note_part.strip(), reason))

    return results
