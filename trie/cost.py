from __future__ import annotations

import warnings
from dataclasses import dataclass

# Pricing snapshot — sourced from https://docs.anthropic.com/en/docs/about-claude/pricing
# (retrieved 2026-08-30). Update when Anthropic changes rates.
# Cache pricing (5-min TTL): write = 1.25x input, read = 0.1x input.


@dataclass(frozen=True)
class ModelPricing:
    model_id: str
    input_per_mtok: float
    output_per_mtok: float
    cache_write_per_mtok: float
    cache_read_per_mtok: float


def _p(model_id: str, inp: float, out: float) -> ModelPricing:
    """Shorthand: derive 5-min cache write (1.25x) and read (0.1x) from input price."""
    return ModelPricing(
        model_id=model_id,
        input_per_mtok=inp,
        output_per_mtok=out,
        cache_write_per_mtok=inp * 1.25,
        cache_read_per_mtok=inp * 0.10,
    )


# fmt: off
PRICING: dict[str, ModelPricing] = {
    # ── Sonnet family ──────────────────────────────────────────────────
    "anthropic/claude-sonnet-5":            _p("anthropic/claude-sonnet-5",            2.00,  10.00),
    "anthropic/claude-sonnet-4-6":          _p("anthropic/claude-sonnet-4-6",          3.00,  15.00),
    "anthropic/claude-sonnet-4-5":          _p("anthropic/claude-sonnet-4-5",          3.00,  15.00),
    "anthropic/claude-sonnet-4-5-20250929": _p("anthropic/claude-sonnet-4-5-20250929", 3.00,  15.00),
    # ── Haiku family ───────────────────────────────────────────────────
    "anthropic/claude-haiku-4-5":           _p("anthropic/claude-haiku-4-5",           1.00,   5.00),
    "anthropic/claude-haiku-4-5-20251001":  _p("anthropic/claude-haiku-4-5-20251001",  1.00,   5.00),
    # ── Opus family ────────────────────────────────────────────────────
    "anthropic/claude-opus-5":              _p("anthropic/claude-opus-5",              5.00,  25.00),
    "anthropic/claude-opus-4-8":            _p("anthropic/claude-opus-4-8",            5.00,  25.00),
    "anthropic/claude-opus-4-7":            _p("anthropic/claude-opus-4-7",            5.00,  25.00),
    "anthropic/claude-opus-4-6":            _p("anthropic/claude-opus-4-6",            5.00,  25.00),
    "anthropic/claude-opus-4-5":            _p("anthropic/claude-opus-4-5",            5.00,  25.00),
    "anthropic/claude-opus-4-5-20251101":   _p("anthropic/claude-opus-4-5-20251101",   5.00,  25.00),
    # ── Fable family ───────────────────────────────────────────────────
    "anthropic/claude-fable-5":             _p("anthropic/claude-fable-5",            10.00,  50.00),
}
# fmt: on


@dataclass(frozen=True)
class FileEstimate:
    file_path: str
    public_symbols: int
    cache_create_tokens: int
    cache_read_tokens: int
    request_tokens: int
    output_tokens: int
    cost_usd: float


def get_pricing(model_id: str) -> ModelPricing | None:
    pricing = PRICING.get(model_id)
    if pricing is None:
        warnings.warn(
            f"No pricing entry for model {model_id!r} — cost estimates will read $0. "
            "Add the model to PRICING in trie/cost.py or verify the model identifier.",
            stacklevel=2,
        )
    return pricing


def estimate_file_cost(
    *,
    file_path: str,
    cached_prefix_tokens: int,
    public_symbols: int,
    pricing: ModelPricing,
    request_tokens_per_symbol: int = 80,
    output_tokens_per_symbol: int = 200,
) -> FileEstimate:
    """Estimate the cost of generating triefacts for one file.

    `cached_prefix_tokens` should come from the Anthropic `count_tokens` API for the actual
    (system + cached context) payload — see `ModelClient.count_tokens`. The cached prefix
    is paid once on the first symbol via cache_write and reused via cache_read for the
    rest. Output tokens cannot be known ahead of time and are approximated by a constant.
    """
    if public_symbols == 0:
        return FileEstimate(
            file_path=file_path,
            public_symbols=0,
            cache_create_tokens=0,
            cache_read_tokens=0,
            request_tokens=0,
            output_tokens=0,
            cost_usd=0.0,
        )

    cache_create = cached_prefix_tokens
    cache_read = cached_prefix_tokens * max(0, public_symbols - 1)
    request = request_tokens_per_symbol * public_symbols
    output = output_tokens_per_symbol * public_symbols

    cost = (
        cache_create * pricing.cache_write_per_mtok / 1_000_000
        + cache_read * pricing.cache_read_per_mtok / 1_000_000
        + request * pricing.input_per_mtok / 1_000_000
        + output * pricing.output_per_mtok / 1_000_000
    )

    return FileEstimate(
        file_path=file_path,
        public_symbols=public_symbols,
        cache_create_tokens=cache_create,
        cache_read_tokens=cache_read,
        request_tokens=request,
        output_tokens=output,
        cost_usd=cost,
    )


def estimate_actual_cost(
    *,
    cache_creation_input_tokens: int,
    cache_read_input_tokens: int,
    input_tokens: int,
    output_tokens: int,
    pricing: ModelPricing,
) -> float:
    """Compute actual cost from the usage counters returned by an LLM call."""
    return (
        cache_creation_input_tokens * pricing.cache_write_per_mtok / 1_000_000
        + cache_read_input_tokens * pricing.cache_read_per_mtok / 1_000_000
        + input_tokens * pricing.input_per_mtok / 1_000_000
        + output_tokens * pricing.output_per_mtok / 1_000_000
    )
