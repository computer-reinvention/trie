---
trie_version: 0.1.5
source: trie/graph/store.py
file_fingerprint: 7db5acbd595b0ea2632ef2ae890d94d99ceb4c41873c960cce2eefc2d7d8290d
last_synced_at: '2026-06-10T13:16:09Z'
defines:
- kind: module
  qualified_name: trie/graph/store:__module__
  lines: 1-1270
- kind: constant
  qualified_name: trie/graph/store:SCHEMA_VERSION
  lines: 15-15
- kind: constant
  qualified_name: trie/graph/store:SCHEMA_SQL
  lines: 19-102
- kind: class
  qualified_name: trie/graph/store:FileRecord
  lines: 106-109
- kind: class
  qualified_name: trie/graph/store:FileStats
  lines: 113-116
- kind: class
  qualified_name: trie/graph/store:SymbolHit
  lines: 120-127
- kind: class
  qualified_name: trie/graph/store:SymbolDetail
  lines: 131-153
- kind: class
  qualified_name: trie/graph/store:GrepPredicate
  lines: 157-176
- kind: function
  qualified_name: trie/graph/store:_synchronized
  lines: 179-196
- kind: function
  qualified_name: trie/graph/store:_synchronize_store
  lines: 199-216
- kind: class
  qualified_name: trie/graph/store:Store
  lines: 220-1269
- kind: method
  qualified_name: trie/graph/store:Store.__init__
  lines: 229-242
- kind: method
  qualified_name: trie/graph/store:Store._open
  lines: 244-270
- kind: method
  qualified_name: trie/graph/store:Store.close
  lines: 272-273
- kind: method
  qualified_name: trie/graph/store:Store.__enter__
  lines: 275-276
- kind: method
  qualified_name: trie/graph/store:Store.__exit__
  lines: 278-279
- kind: method
  qualified_name: trie/graph/store:Store.transaction
  lines: 282-288
- kind: method
  qualified_name: trie/graph/store:Store.get_file
  lines: 292-297
- kind: method
  qualified_name: trie/graph/store:Store.upsert_file
  lines: 299-310
- kind: method
  qualified_name: trie/graph/store:Store.delete_file
  lines: 312-314
- kind: method
  qualified_name: trie/graph/store:Store.list_files
  lines: 316-322
- kind: method
  qualified_name: trie/graph/store:Store.replace_file_symbols
  lines: 326-355
- kind: method
  qualified_name: trie/graph/store:Store.count_symbols
  lines: 357-368
- kind: method
  qualified_name: trie/graph/store:Store.count_section_records
  lines: 370-372
- kind: method
  qualified_name: trie/graph/store:Store.count_symbols_missing_role
  lines: 374-391
- kind: method
  qualified_name: trie/graph/store:Store.replace_all_edges
  lines: 395-426
- kind: method
  qualified_name: trie/graph/store:Store.references_in
  lines: 428-440
- kind: method
  qualified_name: trie/graph/store:Store.references_in_with_files
  lines: 442-454
- kind: method
  qualified_name: trie/graph/store:Store.qnames_in_file
  lines: 456-462
- kind: method
  qualified_name: trie/graph/store:Store.symbols_in_file_with_lines
  lines: 464-483
- kind: method
  qualified_name: trie/graph/store:Store.search_symbols
  lines: 485-512
- kind: method
  qualified_name: trie/graph/store:Store.references_out
  lines: 514-526
- kind: method
  qualified_name: trie/graph/store:Store.count_edges
  lines: 528-529
- kind: method
  qualified_name: trie/graph/store:Store.inbound_count_per_symbol
  lines: 531-540
- kind: method
  qualified_name: trie/graph/store:Store.file_ref_counts
  lines: 542-573
- kind: method
  qualified_name: trie/graph/store:Store.file_stats
  lines: 575-597
- kind: method
  qualified_name: trie/graph/store:Store.upsert_section_record
  lines: 601-679
- kind: method
  qualified_name: trie/graph/store:Store.one_liner_for
  lines: 681-694
- kind: method
  qualified_name: trie/graph/store:Store.one_liners_for
  lines: 696-709
- kind: method
  qualified_name: trie/graph/store:Store.historical_mass_all
  lines: 711-742
- kind: method
  qualified_name: trie/graph/store:Store.add_patch
  lines: 746-778
- kind: method
  qualified_name: trie/graph/store:Store.add_delete_patch
  lines: 780-782
- kind: method
  qualified_name: trie/graph/store:Store.add_rename_patch
  lines: 784-786
- kind: method
  qualified_name: trie/graph/store:Store.add_create_patch
  lines: 788-814
- kind: method
  qualified_name: trie/graph/store:Store.get_create_patches_grouped
  lines: 816-838
- kind: method
  qualified_name: trie/graph/store:Store.delete_create_patches
  lines: 840-864
- kind: method
  qualified_name: trie/graph/store:Store.get_patches_for_qname
  lines: 866-875
- kind: method
  qualified_name: trie/graph/store:Store._get_patches_by_symbol_id
  lines: 877-894
- kind: method
  qualified_name: trie/graph/store:Store.get_all_patches_grouped
  lines: 896-919
- kind: method
  qualified_name: trie/graph/store:Store.delete_patches
  lines: 921-955
- kind: method
  qualified_name: trie/graph/store:Store.get_patched_qnames
  lines: 957-965
- kind: method
  qualified_name: trie/graph/store:Store.patch_count_for_symbol
  lines: 967-973
- kind: method
  qualified_name: trie/graph/store:Store.patch_summary
  lines: 975-1004
- kind: method
  qualified_name: trie/graph/store:Store.get_symbol_detail
  lines: 1008-1056
- kind: method
  qualified_name: trie/graph/store:Store.grep_symbols
  lines: 1058-1162
- kind: method
  qualified_name: trie/graph/store:Store.all_symbol_names
  lines: 1164-1167
- kind: method
  qualified_name: trie/graph/store:Store.all_qualified_names
  lines: 1169-1172
- kind: method
  qualified_name: trie/graph/store:Store.survey_symbols
  lines: 1174-1193
- kind: method
  qualified_name: trie/graph/store:Store.find_paths
  lines: 1195-1269
incoming_refs: 123
outgoing_refs: 2
---
<!-- trie:section symbol=trie/graph/store:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=6f905ee5b88763bc3efda571c4cc279538d18efe8ee96eddcd1224a9d34490e2 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
SQLite-backed persistence layer for trie's symbol graph, file fingerprints, and documentation metadata.

- Stores parsed symbols with cross-references as a queryable graph
- Caches file fingerprints to enable incremental scanning
- Tracks triefact section metadata including LLM-inferred roles and boundaries
- Supports patch management for pending documentation updates
- Provides search, path-finding, and batch operations for agent tools
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:SCHEMA_VERSION fingerprint=af8f236b323a21430d1b518fa4344b277391f114013b0d70fa465fc3d0add0e1 body_fp=6a09e5a6737a4a1a5d051ca7dcd499b0b89812f914c6a1cbb2d50b95edffa080 source_ref=dd47f824faeb09b6106e6961b05962e87fe03c05 role=config -->
Version number for the SQLite database schema, triggering recreation when incremented.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:SCHEMA_SQL fingerprint=7cee1415a5555416a1675079288d2a0a887ae388cecca9e52b3e38523e9d32b6 body_fp=63d4e2eeb7c45ddff2f267923c2561563ed157f4b9be4a465e15f0095969c20e source_ref=dd47f824faeb09b6106e6961b05962e87fe03c05 role=model -->
Defines SQLite schema for trie's symbol graph database with tables for files, symbols, edges, triefact sections, and patches.

- `files`: tracks file paths, fingerprints, and scan timestamps
- `symbols`: stores parsed symbol metadata including qualified names, signatures, and line ranges
- `edges`: represents call/reference relationships between symbols with edge kind classification
- `triefact_sections`: caches generated documentation sections with LLM-inferred roles, boundaries, and historical attention mass
- `patches`: stores pending symbol modifications with kind (modify/delete/rename) and optional rename targets
- `create_patches`: stores pending symbol creations targeting non-existent symbols
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:FileRecord fingerprint=9e5bd64fbbf95f8eb3616b9da3d84b73687a569550e6ace513eef354bd16b1e1 body_fp=69e2f399080b208d3c7ccbb3aa97c6e5d2cd61f0c15b47f94fd56a371feab89a source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=model -->
Immutable record storing file path, content fingerprint, and last scan timestamp.

- `fingerprint`: content hash for detecting file changes
- `last_scanned_at`: Unix timestamp of most recent scan
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:FileStats fingerprint=c724d544428a38f276d944f8e7e7b5ad7459d6b1a250e18b87c7d3031e7a4b40 body_fp=48b2465dc92205407be80ea6888eefa1c03f4fb7b692a5e88dee304506e48d2b source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=model -->
Immutable record containing per-file symbol counts returned by Store.file_stats.

- `public_symbols`: legacy field name; equals `total_symbols` under current implementation
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:SymbolHit fingerprint=c97f130190c9d3e96d5d1b0be1314de0ae372cc1d5256f00b330cad27aac1b3e body_fp=93bac69bb367bb12ed26e699829f26a14e8e57a30edf5a6e79b69f2b9d009eda source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=model -->
Immutable data record for symbol search results returned by `Store.search_symbols`.

- `name`: Local symbol name (not qualified)
- `qualified_name`: Full dotted path including module/class hierarchy
- `signature`: Function/method signature string; `None` for non-callable symbols
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:SymbolDetail fingerprint=1e515ecffc52bd585a648f1bb56ec9457c55025ee03662bbb8207af081253cc1 body_fp=57c2000e6c177d1fd27ca8c3d789b10d4f340ba3b440e6aef3aa104b0e7452be source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=model -->
Full per-symbol record with graph counts and cached one-liner for MCP tools.

- `one_liner`: empty string when no triefact section exists
- `role`: LLM-inferred architectural role tag, empty when unknown
- `boundary`: LLM-inferred boundary class (entry/exit/internal), empty when unknown
- `decorators`: newline-joined decorator lines, empty when none
- `pending_patches`: list of patch dictionaries for this symbol
- `pending_patch_count`: number of pending patches
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:GrepPredicate fingerprint=bb94fc53eb9ffe605f051d331b0b74099549200f353c204750e987092d9ac0e6 body_fp=13c49693f77698ef612a29e932bd8c64f0f9b485973a915252a8bc3abe0b4ac5 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=model -->
Server-side filter object for symbol search queries in Store.grep_symbols.

- `name_contains`: substring match against symbol name
- `scope_prefix`: file path prefix filter
- `scope_exclude`: tuple of file path prefixes to exclude
- `inbound_count_min/max`: edge count range filters for incoming references
- `outbound_count_min/max`: edge count range filters for outgoing references
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:_synchronized fingerprint=c94c45b26af5cc2b0f699d277c3b8f0b0b6cb111ffccb411c1975b0481c9333f body_fp=c7e75454a8f2b7f1565ed5eb80b01af9c9bd10a154092e924f2cb357a362dc99 source_ref=745f21ee2948bc12ab64d268d7880452f6a96d0b role=util -->
Wraps a Store method to execute its entire body under `self._lock` for SQLite thread safety.

- Prevents concurrent access to the shared connection which causes misleading SQLite errors
- Returns a wrapper function that acquires the re-entrant lock before calling the original method
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:_synchronize_store fingerprint=d1b9aace629d6d0844b4d70d2944ac013cb73c7b14e7e0eba36652fd84d9533f body_fp=09442efa62629e536a5e5e6f7f0c22cf1afbd4576dfc2cd2199d11ad7eb24fe4 source_ref=745f21ee2948bc12ab64d268d7880452f6a96d0b role=util -->
Decorates a class to apply `_synchronized` to all public methods for thread-safe database access.

- Skips dunder methods and the `transaction` contextmanager to avoid lock conflicts
- Only wraps callable instance methods, not static or class methods
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store fingerprint=2cc3d98f8059d719ff97cc35e1ecebb8bcf5f457626c068f54bb9227c792d2ac body_fp=1a89d9d8f6785e81b845ceeabd1f91c94e4f88c27f45f5a975b09ff0a72231f7 source_ref=dd47f824faeb09b6106e6961b05962e87fe03c05 role=persistence -->
SQLite-backed persistence for trie's symbol graph and file fingerprints.

Store provides thread-safe access to a SQLite database containing files, symbols, reference edges, triefact sections, and patches. All schema is auto-created and version-bumped when stale. The connection uses a re-entrant lock to guard concurrent access from worker threads during wave-based sync.

- `db_path`: Database file path, created with parent directories if needed
- `_lock`: Threading RLock protecting all connection operations  
- `_conn`: SQLite connection with foreign keys enabled
- File operations: track fingerprints and scan timestamps for incremental updates
- Symbol operations: store parsed symbols with metadata like qualified names, signatures, line ranges
- Edge operations: maintain reference graph between symbols, filtering external/self-references, storing edge kind
- Section operations: cache generated triefact one-liners and LLM-inferred role/boundary tags, track historical mass for attention decay
- Patch operations: store pending documentation corrections with session tracking, including creation patches for new symbols
- Query methods: search symbols by name patterns, get details with edge counts, find call paths
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.__init__ fingerprint=96b28781440a25c3d116c96dc0909cc81a80b4ab488857c0f7339c90620fdcb4 body_fp=4f8441c77049399d4a8cee059c8e9d78d7c5345ba519d8245509292950a51ca4 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=orchestration -->
Store initializer creates a re-entrant lock, database directory, and opens the SQLite connection.

- Creates parent directories if they don't exist
- Initializes threading lock to guard concurrent access to connection
- Calls `_open()` to establish connection and apply schema
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store._open fingerprint=2db77cc3475ec4448fea96703d16cab52d1530182b8118e946b15feccd865d62 body_fp=9fdb0da63fed96a2e52027b2136e5deabeef4357ae4dbb81965ef97b7715ac46 source_ref=745f21ee2948bc12ab64d268d7880452f6a96d0b role=persistence -->
Store._open opens SQLite connection and initializes/migrates the database schema.

- Detects schema version mismatches and deletes stale database files
- Enables foreign key constraints via PRAGMA
- Creates tables from SCHEMA_SQL if not present
- Inserts current SCHEMA_VERSION on fresh database creation
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.close fingerprint=a913f96235959366c1550f3902f93fb0cb6321b2a3dd492c780b5af0ba6b8e7b body_fp=98f31ca518d69b57bba5fdfbfc3c96ac65744a91df545d8a61a60fc5e8cc74c2 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
Closes the Store's SQLite connection.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.__enter__ fingerprint=9f210cb9718c0e2ccf1afd3e1a8f2d55beb6c6390abbe06ed35fdd33a7172f7f body_fp=2528fd41a394239f4067269aebd5f7269ff6e3f0ae5afaa317f5824aba39bbe8 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=util -->
Returns the Store instance for context manager entry.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.__exit__ fingerprint=67b1b6b146522ac7c8bdfff45bab8a41537d8e61231b937b0475a712971729e7 body_fp=79c4706aba3baab3601c54630b3e809e12d56e48f2952516541aaf4ce43455db source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=util -->
Store context manager exit method that closes the SQLite connection.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.transaction fingerprint=92d85419eab7f0eb88451072a4fe4fd3da121109143afd8912055c863389d51b body_fp=68e90f0886394175affe4344a06e6e211f2b292a3c309a044cb73826f4f6bb2e source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=util -->
Wraps Store database operations in a context manager that commits on success and rolls back on exceptions.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.get_file fingerprint=eb7697a3a025059d896bd28c96b0f208e7ee3dc597aa5702581ea24d86dcb5de body_fp=50a6fc466cfbf0bbe367d1edaca2e9373a9df3f7f743dbe237c5fd13627ccb9f source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
Store.get_file retrieves a FileRecord for the given path from the files table.

- Returns None if no record exists for the path.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.upsert_file fingerprint=6d8542fa2fb58dc7c77adab00e96758e35a7b4106aca18f02c39064c1ff2eeb6 body_fp=9039f4b543b0e1c7ed60d6078eff9e04e42e601402fa989bd53c3bdb08f970e4 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
Store.upsert_file inserts or updates a file record with path, fingerprint, and scan timestamp.

- `now`: optional timestamp override; defaults to current time if None
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.delete_file fingerprint=3cc0d8d1dfff6afab640378b3cec46ac06299bab51b118ae1e695914bcdb5e9d body_fp=fa33109c2d6952813f78c81d5c23b845d29fb95ff6ec209c76ac83009eb6adf6 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
Store.delete_file removes a file record from the database and commits the transaction.

- Cascades to delete all associated symbols due to foreign key constraints
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.list_files fingerprint=0ad09ddc7d8033f74e03712636d0159e4ad107c8be9c4d803563162dc7be55c5 body_fp=6871936600b9f5efb705a7f5befc09beb23f544275a9ab6e88d307a2cad8e8d2 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
Returns all FileRecord instances from the database, ordered by path.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.replace_file_symbols fingerprint=40b1980316c50d05be01ab45d27176c3428961e7489644041c1872db015f19c1 body_fp=fc37f7bf5cb73fbdb1b8de623f3b852c56e7925cb0936e30f3c400bc4cbf3cde source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
Store.replace_file_symbols atomically deletes all existing symbols for a file and inserts new ones from the provided list.

- Uses a transaction to ensure atomicity between deletion and insertion
- Converts Symbol objects to database row tuples with proper type casting
- Joins decorator lists with newlines for storage
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.count_symbols fingerprint=2580fe16b3b00ec0a0343c0d528630dd899ab90e6d1a008d340e1aa6c5d92002 body_fp=d68eda0afbc5e9483487a08689e61be7d684b178b1bc9e21a6f17e8cccdbd77f source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
Count symbols in the database with optional file and visibility filtering.

- `file_path`: when provided, count only symbols in that file
- `public_only`: when True, count only symbols marked as public
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.count_section_records fingerprint=610f302acb473963e5a29105d08a8808237b8ffa314427ab6ac1f9a61e853fbe body_fp=8a7f36b9abb46d40e4d3df142b62921e8117d4c343864fb86686d48911cbeabf source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
Store.count_section_records returns the number of rows in the triefact_sections table.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.count_symbols_missing_role fingerprint=b561b4d71aee1cc5a1c9bd9db7eb9512fd5929bdd36a0d3d108e502a516c06cd body_fp=d7a549ec4e33631720283a424a007c49e91be58fe63fcd075ced151475db9fdf source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
Store.count_symbols_missing_role counts symbols without non-empty role tags in triefact_sections.

- Returns symbols with no section record or empty role string
- Used to short-circuit role auto-backfill when all symbols are tagged
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.replace_all_edges fingerprint=41beb7afd9fb09d3072e05b524261ba259d6f9ecaed8f6ea1dc7126e95a5608a body_fp=19d50dc47df7c68b40f843b5d7f4d183f4e06ad4422f1dfcc5628481b7e68d60 source_ref=dd47f824faeb09b6106e6961b05962e87fe03c05 role=persistence -->
Store method that wipes the edges table, resolves references to symbol IDs, and inserts new edges.

- Drops references where source or destination qualified names aren't found in symbols table
- Deduplicates identical edges and skips self-references
- Stores reference kind alongside edge source and destination IDs
- Returns count of edges actually inserted
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.references_in fingerprint=a64405c25c8effa2d37a933ece61b1b112c7cc2bc999fd7d05000ede0188ddc7 body_fp=dd53fa96d7318710482a05bea31d7b39d521f712f422505935328a443acbfd1a source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
Store.references_in returns qualified names of all symbols that reference the given qualified name.

- `qualified_name`: target symbol to find incoming references to
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.references_in_with_files fingerprint=773412d3d4e3f39ea3f1a7f9a058c6cf53d88e3ec7a563822446a9c4e2f271fe body_fp=dbc7b3dec9075efd4740130d8770c0bc55cf208b6131bdbdaf078f8d08adadc8 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
Store.references_in_with_files returns `(src_qname, src_file_path)` tuples for every symbol that references the given `qualified_name`.

- Extends `references_in` by including the file path of each referencing symbol
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.qnames_in_file fingerprint=0345839c8b81209c9f8e501ba0bbd84b97b79bcdffd157276f2c5f9433f1bf53 body_fp=7c9dd2be6706cdcdd17fa2a973943e3284d98f7700200cc253b0d901e95e0102 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
Store.qnames_in_file returns qualified names of all symbols defined in the given file path, ordered by start line.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.symbols_in_file_with_lines fingerprint=6c50f1692f561e61d68233e23f1452068b7dc5151923fcf1a75c9e9f32d8fc97 body_fp=585b4e06b98e3dfc5f57a888616c5b7edb994658e8d6ec2ae4d4b89efd93fe02 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
Store.symbols_in_file_with_lines returns qualified names and line ranges for symbols in a file, ordered by start line.

- Returns tuples of `(qname, start_line, end_line)` for line bracket calculations
- Used by locate's grep fallback to map source lines to enclosing symbols
- Returns empty list if file has no recorded symbols or doesn't exist
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.search_symbols fingerprint=843fc4a051517ce70282ea2a98897dd8f7258793682bd113ad354a6fc4c517f6 body_fp=b07642064e8917e154033e3c0e72dac26ac5188f59f8ca86d0db8647060874bb source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=api -->
Finds symbols whose local name contains a pattern via case-insensitive substring match.

- Returns up to `limit` `SymbolHit` instances ordered by public symbols first
- Searches the `name` field (local part) not the fully qualified name
- Designed for agent "find_symbol" queries that typically use local names
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.references_out fingerprint=a6810cd7afde7caf6868995ebd2d05049eb7e7d1f292600fc55fed2112ad0138 body_fp=735ee0d0262bc1091f50f4ecb36ac823778a212317ce886aa65e26138db75817 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
Returns qualified names of all symbols referenced by the given symbol.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.count_edges fingerprint=dd4f0506260e96b70c2e6c1cf90803909315a59857fe188eb5f56d47f7d9d49d body_fp=76010464946ee977eaa8ca8e9f7e82748d2ab16b8fe0601c016a4ccc8df46edb source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
Store.count_edges returns the total number of edges in the graph database.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.inbound_count_per_symbol fingerprint=d02ef2425e589304c3c468f57c53c886dd73de83d538963d490f437f8fdb19c2 body_fp=e9f37d89d2eb1efb93113aa555174551d03e01f4d934e0eceac89496ffc92b02 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=domain -->
Store.inbound_count_per_symbol returns a dictionary mapping qualified names to their inbound edge counts.

- Used to detect hub symbols with many incoming references
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.file_ref_counts fingerprint=bf982e54730e691d4f235e2ea25f000e8eb351ce5f091f72ab4a025d077abe4d body_fp=937140429a4e663eea66b9c39335bb4c528ff281b39ec03c89589e45fa51b405 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
Store.file_ref_counts returns cross-file inbound and outbound reference counts for a file.

- Inbound: references to symbols in this file from symbols in other files
- Outbound: references from symbols in this file to symbols in other files
- Excludes intra-file edges between symbols within the same file
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.file_stats fingerprint=818ee47e02de6186ac43c3deb53c5ddc50df1980e52047b405fca30d50d264d6 body_fp=826f73836081b81f89a68eda610b4522cdadc060b24451fbc0c4d91bf537b1db source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
Returns per-file symbol counts from the Store for bootstrap ranking.

- `public_symbols` field is legacy naming; equals total_symbols count under current parser
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.upsert_section_record fingerprint=3942b3fc9510f3f36111f1270810c23831716b052541459a3cd795381560d48f body_fp=929f2500905df2a371dedc76f258f113e48944dedd5539c34775852bc741d2a2 source_ref=dd47f824faeb09b6106e6961b05962e87fe03c05 role=persistence -->
Records or refreshes Store triefact section metadata for a symbol with LLM-inferred tags and historical mass.

- Silently skips if symbol no longer exists in database
- Empty role/boundary values preserve existing non-empty values during updates
- Zero hist_mass preserves existing non-zero values during updates
- Commits transaction immediately after upsert
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.one_liner_for fingerprint=1f204b6ac59d246ef09d1541e51816e9a3261e8bcd10c625cb2b426a5c5dbaaa body_fp=61c0d0acfc5b88ef5796795fb10f13d98f4e13ae7bec7102313f2ffaada710bb source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
Store.one_liner_for returns the cached one-liner documentation for a symbol by qualified name, or empty string if none exists.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.one_liners_for fingerprint=41fe88c62a162851d437d2e65cd15c753d88bdc5f4d13d59609b2ab4f92550b4 body_fp=6e1be331518a1dfa903f5d6321e165f839a6f24b9a5936bb70e5d04d692a3892 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
Store method that batch-retrieves cached one-liners for multiple symbol qualified names.

- Returns dictionary mapping qualified names to their cached one-liners
- Only includes entries found in triefact_sections table; missing symbols are omitted
- Empty one-liners are normalized to empty strings in the result
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.historical_mass_all fingerprint=587d5f960400265e9e4e400ca49d56d104ff85e007ba104d96731171f4132940 body_fp=2205918257936485589f57594e18380bf41848fcf32957688d96862bddaa45c7 source_ref=dd47f824faeb09b6106e6961b05962e87fe03c05 role=persistence -->
Returns decayed historical attention mass for all symbols with non-zero AGM values.

- Applies exponential decay from stored timestamp to current time using AGM half-life
- Mass sourced from triefact_sections.hist_mass (cached from triefact sentinels)
- Omits symbols with zero mass entirely
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.add_patch fingerprint=c540848c729742b267865b443ba70474c9ffba20841b552eafa72d11550529aa body_fp=d371c5dd9ce55b0b49dd7bdb696678bee4e3115da7c9cfc86a6409007dd46564 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
Store.add_patch inserts a patch record for the symbol with given qualified name and returns the new patch ID.

- `kind` defaults to "modify"; accepts "modify", "delete", or "rename"
- `rename_to` specifies the new local name when `kind` is "rename"
- Raises `KeyError` if the qualified name doesn't exist in the symbols table
- Returns the database-generated patch ID on success
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.add_delete_patch fingerprint=a20fe579a52fe50e5cb946c96461ef74dcbca5bc0ba560a4877bab37796c5b98 body_fp=3493116ad8cb9e5b9d4cb0d4be8f421f0530b3f189d83a57aec216cbac24b28d source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
Stages a deletion patch for an existing symbol by qname, raising KeyError if the symbol doesn't exist.

- Delegates to `add_patch` with empty note and kind="delete"
- Returns the new patch ID on success
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.add_rename_patch fingerprint=5ec878db09687bb2af48f86ca34e8f19c5a90c248c1d6d9a47627f874624f506 body_fp=2e9e8e23115a49cff89da873b2889ae0a8a1535efca9e1e3cbdd1f3937d9b0ce source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
Stages a rename patch for an existing symbol to the specified local name.

- `new_name`: the new local name (not qualified name) for the symbol
- Returns the new patch ID
- Raises KeyError if the symbol doesn't exist
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.add_create_patch fingerprint=5f404888744632f95f296e341da34e919e8a80a325315c80327e8c38e5f521a4 body_fp=78e900f8f44e03b857eab69daace8b015ad3eb4091d3284d01e541d6eb145909 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
Store method inserts a create_patch record for a new symbol that doesn't exist yet.

- Returns the database row id of the inserted patch record
- `anchor_qname` specifies location context for symbol placement
- `parent_class` indicates class membership for new methods
- Does not validate target_qname absence (caller responsibility)
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.get_create_patches_grouped fingerprint=7d8b1b54d9652e884dd0ef5328d60c0fbc7c08301ea60b6fc95318cb0e501741 body_fp=1ca5d01f578a85174a84a322680b3b4d9f9cd33bdef540eb3041646f612f9383 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
Retrieves all pending create patches from the Store, grouped by target_file.

- Returns a dict mapping target_file paths to lists of create patch records
- Each patch record contains all create_patches table fields as a dict
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.delete_create_patches fingerprint=f5ee8cd63465f9f99615fd905f904caac138ba603909cdeed45f6c2d6742e977 body_fp=841dab485bbe6c12d42299dc291a0c3544cd17c3c849692f990d18a66202a56f source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
Delete create patches by target_qname, session_id, or all patches, returning count of deleted rows.

- `target_qname`: delete patches creating this qualified name
- `session_id`: delete patches from this agent session  
- `all`: delete all create patches (overrides other filters)
- Returns 0 if no matching criteria specified
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.get_patches_for_qname fingerprint=99cf3d176ccf53de862a8deb7087fe8c39df8552d648c1cafb1bd48c038fa021 body_fp=2e8133cc3626fa6a3a0be6d8fbe2104de3bcf7be532c1d2e8edf01abd7fd90c6 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
Store.get_patches_for_qname returns all pending patches for a symbol as dicts.

- Returns empty list when qualified name has no corresponding symbol record
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store._get_patches_by_symbol_id fingerprint=feedff9fd5024f7c3303fba4f61fd961a6a5596ed968b03ecb7fe2c6776507ff body_fp=324c0ce8a1d530ce469070a39c3fc7b6d24f7f7464c282b511393745dea0b966 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
Store._get_patches_by_symbol_id retrieves all pending patches for the given symbol_id as dictionary records.

- Returns list of patch dicts with keys: id, note, reason, session_id, created_at, kind, rename_to
- Results ordered by patch id (creation order)
- kind defaults to "modify" when database value is null
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.get_all_patches_grouped fingerprint=994b7e84d50bd5477f8242576862c940b1c747a47938659fc23c17bf137591cb body_fp=0fd992e281ceb326b2972533f4ed4b65c4ec56bb1e259f4a365bc3da3ba7b3e6 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
Store.get_all_patches_grouped returns pending patches organized by symbol_id.

- Returns dict mapping symbol_id to list of patch records with id, note, reason, session_id, created_at, kind, rename_to
- Ordered by symbol_id then patch id
- Kind defaults to 'modify' when null
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.delete_patches fingerprint=c1457117713979a51e97ee435994b5d9819075c1f5bce24aaa7f31c328e1f99d body_fp=462bc3bf41ddea2e18aebe8a1b855b1545ed2c568c0c786562b405e530b97a34 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
Store method that deletes patches matching specified criteria and returns count of deleted rows.

- `qname`: Delete all patches for a specific symbol's qualified name
- `session_id`: Delete all patches created in a specific session
- `all`: Delete all patches in the database
- At least one parameter must be specified
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.get_patched_qnames fingerprint=0e2e2afe6da23a44267b7db00a8fdca0a377fddfffb84b1d624128b0a1eb5136 body_fp=9e56083073be85dcbbf4298d9e3e4f419bd713d2ef65c3d227ceea86414b173b source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
Store.get_patched_qnames returns all symbol qualified names that have pending patches.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.patch_count_for_symbol fingerprint=0b9529da6e2ea49324486ddca6f3b682563b67ac8c3504c0249c1bebbb9dc8bd body_fp=85d900e9e27b9e8dd7fbeedae268ef343e56608b6e6477c8f8bfad39293cf605 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
Store.patch_count_for_symbol returns the count of pending patches for a given symbol_id.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.patch_summary fingerprint=4c1992182c3e5535231c479a8571c56c91c8a8190a889a5e31671db82e46106b body_fp=8322a4da05ac51789356b0ef29ee78a56d952be76d732bb9dd9a19aa357d19e0 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
Store.patch_summary aggregates pending-patch state into counts and classifications by session origin.

- `total_patches`: total number of patch rows across all symbols
- `symbol_count`: number of distinct symbols with pending patches
- `create_count`: number of create_patches (new symbols to be created)
- `by_origin`: symbols bucketed by patch session type (agent/cascade/mixed)
- `qnames`: sorted list of qualified names having pending patches
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.get_symbol_detail fingerprint=36a84ec98936b9f4f1c0523d443824942263414e0a24746ded84d93e76f5eff1 body_fp=258c4b6e8b4537931875e26ee2b61909ebd989793870ce2bc7859b247328b4f8 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=domain -->
Store.get_symbol_detail retrieves complete symbol metadata and graph metrics for an agent query in one roundtrip.

- Returns None if qualified_name is not found
- Includes inbound/outbound edge counts, cached one-liner, role/boundary tags, decorators, and pending patches
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.grep_symbols fingerprint=e78b8da8b52fe6745f7650acdc19da820d8037915bd2cbb2c50c4550cbf71e49 body_fp=2e7cb2886ec3b5ae6d2ac3a2f016fefedbfcdbc51192b9aaaa9c89500f88de88 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
Store.grep_symbols searches symbols using predicate filters, returning SymbolDetail objects sorted by rank_by.

- `rank_by`: "public_first", "inbound_count", or "alphabetical" (defaults to "public_first")
- Edge count filters use scalar subqueries repeated in WHERE clause due to SQLite resolution order
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.all_symbol_names fingerprint=fd7275a10e4d910bbe493d3316de5e7e152c08eabc201043b81db9d247002f65 body_fp=192316a90c2b00ad9f61cd30e388c87d204ff74d8644a4f3cb87e4008aad330e source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=util -->
Returns all distinct local symbol names from the symbols table for fuzzy-match suggestions.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.all_qualified_names fingerprint=81e36419552fcadd1ffbad7e8109246d3055e765019c0633cfcabdafa0ad9eff body_fp=e8b4083ed5bdeabf6cd7ee2b212f4d2b24b914944fcf91b7f52aaeb5f67f76ab source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=util -->
Returns all qualified names from the symbols table as a list of strings.

- Used by suggest systems for near-miss matching when explain/walk operations fail to find symbols
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.survey_symbols fingerprint=f68870a5028109f1a34ab0b012829014f156b48313c712e0bc9d0b20d440bcc9 body_fp=8f3ce460e796a14aca02e325b69fc22760d10d1b13b430ed9fc8539fae6680b1 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
Store.survey_symbols returns tuples of (qualified_name, kind, one_liner, file_path) for all symbols, optionally filtered to public ones.

- `public_only`: when True, filters to symbols where is_public=1
- Returns empty string for one_liner when no triefact section exists
- Results ordered by file_path then start_line
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.find_paths fingerprint=1e0bfe75b333b57d1f17f2fd413879fcc9f8615e5c9313a5804159d4e9eaa1b9 body_fp=74407c7cda35c5c5fd23c875810b5deafce99b645f4cc0a2f42858e5021e1e3f source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=domain -->
Store.find_paths performs breadth-first search to find shortest call paths between two symbols.

- Returns list of qualified name sequences from `from_qname` to `to_qname` following callee edges
- Limits search by `max_depth` hops, `max_paths` results, skips cycles and high-fanin hubs
- Empty return when no path exists within constraints
- For reverse direction (caller chains), swap the arguments
<!-- trie:end -->