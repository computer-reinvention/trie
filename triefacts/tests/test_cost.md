---
trie_version: 0.1.2
source: tests/test_cost.py
file_fingerprint: 56d003bc1c51065a50091fc9753ea5136e0956ccf0df15638afb26e1b9d064d3
last_synced_at: '2026-05-23T23:54:05Z'
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
outgoing_refs: 7
---
<!-- trie:section symbol=tests/test_cost:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=dc858d17916b365adfeb96badffa0e20a68aa1b19cb64ec9c996d005e47ba178 source_ref=5dfe03cdd4810107b784dfce8ae2ed82de50b669 -->
## `tests/test_cost`

Test suite for `trie.cost` pricing utilities: `get_pricing`, `estimate_file_cost`, and `estimate_actual_cost`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cost:test_get_pricing_known fingerprint=bbd02a076da541cef07fa6081976ed6de9aaf330ae33ec2a51c75d2db8c710cc body_fp=521c240e75df5935838f115b61dd25fd4fc35ef0467792048217d231b73b53b6 source_ref=5dfe03cdd4810107b784dfce8ae2ed82de50b669 -->
## `test_get_pricing_known()`

Assert `get_pricing` returns correct input/output pricing for a known Claude Sonnet model.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cost:test_get_pricing_unknown fingerprint=90e9070ea2d577508b09545ff08ba8518602b92df10e12cbb92f96127a284d58 body_fp=26e6ecc224454254eca360216350268fa4c28c7fae5a52a1e1902acb678e861f source_ref=5dfe03cdd4810107b784dfce8ae2ed82de50b669 -->
## `test_get_pricing_unknown()`

Assert that `get_pricing` returns `None` for an unrecognised model identifier.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cost:test_zero_public_symbols_costs_nothing fingerprint=2ea2b94a267c2897ce389247503958f55e5e14e2fa34592471ee2882ede9ece2 body_fp=d3a2c2d98be79c4a06179af1c208248e5cc96bd14126ff58e4d6afe8a758cf83 source_ref=5dfe03cdd4810107b784dfce8ae2ed82de50b669 -->
## `test_zero_public_symbols_costs_nothing()`

Assert that `estimate_file_cost` returns zero cost and zero cache tokens when `public_symbols=0`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cost:test_single_symbol_only_pays_cache_create fingerprint=3c5d08ddba36f5818e5149e2711a37784ba4d691d5da9a218d06d1ac14700662 body_fp=84861e82b336fcd7af3518a3628d3e755e84b7058b7fac67dbbeb5aac64d5f1b source_ref=5dfe03cdd4810107b784dfce8ae2ed82de50b669 -->
## `test_single_symbol_only_pays_cache_create()`

Assert that a file with one public symbol incurs cache-create tokens but zero cache-read tokens.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cost:test_multiple_symbols_amortize_via_cache fingerprint=cc5a746bba0718b6cb0001d6bc37beb464207197d0a2652a42a4d977e637dcce body_fp=c3ff1282d388debf5355336fa88d9f3e0735c94344cf2a963a0541571db908cd source_ref=5dfe03cdd4810107b784dfce8ae2ed82de50b669 -->
## `test_multiple_symbols_amortize_via_cache()`

Assert that two-symbol file cost is less than 1.5× one-symbol cost due to cache-read amortization.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cost:test_haiku_cheaper_than_sonnet fingerprint=92a67d6cd74211b78c4e308d2b0e42bac7bd60326f08acad5a2cfab355352edf body_fp=aff2f6af838e55ea7e8856f7d0e132b7889f84b42d70076f8d74f6bee325b16e source_ref=5dfe03cdd4810107b784dfce8ae2ed82de50b669 -->
## `test_haiku_cheaper_than_sonnet()`

Assert that `estimate_file_cost` produces a lower USD cost for Haiku pricing than for Sonnet pricing.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cost:test_estimate_actual_cost_matches_pricing fingerprint=1ec34314487a54cd97ef862b8dd5bbfe131dd0a0b383382192ada3f3cde40da9 body_fp=fd713f830950fefc359f38f8bc8e23fae71fc7bfd1a5844856a35fb99e773731 source_ref=5dfe03cdd4810107b784dfce8ae2ed82de50b669 -->
## `test_estimate_actual_cost_matches_pricing()`

Verify `estimate_actual_cost` computes the correct USD cost for mixed cache-creation, cache-read, input, and output tokens.
<!-- trie:end -->