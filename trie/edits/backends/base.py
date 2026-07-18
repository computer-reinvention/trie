"""The pluggable per-symbol edit backend seam.

The pipeline talks ONLY to `SymbolEditBackend` — never to a concrete generator.
This is the plug-and-play seam from the cascade-editing plan (§2.7): the default
in-process LLM backend and a future opencode-instance-per-symbol backend are
interchangeable behind this one interface. Everything downstream (cascade, gates,
atomic apply, report, tool surface) consumes `EditResult` and never the backend.

A backend's `generate` MUST be a pure function of its `EditRequest`: no shared
mutable state, no reliance on call order. The apply pipeline fans `generate` out
across a thread pool, so two concurrent calls must not interfere.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Protocol, runtime_checkable


@dataclass(frozen=True)
class NeighbourCtx:
    """Signature + prose for one graph neighbour (callee or caller) of an edit target.

    Fed into generation context (§2.6) so the edit respects the contracts it
    depends on (callees) and how its result is consumed (callers). This is the
    success-rate mechanism: the dominant single-symbol failure mode is a wrong
    assumption about a neighbour, and this carries the neighbour's shape directly.
    """

    qname: str
    signature: str
    one_liner: str = ""


@dataclass(frozen=True)
class EditRequest:
    """Everything a backend needs to produce a new body + prose for one symbol.

    Backend-agnostic by construction: an in-process LLM call and a spawned
    opencode instance both render this into their own instruction shape.
    """

    qname: str
    op: str  # "modify" | "create" | "delete" | "rename"
    old_source: str  # "" for create
    old_prose: str
    merged_notes: list[str]  # the intent (from patches), already merged
    merged_reasons: list[str]
    session_note: str  # unifying batch intent ("" for single-symbol applies)
    callees: list[NeighbourCtx] = field(default_factory=list)
    callers: list[NeighbourCtx] = field(default_factory=list)
    file_path: str = ""
    new_name: str = ""  # populated only for op == "rename"


@dataclass(frozen=True)
class EditResult:
    """Everything the pipeline needs back from a backend for one symbol.

    `ok=False` with a populated `error` means a backend-level failure (the
    backend could not produce a candidate at all). A produced-but-broken
    candidate is still `ok=True`; the downstream compile/LSP gates judge
    well-formedness, never the backend.
    """

    qname: str
    new_source: str
    new_prose: str
    ok: bool = True
    error: str | None = None
    # Free-text module-level remarks: new imports / top-level changes the symbol
    # body needs to compile or work. The pipeline does not apply these; it
    # surfaces them in the ApplyReport for the agent to handle via force-edit.
    module_remarks: str = ""
    # New external package names the symbol introduced. trie does not install
    # them; they are deduped across the batch and reported for the agent to
    # install via shell.
    new_dependencies: tuple[str, ...] = ()


@runtime_checkable
class SymbolEditBackend(Protocol):
    """One method, pure per symbol. The only contract the pipeline depends on."""

    def generate(self, req: EditRequest) -> EditResult: ...
