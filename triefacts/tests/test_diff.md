---
trie_version: 0.1.5
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
<!-- trie:section symbol=tests/test_diff:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=4197c295cec71e22894d2c9e50f99741ef1932f46191f01b5068074b9a9a2d4b source_ref=6e1055a06b208b8b3b614db15da47304d012b68a role=test-infrastructure -->
Tests for the diff functionality that compares current source code against existing triefacts and generates unified diffs for changes.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_diff:project fingerprint=cd6f42afcf67cc71ef8f9decc80cf1252526bcf42bc7ac1d0055f21d53a8719b body_fp=17d0d5d8573c58623f1dbe8a91ce33e91be22a9cc6246f5f61381d5796cc371d source_ref=6e1055a06b208b8b3b614db15da47304d012b68a role=test-infrastructure -->
Creates a temporary project directory with trie configuration file and sample Python source file for testing.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_diff:test_diff_returns_empty_when_clean fingerprint=d2a7fa508081814258d613ec8b2872d7afd765927bf7186ab357128ee7f9bf0d body_fp=fd798d684dffd6be1924d0a1b52592fe06c2a4b1fca946aa5479728cb878784f source_ref=6e1055a06b208b8b3b614db15da47304d012b68a role=test-infrastructure -->
Verifies that diff_project returns no diffs when triefacts are up-to-date with source files.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_diff:test_diff_shows_regenerated_content fingerprint=89d814a6af063c4e94a927e1ad9a5d3ba321e11e78109c5408a5c8c3fdc11a86 body_fp=73ff4b8008beed743a15a1c822632205aa79b51183d13a179b0aba587d23a521 source_ref=6e1055a06b208b8b3b614db15da47304d012b68a role=test-infrastructure -->
Verifies diff_project detects stale triefacts and generates preview diffs without modifying live files.

- Syncs v1 triefact, modifies source, then diffs with v2 client
- Asserts unified diff contains both v1 and v2 content
- Confirms preview file exists while canonical file remains unchanged
<!-- trie:end -->
<!-- trie:section symbol=tests/test_diff:test_diff_writes_to_preview_dir fingerprint=6186a6b103b571bb8d221bc104bdbe3c8a225ebb2613b5d5158913e45b95d3e5 body_fp=3d3141ce1f887443b029bfe677f6f81b129b3b93dc28e77298ad1fc5713278da source_ref=6e1055a06b208b8b3b614db15da47304d012b68a role=test-infrastructure -->
Verifies that diff_project writes preview triefacts to `.trie/preview` directory without modifying canonical files.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_diff:test_diff_respects_limit fingerprint=71c42631990c386a9403ab70f96ea8d4074843ec7a0a344e69c56129512ea813 body_fp=caabb2ee1b3e28cb237dbcf955cdf8831ac3f9d63977430a4a26ace7545a5808 source_ref=6e1055a06b208b8b3b614db15da47304d012b68a role=documentation-sync -->
Verifies that `diff_project` respects the `limit` parameter by processing at most the specified number of files.

- Creates 3 Python files but limits processing to 2
- Asserts exactly 2 diffs are generated and at least 1 file is skipped
<!-- trie:end -->
<!-- trie:section symbol=tests/test_diff:test_diff_respects_budget fingerprint=95de6fbbd940c39eb444cde0d455543f20ea4616710b08dff6a0891436f92691 body_fp=33bb41e452ff2caa749ba3364691cab5eb517723c0d90a05ed4fc748599caedb source_ref=6e1055a06b208b8b3b614db15da47304d012b68a role=test-infrastructure -->
Verifies that diff_project respects the budget_usd parameter by limiting documentation generation when funds are insufficient.

- Creates multiple source files to test budget enforcement across files
- Sets an intentionally tiny budget (0.00001 USD) to trigger budget limits
- Asserts that some but not all files are processed when budget is exhausted
<!-- trie:end -->
<!-- trie:section symbol=tests/test_diff:test_cli_sync_dry_run_routes_through_diff fingerprint=010c932914ab38809bb11f22bd06bb023d694dfc73a6ae2319a8b5110c7f2bf6 body_fp=5cf96e26ff212ec125d516c7ea9220eef2fce50cfa6ad7c6cdb8c1058783b8e3 source_ref=6e1055a06b208b8b3b614db15da47304d012b68a role=cli-interface -->
Tests that `trie sync --dry-run` command routes through diff functionality to preview changes without modifying files.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_diff:test_cli_sync_dry_run_no_stale fingerprint=d6f94373a6ce8ad7631f8fb0e92857adf69fbcb9fa419531cb8d56b4ef087435 body_fp=20bd6dfacef9cc477ed01aaf9f7f3bb074f3d997ed126e7362cdaac054f8c792 source_ref=6e1055a06b208b8b3b614db15da47304d012b68a role=cli-interface -->
Tests that CLI sync --dry-run outputs "no stale triefacts" when all documentation is current.
<!-- trie:end -->









