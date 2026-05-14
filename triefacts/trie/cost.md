---
trie_version: 0.1.0
source: trie/cost.py
file_fingerprint: a130d170e7b2e7efba48619ef0c572f926298712916f848f8e2e7eac3fac1e6e
last_synced_at: '2026-05-14T17:29:17Z'
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
<!-- trie:section symbol=trie/cost:ModelPricing fingerprint=f9ce4d87fdcdcaeb6884df7e5f35c0b5787858b143344b6dcc4013c403030344 body_fp=dbad66594404f9458aa32af450f57602e6542b2d0671e6c47a1f1f47018105ae -->
## `ModelPricing(model_id, input_per_mtok, output_per_mtok, cache_write_per_mtok, cache_read_per_mtok)`

Frozen dataclass holding per-million-token pricing rates for one model.

- `input_per_mtok`, `output_per_mtok`, `cache_write_per_mtok`, `cache_read_per_mtok`: USD per million tokens for each billing category.
<!-- trie:end -->

<!-- trie:section symbol=trie/cost:FileEstimate fingerprint=8d740615b193888076da794ca34ef357eefe7e61ecaf7a13b910609d7d02c6e4 body_fp=a09a31b130e03055b34bc1b5c9083efa1c2b6b2d6774fded6e80b482d66aab32 -->
## `FileEstimate`

Frozen dataclass holding token counts and estimated USD cost for processing one file's public symbols.
<!-- trie:end -->

<!-- trie:section symbol=trie/cost:get_pricing fingerprint=29a71728aa28685af7dadf00cbf539b7856c20a7ff58ccc9dc480f432b63699b body_fp=ac9f1aae2a31015bf48d65f87b50697870c2102f7a6f351c42009bfa0e709b61 -->
## `get_pricing(model_id: str) -> ModelPricing | None`

Look up a `ModelPricing` entry by model ID, returning `None` if unknown.
<!-- trie:end -->

<!-- trie:section symbol=trie/cost:estimate_file_cost fingerprint=b3ba0b1d128a0b519a76004e2b7267afe662074831ac3b79be3771b23172e4d2 body_fp=31e66fdb81f4c915295b4ecd7d7306d03327790e99b79c39ec5148db9e146048 -->
## `estimate_file_cost(*, file_path: str, cached_prefix_tokens: int, public_symbols: int, pricing: ModelPricing, request_tokens_per_symbol: int = 80, output_tokens_per_symbol: int = 200) -> FileEstimate`

Estimate USD cost of generating triefacts for all public symbols in one file.

- `cached_prefix_tokens`: token count from `count_tokens` for the system + cached-context payload.
- Cache write is charged once (first symbol); cache read is charged for the remaining symbols.
- `request_tokens_per_symbol` / `output_tokens_per_symbol`: per-symbol approximations; output tokens are unknowable ahead of time.
- Returns a zeroed `FileEstimate` when `public_symbols == 0`.
<!-- trie:end -->

<!-- trie:section symbol=trie/cost:estimate_actual_cost fingerprint=1adff2cb8f24277a094a096c7a008d4370584ceba59f49c4fd755cd884a13ccb body_fp=ed315ebc678158f6e3b508116b3e4429da9b680583a2c4e92b4aa940899ea8d8 -->
## `estimate_actual_cost(*, cache_creation_input_tokens: int, cache_read_input_tokens: int, input_tokens: int, output_tokens: int, pricing: ModelPricing) -> float`

Compute USD cost from token usage counters returned by a real LLM API response.
<!-- trie:end -->