---
trie_version: 0.1.5
source: tests/test_metadata_refresh.py
file_fingerprint: 2bea858f50a5d11432e54ce0156a70e43c81025119d87ce6a8965da7a4561aa6
last_synced_at: '2026-05-28T14:39:34Z'
description: Metadata-only triefact refresh.
defines:
- kind: module
  qualified_name: tests/test_metadata_refresh:__module__
  lines: 1-321
- kind: function
  qualified_name: tests/test_metadata_refresh:project
  lines: 39-59
- kind: function
  qualified_name: tests/test_metadata_refresh:_sync_both
  lines: 62-79
- kind: function
  qualified_name: tests/test_metadata_refresh:_read_yaml_front
  lines: 82-87
- kind: function
  qualified_name: tests/test_metadata_refresh:_section_bodies
  lines: 90-104
- kind: function
  qualified_name: tests/test_metadata_refresh:test_refresh_does_not_call_the_llm
  lines: 112-128
- kind: function
  qualified_name: tests/test_metadata_refresh:test_refresh_preserves_section_bodies_byte_for_byte
  lines: 131-152
- kind: function
  qualified_name: tests/test_metadata_refresh:test_refresh_preserves_last_synced_at
  lines: 155-175
- kind: function
  qualified_name: tests/test_metadata_refresh:test_refresh_picks_up_new_edges_in_front_matter
  lines: 178-207
- kind: function
  qualified_name: tests/test_metadata_refresh:test_refresh_is_idempotent
  lines: 210-225
- kind: function
  qualified_name: tests/test_metadata_refresh:test_refresh_skips_missing_triefact
  lines: 228-238
- kind: function
  qualified_name: tests/test_metadata_refresh:test_verify_passes_after_refresh
  lines: 241-263
- kind: function
  qualified_name: tests/test_metadata_refresh:test_cli_sync_metadata_only_mutex_with_other_flags
  lines: 271-294
- kind: function
  qualified_name: tests/test_metadata_refresh:test_cli_sync_metadata_only_runs
  lines: 297-320
incoming_refs: 0
outgoing_refs: 22
---
<!-- trie:section symbol=tests/test_metadata_refresh:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=51a9f7e168f219e58d85db68c446a95884ec617e03aec64c9baa5ac2120eeb41 source_ref=a2c02bf233ff62220d2358d894f11d3f63345166 -->
## `tests/test_metadata_refresh`

Test suite for the metadata-only triefact refresh contract.

- `refresh_triefact_metadata`: must not call the LLM, preserve section bodies, and preserve `last_synced_at`.
- Covers idempotency, new-edge detection, missing-triefact skipping, `trie verify` compatibility, and CLI flag mutex enforcement.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_metadata_refresh:project fingerprint=65fd0b8d1c2fe0511dfb8e02ca8712e1da978440f17e1e72a14ebc38292a6981 body_fp=23eb3fc15d9e82ec4f34f56682d8c6c4ab0bdda8194e24cee7c8a411815664ab source_ref=a2c02bf233ff62220d2358d894f11d3f63345166 -->
## `project(tmp_path: Path) -> Path`

Pytest fixture providing a two-module project where `beta.py` imports from `alpha.py`, enabling ref-count assertions.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_metadata_refresh:_sync_both fingerprint=34f3862f727710588e479ae81af4b72c3d861240fedba9be071fe5ad9af64a17 body_fp=869688e7ac1bf7d689aac031c27e115eb5e57113fff77ec264f2b98e24287b71 source_ref=65204173c592bc34e87ebc59176aeb0c67ef4747 -->
## `_sync_both(project: Path) -> Store`

Scan and cold-sync `alpha.py` and `beta.py` into a new `Store`, returning it open for the caller to close.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_metadata_refresh:_read_yaml_front fingerprint=7e5679b0a04dfddc9fdfb4811524e98777352d0e45971091c9817ede8816a4a2 body_fp=a937a8f161dba5ae416687786451889c58c2f81237c6f1eb5db6549cb125a039 source_ref=a2c02bf233ff62220d2358d894f11d3f63345166 -->
## `_read_yaml_front(triefact_path: Path) -> dict`

Parse and return the YAML front matter from a triefact file as a dictionary.

- Asserts front matter is present; raises `AssertionError` if absent.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_metadata_refresh:_section_bodies fingerprint=a78be54ef29af611dbd8e6b081cebdb4f8bf91b70f60e801bb64fc6705ca735a body_fp=7cf7f6ec8349dcc52f85c4dc9cda354a4c70396f648bbc11f21bbfbd22d97f00 source_ref=a2c02bf233ff62220d2358d894f11d3f63345166 -->
## `_section_bodies(triefact_path: Path) -> dict[str, str]`

Extract a `{qname: body}` map of all trie section bodies from a triefact file.

- **returns**: keyed by the `symbol=` attribute value from each `<!-- trie:section -->` sentinel.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_metadata_refresh:test_refresh_does_not_call_the_llm fingerprint=10efbe7f965fac4bfe13d5fb4ca4d3823e9bbe88e28e269add9756d9241929f6 body_fp=a6b04cf93733b907352613d5f7188a2bc333ee95513969aac4eb1ace8cef6fec source_ref=a2c02bf233ff62220d2358d894f11d3f63345166 -->
## `test_refresh_does_not_call_the_llm(project: Path)`

Assert that `refresh_triefact_metadata` accepts no LLM client argument and returns a `MetadataRefreshResult` without invoking any generation.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_metadata_refresh:test_refresh_preserves_section_bodies_byte_for_byte fingerprint=31af1871d315749a9c025d6b02b4438439f67bf623d93180d8dd9362c6159957 body_fp=c57ddcb05d38b1757ec4ca1b1911e3a03792c94176fbfe9aeea7bc7da06c0e18 source_ref=a2c02bf233ff62220d2358d894f11d3f63345166 -->
## `test_refresh_preserves_section_bodies_byte_for_byte(project: Path)`

Assert that `refresh_triefact_metadata` leaves section sentinel comments and body text byte-identical in `beta.md`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_metadata_refresh:test_refresh_preserves_last_synced_at fingerprint=347a26e83a5aa2b48ca7bf04dafc020f7cd666df80981ad495d005d3baaf8f53 body_fp=1ded8f5d38a1126056d3570465f7033aa75d738071917808aff22703f571119c source_ref=a2c02bf233ff62220d2358d894f11d3f63345166 -->
## `test_refresh_preserves_last_synced_at(project: Path)`

Assert that `refresh_triefact_metadata` leaves `last_synced_at` in the YAML front matter unchanged.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_metadata_refresh:test_refresh_picks_up_new_edges_in_front_matter fingerprint=6263b0a5f31e8703e1010346c981e743ea8bfd5e1648e1ff930951164076bc6c body_fp=d48671d5e641018977d118a7a116ff63017e9b8cba10ce9acbfc4d4cfb2ada30 source_ref=a2c02bf233ff62220d2358d894f11d3f63345166 -->
## `test_refresh_picks_up_new_edges_in_front_matter(project: Path)`

Assert that `refresh_triefact_metadata` updates `incoming_refs` in front matter when the graph gains a new edge post-initial-sync.

- Adds `gamma.py` referencing `alpha_fn`, rescans, then refreshes `alpha.py` metadata.
- Asserts `incoming_refs` increments by exactly 1.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_metadata_refresh:test_refresh_is_idempotent fingerprint=0c9ddae21b38445f7612817c1a778908943e8e78e7f37def01bdefe1c08774de body_fp=a87d9aa327334ca47e7ebb4e3ecacf49721b3337d699c7519f9ffc761afbd51f source_ref=a2c02bf233ff62220d2358d894f11d3f63345166 -->
## `test_refresh_is_idempotent(project: Path)`

Assert that a second consecutive `refresh_triefact_metadata` call on the same file returns `changed=False`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_metadata_refresh:test_refresh_skips_missing_triefact fingerprint=f78515fc126a5e94dc695fb2c41fc0a47424413eb197cf2c80054305065d3589 body_fp=6a3716e83e6aedac5804ccc23459ff4810bee46cbf2294a927aadba57da6d672 source_ref=a2c02bf233ff62220d2358d894f11d3f63345166 -->
## `test_refresh_skips_missing_triefact(project: Path, tmp_path: Path)`

Assert that `refresh_triefact_metadata` returns `changed=False` for a source file with no existing triefact.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_metadata_refresh:test_verify_passes_after_refresh fingerprint=4eaa18dfe98b605a6c3f831c8389b56cb62a3a1a6c9516dcd97cb212e9e1049d body_fp=1b165fcb6bf3ff6aa2ef3715c1a328c63419ba54ae7a61219fdbedd163b32c88 source_ref=a2c02bf233ff62220d2358d894f11d3f63345166 -->
## `test_verify_passes_after_refresh(project: Path)`

Assert that `check_project` reports clean before and after `refresh_triefact_metadata` runs on all synced modules.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_metadata_refresh:test_cli_sync_metadata_only_mutex_with_other_flags fingerprint=bcc16ea751d379805d3dcab93e5c08c3d015fa75936a750c7d0720dad41bc5e8 body_fp=c9a975a872c3472d0c40b8822c3f64c7b0f8f77a9a086e8cd94f874c5ea5f26f source_ref=a2c02bf233ff62220d2358d894f11d3f63345166 -->
## `test_cli_sync_metadata_only_mutex_with_other_flags(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `--metadata-only` combined with `--all`, `--dry-run`, `--budget`, `--limit`, or `--file` exits with code 1 and prints "cannot be combined".
<!-- trie:end -->
<!-- trie:section symbol=tests/test_metadata_refresh:test_cli_sync_metadata_only_runs fingerprint=638512cb71cdff8c21b134ba723f92f1951cce6873edf584fb30513f4b34677e body_fp=ba622a8997ea362254fb1d2fdb849bb7a3784178a4fba9391be2521ce6ba3e76 source_ref=a2c02bf233ff62220d2358d894f11d3f63345166 -->
## `test_cli_sync_metadata_only_runs(project: Path, monkeypatch: pytest.MonkeyPatch)`

Verify that `trie sync --metadata-only` exits cleanly and reports a refresh count without constructing an LLM client.

- `make_client` is patched to raise `AssertionError` if called, guarding against accidental LLM construction.
<!-- trie:end -->