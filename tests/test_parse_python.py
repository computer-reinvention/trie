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
    """The module docstring feeds the file-level `description:` field; it
    should not also be emitted as a `__module__` symbol. And the SAMPLE
    fixture's residual after consuming defs/classes/constants is just the
    docstring + imports (both classified as noise), so the parser must
    not emit a `__module__` symbol either."""
    syms = extract_symbols(sample_file)
    qnames = {s.qualified_name for s in syms}
    # The SAMPLE residual is imports + the module docstring only; no
    # operational code at module level, so no `__module__` symbol fires.
    assert all(":__module__" not in q for q in qnames)


def test_module_level_constants_are_indexed(sample_file: Path):
    """The parser surfaces module-level `NAME = value` assignments as
    `kind='constant'` symbols. Captures dunders (`__version__`, `__all__`),
    config knobs (`DEFAULT_TIMEOUT = ...`), sentinel objects, and simple
    framework instantiations (`app = FastAPI()`)."""
    syms = {s.qualified_name: s for s in extract_symbols(sample_file)}
    assert "sample:CONSTANT" in syms
    assert syms["sample:CONSTANT"].kind == "constant"
    assert syms["sample:CONSTANT"].is_public is True
    # The signature line is the assignment statement itself, single-lined,
    # so the agent can triage the constant from one glance.
    assert "CONSTANT = 42" in syms["sample:CONSTANT"].signature


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


# ---------------------------------------------------------------------------
# Module-level constants and the synthetic `__module__` symbol
# ---------------------------------------------------------------------------


def test_dunder_constants_are_public(tmp_path: Path):
    """`__version__`, `__all__`, `__author__` start with an underscore but
    are part of a module's documented surface — `is_public` must be True.
    The parser uses a dunder-name check to distinguish module-API dunders
    from private (single-leading-underscore) identifiers."""
    f = tmp_path / "pkg.py"
    f.write_text('__version__ = "1.2.3"\n__all__ = ["foo", "bar"]\n_internal = 42\n')
    syms = {s.qualified_name: s for s in extract_symbols(f)}
    assert syms["pkg:__version__"].is_public is True
    assert syms["pkg:__all__"].is_public is True
    # Single leading underscore is still private.
    assert syms["pkg:_internal"].is_public is False


def test_annotated_constants_are_indexed(tmp_path: Path):
    """`NAME: T = value` (annotated assignment) should also produce a
    constant symbol — the type annotation doesn't change the fact that
    it's a module-level binding."""
    f = tmp_path / "annotated.py"
    f.write_text("from typing import Final\nMAX_RETRIES: Final[int] = 5\n")
    syms = {s.qualified_name: s for s in extract_symbols(f)}
    assert "annotated:MAX_RETRIES" in syms
    assert syms["annotated:MAX_RETRIES"].kind == "constant"


def test_tuple_unpacking_assignment_is_not_indexed(tmp_path: Path):
    """`X, Y = 1, 2` has multiple targets — the "symbol name" is
    ambiguous. The parser deliberately skips these to keep the symbol
    table clean. Single-identifier targets remain the only constant
    shape we recognise."""
    f = tmp_path / "tuples.py"
    f.write_text("X, Y = 1, 2\nZ = 3\n")
    syms = {s.qualified_name: s for s in extract_symbols(f)}
    # Z (single target) is in; X, Y (tuple unpacking) are not.
    assert "tuples:Z" in syms
    assert "tuples:X" not in syms
    assert "tuples:Y" not in syms


def test_module_symbol_emitted_for_setup_py_style_call(tmp_path: Path):
    """A file like `setup.py` has a few helper functions plus a big
    module-level `setup(...)` call. The synthetic `__module__` symbol
    captures the residual module-level code so the LLM-generated triefact
    can describe the file's import-time behaviour. Without this, the
    triefact would list the helpers but say nothing about what the file
    actually *does*."""
    f = tmp_path / "setup.py"
    f.write_text(
        "from setuptools import setup\n"
        "\n"
        "def get_version():\n"
        "    return '1.0.0'\n"
        "\n"
        "setup(name='thing', version=get_version())\n"
    )
    syms = {s.qualified_name: s for s in extract_symbols(f)}
    assert "setup:__module__" in syms
    mod = syms["setup:__module__"]
    assert mod.kind == "module"
    # The residual body must contain the `setup(...)` call — that's the
    # whole point of this symbol.
    assert "setup(" in mod.body_text


def test_module_symbol_not_emitted_for_pure_defs_with_imports(tmp_path: Path):
    """A file whose entire residual is imports + a module docstring +
    function/class definitions has no module-level behaviour worth a
    synthetic symbol. The parser must NOT emit `__module__` in this
    case — otherwise every Python file in the project would carry an
    extra triefact section with effectively no content."""
    f = tmp_path / "purefuncs.py"
    f.write_text(
        '"""Pure-functions module."""\n'
        "from typing import Any\n"
        "import os\n"
        "\n"
        "def helper(x):\n"
        "    return x + 1\n"
        "\n"
        "def other():\n"
        "    return 0\n"
    )
    syms = {s.qualified_name for s in extract_symbols(f)}
    assert "purefuncs:helper" in syms
    assert "purefuncs:other" in syms
    # No `__module__` — the file has no operational module-level code.
    assert all(":__module__" not in q for q in syms)


def test_method_has_parent_class(sample_file: Path):
    syms = _by_qname(extract_symbols(sample_file))
    assert syms["sample:Greeter.__init__"].parent_class == "Greeter"
    assert syms["sample:Greeter.hello"].parent_class == "Greeter"
    assert syms["sample:Greeter.make"].parent_class == "Greeter"


def test_function_has_no_parent_class(sample_file: Path):
    syms = _by_qname(extract_symbols(sample_file))
    assert syms["sample:public_fn"].parent_class is None


def test_class_has_no_parent_class(sample_file: Path):
    syms = _by_qname(extract_symbols(sample_file))
    assert syms["sample:Greeter"].parent_class is None


def test_decorator_captured_on_method(sample_file: Path):
    syms = _by_qname(extract_symbols(sample_file))
    assert "@classmethod" in syms["sample:Greeter.make"].decorators


def test_decorator_captured_on_class(sample_file: Path):
    syms = _by_qname(extract_symbols(sample_file))
    assert "@dataclass" in syms["sample:Decorated"].decorators


def test_undecorated_method_has_empty_decorators(sample_file: Path):
    syms = _by_qname(extract_symbols(sample_file))
    assert syms["sample:Greeter.hello"].decorators == ()


def test_property_decorator_captured(tmp_path: Path):
    f = tmp_path / "p.py"
    f.write_text("class Foo:\n    @property\n    def val(self) -> int:\n        return 1\n")
    syms = _by_qname(extract_symbols(f))
    assert "@property" in syms["p:Foo.val"].decorators
    assert syms["p:Foo.val"].parent_class == "Foo"


def test_symbols_sorted_by_start_line(tmp_path: Path):
    f = tmp_path / "order.py"
    f.write_text(
        "class A:\n"
        "    @overload\n"
        "    def go(self) -> int: ...\n"
        "    def go(self): return 1\n"
        "\n"
        "def standalone(): pass\n"
    )
    syms = extract_symbols(f)
    lines = [s.start_line for s in syms]
    assert lines == sorted(lines), f"Symbols not in source order: {lines}"


def test_module_symbol_emitted_for_if_main_block(tmp_path: Path):
    """An `if __name__ == '__main__':` block is module-level behaviour —
    code that runs when the file is executed directly. The parser
    captures it as part of the `__module__` symbol's residual body."""
    f = tmp_path / "script.py"
    f.write_text("def main():\n    print('hello')\n\nif __name__ == '__main__':\n    main()\n")
    syms = {s.qualified_name: s for s in extract_symbols(f)}
    assert "script:__module__" in syms
    assert "__main__" in syms["script:__module__"].body_text
