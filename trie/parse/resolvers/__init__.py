"""Concrete `ReferenceResolver` implementations, one per analysis engine.

Each resolver pairs with a tree-sitter `LanguageBackend` to fill the method-call
gap tree-sitter leaves. `JediResolver` is the Python reference implementation
(in-process, static type inference). A future generic LSP-client resolver slots
in here for languages served by a language server.
"""

from __future__ import annotations
