---
trie_version: 0.1.5
source: tests/test_cost.py
file_fingerprint: 56d003bc1c51065a50091fc9753ea5136e0956ccf0df15638afb26e1b9d064d3
last_synced_at: '2026-06-06T13:16:18Z'
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
<!-- trie:section symbol=tests/test_cost:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=79bc44dab98cf1a69d69538faa9b7dd0d8abe8280dc4d36888374f99d13d4d88 source_ref=5dfe03cdd4810107b784dfce8ae2ed82de50b669 role=test-infrastructure -->
Tests cost estimation functions from the `trie.cost` module, verifying pricing lookups, file cost calculations, and cache optimization behavior.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cost:test_get_pricing_known fingerprint=bbd02a076da541cef07fa6081976ed6de9aaf330ae33ec2a51c75d2db8c710cc body_fp=42c0f772e8cebf01452e181be18752d4e706a66dbc5d5aa2d041b377805cf0cf source_ref=5dfe03cdd4810107b784dfce8ae2ed82de50b669 role=test-infrastructure -->
Verifies that get_pricing returns correct pricing data for a known model.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cost:test_get_pricing_unknown fingerprint=90e9070ea2d577508b09545ff08ba8518602b92df10e12cbb92f96127a284d58 body_fp=f4f5288e1d7e56e07e11830351cea3546e1bd39a80e75d94bba81b36f8c8c8fa source_ref=5dfe03cdd4810107b784dfce8ae2ed82de50b669 role=test-infrastructure -->
Tests that `get_pricing` returns `None` for unknown model names.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cost:test_zero_public_symbols_costs_nothing fingerprint=2ea2b94a267c2897ce389247503958f55e5e14e2fa34592471ee2882ede9ece2 body_fp=1574426381a7b1627c1e1458f0d515d166202b21771b861e5ffec1e077d30812 source_ref=5dfe03cdd4810107b784dfce8ae2ed82de50b669 role=monitoring-telemetry -->
Verifies that estimating cost for a file with zero public symbols returns zero cost and cache tokens.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cost:test_single_symbol_only_pays_cache_create fingerprint=3c5d08ddba36f5818e5149e2711a37784ba4d691d5da9a218d06d1ac14700662 body_fp=6f384bb9e80d13c122a3c319b3742fb1eee94904b4d518129df505bae6a48677 source_ref=5dfe03cdd4810107b784dfce8ae2ed82de50b669 role=monitoring-telemetry -->
Tests that a file with one symbol creates cache tokens without reading cache on first call.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cost:test_multiple_symbols_amortize_via_cache fingerprint=cc5a746bba0718b6cb0001d6bc37beb464207197d0a2652a42a4d977e637dcce body_fp=3977450718248b7048080591cbaf39e9984cb716dafead22ab4e09432a993b22 source_ref=5dfe03cdd4810107b784dfce8ae2ed82de50b669 role=monitoring-telemetry -->
Tests that processing multiple symbols in a file benefits from cache read cost savings.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cost:test_haiku_cheaper_than_sonnet fingerprint=92a67d6cd74211b78c4e308d2b0e42bac7bd60326f08acad5a2cfab355352edf body_fp=2fe995c258b1eb643cc556c67a1047a58fc58c6175fd68f0f3394f149301f234 source_ref=5dfe03cdd4810107b784dfce8ae2ed82de50b669 role=test-infrastructure -->
Verifies that Haiku pricing produces lower cost estimates than Sonnet pricing for identical file processing scenarios.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cost:test_estimate_actual_cost_matches_pricing fingerprint=1ec34314487a54cd97ef862b8dd5bbfe131dd0a0b383382192ada3f3cde40da9 body_fp=2a3eb865c576d466d0808c7c1c053a181fd9ec60338520030cfae3ffabbe425b source_ref=5dfe03cdd4810107b784dfce8ae2ed82de50b669 role=test-infrastructure -->
Verifies estimate_actual_cost returns correct USD amount by comparing against manual calculation using Claude Sonnet pricing.
<!-- trie:end -->








