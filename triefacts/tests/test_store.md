---
trie_version: 0.1.9
source: tests/test_store.py
file_fingerprint: e545ba31c90987f93a7e73415a9fdee3e2ea4b13839b609bf2bf4e14ddbb0f19
last_synced_at: '2026-07-25T01:43:41Z'
defines:
- kind: module
  qualified_name: tests/test_store:__module__
  lines: 1-435
- kind: function
  qualified_name: tests/test_store:store
  lines: 13-16
- kind: function
  qualified_name: tests/test_store:test_schema_version_recorded
  lines: 19-21
- kind: function
  qualified_name: tests/test_store:test_upsert_and_get_file
  lines: 24-28
- kind: function
  qualified_name: tests/test_store:test_upsert_overwrites_existing
  lines: 31-37
- kind: function
  qualified_name: tests/test_store:test_list_files_sorted
  lines: 40-44
- kind: function
  qualified_name: tests/test_store:test_delete_file_cascades_symbols
  lines: 47-57
- kind: function
  qualified_name: tests/test_store:test_replace_file_symbols_replaces_atomically
  lines: 60-76
- kind: function
  qualified_name: tests/test_store:test_count_symbols_public_only
  lines: 79-89
- kind: function
  qualified_name: tests/test_store:test_file_stats
  lines: 92-112
- kind: function
  qualified_name: tests/test_store:test_context_manager_closes
  lines: 115-121
- kind: function
  qualified_name: tests/test_store:test_transaction_rolls_back_on_error
  lines: 124-131
- kind: function
  qualified_name: tests/test_store:test_patches_table_exists
  lines: 137-142
- kind: function
  qualified_name: tests/test_store:test_add_patch_creates_row
  lines: 145-153
- kind: function
  qualified_name: tests/test_store:test_add_patch_unknown_qname_raises
  lines: 156-158
- kind: function
  qualified_name: tests/test_store:test_get_patches_for_qname
  lines: 161-174
- kind: function
  qualified_name: tests/test_store:test_get_patches_for_unknown_qname_returns_empty
  lines: 177-178
- kind: function
  qualified_name: tests/test_store:test_get_all_patches_grouped
  lines: 181-194
- kind: function
  qualified_name: tests/test_store:test_patch_count_for_symbol
  lines: 197-208
- kind: function
  qualified_name: tests/test_store:test_delete_patches_by_qname
  lines: 211-221
- kind: function
  qualified_name: tests/test_store:test_delete_patches_all
  lines: 224-234
- kind: function
  qualified_name: tests/test_store:test_delete_patches_by_session
  lines: 237-250
- kind: function
  qualified_name: tests/test_store:test_get_patched_qnames
  lines: 253-262
- kind: function
  qualified_name: tests/test_store:test_get_symbol_detail_includes_patches
  lines: 265-282
- kind: function
  qualified_name: tests/test_store:test_grep_symbols_includes_patch_count
  lines: 285-297
- kind: function
  qualified_name: tests/test_store:test_patches_cascaded_on_symbol_delete
  lines: 300-310
- kind: function
  qualified_name: tests/test_store:_seed_greet
  lines: 316-320
- kind: function
  qualified_name: tests/test_store:test_add_patch_defaults_to_modify_kind
  lines: 323-328
- kind: function
  qualified_name: tests/test_store:test_add_delete_patch
  lines: 331-335
- kind: function
  qualified_name: tests/test_store:test_add_rename_patch_carries_new_name
  lines: 338-343
- kind: function
  qualified_name: tests/test_store:test_delete_and_rename_patches_require_existing_symbol
  lines: 346-350
- kind: function
  qualified_name: tests/test_store:test_grouped_patches_include_kind
  lines: 353-359
- kind: function
  qualified_name: tests/test_store:test_add_and_group_create_patches
  lines: 362-376
- kind: function
  qualified_name: tests/test_store:test_delete_create_patches_by_target
  lines: 379-388
- kind: function
  qualified_name: tests/test_store:test_delete_create_patches_by_session_and_all
  lines: 391-400
- kind: function
  qualified_name: tests/test_store:test_concurrent_access_does_not_raise
  lines: 403-434
incoming_refs: 0
outgoing_refs: 20
---
<!-- trie:section symbol=tests/test_store:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=2d1341b8890e47f362cedf6a759abc378781b43a6f94b51c35b858f92b1a8f77 source_ref=a95486d535aed1c6b87b5026c7d31274c719666f role=test-infrastructure -->
Test suite for the `trie.graph.store` module, verifying Store database operations and patch management functionality.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:store fingerprint=c5420fff5b078bc5c2e95aff6471bdee364032edad5dee901f70ebfc07cd85eb body_fp=5265166b02760249029ce3e15608512615a7d745b13ea2a100d1f95a8a2a2191 source_ref=a95486d535aed1c6b87b5026c7d31274c719666f role=test-infrastructure -->
Pytest fixture that creates a temporary Store instance and ensures cleanup after test completion.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_schema_version_recorded fingerprint=2581df1e7e37dd6979078449702b4844298aace7f2e4a4facfc5eb87a6766f78 body_fp=2cd16a2738563fa5d743d07394affde0d0234f2f77be8a0d5773d9e30c94a664 source_ref=3df998e45be4b2a697de43a24a7dc9bdd57b152b role=test -->
Verifies that Store records the correct schema version in the database on initialization.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_upsert_and_get_file fingerprint=f3b58b4e3b9159727ab6287bf2302a550f35296a8d1eb39f62d33d4cdea3b959 body_fp=1edef73a1d6a1c5f5f6ddd7905f4705e7372824bf07b55cfad0716bcaf6909f0 source_ref=3df998e45be4b2a697de43a24a7dc9bdd57b152b role=test -->
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
<!-- trie:section symbol=tests/test_store:_seed_greet fingerprint=b4f933e9d0fc5f1b3df00d2ecaddadf5acff9c3de6c5276bba5e2df543e155ef body_fp=6cede5dfaafb62598b41b6540260e85f13ac251b6cab4de92c6de01401a9fcbb source_ref=459b5c5d3e63364c6de2c5475ae57476758c3a65 role=test -->
Creates test file `a.py` with a `greet` function and populates the Store with its symbols.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_add_patch_defaults_to_modify_kind fingerprint=606e8dc48e5e2fe6013da111d3a82e4eaeaa94aafddec9495a0d4174c0039186 body_fp=a73a3102cb7fcca9933fc2388f146152a3d75447552975a619f33579883db98c source_ref=459b5c5d3e63364c6de2c5475ae57476758c3a65 role=test -->
Verifies that Store.add_patch() creates patches with "modify" kind and null rename_to by default.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_add_delete_patch fingerprint=33dddbd1aa68979161707f029260a460c813e2a4f445052ece97ff1c18071d3c body_fp=6a5ea260ba308f2cfc7949334898d24a0b1d3e634dc608a873314a52d29b6344 source_ref=459b5c5d3e63364c6de2c5475ae57476758c3a65 role=test -->
Tests Store.add_delete_patch creates a patch record with "delete" kind.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_add_rename_patch_carries_new_name fingerprint=0345c8c472cc1210507249cce3f4707a9e49eb1a9067c88e10ff357ca0d39eed body_fp=82409b89d89a1d291bb6ee6b7c9494b49bf12ac4207f4ff09364093b6585ba76 source_ref=459b5c5d3e63364c6de2c5475ae57476758c3a65 role=test -->
Tests that Store.add_rename_patch correctly stores the new name in the rename_to field.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_delete_and_rename_patches_require_existing_symbol fingerprint=0f82fc6ea84900e12de2e436c4605cc3e70f58bc630e6853a35e11bbecfaf703 body_fp=4f101ad548df42002e716199a738d14220068057c5602b8a066ac19deb251bdc source_ref=459b5c5d3e63364c6de2c5475ae57476758c3a65 role=test -->
Verifies that Store.add_delete_patch and Store.add_rename_patch raise KeyError for nonexistent symbols.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_grouped_patches_include_kind fingerprint=6ed5a206b6d18f5184ebb566b17e6471b1fb1ed8f89b7b34756d662a69eff126 body_fp=a93d730495828e4fbaa4bbfe001903b1f15f30c8f80092a0278592d2d4106dcc source_ref=459b5c5d3e63364c6de2c5475ae57476758c3a65 role=test -->
Tests that grouped patches include kind and rename_to fields when retrieving all patches grouped by symbol.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_add_and_group_create_patches fingerprint=a5714e3fcef688d462c9f2c02ec982d9b2c6c6f8c10d79c7cc3711b841162938 body_fp=9c0c25fa5370773567e4338f67a4c8024a3fdc836c33d2a0c36a6e1e44b89ce5 source_ref=459b5c5d3e63364c6de2c5475ae57476758c3a65 role=test -->
Tests that Store can add create patches and group them by target file.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_delete_create_patches_by_target fingerprint=5779d676f4d936f6ad0cfb6fa4a8f322af52636776ff73404506da7b501bdea8 body_fp=417ca9378d124dbaa4b66791e6f6bc50ba14357ab07e54d10bcba501c7ae91bb source_ref=459b5c5d3e63364c6de2c5475ae57476758c3a65 role=test -->
Tests that Store.delete_create_patches removes only the patch matching the specified target_qname.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_delete_create_patches_by_session_and_all fingerprint=60d3b3d4f38da1eed2dcb3f0644e5c4de216b985873c7367c4b5842abccf6833 body_fp=7a6f8b30fa5c7009fea955745a2b4b5c82e809a7b920b94651f7068f33649dfa source_ref=459b5c5d3e63364c6de2c5475ae57476758c3a65 role=test -->
Verifies Store can delete create patches by session ID and delete all remaining patches.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_store:test_concurrent_access_does_not_raise fingerprint=f77f538ec993ec2bd6ed39e22e21e9b442d79ae54bbc55a3754cd3a8d4932cf3 body_fp=e7aaf940b082ca19f7696fb37501d9fad9586457d04d837738eb4c1d1765133a source_ref=3df998e45be4b2a697de43a24a7dc9bdd57b152b role=test -->
Tests that concurrent Store access from 16 threads does not raise threading-related errors.

- Creates 16 worker threads that each perform 50 iterations of Store operations
- Uses threading.Barrier to synchronize thread startup for maximum contention
- Verifies no OperationalError or recursive cursor use exceptions occur
<!-- trie:end -->