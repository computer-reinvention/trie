---
trie_version: 0.1.5
source: trie/check.py
file_fingerprint: 7f06c7053f40e5352b290eaab4c216f06e376680c60d9886afcf46daa647c6aa
last_synced_at: '2026-06-06T14:18:59Z'
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
incoming_refs: 23
outgoing_refs: 6
---
<!-- trie:section symbol=trie/check:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=e75d59ec8e0be55d54ce1acd9587d0bf4fd631bb2424d3f9513a7179e684f3a9 source_ref=b13418772d94c7dea0e494653a1d4aadcca3a1c6 role=change-detection -->
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
<!-- trie:section symbol=trie/check:check_project fingerprint=71986a167d15fdde338406e22b9dab333730ee7e600b59d1f9940206c6f5333f body_fp=f6dc9fb611d7299dd41290bb391c2293f34b9abd26f4b6d2b88fd87eb7b20fa5 source_ref=b13418772d94c7dea0e494653a1d4aadcca3a1c6 role=change-detection -->
Compute stale items by comparing each in-scope source file's symbols to its triefact.

- Returns `CheckResult` containing bidirectional drift detection between source code and documentation
- Detects missing triefact files, missing sections, stale sections, orphan sections, tampered bodies, and legacy sections
- Uses fingerprints from triefact sentinels for integrity verification without database access
<!-- trie:end -->
<!-- trie:section symbol=trie/check:_check_project_inner fingerprint=43b2ccab358f3cca3c315d2d842d841287809a0a13c40e980ba1e1b5498e925e body_fp=c3c2f2c170543ef017cb1bf035939e0aeb6262e25dd28dc74777749cd6641005 source_ref=b13418772d94c7dea0e494653a1d4aadcca3a1c6 role=domain -->
Performs bidirectional staleness detection between source symbols and triefact sections, populating telemetry.

- Discovers in-scope files, extracts symbols, and compares with existing triefact sections
- Detects missing triefacts, missing/stale/orphaned sections, tampered bodies, and legacy sections
- Records file counts, issue counts, and issue breakdown by reason in telemetry dictionary
<!-- trie:end -->