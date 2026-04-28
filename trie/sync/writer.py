from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any

import yaml

# A trie section is delimited by an open and close HTML comment. The open carries the
# fully-qualified symbol name and a fingerprint over the source content used to generate it.
# Anything outside open/close pairs is treated as human prose and preserved verbatim.
#
# Known limitation (v0.1): the parser does not skip code fences, so a literal
# `<!-- trie:section ... -->` inside a fenced block will be interpreted as a real sentinel.
# Avoid documenting trie's own sentinel format inside trie-managed Markdown for now.

SECTION_OPEN_RE = re.compile(
    r"<!--\s*trie:section\s+symbol=(?P<symbol>\S+)\s+fingerprint=(?P<fp>\S+)\s*-->"
)
SECTION_CLOSE = "<!-- trie:end -->"
FRONT_MATTER_RE = re.compile(r"\A---\s*\n(?P<yaml>.*?)\n---\s*\n", re.DOTALL)


@dataclass(frozen=True)
class Section:
    qualified_name: str
    fingerprint: str
    body: str  # text between sentinels, leading/trailing newlines stripped


@dataclass(frozen=True)
class Prose:
    text: str  # raw bytes preserved verbatim


Chunk = Section | Prose


@dataclass
class DocFile:
    front_matter: dict[str, Any] = field(default_factory=dict)
    chunks: list[Chunk] = field(default_factory=list)

    @classmethod
    def parse(cls, text: str) -> DocFile:
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
            if open_match.start() > cursor:
                chunks.append(Prose(rest[cursor : open_match.start()]))
            close_idx = rest.find(SECTION_CLOSE, open_match.end())
            if close_idx == -1:
                raise ValueError(
                    f"Unterminated trie section opened at offset {open_match.start()} "
                    f"(symbol={open_match.group('symbol')})"
                )
            body = rest[open_match.end() : close_idx]
            if body.startswith("\n"):
                body = body[1:]
            if body.endswith("\n"):
                body = body[:-1]
            chunks.append(
                Section(
                    qualified_name=open_match.group("symbol"),
                    fingerprint=open_match.group("fp"),
                    body=body,
                )
            )
            cursor = close_idx + len(SECTION_CLOSE)
        if cursor < len(rest):
            chunks.append(Prose(rest[cursor:]))
        return cls(front_matter=fm, chunks=chunks)

    @classmethod
    def empty(cls) -> DocFile:
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

    def upsert_section(self, *, qualified_name: str, fingerprint: str, body: str) -> None:
        """Replace an existing section by qualified_name, or append a new one at the end."""
        for i, c in enumerate(self.chunks):
            if isinstance(c, Section) and c.qualified_name == qualified_name:
                self.chunks[i] = Section(qualified_name, fingerprint, body)
                return
        self._append_section(Section(qualified_name, fingerprint, body))

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
                parts.append(
                    f"<!-- trie:section symbol={c.qualified_name} fingerprint={c.fingerprint} -->\n"
                )
                parts.append(c.body)
                if not c.body.endswith("\n"):
                    parts.append("\n")
                parts.append(SECTION_CLOSE)
        return "".join(parts)
