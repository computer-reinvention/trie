---
trie_version: 0.1.2
source: tests/test_config.py
file_fingerprint: ab2f4ec56dd812bf269b73522f1b37903706c25cce64bacbd8c7216033936e80
last_synced_at: '2026-05-19T15:24:04Z'
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
<!-- trie:section symbol=tests/test_config:test_defaults_when_empty_dict fingerprint=4074056b63de5e2a478fad3e1678a1bb80a87e6170ce3efaea444173402832a3 body_fp=4474e7d14a413f900957814b63b7780415b4cca31f59a9a5138852a3862a129c source_ref=3e8bc28037d2b7d09075a457bbb71839f3f57bbf -->
## `test_defaults_when_empty_dict()`

Assert that `Config.from_dict({})` produces correct default values for all config sections.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_config:test_overrides_merge_per_section fingerprint=5baed518a1d25e4a0508e76368d6bdcfd516757fecf5e7e4f4e79b4a9731b35e body_fp=f7e5837464b7b59443bb1ec4a6d6fb5013be3eaa79628745c5cf57a64bf376e7 source_ref=c2c8854a973a93468da00905a2b700073a289bf7 -->
## `test_overrides_merge_per_section()`

Verify that `Config.from_dict` merges overridden sections while preserving defaults in untouched sections and untouched keys within partially-overridden sections.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_config:test_load_roundtrips_default_template fingerprint=09862766e0214b1097784113034f5fe29f81c8142cff315d70c8c10ede315fc4 body_fp=4a6e6dcfeb3c7b5a056fc3c9b8013a3eefc59505a063ef97e16651da9652a1b5 source_ref=3e8bc28037d2b7d09075a457bbb71839f3f57bbf -->
## `test_load_roundtrips_default_template(tmp_path: Path)`

Verify that writing `DEFAULT_CONFIG_TOML` to disk and loading it produces correct default values.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_config:test_find_and_load_walks_up fingerprint=c2e6b43592156a913d5cfee00fbb8028609cdf2318d3de8a975915503cbec7dd body_fp=af35372cd67cb723c816484c19ef7b796be02e41f5e5659b5241fbd24da4aee3 source_ref=c2c8854a973a93468da00905a2b700073a289bf7 -->
## `test_find_and_load_walks_up(tmp_path: Path)`

Verify that `Config.find_and_load` walks up the directory tree to locate `trie.toml` from a deeply nested subdirectory.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_config:test_find_and_load_raises_when_missing fingerprint=34e4b7c5c6730ec2a6f2bf88e37ab6412ebad59f63491fcba83fb3be61de3093 body_fp=d5a47e99778c1c7f214a77c2b9a61dca86e5e7a58adb32ef06b2b2ea76795e15 source_ref=c2c8854a973a93468da00905a2b700073a289bf7 -->
## `test_find_and_load_raises_when_missing(tmp_path: Path)`

Assert that `Config.find_and_load` raises `ConfigNotFoundError` when no `trie.toml` exists in the directory tree.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_config:test_unknown_top_level_keys_are_ignored fingerprint=406e28384661339d41a663749e228fb9f5c3b5f901bf1174a1faf4bec5565895 body_fp=cb661b9fd6b77c914650ab8d33a8a37ed51df324549baa84afa3e91035936dcf source_ref=c2c8854a973a93468da00905a2b700073a289bf7 -->
## `test_unknown_top_level_keys_are_ignored()`

Assert that unrecognised top-level TOML sections are silently ignored for forward compatibility.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_config:test_unknown_keys_within_known_section_raise fingerprint=8e6e05e7e17ed2a96bd9abfe62dd6db3ef656dae01c649e891afb67f5f7de532 body_fp=76fa035eadbc52c639b29a969dffea1a7cab18853b77bc1c9a0815bd230e3d27 source_ref=c2c8854a973a93468da00905a2b700073a289bf7 -->
## `test_unknown_keys_within_known_section_raise()`

Assert that a typo within a known config section raises `TypeError`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_config:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=c5e3ffdd301fd79ee88df80de3137af460a32fda28e946740b06fcad751fdd48 source_ref=9ae3cf8607b8195c64ecbbda358ad1a86a84bbe2 -->
## `tests/test_config`

Test suite for `Config` loading, merging, file-discovery, and error-handling behaviour.
<!-- trie:end -->