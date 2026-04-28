from __future__ import annotations

from dataclasses import dataclass

from trie.models import GenerationRequest, ModelClient
from trie.parse.python import Symbol

SYSTEM_PROMPT = """\
You are trie, a documentation generator that writes concise, accurate Markdown for Python source symbols.

Rules:
- Output ONLY the Markdown body for the requested symbol. No front-matter, no sentinel comments, no preamble like "Here is the doc...".
- Begin with a level-2 heading containing the symbol name and signature in backticks: `## \\`<signature>\\``.
- Follow with a single short paragraph (1-3 sentences) describing the symbol's role.
- If the parameters or return value have semantics worth highlighting, add a short bulleted list. Skip the list when the signature is self-explanatory.
- Be precise: do not invent function names, types, or relationships absent from the source. State what is observable, not what you guess.
- Use a technical voice. No hedging ("might", "perhaps"), no marketing tone.
- Code examples are off by default. Include one only if the symbol's usage pattern is genuinely non-obvious from the signature.
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


def _build_cached_context(ctx: FileGenerationContext) -> str:
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
        cached_context=_build_cached_context(file_ctx),
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
