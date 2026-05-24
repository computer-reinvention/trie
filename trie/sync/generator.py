from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from trie.models import GenerationRequest, ModelClient
from trie.parse.python import Symbol

SYSTEM_PROMPT = """\
You are trie, a documentation generator that writes terse, accurate Markdown summaries of Python source symbols.

Output a single section per symbol. Optimise for token economy: a triefact is only worth its cost if it is meaningfully smaller and more navigable than re-reading the source. Be ruthless.

Format (exactly):
- Line 1: `## \\`<signature>\\`` — the level-2 heading is the symbol's signature in backticks. No name on a separate line, no extra prose on this line.
- Then ONE blank line.
- Then ONE sentence (≤ 25 words) stating what the symbol does. Imperative mood, no hedging, no filler. Example: "Compute the cascade closure for a set of changed files." NOT "This function might be used to..."
- Optionally append a single bulleted list ONLY when a parameter, return value, raised exception, or (for classes/dataclasses) field has semantics that aren't obvious from the type / name. One bullet per item, ≤ 12 words each. Skip the list entirely when the signature speaks for itself.
- Do NOT include a "Description", "Parameters", "Returns", or "Examples" header. Do NOT include code examples — the source is one click away.
- Do NOT mention the file name, module name, or surrounding context. The triefact already carries that metadata.

Hard rules:
- Output ONLY the Markdown body. No front-matter, no sentinel comments, no preambles like "Here is the documentation".
- State what is observable in the source. Do not invent types, callers, or behaviour.
- Use a technical, present-tense voice. No marketing language. No "this function" / "this class" — name the thing if you must, or omit the subject.
- Trivial accessors, dunder methods, and one-line forwards: a single sentence is sufficient. No bullets. No expanded prose. Brevity over completeness.
- For methods and properties: always name the owning class in the prose (e.g. "Close the `Store` connection." not "Close the connection."). This is the only place the class relationship is visible.
- For `@property` methods: describe them as attributes, not as callable functions. Do not say "Return X" — say what X is.
- For `@classmethod` / `@staticmethod`: make clear they are called on the class, not an instance.
- For class symbols: do NOT add any `##` sub-headings for methods inside the class body. Each method has its own separate section — do not duplicate it. You may reference method names in bullet points but never as Markdown headings.
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

When uncertain whether a change is cosmetic or behavioural, prefer preserving the previous prose verbatim. Drift is worse than missing a subtle change — the next sync will catch genuine semantics if they materialise.

If the source change is purely cosmetic, output PREVIOUS_PROSE verbatim. If behavioural, output prose that preserves unchanged information from PREVIOUS_PROSE and reflects the behavioural change. Either way, follow the same formatting rules as a fresh generation.
"""


@dataclass(frozen=True)
class FileGenerationContext:
    file_path: str  # source-root-relative, used for the prompt
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


def build_cached_context(ctx: FileGenerationContext) -> str:
    return (
        f"You are documenting symbols in the file `{ctx.file_path}`. "
        f"Below is the complete source of that file.\n\n"
        f"```python\n{ctx.source_text}\n```"
    )


def _symbol_context_clause(symbol: Symbol) -> str:
    """Return a human-readable clause describing the symbol's kind and class membership.

    Examples:
      "a function"
      "a method of class `Store`"
      "a @property of class `McpCallStats`"
      "a @classmethod of class `Greeter`"
    """
    if symbol.kind == "method" and symbol.parent_class:
        # Surface the most semantically significant decorator (property, classmethod,
        # staticmethod, abstractmethod) so the LLM knows how the method is called.
        significant = {
            "@property",
            "@classmethod",
            "@staticmethod",
            "@abstractmethod",
        }
        label = next(
            (d for d in symbol.decorators if d.split("(")[0] in significant),
            None,
        )
        if label:
            return f"a {label} of class `{symbol.parent_class}`"
        return f"a method of class `{symbol.parent_class}`"
    if symbol.kind == "class" and symbol.decorators:
        dec_str = " ".join(symbol.decorators)
        return f"a class (decorated with {dec_str})"
    return f"a {symbol.kind}"


def _build_request(symbol: Symbol) -> str:
    context = _symbol_context_clause(symbol)
    source_block = _symbol_source(symbol)
    return (
        f"Write the Markdown body for the symbol `{symbol.qualified_name}` "
        f"({context}, lines {symbol.start_line}-{symbol.end_line}).\n\n"
        f"<source>\n{source_block}\n</source>\n\n"
        f"Output the Markdown body only — no front-matter, no sentinels, no surrounding commentary."
    )


def _build_diff_aware_request(
    symbol: Symbol,
    *,
    previous_source: str,
    previous_prose: str,
    current_source: str,
) -> str:
    """Build the user message for diff-aware regen.

    The three labelled blocks (PREVIOUS_SOURCE, PREVIOUS_PROSE, CURRENT_SOURCE) give the
    LLM everything it needs to decide whether the source change is cosmetic or behavioural.
    The rubric (DIFF_AWARE_RUBRIC) is concatenated above the blocks. The closing
    instruction restates the format constraint so the model doesn't slip out of the
    expected output shape.

    Callers pass `previous_source` and `current_source` already containing both the
    signature and the body (so the LLM can see signature-level changes like new
    parameters); this function does not synthesise them from the Symbol object.
    """
    context = _symbol_context_clause(symbol)
    return (
        f"{DIFF_AWARE_RUBRIC}\n"
        f"Symbol: `{symbol.qualified_name}` "
        f"({context}, lines {symbol.start_line}-{symbol.end_line} in the current file).\n\n"
        f"<previous_source>\n{previous_source}\n</previous_source>\n\n"
        f"<previous_prose>\n{previous_prose}\n</previous_prose>\n\n"
        f"<current_source>\n{current_source}\n</current_source>\n\n"
        f"Output the updated Markdown body only — no front-matter, no sentinels, "
        f"no surrounding commentary. If the change is cosmetic, output the previous "
        f"prose verbatim."
    )


def _symbol_source(symbol: Symbol) -> str:
    """Reconstruct the full decorated source block for a Symbol: decorators + signature + body.

    The Symbol's `body_text` excludes the signature and decorators. For diff-aware prompts
    we want the complete block so the LLM can see decorator changes (e.g. `@property` added)
    as well as signature-level changes (new parameter, changed return type). Decorators are
    joined with newlines and prepended before the `signature:\nbody` pair.
    """
    parts: list[str] = []
    if symbol.decorators:
        parts.extend(symbol.decorators)
    parts.append(f"{symbol.signature}:\n{symbol.body_text}")
    return "\n".join(parts)


def generate_section(
    *,
    symbol: Symbol,
    file_ctx: FileGenerationContext,
    client: ModelClient,
    max_tokens: int = 1024,
    previous_source: str | None = None,
    previous_prose: str | None = None,
) -> GeneratedSection:
    """Generate the Markdown body for a single symbol.

    The cached_context portion of the request (system prompt + full source file) is intended
    to be reused across all symbols in the same file via prompt caching, so the per-symbol
    cost is roughly `request_tokens + output_tokens` after the first symbol.

    When both `previous_source` and `previous_prose` are provided, switches to
    diff-aware mode: the request body includes the previous source body, the previous
    prose, and the current source body, plus a rubric instructing the model to
    preserve prose verbatim on cosmetic changes and only update on behavioural ones.
    Cosmetic-vs-behavioural is judged by the model; the prompt anchors strongly toward
    preservation under uncertainty.

    When either previous-* argument is None, falls back to the original cold-write
    prompt — same behaviour as pre-Level-1 trie.
    """
    diff_aware = previous_source is not None and previous_prose is not None
    if diff_aware:
        request_text = _build_diff_aware_request(
            symbol,
            previous_source=previous_source,
            previous_prose=previous_prose,
            current_source=_symbol_source(symbol),
        )
        mode: RegenMode = "diff_aware"
    else:
        request_text = _build_request(symbol)
        mode = "cold"

    req = GenerationRequest(
        system_prompt=SYSTEM_PROMPT,
        cached_context=build_cached_context(file_ctx),
        request=request_text,
        max_tokens=max_tokens,
    )
    resp = client.generate(req)
    return GeneratedSection(
        qualified_name=symbol.qualified_name,
        body=resp.text.strip(),
        input_tokens=resp.input_tokens,
        output_tokens=resp.output_tokens,
        cache_creation_input_tokens=resp.cache_creation_input_tokens,
        cache_read_input_tokens=resp.cache_read_input_tokens,
        mode=mode,
    )
