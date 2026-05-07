from __future__ import annotations

from dataclasses import dataclass

from trie.models import GenerationRequest, ModelClient
from trie.parse.python import Symbol

SYSTEM_PROMPT = """\
You are trie, a documentation generator that writes terse, accurate Markdown summaries of Python source symbols.

Output a single section per symbol. Optimise for token economy: a triefact is only worth its cost if it is meaningfully smaller and more navigable than re-reading the source. Be ruthless.

Format (exactly):
- Line 1: `## \\`<signature>\\`` — the level-2 heading is the symbol's signature in backticks. No name on a separate line, no extra prose on this line.
- Then ONE blank line.
- Then ONE sentence (≤ 25 words) stating what the symbol does. Imperative mood, no hedging, no filler. Example: "Compute the cascade closure for a set of changed files." NOT "This function might be used to..."
- Optionally append a single bulleted list ONLY when a parameter, return value, or raised exception has semantics that aren't obvious from the type / name. One bullet per item, ≤ 12 words each. Skip the list entirely when the signature speaks for itself.
- Do NOT include a "Description", "Parameters", "Returns", or "Examples" header. Do NOT include code examples — the source is one click away.
- Do NOT mention the file name, module name, or surrounding context. The triefact already carries that metadata.

Hard rules:
- Output ONLY the Markdown body. No front-matter, no sentinel comments, no preambles like "Here is the documentation".
- State what is observable in the source. Do not invent types, callers, or behaviour.
- Use a technical, present-tense voice. No marketing language. No "this function" / "this class" — name the thing if you must, or omit the subject.
- Trivial accessors, dunder methods, and one-line forwards: a single sentence is sufficient. No bullets. No expanded prose. Brevity over completeness.
"""


@dataclass(frozen=True)
class FileGenerationContext:
    file_path: str  # source-root-relative, used for the prompt
    source_text: str


@dataclass(frozen=True)
class GeneratedSection:
    qualified_name: str
    body: str
    input_tokens: int
    output_tokens: int
    cache_creation_input_tokens: int
    cache_read_input_tokens: int


def build_cached_context(ctx: FileGenerationContext) -> str:
    return (
        f"You are documenting symbols in the file `{ctx.file_path}`. "
        f"Below is the complete source of that file.\n\n"
        f"```python\n{ctx.source_text}\n```"
    )


def _build_request(symbol: Symbol) -> str:
    return (
        f"Write the Markdown body for the symbol `{symbol.qualified_name}` "
        f"(a {symbol.kind} named `{symbol.name}` defined at lines "
        f"{symbol.start_line}-{symbol.end_line}).\n\n"
        f"Output the Markdown body only — no front-matter, no sentinels, no surrounding commentary."
    )


def generate_section(
    *,
    symbol: Symbol,
    file_ctx: FileGenerationContext,
    client: ModelClient,
    max_tokens: int = 1024,
) -> GeneratedSection:
    """Generate the Markdown body for a single symbol.

    The cached_context portion of the request (system prompt + full source file) is intended
    to be reused across all symbols in the same file via prompt caching, so the per-symbol
    cost is roughly `request_tokens + output_tokens` after the first symbol.
    """
    req = GenerationRequest(
        system_prompt=SYSTEM_PROMPT,
        cached_context=build_cached_context(file_ctx),
        request=_build_request(symbol),
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
    )
