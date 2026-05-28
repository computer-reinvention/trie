---
trie_version: 0.1.5
source: tests/test_store.py
file_fingerprint: 5b0ca061e713690a8161eac959468358abf65b6641c42e59a55b34262d85bacc
last_synced_at: '2026-05-28T01:37:44Z'
defines:
- kind: module
  qualified_name: tests/test_store:__module__
  lines: 1-310
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
- kind: function
  qualified_name: tests/test_store:test_patches_table_exists
  lines: 136-141
- kind: function
  qualified_name: tests/test_store:test_add_patch_creates_row
  lines: 144-152
- kind: function
  qualified_name: tests/test_store:test_add_patch_unknown_qname_raises
  lines: 155-157
- kind: function
  qualified_name: tests/test_store:test_get_patches_for_qname
  lines: 160-173
- kind: function
  qualified_name: tests/test_store:test_get_patches_for_unknown_qname_returns_empty
  lines: 176-177
- kind: function
  qualified_name: tests/test_store:test_get_all_patches_grouped
  lines: 180-193
- kind: function
  qualified_name: tests/test_store:test_patch_count_for_symbol
  lines: 196-207
- kind: function
  qualified_name: tests/test_store:test_delete_patches_by_qname
  lines: 210-220
- kind: function
  qualified_name: tests/test_store:test_delete_patches_all
  lines: 223-233
- kind: function
  qualified_name: tests/test_store:test_delete_patches_by_session
  lines: 236-249
- kind: function
  qualified_name: tests/test_store:test_get_patched_qnames
  lines: 252-261
- kind: function
  qualified_name: tests/test_store:test_get_symbol_detail_includes_patches
  lines: 264-281
- kind: function
  qualified_name: tests/test_store:test_grep_symbols_includes_patch_count
  lines: 284-296
- kind: function
  qualified_name: tests/test_store:test_patches_cascaded_on_symbol_delete
  lines: 299-309
incoming_refs: 0
outgoing_refs: 19
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
<!-- trie:section symbol=tests/test_store:test_patches_table_exists fingerprint=39a2650346d0847b44524744d583f1e3d653872fab888dde254d29ee4774f7c5 body_fp=479d8f437e11f6db4ba00145f8165ce1669c657e5eb6603ab3f5b9ee02a85d36 source_ref=a95486d535aed1c6b87b5026c7d31274c719666f -->
## `test_patches_table_exists(store: Store)`

Assert that the `patches` table is created by `SCHEMA_SQL` during `Store` initialisation.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_add_patch_creates_row fingerprint=51ccf2a59a0cfe4f33150d76d586c9975a39b92ba10bab093140d2ffdf9fc793 body_fp=f4c955a4aabeb47e2e11f09a0f75d1282a3378d90790c038a21e45e8ce158ca8 source_ref=a95486d535aed1c6b87b5026c7d31274c719666f -->
## `test_add_patch_creates_row(store: Store, tmp_path: Path)`

Verify that `Store.add_patch` returns a positive integer row ID when given a valid qualified name.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_add_patch_unknown_qname_raises fingerprint=2c5cf871b9971802156207d3ca60e7ec26bb025030323423a338bba5d046430d body_fp=1c02500697a7d5e40fefb98064e4b872e0221cf4a7e074861f03773ff2f96a05 source_ref=a95486d535aed1c6b87b5026c7d31274c719666f -->
## `test_add_patch_unknown_qname_raises(store: Store)`

Assert that `Store.add_patch` raises `KeyError` when the qualified name does not exist in the symbols table.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_get_patches_for_qname fingerprint=f1e9302dc1854b0bcc2d638fdc9cabf9cc42c3bafd3cfcb84094c1c43b34de34 body_fp=6b511ac7c9f2abb03f3884f5cc04a205f0d1a7f3ee4abb0ba6984b6af6664f16 source_ref=a95486d535aed1c6b87b5026c7d31274c719666f -->
## `test_get_patches_for_qname(store: Store, tmp_path: Path)`

Assert that `Store.get_patches_for_qname` returns all patches in insertion order for a given qualified name.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_get_patches_for_unknown_qname_returns_empty fingerprint=575896bc579c59f1266dd243ad1bf7faf63c9ce97c6f595cce38deb395e38663 body_fp=26401ea97a6b9a16232f26dcea5de3ddbb91a97190839a4ff44f1bdfdad3cc6e source_ref=a95486d535aed1c6b87b5026c7d31274c719666f -->
## `test_get_patches_for_unknown_qname_returns_empty(store: Store)`

Assert that `Store.get_patches_for_qname` returns an empty list for a non-existent qualified name.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_get_all_patches_grouped fingerprint=139f996fd76951ad17c9c62f541783e5f82a92a8395be9f8582a15e879519bc8 body_fp=8d5286bb0bd8af3b8a609433348028507883dc1068ce56059b5578bfad55bc6f source_ref=a95486d535aed1c6b87b5026c7d31274c719666f -->
## `test_get_all_patches_grouped(store: Store, tmp_path: Path)`

Verify that `Store.get_all_patches_grouped` returns all patches keyed by qualified name across multiple symbols.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_patch_count_for_symbol fingerprint=37e26e2eba0a6cdb1440a0bb6613cc1c86d8bcae92fab1b59b12c4b0a4b852c9 body_fp=85c07c304aebdcfacd1f63c57bd4d7c0d6f9999b44c3b9f8c005b752f76bb333 source_ref=a95486d535aed1c6b87b5026c7d31274c719666f -->
## `test_patch_count_for_symbol(store: Store, tmp_path: Path)`

Verify that `Store.patch_count_for_symbol` returns the correct count for a symbol looked up by its database ID.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_delete_patches_by_qname fingerprint=0c9fc98460b4ef85d24cf18a48d1c2b0910038a53bf6ad56b6018dd9acdbebef body_fp=881558825e84207c49b4a433514a574d97a5a7868046d07ac2064ba16267d51f source_ref=a95486d535aed1c6b87b5026c7d31274c719666f -->
## `test_delete_patches_by_qname(store: Store, tmp_path: Path)`

Verify that `Store.delete_patches(qname=...)` removes all patches for the given qualified name.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_delete_patches_all fingerprint=409fdba5741ad09c0aeb9edde44de1b401b66d2c151b4242bbb3f7537e3a2f95 body_fp=8d8ee67254ec8fe1f55635fa8e56f6b96c80b2e56d3a725c9d5949956b3ead06 source_ref=a95486d535aed1c6b87b5026c7d31274c719666f -->
## `test_delete_patches_all(store: Store, tmp_path: Path)`

Verify that `Store.delete_patches(all=True)` removes all patches and returns a count ≥ 1.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_delete_patches_by_session fingerprint=4bb84ebd549f63ef2bdb8de200c745ec136e877f76149edca7c0220f74e20fa9 body_fp=aab9eb8cea2bcebb60e56917784f5e30bd2281e5830573ecf7df578765dec0ec source_ref=a95486d535aed1c6b87b5026c7d31274c719666f -->
## `test_delete_patches_by_session(store: Store, tmp_path: Path)`

Verify that `Store.delete_patches(session_id=...)` removes only patches belonging to the specified session, leaving others intact.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_get_patched_qnames fingerprint=df07146b14c4766ffce62585b55421cee5581952defc5bef677a6ba24b31fa6c body_fp=86df58f51881e073a79f3ea8b6c37be62b51bf30f8f669867614800250857627 source_ref=a95486d535aed1c6b87b5026c7d31274c719666f -->
## `test_get_patched_qnames(store: Store, tmp_path: Path)`

Verify that `Store.get_patched_qnames` returns an empty list before any patches and the correct qualified name after one is added.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_get_symbol_detail_includes_patches fingerprint=a0d630abfbed72d3d15dabcd1b0b92a856415e3701bb569ca878dfa978ef6ad4 body_fp=38a7f364a3f3548ce694664369372bb51935ac9e2bdcb4c9745c769d1f2e4d97 source_ref=a95486d535aed1c6b87b5026c7d31274c719666f -->
## `test_get_symbol_detail_includes_patches(store: Store, tmp_path: Path)`

Verify that `Store.get_symbol_detail` reflects `pending_patches` and `pending_patch_count` before and after adding a patch.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_grep_symbols_includes_patch_count fingerprint=546b4968e60f78c2998c148fa93e213ff4eb900e810e0e3deeddc7cdb570a78e body_fp=12a141c7a9e16dad97fe50fc3c623926e2bd1e23f994a75174b754cac72dc87d source_ref=a95486d535aed1c6b87b5026c7d31274c719666f -->
## `test_grep_symbols_includes_patch_count(store: Store, tmp_path: Path)`

Verify that `Store.grep_symbols` results include a correct `pending_patch_count` for matched symbols.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_patches_cascaded_on_symbol_delete fingerprint=0bec0a50276615fa649a442fa7ed2d8a5203852f243f7241672781c016e62d80 body_fp=3ce1b39b5acf59a8d195112e9bec3a6dab1cd98a2965239179919c85d14c7e71 source_ref=a95486d535aed1c6b87b5026c7d31274c719666f -->
## `test_patches_cascaded_on_symbol_delete(store: Store, tmp_path: Path)`

Assert that patches are deleted when their parent symbol is removed via `replace_file_symbols`.
<!-- trie:end -->