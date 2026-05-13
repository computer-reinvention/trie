---
trie_version: 0.1.0
source: tests/test_cost.py
file_fingerprint: 56d003bc1c51065a50091fc9753ea5136e0956ccf0df15638afb26e1b9d064d3
last_synced_at: '2026-05-12T18:33:13Z'
defines:
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
outgoing_refs: 7
---
<!-- trie:section symbol=tests/test_cost:test_get_pricing_known fingerprint=bbd02a076da541cef07fa6081976ed6de9aaf330ae33ec2a51c75d2db8c710cc body_fp=6c6609eafafb3682a9c7e0ddfc6db963b850cc3b96533acf17859a1267f4e245 -->
## `test_get_pricing_known()`

Assert that `get_pricing` returns correct input/output prices for a known Claude Sonnet model.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_cost:test_get_pricing_unknown fingerprint=90e9070ea2d577508b09545ff08ba8518602b92df10e12cbb92f96127a284d58 body_fp=26e6ecc224454254eca360216350268fa4c28c7fae5a52a1e1902acb678e861f -->
## `test_get_pricing_unknown()`

Assert that `get_pricing` returns `None` for an unrecognised model identifier.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_cost:test_zero_public_symbols_costs_nothing fingerprint=2ea2b94a267c2897ce389247503958f55e5e14e2fa34592471ee2882ede9ece2 body_fp=d3a2c2d98be79c4a06179af1c208248e5cc96bd14126ff58e4d6afe8a758cf83 -->
## `test_zero_public_symbols_costs_nothing()`

Assert that `estimate_file_cost` returns zero cost and zero cache tokens when `public_symbols=0`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_cost:test_single_symbol_only_pays_cache_create fingerprint=3c5d08ddba36f5818e5149e2711a37784ba4d691d5da9a218d06d1ac14700662 body_fp=5baff391593301d1a4a93729741473c82ad40eb0124fe5018f080734ae6f6396 -->
## `test_single_symbol_only_pays_cache_create()`

Assert that a single-symbol file estimate creates cache tokens but reads none.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_cost:test_multiple_symbols_amortize_via_cache fingerprint=cc5a746bba0718b6cb0001d6bc37beb464207197d0a2652a42a4d977e637dcce body_fp=94fc26000c5d7d8c1f16718a66e5e2802e157833c77a07c8e4ff666f39d2774e -->
## `test_multiple_symbols_amortize_via_cache()`

Assert that processing two symbols costs less than 1.5× the single-symbol cost due to cache reads.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_cost:test_haiku_cheaper_than_sonnet fingerprint=92a67d6cd74211b78c4e308d2b0e42bac7bd60326f08acad5a2cfab355352edf body_fp=52a395e720e7d6e456e25f7f434e3a01f9623c3b0403b942f5e9aa92379c14fa -->
## `test_haiku_cheaper_than_sonnet()`

Assert that Haiku pricing produces a lower estimated cost than Sonnet for identical inputs.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_cost:test_estimate_actual_cost_matches_pricing fingerprint=1ec34314487a54cd97ef862b8dd5bbfe131dd0a0b383382192ada3f3cde40da9 body_fp=8e5580b9a9326dafc5791cab13c3d8e323433ca6fcb1b73c821603ead16332a1 -->
## `test_estimate_actual_cost_matches_pricing()`

Verify `estimate_actual_cost` computes USD cost correctly across all four token categories.
<!-- trie:end -->