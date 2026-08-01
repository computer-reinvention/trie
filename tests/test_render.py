"""Tests for trie/render.py — the plain-text envelope renderer that is the
default output format on every interaction surface (CLI + MCP)."""

from __future__ import annotations

from trie.render import render_envelope


def test_symbol_records_render_compact():
    """Symbol dicts become header + squeezed signature + one-liner — a
    multi-line typer signature must collapse to one line."""
    out = render_envelope(
        {
            "hits": [
                {
                    "qname": "pkg/mod:thing",
                    "kind": "function",
                    "file_pointer": "pkg/mod.py:10",
                    "signature": "def thing(\n    a: int,\n    b: str,\n) -> None",
                    "one_liner": "Does the thing.",
                    "inbound_count": 3,
                    "score": 92.0,
                }
            ]
        }
    )
    assert "pkg/mod:thing  function  pkg/mod.py:10  in:3 score:92.0" in out
    assert "def thing( a: int, b: str, ) -> None" in out
    assert "Does the thing." in out
    assert "\\n" not in out, "no escaped newlines — that was the whole point"


def test_call_chains_render_as_arrows():
    out = render_envelope({"paths": [["a/b:f", "a/b:g", "a/c:h"], ["a/b:f", "a/c:h"]]})
    assert "1. a/b:f → a/b:g → a/c:h" in out
    assert "2. a/b:f → a/c:h" in out
    assert "[" not in out


def test_prose_fields_render_verbatim():
    story = "**caller one** does X.\n\n**caller two** does Y."
    out = render_envelope({"usage_story": story})
    assert "**caller one** does X." in out
    assert "**caller two** does Y." in out


def test_story_suppresses_duplicate_caller_records():
    """The explain tools weave callers into the story; the raw arrays would
    repeat every line of it."""
    out = render_envelope(
        {
            "usage_story": "**a:b** calls it.",
            "callers": [{"qname": "a:b", "one_liner": "calls it"}],
        }
    )
    assert "**a:b** calls it." in out
    assert out.count("a:b") == 1


def test_error_envelope_renders_code_message_suggestion():
    out = render_envelope(
        {"error": {"code": "not_found", "message": "nope.", "suggestion": "try grep."}}
    )
    assert out.splitlines()[0] == "error not_found: nope."
    assert "try grep." in out


def test_empty_list_and_scalars():
    out = render_envelope({"hits": [], "count": 3, "flag": True})
    assert "hits: (none)" in out
    assert "count: 3" in out
    assert "flag: True" in out
