from __future__ import annotations

import pytest
from pytest_mock import MockerFixture

from trie.edits.infer import infer_source_and_prose, merge_notes


def _make_response(text: str):
    """Build a minimal GenerationResponse-like object."""
    from types import SimpleNamespace

    return SimpleNamespace(
        text=text,
        input_tokens=10,
        output_tokens=len(text.split()),
        cache_creation_input_tokens=0,
        cache_read_input_tokens=0,
    )


class TestMergeNotes:
    def test_empty_patches(self, mocker: MockerFixture):
        client = mocker.MagicMock()
        client.generate.side_effect = []
        notes, reasons = merge_notes(client, [])
        assert notes == []
        assert reasons == []

    def test_single_patch_preserved(self, mocker: MockerFixture):
        client = mocker.MagicMock()
        client.generate.side_effect = [_make_response("use gzip instead of brotli")]
        patches = [{"note": "use gzip instead of brotli", "reason": "faster decompression"}]
        notes, _reasons = merge_notes(client, patches)
        assert len(notes) == 1
        assert "gzip" in notes[0]

    def test_empty_response_returns_empty(self, mocker: MockerFixture):
        client = mocker.MagicMock()
        client.generate.side_effect = [_make_response("")]
        patches = [{"note": "old change", "reason": "no longer relevant"}]
        notes, reasons = merge_notes(client, patches)
        assert notes == []
        assert reasons == []

    def test_preserves_reasons_via_delimiter(self, mocker: MockerFixture):
        client = mocker.MagicMock()
        client.generate.side_effect = [_make_response("* use gzip  —  faster decompression")]
        patches = [{"note": "use gzip", "reason": "faster decompression"}]
        notes, reasons = merge_notes(client, patches)
        assert len(notes) == 1
        assert "gzip" in notes[0]
        assert reasons == ["faster decompression"]

    def test_preserves_reasons_multiple_lines(self, mocker: MockerFixture):
        client = mocker.MagicMock()
        client.generate.side_effect = [
            _make_response(
                "- add streaming  —  large payload support\n* use gzip  —  faster decompression"
            )
        ]
        patches = [
            {"note": "add streaming", "reason": "large payload support"},
            {"note": "use gzip", "reason": "faster decompression"},
        ]
        notes, reasons = merge_notes(client, patches)
        assert len(notes) == 2
        assert reasons == ["large payload support", "faster decompression"]

    def test_fallback_no_delimiter(self, mocker: MockerFixture):
        client = mocker.MagicMock()
        client.generate.side_effect = [_make_response("just a bare note\n- another note")]
        patches = [
            {"note": "just a bare note", "reason": "some reason"},
            {"note": "another note", "reason": "another reason"},
        ]
        notes, reasons = merge_notes(client, patches)
        assert len(notes) == 2
        assert reasons == ["merged", "merged"]

    def test_mixed_bullet_formats(self, mocker: MockerFixture):
        client = mocker.MagicMock()
        client.generate.side_effect = [
            _make_response(
                "<bullet> note one  —  reason one\n"
                "* note two  —  reason two\n"
                "- note three  —  reason three"
            )
        ]
        patches = [
            {"note": "x", "reason": "r1"},
            {"note": "y", "reason": "r2"},
            {"note": "z", "reason": "r3"},
        ]
        notes, reasons = merge_notes(client, patches)
        assert len(notes) == 3
        assert reasons == ["reason one", "reason two", "reason three"]


class TestInferSourceAndProse:
    def test_basic_inference(self, mocker: MockerFixture):
        client = mocker.MagicMock()
        client.generate.side_effect = [
            _make_response(
                "```python\ndef greet() -> str:\n    return 'hello world'\n```\n\n---PROSE---\nReturn a greeting string."
            )
        ]
        new_source, _new_prose = infer_source_and_prose(
            client,
            old_source="def greet():\n    return 'hello'",
            old_prose="Return a greeting.",
            notes=["change return value"],
            reasons=["update message"],
        )
        assert "greet" in new_source
        assert "hello" in new_source

    def test_unknown_delimiter_raises(self, mocker: MockerFixture):
        client = mocker.MagicMock()
        client.generate.side_effect = [_make_response("some text without the delimiter")]
        with pytest.raises(ValueError):
            infer_source_and_prose(
                client,
                old_source="def foo(): pass",
                old_prose="Does nothing.",
                notes=["test"],
                reasons=["test"],
            )

    def test_source_without_code_block(self, mocker: MockerFixture):
        """LLM returns source without triple-backticks."""
        client = mocker.MagicMock()
        client.generate.side_effect = [
            _make_response(
                "def greet() -> str:\n    return 'hello'\n\n---PROSE---\nGreet the user."
            )
        ]
        new_source, new_prose = infer_source_and_prose(
            client,
            old_source="def greet():\n    return 'hi'",
            old_prose="Say hi.",
            notes=["formalize"],
            reasons=["style"],
        )
        assert new_source.strip().startswith("def greet")
        assert "Greet" in new_prose

    def test_multiline_prose(self, mocker: MockerFixture):
        """Prose section spans multiple paragraphs."""
        client = mocker.MagicMock()
        client.generate.side_effect = [
            _make_response(
                "```python\ndef foo():\n    pass\n```\n\n"
                "---PROSE---\nFirst paragraph.\n\nSecond paragraph.\n"
            )
        ]
        _new_source, new_prose = infer_source_and_prose(
            client,
            old_source="def foo():\n    pass",
            old_prose="Do stuff.",
            notes=["expand"],
            reasons=["docs"],
        )
        assert "First paragraph." in new_prose
        assert "Second paragraph." in new_prose
