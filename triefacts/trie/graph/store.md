---
trie_version: 0.2.1
source: trie/graph/store.py
file_fingerprint: ca79cb847185dbec258df42caea5059da06f1d421d40ed55af36095f5762983a
last_synced_at: '2026-08-01T01:52:14Z'
defines:
- kind: module
  qualified_name: trie/graph/store:__module__
  lines: 1-1260
- kind: constant
  qualified_name: trie/graph/store:SCHEMA_VERSION
  lines: 18-18
- kind: constant
  qualified_name: trie/graph/store:SCHEMA_SQL
  lines: 22-116
- kind: class
  qualified_name: trie/graph/store:FileRecord
  lines: 120-123
- kind: class
  qualified_name: trie/graph/store:FileStats
  lines: 127-130
- kind: class
  qualified_name: trie/graph/store:SymbolHit
  lines: 134-141
- kind: class
  qualified_name: trie/graph/store:SymbolDetail
  lines: 145-170
- kind: class
  qualified_name: trie/graph/store:GrepPredicate
  lines: 174-196
- kind: function
  qualified_name: trie/graph/store:_synchronized
  lines: 199-216
- kind: function
  qualified_name: trie/graph/store:_synchronize_store
  lines: 219-236
- kind: class
  qualified_name: trie/graph/store:Store
  lines: 240-1259
- kind: method
  qualified_name: trie/graph/store:Store.__init__
  lines: 249-262
- kind: method
  qualified_name: trie/graph/store:Store._open
  lines: 264-290
- kind: method
  qualified_name: trie/graph/store:Store.close
  lines: 292-293
- kind: method
  qualified_name: trie/graph/store:Store.__enter__
  lines: 295-296
- kind: method
  qualified_name: trie/graph/store:Store.__exit__
  lines: 298-299
- kind: method
  qualified_name: trie/graph/store:Store.transaction
  lines: 302-308
- kind: method
  qualified_name: trie/graph/store:Store.get_file
  lines: 312-317
- kind: method
  qualified_name: trie/graph/store:Store.upsert_file
  lines: 319-330
- kind: method
  qualified_name: trie/graph/store:Store.delete_file
  lines: 332-334
- kind: method
  qualified_name: trie/graph/store:Store.list_files
  lines: 336-342
- kind: method
  qualified_name: trie/graph/store:Store.replace_file_symbols
  lines: 346-375
- kind: method
  qualified_name: trie/graph/store:Store.count_symbols
  lines: 377-388
- kind: method
  qualified_name: trie/graph/store:Store.count_section_records
  lines: 390-392
- kind: method
  qualified_name: trie/graph/store:Store.count_symbols_missing_role
  lines: 394-411
- kind: method
  qualified_name: trie/graph/store:Store.replace_all_edges
  lines: 415-446
- kind: method
  qualified_name: trie/graph/store:Store.references_in
  lines: 448-460
- kind: method
  qualified_name: trie/graph/store:Store.references_in_with_files
  lines: 462-474
- kind: method
  qualified_name: trie/graph/store:Store.symbol_hashes_for_file
  lines: 476-487
- kind: method
  qualified_name: trie/graph/store:Store.qnames_in_file
  lines: 489-495
- kind: method
  qualified_name: trie/graph/store:Store.symbols_in_file_with_lines
  lines: 497-516
- kind: method
  qualified_name: trie/graph/store:Store.search_symbols
  lines: 518-545
- kind: method
  qualified_name: trie/graph/store:Store.references_out
  lines: 547-559
- kind: method
  qualified_name: trie/graph/store:Store.count_edges
  lines: 561-562
- kind: method
  qualified_name: trie/graph/store:Store.inbound_count_per_symbol
  lines: 564-573
- kind: method
  qualified_name: trie/graph/store:Store.file_ref_counts
  lines: 575-606
- kind: method
  qualified_name: trie/graph/store:Store.file_stats
  lines: 608-630
- kind: method
  qualified_name: trie/graph/store:Store.upsert_section_record
  lines: 634-694
- kind: method
  qualified_name: trie/graph/store:Store.one_liner_for
  lines: 696-709
- kind: method
  qualified_name: trie/graph/store:Store.one_liners_for
  lines: 711-724
- kind: method
  qualified_name: trie/graph/store:Store.add_patch
  lines: 726-762
- kind: method
  qualified_name: trie/graph/store:Store.add_delete_patch
  lines: 764-766
- kind: method
  qualified_name: trie/graph/store:Store.add_rename_patch
  lines: 768-770
- kind: method
  qualified_name: trie/graph/store:Store.add_create_patch
  lines: 772-798
- kind: method
  qualified_name: trie/graph/store:Store.get_create_patches_grouped
  lines: 800-827
- kind: method
  qualified_name: trie/graph/store:Store.delete_create_patches
  lines: 829-853
- kind: method
  qualified_name: trie/graph/store:Store._patch_row_to_dict
  lines: 856-867
- kind: method
  qualified_name: trie/graph/store:Store.get_patches_for_qname
  lines: 871-879
- kind: method
  qualified_name: trie/graph/store:Store.get_all_patches_grouped
  lines: 881-892
- kind: method
  qualified_name: trie/graph/store:Store.mark_patches_applied
  lines: 894-909
- kind: method
  qualified_name: trie/graph/store:Store.delete_applied_patches
  lines: 911-916
- kind: method
  qualified_name: trie/graph/store:Store.delete_patches
  lines: 918-943
- kind: method
  qualified_name: trie/graph/store:Store.get_patched_qnames
  lines: 945-953
- kind: method
  qualified_name: trie/graph/store:Store.patch_summary
  lines: 955-981
- kind: method
  qualified_name: trie/graph/store:Store.get_symbol_detail
  lines: 985-1035
- kind: method
  qualified_name: trie/graph/store:Store.grep_symbols
  lines: 1037-1152
- kind: method
  qualified_name: trie/graph/store:Store.all_symbol_names
  lines: 1154-1157
- kind: method
  qualified_name: trie/graph/store:Store.all_qualified_names
  lines: 1159-1162
- kind: method
  qualified_name: trie/graph/store:Store.survey_symbols
  lines: 1164-1183
- kind: method
  qualified_name: trie/graph/store:Store.find_paths
  lines: 1185-1259
incoming_refs: 95
outgoing_refs: 0
---
<!-- trie:section symbol=trie/graph/store:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=6f905ee5b88763bc3efda571c4cc279538d18efe8ee96eddcd1224a9d34490e2 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
SQLite-backed persistence layer for trie's symbol graph, file fingerprints, and documentation metadata.

- Stores parsed symbols with cross-references as a queryable graph
- Caches file fingerprints to enable incremental scanning
- Tracks triefact section metadata including LLM-inferred roles and boundaries
- Supports patch management for pending documentation updates
- Provides search, path-finding, and batch operations for agent tools
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:SCHEMA_VERSION fingerprint=8684c9277e19a742142d499c38b1e1fee8a8ff5a930544a68015f399f4e17dc8 body_fp=6a09e5a6737a4a1a5d051ca7dcd499b0b89812f914c6a1cbb2d50b95edffa080 source_ref=a24eaf0dc9b17f272094d1b0167721b0dc9ceb26 role=config -->
Version number for the SQLite database schema, triggering recreation when incremented.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:SCHEMA_SQL fingerprint=e447a4f3d69ac65cd9aabaf7580306df5387ceae40e22589ce501c8f558dfdc0 body_fp=231cf935eff06abed63919b4d7ccbe1db39d46f804995b7359cad07f2a701c6d source_ref=a24eaf0dc9b17f272094d1b0167721b0dc9ceb26 role=config -->
Defines SQLite schema for trie's symbol graph database with tables for files, symbols, edges, triefact sections, and patches.

- `files`: tracks file paths, fingerprints, and scan timestamps
- `symbols`: stores parsed symbol metadata including qualified names, signatures, and line ranges
- `edges`: represents call/reference relationships between symbols with edge kind classification
- `triefact_sections`: caches generated documentation sections with LLM-inferred roles and boundaries; `hist_mass` / `hist_mass_ts` columns removed in this version
- `patches`: keyed by `qname TEXT` (not a symbol FK) to survive graph refreshes; includes `applied` and `session_note` seal columns and an index on `applied`
- `create_patches`: stores pending symbol creations targeting non-existent symbols; includes `applied` and `session_note` seal columns
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
<!-- trie:section symbol=trie/graph/store:SymbolDetail fingerprint=434842c012b192c81334be8234403afc16f625ca71260f2296d77e12059eb78a body_fp=e2302bf298866037f79300635a4d122c4217ceebec4beaa225c43c969d7ff8d6 source_ref=6b17f7c7cdeef9470455fb704935cf18a7bdd3d0 role=model -->
Full per-symbol record with graph counts and cached one-liner for MCP tools.

- `one_liner`: empty string when no triefact section exists
- `role`: LLM-inferred architectural role tag, empty when unknown
- `boundary`: LLM-inferred boundary class (entry/exit/internal), empty when unknown
- `decorators`: newline-joined decorator lines, empty when none
- `fingerprint`: `body_normalized_hash` from the last scan; empty when unavailable; differs from sentinel fingerprint when prose predates current source
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
<!-- trie:section symbol=trie/graph/store:Store fingerprint=33e359213306b5a83ff713ac1cbe1397b7443e18d4e893132c4809adf5e1ef12 body_fp=2db7f26b1df1c06c34348cad964904d46131230cfe06f1564a7b12899059ec87 source_ref=c1b107d3bdcc6c0717d71bfa4abea1d9a4020944 role=persistence -->
SQLite-backed persistence for trie's symbol graph and file fingerprints.

Store provides thread-safe access to a SQLite database containing files, symbols, reference edges, triefact sections, and patches. All schema is auto-created and version-bumped when stale. The connection uses a re-entrant lock to guard concurrent access from worker threads during wave-based sync.

- `db_path`: Database file path, created with parent directories if needed
- `_lock`: Threading RLock protecting all connection operations
- `_conn`: SQLite connection with foreign keys enabled
- File operations: track fingerprints and scan timestamps for incremental updates
- Symbol operations: store parsed symbols with metadata like qualified names, signatures, line ranges
- Edge operations: maintain reference graph between symbols, filtering external/self-references, storing edge kind
- Section operations: cache generated triefact one-liners and LLM-inferred role/boundary tags; `upsert_section_record` no longer accepts or stores `hist_mass`/`hist_mass_ts` parameters
- Patch operations: store pending documentation corrections keyed by qname (survives graph refreshes); `add_patch` accepts `require_symbol=False` to allow removal notes for gone symbols; `get_patches_for_qname`, `get_all_patches_grouped`, `get_patched_qnames`, and `get_create_patches_grouped` all accept an `applied` filter; `mark_patches_applied` and `delete_applied_patches` manage the apply/consume lifecycle
- `grep_symbols`: ranking demotes test-path symbols within every bucket before `LIMIT` is applied, preventing test symbols from crowding production symbols out of results
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
<!-- trie:section symbol=trie/graph/store:Store.symbol_hashes_for_file fingerprint=c7cfa2cf6e7561a2887cee891e877879584d005ce8e7a9e1b5fcdf1afcfa24c0 body_fp=1e263b0d7c56bf9002c438924b50d2597241f66343fef568df47b15210a2b467 source_ref=c1b107d3bdcc6c0717d71bfa4abea1d9a4020944 role=persistence -->
Return `{qualified_name: body_normalized_hash}` for all symbols in `file_path` from `Store`'s `symbols` table.
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
<!-- trie:section symbol=trie/graph/store:Store.upsert_section_record fingerprint=4e4648b17b75c619be60bae4c667fd4ae21f12f086877226dc45b454cf980256 body_fp=bddf59c584a0bcc880a2773a3289e14513bf22d75e72c9e9636942f704a2ed7e source_ref=a24eaf0dc9b17f272094d1b0167721b0dc9ceb26 role=persistence -->
Records or refreshes Store triefact section metadata for a symbol with LLM-inferred tags.

- Silently skips if symbol no longer exists in database
- Empty role/boundary values preserve existing non-empty values during updates
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
<!-- trie:section symbol=trie/graph/store:Store.add_patch fingerprint=02eaf1e0cb8c1f60de79caef696b5fc235cf444669b9bf1b8156141aa1fe96f3 body_fp=c54e65ada13387f9dd7a250f4e8cdcac95cabb4534d8e117a5dd7af1164b1992 source_ref=d3fae78bb74f28009aa7e2af9642e5cb5b1e1779 role=persistence -->
Store.add_patch inserts a patch record keyed by qname and returns the new patch ID.

- `kind` defaults to "modify"; accepts "modify", "delete", or "rename"
- `rename_to` specifies the new local name when `kind` is "rename"
- `require_symbol` (default `True`) validates qname exists in the graph; pass `False` for removal notes on already-deleted symbols
- Raises `KeyError` if qname is absent and `require_symbol` is `True`
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
<!-- trie:section symbol=trie/graph/store:Store.get_create_patches_grouped fingerprint=5321a1bf1fbffeeaf55a77192770692b8f0bd4d85a847e24330868f3b3f2a4d9 body_fp=ea612a0398449e2e3c0ae198cf0154c1fc63a7db1d9edf990efc51211849a0c0 source_ref=d3fae78bb74f28009aa7e2af9642e5cb5b1e1779 role=persistence -->
Return `Store` create patches grouped by target_file, optionally filtered by seal state.

- `applied`: `True`/`False` filters to sealed/unsealed rows; `None` returns all
- Each patch dict includes `applied` (bool) and `session_note` (str) fields in addition to core create-patch columns
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.delete_create_patches fingerprint=f5ee8cd63465f9f99615fd905f904caac138ba603909cdeed45f6c2d6742e977 body_fp=841dab485bbe6c12d42299dc291a0c3544cd17c3c849692f990d18a66202a56f source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
Delete create patches by target_qname, session_id, or all patches, returning count of deleted rows.

- `target_qname`: delete patches creating this qualified name
- `session_id`: delete patches from this agent session  
- `all`: delete all create patches (overrides other filters)
- Returns 0 if no matching criteria specified
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store._patch_row_to_dict fingerprint=13cf875676503735a3d9b60de815590f1061b036dfda8810b1581f7e25612b78 body_fp=4e6bb3225b403482b8c5cd0eb23e182c86e380d94918961c5225f2499a41b237 source_ref=d3fae78bb74f28009aa7e2af9642e5cb5b1e1779 role=util -->
Convert a raw `patches` DB row tuple into the canonical patch dict used by `Store` query methods.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.get_patches_for_qname fingerprint=ed02f1cb7614c48b7c57bc9009149334a09d5cac1484e3c5a16245418bcdaedb body_fp=9c0cb118befc35417f3ae82aa3abb078a27dd9f9c9663591291a38dd97303d2b source_ref=d3fae78bb74f28009aa7e2af9642e5cb5b1e1779 role=persistence -->
Return patches for one qname as dicts, optionally filtered by seal state via `applied`.

- `applied`: `True` = sealed only, `False` = pending only, `None` = all rows
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.get_all_patches_grouped fingerprint=c9470f3993903df761f557c439a95f27c77bbb3f60fa126443b17e1b0fe64f7a body_fp=878fb2d1b069a57d6674fcffd2d0f6697d0a072505d24f78a2d26ac2c1568e9e source_ref=d3fae78bb74f28009aa7e2af9642e5cb5b1e1779 role=persistence -->
Return all patches grouped by `qname`; `applied` filters to sealed or unsealed rows only (None = all).

- Returns `dict[str, list[dict]]` keyed by qname (was symbol_id in previous version)
- Each patch dict includes `applied` and `session_note` fields in addition to previous fields
- `applied=True` returns only sealed rows; `applied=False` only pending rows
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.mark_patches_applied fingerprint=9ca7fdb0b6144ac0c487bf8d5b5be56b7f9150e1191720bcdfe852288a7c09c1 body_fp=08c27330c85513d8c65cbe6033742d07c32754f1f6a2733580e75b2dc9ea4be0 source_ref=d3fae78bb74f28009aa7e2af9642e5cb5b1e1779 role=persistence -->
Stamp every unapplied row in `patches` and `create_patches` with `session_note` and `applied = 1`, then return the total count of sealed rows.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.delete_applied_patches fingerprint=c67f14662f9b48c82b4dd6043baec1d01536466c1ea2daf5f8d2427dd9419f27 body_fp=d9796ed4c27c45945975abee897569f754ed93012c59815c22b7f42d84bf2659 source_ref=d3fae78bb74f28009aa7e2af9642e5cb5b1e1779 role=persistence -->
Delete all applied `patches` and `create_patches` rows, returning the total count of deleted rows.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.delete_patches fingerprint=a059c49514e3e3e6326509ce064d54534ef91fdcb02041ae9ccbe0ee4eaef2ef body_fp=685e0349f387271aa2e1ee8cd2dd1e4ac25f5772b37ab424c101683994c54c17 source_ref=d3fae78bb74f28009aa7e2af9642e5cb5b1e1779 role=persistence -->
Store method that deletes patches matching specified criteria and returns count of deleted rows.

- `qname`: Delete all patches directly by `qname` column (no longer validates symbol existence)
- `session_id`: Delete all patches created in a specific session
- `all`: Delete all patches in the database
- At least one parameter must be specified
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.get_patched_qnames fingerprint=caa0e417b575e83267895367b57e795e5928e9344044d6607f471915c22b6ca1 body_fp=d98e61fbab7de6dd4e2fa4faf47c5105aaccf0b414768614a8e00898943ac0a2 source_ref=d3fae78bb74f28009aa7e2af9642e5cb5b1e1779 role=persistence -->
Return distinct qnames from `patches`; `applied` filters by seal state (None returns all rows, True/False restricts to sealed/unsealed).
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.patch_summary fingerprint=ee1164a6a6761ae48bfe4436a38be3f34d6fb9ef25040ce8a8d7ae23f876f921 body_fp=8322a4da05ac51789356b0ef29ee78a56d952be76d732bb9dd9a19aa357d19e0 source_ref=d3fae78bb74f28009aa7e2af9642e5cb5b1e1779 role=persistence -->
Store.patch_summary aggregates pending-patch state into counts and classifications by session origin.

- `total_patches`: total number of patch rows across all symbols
- `symbol_count`: number of distinct symbols with pending patches
- `create_count`: number of create_patches (new symbols to be created)
- `by_origin`: symbols bucketed by patch session type (agent/cascade/mixed)
- `qnames`: sorted list of qualified names having pending patches
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.get_symbol_detail fingerprint=4810eb0c5b83545ed08d9625075a3a9b7715fcbe1c52ef4d28c2d2c79dbc394b body_fp=60fffd80a93b3d0307075e101470487e5be660b7ce547df6ea920c257c39916e source_ref=6b17f7c7cdeef9470455fb704935cf18a7bdd3d0 role=persistence -->
Store.get_symbol_detail retrieves complete symbol metadata and graph metrics for an agent query in one roundtrip.

- Returns None if qualified_name is not found
- Includes inbound/outbound edge counts, cached one-liner, role/boundary tags, decorators, fingerprint, and pending patches
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.grep_symbols fingerprint=ace8af747c7eb029b2268d33c835964089f14085c7b416ed8016d3108366a8bb body_fp=048872d8a04c221daf0dcaa0304a66ad7ffc55a74360f09e08e57137ea887876 source_ref=c1b107d3bdcc6c0717d71bfa4abea1d9a4020944 role=persistence -->
Store.grep_symbols searches symbols using predicate filters, returning SymbolDetail objects sorted by rank_by.

- `rank_by`: "public_first", "inbound_count", or "alphabetical" (defaults to "public_first"); test-path symbols are demoted within every bucket except "alphabetical"
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