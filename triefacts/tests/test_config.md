---
trie_version: 0.1.9
source: tests/test_config.py
file_fingerprint: 7ecefff2079a1cb6887a8b5420ffffa320bee5cd2ecdcc3cd2e97a499c128db7
last_synced_at: '2026-07-29T02:54:40Z'
defines:
- kind: module
  qualified_name: tests/test_config:__module__
  lines: 1-104
- kind: function
  qualified_name: tests/test_config:test_defaults_when_empty_dict
  lines: 10-17
- kind: function
  qualified_name: tests/test_config:test_resolver_defaults
  lines: 20-24
- kind: function
  qualified_name: tests/test_config:test_resolver_overrides
  lines: 27-39
- kind: function
  qualified_name: tests/test_config:test_resolver_config_gates_specs
  lines: 42-52
- kind: function
  qualified_name: tests/test_config:test_overrides_merge_per_section
  lines: 55-69
- kind: function
  qualified_name: tests/test_config:test_load_roundtrips_default_template
  lines: 72-77
- kind: function
  qualified_name: tests/test_config:test_find_and_load_walks_up
  lines: 80-86
- kind: function
  qualified_name: tests/test_config:test_find_and_load_raises_when_missing
  lines: 89-91
- kind: function
  qualified_name: tests/test_config:test_unknown_top_level_keys_are_ignored
  lines: 94-97
- kind: function
  qualified_name: tests/test_config:test_unknown_keys_within_known_section_raise
  lines: 100-103
incoming_refs: 0
outgoing_refs: 12
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
<!-- trie:section symbol=tests/test_config:test_defaults_when_empty_dict fingerprint=066aeae5689065e419890e05123f580e116ce68b914243ce1b10f34c16ba263e body_fp=668330ccfa005e543658cf2d9ef63d977b7afdb2e95eab72ae8350ab720a2ebe source_ref=2ca0238ab756d0c60b52d70fdaccabde793f48a0 role=test -->
Verifies that `Config.from_dict` uses default values when initialized with empty dictionary.

- Checks version, scope patterns, triefacts root, model names, and cascade settings
- Uses assertion-based verification of expected default configuration values
<!-- trie:end -->
<!-- trie:section symbol=tests/test_config:test_resolver_defaults fingerprint=4ae5ba89041145ad9bb8a42db5266fc9bd436457b3b0c177fa604868634daaab body_fp=f933b74ab85562823d6a59eab1f17d2c5c901326372b739a34fac3a17714af36 source_ref=3d37fa183314a6c47e966911cbaba79329583648 role=test -->
Assert that `Config.from_dict({})` produces resolver defaults: `enabled=True`, `disabled_languages=[]`, `servers={}`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_config:test_resolver_overrides fingerprint=712f4d1baaea759d15cb55edaf443cdc0d8266b6b06c4dec4084dfe79018a6e4 body_fp=f332801b12c0dbe3facee7cca21d17f1b867430a66ca993e8a6ed8cd011176cc source_ref=3d37fa183314a6c47e966911cbaba79329583648 role=test -->
Verify that resolver config fields (`enabled`, `disabled_languages`, `servers`) correctly override defaults when supplied via `Config.from_dict`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_config:test_resolver_config_gates_specs fingerprint=82d7995478c0bef11b738d21cb9b549ada75e9de2c50839ec6764dfe61686537 body_fp=8c7a47c3a182adaa6bdbd539378f298a5cef53688889fe3146ddbee14d0647c9 source_ref=3d37fa183314a6c47e966911cbaba79329583648 role=test -->
Verify that `specs.configure_resolver` gates language spec resolution, returning `None` for disabled or globally-disabled languages.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_config:test_overrides_merge_per_section fingerprint=5baed518a1d25e4a0508e76368d6bdcfd516757fecf5e7e4f4e79b4a9731b35e body_fp=cba865c6b785bc6d77a4e69e8ca96aa5868e8ddfc45a5afac55fb6a7dcc6425f source_ref=ce0170296e1b69f535154cc3d8fa01546c83fc5e role=test-infrastructure -->
Tests that Config.from_dict merges overrides per section while preserving defaults for untouched sections and keys.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_config:test_load_roundtrips_default_template fingerprint=333b6309d910ec325894a15776b361f1510c756466a548083fb8d124b2abf6a5 body_fp=f1c706a20bc4863d933f2f914c487448722750b9d2a3c369ab4724891c45e9bf source_ref=2ca0238ab756d0c60b52d70fdaccabde793f48a0 role=test -->
Verifies that Config.load can parse the default TOML configuration template and produces expected defaults.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_config:test_find_and_load_walks_up fingerprint=c2e6b43592156a913d5cfee00fbb8028609cdf2318d3de8a975915503cbec7dd body_fp=28882492ca4ad2950d26e82976d8d6014e40aa4ca48c771478d82de341ebf79b source_ref=fc39661b30c3a7ba13e052fbab6504196bb5bc1d role=test -->
Verifies Config.find_and_load() walks up from deeply nested directories to find configuration files.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_config:test_find_and_load_raises_when_missing fingerprint=34e4b7c5c6730ec2a6f2bf88e37ab6412ebad59f63491fcba83fb3be61de3093 body_fp=c2ab318e15cc867027117c569ed94aa73cdf3bd4764dcd944fa525c4e3140e6e source_ref=ce0170296e1b69f535154cc3d8fa01546c83fc5e role=test-infrastructure -->
Verifies Config.find_and_load raises ConfigNotFoundError when no configuration file is found in the directory tree.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_config:test_unknown_top_level_keys_are_ignored fingerprint=406e28384661339d41a663749e228fb9f5c3b5f901bf1174a1faf4bec5565895 body_fp=79d54563e7abd9e41e699b15b2e2e8ef784f60bc49410aec7f8ad077eebdcb54 source_ref=ce0170296e1b69f535154cc3d8fa01546c83fc5e role=test-infrastructure -->
Verifies Config.from_dict ignores unknown top-level sections for forward compatibility.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_config:test_unknown_keys_within_known_section_raise fingerprint=8e6e05e7e17ed2a96bd9abfe62dd6db3ef656dae01c649e891afb67f5f7de532 body_fp=d44f3b897c175b7366a1c1152f5b05ee8341da306ddac21dec8cdfb489a93a07 source_ref=ce0170296e1b69f535154cc3d8fa01546c83fc5e role=config-management -->
Verifies that Config.from_dict raises TypeError when given unknown keys within known configuration sections.
<!-- trie:end -->