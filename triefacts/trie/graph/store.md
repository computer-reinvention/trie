---
trie_version: 0.1.0
source: trie/graph/store.py
file_fingerprint: 361ae12b4d8899b92fb7673d0847fd1cc711675faa3869ccd36f5c4fcf977702
last_synced_at: '2026-05-14T17:13:02Z'
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
  qualified_name: trie/graph/store:SymbolDetail
  lines: 91-108
- kind: class
  qualified_name: trie/graph/store:LocatePredicate
  lines: 112-129
- kind: class
  qualified_name: trie/graph/store:Store
  lines: 132-649
- kind: method
  qualified_name: trie/graph/store:Store.close
  lines: 169-170
- kind: method
  qualified_name: trie/graph/store:Store.transaction
  lines: 179-185
- kind: method
  qualified_name: trie/graph/store:Store.get_file
  lines: 189-194
- kind: method
  qualified_name: trie/graph/store:Store.upsert_file
  lines: 196-207
- kind: method
  qualified_name: trie/graph/store:Store.delete_file
  lines: 209-211
- kind: method
  qualified_name: trie/graph/store:Store.list_files
  lines: 213-219
- kind: method
  qualified_name: trie/graph/store:Store.replace_file_symbols
  lines: 223-250
- kind: method
  qualified_name: trie/graph/store:Store.count_symbols
  lines: 252-263
- kind: method
  qualified_name: trie/graph/store:Store.replace_all_edges
  lines: 267-298
- kind: method
  qualified_name: trie/graph/store:Store.references_in
  lines: 300-312
- kind: method
  qualified_name: trie/graph/store:Store.references_in_with_files
  lines: 314-326
- kind: method
  qualified_name: trie/graph/store:Store.qnames_in_file
  lines: 328-334
- kind: method
  qualified_name: trie/graph/store:Store.search_symbols
  lines: 336-363
- kind: method
  qualified_name: trie/graph/store:Store.references_out
  lines: 365-377
- kind: method
  qualified_name: trie/graph/store:Store.count_edges
  lines: 379-380
- kind: method
  qualified_name: trie/graph/store:Store.inbound_count_per_symbol
  lines: 382-391
- kind: method
  qualified_name: trie/graph/store:Store.file_ref_counts
  lines: 393-423
- kind: method
  qualified_name: trie/graph/store:Store.file_stats
  lines: 425-442
- kind: method
  qualified_name: trie/graph/store:Store.upsert_section_record
  lines: 446-481
- kind: method
  qualified_name: trie/graph/store:Store.one_liner_for
  lines: 483-496
- kind: method
  qualified_name: trie/graph/store:Store.one_liners_for
  lines: 498-511
- kind: method
  qualified_name: trie/graph/store:Store.get_symbol_detail
  lines: 515-548
- kind: method
  qualified_name: trie/graph/store:Store.locate_symbols
  lines: 550-639
- kind: method
  qualified_name: trie/graph/store:Store.all_symbol_names
  lines: 641-644
- kind: method
  qualified_name: trie/graph/store:Store.all_qualified_names
  lines: 646-649
incoming_refs: 32
outgoing_refs: 2
---
<!-- trie:section symbol=trie/graph/store:FileRecord fingerprint=9e5bd64fbbf95f8eb3616b9da3d84b73687a569550e6ace513eef354bd16b1e1 body_fp=e1fee4fb8b9b7cc07b5ccb4429ec05af6c78ba1ddf9742b8b128b0126066d737 -->
## `FileRecord(path: str, fingerprint: str, last_scanned_at: int)`

Frozen dataclass representing a file row from the `files` table.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:FileStats fingerprint=c724d544428a38f276d944f8e7e7b5ad7459d6b1a250e18b87c7d3031e7a4b40 body_fp=84e5f9cfb9ee7ff62ab8cbf54cb59b5a4b5b00bb208c8a83fdc0ec05e524b191 -->
## `FileStats`

Frozen dataclass holding per-file symbol counts returned by `Store.file_stats`.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:SymbolHit fingerprint=c97f130190c9d3e96d5d1b0be1314de0ae372cc1d5256f00b330cad27aac1b3e body_fp=47b138cd522fcc3e4fa0597b826bafec29d486ac5617dfc1e8835e7d7375c2c7 -->
## `SymbolHit`

Frozen dataclass representing a lightweight symbol match returned by `search_symbols`.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:SymbolDetail fingerprint=79b8fb53099949838219ec9a398c584ec95ec2bad4f37021becc742118d59a63 body_fp=d2ea54af4e2d6559556bb61c2e65903435f4b28934b200cb8a56b0ec8eadde8c -->
## `SymbolDetail`

Immutable dataclass holding full symbol metadata plus graph edge counts and cached one-liner for agent responses.

- `inbound_count`: number of edges whose destination is this symbol
- `outbound_count`: number of edges whose source is this symbol
- `one_liner`: empty string when no triefact section has been generated yet
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:LocatePredicate fingerprint=6c7f06d296f6fd21237853f2fbf326f7769fb6c93f91e321ad999c43eee096ac body_fp=dab08299dcdda719dd6c1b6fac304063f38847e9d450da7c74c694253ca2d9dd -->
## `LocatePredicate(name_contains=None, kind=None, scope_prefix=None, scope_exclude=(), public_only=False, inbound_count_min=None, inbound_count_max=None, outbound_count_min=None, outbound_count_max=None)`

Server-side filter for `Store.locate_symbols`; all fields optional.

- `kind`: `"function"`, `"class"`, `"method"`, `"any"`, or `None`
- `scope_prefix`: matched as prefix against `file_path`
- `scope_exclude`: each entry matched as prefix against `file_path`
- `inbound_count_min/max`, `outbound_count_min/max`: inclusive edge-count bounds
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store fingerprint=582997ccb7efd7161561ec9e4ded46cd2f4e572cfad88ff3a5b6535f96703f55 body_fp=a4962e9497ea403cd2a47a734615fb46d050a11d6bb4e512fb029865e2396752 -->
## `Store(db_path: Path)`

SQLite-backed store for trie's symbol graph, file fingerprints, edges, and triefact section metadata.

- `db_path`: path to the `.trie/` cache DB; parent directories are created automatically.
- Stale schema (version mismatch) causes the DB file to be deleted and rebuilt from scratch.
- Use as a context manager to ensure the connection is closed on exit.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.close fingerprint=a913f96235959366c1550f3902f93fb0cb6321b2a3dd492c780b5af0ba6b8e7b body_fp=3c968b282b4cec11f7e100fef24fd94bd6236359ef4715ea4108e5c6db9becb1 -->
## `close(self) -> None`

Close the underlying SQLite connection.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.transaction fingerprint=92d85419eab7f0eb88451072a4fe4fd3da121109143afd8912055c863389d51b body_fp=efd08e8f65b03fab4406b30520e5de35aa3aceda297b1936c1ac3001fbc3209d -->
## `transaction(self) -> Iterator[sqlite3.Connection]`

Yield the connection inside a commit/rollback transaction block.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.get_file fingerprint=eb7697a3a025059d896bd28c96b0f208e7ee3dc597aa5702581ea24d86dcb5de body_fp=9ce5f140519cee67fa5352515b4f10ca3b0aee1601426f843ba36ff91dfe05b4 -->
## `get_file(self, path: str) -> FileRecord | None`

Return the `FileRecord` for `path`, or `None` if not found.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.upsert_file fingerprint=6d8542fa2fb58dc7c77adab00e96758e35a7b4106aca18f02c39064c1ff2eeb6 body_fp=b0553e214a1fdb31e8e337cf2a7165dbaf820a88a38d71580b9cb0818b45bebc -->
## `upsert_file(self, *, path: str, fingerprint: str, now: int | None = None) -> None`

Insert or update a file record, setting `last_scanned_at` to `now` or the current epoch second.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.delete_file fingerprint=3cc0d8d1dfff6afab640378b3cec46ac06299bab51b118ae1e695914bcdb5e9d body_fp=b4f8476785d308ce0ba11a8bf89a34821c0d414c55af576e4adc2ff9d1ded55b -->
## `delete_file(self, path: str) -> None`

Delete the file record for `path` and commit.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.list_files fingerprint=0ad09ddc7d8033f74e03712636d0159e4ad107c8be9c4d803563162dc7be55c5 body_fp=4294221590b393f9f894949bef5f966f14d007c80d4c03abe04c7b0e0b870f2e -->
## `list_files(self) -> list[FileRecord]`

Return all file records ordered by path.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.replace_file_symbols fingerprint=d8e44858ebcda72ec803e6d2d297bdbbd2658509fa3f8bcbbd924b106093881c body_fp=9d44dab4756af9fd18462f3c64b2a31f349e00558ed888881ab03356ec3e3135 -->
## `replace_file_symbols(self, file_path: str, symbols: list[Symbol]) -> None`

Atomically replace all symbols for a file in a single transaction.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.count_symbols fingerprint=2580fe16b3b00ec0a0343c0d528630dd899ab90e6d1a008d340e1aa6c5d92002 body_fp=22913cccfeac7735c787d8ce3a0d3283a87ad4a29f01e75ecb01370467f76505 -->
## `count_symbols(self, *, file_path: str | None = None, public_only: bool = False) -> int`

Count symbols in the DB, optionally filtered by file and/or public visibility.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.replace_all_edges fingerprint=f723b23ba6b913c951a282870d919431f131b8e31d304ccf18880dc9d37bfe93 body_fp=160215af7dac8b29283a1805b0889b3c4b19864a5032842e2fe1428e96fc178c -->
## `replace_all_edges(self, references_by_file: dict[str, list[Reference]]) -> int`

Wipe the edges table, resolve references to symbol IDs, and insert all valid cross-symbol edges atomically.

- `references_by_file`: mapping of file path to its outbound `Reference` list.
- Returns count of edges inserted; unresolvable or self-referential references are silently dropped.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.references_in fingerprint=a64405c25c8effa2d37a933ece61b1b112c7cc2bc999fd7d05000ede0188ddc7 body_fp=818c68afa2e9fbef7f63c71fed7492aaf9801c859ddd6c9d3dd298032d381209 -->
## `references_in(self, qualified_name: str) -> list[str]`

Return qualified names of all symbols that reference the given symbol (inbound edges).
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.references_in_with_files fingerprint=773412d3d4e3f39ea3f1a7f9a058c6cf53d88e3ec7a563822446a9c4e2f271fe body_fp=16719ffc3dc460a969f59bedbe22c0e2432e66a6a690a9a138c35c9414d84937 -->
## `references_in_with_files(self, qualified_name: str) -> list[tuple[str, str]]`

Return `(src_qname, src_file_path)` pairs for every symbol with an inbound edge to `qualified_name`.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.qnames_in_file fingerprint=0345839c8b81209c9f8e501ba0bbd84b97b79bcdffd157276f2c5f9433f1bf53 body_fp=03fcdaa2a35dc8cb4f625092defafc94e96e570ce5ef8179dbcb7e004a8fb5db -->
## `qnames_in_file(self, file_path: str) -> list[str]`

Return qualified names of all symbols defined in `file_path`, ordered by source line.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.search_symbols fingerprint=843fc4a051517ce70282ea2a98897dd8f7258793682bd113ad354a6fc4c517f6 body_fp=6f3bdb11e41417a581c52b98d1717821ddde4741a092822c5ab783ad86d37cd1 -->
## `search_symbols(self, name_pattern: str, *, limit: int = 50) -> list[SymbolHit]`

Case-insensitive substring search on the local symbol `name`, returning ranked `SymbolHit` results.

- `name_pattern`: matched as `%pattern%` against the `name` column, not the qualified name.
- Results ordered public-first, then alphabetically by qualified name.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.references_out fingerprint=a6810cd7afde7caf6868995ebd2d05049eb7e7d1f292600fc55fed2112ad0138 body_fp=e67a6fb3800a41c941f9c9b858c677de34b8b7f16c397c63dad851d01dc4d873 -->
## `references_out(self, qualified_name: str) -> list[str]`

Return all `qualified_name`s of symbols that `qualified_name` references (outbound edges).
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.count_edges fingerprint=dd4f0506260e96b70c2e6c1cf90803909315a59857fe188eb5f56d47f7d9d49d body_fp=1056160e655caffc348e739a16a30308ffccc7c4bd2b09ba6fb07ceb4753245a -->
## `count_edges(self) -> int`

Return the total number of edges in the graph.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.inbound_count_per_symbol fingerprint=d02ef2425e589304c3c468f57c53c886dd73de83d538963d490f437f8fdb19c2 body_fp=4d2d2c3214df55e9e5123d359b376259fd47a5da5f5c1cbb1e9b91baf3f823c6 -->
## `inbound_count_per_symbol(self) -> dict[str, int]`

Return a mapping of every symbol's `qualified_name` to its inbound edge count.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.file_ref_counts fingerprint=c91d16db66c8427e33861dc7b12859ce10573b7accd08ebfe18b42eaff7c8c62 body_fp=351ac1f87fbfe5a94cd78c028c03c2ab9c4d2af6d2b15f5ff577a670b504b29b -->
## `file_ref_counts(self, file_path: str) -> tuple[int, int]`

Return `(inbound, outbound)` cross-file edge counts for the given file, excluding intra-file edges.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.file_stats fingerprint=ef7e2ff41a140fa94160ce524f5702ffa2e408fcef2da886345c76b343e50164 body_fp=f524e577cbffc87c57819d82e1b5fe3bad2f92dc4c0396d07b40253f846fb2dd -->
## `file_stats(self) -> list[FileStats]`

Return per-file total and public symbol counts for all tracked files.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.upsert_section_record fingerprint=c0ed5ba8a45dd21c6a60068fbc428a85bfe91bc62951744e0c93ca03042bdd96 body_fp=e38c2819fabd527d7c3ed619a69c0b07140a3cfdf5c034b77e35e10d395c886f -->
## `upsert_section_record(self, *, triefact_path: str, symbol_qname: str, section_fingerprint: str, one_liner: str, now: int | None = None) -> None`

Insert or update a `triefact_sections` row linking a generated section to its symbol.

- `symbol_qname`: looked up live; silently no-ops if the symbol no longer exists.
- `now`: Unix timestamp; defaults to `time.time()` if omitted.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.one_liner_for fingerprint=1f204b6ac59d246ef09d1541e51816e9a3261e8bcd10c625cb2b426a5c5dbaaa body_fp=2ca37524618426a38984ee105e1b5a187135a40a5ce1fe97460ef7be1c075c2e -->
## `one_liner_for(self, qualified_name: str) -> str`

Return the cached one-liner for a symbol, or `''` if no triefact section exists.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.one_liners_for fingerprint=41fe88c62a162851d437d2e65cd15c753d88bdc5f4d13d59609b2ab4f92550b4 body_fp=904de37bc41715735de7d108e6362189093ea70b82ef0cd9b65af89fc5b3fc1f -->
## `one_liners_for(self, qnames: list[str]) -> dict[str, str]`

Batch-fetch cached one-liners for a list of qualified names.

- Returns only entries that exist; missing qnames are absent from the dict.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.get_symbol_detail fingerprint=035c308d0bc43eb38d36a7245a821ffa036ba178cbd25c058ef045f1d485d90d body_fp=505eebbc3d944d850a6e5a98c0346d14837c8bbe9512bea70567f9723abe6bed -->
## `get_symbol_detail(self, qualified_name: str) -> SymbolDetail | None`

Return full symbol metadata including edge counts and cached one-liner in a single query, or `None` if not found.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.locate_symbols fingerprint=83b17a895d0060e7833abe22296476ad93ea93e488e0fd8bccb18773bec91068 body_fp=673e249f72678d9d218d40838d30ecbd0fbfd4b6928c458280938ff20345eb5c -->
## `locate_symbols(self, predicate: LocatePredicate, *, rank_by: str = "public_first", limit: int = 10) -> list[SymbolDetail]`

Execute a predicate-driven symbol search and return ranked `SymbolDetail` results.

- `rank_by`: `"public_first"`, `"inbound_count"`, or `"alphabetical"`; unknown values fall back to `"public_first"`.
- `limit`: maximum number of results returned.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.all_symbol_names fingerprint=fd7275a10e4d910bbe493d3316de5e7e152c08eabc201043b81db9d247002f65 body_fp=4c7c97feae5fd43d125fed3e6ce048b962a02d57f9a7d354bc49440f020186e8 -->
## `all_symbol_names(self) -> list[str]`

Return all distinct local symbol names for fuzzy-match suggestion on not-found lookups.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.all_qualified_names fingerprint=81e36419552fcadd1ffbad7e8109246d3055e765019c0633cfcabdafa0ad9eff body_fp=888b119384c653269c1efa9bd0d68d00d2ec74c5bbd1375b4c95d6a6e9f32aae -->
## `all_qualified_names(self) -> list[str]`

Return all qualified symbol names from the database.
<!-- trie:end -->