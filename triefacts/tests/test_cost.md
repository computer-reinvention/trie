---
trie_version: 0.1.5
source: tests/test_cost.py
file_fingerprint: 56d003bc1c51065a50091fc9753ea5136e0956ccf0df15638afb26e1b9d064d3
last_synced_at: '2026-06-03T20:53:18Z'
defines:
- kind: module
  qualified_name: tests/test_cost:__module__
  lines: 1-86
- kind: function
  qualified_name: tests/test_cost:test_get_pricing_known
  lines: 13-17
- kind: function
  qualified_name: tests/test_cost:test_get_pricing_unknown
  lines: 20-21
- kind: function
  qualified_name: tests/test_cost:test_zero_public_symbols_costs_nothing
  lines: 24-30
- kind: function
  qualified_name: tests/test_cost:test_single_symbol_only_pays_cache_create
  lines: 33-42
- kind: function
  qualified_name: tests/test_cost:test_multiple_symbols_amortize_via_cache
  lines: 45-55
- kind: function
  qualified_name: tests/test_cost:test_haiku_cheaper_than_sonnet
  lines: 58-67
- kind: function
  qualified_name: tests/test_cost:test_estimate_actual_cost_matches_pricing
  lines: 70-85
incoming_refs: 0
outgoing_refs: 12
---
<!-- trie:section symbol=tests/test_cost:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=600a0a19dcc95f289780fa41db20072fd600534e37d4bae2306b672222f3b035 source_ref=5dfe03cdd4810107b784dfce8ae2ed82de50b669 -->
Tests cost estimation functions for LLM API pricing calculations and token usage optimization.

- `test_get_pricing_known` — verifies pricing retrieval for known models returns correct rates
- `test_get_pricing_unknown` — confirms None return for unrecognized model names
- `test_zero_public_symbols_costs_nothing` — validates zero-cost estimation for empty files
- `test_single_symbol_only_pays_cache_create` — checks cache creation cost for single symbol processing
- `test_multiple_symbols_amortize_via_cache` — demonstrates cost savings from cache reads with multiple symbols
- `test_haiku_cheaper_than_sonnet` — compares pricing between different model tiers
- `test_estimate_actual_cost_matches_pricing` — validates actual cost calculation against expected pricing formulas
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cost:test_get_pricing_known fingerprint=bbd02a076da541cef07fa6081976ed6de9aaf330ae33ec2a51c75d2db8c710cc body_fp=511827137317ec8a04fda420b060dd27834dd3a89eda2395b3fde59015d67caa source_ref=5dfe03cdd4810107b784dfce8ae2ed82de50b669 -->
Tests that `get_pricing` returns correct pricing data for a known model identifier.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cost:test_get_pricing_unknown fingerprint=90e9070ea2d577508b09545ff08ba8518602b92df10e12cbb92f96127a284d58 body_fp=9b21660a77c6e065fa34938edcf1698edc61b27373daaa5ca25332ed9e8cdf12 source_ref=5dfe03cdd4810107b784dfce8ae2ed82de50b669 -->
Tests that `get_pricing` returns `None` when queried for an unknown model identifier.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cost:test_zero_public_symbols_costs_nothing fingerprint=2ea2b94a267c2897ce389247503958f55e5e14e2fa34592471ee2882ede9ece2 body_fp=bae8cf50c618dfbf2d527ee12772402cc256d9b13314aa6492467e8cf96e5b48 source_ref=5dfe03cdd4810107b784dfce8ae2ed82de50b669 -->
Verifies that `estimate_file_cost` returns zero cost and cache tokens when no public symbols exist.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cost:test_single_symbol_only_pays_cache_create fingerprint=3c5d08ddba36f5818e5149e2711a37784ba4d691d5da9a218d06d1ac14700662 body_fp=f9589535693508958b665c70fabb9f0448555ef4c1f4b01f0fba8786e4246345 source_ref=5dfe03cdd4810107b784dfce8ae2ed82de50b669 -->
Tests that processing a single symbol requires only cache creation tokens with no cache reads.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cost:test_multiple_symbols_amortize_via_cache fingerprint=cc5a746bba0718b6cb0001d6bc37beb464207197d0a2652a42a4d977e637dcce body_fp=ee4234fa413b226260900aefaa99a529ef5d4db143bf53fdfa41d6bc83f3c577 source_ref=5dfe03cdd4810107b784dfce8ae2ed82de50b669 -->
Verifies that processing multiple symbols benefits from caching by comparing two-symbol cost against single-symbol cost.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cost:test_haiku_cheaper_than_sonnet fingerprint=92a67d6cd74211b78c4e308d2b0e42bac7bd60326f08acad5a2cfab355352edf body_fp=677d3401317e61ec8355910fe1fa17c130c4af9c2a0808e0b866c9f61207afee source_ref=5dfe03cdd4810107b784dfce8ae2ed82de50b669 -->
Verifies that Haiku pricing produces lower file documentation costs than Sonnet pricing for identical inputs.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cost:test_estimate_actual_cost_matches_pricing fingerprint=1ec34314487a54cd97ef862b8dd5bbfe131dd0a0b383382192ada3f3cde40da9 body_fp=0ba0489dbb4f891ed362b3325e9e3b506e337541a07b1cf14d419b02c59a75f7 source_ref=5dfe03cdd4810107b784dfce8ae2ed82de50b669 -->
Verifies that `estimate_actual_cost` correctly calculates total costs using pricing rates for different token types.
<!-- trie:end -->