---
trie_version: 0.1.0
source: trie/check.py
file_fingerprint: 043d1bb59ae40d8b67b60cf4403eca1977677098d99470bfa2befdb879aee8ab
last_synced_at: '2026-05-14T17:28:50Z'
defines:
- kind: class
  qualified_name: trie/check:StaleReason
  lines: 13-19
- kind: class
  qualified_name: trie/check:StaleItem
  lines: 23-27
- kind: class
  qualified_name: trie/check:CheckResult
  lines: 31-36
- kind: method
  qualified_name: trie/check:CheckResult.is_clean
  lines: 35-36
- kind: function
  qualified_name: trie/check:check_project
  lines: 45-153
incoming_refs: 18
outgoing_refs: 5
---
<!-- trie:section symbol=trie/check:StaleReason fingerprint=b7162ffe7f29cd254fc576ebd54af00f835144adc63c5f9a2d54a96b4f1fec3b body_fp=4fab4b6d3ea4b45484bd158db0d7bb0c6e0c0d7c8e06a67ca176df7ede28ce0d -->
## `class StaleReason(StrEnum)`

Enumerate all reasons a triefact section or file can be considered stale or invalid.

- `MISSING_TRIEFACT`: source has public symbols but no triefact file exists.
- `MISSING_SECTION`: public symbol exists but has no corresponding section.
- `STALE_SECTION`: section fingerprint doesn't match current source hash.
- `ORPHAN_SECTION`: section exists but its symbol has been removed or renamed.
- `TAMPERED_BODY`: section body hash doesn't match the recorded `body_fp`.
- `LEGACY_SECTION`: section written by trie ≤ 0.1; no `body_fp` to verify.
<!-- trie:end -->

<!-- trie:section symbol=trie/check:StaleItem fingerprint=ae18783ed30cfaf25c1fae63551aab0aeff0994376e794990d7351af538d0108 body_fp=022b6fa1779e576f0782642e3801a64714f15ab5d85b906072f187e4fd3a6884 -->
## `StaleItem(source_path, triefact_path, reason, qualified_name)`

Frozen dataclass representing a single drift finding between a source file and its triefact.

- `source_path`: source-root-relative path to the Python file.
- `triefact_path`: source-root-relative path to the `.md` triefact file.
- `qualified_name`: `None` only for `MISSING_TRIEFACT` (file-level reason).
<!-- trie:end -->

<!-- trie:section symbol=trie/check:CheckResult fingerprint=51653a7d76b12e0701519325bb7218c14d9075f17d4cc3777a9548c6dec10a4f body_fp=fc54936b50704fce2c662bd8e453fb170e4520647a2508e51b732758d9b24cfe -->
## `CheckResult(items: list[StaleItem] = <factory>)`

Aggregate result of a project-wide staleness check.

- `is_clean`: `True` when no stale items were found.
<!-- trie:end -->

<!-- trie:section symbol=trie/check:CheckResult.is_clean fingerprint=ebbc3dee0f4617059834db12a6f442ac8da1450e86eba997049d21c1f3b8da10 body_fp=833c4976e84006f9758485206393915e5bf929deb12b90036710528239e91ff4 -->
## `is_clean -> bool`

Return `True` when no stale items were found.
<!-- trie:end -->

<!-- trie:section symbol=trie/check:check_project fingerprint=bccd1125630b39496b68abc508d2af39df9f1c2204a5ce7a03b449358d6a87f4 body_fp=2982c25a90e711380ce8d96e80f68f53db279f19f028ce0d8723e28b4dd1cd19 -->
## `check_project(*, project_root: Path, config: Config) -> CheckResult`

Compute stale items by comparing each in-scope source file's public symbols to its triefact, bidirectionally.

- `project_root`: resolved to absolute before use
- Returns `CheckResult` whose `items` list is empty when everything is in sync
- Emits `MISSING_TRIEFACT` when a public-symbol file has no triefact at all
- Emits `MISSING_SECTION` / `STALE_SECTION` for Code→Triefact drift
- Emits `ORPHAN_SECTION` for symbols removed from source
- Emits `TAMPERED_BODY` when section body hash mismatches recorded fingerprint
- Emits `LEGACY_SECTION` for sections written by trie ≤ 0.1 with no `body_fp`
<!-- trie:end -->