---
trie_version: 0.1.5
source: trie/sync/attention_fold.py
file_fingerprint: 657e90d0ff0798a3437c223162347c255b4089fa95667bb9b55dd41be608cb84
last_synced_at: '2026-06-10T13:16:17Z'
description: Sync-time historical-mass fold for AGM.
defines:
- kind: module
  qualified_name: trie/sync/attention_fold:__module__
  lines: 1-95
- kind: function
  qualified_name: trie/sync/attention_fold:fold_historical_mass
  lines: 36-77
- kind: function
  qualified_name: trie/sync/attention_fold:advance_fold_watermark
  lines: 80-85
- kind: function
  qualified_name: trie/sync/attention_fold:_decayed
  lines: 88-94
incoming_refs: 2
outgoing_refs: 4
---
<!-- trie:section symbol=trie/sync/attention_fold:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=1393b7e8ddeed76d9502e1296552af112ee1977517b873302b5667daa34bcbbf source_ref=bab77ce31e6099bb75fcbeb5887722474d507273 role=orchestration -->
Implements decay-and-accrue historical mass folding for AGM's cognitive importance signals.

- Historical mass tracks how often agent cognition returns to symbols across investigations
- Uses 21-day exponential decay with recurrence-based accumulation rather than raw attention magnitude
- Recurrence counts distinct investigations that touched each symbol since last fold
- Updates triefact sentinels during sync to avoid extra diff churn
- Fold watermark prevents double-counting attention events across sync runs
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/attention_fold:fold_historical_mass fingerprint=c22c71e8730ad568b4e1e357194b4194166f20cbd43bd6c1604cef6fc2249225 body_fp=26d1c0c408dcca6c4e0379f1d564d9d0c41124af4931ef10eea31c37e3e88558 source_ref=bab77ce31e6099bb75fcbeb5887722474d507273 role=orchestration -->
Decays and accrues historical mass for all sections in a triefact file.

- `since`: defaults to last fold watermark; explicit value for tests
- Returns number of sections whose mass changed
- Only restamps when quantized value changes or recurrence exceeds zero
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/attention_fold:advance_fold_watermark fingerprint=b413948a33ca3ab02bd6bdac5d24f05c6d7f5bc024a7db7fcbbcfdf5e23a4247 body_fp=8a0ca0b94bea594dc79dd456deb754044f6090b55203651419456152139924d8 source_ref=bab77ce31e6099bb75fcbeb5887722474d507273 role=persistence -->
Records that the fold has consumed attention events up to the given timestamp (defaults to now).

- Called once at the end of a sync run to set the next run's recurrence window start
- Best-effort operation that swallows failures from the attention store
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/attention_fold:_decayed fingerprint=67efcb221028f313514cd2098d1d019f61c7c9d7fb960504b19534f0b7b43275 body_fp=6455d30eb42d262c8bc875240548968d9e1edc96ad7693a9219a1b780105d424 source_ref=bab77ce31e6099bb75fcbeb5887722474d507273 role=util -->
Exponentially decay historical mass using time-based half-life calculation.

- Returns mass unchanged when mass or mass_ts is zero/unset
- Uses HISTORICAL_LAMBDA constant for decay rate
<!-- trie:end -->