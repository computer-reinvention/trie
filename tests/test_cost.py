from __future__ import annotations

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
    assert get_pricing("openai/some-future-model") is None


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
