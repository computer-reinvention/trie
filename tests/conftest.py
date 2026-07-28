"""Shared pytest configuration.

The LSP-backed reference resolver spawns a language server per source root and
adds real latency to any test that scans a project. The vast majority of the
suite asserts on tree-sitter's structural extraction and does not need
type-aware method edges, so the resolver is disabled by default for the whole
session (keeping CI fast and free of a language-server dependency). Tests that
specifically exercise the resolver re-enable it via the `enable_resolver`
fixture.
"""

from __future__ import annotations

import os

import pytest


def pytest_configure(config: pytest.Config) -> None:
    # Default the whole session to tree-sitter-only extraction unless a test
    # explicitly opts into the resolver.
    os.environ.setdefault("TRIE_DISABLE_RESOLVER", "1")


@pytest.fixture
def enable_resolver(monkeypatch: pytest.MonkeyPatch):
    """Re-enable the LSP resolver for a single test."""
    monkeypatch.delenv("TRIE_DISABLE_RESOLVER", raising=False)
