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
