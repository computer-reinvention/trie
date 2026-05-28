---
trie_version: 0.1.5
source: tests/test_diff.py
file_fingerprint: d83d0840359a9c272308c62c367d58bffef9a016ff138381191538600ddfaa56
last_synced_at: '2026-05-28T14:39:13Z'
defines:
- kind: module
  qualified_name: tests/test_diff:__module__
  lines: 1-173
- kind: function
  qualified_name: tests/test_diff:project
  lines: 17-28
- kind: function
  qualified_name: tests/test_diff:test_diff_returns_empty_when_clean
  lines: 31-42
- kind: function
  qualified_name: tests/test_diff:test_diff_shows_regenerated_content
  lines: 45-73
- kind: function
  qualified_name: tests/test_diff:test_diff_writes_to_preview_dir
  lines: 76-93
- kind: function
  qualified_name: tests/test_diff:test_diff_respects_limit
  lines: 96-109
- kind: function
  qualified_name: tests/test_diff:test_diff_respects_budget
  lines: 112-126
- kind: function
  qualified_name: tests/test_diff:test_cli_sync_dry_run_routes_through_diff
  lines: 129-153
- kind: function
  qualified_name: tests/test_diff:test_cli_sync_dry_run_no_stale
  lines: 156-172
incoming_refs: 0
outgoing_refs: 30
---
<!-- trie:section symbol=tests/test_diff:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=b0f4fd73434a4b5b98be1485b450ce20243bf35e3591c39aa502a22ed2571e9a source_ref=8dc0a9126adca8d8c25210e48ac9e88c059af184 -->
## `tests/test_diff`

Integration tests for `diff_project` and the `trie sync --dry-run` CLI route.

- `StableClient`: stub LLM client returning configurable body text
- `project`: pytest fixture providing a minimal `trie.toml` workspace in `tmp_path`
<!-- trie:end -->
<!-- trie:section symbol=tests/test_diff:project fingerprint=cd6f42afcf67cc71ef8f9decc80cf1252526bcf42bc7ac1d0055f21d53a8719b body_fp=f6716f0d46629cb46040354e5b48c03a5aaf87934ca2a824a18b03e4d08710f4 source_ref=8dc0a9126adca8d8c25210e48ac9e88c059af184 -->
## `project(tmp_path: Path) -> Path`

Pytest fixture that creates a minimal trie project with a `trie.toml` config and one source file `src/alpha.py`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_diff:test_diff_returns_empty_when_clean fingerprint=d2a7fa508081814258d613ec8b2872d7afd765927bf7186ab357128ee7f9bf0d body_fp=c8a27103d7b97bf94ec949aa605bd8ef906d613d5257797022dafa71b7fa8418 source_ref=6e1055a06b208b8b3b614db15da47304d012b68a -->
## `test_diff_returns_empty_when_clean(project: Path)`

Assert that `diff_project` returns no diffs when the triefact is already up-to-date with the source.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_diff:test_diff_shows_regenerated_content fingerprint=89d814a6af063c4e94a927e1ad9a5d3ba321e11e78109c5408a5c8c3fdc11a86 body_fp=9769182d1780878cafda5edeb15a71889c44e94abb36651831ca2a0a9f2c976e source_ref=6e1055a06b208b8b3b614db15da47304d012b68a -->
## `test_diff_shows_regenerated_content(project: Path)`

Assert that `diff_project` produces a unified diff between stale v1 and regenerated v2 content without mutating the canonical triefact.

- `preview_triefact_path`: written to disk; `canonical_triefact_path` left unchanged containing v1.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_diff:test_diff_writes_to_preview_dir fingerprint=6186a6b103b571bb8d221bc104bdbe3c8a225ebb2613b5d5158913e45b95d3e5 body_fp=a3ba323a792c96d6edb40c28d3c867e545780c83f22eaec4ce270ae23a5a22c5 source_ref=6e1055a06b208b8b3b614db15da47304d012b68a -->
## `test_diff_writes_to_preview_dir(project: Path)`

Assert that `diff_project` writes generated content under `.trie/preview` and leaves the canonical triefact untouched.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_diff:test_diff_respects_limit fingerprint=71c42631990c386a9403ab70f96ea8d4074843ec7a0a344e69c56129512ea813 body_fp=874d27b1d07a5203731767b73db1465683774edf87f3fcb4917564a1138868ef source_ref=6e1055a06b208b8b3b614db15da47304d012b68a -->
## `test_diff_respects_limit(project: Path)`

Assert that `diff_project` honours the `limit` parameter and reports skipped files in `files_skipped_no_budget`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_diff:test_diff_respects_budget fingerprint=95de6fbbd940c39eb444cde0d455543f20ea4616710b08dff6a0891436f92691 body_fp=8285f7372da8aa060976be800785aa68906159e98bbbfe071afa40e2a94275d9 source_ref=6e1055a06b208b8b3b614db15da47304d012b68a -->
## `test_diff_respects_budget(project: Path)`

Assert that `diff_project` stops processing files once a tiny USD budget is exhausted, producing fewer than all three diffs.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_diff:test_cli_sync_dry_run_routes_through_diff fingerprint=010c932914ab38809bb11f22bd06bb023d694dfc73a6ae2319a8b5110c7f2bf6 body_fp=171a238c9a2f2d02ccafb2a7a873fed57769ec1917ae6fd01b2d7f38ff31ec49 source_ref=6e1055a06b208b8b3b614db15da47304d012b68a -->
## `test_cli_sync_dry_run_routes_through_diff(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie sync --dry-run` prints unified diffs and leaves canonical triefacts unmodified.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_diff:test_cli_sync_dry_run_no_stale fingerprint=d6f94373a6ce8ad7631f8fb0e92857adf69fbcb9fa419531cb8d56b4ef087435 body_fp=582bc893eeb84d7c25980434748bf37df4f3ff93711d5df708382b0c196ecaff source_ref=6e1055a06b208b8b3b614db15da47304d012b68a -->
## `test_cli_sync_dry_run_no_stale(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie sync --dry-run` reports "no stale triefacts" when all triefacts are current.
<!-- trie:end -->