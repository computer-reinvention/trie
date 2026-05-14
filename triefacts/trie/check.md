---
trie_version: 0.1.0
source: trie/check.py
file_fingerprint: 21ddc33581d7cdf8967f5ca49c870251e5859b00cbf5e80f2243f0807e8fe567
last_synced_at: '2026-05-14T18:30:10Z'
defines:
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
  qualified_name: trie/check:check_project
  lines: 46-63
incoming_refs: 18
outgoing_refs: 5
---
<!-- trie:section symbol=trie/check:StaleReason fingerprint=b7162ffe7f29cd254fc576ebd54af00f835144adc63c5f9a2d54a96b4f1fec3b body_fp=828b224284bab2e6e18af0467a5fcd38397b633384226a7baae1386a8f419341 -->
## `class StaleReason(StrEnum)`

Enumerate all reasons a triefact section or file can be considered stale or invalid.

- `MISSING_TRIEFACT`: source has public symbols but no triefact file exists.
- `MISSING_SECTION`: public symbol present but no matching section in triefact.
- `STALE_SECTION`: section fingerprint differs from current source hash.
- `ORPHAN_SECTION`: section exists for a symbol that no longer exists.
- `TAMPERED_BODY`: section body hash differs from recorded `body_fp`.
- `LEGACY_SECTION`: section written by trie ≤ 0.1; no `body_fp` present.
<!-- trie:end -->

<!-- trie:section symbol=trie/check:StaleItem fingerprint=ae18783ed30cfaf25c1fae63551aab0aeff0994376e794990d7351af538d0108 body_fp=940d615a2fb4984786cb4efaa950f89adcb703fe17a5b78368cc4a8688511dc2 -->
## `StaleItem(source_path: str, triefact_path: str, reason: StaleReason, qualified_name: str | None)`

Frozen dataclass representing a single detected drift between a source file and its triefact.

- `source_path`: source-root-relative path to the Python file.
- `triefact_path`: source-root-relative path to the `.md` triefact file.
- `qualified_name`: `None` only for `MISSING_TRIEFACT`; symbol name otherwise.
<!-- trie:end -->

<!-- trie:section symbol=trie/check:CheckResult fingerprint=51653a7d76b12e0701519325bb7218c14d9075f17d4cc3777a9548c6dec10a4f body_fp=fdf428401be19a785548c93737735d52761f5bf74b685dda09f4435bcaba7289 -->
## `CheckResult(items: list[StaleItem] = field(default_factory=list))`

Frozen dataclass holding all stale items found during a project check.

- `is_clean`: returns `True` when `items` is empty.
<!-- trie:end -->

<!-- trie:section symbol=trie/check:CheckResult.is_clean fingerprint=ebbc3dee0f4617059834db12a6f442ac8da1450e86eba997049d21c1f3b8da10 body_fp=969a0c953cbffe37743fab11a7e0aa75fe2b737e0839545b7091977c47dc43fa -->
## `is_clean -> bool`

Return `True` when no stale items exist.
<!-- trie:end -->

<!-- trie:section symbol=trie/check:check_project fingerprint=71986a167d15fdde338406e22b9dab333730ee7e600b59d1f9940206c6f5333f body_fp=91e9d086c2031dca05e09a92bc5359621cb277174ac382f8dcf126f4119cc25e -->
## `check_project(*, project_root: Path, config: Config) -> CheckResult`

Compute stale items by comparing each in-scope source file's symbols to its triefact file.

- Covers both Code→Triefact and Triefact→Code drift directions.
- No database access; uses source files and sentinel fingerprints as truth.
- Returns a `CheckResult` whose `items` list is empty when everything is clean.
<!-- trie:end -->