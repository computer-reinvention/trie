---
trie_version: 0.1.0
source: tests/test_e2e_sync.py
file_fingerprint: 90d68079a850ec282b726421f3ffe31992e90309f93ad90186c79440d3016e87
last_synced_at: '2026-05-16T10:51:12Z'
description: End-to-end test for `trie sync --file` against the tiny fixture repo.
defines:
- kind: class
  qualified_name: tests/test_e2e_sync:FakeClient
  lines: 26-50
- kind: method
  qualified_name: tests/test_e2e_sync:FakeClient.__post_init__
  lines: 33-34
- kind: method
  qualified_name: tests/test_e2e_sync:FakeClient.generate
  lines: 36-47
- kind: method
  qualified_name: tests/test_e2e_sync:FakeClient.count_tokens
  lines: 49-50
- kind: function
  qualified_name: tests/test_e2e_sync:project
  lines: 54-67
- kind: function
  qualified_name: tests/test_e2e_sync:test_sync_single_file_writes_triefact
  lines: 70-102
- kind: function
  qualified_name: tests/test_e2e_sync:test_human_prose_between_sections_survives_resync
  lines: 105-140
- kind: function
  qualified_name: tests/test_e2e_sync:test_resync_updates_section_when_source_changes
  lines: 143-174
- kind: function
  qualified_name: tests/test_e2e_sync:test_resync_removes_section_when_symbol_deleted
  lines: 177-202
- kind: function
  qualified_name: tests/test_e2e_sync:test_first_call_creates_cache_subsequent_calls_read
  lines: 205-219
- kind: function
  qualified_name: tests/test_e2e_sync:test_cli_sync_auto_bootstraps_first_run
  lines: 222-235
- kind: function
  qualified_name: tests/test_e2e_sync:test_cli_sync_errors_on_missing_file
  lines: 238-242
- kind: function
  qualified_name: tests/test_e2e_sync:test_cli_sync_errors_when_no_config
  lines: 245-251
- kind: function
  qualified_name: tests/test_e2e_sync:_init_git
  lines: 257-263
- kind: function
  qualified_name: tests/test_e2e_sync:test_first_sync_in_git_repo_stamps_source_ref
  lines: 266-284
- kind: function
  qualified_name: tests/test_e2e_sync:test_sync_outside_git_repo_omits_source_ref
  lines: 287-299
- kind: function
  qualified_name: tests/test_e2e_sync:test_resync_with_committed_history_takes_diff_aware_path
  lines: 302-342
- kind: function
  qualified_name: tests/test_e2e_sync:test_resync_after_uncommitted_change_falls_back_to_cold
  lines: 345-375
incoming_refs: 0
outgoing_refs: 26
---
<!-- trie:section symbol=tests/test_e2e_sync:FakeClient fingerprint=464e2049df41370146411117991983091506f10d89f570b2aa42a935790758e0 body_fp=9852cd47a02dd04f455480536d875320091630d48396ecdd6bed11d0336eab23 source_ref=71542c3c3e0ef178aa3ed0414dd5c02ff50b0c94 -->
## `FakeClient`

Deterministic LLM client stub that returns templated responses and records call count for cache-accounting assertions.

- `calls`: incremented on each `generate` invocation; used to vary cache token fields.
- `requests_seen`: accumulates every `GenerationRequest` passed to `generate`.
- First call sets `cache_creation_input_tokens=100`; subsequent calls set `cache_read_input_tokens=100`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_e2e_sync:FakeClient.generate fingerprint=32144d57a656826d76eaf8439dcfc814411dfe621be53b51e279bc7343b2ba1e body_fp=cf30aea7c67edc55eace2ecf01ab57fa6ec472a867e7157aff6f248b2af25793 source_ref=71542c3c3e0ef178aa3ed0414dd5c02ff50b0c94 -->
## `generate(self, req: GenerationRequest) -> GenerationResponse`

Return a deterministic canned `GenerationResponse`, incrementing call count and recording the request.

- First call sets `cache_creation_input_tokens=100`; subsequent calls set `cache_read_input_tokens=100`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_e2e_sync:FakeClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=9d067b772e73f67b1bb1b8cb6fc3a256c95035c670c6695fa426a36018030c0b source_ref=71542c3c3e0ef178aa3ed0414dd5c02ff50b0c94 -->
## `count_tokens(_req: GenerationRequest) -> int`

Return a fixed token count of 100 for any request.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_e2e_sync:project fingerprint=16df3ebd676a6f8d2473a730ffb75c5fd86a5da52f7caae13faab42c03ae674f body_fp=90e01297f24ca4631800ee4d8f3ac5b6be0ad06974411d39fec664465fd7e8a5 source_ref=71542c3c3e0ef178aa3ed0414dd5c02ff50b0c94 -->
## `project(tmp_path: Path) -> Path`

Copy the tiny fixture repo into a temp dir and write a minimal `trie.toml` for `Config.find_and_load`.

- **returns** path to the populated project root inside `tmp_path`
<!-- trie:end -->

<!-- trie:section symbol=tests/test_e2e_sync:test_sync_single_file_writes_triefact fingerprint=94b9928853195be421740237bfaca67bdaa59a4ba7330e35e51099530b458628 body_fp=62794588a127fcd52bcafd93a75344430c1e2452cf0f4382f65c6f20500f7986 source_ref=491d210417adfffde3fc0215cd433e1dae6e3a49 -->
## `test_sync_single_file_writes_triefact(project: Path)`

Verify that syncing `calculator.py` generates exactly 6 sections (all parser-surfaced symbols including `_internal_helper`), writes a triefact file with correct front matter, and no longer omits private symbols.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_e2e_sync:test_human_prose_between_sections_survives_resync fingerprint=918ac4736b7f4fb6b3d9d2da82a2d4084996a1f4547563434cf25bfcc35c6abe body_fp=1ebd39b08ee00b557357e0e2e42d69b5595a57d159cca148fe63f1badab81a06 source_ref=71542c3c3e0ef178aa3ed0414dd5c02ff50b0c94 -->
## `test_human_prose_between_sections_survives_resync(project: Path)`

Verify that hand-written Markdown prose inserted between managed sections is preserved across a resync.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_e2e_sync:test_resync_updates_section_when_source_changes fingerprint=511dda2600814a422bce301b8428b60e6ba80391945cfcaa349e66b7675df2bb body_fp=71b0f78b39bd4f0b428943910091611dc3bc79762359fce05b62fcc363f2a8ea source_ref=71542c3c3e0ef178aa3ed0414dd5c02ff50b0c94 -->
## `test_resync_updates_section_when_source_changes(project: Path)`

Verify that re-syncing a file whose source has changed produces a section with an updated fingerprint.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_e2e_sync:test_resync_removes_section_when_symbol_deleted fingerprint=9f7d8ea0b59c3bde607537336b4d182624eb6e60374ad8f6f4307c66a3767229 body_fp=fddd3ad4deafd68c0c87c27af76084ffb3d73adbfca08a654a98e9ebf0727a88 source_ref=71542c3c3e0ef178aa3ed0414dd5c02ff50b0c94 -->
## `test_resync_removes_section_when_symbol_deleted(project: Path)`

Verify that resyncing after a symbol is deleted from source removes its section from the triefact.

- `project`: fixture providing a temp copy of the tiny repo with config.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_e2e_sync:test_first_call_creates_cache_subsequent_calls_read fingerprint=d349234f6f28f8ec4ddae981bc0d114c8a9720ace243788a9b245d233d30c096 body_fp=86980e18df5e5e1cfa912417f7e092cbc866fd2f7d9842244f92aa6219fd4074 source_ref=491d210417adfffde3fc0215cd433e1dae6e3a49 -->
## `test_first_call_creates_cache_subsequent_calls_read(project: Path)`

Verify that the first LLM call accumulates cache-creation tokens and all subsequent calls accumulate cache-read tokens.

- `cache_creation_input_tokens`: expected 100 (first call only).
- `cache_read_input_tokens`: expected 500 (5 remaining calls × 100).
<!-- trie:end -->

<!-- trie:section symbol=tests/test_e2e_sync:test_cli_sync_auto_bootstraps_first_run fingerprint=2bcfc5f6118090e540d8bf670a676551d99e301c4e54623b6d9463d576f6ad4a body_fp=5ff57e66c778a6a78d30b673e101b395748e87326d5b010dd4bc3b82adcccffa source_ref=639d88fa0c90df5f1040715075c2c2de1239593e -->
## `test_cli_sync_auto_bootstraps_first_run(project: Path, monkeypatch)`

Verify that `trie sync --limit 10` exits successfully and prints "synced" on a fresh project with no prior triefacts.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_e2e_sync:test_cli_sync_errors_on_missing_file fingerprint=ac055df6cd0b2982d47b7f5ddf8e532f4a1c38dfbefaefb6c220970792004945 body_fp=4d1a9563784682a40bdde2ae37f1f7638df0d0faedd8fda6f7baee5f255368f0 source_ref=71542c3c3e0ef178aa3ed0414dd5c02ff50b0c94 -->
## `test_cli_sync_errors_on_missing_file(project: Path)`

Assert that `trie sync --file` exits with code 1 and reports "does not exist" for a non-existent path.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_e2e_sync:test_cli_sync_errors_when_no_config fingerprint=f24a74ab8515b27a1593fa499df188e4ff6ff93508d61d9afbceebd6daffa72e body_fp=ff5194a889df0972c8902cf38c4311f242c4308884547f580bddf3c86818d806 source_ref=71542c3c3e0ef178aa3ed0414dd5c02ff50b0c94 -->
## `test_cli_sync_errors_when_no_config(tmp_path: Path)`

Assert that `trie sync --file` exits with code 1 and mentions `trie.toml` when no config file is found.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_e2e_sync:test_first_sync_in_git_repo_stamps_source_ref fingerprint=3cf6343c5a3f146e8cd69642be21dbf0170a9a1f397e446884acb686081434a3 body_fp=9a0665c3ff5e7567e34ecdb998d90b70a5ad768dfa74ee0b1e85f18d87441da8 source_ref=71542c3c3e0ef178aa3ed0414dd5c02ff50b0c94 -->
## `test_first_sync_in_git_repo_stamps_source_ref(project: Path)`

Assert that syncing a git-managed file writes a 40-character SHA-1 `source_ref` into every triefact section.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_e2e_sync:test_sync_outside_git_repo_omits_source_ref fingerprint=9cf4b71feeef97f2de3c2c1fc42f325f5326babf39a788ac1bf7f712228a8649 body_fp=bebc5577b793d8c31d3e8144d83edb1f391598ac2f5026b6eaaddb5ea23a7972 source_ref=71542c3c3e0ef178aa3ed0414dd5c02ff50b0c94 -->
## `test_sync_outside_git_repo_omits_source_ref(project: Path)`

Assert that syncing a file outside a git repo produces triefact sections with no `source_ref` field.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_e2e_sync:test_resync_with_committed_history_takes_diff_aware_path fingerprint=1bd65ccdbd4b8049db3ee27391af7a14573c6e435c527292269a33fabdac7c75 body_fp=40b03d75ce56657730ad21d8bf755e8c04c1f3e9c864cb7686e15040ec9ddfad source_ref=71542c3c3e0ef178aa3ed0414dd5c02ff50b0c94 -->
## `test_resync_with_committed_history_takes_diff_aware_path(project: Path)`

Verify that resyncing a committed-then-modified file passes previous source and prose to the generator via `<previous_source>` and `<previous_prose>` tags in the request.

- `project`: temp directory with fixture repo, initialised with a git repo and first commit before modification.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_e2e_sync:test_resync_after_uncommitted_change_falls_back_to_cold fingerprint=5d3a03ac89ffaf02efdd90a0b822ca9d456842b2602ae29c024e7470ef1b6530 body_fp=e848b73bf8549064594283fac633410b6116b1d9d013a49ac491acbea87dc75d source_ref=71542c3c3e0ef178aa3ed0414dd5c02ff50b0c94 -->
## `test_resync_after_uncommitted_change_falls_back_to_cold(project: Path)`

Verify that modifying a file without committing causes resync to fall back to cold generation, omitting `<previous_source>` from all requests.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_e2e_sync:FakeClient.__post_init__ fingerprint=acb5f189b6faf4617c18bdcf095ff513902e065e9313e669660eb6579ac7a01f body_fp=d3cd75b1f15faecb54c8436c1279b02e02baf3a2f8c17967da4e260bde105996 source_ref=491d210417adfffde3fc0215cd433e1dae6e3a49 -->
## `__post_init__(self) -> None`

Initialize `requests_seen` to an empty list after dataclass field assignment.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_e2e_sync:_init_git fingerprint=aa18a74813989bea6f6328ca8a6d8a11921def8852349e9daaea55280c606b4c body_fp=1b2e5e738e5761c5bf871861027e03a932da6e64d83ad64eb3b9882d35645d4e source_ref=491d210417adfffde3fc0215cd433e1dae6e3a49 -->
## `_init_git(repo: Path) -> None`

Initialize a bare git repository with a default `main` branch and test identity in `repo`.
<!-- trie:end -->