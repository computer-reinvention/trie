from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pytest

from trie.models import GenerationRequest, GenerationResponse, make_client
from trie.parse.python import extract_symbols
from trie.sync.generator import (
    SYSTEM_PROMPT,
    FileGenerationContext,
    _build_request,
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
