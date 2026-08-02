---
trie_version: 0.3.0
source: tests/fake_client.py
file_fingerprint: 0d18b2c2cab5e0a1aae7dff95ef472d83c9b84faace25f84f24ffab23089bcaf
last_synced_at: '2026-08-01T01:52:31Z'
defines:
- kind: module
  qualified_name: tests/fake_client:__module__
  lines: 1-165
- kind: function
  qualified_name: tests/fake_client:_make_default_body
  lines: 8-9
  signature: 'def _make_default_body(qname: str) -> str'
- kind: class
  qualified_name: tests/fake_client:FakeTrieClient
  lines: 12-164
  signature: class FakeTrieClient
- kind: method
  qualified_name: tests/fake_client:FakeTrieClient.__init__
  lines: 19-69
  signature: 'def __init__( self, *, output_body: str | None = None, output_prose: str = "## Updated\n\nModified by patch.", output_notes: list[str] | None = None, output_reasons: list[str] | None = None, output_source: str | None = None, output_file_content: str | None = None, output_fixup_content: str | None = None, output_role: str = "domain", output_boundary: str = "internal", output_taxonomy: list[tuple[str, str]] | None = None, input_tokens: int = 10, output_tokens: int = 20, cache_creation_input_tokens: int = 0, cache_read_input_tokens: int = 0, model_id: str = "fake/test", ) -> None'
- kind: method
  qualified_name: tests/fake_client:FakeTrieClient.model_id
  lines: 72-73
  signature: def model_id(self) -> str
- kind: method
  qualified_name: tests/fake_client:FakeTrieClient.run
  lines: 75-161
  signature: 'def run( self, output_type: type[BaseModel], system_prompt: str, user_prompt: str, *, max_tokens: int = 1024, cache_prefix: str | None = None, ) -> ModelResult'
- kind: method
  qualified_name: tests/fake_client:FakeTrieClient.count_tokens
  lines: 163-164
  signature: 'def count_tokens(self, system_prompt: str, user_prompt: str) -> int'
incoming_refs: 80
outgoing_refs: 24
---
<!-- trie:section symbol=tests/fake_client:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=8ab7322b142a256effc96283d1b1444a68ae807ab35f52ec049dfa548d1ad88f source_ref=8dfa8300f3e84c7193b607f32b1fe8d92821397a role=test-infrastructure -->
Provides test doubles for the TrieClient to enable deterministic testing of LLM interactions.

- `FakeTrieClient` - deterministic test double that records calls and returns canned responses
- `_make_default_body` - generates default markdown body for symbol documentation
<!-- trie:end -->
<!-- trie:section symbol=tests/fake_client:_make_default_body fingerprint=c93d0b492761d8ec79615239de75f928f9ddd9f76b6f2844c1cee9586f630c57 body_fp=eec6b08af485a3b56ee8f9b42810819843d4f76c18754cebe6883e9d511614f2 source_ref=8dfa8300f3e84c7193b607f32b1fe8d92821397a role=test-infrastructure -->
## `def _make_default_body(qname: str) -> str`

Generates a default Markdown documentation body template for a given qualified symbol name.
<!-- trie:end -->
<!-- trie:section symbol=tests/fake_client:FakeTrieClient fingerprint=489eecbbf08929cafcc4726e6493e875f8f0104c9c5e0b632a84d49b6cb824fe body_fp=89ae2c1c6064a846fc5ca6c7b3c1e1c600a70a74bb840c88b1ec0eda22c5c34c source_ref=8dfa8300f3e84c7193b607f32b1fe8d92821397a role=test -->
## `class FakeTrieClient`

Test double for `TrieClient` that returns preconfigured structured outputs and records call parameters for verification.

- `run`: Routes to different output types based on the requested `output_type` model class
- `model_id`: Returns the configured fake model identifier
- `count_tokens`: Always returns 100 for deterministic testing
- `calls`: Increments on each `run` call to track invocation count
- `last_*` attributes: Store the most recent call parameters for test assertions
- `output_*` attributes: Configure the canned responses returned by `run`
<!-- trie:end -->
<!-- trie:section symbol=tests/fake_client:FakeTrieClient.__init__ fingerprint=63f468c2eeed573a2e685611c12cf9c5a1593d6aec023162e5b465bca53cdc1c body_fp=c21387defc9591af7aff5f747338709405f32b4d364e0189ad2e5850ee84b4f8 source_ref=8dfa8300f3e84c7193b607f32b1fe8d92821397a role=test-infrastructure -->
## `def __init__( self, *, output_body: str | None = None, output_prose: str = "## Updated\n\nModified by patch.", output_notes: list[str] | None = None, output_reasons: list[str] | None = None, output_source: str | None = None, output_file_content: str | None = None, output_fixup_content: str | None = None, output_role: str = "domain", output_boundary: str = "internal", output_taxonomy: list[tuple[str, str]] | None = None, input_tokens: int = 10, output_tokens: int = 20, cache_creation_input_tokens: int = 0, cache_read_input_tokens: int = 0, model_id: str = "fake/test", ) -> None`

Initializes FakeTrieClient with configurable mock outputs and token counts.

- `output_notes`: defaults to `["* change return value  —  test"]`
- `output_reasons`: defaults to `["test"]`
- `output_taxonomy`: defaults to three standard role categories for testing
<!-- trie:end -->
<!-- trie:section symbol=tests/fake_client:FakeTrieClient.model_id fingerprint=97f92be530ac0cf7719ccd4e66d90df3ff1ec6a091d81261c51f210e24af53d3 body_fp=59f20a95d2d9f4a9f0ebd3dd579eea86743d0deee8bd46b17d012bb258c069ad source_ref=8dfa8300f3e84c7193b607f32b1fe8d92821397a role=test-infrastructure -->
## `def model_id(self) -> str`

Returns the FakeTrieClient's model identifier as a string.
<!-- trie:end -->
<!-- trie:section symbol=tests/fake_client:FakeTrieClient.run fingerprint=b415664ef59436207acfe87d115d47a521b20a17c5869aeff4231559d73980c6 body_fp=51e1dac88754692b85c23b885199d5ad22a9296d7d9ce9ffce3805415d52d2e2 source_ref=8dfa8300f3e84c7193b607f32b1fe8d92821397a role=test -->
## `def run( self, output_type: type[BaseModel], system_prompt: str, user_prompt: str, *, max_tokens: int = 1024, cache_prefix: str | None = None, ) -> ModelResult`

FakeTrieClient method that simulates LLM calls by recording parameters and returning canned structured output based on output_type.

- Records all call parameters in instance attributes for test verification
- Returns predefined structured output matching the requested Pydantic model type
- Generates realistic default SectionBody content by extracting symbol name from user_prompt
- Creates mock usage statistics with configurable token counts
<!-- trie:end -->
<!-- trie:section symbol=tests/fake_client:FakeTrieClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=f20cf825d4a2bb753113a1ad55b25c8e8d3d01f659aeada4f1dbff86ce3540b0 source_ref=8dfa8300f3e84c7193b607f32b1fe8d92821397a role=test-infrastructure -->
## `def count_tokens(self, system_prompt: str, user_prompt: str) -> int`

Returns a fixed token count of 100 for any prompt combination in FakeTrieClient tests.
<!-- trie:end -->