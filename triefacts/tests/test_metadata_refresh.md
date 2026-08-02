---
trie_version: 0.3.0
source: tests/test_metadata_refresh.py
file_fingerprint: 2bea858f50a5d11432e54ce0156a70e43c81025119d87ce6a8965da7a4561aa6
last_synced_at: '2026-08-02T21:19:28Z'
description: Metadata-only triefact refresh.
defines:
- kind: module
  qualified_name: tests/test_metadata_refresh:__module__
  lines: 1-321
- kind: function
  qualified_name: tests/test_metadata_refresh:project
  lines: 39-59
  signature: 'def project(tmp_path: Path) -> Path'
- kind: function
  qualified_name: tests/test_metadata_refresh:_sync_both
  lines: 62-79
  signature: 'def _sync_both(project: Path) -> Store'
- kind: function
  qualified_name: tests/test_metadata_refresh:_read_yaml_front
  lines: 82-87
  signature: 'def _read_yaml_front(triefact_path: Path) -> dict'
- kind: function
  qualified_name: tests/test_metadata_refresh:_section_bodies
  lines: 90-104
  signature: 'def _section_bodies(triefact_path: Path) -> dict[str, str]'
- kind: function
  qualified_name: tests/test_metadata_refresh:test_refresh_does_not_call_the_llm
  lines: 112-128
  signature: 'def test_refresh_does_not_call_the_llm(project: Path)'
- kind: function
  qualified_name: tests/test_metadata_refresh:test_refresh_preserves_section_bodies_byte_for_byte
  lines: 131-152
  signature: 'def test_refresh_preserves_section_bodies_byte_for_byte(project: Path)'
- kind: function
  qualified_name: tests/test_metadata_refresh:test_refresh_preserves_last_synced_at
  lines: 155-175
  signature: 'def test_refresh_preserves_last_synced_at(project: Path)'
- kind: function
  qualified_name: tests/test_metadata_refresh:test_refresh_picks_up_new_edges_in_front_matter
  lines: 178-207
  signature: 'def test_refresh_picks_up_new_edges_in_front_matter(project: Path)'
- kind: function
  qualified_name: tests/test_metadata_refresh:test_refresh_is_idempotent
  lines: 210-225
  signature: 'def test_refresh_is_idempotent(project: Path)'
- kind: function
  qualified_name: tests/test_metadata_refresh:test_refresh_skips_missing_triefact
  lines: 228-238
  signature: 'def test_refresh_skips_missing_triefact(project: Path, tmp_path: Path)'
- kind: function
  qualified_name: tests/test_metadata_refresh:test_verify_passes_after_refresh
  lines: 241-263
  signature: 'def test_verify_passes_after_refresh(project: Path)'
- kind: function
  qualified_name: tests/test_metadata_refresh:test_cli_sync_metadata_only_mutex_with_other_flags
  lines: 271-294
  signature: 'def test_cli_sync_metadata_only_mutex_with_other_flags( project: Path, monkeypatch: pytest.MonkeyPatch )'
- kind: function
  qualified_name: tests/test_metadata_refresh:test_cli_sync_metadata_only_runs
  lines: 297-320
  signature: 'def test_cli_sync_metadata_only_runs(project: Path, monkeypatch: pytest.MonkeyPatch)'
incoming_refs: 0
outgoing_refs: 32
---
<!-- trie:section symbol=tests/test_metadata_refresh:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=3c16a1d6c0df615766baa0df7332a78ce75269150f5a3c1e9782aea5082a767b source_ref=65204173c592bc34e87ebc59176aeb0c67ef4747 role=test-infrastructure -->
Tests metadata-only triefact refresh functionality to ensure it updates front matter without calling the LLM.

- Verifies section bodies and fingerprints remain byte-identical after refresh
- Tests that `last_synced_at` timestamp preservation indicates LLM didn't run
- Confirms refresh picks up new graph edges in `incoming_refs`/`outgoing_refs`
- Validates idempotent behavior and CLI integration with exclusive flag handling
<!-- trie:end -->
<!-- trie:section symbol=tests/test_metadata_refresh:project fingerprint=65fd0b8d1c2fe0511dfb8e02ca8712e1da978440f17e1e72a14ebc38292a6981 body_fp=7cad9592f41167c8a47c8c87090d79e49aa202b098b717d909d8616406be1a23 source_ref=65204173c592bc34e87ebc59176aeb0c67ef4747 role=test-infrastructure -->
## `def project(tmp_path: Path) -> Path`

Creates a test project with two Python modules where beta imports from alpha.

- Returns the temporary project root directory path
- Sets up complete trie configuration in `trie.toml`
- Creates `src/alpha.py` with `alpha_fn()` function
- Creates `src/beta.py` that imports and calls `alpha_fn()`
<!-- trie:end -->
<!-- trie:section symbol=tests/test_metadata_refresh:_sync_both fingerprint=34f3862f727710588e479ae81af4b72c3d861240fedba9be071fe5ad9af64a17 body_fp=2060d0b8cb20c971426cd30576d78fbcb9eb716a46e184d522d65acb575cff47 source_ref=65204173c592bc34e87ebc59176aeb0c67ef4747 role=test-infrastructure -->
## `def _sync_both(project: Path) -> Store`

Scans and syncs both alpha.py and beta.py modules to create real triefacts on disk for testing refresh functionality.

- Returns an open Store that the caller must close
- Uses FakeTrieClient with deterministic prose output
- Creates .trie/graph.db database and performs initial sync
<!-- trie:end -->
<!-- trie:section symbol=tests/test_metadata_refresh:_read_yaml_front fingerprint=7e5679b0a04dfddc9fdfb4811524e98777352d0e45971091c9817ede8816a4a2 body_fp=bcee1f97c41f26513e23a8dadb69153c2a93f394df4b1f4a388e147d5fb4a7e7 source_ref=65204173c592bc34e87ebc59176aeb0c67ef4747 role=test-infrastructure -->
## `def _read_yaml_front(triefact_path: Path) -> dict`

Parse YAML front matter from a triefact file and return it as a dictionary.

- Raises AssertionError if no YAML front matter is found
<!-- trie:end -->
<!-- trie:section symbol=tests/test_metadata_refresh:_section_bodies fingerprint=a78be54ef29af611dbd8e6b081cebdb4f8bf91b70f60e801bb64fc6705ca735a body_fp=5305b51a97a824a9a5479b415dea6ee402b4b7c69a8bde05cacf05673e907034 source_ref=65204173c592bc34e87ebc59176aeb0c67ef4747 role=test-infrastructure -->
## `def _section_bodies(triefact_path: Path) -> dict[str, str]`

Extracts section bodies from a triefact file as a qualified name to content mapping.

- Returns: dict mapping symbol qualified names to their section body text between HTML comment sentinels
<!-- trie:end -->
<!-- trie:section symbol=tests/test_metadata_refresh:test_refresh_does_not_call_the_llm fingerprint=10efbe7f965fac4bfe13d5fb4ca4d3823e9bbe88e28e269add9756d9241929f6 body_fp=84b9affdca8491b16ab9da9f5f92f1c22a6701e4f505dce79d2c3e12695f42ac source_ref=65204173c592bc34e87ebc59176aeb0c67ef4747 role=test -->
## `def test_refresh_does_not_call_the_llm(project: Path)`

Verifies that `refresh_triefact_metadata` runs without requiring an LLM client, confirming metadata refresh is free and returns a `MetadataRefreshResult`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_metadata_refresh:test_refresh_preserves_section_bodies_byte_for_byte fingerprint=31af1871d315749a9c025d6b02b4438439f67bf623d93180d8dd9362c6159957 body_fp=103f00e58a5239edbb884b53ac99ab35394129c26510eebef3c96ba18cbd3844 source_ref=65204173c592bc34e87ebc59176aeb0c67ef4747 role=test -->
## `def test_refresh_preserves_section_bodies_byte_for_byte(project: Path)`

Verifies that refresh_triefact_metadata preserves section body content and sentinel comments unchanged.

- Captures section bodies and sentinels before metadata refresh operation
- Asserts bodies and sentinels remain byte-identical after refresh completes
<!-- trie:end -->
<!-- trie:section symbol=tests/test_metadata_refresh:test_refresh_preserves_last_synced_at fingerprint=347a26e83a5aa2b48ca7bf04dafc020f7cd666df80981ad495d005d3baaf8f53 body_fp=13bd7e02684d799d8a0a91f632ade34a9ffb3ed68401132f57fa598a7f126b17 source_ref=65204173c592bc34e87ebc59176aeb0c67ef4747 role=test -->
## `def test_refresh_preserves_last_synced_at(project: Path)`

Verifies that metadata refresh preserves the `last_synced_at` timestamp from triefact front matter.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_metadata_refresh:test_refresh_picks_up_new_edges_in_front_matter fingerprint=6263b0a5f31e8703e1010346c981e743ea8bfd5e1648e1ff930951164076bc6c body_fp=fddf4ec4bab79ae971f87a1d528e45b04a90b4724c4b8e74545a5afa261bb689 source_ref=65204173c592bc34e87ebc59176aeb0c67ef4747 role=test -->
## `def test_refresh_picks_up_new_edges_in_front_matter(project: Path)`

Tests that metadata refresh detects new cross-module references and updates ref counts in triefact front matter.

- Adds a new module referencing an existing function after initial sync
- Verifies `incoming_refs` count increases by 1 after refresh
<!-- trie:end -->
<!-- trie:section symbol=tests/test_metadata_refresh:test_refresh_is_idempotent fingerprint=0c9ddae21b38445f7612817c1a778908943e8e78e7f37def01bdefe1c08774de body_fp=fb6450b0d792428affbdecea78b122b3e1515def1b48263dd2d5f45c20b270ae source_ref=65204173c592bc34e87ebc59176aeb0c67ef4747 role=test -->
## `def test_refresh_is_idempotent(project: Path)`

Tests that `refresh_triefact_metadata` is idempotent by verifying consecutive refresh calls return `changed=False` on the second call.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_metadata_refresh:test_refresh_skips_missing_triefact fingerprint=f78515fc126a5e94dc695fb2c41fc0a47424413eb197cf2c80054305065d3589 body_fp=b063797303fa9c025ef0cd647061fa23de57ec0e2f1443c38702f4bf22344444 source_ref=65204173c592bc34e87ebc59176aeb0c67ef4747 role=test -->
## `def test_refresh_skips_missing_triefact(project: Path, tmp_path: Path)`

Tests that `refresh_triefact_metadata` returns unchanged result when triefact file doesn't exist yet.

- Creates new source file without syncing it first
- Verifies refresh returns `changed=False` for missing triefact
<!-- trie:end -->
<!-- trie:section symbol=tests/test_metadata_refresh:test_verify_passes_after_refresh fingerprint=4eaa18dfe98b605a6c3f831c8389b56cb62a3a1a6c9516dcd97cb212e9e1049d body_fp=87e63567eddd93a9a42b92970420f1fdaa4ddea5644586898698d4095c3f7b34 source_ref=65204173c592bc34e87ebc59176aeb0c67ef4747 role=test -->
## `def test_verify_passes_after_refresh(project: Path)`

Tests that `trie verify` passes after metadata refresh, ensuring no drift in section fingerprints.

- Verifies project is clean before and after refreshing metadata for both test modules
- Confirms metadata refresh preserves section content that verify checks against
<!-- trie:end -->
<!-- trie:section symbol=tests/test_metadata_refresh:test_cli_sync_metadata_only_mutex_with_other_flags fingerprint=bcc16ea751d379805d3dcab93e5c08c3d015fa75936a750c7d0720dad41bc5e8 body_fp=e89ec8724bb780b1e49487aa9f408dadc209e14b78ccac3b3002719ed577e1c9 source_ref=65204173c592bc34e87ebc59176aeb0c67ef4747 role=test-infrastructure -->
## `def test_cli_sync_metadata_only_mutex_with_other_flags( project: Path, monkeypatch: pytest.MonkeyPatch )`

Tests that `--metadata-only` flag is mutually exclusive with other sync command flags.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_metadata_refresh:test_cli_sync_metadata_only_runs fingerprint=638512cb71cdff8c21b134ba723f92f1951cce6873edf584fb30513f4b34677e body_fp=8598ef0fd70e5818f6976f118f73ebe60d6a52fb5f46086310233b83976f9f29 source_ref=65204173c592bc34e87ebc59176aeb0c67ef4747 role=cli-interface -->
## `def test_cli_sync_metadata_only_runs(project: Path, monkeypatch: pytest.MonkeyPatch)`

Tests end-to-end CLI execution of `trie sync --metadata-only` after cold sync, verifying it runs without invoking the LLM.

- Patches `make_client` to fail if the LLM client is constructed during metadata-only refresh
- Asserts CLI exits cleanly and reports refresh count in output
<!-- trie:end -->