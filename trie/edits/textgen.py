"""Plaintext code-generation protocol + parser.

Code generation does NOT go through pydantic structured output. Forcing the
model to emit a whole symbol/file body as an escaped JSON string field (the
``SymbolEdit.source`` / ``FileEdit.content`` approach) is fragile: under load
the model malforms or truncates the JSON and pydantic-ai burns its output
retries before raising ``UnexpectedModelBehavior`` — a ~100s dead end that
aborted whole applies on large files.

Instead we ask the model for plaintext: a single fenced code block (which the
model is already trained to produce flawlessly) followed by optional delimited
prose sections. ``TrieClient.run_text`` returns that text unvalidated, and the
helpers here parse it. pydantic-ai is used only as the API client.

Format the model is asked to produce (single-symbol):

    ```<fence>
    <complete new source>
    ```

    <<<PROSE>>>
    <one-paragraph prose summary>
    <<<END>>>

Multi-symbol / file edit:

    ```<fence>
    <complete updated file content>
    ```

    <<<PROSE qname=path/to/mod:Symbol>>>
    <prose for that symbol>
    <<<END>>>
    <<<PROSE qname=path/to/mod:Other>>>
    <prose for that symbol>
    <<<END>>>
"""

from __future__ import annotations

import re

# Prose-section delimiters. Chosen to be vanishingly unlikely to appear in real
# source or prose, and trivially regex-parseable even if the surrounding text is
# slightly off (extra blank lines, stray prose before/after).
PROSE_OPEN = "<<<PROSE>>>"
PROSE_OPEN_QNAME = "<<<PROSE qname="
PROSE_END = "<<<END>>>"

# Module-level remarks: free-text notes the model emits when the symbol body it
# returned needs a NEW import or other module-level change to compile/work. The
# pipeline does NOT apply these (the symbol body is spliced alone); it collects
# them and returns them in the ApplyReport so the agent can make those small
# file-header edits via the force escape hatch in one pass.
REMARKS_OPEN = "<<<MODULE-REMARKS>>>"
REMARKS_END = "<<<END-REMARKS>>>"

# New external dependencies the model introduced (bare package specifiers it
# imported that the project may not have installed yet). trie does NOT install
# these; it collects + dedups them across the batch and reports them in the
# ApplyReport so the agent installs any missing ones via its shell tool. This
# keeps trie package-manager agnostic.
NEW_DEPS_OPEN = "<<<NEW-DEPS>>>"
NEW_DEPS_END = "<<<END-DEPS>>>"

# A fenced code block: opening fence + optional language, non-greedy body, DOTALL.
# The closing fence is line-anchored (must start at column 0, followed only by
# optional spaces/tabs then a newline or end-of-string) so that triple-backtick
# runs embedded mid-line inside string literals in the generated code — e.g. a
# function that builds a markdown diff fence — don't terminate extraction early
# and truncate the code. An inner fence alone on its own line can still end the
# match early; acceptable residual, models rarely emit that inside code.
_FENCE_RE = re.compile(r"```[^\n]*\n(.*?)\n```[ \t]*(?:\n|$)", re.DOTALL)

_SINGLE_PROSE_RE = re.compile(
    re.escape(PROSE_OPEN) + r"\s*\n(.*?)\n?" + re.escape(PROSE_END),
    re.DOTALL,
)

_QNAME_PROSE_RE = re.compile(
    re.escape(PROSE_OPEN_QNAME)
    + r"(?P<qname>[^>\n]+?)\s*>>>\s*\n(?P<prose>.*?)\n?"
    + re.escape(PROSE_END),
    re.DOTALL,
)

_REMARKS_RE = re.compile(
    re.escape(REMARKS_OPEN) + r"\s*\n(.*?)\n?" + re.escape(REMARKS_END),
    re.DOTALL,
)

_NEW_DEPS_RE = re.compile(
    re.escape(NEW_DEPS_OPEN) + r"\s*\n(.*?)\n?" + re.escape(NEW_DEPS_END),
    re.DOTALL,
)


def code_block_instructions(fence: str) -> str:
    """Instruction fragment telling the model to emit a single fenced code block."""
    return (
        "Return the complete result as a SINGLE fenced code block:\n"
        f"```{fence}\n"
        "<the complete code>\n"
        "```\n"
        "Output the entire code verbatim inside the fence — do not abbreviate, "
        "do not use placeholders like '// ...', do not wrap it in JSON."
    )


def single_prose_instructions() -> str:
    """Instruction fragment for one prose section after the code block."""
    return (
        f"After the code block, on a new line, write the prose summary delimited "
        f"exactly like this:\n{PROSE_OPEN}\n<one short paragraph describing what the "
        f"symbol does at a high level — no bullet points, no implementation notes>\n"
        f"{PROSE_END}"
    )


def new_deps_instructions() -> str:
    """Instruction fragment for declaring new external dependencies."""
    return (
        "If the code introduces a NEW external package (a bare import like "
        "'uuid' or '@scope/pkg' — NOT a relative './' import) that the project may "
        "not have installed, list each package name on its own line in this "
        "OPTIONAL section (omit it entirely if none):\n"
        f"{NEW_DEPS_OPEN}\n"
        "<package-name>\n"
        f"{NEW_DEPS_END}"
    )


def module_remarks_instructions() -> str:
    """Instruction fragment for the optional module-level remarks section.

    The model must keep the code block to the symbol's OWN definition only. If
    that body needs a new import or any other module-level addition/change to
    compile or work, it lists those — in plain language — in this section so the
    agent can make the file-header edits afterward.
    """
    return (
        "The code block above must contain ONLY the symbol's own definition — no "
        "`import` lines, no other top-level declarations (they would be spliced "
        "mid-file and break the parse). If the new/updated body requires a new "
        "import or any module-level change to compile or work, list each one on "
        "its own line in this OPTIONAL section (omit the whole section if none):\n"
        f"{REMARKS_OPEN}\n"
        "<e.g. add: import {{ CustomMix }} from './storage'>\n"
        f"{REMARKS_END}"
    )


def multi_prose_instructions(qnames: list[str]) -> str:
    """Instruction fragment for one delimited prose section per changed symbol."""
    blocks = "\n".join(f"{PROSE_OPEN_QNAME}{qn}>>>\n<prose for {qn}>\n{PROSE_END}" for qn in qnames)
    return (
        "After the code block, write one prose section per changed symbol, each "
        "delimited exactly like this (keep the qname verbatim):\n" + blocks
    )


def parse_code(text: str) -> str:
    """Extract the code from the first fenced block, or fall back to raw text.

    If the model omitted the fence entirely (rare), we treat the whole response,
    minus any trailing prose sections, as the code — better than failing the
    whole apply over a missing pair of backticks.

    The closing fence is only recognised at the start of a line, so
    triple-backticks embedded mid-line inside the code body (e.g. markdown
    fence markers built inside string literals) do not prematurely truncate
    extraction.
    """
    m = _FENCE_RE.search(text)
    if m is not None:
        return m.group(1)
    # No fence: strip prose sections and return the remainder.
    cut = text
    idx = cut.find(PROSE_OPEN_QNAME)
    if idx == -1:
        idx = cut.find(PROSE_OPEN)
    if idx != -1:
        cut = cut[:idx]
    return cut.strip("\n")


def parse_single_prose(text: str) -> str:
    """Extract the single delimited prose section, or empty string if absent."""
    m = _SINGLE_PROSE_RE.search(text)
    return m.group(1).strip() if m else ""


def parse_qname_prose(text: str) -> dict[str, str]:
    """Extract all ``qname=...`` delimited prose sections into a dict."""
    out: dict[str, str] = {}
    for m in _QNAME_PROSE_RE.finditer(text):
        out[m.group("qname").strip()] = m.group("prose").strip()
    return out


def parse_module_remarks(text: str) -> str:
    """Extract the module-level remarks block, or empty string if absent."""
    m = _REMARKS_RE.search(text)
    return m.group(1).strip() if m else ""


def parse_new_deps(text: str) -> list[str]:
    """Extract declared new dependency package names, one per line.

    Strips any leading bullet/quote noise and ignores relative ('.'-prefixed)
    specifiers — only bare package names are dependencies. Returns [] if absent.
    """
    m = _NEW_DEPS_RE.search(text)
    if not m:
        return []
    out: list[str] = []
    for raw in m.group(1).splitlines():
        name = raw.strip().lstrip("-*• ").strip().strip("'\"`").strip()
        if not name or name.startswith("."):
            continue
        out.append(name)
    return out
