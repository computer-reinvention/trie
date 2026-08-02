---
trie_version: 0.3.0
source: trie/session_diff.py
file_fingerprint: 4bf16215ed8b60feaf14439bc2af3a62856120983a341f8647a60b4ea870090b
last_synced_at: '2026-08-02T21:19:45Z'
defines:
- kind: module
  qualified_name: trie/session_diff:__module__
  lines: 1-882
- kind: class
  qualified_name: trie/session_diff:SessionDiff
  lines: 11-30
  signature: class SessionDiff
- kind: method
  qualified_name: trie/session_diff:SessionDiff.is_empty
  lines: 19-21
  signature: def is_empty(self) -> bool
- kind: method
  qualified_name: trie/session_diff:SessionDiff.session_ids
  lines: 23-30
  signature: def session_ids(self) -> list[str]
- kind: function
  qualified_name: trie/session_diff:_triefact_pathspecs
  lines: 33-46
  signature: 'def _triefact_pathspecs(config: Any) -> list[str]'
- kind: function
  qualified_name: trie/session_diff:collect_session_diff
  lines: 49-108
  signature: 'def collect_session_diff( project_root: Any, config: Any, store: Any, *, base: str = "HEAD", ) -> SessionDiff'
- kind: function
  qualified_name: trie/session_diff:_one_line
  lines: 111-143
  signature: 'def _one_line(text: str, max_chars: int = 160) -> str'
- kind: function
  qualified_name: trie/session_diff:_first_line
  lines: 146-162
  signature: 'def _first_line(text: str) -> str'
- kind: constant
  qualified_name: trie/session_diff:_FENCE
  lines: 165-165
- kind: function
  qualified_name: trie/session_diff:build_narrative_prompt
  lines: 168-240
  signature: 'def build_narrative_prompt(data: SessionDiff, *, max_diff_chars: int = 24000) -> str'
- kind: class
  qualified_name: trie/session_diff:SessionNarrative
  lines: 243-277
  signature: class SessionNarrative(BaseModel)
- kind: method
  qualified_name: trie/session_diff:SessionNarrative.as_markdown
  lines: 257-277
  signature: def as_markdown(self) -> str
- kind: constant
  qualified_name: trie/session_diff:_NARRATIVE_SYSTEM_PROMPT
  lines: 280-294
- kind: function
  qualified_name: trie/session_diff:synthesize_narrative
  lines: 297-341
  signature: 'def synthesize_narrative( data: SessionDiff, client: Any, *, max_diff_chars: int = 24000, max_tokens: int = 1024 ) -> SessionNarrative'
- kind: function
  qualified_name: trie/session_diff:render_digest_section
  lines: 344-491
  signature: 'def render_digest_section( data: SessionDiff, *, title: str, date_str: str, parent_short: str, narrative: str = "", deltas: list[dict] | None = None, max_changes: int = 20, ) -> str'
- kind: constant
  qualified_name: trie/session_diff:DIGEST_FILE_HEADER
  lines: 494-498
- kind: constant
  qualified_name: trie/session_diff:DIGEST_HEADING_RE
  lines: 504-508
- kind: function
  qualified_name: trie/session_diff:_parse_digest_file
  lines: 511-549
  signature: 'def _parse_digest_file(path: Any) -> dict | None'
- kind: function
  qualified_name: trie/session_diff:iter_digest_entries
  lines: 552-564
  signature: 'def iter_digest_entries(project_root: Any, *, diffs_dir: str = "triefacts/triediffs") -> list[dict]'
- kind: function
  qualified_name: trie/session_diff:symbol_history
  lines: 567-599
  signature: 'def symbol_history( project_root: Any, qname: str, *, diffs_dir: str = "triefacts/triediffs", limit: int = 5, ) -> list[dict]'
- kind: function
  qualified_name: trie/session_diff:file_history
  lines: 602-630
  signature: 'def file_history( project_root: Any, module_prefix: str, *, diffs_dir: str = "triefacts/triediffs", limit: int = 5, ) -> list[dict]'
- kind: function
  qualified_name: trie/session_diff:rows_from_digest_entry
  lines: 633-660
  signature: 'def rows_from_digest_entry(entry: dict) -> list[dict]'
- kind: function
  qualified_name: trie/session_diff:_new_digest_filename
  lines: 663-674
  signature: def _new_digest_filename() -> str
- kind: function
  qualified_name: trie/session_diff:write_digest
  lines: 677-750
  signature: 'def write_digest( project_root: Any, section: str, *, diffs_dir: str = "triefacts/triediffs", symlink_path: str = "TRIE_DIFF.md", max_entries: int = 20, reuse_file: str | None = None, ) -> str'
- kind: function
  qualified_name: trie/session_diff:collect_symbol_deltas
  lines: 753-860
  signature: 'def collect_symbol_deltas(project_root, config, base: str = "HEAD") -> list'
- kind: function
  qualified_name: trie/session_diff:merge_applied_by_symbol
  lines: 863-881
  signature: 'def merge_applied_by_symbol(applied: list[dict]) -> list[dict]'
incoming_refs: 44
outgoing_refs: 7
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
<!-- trie:section symbol=trie/session_diff:SessionDiff fingerprint=7c0b1e542ac3b479e297632536c9d57689d4ef3ee060d3adaadb6729307fa85d body_fp=0ce278ed48d87d74fe215ee251734d2ca8597cd2e626c5abe920e9a5415f3c31 source_ref=ac6022b60d3c7ae0d5a92f1a4a4baad1193147c7 role=model -->
## `class SessionDiff`

Immutable dataclass holding one session's evidence: a raw triefact git diff, sealed patch rows, and staged patch rows.

- `triefact_diff`: unified diff of the triefact tree against `base`.
- `applied`: patch rows already consumed (sealed) from the store.
- `pending`: patch rows staged but not yet applied.
- `base`: git ref the diff is computed against; defaults to `HEAD`.
- `is_empty()`: returns `True` when all three evidence fields are blank/empty.
- `session_ids()`: returns distinct non-empty `session_id` values across `applied` + `pending`, insertion-ordered.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:SessionDiff.is_empty fingerprint=b504b8745ff4143898c9714c49334e7cddcc10cdc565b4138d8a7af47c65b935 body_fp=cbaa448751aabaf6898a99dd09a205ec0190f086f932de01e5f0469f47713ec1 source_ref=ac6022b60d3c7ae0d5a92f1a4a4baad1193147c7 role=domain -->
## `def is_empty(self) -> bool`

Returns `True` when `SessionDiff` has no diff text, no applied rows, and no pending rows.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:SessionDiff.session_ids fingerprint=f8703e92cc108bac529c20bce6b83766f976d0424f7683d4e60f831b962e00f2 body_fp=6db0f22c9d20a592191f596e51544a25789e5af54c19c82b46ff236c0fcd7898 source_ref=ac6022b60d3c7ae0d5a92f1a4a4baad1193147c7 role=domain -->
## `def session_ids(self) -> list[str]`

Return all distinct non-empty `session_id` values from `SessionDiff.applied` and `SessionDiff.pending`, preserving insertion order.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:_triefact_pathspecs fingerprint=c1584da79e5bd71fa3f6f87e83e878f6710c3c911a9e94b7a15582a62f005dbe body_fp=73c5029eb433b01929d9011ddf7d3550a4f28b4d06dfd2fa6d297d44e5af841e source_ref=ac6022b60d3c7ae0d5a92f1a4a4baad1193147c7 role=util -->
## `def _triefact_pathspecs(config: Any) -> list[str]`

Return git pathspecs covering the triefact root while excluding `config.diff.diffs_dir` and the root `README.md` to prevent digest files and the generated index from polluting evidence collection.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:collect_session_diff fingerprint=d5deda25aae97134ae780ee9e44af1419dbb22867ec644b8d2956e99746fb618 body_fp=c90ff31148dbe99c067edca6ce2eed58217b729d23e2392efe96387b70e3b2b7 source_ref=ac6022b60d3c7ae0d5a92f1a4a4baad1193147c7 role=orchestration -->
## `def collect_session_diff( project_root: Any, config: Any, store: Any, *, base: str = "HEAD", ) -> SessionDiff`

Gather one session's evidence into a `SessionDiff`: git diff of the triefact tree vs `base`, applied and pending rows built from the store's qname-keyed patches tables (no longer from a pending-intent file).

- `applied`: built via `store.get_all_patches_grouped(applied=True)` and `store.get_create_patches_grouped(applied=True)`; each entry carries `notes`, `reasons`, `session_note`, and `op`.
- `pending`: built via the same store methods with `applied=False`.
- `base`: git ref used as the diff baseline; defaults to `"HEAD"`.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:_one_line fingerprint=c9d246ecf903076038d2359f4e58b3377b6bf54c959c1b6eba19d30ac55795a3 body_fp=133ba9d12fef544fbd0f04765fc4a3b048b39f7c1ff7e2e64bc6f34b7c2a570d source_ref=ac6022b60d3c7ae0d5a92f1a4a4baad1193147c7 role=util -->
## `def _one_line(text: str, max_chars: int = 160) -> str`

Extract the first non-empty line of `text`, collapse whitespace, truncate at the first sentence boundary or `max_chars`, appending `…` if hard-truncated.

- `max_chars`: character budget before hard truncation with ellipsis; hard cut prefers the last word boundary to avoid mid-word splits; default 160.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:_first_line fingerprint=fad7fea6a2051dbda83458ee172021c0594d470f1bfaab108853f42fa6f6971b body_fp=4fd786524a2475b5d8761929a33600619b9d29f0f2be96f502c15a4d5c131e39 source_ref=524bcb92d10e2b1f1c66e559b1e78d5aaec69675 role=util -->
## `def _first_line(text: str) -> str`

Return the first non-empty line of `text` with whitespace runs collapsed to single spaces, without truncation or ellipsis.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:_FENCE fingerprint=7c0a24375f67cb32fbd350a1aa89f4ee1f6465b35df8cd422b0b4544c79625fd body_fp=716700dda7d154daafd12f8d2485eb55825aa77b76cc55de6c0752655f91f4aa source_ref=ac6022b60d3c7ae0d5a92f1a4a4baad1193147c7 role=util -->
Module-level constant holding three backtick characters used to open and close fenced code blocks in prompt assembly.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:build_narrative_prompt fingerprint=5773311045be8b578e3b765937c1e6be9ed0a79774f919b8cea167a0cc3883c1 body_fp=dfc7ce3ac525c3c75067dff70d4913e8d20a78f998c564806776665f0a3fac3f source_ref=ac6022b60d3c7ae0d5a92f1a4a4baad1193147c7 role=orchestration -->
## `def build_narrative_prompt(data: SessionDiff, *, max_diff_chars: int = 24000) -> str`

Assemble the LLM user prompt from a `SessionDiff`, ordering intent (patch notes) before observed effect (triefact diff), truncated to `max_diff_chars`.

- `max_diff_chars`: hard character cap on the raw diff block; excess is replaced with a truncation notice.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:SessionNarrative fingerprint=51f08fbd08fbfd4d9e39cdb7d1fc37af19ab3d91d7b60d0334d6c785991592ad body_fp=56cd12eee5e4d243653e77e37edf52d6850b15efda29cb8733bc178daaded1fa source_ref=ac6022b60d3c7ae0d5a92f1a4a4baad1193147c7 role=model -->
## `class SessionNarrative(BaseModel)`

Pydantic model holding structured LLM output for one session's change digest narrative.

- `one_liner`: plain-text sentence (≤ ~25 words) summarising the net change; no markdown.
- `body`: full narrative markdown, max 120 words; no headings; must not restate `one_liner`.
- `conflicts`: one sentence per intent-vs-diff discrepancy naming the symbol; empty by default.
- `as_markdown()`: renders the three fields as a markdown block — bold `one_liner`, `body`, then each conflict as a `> **Intent vs. diff:**` blockquote line.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:SessionNarrative.as_markdown fingerprint=6e4e10690d4953fdf7b0acf410f46850d9857ffcaa0aae06b1d047afcedf8e80 body_fp=4020639e624dfde82f8adcdc49befb0b1abc58c1e6474598a0f5317772b0fdd4 source_ref=ac6022b60d3c7ae0d5a92f1a4a4baad1193147c7 role=domain -->
## `def as_markdown(self) -> str`

Render `SessionNarrative` as a markdown string: bold `one_liner`, `body`, then each conflict as a `> **Intent vs. diff:**` blockquote, joined by blank lines.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:_NARRATIVE_SYSTEM_PROMPT fingerprint=5ae3e688d07cf82019d724e5e271f6c2b012681399899c6b3b97b57a5eb23c73 body_fp=736af664a527ba47cb51fdc2e9f8cfa2db7224dc02c3941926ff31ca4ce1d4cd source_ref=ac6022b60d3c7ae0d5a92f1a4a4baad1193147c7 role=config -->
System prompt string passed to the LLM in `synthesize_narrative`, instructing it to produce a structured `SessionNarrative` (one_liner + body + conflicts) from patch-note and triefact-diff evidence.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:synthesize_narrative fingerprint=42eb5b13ff05c64d804aaa596a5affd2182c18b83b00c6d5441a74f087d4b74f body_fp=7ae6618a1baa9ed3d3e2015e6caaf27c581c57e1f8213294523a9fed2a198d2a source_ref=ac6022b60d3c7ae0d5a92f1a4a4baad1193147c7 role=io -->
## `def synthesize_narrative( data: SessionDiff, client: Any, *, max_diff_chars: int = 24000, max_tokens: int = 1024 ) -> SessionNarrative`

Send `SessionDiff` evidence to an LLM client and return a structured `SessionNarrative` (one_liner + body + conflicts).

- `client`: must expose `run`; `cache_prefix` kwarg is used when supported, otherwise falls back to a single-prompt call.
- `max_diff_chars`: forwarded to `build_narrative_prompt` to cap diff size before sending.
- `max_tokens`: runaway guard only; default raised to 1024 to avoid mid-sentence truncation.
- Returns a `SessionNarrative`; if the client returns bare text, wraps it defensively in `SessionNarrative(one_liner="", body=…)`.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:render_digest_section fingerprint=7f31b182db9d18f0771b151e1fd7873fb19c79f3f033cfcbd5e2a91b4707b1dc body_fp=3c98aa04145164d4db453f16f637d1c70a94cef933b3e8b816906ad384d99318 source_ref=524bcb92d10e2b1f1c66e559b1e78d5aaec69675 role=domain -->
## `def render_digest_section( data: SessionDiff, *, title: str, date_str: str, parent_short: str, narrative: str = "", deltas: list[dict] | None = None, max_changes: int = 20, ) -> str`

Render a `SessionDiff` as a single markdown digest-entry string with heading, optional narrative, per-symbol change bullets, and staged pending entries.

- `title` / `date_str` / `parent_short`: compose the `## …` heading used as an `upsert_digest` boundary anchor.
- `narrative`: heading levels `#` and `##` are demoted to `###` to prevent structural collisions.
- `deltas`: precomputed per-symbol diff rows; merged with `data.applied` by qname, applied-order first; one-liner text is extracted via `_first_line` (no truncation or ellipsis) rather than `_one_line`.
- `max_changes`: caps visible change bullets; overflow becomes a `… and N more` line **plus an HTML comment block** (`<!-- trie:changes-overflow … -->`) preserving all overflow rows for parsing by `_parse_digest_file`.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:DIGEST_FILE_HEADER fingerprint=953f1e9f7f8034daa19d5deb0c1e678442b7f17daadb9e7f5b87b94d13a32ebe body_fp=f688decefb16ed2e9df6e61b9b495e64c77ef53ec2a17f8192758caf7f24f7ed source_ref=ac6022b60d3c7ae0d5a92f1a4a4baad1193147c7 role=model -->
HTML comment prepended to every digest file warning that it is auto-generated and should not be edited by hand.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:DIGEST_HEADING_RE fingerprint=78c13b203259b9f5a435357b2341c22b26861c234924d85fa49293455be166f1 body_fp=2b8b72fff0cdc57f0f3141515c2aaf5a5770c5957a3177ca57f69d843f83022d source_ref=ac6022b60d3c7ae0d5a92f1a4a4baad1193147c7 role=config -->
Compiled multiline regex matching digest entry headings emitted by `render_digest_section`, capturing `title`, `date`, and `parent` SHA groups.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:_parse_digest_file fingerprint=8b340b9e1d0e020732bfa45e3660f0ff46f89591c72bedad8ce84f90e6fe0059 body_fp=602692511a864aeeab2aee57f274ae8dd51b161111c1d1e02bd78215397234d6 source_ref=ac6022b60d3c7ae0d5a92f1a4a4baad1193147c7 role=parsing -->
## `def _parse_digest_file(path: Any) -> dict | None`

Parse a single digest file into `{name, title, date, parent, changes}`, returning `None` if no parseable entry heading is found.

- `changes`: per-symbol bullet lines from `### Changes`, stripped of leading `- `; overflow lines (`… and N more`) are excluded; lines inside `<!-- trie:changes-overflow … -->` blocks are included.
- Returns `None` on `OSError` or missing `DIGEST_HEADING_RE` match (foreign files in archive dir).
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:iter_digest_entries fingerprint=e1af40bb6403df2afd47800cd71d614eddcf6d5de125bf0e863d91ddcbf4f31e body_fp=e668d47a6886d4feb3b49ad43c92926a464eaa96daa8b468a48756a1366d4e41 source_ref=ac6022b60d3c7ae0d5a92f1a4a4baad1193147c7 role=persistence -->
## `def iter_digest_entries(project_root: Any, *, diffs_dir: str = "triefacts/triediffs") -> list[dict]`

Return all parsed digest entries from `diffs_dir` under `project_root`, sorted newest first by filename.

- `diffs_dir`: project-relative path to the digest archive directory.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:symbol_history fingerprint=866363c246d6d7467522638ef1dcbb489f4a703d73b3e6fb4ddde5b0789babaa body_fp=67939d02b60bcc477b32987152009911b538c4c84c368a27d78073aaa7493fbf source_ref=ac6022b60d3c7ae0d5a92f1a4a4baad1193147c7 role=domain -->
## `def symbol_history( project_root: Any, qname: str, *, diffs_dir: str = "triefacts/triediffs", limit: int = 5, ) -> list[dict]`

Search the digest archive for all entries mentioning `qname` and return up to `limit` rows newest-first.

- `qname`: exact qualified name matched against change-line markers (`~`, `+`, `−`).
- Returns `{date, title, change, digest}` per matching digest entry; at most one row per entry.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:file_history fingerprint=75e0ea8e87f82472ab1936c8e7467b3db68fabc8efe981bdf65da783899a419a body_fp=3254108cc98ed06f8a109adb58f00f78f267c30fff9ff1ed7a4102343aec0fd5 source_ref=ac6022b60d3c7ae0d5a92f1a4a4baad1193147c7 role=domain -->
## `def file_history( project_root: Any, module_prefix: str, *, diffs_dir: str = "triefacts/triediffs", limit: int = 5, ) -> list[dict]`

Return up to `limit` digest entries touching any symbol in a module, newest first.

- `module_prefix`: qname module part without extension (e.g. `trie/session_diff`); matches `<prefix>:*` change lines.
- Each row contains `date`, `title`, `change` (marker + qname + description), and `digest` (filename).
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:rows_from_digest_entry fingerprint=6c1d4c44e841bacedaeff48aefadb105fb93fb8e2895c963269e466ac051ea01 body_fp=7a1d629db9a3aa54640d07979e2a2685e99fc34c82c5831581861a4335456ae5 source_ref=ac6022b60d3c7ae0d5a92f1a4a4baad1193147c7 role=domain -->
## `def rows_from_digest_entry(entry: dict) -> list[dict]`

Convert a parsed digest entry's `changes` lines back into applied-row dicts for amend/retry merging.

- `entry`: output of `_parse_digest_file`; uses `"changes"` and `"title"` keys
- Returns rows with `qname`, `op` (`modify`/`create`/`delete`), `notes`, `reasons`, `session_note`
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:_new_digest_filename fingerprint=1a7047bc70cbdc55046a26f41bb89c15ef3b774b5027bc3e5a524bfb3420f10c body_fp=032cbd70f8c19d6b1c3ea9cf2059b14f7fca5e4c0a0e16f3fd30bbf7d62a916b source_ref=ac6022b60d3c7ae0d5a92f1a4a4baad1193147c7 role=util -->
## `def _new_digest_filename() -> str`

Generate a digest filename combining a UTC timestamp and a UUID4 hex suffix, formatted as `<YYYYMMDDTHHMMSSz>-<uuid4hex>.md`.

- Timestamp prefix ensures lexicographic order equals chronological order.
- UUID suffix guarantees uniqueness within the same second.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:write_digest fingerprint=2d481309d53c9a983e4c6b2d320a4671331d48505f4a11a19574929799f2afc7 body_fp=f361bf4e7d56d77c13e6c3f058d1e8316eb190fdbfb490ec3bae622c573fa7cd source_ref=ac6022b60d3c7ae0d5a92f1a4a4baad1193147c7 role=io -->
## `def write_digest( project_root: Any, section: str, *, diffs_dir: str = "triefacts/triediffs", symlink_path: str = "TRIE_DIFF.md", max_entries: int = 20, reuse_file: str | None = None, ) -> str`

Write a rendered digest section to a timestamped file under `diffs_dir`, atomically repoint the latest-symlink, and prune old entries.

- `reuse_file`: project-relative path to overwrite in place (amend/retry); creates a new file if absent or outside `diffs_dir`.
- `symlink_path`: relative symlink at project root pointing to the latest digest file; falls back to a plain text pointer on symlink-unsupported filesystems.
- `max_entries`: files beyond this count (by mtime, newest first) are unlinked from disk but retained in git history.
- Returns the project-relative path of the file written.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:collect_symbol_deltas fingerprint=313196f2dad6a3ecbf02fd525acc27ecad2ddc70e394332b331b7d2bb2a70b8c body_fp=82f41c659a8cbd64a99fd5537ba4504919a33cfd8f54ab163ca71b21943b96cf source_ref=524bcb92d10e2b1f1c66e559b1e78d5aaec69675 role=domain -->
## `def collect_symbol_deltas(project_root, config, base: str = "HEAD") -> list`

Diff the triefact tree against `base`, parse each changed file into `{qname: one_liner}` maps, and return a sorted list of per-symbol delta dicts.

- `status`: one of `"added"`, `"removed"`, or `"changed"`; `"changed"` rows are suppressed when the one-liner is identical (churn gate)
- Returns dicts with keys `file`, `qname`, `status`, and `before`/`after` as applicable; sorted by `(file, qname)`
- Silently skips any file that raises an exception during processing
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:merge_applied_by_symbol fingerprint=74952e7ab3f4a68835b255f9cfddd3440c0e18793ecea3ba49ef5464a76e2cb3 body_fp=8dbe2ff53d7e7942d1910617676949f9c5bff55c46340a1d106b95b494c7564e source_ref=ac6022b60d3c7ae0d5a92f1a4a4baad1193147c7 role=domain -->
## `def merge_applied_by_symbol(applied: list[dict]) -> list[dict]`

Collapse a list of applied patch-log entries into one merged record per `qname`, counting repeated notes as follow-ups.

- `followups`: count of notes beyond the first; each subsequent entry contributes `max(len(notes), 1)`.
- Returns insertion-ordered list of `{qname, op, note, followups}` dicts.
<!-- trie:end -->