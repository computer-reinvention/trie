---
trie_version: 0.1.5
source: tests/fake_client.py
file_fingerprint: 0d18b2c2cab5e0a1aae7dff95ef472d83c9b84faace25f84f24ffab23089bcaf
last_synced_at: '2026-06-06T13:44:28Z'
defines:
- kind: module
  qualified_name: tests/fake_client:__module__
  lines: 1-165
- kind: function
  qualified_name: tests/fake_client:_make_default_body
  lines: 8-9
- kind: class
  qualified_name: tests/fake_client:FakeTrieClient
  lines: 12-164
- kind: method
  qualified_name: tests/fake_client:FakeTrieClient.__init__
  lines: 19-69
- kind: method
  qualified_name: tests/fake_client:FakeTrieClient.model_id
  lines: 72-73
- kind: method
  qualified_name: tests/fake_client:FakeTrieClient.run
  lines: 75-161
- kind: method
  qualified_name: tests/fake_client:FakeTrieClient.count_tokens
  lines: 163-164
incoming_refs: 90
outgoing_refs: 2
---
<!-- trie:section symbol=tests/fake_client:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=7c896717304f03fb1266769941f21a61c86acfbfa47a863728499ddb2c607b4c source_ref=2531228f8acb585736a73a490870ae5a63bdfe87 role=test-infrastructure -->
Test double module providing FakeTrieClient for deterministic testing of TrieClient interactions.

- Contains helper function to generate default documentation bodies
- Provides canned responses based on output type to verify prompt generation and token accounting
<!-- trie:end -->
<!-- trie:section symbol=tests/fake_client:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=8ab7322b142a256effc96283d1b1444a68ae807ab35f52ec049dfa548d1ad88f source_ref=8dfa8300f3e84c7193b607f32b1fe8d92821397a -->
Provides test doubles for the TrieClient to enable deterministic testing of LLM interactions.

- `FakeTrieClient` - deterministic test double that records calls and returns canned responses
- `_make_default_body` - generates default markdown body for symbol documentation
<!-- trie:end -->
<!-- trie:section symbol=tests/fake_client:_make_default_body fingerprint=c93d0b492761d8ec79615239de75f928f9ddd9f76b6f2844c1cee9586f630c57 body_fp=aaaf47826e7fcc6037e6ead6d2383eb5f87c30d3de1f8ac49adce0d072e299c0 source_ref=2531228f8acb585736a73a490870ae5a63bdfe87 role=test-infrastructure -->
Generates a default Markdown documentation body with a heading and placeholder text for the given qualified name.
<!-- trie:end -->
<!-- trie:section symbol=tests/fake_client:_make_default_body fingerprint=c93d0b492761d8ec79615239de75f928f9ddd9f76b6f2844c1cee9586f630c57 body_fp=c5a24e78940d9406a6829a7fb7c52bad5af50c076398372915364971a681a619 source_ref=8dfa8300f3e84c7193b607f32b1fe8d92821397a -->
## `_make_default_body`

Generates a default Markdown documentation body template for a given qualified symbol name.
<!-- trie:end -->
<!-- trie:section symbol=tests/fake_client:FakeTrieClient fingerprint=489eecbbf08929cafcc4726e6493e875f8f0104c9c5e0b632a84d49b6cb824fe body_fp=26badcc40fb197baa05c0afd152263bcf1e7c652c8bf58e0f1c8b49eb6c72e9a source_ref=8dfa8300f3e84c7193b607f32b1fe8d92821397a role=test -->
## `FakeTrieClient`

Test double for TrieClient that returns canned structured output and records call parameters for verification.

- Provides configurable output for different model output types with realistic defaults
- Records all run method parameters including prompts, tokens, and cache settings
- Returns ModelResult with mock usage statistics for token accounting tests
- Supports SectionBody, MergeNotesOutput, SymbolEdit, FileEdit, BatchFilterOutput, FixupOutput, RoleTaxonomy, and RoleTag outputs
<!-- trie:end -->
<!-- trie:section symbol=tests/fake_client:FakeTrieClient fingerprint=489eecbbf08929cafcc4726e6493e875f8f0104c9c5e0b632a84d49b6cb824fe body_fp=b12ad26b1863d27399fac007e71c06a0039111fb4df3fb478088313bdbd14542 source_ref=8dfa8300f3e84c7193b607f32b1fe8d92821397a -->
Test double for TrieClient that returns preconfigured structured outputs and records call parameters for verification.

- `run`: Routes to different output types based on the requested `output_type` model class
- `model_id`: Returns the configured fake model identifier
- `count_tokens`: Always returns 100 for deterministic testing
- `calls`: Increments on each `run` call to track invocation count
- `last_*` attributes: Store the most recent call parameters for test assertions
- `output_*` attributes: Configure the canned responses returned by `run`
<!-- trie:end -->
<!-- trie:section symbol=tests/fake_client:FakeTrieClient.__init__ fingerprint=63f468c2eeed573a2e685611c12cf9c5a1593d6aec023162e5b465bca53cdc1c body_fp=793f9fce87fd1fafcc19b9f6fe8443dca86e79825a55d334437a2106874934f8 source_ref=8dfa8300f3e84c7193b607f32b1fe8d92821397a role=model -->
## `tests/fake_client:FakeTrieClient.__init__`

Initializes FakeTrieClient with canned output values and token counts for testing.

- `output_notes`: defaults to `["* change return value  —  test"]` if None
- `output_reasons`: defaults to `["test"]` if None
- `output_taxonomy`: defaults to three role tuples (domain, persistence, api) if None
- `model_id`: stored as `full_model_id` attribute
- `calls`: initialized to 0 to track invocation count
<!-- trie:end -->
<!-- trie:section symbol=tests/fake_client:FakeTrieClient.__init__ fingerprint=63f468c2eeed573a2e685611c12cf9c5a1593d6aec023162e5b465bca53cdc1c body_fp=39ae873a3d103a2c1633248ebaf1a35b16420ca082373b657bb68d24f31417f3 source_ref=8dfa8300f3e84c7193b607f32b1fe8d92821397a -->
Initializes FakeTrieClient with configurable mock outputs and token counts.

- `output_notes`: defaults to `["* change return value  —  test"]`
- `output_reasons`: defaults to `["test"]`
- `output_taxonomy`: defaults to three standard role categories for testing
<!-- trie:end -->
<!-- trie:section symbol=tests/fake_client:FakeTrieClient.model_id fingerprint=97f92be530ac0cf7719ccd4e66d90df3ff1ec6a091d81261c51f210e24af53d3 body_fp=f7dd8aed78ab2fbcb578ecf6658603fc440fc4f609a89ab11ce8456235a31dae source_ref=2531228f8acb585736a73a490870ae5a63bdfe87 role=test-infrastructure -->
Returns the FakeTrieClient's model ID as a string property.
<!-- trie:end -->
<!-- trie:section symbol=tests/fake_client:FakeTrieClient.model_id fingerprint=97f92be530ac0cf7719ccd4e66d90df3ff1ec6a091d81261c51f210e24af53d3 body_fp=3cbf1ffbb67aa82f1ea500d7d494599fbf819914411a1e06d8b06448f55a20e2 source_ref=8dfa8300f3e84c7193b607f32b1fe8d92821397a -->
Returns the FakeTrieClient's model identifier as a string.
<!-- trie:end -->
<!-- trie:section symbol=tests/fake_client:FakeTrieClient.run fingerprint=b415664ef59436207acfe87d115d47a521b20a17c5869aeff4231559d73980c6 body_fp=dba5e12cb4dae968649d8cf8943808c6445ea7eb56cc72a9105251bb3ae40939 source_ref=8dfa8300f3e84c7193b607f32b1fe8d92821397a role=test -->
FakeTrieClient.run returns canned structured output based on requested type, recording call parameters for test verification.

- Records prompts, max_tokens, cache_prefix, and increments call count
- Returns different model instances based on output_type parameter
- For SectionBody: extracts qname from user_prompt if output_body is None
- Usage object includes configurable token counts and cache metrics
<!-- trie:end -->
<!-- trie:section symbol=tests/fake_client:FakeTrieClient.run fingerprint=b415664ef59436207acfe87d115d47a521b20a17c5869aeff4231559d73980c6 body_fp=e8f6158d5836974a3e413c8583e4de40b31728aace83d9bc02b8fa544c1e450b source_ref=8dfa8300f3e84c7193b607f32b1fe8d92821397a -->
FakeTrieClient method that simulates LLM calls by recording parameters and returning canned structured output based on output_type.

- Records all call parameters in instance attributes for test verification
- Returns predefined structured output matching the requested Pydantic model type
- Generates realistic default SectionBody content by extracting symbol name from user_prompt
- Creates mock usage statistics with configurable token counts
<!-- trie:end -->
<!-- trie:section symbol=tests/fake_client:FakeTrieClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=3aeb4635ead87c3491bcf7c1c22d3a2a709dc02874606ec0f49996c30dc0ce28 source_ref=2531228f8acb585736a73a490870ae5a63bdfe87 role=test-infrastructure -->
FakeTrieClient method that returns a fixed token count for testing purposes.
<!-- trie:end -->
<!-- trie:section symbol=tests/fake_client:FakeTrieClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=791dc2b9060d0603c4b69b34375c9260efcc1c180516d8d93796e8fbcc5d75de source_ref=8dfa8300f3e84c7193b607f32b1fe8d92821397a -->
Returns a fixed token count of 100 for any prompt combination in FakeTrieClient tests.
<!-- trie:end -->