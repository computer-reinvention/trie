---
trie_version: 0.1.0
source: tests/test_models.py
file_fingerprint: b308887d2a458d142f8af7881da7183c7a9158aa32f833ef12ad36d59684d3c7
last_synced_at: '2026-05-14T17:31:01Z'
defines:
- kind: function
  qualified_name: tests/test_models:test_count_tokens_returns_input_tokens_from_api
  lines: 15-19
- kind: function
  qualified_name: tests/test_models:test_payload_includes_request_block_when_non_empty
  lines: 22-30
- kind: function
  qualified_name: tests/test_models:test_payload_skips_empty_request_block
  lines: 33-44
- kind: function
  qualified_name: tests/test_models:test_payload_carries_model_and_system_prompt
  lines: 47-54
incoming_refs: 0
outgoing_refs: 5
---
<!-- trie:section symbol=tests/test_models:test_count_tokens_returns_input_tokens_from_api fingerprint=0d10b6e1337540a4232e8ff6027844fe7b7fb98efa5d37d1961a9afb01ded719 body_fp=d4de0947b2d819dbaa003b324759c0c791f6938a92cdb3e574e62d76c34c20be -->
## `test_count_tokens_returns_input_tokens_from_api()`

Assert that `AnthropicClient.count_tokens` returns the `input_tokens` value from the API response.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_models:test_payload_includes_request_block_when_non_empty fingerprint=4f22ab41ab118aa5cf77f32ccf8402bce46a22a67fdb26a51f50639150cc0233 body_fp=574325fa97ea1d8b27431173d661a8c489e74b495ac5423b8137190fa8b204f5 -->
## `test_payload_includes_request_block_when_non_empty()`

Assert that a non-empty `request` field produces two content blocks in the `count_tokens` API payload.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_models:test_payload_skips_empty_request_block fingerprint=fede8ab1ff54693374262d939db8635af46c0c671971b0682aad8fda0f662dbe body_fp=03f4aaf13d756704e64acd501fbba71afbe1c4c25e6e6b5220a7ae161a90029a -->
## `test_payload_skips_empty_request_block()`

Assert that `count_tokens` omits empty text blocks and preserves `cache_control` on the cached-context block.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_models:test_payload_carries_model_and_system_prompt fingerprint=55ff54e49d83aae379c8a9ad8c229250ed330a0905def5228a6662e4728409b3 body_fp=684a5e485349a048495349106e9d3ad44c143c1a9615c7aa02e98bafc241b118 -->
## `test_payload_carries_model_and_system_prompt()`

Verify that `count_tokens` passes the correct model name and system prompt (with ephemeral cache control) to the Anthropic API.
<!-- trie:end -->