---
trie_version: 0.1.0
source: tests/test_diff.py
file_fingerprint: 3c845bf01769c96238939850337c6e86b9e68a5769aa381ce7efa60879d00785
last_synced_at: '2026-05-12T18:27:12Z'
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
<!-- trie:section symbol=tests/test_diff:StableClient fingerprint=109768c2e5c2fad4aae6fbacbbbb331ec1dfe34d8d55d99c6acc942db573c9f2 body_fp=ed1f97a00f00fa433e6e307549b4abe9f58549506cfbc7e1319cb7939433cc2f -->
## `StableClient`

Fake LLM client returning configurable body text for diff testing; first call uses `body`, and `calls` tracks invocations.

- `body`: default `"## v1\n\nv1 body."`, returned by every `generate` call
- `calls`: incremented on each `generate` invocation
<!-- trie:end -->

<!-- trie:section symbol=tests/test_diff:StableClient.generate fingerprint=e73ecb3979350381e7d4da206e76fc08a2ae8c1c03f404b35cbc93c68259111e body_fp=9b526e241a33e65d31eeee198ddff3c4cb5a85c78ffe76187b75daee6bbd3ddd -->
## `generate(self, _req: GenerationRequest) -> GenerationResponse`

Increment call counter and return a fixed `GenerationResponse` with the client's preset body text.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_diff:StableClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=9d067b772e73f67b1bb1b8cb6fc3a256c95035c670c6695fa426a36018030c0b -->
## `count_tokens(_req: GenerationRequest) -> int`

Return a fixed token count of 100 for any request.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_diff:project fingerprint=cd6f42afcf67cc71ef8f9decc80cf1252526bcf42bc7ac1d0055f21d53a8719b body_fp=57c7d007fe0660534855f28613d814d48b22261af4015789380880a6235d5ac1 -->
## `project(tmp_path: Path) -> Path`

Pytest fixture that creates a minimal trie project with config and one Python source file.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_diff:test_diff_returns_empty_when_clean fingerprint=4e23d7ea054a36f10ff1e59f1f4e079cafb0b4b0e192e6474d0b230ca879af4e body_fp=c8a27103d7b97bf94ec949aa605bd8ef906d613d5257797022dafa71b7fa8418 -->
## `test_diff_returns_empty_when_clean(project: Path)`

Assert that `diff_project` returns no diffs when the triefact is already up-to-date with the source.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_diff:test_diff_shows_regenerated_content fingerprint=43af4c03a30eee9f84530667254a25c0db9574e4c3660a612b13921b03f7d279 body_fp=22f03380ce872655fb2ad01a47719eedb11de164079cf8fe0fcf496100ffdb7b -->
## `test_diff_shows_regenerated_content(project: Path)`

Assert that `diff_project` detects a stale triefact, regenerates with new content, and writes a preview without touching the canonical file.

- `project`: tmp directory fixture with a pre-configured `trie.toml` and source file.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_diff:test_diff_writes_to_preview_dir fingerprint=45565793de7c683899c57423072bab788f3854bead7975eaf4528d96633e85a4 body_fp=42621ee50db600cdfcc3b09b1302ec316ff899016d38c793d0bdbbb0c535d22c -->
## `test_diff_writes_to_preview_dir(project: Path)`

Assert that `diff_project` writes preview files under `.trie/preview` without touching the canonical triefact tree.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_diff:test_diff_respects_limit fingerprint=843d3e9f6fb2d2f5d036febeb7301708bc1122d0ecda19f54ad83e1f77871b21 body_fp=253218455052d3bfea929718524df7d0235cd84897c2233400c189c6cd9b94ae -->
## `test_diff_respects_limit(project: Path)`

Assert that `diff_project` returns at most `limit` diffs and records skipped files when more stale files exist than the limit allows.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_diff:test_diff_respects_budget fingerprint=07ec62b72193e2c10db841de90b3893f8b82c29dd9d51d41f6d3cbdda6bed73f body_fp=428fffa04d2228365cead726d735e9be66078e85aece3b47aa2cacee0cef6eaf -->
## `test_diff_respects_budget(project: Path)`

Verify that `diff_project` stops processing files once a tiny USD budget is exhausted, producing fewer than all possible diffs.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_diff:test_cli_sync_dry_run_routes_through_diff fingerprint=831194ab02e9603646bf0707cbf213dea38ecb0aee6c955a10996d3c9063cb87 body_fp=171a238c9a2f2d02ccafb2a7a873fed57769ec1917ae6fd01b2d7f38ff31ec49 -->
## `test_cli_sync_dry_run_routes_through_diff(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie sync --dry-run` prints unified diffs and leaves canonical triefacts unmodified.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_diff:test_cli_sync_dry_run_no_stale fingerprint=e9d986de7ddd7664af9b0ae824115ee40ac9408d99a4d76615e0a8d163722375 body_fp=e87b56ad556f7aaa056235de39aa690104cd63a157c04910719fb32a92038751 -->
## `test_cli_sync_dry_run_no_stale(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie sync --dry-run` prints "no stale triefacts" when all triefacts are current.
<!-- trie:end -->