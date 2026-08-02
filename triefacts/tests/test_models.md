---
trie_version: 0.3.0
source: tests/test_models.py
file_fingerprint: f88ed091cf71cbf29e268a0c15198e39859ca76319de786885b50b1bfb35eaa5
last_synced_at: '2026-08-01T01:51:58Z'
defines:
- kind: module
  qualified_name: tests/test_models:__module__
  lines: 1-148
- kind: function
  qualified_name: tests/test_models:_make_client
  lines: 13-18
  signature: 'def _make_client(input_tokens: int = 42) -> tuple[TrieClient, MagicMock]'
- kind: function
  qualified_name: tests/test_models:test_count_tokens_returns_input_tokens_from_api
  lines: 21-24
  signature: def test_count_tokens_returns_input_tokens_from_api()
- kind: function
  qualified_name: tests/test_models:test_payload_includes_system_prompt
  lines: 27-32
  signature: def test_payload_includes_system_prompt()
- kind: function
  qualified_name: tests/test_models:test_payload_omits_system_key_when_empty
  lines: 35-39
  signature: def test_payload_omits_system_key_when_empty()
- kind: function
  qualified_name: tests/test_models:test_payload_carries_model_and_user_message
  lines: 42-47
  signature: def test_payload_carries_model_and_user_message()
- kind: function
  qualified_name: tests/test_models:test_empty_user_prompt_gets_nonwhitespace_placeholder
  lines: 50-59
  signature: 'def test_empty_user_prompt_gets_nonwhitespace_placeholder(): # The Anthropic API rejects empty or whitespace-only user content, but the # plan-time cost preview passes an empty prompt to measure only the cached # prefix. The client must substitute a non-whitespace placeholder.'
- kind: function
  qualified_name: tests/test_models:_mock_agent
  lines: 69-96
  signature: def _mock_agent(mocker)
- kind: function
  qualified_name: tests/test_models:test_run_without_cache_prefix_sends_bare_string
  lines: 99-105
  signature: def test_run_without_cache_prefix_sends_bare_string(mocker)
- kind: function
  qualified_name: tests/test_models:test_run_with_cache_prefix_inserts_cachepoint
  lines: 108-122
  signature: def test_run_with_cache_prefix_inserts_cachepoint(mocker)
- kind: function
  qualified_name: tests/test_models:test_run_caches_system_instructions
  lines: 125-133
  signature: def test_run_caches_system_instructions(mocker)
- kind: function
  qualified_name: tests/test_models:test_batch_filter_output_tolerates_empty_object
  lines: 136-147
  signature: def test_batch_filter_output_tolerates_empty_object()
incoming_refs: 0
outgoing_refs: 22
---
<!-- trie:section symbol=tests/test_models:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=3744fb3808fe3555bb15d5f07f548cd7c8584688007f6c4b27c159e4a823e3cf source_ref=cd01e48f99e715d106504085b600e52b32176ce5 role=test-infrastructure -->
Tests for the `trie.models` module, focusing on `TrieClient` token counting and prompt caching behavior.

- Validates token counting API calls and payload structure
- Ensures prompt caching integration works correctly with pydantic-ai Agent
- Tests edge cases like empty prompts and system message handling
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models:_make_client fingerprint=a87fc52a2f0cb01b6398fe71cfd598d23333ce14a768a02b8cadfec453057b6e body_fp=8d0b0822f4a2aa89a99fa1f55a6fdd244bdf13c6e03e0698df8ce2ba9b2fb8c4 source_ref=5cc4e8f43f2f4332eaa79612f94c3e1071fb95ff role=test -->
## `def _make_client(input_tokens: int = 42) -> tuple[TrieClient, MagicMock]`

Creates a TrieClient with a mocked Anthropic client for testing token counting functionality.

- `input_tokens`: configures the mock to return this token count from count_tokens calls
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models:test_count_tokens_returns_input_tokens_from_api fingerprint=a028d47c66bae4b57a69b6d7037781a2e029fa9928bd671ade2f95c2220a6ba8 body_fp=95f2c8f5182d4feebc69d8d0af574fa74b350be2a84adfc07c288223e7f9f21c source_ref=cd01e48f99e715d106504085b600e52b32176ce5 role=llm-client -->
## `def test_count_tokens_returns_input_tokens_from_api()`

Verifies TrieClient.count_tokens returns the input_tokens value from the Anthropic API response.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models:test_payload_includes_system_prompt fingerprint=0601063e0e3e26b827a2b0ee9f27f57eef2a5b99bed5d4aa2418b2fe5f1d3889 body_fp=9ba88c2a5c6408daf6209de2dea77185e14b9aedb3f1c965d1a3d54989ae7aeb source_ref=cd01e48f99e715d106504085b600e52b32176ce5 role=llm-client -->
## `def test_payload_includes_system_prompt()`

Verifies TrieClient.count_tokens includes system prompt in API payload with correct model and system text structure.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models:test_payload_omits_system_key_when_empty fingerprint=7458917da8505fecea0545fe6177fdc24e1d2427cd83177d318e9c88fdf493c3 body_fp=f8297ce29ba153a83a132ceaa5e8c90b5e62698282c60081bbfea82796188182 source_ref=cd01e48f99e715d106504085b600e52b32176ce5 role=test-infrastructure -->
## `def test_payload_omits_system_key_when_empty()`

Verifies that TrieClient.count_tokens excludes the system key from API payload when system_prompt is empty.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models:test_payload_carries_model_and_user_message fingerprint=25b376588951dba6e8b4836074f61ec50fc9cdb94a4a39cffbc4f8397a56d079 body_fp=bfe41f36757744c46c432d7418481037128846a6163c566cf9cd96fe4b97cce6 source_ref=cd01e48f99e715d106504085b600e52b32176ce5 role=test-infrastructure -->
## `def test_payload_carries_model_and_user_message()`

Verifies that TrieClient.count_tokens includes model name and user message in API payload.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models:test_empty_user_prompt_gets_nonwhitespace_placeholder fingerprint=ffe4abecc9bd68845bf49d218b64926fdd9ace393cc2ebfd0403b840d64edf02 body_fp=d20aa6eacf30e96aacb070f171620ea109fbda8af822761fd47f17b1f8b67d39 source_ref=cd01e48f99e715d106504085b600e52b32176ce5 role=llm-client -->
## `def test_empty_user_prompt_gets_nonwhitespace_placeholder(): # The Anthropic API rejects empty or whitespace-only user content, but the # plan-time cost preview passes an empty prompt to measure only the cached # prefix. The client must substitute a non-whitespace placeholder.`

Tests that TrieClient.count_tokens substitutes non-whitespace placeholder for empty or whitespace-only user prompts.

- Verifies placeholder content is non-whitespace when user_prompt is empty, spaces, or tabs
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models:_mock_agent fingerprint=69e504eca40dd7272598afc8597bdedad27cf4e3f02efab7a599528ca424fd26 body_fp=904be2d98c9be8998db2fc581d5b147e60e23fb690ce99d59d7437ed2004e07f source_ref=4145f3e553fb1593dbbb485f4b60ec4984b8e1f4 role=test -->
## `def _mock_agent(mocker)`

Patches `trie.models.Agent` (via the lazy `_sdk()` namespace) to return canned results and record calls for testing.

- Returns tuple of (mock agent class, calls dict) for test assertions
- Mock run method returns fake SectionBody output with predetermined usage stats
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models:test_run_without_cache_prefix_sends_bare_string fingerprint=caa80bfff386b0f6fd54edaa2ce9788b218cfebd3216710e9d27541355286f7a body_fp=8436a77c43cc5e5eaa623e5ffd2184c959d5703a5adcaf23d66704db5ba8bae1 source_ref=5cc4e8f43f2f4332eaa79612f94c3e1071fb95ff role=test -->
## `def test_run_without_cache_prefix_sends_bare_string(mocker)`

Verifies TrieClient.run passes the user prompt as a plain string when no cache prefix is provided.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models:test_run_with_cache_prefix_inserts_cachepoint fingerprint=7358de945990d8a124cacf2562d4ca168840e828b1d277b254d6851498d1c9bd body_fp=461aa8bb1f4f2e9bfc52998aabfea90b3d26c4c9f41900b173a292cfb3b20ee8 source_ref=5cc4e8f43f2f4332eaa79612f94c3e1071fb95ff role=test -->
## `def test_run_with_cache_prefix_inserts_cachepoint(mocker)`

Tests that TrieClient.run with cache_prefix creates a three-element user input list with cache prefix, CachePoint, and user prompt.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models:test_run_caches_system_instructions fingerprint=3b36a8d3e4deb5a4cf342762aaf8ae850418601ec55f7c2117c0a462a582eb1c body_fp=a425859ad31bcf421ee4bd520bcb95452ec2c548c316b979a31d2c29f4f8e203 source_ref=5cc4e8f43f2f4332eaa79612f94c3e1071fb95ff role=test -->
## `def test_run_caches_system_instructions(mocker)`

Verifies TrieClient.run passes anthropic_cache_instructions=True and max_tokens=1024 in model_settings.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models:test_batch_filter_output_tolerates_empty_object fingerprint=72f3b581341ea22e805b3f44c40b2b8298c646765cde22c8bf6466b0a2446f4c body_fp=72ce906455accfcf1d15069c3a41c103c8686f07dac417944d8971866f073e5f source_ref=5cc4e8f43f2f4332eaa79612f94c3e1071fb95ff role=test -->
## `def test_batch_filter_output_tolerates_empty_object()`

Assert that `BatchFilterOutput` validates an empty dict `{}` to an instance with `decisions == []`, preventing a pydantic `ValidationError` regression.
<!-- trie:end -->