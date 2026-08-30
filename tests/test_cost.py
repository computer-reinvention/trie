from __future__ import annotations

import warnings

import pytest

from trie.cost import (
    PRICING,
    estimate_actual_cost,
    estimate_file_cost,
    get_pricing,
)


def test_get_pricing_known():
    p = get_pricing("anthropic/claude-sonnet-4-6")
    assert p is not None
    assert p.input_per_mtok == 3.00
    assert p.output_per_mtok == 15.00


def test_get_pricing_unknown():
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        assert get_pricing("openai/some-future-model") is None
        assert len(w) == 1
        assert "No pricing entry" in str(w[0].message)


def test_get_pricing_unknown_emits_warning():
    """An unrecognized model should trigger a visible warning, not silently return None."""
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        get_pricing("anthropic/claude-hypothetical-99")
        assert len(w) == 1
        assert "claude-hypothetical-99" in str(w[0].message)


def test_zero_public_symbols_costs_nothing():
    p = PRICING["anthropic/claude-sonnet-4-6"]
    est = estimate_file_cost(
        file_path="empty.py", cached_prefix_tokens=0, public_symbols=0, pricing=p
    )
    assert est.cost_usd == 0.0
    assert est.cache_create_tokens == 0


def test_single_symbol_only_pays_cache_create():
    p = PRICING["anthropic/claude-sonnet-4-6"]
    est = estimate_file_cost(
        file_path="x.py",
        cached_prefix_tokens=250,
        public_symbols=1,
        pricing=p,
    )
    assert est.cache_create_tokens == 250
    assert est.cache_read_tokens == 0  # nothing to read on the first call


def test_multiple_symbols_amortize_via_cache():
    """Two-symbol cost should be far less than 2x single-symbol cost thanks to cache reads."""
    p = PRICING["anthropic/claude-sonnet-4-6"]
    one = estimate_file_cost(
        file_path="x.py", cached_prefix_tokens=2000, public_symbols=1, pricing=p
    )
    two = estimate_file_cost(
        file_path="x.py", cached_prefix_tokens=2000, public_symbols=2, pricing=p
    )
    # Cache read at 0.1x input is cheap; second symbol should cost much less than the first.
    assert two.cost_usd < 1.5 * one.cost_usd


def test_haiku_cheaper_than_sonnet():
    sonnet = PRICING["anthropic/claude-sonnet-4-6"]
    haiku = PRICING["anthropic/claude-haiku-4-5-20251001"]
    s = estimate_file_cost(
        file_path="x.py", cached_prefix_tokens=1000, public_symbols=5, pricing=sonnet
    )
    h = estimate_file_cost(
        file_path="x.py", cached_prefix_tokens=1000, public_symbols=5, pricing=haiku
    )
    assert h.cost_usd < s.cost_usd


def test_estimate_actual_cost_matches_pricing():
    p = PRICING["anthropic/claude-sonnet-4-6"]
    cost = estimate_actual_cost(
        cache_creation_input_tokens=1000,
        cache_read_input_tokens=4000,
        input_tokens=500,
        output_tokens=200,
        pricing=p,
    )
    expected = (
        1000 * 3.75 / 1_000_000
        + 4000 * 0.30 / 1_000_000
        + 500 * 3.00 / 1_000_000
        + 200 * 15.00 / 1_000_000
    )
    assert cost == pytest.approx(expected)


# ---------------------------------------------------------------------------
# Regression: every model configurable in trie.toml must have pricing
# ---------------------------------------------------------------------------

# Models that trie's default config, CLI docs, and real-world trie.toml files
# reference. A new model added to trie's supported surface without a pricing
# entry would silently report $0 cost — the exact bug this test catches.
_EXPECTED_MODELS = [
    "anthropic/claude-sonnet-5",
    "anthropic/claude-sonnet-4-6",
    "anthropic/claude-sonnet-4-5",
    "anthropic/claude-sonnet-4-5-20250929",
    "anthropic/claude-haiku-4-5",
    "anthropic/claude-haiku-4-5-20251001",
    "anthropic/claude-opus-5",
    "anthropic/claude-opus-4-8",
    "anthropic/claude-opus-4-7",
    "anthropic/claude-opus-4-6",
    "anthropic/claude-opus-4-5",
    "anthropic/claude-opus-4-5-20251101",
    "anthropic/claude-fable-5",
]


@pytest.mark.parametrize("model_id", _EXPECTED_MODELS)
def test_every_known_model_has_pricing(model_id: str):
    """Every model in the supported set must have a non-zero pricing entry."""
    p = PRICING.get(model_id)
    assert p is not None, f"missing PRICING entry for {model_id}"
    assert p.input_per_mtok > 0
    assert p.output_per_mtok > 0
    assert p.cache_write_per_mtok > 0
    assert p.cache_read_per_mtok > 0


def test_sonnet_5_pricing_is_correct():
    """Claude Sonnet 5 pricing: $2/MTok input, $10/MTok output (source: docs.anthropic.com)."""
    p = PRICING["anthropic/claude-sonnet-5"]
    assert p.input_per_mtok == 2.00
    assert p.output_per_mtok == 10.00
    assert p.cache_write_per_mtok == pytest.approx(2.50)  # 1.25x input
    assert p.cache_read_per_mtok == pytest.approx(0.20)  # 0.1x input


def test_cache_pricing_follows_multiplier_convention():
    """All entries must use 1.25x input for cache write and 0.1x input for cache read."""
    for model_id, p in PRICING.items():
        assert p.cache_write_per_mtok == pytest.approx(p.input_per_mtok * 1.25), (
            f"{model_id}: cache_write should be 1.25x input"
        )
        assert p.cache_read_per_mtok == pytest.approx(p.input_per_mtok * 0.10), (
            f"{model_id}: cache_read should be 0.1x input"
        )


def test_default_config_models_have_pricing():
    """The default models in Config.models must have pricing entries."""
    from trie.config import Models

    defaults = Models()
    for field_name in ("bootstrap", "cascade"):
        model_id = getattr(defaults, field_name)
        assert model_id in PRICING, (
            f"Config.models.{field_name} default {model_id!r} has no PRICING entry"
        )
