"""In-process LLM edit backend — the default `SymbolEditBackend`.

Wraps a `TrieClient` to generate one symbol's new source + prose from an
`EditRequest`, feeding callee/caller context (§2.6) into the prompt. This is the
backend that ships first; the opencode-instance backend (Phase 2) implements the
same `SymbolEditBackend` protocol and is selected via config without touching the
pipeline.
"""

from __future__ import annotations

from trie.models import SymbolEdit, TrieClient

from .base import EditRequest, EditResult

INFER_SYSTEM_PROMPT = """\
You update Python source code based on implementation notes and return the updated \
source and an updated prose summary of the symbol's purpose. The prose should \
describe what the symbol does at a high level — do not include implementation \
notes or bullet points. Respect the signatures and behaviour of the callees this \
symbol depends on and the way its callers consume its result."""


def _format_bullets(notes: list[str], reasons: list[str]) -> str:
    lines: list[str] = []
    for note, reason in zip(notes, reasons, strict=False):
        lines.append(f"- {note}  — {reason}")
    return "\n".join(lines)


def _format_neighbours(label: str, neighbours: list) -> str:
    if not neighbours:
        return f"{label}: (none)"
    lines = [f"{label}:"]
    for n in neighbours:
        sig = n.signature or n.qname
        role = f"  — {n.one_liner}" if n.one_liner else ""
        lines.append(f"  - {sig}{role}")
    return "\n".join(lines)


def build_user_prompt(req: EditRequest) -> str:
    """Render an EditRequest into the user prompt for the LLM.

    Public so the opencode backend (Phase 2) can reuse the exact same instruction
    rendering — the only delta between backends is where the text is sent.
    """
    bullet_list = _format_bullets(req.merged_notes, req.merged_reasons)
    callees = _format_neighbours("Callees (contracts this symbol depends on)", req.callees)
    callers = _format_neighbours("Callers (how this symbol's result is used)", req.callers)
    intent = f"Overall change intent: {req.session_note}\n\n" if req.session_note else ""
    create_clause = ""
    if req.op == "create":
        create_clause = (
            f"\nThis is a NEW symbol `{req.qname}` to be created. "
            "Write its complete source from the notes below.\n"
        )

    return f"""\
{intent}Symbol: {req.qname}
{create_clause}
{callees}

{callers}

Old prose (the symbol's documented purpose):
{req.old_prose or "(none)"}

Implementation notes (what to change):
{bullet_list or "(none)"}

Old source:
```python
{req.old_source}
```"""


class InProcessLLMBackend:
    """Default backend: one LLM call per symbol via a shared `TrieClient`.

    Stateless apart from the client handle, so the apply pipeline can fan
    `generate` out across its thread pool safely.
    """

    def __init__(self, client: TrieClient, *, max_tokens: int = 4096) -> None:
        self._client = client
        self._max_tokens = max_tokens

    def generate(self, req: EditRequest) -> EditResult:
        try:
            result = self._client.run(
                SymbolEdit,
                system_prompt=INFER_SYSTEM_PROMPT,
                user_prompt=build_user_prompt(req),
                max_tokens=self._max_tokens,
            )
            edit: SymbolEdit = result.output
            return EditResult(
                qname=req.qname,
                new_source=edit.source,
                new_prose=edit.prose,
                ok=True,
            )
        except Exception as exc:  # backend-level failure → ok=False
            return EditResult(
                qname=req.qname,
                new_source="",
                new_prose="",
                ok=False,
                error=str(exc),
            )
