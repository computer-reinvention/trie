---
trie_version: 0.1.5
source: tests/test_config.py
file_fingerprint: c659474b9bf3edbb4f7ce11684a1910ce0fdcfeeb1e98b156f427f0788592352
last_synced_at: '2026-06-06T14:03:39Z'
defines:
- kind: module
  qualified_name: tests/test_config:__module__
  lines: 1-69
- kind: function
  qualified_name: tests/test_config:test_defaults_when_empty_dict
  lines: 10-17
- kind: function
  qualified_name: tests/test_config:test_overrides_merge_per_section
  lines: 20-34
- kind: function
  qualified_name: tests/test_config:test_load_roundtrips_default_template
  lines: 37-42
- kind: function
  qualified_name: tests/test_config:test_find_and_load_walks_up
  lines: 45-51
- kind: function
  qualified_name: tests/test_config:test_find_and_load_raises_when_missing
  lines: 54-56
- kind: function
  qualified_name: tests/test_config:test_unknown_top_level_keys_are_ignored
  lines: 59-62
- kind: function
  qualified_name: tests/test_config:test_unknown_keys_within_known_section_raise
  lines: 65-68
incoming_refs: 0
outgoing_refs: 10
---
<!-- trie:section symbol=tests/test_config:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=ce2218b9062b82cfac346bbfa304ec5a3f34f1ccbc7ce075aeada47e602a06b4 source_ref=ce0170296e1b69f535154cc3d8fa01546c83fc5e role=test-infrastructure -->
Tests configuration loading, validation, and file discovery behavior for the Config class.

- `test_defaults_when_empty_dict`: verifies default values are applied when no config is provided
- `test_overrides_merge_per_section`: confirms partial overrides preserve defaults in untouched sections
- `test_load_roundtrips_default_template`: validates loading from TOML file works correctly
- `test_find_and_load_walks_up`: tests directory traversal to locate config files
- `test_find_and_load_raises_when_missing`: ensures ConfigNotFoundError is raised when no config found
- `test_unknown_top_level_keys_are_ignored`: verifies forward compatibility with unknown sections
- `test_unknown_keys_within_known_section_raise`: confirms typos in known sections fail loudly
<!-- trie:end -->
<!-- trie:section symbol=tests/test_config:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=4c19dcc1dd79e84522cba2e81e74fb8cbde04913c1a842843b260f43a9ca9b73 source_ref=ce0170296e1b69f535154cc3d8fa01546c83fc5e -->
Tests configuration loading, merging, and validation for the Config class.

- `test_defaults_when_empty_dict`: Verifies default values are applied when no config is provided
- `test_overrides_merge_per_section`: Tests section-level merging preserves defaults in untouched sections
- `test_load_roundtrips_default_template`: Validates loading from TOML file works correctly
- `test_find_and_load_walks_up`: Tests filesystem traversal to locate config files
- `test_find_and_load_raises_when_missing`: Ensures ConfigNotFoundError is raised when no config found
- `test_unknown_top_level_keys_are_ignored`: Verifies forward compatibility with unknown sections
- `test_unknown_keys_within_known_section_raise`: Ensures typos in known sections fail loudly
<!-- trie:end -->
<!-- trie:section symbol=tests/test_config:test_defaults_when_empty_dict fingerprint=7079d25ce5bd1212e3cd6b3e6e1f639440d455340183fa74f6757abae21a6ca7 body_fp=9e79027f70a6724477e51a59214b64567283ead97f9c794f56c1275df2fb1f73 source_ref=ce0170296e1b69f535154cc3d8fa01546c83fc5e role=test-infrastructure -->
Verifies that Config.from_dict with empty dictionary returns default configuration values.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_config:test_defaults_when_empty_dict fingerprint=7079d25ce5bd1212e3cd6b3e6e1f639440d455340183fa74f6757abae21a6ca7 body_fp=8e23f2407170afea9f1b23b78a647d3fc882b9229c95d5c31f1a24ca7436043c source_ref=ce0170296e1b69f535154cc3d8fa01546c83fc5e -->
Verifies that Config.from_dict uses default values when initialized with empty dictionary.

- Checks version, scope patterns, triefacts root, model names, and cascade settings
- Uses assertion-based verification of expected default configuration values
<!-- trie:end -->
<!-- trie:section symbol=tests/test_config:test_overrides_merge_per_section fingerprint=5baed518a1d25e4a0508e76368d6bdcfd516757fecf5e7e4f4e79b4a9731b35e body_fp=78f9206b8adbf63e49c65b31763d1be6400288e03e820e84fc911fefa0b6bda0 source_ref=ce0170296e1b69f535154cc3d8fa01546c83fc5e role=test-infrastructure -->
Verifies that Config.from_dict merges overrides per section while preserving defaults for untouched sections and keys.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_config:test_overrides_merge_per_section fingerprint=5baed518a1d25e4a0508e76368d6bdcfd516757fecf5e7e4f4e79b4a9731b35e body_fp=cba865c6b785bc6d77a4e69e8ca96aa5868e8ddfc45a5afac55fb6a7dcc6425f source_ref=ce0170296e1b69f535154cc3d8fa01546c83fc5e -->
Tests that Config.from_dict merges overrides per section while preserving defaults for untouched sections and keys.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_config:test_load_roundtrips_default_template fingerprint=7976917fe1d121c59caeee292e0ba1615d530e55cb060757bdf0763e61f59674 body_fp=95ba4faf9d6e56250ddf46c4ab09057b6ba6e7ee7e552d9ba582eecf035a4feb source_ref=ce0170296e1b69f535154cc3d8fa01546c83fc5e role=test -->
Verifies Config.load can parse and load the default TOML configuration template without data loss.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_config:test_load_roundtrips_default_template fingerprint=7976917fe1d121c59caeee292e0ba1615d530e55cb060757bdf0763e61f59674 body_fp=f1c706a20bc4863d933f2f914c487448722750b9d2a3c369ab4724891c45e9bf source_ref=ce0170296e1b69f535154cc3d8fa01546c83fc5e -->
Verifies that Config.load can parse the default TOML configuration template and produces expected defaults.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_config:test_find_and_load_walks_up fingerprint=c2e6b43592156a913d5cfee00fbb8028609cdf2318d3de8a975915503cbec7dd body_fp=0008a8215c72c2d96091d5d7c2d518b1c5befddf5b38739f4c0462530f3c7a10 source_ref=ce0170296e1b69f535154cc3d8fa01546c83fc5e role=test -->
Verifies that Config.find_and_load searches upward through parent directories to locate trie.toml.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_config:test_find_and_load_walks_up fingerprint=c2e6b43592156a913d5cfee00fbb8028609cdf2318d3de8a975915503cbec7dd body_fp=28882492ca4ad2950d26e82976d8d6014e40aa4ca48c771478d82de341ebf79b source_ref=ce0170296e1b69f535154cc3d8fa01546c83fc5e -->
Verifies Config.find_and_load() walks up from deeply nested directories to find configuration files.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_config:test_find_and_load_raises_when_missing fingerprint=34e4b7c5c6730ec2a6f2bf88e37ab6412ebad59f63491fcba83fb3be61de3093 body_fp=fb3459bf966483dfbca8304f93fb3b504f7f4feaac3a2c943b93ab04f1e50083 source_ref=ce0170296e1b69f535154cc3d8fa01546c83fc5e role=test-infrastructure -->
Verifies that Config.find_and_load raises ConfigNotFoundError when no config file exists in the directory tree.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_config:test_find_and_load_raises_when_missing fingerprint=34e4b7c5c6730ec2a6f2bf88e37ab6412ebad59f63491fcba83fb3be61de3093 body_fp=c2ab318e15cc867027117c569ed94aa73cdf3bd4764dcd944fa525c4e3140e6e source_ref=ce0170296e1b69f535154cc3d8fa01546c83fc5e -->
Verifies Config.find_and_load raises ConfigNotFoundError when no configuration file is found in the directory tree.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_config:test_unknown_top_level_keys_are_ignored fingerprint=406e28384661339d41a663749e228fb9f5c3b5f901bf1174a1faf4bec5565895 body_fp=9f54abbdedd1f06e6441b6253068fda34ecca6652c6ab54fcb7b4312fa1690d3 source_ref=ce0170296e1b69f535154cc3d8fa01546c83fc5e role=test-infrastructure -->
Verifies that Config.from_dict ignores unknown top-level configuration sections for forward compatibility.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_config:test_unknown_top_level_keys_are_ignored fingerprint=406e28384661339d41a663749e228fb9f5c3b5f901bf1174a1faf4bec5565895 body_fp=79d54563e7abd9e41e699b15b2e2e8ef784f60bc49410aec7f8ad077eebdcb54 source_ref=ce0170296e1b69f535154cc3d8fa01546c83fc5e -->
Verifies Config.from_dict ignores unknown top-level sections for forward compatibility.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_config:test_unknown_keys_within_known_section_raise fingerprint=8e6e05e7e17ed2a96bd9abfe62dd6db3ef656dae01c649e891afb67f5f7de532 body_fp=2094ab72dfbe7c619adb7d9abac9bc2cb0258608302729cb2c1a048e26c6c408 source_ref=ce0170296e1b69f535154cc3d8fa01546c83fc5e role=test-infrastructure -->
Verifies that Config.from_dict raises TypeError when given unknown keys within a recognized configuration section.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_config:test_unknown_keys_within_known_section_raise fingerprint=8e6e05e7e17ed2a96bd9abfe62dd6db3ef656dae01c649e891afb67f5f7de532 body_fp=d44f3b897c175b7366a1c1152f5b05ee8341da306ddac21dec8cdfb489a93a07 source_ref=ce0170296e1b69f535154cc3d8fa01546c83fc5e -->
Verifies that Config.from_dict raises TypeError when given unknown keys within known configuration sections.
<!-- trie:end -->