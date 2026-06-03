---
trie_version: 0.1.5
source: tests/fake_client.py
file_fingerprint: af7bc15b5f0cf20bec1e916105cf99a089a73228e131a20a015a0df512784c76
last_synced_at: '2026-06-03T21:17:51Z'
defines:
- kind: module
  qualified_name: tests/fake_client:__module__
  lines: 1-138
- kind: function
  qualified_name: tests/fake_client:_make_default_body
  lines: 8-9
- kind: class
  qualified_name: tests/fake_client:FakeTrieClient
  lines: 12-137
- kind: method
  qualified_name: tests/fake_client:FakeTrieClient.__init__
  lines: 19-54
- kind: method
  qualified_name: tests/fake_client:FakeTrieClient.model_id
  lines: 57-58
- kind: method
  qualified_name: tests/fake_client:FakeTrieClient.run
  lines: 60-134
- kind: method
  qualified_name: tests/fake_client:FakeTrieClient.count_tokens
  lines: 136-137
incoming_refs: 82
outgoing_refs: 2
---
<!-- trie:section symbol=tests/fake_client:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=7c896717304f03fb1266769941f21a61c86acfbfa47a863728499ddb2c607b4c source_ref=2531228f8acb585736a73a490870ae5a63bdfe87 -->
Test double module providing FakeTrieClient for deterministic testing of TrieClient interactions.

- Contains helper function to generate default documentation bodies
- Provides canned responses based on output type to verify prompt generation and token accounting
<!-- trie:end -->
<!-- trie:section symbol=tests/fake_client:_make_default_body fingerprint=c93d0b492761d8ec79615239de75f928f9ddd9f76b6f2844c1cee9586f630c57 body_fp=aaaf47826e7fcc6037e6ead6d2383eb5f87c30d3de1f8ac49adce0d072e299c0 source_ref=2531228f8acb585736a73a490870ae5a63bdfe87 -->
Generates a default Markdown documentation body with a heading and placeholder text for the given qualified name.
<!-- trie:end -->
<!-- trie:section symbol=tests/fake_client:FakeTrieClient fingerprint=5abb4ff676c1f72c4c801ffdc3318837243fec77566936c77b0f5dfa23098945 body_fp=b67ef2c57bb7f99f4745f0790f105a68f3726e7d17e6456f0f614d725a9026b0 source_ref=2531228f8acb585736a73a490870ae5a63bdfe87 -->
Test double that mocks TrieClient with configurable canned responses and records all method calls.

- `run`: returns ModelResult with output based on output_type parameter and preset field values
- `count_tokens`: always returns 100 regardless of input
- `calls`: tracks number of times run method was invoked
- `last_*`: stores parameters from most recent run call for test verification
<!-- trie:end -->
<!-- trie:section symbol=tests/fake_client:FakeTrieClient.__init__ fingerprint=38a05b65413e4ef41df7486ccbd447ba80ac1063b21ae6a59cc06215cf930f6c body_fp=956f8e1415b6ad50ed9bd96d9fb39bd4d26cb934ba43c65a9aaf5516466dbf6e source_ref=2531228f8acb585736a73a490870ae5a63bdfe87 -->
## `tests/fake_client:FakeTrieClient.__init__`

Initializes FakeTrieClient with canned output values and token counts for testing.

- `output_notes`: defaults to `["* change return value  —  test"]` if None
- `output_reasons`: defaults to `["test"]` if None
- `model_id`: stored as `full_model_id` attribute
- `calls`: initialized to 0 to track invocation count
<!-- trie:end -->
<!-- trie:section symbol=tests/fake_client:FakeTrieClient.model_id fingerprint=97f92be530ac0cf7719ccd4e66d90df3ff1ec6a091d81261c51f210e24af53d3 body_fp=f7dd8aed78ab2fbcb578ecf6658603fc440fc4f609a89ab11ce8456235a31dae source_ref=2531228f8acb585736a73a490870ae5a63bdfe87 -->
Returns the FakeTrieClient's model ID as a string property.
<!-- trie:end -->
<!-- trie:section symbol=tests/fake_client:FakeTrieClient.run fingerprint=200f4ae7f8e829284e069e67fa5284cd68ed649309d75665c47225b451616c79 body_fp=09ca68f5aab20fff86aca85f1fc4acfd9c5b00fb10c56749089a500a282ebf4d source_ref=2531228f8acb585736a73a490870ae5a63bdfe87 -->
FakeTrieClient run method simulates LLM calls by recording parameters and returning canned structured output.

- Records call count and all input parameters in instance attributes
- Returns pre-configured output based on output_type with fake token usage
- Supports SectionBody, MergeNotesOutput, SymbolEdit, FileEdit, BatchFilterOutput, and FixupOutput types
<!-- trie:end -->
<!-- trie:section symbol=tests/fake_client:FakeTrieClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=3aeb4635ead87c3491bcf7c1c22d3a2a709dc02874606ec0f49996c30dc0ce28 source_ref=2531228f8acb585736a73a490870ae5a63bdfe87 -->
FakeTrieClient method that returns a fixed token count for testing purposes.
<!-- trie:end -->