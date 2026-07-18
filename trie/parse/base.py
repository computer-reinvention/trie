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
from typing import TYPE_CHECKING, Protocol, runtime_checkable

from trie.parse.types import FileData, Symbol

if TYPE_CHECKING:
    from trie.config import LspBackend


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

    def lsp_backends(self) -> list[LspBackend]:
        """Default diagnostic checkers for the edit pipeline (e.g. pyright, tsc).

        The configured `Edits.lsp_backends` is the fallback when this is empty.
        """
        ...

    def overlay_globs(self) -> tuple[str, ...]:
        """Globs for files hardlinked into the edit scratch tree so the checker
        sees the full import graph (e.g. ("*.py",) or ("*.ts", "*.tsx"))."""
        ...

    def overlay_extra_files(self) -> tuple[str, ...]:
        """Non-source config files the checker needs in the scratch tree, by
        basename (e.g. ("tsconfig.json", "package.json")). Empty for Python."""
        ...

    def system_prompt(self) -> str:
        """The language-tuned generator system prompt for triefact prose."""
        ...

    def edit_system_prompt(self) -> str:
        """The language-tuned system prompt for the EDIT pipeline.

        Distinct from `system_prompt()` (which documents prose): this instructs
        the model that it is editing THIS language's source and returning updated
        source + prose. Python's is the historical default; TypeScript's tells
        the model to emit idiomatic TS/TSX so the spliced result passes `tsc`.
        """
        ...

    def code_fence(self) -> str:
        """Markdown code-fence language tag for this backend (e.g. "python",
        "typescript"). Used when embedding source in edit prompts so the model
        is shown the right language."""
        ...

    def validate_syntax(self, source: str, *, file_path: Path) -> bool:
        """Cheap/authoritative syntax gate for a candidate spliced file.

        Returns True when `source` is well-formed for this language. Python uses
        the builtin `compile`; TypeScript runs `tsc --noEmit` on the candidate in
        an isolated scratch dir. `file_path` is the project-relative target path
        (its extension/name can matter, e.g. `.tsx`). Must never raise — on any
        internal error it should return True (degrade to "accept"; the LSP/tsc
        diagnostics pass remains the real gate)."""
        ...
