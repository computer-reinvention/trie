from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from trie.models import RoleTag, SectionBody, TrieClient
from trie.parse.python import Symbol

# Domain knowledge — what makes good triefact prose.
# NO format instructions: the SectionBody Pydantic model defines the output
# shape, and the LLM uses tool-calling to produce a valid body.
SYSTEM_PROMPT = """\
You are trie, a documentation generator that writes terse, accurate Markdown summaries of Python source symbols.

Write a single section per symbol. Optimise for token economy: a triefact is only worth its cost if it is meaningfully smaller and more navigable than re-reading the source.

Guidelines:
- One sentence (≤ 25 words) stating what the symbol does. Imperative mood, no hedging, no filler.
- Optionally add a single bulleted list ONLY when a parameter, return value, raised exception, or (for classes/dataclasses) field has semantics that aren't obvious from the type or name. One bullet per item, ≤ 12 words each.
- Do not include code examples — the source is one click away.
- State what is observable in the source. Do not invent types, callers, or behaviour.
- Use a technical, present-tense voice. No marketing language.
- Trivial accessors, dunder methods, and one-line forwards: a single sentence is sufficient.
- For methods and properties: always name the owning class in the prose.
- For @property methods: describe them as attributes, not as callable functions.
- For @classmethod / @staticmethod: make clear they are called on the class, not an instance.
- For class symbols: do not add sub-headings for methods inside the class body.

Also classify the symbol's architectural role via the `role` field. Pick the single most specific role describing what the symbol primarily does, preferring the standard vocabulary listed in the field description. The role drives how the symbol is grouped in the graph view, so be consistent: symbols doing the same kind of work should get the same role.
"""

# Diff-aware regeneration rubric. Prepended to the user message when we have both
# the previous source and the previous prose. The goal is to anchor the LLM toward
# "preserve unless behaviour actually changed" so cosmetic edits (renames, formatting,
# comment churn) don't trigger paraphrase drift in the prose.
DIFF_AWARE_RUBRIC = """\
A previous version of this symbol's prose already exists, written against a previous version of the source. Your job is to update the prose only if the *behaviour* of the symbol has changed. Cosmetic changes must not change the prose.

Cosmetic changes (do NOT change the prose):
- Renaming local variables, parameters, or private helpers
- Whitespace, formatting, line breaks, comment edits
- Reordering statements when the order doesn't affect behaviour
- Replacing one local construct with a semantically equivalent one
- Adding or refining type hints that don't change runtime semantics

Behavioural changes (MUST be reflected in the prose):
- New branches, new return paths, new raised exceptions
- Changed return type or shape (not just hint, actual structure)
- New or removed side effects (I/O, mutation, logging, telemetry)
- New or removed external calls
- Changed invariants, preconditions, or error handling
- Changed parameters in number or meaning (renaming alone is cosmetic; semantic change is not)

When uncertain whether a change is cosmetic or behavioural, prefer preserving the previous prose verbatim.
"""


@dataclass(frozen=True)
class FileGenerationContext:
    file_path: str
    source_text: str


RegenMode = Literal["cold", "diff_aware"]


@dataclass(frozen=True)
class GeneratedSection:
    qualified_name: str
    body: str
    input_tokens: int
    output_tokens: int
    cache_creation_input_tokens: int
    cache_read_input_tokens: int
    mode: RegenMode = "cold"
    role: str = ""
    boundary: str = ""


def build_cached_context(ctx: FileGenerationContext) -> str:
    return (
        f"You are documenting symbols in the file `{ctx.file_path}`. "
        f"Below is the complete source of that file.\n\n"
        f"```python\n{ctx.source_text}\n```"
    )


def _symbol_context_clause(symbol: Symbol) -> str:
    if symbol.kind == "method" and symbol.parent_class:
        significant = {"@property", "@classmethod", "@staticmethod", "@abstractmethod"}
        label = next((d for d in symbol.decorators if d.split("(")[0] in significant), None)
        if label:
            return f"a {label} of class `{symbol.parent_class}`"
        return f"a method of class `{symbol.parent_class}`"
    if symbol.kind == "class" and symbol.decorators:
        dec_str = " ".join(symbol.decorators)
        return f"a class (decorated with {dec_str})"
    return f"a {symbol.kind}"


def _symbol_source(symbol: Symbol) -> str:
    parts: list[str] = []
    if symbol.decorators:
        parts.extend(symbol.decorators)
    parts.append(f"{symbol.signature}:\n{symbol.body_text}")
    return "\n".join(parts)


def _build_request(symbol: Symbol) -> str:
    context = _symbol_context_clause(symbol)
    source_block = _symbol_source(symbol)
    return (
        f"Write the Markdown body for the symbol `{symbol.qualified_name}` "
        f"({context}, lines {symbol.start_line}-{symbol.end_line}).\n\n"
        f"<source>\n{source_block}\n</source>"
    )


def _build_diff_aware_request(
    symbol: Symbol,
    *,
    previous_source: str,
    previous_prose: str,
    current_source: str,
) -> str:
    context = _symbol_context_clause(symbol)
    return (
        f"{DIFF_AWARE_RUBRIC}\n"
        f"Symbol: `{symbol.qualified_name}` "
        f"({context}, lines {symbol.start_line}-{symbol.end_line} in the current file).\n\n"
        f"<previous_source>\n{previous_source}\n</previous_source>\n\n"
        f"<previous_prose>\n{previous_prose}\n</previous_prose>\n\n"
        f"<current_source>\n{current_source}\n</current_source>"
    )


def generate_section(
    *,
    symbol: Symbol,
    file_ctx: FileGenerationContext,
    client: TrieClient,
    max_tokens: int = 1024,
    previous_source: str | None = None,
    previous_prose: str | None = None,
) -> GeneratedSection:
    diff_aware = previous_source is not None and previous_prose is not None
    if diff_aware:
        user_prompt = _build_diff_aware_request(
            symbol,
            previous_source=previous_source,
            previous_prose=previous_prose,
            current_source=_symbol_source(symbol),
        )
        mode: RegenMode = "diff_aware"
    else:
        user_prompt = _build_request(symbol)
        mode = "cold"

    result = client.run(
        SectionBody,
        system_prompt=SYSTEM_PROMPT,
        user_prompt=user_prompt,
        cache_prefix=build_cached_context(file_ctx),
        max_tokens=max_tokens,
    )
    section_body: SectionBody = result.output
    return GeneratedSection(
        qualified_name=symbol.qualified_name,
        body=section_body.body,
        input_tokens=result.input_tokens,
        output_tokens=result.output_tokens,
        cache_creation_input_tokens=result.cache_creation_input_tokens,
        cache_read_input_tokens=result.cache_read_input_tokens,
        mode=mode,
        role=section_body.role.strip().lower(),
        boundary=section_body.boundary.strip().lower(),
    )


ROLE_SYSTEM_PROMPT = """\
You are trie, classifying the architectural role of a Python source symbol against
a fixed, project-specific role vocabulary supplied in the prompt.

You are given the allowed roles, the symbol's source, and (when available) its
existing documentation prose. Return ONLY the classification fields — do not write
any prose. Pick exactly one role NAME from the supplied vocabulary; never invent a
new name. Judge by what the symbol actually does in the source. Be consistent:
symbols doing the same kind of work get the same role.
"""


@dataclass(frozen=True)
class InferredRole:
    """Role/boundary classification for one symbol, plus the call's token usage."""

    qualified_name: str
    role: str
    boundary: str
    input_tokens: int
    output_tokens: int
    cache_creation_input_tokens: int
    cache_read_input_tokens: int


def _taxonomy_clause(allowed_roles: list[tuple[str, str]]) -> str:
    """Render the fixed role vocabulary into the prompt. Each entry is (name, desc)."""
    lines = [f"- {name}: {desc}" if desc else f"- {name}" for name, desc in allowed_roles]
    return "Choose exactly one role from this vocabulary:\n" + "\n".join(lines)


def infer_role(
    *,
    symbol: Symbol,
    file_ctx: FileGenerationContext,
    client: TrieClient,
    allowed_roles: list[tuple[str, str]],
    existing_prose: str | None = None,
    max_tokens: int = 128,
) -> InferredRole:
    """Classify a symbol against a fixed role vocabulary, without regenerating prose.

    This is the per-symbol unit of `trie sync --roles-only` (pass 2). `allowed_roles`
    is the derived taxonomy as `(name, description)` pairs — injected into the prompt
    so the model picks one existing role rather than coining a new one. Reuses the
    cached file context (source billed once per file) and feeds the symbol's existing
    prose as an extra signal. The output is role + boundary only, so the call stays
    tiny relative to a full section regeneration.
    """
    prose_clause = (
        f"\n\n<existing_prose>\n{existing_prose}\n</existing_prose>" if existing_prose else ""
    )
    user_prompt = (
        f"{_taxonomy_clause(allowed_roles)}\n\n"
        f"Classify the symbol `{symbol.qualified_name}` "
        f"({_symbol_context_clause(symbol)}, lines {symbol.start_line}-{symbol.end_line}).\n\n"
        f"<source>\n{_symbol_source(symbol)}\n</source>{prose_clause}"
    )
    result = client.run(
        RoleTag,
        system_prompt=ROLE_SYSTEM_PROMPT,
        user_prompt=user_prompt,
        cache_prefix=build_cached_context(file_ctx),
        max_tokens=max_tokens,
    )
    tag: RoleTag = result.output
    # Clamp to the vocabulary: if the model returns a name outside the taxonomy
    # (rare, but the field is a free string), drop it to "" rather than pollute the
    # role axis with a one-off. "" is treated as untagged downstream.
    role = tag.role.strip().lower()
    allowed_names = {name for name, _ in allowed_roles}
    if role and role not in allowed_names:
        role = ""
    return InferredRole(
        qualified_name=symbol.qualified_name,
        role=role,
        boundary=tag.boundary.strip().lower(),
        input_tokens=result.input_tokens,
        output_tokens=result.output_tokens,
        cache_creation_input_tokens=result.cache_creation_input_tokens,
        cache_read_input_tokens=result.cache_read_input_tokens,
    )
