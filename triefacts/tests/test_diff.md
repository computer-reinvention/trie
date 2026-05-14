---
trie_version: 0.1.0
source: tests/test_diff.py
file_fingerprint: 3c845bf01769c96238939850337c6e86b9e68a5769aa381ce7efa60879d00785
last_synced_at: '2026-05-14T17:24:48Z'
defines:
- kind: class
  qualified_name: tests/test_diff:StableClient
  lines: 18-36
- kind: method
  qualified_name: tests/test_diff:StableClient.generate
  lines: 25-33
- kind: method
  qualified_name: tests/test_diff:StableClient.count_tokens
  lines: 35-36
- kind: function
  qualified_name: tests/test_diff:project
  lines: 40-51
- kind: function
  qualified_name: tests/test_diff:test_diff_returns_empty_when_clean
  lines: 54-65
- kind: function
  qualified_name: tests/test_diff:test_diff_shows_regenerated_content
  lines: 68-96
- kind: function
  qualified_name: tests/test_diff:test_diff_writes_to_preview_dir
  lines: 99-116
- kind: function
  qualified_name: tests/test_diff:test_diff_respects_limit
  lines: 119-132
- kind: function
  qualified_name: tests/test_diff:test_diff_respects_budget
  lines: 135-149
- kind: function
  qualified_name: tests/test_diff:test_cli_sync_dry_run_routes_through_diff
  lines: 152-176
- kind: function
  qualified_name: tests/test_diff:test_cli_sync_dry_run_no_stale
  lines: 179-195
incoming_refs: 0
outgoing_refs: 24
---
<!-- trie:section symbol=tests/test_diff:StableClient fingerprint=109768c2e5c2fad4aae6fbacbbbb331ec1dfe34d8d55d99c6acc942db573c9f2 body_fp=b5c6133f15e8311615ad1428c99185e247cb5efab4eb642bee538b179fd53246 -->
## `StableClient`

Stub LLM client returning a fixed body on every `generate` call, tracking call count.

- `body`: text returned by `generate`; change it between uses to simulate model output drift.
- `calls`: incremented on each `generate` invocation.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_diff:StableClient.generate fingerprint=e73ecb3979350381e7d4da206e76fc08a2ae8c1c03f404b35cbc93c68259111e body_fp=13b47dabf134ae64bb2ba66a37f9007b4d2a451125d28333f49afc1e4d31d4e3 -->
## `generate(self, _req: GenerationRequest) -> GenerationResponse`

Increment call counter and return a fixed `GenerationResponse` with the configured body text.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_diff:StableClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=9d067b772e73f67b1bb1b8cb6fc3a256c95035c670c6695fa426a36018030c0b -->
## `count_tokens(_req: GenerationRequest) -> int`

Return a fixed token count of 100 for any request.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_diff:project fingerprint=cd6f42afcf67cc71ef8f9decc80cf1252526bcf42bc7ac1d0055f21d53a8719b body_fp=d3b5676e4cb8d9ca588fcb5654abffc5bb6a842b48a530d2d7de71cacdeea18d -->
## `project(tmp_path: Path) -> Path`

Pytest fixture that creates a minimal trie project with config and one source file.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_diff:test_diff_returns_empty_when_clean fingerprint=4e23d7ea054a36f10ff1e59f1f4e079cafb0b4b0e192e6474d0b230ca879af4e body_fp=9c15c50f1e7bfe59a0c05b5ace5b83b9bfa06942ecf34ac3b90bb7fdf0fb78bb -->
## `test_diff_returns_empty_when_clean(project: Path)`

Assert that `diff_project` returns no diffs when triefacts are already up to date.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_diff:test_diff_shows_regenerated_content fingerprint=43af4c03a30eee9f84530667254a25c0db9574e4c3660a612b13921b03f7d279 body_fp=0a5b2c6f816709f990e866523b2dfbed15681041f29116c8802b465f8f46d314 -->
## `test_diff_shows_regenerated_content(project: Path)`

Verify that `diff_project` detects stale content, writes a preview triefact, and leaves the canonical triefact unchanged.

- `project`: temporary project fixture with a pre-configured `trie.toml` and source file.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_diff:test_diff_writes_to_preview_dir fingerprint=45565793de7c683899c57423072bab788f3854bead7975eaf4528d96633e85a4 body_fp=e71fa83d7758b1057f14fdbeb4f7c4c9ee101ecd0040c23d25e415066943f474 -->
## `test_diff_writes_to_preview_dir(project: Path)`

Assert that `diff_project` writes preview files under `.trie/preview` without modifying the canonical triefact tree.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_diff:test_diff_respects_limit fingerprint=843d3e9f6fb2d2f5d036febeb7301708bc1122d0ecda19f54ad83e1f77871b21 body_fp=0a8e88300c66a184f3aa841b0bb5b9207d35f244064d5540367ea0eec4dbbe2c -->
## `test_diff_respects_limit(project: Path)`

Assert that `diff_project` returns exactly `limit` diffs and records skipped files when more stale files exist than the limit allows.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_diff:test_diff_respects_budget fingerprint=07ec62b72193e2c10db841de90b3893f8b82c29dd9d51d41f6d3cbdda6bed73f body_fp=c32572db901456176447d66c7d1b7cfbdc703f1465c00da795f26ebd5b1462e7 -->
## `test_diff_respects_budget(project: Path)`

Verify that `diff_project` stops processing files once a tiny USD budget is exhausted, returning fewer diffs than total stale files.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_diff:test_cli_sync_dry_run_routes_through_diff fingerprint=831194ab02e9603646bf0707cbf213dea38ecb0aee6c955a10996d3c9063cb87 body_fp=dfe00d1478f4b4f66dc1d87bceeac26cbd46442eedc3be685eb3d2a7cae5110a -->
## `test_cli_sync_dry_run_routes_through_diff(project: Path, monkeypatch: pytest.MonkeyPatch)`

Verify that `trie sync --dry-run` prints unified diffs and leaves the live triefact unmodified.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_diff:test_cli_sync_dry_run_no_stale fingerprint=e9d986de7ddd7664af9b0ae824115ee40ac9408d99a4d76615e0a8d163722375 body_fp=582bc893eeb84d7c25980434748bf37df4f3ff93711d5df708382b0c196ecaff -->
## `test_cli_sync_dry_run_no_stale(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie sync --dry-run` reports "no stale triefacts" when all triefacts are current.
<!-- trie:end -->