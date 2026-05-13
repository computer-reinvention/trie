---
trie_version: 0.1.0
source: trie/cost.py
file_fingerprint: a130d170e7b2e7efba48619ef0c572f926298712916f848f8e2e7eac3fac1e6e
last_synced_at: '2026-05-12T18:32:45Z'
defines:
- kind: class
  qualified_name: trie/cost:ModelPricing
  lines: 10-15
- kind: class
  qualified_name: trie/cost:FileEstimate
  lines: 44-51
- kind: function
  qualified_name: trie/cost:get_pricing
  lines: 54-55
- kind: function
  qualified_name: trie/cost:estimate_file_cost
  lines: 58-105
- kind: function
  qualified_name: trie/cost:estimate_actual_cost
  lines: 108-122
incoming_refs: 34
outgoing_refs: 0
---
<!-- trie:section symbol=trie/cost:ModelPricing fingerprint=f9ce4d87fdcdcaeb6884df7e5f35c0b5787858b143344b6dcc4013c403030344 body_fp=ac83350b9bf38e5bb19938a1f79816b67af96052eaa67a8c03fdfb67ac165ca2 -->
## `ModelPricing(model_id, input_per_mtok, output_per_mtok, cache_write_per_mtok, cache_read_per_mtok)`

Frozen dataclass holding per-million-token pricing for one model.

- `input_per_mtok` / `output_per_mtok`: USD cost per 1 M tokens for input/output.
- `cache_write_per_mtok` / `cache_read_per_mtok`: USD cost per 1 M tokens for Anthropic prompt-cache write/read.
<!-- trie:end -->

<!-- trie:section symbol=trie/cost:FileEstimate fingerprint=8d740615b193888076da794ca34ef357eefe7e61ecaf7a13b910609d7d02c6e4 body_fp=cc3242e72d3e0e91693ffd6efc56ee6254a7b38e33f4608e5472ad04bc542101 -->
## `FileEstimate(file_path, public_symbols, cache_create_tokens, cache_read_tokens, request_tokens, output_tokens, cost_usd)`

Frozen dataclass holding per-file token counts and estimated USD cost for triefact generation.
<!-- trie:end -->

<!-- trie:section symbol=trie/cost:get_pricing fingerprint=29a71728aa28685af7dadf00cbf539b7856c20a7ff58ccc9dc480f432b63699b body_fp=6e56be7a3a5d4a6eb8e36a2520e241695875486d8a22acffef66de6abec87ecf -->
## `get_pricing(model_id: str) -> ModelPricing | None`

Look up a `ModelPricing` entry from the global `PRICING` registry by model ID.
<!-- trie:end -->

<!-- trie:section symbol=trie/cost:estimate_file_cost fingerprint=b3ba0b1d128a0b519a76004e2b7267afe662074831ac3b79be3771b23172e4d2 body_fp=50983be7d6a8247646d10cd06eba968f0f2c486136432b5fa1139680c6952737 -->
## `estimate_file_cost(*, file_path: str, cached_prefix_tokens: int, public_symbols: int, pricing: ModelPricing, request_tokens_per_symbol: int = 80, output_tokens_per_symbol: int = 200) -> FileEstimate`

Estimate the USD cost of generating triefacts for all public symbols in one file.

- `cached_prefix_tokens`: token count of the system + cached context payload, from `count_tokens` API.
- Cache write is charged once; cache read is charged for each subsequent symbol.
- `request_tokens_per_symbol` / `output_tokens_per_symbol`: per-symbol approximations when actuals are unknown.
- Returns a zero-cost `FileEstimate` immediately when `public_symbols == 0`.
<!-- trie:end -->

<!-- trie:section symbol=trie/cost:estimate_actual_cost fingerprint=1adff2cb8f24277a094a096c7a008d4370584ceba59f49c4fd755cd884a13ccb body_fp=428ecaf086d96b840b3d72a8d76fae4e2ed54edf1ee0aaba3265fadd97a542fe -->
## `estimate_actual_cost(*, cache_creation_input_tokens: int, cache_read_input_tokens: int, input_tokens: int, output_tokens: int, pricing: ModelPricing) -> float`

Compute actual USD cost from LLM usage counters and a `ModelPricing` rate table.
<!-- trie:end -->