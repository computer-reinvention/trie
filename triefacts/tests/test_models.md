---
trie_version: 0.1.5
source: tests/test_models.py
file_fingerprint: 8f1edbf377de7342617fc8884113224228431515ab09acca8bd8f2aea0c5b83d
last_synced_at: '2026-06-03T21:07:24Z'
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
<!-- trie:section symbol=tests/test_models:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=fc36a415c00edb2f85fb86d8d20b50c57e955b5a819872ef52f2cdf0b147f1bc source_ref=3d870eb114b9c996f1ff14ad3e9b03f32e00a0d5 -->
Tests for the TrieClient model interface, covering token counting, prompt payload construction, and pydantic-ai prompt caching integration.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models:_make_client fingerprint=a87fc52a2f0cb01b6398fe71cfd598d23333ce14a768a02b8cadfec453057b6e body_fp=8c5efd5bfef3ed32cf42e6a81f4ce3098da708e8bb69a936671eb35660fd4b42 source_ref=3d870eb114b9c996f1ff14ad3e9b03f32e00a0d5 -->
Creates a TrieClient with mocked Anthropic backend for testing token counting.

- `input_tokens`: value returned by the mocked count_tokens API call
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models:test_count_tokens_returns_input_tokens_from_api fingerprint=a028d47c66bae4b57a69b6d7037781a2e029fa9928bd671ade2f95c2220a6ba8 body_fp=401cb607b8dfd7a87c7ea7c7b37bb826cc7b71590e26127c5dee1500db6cdeb5 source_ref=3d870eb114b9c996f1ff14ad3e9b03f32e00a0d5 -->
Tests that TrieClient.count_tokens returns the input_tokens value from the Anthropic API response.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models:test_payload_includes_system_prompt fingerprint=0601063e0e3e26b827a2b0ee9f27f57eef2a5b99bed5d4aa2418b2fe5f1d3889 body_fp=bcb40626cf0b3e4b0f123b8068ac46cad99e6a4a415366eb32ddc25a0fb678dd source_ref=3d870eb114b9c996f1ff14ad3e9b03f32e00a0d5 -->
Verifies that TrieClient.count_tokens includes the system prompt in the API payload when provided.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models:test_payload_omits_system_key_when_empty fingerprint=7458917da8505fecea0545fe6177fdc24e1d2427cd83177d318e9c88fdf493c3 body_fp=1beaf43e9f79b1b247df34b8d33812e63a0d79b0c8d44315624f059a1d52f43a source_ref=3d870eb114b9c996f1ff14ad3e9b03f32e00a0d5 -->
Verifies TrieClient excludes the system key from API payload when system_prompt is empty.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models:test_payload_carries_model_and_user_message fingerprint=25b376588951dba6e8b4836074f61ec50fc9cdb94a4a39cffbc4f8397a56d079 body_fp=f1c93e7805e3f4e6e24a8e0048d7ea8feda9bb0066e382e7e325c12ad1c898d8 source_ref=3d870eb114b9c996f1ff14ad3e9b03f32e00a0d5 -->
Verifies that TrieClient.count_tokens passes the correct model name and user message structure to the underlying API.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models:test_empty_user_prompt_gets_nonwhitespace_placeholder fingerprint=ffe4abecc9bd68845bf49d218b64926fdd9ace393cc2ebfd0403b840d64edf02 body_fp=d7d6429427156fb3c18c70f43ee235fee3a7879b0a1cdb4bb91c36c2cc0915ba source_ref=3d870eb114b9c996f1ff14ad3e9b03f32e00a0d5 -->
Tests that TrieClient.count_tokens replaces empty/whitespace-only user prompts with non-whitespace placeholders.

- Verifies behavior for empty string, spaces-only, and newline/tab-only inputs
- Ensures API compliance when measuring cached prefix costs during planning
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models:_mock_agent fingerprint=5d921d57ad5ad09b4fc1dfe5a3ffc79ed26a5962b14ba670203ab8daac6a6552 body_fp=7f36f41ccda9bb2e1639ae2365602767db32217696df1e4eee7cbee0da5e08c9 source_ref=cd01e48f99e715d106504085b600e52b32176ce5 -->
Patches `trie.models.Agent` with an async mock that returns a canned `SectionBody` result, recording call arguments for inspection.

- Returns tuple of mocked Agent class and calls dictionary containing captured arguments
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models:test_run_without_cache_prefix_sends_bare_string fingerprint=caa80bfff386b0f6fd54edaa2ce9788b218cfebd3216710e9d27541355286f7a body_fp=b4013be915a707341de43bb99a8deb437581f2e1ebd14e5fc304034ad0dfef6a source_ref=cd01e48f99e715d106504085b600e52b32176ce5 -->
Verifies TrieClient.run passes user prompt directly when no cache prefix is provided.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models:test_run_with_cache_prefix_inserts_cachepoint fingerprint=7358de945990d8a124cacf2562d4ca168840e828b1d277b254d6851498d1c9bd body_fp=b93c99db0de6d7c5dfe1b7e226d5835d309d828d3fbbc3d8f40eae88af1f459b source_ref=cd01e48f99e715d106504085b600e52b32176ce5 -->
Verifies TrieClient.run inserts a CachePoint between cache_prefix and user_prompt when cache_prefix is provided.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models:test_run_caches_system_instructions fingerprint=3b36a8d3e4deb5a4cf342762aaf8ae850418601ec55f7c2117c0a462a582eb1c body_fp=adc3c54549c1d7386ea1cc1667953e978999d4c58e3f98024f37cd3eec3dce3d source_ref=cd01e48f99e715d106504085b600e52b32176ce5 -->
Verifies that TrieClient.run enables system instruction caching and sets max_tokens to 1024.
<!-- trie:end -->