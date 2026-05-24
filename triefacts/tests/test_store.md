---
trie_version: 0.1.2
source: tests/test_store.py
file_fingerprint: afbabafdabc5fae36b75de2bc15153adc4a70c97d1b0bf6cf9079460d646fab0
last_synced_at: '2026-05-23T23:52:49Z'
defines:
- kind: module
  qualified_name: tests/test_store:__module__
  lines: 1-131
- kind: function
  qualified_name: tests/test_store:store
  lines: 12-15
- kind: function
  qualified_name: tests/test_store:test_schema_version_recorded
  lines: 18-20
- kind: function
  qualified_name: tests/test_store:test_upsert_and_get_file
  lines: 23-27
- kind: function
  qualified_name: tests/test_store:test_upsert_overwrites_existing
  lines: 30-36
- kind: function
  qualified_name: tests/test_store:test_list_files_sorted
  lines: 39-43
- kind: function
  qualified_name: tests/test_store:test_delete_file_cascades_symbols
  lines: 46-56
- kind: function
  qualified_name: tests/test_store:test_replace_file_symbols_replaces_atomically
  lines: 59-75
- kind: function
  qualified_name: tests/test_store:test_count_symbols_public_only
  lines: 78-88
- kind: function
  qualified_name: tests/test_store:test_file_stats
  lines: 91-111
- kind: function
  qualified_name: tests/test_store:test_context_manager_closes
  lines: 114-120
- kind: function
  qualified_name: tests/test_store:test_transaction_rolls_back_on_error
  lines: 123-130
incoming_refs: 0
outgoing_refs: 8
---
<!-- trie:section symbol=tests/test_store:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=a6901984a3b040754290edbe55e41d38bb5844812bf0df88f1c6dd700b97d6b4 source_ref=839b1a45c99e07b791659b6edeac04dc61a4910c -->
## `tests/test_store`

Integration tests for `Store`: schema versioning, file upsert/delete, symbol replacement, stats, context-manager behaviour, and transaction rollback.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:store fingerprint=c5420fff5b078bc5c2e95aff6471bdee364032edad5dee901f70ebfc07cd85eb body_fp=65140b3fa7b99be6156acb6b0394918934deecb76dc7e80b686c720d3742c976 source_ref=839b1a45c99e07b791659b6edeac04dc61a4910c -->
## `store(tmp_path: Path) -> Store`

Pytest fixture that yields an open `Store` backed by a temporary database, then closes it.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_schema_version_recorded fingerprint=2581df1e7e37dd6979078449702b4844298aace7f2e4a4facfc5eb87a6766f78 body_fp=6f178b0c763d064d63683c2dbb3bd02ecec15ffd88e100ee70201a3346e12f74 source_ref=839b1a45c99e07b791659b6edeac04dc61a4910c -->
## `test_schema_version_recorded(store: Store)`

Assert that the `schema_version` table contains the expected `SCHEMA_VERSION` constant after `Store` initialisation.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_upsert_and_get_file fingerprint=f3b58b4e3b9159727ab6287bf2302a550f35296a8d1eb39f62d33d4cdea3b959 body_fp=e59d2287f5aedb8bbbb5c218360737ed8eb6bae963e995d713aee285a90cdccd source_ref=839b1a45c99e07b791659b6edeac04dc61a4910c -->
## `test_upsert_and_get_file(store: Store)`

Verify that `Store.upsert_file` persists a `FileRecord` retrievable via `get_file`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_upsert_overwrites_existing fingerprint=9db6492c71548100dcb1641379202911793ae4f436b4e9aaa3c7c555be8aa398 body_fp=eb371d4971bc6a274b8e685db154170e30ebbec4554803ab282eb7a8ca4a5f3d source_ref=839b1a45c99e07b791659b6edeac04dc61a4910c -->
## `test_upsert_overwrites_existing(store: Store)`

Verify that a second `upsert_file` call replaces fingerprint and timestamp of an existing file record.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_list_files_sorted fingerprint=2527e7f0347a9473606b15234fc7a71b2b0d4c8048a320f4f01796e0d79debef body_fp=8007ecddb50bf65167e6df384aee6e1620c604ce786eef2ea137ec7f3cd2835d source_ref=839b1a45c99e07b791659b6edeac04dc61a4910c -->
## `test_list_files_sorted(store: Store)`

Assert that `Store.list_files()` returns files ordered alphabetically by path.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_delete_file_cascades_symbols fingerprint=f7eddba29276842b42c4218e2c41613b855a0ec86a39fdf3a1e28db3dba2d5fb body_fp=2b7fdaf2a27a604427f2651b6f4474cf4931d3e2d1158058591aea1fc6fe4294 source_ref=839b1a45c99e07b791659b6edeac04dc61a4910c -->
## `test_delete_file_cascades_symbols(store: Store, tmp_path: Path)`

Assert that deleting a file from the `Store` also removes all its associated symbols.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_replace_file_symbols_replaces_atomically fingerprint=eba7fb5f4d931588f59a8eb9248ec60869b10664d0c8d0fdbcf37929d3123559 body_fp=ba837735ebd2e00eee1191a8b028180f35a280913235f3d5ac7ffeb358648c67 source_ref=839b1a45c99e07b791659b6edeac04dc61a4910c -->
## `test_replace_file_symbols_replaces_atomically(store: Store, tmp_path: Path)`

Verify `Store.replace_file_symbols` updates symbol counts correctly and tolerates repeated upserts without violating unique constraints.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_count_symbols_public_only fingerprint=222c17ff3cda50356d07214099dc6b04be5f340bf11bbff7957250e3a2f53cdd body_fp=5795d0baacc566892351f394c8461266cc81eeebfcd390dbba9bf7eabd309d35 source_ref=839b1a45c99e07b791659b6edeac04dc61a4910c -->
## `test_count_symbols_public_only(store: Store, tmp_path: Path)`

Verify that `Store.count_symbols` with `public_only=True` counts only non-underscore-prefixed top-level symbols.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_file_stats fingerprint=d9c36a2293bcc3553bccb18227e7f62b1745bdcce0cc7886a4a0f4b99c31d6a0 body_fp=ff2f4c442361eb42d7bdf9c515fafa94ac6c49bc4690908192b22e28618ea690 source_ref=839b1a45c99e07b791659b6edeac04dc61a4910c -->
## `test_file_stats(store: Store, tmp_path: Path)`

Verify `Store.file_stats()` returns correct `total_symbols` and `public_symbols` counts per file.

- `public_symbols` equals `total_symbols` because all parser-surfaced symbols are treated as public.
- A file with no symbols reports zero for both fields.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_context_manager_closes fingerprint=65d7ddf8931633bad6022ea097f4d7205028b3ba29b009cc72ff71f01b4d0c14 body_fp=390db287d2615230f33b2f4e0c5570402f014ce7eb0dc5785c253d7b5c45dedb source_ref=839b1a45c99e07b791659b6edeac04dc61a4910c -->
## `test_context_manager_closes(tmp_path: Path)`

Verify that `Store` used as a context manager closes cleanly and persists data readable by a subsequent `Store` instance.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_transaction_rolls_back_on_error fingerprint=8137c9af2218b70b56eb96a6ae7becf72e2277f0977f03c442cf700b067d7e04 body_fp=e56d0e44c1a1f4600c47641c60f57dfa4396aad8003896dfe1b0a2e2844008e4 source_ref=839b1a45c99e07b791659b6edeac04dc61a4910c -->
## `test_transaction_rolls_back_on_error(store: Store)`

Verify that `Store.transaction()` rolls back all changes when an exception is raised mid-transaction.
<!-- trie:end -->