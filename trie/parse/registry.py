"""Language-backend registry — dispatch by file extension.

The engine's parse call sites go through the free functions here instead of
importing a specific language module. `get_backend_for_file` picks the backend
that owns a path's extension; `extract_file_data` / `extract_symbols` are
drop-in replacements for the old direct imports.

Extension matching is longest-suffix-first so a compound suffix like `.d.ts`
wins over `.ts`. `source_suffixes()` exposes the same ordering so triefact↔
source mapping can recover the right source extension for a given `.md`.

See docs/core/multi-language-backend-prd.md §3.3.
"""

from __future__ import annotations

from pathlib import Path

from trie.parse.base import LanguageBackend
from trie.parse.python import PythonBackend
from trie.parse.types import FileData, Symbol


def _build_registry() -> list[LanguageBackend]:
    backends: list[LanguageBackend] = [PythonBackend()]
    # TypeScript registers here in Phase 3 once trie/parse/typescript.py exists:
    #   from trie.parse.typescript import TypeScriptBackend
    #   backends.append(TypeScriptBackend())
    try:
        from trie.parse.typescript import TypeScriptBackend

        backends.append(TypeScriptBackend())
    except ImportError:
        # TypeScript backend / its tree-sitter grammar not installed yet.
        pass
    return backends


_BACKENDS: list[LanguageBackend] = _build_registry()

# Map every owned extension to its backend, longest suffix first so compound
# suffixes (".d.ts") resolve before their base (".ts").
_BY_EXTENSION: list[tuple[str, LanguageBackend]] = sorted(
    ((ext, b) for b in _BACKENDS for ext in b.extensions),
    key=lambda pair: len(pair[0]),
    reverse=True,
)


def all_backends() -> tuple[LanguageBackend, ...]:
    """Every registered backend."""
    return tuple(_BACKENDS)


def get_backend(name: str) -> LanguageBackend | None:
    """The backend registered under `name` (e.g. "python"), or None."""
    for b in _BACKENDS:
        if b.name == name:
            return b
    return None


def get_backend_for_file(path: str | Path) -> LanguageBackend | None:
    """The backend owning `path`'s extension, or None if no backend claims it.

    Matches the longest registered suffix so `foo.d.ts` resolves to the
    TypeScript backend via `.d.ts`, not `.ts`.
    """
    name = str(path)
    for ext, backend in _BY_EXTENSION:
        if name.endswith(ext):
            return backend
    return None


def source_suffixes() -> tuple[str, ...]:
    """All registered source suffixes, longest first.

    Triefact↔source mapping probes these in order to recover the source file
    for a `.md` triefact (e.g. `foo.d.md` → `foo.d.ts` before `foo.ts`).
    """
    return tuple(ext for ext, _ in _BY_EXTENSION)


def is_indexable(path: str | Path) -> bool:
    """True if some backend claims this path's extension."""
    return get_backend_for_file(path) is not None


def extract_file_data(
    file_path: Path,
    source_root: Path | None = None,
    *,
    source_text: str | None = None,
) -> FileData:
    """Dispatch parse-to-FileData to the owning backend.

    Raises ValueError if no backend claims the file's extension — callers that
    discover files via scope globs should only pass indexable paths.
    """
    backend = get_backend_for_file(file_path)
    if backend is None:
        raise ValueError(f"No language backend for file: {file_path}")
    return backend.extract_file_data(file_path, source_root, source_text=source_text)


def extract_symbols(
    file_path: Path,
    source_root: Path | None = None,
    *,
    source_text: str | None = None,
) -> list[Symbol]:
    """Dispatch parse-to-symbols to the owning backend."""
    backend = get_backend_for_file(file_path)
    if backend is None:
        raise ValueError(f"No language backend for file: {file_path}")
    return backend.extract_symbols(file_path, source_root, source_text=source_text)
