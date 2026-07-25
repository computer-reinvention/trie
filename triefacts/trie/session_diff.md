---
trie_version: 0.1.9
source: trie/session_diff.py
file_fingerprint: ff21966379c1c0c5993158671f9f42013c27c371072d60fd26e633a57b70c563
last_synced_at: '2026-07-25T01:52:10Z'
defines:
- kind: module
  qualified_name: trie/session_diff:__module__
  lines: 1-606
- kind: class
  qualified_name: trie/session_diff:SessionDiff
  lines: 8-27
- kind: method
  qualified_name: trie/session_diff:SessionDiff.is_empty
  lines: 16-18
- kind: method
  qualified_name: trie/session_diff:SessionDiff.session_ids
  lines: 20-27
- kind: function
  qualified_name: trie/session_diff:_triefact_pathspecs
  lines: 30-43
- kind: function
  qualified_name: trie/session_diff:collect_session_diff
  lines: 46-79
- kind: function
  qualified_name: trie/session_diff:_one_line
  lines: 82-114
- kind: constant
  qualified_name: trie/session_diff:_FENCE
  lines: 117-117
- kind: function
  qualified_name: trie/session_diff:build_narrative_prompt
  lines: 120-192
- kind: constant
  qualified_name: trie/session_diff:_NARRATIVE_SYSTEM_PROMPT
  lines: 195-204
- kind: function
  qualified_name: trie/session_diff:synthesize_narrative
  lines: 207-235
- kind: function
  qualified_name: trie/session_diff:render_digest_section
  lines: 238-377
- kind: constant
  qualified_name: trie/session_diff:DIGEST_FILE_HEADER
  lines: 380-384
- kind: function
  qualified_name: trie/session_diff:_new_digest_filename
  lines: 387-398
- kind: function
  qualified_name: trie/session_diff:write_digest
  lines: 401-474
- kind: function
  qualified_name: trie/session_diff:collect_symbol_deltas
  lines: 477-584
- kind: function
  qualified_name: trie/session_diff:merge_applied_by_symbol
  lines: 587-605
incoming_refs: 7
outgoing_refs: 0
---
<!-- trie:section symbol=trie/session_diff:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=f7ac74e700c9f55a4df46bc527fd1934f92f28b128cdb3a9aa08fcdc246c476a source_ref=2fd24a66abd87a87819892d8d61ea7471cee29cb role=domain -->
Defines `SessionDiff` and utilities for collecting, formatting, and synthesising LLM narratives from per-session triefact diffs and patch notes.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:SessionDiff fingerprint=7c0b1e542ac3b479e297632536c9d57689d4ef3ee060d3adaadb6729307fa85d body_fp=099e1a45d5f9276ca9c87608b05863ae8aff4d045b9903a76b0d559c4f797a3c role=monitoring-telemetry -->
`SessionDiff` is a dataclass that bundles all evidence gathered for a single working session during a `trie diff` run: the raw git diff of the triefact tree (the observed effect), a list of patch notes that agents have already applied (stated intent from the session log archive), and a list of patch notes still pending in the store's patch queue. It exposes helpers to check whether there is anything substantive to report (`is_empty`) and to enumerate the distinct session identifiers that appear across both note collections (`session_ids`), providing a self-contained evidence package that downstream functions use to assemble prompts and synthesise intent-level narratives via the LLM.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:SessionDiff.is_empty fingerprint=b504b8745ff4143898c9714c49334e7cddcc10cdc565b4138d8a7af47c65b935 body_fp=5234d8be87e1b1a18b15c598ba1072f96483ee8544646ea3d00c11b30fbe2976 source_ref=2fd24a66abd87a87819892d8d61ea7471cee29cb role=domain -->
Return `True` when `SessionDiff` has no diff text, no applied entries, and no pending entries.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:SessionDiff.session_ids fingerprint=f8703e92cc108bac529c20bce6b83766f976d0424f7683d4e60f831b962e00f2 body_fp=a965b48afc59b753e1813be79724b80ffd65d52960bca31c9e3774495446941a source_ref=2fd24a66abd87a87819892d8d61ea7471cee29cb role=domain -->
Return distinct, non-empty session IDs from `SessionDiff.applied` and `SessionDiff.pending`, preserving insertion order.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:_triefact_pathspecs fingerprint=c1584da79e5bd71fa3f6f87e83e878f6710c3c911a9e94b7a15582a62f005dbe body_fp=4af57e3caf077f952f1548210fa3349f41121a72c02b8a9580ca95eb157fcc7c source_ref=876ccb9eaba2478453b69c9d3923da1f51105118 role=util -->
Return git pathspecs covering the triefact root while excluding `config.diff.diffs_dir` and the root `README.md` to prevent digest files and the generated index from polluting evidence collection.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:collect_session_diff fingerprint=c890a4f48029ac679e66239a6d6522bc61572276a1a52cc2da911309cdb1ecf2 body_fp=a559ab9075f3b849a287b0bb954b2f5622db71a9fad5d5d02f26a30d95011351 source_ref=4c4e91c3c881299bbd6cbb84617acdafd0760205 role=orchestration -->
Gather one session's evidence into a `SessionDiff`: git diff of the triefact tree vs `base`, applied patch notes from the session log, and pending patch notes from the store.

- `session_id`: `None` collects across all sessions; otherwise filters both applied and pending entries.
- `since`: restricts applied log entries to those recorded after the given Unix timestamp.
- `base`: git ref used as the diff baseline; defaults to `"HEAD"`.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:_one_line fingerprint=c9d246ecf903076038d2359f4e58b3377b6bf54c959c1b6eba19d30ac55795a3 body_fp=841114585aa8684f0cd69efb0b04199fe309daf2a83c450788450b07d7182c36 source_ref=6496768f11e8dbbd9f62de10da624109491b7be3 role=util -->
Extract the first non-empty line of `text`, collapse whitespace, truncate at the first sentence boundary or `max_chars`, appending `…` if hard-truncated.

- `max_chars`: character budget before hard truncation with ellipsis; hard cut prefers the last word boundary to avoid mid-word splits; default 160.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:_FENCE fingerprint=7c0a24375f67cb32fbd350a1aa89f4ee1f6465b35df8cd422b0b4544c79625fd body_fp=495f5faefeb45ddc9bcce9c02534008c66427931a9356c9dbaa0b4f96ac92de2 source_ref=2fd24a66abd87a87819892d8d61ea7471cee29cb role=util -->
Module-level constant holding a triple-backtick string used to open and close fenced code blocks in prompt assembly.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:build_narrative_prompt fingerprint=5773311045be8b578e3b765937c1e6be9ed0a79774f919b8cea167a0cc3883c1 body_fp=527197f111b13f32dd55a7e79273a8e63bf4766bd070e6b7b0e4a59a358c2ad9 source_ref=2fd24a66abd87a87819892d8d61ea7471cee29cb role=util -->
Assemble the LLM user prompt from a `SessionDiff`, ordering session intents, applied patch notes, pending patch notes, and the raw triefact diff as Markdown sections.

- `max_diff_chars`: hard character limit at which the diff block is truncated before inclusion.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:_NARRATIVE_SYSTEM_PROMPT fingerprint=94f4e4216e8a9d9fc06825bafedd1bc8ae49d871919761f6fe9d2b579baa8d7f body_fp=07b82799f6257750ff5cb583288729e2f27720d65cac7e0fd9b15446d3f73ecf source_ref=b52fb7d875efc22b57e789d47535774fa98128e8 role=config -->
System prompt string passed to the LLM in `synthesize_narrative`, instructing it to produce a ≤120-word plain-markdown PR change digest from patch-note and triefact-diff evidence.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:synthesize_narrative fingerprint=6fce00f5e91562cd9f5469fd3086084b1875dc517acbd71920a6f1fbb590217a body_fp=087844e6f141b58f246e002987af61b63be0febf0172142e9324810f22d663c4 source_ref=b52fb7d875efc22b57e789d47535774fa98128e8 role=io -->
Send `SessionDiff` evidence to an LLM client and return a concise markdown session narrative.

- `client`: must expose `run_text`; `cache_prefix` kwarg is used when supported, otherwise falls back to a single-prompt call.
- `max_diff_chars`: forwarded to `build_narrative_prompt` to cap diff size before sending.
- Returns stripped markdown text from `result.output`.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:render_digest_section fingerprint=f10f6e53343eafd65a948ead2e37a63c1b0601e432cdec6c33e732e787fac7ca body_fp=019a5dfbae1a48a62cf17db686254b0ee9b73d94725ecfdc7d56bd932318835d source_ref=b52fb7d875efc22b57e789d47535774fa98128e8 role=domain -->
Render a `SessionDiff` as a single markdown digest-entry string with heading, optional narrative, per-symbol change bullets, and staged pending entries.

- `title` / `date_str` / `parent_short`: compose the `## …` heading used as an `upsert_digest` boundary anchor.
- `narrative`: heading levels `#` and `##` are demoted to `###` to prevent structural collisions.
- `deltas`: precomputed per-symbol diff rows; merged with `data.applied` by qname, applied-order first.
- `max_changes`: caps change bullets; overflow becomes a `… and N more` line.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:DIGEST_FILE_HEADER fingerprint=953f1e9f7f8034daa19d5deb0c1e678442b7f17daadb9e7f5b87b94d13a32ebe body_fp=f688decefb16ed2e9df6e61b9b495e64c77ef53ec2a17f8192758caf7f24f7ed source_ref=7fd2d148e339b19fb869f262ffbed20d2c29c036 role=config -->
HTML comment prepended to every digest file warning that it is auto-generated and should not be edited by hand.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:_new_digest_filename fingerprint=1a7047bc70cbdc55046a26f41bb89c15ef3b774b5027bc3e5a524bfb3420f10c body_fp=881d2bdb34fc83bd71a476a4664058f046e54bb233f494554827c6e990b0d0fa source_ref=7fd2d148e339b19fb869f262ffbed20d2c29c036 role=util -->
Generate a digest filename combining a UTC timestamp and a UUID4 hex suffix, formatted as `<YYYYMMDDTHHMMSSz>-<uuid4hex>.md`.

- Timestamp prefix ensures lexicographic order equals chronological order.
- UUID suffix guarantees uniqueness within the same second.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:write_digest fingerprint=2d481309d53c9a983e4c6b2d320a4671331d48505f4a11a19574929799f2afc7 body_fp=7837b717eb63e71d8930f5718739b6c80ad077179db24c6681e4be191e5f6a2d source_ref=7fd2d148e339b19fb869f262ffbed20d2c29c036 role=io -->
Write a rendered digest section to a timestamped file under `diffs_dir`, atomically repoint the latest-symlink, and prune old entries.

- `reuse_file`: project-relative path to overwrite in place (amend/retry); creates a new file if absent or outside `diffs_dir`.
- `symlink_path`: relative symlink at project root pointing to the latest digest file; falls back to a plain text pointer on symlink-unsupported filesystems.
- `max_entries`: files beyond this count (by mtime, newest first) are unlinked from disk but retained in git history.
- Returns the project-relative path of the file written.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:collect_symbol_deltas fingerprint=313196f2dad6a3ecbf02fd525acc27ecad2ddc70e394332b331b7d2bb2a70b8c body_fp=7358074bbb75e94a5f7e447dd356b7339d69a794f24eaf4b593f214cf7d2d1be source_ref=4c4e91c3c881299bbd6cbb84617acdafd0760205 role=domain -->
Diff the triefact tree against `base`, parse each changed file into `{qname: one_liner}` maps, and return a sorted list of per-symbol delta dicts.

- `status`: one of `"added"`, `"removed"`, or `"changed"`; `"changed"` rows are suppressed when the one-liner is identical (churn gate)
- Returns dicts with keys `file`, `qname`, `status`, and `before`/`after` as applicable; sorted by `(file, qname)`
- Silently skips any file that raises an exception during processing
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:merge_applied_by_symbol fingerprint=74952e7ab3f4a68835b255f9cfddd3440c0e18793ecea3ba49ef5464a76e2cb3 body_fp=760d01e91eda022e2e8ca765dba32d75870c0eab79b36bc8349e719c85724454 source_ref=b52fb7d875efc22b57e789d47535774fa98128e8 role=util -->
Collapse a list of applied patch-log entries into one merged record per `qname`, counting repeated notes as follow-ups.

- `followups`: count of notes beyond the first; each subsequent entry contributes `max(len(notes), 1)`.
- Returns insertion-ordered list of `{qname, op, note, followups}` dicts.
<!-- trie:end -->