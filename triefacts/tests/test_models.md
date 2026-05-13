---
trie_version: 0.1.0
source: tests/test_models.py
file_fingerprint: b308887d2a458d142f8af7881da7183c7a9158aa32f833ef12ad36d59684d3c7
last_synced_at: '2026-05-12T18:34:45Z'
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
<!-- trie:section symbol=tests/test_models:test_count_tokens_returns_input_tokens_from_api fingerprint=0d10b6e1337540a4232e8ff6027844fe7b7fb98efa5d37d1961a9afb01ded719 body_fp=58dcb21ab87095c0775cdad7e676603a359f7351b294f4a4dc16f3122cf9a994 -->
## `test_count_tokens_returns_input_tokens_from_api()`

Verify that `AnthropicClient.count_tokens` returns the `input_tokens` value from the API response.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_models:test_payload_includes_request_block_when_non_empty fingerprint=4f22ab41ab118aa5cf77f32ccf8402bce46a22a67fdb26a51f50639150cc0233 body_fp=192f6bad5e51820e14e9d142d0a9f5884b08880069d2f2b54a69933e96118387 -->
## `test_payload_includes_request_block_when_non_empty()`

Assert that `count_tokens` sends both the cached context and request as separate content blocks when request is non-empty.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_models:test_payload_skips_empty_request_block fingerprint=fede8ab1ff54693374262d939db8635af46c0c671971b0682aad8fda0f662dbe body_fp=673b9a53194de8ea2615b3ff0b7b25eeca9ddb5839509b9ed85ad6faa4adb3ab -->
## `test_payload_skips_empty_request_block()`

Assert that an empty `request` field is omitted from the API payload and `cache_control` is preserved on the cached-context block.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_models:test_payload_carries_model_and_system_prompt fingerprint=55ff54e49d83aae379c8a9ad8c229250ed330a0905def5228a6662e4728409b3 body_fp=c9687a3f2ac146dd839100866cbafbbed22f05b77b4abefae6518f769c7252b6 -->
## `test_payload_carries_model_and_system_prompt()`

Verify that `count_tokens` sends the correct model name and system prompt with ephemeral cache control to the Anthropic API.
<!-- trie:end -->