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
    # Each additional backend is optional at import time: if its tree-sitter
    # grammar isn't installed, it's simply not registered (the language becomes
    # unindexable rather than crashing the whole registry).
    for module_name, class_name in (
        ("trie.parse.typescript", "TypeScriptBackend"),
        ("trie.parse.go", "GoBackend"),
        ("trie.parse.rust", "RustBackend"),
        ("trie.parse.c", "CBackend"),
        ("trie.parse.lua", "LuaBackend"),
    ):
        try:
            module = __import__(module_name, fromlist=[class_name])
            backends.append(getattr(module, class_name)())
        except ImportError:
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


def resolve_create_target(source_root: Path, qname: str) -> str:
    """Map a new-symbol qname to its source file path (relative to source_root).

    The qname's module part is the file path minus extension. Probe the
    registered suffixes (longest first, e.g. `.d.ts` before `.ts`) for an
    existing file — the file the symbol should be added to. When none exists
    (true new-file creation), infer the language from a sibling source file in
    the target directory, else fall back to the first backend's default
    `source_suffix()`, else `.py`.
    """
    module = qname.split(":", 1)[0]
    for suf in source_suffixes():
        if (source_root / (module + suf)).is_file():
            return module + suf
    target_dir = (source_root / module).parent
    if target_dir.is_dir():
        for child in sorted(target_dir.iterdir()):
            if not child.is_file():
                continue
            sibling_backend = get_backend_for_file(child)
            if sibling_backend is not None:
                return module + sibling_backend.source_suffix()
    backends = all_backends()
    return module + (backends[0].source_suffix() if backends else ".py")


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
