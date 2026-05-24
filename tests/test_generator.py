from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pytest

from trie.models import GenerationRequest, GenerationResponse, make_client
from trie.parse.python import extract_symbols
from trie.sync.generator import (
    DIFF_AWARE_RUBRIC,
    SYSTEM_PROMPT,
    FileGenerationContext,
    _build_diff_aware_request,
    _build_request,
    _symbol_context_clause,
    _symbol_source,
    build_cached_context,
    generate_section,
)


@dataclass
class FakeClient:
    """Records the request, returns a canned response. Replaces a real model client."""

    response_text: str = "## `foo()`\n\nA function."
    model_id: str = "fake/test"
    last_request: GenerationRequest | None = None

    def generate(self, req: GenerationRequest) -> GenerationResponse:
        self.last_request = req
        return GenerationResponse(
            text=self.response_text,
            input_tokens=100,
            output_tokens=20,
            cache_creation_input_tokens=80,
            cache_read_input_tokens=0,
        )


def test_cached_context_includes_source_and_filename():
    ctx = FileGenerationContext(file_path="src/foo.py", source_text="def foo():\n    pass\n")
    out = build_cached_context(ctx)
    assert "src/foo.py" in out
    assert "def foo()" in out
    assert "```python" in out


def test_request_names_symbol_and_lines(tmp_path: Path):
    f = tmp_path / "foo.py"
    f.write_text("def foo(x: int) -> int:\n    return x\n")
    sym = extract_symbols(f)[0]
    out = _build_request(sym)
    assert sym.qualified_name in out
    assert "function" in out
    assert "lines" in out
    # Cold-write request now includes the symbol source block directly.
    assert "<source>" in out
    assert "def foo" in out


def test_generate_section_passes_correct_prompt(tmp_path: Path):
    f = tmp_path / "foo.py"
    f.write_text("def foo(x: int) -> int:\n    return x\n")
    sym = extract_symbols(f)[0]
    ctx = FileGenerationContext(file_path="foo.py", source_text=f.read_text())
    client = FakeClient()

    sec = generate_section(symbol=sym, file_ctx=ctx, client=client)

    assert client.last_request is not None
    assert client.last_request.system_prompt == SYSTEM_PROMPT
    assert "def foo" in client.last_request.cached_context
    assert sym.qualified_name in client.last_request.request
    assert sec.qualified_name == sym.qualified_name
    assert sec.body.startswith("## ")
    assert sec.body == "## `foo()`\n\nA function."  # stripped of surrounding whitespace
    assert sec.cache_creation_input_tokens == 80


def test_generate_section_strips_surrounding_whitespace(tmp_path: Path):
    f = tmp_path / "foo.py"
    f.write_text("def foo():\n    pass\n")
    sym = extract_symbols(f)[0]
    ctx = FileGenerationContext(file_path="foo.py", source_text=f.read_text())
    client = FakeClient(response_text="\n\n## `foo()`\n\nstuff\n\n")

    sec = generate_section(symbol=sym, file_ctx=ctx, client=client)
    assert sec.body == "## `foo()`\n\nstuff"


# --- diff-aware mode ---


def test_generate_section_defaults_to_cold_mode(tmp_path: Path):
    """When neither previous_source nor previous_prose is supplied, mode == 'cold'."""
    f = tmp_path / "foo.py"
    f.write_text("def foo():\n    return 1\n")
    sym = extract_symbols(f)[0]
    ctx = FileGenerationContext(file_path="foo.py", source_text=f.read_text())
    client = FakeClient()

    sec = generate_section(symbol=sym, file_ctx=ctx, client=client)

    assert sec.mode == "cold"
    # Cold-write request does NOT contain the rubric or diff-aware labelled blocks.
    assert client.last_request is not None
    assert DIFF_AWARE_RUBRIC not in client.last_request.request
    assert "<previous_source>" not in client.last_request.request
    # But it DOES contain the symbol source block.
    assert "<source>" in client.last_request.request


def test_generate_section_takes_diff_aware_when_both_previous_provided(tmp_path: Path):
    """previous_source + previous_prose both non-None → diff-aware request shape."""
    f = tmp_path / "foo.py"
    f.write_text("def foo():\n    return 2\n")
    sym = extract_symbols(f)[0]
    ctx = FileGenerationContext(file_path="foo.py", source_text=f.read_text())
    client = FakeClient()

    sec = generate_section(
        symbol=sym,
        file_ctx=ctx,
        client=client,
        previous_source="def foo():\n    return 1\n",
        previous_prose="## `foo()`\n\nReturn 1.",
    )

    assert sec.mode == "diff_aware"
    assert client.last_request is not None
    req = client.last_request.request
    # Both labelled blocks appear, rubric is included, both previous strings are present.
    assert "<previous_source>" in req
    assert "<previous_prose>" in req
    assert "<current_source>" in req
    assert "return 1" in req
    assert "return 2" in req
    assert "Return 1." in req


def test_generate_section_partial_previous_falls_back_to_cold(tmp_path: Path):
    """Only one of previous_source / previous_prose → cold mode, both blocks suppressed."""
    f = tmp_path / "foo.py"
    f.write_text("def foo():\n    return 2\n")
    sym = extract_symbols(f)[0]
    ctx = FileGenerationContext(file_path="foo.py", source_text=f.read_text())

    client1 = FakeClient()
    sec1 = generate_section(
        symbol=sym, file_ctx=ctx, client=client1, previous_source="def foo():\n    return 1\n"
    )
    assert sec1.mode == "cold"

    client2 = FakeClient()
    sec2 = generate_section(
        symbol=sym, file_ctx=ctx, client=client2, previous_prose="## `foo()`\n\nReturn 1."
    )
    assert sec2.mode == "cold"


def test_diff_aware_request_carries_cosmetic_preserve_instruction(tmp_path: Path):
    """The rubric explicitly tells the model to preserve prose on cosmetic changes.

    This is the load-bearing piece: without it, the LLM produces a paraphrase
    even when the source change is trivial. We verify the relevant language is
    in the rubric so a future prompt edit doesn't silently weaken the contract.
    """
    f = tmp_path / "foo.py"
    f.write_text("def foo():\n    return 1\n")
    sym = extract_symbols(f)[0]
    req = _build_diff_aware_request(
        sym,
        previous_source="def foo():\n    return 1\n",
        previous_prose="## `foo()`\n\nReturn 1.",
        current_source="def foo():\n    return 1\n",
    )
    assert "Cosmetic changes" in req
    assert "Behavioural changes" in req
    assert "verbatim" in req.lower()
    assert "prefer preserving" in req.lower()


# --- symbol context clause and decorator propagation ---


def test_symbol_context_clause_plain_method(tmp_path: Path):
    f = tmp_path / "m.py"
    f.write_text("class Foo:\n    def bar(self): pass\n")
    syms = {s.qualified_name: s for s in extract_symbols(f)}
    clause = _symbol_context_clause(syms["m:Foo.bar"])
    assert "method of class" in clause
    assert "Foo" in clause


def test_symbol_context_clause_property(tmp_path: Path):
    f = tmp_path / "m.py"
    f.write_text("class Foo:\n    @property\n    def val(self) -> int: return 1\n")
    syms = {s.qualified_name: s for s in extract_symbols(f)}
    clause = _symbol_context_clause(syms["m:Foo.val"])
    assert "@property" in clause
    assert "Foo" in clause


def test_symbol_context_clause_classmethod(tmp_path: Path):
    f = tmp_path / "m.py"
    f.write_text("class Foo:\n    @classmethod\n    def make(cls): return cls()\n")
    syms = {s.qualified_name: s for s in extract_symbols(f)}
    clause = _symbol_context_clause(syms["m:Foo.make"])
    assert "@classmethod" in clause
    assert "Foo" in clause


def test_symbol_context_clause_plain_function(tmp_path: Path):
    f = tmp_path / "m.py"
    f.write_text("def foo(): pass\n")
    syms = extract_symbols(f)
    clause = _symbol_context_clause(syms[0])
    assert clause == "a function"


def test_symbol_source_includes_decorators(tmp_path: Path):
    f = tmp_path / "m.py"
    f.write_text("class Foo:\n    @property\n    def val(self) -> int: return 1\n")
    syms = {s.qualified_name: s for s in extract_symbols(f)}
    src = _symbol_source(syms["m:Foo.val"])
    assert "@property" in src
    assert "def val" in src


def test_request_method_names_class(tmp_path: Path):
    f = tmp_path / "m.py"
    f.write_text("class Store:\n    def close(self): pass\n")
    syms = {s.qualified_name: s for s in extract_symbols(f)}
    out = _build_request(syms["m:Store.close"])
    assert "Store" in out
    assert "method" in out


def test_make_client_rejects_unknown_provider():
    with pytest.raises(NotImplementedError):
        make_client("openai/gpt-4")


def test_make_client_requires_provider_prefix():
    with pytest.raises(ValueError):
        make_client("claude-sonnet-4-6")


def test_make_client_anthropic_constructs(monkeypatch: pytest.MonkeyPatch):
    # Don't actually init the SDK; just verify the type and model_id propagation.
    captured = {}

    class FakeAnthropic:
        def __init__(self, *args, **kwargs):
            captured["constructed"] = True

    monkeypatch.setattr("trie.models.Anthropic", FakeAnthropic)
    client = make_client("anthropic/claude-sonnet-4-6")
    assert client.model_id == "claude-sonnet-4-6"
    assert captured["constructed"] is True
