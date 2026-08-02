---
trie_version: 0.3.0
source: tests/test_config.py
file_fingerprint: 8024154fe32c6249fdf9e9b7038a70e421f7ed78a88e2b6510d5331674feaf36
last_synced_at: '2026-08-01T14:59:14Z'
defines:
- kind: module
  qualified_name: tests/test_config:__module__
  lines: 1-104
- kind: function
  qualified_name: tests/test_config:test_defaults_when_empty_dict
  lines: 10-17
  signature: def test_defaults_when_empty_dict()
- kind: function
  qualified_name: tests/test_config:test_resolver_defaults
  lines: 20-24
  signature: def test_resolver_defaults()
- kind: function
  qualified_name: tests/test_config:test_resolver_overrides
  lines: 27-39
  signature: def test_resolver_overrides()
- kind: function
  qualified_name: tests/test_config:test_resolver_config_gates_specs
  lines: 42-52
  signature: def test_resolver_config_gates_specs()
- kind: function
  qualified_name: tests/test_config:test_overrides_merge_per_section
  lines: 55-69
  signature: def test_overrides_merge_per_section()
- kind: function
  qualified_name: tests/test_config:test_load_roundtrips_default_template
  lines: 72-77
  signature: 'def test_load_roundtrips_default_template(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_config:test_find_and_load_walks_up
  lines: 80-86
  signature: 'def test_find_and_load_walks_up(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_config:test_find_and_load_raises_when_missing
  lines: 89-91
  signature: 'def test_find_and_load_raises_when_missing(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_config:test_unknown_top_level_keys_are_ignored
  lines: 94-97
  signature: 'def test_unknown_top_level_keys_are_ignored(): # Forward-compat: future versions may add sections; old trie shouldn''t crash.'
- kind: function
  qualified_name: tests/test_config:test_unknown_keys_within_known_section_raise
  lines: 100-103
  signature: 'def test_unknown_keys_within_known_section_raise(): # Typos within a known section should fail loudly.'
incoming_refs: 0
outgoing_refs: 25
---
<!-- trie:section symbol=tests/test_config:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=4c19dcc1dd79e84522cba2e81e74fb8cbde04913c1a842843b260f43a9ca9b73 source_ref=ce0170296e1b69f535154cc3d8fa01546c83fc5e role=test-infrastructure -->
Tests configuration loading, merging, and validation for the Config class.

- `test_defaults_when_empty_dict`: Verifies default values are applied when no config is provided
- `test_overrides_merge_per_section`: Tests section-level merging preserves defaults in untouched sections
- `test_load_roundtrips_default_template`: Validates loading from TOML file works correctly
- `test_find_and_load_walks_up`: Tests filesystem traversal to locate config files
- `test_find_and_load_raises_when_missing`: Ensures ConfigNotFoundError is raised when no config found
- `test_unknown_top_level_keys_are_ignored`: Verifies forward compatibility with unknown sections
- `test_unknown_keys_within_known_section_raise`: Ensures typos in known sections fail loudly
<!-- trie:end -->
<!-- trie:section symbol=tests/test_config:test_defaults_when_empty_dict fingerprint=066aeae5689065e419890e05123f580e116ce68b914243ce1b10f34c16ba263e body_fp=b7cba99d759b9556dea086005dbfcb5b7475bc6e4ffe0c9e8cc1976bd1f8be82 source_ref=2ca0238ab756d0c60b52d70fdaccabde793f48a0 role=test -->
## `def test_defaults_when_empty_dict()`

Verifies that `Config.from_dict` uses default values when initialized with empty dictionary.

- Checks version, scope patterns, triefacts root, model names, and cascade settings
- Uses assertion-based verification of expected default configuration values
<!-- trie:end -->
<!-- trie:section symbol=tests/test_config:test_resolver_defaults fingerprint=4ae5ba89041145ad9bb8a42db5266fc9bd436457b3b0c177fa604868634daaab body_fp=635a69d6101f2ab3aaa11a8ea8bbd5c29fc6b40a3b0fdfa6462984f535df4f48 source_ref=2ca0238ab756d0c60b52d70fdaccabde793f48a0 role=test -->
## `def test_resolver_defaults()`

Assert that `Config.from_dict({})` produces resolver defaults: `enabled=True`, `disabled_languages=[]`, `servers={}`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_config:test_resolver_overrides fingerprint=712f4d1baaea759d15cb55edaf443cdc0d8266b6b06c4dec4084dfe79018a6e4 body_fp=af31ee220108a2bbc6b190cc58cf42512f8dbd8513433b6ce3a7a9deea64213f source_ref=2ca0238ab756d0c60b52d70fdaccabde793f48a0 role=test -->
## `def test_resolver_overrides()`

Verify that resolver config fields (`enabled`, `disabled_languages`, `servers`) correctly override defaults when supplied via `Config.from_dict`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_config:test_resolver_config_gates_specs fingerprint=82d7995478c0bef11b738d21cb9b549ada75e9de2c50839ec6764dfe61686537 body_fp=1ec1c6fecfa08379ee5541ad31b356034554a1327147bf264358c2631576c3fd source_ref=3d37fa183314a6c47e966911cbaba79329583648 role=test -->
## `def test_resolver_config_gates_specs()`

Verify that `specs.configure_resolver` gates language spec resolution, returning `None` for disabled or globally-disabled languages.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_config:test_overrides_merge_per_section fingerprint=0b95159c2bf1033bd97534168110a5f7883670992535e93232c8724fa675f634 body_fp=f51c3bfd8610320250a437cf9e5e883c6ccfa8ae2fdc42b1b1a1e81dd2023d0a source_ref=d03a084837bba170473c3f70129ef79f0faeecb9 role=test -->
## `def test_overrides_merge_per_section()`

Tests that `Config.from_dict` merges overrides per section while preserving defaults for untouched sections and keys.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_config:test_load_roundtrips_default_template fingerprint=333b6309d910ec325894a15776b361f1510c756466a548083fb8d124b2abf6a5 body_fp=0f5a9f6be7ab56dd419589c729628eb426d703660a91b721cf50bd4db3c8b2ea source_ref=2ca0238ab756d0c60b52d70fdaccabde793f48a0 role=test -->
## `def test_load_roundtrips_default_template(tmp_path: Path)`

Verifies that Config.load can parse the default TOML configuration template and produces expected defaults.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_config:test_find_and_load_walks_up fingerprint=c2e6b43592156a913d5cfee00fbb8028609cdf2318d3de8a975915503cbec7dd body_fp=fa0f35064fd1db5596e0e148c84f018c111c6270ad0fbe8cdfb488eab5d0e9a5 source_ref=2ca0238ab756d0c60b52d70fdaccabde793f48a0 role=test -->
## `def test_find_and_load_walks_up(tmp_path: Path)`

Verifies Config.find_and_load() walks up from deeply nested directories to find configuration files.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_config:test_find_and_load_raises_when_missing fingerprint=34e4b7c5c6730ec2a6f2bf88e37ab6412ebad59f63491fcba83fb3be61de3093 body_fp=9326c3e213f9142eb75738b0ad155bc1a66887f68c03dda6af811975d86555f6 source_ref=ce0170296e1b69f535154cc3d8fa01546c83fc5e role=test-infrastructure -->
## `def test_find_and_load_raises_when_missing(tmp_path: Path)`

Verifies Config.find_and_load raises ConfigNotFoundError when no configuration file is found in the directory tree.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_config:test_unknown_top_level_keys_are_ignored fingerprint=406e28384661339d41a663749e228fb9f5c3b5f901bf1174a1faf4bec5565895 body_fp=0718b674f2a37af71fea14a06f29245b4d597845dc548804dedf8234545a6dea source_ref=2ca0238ab756d0c60b52d70fdaccabde793f48a0 role=test-infrastructure -->
## `def test_unknown_top_level_keys_are_ignored(): # Forward-compat: future versions may add sections; old trie shouldn't crash.`

Verifies Config.from_dict ignores unknown top-level sections for forward compatibility.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_config:test_unknown_keys_within_known_section_raise fingerprint=8e6e05e7e17ed2a96bd9abfe62dd6db3ef656dae01c649e891afb67f5f7de532 body_fp=e34507ff63302fefa38109b179c6d2fc4a74832ba0a89f3dcdc0cc8199dd061c source_ref=2ca0238ab756d0c60b52d70fdaccabde793f48a0 role=config-management -->
## `def test_unknown_keys_within_known_section_raise(): # Typos within a known section should fail loudly.`

Verifies that Config.from_dict raises TypeError when given unknown keys within known configuration sections.
<!-- trie:end -->