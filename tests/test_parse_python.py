from __future__ import annotations

from pathlib import Path

import pytest

from trie.parse.python import Symbol, extract_symbols

SAMPLE = '''\
"""Module docstring should be ignored as a symbol."""

import os
from typing import Iterable

CONSTANT = 42  # not a tracked symbol in v0.1


def public_fn(x: int, y: int = 0) -> int:
    """Adds two ints."""
    return x + y


def _private_fn():
    return None


@staticmethod
def decorated_fn(name: str) -> str:
    return name


class Greeter:
    """Says hi."""

    DEFAULT_NAME: str = "world"

    def __init__(self, name: str = "world") -> None:
        self.name = name

    @classmethod
    def make(cls, name: str) -> "Greeter":
        return cls(name)

    def hello(self) -> str:
        return f"hello, {self.name}"

    def _shout(self) -> str:
        return self.hello().upper()


@dataclass
class Decorated:
    x: int

    def thing(self) -> int:
        return self.x
'''


@pytest.fixture
def sample_file(tmp_path: Path) -> Path:
    p = tmp_path / "sample.py"
    p.write_text(SAMPLE)
    return p


def _by_qname(syms: list[Symbol]) -> dict[str, Symbol]:
    return {s.qualified_name: s for s in syms}


def test_extracts_top_level_functions(sample_file: Path):
    syms = _by_qname(extract_symbols(sample_file))
    assert "sample:public_fn" in syms
    assert syms["sample:public_fn"].kind == "function"
    assert syms["sample:public_fn"].is_public is True
    assert "Adds two ints." in (syms["sample:public_fn"].docstring or "")


def test_private_marked_correctly(sample_file: Path):
    syms = _by_qname(extract_symbols(sample_file))
    assert syms["sample:_private_fn"].is_public is False


def test_decorated_function_is_extracted(sample_file: Path):
    syms = _by_qname(extract_symbols(sample_file))
    assert "sample:decorated_fn" in syms


def test_class_and_methods(sample_file: Path):
    syms = _by_qname(extract_symbols(sample_file))
    assert syms["sample:Greeter"].kind == "class"
    assert syms["sample:Greeter.__init__"].kind == "method"
    assert syms["sample:Greeter.hello"].kind == "method"
    assert syms["sample:Greeter._shout"].is_public is False
    assert syms["sample:Greeter.make"].kind == "method"


def test_decorated_class_and_methods(sample_file: Path):
    syms = _by_qname(extract_symbols(sample_file))
    assert syms["sample:Decorated"].kind == "class"
    assert syms["sample:Decorated.thing"].kind == "method"


def test_methods_of_private_class_inherit_privacy(tmp_path: Path):
    f = tmp_path / "x.py"
    f.write_text(
        "class _Internal:\n"
        "    def helper(self):\n        return 1\n"
        "    def _double_private(self):\n        return 2\n\n\n"
        "class Public:\n"
        "    def visible(self):\n        return 1\n"
    )
    syms = _by_qname(extract_symbols(f))
    assert syms["x:_Internal"].is_public is False
    assert syms["x:_Internal.helper"].is_public is False  # parent private → private
    assert syms["x:_Internal._double_private"].is_public is False
    assert syms["x:Public"].is_public is True
    assert syms["x:Public.visible"].is_public is True


def test_module_docstring_is_not_a_symbol(sample_file: Path):
    syms = extract_symbols(sample_file)
    qnames = {s.qualified_name for s in syms}
    # No symbol should be the module docstring.
    assert all(":__module__" not in q for q in qnames)
    # Top-level CONSTANT and import statements aren't tracked either in v0.1.
    assert "sample:CONSTANT" not in qnames


def test_signature_includes_annotations_and_return_type(sample_file: Path):
    syms = _by_qname(extract_symbols(sample_file))
    sig = syms["sample:public_fn"].signature
    assert "def public_fn" in sig
    assert "-> int" in sig
    # Trailing colon should be stripped — we can re-add it when rendering.
    assert not sig.rstrip().endswith(":")


def test_body_normalized_hash_is_stable_across_whitespace(tmp_path: Path):
    a = tmp_path / "a.py"
    b = tmp_path / "b.py"
    a.write_text("def f(x):\n    return x + 1\n")
    b.write_text("def f(x):\n        return    x + 1\n\n")  # different whitespace
    sa = extract_symbols(a)[0]
    sb = extract_symbols(b)[0]
    assert sa.body_normalized_hash == sb.body_normalized_hash


def test_body_normalized_hash_ignores_comments(tmp_path: Path):
    a = tmp_path / "a.py"
    b = tmp_path / "b.py"
    a.write_text("def f(x):\n    return x + 1\n")
    b.write_text("def f(x):\n    # explanatory comment\n    return x + 1\n")
    sa = extract_symbols(a)[0]
    sb = extract_symbols(b)[0]
    assert sa.body_normalized_hash == sb.body_normalized_hash


def test_body_normalized_hash_changes_on_real_change(tmp_path: Path):
    a = tmp_path / "a.py"
    b = tmp_path / "b.py"
    a.write_text("def f(x):\n    return x + 1\n")
    b.write_text("def f(x):\n    return x + 2\n")
    sa = extract_symbols(a)[0]
    sb = extract_symbols(b)[0]
    assert sa.body_normalized_hash != sb.body_normalized_hash


def test_signature_hash_changes_on_signature_change(tmp_path: Path):
    a = tmp_path / "a.py"
    b = tmp_path / "b.py"
    a.write_text("def f(x: int) -> int:\n    return x\n")
    b.write_text("def f(x: int, y: int = 0) -> int:\n    return x\n")
    sa = extract_symbols(a)[0]
    sb = extract_symbols(b)[0]
    assert sa.signature_hash != sb.signature_hash


def test_qualified_name_uses_source_root(tmp_path: Path):
    pkg = tmp_path / "src" / "pkg"
    pkg.mkdir(parents=True)
    f = pkg / "mod.py"
    f.write_text("def foo():\n    pass\n")
    syms = extract_symbols(f, source_root=tmp_path)
    assert syms[0].qualified_name == "src/pkg/mod:foo"
    assert syms[0].file_path == "src/pkg/mod.py"


def test_line_numbers_are_one_indexed(sample_file: Path):
    syms = _by_qname(extract_symbols(sample_file))
    s = syms["sample:public_fn"]
    # Line 1 is the module docstring; public_fn starts at line 9 in SAMPLE.
    assert s.start_line >= 1
    assert s.end_line >= s.start_line


def test_typing_overloads_dedupe_to_implementation(tmp_path: Path):
    """typing.@overload creates multiple defs with the same qualified_name. Last
    (the actual implementation, per Python's overload rules) must win — otherwise
    the symbols table's UNIQUE constraint blows up on real codebases like httpx."""
    f = tmp_path / "client.py"
    f.write_text(
        "from typing import overload\n\n\n"
        "class Client:\n"
        "    @overload\n"
        "    def send(self, request: int) -> int: ...\n"
        "    @overload\n"
        "    def send(self, request: str) -> str: ...\n"
        "    def send(self, request):\n"
        "        return request\n"
    )
    syms = extract_symbols(f)
    by_qname = _by_qname(syms)
    # Exactly one entry for Client.send — the deduper kept the last one.
    sends = [s for s in syms if s.qualified_name == "client:Client.send"]
    assert len(sends) == 1
    # The implementation body (no ellipsis) is what survived.
    assert "..." not in sends[0].body_text
    assert "client:Client.send" in by_qname


def test_property_setter_pair_dedupes(tmp_path: Path):
    """@property + @x.setter both produce a method named `x`. They should not
    collide in the symbols table."""
    f = tmp_path / "thing.py"
    f.write_text(
        "class Thing:\n"
        "    @property\n"
        "    def name(self) -> str:\n"
        "        return self._name\n"
        "    @name.setter\n"
        "    def name(self, value: str) -> None:\n"
        "        self._name = value\n"
    )
    syms = extract_symbols(f)
    name_syms = [s for s in syms if s.qualified_name == "thing:Thing.name"]
    assert len(name_syms) == 1
