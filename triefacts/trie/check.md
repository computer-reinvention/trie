---
trie_version: 0.3.0
source: trie/check.py
file_fingerprint: 01f5b8105ecd6cdccb350beeda8b73d19d4cb2b377699ac78a5ae0ff5020184a
last_synced_at: '2026-08-02T21:19:27Z'
defines:
- kind: module
  qualified_name: trie/check:__module__
  lines: 1-209
- kind: class
  qualified_name: trie/check:StaleReason
  lines: 18-24
  signature: class StaleReason(StrEnum)
- kind: class
  qualified_name: trie/check:StaleItem
  lines: 28-32
  signature: class StaleItem
- kind: class
  qualified_name: trie/check:CheckResult
  lines: 36-41
  signature: class CheckResult
- kind: method
  qualified_name: trie/check:CheckResult.is_clean
  lines: 40-41
  signature: def is_clean(self) -> bool
- kind: function
  qualified_name: trie/check:_triefact_path_for
  lines: 44-47
  signature: 'def _triefact_path_for(rel_source: str, config: Config) -> str'
- kind: function
  qualified_name: trie/check:check_project
  lines: 50-79
  signature: 'def check_project(*, project_root: Path, config: Config, store: Store | None = None) -> CheckResult'
- kind: function
  qualified_name: trie/check:_check_project_inner
  lines: 82-208
  signature: 'def _check_project_inner( *, project_root: Path, config: Config, _tele: dict, store: Store | None = None ) -> CheckResult'
incoming_refs: 25
outgoing_refs: 9
---
<!-- trie:section symbol=trie/check:__module__ fingerprint=c33905a374e32f0fd9375bd80c1768b3ee3c844280751544dfe534a5f4fa7be9 body_fp=e75d59ec8e0be55d54ce1acd9587d0bf4fd631bb2424d3f9513a7179e684f3a9 source_ref=3027902518aa736256f99f988058880d98ed7383 role=change-detection -->
Detects staleness between source files and their triefact documentation by comparing symbol fingerprints.

- `check_project()` — main entry point that scans all in-scope files and returns drift items
- `StaleReason` — enum of the six types of drift that can occur between code and docs
- `StaleItem` — represents one specific instance of drift with source/triefact paths and reason
- `CheckResult` — container for all drift items found, with `is_clean` property for zero-drift state
<!-- trie:end -->
<!-- trie:section symbol=trie/check:StaleReason fingerprint=b7162ffe7f29cd254fc576ebd54af00f835144adc63c5f9a2d54a96b4f1fec3b body_fp=00fc706a0be35a2709a696dca5aea2ac42c701fd0e61692f87067371fbaf1139 source_ref=b13418772d94c7dea0e494653a1d4aadcca3a1c6 role=change-detection -->
## `class StaleReason(StrEnum)`

Enumeration of reasons why a triefact item is stale or inconsistent with source code.

- `MISSING_TRIEFACT` - source has public symbols but no triefact file exists
- `MISSING_SECTION` - public symbol exists but has no corresponding documentation section
- `STALE_SECTION` - section fingerprint doesn't match current source hash
- `ORPHAN_SECTION` - section exists but the documented symbol was removed
- `TAMPERED_BODY` - section body was manually edited, breaking integrity hash
- `LEGACY_SECTION` - section written by trie ≤ 0.1 without body fingerprint
<!-- trie:end -->
<!-- trie:section symbol=trie/check:StaleItem fingerprint=ae18783ed30cfaf25c1fae63551aab0aeff0994376e794990d7351af538d0108 body_fp=56c15eb37e65e508bbb831afab7ab1ee5d2871148116efc14aad23b75851000d source_ref=b13418772d94c7dea0e494653a1d4aadcca3a1c6 role=change-detection -->
## `class StaleItem`

Represents a single drift detection issue between source code and its triefact documentation.

- `qualified_name`: None for file-level issues (missing triefact), symbol name for symbol-level issues
<!-- trie:end -->
<!-- trie:section symbol=trie/check:CheckResult fingerprint=51653a7d76b12e0701519325bb7218c14d9075f17d4cc3777a9548c6dec10a4f body_fp=ead303de8d68fec0806bb9145d5e160aff63e5f72860c68e95497723e0a2bc70 source_ref=b13418772d94c7dea0e494653a1d4aadcca3a1c6 role=change-detection -->
## `class CheckResult`

Holds the result of checking a project for stale documentation items.

- `items`: List of discovered stale items; empty if project is clean
- `is_clean`: True when no stale items exist
<!-- trie:end -->
<!-- trie:section symbol=trie/check:CheckResult.is_clean fingerprint=ebbc3dee0f4617059834db12a6f442ac8da1450e86eba997049d21c1f3b8da10 body_fp=ed82e87f0986a305fb1dc334c22eb3241a755a25546b286609295294c0f10d86 source_ref=b13418772d94c7dea0e494653a1d4aadcca3a1c6 role=change-detection -->
## `def is_clean(self) -> bool`

CheckResult.is_clean returns True when no stale items were found during verification.
<!-- trie:end -->
<!-- trie:section symbol=trie/check:_triefact_path_for fingerprint=4a1dcef0054474a18efab389b26d7da835bb361c92aaee997af6d5a2473cab49 body_fp=924198afef42b957f87eab20b86ceaad3d0b0c5472fe013f78bedf65299ef13d source_ref=b13418772d94c7dea0e494653a1d4aadcca3a1c6 role=change-detection -->
## `def _triefact_path_for(rel_source: str, config: Config) -> str`

Converts source file path to corresponding triefact markdown file path under configured root directory.
<!-- trie:end -->
<!-- trie:section symbol=trie/check:check_project fingerprint=080565f6299a1c159128bf026f0394c9bc8bb741d9a0ae4c62484269eca13c4b body_fp=38bfdb43be07968be28ca1844686417922c343a93f526eab0c005c1c6322ad46 source_ref=3027902518aa736256f99f988058880d98ed7383 role=domain -->
## `def check_project(*, project_root: Path, config: Config, store: Store | None = None) -> CheckResult`

Compute stale items by comparing each in-scope source file's symbols to its triefact.

- Returns `CheckResult` containing bidirectional drift detection between source code and documentation
- Detects missing triefact files, missing sections, stale sections, orphan sections, tampered bodies, and legacy sections
- `store`: optional content-addressed cache; symbol hashes are read from it only when the file fingerprint matches, falling back to parsing on any mismatch or miss
- Uses fingerprints from triefact sentinels for integrity verification
<!-- trie:end -->
<!-- trie:section symbol=trie/check:_check_project_inner fingerprint=d89f8fe98702a37dff755b59db452db8796dd5d199bde2d8840bfaab1c4c3e77 body_fp=ec16ddddf859e48f9b733d4554ea632760894dd9292c626e420c857fddb5c9a9 source_ref=3027902518aa736256f99f988058880d98ed7383 role=domain -->
## `def _check_project_inner( *, project_root: Path, config: Config, _tele: dict, store: Store | None = None ) -> CheckResult`

Performs bidirectional staleness detection between source symbols and triefact sections, populating telemetry.

- Discovers in-scope files, extracts symbols, and compares with existing triefact sections
- Skips files not indexable by the parser registry before counting or processing them
- Accepts an optional `store` for a content-addressed fast path; bypasses parsing when the file fingerprint matches the store record
- Detects missing triefacts, missing/stale/orphaned sections, tampered bodies, and legacy sections
- Records file counts, store fast-path hit counts, issue counts, and issue breakdown by reason in telemetry dictionary
<!-- trie:end -->