from __future__ import annotations

import re
from dataclasses import dataclass, field
from hashlib import sha256
from typing import Any

import yaml

# A trie section is delimited by an open and close HTML comment. The open carries the
# fully-qualified symbol name and several optional metadata fields:
#   - `fingerprint`: SHA-256 over the *source* symbol body (always present)
#   - `body_fp`:     SHA-256 over the *triefact* section body itself
#   - `source_ref`:  git blob hash of the file whose source state this prose describes
#
# Together they let the coherence check work both ways:
#   - source changed but triefact wasn't regen'd  → fingerprint mismatch
#   - triefact body manually tampered with        → body_fp mismatch
# And `source_ref` lets diff-aware regeneration retrieve "the previous source" without
# guessing — we resolve the blob via git and parse it the same way we parse current
# source. Anything outside open/close pairs is treated as human prose and preserved
# verbatim.
#
# Backward compatibility: every field after `fingerprint` is optional in the regex.
# Sections written by trie ≤ 0.1 don't carry `body_fp`; check.py treats those as
# LEGACY_SECTION and nudges the user to re-sync. Sections written before Level 1
# don't carry `source_ref`; they take the cold-write regen path on next sync, which
# stamps the new field. After one organic regen, every section carries everything.
#
# Structural rule: both sentinels must occupy their own line. The renderer always
# emits them that way; the parser enforces the same. Anything that looks like a
# sentinel but is inside backticks, a fenced block, or otherwise mid-line, is treated
# as prose and ignored. This makes it safe to document trie's own sentinel syntax
# inside trie-managed Markdown without confusing the parser. The match anchors are
# `(?m)^` for line start and `$` for line end (so trailing whitespace on the sentinel
# line is allowed, but trailing text is not).
#
# Field-order rule: the renderer emits fields in a fixed order (symbol, fingerprint,
# body_fp, source_ref) so two regenerations of the same section produce byte-identical
# sentinels when nothing has changed. The parser accepts any order via named groups.

SECTION_OPEN_RE = re.compile(
    r"(?m)^<!--\s*trie:section\s+symbol=(?P<symbol>\S+)\s+fingerprint=(?P<fp>\S+)"
    r"(?:\s+body_fp=(?P<body_fp>\S+))?"
    r"(?:\s+source_ref=(?P<source_ref>\S+))?"
    r"\s*-->[ \t]*$"
)
SECTION_CLOSE_RE = re.compile(r"(?m)^<!--\s*trie:end\s*-->[ \t]*$")
SECTION_CLOSE = "<!-- trie:end -->"  # canonical form used by render()
FRONT_MATTER_RE = re.compile(r"\A---\s*\n(?P<yaml>.*?)\n---\s*\n", re.DOTALL)


def hash_body(body: str) -> str:
    """SHA-256 over the section body with leading/trailing whitespace stripped.

    Whitespace is the only thing trie's renderer normalizes between parse and render
    (a trailing newline is auto-inserted when missing), so stripping it before hashing
    matches what the round-trip writes back.
    """
    return sha256(body.strip().encode("utf-8")).hexdigest()


_HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s")
_SENTENCE_END_RE = re.compile(r"(?<=[.!?])\s+|\Z")


def extract_one_liner(body: str, *, max_chars: int = 200) -> str:
    """Pull the first sentence of a section body, skipping any leading heading.

    The body has the shape `## signature\n\n<prose...>`. The first non-heading,
    non-blank paragraph is treated as the description; we take its first sentence,
    collapse whitespace, and truncate to `max_chars`.

    Returns "" if no usable text is found.
    """
    text_lines: list[str] = []
    for raw in body.splitlines():
        line = raw.strip()
        if not line:
            if text_lines:
                break  # paragraph break ends the candidate sentence
            continue
        if _HEADING_RE.match(line):
            continue
        text_lines.append(line)
    if not text_lines:
        return ""
    paragraph = " ".join(text_lines)
    paragraph = re.sub(r"\s+", " ", paragraph).strip()
    if not paragraph:
        return ""
    # First sentence: up to the first ., !, or ? followed by whitespace or end.
    match = _SENTENCE_END_RE.search(paragraph)
    first = paragraph[: match.start()] if match else paragraph
    first = first.strip()
    if len(first) > max_chars:
        first = first[: max_chars - 1].rstrip() + "\u2026"
    return first


@dataclass(frozen=True)
class Section:
    qualified_name: str
    fingerprint: str  # SHA-256 over normalized source symbol body
    body: str  # text between sentinels, leading/trailing newlines stripped
    body_fingerprint: str | None = None  # SHA-256 over `body`; None for legacy sections
    source_ref: str | None = None  # git blob hash of the file at generation time


@dataclass(frozen=True)
class Prose:
    text: str  # raw bytes preserved verbatim


Chunk = Section | Prose


@dataclass
class TriefactFile:
    front_matter: dict[str, Any] = field(default_factory=dict)
    chunks: list[Chunk] = field(default_factory=list)

    @classmethod
    def parse(cls, text: str) -> TriefactFile:
        fm: dict[str, Any] = {}
        rest = text
        m = FRONT_MATTER_RE.match(text)
        if m:
            try:
                loaded = yaml.safe_load(m.group("yaml"))
                if isinstance(loaded, dict):
                    fm = loaded
            except yaml.YAMLError:
                fm = {}
            rest = text[m.end() :]

        chunks: list[Chunk] = []
        cursor = 0
        for open_match in SECTION_OPEN_RE.finditer(rest):
            # Skip open sentinels that fall inside an already-claimed range — the regex
            # might match an open sentinel that lives inside a previous section's body
            # if that body contains a stray line-anchored sentinel-like string. Cursor
            # advances past every consumed section so this stays a forward-only scan.
            if open_match.start() < cursor:
                continue
            if open_match.start() > cursor:
                chunks.append(Prose(rest[cursor : open_match.start()]))
            close_match = SECTION_CLOSE_RE.search(rest, open_match.end())
            if close_match is None:
                raise ValueError(
                    f"Unterminated trie section opened at offset {open_match.start()} "
                    f"(symbol={open_match.group('symbol')})"
                )
            body = rest[open_match.end() : close_match.start()]
            if body.startswith("\n"):
                body = body[1:]
            if body.endswith("\n"):
                body = body[:-1]
            chunks.append(
                Section(
                    qualified_name=open_match.group("symbol"),
                    fingerprint=open_match.group("fp"),
                    body=body,
                    body_fingerprint=open_match.group("body_fp"),
                    source_ref=open_match.group("source_ref"),
                )
            )
            cursor = close_match.end()
        if cursor < len(rest):
            chunks.append(Prose(rest[cursor:]))
        return cls(front_matter=fm, chunks=chunks)

    @classmethod
    def empty(cls) -> TriefactFile:
        return cls()

    # --- queries ---

    def get_section(self, qualified_name: str) -> Section | None:
        for c in self.chunks:
            if isinstance(c, Section) and c.qualified_name == qualified_name:
                return c
        return None

    def section_qnames(self) -> list[str]:
        return [c.qualified_name for c in self.chunks if isinstance(c, Section)]

    # --- mutations ---

    def upsert_section(
        self,
        *,
        qualified_name: str,
        fingerprint: str,
        body: str,
        source_ref: str | None = None,
    ) -> None:
        """Replace an existing section by qualified_name, or append a new one at the end.

        The body fingerprint is computed automatically from `body` so callers can't
        forget to set it. Re-rendering emits `body_fp=` in the open sentinel; if
        `source_ref` is non-None, it's stamped too. Callers that don't have a git
        blob hash available (no git repo, ad-hoc generation) can pass None and the
        field is simply omitted from the rendered sentinel.
        """
        new = Section(
            qualified_name=qualified_name,
            fingerprint=fingerprint,
            body=body,
            body_fingerprint=hash_body(body),
            source_ref=source_ref,
        )
        for i, c in enumerate(self.chunks):
            if isinstance(c, Section) and c.qualified_name == qualified_name:
                self.chunks[i] = new
                return
        self._append_section(new)

    def remove_section(self, qualified_name: str) -> bool:
        for i, c in enumerate(self.chunks):
            if isinstance(c, Section) and c.qualified_name == qualified_name:
                del self.chunks[i]
                return True
        return False

    def _append_section(self, section: Section) -> None:
        # Ensure a blank-line separator before the new section.
        if self.chunks and isinstance(self.chunks[-1], Prose):
            tail = self.chunks[-1].text
            if not tail.endswith("\n\n"):
                self.chunks[-1] = Prose(tail + ("\n" if tail.endswith("\n") else "\n\n"))
        elif self.chunks and isinstance(self.chunks[-1], Section):
            # Section close sentinel doesn't carry a trailing newline; insert one.
            self.chunks.append(Prose("\n\n"))
        # If this is the very first chunk, the front matter (if any) ends with `---\n`,
        # which provides separation already. No prefix needed.
        self.chunks.append(section)

    # --- rendering ---

    def render(self) -> str:
        parts: list[str] = []
        if self.front_matter:
            yaml_text = yaml.safe_dump(self.front_matter, sort_keys=False, default_flow_style=False)
            parts.append("---\n")
            parts.append(yaml_text)
            parts.append("---\n")
        for c in self.chunks:
            if isinstance(c, Prose):
                parts.append(c.text)
            else:
                # Always emit body_fp on render. If a parsed legacy section is being
                # rewritten unchanged, hash the current body so future checks can verify it.
                body_fp = (
                    c.body_fingerprint if c.body_fingerprint is not None else hash_body(c.body)
                )
                fields = [
                    f"symbol={c.qualified_name}",
                    f"fingerprint={c.fingerprint}",
                    f"body_fp={body_fp}",
                ]
                if c.source_ref:
                    fields.append(f"source_ref={c.source_ref}")
                parts.append("<!-- trie:section " + " ".join(fields) + " -->\n")
                parts.append(c.body)
                if not c.body.endswith("\n"):
                    parts.append("\n")
                parts.append(SECTION_CLOSE)
        return "".join(parts)
