"""Concrete `ReferenceResolver` implementations.

Every language uses the same generic `LspResolver` (`lsp_resolver.py`), driving
a real language server over LSP to fill tree-sitter's method-dispatch gap. The
per-language wiring — server command, LSP languageId, and the tree-sitter
member-call-site extractor — lives in `specs.py`. Adding a language is a spec
plus a `backend.resolver()` that returns `LspResolver(spec)`; no new resolver
class is needed.
"""

from __future__ import annotations
