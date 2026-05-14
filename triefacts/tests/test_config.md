---
trie_version: 0.1.0
source: tests/test_config.py
file_fingerprint: 2bcb482da874ab07a264159020e701c8eefa3f0880189896ae7f44f0d7bebad6
last_synced_at: '2026-05-14T17:30:17Z'
defines:
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
outgoing_refs: 8
---
<!-- trie:section symbol=tests/test_config:test_defaults_when_empty_dict fingerprint=e07d66512eca607a9bd0f0421b3df024c58df86472cc0f51eee7bfd3a637c455 body_fp=0652a4ee298ec26ec248ddb4ee385ac459f6f71c1f1a1e43baa8119e4a2f2c43 -->
## `test_defaults_when_empty_dict()`

Verify that `Config.from_dict({})` produces correct default values for all sections.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_config:test_overrides_merge_per_section fingerprint=5baed518a1d25e4a0508e76368d6bdcfd516757fecf5e7e4f4e79b4a9731b35e body_fp=732c30dba77047de3882eab6c7f079668e5a065d490f9877992c4f1093b52913 -->
## `test_overrides_merge_per_section()`

Verify that `Config.from_dict` merges per-section overrides while preserving defaults in untouched sections and keys.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_config:test_load_roundtrips_default_template fingerprint=a6001c4f5f8795eac0885db407a83136d060b5e94b6f03d3bb8d4945368db3e0 body_fp=b634bf2ac08f9209bb916f52a2eb4914c7c8f85602589e71115990969761f88f -->
## `test_load_roundtrips_default_template(tmp_path: Path)`

Verify that writing `DEFAULT_CONFIG_TOML` to disk and loading it via `Config.load` preserves default values.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_config:test_find_and_load_walks_up fingerprint=c2e6b43592156a913d5cfee00fbb8028609cdf2318d3de8a975915503cbec7dd body_fp=169e760c75e6b90f79a253903aa1c99c41745915a8b21eff37e0348325b11f15 -->
## `test_find_and_load_walks_up(tmp_path: Path)`

Verify that `Config.find_and_load` walks up ancestor directories to locate `trie.toml`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_config:test_find_and_load_raises_when_missing fingerprint=34e4b7c5c6730ec2a6f2bf88e37ab6412ebad59f63491fcba83fb3be61de3093 body_fp=43a4eb23d57d43aff2a04ddd39ede03bd6422c67bacb04cab952b60f91411862 -->
## `test_find_and_load_raises_when_missing(tmp_path: Path)`

Assert `Config.find_and_load` raises `ConfigNotFoundError` when no `trie.toml` exists in the directory tree.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_config:test_unknown_top_level_keys_are_ignored fingerprint=406e28384661339d41a663749e228fb9f5c3b5f901bf1174a1faf4bec5565895 body_fp=cb661b9fd6b77c914650ab8d33a8a37ed51df324549baa84afa3e91035936dcf -->
## `test_unknown_top_level_keys_are_ignored()`

Assert that unrecognised top-level TOML sections are silently ignored for forward compatibility.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_config:test_unknown_keys_within_known_section_raise fingerprint=8e6e05e7e17ed2a96bd9abfe62dd6db3ef656dae01c649e891afb67f5f7de532 body_fp=e9102f0a7815bcbec13aaaf0931d91d7a1e6c499dbd0c163fa8de967abe0a538 -->
## `test_unknown_keys_within_known_section_raise()`

Assert that a typo inside a known config section raises `TypeError`.
<!-- trie:end -->