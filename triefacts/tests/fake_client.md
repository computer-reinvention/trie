---
trie_version: 0.1.9
source: tests/fake_client.py
file_fingerprint: 17ddeb0f4e67acd0e2f9c12ec7820235fed2153658f4f0180e628540b603e107
last_synced_at: '2026-07-20T09:53:37Z'
defines:
- kind: module
  qualified_name: tests/fake_client:__module__
  lines: 1-245
- kind: function
  qualified_name: tests/fake_client:_make_default_body
  lines: 8-9
- kind: class
  qualified_name: tests/fake_client:FakeTrieClient
  lines: 12-244
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
  qualified_name: tests/fake_client:FakeTrieClient.run_text
  lines: 163-226
- kind: method
  qualified_name: tests/fake_client:FakeTrieClient._extract_requested_qnames
  lines: 229-241
- kind: method
  qualified_name: tests/fake_client:FakeTrieClient.count_tokens
  lines: 243-244
incoming_refs: 92
outgoing_refs: 3
---
<!-- trie:section symbol=tests/fake_client:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=8ab7322b142a256effc96283d1b1444a68ae807ab35f52ec049dfa548d1ad88f source_ref=8dfa8300f3e84c7193b607f32b1fe8d92821397a role=test-infrastructure -->
Provides test doubles for the TrieClient to enable deterministic testing of LLM interactions.

- `FakeTrieClient` - deterministic test double that records calls and returns canned responses
- `_make_default_body` - generates default markdown body for symbol documentation
<!-- trie:end -->
<!-- trie:section symbol=tests/fake_client:_make_default_body fingerprint=c93d0b492761d8ec79615239de75f928f9ddd9f76b6f2844c1cee9586f630c57 body_fp=c5a24e78940d9406a6829a7fb7c52bad5af50c076398372915364971a681a619 source_ref=8dfa8300f3e84c7193b607f32b1fe8d92821397a role=test-infrastructure -->
## `_make_default_body`

Generates a default Markdown documentation body template for a given qualified symbol name.
<!-- trie:end -->
<!-- trie:section symbol=tests/fake_client:FakeTrieClient fingerprint=024d20c23b6895363d9553b604b95925edbc79e94449f432fc52db31a0280a1b body_fp=166a972c896931b69ff1b14153d21a37d8a0ffb7c5385b0a17aefce90273f8ce source_ref=7043450bc2c776769f4f0bdd5aa31f38c60da05b role=test -->
Test double for `TrieClient` that returns preconfigured structured outputs and records call parameters for verification.

- `run`: Routes to different output types based on the requested `output_type` model class
- `run_text`: Returns canned fenced-code-block plaintext for the code-gen path, inferring fixup/file/single-symbol shape from the prompt
- `model_id`: Returns the configured fake model identifier
- `count_tokens`: Always returns 100 for deterministic testing
- `calls`: Increments on each `run` or `run_text` call to track invocation count
- `last_*` attributes: Store the most recent call parameters for test assertions
- `output_*` attributes: Configure the canned responses returned by `run` and `run_text`
<!-- trie:end -->
<!-- trie:section symbol=tests/fake_client:FakeTrieClient.__init__ fingerprint=63f468c2eeed573a2e685611c12cf9c5a1593d6aec023162e5b465bca53cdc1c body_fp=39ae873a3d103a2c1633248ebaf1a35b16420ca082373b657bb68d24f31417f3 source_ref=8dfa8300f3e84c7193b607f32b1fe8d92821397a role=test-infrastructure -->
Initializes FakeTrieClient with configurable mock outputs and token counts.

- `output_notes`: defaults to `["* change return value  —  test"]`
- `output_reasons`: defaults to `["test"]`
- `output_taxonomy`: defaults to three standard role categories for testing
<!-- trie:end -->
<!-- trie:section symbol=tests/fake_client:FakeTrieClient.model_id fingerprint=97f92be530ac0cf7719ccd4e66d90df3ff1ec6a091d81261c51f210e24af53d3 body_fp=3cbf1ffbb67aa82f1ea500d7d494599fbf819914411a1e06d8b06448f55a20e2 source_ref=8dfa8300f3e84c7193b607f32b1fe8d92821397a role=test-infrastructure -->
Returns the FakeTrieClient's model identifier as a string.
<!-- trie:end -->
<!-- trie:section symbol=tests/fake_client:FakeTrieClient.run fingerprint=b415664ef59436207acfe87d115d47a521b20a17c5869aeff4231559d73980c6 body_fp=e8f6158d5836974a3e413c8583e4de40b31728aace83d9bc02b8fa544c1e450b source_ref=8dfa8300f3e84c7193b607f32b1fe8d92821397a role=test -->
FakeTrieClient method that simulates LLM calls by recording parameters and returning canned structured output based on output_type.

- Records all call parameters in instance attributes for test verification
- Returns predefined structured output matching the requested Pydantic model type
- Generates realistic default SectionBody content by extracting symbol name from user_prompt
- Creates mock usage statistics with configurable token counts
<!-- trie:end -->
<!-- trie:section symbol=tests/fake_client:FakeTrieClient.run_text fingerprint=6f8d46a0d20b77644cce10db9b39defa526b1878c22eba04ebbb626742fb959c body_fp=50e368721b948526caf71ad66b5cb74d25eda46d9ad5000a65f03433e86efcf7 source_ref=7043450bc2c776769f4f0bdd5aa31f38c60da05b role=test -->
Synthesise a canned `textgen`-formatted plaintext response from `FakeTrieClient`'s preconfigured fields, routing to fixup, file, or single-symbol output based on prompt content.

- `user_prompt`: inspected for diagnostic/fixup signals and `PROSE_OPEN_QNAME` delimiter to select output branch.
- Returns a `ModelResult` with `output` as a fenced-code-block string, not a `BaseModel`.
<!-- trie:end -->
<!-- trie:section symbol=tests/fake_client:FakeTrieClient._extract_requested_qnames fingerprint=b9bb7db81c5eb0ebf1d3ea64d9b4940fe443488afa119d2b7818f2034d4405f5 body_fp=781efdd0b955de30cae15b763f9e2c14ae23cfa46a3685c0d1b2a3adbf21490b source_ref=7043450bc2c776769f4f0bdd5aa31f38c60da05b role=util -->
Extract deduplicated, order-preserved qnames from prose-delimiter markers in `user_prompt`, returning `[""]` as fallback for legacy single-symbol prompts.
<!-- trie:end -->
<!-- trie:section symbol=tests/fake_client:FakeTrieClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=791dc2b9060d0603c4b69b34375c9260efcc1c180516d8d93796e8fbcc5d75de source_ref=8dfa8300f3e84c7193b607f32b1fe8d92821397a role=test-infrastructure -->
Returns a fixed token count of 100 for any prompt combination in FakeTrieClient tests.
<!-- trie:end -->