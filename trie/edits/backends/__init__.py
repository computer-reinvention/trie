"""Pluggable per-symbol edit backends.

`make_backend` is the single selection point. Adding a backend is one class plus
one branch here — no other code in the pipeline branches on the backend.
"""

from __future__ import annotations

from trie.config import Config
from trie.models import TrieClient, make_client

from .base import EditRequest, EditResult, NeighbourCtx, SymbolEditBackend
from .fake import FakeBackend
from .llm import InProcessLLMBackend

__all__ = [
    "EditRequest",
    "EditResult",
    "FakeBackend",
    "InProcessLLMBackend",
    "NeighbourCtx",
    "SymbolEditBackend",
    "make_backend",
]


def make_backend(
    config: Config,
    *,
    backend: str | None = None,
    client: TrieClient | None = None,
    model: str | None = None,
) -> SymbolEditBackend:
    """Construct the configured edit backend.

    `backend` (run override) wins over `config.edits.backend`. `client` lets a
    caller inject a pre-built TrieClient (so the apply pipeline reuses one client
    for the whole run); otherwise one is built from `model` or `config.models.edits`.
    """
    name = (backend or config.edits.backend or "llm").lower()

    if name == "llm":
        if client is None:
            client = make_client(model or config.models.edits, sync_cfg=config.sync)
        return InProcessLLMBackend(client)

    if name == "opencode":
        # Phase 2: OpencodeInstanceBackend implements the same protocol. Until it
        # lands, fail loudly rather than silently degrading to the LLM backend.
        raise NotImplementedError(
            "opencode backend is Phase 2; set [edits].backend = 'llm' for now."
        )

    raise ValueError(f"unknown edit backend {name!r}; expected 'llm' or 'opencode'.")
