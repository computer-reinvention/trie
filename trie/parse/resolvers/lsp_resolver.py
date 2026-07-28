"""Generic, language-agnostic `ReferenceResolver` backed by an LSP server.

This is the single resolver every language reuses. Tree-sitter does the fast
structural pass; this resolver supplements it with the type-dependent edges
tree-sitter can't derive — method/member dispatch through a value
(`obj.method()`, `self.helper()`, `this.helper()`). It works by driving a real
language server (`pyright-langserver`, `typescript-language-server`, later
`gopls`, `rust-analyzer`, …) over LSP: open the file, ask
`textDocument/definition` at each call site, map the definition location back to
a project symbol qname.

A language plugs in by constructing an `LspResolver` with an `LspServerSpec`:
the server command, the LSP `languageId`, and a small tree-sitter callback that
yields the member-call sites for that grammar. Everything else — process
lifecycle, JSON-RPC, definition→qname mapping — is shared here.

Robustness contract (per `ReferenceResolver`): if the server binary is missing
or any analysis step fails, `resolve_file` returns `[]` and the backend falls
back to tree-sitter-only. A resolver is only *offered* by a backend when its
server is discoverable, so the common "no server installed" case degrades to
today's behaviour rather than erroring.
"""

from __future__ import annotations

import shutil
from collections.abc import Callable, Iterable
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import url2pathname

from trie.parse.lsp_client import LspClient, LspError
from trie.parse.types import Reference, Symbol

# A call site the resolver should try to resolve: the 0-based (line, character)
# of the *member name* being called, e.g. the `helper` in `self.helper()`.
CallSite = tuple[int, int]

# Given a file's raw bytes, yield the member-call sites to resolve. This is the
# only language-specific input to the otherwise-generic resolver.
CallSiteExtractor = Callable[[bytes], Iterable[CallSite]]


@dataclass(frozen=True)
class LspServerSpec:
    """Everything needed to drive one language's LSP server for resolution."""

    name: str  # resolver identity for telemetry, e.g. "pyright", "tsserver"
    command: list[str]  # argv to spawn the server in stdio mode
    language_id: str  # LSP languageId, e.g. "python", "typescript"
    call_sites: CallSiteExtractor  # member-call sites for this grammar

    def is_available(self) -> bool:
        """True if the server binary is on PATH (so a backend can offer it)."""
        return bool(self.command) and shutil.which(self.command[0]) is not None


class LspResolver:
    """`ReferenceResolver` that resolves member calls via a language server."""

    def __init__(self, spec: LspServerSpec) -> None:
        self._spec = spec
        # One client per source root, reused across files in a scan. Language
        # servers pay a workspace-warmup cost on first open; caching amortises
        # it. Keyed by resolved root path string.
        self._clients: dict[str, LspClient] = {}

    @property
    def name(self) -> str:
        return self._spec.name

    def resolve_file(
        self,
        file_path: Path,
        source_root: Path,
        symbols: list[Symbol],
    ) -> list[Reference]:
        try:
            return self._resolve_file_inner(file_path, source_root, symbols)
        except LspError:
            return []
        except Exception:
            return []

    def _client_for(self, source_root: Path) -> LspClient:
        key = str(source_root.resolve())
        client = self._clients.get(key)
        if client is None:
            client = LspClient(self._spec.command, source_root)
            client.start()
            self._clients[key] = client
        return client

    def _resolve_file_inner(
        self,
        file_path: Path,
        source_root: Path,
        symbols: list[Symbol],
    ) -> list[Reference]:
        source = file_path.read_bytes()
        sites = list(self._spec.call_sites(source))
        if not sites:
            return []

        own_by_line = _symbols_by_line(symbols)
        client = self._client_for(source_root)
        client.did_open(file_path, self._spec.language_id, source.decode("utf-8", "replace"))

        target_index: dict[Path, dict[int, str]] = {}
        references: list[Reference] = []
        seen: set[tuple[str, str]] = set()

        for line, char in sites:
            src_qname = own_by_line.get(line + 1)  # symbols are 1-based
            if src_qname is None:
                continue
            locations = client.definition(file_path, line, char)
            for loc in locations:
                def_path = _uri_to_path(loc.get("uri", ""))
                if def_path is None:
                    continue
                def_line = loc.get("range", {}).get("start", {}).get("line")
                if def_line is None:
                    continue
                tgt = _target_qname(def_path, def_line + 1, source_root, target_index)
                if tgt is None or tgt == src_qname:
                    continue
                key = (src_qname, tgt)
                if key in seen:
                    continue
                seen.add(key)
                references.append(Reference(src_qname=src_qname, target_qname=tgt, kind="calls"))
                break

        return references

    def close(self) -> None:
        """Shut down all cached language-server processes."""
        for client in self._clients.values():
            client.shutdown()
        self._clients.clear()


def _symbols_by_line(symbols: list[Symbol]) -> dict[int, str]:
    """Map each 1-based line to the innermost def/class/method covering it."""
    by_line: dict[int, str] = {}
    ordered = sorted(
        (s for s in symbols if s.kind in ("function", "method", "class")),
        key=lambda s: s.end_line - s.start_line,
        reverse=True,
    )
    for s in ordered:
        for ln in range(s.start_line, s.end_line + 1):
            by_line[ln] = s.qualified_name
    return by_line


def _target_qname(
    def_path: Path,
    def_line: int,  # 1-based
    source_root: Path,
    cache: dict[Path, dict[int, str]],
) -> str | None:
    """Map an LSP definition location to a project symbol qname, or None.

    Off-project definitions (stdlib, node_modules, .venv) resolve outside the
    source root and yield no edge — the resolver stays project-internal.
    """
    resolved = def_path.resolve()
    root = source_root.resolve()
    if not resolved.is_relative_to(root):
        return None
    idx = cache.get(resolved)
    if idx is None:
        idx = _file_symbols_by_line(resolved, root)
        cache[resolved] = idx
    return idx.get(def_line)


def _file_symbols_by_line(abs_path: Path, source_root: Path) -> dict[int, str]:
    """Index a target file's symbols by their 1-based start line → qname.

    LSP reports a definition at the symbol's own declaration line, which trie
    records as `Symbol.start_line`, so start-line keying is the robust,
    name-collision-free mapping.
    """
    from trie.parse import registry

    try:
        syms = registry.extract_symbols(abs_path, source_root=source_root)
    except Exception:
        return {}
    return {s.start_line: s.qualified_name for s in syms}


def _uri_to_path(uri: str) -> Path | None:
    if not uri.startswith("file:"):
        return None
    parsed = urlparse(uri)
    return Path(url2pathname(parsed.path))


__all__ = ["CallSite", "CallSiteExtractor", "LspResolver", "LspServerSpec"]
