from __future__ import annotations

import pytest

from trie.sync.writer import Prose, Section, TriefactFile, hash_body

# --- parsing ---


def test_parse_empty():
    triefact = TriefactFile.parse("")
    assert triefact.front_matter == {}
    assert triefact.chunks == []


def test_parse_only_prose():
    triefact = TriefactFile.parse("# hello\n\nplain markdown\n")
    assert triefact.front_matter == {}
    assert len(triefact.chunks) == 1
    assert isinstance(triefact.chunks[0], Prose)
    assert triefact.chunks[0].text == "# hello\n\nplain markdown\n"


def test_parse_front_matter_only():
    text = "---\nfoo: bar\nnested:\n  x: 1\n---\n"
    triefact = TriefactFile.parse(text)
    assert triefact.front_matter == {"foo": "bar", "nested": {"x": 1}}
    assert triefact.chunks == []


def test_parse_front_matter_and_prose():
    text = "---\nkey: value\n---\n# heading\n\nbody\n"
    triefact = TriefactFile.parse(text)
    assert triefact.front_matter == {"key": "value"}
    assert len(triefact.chunks) == 1
    assert isinstance(triefact.chunks[0], Prose)
    assert triefact.chunks[0].text == "# heading\n\nbody\n"


def test_parse_single_section():
    text = (
        "# heading\n\n"
        "<!-- trie:section symbol=mod:foo fingerprint=abc -->\n"
        "## `foo`\n"
        "Generated.\n"
        "<!-- trie:end -->\n"
    )
    triefact = TriefactFile.parse(text)
    # Prose before, the section itself, and trailing newline prose after the close sentinel.
    assert len(triefact.chunks) == 3
    assert isinstance(triefact.chunks[0], Prose)
    assert triefact.chunks[0].text == "# heading\n\n"
    sec = triefact.chunks[1]
    assert isinstance(sec, Section)
    assert sec.qualified_name == "mod:foo"
    assert sec.fingerprint == "abc"
    assert sec.body == "## `foo`\nGenerated."
    assert isinstance(triefact.chunks[2], Prose)
    assert triefact.chunks[2].text == "\n"


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
    triefact = TriefactFile.parse(text)
    qnames = [c.qualified_name for c in triefact.chunks if isinstance(c, Section)]
    assert qnames == ["mod:a", "mod:b"]
    prose_chunks = [c for c in triefact.chunks if isinstance(c, Prose)]
    # One prose chunk between, one trailing newline chunk
    assert any("human prose between" in p.text for p in prose_chunks)


def test_parse_unterminated_section_raises():
    text = "<!-- trie:section symbol=mod:a fingerprint=1 -->\nbody never closes\n"
    with pytest.raises(ValueError, match="Unterminated"):
        TriefactFile.parse(text)


# --- round-trip ---


def test_roundtrip_only_prose_is_byte_identical():
    text = "# hello\n\nsome text\n\nmore\n"
    assert TriefactFile.parse(text).render() == text


def test_roundtrip_with_front_matter_and_section_carrying_body_fp():
    body = "## `bar`\n\nBody of generated section."
    bfp = hash_body(body)
    text = (
        "---\n"
        "trie_version: 0.1.0\n"
        "source: src/foo.py\n"
        "---\n"
        "# foo.py\n\n"
        f"<!-- trie:section symbol=src/foo:bar fingerprint=abc123 body_fp={bfp} -->\n"
        f"{body}\n"
        "<!-- trie:end -->\n"
    )
    triefact = TriefactFile.parse(text)
    assert triefact.render() == text


def test_roundtrip_multiple_sections_with_human_prose():
    alpha_body = "alpha section content"
    beta_body = "beta section content"
    abp = hash_body(alpha_body)
    bbp = hash_body(beta_body)
    text = (
        "---\n"
        "source: src/foo.py\n"
        "---\n"
        "# foo.py\n\n"
        f"<!-- trie:section symbol=src/foo:alpha fingerprint=1 body_fp={abp} -->\n"
        f"{alpha_body}\n"
        "<!-- trie:end -->\n\n"
        "Some hand-written prose here that explains things.\n\n"
        f"<!-- trie:section symbol=src/foo:beta fingerprint=2 body_fp={bbp} -->\n"
        f"{beta_body}\n"
        "<!-- trie:end -->\n"
    )
    rendered = TriefactFile.parse(text).render()
    assert rendered == text


def test_legacy_section_without_body_fp_parses_and_promotes_on_render():
    """Sections written by trie ≤ 0.1 lack `body_fp=`. They parse fine and the renderer
    promotes them to the new format by hashing the current body."""
    text = "<!-- trie:section symbol=mod:foo fingerprint=abc -->\nlegacy body\n<!-- trie:end -->"
    triefact = TriefactFile.parse(text)
    sec = triefact.chunks[0]
    assert isinstance(sec, Section)
    assert sec.body_fingerprint is None
    rendered = triefact.render()
    assert "body_fp=" in rendered
    assert hash_body(sec.body) in rendered


def test_section_round_trips_source_ref():
    """source_ref= round-trips through parse → render unchanged."""
    bfp = hash_body("body")
    text = (
        f"<!-- trie:section symbol=mod:foo fingerprint=fp1 body_fp={bfp} "
        f"source_ref=deadbeef1234567890abcdef1234567890abcdef -->\n"
        "body\n"
        "<!-- trie:end -->"
    )
    triefact = TriefactFile.parse(text)
    sec = triefact.chunks[0]
    assert isinstance(sec, Section)
    assert sec.source_ref == "deadbeef1234567890abcdef1234567890abcdef"
    rendered = triefact.render()
    assert "source_ref=deadbeef1234567890abcdef1234567890abcdef" in rendered


def test_section_without_source_ref_renders_without_it():
    """Cold-write path: section has no source_ref; renderer omits the field cleanly."""
    triefact = TriefactFile.empty()
    triefact.upsert_section(qualified_name="mod:foo", fingerprint="fp1", body="body")
    out = triefact.render()
    assert "source_ref=" not in out
    assert "fingerprint=fp1" in out
    assert "body_fp=" in out


def test_section_with_source_ref_renders_field_in_stable_position():
    """source_ref= appears after body_fp= so two renders of the same section
    produce byte-identical sentinels."""
    triefact = TriefactFile.empty()
    triefact.upsert_section(
        qualified_name="mod:foo",
        fingerprint="fp1",
        body="body",
        source_ref="a" * 40,
    )
    out = triefact.render()
    # Verify ordering: fingerprint comes before body_fp comes before source_ref.
    fp_at = out.index("fingerprint=")
    bfp_at = out.index("body_fp=")
    sr_at = out.index("source_ref=")
    assert fp_at < bfp_at < sr_at


def test_section_legacy_format_with_source_ref_appended_parses():
    """Forward compatibility: if a section happens to carry source_ref= but no
    body_fp= (pathological hand-edit), parser still extracts both fields."""
    text = (
        "<!-- trie:section symbol=mod:foo fingerprint=fp1 "
        "source_ref=deadbeef1234567890abcdef1234567890abcdef -->\n"
        "body\n"
        "<!-- trie:end -->"
    )
    triefact = TriefactFile.parse(text)
    sec = triefact.chunks[0]
    assert isinstance(sec, Section)
    # Without body_fp= the section is still legacy-flagged; source_ref came through.
    assert sec.body_fingerprint is None
    assert sec.source_ref == "deadbeef1234567890abcdef1234567890abcdef"


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
    triefact = TriefactFile.parse(text)
    triefact.upsert_section(qualified_name="mod:foo", fingerprint="new", body="new body")
    out = triefact.render()
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
    triefact = TriefactFile.parse(text)
    triefact.upsert_section(qualified_name="mod:new", fingerprint="aa", body="content")
    out = triefact.render()
    assert "preamble" in out
    assert "<!-- trie:section symbol=mod:new fingerprint=aa" in out
    assert f"body_fp={hash_body('content')}" in out
    assert out.index("preamble") < out.index("trie:section")


def test_upsert_into_empty_triefact():
    triefact = TriefactFile.empty()
    triefact.upsert_section(qualified_name="mod:foo", fingerprint="abc", body="hello")
    out = triefact.render()
    expected = (
        f"<!-- trie:section symbol=mod:foo fingerprint=abc body_fp={hash_body('hello')} -->\n"
        "hello\n<!-- trie:end -->"
    )
    assert out == expected


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
    triefact = TriefactFile.parse(text)
    assert triefact.remove_section("mod:foo") is True
    out = triefact.render()
    assert "mod:foo" not in out
    assert "foo body" not in out
    assert "mod:bar" in out
    assert "bar body" in out
    assert "head" in out


def test_remove_missing_section_returns_false():
    triefact = TriefactFile.parse("plain\n")
    assert triefact.remove_section("mod:nope") is False


def test_section_qnames_in_order():
    text = (
        "<!-- trie:section symbol=mod:c fingerprint=1 -->\nC\n<!-- trie:end -->\n"
        "<!-- trie:section symbol=mod:a fingerprint=2 -->\nA\n<!-- trie:end -->\n"
        "<!-- trie:section symbol=mod:b fingerprint=3 -->\nB\n<!-- trie:end -->\n"
    )
    triefact = TriefactFile.parse(text)
    assert triefact.section_qnames() == ["mod:c", "mod:a", "mod:b"]


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
    triefact = TriefactFile.parse(original)
    # Simulate regen: replace alpha with new content + new fingerprint
    triefact.upsert_section(
        qualified_name="mod:alpha",
        fingerprint="updated",
        body="Regenerated alpha description.",
    )
    rendered = triefact.render()
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
    triefact = TriefactFile.parse(text)
    out = triefact.render()
    src_idx = out.index("source")
    fp_idx = out.index("file_fingerprint")
    assert src_idx < fp_idx
