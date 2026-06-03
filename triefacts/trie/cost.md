---
trie_version: 0.1.5
source: trie/cost.py
file_fingerprint: a130d170e7b2e7efba48619ef0c572f926298712916f848f8e2e7eac3fac1e6e
last_synced_at: '2026-06-03T20:47:47Z'
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
incoming_refs: 41
outgoing_refs: 0
---
<!-- trie:section symbol=trie/cost:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=1f26a9bf45f92c78c668a6050abbe7e6ef58f3f1f5efd61f5ad4c5b0f7c29671 source_ref=6bcbb1cf99dda1893150e55184f4c38d9b7a9986 -->
Provides cost estimation utilities for LLM API usage in triefact generation.

- `ModelPricing`: pricing configuration for different models including cache costs
- `FileEstimate`: estimated token usage and cost breakdown for processing a file
- `PRICING`: hardcoded pricing data for Anthropic Claude models as of 2026-04
- `get_pricing()`: retrieves pricing config by model ID
- `estimate_file_cost()`: estimates cost for generating triefacts for one file
- `estimate_actual_cost()`: computes actual cost from LLM usage counters
<!-- trie:end -->
<!-- trie:section symbol=trie/cost:ModelPricing fingerprint=f9ce4d87fdcdcaeb6884df7e5f35c0b5787858b143344b6dcc4013c403030344 body_fp=4ba5dc5fac46748fefe3c79ef9a33c321aee910d5870f9c9df687702789c14b7 source_ref=6bcbb1cf99dda1893150e55184f4c38d9b7a9986 -->
Immutable dataclass storing pricing rates for an LLM model.

- `input_per_mtok`: Cost in USD per million input tokens
- `output_per_mtok`: Cost in USD per million output tokens  
- `cache_write_per_mtok`: Cost in USD per million tokens when writing to cache
- `cache_read_per_mtok`: Cost in USD per million tokens when reading from cache
<!-- trie:end -->
<!-- trie:section symbol=trie/cost:PRICING fingerprint=4ce2b7b5eb1a916633a98aef001ac4eae62b45ae55ca84fbc5936272f12f4e34 body_fp=bf0a6160a4c7804416497852e29ba8faf530dbe6c46d626389d9d136e3e6a8eb source_ref=6bcbb1cf99dda1893150e55184f4c38d9b7a9986 -->
Maps model IDs to their pricing structures for cost calculations.

- Contains pricing for three Anthropic Claude models (Sonnet, Haiku, Opus)
- Prices are in USD per million tokens as of 2026-04
<!-- trie:end -->
<!-- trie:section symbol=trie/cost:FileEstimate fingerprint=8d740615b193888076da794ca34ef357eefe7e61ecaf7a13b910609d7d02c6e4 body_fp=91d340cf9c82619adc5f8e745ef4ce5442b60bce59b48efc31e7ed0cc8ceee62 source_ref=6bcbb1cf99dda1893150e55184f4c38d9b7a9986 -->
Represents estimated token usage and cost breakdown for generating documentation for one file.

- `cache_create_tokens`: tokens written to cache on first symbol
- `cache_read_tokens`: tokens read from cache for remaining symbols
- `request_tokens`: non-cached input tokens across all symbols
- `output_tokens`: generated response tokens across all symbols
- `cost_usd`: total estimated cost in US dollars
<!-- trie:end -->
<!-- trie:section symbol=trie/cost:get_pricing fingerprint=29a71728aa28685af7dadf00cbf539b7856c20a7ff58ccc9dc480f432b63699b body_fp=48e9433a08c360dcd0fa4097ce98884be9b334e582d4071e130eafec4e6a1b0d source_ref=6bcbb1cf99dda1893150e55184f4c38d9b7a9986 -->
Returns the ModelPricing for the given model ID from the PRICING dictionary.
<!-- trie:end -->
<!-- trie:section symbol=trie/cost:estimate_file_cost fingerprint=b3ba0b1d128a0b519a76004e2b7267afe662074831ac3b79be3771b23172e4d2 body_fp=1111c320bb497ddcbfc35be28584bab3605d0f4255e5e17d50818832b001b16a source_ref=6bcbb1cf99dda1893150e55184f4c38d9b7a9986 -->
Estimate the cost of generating triefacts for one file's public symbols.

- `cached_prefix_tokens`: token count from Anthropic `count_tokens` API for system + cached context
- `request_tokens_per_symbol`: defaults to 80 tokens per symbol
- `output_tokens_per_symbol`: defaults to 200 tokens per symbol
- Returns zero cost if no public symbols
<!-- trie:end -->
<!-- trie:section symbol=trie/cost:estimate_actual_cost fingerprint=1adff2cb8f24277a094a096c7a008d4370584ceba59f49c4fd755cd884a13ccb body_fp=c1690a18f6e5add7b342e65b3fa4c778fb6111afd8ea0469d50b890769474feb source_ref=6bcbb1cf99dda1893150e55184f4c38d9b7a9986 -->
Compute actual USD cost from token usage counters returned by an LLM call.
<!-- trie:end -->