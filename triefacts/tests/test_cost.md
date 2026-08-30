---
trie_version: 0.3.0
source: tests/test_cost.py
file_fingerprint: bf6f91573a683679cde682820bbf68623adaf405f78f994013d046d66012fdc0
last_synced_at: '2026-08-30T14:33:15Z'
defines:
- kind: module
  qualified_name: tests/test_cost:__module__
  lines: 1-168
- kind: function
  qualified_name: tests/test_cost:test_get_pricing_known
  lines: 15-19
  signature: def test_get_pricing_known()
- kind: function
  qualified_name: tests/test_cost:test_get_pricing_unknown
  lines: 22-27
  signature: def test_get_pricing_unknown()
- kind: function
  qualified_name: tests/test_cost:test_get_pricing_unknown_emits_warning
  lines: 30-36
  signature: def test_get_pricing_unknown_emits_warning()
- kind: function
  qualified_name: tests/test_cost:test_zero_public_symbols_costs_nothing
  lines: 39-45
  signature: def test_zero_public_symbols_costs_nothing()
- kind: function
  qualified_name: tests/test_cost:test_single_symbol_only_pays_cache_create
  lines: 48-57
  signature: def test_single_symbol_only_pays_cache_create()
- kind: function
  qualified_name: tests/test_cost:test_multiple_symbols_amortize_via_cache
  lines: 60-70
  signature: def test_multiple_symbols_amortize_via_cache()
- kind: function
  qualified_name: tests/test_cost:test_haiku_cheaper_than_sonnet
  lines: 73-82
  signature: def test_haiku_cheaper_than_sonnet()
- kind: function
  qualified_name: tests/test_cost:test_estimate_actual_cost_matches_pricing
  lines: 85-100
  signature: def test_estimate_actual_cost_matches_pricing()
- kind: constant
  qualified_name: tests/test_cost:_EXPECTED_MODELS
  lines: 110-124
- kind: function
  qualified_name: tests/test_cost:test_every_known_model_has_pricing
  lines: 128-135
  signature: 'def test_every_known_model_has_pricing(model_id: str)'
- kind: function
  qualified_name: tests/test_cost:test_sonnet_5_pricing_is_correct
  lines: 138-144
  signature: def test_sonnet_5_pricing_is_correct()
- kind: function
  qualified_name: tests/test_cost:test_cache_pricing_follows_multiplier_convention
  lines: 147-155
  signature: def test_cache_pricing_follows_multiplier_convention()
- kind: function
  qualified_name: tests/test_cost:test_default_config_models_have_pricing
  lines: 158-167
  signature: def test_default_config_models_have_pricing()
incoming_refs: 0
outgoing_refs: 12
---
<!-- trie:section symbol=tests/test_cost:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=79bc44dab98cf1a69d69538faa9b7dd0d8abe8280dc4d36888374f99d13d4d88 source_ref=5dfe03cdd4810107b784dfce8ae2ed82de50b669 role=test-infrastructure -->
Tests cost estimation functions from the `trie.cost` module, verifying pricing lookups, file cost calculations, and cache optimization behavior.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cost:test_get_pricing_known fingerprint=bbd02a076da541cef07fa6081976ed6de9aaf330ae33ec2a51c75d2db8c710cc body_fp=40d29078d0cafcbdc69da38369fc4f0db88229e6ff90f69adaeeb1a2dfee39df source_ref=5dfe03cdd4810107b784dfce8ae2ed82de50b669 role=test-infrastructure -->
## `def test_get_pricing_known()`

Verifies that get_pricing returns correct pricing data for a known model.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cost:test_get_pricing_unknown fingerprint=a664e93079751f2d6d8c7ffe1f9d713b7f9198fcc24f6cc6323cd3149b42a051 body_fp=84317dee33177230c7abed2b8b9a28f28a9cbbed771c59a9e21ee6bc4ad3fa1f source_ref=031f9e2b5d93ed3515166e0a32226167c7411945 role=test -->
## `def test_get_pricing_unknown()`

Tests that `get_pricing` returns `None` for unknown model names and emits exactly one warning containing "No pricing entry".
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cost:test_get_pricing_unknown_emits_warning fingerprint=b95b0743fde9c64dbe71ceb3e8f9a39f6b32d06ff286c79cc9714273febe4a1f body_fp=e8e110fa6e0309acff65a3dedf36a0b923d317fe6b3ba2df5a6d62560caf8d6e source_ref=031f9e2b5d93ed3515166e0a32226167c7411945 role=test -->
## `def test_get_pricing_unknown_emits_warning()`

Assert that `get_pricing` emits exactly one warning containing the unknown model name when called with an unrecognized model identifier.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cost:test_zero_public_symbols_costs_nothing fingerprint=2ea2b94a267c2897ce389247503958f55e5e14e2fa34592471ee2882ede9ece2 body_fp=929adb6fcdfd4789873842ca73e2956c61f97e622bcf262cb09bb52787ee0de2 source_ref=5dfe03cdd4810107b784dfce8ae2ed82de50b669 role=monitoring-telemetry -->
## `def test_zero_public_symbols_costs_nothing()`

Verifies that estimating cost for a file with zero public symbols returns zero cost and cache tokens.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cost:test_single_symbol_only_pays_cache_create fingerprint=3c5d08ddba36f5818e5149e2711a37784ba4d691d5da9a218d06d1ac14700662 body_fp=a901bfc009f033d1ce09559f10570fee81a09c997388ee1c6fe7f650e3a7a8a4 source_ref=5dfe03cdd4810107b784dfce8ae2ed82de50b669 role=monitoring-telemetry -->
## `def test_single_symbol_only_pays_cache_create()`

Tests that a file with one symbol creates cache tokens without reading cache on first call.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cost:test_multiple_symbols_amortize_via_cache fingerprint=cc5a746bba0718b6cb0001d6bc37beb464207197d0a2652a42a4d977e637dcce body_fp=7aee3269687a33be4dfd4fc3518b29f4f90b48ea4b0b2f15df23b180db8cf69c source_ref=5dfe03cdd4810107b784dfce8ae2ed82de50b669 role=monitoring-telemetry -->
## `def test_multiple_symbols_amortize_via_cache()`

Tests that processing multiple symbols in a file benefits from cache read cost savings.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cost:test_haiku_cheaper_than_sonnet fingerprint=92a67d6cd74211b78c4e308d2b0e42bac7bd60326f08acad5a2cfab355352edf body_fp=949deae2c432b7ea90ceedbeb4bc3551550cf4fe178936fa0a2218fdb4e3960c source_ref=5dfe03cdd4810107b784dfce8ae2ed82de50b669 role=test-infrastructure -->
## `def test_haiku_cheaper_than_sonnet()`

Verifies that Haiku pricing produces lower cost estimates than Sonnet pricing for identical file processing scenarios.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cost:test_estimate_actual_cost_matches_pricing fingerprint=1ec34314487a54cd97ef862b8dd5bbfe131dd0a0b383382192ada3f3cde40da9 body_fp=4175ede42dc146522f7cd1df133fccf92b96c526c703ff9d7c041fe245727d9e source_ref=5dfe03cdd4810107b784dfce8ae2ed82de50b669 role=test-infrastructure -->
## `def test_estimate_actual_cost_matches_pricing()`

Verifies estimate_actual_cost returns correct USD amount by comparing against manual calculation using Claude Sonnet pricing.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cost:_EXPECTED_MODELS fingerprint=830b0f91a627a9d689fb722cc1c27866851c17a4f202be77d87f9c7cc5c35f8d body_fp=1c6f6857bb20de56f1bc83f30e8fecefea669f3dbbe9d561aee2ceaae608cfcf source_ref=031f9e2b5d93ed3515166e0a32226167c7411945 role=test -->
List of model IDs that must have `PRICING` entries, used by `test_every_known_model_has_pricing` to catch models added to trie's supported surface without cost data.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cost:test_every_known_model_has_pricing fingerprint=2e8eb98c7848a526cb12788e78c0237b4c2157ed2326834f305493c0090ace94 body_fp=de369dcb42376a3fdfb1908bb17dba27bf888a4c09686f66483242d359833d4d source_ref=031f9e2b5d93ed3515166e0a32226167c7411945 role=test -->
## `def test_every_known_model_has_pricing(model_id: str)`

Assert that every model in `_EXPECTED_MODELS` has a `PRICING` entry with all four rate fields greater than zero.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cost:test_sonnet_5_pricing_is_correct fingerprint=6b0e875112623c47ad3c5d8d8f311d3b13e6d9a56edf4a8b92027ddf52e4e4dd body_fp=542721c819f9475e3e00b7184bd352de292aa9cc1180c58100b550f0eb1cc2f6 source_ref=031f9e2b5d93ed3515166e0a32226167c7411945 role=test -->
## `def test_sonnet_5_pricing_is_correct()`

Assert that `PRICING["anthropic/claude-sonnet-5"]` carries the correct per-MTok rates for input, output, cache write, and cache read.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cost:test_cache_pricing_follows_multiplier_convention fingerprint=1c454cd3a16726c7e77c72e13464216c846b839ad3542f47bd546de2eda22065 body_fp=0e918ec65bc3c68168b5bd54e59519d81b0e9c4e80d72a6244829b3feb215ccb source_ref=031f9e2b5d93ed3515166e0a32226167c7411945 role=test -->
## `def test_cache_pricing_follows_multiplier_convention()`

Assert that every entry in `PRICING` sets `cache_write_per_mtok` to exactly 1.25× and `cache_read_per_mtok` to exactly 0.10× the entry's `input_per_mtok`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cost:test_default_config_models_have_pricing fingerprint=96bd4604f5097cf81a704ff6ce11bb81a3d92d1358fde898eb1bd180b72ebaf1 body_fp=624291d5aa0fc4bd0dd34747843ddec65e148b4135bb6d3949a5bb96a39a4919 source_ref=031f9e2b5d93ed3515166e0a32226167c7411945 role=test -->
## `def test_default_config_models_have_pricing()`

Assert that every model ID referenced by `Models` default fields `bootstrap` and `cascade` has a corresponding entry in `PRICING`.
<!-- trie:end -->