from __future__ import annotations

from trie.models import GenerationRequest, ModelClient

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
