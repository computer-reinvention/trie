---
trie_version: 0.1.5
source: trie/attention_store.py
file_fingerprint: 5c68788139cc8d36769ae00b7ea6f24b7a7688c74ba9b99cdaaad9b692faae88
last_synced_at: '2026-06-10T13:16:28Z'
description: Compressed attention-event capture, backed by SQLite under `.trie/`.
defines:
- kind: module
  qualified_name: trie/attention_store:__module__
  lines: 1-279
- kind: constant
  qualified_name: trie/attention_store:DB_FILENAME
  lines: 48-48
- kind: constant
  qualified_name: trie/attention_store:COALESCE_WINDOW_SECONDS
  lines: 52-52
- kind: constant
  qualified_name: trie/attention_store:MAX_INVESTIGATIONS
  lines: 56-56
- kind: constant
  qualified_name: trie/attention_store:MAX_AGE_SECONDS
  lines: 57-57
- kind: constant
  qualified_name: trie/attention_store:_SCHEMA
  lines: 59-80
- kind: function
  qualified_name: trie/attention_store:db_path
  lines: 83-84
- kind: function
  qualified_name: trie/attention_store:_connect
  lines: 88-103
- kind: class
  qualified_name: trie/attention_store:StoredEvent
  lines: 107-114
- kind: function
  qualified_name: trie/attention_store:record_event
  lines: 117-170
- kind: function
  qualified_name: trie/attention_store:read_events
  lines: 173-194
- kind: function
  qualified_name: trie/attention_store:investigations_touching_symbol_since
  lines: 197-221
- kind: function
  qualified_name: trie/attention_store:get_last_fold_ts
  lines: 224-236
- kind: function
  qualified_name: trie/attention_store:set_last_fold_ts
  lines: 239-248
- kind: function
  qualified_name: trie/attention_store:_prune
  lines: 251-278
incoming_refs: 14
outgoing_refs: 1
---
<!-- trie:section symbol=trie/attention_store:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=e6d42df7499a894d8f1713b258e71bda54daeba179594ce6113eeea34182c7c4 source_ref=412a37404099a60c0261bd14be762db3b6ba77ba role=persistence -->
Provides SQLite-backed compression and storage for agent attention events under `.trie/attention.db`.

- Coalesces repeated events within 5-second windows to bound log size
- Retains events from last 20 investigations or 7 days, whichever is more generous
- Supports replay hydration for desktop app restarts and historical mass calculation for sync operations
- All write operations are best-effort and never raise exceptions into agent tool paths
<!-- trie:end -->
<!-- trie:section symbol=trie/attention_store:DB_FILENAME fingerprint=89b4b97d7ba7c2a4539aa52382a2e1253a98cc4fbf8ba7e572ec6f7dada5fc86 body_fp=05c79825e0eb5bbff3960836a59bd44b86f4e4ec7d6d99994dfa1a1964089774 source_ref=412a37404099a60c0261bd14be762db3b6ba77ba role=config -->
Defines the SQLite database filename for storing compressed attention events in the `.trie/` directory.
<!-- trie:end -->
<!-- trie:section symbol=trie/attention_store:COALESCE_WINDOW_SECONDS fingerprint=c60f50552115f59e7b22e6cb5b44e508262e5f55082661c0a7e7b9801a018759 body_fp=d7e648eedf24a828952468526fae19cd4cba08c3d128e94bd392707937a9214a source_ref=412a37404099a60c0261bd14be762db3b6ba77ba role=config -->
Time window in seconds for merging duplicate attention events into a single row with accumulated weight.
<!-- trie:end -->
<!-- trie:section symbol=trie/attention_store:MAX_INVESTIGATIONS fingerprint=f93af69920c73e1a312a0fd0a5c52731cfada730b6b495e5700cdee601fe1412 body_fp=5cdd2fd3367cae67d1f8ada02d0aa58da8c92d312a853a57cd56676c8a23b861 source_ref=412a37404099a60c0261bd14be762db3b6ba77ba role=config -->
Maximum number of recent investigations to retain when pruning old attention events.
<!-- trie:end -->
<!-- trie:section symbol=trie/attention_store:MAX_AGE_SECONDS fingerprint=16782c2237520c6fdb61dfb49dcce8b95e7147004f4299aac70115a5ff27bd5b body_fp=93c55bc67ddcd1edccb728320f69c12678abd2059f8361ab279a0a7090fb242a source_ref=412a37404099a60c0261bd14be762db3b6ba77ba role=config -->
Retention cutoff for attention events in seconds (7 days).

Events older than this are pruned unless they fall within the most recent `MAX_INVESTIGATIONS` investigations.
<!-- trie:end -->
<!-- trie:section symbol=trie/attention_store:_SCHEMA fingerprint=3cf8018051d17a3acc00ee038542c69dae7819079c6a39d1f9777bcddd6fc586 body_fp=142a6309a887b3c571b321b2114c349bf3a4b357bb5c2fbe6499f50e23e21558 source_ref=412a37404099a60c0261bd14be762db3b6ba77ba role=persistence -->
SQL DDL script defining the attention store database schema with events table and metadata table.

- `attention_events` table stores timestamped attention events with target, weight, and investigation tracking
- `attention_meta` table tracks sync fold watermarks to avoid reprocessing events
- Includes indexes on target, timestamp, and investigation_id for query performance
<!-- trie:end -->
<!-- trie:section symbol=trie/attention_store:db_path fingerprint=23fb5be98a9ec4515c2044254a25da56fe69f828f8d48f301452ebf9bb01a100 body_fp=d1db3375bc5c9f04e4241564f6329c33913c966d167e2366fa5d746379c98ae2 source_ref=412a37404099a60c0261bd14be762db3b6ba77ba role=util -->
Returns the path to the attention database file within the project's `.trie` directory.
<!-- trie:end -->
<!-- trie:section symbol=trie/attention_store:_connect fingerprint=03211ddea8f84f33f74b57de1b2e04e46a70876f8beb0415050e721f5571c3c5 body_fp=36c273480dfe58bfad4797b78fcb4f812e0956196d49459ac24af93d7f1ec4ba source_ref=412a37404099a60c0261bd14be762db3b6ba77ba role=persistence -->
Opens attention SQLite database with concurrent-safe configuration and schema setup.

- Creates `.trie/` directory and database file if missing
- Enables WAL mode for concurrent read/write access
- Sets 5-second busy timeout to handle lock contention
- Initializes schema on first connection
<!-- trie:end -->
<!-- trie:section symbol=trie/attention_store:StoredEvent fingerprint=46787917a31170f7e082211572c1efe144bf55e183c50b6497b69fa8c8415df3 body_fp=efdfdb94a462e0aa110690794caa2625d090ac6e2c01eaeaf6aef92d539ea706 source_ref=412a37404099a60c0261bd14be762db3b6ba77ba role=model -->
Immutable data structure representing a stored attention event from the SQLite database.

- `ts`: Unix timestamp when the event occurred
- `weight`: Accumulated weight from coalesced events of the same type
- `target`: Symbol or file that received attention
- `investigation_id`: Groups related events within a single investigation session
<!-- trie:end -->
<!-- trie:section symbol=trie/attention_store:record_event fingerprint=cb55a661b30e4dcce2b3928b37e66d651c0c00ca3fc0b363bcb4aaf22f4df95d body_fp=3e377e2c4038e586a8ac78db89dffa6d21ab8a20f3e31650a7acb121243238c7 source_ref=412a37404099a60c0261bd14be762db3b6ba77ba role=persistence -->
Records an attention event to the SQLite store, coalescing into recent matching rows to compress repeated events.

- Coalesces events within `COALESCE_WINDOW_SECONDS` that share target, type, and investigation ID
- Uses canonical weight from `EVENT_WEIGHTS` for the event type
- Swallows all database errors to prevent agent tool failures
- Runs bounded pruning after write to maintain retention limits
<!-- trie:end -->
<!-- trie:section symbol=trie/attention_store:read_events fingerprint=13888355f022267bd15833e1e6b333b8e5baa494e432187c5b08033c202701ec body_fp=72285da64101638faa3d8f99144706e7f2db4fc5a101a53f7f051b297931d603 source_ref=412a37404099a60c0261bd14be762db3b6ba77ba role=persistence -->
Returns attention events from the SQLite store with timestamps greater than `since`, ordered oldest-first.

- `since`: timestamp threshold (default 0.0 returns all events)
- `limit`: maximum number of events to return (default 5000)
- Returns empty list if database doesn't exist or on SQLite errors
<!-- trie:end -->
<!-- trie:section symbol=trie/attention_store:investigations_touching_symbol_since fingerprint=f3f57f73d411fd5156f0c83101699c107cd24264b94f24321fdc58d3feb8b50a body_fp=48be99d9a85e348e374bc606323559beace745bd3b7c12a5912099e2b21d1767 source_ref=412a37404099a60c0261bd14be762db3b6ba77ba role=persistence -->
Returns investigation IDs that drew attention to a target symbol after the given timestamp.

- Returns empty set if database doesn't exist or on SQLite errors
- Empty string investigation ID represents untracked investigations
- Used by sync process to calculate symbol recurrence for historical mass weighting
<!-- trie:end -->
<!-- trie:section symbol=trie/attention_store:get_last_fold_ts fingerprint=f624774071953a69049f219d0b5b889c2042a07722717aef98c82912a6e7bb70 body_fp=770837fa6508aefa732b2127080f70d90cb0ecf69b0b2c47561425cb0b4e11f4 source_ref=412a37404099a60c0261bd14be762db3b6ba77ba role=persistence -->
Returns the timestamp of the last historical-mass fold from the attention database, or 0.0 if never folded.

- Returns 0.0 if database doesn't exist or any SQLite error occurs
<!-- trie:end -->
<!-- trie:section symbol=trie/attention_store:set_last_fold_ts fingerprint=79d6d3a5890512d3bdcd9c040fa5b9061b493f5c3c6ce7ad5175254eae2e5ff4 body_fp=c48eba1f550bf0f532992f3f18a161d6dd73c989be74c7fb9afd9c551c0759fd source_ref=412a37404099a60c0261bd14be762db3b6ba77ba role=persistence -->
Records the timestamp of the last historical-mass fold operation in the attention database.

- **project_root**: Path to the project's root directory
- **ts**: Timestamp to record as the fold watermark
- Swallows SQLite errors to ensure fold failures don't propagate
<!-- trie:end -->
<!-- trie:section symbol=trie/attention_store:_prune fingerprint=43c5ec7a71c705272b7daadaac48bb074b7f6f26e6461a56c6f7af1f4cd97458 body_fp=734d225aa0d000bb521e94f3068132362fca1ba8a12e90fb61065c251b780bb7 source_ref=412a37404099a60c0261bd14be762db3b6ba77ba role=persistence -->
Deletes old attention events from the database, keeping only the most recent investigations or events within the age limit.

- Uses the more generous of two cutoffs: MAX_INVESTIGATIONS recent investigations or MAX_AGE_SECONDS time window
- Runs within the caller's transaction context
<!-- trie:end -->