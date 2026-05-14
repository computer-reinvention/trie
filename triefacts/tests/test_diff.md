---
trie_version: 0.1.0
source: tests/test_diff.py
file_fingerprint: 3c845bf01769c96238939850337c6e86b9e68a5769aa381ce7efa60879d00785
last_synced_at: '2026-05-14T18:25:14Z'
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
<!-- trie:section symbol=tests/test_diff:StableClient fingerprint=109768c2e5c2fad4aae6fbacbbbb331ec1dfe34d8d55d99c6acc942db573c9f2 body_fp=82d8da0655254e4214c2abb2b87e85e11599b47a58e8c2a6ede0fb80c64f6731 source_ref=a5296757622b2c57f6957aab50d948d8174a61ce -->
## `StableClient`

Fake LLM client returning a fixed body string for deterministic diff testing.

- `body`: text returned by every `generate` call; swap to simulate content change.
- `calls`: incremented on each `generate` invocation.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_diff:StableClient.generate fingerprint=e73ecb3979350381e7d4da206e76fc08a2ae8c1c03f404b35cbc93c68259111e body_fp=13b47dabf134ae64bb2ba66a37f9007b4d2a451125d28333f49afc1e4d31d4e3 source_ref=a5296757622b2c57f6957aab50d948d8174a61ce -->
## `generate(self, _req: GenerationRequest) -> GenerationResponse`

Increment call counter and return a fixed `GenerationResponse` with the configured body text.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_diff:StableClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=9d067b772e73f67b1bb1b8cb6fc3a256c95035c670c6695fa426a36018030c0b source_ref=a5296757622b2c57f6957aab50d948d8174a61ce -->
## `count_tokens(_req: GenerationRequest) -> int`

Return a fixed token count of 100 for any request.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_diff:project fingerprint=cd6f42afcf67cc71ef8f9decc80cf1252526bcf42bc7ac1d0055f21d53a8719b body_fp=b40029bad44d26fbf286620ba55bddab1c5cb73d3c00e38d4cf5e798ac8d6906 source_ref=a5296757622b2c57f6957aab50d948d8174a61ce -->
## `project(tmp_path: Path) -> Path`

Pytest fixture that creates a minimal trie project with config and one source file in `tmp_path`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_diff:test_diff_returns_empty_when_clean fingerprint=4e23d7ea054a36f10ff1e59f1f4e079cafb0b4b0e192e6474d0b230ca879af4e body_fp=c8a27103d7b97bf94ec949aa605bd8ef906d613d5257797022dafa71b7fa8418 source_ref=a5296757622b2c57f6957aab50d948d8174a61ce -->
## `test_diff_returns_empty_when_clean(project: Path)`

Assert that `diff_project` returns no diffs when the triefact is already up-to-date with the source.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_diff:test_diff_shows_regenerated_content fingerprint=43af4c03a30eee9f84530667254a25c0db9574e4c3660a612b13921b03f7d279 body_fp=1dc232fda8279d0ba9a3d25dbf869bc88934687c1c7761d5f3ab4b96211730cc source_ref=a5296757622b2c57f6957aab50d948d8174a61ce -->
## `test_diff_shows_regenerated_content(project: Path)`

Assert that `diff_project` detects stale triefacts and produces a unified diff containing old and new content without modifying the canonical file.

- `project`: tmp directory fixture with a pre-configured `trie.toml` and source file.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_diff:test_diff_writes_to_preview_dir fingerprint=45565793de7c683899c57423072bab788f3854bead7975eaf4528d96633e85a4 body_fp=e71fa83d7758b1057f14fdbeb4f7c4c9ee101ecd0040c23d25e415066943f474 source_ref=a5296757622b2c57f6957aab50d948d8174a61ce -->
## `test_diff_writes_to_preview_dir(project: Path)`

Assert that `diff_project` writes preview files under `.trie/preview` without modifying the canonical triefact tree.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_diff:test_diff_respects_limit fingerprint=843d3e9f6fb2d2f5d036febeb7301708bc1122d0ecda19f54ad83e1f77871b21 body_fp=8191bb5c6b720ea7cbadc97c5e17e974f7d2e09083f499ca97c82df62c41c7cf source_ref=a5296757622b2c57f6957aab50d948d8174a61ce -->
## `test_diff_respects_limit(project: Path)`

Verify that `diff_project` honours the `limit` parameter and reports skipped files.

- `result.files_skipped_no_budget` must be ≥ 1 when three files exist and limit is 2.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_diff:test_diff_respects_budget fingerprint=07ec62b72193e2c10db841de90b3893f8b82c29dd9d51d41f6d3cbdda6bed73f body_fp=4091536d9b9ff6ce57ff33b918bf60fb4ecb87a0991222e2a20338d2430d78d3 source_ref=a5296757622b2c57f6957aab50d948d8174a61ce -->
## `test_diff_respects_budget(project: Path)`

Verify that `diff_project` stops processing files once a tiny USD budget is exhausted.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_diff:test_cli_sync_dry_run_routes_through_diff fingerprint=831194ab02e9603646bf0707cbf213dea38ecb0aee6c955a10996d3c9063cb87 body_fp=2a96ea1be960f3276e25edb4dea1a2afe924c89e97f30d744743d8f94f48213d source_ref=a5296757622b2c57f6957aab50d948d8174a61ce -->
## `test_cli_sync_dry_run_routes_through_diff(project: Path, monkeypatch: pytest.MonkeyPatch)`

Verify that `trie sync --dry-run` prints unified diffs and leaves canonical triefacts unmodified.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_diff:test_cli_sync_dry_run_no_stale fingerprint=e9d986de7ddd7664af9b0ae824115ee40ac9408d99a4d76615e0a8d163722375 body_fp=e87b56ad556f7aaa056235de39aa690104cd63a157c04910719fb32a92038751 source_ref=a5296757622b2c57f6957aab50d948d8174a61ce -->
## `test_cli_sync_dry_run_no_stale(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie sync --dry-run` prints "no stale triefacts" when all triefacts are current.
<!-- trie:end -->