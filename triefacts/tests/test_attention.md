---
trie_version: 0.1.5
source: tests/test_attention.py
file_fingerprint: e811343e585aec084946f8003593bfcc0e3adf88d06b53362f29fac21d284e60
last_synced_at: '2026-06-10T13:16:32Z'
description: Tests for AGM attention contracts, event store, sync-time fold, and typed
  edges.
defines:
- kind: module
  qualified_name: tests/test_attention:__module__
  lines: 1-268
- kind: function
  qualified_name: tests/test_attention:test_event_weights_canonical
  lines: 31-32
- kind: function
  qualified_name: tests/test_attention:test_classify_tool
  lines: 54-55
- kind: function
  qualified_name: tests/test_attention:test_classify_tool_strips_prefix
  lines: 58-59
- kind: function
  qualified_name: tests/test_attention:test_classify_synthetic
  lines: 62-65
- kind: function
  qualified_name: tests/test_attention:test_edge_weights_and_fallback
  lines: 68-73
- kind: function
  qualified_name: tests/test_attention:test_display_mass_log_compression
  lines: 76-81
- kind: function
  qualified_name: tests/test_attention:test_live_lambda_matches_halflife
  lines: 84-87
- kind: function
  qualified_name: tests/test_attention:test_synthetic_qname_roundtrip
  lines: 90-94
- kind: function
  qualified_name: tests/test_attention:test_attention_event_make_fills_weight
  lines: 97-100
- kind: function
  qualified_name: tests/test_attention:test_typed_edges
  lines: 106-126
- kind: function
  qualified_name: tests/test_attention:test_call_vs_reference_kind
  lines: 129-139
- kind: function
  qualified_name: tests/test_attention:test_store_record_and_read
  lines: 145-154
- kind: function
  qualified_name: tests/test_attention:test_store_coalesces_within_window
  lines: 157-166
- kind: function
  qualified_name: tests/test_attention:test_store_distinct_investigations
  lines: 169-180
- kind: function
  qualified_name: tests/test_attention:test_store_fold_watermark
  lines: 183-186
- kind: function
  qualified_name: tests/test_attention:test_store_missing_db_is_empty
  lines: 189-192
- kind: function
  qualified_name: tests/test_attention:test_hist_mass_parse_format
  lines: 198-202
- kind: function
  qualified_name: tests/test_attention:test_legacy_sentinel_no_hist_mass
  lines: 205-211
- kind: function
  qualified_name: tests/test_attention:test_hist_mass_roundtrip_preserves_role
  lines: 214-223
- kind: function
  qualified_name: tests/test_attention:test_upsert_preserves_existing_hist_mass
  lines: 226-233
- kind: function
  qualified_name: tests/test_attention:test_fold_accrues_recurrence
  lines: 239-256
- kind: function
  qualified_name: tests/test_attention:test_fold_decays_existing
  lines: 259-267
incoming_refs: 0
outgoing_refs: 35
---
<!-- trie:section symbol=tests/test_attention:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=1ce7c0cc2f345a4ac8197e944788cbf867a0b9ebbbaf9f6f74cf77cb35835073 source_ref=a025f7fa9e7f1375a8533e7e840733e4eee47256 role=test -->
Tests for AGM attention contracts, event store, sync-time fold, and typed edges functionality.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_attention:test_event_weights_canonical fingerprint=06a4885e48741bb47b5fd1bcf15de8d2a3d31b2bc03c586c54a8e1df3e79322c body_fp=e68941419c638c3b33b52d01c7f5e461821304c579bbbca696ddd05242b9308c source_ref=a025f7fa9e7f1375a8533e7e840733e4eee47256 role=test -->
Verifies EVENT_WEIGHTS dictionary contains canonical weight values for attention event types.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_attention:test_classify_tool fingerprint=c980b2c601066bca3123a89e010d362d12f5aba8c9a1640f34e1c6df7428060b body_fp=fdbf70ed480450d9fae99c3999868a76a9486c9e9f76aa5e3b87e596409d7c6a source_ref=a025f7fa9e7f1375a8533e7e840733e4eee47256 role=test -->
Tests that `classify_tool` correctly maps tool names to attention event types.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_attention:test_classify_tool_strips_prefix fingerprint=7b944b52efe4521b450c45d4b11698a12cfa859f1f01e0a8a840cfab101e8825 body_fp=9b05c3684395fd25704dfbd15ca89d96dc862e0c761cc591b5188e37fd1313a7 source_ref=a025f7fa9e7f1375a8533e7e840733e4eee47256 role=test -->
Tests that classify_tool strips "trie_" prefix from tool names before classification.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_attention:test_classify_synthetic fingerprint=f6b12dc58e7b8c946f18c14b0e6da0360b0bf6e542ae08a421575a6dd5c6ccfa body_fp=533b4284dd3881d64ee7f4b89436f4579002fbdde4780a9adfe5c9fe3336e4a7 source_ref=a025f7fa9e7f1375a8533e7e840733e4eee47256 role=test -->
Tests that `classify_synthetic` correctly categorizes tool names as synthetic entities or returns None.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_attention:test_edge_weights_and_fallback fingerprint=9472f7658211f4796d1df6c4474a354055638ed046b940e6543faf65a590680d body_fp=3ef41aa36903066660719c8716fab279350fc25599fa68968930037e018b4dce source_ref=a025f7fa9e7f1375a8533e7e840733e4eee47256 role=test -->
Verifies edge weight values for known edge types and fallback behavior for unknown types.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_attention:test_display_mass_log_compression fingerprint=fbf2a984383820148e7fc12c37ff1599de3a0fb112c264f0f016825570c29da7 body_fp=724c67ecd0ed04fd5e47611ca9b8ccc016fb8b4a52f2d1307273b0c5e6fac400 source_ref=a025f7fa9e7f1375a8533e7e840733e4eee47256 role=test -->
Verifies display_mass function clamps negative values to zero and applies logarithmic compression to positive values.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_attention:test_live_lambda_matches_halflife fingerprint=01a83824a03ec511399a17839cd9141e753aad155a08e4934cfbe2f7879a7a1a body_fp=177e4c95c98f41322c5234403cacb32fcdbcef5383fc85eedb510a58e5746e45 source_ref=a025f7fa9e7f1375a8533e7e840733e4eee47256 role=test -->
Verifies that live_lambda produces a decay constant matching the expected 30-day half-life for grep events.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_attention:test_synthetic_qname_roundtrip fingerprint=f2b927c1074eea26533cc55257006051af50e2e155f074d20c33f26d69fdef8c body_fp=e9cf32a4f88094f5e0591d7600a48a4e7bf62dd56df0711a4b850f3acac989da source_ref=a025f7fa9e7f1375a8533e7e840733e4eee47256 role=test -->
Tests synthetic qualified name creation and detection functions for bidirectional validation.

- Verifies `synthetic_qname("Bash")` produces `"agm:synthetic/Bash"`
- Confirms `is_synthetic_qname` correctly identifies synthetic vs regular qualified names
<!-- trie:end -->
<!-- trie:section symbol=tests/test_attention:test_attention_event_make_fills_weight fingerprint=6d99e5b49a8c1a86ecad3139100bc784881c6a83c85e90ba505bc9fa10ac6b04 body_fp=73ee102c3cc7a2f90a118136ac8d47e26226354629dc36423373c9ad5365c282 source_ref=a025f7fa9e7f1375a8533e7e840733e4eee47256 role=test -->
Verifies that AttentionEvent.make() automatically fills the weight field based on event type.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_attention:test_typed_edges fingerprint=5a89da67b8b1b760bb6051ce56c88a4d3b81f6f817b5fbd686d627ee0c163b1d body_fp=de486e41a49985cf1279988d23e440d0256bd23f00ed8954c2be805c1c1b3802 source_ref=a025f7fa9e7f1375a8533e7e840733e4eee47256 role=test -->
Tests that extract_file_data correctly classifies reference kinds (inherits, implements, contains, calls) from Python source.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_attention:test_call_vs_reference_kind fingerprint=ff55dff0b657866a5d712faa687d608a36cd4bdf00a1fdb2ce90667b87cdbda5 body_fp=f95803a57c82d56c9f544f26bb1f559dbc716020a1b07fa775f43f3257ee1a56 source_ref=a025f7fa9e7f1375a8533e7e840733e4eee47256 role=test -->
Verifies that function invocations are classified as "calls" while name assignments are classified as "references".
<!-- trie:end -->
<!-- trie:section symbol=tests/test_attention:test_store_record_and_read fingerprint=3ac04af0c375fe4eaa27936e3c0bc401a8b027af544986be6c5681d57daae128 body_fp=083394164f26bbf813436498d3f55ea8bc65c41c43e4c3b8be6498a224b4db0f source_ref=a025f7fa9e7f1375a8533e7e840733e4eee47256 role=test -->
Tests that attention store can record events and read them back correctly.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_attention:test_store_coalesces_within_window fingerprint=d5e0130caa686bb34a3a7e0749ddb954396742bcd4d0ff22cc1417a169635054 body_fp=d0c3b9006e44c7ebd40d2a93d581dbdb4a0a8e82e254f900f26022a939b317c5 source_ref=a025f7fa9e7f1375a8533e7e840733e4eee47256 role=test -->
Tests that attention store coalesces duplicate events from the same investigation within a time window.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_attention:test_store_distinct_investigations fingerprint=6953d7d4cb6d918ba47fdbc66e0bde707929e768b26b59bbede9d23504052745 body_fp=59a36422b39021679a739cec03371ae4e21162e409afe9088113314c8f392fad source_ref=a025f7fa9e7f1375a8533e7e840733e4eee47256 role=test -->
Tests that the attention store correctly tracks distinct investigation IDs that touch symbols and filters by timestamp.

- Records events for multiple investigations at different timestamps
- Verifies all investigations are returned when no time filter is applied
- Verifies only investigations after a given timestamp are returned when filtered
<!-- trie:end -->
<!-- trie:section symbol=tests/test_attention:test_store_fold_watermark fingerprint=d5e26c27e91f8cf8fbafa74c368e47f0a341ad093c0882ca2508361660e5f193 body_fp=33b58c60514c69eca9d8c6f67b6b0de8762c43e50026a28557c58300cf2732a2 source_ref=a025f7fa9e7f1375a8533e7e840733e4eee47256 role=test -->
Verifies attention store watermark functionality for tracking last fold timestamp.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_attention:test_store_missing_db_is_empty fingerprint=dbb9b2d37e6f39b500e3068451dc766da766e0ee55cfea3d7d1e2224d0b429e4 body_fp=6b5d344a5c8f0c73b3763d5fe1f2507e8b545b236461af305475840e63e771da source_ref=a025f7fa9e7f1375a8533e7e840733e4eee47256 role=test -->
Verifies that attention store operations return empty results when database file doesn't exist.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_attention:test_hist_mass_parse_format fingerprint=ee8bb5d63096b7d5f1b5aa7d96c24809c09d5eb91aeddb4d36b912530905ccca body_fp=28bcfb9de41cda87c2546fb48b02ea9e415d3acf3e89e0efdd5e13585156a38e source_ref=a025f7fa9e7f1375a8533e7e840733e4eee47256 role=test -->
Tests round-trip parsing and formatting of historical mass values in "value@timestamp" format.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_attention:test_legacy_sentinel_no_hist_mass fingerprint=ed8f9b8b5019dfb4e5694da0c51cdcddbae743bd59ae14e9593023d91c4d16f0 body_fp=b8a43323a39c07031a5be48fb3bfb67db17c2bdce1246202cf5bbe1569bac2c4 source_ref=a025f7fa9e7f1375a8533e7e840733e4eee47256 role=test -->
Tests that legacy triefact sections without hist_mass attributes default to zero historical mass and preserve clean formatting.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_attention:test_hist_mass_roundtrip_preserves_role fingerprint=5181c15645d798d365a8c50eef70819b59f22e4e754232833f8c1d1eccd5734c body_fp=d85da3a0b831beeac9bf86dca49890bac86d74a7a90785404aa233dc67d479ba source_ref=a025f7fa9e7f1375a8533e7e840733e4eee47256 role=test -->
Tests that setting historical mass on a TriefactFile section preserves the existing role attribute through serialization roundtrip.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_attention:test_upsert_preserves_existing_hist_mass fingerprint=f38e3cb0637c2d25e2a91d27b4090c0d16cb903050fa31f585e4351db7446eb1 body_fp=3760391dffd6f852233a8778d820b6627d575d2965e5cf7b0e224c2dd9cd8516 source_ref=a025f7fa9e7f1375a8533e7e840733e4eee47256 role=test -->
Verifies that TriefactFile.upsert_section preserves existing historical mass when updating section content.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_attention:test_fold_accrues_recurrence fingerprint=e8a9f67b0142be6c7445af039cebf8f2848f9fc96e760a15747c75ae3f4f7ed7 body_fp=9b6316a193832c55be21d2b9e89954e2204d3db432eaf87e61a26dc7aecd3fce source_ref=a025f7fa9e7f1375a8533e7e840733e4eee47256 role=test -->
Tests that fold_historical_mass accumulates investigation recurrence correctly across multiple events and symbols.

- Records events from two investigations touching "a:b" and one touching "c:d"
- Verifies historical mass reflects distinct investigation count (2.0 for "a:b", 1.0 for "c:d")
<!-- trie:end -->
<!-- trie:section symbol=tests/test_attention:test_fold_decays_existing fingerprint=d8047d48f80084d4462f4df9cff65af4f5d44e2e18770b80f14592569f1fb103 body_fp=3416a0d1adc01e1112a97d2db91ce9409747cac04bdea2260955ade6bb5c2814 source_ref=a025f7fa9e7f1375a8533e7e840733e4eee47256 role=test -->
Tests that historical attention mass decays exponentially over time when no new events occur.
<!-- trie:end -->