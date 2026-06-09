---
trie_version: 0.1.5
source: tests/test_models.py
file_fingerprint: 8f1edbf377de7342617fc8884113224228431515ab09acca8bd8f2aea0c5b83d
last_synced_at: '2026-06-07T05:47:08Z'
defines:
- kind: module
  qualified_name: tests/test_models:__module__
  lines: 1-132
- kind: function
  qualified_name: tests/test_models:_make_client
  lines: 13-18
- kind: function
  qualified_name: tests/test_models:test_count_tokens_returns_input_tokens_from_api
  lines: 21-24
- kind: function
  qualified_name: tests/test_models:test_payload_includes_system_prompt
  lines: 27-32
- kind: function
  qualified_name: tests/test_models:test_payload_omits_system_key_when_empty
  lines: 35-39
- kind: function
  qualified_name: tests/test_models:test_payload_carries_model_and_user_message
  lines: 42-47
- kind: function
  qualified_name: tests/test_models:test_empty_user_prompt_gets_nonwhitespace_placeholder
  lines: 50-59
- kind: function
  qualified_name: tests/test_models:_mock_agent
  lines: 69-94
- kind: function
  qualified_name: tests/test_models:test_run_without_cache_prefix_sends_bare_string
  lines: 97-103
- kind: function
  qualified_name: tests/test_models:test_run_with_cache_prefix_inserts_cachepoint
  lines: 106-120
- kind: function
  qualified_name: tests/test_models:test_run_caches_system_instructions
  lines: 123-131
incoming_refs: 0
outgoing_refs: 12
---
<!-- trie:section symbol=tests/test_models:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=3744fb3808fe3555bb15d5f07f548cd7c8584688007f6c4b27c159e4a823e3cf source_ref=cd01e48f99e715d106504085b600e52b32176ce5 role=test-infrastructure -->
Tests for the `trie.models` module, focusing on `TrieClient` token counting and prompt caching behavior.

- Validates token counting API calls and payload structure
- Ensures prompt caching integration works correctly with pydantic-ai Agent
- Tests edge cases like empty prompts and system message handling
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models:_make_client fingerprint=a87fc52a2f0cb01b6398fe71cfd598d23333ce14a768a02b8cadfec453057b6e body_fp=59c2016d33cb90c7c93194cb9d923e4e6492004e2888658b1ebd7acb4b0c57f8 source_ref=cd01e48f99e715d106504085b600e52b32176ce5 role=util -->
Creates a TrieClient with a mocked Anthropic client for testing token counting functionality.

- `input_tokens`: configures the mock to return this token count from count_tokens calls
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models:test_count_tokens_returns_input_tokens_from_api fingerprint=a028d47c66bae4b57a69b6d7037781a2e029fa9928bd671ade2f95c2220a6ba8 body_fp=e4ca717385e614bc159e180d12f5c75a31bf8560c07bea047a9c682bac7d148a source_ref=cd01e48f99e715d106504085b600e52b32176ce5 role=llm-client -->
Verifies TrieClient.count_tokens returns the input_tokens value from the Anthropic API response.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models:test_payload_includes_system_prompt fingerprint=0601063e0e3e26b827a2b0ee9f27f57eef2a5b99bed5d4aa2418b2fe5f1d3889 body_fp=a271125c1d7e97f8106495b43939c3b98a91f9edbb755bd191ab205e16d5fb2a source_ref=cd01e48f99e715d106504085b600e52b32176ce5 role=llm-client -->
Verifies TrieClient.count_tokens includes system prompt in API payload with correct model and system text structure.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models:test_payload_omits_system_key_when_empty fingerprint=7458917da8505fecea0545fe6177fdc24e1d2427cd83177d318e9c88fdf493c3 body_fp=d8758128d581e02038b90b79481b3877b5bd9eacf4045d4c53848cdd664927c8 source_ref=cd01e48f99e715d106504085b600e52b32176ce5 role=test-infrastructure -->
Verifies that TrieClient.count_tokens excludes the system key from API payload when system_prompt is empty.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models:test_payload_carries_model_and_user_message fingerprint=25b376588951dba6e8b4836074f61ec50fc9cdb94a4a39cffbc4f8397a56d079 body_fp=618885a8e33c984fcd0a325fb0a8c2dfa3d6024025f5ba137ee5da735f469add source_ref=cd01e48f99e715d106504085b600e52b32176ce5 role=test-infrastructure -->
Verifies that TrieClient.count_tokens includes model name and user message in API payload.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models:test_empty_user_prompt_gets_nonwhitespace_placeholder fingerprint=ffe4abecc9bd68845bf49d218b64926fdd9ace393cc2ebfd0403b840d64edf02 body_fp=0429ea25a957c970bf085f0db3411755a85bdbbc14839712db1b17ab5a23421b source_ref=cd01e48f99e715d106504085b600e52b32176ce5 role=llm-client -->
Tests that TrieClient.count_tokens substitutes non-whitespace placeholder for empty or whitespace-only user prompts.

- Verifies placeholder content is non-whitespace when user_prompt is empty, spaces, or tabs
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models:_mock_agent fingerprint=5d921d57ad5ad09b4fc1dfe5a3ffc79ed26a5962b14ba670203ab8daac6a6552 body_fp=94fa3fe6fbfa42c6025d585c97214f940ac52fcfd869980a471ceeae08c769ab source_ref=cd01e48f99e715d106504085b600e52b32176ce5 role=test -->
Patches trie.models.Agent to return canned results and record calls for testing.

• Returns tuple of (mock agent class, calls dict) for test assertions
• Mock run method returns fake SectionBody output with predetermined usage stats
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models:test_run_without_cache_prefix_sends_bare_string fingerprint=caa80bfff386b0f6fd54edaa2ce9788b218cfebd3216710e9d27541355286f7a body_fp=b4a57fba20362fc3df7469ca07712c7ea24a3361a051035de56d07eb08a15783 source_ref=cd01e48f99e715d106504085b600e52b32176ce5 role=test -->
Verifies TrieClient.run passes the user prompt as a plain string when no cache prefix is provided.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models:test_run_with_cache_prefix_inserts_cachepoint fingerprint=7358de945990d8a124cacf2562d4ca168840e828b1d277b254d6851498d1c9bd body_fp=6a64f08d49877c2ecb9f1adcdad8b9aba7166be12e7f557d3478ff22d6a304d7 source_ref=cd01e48f99e715d106504085b600e52b32176ce5 role=test -->
Tests that TrieClient.run with cache_prefix creates a three-element user input list with cache prefix, CachePoint, and user prompt.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models:test_run_caches_system_instructions fingerprint=3b36a8d3e4deb5a4cf342762aaf8ae850418601ec55f7c2117c0a462a582eb1c body_fp=a4daf31905cfcd5c45b6d43e13229f698e250eaa2041b9285bb6bdb59231b65b source_ref=cd01e48f99e715d106504085b600e52b32176ce5 role=test -->
Verifies TrieClient.run passes anthropic_cache_instructions=True and max_tokens=1024 in model_settings.
<!-- trie:end -->