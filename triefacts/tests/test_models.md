---
trie_version: 0.1.2
source: tests/test_models.py
file_fingerprint: b308887d2a458d142f8af7881da7183c7a9158aa32f833ef12ad36d59684d3c7
last_synced_at: '2026-05-23T23:54:39Z'
defines:
- kind: module
  qualified_name: tests/test_models:__module__
  lines: 1-55
- kind: function
  qualified_name: tests/test_models:_make_client
  lines: 9-12
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
<!-- trie:section symbol=tests/test_models:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=ddbef35b8571260ded695ed158a2c5098bf2dc72610879b94ce3b438526c21fd source_ref=afdf164a14b52d4a76e32a6ebe1eefd605ccd95d -->
## `tests/test_models`

Test `AnthropicClient.count_tokens` payload construction and token-count return value.

- `_make_client`: builds an `AnthropicClient` backed by a `MagicMock` Anthropic SDK object.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models:_make_client fingerprint=d156a4aa22c94c9c11c7e4c6b8392815d9850cf211eea2b9c5a0eed19b424aa6 body_fp=8115b5bfd2b54f9617692f57698750508b6937bd3c8de46c7e9240363de0727c source_ref=afdf164a14b52d4a76e32a6ebe1eefd605ccd95d -->
## `_make_client(input_tokens: int = 42) -> tuple[AnthropicClient, MagicMock]`

Build a test `AnthropicClient` backed by a `MagicMock` with a stubbed `count_tokens` response.

- `input_tokens`: value returned by the mock's `messages.count_tokens` call.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models:test_count_tokens_returns_input_tokens_from_api fingerprint=0d10b6e1337540a4232e8ff6027844fe7b7fb98efa5d37d1961a9afb01ded719 body_fp=cc577316501e5f26d6c62720fade35cd49465b78de5d08e75a1a18efc6ce0951 source_ref=afdf164a14b52d4a76e32a6ebe1eefd605ccd95d -->
## `test_count_tokens_returns_input_tokens_from_api()`

Assert that `AnthropicClient.count_tokens` returns the `input_tokens` value from the Anthropic API response.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models:test_payload_includes_request_block_when_non_empty fingerprint=4f22ab41ab118aa5cf77f32ccf8402bce46a22a67fdb26a51f50639150cc0233 body_fp=8383f3689faf7c5c93bc9dcbe12304b36d66916a2560db0ba809eb1d181a3920 source_ref=afdf164a14b52d4a76e32a6ebe1eefd605ccd95d -->
## `test_payload_includes_request_block_when_non_empty()`

Assert that a non-empty `request` field produces two content blocks in the `count_tokens` payload.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models:test_payload_skips_empty_request_block fingerprint=fede8ab1ff54693374262d939db8635af46c0c671971b0682aad8fda0f662dbe body_fp=6d3c259184de50296fbb0cee7b8eb0ef0c5c27c0998993e341cde8ebb23c2f5a source_ref=afdf164a14b52d4a76e32a6ebe1eefd605ccd95d -->
## `test_payload_skips_empty_request_block()`

Assert that `AnthropicClient.count_tokens` omits empty text blocks and preserves `cache_control` on the cached-context block.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models:test_payload_carries_model_and_system_prompt fingerprint=55ff54e49d83aae379c8a9ad8c229250ed330a0905def5228a6662e4728409b3 body_fp=8cb2824459bffba1a453e9ff60938145900aa5786fd77306f90fcf1f2f2be6b4 source_ref=afdf164a14b52d4a76e32a6ebe1eefd605ccd95d -->
## `test_payload_carries_model_and_system_prompt()`

Assert that `count_tokens` sends the correct model name and ephemeral-cached system prompt to the API.
<!-- trie:end -->