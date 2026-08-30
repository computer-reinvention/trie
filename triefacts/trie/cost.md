---
trie_version: 0.3.0
source: trie/cost.py
file_fingerprint: d3dd80a4ff88ddcaf64216579b55c8239540a74d3d3d900ec4a4597fc99416c7
last_synced_at: '2026-08-30T14:33:01Z'
defines:
- kind: module
  qualified_name: trie/cost:__module__
  lines: 1-141
- kind: class
  qualified_name: trie/cost:ModelPricing
  lines: 12-17
  signature: class ModelPricing
- kind: function
  qualified_name: trie/cost:_p
  lines: 20-28
  signature: 'def _p(model_id: str, inp: float, out: float) -> ModelPricing'
- kind: constant
  qualified_name: trie/cost:PRICING
  lines: 32-50
- kind: class
  qualified_name: trie/cost:FileEstimate
  lines: 55-62
  signature: class FileEstimate
- kind: function
  qualified_name: trie/cost:get_pricing
  lines: 65-73
  signature: 'def get_pricing(model_id: str) -> ModelPricing | None'
- kind: function
  qualified_name: trie/cost:estimate_file_cost
  lines: 76-123
  signature: 'def estimate_file_cost( *, file_path: str, cached_prefix_tokens: int, public_symbols: int, pricing: ModelPricing, request_tokens_per_symbol: int = 80, output_tokens_per_symbol: int = 200, ) -> FileEstimate'
- kind: function
  qualified_name: trie/cost:estimate_actual_cost
  lines: 126-140
  signature: 'def estimate_actual_cost( *, cache_creation_input_tokens: int, cache_read_input_tokens: int, input_tokens: int, output_tokens: int, pricing: ModelPricing, ) -> float'
incoming_refs: 41
outgoing_refs: 0
---
<!-- trie:section symbol=trie/cost:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=1f26a9bf45f92c78c668a6050abbe7e6ef58f3f1f5efd61f5ad4c5b0f7c29671 source_ref=6bcbb1cf99dda1893150e55184f4c38d9b7a9986 role=monitoring-telemetry -->
Provides cost estimation utilities for LLM API usage in triefact generation.

- `ModelPricing`: pricing configuration for different models including cache costs
- `FileEstimate`: estimated token usage and cost breakdown for processing a file
- `PRICING`: hardcoded pricing data for Anthropic Claude models as of 2026-04
- `get_pricing()`: retrieves pricing config by model ID
- `estimate_file_cost()`: estimates cost for generating triefacts for one file
- `estimate_actual_cost()`: computes actual cost from LLM usage counters
<!-- trie:end -->
<!-- trie:section symbol=trie/cost:ModelPricing fingerprint=f9ce4d87fdcdcaeb6884df7e5f35c0b5787858b143344b6dcc4013c403030344 body_fp=ba60411235f319634ef88226f62ca1dc559782b530eeb754ea7b6482a9c3a440 source_ref=6bcbb1cf99dda1893150e55184f4c38d9b7a9986 role=monitoring-telemetry -->
## `class ModelPricing`

Immutable dataclass storing pricing rates for an LLM model.

- `input_per_mtok`: Cost in USD per million input tokens
- `output_per_mtok`: Cost in USD per million output tokens  
- `cache_write_per_mtok`: Cost in USD per million tokens when writing to cache
- `cache_read_per_mtok`: Cost in USD per million tokens when reading from cache
<!-- trie:end -->
<!-- trie:section symbol=trie/cost:_p fingerprint=a4eb46b784f2b98becded476576555ba2242649b39d8957bba4ca5f6182935d9 body_fp=0fbc4c07975cd261e20abb9e8b59ba79fb5c05c9af79218edf9e3db1e8192dd3 source_ref=2e2b5d0272fcd6b30c6560da3d39da91148555de role=util -->
## `def _p(model_id: str, inp: float, out: float) -> ModelPricing`

Construct a `ModelPricing` by deriving cache prices from the input price using fixed Anthropic 5-min TTL multipliers.

- `inp`: input cost per million tokens; cache write = `inp × 1.25`, cache read = `inp × 0.10`
- `out`: output cost per million tokens; passed through directly
<!-- trie:end -->
<!-- trie:section symbol=trie/cost:PRICING fingerprint=a5781511dc6ce43ee2eaeb9a48ca0c28a9433b91a1a211175f079ae485c741ec body_fp=f594d037b26769eb22e1fd054e20b4318babf274dcbb4309e33c45352002f561 source_ref=2e2b5d0272fcd6b30c6560da3d39da91148555de role=config -->
Maps model IDs to their pricing structures for cost calculations.

- Contains pricing for 13 Anthropic Claude models across Sonnet, Haiku, Opus, and Fable families
- Opus prices revised to $5.00/$25.00 per mtok (input/output); Fable added at $10.00/$50.00
- Prices are in USD per million tokens as of 2026-08-30
<!-- trie:end -->
<!-- trie:section symbol=trie/cost:FileEstimate fingerprint=8d740615b193888076da794ca34ef357eefe7e61ecaf7a13b910609d7d02c6e4 body_fp=308906bc2aa974f762254d7865f41540d41c837271aca54c1888cc6db9435279 source_ref=6bcbb1cf99dda1893150e55184f4c38d9b7a9986 role=monitoring-telemetry -->
## `class FileEstimate`

Represents estimated token usage and cost breakdown for generating documentation for one file.

- `cache_create_tokens`: tokens written to cache on first symbol
- `cache_read_tokens`: tokens read from cache for remaining symbols
- `request_tokens`: non-cached input tokens across all symbols
- `output_tokens`: generated response tokens across all symbols
- `cost_usd`: total estimated cost in US dollars
<!-- trie:end -->
<!-- trie:section symbol=trie/cost:get_pricing fingerprint=21ebdc175e4bb5a081ee8e077ebbbc71ef9889d640f4983a9a2af79b317bead8 body_fp=6b185db43800093157de48d2f0c8f681c32ba404082104e9cd1dd940a0120a0d source_ref=2e2b5d0272fcd6b30c6560da3d39da91148555de role=util -->
## `def get_pricing(model_id: str) -> ModelPricing | None`

Returns the `ModelPricing` for the given model ID from `PRICING`, emitting a `warnings.warn` if the ID is not found.
<!-- trie:end -->
<!-- trie:section symbol=trie/cost:estimate_file_cost fingerprint=b3ba0b1d128a0b519a76004e2b7267afe662074831ac3b79be3771b23172e4d2 body_fp=ff1a1eae6ffea2a87c9a10577f94deda12191266184906b339af302411bcdf6a source_ref=6bcbb1cf99dda1893150e55184f4c38d9b7a9986 role=monitoring-telemetry -->
## `def estimate_file_cost( *, file_path: str, cached_prefix_tokens: int, public_symbols: int, pricing: ModelPricing, request_tokens_per_symbol: int = 80, output_tokens_per_symbol: int = 200, ) -> FileEstimate`

Estimate the cost of generating triefacts for one file's public symbols.

- `cached_prefix_tokens`: token count from Anthropic `count_tokens` API for system + cached context
- `request_tokens_per_symbol`: defaults to 80 tokens per symbol
- `output_tokens_per_symbol`: defaults to 200 tokens per symbol
- Returns zero cost if no public symbols
<!-- trie:end -->
<!-- trie:section symbol=trie/cost:estimate_actual_cost fingerprint=1adff2cb8f24277a094a096c7a008d4370584ceba59f49c4fd755cd884a13ccb body_fp=4ebcdefa51b9fb49e682d118cb69223fd27f20b20fefdc89497b998c23067035 source_ref=6bcbb1cf99dda1893150e55184f4c38d9b7a9986 role=monitoring-telemetry -->
## `def estimate_actual_cost( *, cache_creation_input_tokens: int, cache_read_input_tokens: int, input_tokens: int, output_tokens: int, pricing: ModelPricing, ) -> float`

Compute actual USD cost from token usage counters returned by an LLM call.
<!-- trie:end -->