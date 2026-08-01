---
trie_version: 0.2.1
source: trie/check.py
file_fingerprint: 01f5b8105ecd6cdccb350beeda8b73d19d4cb2b377699ac78a5ae0ff5020184a
last_synced_at: '2026-08-01T01:52:05Z'
defines:
- kind: module
  qualified_name: trie/check:__module__
  lines: 1-209
- kind: class
  qualified_name: trie/check:StaleReason
  lines: 18-24
- kind: class
  qualified_name: trie/check:StaleItem
  lines: 28-32
- kind: class
  qualified_name: trie/check:CheckResult
  lines: 36-41
- kind: method
  qualified_name: trie/check:CheckResult.is_clean
  lines: 40-41
- kind: function
  qualified_name: trie/check:_triefact_path_for
  lines: 44-47
- kind: function
  qualified_name: trie/check:check_project
  lines: 50-79
- kind: function
  qualified_name: trie/check:_check_project_inner
  lines: 82-208
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
<!-- trie:section symbol=trie/check:StaleReason fingerprint=b7162ffe7f29cd254fc576ebd54af00f835144adc63c5f9a2d54a96b4f1fec3b body_fp=039fabb1d907a687d9c2d68930c31d605fc58a36f8429acb27adf82c2d8f78e0 source_ref=b13418772d94c7dea0e494653a1d4aadcca3a1c6 role=change-detection -->
Enumeration of reasons why a triefact item is stale or inconsistent with source code.

- `MISSING_TRIEFACT` - source has public symbols but no triefact file exists
- `MISSING_SECTION` - public symbol exists but has no corresponding documentation section
- `STALE_SECTION` - section fingerprint doesn't match current source hash
- `ORPHAN_SECTION` - section exists but the documented symbol was removed
- `TAMPERED_BODY` - section body was manually edited, breaking integrity hash
- `LEGACY_SECTION` - section written by trie ≤ 0.1 without body fingerprint
<!-- trie:end -->
<!-- trie:section symbol=trie/check:StaleItem fingerprint=ae18783ed30cfaf25c1fae63551aab0aeff0994376e794990d7351af538d0108 body_fp=c86761b1d8418937984c6b750050af1d978b8d8fbea6bf946190d62bf9a300c3 source_ref=b13418772d94c7dea0e494653a1d4aadcca3a1c6 role=change-detection -->
Represents a single drift detection issue between source code and its triefact documentation.

- `qualified_name`: None for file-level issues (missing triefact), symbol name for symbol-level issues
<!-- trie:end -->
<!-- trie:section symbol=trie/check:CheckResult fingerprint=51653a7d76b12e0701519325bb7218c14d9075f17d4cc3777a9548c6dec10a4f body_fp=a233800e58be2fbdfcb8f66f3785cea988a792f3ef12a75d14dbf48daf2f4a06 source_ref=b13418772d94c7dea0e494653a1d4aadcca3a1c6 role=change-detection -->
Holds the result of checking a project for stale documentation items.

- `items`: List of discovered stale items; empty if project is clean
- `is_clean`: True when no stale items exist
<!-- trie:end -->
<!-- trie:section symbol=trie/check:CheckResult.is_clean fingerprint=ebbc3dee0f4617059834db12a6f442ac8da1450e86eba997049d21c1f3b8da10 body_fp=b4c1a57df4e6c42982c261982945d1118859013d7d02c4950cb9f71162ba8e58 source_ref=b13418772d94c7dea0e494653a1d4aadcca3a1c6 role=change-detection -->
CheckResult.is_clean returns True when no stale items were found during verification.
<!-- trie:end -->
<!-- trie:section symbol=trie/check:_triefact_path_for fingerprint=4a1dcef0054474a18efab389b26d7da835bb361c92aaee997af6d5a2473cab49 body_fp=243ae4d1491b85becf398309ea3e1c24d9f59c02c654ca31fcf382332104d7e8 source_ref=b13418772d94c7dea0e494653a1d4aadcca3a1c6 role=change-detection -->
Converts source file path to corresponding triefact markdown file path under configured root directory.
<!-- trie:end -->
<!-- trie:section symbol=trie/check:check_project fingerprint=080565f6299a1c159128bf026f0394c9bc8bb741d9a0ae4c62484269eca13c4b body_fp=1068d3ee93faf9f55243daa2af3b13d39a5a3d303773aff207fa528482f3374c source_ref=3027902518aa736256f99f988058880d98ed7383 role=domain -->
Compute stale items by comparing each in-scope source file's symbols to its triefact.

- Returns `CheckResult` containing bidirectional drift detection between source code and documentation
- Detects missing triefact files, missing sections, stale sections, orphan sections, tampered bodies, and legacy sections
- `store`: optional content-addressed cache; symbol hashes are read from it only when the file fingerprint matches, falling back to parsing on any mismatch or miss
- Uses fingerprints from triefact sentinels for integrity verification
<!-- trie:end -->
<!-- trie:section symbol=trie/check:_check_project_inner fingerprint=d89f8fe98702a37dff755b59db452db8796dd5d199bde2d8840bfaab1c4c3e77 body_fp=c21ff27c8b0e4cc7ec8cf78947b83e36d9df38e3769273df8714cebcaceeba49 source_ref=3027902518aa736256f99f988058880d98ed7383 role=domain -->
Performs bidirectional staleness detection between source symbols and triefact sections, populating telemetry.

- Discovers in-scope files, extracts symbols, and compares with existing triefact sections
- Skips files not indexable by the parser registry before counting or processing them
- Accepts an optional `store` for a content-addressed fast path; bypasses parsing when the file fingerprint matches the store record
- Detects missing triefacts, missing/stale/orphaned sections, tampered bodies, and legacy sections
- Records file counts, store fast-path hit counts, issue counts, and issue breakdown by reason in telemetry dictionary
<!-- trie:end -->