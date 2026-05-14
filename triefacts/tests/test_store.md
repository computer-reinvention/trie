---
trie_version: 0.1.0
source: tests/test_store.py
file_fingerprint: 00985eef34289663d51531504237528eae803e32d20b342ddd394043268f245c
last_synced_at: '2026-05-14T17:26:04Z'
defines:
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
  lines: 91-109
- kind: function
  qualified_name: tests/test_store:test_context_manager_closes
  lines: 112-118
- kind: function
  qualified_name: tests/test_store:test_transaction_rolls_back_on_error
  lines: 121-128
incoming_refs: 0
outgoing_refs: 7
---
<!-- trie:section symbol=tests/test_store:store fingerprint=c5420fff5b078bc5c2e95aff6471bdee364032edad5dee901f70ebfc07cd85eb body_fp=523177dba4cdc547dc64909b312d8ee926bb54611d2b750dfe016ad5f67a4e7d -->
## `store(tmp_path: Path) -> Store`

Pytest fixture that yields a temporary `Store` instance backed by a fresh database, then closes it.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_store:test_schema_version_recorded fingerprint=2581df1e7e37dd6979078449702b4844298aace7f2e4a4facfc5eb87a6766f78 body_fp=ee6aab331a0677eb771a2f745388df5b71fdb9ecf6074ed0508150868d231e42 -->
## `test_schema_version_recorded(store: Store)`

Assert that the `schema_version` table contains the expected `SCHEMA_VERSION` constant.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_store:test_upsert_and_get_file fingerprint=f3b58b4e3b9159727ab6287bf2302a550f35296a8d1eb39f62d33d4cdea3b959 body_fp=a219d314fcb2fa369624eace63d426f32876bb920fad79fd4c5b27d591e05278 -->
## `test_upsert_and_get_file(store: Store)`

Verify that `get_file` returns `None` before insert and a matching `FileRecord` after `upsert_file`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_store:test_upsert_overwrites_existing fingerprint=9db6492c71548100dcb1641379202911793ae4f436b4e9aaa3c7c555be8aa398 body_fp=bcd1ae20ac6867a464ba5054d07db3431d204c65797d355b32eacf9137fb4fe3 -->
## `test_upsert_overwrites_existing(store: Store)`

Verify that upserting a file twice replaces the fingerprint and timestamp with the latest values.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_store:test_list_files_sorted fingerprint=2527e7f0347a9473606b15234fc7a71b2b0d4c8048a320f4f01796e0d79debef body_fp=b1afea30a7a20b9cf14d43c05084bc9d8f5184917f8a26e235fb4853079409b8 -->
## `test_list_files_sorted(store: Store)`

Verify that `list_files` returns file records sorted alphabetically by path.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_store:test_delete_file_cascades_symbols fingerprint=f7eddba29276842b42c4218e2c41613b855a0ec86a39fdf3a1e28db3dba2d5fb body_fp=be16d86d10201354ecfc610eadbe9979ecee31d1d7c20609667db6141f8b298d -->
## `test_delete_file_cascades_symbols(store: Store, tmp_path: Path)`

Verify that deleting a file record also removes all its associated symbols.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_store:test_replace_file_symbols_replaces_atomically fingerprint=eba7fb5f4d931588f59a8eb9248ec60869b10664d0c8d0fdbcf37929d3123559 body_fp=ca393009e5c9ac774ea8a937fa892b129f7ae3aee672369e2e124ebf59d48917 -->
## `test_replace_file_symbols_replaces_atomically(store: Store, tmp_path: Path)`

Verify that `replace_file_symbols` overwrites stale symbols atomically and tolerates repeated upserts without violating unique constraints.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_store:test_count_symbols_public_only fingerprint=222c17ff3cda50356d07214099dc6b04be5f340bf11bbff7957250e3a2f53cdd body_fp=778809d8a5108ee3ac6c66423483d0802329aabd1cf508054c75e2920bb7af63 -->
## `test_count_symbols_public_only(store: Store, tmp_path: Path)`

Verify that `count_symbols` with `public_only=True` excludes private functions and private classes.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_store:test_file_stats fingerprint=60d0859a360ca33fb52b55a651b0a9873def70d5663820ce72a5b02e48979082 body_fp=08e45f5fe5e7030027a9cc7762bd4f2e82b056eee6691d6c9aaccc6f0da1d62f -->
## `test_file_stats(store: Store, tmp_path: Path)`

Verify `file_stats()` returns correct total and public symbol counts per file.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_store:test_context_manager_closes fingerprint=65d7ddf8931633bad6022ea097f4d7205028b3ba29b009cc72ff71f01b4d0c14 body_fp=f7b385bfe6262e4d452bc4db45962e4d50bb5bf771cf5b7734afdbba03c4291b -->
## `test_context_manager_closes(tmp_path: Path)`

Verify that `Store` used as a context manager closes and persists data, readable by a subsequent `Store` instance.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_store:test_transaction_rolls_back_on_error fingerprint=8137c9af2218b70b56eb96a6ae7becf72e2277f0977f03c442cf700b067d7e04 body_fp=e56d0e44c1a1f4600c47641c60f57dfa4396aad8003896dfe1b0a2e2844008e4 -->
## `test_transaction_rolls_back_on_error(store: Store)`

Verify that `Store.transaction()` rolls back all changes when an exception is raised mid-transaction.
<!-- trie:end -->