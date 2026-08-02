---
trie_version: 0.3.0
source: trie/sync/writer.py
file_fingerprint: 0f7d6e2db4d8a78b597b6228ba55bb49a8ae1ccb74dd6c5ad85e4b900ca6b716
last_synced_at: '2026-08-02T21:19:17Z'
defines:
- kind: module
  qualified_name: trie/sync/writer:__module__
  lines: 1-617
- kind: constant
  qualified_name: trie/sync/writer:SECTION_OPEN_RE
  lines: 43-52
- kind: constant
  qualified_name: trie/sync/writer:SECTION_CLOSE_RE
  lines: 53-53
- kind: constant
  qualified_name: trie/sync/writer:SECTION_CLOSE
  lines: 54-54
- kind: constant
  qualified_name: trie/sync/writer:FRONT_MATTER_RE
  lines: 55-55
- kind: function
  qualified_name: trie/sync/writer:hash_body
  lines: 58-65
  signature: 'def hash_body(body: str) -> str'
- kind: constant
  qualified_name: trie/sync/writer:_HEADING_RE
  lines: 68-68
- kind: constant
  qualified_name: trie/sync/writer:_SENTENCE_END_RE
  lines: 69-69
- kind: function
  qualified_name: trie/sync/writer:squeeze_signature
  lines: 72-80
  signature: 'def squeeze_signature(signature: str) -> str'
- kind: function
  qualified_name: trie/sync/writer:signature_heading
  lines: 83-91
  signature: 'def signature_heading(signature: str) -> str'
- kind: function
  qualified_name: trie/sync/writer:ensure_signature_heading
  lines: 94-116
  signature: 'def ensure_signature_heading(body: str, signature: str) -> str'
- kind: function
  qualified_name: trie/sync/writer:extract_one_liner
  lines: 119-150
  signature: 'def extract_one_liner(body: str, *, max_chars: int = 200) -> str'
- kind: constant
  qualified_name: trie/sync/writer:AGENT_FRONT_MATTER_KEYS
  lines: 158-163
- kind: class
  qualified_name: trie/sync/writer:Section
  lines: 167-176
  signature: class Section
- kind: class
  qualified_name: trie/sync/writer:Prose
  lines: 180-181
  signature: class Prose
- kind: constant
  qualified_name: trie/sync/writer:Chunk
  lines: 184-184
- kind: function
  qualified_name: trie/sync/writer:_dedupe_sections
  lines: 187-215
  signature: 'def _dedupe_sections(chunks: list[Chunk]) -> list[Chunk]'
- kind: class
  qualified_name: trie/sync/writer:TriefactFile
  lines: 219-443
  signature: class TriefactFile
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.parse
  lines: 224-285
  signature: 'def parse(cls, text: str, *, parse_front_matter: bool = True) -> TriefactFile'
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.empty
  lines: 288-289
  signature: def empty(cls) -> TriefactFile
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.get_section
  lines: 293-297
  signature: 'def get_section(self, qualified_name: str) -> Section | None'
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.section_qnames
  lines: 299-300
  signature: def section_qnames(self) -> list[str]
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.upsert_section
  lines: 304-336
  signature: 'def upsert_section( self, *, qualified_name: str, fingerprint: str, body: str, source_ref: str | None = None, role: str = "", ) -> None'
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.set_section_role
  lines: 338-352
  signature: 'def set_section_role(self, qualified_name: str, role: str) -> bool'
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.sort_sections
  lines: 354-376
  signature: 'def sort_sections(self, start_line_by_qname: dict[str, int]) -> None'
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.remove_section
  lines: 378-383
  signature: 'def remove_section(self, qualified_name: str) -> bool'
- kind: method
  qualified_name: trie/sync/writer:TriefactFile._append_section
  lines: 385-396
  signature: 'def _append_section(self, section: Section) -> None: # Ensure a blank-line separator before the new section.'
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.render
  lines: 400-443
  signature: def render(self) -> str
- kind: function
  qualified_name: trie/sync/writer:render_for_agent
  lines: 446-511
  signature: 'def render_for_agent(text: str) -> str'
- kind: function
  qualified_name: trie/sync/writer:_section_signature
  lines: 514-532
  signature: 'def _section_signature(body: str) -> str'
- kind: function
  qualified_name: trie/sync/writer:_is_public_qname
  lines: 535-540
  signature: 'def _is_public_qname(qname: str) -> bool'
- kind: function
  qualified_name: trie/sync/writer:compact_triefact_view
  lines: 543-616
  signature: 'def compact_triefact_view( text: str, file_path: str, *, lines_by_qname: dict[str, str] | None = None, kind_by_qname: dict[str, str] | None = None, ) -> str'
incoming_refs: 260
outgoing_refs: 0
---
<!-- trie:section symbol=trie/sync/writer:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=571ed790c5501af20434b677bbce77f9f2dcb639b349a9deef17d9bc5ceef1be source_ref=f889eae6ac8fb78e9f35b521cfd5dd3cb5a4de2e role=parsing -->
Parses and renders triefact files with embedded trie sections delimited by HTML comment sentinels.

- **Section format**: `<!-- trie:section symbol=name fingerprint=hash ... -->` with optional `body_fp`, `source_ref`, `role`, and `hist_mass`
- **Fingerprints**: SHA-256 hashes ensure source/triefact coherence and detect manual tampering
- **Parsing**: Extracts YAML frontmatter and alternating prose/section chunks while preserving human content
- **Rendering**: Reconstructs complete triefact files with proper sentinel formatting and blank line separation
- **Agent rendering**: Strips internal bookkeeping (fingerprints, sentinels) for clean agent-facing Markdown
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:SECTION_OPEN_RE fingerprint=c9cf0ba51412fbddf63c93cf4fe3e38c2ca2ad538f4d4fa627674a4aa0ad7a88 body_fp=59a47e9bcd586814d2cd750c6078081d9c24f5fa682c7a375d18d943d91dd892 source_ref=cc69b7ec423280f825f4e5afc67e408d002041ae role=parsing -->
Compiled regex pattern for matching trie section opening HTML comments with embedded metadata.

- Captures `symbol`, `fp` (fingerprint), and optional `body_fp`, `source_ref`, `role` fields
- Tolerates `hist_mass` token for backward compatibility but does not capture it
- Anchored to line boundaries with multiline mode for standalone sentinel detection
- Trailing whitespace allowed but trailing text forbidden on sentinel lines
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:SECTION_CLOSE_RE fingerprint=49aa71874073d7e43da82cffb2e8446d3946ff6b664d86a74e4b8105f2ce602a body_fp=f7dc8b2dde7bd1b5c0eb62222998112d7b305d3cf65daa43bc1a4a882d08b964 source_ref=f889eae6ac8fb78e9f35b521cfd5dd3cb5a4de2e role=config -->
Regex pattern that matches HTML comment closing sentinels for trie documentation sections.

- Requires the comment to start at line beginning and end at line end
- Allows optional trailing horizontal whitespace after the comment
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:SECTION_CLOSE fingerprint=742e69c224d8d71b2d79094222e59b783d57ae9cf4e3a050b3874e1d05981d20 body_fp=520583f2b620aea2bbfaae9cdcb5f922e822c25036119e353ca6e7b3185c5f27 source_ref=f889eae6ac8fb78e9f35b521cfd5dd3cb5a4de2e role=model -->
Canonical HTML comment string used to close trie documentation sections in Markdown files.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:FRONT_MATTER_RE fingerprint=f100241e2f09e0c34d4dd9fbfafad078e9b2edeb64ad505b28512c83a51cdb48 body_fp=9254c9d02fb4b25f0638e2411d74cafb747378f61b30a224b651652875eecbbb source_ref=f889eae6ac8fb78e9f35b521cfd5dd3cb5a4de2e role=config -->
Matches YAML frontmatter at the start of a file, capturing the YAML content between `---` delimiters.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:hash_body fingerprint=ab22edfb13d8ba9c75b86d2384923163f1c839f46c4a2ed06ca566491fc6f96d body_fp=fe1f10f792c8ef836d059883fec08f8fc555c0b1f2e51b85546914ec772326ca source_ref=f889eae6ac8fb78e9f35b521cfd5dd3cb5a4de2e role=util -->
## `def hash_body(body: str) -> str`

Computes SHA-256 hash of section body with leading/trailing whitespace stripped.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:_HEADING_RE fingerprint=b171a12459c1801f28b3970483335daeacef5462126ceb123ef5793ee735f80b body_fp=99086de5a8a2b5859b8df2d8e8d7c98da3d839a0666ffea2c1e8fe95524ea5d3 source_ref=f889eae6ac8fb78e9f35b521cfd5dd3cb5a4de2e role=util -->
Regex pattern matching Markdown headings with optional leading whitespace (0-3 spaces) followed by 1-6 hash characters and whitespace.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:_SENTENCE_END_RE fingerprint=46839332c70a94fc506bb56b7637497fd1a8b3a93af0eb5c4ff8390ddeb08946 body_fp=9af3df6824cb757c005266be172ce35df7bbb6674cedd309eb1036f48d8565f1 source_ref=f889eae6ac8fb78e9f35b521cfd5dd3cb5a4de2e role=util -->
Regex pattern that matches sentence boundaries: punctuation (`.!?`) followed by whitespace or end of string.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:squeeze_signature fingerprint=f0a83d3cb0e0a99442aa13525b6c3ec1995cf92264206f9bb74dcebb19540329 body_fp=23f40def506d990be83c050588f483927178153443fa93c080300361517fa272 source_ref=a6a9c941b3ce70ec52b2bbe69087c877f3edaa0c role=util -->
## `def squeeze_signature(signature: str) -> str`

Collapse all whitespace runs in a raw, possibly multi-line signature string to a single space, producing a one-line result safe for YAML scalars and Markdown headings.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:signature_heading fingerprint=bea79462563e8af2f5ab74d895534d9efc7dffd3e5183d5e8e786b3c68226760 body_fp=b981769248af0af306b0486dc2015573e7c2295cf62a48f3b20cef0029c61f3e source_ref=a6a9c941b3ce70ec52b2bbe69087c877f3edaa0c role=util -->
## `def signature_heading(signature: str) -> str`

Produce the canonical `## \`...\`` heading string for a triefact section body from a raw symbol signature.

- `signature` — may be multi-line; squeezed to one line via `squeeze_signature` before wrapping.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:ensure_signature_heading fingerprint=75160f8faaac773b4522287d0f61dfe389dc1dff9f2001b7652e40a226a63fb8 body_fp=a550e093384980e208d1b4e75cb81d7156fcfb5c312878ac564e6f7b1256d6d0 source_ref=a6a9c941b3ce70ec52b2bbe69087c877f3edaa0c role=util -->
## `def ensure_signature_heading(body: str, signature: str) -> str`

Normalize `body` so it begins with the canonical `signature_heading` derived from `signature`, replacing any existing `## …` heading or prepending one if absent.

- `body`: section prose, possibly leading with an LLM-authored or missing heading.
- `signature`: raw parser-captured signature string; passed through `signature_heading` to produce the authoritative heading.
- Returns `body` with exactly one correct level-2 heading at the start, separated from remaining prose by a blank line; idempotent.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:extract_one_liner fingerprint=fb87254713b9705aec49bf5aaed06df13d5765c8d66d19dd661b746b0045cd82 body_fp=694368b67743bf4635e90c7353ba49cbef9098ac577df322b826b0df5b6fd545 source_ref=f889eae6ac8fb78e9f35b521cfd5dd3cb5a4de2e role=util -->
## `def extract_one_liner(body: str, *, max_chars: int = 200) -> str`

Extracts the first sentence from a triefact section body, skipping headings and truncating to a character limit.

- Returns empty string if no usable text is found
- Collapses whitespace and adds ellipsis when truncated
- Stops at first paragraph break or sentence-ending punctuation
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:AGENT_FRONT_MATTER_KEYS fingerprint=4ffdf447d675342eb7e62f591eb81f0dbe4b8236a7ecbc21145d49565aaf7fa7 body_fp=8294eda21e5594b41824b5d4aa60944267192f07531bea2c9d8f94d349761f2e source_ref=f889eae6ac8fb78e9f35b521cfd5dd3cb5a4de2e role=config -->
Defines the frontmatter keys that are preserved when rendering triefacts for agents, filtering out trie's internal bookkeeping fields.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:Section fingerprint=734c957605002e25718f8ced8d064dac205226486fbad13ec4c1646c788be4d8 body_fp=13d49c20df96010717aa2161933516d3f4d5e5abde45c8c22f3b7dec33579564 source_ref=cc69b7ec423280f825f4e5afc67e408d002041ae role=model -->
## `class Section`

Frozen dataclass representing a parsed triefact section with its fingerprinting and role metadata.

- `body_fingerprint`: SHA-256 over section body; None for legacy sections without body fingerprints
- `source_ref`: git blob hash of the source file when this section was generated
- `role`: architectural role tag inferred by LLM, persisted to survive graph DB rebuilds
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:Prose fingerprint=cf49910dc87437bc09897192fbd13b0a347f9433a85c94f1e599b18c7eceaf2b body_fp=02829226dc7c09194b519eac7fcdfb5d5c0a36d875334f6c1827412ed3f86ad7 source_ref=f889eae6ac8fb78e9f35b521cfd5dd3cb5a4de2e role=model -->
## `class Prose`

Represents verbatim text content between trie sections in a triefact file.

- `text`: Raw string content preserved exactly as written in the source file
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:Chunk fingerprint=27a576a701491dcbdfeae28c3b7f87ee71a034e04c90aa8a336c241cf4a788c1 body_fp=053f0d0a4910d0fbf1cc2bf6dca20f21cc062ed857b3a63b85cbf21506ec62b0 source_ref=f889eae6ac8fb78e9f35b521cfd5dd3cb5a4de2e role=model -->
Type alias for a triefact file component that is either a documentation section or human-written prose.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:_dedupe_sections fingerprint=e73e778d47cb90bc42312db46f5c9edcdcff2d282e48ca058689657619c8938d body_fp=55ed349ac64872e643680b9ee92eb20991a9fc2ea640f3006f7b9576719f9c43 source_ref=f889eae6ac8fb78e9f35b521cfd5dd3cb5a4de2e role=util -->
## `def _dedupe_sections(chunks: list[Chunk]) -> list[Chunk]`

Removes duplicate sections with the same qualified_name, keeping the last occurrence at the first occurrence's position.

- Preserves source-order layout while using the most recently written section body
- Passes through non-section prose chunks unchanged
- Enables self-healing of accumulated duplicates on next read/render cycle
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile fingerprint=804d05b8f3605f4870b9a5f7c4f696a2446cd23931c9897839984ebefa5ae991 body_fp=d2c5542dbb38f1823e539e0aef4f938f5d9f9840e056732098ec823d1f2607fa source_ref=a6a9c941b3ce70ec52b2bbe69087c877f3edaa0c role=persistence -->
## `class TriefactFile`

Parses, manipulates, and renders triefact files containing YAML frontmatter and trie-managed documentation sections.

- `front_matter`: YAML metadata dictionary at file start
- `chunks`: sequence of Section and Prose objects representing file structure
- `parse()`: extracts frontmatter and HTML-delimited sections from raw text; accepts `parse_front_matter=False` to skip YAML loading entirely for fingerprint-only consumers
- `upsert_section()`: replaces existing section or appends new one; no longer preserves historical mass from the existing section
- `set_section_role()`: updates only the role field of existing section
- `sort_sections()`: reorders sections by source line number while preserving prose
- `render()`: serializes back to text with HTML sentinels and YAML frontmatter; no longer emits `hist_mass=` field
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile.parse fingerprint=5547ae2066907fa2bff6eb30e98cbb4c4b9e9a979a7cae47197b030bee59efa1 body_fp=b62c73de0e32784c5a5193460971fc88f3b77528e0681fa6022ac302e49543af source_ref=5b7825700eebcfd1cf76905d45abb17aa8ccbe06 role=parsing -->
## `def parse(cls, text: str, *, parse_front_matter: bool = True) -> TriefactFile`

Creates `TriefactFile` from Markdown text by parsing YAML frontmatter and trie section sentinels.

- Extracts YAML frontmatter from opening `---` blocks, ignoring malformed YAML
- `parse_front_matter=False` skips the YAML load entirely, leaving `front_matter` empty
- Prefers LibYAML's `CSafeLoader` over the pure-Python loader when available
- Parses trie sections between `<!-- trie:section -->` and `<!-- trie:end -->` sentinels
- Preserves prose chunks between sections as-is
- Strips leading/trailing newlines from section bodies
- Deduplicates sections with same qualified_name, keeping the last occurrence
- Raises `ValueError` for unterminated sections (missing close sentinel)
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile.empty fingerprint=cc0676809bee8efb34856efbd9c950ae148db930ab90e76ebd3d17bd1eefbc7e body_fp=b39cc17272ea112c0ce16abc03e234d0c0fa2fbcb709a75519a29e7ffd5ca9d9 source_ref=f889eae6ac8fb78e9f35b521cfd5dd3cb5a4de2e role=util -->
## `def empty(cls) -> TriefactFile`

Creates an empty `TriefactFile` instance with no front matter or chunks.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile.get_section fingerprint=aec43c04e2eaaaaf39f4d6be228e0198afa191d15abda68a3879b41b391204d8 body_fp=2ca589cb17d418e0a9ae8085efcfd29918040bffbc324936b7622ed82ac718e9 source_ref=f889eae6ac8fb78e9f35b521cfd5dd3cb5a4de2e role=domain -->
## `def get_section(self, qualified_name: str) -> Section | None`

Returns the first `Section` in `TriefactFile.chunks` matching the given `qualified_name`, or `None` if not found.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile.section_qnames fingerprint=b3198e06079669f9cdabe77cd2292e047d5fc68e79e8ecb7e0a9f7bff28f0f60 body_fp=66a70ecfbc0a1f92aef802d582c59c3d89ecd41352f56c346e5e3dd3f8e0acd4 source_ref=f889eae6ac8fb78e9f35b521cfd5dd3cb5a4de2e role=domain -->
## `def section_qnames(self) -> list[str]`

Returns a list of qualified names for all Section chunks in the TriefactFile.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile.upsert_section fingerprint=f5c3375f4ca32ffb59e2513e49b00f2122e6cc7c95d3e57f4f28ecad0710d40d body_fp=3ae5365834051a6dc73e453fe6e55b8479b934c2b8294d2a0b679658738baa4b source_ref=cc69b7ec423280f825f4e5afc67e408d002041ae role=persistence -->
## `def upsert_section( self, *, qualified_name: str, fingerprint: str, body: str, source_ref: str | None = None, role: str = "", ) -> None`

TriefactFile method that replaces an existing section by qualified_name or appends new one at end.

- `body`: section content; body fingerprint computed automatically
- `source_ref`: git blob hash stamped in sentinel when non-None
- `role`: architectural role tag; empty string omits from sentinel
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile.set_section_role fingerprint=b32057736b75dff6ad04d492a7449b92d83d6a102a4787fecfd922b9fd27403a body_fp=6f46b2c53548c66871b6d6abf93de1b3618d657d34c5273e1846b2d35626cbae source_ref=f889eae6ac8fb78e9f35b521cfd5dd3cb5a4de2e role=persistence -->
## `def set_section_role(self, qualified_name: str, role: str) -> bool`

Update only the `role` tag of an existing `TriefactFile` section, leaving all other fields unchanged.

- Returns `False` if no section with `qualified_name` exists.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile.sort_sections fingerprint=3a5abfe00c1190b093875944af69f77a27689bb7a756b7a12c709e067e398038 body_fp=764701d5c34a5c7c18ab3483dbe8cf5bdbea15b4a2a0a68dc0190021307d7b55 source_ref=f889eae6ac8fb78e9f35b521cfd5dd3cb5a4de2e role=domain -->
## `def sort_sections(self, start_line_by_qname: dict[str, int]) -> None`

Reorders TriefactFile sections to match their source file line order based on provided line number mapping.

- `start_line_by_qname`: Maps qualified symbol names to their source line numbers
- Sections without mapping entries are placed at the end in original order
- Preserves non-whitespace prose chunks at the beginning
- Drops whitespace-only prose chunks (recreated during rendering)
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile.remove_section fingerprint=d8dc7a57db15d5144ac0f1cb113b03fbe74d7608b5e9b23572384079c5ce8032 body_fp=01e74681a4a6620c3bb59c59e1f6687db51b80a1556098ca3c930d3c84efd5a2 source_ref=f889eae6ac8fb78e9f35b521cfd5dd3cb5a4de2e role=domain -->
## `def remove_section(self, qualified_name: str) -> bool`

Remove a section from TriefactFile chunks by qualified name, returning whether one was found.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile._append_section fingerprint=39d0ed815c7e15cf563957738a217245397a9ae9c72076762ea523a6b7cb189c body_fp=035dc2a130a019a695fdba95edff0dc8f5c300b4654736a58bfbef7a0e79b150 source_ref=f889eae6ac8fb78e9f35b521cfd5dd3cb5a4de2e role=domain -->
## `def _append_section(self, section: Section) -> None: # Ensure a blank-line separator before the new section.`

Appends a section to TriefactFile.chunks, ensuring proper blank-line separation from preceding content.

- Adds newlines to the last Prose chunk if it doesn't end with double newline
- Inserts a new Prose chunk with double newline after the last Section
- No prefix needed when appending to empty chunks or after front matter
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile.render fingerprint=824091f46be5e14a70e75ce9bbe121aebd9b9b8b4eea0b466136612453895263 body_fp=c8f466f490f4120be980eeea0209fcc84ca07447c21c8bbf59a551e048a654bb source_ref=a6a9c941b3ce70ec52b2bbe69087c877f3edaa0c role=persistence -->
## `def render(self) -> str`

Converts `TriefactFile` to complete triefact text with YAML frontmatter and sentinel-wrapped sections.

- Emits `body_fp` field automatically, computing from body if missing for legacy sections
- Separates consecutive sections with blank lines to meet parser requirements
- Includes optional fields (`source_ref`, `role`) only when non-empty
- Maintains field order: `symbol`, `fingerprint`, `body_fp`, `source_ref`, `role`
- YAML dump uses `width=2**20` to suppress PyYAML's 80-column scalar folding, keeping long values on one line
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:render_for_agent fingerprint=b97c1f5ff392bd22e1173f27efd92b1064a8b8f44753046da510e04539c1430e body_fp=ca9d6f88927efe85bb4d8959aa2f171f28695ef28864a0a9e132611af21aff83 source_ref=a6a9c941b3ce70ec52b2bbe69087c877f3edaa0c role=util -->
## `def render_for_agent(text: str) -> str`

Strips trie machinery noise from triefact text to produce clean agent-readable Markdown.

- Removes frontmatter bookkeeping fields, keeping only `description`, `defines`, `incoming_refs`, `outgoing_refs`
- Strips HTML comment sentinels around sections, preserving only body content
- Maintains blank line separation between consecutive sections
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:_section_signature fingerprint=c13797b953a41fafe0f97c80bae8182a579a9773d7321323b9fcf7025f407491 body_fp=f70e92f1eb38a3d1384d7f981eff74b099fcb0bb594f5f8229a92ceb5846c09b source_ref=a6a9c941b3ce70ec52b2bbe69087c877f3edaa0c role=util -->
## `def _section_signature(body: str) -> str`

Extract the signature string from a section body's leading `## ` heading, stripping the heading marker and any surrounding backticks; returns `""` for blank, non-heading, or empty bodies.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:_is_public_qname fingerprint=8ff55308ca377eb4bb43d890bd42be3fc6a7ce304fd98eeeebe7759f03b6e1cd body_fp=f6b5fd4702adda30f551c0f05e176b59d343b1938e67b0745af7b93d3cfdb3e4 source_ref=f889eae6ac8fb78e9f35b521cfd5dd3cb5a4de2e role=util -->
## `def _is_public_qname(qname: str) -> bool`

Return `True` if the local part of `qname` is public; dunder names (`__x__`) are treated as public, single-underscore-prefixed names are not.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:compact_triefact_view fingerprint=1fa5a405eb80664308d3f5a9b8ae0bf89143aaa878983d9f661baf66a82ae9bd body_fp=7984ee0a56cc0bb78e181a88b53801a5c330cfaa9cc634d6bd2998598a9886e7 source_ref=a6a9c941b3ce70ec52b2bbe69087c877f3edaa0c role=domain -->
## `def compact_triefact_view( text: str, file_path: str, *, lines_by_qname: dict[str, str] | None = None, kind_by_qname: dict[str, str] | None = None, ) -> str`

Render a triefact file as a compact, token-cheap overview listing each symbol's kind, line range, signature, and first-sentence intro.

- `text`: raw triefact Markdown to parse
- `lines_by_qname`: overrides per-symbol line ranges from the frontmatter `defines` manifest
- `kind_by_qname`: overrides per-symbol kind values from the frontmatter `defines` manifest
- `signature`: preferred from the frontmatter `defines` entry; falls back to the section-body `## ` heading for legacy triefacts lacking the key
<!-- trie:end -->