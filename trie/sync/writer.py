from __future__ import annotations

import re
from dataclasses import dataclass, field, replace
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
# body_fp, source_ref, role) so two regenerations of the same section produce
# byte-identical sentinels when nothing has changed. The parser accepts any order
# via named groups. `role` is appended last so sections written before role
# persistence existed render identically until they're next regenerated with a role.
SECTION_OPEN_RE = re.compile(
    r"(?m)^<!--\s*trie:section\s+symbol=(?P<symbol>\S+)\s+fingerprint=(?P<fp>\S*)"
    r"(?:\s+body_fp=(?P<body_fp>\S+))?"
    r"(?:\s+source_ref=(?P<source_ref>\S+))?"
    r"(?:\s+role=(?P<role>\S+))?"
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


# Frontmatter keys that are useful to a reader (human or agent): the file's
# synthesised description, the manifest of symbols it defines, and the inbound/
# outbound reference counts. Everything else in frontmatter is trie's own
# bookkeeping (versions, fingerprints, sync timestamps, git blob refs) and is
# noise on the agent surface — see `render_for_agent` below.
AGENT_FRONT_MATTER_KEYS: tuple[str, ...] = (
    "description",
    "defines",
    "incoming_refs",
    "outgoing_refs",
)


@dataclass(frozen=True)
class Section:
    qualified_name: str
    fingerprint: str  # SHA-256 over normalized source symbol body
    body: str  # text between sentinels, leading/trailing newlines stripped
    body_fingerprint: str | None = None  # SHA-256 over `body`; None for legacy sections
    source_ref: str | None = None  # git blob hash of the file at generation time
    role: str = ""  # LLM-inferred architectural role; "" when unknown/legacy.
    # Persisted in the sentinel so the role survives a graph.db wipe: the DB is a
    # rebuildable cache, the triefact files are the source of truth. Without this
    # the role lived only in triefact_sections.role and was lost on any rebuild.


@dataclass(frozen=True)
class Prose:
    text: str  # raw bytes preserved verbatim


Chunk = Section | Prose


def _dedupe_sections(chunks: list[Chunk]) -> list[Chunk]:
    """Collapse duplicate sections (same qualified_name) to a single, freshest copy.

    A correct triefact has exactly one section per symbol. A bug or an interrupted/
    concurrent write can leave two sections for the same qname; left alone they
    accumulate and the symbol reads as permanently drifted (the drift check sees
    one fingerprint, sync rewrites another). We defend at the parse boundary:
    keep the LAST occurrence of each qname (the most recently written, hence
    freshest), at the position of its FIRST occurrence (so source-order layout is
    preserved). Non-section prose is passed through untouched. This makes any
    accumulated duplication self-heal on the next read → render round-trip.
    """
    seen: set[str] = set()
    # Walk once to find the last Section per qname.
    last_by_qname: dict[str, Section] = {}
    for c in chunks:
        if isinstance(c, Section):
            last_by_qname[c.qualified_name] = c

    out: list[Chunk] = []
    for c in chunks:
        if isinstance(c, Section):
            if c.qualified_name in seen:
                continue  # a later duplicate handled at the first position
            seen.add(c.qualified_name)
            out.append(last_by_qname[c.qualified_name])
        else:
            out.append(c)
    return out


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
                    role=open_match.group("role") or "",
                )
            )
            cursor = close_match.end()
        if cursor < len(rest):
            chunks.append(Prose(rest[cursor:]))
        chunks = _dedupe_sections(chunks)
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
        role: str = "",
    ) -> None:
        """Replace an existing section by qualified_name, or append a new one at the end.

        The body fingerprint is computed automatically from `body` so callers can't
        forget to set it. Re-rendering emits `body_fp=` in the open sentinel; if
        `source_ref` is non-None, it's stamped too. Callers that don't have a git
        blob hash available (no git repo, ad-hoc generation) can pass None and the
        field is simply omitted from the rendered sentinel.

        `role` is the LLM-inferred architectural role tag; "" omits the field from
        the sentinel. It's stamped so the role survives a graph.db rebuild.
        """
        new = Section(
            qualified_name=qualified_name,
            fingerprint=fingerprint,
            body=body,
            body_fingerprint=hash_body(body),
            source_ref=source_ref,
            role=role,
        )
        for i, c in enumerate(self.chunks):
            if isinstance(c, Section) and c.qualified_name == qualified_name:
                self.chunks[i] = new
                return
        self._append_section(new)

    def set_section_role(self, qualified_name: str, role: str) -> bool:
        """Update only the role tag of an existing section, preserving its body and
        all other fields. Returns True if the section existed and was updated.

        This is the durable half of `trie sync --roles-only`: it stamps the
        inferred role into the sentinel without touching prose or fingerprints, so
        a roles-only pass produces a minimal diff (only role= changes).
        """
        for i, c in enumerate(self.chunks):
            if isinstance(c, Section) and c.qualified_name == qualified_name:
                if c.role == role:
                    return True
                self.chunks[i] = replace(c, role=role)
                return True
        return False

    def sort_sections(self, start_line_by_qname: dict[str, int]) -> None:
        """Reorder Section chunks to match source-line order.

        `start_line_by_qname` maps each qualified_name to its `start_line` in the
        current source. Sections whose qname is absent from the map (e.g. legacy
        hand-written sections) are placed at the end, preserving their relative order.

        Whitespace-only Prose chunks (the `\\n\\n` separators inserted by
        `_append_section`) are dropped — `render()` recreates them. Non-whitespace
        Prose (hand-written content between sections) is preserved at the front,
        before the first section, where it was originally placed by the author.
        """
        content_prose: list[Prose] = [
            c for c in self.chunks if isinstance(c, Prose) and c.text.strip()
        ]
        sections = [c for c in self.chunks if isinstance(c, Section)]
        sections.sort(
            key=lambda s: (
                start_line_by_qname.get(s.qualified_name, 10**9),
                s.qualified_name,
            )
        )
        self.chunks = content_prose + sections  # type: ignore[assignment]

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
        prev_was_section = False
        for c in self.chunks:
            if isinstance(c, Prose):
                parts.append(c.text)
                prev_was_section = False
            else:
                # Ensure consecutive sections are separated by a blank line so
                # each sentinel starts on its own line (required by the parser).
                if prev_was_section:
                    parts.append("\n")
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
                if c.role:
                    fields.append(f"role={c.role}")
                parts.append("<!-- trie:section " + " ".join(fields) + " -->\n")
                parts.append(c.body)
                if not c.body.endswith("\n"):
                    parts.append("\n")
                parts.append(SECTION_CLOSE)
                prev_was_section = True
        return "".join(parts)


def render_for_agent(text: str) -> str:
    """Re-render a triefact for an agent-facing surface.

    Strips two classes of noise that exist for trie's machinery but mean
    nothing to a reader:

    1. **Frontmatter bookkeeping.** The YAML block at the top of every
       triefact carries `trie_version`, `source`, `file_fingerprint`,
       `last_synced_at`, plus the user-facing keys (`description`,
       `defines`, `incoming_refs`, `outgoing_refs`). Only the user-facing
       keys (`AGENT_FRONT_MATTER_KEYS`) survive the render; the rest is
       dropped. When *no* agent-relevant keys are present the frontmatter
       block is omitted entirely rather than emitting a confusing empty
       `---/---` pair.

    2. **Section sentinels.** The `<!-- trie:section ... -->` /
       `<!-- trie:end -->` pairs that wrap each body carry fingerprints
       (`fingerprint=`, `body_fp=`, `source_ref=`) used by the coherence
       checker. None of that helps an agent reading the prose. Sentinels
       are removed entirely; the section bodies they wrapped come through
       as plain Markdown, separated by blank lines, with any inter-section
       prose preserved.

    Robust to legacy / partial triefacts — anything `TriefactFile.parse`
    accepts round-trips here too.
    """
    tf = TriefactFile.parse(text)

    parts: list[str] = []

    # Frontmatter: keep only the agent-relevant keys, preserving their
    # original order from the source file. PyYAML's safe_load honours
    # insertion order, and we feed the subset back to safe_dump with
    # sort_keys=False so what the agent sees mirrors the source order.
    fm_subset = {k: tf.front_matter[k] for k in tf.front_matter if k in AGENT_FRONT_MATTER_KEYS}
    if fm_subset:
        yaml_text = yaml.safe_dump(fm_subset, sort_keys=False, default_flow_style=False)
        parts.append("---\n")
        parts.append(yaml_text)
        parts.append("---\n")

    # Chunks: emit Prose verbatim, emit Section bodies without their
    # sentinels. Insert a blank-line separator between back-to-back
    # sections (where the sentinels used to provide visual separation)
    # so the result is a clean Markdown document instead of bodies
    # butting up against each other.
    prev_was_section = False
    for c in tf.chunks:
        if isinstance(c, Prose):
            parts.append(c.text)
            prev_was_section = False
        else:
            if prev_was_section:
                # Ensure a blank line precedes this section's body.
                tail = parts[-1] if parts else ""
                if not tail.endswith("\n\n"):
                    parts.append("\n" if tail.endswith("\n") else "\n\n")
            parts.append(c.body)
            if not c.body.endswith("\n"):
                parts.append("\n")
            prev_was_section = True

    return "".join(parts)
