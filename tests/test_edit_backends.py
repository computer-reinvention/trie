from __future__ import annotations

import pytest

from trie.config import Config
from trie.edits.backends import (
    EditRequest,
    FakeBackend,
    InProcessLLMBackend,
    NeighbourCtx,
    SymbolEditBackend,
    make_backend,
)
from trie.edits.backends.llm import build_user_prompt


def _req(op: str = "modify", **kw) -> EditRequest:
    base = dict(
        qname="src/foo:bar",
        op=op,
        old_source="def bar():\n    return 1\n",
        old_prose="returns one",
        merged_notes=["return two instead"],
        merged_reasons=["spec change"],
        session_note="bump return value",
        callees=[NeighbourCtx("src/x:dep", "def dep() -> int", "the dep")],
        callers=[NeighbourCtx("src/y:caller", "def caller()", "uses bar")],
        file_path="src/foo.py",
    )
    base.update(kw)
    return EditRequest(**base)


class TestFakeBackend:
    def test_passthrough_echoes_source(self):
        b = FakeBackend("passthrough")
        r = b.generate(_req())
        assert r.ok
        assert r.new_source == "def bar():\n    return 1\n"

    def test_append_changes_source(self):
        b = FakeBackend("append")
        r = b.generate(_req())
        assert r.ok
        assert "trie-fake-edit" in r.new_source

    def test_broken_returns_noncompiling(self):
        b = FakeBackend("broken")
        r = b.generate(_req())
        assert r.ok  # produced a candidate; compile gate judges it, not the backend
        assert "broken" in r.new_source

    def test_fail_returns_not_ok(self):
        b = FakeBackend("fail")
        r = b.generate(_req())
        assert not r.ok
        assert r.error

    def test_per_qname_override(self):
        b = FakeBackend("passthrough", per_qname={"src/foo:bar": "fail"})
        assert not b.generate(_req()).ok
        # a different qname uses the default mode
        assert b.generate(_req(qname="src/foo:other")).ok

    def test_create_synthesizes_when_empty(self):
        b = FakeBackend("passthrough")
        r = b.generate(_req(op="create", old_source=""))
        assert r.ok
        assert "def bar" in r.new_source

    def test_satisfies_protocol(self):
        assert isinstance(FakeBackend(), SymbolEditBackend)


class TestLLMBackend:
    def test_build_user_prompt_includes_context(self):
        prompt = build_user_prompt(_req())
        assert "src/foo:bar" in prompt
        assert "Callees" in prompt and "def dep() -> int" in prompt
        assert "Callers" in prompt and "def caller()" in prompt
        assert "bump return value" in prompt  # session note
        assert "return two instead" in prompt  # the intent note

    def test_create_clause_present_for_create(self):
        prompt = build_user_prompt(_req(op="create", old_source=""))
        assert "NEW symbol" in prompt

    def test_satisfies_protocol(self):
        # Build with a dummy client object; we only check the protocol shape.
        class _DummyClient:
            def run(self, *a, **k):  # pragma: no cover - not invoked here
                raise NotImplementedError

        assert isinstance(InProcessLLMBackend(_DummyClient()), SymbolEditBackend)


class TestFactory:
    def test_default_is_llm(self):
        cfg = Config()

        class _DummyClient:
            pass

        b = make_backend(cfg, client=_DummyClient())
        assert isinstance(b, InProcessLLMBackend)

    def test_opencode_not_yet_implemented(self):
        cfg = Config()
        with pytest.raises(NotImplementedError):
            make_backend(cfg, backend="opencode")

    def test_unknown_backend_raises(self):
        cfg = Config()
        with pytest.raises(ValueError):
            make_backend(cfg, backend="nope")

    def test_run_override_wins_over_config(self):
        cfg = Config()
        cfg.edits.backend = "opencode"
        # run override forces llm despite config saying opencode

        class _DummyClient:
            pass

        b = make_backend(cfg, backend="llm", client=_DummyClient())
        assert isinstance(b, InProcessLLMBackend)
