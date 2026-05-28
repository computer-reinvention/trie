---
trie_version: 0.1.5
source: tests/test_config.py
file_fingerprint: c659474b9bf3edbb4f7ce11684a1910ce0fdcfeeb1e98b156f427f0788592352
last_synced_at: '2026-05-28T01:36:14Z'
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
<!-- trie:section symbol=tests/test_config:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=3ad55626b589bf070f713750baf35d95aef21bb49187d9a83341558d471bf58d source_ref=3e8bc28037d2b7d09075a457bbb71839f3f57bbf -->
## `tests/test_config`

Test suite for `Config` loading, merging, file discovery, and error handling.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_config:test_defaults_when_empty_dict fingerprint=7079d25ce5bd1212e3cd6b3e6e1f639440d455340183fa74f6757abae21a6ca7 body_fp=d99384c3816ff454240dcb0bed57aaac043a299ad76cdbdb1414949667eede4d source_ref=ce0170296e1b69f535154cc3d8fa01546c83fc5e -->
## `test_defaults_when_empty_dict()`

Verify that `Config.from_dict({})` populates all sections with correct default values.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_config:test_overrides_merge_per_section fingerprint=5baed518a1d25e4a0508e76368d6bdcfd516757fecf5e7e4f4e79b4a9731b35e body_fp=2912a1c341cf5fc13d80caacdfc2e13af588659a9630bc88164f8c2f89fb01c0 source_ref=3e8bc28037d2b7d09075a457bbb71839f3f57bbf -->
## `test_overrides_merge_per_section()`

Verify that `Config.from_dict` merges overrides per-section while preserving untouched keys and sections at their defaults.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_config:test_load_roundtrips_default_template fingerprint=7976917fe1d121c59caeee292e0ba1615d530e55cb060757bdf0763e61f59674 body_fp=ca7c2ca27435aff82b631a63bf59b5e3e29ca8787036e4110bf3c97d585845a5 source_ref=ce0170296e1b69f535154cc3d8fa01546c83fc5e -->
## `test_load_roundtrips_default_template(tmp_path: Path)`

Verify that writing `DEFAULT_CONFIG_TOML` to disk and loading it via `Config.load` preserves default field values.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_config:test_find_and_load_walks_up fingerprint=c2e6b43592156a913d5cfee00fbb8028609cdf2318d3de8a975915503cbec7dd body_fp=da9143f8e535095870a6cec696563625f0a673b4e0ac382b59c87b0e173b7528 source_ref=3e8bc28037d2b7d09075a457bbb71839f3f57bbf -->
## `test_find_and_load_walks_up(tmp_path: Path)`

Verify that `Config.find_and_load` walks up ancestor directories to locate `trie.toml` and returns the correct root.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_config:test_find_and_load_raises_when_missing fingerprint=34e4b7c5c6730ec2a6f2bf88e37ab6412ebad59f63491fcba83fb3be61de3093 body_fp=d5a47e99778c1c7f214a77c2b9a61dca86e5e7a58adb32ef06b2b2ea76795e15 source_ref=3e8bc28037d2b7d09075a457bbb71839f3f57bbf -->
## `test_find_and_load_raises_when_missing(tmp_path: Path)`

Assert that `Config.find_and_load` raises `ConfigNotFoundError` when no `trie.toml` exists in the directory tree.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_config:test_unknown_top_level_keys_are_ignored fingerprint=406e28384661339d41a663749e228fb9f5c3b5f901bf1174a1faf4bec5565895 body_fp=a8a753080a64502c34df7a0be95b9a1870d7fc5476e140fb9e119fb75896be00 source_ref=3e8bc28037d2b7d09075a457bbb71839f3f57bbf -->
## `test_unknown_top_level_keys_are_ignored()`

Verify that `Config.from_dict` silently ignores unrecognised top-level TOML sections for forward compatibility.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_config:test_unknown_keys_within_known_section_raise fingerprint=8e6e05e7e17ed2a96bd9abfe62dd6db3ef656dae01c649e891afb67f5f7de532 body_fp=4277aabfe33740002105bf7b10be745914e979d75f97633098ce3172c350bcfb source_ref=3e8bc28037d2b7d09075a457bbb71839f3f57bbf -->
## `test_unknown_keys_within_known_section_raise()`

Assert that `Config.from_dict` raises `TypeError` when a known section contains an unrecognised key.
<!-- trie:end -->