---
trie_version: 0.1.0
source: trie/check.py
file_fingerprint: 043d1bb59ae40d8b67b60cf4403eca1977677098d99470bfa2befdb879aee8ab
last_synced_at: '2026-05-14T17:51:41Z'
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
<!-- trie:section symbol=trie/check:StaleReason fingerprint=b7162ffe7f29cd254fc576ebd54af00f835144adc63c5f9a2d54a96b4f1fec3b body_fp=193cb9aa59a7fd70e9100715a9b7385c765a8f47ce48cd7601c86f1482334eb5 -->
## `class StaleReason(StrEnum)`

Enumerate all reasons a triefact section or file can be considered stale.

- `MISSING_TRIEFACT`: source has public symbols but no triefact file exists.
- `MISSING_SECTION`: public symbol present but no matching section in triefact.
- `STALE_SECTION`: section fingerprint doesn't match current source hash.
- `ORPHAN_SECTION`: section exists but its symbol has been removed or renamed.
- `TAMPERED_BODY`: section body hash doesn't match recorded `body_fp`.
- `LEGACY_SECTION`: section written by trie ≤ 0.1 with no `body_fp` field.
<!-- trie:end -->

<!-- trie:section symbol=trie/check:StaleItem fingerprint=ae18783ed30cfaf25c1fae63551aab0aeff0994376e794990d7351af538d0108 body_fp=095d30482ab3b8c7c9399a535fd9d1685ec512c3a765b2b2871a8ca112313e9b -->
## `StaleItem(source_path: str, triefact_path: str, reason: StaleReason, qualified_name: str | None)`

Frozen dataclass representing a single detected staleness issue for a source/triefact pair.

- `source_path`: source-root-relative path to the Python file.
- `triefact_path`: source-root-relative path to the `.md` triefact file.
- `qualified_name`: `None` only for `MISSING_TRIEFACT`; otherwise the offending symbol.
<!-- trie:end -->

<!-- trie:section symbol=trie/check:CheckResult fingerprint=51653a7d76b12e0701519325bb7218c14d9075f17d4cc3777a9548c6dec10a4f body_fp=4743630f5bde915e8cffcd666df90158cd592be8531128084a36960b186abb9e -->
## `CheckResult(items: list[StaleItem] = field(default_factory=list))`

Immutable container for all stale items found during a project check.

- `is_clean`: `True` when `items` is empty, indicating no drift detected.
<!-- trie:end -->

<!-- trie:section symbol=trie/check:CheckResult.is_clean fingerprint=ebbc3dee0f4617059834db12a6f442ac8da1450e86eba997049d21c1f3b8da10 body_fp=833c4976e84006f9758485206393915e5bf929deb12b90036710528239e91ff4 -->
## `is_clean -> bool`

Return `True` when no stale items were found.
<!-- trie:end -->

<!-- trie:section symbol=trie/check:check_project fingerprint=bccd1125630b39496b68abc508d2af39df9f1c2204a5ce7a03b449358d6a87f4 body_fp=00a0165eb8dee1edde2d5e7079522b23ead7f061dd5f94eb43a036c9b1589a89 -->
## `check_project(*, project_root: Path, config: Config) -> CheckResult`

Compute stale items by comparing each in-scope source file's public symbols to its triefact file.

- Covers both drift directions: Code→Triefact and Triefact→Code.
- `MISSING_TRIEFACT`: public symbols exist but no triefact file found.
- `MISSING_SECTION`: public symbol has no matching section in the triefact.
- `STALE_SECTION`: section fingerprint doesn't match current source hash.
- `ORPHAN_SECTION`: section exists for a symbol that no longer exists.
- `TAMPERED_BODY`: section body hash doesn't match recorded body fingerprint.
- `LEGACY_SECTION`: section written by trie ≤ 0.1 with no body fingerprint.
<!-- trie:end -->