---
trie_version: 0.1.9
source: trie/session_diff.py
file_fingerprint: a0e38753224db01f448e83ab60f243faa495d9766ef59b6af8307a1300f74dc0
last_synced_at: '2026-07-29T12:09:44Z'
defines:
- kind: module
  qualified_name: trie/session_diff:__module__
  lines: 1-863
- kind: class
  qualified_name: trie/session_diff:SessionDiff
  lines: 11-30
- kind: method
  qualified_name: trie/session_diff:SessionDiff.is_empty
  lines: 19-21
- kind: method
  qualified_name: trie/session_diff:SessionDiff.session_ids
  lines: 23-30
- kind: function
  qualified_name: trie/session_diff:_triefact_pathspecs
  lines: 33-46
- kind: function
  qualified_name: trie/session_diff:collect_session_diff
  lines: 49-108
- kind: function
  qualified_name: trie/session_diff:_one_line
  lines: 111-143
- kind: constant
  qualified_name: trie/session_diff:_FENCE
  lines: 146-146
- kind: function
  qualified_name: trie/session_diff:build_narrative_prompt
  lines: 149-221
- kind: class
  qualified_name: trie/session_diff:SessionNarrative
  lines: 224-258
- kind: method
  qualified_name: trie/session_diff:SessionNarrative.as_markdown
  lines: 238-258
- kind: constant
  qualified_name: trie/session_diff:_NARRATIVE_SYSTEM_PROMPT
  lines: 261-275
- kind: function
  qualified_name: trie/session_diff:synthesize_narrative
  lines: 278-322
- kind: function
  qualified_name: trie/session_diff:render_digest_section
  lines: 325-472
- kind: constant
  qualified_name: trie/session_diff:DIGEST_FILE_HEADER
  lines: 475-479
- kind: constant
  qualified_name: trie/session_diff:DIGEST_HEADING_RE
  lines: 485-489
- kind: function
  qualified_name: trie/session_diff:_parse_digest_file
  lines: 492-530
- kind: function
  qualified_name: trie/session_diff:iter_digest_entries
  lines: 533-545
- kind: function
  qualified_name: trie/session_diff:symbol_history
  lines: 548-580
- kind: function
  qualified_name: trie/session_diff:file_history
  lines: 583-611
- kind: function
  qualified_name: trie/session_diff:rows_from_digest_entry
  lines: 614-641
- kind: function
  qualified_name: trie/session_diff:_new_digest_filename
  lines: 644-655
- kind: function
  qualified_name: trie/session_diff:write_digest
  lines: 658-731
- kind: function
  qualified_name: trie/session_diff:collect_symbol_deltas
  lines: 734-841
- kind: function
  qualified_name: trie/session_diff:merge_applied_by_symbol
  lines: 844-862
incoming_refs: 6
outgoing_refs: 0
---
<!-- trie:section symbol=trie/session_diff:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=013090f2c0eff25aa3a245e1e001d311d7631093a9b3105b60ed2a55880195f9 source_ref=ac6022b60d3c7ae0d5a92f1a4a4baad1193147c7 role=orchestration -->
Provides session evidence collection, narrative synthesis, and digest persistence for `trie diff` workflows.

- `SessionDiff` — frozen dataclass holding raw git diff, applied patches, and pending patches for one session
- `collect_session_diff` — gathers live evidence (git diff + store rows) into a `SessionDiff`
- `build_narrative_prompt` — assembles deterministic LLM prompt from `SessionDiff` evidence
- `synthesize_narrative` — calls an LLM client to produce a structured `SessionNarrative`
- `render_digest_section` — renders one markdown digest entry from evidence and deltas
- `write_digest` — writes the rendered entry to a timestamped file and maintains the latest-symlink
- `collect_symbol_deltas` — computes per-symbol one-liner before/after deltas from the working tree
- `iter_digest_entries` / `_parse_digest_file` — read and parse the digest archive
- `symbol_history` / `file_history` — query the archive for a symbol's or module's intent trail
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:SessionDiff fingerprint=7c0b1e542ac3b479e297632536c9d57689d4ef3ee060d3adaadb6729307fa85d body_fp=b29b8bea214ab55e66d5e5a60c1fe5458b76d628ab0e7f3a6c3fcadbc696ee7c source_ref=ac6022b60d3c7ae0d5a92f1a4a4baad1193147c7 role=model -->
Immutable dataclass holding one session's evidence: a raw triefact git diff, sealed patch rows, and staged patch rows.

- `triefact_diff`: unified diff of the triefact tree against `base`.
- `applied`: patch rows already consumed (sealed) from the store.
- `pending`: patch rows staged but not yet applied.
- `base`: git ref the diff is computed against; defaults to `HEAD`.
- `is_empty()`: returns `True` when all three evidence fields are blank/empty.
- `session_ids()`: returns distinct non-empty `session_id` values across `applied` + `pending`, insertion-ordered.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:SessionDiff.is_empty fingerprint=b504b8745ff4143898c9714c49334e7cddcc10cdc565b4138d8a7af47c65b935 body_fp=6040131dd6138cce3b9d67c6c7dd8b115c0b326f9676dd0ea0df19405b4c97b9 source_ref=ac6022b60d3c7ae0d5a92f1a4a4baad1193147c7 role=domain -->
Returns `True` when `SessionDiff` has no diff text, no applied rows, and no pending rows.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:SessionDiff.session_ids fingerprint=f8703e92cc108bac529c20bce6b83766f976d0424f7683d4e60f831b962e00f2 body_fp=bd0a5a737da944e6bf00e4a5328e3ffb9452fdac3f9c3ab72bfb33978edadd0d source_ref=ac6022b60d3c7ae0d5a92f1a4a4baad1193147c7 role=domain -->
Return all distinct non-empty `session_id` values from `SessionDiff.applied` and `SessionDiff.pending`, preserving insertion order.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:_triefact_pathspecs fingerprint=c1584da79e5bd71fa3f6f87e83e878f6710c3c911a9e94b7a15582a62f005dbe body_fp=4af57e3caf077f952f1548210fa3349f41121a72c02b8a9580ca95eb157fcc7c source_ref=ac6022b60d3c7ae0d5a92f1a4a4baad1193147c7 role=util -->
Return git pathspecs covering the triefact root while excluding `config.diff.diffs_dir` and the root `README.md` to prevent digest files and the generated index from polluting evidence collection.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:collect_session_diff fingerprint=d5deda25aae97134ae780ee9e44af1419dbb22867ec644b8d2956e99746fb618 body_fp=abf373bc162527627c1859123535971f98ae883b744d8006ef10d7c897169cec source_ref=ac6022b60d3c7ae0d5a92f1a4a4baad1193147c7 role=orchestration -->
Gather one session's evidence into a `SessionDiff`: git diff of the triefact tree vs `base`, applied and pending rows built from the store's qname-keyed patches tables (no longer from a pending-intent file).

- `applied`: built via `store.get_all_patches_grouped(applied=True)` and `store.get_create_patches_grouped(applied=True)`; each entry carries `notes`, `reasons`, `session_note`, and `op`.
- `pending`: built via the same store methods with `applied=False`.
- `base`: git ref used as the diff baseline; defaults to `"HEAD"`.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:_one_line fingerprint=c9d246ecf903076038d2359f4e58b3377b6bf54c959c1b6eba19d30ac55795a3 body_fp=841114585aa8684f0cd69efb0b04199fe309daf2a83c450788450b07d7182c36 source_ref=ac6022b60d3c7ae0d5a92f1a4a4baad1193147c7 role=util -->
Extract the first non-empty line of `text`, collapse whitespace, truncate at the first sentence boundary or `max_chars`, appending `…` if hard-truncated.

- `max_chars`: character budget before hard truncation with ellipsis; hard cut prefers the last word boundary to avoid mid-word splits; default 160.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:_FENCE fingerprint=7c0a24375f67cb32fbd350a1aa89f4ee1f6465b35df8cd422b0b4544c79625fd body_fp=716700dda7d154daafd12f8d2485eb55825aa77b76cc55de6c0752655f91f4aa source_ref=ac6022b60d3c7ae0d5a92f1a4a4baad1193147c7 role=util -->
Module-level constant holding three backtick characters used to open and close fenced code blocks in prompt assembly.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:build_narrative_prompt fingerprint=5773311045be8b578e3b765937c1e6be9ed0a79774f919b8cea167a0cc3883c1 body_fp=76790cecac84122f570ad256b873d5d7c8e9bb3ec430dc8c50953fa378683610 source_ref=ac6022b60d3c7ae0d5a92f1a4a4baad1193147c7 role=orchestration -->
Assemble the LLM user prompt from a `SessionDiff`, ordering intent (patch notes) before observed effect (triefact diff), truncated to `max_diff_chars`.

- `max_diff_chars`: hard character cap on the raw diff block; excess is replaced with a truncation notice.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:SessionNarrative fingerprint=51f08fbd08fbfd4d9e39cdb7d1fc37af19ab3d91d7b60d0334d6c785991592ad body_fp=576725a688b271da6e1132b002e389395e052abcf1a63cf17758c1cf3b355c1f source_ref=ac6022b60d3c7ae0d5a92f1a4a4baad1193147c7 role=model -->
Pydantic model holding structured LLM output for one session's change digest narrative.

- `one_liner`: plain-text sentence (≤ ~25 words) summarising the net change; no markdown.
- `body`: full narrative markdown, max 120 words; no headings; must not restate `one_liner`.
- `conflicts`: one sentence per intent-vs-diff discrepancy naming the symbol; empty by default.
- `as_markdown()`: renders the three fields as a markdown block — bold `one_liner`, `body`, then each conflict as a `> **Intent vs. diff:**` blockquote line.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:SessionNarrative.as_markdown fingerprint=6e4e10690d4953fdf7b0acf410f46850d9857ffcaa0aae06b1d047afcedf8e80 body_fp=15408f121d5fd5faf3930a0a2d149b941d78b01a1dac1b94e22564b6433ee4a7 source_ref=ac6022b60d3c7ae0d5a92f1a4a4baad1193147c7 role=domain -->
Render `SessionNarrative` as a markdown string: bold `one_liner`, `body`, then each conflict as a `> **Intent vs. diff:**` blockquote, joined by blank lines.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:_NARRATIVE_SYSTEM_PROMPT fingerprint=5ae3e688d07cf82019d724e5e271f6c2b012681399899c6b3b97b57a5eb23c73 body_fp=736af664a527ba47cb51fdc2e9f8cfa2db7224dc02c3941926ff31ca4ce1d4cd source_ref=ac6022b60d3c7ae0d5a92f1a4a4baad1193147c7 role=config -->
System prompt string passed to the LLM in `synthesize_narrative`, instructing it to produce a structured `SessionNarrative` (one_liner + body + conflicts) from patch-note and triefact-diff evidence.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:synthesize_narrative fingerprint=42eb5b13ff05c64d804aaa596a5affd2182c18b83b00c6d5441a74f087d4b74f body_fp=500a624fa7adeae23f0f09d3c9f8703fc05901bab82dbd7a5789ce7cc142fa8c source_ref=ac6022b60d3c7ae0d5a92f1a4a4baad1193147c7 role=io -->
Send `SessionDiff` evidence to an LLM client and return a structured `SessionNarrative` (one_liner + body + conflicts).

- `client`: must expose `run`; `cache_prefix` kwarg is used when supported, otherwise falls back to a single-prompt call.
- `max_diff_chars`: forwarded to `build_narrative_prompt` to cap diff size before sending.
- `max_tokens`: runaway guard only; default raised to 1024 to avoid mid-sentence truncation.
- Returns a `SessionNarrative`; if the client returns bare text, wraps it defensively in `SessionNarrative(one_liner="", body=…)`.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:render_digest_section fingerprint=70fee0b244f4377bb62ae9afa610a980ef10986da6671855628826d1fff6bee0 body_fp=1df6f14879e4f5901ba5538d489c5a2a18d4124a09175143017426b83c3f2f61 source_ref=ac6022b60d3c7ae0d5a92f1a4a4baad1193147c7 role=domain -->
Render a `SessionDiff` as a single markdown digest-entry string with heading, optional narrative, per-symbol change bullets, and staged pending entries.

- `title` / `date_str` / `parent_short`: compose the `## …` heading used as an `upsert_digest` boundary anchor.
- `narrative`: heading levels `#` and `##` are demoted to `###` to prevent structural collisions.
- `deltas`: precomputed per-symbol diff rows; merged with `data.applied` by qname, applied-order first.
- `max_changes`: caps visible change bullets; overflow becomes a `… and N more` line **plus an HTML comment block** (`<!-- trie:changes-overflow … -->`) preserving all overflow rows for parsing by `_parse_digest_file`.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:DIGEST_FILE_HEADER fingerprint=953f1e9f7f8034daa19d5deb0c1e678442b7f17daadb9e7f5b87b94d13a32ebe body_fp=f688decefb16ed2e9df6e61b9b495e64c77ef53ec2a17f8192758caf7f24f7ed source_ref=ac6022b60d3c7ae0d5a92f1a4a4baad1193147c7 role=model -->
HTML comment prepended to every digest file warning that it is auto-generated and should not be edited by hand.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:DIGEST_HEADING_RE fingerprint=78c13b203259b9f5a435357b2341c22b26861c234924d85fa49293455be166f1 body_fp=2b8b72fff0cdc57f0f3141515c2aaf5a5770c5957a3177ca57f69d843f83022d source_ref=ac6022b60d3c7ae0d5a92f1a4a4baad1193147c7 role=config -->
Compiled multiline regex matching digest entry headings emitted by `render_digest_section`, capturing `title`, `date`, and `parent` SHA groups.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:_parse_digest_file fingerprint=8b340b9e1d0e020732bfa45e3660f0ff46f89591c72bedad8ce84f90e6fe0059 body_fp=6a5b5be524720fdf081b220df391cafa7578c44db68c231494816e6d78b6cb1d source_ref=ac6022b60d3c7ae0d5a92f1a4a4baad1193147c7 role=parsing -->
Parse a single digest file into `{name, title, date, parent, changes}`, returning `None` if no parseable entry heading is found.

- `changes`: per-symbol bullet lines from `### Changes`, stripped of leading `- `; overflow lines (`… and N more`) are excluded; lines inside `<!-- trie:changes-overflow … -->` blocks are included.
- Returns `None` on `OSError` or missing `DIGEST_HEADING_RE` match (foreign files in archive dir).
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:iter_digest_entries fingerprint=e1af40bb6403df2afd47800cd71d614eddcf6d5de125bf0e863d91ddcbf4f31e body_fp=14bcfc7841084b792135d2f7b68e130ba761abde6d371e5dd7b137a00e8369c9 source_ref=ac6022b60d3c7ae0d5a92f1a4a4baad1193147c7 role=persistence -->
Return all parsed digest entries from `diffs_dir` under `project_root`, sorted newest first by filename.

- `diffs_dir`: project-relative path to the digest archive directory.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:symbol_history fingerprint=866363c246d6d7467522638ef1dcbb489f4a703d73b3e6fb4ddde5b0789babaa body_fp=dba8315cd8bd867fe02323655ed01a8ec7cac7bb0d49c2f47d89ff4469a877cd source_ref=ac6022b60d3c7ae0d5a92f1a4a4baad1193147c7 role=domain -->
Search the digest archive for all entries mentioning `qname` and return up to `limit` rows newest-first.

- `qname`: exact qualified name matched against change-line markers (`~`, `+`, `−`).
- Returns `{date, title, change, digest}` per matching digest entry; at most one row per entry.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:file_history fingerprint=75e0ea8e87f82472ab1936c8e7467b3db68fabc8efe981bdf65da783899a419a body_fp=90b8fa73296d5f7718b8997eb6c45f2dce907e0b4072e4cdf01edfe7990024ff source_ref=ac6022b60d3c7ae0d5a92f1a4a4baad1193147c7 role=domain -->
Return up to `limit` digest entries touching any symbol in a module, newest first.

- `module_prefix`: qname module part without extension (e.g. `trie/session_diff`); matches `<prefix>:*` change lines.
- Each row contains `date`, `title`, `change` (marker + qname + description), and `digest` (filename).
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:rows_from_digest_entry fingerprint=6c1d4c44e841bacedaeff48aefadb105fb93fb8e2895c963269e466ac051ea01 body_fp=3fc39472b70afefced5863ccf0c797c4a89439154ca87fc5002009e2bd660e18 source_ref=ac6022b60d3c7ae0d5a92f1a4a4baad1193147c7 role=domain -->
Convert a parsed digest entry's `changes` lines back into applied-row dicts for amend/retry merging.

- `entry`: output of `_parse_digest_file`; uses `"changes"` and `"title"` keys
- Returns rows with `qname`, `op` (`modify`/`create`/`delete`), `notes`, `reasons`, `session_note`
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:_new_digest_filename fingerprint=1a7047bc70cbdc55046a26f41bb89c15ef3b774b5027bc3e5a524bfb3420f10c body_fp=881d2bdb34fc83bd71a476a4664058f046e54bb233f494554827c6e990b0d0fa source_ref=ac6022b60d3c7ae0d5a92f1a4a4baad1193147c7 role=util -->
Generate a digest filename combining a UTC timestamp and a UUID4 hex suffix, formatted as `<YYYYMMDDTHHMMSSz>-<uuid4hex>.md`.

- Timestamp prefix ensures lexicographic order equals chronological order.
- UUID suffix guarantees uniqueness within the same second.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:write_digest fingerprint=2d481309d53c9a983e4c6b2d320a4671331d48505f4a11a19574929799f2afc7 body_fp=7837b717eb63e71d8930f5718739b6c80ad077179db24c6681e4be191e5f6a2d source_ref=ac6022b60d3c7ae0d5a92f1a4a4baad1193147c7 role=io -->
Write a rendered digest section to a timestamped file under `diffs_dir`, atomically repoint the latest-symlink, and prune old entries.

- `reuse_file`: project-relative path to overwrite in place (amend/retry); creates a new file if absent or outside `diffs_dir`.
- `symlink_path`: relative symlink at project root pointing to the latest digest file; falls back to a plain text pointer on symlink-unsupported filesystems.
- `max_entries`: files beyond this count (by mtime, newest first) are unlinked from disk but retained in git history.
- Returns the project-relative path of the file written.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:collect_symbol_deltas fingerprint=313196f2dad6a3ecbf02fd525acc27ecad2ddc70e394332b331b7d2bb2a70b8c body_fp=7358074bbb75e94a5f7e447dd356b7339d69a794f24eaf4b593f214cf7d2d1be source_ref=ac6022b60d3c7ae0d5a92f1a4a4baad1193147c7 role=domain -->
Diff the triefact tree against `base`, parse each changed file into `{qname: one_liner}` maps, and return a sorted list of per-symbol delta dicts.

- `status`: one of `"added"`, `"removed"`, or `"changed"`; `"changed"` rows are suppressed when the one-liner is identical (churn gate)
- Returns dicts with keys `file`, `qname`, `status`, and `before`/`after` as applicable; sorted by `(file, qname)`
- Silently skips any file that raises an exception during processing
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:merge_applied_by_symbol fingerprint=74952e7ab3f4a68835b255f9cfddd3440c0e18793ecea3ba49ef5464a76e2cb3 body_fp=760d01e91eda022e2e8ca765dba32d75870c0eab79b36bc8349e719c85724454 source_ref=ac6022b60d3c7ae0d5a92f1a4a4baad1193147c7 role=domain -->
Collapse a list of applied patch-log entries into one merged record per `qname`, counting repeated notes as follow-ups.

- `followups`: count of notes beyond the first; each subsequent entry contributes `max(len(notes), 1)`.
- Returns insertion-ordered list of `{qname, op, note, followups}` dicts.
<!-- trie:end -->