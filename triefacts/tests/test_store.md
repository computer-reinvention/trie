---
trie_version: 0.1.5
source: tests/test_store.py
file_fingerprint: 5b0ca061e713690a8161eac959468358abf65b6641c42e59a55b34262d85bacc
last_synced_at: '2026-06-06T13:44:40Z'
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
<!-- trie:section symbol=tests/test_store:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=2d1341b8890e47f362cedf6a759abc378781b43a6f94b51c35b858f92b1a8f77 source_ref=a95486d535aed1c6b87b5026c7d31274c719666f role=test-infrastructure -->
Test suite for the `trie.graph.store` module, verifying Store database operations and patch management functionality.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:store fingerprint=c5420fff5b078bc5c2e95aff6471bdee364032edad5dee901f70ebfc07cd85eb body_fp=5265166b02760249029ce3e15608512615a7d745b13ea2a100d1f95a8a2a2191 source_ref=a95486d535aed1c6b87b5026c7d31274c719666f role=test-infrastructure -->
Pytest fixture that creates a temporary Store instance and ensures cleanup after test completion.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_schema_version_recorded fingerprint=2581df1e7e37dd6979078449702b4844298aace7f2e4a4facfc5eb87a6766f78 body_fp=2cd16a2738563fa5d743d07394affde0d0234f2f77be8a0d5773d9e30c94a664 source_ref=a95486d535aed1c6b87b5026c7d31274c719666f role=test -->
Verifies that Store records the correct schema version in the database on initialization.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_upsert_and_get_file fingerprint=f3b58b4e3b9159727ab6287bf2302a550f35296a8d1eb39f62d33d4cdea3b959 body_fp=1edef73a1d6a1c5f5f6ddd7905f4705e7372824bf07b55cfad0716bcaf6909f0 source_ref=a95486d535aed1c6b87b5026c7d31274c719666f role=test -->
Tests that Store can insert a new file record and retrieve it with correct values.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_upsert_overwrites_existing fingerprint=9db6492c71548100dcb1641379202911793ae4f436b4e9aaa3c7c555be8aa398 body_fp=86d75d61abbc3cfb15d195e797762874e8a894cbae180a651afab3aaf2b3e632 source_ref=a95486d535aed1c6b87b5026c7d31274c719666f role=test-infrastructure -->
Verifies that Store.upsert_file overwrites existing file records with new fingerprint and timestamp values.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_list_files_sorted fingerprint=2527e7f0347a9473606b15234fc7a71b2b0d4c8048a320f4f01796e0d79debef body_fp=1fca19f4bd172775d8942203e02cfaf971643247811e92b558f584af582b08d4 source_ref=a95486d535aed1c6b87b5026c7d31274c719666f role=test-infrastructure -->
Verifies that Store.list_files returns file records sorted alphabetically by path.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_delete_file_cascades_symbols fingerprint=f7eddba29276842b42c4218e2c41613b855a0ec86a39fdf3a1e28db3dba2d5fb body_fp=93b6a935106e95fd136ec0a88408beb5f39e957c96fbfb20bd586f523adfcbc3 source_ref=a95486d535aed1c6b87b5026c7d31274c719666f role=graph-database -->
Tests that Store.delete_file removes associated symbols via database cascade.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_replace_file_symbols_replaces_atomically fingerprint=eba7fb5f4d931588f59a8eb9248ec60869b10664d0c8d0fdbcf37929d3123559 body_fp=bd23c1e803bf6d9e8c2562718a48c0796161b9a969f1c24aa11168e4b628618e source_ref=a95486d535aed1c6b87b5026c7d31274c719666f role=graph-database -->
Tests that `Store.replace_file_symbols` atomically replaces all symbols for a file and handles repeated operations without constraint violations.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_count_symbols_public_only fingerprint=222c17ff3cda50356d07214099dc6b04be5f340bf11bbff7957250e3a2f53cdd body_fp=8ec52129e57a3b15a0b77f628f6169cd3ca464fef25e37a489cf9a36f0f8122e source_ref=a95486d535aed1c6b87b5026c7d31274c719666f role=test-infrastructure -->
Validates that Store.count_symbols correctly filters private symbols when public_only=True.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_file_stats fingerprint=d9c36a2293bcc3553bccb18227e7f62b1745bdcce0cc7886a4a0f4b99c31d6a0 body_fp=279f882f4b6caac5ecdc1c479d6e87b39f19629165d348b97a53fa84bd547280 source_ref=a95486d535aed1c6b87b5026c7d31274c719666f role=test-infrastructure -->
Tests Store file_stats method by verifying symbol count statistics for files with varying symbol visibility.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_context_manager_closes fingerprint=65d7ddf8931633bad6022ea097f4d7205028b3ba29b009cc72ff71f01b4d0c14 body_fp=489721804e031c8c4a961a0d28638cc7148873a6cd7db97b346659dfb76bfb88 source_ref=a95486d535aed1c6b87b5026c7d31274c719666f role=test-infrastructure -->
Tests that Store context manager properly closes database connection and persists data.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_transaction_rolls_back_on_error fingerprint=8137c9af2218b70b56eb96a6ae7becf72e2277f0977f03c442cf700b067d7e04 body_fp=311c2267024817a5ae3f0372bd81483884cb8016b1629b0f3858fbfe5b9dd20d source_ref=a95486d535aed1c6b87b5026c7d31274c719666f role=test-infrastructure -->
Verifies that Store transaction context manager rolls back database changes when an exception occurs.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_patches_table_exists fingerprint=39a2650346d0847b44524744d583f1e3d653872fab888dde254d29ee4774f7c5 body_fp=66d5218f0dc9b21d1970575ca233305fbd24a8c5e041d6d509646d1abc13348b source_ref=a95486d535aed1c6b87b5026c7d31274c719666f role=test-infrastructure -->
Verifies the patches table exists in the database schema by querying sqlite_master.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_add_patch_creates_row fingerprint=51ccf2a59a0cfe4f33150d76d586c9975a39b92ba10bab093140d2ffdf9fc793 body_fp=4296495f1413e304a63f61dd029073c7b71d70c1146f2ece5ad20258b360fa5d source_ref=a95486d535aed1c6b87b5026c7d31274c719666f role=test-infrastructure -->
Tests that Store.add_patch returns a positive integer patch ID when creating a patch for an existing symbol.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_add_patch_unknown_qname_raises fingerprint=2c5cf871b9971802156207d3ca60e7ec26bb025030323423a338bba5d046430d body_fp=24420ff3fd31af1f6e3c93812a87dafcf22897776dff3345d0275a0c07a57145 source_ref=a95486d535aed1c6b87b5026c7d31274c719666f role=test-infrastructure -->
Verifies that Store.add_patch raises KeyError when given a qualified name that doesn't exist in the symbols table.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_get_patches_for_qname fingerprint=f1e9302dc1854b0bcc2d638fdc9cabf9cc42c3bafd3cfcb84094c1c43b34de34 body_fp=f583d2287398a44ea5e6b473ba0f8ffe736548e620a0ef3a2b270a8275411718 source_ref=a95486d535aed1c6b87b5026c7d31274c719666f role=test-infrastructure -->
Tests that Store.get_patches_for_qname returns all patches for a given qualified symbol name.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_get_patches_for_unknown_qname_returns_empty fingerprint=575896bc579c59f1266dd243ad1bf7faf63c9ce97c6f595cce38deb395e38663 body_fp=4b1d6529af2fdf7482ed455d29c55f1c774fad96cbfc90bd80cc9fe234395718 source_ref=a95486d535aed1c6b87b5026c7d31274c719666f role=test-infrastructure -->
Verifies that Store.get_patches_for_qname returns an empty list for non-existent symbol qualified names.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_get_all_patches_grouped fingerprint=139f996fd76951ad17c9c62f541783e5f82a92a8395be9f8582a15e879519bc8 body_fp=d7ab242a9ac110f263d811a9568e491338a559642d5b3684be9a559e77372c5a source_ref=a95486d535aed1c6b87b5026c7d31274c719666f role=graph-database -->
Verifies that Store.get_all_patches_grouped returns patches organized by qualified name.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_patch_count_for_symbol fingerprint=37e26e2eba0a6cdb1440a0bb6613cc1c86d8bcae92fab1b59b12c4b0a4b852c9 body_fp=488a29efdef1f0ddedc0d8d1f0652083b801e845ccf3e3bde666eb2c831e914c source_ref=a95486d535aed1c6b87b5026c7d31274c719666f role=test-infrastructure -->
Tests that Store.patch_count_for_symbol correctly counts patches associated with a symbol ID.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_delete_patches_by_qname fingerprint=0c9fc98460b4ef85d24cf18a48d1c2b0910038a53bf6ad56b6018dd9acdbebef body_fp=9fe4b0f36b26672ecc3cab6d6cb2c854ec65108bb3bde2e3267bdf8e1365a496 source_ref=a95486d535aed1c6b87b5026c7d31274c719666f role=test-infrastructure -->
Tests Store.delete_patches method with qname parameter removes patches for specific symbol.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_delete_patches_all fingerprint=409fdba5741ad09c0aeb9edde44de1b401b66d2c151b4242bbb3f7537e3a2f95 body_fp=caca4a0f8d2827be7a96437828708e242821a12ea06a73de2c7e322261f0480d source_ref=a95486d535aed1c6b87b5026c7d31274c719666f role=test-infrastructure -->
Tests Store.delete_patches with all=True parameter removes all patches from database.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_delete_patches_by_session fingerprint=4bb84ebd549f63ef2bdb8de200c745ec136e877f76149edca7c0220f74e20fa9 body_fp=c8641ca8ce169eda8c380436dd2c43c4d3e9f1694ea5f7bb7fb1ce6ee6834e93 source_ref=a95486d535aed1c6b87b5026c7d31274c719666f role=graph-database -->
Tests that Store.delete_patches removes only patches matching the specified session ID.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_get_patched_qnames fingerprint=df07146b14c4766ffce62585b55421cee5581952defc5bef677a6ba24b31fa6c body_fp=75d82e42c87a4c63e528d7705ce38e3aa4d0e10ac1dedfadaf1206e42a82ad23 source_ref=a95486d535aed1c6b87b5026c7d31274c719666f role=test-infrastructure -->
Tests that Store.get_patched_qnames returns qualified names of symbols with pending patches.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_get_symbol_detail_includes_patches fingerprint=a0d630abfbed72d3d15dabcd1b0b92a856415e3701bb569ca878dfa978ef6ad4 body_fp=fd8c093e12e333a908bfacd793665ef4f27df5ca3238a39bc3eef094340e84bb source_ref=a95486d535aed1c6b87b5026c7d31274c719666f role=graph-database -->
Verifies Store.get_symbol_detail returns patch information for symbols with pending patches.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_grep_symbols_includes_patch_count fingerprint=546b4968e60f78c2998c148fa93e213ff4eb900e810e0e3deeddc7cdb570a78e body_fp=3053241b9d8f39ba735d9eed6d030b1037b41704a1a04f755da353cc51fd2a23 source_ref=a95486d535aed1c6b87b5026c7d31274c719666f role=graph-database -->
Verifies that Store.grep_symbols returns results with accurate pending patch counts for symbols.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_patches_cascaded_on_symbol_delete fingerprint=0bec0a50276615fa649a442fa7ed2d8a5203852f243f7241672781c016e62d80 body_fp=f2608840ce38d7625b5a64ffe09d5f9b6e6e4fdc8c15f279d8fe1baab3d05ee4 source_ref=a95486d535aed1c6b87b5026c7d31274c719666f role=test-infrastructure -->
Verifies that patches are automatically deleted when their associated symbol is removed from the store.
<!-- trie:end -->