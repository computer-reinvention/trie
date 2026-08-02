---
trie_version: 0.3.0
source: tests/test_store.py
file_fingerprint: 037ade0bd37f123db34a21ffcec7b3206355ddf1b6f4ce38045055493d3b7be9
last_synced_at: '2026-08-01T01:51:57Z'
defines:
- kind: module
  qualified_name: tests/test_store:__module__
  lines: 1-482
- kind: function
  qualified_name: tests/test_store:store
  lines: 13-16
  signature: 'def store(tmp_path: Path) -> Store'
- kind: function
  qualified_name: tests/test_store:test_schema_version_recorded
  lines: 19-21
  signature: 'def test_schema_version_recorded(store: Store)'
- kind: function
  qualified_name: tests/test_store:test_upsert_and_get_file
  lines: 24-28
  signature: 'def test_upsert_and_get_file(store: Store)'
- kind: function
  qualified_name: tests/test_store:test_upsert_overwrites_existing
  lines: 31-37
  signature: 'def test_upsert_overwrites_existing(store: Store)'
- kind: function
  qualified_name: tests/test_store:test_list_files_sorted
  lines: 40-44
  signature: 'def test_list_files_sorted(store: Store)'
- kind: function
  qualified_name: tests/test_store:test_delete_file_cascades_symbols
  lines: 47-57
  signature: 'def test_delete_file_cascades_symbols(store: Store, tmp_path: Path)'
- kind: function
  qualified_name: tests/test_store:test_replace_file_symbols_replaces_atomically
  lines: 60-76
  signature: 'def test_replace_file_symbols_replaces_atomically(store: Store, tmp_path: Path)'
- kind: function
  qualified_name: tests/test_store:test_count_symbols_public_only
  lines: 79-89
  signature: 'def test_count_symbols_public_only(store: Store, tmp_path: Path)'
- kind: function
  qualified_name: tests/test_store:test_file_stats
  lines: 92-112
  signature: 'def test_file_stats(store: Store, tmp_path: Path)'
- kind: function
  qualified_name: tests/test_store:test_context_manager_closes
  lines: 115-121
  signature: 'def test_context_manager_closes(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_store:test_transaction_rolls_back_on_error
  lines: 124-131
  signature: 'def test_transaction_rolls_back_on_error(store: Store)'
- kind: function
  qualified_name: tests/test_store:test_patches_table_exists
  lines: 137-142
  signature: 'def test_patches_table_exists(store: Store)'
- kind: function
  qualified_name: tests/test_store:test_add_patch_creates_row
  lines: 145-153
  signature: 'def test_add_patch_creates_row(store: Store, tmp_path: Path)'
- kind: function
  qualified_name: tests/test_store:test_add_patch_unknown_qname_raises
  lines: 156-158
  signature: 'def test_add_patch_unknown_qname_raises(store: Store)'
- kind: function
  qualified_name: tests/test_store:test_get_patches_for_qname
  lines: 161-174
  signature: 'def test_get_patches_for_qname(store: Store, tmp_path: Path)'
- kind: function
  qualified_name: tests/test_store:test_get_patches_for_unknown_qname_returns_empty
  lines: 177-178
  signature: 'def test_get_patches_for_unknown_qname_returns_empty(store: Store)'
- kind: function
  qualified_name: tests/test_store:test_get_all_patches_grouped
  lines: 181-194
  signature: 'def test_get_all_patches_grouped(store: Store, tmp_path: Path)'
- kind: function
  qualified_name: tests/test_store:test_patch_rows_are_qname_keyed
  lines: 197-212
  signature: 'def test_patch_rows_are_qname_keyed(store: Store, tmp_path: Path)'
- kind: function
  qualified_name: tests/test_store:test_delete_patches_by_qname
  lines: 215-225
  signature: 'def test_delete_patches_by_qname(store: Store, tmp_path: Path)'
- kind: function
  qualified_name: tests/test_store:test_delete_patches_all
  lines: 228-238
  signature: 'def test_delete_patches_all(store: Store, tmp_path: Path)'
- kind: function
  qualified_name: tests/test_store:test_delete_patches_by_session
  lines: 241-254
  signature: 'def test_delete_patches_by_session(store: Store, tmp_path: Path)'
- kind: function
  qualified_name: tests/test_store:test_get_patched_qnames
  lines: 257-266
  signature: 'def test_get_patched_qnames(store: Store, tmp_path: Path)'
- kind: function
  qualified_name: tests/test_store:test_get_symbol_detail_includes_patches
  lines: 269-286
  signature: 'def test_get_symbol_detail_includes_patches(store: Store, tmp_path: Path)'
- kind: function
  qualified_name: tests/test_store:test_grep_symbols_includes_patch_count
  lines: 289-301
  signature: 'def test_grep_symbols_includes_patch_count(store: Store, tmp_path: Path)'
- kind: function
  qualified_name: tests/test_store:test_patches_survive_symbol_replacement
  lines: 304-318
  signature: 'def test_patches_survive_symbol_replacement(store: Store, tmp_path: Path)'
- kind: function
  qualified_name: tests/test_store:_seed_greet
  lines: 324-328
  signature: 'def _seed_greet(store: Store, tmp_path: Path) -> None'
- kind: function
  qualified_name: tests/test_store:test_add_patch_defaults_to_modify_kind
  lines: 331-336
  signature: 'def test_add_patch_defaults_to_modify_kind(store: Store, tmp_path: Path)'
- kind: function
  qualified_name: tests/test_store:test_add_delete_patch
  lines: 339-343
  signature: 'def test_add_delete_patch(store: Store, tmp_path: Path)'
- kind: function
  qualified_name: tests/test_store:test_add_rename_patch_carries_new_name
  lines: 346-351
  signature: 'def test_add_rename_patch_carries_new_name(store: Store, tmp_path: Path)'
- kind: function
  qualified_name: tests/test_store:test_delete_and_rename_patches_require_existing_symbol
  lines: 354-358
  signature: 'def test_delete_and_rename_patches_require_existing_symbol(store: Store)'
- kind: function
  qualified_name: tests/test_store:test_grouped_patches_include_kind
  lines: 361-367
  signature: 'def test_grouped_patches_include_kind(store: Store, tmp_path: Path)'
- kind: function
  qualified_name: tests/test_store:test_add_and_group_create_patches
  lines: 370-384
  signature: 'def test_add_and_group_create_patches(store: Store)'
- kind: function
  qualified_name: tests/test_store:test_delete_create_patches_by_target
  lines: 387-396
  signature: 'def test_delete_create_patches_by_target(store: Store)'
- kind: function
  qualified_name: tests/test_store:test_delete_create_patches_by_session_and_all
  lines: 399-408
  signature: 'def test_delete_create_patches_by_session_and_all(store: Store)'
- kind: function
  qualified_name: tests/test_store:test_concurrent_access_does_not_raise
  lines: 411-442
  signature: 'def test_concurrent_access_does_not_raise(store: Store)'
- kind: function
  qualified_name: tests/test_store:test_grep_symbols_demotes_test_paths_within_page
  lines: 445-481
  signature: 'def test_grep_symbols_demotes_test_paths_within_page(store: Store)'
incoming_refs: 0
outgoing_refs: 23
---
<!-- trie:section symbol=tests/test_store:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=2d1341b8890e47f362cedf6a759abc378781b43a6f94b51c35b858f92b1a8f77 source_ref=a95486d535aed1c6b87b5026c7d31274c719666f role=test-infrastructure -->
Test suite for the `trie.graph.store` module, verifying Store database operations and patch management functionality.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:store fingerprint=c5420fff5b078bc5c2e95aff6471bdee364032edad5dee901f70ebfc07cd85eb body_fp=9ed28d0e621eb5bb7cfb30a3dee4bb5d89e2153bb9c09273a8975fdc20f0c903 source_ref=a95486d535aed1c6b87b5026c7d31274c719666f role=test-infrastructure -->
## `def store(tmp_path: Path) -> Store`

Pytest fixture that creates a temporary Store instance and ensures cleanup after test completion.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_schema_version_recorded fingerprint=2581df1e7e37dd6979078449702b4844298aace7f2e4a4facfc5eb87a6766f78 body_fp=f2a84af2751ff976ef0818da028799d75c2f1d611ff746bb982da12a346ada1d source_ref=1edb270eac372aff1b5ed83bb2dca1b284166f88 role=test -->
## `def test_schema_version_recorded(store: Store)`

Verifies that Store records the correct schema version in the database on initialization.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_upsert_and_get_file fingerprint=f3b58b4e3b9159727ab6287bf2302a550f35296a8d1eb39f62d33d4cdea3b959 body_fp=02ff5f5ad383ac1e652984f908e2bc51b45121de623d7794674b981ca45d834b source_ref=1edb270eac372aff1b5ed83bb2dca1b284166f88 role=test -->
## `def test_upsert_and_get_file(store: Store)`

Tests that Store can insert a new file record and retrieve it with correct values.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_upsert_overwrites_existing fingerprint=9db6492c71548100dcb1641379202911793ae4f436b4e9aaa3c7c555be8aa398 body_fp=202770d0506d8087c40496f799892687b114c685428cfa4128f2df95b0a840a6 source_ref=a95486d535aed1c6b87b5026c7d31274c719666f role=test-infrastructure -->
## `def test_upsert_overwrites_existing(store: Store)`

Verifies that Store.upsert_file overwrites existing file records with new fingerprint and timestamp values.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_list_files_sorted fingerprint=2527e7f0347a9473606b15234fc7a71b2b0d4c8048a320f4f01796e0d79debef body_fp=4a1d60e9cd5be4d708488db268a98892839fd0d033af404f04fe223b1218f51d source_ref=a95486d535aed1c6b87b5026c7d31274c719666f role=test-infrastructure -->
## `def test_list_files_sorted(store: Store)`

Verifies that Store.list_files returns file records sorted alphabetically by path.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_delete_file_cascades_symbols fingerprint=f7eddba29276842b42c4218e2c41613b855a0ec86a39fdf3a1e28db3dba2d5fb body_fp=324948e02d8972762b771e6496d9721d84d006b3e491ead1ad4aee3bd780c50c source_ref=a95486d535aed1c6b87b5026c7d31274c719666f role=graph-database -->
## `def test_delete_file_cascades_symbols(store: Store, tmp_path: Path)`

Tests that Store.delete_file removes associated symbols via database cascade.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_replace_file_symbols_replaces_atomically fingerprint=eba7fb5f4d931588f59a8eb9248ec60869b10664d0c8d0fdbcf37929d3123559 body_fp=03b469ffbe82f8fcb296ecfc128840306ee33dbc5c7c33962bf2c5804f77cdf8 source_ref=a95486d535aed1c6b87b5026c7d31274c719666f role=graph-database -->
## `def test_replace_file_symbols_replaces_atomically(store: Store, tmp_path: Path)`

Tests that `Store.replace_file_symbols` atomically replaces all symbols for a file and handles repeated operations without constraint violations.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_count_symbols_public_only fingerprint=222c17ff3cda50356d07214099dc6b04be5f340bf11bbff7957250e3a2f53cdd body_fp=7196c309b754173c796097005696f9ec4af9c18a43370764384d1b338c1cb27b source_ref=a95486d535aed1c6b87b5026c7d31274c719666f role=test-infrastructure -->
## `def test_count_symbols_public_only(store: Store, tmp_path: Path)`

Validates that Store.count_symbols correctly filters private symbols when public_only=True.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_file_stats fingerprint=d9c36a2293bcc3553bccb18227e7f62b1745bdcce0cc7886a4a0f4b99c31d6a0 body_fp=924617e218aabb3727a5027950c7e0ab9aa78ccc8c797c079a82790f642a8c3a source_ref=a95486d535aed1c6b87b5026c7d31274c719666f role=test-infrastructure -->
## `def test_file_stats(store: Store, tmp_path: Path)`

Tests Store file_stats method by verifying symbol count statistics for files with varying symbol visibility.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_context_manager_closes fingerprint=65d7ddf8931633bad6022ea097f4d7205028b3ba29b009cc72ff71f01b4d0c14 body_fp=5529dc906482f3186a46b7f67194080a0af9978d9d745a853aec0b3956b212d0 source_ref=a95486d535aed1c6b87b5026c7d31274c719666f role=test-infrastructure -->
## `def test_context_manager_closes(tmp_path: Path)`

Tests that Store context manager properly closes database connection and persists data.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_transaction_rolls_back_on_error fingerprint=8137c9af2218b70b56eb96a6ae7becf72e2277f0977f03c442cf700b067d7e04 body_fp=7fded4646734e486ab11b0e0e337c0c6e6bfa627f4b7356a17a02a56a1bb4e99 source_ref=a95486d535aed1c6b87b5026c7d31274c719666f role=test-infrastructure -->
## `def test_transaction_rolls_back_on_error(store: Store)`

Verifies that Store transaction context manager rolls back database changes when an exception occurs.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_patches_table_exists fingerprint=39a2650346d0847b44524744d583f1e3d653872fab888dde254d29ee4774f7c5 body_fp=b6b9917851b69417dd42b22272cafbc847581088633ad906f30a23ca0366366c source_ref=a95486d535aed1c6b87b5026c7d31274c719666f role=test-infrastructure -->
## `def test_patches_table_exists(store: Store)`

Verifies the patches table exists in the database schema by querying sqlite_master.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_add_patch_creates_row fingerprint=51ccf2a59a0cfe4f33150d76d586c9975a39b92ba10bab093140d2ffdf9fc793 body_fp=18538354304891b7ec9f55f7dc07a7feb7d01b330b291deb62962f1b097a5960 source_ref=a95486d535aed1c6b87b5026c7d31274c719666f role=test-infrastructure -->
## `def test_add_patch_creates_row(store: Store, tmp_path: Path)`

Tests that Store.add_patch returns a positive integer patch ID when creating a patch for an existing symbol.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_add_patch_unknown_qname_raises fingerprint=2c5cf871b9971802156207d3ca60e7ec26bb025030323423a338bba5d046430d body_fp=c674d1b5a0a7a19f01eed0d491cc2fbf8b34a56830026268cd3e9398219842ec source_ref=a95486d535aed1c6b87b5026c7d31274c719666f role=test-infrastructure -->
## `def test_add_patch_unknown_qname_raises(store: Store)`

Verifies that Store.add_patch raises KeyError when given a qualified name that doesn't exist in the symbols table.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_get_patches_for_qname fingerprint=f1e9302dc1854b0bcc2d638fdc9cabf9cc42c3bafd3cfcb84094c1c43b34de34 body_fp=f557920cbf3fe9488da988e01490e128d5a09c8004f938af3c498d699f542d96 source_ref=a95486d535aed1c6b87b5026c7d31274c719666f role=test-infrastructure -->
## `def test_get_patches_for_qname(store: Store, tmp_path: Path)`

Tests that Store.get_patches_for_qname returns all patches for a given qualified symbol name.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_get_patches_for_unknown_qname_returns_empty fingerprint=575896bc579c59f1266dd243ad1bf7faf63c9ce97c6f595cce38deb395e38663 body_fp=899ed8eda73cc4e53591a670a9765f1dafb93c1040cf82d438516275a2c810e9 source_ref=a95486d535aed1c6b87b5026c7d31274c719666f role=test-infrastructure -->
## `def test_get_patches_for_unknown_qname_returns_empty(store: Store)`

Verifies that Store.get_patches_for_qname returns an empty list for non-existent symbol qualified names.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_get_all_patches_grouped fingerprint=139f996fd76951ad17c9c62f541783e5f82a92a8395be9f8582a15e879519bc8 body_fp=2f0041c6fcab47e6ba9252e785a7f8f582a26c15ea58b2619cd3cd8667d60240 source_ref=a95486d535aed1c6b87b5026c7d31274c719666f role=graph-database -->
## `def test_get_all_patches_grouped(store: Store, tmp_path: Path)`

Verifies that Store.get_all_patches_grouped returns patches organized by qualified name.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_patch_rows_are_qname_keyed fingerprint=fc57e0d6e81b997d39c2187e97853934bb321da9f541d60a1009a13062932ef5 body_fp=ad3084fcb9fad062c0ca01631c3b1a481cc379a2146ee2b8e7a872da5e3ac650 source_ref=1edb270eac372aff1b5ed83bb2dca1b284166f88 role=test -->
## `def test_patch_rows_are_qname_keyed(store: Store, tmp_path: Path)`

Assert that `Store.add_patch` guards against unknown qnames by default and allows bypass via `require_symbol=False`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_delete_patches_by_qname fingerprint=0c9fc98460b4ef85d24cf18a48d1c2b0910038a53bf6ad56b6018dd9acdbebef body_fp=e3b3929d763817db408f922a36f9b9f08cbe181749cb57a209237e5bd684f8a9 source_ref=a95486d535aed1c6b87b5026c7d31274c719666f role=test-infrastructure -->
## `def test_delete_patches_by_qname(store: Store, tmp_path: Path)`

Tests Store.delete_patches method with qname parameter removes patches for specific symbol.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_delete_patches_all fingerprint=409fdba5741ad09c0aeb9edde44de1b401b66d2c151b4242bbb3f7537e3a2f95 body_fp=c543275d3305aac6350274b268ca97305b4ce68ca5e3af02935c31b482b8459f source_ref=a95486d535aed1c6b87b5026c7d31274c719666f role=test-infrastructure -->
## `def test_delete_patches_all(store: Store, tmp_path: Path)`

Tests Store.delete_patches with all=True parameter removes all patches from database.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_delete_patches_by_session fingerprint=4bb84ebd549f63ef2bdb8de200c745ec136e877f76149edca7c0220f74e20fa9 body_fp=3ed732ba607509a2513e5f685e82a790058a6e59f9cfaa8aad61c989edf578fc source_ref=a95486d535aed1c6b87b5026c7d31274c719666f role=graph-database -->
## `def test_delete_patches_by_session(store: Store, tmp_path: Path)`

Tests that Store.delete_patches removes only patches matching the specified session ID.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_get_patched_qnames fingerprint=df07146b14c4766ffce62585b55421cee5581952defc5bef677a6ba24b31fa6c body_fp=824f387060a777528a1fd1ef6c66e0fc1f331a682239360fdbd40476b41c1f30 source_ref=a95486d535aed1c6b87b5026c7d31274c719666f role=test-infrastructure -->
## `def test_get_patched_qnames(store: Store, tmp_path: Path)`

Tests that Store.get_patched_qnames returns qualified names of symbols with pending patches.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_get_symbol_detail_includes_patches fingerprint=a0d630abfbed72d3d15dabcd1b0b92a856415e3701bb569ca878dfa978ef6ad4 body_fp=142331f6267248ac1be19689e170a872e81749299cf553693fa46ff0fd56c225 source_ref=a95486d535aed1c6b87b5026c7d31274c719666f role=graph-database -->
## `def test_get_symbol_detail_includes_patches(store: Store, tmp_path: Path)`

Verifies Store.get_symbol_detail returns patch information for symbols with pending patches.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_grep_symbols_includes_patch_count fingerprint=546b4968e60f78c2998c148fa93e213ff4eb900e810e0e3deeddc7cdb570a78e body_fp=f6ddf7fbc14017d7c7dc0ca45fc8c0a43b30a97801f0040e2046fddd7edac598 source_ref=a95486d535aed1c6b87b5026c7d31274c719666f role=graph-database -->
## `def test_grep_symbols_includes_patch_count(store: Store, tmp_path: Path)`

Verifies that Store.grep_symbols returns results with accurate pending patch counts for symbols.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_patches_survive_symbol_replacement fingerprint=71821a66c3ff86b20fa0c5bc1efdd3006671ec1c40e6deb97a37baf66a74ef71 body_fp=bf1a0af859feca0d97fd0b8b1d8bcde0756c353daaff0c9538abf1c3d40e57bf source_ref=1edb270eac372aff1b5ed83bb2dca1b284166f88 role=test -->
## `def test_patches_survive_symbol_replacement(store: Store, tmp_path: Path)`

Assert that patches keyed by qname survive a `replace_file_symbols` call that removes the associated symbol row.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:_seed_greet fingerprint=b4f933e9d0fc5f1b3df00d2ecaddadf5acff9c3de6c5276bba5e2df543e155ef body_fp=2308325da19bf066d650f48e9a7dfe9fd303485a5390bfc79472568517c2637e source_ref=459b5c5d3e63364c6de2c5475ae57476758c3a65 role=test -->
## `def _seed_greet(store: Store, tmp_path: Path) -> None`

Creates test file `a.py` with a `greet` function and populates the Store with its symbols.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_add_patch_defaults_to_modify_kind fingerprint=606e8dc48e5e2fe6013da111d3a82e4eaeaa94aafddec9495a0d4174c0039186 body_fp=4edb687024fdb1821b2bd4581b6d5350cf614a45b30910da72b0c7d7370f3a34 source_ref=459b5c5d3e63364c6de2c5475ae57476758c3a65 role=test -->
## `def test_add_patch_defaults_to_modify_kind(store: Store, tmp_path: Path)`

Verifies that Store.add_patch() creates patches with "modify" kind and null rename_to by default.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_add_delete_patch fingerprint=33dddbd1aa68979161707f029260a460c813e2a4f445052ece97ff1c18071d3c body_fp=11dc859732ccda37a25a341be6b83167f08ba240f9e94da8b253667e3d324003 source_ref=459b5c5d3e63364c6de2c5475ae57476758c3a65 role=test -->
## `def test_add_delete_patch(store: Store, tmp_path: Path)`

Tests Store.add_delete_patch creates a patch record with "delete" kind.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_add_rename_patch_carries_new_name fingerprint=0345c8c472cc1210507249cce3f4707a9e49eb1a9067c88e10ff357ca0d39eed body_fp=bb98ac2797123336ae828522608ab9255fac0a4551f51535273988723df62621 source_ref=459b5c5d3e63364c6de2c5475ae57476758c3a65 role=test -->
## `def test_add_rename_patch_carries_new_name(store: Store, tmp_path: Path)`

Tests that Store.add_rename_patch correctly stores the new name in the rename_to field.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_delete_and_rename_patches_require_existing_symbol fingerprint=0f82fc6ea84900e12de2e436c4605cc3e70f58bc630e6853a35e11bbecfaf703 body_fp=e1cc64912cf6bbc96f4284535a2b2f6b74e501f6f359f4e47d8d5a926d5c2f26 source_ref=459b5c5d3e63364c6de2c5475ae57476758c3a65 role=test -->
## `def test_delete_and_rename_patches_require_existing_symbol(store: Store)`

Verifies that Store.add_delete_patch and Store.add_rename_patch raise KeyError for nonexistent symbols.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_grouped_patches_include_kind fingerprint=6ed5a206b6d18f5184ebb566b17e6471b1fb1ed8f89b7b34756d662a69eff126 body_fp=fe4e1bebfe6b4b5d204491559f26690fc5f89d83951dda955133218c2fce95d1 source_ref=459b5c5d3e63364c6de2c5475ae57476758c3a65 role=test -->
## `def test_grouped_patches_include_kind(store: Store, tmp_path: Path)`

Tests that grouped patches include kind and rename_to fields when retrieving all patches grouped by symbol.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_add_and_group_create_patches fingerprint=a5714e3fcef688d462c9f2c02ec982d9b2c6c6f8c10d79c7cc3711b841162938 body_fp=8837b358dc4ff62b8044d6ee0d4dda72bc49120ecba35e5572f85ce1085ccf6d source_ref=459b5c5d3e63364c6de2c5475ae57476758c3a65 role=test -->
## `def test_add_and_group_create_patches(store: Store)`

Tests that Store can add create patches and group them by target file.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_delete_create_patches_by_target fingerprint=5779d676f4d936f6ad0cfb6fa4a8f322af52636776ff73404506da7b501bdea8 body_fp=31d1bfab9e0521c9cf23b6284f20af31762c4df8dee6b1d25644f35b06827aa4 source_ref=459b5c5d3e63364c6de2c5475ae57476758c3a65 role=test -->
## `def test_delete_create_patches_by_target(store: Store)`

Tests that Store.delete_create_patches removes only the patch matching the specified target_qname.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_delete_create_patches_by_session_and_all fingerprint=60d3b3d4f38da1eed2dcb3f0644e5c4de216b985873c7367c4b5842abccf6833 body_fp=b469edd9c4fff06312bfb6179fa03af40b620a88249578a2378287376b1d20cb source_ref=459b5c5d3e63364c6de2c5475ae57476758c3a65 role=test -->
## `def test_delete_create_patches_by_session_and_all(store: Store)`

Verifies Store can delete create patches by session ID and delete all remaining patches.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_concurrent_access_does_not_raise fingerprint=f77f538ec993ec2bd6ed39e22e21e9b442d79ae54bbc55a3754cd3a8d4932cf3 body_fp=8cba001474c90ba18b8bf174427630fcd7268054f21fe6d4738dfe02caaca6df source_ref=3df998e45be4b2a697de43a24a7dc9bdd57b152b role=test -->
## `def test_concurrent_access_does_not_raise(store: Store)`

Tests that concurrent Store access from 16 threads does not raise threading-related errors.

- Creates 16 worker threads that each perform 50 iterations of Store operations
- Uses threading.Barrier to synchronize thread startup for maximum contention
- Verifies no OperationalError or recursive cursor use exceptions occur
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_grep_symbols_demotes_test_paths_within_page fingerprint=fb8cb71121af3b1f2432c9890c0235fbc1b8446b0a96e660355839959475bfaa body_fp=917f4d64473c997fc1fbf6eb9b0053eff77ff7759b32ac87da85e77ed7843ed7 source_ref=20f28786eb725279816890dcb3a120aa0d0d5ec3 role=test -->
## `def test_grep_symbols_demotes_test_paths_within_page(store: Store)`

Regression test asserting that `Store.grep_symbols` demotes `tests/` paths in SQL `ORDER BY` so production symbols appear first within a limited result page.
<!-- trie:end -->