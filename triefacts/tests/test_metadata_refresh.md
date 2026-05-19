---
trie_version: 0.1.2
source: tests/test_metadata_refresh.py
file_fingerprint: 48334331aa6e68f827240e91235704508013e5ce086fe887a8b5f441aa12c023
last_synced_at: '2026-05-19T10:38:28Z'
description: Metadata-only triefact refresh.
defines:
- kind: module
  qualified_name: tests/test_metadata_refresh:__module__
  lines: 1-345
- kind: class
  qualified_name: tests/test_metadata_refresh:FakeClient
  lines: 40-59
- kind: method
  qualified_name: tests/test_metadata_refresh:FakeClient.generate
  lines: 48-56
- kind: method
  qualified_name: tests/test_metadata_refresh:FakeClient.count_tokens
  lines: 58-59
- kind: function
  qualified_name: tests/test_metadata_refresh:project
  lines: 63-83
- kind: function
  qualified_name: tests/test_metadata_refresh:_sync_both
  lines: 86-103
- kind: function
  qualified_name: tests/test_metadata_refresh:_read_yaml_front
  lines: 106-111
- kind: function
  qualified_name: tests/test_metadata_refresh:_section_bodies
  lines: 114-128
- kind: function
  qualified_name: tests/test_metadata_refresh:test_refresh_does_not_call_the_llm
  lines: 136-152
- kind: function
  qualified_name: tests/test_metadata_refresh:test_refresh_preserves_section_bodies_byte_for_byte
  lines: 155-176
- kind: function
  qualified_name: tests/test_metadata_refresh:test_refresh_preserves_last_synced_at
  lines: 179-199
- kind: function
  qualified_name: tests/test_metadata_refresh:test_refresh_picks_up_new_edges_in_front_matter
  lines: 202-231
- kind: function
  qualified_name: tests/test_metadata_refresh:test_refresh_is_idempotent
  lines: 234-249
- kind: function
  qualified_name: tests/test_metadata_refresh:test_refresh_skips_missing_triefact
  lines: 252-262
- kind: function
  qualified_name: tests/test_metadata_refresh:test_verify_passes_after_refresh
  lines: 265-287
- kind: function
  qualified_name: tests/test_metadata_refresh:test_cli_sync_metadata_only_mutex_with_other_flags
  lines: 295-318
- kind: function
  qualified_name: tests/test_metadata_refresh:test_cli_sync_metadata_only_runs
  lines: 321-344
incoming_refs: 0
outgoing_refs: 24
---
<!-- trie:section symbol=tests/test_metadata_refresh:FakeClient fingerprint=212d1e31e2179767aec84975b3d31b7e75fe9d651f0dbb060df73b9d8eeef8db body_fp=22b7ad288c9133e7874cf41ccbefa01fa69bd4e208c91b06b1d076bb36f07bcd source_ref=4a7b0bcd10b44c848a1d71eea71f3475cd7367ed -->
## `FakeClient`

Deterministic LLM stub for initial triefact cold-writes; records call count and returns fixed token counts.

- `calls`: incremented on each `generate` invocation to detect unexpected LLM usage.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_metadata_refresh:FakeClient.generate fingerprint=7328b86a4ba976097f1e8eec40c045a8090951dfeca29ef5debd39c4e6fc9a4b body_fp=e79bb5123c976321ce667677b5357e9caa8bdbb2a3b1e1cab801870a705a03fd source_ref=4a7b0bcd10b44c848a1d71eea71f3475cd7367ed -->
## `generate(self, _req: GenerationRequest) -> GenerationResponse`

Increment call counter and return a fixed deterministic `GenerationResponse` with hardcoded token counts and prose.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_metadata_refresh:FakeClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=c9fe918d06166ff51b2a10cfce7fb2648d6460a31168bee5233a6788df7c2b7c source_ref=4a7b0bcd10b44c848a1d71eea71f3475cd7367ed -->
## `count_tokens(_req: GenerationRequest) -> int`

Return a fixed token count of 100 without inspecting the request.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_metadata_refresh:project fingerprint=65fd0b8d1c2fe0511dfb8e02ca8712e1da978440f17e1e72a14ebc38292a6981 body_fp=b06937750b996ca8281f0024c902822633590dffc5b9c55bd4a239fe6a8a8cd1 source_ref=4a7b0bcd10b44c848a1d71eea71f3475cd7367ed -->
## `project(tmp_path: Path) -> Path`

Pytest fixture creating a two-module project with a cross-file import edge in a temporary directory.

- **returns** `tmp_path` configured with `trie.toml`, `src/alpha.py`, and `src/beta.py`
<!-- trie:end -->

<!-- trie:section symbol=tests/test_metadata_refresh:_sync_both fingerprint=1eea9e64b03fbdd8dea2d39175d9688c84811c137d1ac9868aa513c1ce8a531f body_fp=7fe328910a516dff4baefebf8cf564998c178645fedfb0afbda78bc4e50cf863 source_ref=4a7b0bcd10b44c848a1d71eea71f3475cd7367ed -->
## `_sync_both(project: Path) -> Store`

Scan and sync both `alpha.py` and `beta.py` modules, writing real triefacts to disk, and return the open `Store`.

- `project`: root path of the temporary test project fixture.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_metadata_refresh:_read_yaml_front fingerprint=7e5679b0a04dfddc9fdfb4811524e98777352d0e45971091c9817ede8816a4a2 body_fp=6fbfac7ac3018492d3cb8fc0ee36ed58b900a15a640093fa4c9a1ab64b9b6d6d source_ref=4a7b0bcd10b44c848a1d71eea71f3475cd7367ed -->
## `_read_yaml_front(triefact_path: Path) -> dict`

Parse and return the YAML front matter from a triefact file as a dict.

- `triefact_path`: asserts front matter exists; raises `AssertionError` if absent.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_metadata_refresh:_section_bodies fingerprint=a78be54ef29af611dbd8e6b081cebdb4f8bf91b70f60e801bb64fc6705ca735a body_fp=f14ceb703dd47c346aec6639f3761c15e5cb5af0fa9c619964ae784ba0e10759 source_ref=4a7b0bcd10b44c848a1d71eea71f3475cd7367ed -->
## `_section_bodies(triefact_path: Path) -> dict[str, str]`

Extract a `{qname: section_body}` map from a triefact file by parsing sentinel comments.

- `triefact_path`: path to a `.md` triefact file with `<!-- trie:section -->` markers.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_metadata_refresh:test_refresh_does_not_call_the_llm fingerprint=10efbe7f965fac4bfe13d5fb4ca4d3823e9bbe88e28e269add9756d9241929f6 body_fp=82ce776765a24f8206cf994d75a59695850e38459e2708faa9c3235dd21c6a3e source_ref=4a7b0bcd10b44c848a1d71eea71f3475cd7367ed -->
## `test_refresh_does_not_call_the_llm(project: Path)`

Assert that `refresh_triefact_metadata` accepts no client argument and returns a `MetadataRefreshResult` without invoking any LLM.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_metadata_refresh:test_refresh_preserves_section_bodies_byte_for_byte fingerprint=31af1871d315749a9c025d6b02b4438439f67bf623d93180d8dd9362c6159957 body_fp=51a072f18f59a1a2287fd6f0d59ae3b5e517fa2416ca601570217d57c9eb2019 source_ref=4a7b0bcd10b44c848a1d71eea71f3475cd7367ed -->
## `test_refresh_preserves_section_bodies_byte_for_byte(project: Path)`

Assert that `refresh_triefact_metadata` leaves section bodies and sentinel comments byte-identical.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_metadata_refresh:test_refresh_preserves_last_synced_at fingerprint=347a26e83a5aa2b48ca7bf04dafc020f7cd666df80981ad495d005d3baaf8f53 body_fp=c0d9242a2b98e3db148a50c713ffed599331de7628e1f095e2542c016b9cf413 source_ref=4a7b0bcd10b44c848a1d71eea71f3475cd7367ed -->
## `test_refresh_preserves_last_synced_at(project: Path)`

Assert that `refresh_triefact_metadata` leaves `last_synced_at` unchanged after an initial sync.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_metadata_refresh:test_refresh_picks_up_new_edges_in_front_matter fingerprint=6263b0a5f31e8703e1010346c981e743ea8bfd5e1648e1ff930951164076bc6c body_fp=40698d6b680a47149439c7909892f08ea975b548bab765cd8d673b4457934c18 source_ref=4a7b0bcd10b44c848a1d71eea71f3475cd7367ed -->
## `test_refresh_picks_up_new_edges_in_front_matter(project: Path)`

Assert that `refresh_triefact_metadata` updates `incoming_refs` in front matter when the graph gains a new edge after the initial sync.

- Adds `gamma.py` referencing `alpha_fn`, rescans, then refreshes alpha's metadata.
- Checks `incoming_refs` incremented by exactly 1.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_metadata_refresh:test_refresh_is_idempotent fingerprint=0c9ddae21b38445f7612817c1a778908943e8e78e7f37def01bdefe1c08774de body_fp=88a16953e3987efbde6a9f068780680ccbf2f3775b8e4e1905fc61bed1104202 source_ref=4a7b0bcd10b44c848a1d71eea71f3475cd7367ed -->
## `test_refresh_is_idempotent(project: Path)`

Assert that a second consecutive `refresh_triefact_metadata` call returns `changed=False`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_metadata_refresh:test_refresh_skips_missing_triefact fingerprint=f78515fc126a5e94dc695fb2c41fc0a47424413eb197cf2c80054305065d3589 body_fp=e0b749d818613d4e5c61f7235efc144af28ca6bad8a2cd420b814c85e70ad905 source_ref=4a7b0bcd10b44c848a1d71eea71f3475cd7367ed -->
## `test_refresh_skips_missing_triefact(project: Path, tmp_path: Path)`

Assert that `refresh_triefact_metadata` returns `changed=False` and raises no error when the source file has no corresponding triefact.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_metadata_refresh:test_verify_passes_after_refresh fingerprint=4eaa18dfe98b605a6c3f831c8389b56cb62a3a1a6c9516dcd97cb212e9e1049d body_fp=6ff68f6905dc434898a8b22d581166d0fa38562cb46e1cd03801029a03932223 source_ref=4a7b0bcd10b44c848a1d71eea71f3475cd7367ed -->
## `test_verify_passes_after_refresh(project: Path)`

Assert that `check_project` reports a clean state both before and after refreshing metadata for all synced modules.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_metadata_refresh:test_cli_sync_metadata_only_mutex_with_other_flags fingerprint=bcc16ea751d379805d3dcab93e5c08c3d015fa75936a750c7d0720dad41bc5e8 body_fp=c9a975a872c3472d0c40b8822c3f64c7b0f8f77a9a086e8cd94f874c5ea5f26f source_ref=4a7b0bcd10b44c848a1d71eea71f3475cd7367ed -->
## `test_cli_sync_metadata_only_mutex_with_other_flags(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `--metadata-only` combined with `--all`, `--dry-run`, `--budget`, `--limit`, or `--file` exits with code 1 and prints "cannot be combined".
<!-- trie:end -->

<!-- trie:section symbol=tests/test_metadata_refresh:test_cli_sync_metadata_only_runs fingerprint=638512cb71cdff8c21b134ba723f92f1951cce6873edf584fb30513f4b34677e body_fp=a3d89a7ab086119c614b6c1bd2c87caf739eee816a7e4eb85d4f57035d4308fb source_ref=4a7b0bcd10b44c848a1d71eea71f3475cd7367ed -->
## `test_cli_sync_metadata_only_runs(project: Path, monkeypatch: pytest.MonkeyPatch)`

Verify `trie sync --metadata-only` succeeds after a cold sync without constructing an LLM client.

- `monkeypatch`: patches `trie.cli.make_client` to raise if called, asserting no LLM access.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_metadata_refresh:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=a34e4eeaa51137909458725b5c25ed35fb2866a4df576976862c574aa4ed1af0 source_ref=02fb0e3fc60bd3c2e10955fd32f6888e43ae2c7e -->
## `tests/test_metadata_refresh`

Test suite for the metadata-only triefact refresh contract.

- Verifies `refresh_triefact_metadata` rewrites front matter without calling the LLM.
- Asserts section bodies, fingerprints, and `last_synced_at` are preserved.
- Covers edge-count deltas, idempotency, missing-triefact no-ops, and CLI mutex validation.
<!-- trie:end -->