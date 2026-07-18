"""In-process LLM edit backend — the default `SymbolEditBackend`.

Wraps a `TrieClient` to generate one symbol's new source + prose from an
`EditRequest`, feeding callee/caller context (§2.6) into the prompt. This is the
backend that ships first; the opencode-instance backend (Phase 2) implements the
same `SymbolEditBackend` protocol and is selected via config without touching the
pipeline.
"""

from __future__ import annotations

from pathlib import Path

from trie.edits import textgen
from trie.models import TrieClient

from .base import EditRequest, EditResult

# Fallback prompt (Python-worded) used only when a request carries no file_path
# from which to resolve a language backend. The neighbour-contract sentence is
# appended to whichever backend's edit_system_prompt() applies.
_NEIGHBOUR_CLAUSE = (
    " Respect the signatures and behaviour of the callees this symbol depends on "
    "and the way its callers consume its result."
)
INFER_SYSTEM_PROMPT = (
    "You update Python source code based on implementation notes and return the "
    "updated source and an updated prose summary of the symbol's purpose. The prose "
    "should describe what the symbol does at a high level — do not include "
    "implementation notes or bullet points." + _NEIGHBOUR_CLAUSE
)


def _backend_for(file_path: str | None):
    """Resolve the language backend for an edit request's file, or None."""
    if not file_path:
        return None
    from trie.parse import registry

    return registry.get_backend_for_file(Path(file_path))


def _system_prompt_for(file_path: str | None) -> str:
    backend = _backend_for(file_path)
    if backend is not None:
        return backend.edit_system_prompt() + _NEIGHBOUR_CLAUSE
    return INFER_SYSTEM_PROMPT


def _fence_for(file_path: str | None) -> str:
    backend = _backend_for(file_path)
    return backend.code_fence() if backend is not None else "python"


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

    fence = _fence_for(req.file_path)
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
```{fence}
{req.old_source}
```

{textgen.code_block_instructions(fence)}

{textgen.single_prose_instructions()}

{textgen.module_remarks_instructions()}

{textgen.new_deps_instructions()}"""


class InProcessLLMBackend:
    """Default backend: one LLM call per symbol via a shared `TrieClient`.

    Stateless apart from the client handle, so the apply pipeline can fan
    `generate` out across its thread pool safely.
    """

    def __init__(
        self, client: TrieClient, *, max_tokens: int = 16384, output_retries: int = 3
    ) -> None:
        self._client = client
        self._max_tokens = max_tokens
        self._output_retries = output_retries

    def generate(self, req: EditRequest) -> EditResult:
        try:
            # Plaintext code-gen: ask for a fenced block + delimited prose and
            # parse it, rather than forcing the body through a pydantic schema
            # (which malforms/truncates on large symbols and burns output
            # retries into UnexpectedModelBehavior). pydantic-ai is the API
            # client only here; there is no schema that can fail to validate.
            result = self._client.run_text(
                system_prompt=_system_prompt_for(req.file_path),
                user_prompt=build_user_prompt(req),
                max_tokens=self._max_tokens,
            )
            text = result.output
            return EditResult(
                qname=req.qname,
                new_source=textgen.parse_code(text),
                new_prose=textgen.parse_single_prose(text),
                ok=True,
                module_remarks=textgen.parse_module_remarks(text),
                new_dependencies=tuple(textgen.parse_new_deps(text)),
            )
        except Exception as exc:  # backend-level failure → ok=False
            return EditResult(
                qname=req.qname,
                new_source="",
                new_prose="",
                ok=False,
                error=str(exc),
            )
