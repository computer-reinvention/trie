---
trie_version: 0.1.5
source: trie/check.py
file_fingerprint: 7f06c7053f40e5352b290eaab4c216f06e376680c60d9886afcf46daa647c6aa
last_synced_at: '2026-05-28T15:00:15Z'
defines:
- kind: module
  qualified_name: trie/check:__module__
  lines: 1-173
- kind: class
  qualified_name: trie/check:StaleReason
  lines: 14-20
- kind: class
  qualified_name: trie/check:StaleItem
  lines: 24-28
- kind: class
  qualified_name: trie/check:CheckResult
  lines: 32-37
- kind: method
  qualified_name: trie/check:CheckResult.is_clean
  lines: 36-37
- kind: function
  qualified_name: trie/check:_triefact_path_for
  lines: 40-43
- kind: function
  qualified_name: trie/check:check_project
  lines: 46-63
- kind: function
  qualified_name: trie/check:_check_project_inner
  lines: 66-172
incoming_refs: 22
outgoing_refs: 6
---
<!-- trie:section symbol=trie/check:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=9308fc81b074da1c432f301abc04ad9f4b2e6861840cc9de7a3586d1477f641a source_ref=b13418772d94c7dea0e494653a1d4aadcca3a1c6 -->
## `trie/check`

Detect drift between Python source symbols and their corresponding triefact documentation sections.

- `StaleReason`: enumeration of six distinct drift conditions
- `StaleItem`: single drift finding, source-root-relative paths
- `CheckResult`: aggregated findings with a clean-state shortcut
- `check_project`: entry point; no DB access, fingerprint-based only
<!-- trie:end -->
<!-- trie:section symbol=trie/check:StaleReason fingerprint=b7162ffe7f29cd254fc576ebd54af00f835144adc63c5f9a2d54a96b4f1fec3b body_fp=0f59c99786213d3ace834e06ffc938ba41ca0277a1f138b5ecbbe01b94b16c16 source_ref=b13418772d94c7dea0e494653a1d4aadcca3a1c6 -->
## `StaleReason`

Enumerate all reasons a triefact section or file can be considered stale.

- `MISSING_TRIEFACT`: source has symbols but no triefact file exists.
- `MISSING_SECTION`: symbol present in source, no matching section in triefact.
- `STALE_SECTION`: section fingerprint differs from current source hash.
- `ORPHAN_SECTION`: section exists but its symbol has been removed or renamed.
- `TAMPERED_BODY`: section body hash doesn't match the recorded `body_fp`.
- `LEGACY_SECTION`: section written by trie ≤ 0.1; lacks `body_fp` for integrity checks.
<!-- trie:end -->
<!-- trie:section symbol=trie/check:StaleItem fingerprint=ae18783ed30cfaf25c1fae63551aab0aeff0994376e794990d7351af538d0108 body_fp=5750b52d2ddc4900f6eb54b024947c7f26dc70bccba1a181263346cc8674ba7b source_ref=b13418772d94c7dea0e494653a1d4aadcca3a1c6 -->
## `StaleItem(source_path, triefact_path, reason, qualified_name)`

Immutable record describing a single staleness finding for a source/triefact pair.

- `source_path`: source-root-relative path to the Python source file.
- `triefact_path`: source-root-relative path to the corresponding triefact file.
- `qualified_name`: `None` for `MISSING_TRIEFACT`; symbol name for all other reasons.
<!-- trie:end -->
<!-- trie:section symbol=trie/check:CheckResult fingerprint=51653a7d76b12e0701519325bb7218c14d9075f17d4cc3777a9548c6dec10a4f body_fp=42485215376c7aa4fb964f017562b8f72f2483befbfb7239c8cbdc8f91ecd343 source_ref=b13418772d94c7dea0e494653a1d4aadcca3a1c6 -->
## `CheckResult`

Immutable result of a project-wide staleness check.

- `items`: all detected stale items; empty list means no drift.
- `is_clean`: `True` when `items` is empty.
<!-- trie:end -->
<!-- trie:section symbol=trie/check:CheckResult.is_clean fingerprint=ebbc3dee0f4617059834db12a6f442ac8da1450e86eba997049d21c1f3b8da10 body_fp=f3f5ce2a362094705bd37e098b640d66d14edf0888842074f87c95500be4cef1 source_ref=b13418772d94c7dea0e494653a1d4aadcca3a1c6 -->
## `CheckResult.is_clean -> bool`

`True` when the `CheckResult` contains no stale items.
<!-- trie:end -->
<!-- trie:section symbol=trie/check:_triefact_path_for fingerprint=4a1dcef0054474a18efab389b26d7da835bb361c92aaee997af6d5a2473cab49 body_fp=97cf360f66b7a434a5a658a4cf48524599a88a34dcb8eccc3e8a4718352a527f source_ref=b13418772d94c7dea0e494653a1d4aadcca3a1c6 -->
## `_triefact_path_for(rel_source: str, config: Config) -> str`

Convert a source-root-relative `.py` path to its corresponding `.md` triefact path.
<!-- trie:end -->
<!-- trie:section symbol=trie/check:check_project fingerprint=71986a167d15fdde338406e22b9dab333730ee7e600b59d1f9940206c6f5333f body_fp=55f71708407a950fbcac918f0b2a6937989d3ece6770dc197daa19cb8c3470c9 source_ref=b13418772d94c7dea0e494653a1d4aadcca3a1c6 -->
## `check_project(*, project_root: Path, config: Config) -> CheckResult`

Compute stale items by comparing every in-scope source file's symbols to its triefact, covering both drift directions.

- `project_root`: resolved to an absolute path before scanning.
- Returns a `CheckResult` whose `items` list is empty when everything is in sync.
<!-- trie:end -->
<!-- trie:section symbol=trie/check:_check_project_inner fingerprint=43b2ccab358f3cca3c315d2d842d841287809a0a13c40e980ba1e1b5498e925e body_fp=7430cb6db54005aefcde54106989e2df781a3fe4c2901160685d69735c458146 source_ref=b13418772d94c7dea0e494653a1d4aadcca3a1c6 -->
## `_check_project_inner(*, project_root: Path, config: Config, _tele: dict) -> CheckResult`

Perform the full bidirectional drift check and populate telemetry in `_tele`.

- `_tele`: mutated in-place with `files_checked`, `issues_found`, and `issues_by_reason`.
<!-- trie:end -->