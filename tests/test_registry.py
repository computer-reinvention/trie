from __future__ import annotations

from pathlib import Path

import pytest

from trie.parse import registry
from trie.parse.base import LanguageBackend

FIXTURE_PY = Path(__file__).parent / "fixtures" / "tiny_repo"
FIXTURE_TS = Path(__file__).parent / "fixtures" / "tiny_ts_repo"


def test_python_and_typescript_registered():
    names = {b.name for b in registry.all_backends()}
    assert "python" in names
    assert "typescript" in names


def test_get_backend_by_name():
    assert registry.get_backend("python").name == "python"
    assert registry.get_backend("typescript").name == "typescript"
    assert registry.get_backend("cobol") is None


def test_extension_dispatch():
    assert registry.get_backend_for_file("a.py").name == "python"
    assert registry.get_backend_for_file("a.ts").name == "typescript"
    assert registry.get_backend_for_file("a.tsx").name == "typescript"
    assert registry.get_backend_for_file("a.d.ts").name == "typescript"
    assert registry.get_backend_for_file("a.txt") is None


def test_dts_wins_over_ts():
    # Longest-suffix-first: a .d.ts file must route via the .d.ts mapping, not .ts.
    b = registry.get_backend_for_file("foo/bar.d.ts")
    assert b is not None and b.name == "typescript"


def test_source_suffixes_longest_first():
    suffixes = registry.source_suffixes()
    assert ".d.ts" in suffixes
    assert ".ts" in suffixes
    # .d.ts must come before .ts so the longest match wins.
    assert suffixes.index(".d.ts") < suffixes.index(".ts")


def test_is_indexable():
    assert registry.is_indexable("x.py")
    assert registry.is_indexable("x.ts")
    assert not registry.is_indexable("x.md")


def test_backends_satisfy_protocol():
    for b in registry.all_backends():
        assert isinstance(b, LanguageBackend)


def test_dispatch_extract_symbols_python():
    syms = registry.extract_symbols(FIXTURE_PY / "calculator.py", source_root=FIXTURE_PY)
    assert any(s.kind == "function" for s in syms)


def test_dispatch_extract_symbols_typescript():
    syms = registry.extract_symbols(FIXTURE_TS / "src" / "util.ts", source_root=FIXTURE_TS)
    assert any(s.qualified_name == "src/util:double" for s in syms)


def test_dispatch_rejects_unknown_extension():
    with pytest.raises(ValueError):
        registry.extract_symbols(Path("a.txt"))
