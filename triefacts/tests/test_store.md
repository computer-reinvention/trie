---
trie_version: 0.1.0
source: tests/test_store.py
file_fingerprint: 00985eef34289663d51531504237528eae803e32d20b342ddd394043268f245c
last_synced_at: '2026-05-12T18:28:33Z'
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
<!-- trie:section symbol=tests/test_store:store fingerprint=c5420fff5b078bc5c2e95aff6471bdee364032edad5dee901f70ebfc07cd85eb body_fp=880968db4a90cf75e27c0e1641604fd55e92019f9870a0d87c5ac30e3a029ef9 -->
## `store(tmp_path: Path) -> Store`

Pytest fixture that yields a `Store` backed by a temp-path database, then closes it.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_store:test_schema_version_recorded fingerprint=2581df1e7e37dd6979078449702b4844298aace7f2e4a4facfc5eb87a6766f78 body_fp=39b27ec4352992b50dfba05443cfb2d70b80a61f75cf94f96122c2dee808b815 -->
## `test_schema_version_recorded(store: Store)`

Verify that the `schema_version` table stores the expected `SCHEMA_VERSION` constant.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_store:test_upsert_and_get_file fingerprint=f3b58b4e3b9159727ab6287bf2302a550f35296a8d1eb39f62d33d4cdea3b959 body_fp=a219d314fcb2fa369624eace63d426f32876bb920fad79fd4c5b27d591e05278 -->
## `test_upsert_and_get_file(store: Store)`

Verify that `get_file` returns `None` before insert and a matching `FileRecord` after `upsert_file`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_store:test_upsert_overwrites_existing fingerprint=9db6492c71548100dcb1641379202911793ae4f436b4e9aaa3c7c555be8aa398 body_fp=ddd4d2deb025e5f7395ed08f14c8cf49d93bdefa22d7e430850f8a789ebe416c -->
## `test_upsert_overwrites_existing(store: Store)`

Verify that upserting the same path twice replaces fingerprint and timestamp with the newer values.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_store:test_list_files_sorted fingerprint=2527e7f0347a9473606b15234fc7a71b2b0d4c8048a320f4f01796e0d79debef body_fp=b1afea30a7a20b9cf14d43c05084bc9d8f5184917f8a26e235fb4853079409b8 -->
## `test_list_files_sorted(store: Store)`

Verify that `list_files` returns file records sorted alphabetically by path.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_store:test_delete_file_cascades_symbols fingerprint=f7eddba29276842b42c4218e2c41613b855a0ec86a39fdf3a1e28db3dba2d5fb body_fp=820d1f91e4d3b0b1b33c557ff97fbdf983eed87231cefebeb6f672f9fa5a477a -->
## `test_delete_file_cascades_symbols(store: Store, tmp_path: Path)`

Verify that deleting a file record also removes all associated symbols from the store.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_store:test_replace_file_symbols_replaces_atomically fingerprint=eba7fb5f4d931588f59a8eb9248ec60869b10664d0c8d0fdbcf37929d3123559 body_fp=b4e3e1ccf98cd2755d2d29c6fddc3072ed110d26f5f1449ad0ee2b07c7f4a96d -->
## `test_replace_file_symbols_replaces_atomically(store: Store, tmp_path: Path)`

Verify that `replace_file_symbols` fully replaces symbol sets across versions without violating unique constraints on repeated calls.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_store:test_count_symbols_public_only fingerprint=222c17ff3cda50356d07214099dc6b04be5f340bf11bbff7957250e3a2f53cdd body_fp=43ba27e0a1df44ac2ce5a0463e6b7c590574f4ef371a7d68f70dd430beaaff5e -->
## `test_count_symbols_public_only(store: Store, tmp_path: Path)`

Verify that `count_symbols` with `public_only=True` excludes private functions and private-class methods.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_store:test_file_stats fingerprint=60d0859a360ca33fb52b55a651b0a9873def70d5663820ce72a5b02e48979082 body_fp=562c16b41955f79577406e0cad646cd288fe2fa7ae69dc14439a5df1362f4145 -->
## `test_file_stats(store: Store, tmp_path: Path)`

Verify `store.file_stats()` returns correct total and public symbol counts per file.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_store:test_context_manager_closes fingerprint=65d7ddf8931633bad6022ea097f4d7205028b3ba29b009cc72ff71f01b4d0c14 body_fp=215f2da0924d6defff1bdd85dd462d7160b8b9e3fc8d818a0b33a9ea5504e698 -->
## `test_context_manager_closes(tmp_path: Path)`

Verify that `Store` used as a context manager closes cleanly and persists data for a subsequent open.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_store:test_transaction_rolls_back_on_error fingerprint=8137c9af2218b70b56eb96a6ae7becf72e2277f0977f03c442cf700b067d7e04 body_fp=2591c41bf600bc0bcbbb8bfeffad957d9bff46935c0a4cc6e955ecd50c0227e7 -->
## `test_transaction_rolls_back_on_error(store: Store)`

Verify that `store.transaction()` rolls back all changes when an exception is raised mid-transaction.
<!-- trie:end -->