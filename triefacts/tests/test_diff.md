---
trie_version: 0.1.2
source: tests/test_diff.py
file_fingerprint: 1f4779afa4009323a30870176334a0872b1aa98a56daa4c2470442fc5094860d
last_synced_at: '2026-05-23T23:52:14Z'
defines:
- kind: module
  qualified_name: tests/test_diff:__module__
  lines: 1-196
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
outgoing_refs: 26
---
<!-- trie:section symbol=tests/test_diff:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=b0f4fd73434a4b5b98be1485b450ce20243bf35e3591c39aa502a22ed2571e9a source_ref=8dc0a9126adca8d8c25210e48ac9e88c059af184 -->
## `tests/test_diff`

Integration tests for `diff_project` and the `trie sync --dry-run` CLI route.

- `StableClient`: stub LLM client returning configurable body text
- `project`: pytest fixture providing a minimal `trie.toml` workspace in `tmp_path`
<!-- trie:end -->
<!-- trie:section symbol=tests/test_diff:StableClient fingerprint=109768c2e5c2fad4aae6fbacbbbb331ec1dfe34d8d55d99c6acc942db573c9f2 body_fp=f07e8a9e69b50c713126eddee14dd90247d5cb2f48ddb7dea7b02f6a9368390f source_ref=8dc0a9126adca8d8c25210e48ac9e88c059af184 -->
## `StableClient`

Fake LLM client for diff tests that returns a configurable fixed body on every `generate` call.

- `body`: the text returned as `GenerationResponse.text`; change between test steps to simulate regeneration.
- `calls`: incremented on each `generate` invocation; useful for asserting call counts.
- `count_tokens`: always returns `100`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_diff:StableClient.generate fingerprint=e73ecb3979350381e7d4da206e76fc08a2ae8c1c03f404b35cbc93c68259111e body_fp=ba3fa578fbbcc5d2fa76cb1deeffe65fea6f530625e7457ce2bad292c012d9eb source_ref=8dc0a9126adca8d8c25210e48ac9e88c059af184 -->
## `StableClient.generate(_req: GenerationRequest) -> GenerationResponse`

Increment `StableClient.calls` and return a fixed `GenerationResponse` using `self.body`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_diff:StableClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=ad353773e18b6cd4b639341be389817905e10474f5976e6e4a89309eeba76b7e source_ref=8dc0a9126adca8d8c25210e48ac9e88c059af184 -->
## `StableClient.count_tokens(_req: GenerationRequest) -> int`

Always returns 100 for any `StableClient` token-count request.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_diff:project fingerprint=cd6f42afcf67cc71ef8f9decc80cf1252526bcf42bc7ac1d0055f21d53a8719b body_fp=f6716f0d46629cb46040354e5b48c03a5aaf87934ca2a824a18b03e4d08710f4 source_ref=8dc0a9126adca8d8c25210e48ac9e88c059af184 -->
## `project(tmp_path: Path) -> Path`

Pytest fixture that creates a minimal trie project with a `trie.toml` config and one source file `src/alpha.py`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_diff:test_diff_returns_empty_when_clean fingerprint=4e23d7ea054a36f10ff1e59f1f4e079cafb0b4b0e192e6474d0b230ca879af4e body_fp=c8a27103d7b97bf94ec949aa605bd8ef906d613d5257797022dafa71b7fa8418 source_ref=8dc0a9126adca8d8c25210e48ac9e88c059af184 -->
## `test_diff_returns_empty_when_clean(project: Path)`

Assert that `diff_project` returns no diffs when the triefact is already up-to-date with the source.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_diff:test_diff_shows_regenerated_content fingerprint=43af4c03a30eee9f84530667254a25c0db9574e4c3660a612b13921b03f7d279 body_fp=9769182d1780878cafda5edeb15a71889c44e94abb36651831ca2a0a9f2c976e source_ref=8dc0a9126adca8d8c25210e48ac9e88c059af184 -->
## `test_diff_shows_regenerated_content(project: Path)`

Assert that `diff_project` produces a unified diff between stale v1 and regenerated v2 content without mutating the canonical triefact.

- `preview_triefact_path`: written to disk; `canonical_triefact_path` left unchanged containing v1.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_diff:test_diff_writes_to_preview_dir fingerprint=45565793de7c683899c57423072bab788f3854bead7975eaf4528d96633e85a4 body_fp=a3ba323a792c96d6edb40c28d3c867e545780c83f22eaec4ce270ae23a5a22c5 source_ref=8dc0a9126adca8d8c25210e48ac9e88c059af184 -->
## `test_diff_writes_to_preview_dir(project: Path)`

Assert that `diff_project` writes generated content under `.trie/preview` and leaves the canonical triefact untouched.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_diff:test_diff_respects_limit fingerprint=843d3e9f6fb2d2f5d036febeb7301708bc1122d0ecda19f54ad83e1f77871b21 body_fp=874d27b1d07a5203731767b73db1465683774edf87f3fcb4917564a1138868ef source_ref=8dc0a9126adca8d8c25210e48ac9e88c059af184 -->
## `test_diff_respects_limit(project: Path)`

Assert that `diff_project` honours the `limit` parameter and reports skipped files in `files_skipped_no_budget`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_diff:test_diff_respects_budget fingerprint=07ec62b72193e2c10db841de90b3893f8b82c29dd9d51d41f6d3cbdda6bed73f body_fp=8285f7372da8aa060976be800785aa68906159e98bbbfe071afa40e2a94275d9 source_ref=8dc0a9126adca8d8c25210e48ac9e88c059af184 -->
## `test_diff_respects_budget(project: Path)`

Assert that `diff_project` stops processing files once a tiny USD budget is exhausted, producing fewer than all three diffs.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_diff:test_cli_sync_dry_run_routes_through_diff fingerprint=b6587b526abd74010f9e1b5cd19969bf6b436434bcccb822cbf776aa7970202c body_fp=171a238c9a2f2d02ccafb2a7a873fed57769ec1917ae6fd01b2d7f38ff31ec49 source_ref=8dc0a9126adca8d8c25210e48ac9e88c059af184 -->
## `test_cli_sync_dry_run_routes_through_diff(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie sync --dry-run` prints unified diffs and leaves canonical triefacts unmodified.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_diff:test_cli_sync_dry_run_no_stale fingerprint=185c02160ac4f6a11a92d047293f7243db9077443bfc2b8a2d17620dfa9b3c57 body_fp=582bc893eeb84d7c25980434748bf37df4f3ff93711d5df708382b0c196ecaff source_ref=8dc0a9126adca8d8c25210e48ac9e88c059af184 -->
## `test_cli_sync_dry_run_no_stale(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie sync --dry-run` reports "no stale triefacts" when all triefacts are current.
<!-- trie:end -->