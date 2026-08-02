---
trie_version: 0.3.0
source: tests/test_diff.py
file_fingerprint: d83d0840359a9c272308c62c367d58bffef9a016ff138381191538600ddfaa56
last_synced_at: '2026-06-06T13:16:29Z'
defines:
- kind: module
  qualified_name: tests/test_diff:__module__
  lines: 1-173
- kind: function
  qualified_name: tests/test_diff:project
  lines: 17-28
  signature: 'def project(tmp_path: Path) -> Path'
- kind: function
  qualified_name: tests/test_diff:test_diff_returns_empty_when_clean
  lines: 31-42
  signature: 'def test_diff_returns_empty_when_clean(project: Path)'
- kind: function
  qualified_name: tests/test_diff:test_diff_shows_regenerated_content
  lines: 45-73
  signature: 'def test_diff_shows_regenerated_content(project: Path)'
- kind: function
  qualified_name: tests/test_diff:test_diff_writes_to_preview_dir
  lines: 76-93
  signature: 'def test_diff_writes_to_preview_dir(project: Path)'
- kind: function
  qualified_name: tests/test_diff:test_diff_respects_limit
  lines: 96-109
  signature: 'def test_diff_respects_limit(project: Path)'
- kind: function
  qualified_name: tests/test_diff:test_diff_respects_budget
  lines: 112-126
  signature: 'def test_diff_respects_budget(project: Path)'
- kind: function
  qualified_name: tests/test_diff:test_cli_sync_dry_run_routes_through_diff
  lines: 129-153
  signature: 'def test_cli_sync_dry_run_routes_through_diff(project: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_diff:test_cli_sync_dry_run_no_stale
  lines: 156-172
  signature: 'def test_cli_sync_dry_run_no_stale(project: Path, monkeypatch: pytest.MonkeyPatch)'
incoming_refs: 0
outgoing_refs: 37
---
<!-- trie:section symbol=tests/test_diff:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=4197c295cec71e22894d2c9e50f99741ef1932f46191f01b5068074b9a9a2d4b source_ref=6e1055a06b208b8b3b614db15da47304d012b68a role=test-infrastructure -->
Tests for the diff functionality that compares current source code against existing triefacts and generates unified diffs for changes.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_diff:project fingerprint=cd6f42afcf67cc71ef8f9decc80cf1252526bcf42bc7ac1d0055f21d53a8719b body_fp=416c2edc6f8142f507501ea83545a920ff46c528098714dbe89c45cccd76ebf1 source_ref=6e1055a06b208b8b3b614db15da47304d012b68a role=test-infrastructure -->
## `def project(tmp_path: Path) -> Path`

Creates a temporary project directory with trie configuration file and sample Python source file for testing.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_diff:test_diff_returns_empty_when_clean fingerprint=d2a7fa508081814258d613ec8b2872d7afd765927bf7186ab357128ee7f9bf0d body_fp=4489ea6a1a5a95615d33eb83af2ab4b33d9d3dc24cb866468bd569134aa5d0f7 source_ref=6e1055a06b208b8b3b614db15da47304d012b68a role=test-infrastructure -->
## `def test_diff_returns_empty_when_clean(project: Path)`

Verifies that diff_project returns no diffs when triefacts are up-to-date with source files.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_diff:test_diff_shows_regenerated_content fingerprint=89d814a6af063c4e94a927e1ad9a5d3ba321e11e78109c5408a5c8c3fdc11a86 body_fp=239cb1cabe6a5896ee4361b10acbab9cfc3cf089e056aecd0d0523b8d3362739 source_ref=6e1055a06b208b8b3b614db15da47304d012b68a role=test-infrastructure -->
## `def test_diff_shows_regenerated_content(project: Path)`

Verifies diff_project detects stale triefacts and generates preview diffs without modifying live files.

- Syncs v1 triefact, modifies source, then diffs with v2 client
- Asserts unified diff contains both v1 and v2 content
- Confirms preview file exists while canonical file remains unchanged
<!-- trie:end -->
<!-- trie:section symbol=tests/test_diff:test_diff_writes_to_preview_dir fingerprint=6186a6b103b571bb8d221bc104bdbe3c8a225ebb2613b5d5158913e45b95d3e5 body_fp=3acdbfab9e482ed2a60d12c49c8ce598324348f638ca7750fd7bc102c310a13d source_ref=6e1055a06b208b8b3b614db15da47304d012b68a role=test-infrastructure -->
## `def test_diff_writes_to_preview_dir(project: Path)`

Verifies that diff_project writes preview triefacts to `.trie/preview` directory without modifying canonical files.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_diff:test_diff_respects_limit fingerprint=71c42631990c386a9403ab70f96ea8d4074843ec7a0a344e69c56129512ea813 body_fp=7f7a1a8472d79fa857bb6d1eb727c6b244ff32df6b7884915c2b3e19ac69c5e7 source_ref=6e1055a06b208b8b3b614db15da47304d012b68a role=documentation-sync -->
## `def test_diff_respects_limit(project: Path)`

Verifies that `diff_project` respects the `limit` parameter by processing at most the specified number of files.

- Creates 3 Python files but limits processing to 2
- Asserts exactly 2 diffs are generated and at least 1 file is skipped
<!-- trie:end -->
<!-- trie:section symbol=tests/test_diff:test_diff_respects_budget fingerprint=95de6fbbd940c39eb444cde0d455543f20ea4616710b08dff6a0891436f92691 body_fp=85a82a43729de7fd3de1530ac952e8178d80f2e35a19d80a77793526c8cb5ea1 source_ref=6e1055a06b208b8b3b614db15da47304d012b68a role=test-infrastructure -->
## `def test_diff_respects_budget(project: Path)`

Verifies that diff_project respects the budget_usd parameter by limiting documentation generation when funds are insufficient.

- Creates multiple source files to test budget enforcement across files
- Sets an intentionally tiny budget (0.00001 USD) to trigger budget limits
- Asserts that some but not all files are processed when budget is exhausted
<!-- trie:end -->
<!-- trie:section symbol=tests/test_diff:test_cli_sync_dry_run_routes_through_diff fingerprint=010c932914ab38809bb11f22bd06bb023d694dfc73a6ae2319a8b5110c7f2bf6 body_fp=f7daa1b536e3282d69e48e2c389d696b13f0502b38071cfc7cb45f1d1b1e6485 source_ref=6e1055a06b208b8b3b614db15da47304d012b68a role=cli-interface -->
## `def test_cli_sync_dry_run_routes_through_diff(project: Path, monkeypatch: pytest.MonkeyPatch)`

Tests that `trie sync --dry-run` command routes through diff functionality to preview changes without modifying files.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_diff:test_cli_sync_dry_run_no_stale fingerprint=d6f94373a6ce8ad7631f8fb0e92857adf69fbcb9fa419531cb8d56b4ef087435 body_fp=0b7651e19036c36dbd3f755069018734e053c609263baef1e583393b66377350 source_ref=6e1055a06b208b8b3b614db15da47304d012b68a role=cli-interface -->
## `def test_cli_sync_dry_run_no_stale(project: Path, monkeypatch: pytest.MonkeyPatch)`

Tests that CLI sync --dry-run outputs "no stale triefacts" when all documentation is current.
<!-- trie:end -->









