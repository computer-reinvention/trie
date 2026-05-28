---
trie_version: 0.1.5
source: tests/test_models.py
file_fingerprint: 86fc0d8bf207018669eb36942ca2b6b38359ea1256b6e495c627c8c6ce496d53
last_synced_at: '2026-05-28T15:01:09Z'
defines:
- kind: module
  qualified_name: tests/test_models:__module__
  lines: 1-45
- kind: function
  qualified_name: tests/test_models:_make_client
  lines: 10-15
- kind: function
  qualified_name: tests/test_models:test_count_tokens_returns_input_tokens_from_api
  lines: 18-21
- kind: function
  qualified_name: tests/test_models:test_payload_includes_system_prompt
  lines: 24-29
- kind: function
  qualified_name: tests/test_models:test_payload_omits_system_key_when_empty
  lines: 32-36
- kind: function
  qualified_name: tests/test_models:test_payload_carries_model_and_user_message
  lines: 39-44
incoming_refs: 0
outgoing_refs: 2
---
<!-- trie:section symbol=tests/test_models:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=ddbef35b8571260ded695ed158a2c5098bf2dc72610879b94ce3b438526c21fd source_ref=afdf164a14b52d4a76e32a6ebe1eefd605ccd95d -->
## `tests/test_models`

Test `AnthropicClient.count_tokens` payload construction and token-count return value.

- `_make_client`: builds an `AnthropicClient` backed by a `MagicMock` Anthropic SDK object.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models:_make_client fingerprint=a87fc52a2f0cb01b6398fe71cfd598d23333ce14a768a02b8cadfec453057b6e body_fp=faa1c61ba8bbe9a13022373c3ed229180e72303d96dfdaac1d590daa3a04ef94 source_ref=11a322a9c5a070d7f4eb658eea13ca9a6b6ec710 -->
## `_make_client(input_tokens: int = 42) -> tuple[TrieClient, MagicMock]`

Build a test `TrieClient` backed by a `MagicMock` with a stubbed `count_tokens` response.

- `input_tokens`: value returned by the mock's `messages.count_tokens` call.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models:test_count_tokens_returns_input_tokens_from_api fingerprint=a028d47c66bae4b57a69b6d7037781a2e029fa9928bd671ade2f95c2220a6ba8 body_fp=f040ec1744d62c26552e5d1c80bca4dc4aa1bcf492172818697edb5bbfe3e0b9 source_ref=11a322a9c5a070d7f4eb658eea13ca9a6b6ec710 -->
## `test_count_tokens_returns_input_tokens_from_api()`

Assert that `TrieClient.count_tokens` returns the `input_tokens` value from the Anthropic API response.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models:test_payload_includes_system_prompt fingerprint=0601063e0e3e26b827a2b0ee9f27f57eef2a5b99bed5d4aa2418b2fe5f1d3889 body_fp=18a6d109fac042ed80e1c24a305a7e9b7b293c7aec4afcbf3ed3964bb0f6c176 source_ref=99da313a8f3c383c5db05edc6907868a8665e826 -->
## `test_payload_includes_system_prompt()`

Assert that `count_tokens` sends the correct model name and system prompt text to the API.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models:test_payload_omits_system_key_when_empty fingerprint=7458917da8505fecea0545fe6177fdc24e1d2427cd83177d318e9c88fdf493c3 body_fp=13beb07a897df2f65dfdc869b21bb5db20a8a9ff4e5bf5be3094ac0e2401c7b4 source_ref=11a322a9c5a070d7f4eb658eea13ca9a6b6ec710 -->
## `test_payload_omits_system_key_when_empty()`

Assert that `count_tokens` omits the `system` key from the API payload when `system_prompt` is empty.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models:test_payload_carries_model_and_user_message fingerprint=25b376588951dba6e8b4836074f61ec50fc9cdb94a4a39cffbc4f8397a56d079 body_fp=94cef4a9625d21e73e79e7dfffc7490fe28b81249fed76c37f219cdd4732884e source_ref=99da313a8f3c383c5db05edc6907868a8665e826 -->
## `test_payload_carries_model_and_user_message()`

Assert that `count_tokens` sends the correct model name and user message in the API payload.
<!-- trie:end -->