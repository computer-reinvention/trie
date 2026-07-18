from __future__ import annotations

from trie.edits import textgen


class TestParseCode:
    def test_extracts_fenced_block(self):
        text = "Here you go:\n```python\ndef f():\n    return 1\n```\nthanks"
        assert textgen.parse_code(text) == "def f():\n    return 1"

    def test_fence_with_no_language(self):
        text = "```\nconst x = 1\n```"
        assert textgen.parse_code(text) == "const x = 1"

    def test_preserves_blank_lines_inside_body(self):
        text = "```ts\nconst a = 1\n\nconst b = 2\n```"
        assert textgen.parse_code(text) == "const a = 1\n\nconst b = 2"

    def test_stops_prose_sections_from_leaking_into_code(self):
        # Prose section after the fence must not be captured as code.
        text = (
            "```python\ndef f():\n    return 1\n```\n\n"
            f"{textgen.PROSE_OPEN}\nDoes a thing.\n{textgen.PROSE_END}\n"
        )
        assert textgen.parse_code(text) == "def f():\n    return 1"

    def test_missing_fence_falls_back_to_raw_minus_prose(self):
        text = (
            f"def f():\n    return 1\n\n{textgen.PROSE_OPEN}\nDoes a thing.\n{textgen.PROSE_END}\n"
        )
        assert textgen.parse_code(text) == "def f():\n    return 1"

    def test_missing_fence_and_no_prose_returns_stripped_text(self):
        assert textgen.parse_code("\ndef f():\n    return 1\n") == "def f():\n    return 1"


class TestParseSingleProse:
    def test_extracts_delimited_prose(self):
        text = (
            "```python\nx = 1\n```\n\n"
            f"{textgen.PROSE_OPEN}\nA one-paragraph summary.\n{textgen.PROSE_END}\n"
        )
        assert textgen.parse_single_prose(text) == "A one-paragraph summary."

    def test_absent_prose_returns_empty(self):
        assert textgen.parse_single_prose("```\nx=1\n```") == ""


class TestParseQnameProse:
    def test_extracts_multiple_qname_sections(self):
        text = (
            "```ts\n// file\n```\n\n"
            f"{textgen.PROSE_OPEN_QNAME}src/a:Foo>>>\nFoo does foo.\n{textgen.PROSE_END}\n"
            f"{textgen.PROSE_OPEN_QNAME}src/b:Bar>>>\nBar does bar.\n{textgen.PROSE_END}\n"
        )
        out = textgen.parse_qname_prose(text)
        assert out == {"src/a:Foo": "Foo does foo.", "src/b:Bar": "Bar does bar."}

    def test_no_sections_returns_empty_dict(self):
        assert textgen.parse_qname_prose("```\nx=1\n```") == {}


class TestParseNewDeps:
    def test_extracts_package_names(self):
        text = (
            "```ts\nx\n```\n\n"
            f"{textgen.NEW_DEPS_OPEN}\nuuid\n@react-native-async-storage/async-storage\n"
            f"{textgen.NEW_DEPS_END}\n"
        )
        assert textgen.parse_new_deps(text) == [
            "uuid",
            "@react-native-async-storage/async-storage",
        ]

    def test_ignores_relative_specifiers_and_bullets(self):
        text = f"{textgen.NEW_DEPS_OPEN}\n- uuid\n* ./local\n`zod`\n.\n{textgen.NEW_DEPS_END}\n"
        assert textgen.parse_new_deps(text) == ["uuid", "zod"]

    def test_absent_returns_empty(self):
        assert textgen.parse_new_deps("```\nx\n```") == []


class TestRoundTrip:
    def test_single_symbol_round_trips_through_format_and_parser(self):
        src = "function widget() {\n  return `template ${x}`;\n}"
        prose = "Renders a widget."
        text = f"```ts\n{src}\n```\n\n{textgen.PROSE_OPEN}\n{prose}\n{textgen.PROSE_END}\n"
        assert textgen.parse_code(text) == src
        assert textgen.parse_single_prose(text) == prose
