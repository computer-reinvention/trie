---
trie_version: 0.1.0
source: trie/graph/store.py
file_fingerprint: bea32abb2cb885e65f34f654561e7cfaf0fa2752228e6b58f5b8fe210811b8c5
last_synced_at: '2026-05-12T18:18:17Z'
defines:
- kind: class
  qualified_name: trie/graph/store:FileRecord
  lines: 66-69
- kind: class
  qualified_name: trie/graph/store:FileStats
  lines: 73-76
- kind: class
  qualified_name: trie/graph/store:SymbolHit
  lines: 80-87
- kind: class
  qualified_name: trie/graph/store:Store
  lines: 90-383
- kind: method
  qualified_name: trie/graph/store:Store.close
  lines: 110-111
- kind: method
  qualified_name: trie/graph/store:Store.transaction
  lines: 120-126
- kind: method
  qualified_name: trie/graph/store:Store.get_file
  lines: 130-135
- kind: method
  qualified_name: trie/graph/store:Store.upsert_file
  lines: 137-148
- kind: method
  qualified_name: trie/graph/store:Store.delete_file
  lines: 150-152
- kind: method
  qualified_name: trie/graph/store:Store.list_files
  lines: 154-160
- kind: method
  qualified_name: trie/graph/store:Store.replace_file_symbols
  lines: 164-191
- kind: method
  qualified_name: trie/graph/store:Store.count_symbols
  lines: 193-204
- kind: method
  qualified_name: trie/graph/store:Store.replace_all_edges
  lines: 208-239
- kind: method
  qualified_name: trie/graph/store:Store.references_in
  lines: 241-253
- kind: method
  qualified_name: trie/graph/store:Store.references_in_with_files
  lines: 255-267
- kind: method
  qualified_name: trie/graph/store:Store.qnames_in_file
  lines: 269-275
- kind: method
  qualified_name: trie/graph/store:Store.search_symbols
  lines: 277-304
- kind: method
  qualified_name: trie/graph/store:Store.references_out
  lines: 306-318
- kind: method
  qualified_name: trie/graph/store:Store.count_edges
  lines: 320-321
- kind: method
  qualified_name: trie/graph/store:Store.inbound_count_per_symbol
  lines: 323-332
- kind: method
  qualified_name: trie/graph/store:Store.file_ref_counts
  lines: 334-364
- kind: method
  qualified_name: trie/graph/store:Store.file_stats
  lines: 366-383
incoming_refs: 28
outgoing_refs: 2
---
<!-- trie:section symbol=trie/graph/store:FileRecord fingerprint=9e5bd64fbbf95f8eb3616b9da3d84b73687a569550e6ace513eef354bd16b1e1 body_fp=90bb448aea60a78b5b938278c6561cc7d4cbde24148b5ef74965e7524d6204ca -->
## `FileRecord(path: str, fingerprint: str, last_scanned_at: int)`

Frozen dataclass representing a scanned file row from the `files` table.

- `last_scanned_at`: Unix timestamp of the most recent scan.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:FileStats fingerprint=c724d544428a38f276d944f8e7e7b5ad7459d6b1a250e18b87c7d3031e7a4b40 body_fp=ed94cc7c2c259a31d1dfee8fe533e7f9b0887be0d15e982f6e4dc32fdf03d099 -->
## `FileStats`

Frozen dataclass holding per-file symbol counts for a single file path.

- `total_symbols`: count of all symbols regardless of visibility.
- `public_symbols`: count of public symbols only.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:SymbolHit fingerprint=c97f130190c9d3e96d5d1b0be1314de0ae372cc1d5256f00b330cad27aac1b3e body_fp=fb7c292c1695ddfb6ae0e36bc0f824cb17c74d6664313d214bc0be3d6d31da7e -->
## `SymbolHit`

Frozen dataclass representing a single symbol result returned by `search_symbols`.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store fingerprint=198388d4d574f342f340c4e35a1790719d1a9d1b965d0b08c0e64c7b9d3b4190 body_fp=7efd700ae2fa33a78537b9714265481fd635b93fe6f12ef0d077caf5c886d02b -->
## `Store(db_path: Path)`

SQLite-backed store for file fingerprints, parsed symbols, and reference edges.

- `db_path`: database file is created (with parent dirs) if absent.
- Use as a context manager to guarantee connection closure.
- Foreign keys are enforced; schema is auto-created on first open.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.close fingerprint=a913f96235959366c1550f3902f93fb0cb6321b2a3dd492c780b5af0ba6b8e7b body_fp=4a05714acaf86eabe0a1ea7f203db51ca49040eb6902941022b2649bbc20b6f6 -->
## `close() -> None`

Close the underlying SQLite connection.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.transaction fingerprint=92d85419eab7f0eb88451072a4fe4fd3da121109143afd8912055c863389d51b body_fp=fb42525277193a772e26376570815c0b6f5814d5b0a549af67518b3b2e7056a4 -->
## `transaction(self) -> Iterator[sqlite3.Connection]`

Yield the open connection inside a commit/rollback boundary as a context manager.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.get_file fingerprint=eb7697a3a025059d896bd28c96b0f208e7ee3dc597aa5702581ea24d86dcb5de body_fp=e674ddcbd711688037ad2903045682b30ee79b949ea91c340138f75f9a18090d -->
## `get_file(self, path: str) -> FileRecord | None`

Return the `FileRecord` for the given path, or `None` if not found.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.upsert_file fingerprint=6d8542fa2fb58dc7c77adab00e96758e35a7b4106aca18f02c39064c1ff2eeb6 body_fp=732b9d9414c178147682b381568f342343371386135c741606d09c60a8a868c9 -->
## `upsert_file(self, *, path: str, fingerprint: str, now: int | None = None) -> None`

Insert or update a file record, setting `last_scanned_at` to `now` or the current Unix timestamp.

- `now`: Unix epoch seconds; defaults to `int(time.time())` if `None`.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.delete_file fingerprint=3cc0d8d1dfff6afab640378b3cec46ac06299bab51b118ae1e695914bcdb5e9d body_fp=b4f8476785d308ce0ba11a8bf89a34821c0d414c55af576e4adc2ff9d1ded55b -->
## `delete_file(self, path: str) -> None`

Delete the file record for `path` and commit.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.list_files fingerprint=0ad09ddc7d8033f74e03712636d0159e4ad107c8be9c4d803563162dc7be55c5 body_fp=7ebc6bfee4cc9093c930ac2e5713cfae724449711c1e95ee1b28698aad03359c -->
## `list_files(self) -> list[FileRecord]`

Return all file records from the database, ordered by path.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.replace_file_symbols fingerprint=d8e44858ebcda72ec803e6d2d297bdbbd2658509fa3f8bcbbd924b106093881c body_fp=60f9ae5e3e894516571d9a53ec0e82f8a6024b0a90daa632fe72666aa9d959a9 -->
## `replace_file_symbols(self, file_path: str, symbols: list[Symbol]) -> None`

Atomically delete and re-insert all symbols for a given file within a single transaction.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.count_symbols fingerprint=2580fe16b3b00ec0a0343c0d528630dd899ab90e6d1a008d340e1aa6c5d92002 body_fp=1e6a76f2e32a295658c43f777168e8f0245e2bec437bf5f802a6e44e5b1f7f6b -->
## `count_symbols(self, *, file_path: str | None = None, public_only: bool = False) -> int`

Count symbols in the database, optionally filtered by file path and/or visibility.

- `file_path`: restrict count to symbols belonging to this file.
- `public_only`: when `True`, count only symbols where `is_public = 1`.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.replace_all_edges fingerprint=c4f75dab4bbca7b1e7ffba77336a51206e53d5c94359a559dd6e549e85f10ce2 body_fp=91d0d16d727788d1b83d5a61c6d0e917c4811be64e073833fe729cc5071c3b86 -->
## `replace_all_edges(self, references_by_file: dict[str, list[Reference]]) -> int`

Wipe the edges table, resolve references to symbol IDs, and insert de-duplicated edges atomically.

- `references_by_file`: map of file path to its outbound `Reference` list.
- References whose `src_qname` or `target_qname` is absent from `symbols`, or where src equals dst, are silently dropped.
- Returns count of edges actually inserted.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.references_in fingerprint=0f4bc3046f03a325ce78a6bdbfb72c890d823055e466a8b6252c02dd21519e8e body_fp=be9086ad503568ec6770832565ccec0150e77da0fd13939de397ef0e772df43e -->
## `references_in(self, qualified_name: str) -> list[tuple[str, str]]`

Return `(src_qname, confidence)` for every symbol that references the given qualified name.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.references_in_with_files fingerprint=40a43f83f53d2ad56866571a18d1020ba8b81d07d55253514c2841edf531b3f9 body_fp=4e0c694e540bac2b03a75fd6632eb6361a5b8693c75cc8116a3b7edf4badf457 -->
## `references_in_with_files(self, qualified_name: str) -> list[tuple[str, str, str]]`

Return `(src_qname, src_file_path, confidence)` for every symbol that references `qualified_name`.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.qnames_in_file fingerprint=0345839c8b81209c9f8e501ba0bbd84b97b79bcdffd157276f2c5f9433f1bf53 body_fp=1aeef4b777499132cc9baf0cf5cb9fd67bfeec96e8f196a39940cfaf64fc5be3 -->
## `qnames_in_file(self, file_path: str) -> list[str]`

Return all symbol qualified names defined in `file_path`, ordered by start line.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.search_symbols fingerprint=843fc4a051517ce70282ea2a98897dd8f7258793682bd113ad354a6fc4c517f6 body_fp=ea946928ed0e07f23d25b91ab1a0c6eba16775db4ec0d5e0783712fb25cfa0ce -->
## `search_symbols(self, name_pattern: str, *, limit: int = 50) -> list[SymbolHit]`

Return symbols whose local `name` contains `name_pattern` via case-insensitive substring match.

- `name_pattern`: matched against the local name, not the qualified name.
- Results ordered by `is_public DESC`, then `qualified_name`; capped at `limit`.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.references_out fingerprint=8c4f635d1ca5c45eae906f0fdbc867a22ee758f415bcd6659ae72cd47644c317 body_fp=95f2c67bb14c5a7c411e35a9a178dac12a79e385a6b5c7e09471e828d156bdb0 -->
## `references_out(self, qualified_name: str) -> list[tuple[str, str]]`

Return `(target_qname, confidence)` for every outbound edge from `qualified_name`.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.count_edges fingerprint=dd4f0506260e96b70c2e6c1cf90803909315a59857fe188eb5f56d47f7d9d49d body_fp=32605d168ba7d98023e42fec43da7b1443f682ef00fcf2b56158ae2aced38bb9 -->
## `count_edges(self) -> int`

Return the total number of rows in the edges table.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.inbound_count_per_symbol fingerprint=d02ef2425e589304c3c468f57c53c886dd73de83d538963d490f437f8fdb19c2 body_fp=ccef85ee40f73a30641c6e1476c892b9a82ed909d989da10889de10c87ae75a8 -->
## `inbound_count_per_symbol(self) -> dict[str, int]`

Return a mapping of every symbol's qualified name to its inbound edge count.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.file_ref_counts fingerprint=c91d16db66c8427e33861dc7b12859ce10573b7accd08ebfe18b42eaff7c8c62 body_fp=351ac1f87fbfe5a94cd78c028c03c2ab9c4d2af6d2b15f5ff577a670b504b29b -->
## `file_ref_counts(self, file_path: str) -> tuple[int, int]`

Return `(inbound, outbound)` cross-file edge counts for the given file, excluding intra-file edges.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.file_stats fingerprint=ef7e2ff41a140fa94160ce524f5702ffa2e408fcef2da886345c76b343e50164 body_fp=7cfc3b29ab5ff2735d8d0c436ec4a9c68ab2fda4eb1dc789e5bbbfa2cf5ccddf -->
## `file_stats(self) -> list[FileStats]`

Return per-file symbol counts (total and public) for every tracked file.
<!-- trie:end -->