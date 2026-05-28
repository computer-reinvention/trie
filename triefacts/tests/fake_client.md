---
trie_version: 0.1.5
source: tests/fake_client.py
file_fingerprint: 4bc2d5e3f5017394dede812dd7c86e5a0d27b386e7166e7a508a11d846b6bf5d
last_synced_at: '2026-05-28T15:04:12Z'
defines:
- kind: module
  qualified_name: tests/fake_client:__module__
  lines: 1-135
- kind: function
  qualified_name: tests/fake_client:_make_default_body
  lines: 8-9
- kind: class
  qualified_name: tests/fake_client:FakeTrieClient
  lines: 12-134
- kind: method
  qualified_name: tests/fake_client:FakeTrieClient.__init__
  lines: 19-53
- kind: method
  qualified_name: tests/fake_client:FakeTrieClient.model_id
  lines: 56-57
- kind: method
  qualified_name: tests/fake_client:FakeTrieClient.run
  lines: 59-131
- kind: method
  qualified_name: tests/fake_client:FakeTrieClient.count_tokens
  lines: 133-134
incoming_refs: 82
outgoing_refs: 2
---
<!-- trie:section symbol=tests/fake_client:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=7c9adf9ebaac86d10909e711c72cc1d60fa6c107fc7efe0686a12a13e2cd5cd9 source_ref=4823170683910a0c815cd3d33e2fda31da8808d6 -->
## `tests/fake_client`

Provide a deterministic test double for `TrieClient` used across the test suite.
<!-- trie:end -->
<!-- trie:section symbol=tests/fake_client:_make_default_body fingerprint=c93d0b492761d8ec79615239de75f928f9ddd9f76b6f2844c1cee9586f630c57 body_fp=2d7bcd6ca9167191c5408a4d1c58244bda3ac961f4b6f0c0ff4a71666569129d source_ref=4823170683910a0c815cd3d33e2fda31da8808d6 -->
## `_make_default_body(qname: str) -> str`

Generate a minimal Markdown section body string for a given qualified name.
<!-- trie:end -->
<!-- trie:section symbol=tests/fake_client:FakeTrieClient fingerprint=bc09564df2920eb38f3e1a3fdc7c4a9b364df965fa25a3c598e7c7a8cfc9c624 body_fp=00d97d1ce2fcf6ed31ed30456b6744b0d98965d7cba1f9c443f66d76e2164af9 source_ref=9752d7c7a0bd5580dfd0af2afb98df81e9607ffb -->
## `FakeTrieClient`

Deterministic test double for `TrieClient` that records prompts and returns canned `ModelResult` outputs.

- `output_body`: canned `SectionBody` text; auto-generated from qname if `None`
- `output_prose`: canned prose string for `SymbolEdit`/`FileEdit` responses
- `output_notes`/`output_reasons`: canned fields for `MergeNotesOutput`
- `output_source`: canned source for `SymbolEdit`
- `output_file_content`: canned content for `FileEdit`
- `output_fixup_content`: canned content for `FixupOutput`
- `calls`: incremented on each `run` invocation
- `last_output_type`, `last_system_prompt`, `last_user_prompt`, `last_max_tokens`: captured from the most recent `run` call
<!-- trie:end -->
<!-- trie:section symbol=tests/fake_client:FakeTrieClient.__init__ fingerprint=1608520d677d1d7f5cc13e617f504e178d5c299577a13fb48fb96a0178e57f82 body_fp=3a70c710fd130a61a2593d5fdc21795c81fa99a7fe093013cc08fc4766c69ab0 source_ref=9752d7c7a0bd5580dfd0af2afb98df81e9607ffb -->
## `FakeTrieClient.__init__(self, *, output_body, output_prose, output_notes, output_reasons, output_source, output_file_content, output_fixup_content, input_tokens, output_tokens, cache_creation_input_tokens, cache_read_input_tokens, model_id)`

Initialise a `FakeTrieClient` with canned outputs and token counts for each supported response type.

- `output_body`: returned as `SectionBody.body`; auto-generated from prompt if `None`.
- `output_notes`: defaults to `["* change return value  —  test"]` when `None`.
- `output_reasons`: defaults to `["test"]` when `None`.
- `calls`, `last_output_type`, `last_system_prompt`, `last_user_prompt`, `last_max_tokens`: call-recording attributes initialised to zero/empty.
<!-- trie:end -->
<!-- trie:section symbol=tests/fake_client:FakeTrieClient.model_id fingerprint=97f92be530ac0cf7719ccd4e66d90df3ff1ec6a091d81261c51f210e24af53d3 body_fp=fa507c56e9e0c5d3dfc3c9cef5ab892cbe86c8488a40fa8f94039d093aa46d00 source_ref=4823170683910a0c815cd3d33e2fda31da8808d6 -->
## `FakeTrieClient.model_id`

The `full_model_id` string set at construction time.
<!-- trie:end -->
<!-- trie:section symbol=tests/fake_client:FakeTrieClient.run fingerprint=466a3535f542c6a3e6d477141cf870caeeebfb845e5ef05481c2d4536c4bbb1c body_fp=aa5e19505e14d316c8a1c5cc0c3d7356776a3ce08876aed51d991ac5a7ceaeb1 source_ref=9752d7c7a0bd5580dfd0af2afb98df81e9607ffb -->
## `FakeTrieClient.run(self, output_type, system_prompt, user_prompt, *, max_tokens=1024) -> ModelResult`

Record call parameters and return a canned `ModelResult` built from the instance's configured output fields.

- `output_type`: selects which model subclass to construct; raises `TypeError` for unsupported types.
- Records call count and last prompt/token values on the instance for test assertions.
<!-- trie:end -->
<!-- trie:section symbol=tests/fake_client:FakeTrieClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=9a00cc857b4117697cf5c1ea176403ed8b4e319eb6879934c9fd24ac1364cec4 source_ref=4823170683910a0c815cd3d33e2fda31da8808d6 -->
## `FakeTrieClient.count_tokens(self, system_prompt: str, user_prompt: str) -> int`

Always return 100 as a fixed token count stub for `FakeTrieClient`.
<!-- trie:end -->