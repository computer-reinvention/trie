"""Plain-text rendering for tool envelopes — the default output format on
every interaction surface.

Agents read tool output; they don't parse it. JSON envelopes made them pay
for braces, escaped newlines (`\\n` inside prose that IS markdown), unicode
escapes (`\\u2026` for an ellipsis), and repeated keys on every query. This
module renders the same envelopes as dense readable text: symbol dicts become
compact records, prose fields print verbatim, call chains join with arrows,
scalars become `key: value` lines.

Consumed by two surfaces:
  - the CLI's `_print_plain` renderer (raw structure stays available behind
    `--json` on every query command), and
  - the MCP server's query-tool registrations, which wrap the dict-returning
    `TrieTools` methods and send text over the wire (the methods themselves
    keep returning dicts, so tests and programmatic callers are unaffected).

Pure string-building — no rich, no console, no I/O — so both surfaces and
the tests can call it without a terminal in the loop.
"""

from __future__ import annotations

PROSE_KEYS = frozenset(
    {"prose", "story", "usage_story", "narrative", "note", "prose_snippet", "next"}
)
"""Envelope keys whose values are prose/markdown: rendered verbatim as blocks,
never squeezed onto one line."""


def _squeeze(text: str, cap: int = 160) -> str:
    """Collapse whitespace runs (multi-line signatures!) to one line, capped."""
    out = " ".join(str(text).split())
    return out if len(out) <= cap else out[: cap - 1] + "…"


def _prose_block(text: str, indent: str) -> list[str]:
    return [f"{indent}{line}" if line.strip() else "" for line in text.strip().splitlines()]


def _is_chain(value: list) -> bool:
    """A call-chain: a list of ≥2 qname-shaped strings."""
    return (
        len(value) >= 2
        and all(isinstance(x, str) for x in value)
        and all(":" in x and " " not in x for x in value)
    )


def _symbol_record(rec: dict, indent: str) -> list[str]:
    """One symbol as a compact record: header line + squeezed signature + one-liner.

    The header packs qname, kind, pointer, and numeric metrics into one line;
    the signature is whitespace-collapsed (a multi-line typer signature used
    to cost ~200 tokens of escaped JSON for zero information).
    """
    parts = [str(rec.get("qname", ""))]
    if rec.get("kind"):
        parts.append(str(rec["kind"]))
    pointer = rec.get("file_pointer") or rec.get("source_pointer")
    if pointer:
        parts.append(str(pointer))
    metrics: list[str] = []
    if rec.get("inbound_count") is not None:
        metrics.append(f"in:{rec['inbound_count']}")
    if rec.get("outbound_count") is not None:
        metrics.append(f"out:{rec['outbound_count']}")
    if rec.get("score") is not None:
        metrics.append(f"score:{rec['score']}")
    hits_in_body = rec.get("match_count") or rec.get("text_match_hits_in_body")
    if hits_in_body:
        metrics.append(f"matches:{hits_in_body}")
    if rec.get("pending_patch_count"):
        metrics.append(f"pending_patches:{rec['pending_patch_count']}")
    if metrics:
        parts.append(" ".join(metrics))
    lines = [indent + "  ".join(p for p in parts if p)]
    if rec.get("signature"):
        lines.append(f"{indent}    {_squeeze(rec['signature'])}")
    if rec.get("one_liner"):
        lines.append(f"{indent}    {str(rec['one_liner']).strip()}")
    for prose_key in ("prose_snippet", "prose"):
        if rec.get(prose_key):
            lines.extend(_prose_block(str(rec[prose_key]), indent + "    "))
    return lines


_RECORD_KEYS = frozenset(
    {
        "qname",
        "kind",
        "file_pointer",
        "source_pointer",
        "signature",
        "one_liner",
        "inbound_count",
        "outbound_count",
        "score",
        "match_count",
        "text_match_hits_in_body",
        "pending_patch_count",
        "is_public",
        "has_pending_patches",
        "prose_snippet",
        "prose",
    }
)


def _render_value(key: str, value: object, indent: str) -> list[str]:
    """Render one envelope entry as text lines; recurse for containers."""
    if isinstance(value, str):
        if key in PROSE_KEYS or "\n" in value:
            return [f"{indent}{key}:", *_prose_block(value, indent + "  ")]
        return [f"{indent}{key}: {value}"]
    if isinstance(value, dict):
        if "qname" in value and set(value) <= _RECORD_KEYS:
            return [f"{indent}{key}:", *_symbol_record(value, indent + "  ")]
        lines = [f"{indent}{key}:"]
        # A dict with a qname but extra non-record keys (e.g. explain_symbol's
        # top-level shape nested somewhere): render record fields first, then
        # the rest generically.
        for k, v in value.items():
            lines.extend(_render_value(str(k), v, indent + "  "))
        return lines
    if isinstance(value, list):
        if not value:
            return [f"{indent}{key}: (none)"]
        if _is_chain(value):
            return [f"{indent}{key}: " + " → ".join(str(x) for x in value)]
        if all(isinstance(x, list) for x in value):
            # e.g. trace_flow paths: a list of call chains.
            lines = [f"{indent}{key} ({len(value)}):"]
            for i, chain in enumerate(value, 1):
                if _is_chain(chain):
                    lines.append(f"{indent}  {i}. " + " → ".join(str(x) for x in chain))
                else:
                    lines.extend(_render_value(str(i), chain, indent + "  "))
            return lines
        if all(isinstance(x, dict) for x in value):
            lines = [f"{indent}{key} ({len(value)}):"]
            for item in value:
                if "qname" in item and set(item) <= _RECORD_KEYS:
                    lines.extend(_symbol_record(item, indent + "  "))
                else:
                    for k, v in item.items():
                        lines.extend(_render_value(str(k), v, indent + "  "))
                    lines.append("")
            while lines and not lines[-1]:
                lines.pop()
            return lines
        return [f"{indent}- {x}" for x in value]
    return [f"{indent}{key}: {value}"]


def render_envelope(envelope: dict) -> str:
    """Render a tool envelope as dense readable text.

    Error envelopes render as `error <code>: <message>` plus the suggestion.
    The explain tools weave callers/callees INTO their story prose, so when a
    story field is present the raw record arrays are dropped — printing both
    repeated every line of the story (the raw structure stays available via
    `--json` / the underlying `TrieTools` dicts).
    """
    err = envelope.get("error")
    if isinstance(err, dict):
        lines = [f"error {err.get('code', '?')}: {err.get('message', '')}"]
        if err.get("suggestion"):
            lines.append(f"  {err['suggestion']}")
        return "\n".join(lines)

    skip: set[str] = set()
    if envelope.get("story") or envelope.get("usage_story"):
        skip = {"callers", "callees"}

    lines: list[str] = []
    for key, value in envelope.items():
        if key in skip:
            continue
        lines.extend(_render_value(str(key), value, ""))
    return "\n".join(lines)
