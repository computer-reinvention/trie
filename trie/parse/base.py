"""The language-backend contract.

A `LanguageBackend` is everything the engine needs to treat a family of source
files (by extension) as indexable code: how to parse symbols and references, how
to map between qnames and file paths, which checkers validate an edit, and what
prose prompt documents its symbols.

Everything downstream of parsing (the graph store, cascade, triefact format,
line-range splicing) is already language-neutral and operates on the
`trie.parse.types` value types — so a backend only has to produce those types
and answer a handful of mapping questions.

The registry (`trie.parse.registry`) dispatches to a backend by file extension.
`PythonBackend` is the reference implementation; `TypeScriptBackend` is the
first non-Python one. See docs/core/multi-language-backend-prd.md §3.
"""

from __future__ import annotations

from pathlib import Path
from typing import Protocol, runtime_checkable

from trie.parse.types import FileData, Symbol


@runtime_checkable
class LanguageBackend(Protocol):
    """What every language plugin must provide.

    Implementations are stateless and cheap to instantiate; the registry holds
    a single instance per language.
    """

    #: Human/config name, e.g. "python", "typescript".
    name: str

    #: Source extensions this backend owns, e.g. (".py",) or (".ts", ".tsx", ".d.ts").
    #: Longer/more-specific suffixes (".d.ts") must precede their shorter
    #: relatives (".ts") so suffix matching is unambiguous.
    extensions: tuple[str, ...]

    def extract_file_data(
        self,
        file_path: Path,
        source_root: Path | None = None,
        *,
        source_text: str | None = None,
    ) -> FileData:
        """Parse one file into symbols + outbound references (single parse)."""
        ...

    def extract_symbols(
        self,
        file_path: Path,
        source_root: Path | None = None,
        *,
        source_text: str | None = None,
    ) -> list[Symbol]:
        """Parse one file into its symbols only (no reference resolution)."""
        ...

    def source_suffix(self) -> str:
        """The canonical source suffix for newly created files of this language.

        Used to reconstruct a file path from a qname (create-symbol). For
        TypeScript this is ".ts"; `.tsx`/`.d.ts` are recognised on read but new
        symbols are created in plain ".ts".
        """
        ...

    def system_prompt(self) -> str:
        """The language-tuned generator system prompt for triefact prose."""
        ...
