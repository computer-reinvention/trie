---
trie_version: 0.1.5
source: trie/graph/store.py
file_fingerprint: 68bce47c31367d1848650eab42f4ff27a82bf4b12c58d6e9db1a3d5f3f9e5b75
last_synced_at: '2026-06-06T13:43:46Z'
defines:
- kind: module
  qualified_name: trie/graph/store:__module__
  lines: 1-1013
- kind: constant
  qualified_name: trie/graph/store:SCHEMA_VERSION
  lines: 14-14
- kind: constant
  qualified_name: trie/graph/store:SCHEMA_SQL
  lines: 18-79
- kind: class
  qualified_name: trie/graph/store:FileRecord
  lines: 83-86
- kind: class
  qualified_name: trie/graph/store:FileStats
  lines: 90-93
- kind: class
  qualified_name: trie/graph/store:SymbolHit
  lines: 97-104
- kind: class
  qualified_name: trie/graph/store:SymbolDetail
  lines: 108-130
- kind: class
  qualified_name: trie/graph/store:GrepPredicate
  lines: 134-153
- kind: class
  qualified_name: trie/graph/store:Store
  lines: 156-1012
- kind: method
  qualified_name: trie/graph/store:Store.__init__
  lines: 165-175
- kind: method
  qualified_name: trie/graph/store:Store._open
  lines: 177-200
- kind: method
  qualified_name: trie/graph/store:Store.close
  lines: 202-203
- kind: method
  qualified_name: trie/graph/store:Store.__enter__
  lines: 205-206
- kind: method
  qualified_name: trie/graph/store:Store.__exit__
  lines: 208-209
- kind: method
  qualified_name: trie/graph/store:Store.transaction
  lines: 212-218
- kind: method
  qualified_name: trie/graph/store:Store.get_file
  lines: 222-227
- kind: method
  qualified_name: trie/graph/store:Store.upsert_file
  lines: 229-240
- kind: method
  qualified_name: trie/graph/store:Store.delete_file
  lines: 242-244
- kind: method
  qualified_name: trie/graph/store:Store.list_files
  lines: 246-252
- kind: method
  qualified_name: trie/graph/store:Store.replace_file_symbols
  lines: 256-285
- kind: method
  qualified_name: trie/graph/store:Store.count_symbols
  lines: 287-298
- kind: method
  qualified_name: trie/graph/store:Store.count_section_records
  lines: 300-302
- kind: method
  qualified_name: trie/graph/store:Store.count_symbols_missing_role
  lines: 304-321
- kind: method
  qualified_name: trie/graph/store:Store.replace_all_edges
  lines: 325-356
- kind: method
  qualified_name: trie/graph/store:Store.references_in
  lines: 358-370
- kind: method
  qualified_name: trie/graph/store:Store.references_in_with_files
  lines: 372-384
- kind: method
  qualified_name: trie/graph/store:Store.qnames_in_file
  lines: 386-392
- kind: method
  qualified_name: trie/graph/store:Store.symbols_in_file_with_lines
  lines: 394-413
- kind: method
  qualified_name: trie/graph/store:Store.search_symbols
  lines: 415-442
- kind: method
  qualified_name: trie/graph/store:Store.references_out
  lines: 444-456
- kind: method
  qualified_name: trie/graph/store:Store.count_edges
  lines: 458-459
- kind: method
  qualified_name: trie/graph/store:Store.inbound_count_per_symbol
  lines: 461-470
- kind: method
  qualified_name: trie/graph/store:Store.file_ref_counts
  lines: 472-503
- kind: method
  qualified_name: trie/graph/store:Store.file_stats
  lines: 505-527
- kind: method
  qualified_name: trie/graph/store:Store.upsert_section_record
  lines: 531-583
- kind: method
  qualified_name: trie/graph/store:Store.one_liner_for
  lines: 585-598
- kind: method
  qualified_name: trie/graph/store:Store.one_liners_for
  lines: 600-613
- kind: method
  qualified_name: trie/graph/store:Store.add_patch
  lines: 617-643
- kind: method
  qualified_name: trie/graph/store:Store.get_patches_for_qname
  lines: 645-654
- kind: method
  qualified_name: trie/graph/store:Store._get_patches_by_symbol_id
  lines: 656-670
- kind: method
  qualified_name: trie/graph/store:Store.get_all_patches_grouped
  lines: 672-693
- kind: method
  qualified_name: trie/graph/store:Store.delete_patches
  lines: 695-729
- kind: method
  qualified_name: trie/graph/store:Store.get_patched_qnames
  lines: 731-739
- kind: method
  qualified_name: trie/graph/store:Store.patch_count_for_symbol
  lines: 741-747
- kind: method
  qualified_name: trie/graph/store:Store.get_symbol_detail
  lines: 751-799
- kind: method
  qualified_name: trie/graph/store:Store.grep_symbols
  lines: 801-905
- kind: method
  qualified_name: trie/graph/store:Store.all_symbol_names
  lines: 907-910
- kind: method
  qualified_name: trie/graph/store:Store.all_qualified_names
  lines: 912-915
- kind: method
  qualified_name: trie/graph/store:Store.survey_symbols
  lines: 917-936
- kind: method
  qualified_name: trie/graph/store:Store.find_paths
  lines: 938-1012
incoming_refs: 81
outgoing_refs: 2
---
<!-- trie:section symbol=trie/graph/store:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=6f905ee5b88763bc3efda571c4cc279538d18efe8ee96eddcd1224a9d34490e2 source_ref=a0647ea4e42a6ddac430f66ebd109dd42974af95 role=graph-database -->
SQLite-backed persistence layer for trie's symbol graph, file fingerprints, and documentation metadata.

- Stores parsed symbols with cross-references as a queryable graph
- Caches file fingerprints to enable incremental scanning
- Tracks triefact section metadata including LLM-inferred roles and boundaries
- Supports patch management for pending documentation updates
- Provides search, path-finding, and batch operations for agent tools
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:SCHEMA_VERSION fingerprint=33db9149a65c0fe1350495d641267e115a5d8dbcecbf27b32221c3f544dcfa30 body_fp=6a09e5a6737a4a1a5d051ca7dcd499b0b89812f914c6a1cbb2d50b95edffa080 source_ref=a0647ea4e42a6ddac430f66ebd109dd42974af95 role=graph-database -->
Version number for the SQLite database schema, triggering recreation when incremented.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:SCHEMA_SQL fingerprint=961283584652f15b299b552ea8cab000fa05213cd6085c62a4da76e52d165a6d body_fp=96c0aeda7528388c0b4ff529d2677684cd5ce5cea45fceb5fff3489cfe9f3dbb source_ref=a0647ea4e42a6ddac430f66ebd109dd42974af95 role=graph-database -->
Defines SQLite schema for trie's symbol graph database with tables for files, symbols, edges, triefact sections, and patches.

- `files`: tracks file paths, fingerprints, and scan timestamps
- `symbols`: stores parsed symbol metadata including qualified names, signatures, and line ranges
- `edges`: represents call/reference relationships between symbols
- `triefact_sections`: caches generated documentation sections with LLM-inferred roles and boundaries
- `patches`: stores pending documentation corrections linked to symbols
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:FileRecord fingerprint=9e5bd64fbbf95f8eb3616b9da3d84b73687a569550e6ace513eef354bd16b1e1 body_fp=69e2f399080b208d3c7ccbb3aa97c6e5d2cd61f0c15b47f94fd56a371feab89a source_ref=a0647ea4e42a6ddac430f66ebd109dd42974af95 role=graph-database -->
Immutable record storing file path, content fingerprint, and last scan timestamp.

- `fingerprint`: content hash for detecting file changes
- `last_scanned_at`: Unix timestamp of most recent scan
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:FileStats fingerprint=c724d544428a38f276d944f8e7e7b5ad7459d6b1a250e18b87c7d3031e7a4b40 body_fp=48b2465dc92205407be80ea6888eefa1c03f4fb7b692a5e88dee304506e48d2b source_ref=a0647ea4e42a6ddac430f66ebd109dd42974af95 role=graph-database -->
Immutable record containing per-file symbol counts returned by Store.file_stats.

- `public_symbols`: legacy field name; equals `total_symbols` under current implementation
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:SymbolHit fingerprint=c97f130190c9d3e96d5d1b0be1314de0ae372cc1d5256f00b330cad27aac1b3e body_fp=93bac69bb367bb12ed26e699829f26a14e8e57a30edf5a6e79b69f2b9d009eda source_ref=a0647ea4e42a6ddac430f66ebd109dd42974af95 role=graph-database -->
Immutable data record for symbol search results returned by `Store.search_symbols`.

- `name`: Local symbol name (not qualified)
- `qualified_name`: Full dotted path including module/class hierarchy
- `signature`: Function/method signature string; `None` for non-callable symbols
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:SymbolDetail fingerprint=1e515ecffc52bd585a648f1bb56ec9457c55025ee03662bbb8207af081253cc1 body_fp=57c2000e6c177d1fd27ca8c3d789b10d4f340ba3b440e6aef3aa104b0e7452be source_ref=a0647ea4e42a6ddac430f66ebd109dd42974af95 role=graph-database -->
Full per-symbol record with graph counts and cached one-liner for MCP tools.

- `one_liner`: empty string when no triefact section exists
- `role`: LLM-inferred architectural role tag, empty when unknown
- `boundary`: LLM-inferred boundary class (entry/exit/internal), empty when unknown
- `decorators`: newline-joined decorator lines, empty when none
- `pending_patches`: list of patch dictionaries for this symbol
- `pending_patch_count`: number of pending patches
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:GrepPredicate fingerprint=bb94fc53eb9ffe605f051d331b0b74099549200f353c204750e987092d9ac0e6 body_fp=13c49693f77698ef612a29e932bd8c64f0f9b485973a915252a8bc3abe0b4ac5 source_ref=a0647ea4e42a6ddac430f66ebd109dd42974af95 role=graph-database -->
Server-side filter object for symbol search queries in Store.grep_symbols.

- `name_contains`: substring match against symbol name
- `scope_prefix`: file path prefix filter
- `scope_exclude`: tuple of file path prefixes to exclude
- `inbound_count_min/max`: edge count range filters for incoming references
- `outbound_count_min/max`: edge count range filters for outgoing references
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store fingerprint=fcc5f9dc30039c6afe3b5abf770423b45e234da7f88e5f6a123351c78d4b759b body_fp=2bb3064f3e69b9c69ca31aeed70f081ec71650f3978abc763b690d88df3404bb source_ref=d377be51db8d287924b99f218a4d7de0bed2d060 role=persistence -->
SQLite-backed persistence for trie's symbol graph and file fingerprints.

Store provides thread-safe access to a SQLite database containing files, symbols, reference edges, triefact sections, and patches. All schema is auto-created and version-bumped when stale. The connection uses a re-entrant lock to guard concurrent access from worker threads during wave-based sync.

- `db_path`: Database file path, created with parent directories if needed
- `_lock`: Threading RLock protecting all connection operations  
- `_conn`: SQLite connection with foreign keys enabled
- File operations: track fingerprints and scan timestamps for incremental updates
- Symbol operations: store parsed symbols with metadata like qualified names, signatures, line ranges
- Edge operations: maintain reference graph between symbols, filtering external/self-references
- Section operations: cache generated triefact one-liners and LLM-inferred role/boundary tags
- Patch operations: store pending documentation corrections with session tracking
- Query methods: search symbols by name patterns, get details with edge counts, find call paths
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.__init__ fingerprint=96b28781440a25c3d116c96dc0909cc81a80b4ab488857c0f7339c90620fdcb4 body_fp=4f8441c77049399d4a8cee059c8e9d78d7c5345ba519d8245509292950a51ca4 source_ref=d377be51db8d287924b99f218a4d7de0bed2d060 role=persistence -->
Store initializer creates a re-entrant lock, database directory, and opens the SQLite connection.

- Creates parent directories if they don't exist
- Initializes threading lock to guard concurrent access to connection
- Calls `_open()` to establish connection and apply schema
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store._open fingerprint=d5775e7d48c270f4a8906ab003e631ae607e8680b16439ada3a0b8fa9f40af37 body_fp=9fdb0da63fed96a2e52027b2136e5deabeef4357ae4dbb81965ef97b7715ac46 source_ref=d377be51db8d287924b99f218a4d7de0bed2d060 role=persistence -->
Store._open opens SQLite connection and initializes/migrates the database schema.

- Detects schema version mismatches and deletes stale database files
- Enables foreign key constraints via PRAGMA
- Creates tables from SCHEMA_SQL if not present
- Inserts current SCHEMA_VERSION on fresh database creation
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.close fingerprint=a913f96235959366c1550f3902f93fb0cb6321b2a3dd492c780b5af0ba6b8e7b body_fp=98f31ca518d69b57bba5fdfbfc3c96ac65744a91df545d8a61a60fc5e8cc74c2 source_ref=a0647ea4e42a6ddac430f66ebd109dd42974af95 role=graph-database -->
Closes the Store's SQLite connection.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.__enter__ fingerprint=9f210cb9718c0e2ccf1afd3e1a8f2d55beb6c6390abbe06ed35fdd33a7172f7f body_fp=2528fd41a394239f4067269aebd5f7269ff6e3f0ae5afaa317f5824aba39bbe8 source_ref=a0647ea4e42a6ddac430f66ebd109dd42974af95 role=graph-database -->
Returns the Store instance for context manager entry.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.__exit__ fingerprint=67b1b6b146522ac7c8bdfff45bab8a41537d8e61231b937b0475a712971729e7 body_fp=79c4706aba3baab3601c54630b3e809e12d56e48f2952516541aaf4ce43455db source_ref=a0647ea4e42a6ddac430f66ebd109dd42974af95 role=graph-database -->
Store context manager exit method that closes the SQLite connection.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.transaction fingerprint=92d85419eab7f0eb88451072a4fe4fd3da121109143afd8912055c863389d51b body_fp=68e90f0886394175affe4344a06e6e211f2b292a3c309a044cb73826f4f6bb2e source_ref=a0647ea4e42a6ddac430f66ebd109dd42974af95 role=graph-database -->
Wraps Store database operations in a context manager that commits on success and rolls back on exceptions.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.get_file fingerprint=eb7697a3a025059d896bd28c96b0f208e7ee3dc597aa5702581ea24d86dcb5de body_fp=138b24c312dda11baf595cd346ffa44efdb718fd404c559e1f16985874c9b2ba source_ref=a0647ea4e42a6ddac430f66ebd109dd42974af95 role=graph-database -->
Store.get_file retrieves a FileRecord for the given path from the files table.

Returns None if no record exists for the path.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.upsert_file fingerprint=6d8542fa2fb58dc7c77adab00e96758e35a7b4106aca18f02c39064c1ff2eeb6 body_fp=9039f4b543b0e1c7ed60d6078eff9e04e42e601402fa989bd53c3bdb08f970e4 source_ref=a0647ea4e42a6ddac430f66ebd109dd42974af95 role=graph-database -->
Store.upsert_file inserts or updates a file record with path, fingerprint, and scan timestamp.

- `now`: optional timestamp override; defaults to current time if None
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.delete_file fingerprint=3cc0d8d1dfff6afab640378b3cec46ac06299bab51b118ae1e695914bcdb5e9d body_fp=fa33109c2d6952813f78c81d5c23b845d29fb95ff6ec209c76ac83009eb6adf6 source_ref=a0647ea4e42a6ddac430f66ebd109dd42974af95 role=graph-database -->
Store.delete_file removes a file record from the database and commits the transaction.

- Cascades to delete all associated symbols due to foreign key constraints
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.list_files fingerprint=0ad09ddc7d8033f74e03712636d0159e4ad107c8be9c4d803563162dc7be55c5 body_fp=6871936600b9f5efb705a7f5befc09beb23f544275a9ab6e88d307a2cad8e8d2 source_ref=a0647ea4e42a6ddac430f66ebd109dd42974af95 role=graph-database -->
Returns all FileRecord instances from the database, ordered by path.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.replace_file_symbols fingerprint=40b1980316c50d05be01ab45d27176c3428961e7489644041c1872db015f19c1 body_fp=fc37f7bf5cb73fbdb1b8de623f3b852c56e7925cb0936e30f3c400bc4cbf3cde source_ref=a0647ea4e42a6ddac430f66ebd109dd42974af95 role=graph-database -->
Store.replace_file_symbols atomically deletes all existing symbols for a file and inserts new ones from the provided list.

- Uses a transaction to ensure atomicity between deletion and insertion
- Converts Symbol objects to database row tuples with proper type casting
- Joins decorator lists with newlines for storage
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.count_symbols fingerprint=2580fe16b3b00ec0a0343c0d528630dd899ab90e6d1a008d340e1aa6c5d92002 body_fp=d68eda0afbc5e9483487a08689e61be7d684b178b1bc9e21a6f17e8cccdbd77f source_ref=a0647ea4e42a6ddac430f66ebd109dd42974af95 role=graph-database -->
Count symbols in the database with optional file and visibility filtering.

- `file_path`: when provided, count only symbols in that file
- `public_only`: when True, count only symbols marked as public
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.count_section_records fingerprint=610f302acb473963e5a29105d08a8808237b8ffa314427ab6ac1f9a61e853fbe body_fp=8a7f36b9abb46d40e4d3df142b62921e8117d4c343864fb86686d48911cbeabf source_ref=a0647ea4e42a6ddac430f66ebd109dd42974af95 role=graph-database -->
Store.count_section_records returns the number of rows in the triefact_sections table.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.count_symbols_missing_role fingerprint=b561b4d71aee1cc5a1c9bd9db7eb9512fd5929bdd36a0d3d108e502a516c06cd body_fp=6e8f179551fb1ff0cfcb3ac93ff87fdaf3378af3f113fe3b2c73148f5ef8eba0 source_ref=607e2f4bea26c04e72afd397633b6fd842990098 role=domain -->
Store.count_symbols_missing_role returns the count of symbols without a non-empty role tag in triefact_sections.

- Used to determine if role auto-backfill can be skipped when count is zero
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.replace_all_edges fingerprint=f723b23ba6b913c951a282870d919431f131b8e31d304ccf18880dc9d37bfe93 body_fp=d26a3cea9be5b7cf848648f7856885a1b88a54c534228955a05992234d01d075 source_ref=a0647ea4e42a6ddac430f66ebd109dd42974af95 role=graph-database -->
Store method that wipes the edges table, resolves references to symbol IDs, and inserts new edges.

- Drops references where source or destination qualified names aren't found in symbols table
- Deduplicates identical edges and skips self-references
- Returns count of edges actually inserted
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.references_in fingerprint=a64405c25c8effa2d37a933ece61b1b112c7cc2bc999fd7d05000ede0188ddc7 body_fp=dd53fa96d7318710482a05bea31d7b39d521f712f422505935328a443acbfd1a source_ref=a0647ea4e42a6ddac430f66ebd109dd42974af95 role=graph-database -->
Store.references_in returns qualified names of all symbols that reference the given qualified name.

- `qualified_name`: target symbol to find incoming references to
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.references_in_with_files fingerprint=773412d3d4e3f39ea3f1a7f9a058c6cf53d88e3ec7a563822446a9c4e2f271fe body_fp=dbc7b3dec9075efd4740130d8770c0bc55cf208b6131bdbdaf078f8d08adadc8 source_ref=a0647ea4e42a6ddac430f66ebd109dd42974af95 role=graph-database -->
Store.references_in_with_files returns `(src_qname, src_file_path)` tuples for every symbol that references the given `qualified_name`.

- Extends `references_in` by including the file path of each referencing symbol
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.qnames_in_file fingerprint=0345839c8b81209c9f8e501ba0bbd84b97b79bcdffd157276f2c5f9433f1bf53 body_fp=7c9dd2be6706cdcdd17fa2a973943e3284d98f7700200cc253b0d901e95e0102 source_ref=a0647ea4e42a6ddac430f66ebd109dd42974af95 role=graph-database -->
Store.qnames_in_file returns qualified names of all symbols defined in the given file path, ordered by start line.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.symbols_in_file_with_lines fingerprint=6c50f1692f561e61d68233e23f1452068b7dc5151923fcf1a75c9e9f32d8fc97 body_fp=585b4e06b98e3dfc5f57a888616c5b7edb994658e8d6ec2ae4d4b89efd93fe02 source_ref=a0647ea4e42a6ddac430f66ebd109dd42974af95 role=graph-database -->
Store.symbols_in_file_with_lines returns qualified names and line ranges for symbols in a file, ordered by start line.

- Returns tuples of `(qname, start_line, end_line)` for line bracket calculations
- Used by locate's grep fallback to map source lines to enclosing symbols
- Returns empty list if file has no recorded symbols or doesn't exist
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.search_symbols fingerprint=843fc4a051517ce70282ea2a98897dd8f7258793682bd113ad354a6fc4c517f6 body_fp=b07642064e8917e154033e3c0e72dac26ac5188f59f8ca86d0db8647060874bb source_ref=a0647ea4e42a6ddac430f66ebd109dd42974af95 role=graph-database -->
Finds symbols whose local name contains a pattern via case-insensitive substring match.

- Returns up to `limit` `SymbolHit` instances ordered by public symbols first
- Searches the `name` field (local part) not the fully qualified name
- Designed for agent "find_symbol" queries that typically use local names
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.references_out fingerprint=a6810cd7afde7caf6868995ebd2d05049eb7e7d1f292600fc55fed2112ad0138 body_fp=735ee0d0262bc1091f50f4ecb36ac823778a212317ce886aa65e26138db75817 source_ref=a0647ea4e42a6ddac430f66ebd109dd42974af95 role=graph-database -->
Returns qualified names of all symbols referenced by the given symbol.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.count_edges fingerprint=dd4f0506260e96b70c2e6c1cf90803909315a59857fe188eb5f56d47f7d9d49d body_fp=76010464946ee977eaa8ca8e9f7e82748d2ab16b8fe0601c016a4ccc8df46edb source_ref=a0647ea4e42a6ddac430f66ebd109dd42974af95 role=graph-database -->
Store.count_edges returns the total number of edges in the graph database.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.inbound_count_per_symbol fingerprint=d02ef2425e589304c3c468f57c53c886dd73de83d538963d490f437f8fdb19c2 body_fp=e9f37d89d2eb1efb93113aa555174551d03e01f4d934e0eceac89496ffc92b02 source_ref=a0647ea4e42a6ddac430f66ebd109dd42974af95 role=graph-database -->
Store.inbound_count_per_symbol returns a dictionary mapping qualified names to their inbound edge counts.

- Used to detect hub symbols with many incoming references
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.file_ref_counts fingerprint=bf982e54730e691d4f235e2ea25f000e8eb351ce5f091f72ab4a025d077abe4d body_fp=937140429a4e663eea66b9c39335bb4c528ff281b39ec03c89589e45fa51b405 source_ref=d377be51db8d287924b99f218a4d7de0bed2d060 role=persistence -->
Store.file_ref_counts returns cross-file inbound and outbound reference counts for a file.

- Inbound: references to symbols in this file from symbols in other files
- Outbound: references from symbols in this file to symbols in other files
- Excludes intra-file edges between symbols within the same file
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.file_stats fingerprint=818ee47e02de6186ac43c3deb53c5ddc50df1980e52047b405fca30d50d264d6 body_fp=826f73836081b81f89a68eda610b4522cdadc060b24451fbc0c4d91bf537b1db source_ref=a0647ea4e42a6ddac430f66ebd109dd42974af95 role=graph-database -->
Returns per-file symbol counts from the Store for bootstrap ranking.

- `public_symbols` field is legacy naming; equals total_symbols count under current parser
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.upsert_section_record fingerprint=9288e2bcdf7b1926bb9e6e00a05b8354f1cbff698d024ff6fbb03d412e96c34b body_fp=bddf59c584a0bcc880a2773a3289e14513bf22d75e72c9e9636942f704a2ed7e source_ref=d377be51db8d287924b99f218a4d7de0bed2d060 role=persistence -->
Records or refreshes Store triefact section metadata for a symbol with LLM-inferred tags.

- Silently skips if symbol no longer exists in database
- Empty role/boundary values preserve existing non-empty values during updates
- Commits transaction immediately after upsert
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.one_liner_for fingerprint=1f204b6ac59d246ef09d1541e51816e9a3261e8bcd10c625cb2b426a5c5dbaaa body_fp=61c0d0acfc5b88ef5796795fb10f13d98f4e13ae7bec7102313f2ffaada710bb source_ref=a0647ea4e42a6ddac430f66ebd109dd42974af95 role=graph-database -->
Store.one_liner_for returns the cached one-liner documentation for a symbol by qualified name, or empty string if none exists.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.one_liners_for fingerprint=41fe88c62a162851d437d2e65cd15c753d88bdc5f4d13d59609b2ab4f92550b4 body_fp=6e1be331518a1dfa903f5d6321e165f839a6f24b9a5936bb70e5d04d692a3892 source_ref=a0647ea4e42a6ddac430f66ebd109dd42974af95 role=graph-database -->
Store method that batch-retrieves cached one-liners for multiple symbol qualified names.

- Returns dictionary mapping qualified names to their cached one-liners
- Only includes entries found in triefact_sections table; missing symbols are omitted
- Empty one-liners are normalized to empty strings in the result
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.add_patch fingerprint=7138f7d0247ef1f8126177ab0ec274e3b5204fe0c5425cd7ceb49ae37ec3a547 body_fp=e1e3668c7650f1fb009cfd9d9b8d8fc5361014bb22657eff1094fb444735a20b source_ref=a0647ea4e42a6ddac430f66ebd109dd42974af95 role=graph-database -->
Store.add_patch inserts a patch record for the symbol with given qualified name and returns the new patch ID.

- Raises `KeyError` if the qualified name doesn't exist in the symbols table
- Returns the database-generated patch ID on success
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.get_patches_for_qname fingerprint=99cf3d176ccf53de862a8deb7087fe8c39df8552d648c1cafb1bd48c038fa021 body_fp=2e8133cc3626fa6a3a0be6d8fbe2104de3bcf7be532c1d2e8edf01abd7fd90c6 source_ref=a0647ea4e42a6ddac430f66ebd109dd42974af95 role=graph-database -->
Store.get_patches_for_qname returns all pending patches for a symbol as dicts.

- Returns empty list when qualified name has no corresponding symbol record
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store._get_patches_by_symbol_id fingerprint=7237e3712892b20f9f97dda9893b1001944188b4c8a9517a3049eece76651481 body_fp=7c76cccda021ac8cdf9f02ed9e105ee7aba4bb3665e103c0d89372807fdaf821 source_ref=a0647ea4e42a6ddac430f66ebd109dd42974af95 role=graph-database -->
Store._get_patches_by_symbol_id retrieves all pending patches for the given symbol_id as dictionary records.

- Returns list of patch dicts with keys: id, note, reason, session_id, created_at
- Results ordered by patch id (creation order)
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.get_all_patches_grouped fingerprint=82c6d9f5fc59b0b4c235714ed11733ead3f39828ab8e1c58b6b44a04469f5419 body_fp=ed341fc781404e6537bd7299bd04c2a6193aa0dd3207958789ca325affa76e98 source_ref=a0647ea4e42a6ddac430f66ebd109dd42974af95 role=graph-database -->
Store.get_all_patches_grouped returns pending patches organized by symbol_id.

- Returns dict mapping symbol_id to list of patch records with id, note, reason, session_id, created_at
- Ordered by symbol_id then patch id
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.delete_patches fingerprint=c1457117713979a51e97ee435994b5d9819075c1f5bce24aaa7f31c328e1f99d body_fp=462bc3bf41ddea2e18aebe8a1b855b1545ed2c568c0c786562b405e530b97a34 source_ref=a0647ea4e42a6ddac430f66ebd109dd42974af95 role=graph-database -->
Store method that deletes patches matching specified criteria and returns count of deleted rows.

- `qname`: Delete all patches for a specific symbol's qualified name
- `session_id`: Delete all patches created in a specific session
- `all`: Delete all patches in the database
- At least one parameter must be specified
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.get_patched_qnames fingerprint=0e2e2afe6da23a44267b7db00a8fdca0a377fddfffb84b1d624128b0a1eb5136 body_fp=9e56083073be85dcbbf4298d9e3e4f419bd713d2ef65c3d227ceea86414b173b source_ref=a0647ea4e42a6ddac430f66ebd109dd42974af95 role=graph-database -->
Store.get_patched_qnames returns all symbol qualified names that have pending patches.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.patch_count_for_symbol fingerprint=0b9529da6e2ea49324486ddca6f3b682563b67ac8c3504c0249c1bebbb9dc8bd body_fp=85d900e9e27b9e8dd7fbeedae268ef343e56608b6e6477c8f8bfad39293cf605 source_ref=a0647ea4e42a6ddac430f66ebd109dd42974af95 role=graph-database -->
Store.patch_count_for_symbol returns the count of pending patches for a given symbol_id.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.get_symbol_detail fingerprint=36a84ec98936b9f4f1c0523d443824942263414e0a24746ded84d93e76f5eff1 body_fp=258c4b6e8b4537931875e26ee2b61909ebd989793870ce2bc7859b247328b4f8 source_ref=a0647ea4e42a6ddac430f66ebd109dd42974af95 role=graph-database -->
Store.get_symbol_detail retrieves complete symbol metadata and graph metrics for an agent query in one roundtrip.

- Returns None if qualified_name is not found
- Includes inbound/outbound edge counts, cached one-liner, role/boundary tags, decorators, and pending patches
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.grep_symbols fingerprint=e78b8da8b52fe6745f7650acdc19da820d8037915bd2cbb2c50c4550cbf71e49 body_fp=2e7cb2886ec3b5ae6d2ac3a2f016fefedbfcdbc51192b9aaaa9c89500f88de88 source_ref=a0647ea4e42a6ddac430f66ebd109dd42974af95 role=graph-database -->
Store.grep_symbols searches symbols using predicate filters, returning SymbolDetail objects sorted by rank_by.

- `rank_by`: "public_first", "inbound_count", or "alphabetical" (defaults to "public_first")
- Edge count filters use scalar subqueries repeated in WHERE clause due to SQLite resolution order
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.all_symbol_names fingerprint=fd7275a10e4d910bbe493d3316de5e7e152c08eabc201043b81db9d247002f65 body_fp=192316a90c2b00ad9f61cd30e388c87d204ff74d8644a4f3cb87e4008aad330e source_ref=a0647ea4e42a6ddac430f66ebd109dd42974af95 role=graph-database -->
Returns all distinct local symbol names from the symbols table for fuzzy-match suggestions.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.all_qualified_names fingerprint=81e36419552fcadd1ffbad7e8109246d3055e765019c0633cfcabdafa0ad9eff body_fp=e8b4083ed5bdeabf6cd7ee2b212f4d2b24b914944fcf91b7f52aaeb5f67f76ab source_ref=a0647ea4e42a6ddac430f66ebd109dd42974af95 role=graph-database -->
Returns all qualified names from the symbols table as a list of strings.

- Used by suggest systems for near-miss matching when explain/walk operations fail to find symbols
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.survey_symbols fingerprint=f68870a5028109f1a34ab0b012829014f156b48313c712e0bc9d0b20d440bcc9 body_fp=2db612189ffe91f2d24b03fe2da682da9aac33a52e86c3d2bc680b8c5c2183eb source_ref=607e2f4bea26c04e72afd397633b6fd842990098 role=domain -->
Returns all symbols as `(qualified_name, kind, one_liner, file_path)` tuples for role taxonomy derivation.

- `public_only`: when True, filters to only public symbols
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.find_paths fingerprint=1e0bfe75b333b57d1f17f2fd413879fcc9f8615e5c9313a5804159d4e9eaa1b9 body_fp=74407c7cda35c5c5fd23c875810b5deafce99b645f4cc0a2f42858e5021e1e3f source_ref=a0647ea4e42a6ddac430f66ebd109dd42974af95 role=graph-database -->
Store.find_paths performs breadth-first search to find shortest call paths between two symbols.

- Returns list of qualified name sequences from `from_qname` to `to_qname` following callee edges
- Limits search by `max_depth` hops, `max_paths` results, skips cycles and high-fanin hubs
- Empty return when no path exists within constraints
- For reverse direction (caller chains), swap the arguments
<!-- trie:end -->