from __future__ import annotations

from tests.fake_client import FakeTrieClient
from trie.edits.infer import infer_source_and_prose, merge_notes


class TestMergeNotes:
    def test_empty_patches(self):
        client = FakeTrieClient()
        notes, reasons = merge_notes(client, [])
        assert notes == []
        assert reasons == []

    def test_single_patch_preserved(self):
        client = FakeTrieClient(
            output_notes=["use gzip instead of brotli"],
            output_reasons=["faster decompression"],
        )
        patches = [{"note": "use gzip instead of brotli", "reason": "faster decompression"}]
        notes, _reasons = merge_notes(client, patches)
        assert len(notes) == 1
        assert "gzip" in notes[0]

    def test_empty_llm_response_falls_back_to_raw_notes(self):
        # merge is an optional dedup pass; an empty/garbage LLM response must NOT
        # drop the agent's notes (which previously aborted the whole apply on a
        # MergeNotesOutput validation error). Fall back to the raw notes.
        client = FakeTrieClient(output_notes=[], output_reasons=[])
        patches = [
            {"note": "change A", "reason": "r1"},
            {"note": "change B", "reason": "r2"},
        ]
        notes, reasons = merge_notes(client, patches)
        assert notes == ["change A", "change B"]
        assert reasons == ["r1", "r2"]

    def test_single_patch_skips_llm(self):
        # A single patch has nothing to merge — return verbatim without an LLM
        # call (so a flaky merge call can't break a one-symbol apply).
        client = FakeTrieClient(output_notes=[], output_reasons=[])
        patches = [{"note": "old change", "reason": "still relevant"}]
        notes, reasons = merge_notes(client, patches)
        assert notes == ["old change"]
        assert reasons == ["still relevant"]

    def test_preserves_reasons_via_delimiter(self):
        client = FakeTrieClient(
            output_notes=["use gzip"],
            output_reasons=["faster decompression"],
        )
        patches = [{"note": "use gzip", "reason": "faster decompression"}]
        notes, reasons = merge_notes(client, patches)
        assert len(notes) == 1
        assert "gzip" in notes[0]
        assert reasons == ["faster decompression"]

    def test_preserves_reasons_multiple_lines(self):
        client = FakeTrieClient(
            output_notes=["add streaming", "use gzip"],
            output_reasons=["large payload support", "faster decompression"],
        )
        patches = [
            {"note": "add streaming", "reason": "large payload support"},
            {"note": "use gzip", "reason": "faster decompression"},
        ]
        notes, reasons = merge_notes(client, patches)
        assert len(notes) == 2
        assert reasons == ["large payload support", "faster decompression"]

    def test_fallback_no_delimiter(self):
        client = FakeTrieClient(
            output_notes=["just a bare note", "another note"],
            output_reasons=["merged", "merged"],
        )
        patches = [
            {"note": "just a bare note", "reason": "some reason"},
            {"note": "another note", "reason": "another reason"},
        ]
        notes, reasons = merge_notes(client, patches)
        assert len(notes) == 2
        assert reasons == ["merged", "merged"]

    def test_mixed_bullet_formats(self):
        client = FakeTrieClient(
            output_notes=["note one", "note two", "note three"],
            output_reasons=["reason one", "reason two", "reason three"],
        )
        patches = [
            {"note": "x", "reason": "r1"},
            {"note": "y", "reason": "r2"},
            {"note": "z", "reason": "r3"},
        ]
        notes, reasons = merge_notes(client, patches)
        assert len(notes) == 3
        assert reasons == ["reason one", "reason two", "reason three"]


class TestInferSourceAndProse:
    def test_basic_inference(self):
        client = FakeTrieClient(
            output_source="def greet() -> str:\n    return 'hello world'\n",
            output_prose="Return a greeting string.",
        )
        new_source, _new_prose = infer_source_and_prose(
            client,
            old_source="def greet():\n    return 'hello'",
            old_prose="Return a greeting.",
            notes=["change return value"],
            reasons=["update message"],
        )
        assert "greet" in new_source
        assert "hello world" in new_source

    def test_source_without_code_block(self):
        """LLM returns source without triple-backticks."""
        client = FakeTrieClient(
            output_source="def greet() -> str:\n    return 'hello'\n",
            output_prose="Greet the user.",
        )
        new_source, new_prose = infer_source_and_prose(
            client,
            old_source="def greet():\n    return 'hi'",
            old_prose="Say hi.",
            notes=["formalize"],
            reasons=["style"],
        )
        assert new_source.strip().startswith("def greet")
        assert "Greet" in new_prose

    def test_multiline_prose(self):
        """Prose section spans multiple paragraphs."""
        client = FakeTrieClient(
            output_source="def foo():\n    pass\n",
            output_prose="First paragraph.\n\nSecond paragraph.\n",
        )
        _new_source, new_prose = infer_source_and_prose(
            client,
            old_source="def foo():\n    pass",
            old_prose="Do stuff.",
            notes=["expand"],
            reasons=["docs"],
        )
        assert "First paragraph." in new_prose
        assert "Second paragraph." in new_prose
