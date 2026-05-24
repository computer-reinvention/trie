---
trie_version: 0.1.2
source: trie/cost.py
file_fingerprint: a130d170e7b2e7efba48619ef0c572f926298712916f848f8e2e7eac3fac1e6e
last_synced_at: '2026-05-23T23:54:01Z'
defines:
- kind: module
  qualified_name: trie/cost:__module__
  lines: 1-123
- kind: class
  qualified_name: trie/cost:ModelPricing
  lines: 10-15
- kind: constant
  qualified_name: trie/cost:PRICING
  lines: 18-40
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
incoming_refs: 36
outgoing_refs: 0
---
<!-- trie:section symbol=trie/cost:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=161d041f78acd67f8bfc5feaebb2395a2348d7e9f11a287f9c9a58b2a15dc4ed source_ref=6bcbb1cf99dda1893150e55184f4c38d9b7a9986 -->
## `cost`

Defines token-pricing data and cost-estimation utilities for triefact generation across supported Anthropic models.

- `PRICING`: snapshot rates (USD per million tokens) for three Claude models.
- `ModelPricing`: frozen dataclass holding per-model input, output, cache-write, and cache-read rates.
- `FileEstimate`: frozen dataclass holding per-file token counts and estimated USD cost.
<!-- trie:end -->
<!-- trie:section symbol=trie/cost:ModelPricing fingerprint=f9ce4d87fdcdcaeb6884df7e5f35c0b5787858b143344b6dcc4013c403030344 body_fp=bbaf7711c30c08744917fb498bcd07c765939d9abdfc63ef1274cdf512fa9fc0 source_ref=6bcbb1cf99dda1893150e55184f4c38d9b7a9986 -->
## `ModelPricing(model_id, input_per_mtok, output_per_mtok, cache_write_per_mtok, cache_read_per_mtok)`

Immutable record of per-token pricing rates for a single model.

- `input_per_mtok` / `output_per_mtok`: USD cost per million tokens for standard input/output.
- `cache_write_per_mtok`: USD per million tokens to write a prompt cache entry.
- `cache_read_per_mtok`: USD per million tokens to read a cached prefix.
<!-- trie:end -->
<!-- trie:section symbol=trie/cost:PRICING fingerprint=4ce2b7b5eb1a916633a98aef001ac4eae62b45ae55ca84fbc5936272f12f4e34 body_fp=3d432767a91543843f523c6dd22849ff61842d0d7b344489657ee3ffa6847045 source_ref=6bcbb1cf99dda1893150e55184f4c38d9b7a9986 -->
## `PRICING: dict[str, ModelPricing]`

Maps model ID strings to `ModelPricing` snapshots for Claude Sonnet 4.6, Haiku 4.5, and Opus 4.7.
<!-- trie:end -->
<!-- trie:section symbol=trie/cost:FileEstimate fingerprint=8d740615b193888076da794ca34ef357eefe7e61ecaf7a13b910609d7d02c6e4 body_fp=660ab099bbbca782886698f409b4625fec8994c5be1ed52644391900d1ae4972 source_ref=6bcbb1cf99dda1893150e55184f4c38d9b7a9986 -->
## `FileEstimate`

Immutable dataclass holding token usage and cost estimates for one file's triefact generation.

- `cache_create_tokens`: tokens paid at cache-write rate (first symbol only)
- `cache_read_tokens`: cached prefix tokens reused across remaining symbols
- `request_tokens`: non-cached input tokens across all symbols
- `cost_usd`: total estimated USD cost for all symbols in the file
<!-- trie:end -->
<!-- trie:section symbol=trie/cost:get_pricing fingerprint=29a71728aa28685af7dadf00cbf539b7856c20a7ff58ccc9dc480f432b63699b body_fp=9fc2663e5a5dc2b1ed12860dcc9b2546de6430ba3f77189c1bba92d6b2183b95 source_ref=6bcbb1cf99dda1893150e55184f4c38d9b7a9986 -->
## `get_pricing(model_id: str) -> ModelPricing | None`

Look up a `ModelPricing` entry from the global `PRICING` registry by model ID, returning `None` if not found.
<!-- trie:end -->
<!-- trie:section symbol=trie/cost:estimate_file_cost fingerprint=b3ba0b1d128a0b519a76004e2b7267afe662074831ac3b79be3771b23172e4d2 body_fp=422c34b3d79c73d671fbe2e3515966e0af7872fd2495d89d18c25f7d26bb2c0b source_ref=6bcbb1cf99dda1893150e55184f4c38d9b7a9986 -->
## `estimate_file_cost(*, file_path, cached_prefix_tokens, public_symbols, pricing, request_tokens_per_symbol=80, output_tokens_per_symbol=200) -> FileEstimate`

Estimate the USD cost of generating triefacts for all public symbols in one file.

- `cached_prefix_tokens`: token count of the shared system+context prefix, written once and read for each subsequent symbol.
- `request_tokens_per_symbol`: per-symbol input token approximation; output tokens are unknown ahead of time.
- Returns a zeroed `FileEstimate` immediately when `public_symbols == 0`.
<!-- trie:end -->
<!-- trie:section symbol=trie/cost:estimate_actual_cost fingerprint=1adff2cb8f24277a094a096c7a008d4370584ceba59f49c4fd755cd884a13ccb body_fp=9747f82df401c27b95ae06a637090c9fc30f1c37a9c1b655264ef4a9376972f7 source_ref=6bcbb1cf99dda1893150e55184f4c38d9b7a9986 -->
## `estimate_actual_cost(*, cache_creation_input_tokens, cache_read_input_tokens, input_tokens, output_tokens, pricing) -> float`

Compute USD cost from exact token usage counters returned by an LLM API response.
<!-- trie:end -->