from __future__ import annotations

import pytest

from trie.sync.writer import DocFile, Prose, Section

# --- parsing ---


def test_parse_empty():
    doc = DocFile.parse("")
    assert doc.front_matter == {}
    assert doc.chunks == []


def test_parse_only_prose():
    doc = DocFile.parse("# hello\n\nplain markdown\n")
    assert doc.front_matter == {}
    assert len(doc.chunks) == 1
    assert isinstance(doc.chunks[0], Prose)
    assert doc.chunks[0].text == "# hello\n\nplain markdown\n"


def test_parse_front_matter_only():
    text = "---\nfoo: bar\nnested:\n  x: 1\n---\n"
    doc = DocFile.parse(text)
    assert doc.front_matter == {"foo": "bar", "nested": {"x": 1}}
    assert doc.chunks == []


def test_parse_front_matter_and_prose():
    text = "---\nkey: value\n---\n# heading\n\nbody\n"
    doc = DocFile.parse(text)
    assert doc.front_matter == {"key": "value"}
    assert len(doc.chunks) == 1
    assert isinstance(doc.chunks[0], Prose)
    assert doc.chunks[0].text == "# heading\n\nbody\n"


def test_parse_single_section():
    text = (
        "# heading\n\n"
        "<!-- trie:section symbol=mod:foo fingerprint=abc -->\n"
        "## `foo`\n"
        "Generated.\n"
        "<!-- trie:end -->\n"
    )
    doc = DocFile.parse(text)
    # Prose before, the section itself, and trailing newline prose after the close sentinel.
    assert len(doc.chunks) == 3
    assert isinstance(doc.chunks[0], Prose)
    assert doc.chunks[0].text == "# heading\n\n"
    sec = doc.chunks[1]
    assert isinstance(sec, Section)
    assert sec.qualified_name == "mod:foo"
    assert sec.fingerprint == "abc"
    assert sec.body == "## `foo`\nGenerated."
    assert isinstance(doc.chunks[2], Prose)
    assert doc.chunks[2].text == "\n"


def test_parse_multiple_sections_with_prose_between():
    text = (
        "<!-- trie:section symbol=mod:a fingerprint=1 -->\n"
        "alpha\n"
        "<!-- trie:end -->\n"
        "human prose between\n"
        "<!-- trie:section symbol=mod:b fingerprint=2 -->\n"
        "beta\n"
        "<!-- trie:end -->\n"
    )
    doc = DocFile.parse(text)
    qnames = [c.qualified_name for c in doc.chunks if isinstance(c, Section)]
    assert qnames == ["mod:a", "mod:b"]
    prose_chunks = [c for c in doc.chunks if isinstance(c, Prose)]
    # One prose chunk between, one trailing newline chunk
    assert any("human prose between" in p.text for p in prose_chunks)


def test_parse_unterminated_section_raises():
    text = "<!-- trie:section symbol=mod:a fingerprint=1 -->\nbody never closes\n"
    with pytest.raises(ValueError, match="Unterminated"):
        DocFile.parse(text)


# --- round-trip ---


def test_roundtrip_only_prose_is_byte_identical():
    text = "# hello\n\nsome text\n\nmore\n"
    assert DocFile.parse(text).render() == text


def test_roundtrip_with_front_matter_and_section():
    text = (
        "---\n"
        "trie_version: 0.1.0\n"
        "source: src/foo.py\n"
        "---\n"
        "# foo.py\n\n"
        "<!-- trie:section symbol=src/foo:bar fingerprint=abc123 -->\n"
        "## `bar`\n\n"
        "Body of generated section.\n"
        "<!-- trie:end -->\n"
    )
    doc = DocFile.parse(text)
    assert doc.render() == text


def test_roundtrip_multiple_sections_with_human_prose():
    text = (
        "---\n"
        "source: src/foo.py\n"
        "---\n"
        "# foo.py\n\n"
        "<!-- trie:section symbol=src/foo:alpha fingerprint=1 -->\n"
        "alpha section content\n"
        "<!-- trie:end -->\n\n"
        "Some hand-written prose here that explains things.\n\n"
        "<!-- trie:section symbol=src/foo:beta fingerprint=2 -->\n"
        "beta section content\n"
        "<!-- trie:end -->\n"
    )
    rendered = DocFile.parse(text).render()
    assert rendered == text


# --- mutations ---


def test_upsert_replaces_existing_section_preserves_prose():
    text = (
        "intro prose\n\n"
        "<!-- trie:section symbol=mod:foo fingerprint=old -->\n"
        "old body\n"
        "<!-- trie:end -->\n\n"
        "between prose preserved\n\n"
        "<!-- trie:section symbol=mod:bar fingerprint=2 -->\n"
        "bar body\n"
        "<!-- trie:end -->\n"
    )
    doc = DocFile.parse(text)
    doc.upsert_section(qualified_name="mod:foo", fingerprint="new", body="new body")
    out = doc.render()
    assert "fingerprint=new" in out
    assert "fingerprint=old" not in out
    assert "new body" in out
    assert "old body" not in out
    # Prose untouched
    assert "intro prose" in out
    assert "between prose preserved" in out
    # Other section untouched
    assert "fingerprint=2" in out
    assert "bar body" in out


def test_upsert_appends_new_section_at_end():
    text = "preamble\n"
    doc = DocFile.parse(text)
    doc.upsert_section(qualified_name="mod:new", fingerprint="aa", body="content")
    out = doc.render()
    assert "preamble" in out
    assert "<!-- trie:section symbol=mod:new fingerprint=aa -->" in out
    assert out.index("preamble") < out.index("trie:section")


def test_upsert_into_empty_doc():
    doc = DocFile.empty()
    doc.upsert_section(qualified_name="mod:foo", fingerprint="abc", body="hello")
    out = doc.render()
    assert out == "<!-- trie:section symbol=mod:foo fingerprint=abc -->\nhello\n<!-- trie:end -->"


def test_remove_section():
    text = (
        "head\n\n"
        "<!-- trie:section symbol=mod:foo fingerprint=1 -->\n"
        "foo body\n"
        "<!-- trie:end -->\n\n"
        "<!-- trie:section symbol=mod:bar fingerprint=2 -->\n"
        "bar body\n"
        "<!-- trie:end -->\n"
    )
    doc = DocFile.parse(text)
    assert doc.remove_section("mod:foo") is True
    out = doc.render()
    assert "mod:foo" not in out
    assert "foo body" not in out
    assert "mod:bar" in out
    assert "bar body" in out
    assert "head" in out


def test_remove_missing_section_returns_false():
    doc = DocFile.parse("plain\n")
    assert doc.remove_section("mod:nope") is False


def test_section_qnames_in_order():
    text = (
        "<!-- trie:section symbol=mod:c fingerprint=1 -->\nC\n<!-- trie:end -->\n"
        "<!-- trie:section symbol=mod:a fingerprint=2 -->\nA\n<!-- trie:end -->\n"
        "<!-- trie:section symbol=mod:b fingerprint=3 -->\nB\n<!-- trie:end -->\n"
    )
    doc = DocFile.parse(text)
    assert doc.section_qnames() == ["mod:c", "mod:a", "mod:b"]


# --- the critical guarantee: human edits between sentinels survive regen ---


def test_human_edit_between_sections_survives_regen():
    original = (
        "# Module foo\n\n"
        "<!-- trie:section symbol=mod:alpha fingerprint=1 -->\n"
        "Generated alpha description.\n"
        "<!-- trie:end -->\n\n"
        "## Why this module exists\n\n"
        "This is **hand-written** prose explaining design rationale.\n"
        "It must survive regeneration of the alpha section.\n\n"
        "<!-- trie:section symbol=mod:beta fingerprint=2 -->\n"
        "Generated beta description.\n"
        "<!-- trie:end -->\n"
    )
    doc = DocFile.parse(original)
    # Simulate regen: replace alpha with new content + new fingerprint
    doc.upsert_section(
        qualified_name="mod:alpha",
        fingerprint="updated",
        body="Regenerated alpha description.",
    )
    rendered = doc.render()
    # Hand-written prose intact
    assert "## Why this module exists" in rendered
    assert "**hand-written** prose explaining design rationale" in rendered
    assert "It must survive regeneration of the alpha section." in rendered
    # Alpha updated
    assert "Regenerated alpha description." in rendered
    assert "Generated alpha description." not in rendered
    assert "fingerprint=updated" in rendered
    # Beta untouched
    assert "Generated beta description." in rendered
    assert "fingerprint=2" in rendered


def test_front_matter_re_renders_in_insertion_order():
    text = "---\nsource: src/x.py\nfile_fingerprint: abc\n---\nbody\n"
    doc = DocFile.parse(text)
    out = doc.render()
    src_idx = out.index("source")
    fp_idx = out.index("file_fingerprint")
    assert src_idx < fp_idx
