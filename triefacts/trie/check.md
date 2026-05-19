---
trie_version: 0.1.2
source: trie/check.py
file_fingerprint: 7f06c7053f40e5352b290eaab4c216f06e376680c60d9886afcf46daa647c6aa
last_synced_at: '2026-05-19T15:19:44Z'
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
incoming_refs: 21
outgoing_refs: 6
---
<!-- trie:section symbol=trie/check:StaleReason fingerprint=b7162ffe7f29cd254fc576ebd54af00f835144adc63c5f9a2d54a96b4f1fec3b body_fp=42e7454a4d73e396f5fd5e68d5a922cfcc0cbdca908c2351ec109fb8a286e761 source_ref=85ed6191c067f50c30ed25f64e46e5b61ce37465 -->
## `class StaleReason(StrEnum)`

Enumerate all reasons a triefact section or file can be considered stale.

- `MISSING_TRIEFACT`: source has public symbols but no triefact file exists.
- `MISSING_SECTION`: public symbol present but no matching section found.
- `STALE_SECTION`: section fingerprint differs from current source hash.
- `ORPHAN_SECTION`: section exists for a symbol that no longer exists.
- `TAMPERED_BODY`: section body hash differs from recorded `body_fp`.
- `LEGACY_SECTION`: section written by trie ≤ 0.1, no `body_fp` recorded.
<!-- trie:end -->

<!-- trie:section symbol=trie/check:StaleItem fingerprint=ae18783ed30cfaf25c1fae63551aab0aeff0994376e794990d7351af538d0108 body_fp=c7af6713ff824220659adcbd0f033e961fadec3a55651f8a7f8a0d5ddeee9f47 source_ref=85ed6191c067f50c30ed25f64e46e5b61ce37465 -->
## `StaleItem(source_path, triefact_path, reason, qualified_name)`

Frozen dataclass representing a single drift incident between a source file and its triefact.

- `source_path`: source-root-relative path to the Python file.
- `triefact_path`: source-root-relative path to the `.md` triefact.
- `qualified_name`: `None` only for `MISSING_TRIEFACT` reason.
<!-- trie:end -->

<!-- trie:section symbol=trie/check:CheckResult fingerprint=51653a7d76b12e0701519325bb7218c14d9075f17d4cc3777a9548c6dec10a4f body_fp=bacc2c1517261d5a43145980d54a6414763559036a79c6afed85a07884b94152 source_ref=85ed6191c067f50c30ed25f64e46e5b61ce37465 -->
## `CheckResult(items: list[StaleItem] = field(default_factory=list))`

Immutable container for all stale items found during a project check.

- `is_clean`: `True` when `items` is empty.
<!-- trie:end -->

<!-- trie:section symbol=trie/check:CheckResult.is_clean fingerprint=ebbc3dee0f4617059834db12a6f442ac8da1450e86eba997049d21c1f3b8da10 body_fp=833c4976e84006f9758485206393915e5bf929deb12b90036710528239e91ff4 source_ref=85ed6191c067f50c30ed25f64e46e5b61ce37465 -->
## `is_clean -> bool`

Return `True` when no stale items were found.
<!-- trie:end -->

<!-- trie:section symbol=trie/check:check_project fingerprint=71986a167d15fdde338406e22b9dab333730ee7e600b59d1f9940206c6f5333f body_fp=f573f1fad330b03d03211f73c36b675c4b28f55db285b7dcc20ca1a0449942c5 source_ref=85ed6191c067f50c30ed25f64e46e5b61ce37465 -->
## `check_project(*, project_root: Path, config: Config) -> CheckResult`

Compute stale items by comparing each in-scope source file's symbols to its triefact file.

- Covers both Code→Triefact and Triefact→Code drift directions.
- Reads no database; uses source files and triefact sentinel fingerprints only.
<!-- trie:end -->

<!-- trie:section symbol=trie/check:_triefact_path_for fingerprint=4a1dcef0054474a18efab389b26d7da835bb361c92aaee997af6d5a2473cab49 body_fp=1b60b87ebb590991b0c281dcd91303b5358f6df9730d8798e91db6cc703acd5b source_ref=b13418772d94c7dea0e494653a1d4aadcca3a1c6 -->
## `_triefact_path_for(rel_source: str, config: Config) -> str`

Map a source-root-relative `.py` path to its corresponding source-root-relative `.md` triefact path.
<!-- trie:end -->

<!-- trie:section symbol=trie/check:_check_project_inner fingerprint=43b2ccab358f3cca3c315d2d842d841287809a0a13c40e980ba1e1b5498e925e body_fp=eec138a20699633967fdd3d2affe9c7e8ab72c7bcdccf5a7aeb8c433005cb610 source_ref=b13418772d94c7dea0e494653a1d4aadcca3a1c6 -->
## `_check_project_inner(*, project_root: Path, config: Config, _tele: dict) -> CheckResult`

Execute the full bidirectional staleness scan and populate telemetry in `_tele`.

- `_tele`: mutable dict updated with `files_checked`, `issues_found`, `issues_by_reason`.
<!-- trie:end -->

<!-- trie:section symbol=trie/check:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=3bd5bb84bb59d70358aa5b064d19f8014389b0e06e3420bed0e416797a499f4a source_ref=b13418772d94c7dea0e494653a1d4aadcca3a1c6 -->
## `check`

Detect drift between Python source symbols and their triefact documentation sections.

- `StaleReason`: six-variant enum covering all forward and reverse drift cases
- `StaleItem`: single drift record with source path, triefact path, reason, and optional symbol name
- `CheckResult`: aggregates `StaleItem` list; `is_clean` is `True` when no drift found
- `check_project`: entry point; wraps telemetry around the inner check loop
- `_check_project_inner`: walks discovered files, compares symbols to sections bidirectionally
<!-- trie:end -->