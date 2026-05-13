---
trie_version: 0.1.0
source: trie/check.py
file_fingerprint: 043d1bb59ae40d8b67b60cf4403eca1977677098d99470bfa2befdb879aee8ab
last_synced_at: '2026-05-12T18:32:17Z'
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
<!-- trie:section symbol=trie/check:StaleReason fingerprint=b7162ffe7f29cd254fc576ebd54af00f835144adc63c5f9a2d54a96b4f1fec3b body_fp=5dfe4769e3de203b5f40698c6f7894e6ee2eb282eabd04d99985b2ae6e4fcf72 -->
## `class StaleReason(StrEnum)`

Enumerate all reasons a triefact section or file can be considered stale.

- `MISSING_TRIEFACT`: source has public symbols but no triefact file exists.
- `MISSING_SECTION`: public symbol present but no corresponding section.
- `STALE_SECTION`: section fingerprint does not match current source hash.
- `ORPHAN_SECTION`: section exists but its symbol has been removed or renamed.
- `TAMPERED_BODY`: section body hash does not match recorded `body_fp`.
- `LEGACY_SECTION`: section written by trie ≤ 0.1; no `body_fp` recorded.
<!-- trie:end -->

<!-- trie:section symbol=trie/check:StaleItem fingerprint=ae18783ed30cfaf25c1fae63551aab0aeff0994376e794990d7351af538d0108 body_fp=ad6ccfa4da43ffbe3717e80feede3e3c5ad91f15115af0bc0afa768287a45867 -->
## `StaleItem(source_path, triefact_path, reason, qualified_name)`

Frozen dataclass representing a single drift finding between a source file and its triefact.

- `source_path`: source-root-relative path to the Python file.
- `triefact_path`: source-root-relative path to the `.md` triefact.
- `qualified_name`: `None` for `MISSING_TRIEFACT`; symbol name otherwise.
<!-- trie:end -->

<!-- trie:section symbol=trie/check:CheckResult fingerprint=51653a7d76b12e0701519325bb7218c14d9075f17d4cc3777a9548c6dec10a4f body_fp=868bc25812e20a9f19938a46d679ac97c8c0a6775c36ab2373f16c16d7886491 -->
## `CheckResult(items: list[StaleItem] = field(default_factory=list))`

Immutable container for all stale items found during a project check.

- `is_clean`: returns `True` when `items` is empty.
<!-- trie:end -->

<!-- trie:section symbol=trie/check:CheckResult.is_clean fingerprint=ebbc3dee0f4617059834db12a6f442ac8da1450e86eba997049d21c1f3b8da10 body_fp=833c4976e84006f9758485206393915e5bf929deb12b90036710528239e91ff4 -->
## `is_clean -> bool`

Return `True` when no stale items were found.
<!-- trie:end -->

<!-- trie:section symbol=trie/check:check_project fingerprint=bccd1125630b39496b68abc508d2af39df9f1c2204a5ce7a03b449358d6a87f4 body_fp=367513c98f545852c66097c31f3a4a76bcda9c9500cb696ec25168b2377b25e7 -->
## `check_project(*, project_root: Path, config: Config) -> CheckResult`

Compute stale items by comparing each in-scope source file's public symbols to its triefact file, bidirectionally.

- `project_root`: resolved to absolute before use.
- Returns `CheckResult` with one `StaleItem` per drift instance found.
- Emits `MISSING_TRIEFACT` when a file has public symbols but no triefact exists.
- Emits `MISSING_SECTION` / `STALE_SECTION` for symbol-level Code→Triefact drift.
- Emits `ORPHAN_SECTION` when a section's symbol no longer exists in source.
- Emits `TAMPERED_BODY` when section content diverges from its recorded fingerprint.
- Emits `LEGACY_SECTION` for sections written by trie ≤ 0.1 lacking a body fingerprint.
<!-- trie:end -->