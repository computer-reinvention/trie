from __future__ import annotations

from dataclasses import dataclass

# Pricing snapshot as of 2026-04. Update when providers change rates.
# Cache pricing (Anthropic): write = 1.25x input, read = 0.1x input.


@dataclass(frozen=True)
class ModelPricing:
    model_id: str
    input_per_mtok: float
    output_per_mtok: float
    cache_write_per_mtok: float
    cache_read_per_mtok: float


PRICING: dict[str, ModelPricing] = {
    "anthropic/claude-sonnet-4-6": ModelPricing(
        model_id="anthropic/claude-sonnet-4-6",
        input_per_mtok=3.00,
        output_per_mtok=15.00,
        cache_write_per_mtok=3.75,
        cache_read_per_mtok=0.30,
    ),
    "anthropic/claude-haiku-4-5-20251001": ModelPricing(
        model_id="anthropic/claude-haiku-4-5-20251001",
        input_per_mtok=1.00,
        output_per_mtok=5.00,
        cache_write_per_mtok=1.25,
        cache_read_per_mtok=0.10,
    ),
    "anthropic/claude-opus-4-7": ModelPricing(
        model_id="anthropic/claude-opus-4-7",
        input_per_mtok=15.00,
        output_per_mtok=75.00,
        cache_write_per_mtok=18.75,
        cache_read_per_mtok=1.50,
    ),
}


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
    return PRICING.get(model_id)


def estimate_tokens(text: str) -> int:
    """Rough token count: ~4 chars per token. Conservative for Python source.

    Anthropic's tokenizer is closer to 3.5 chars per token for code; using 4 errs slightly
    on the low side. The estimate is for plan/budget UX, not billing — actual cost is
    reported after the fact from the API's usage counters.
    """
    return max(1, len(text) // 4)


def estimate_file_cost(
    *,
    file_path: str,
    source_text: str,
    public_symbols: int,
    pricing: ModelPricing,
    system_prompt_tokens: int = 200,
    request_tokens_per_symbol: int = 80,
    output_tokens_per_symbol: int = 200,
) -> FileEstimate:
    """Estimate the cost of generating docs for one file.

    Assumes the cached prefix (system prompt + full source file) is paid once on the first
    symbol and reused via cache reads for the remaining symbols in the same file.
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

    cached_prefix_tokens = estimate_tokens(source_text) + system_prompt_tokens
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
