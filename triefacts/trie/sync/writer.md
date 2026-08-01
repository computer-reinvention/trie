---
trie_version: 0.2.1
source: trie/sync/writer.py
file_fingerprint: 6e10670f3565ce1143f95880da1b091b77c8e829d567e27c18303b4666b5abc7
last_synced_at: '2026-08-01T01:52:14Z'
defines:
- kind: module
  qualified_name: trie/sync/writer:__module__
  lines: 1-552
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
- kind: constant
  qualified_name: trie/sync/writer:_HEADING_RE
  lines: 68-68
- kind: constant
  qualified_name: trie/sync/writer:_SENTENCE_END_RE
  lines: 69-69
- kind: function
  qualified_name: trie/sync/writer:extract_one_liner
  lines: 72-103
- kind: constant
  qualified_name: trie/sync/writer:AGENT_FRONT_MATTER_KEYS
  lines: 111-116
- kind: class
  qualified_name: trie/sync/writer:Section
  lines: 120-129
- kind: class
  qualified_name: trie/sync/writer:Prose
  lines: 133-134
- kind: constant
  qualified_name: trie/sync/writer:Chunk
  lines: 137-137
- kind: function
  qualified_name: trie/sync/writer:_dedupe_sections
  lines: 140-168
- kind: class
  qualified_name: trie/sync/writer:TriefactFile
  lines: 172-390
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.parse
  lines: 177-238
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.empty
  lines: 241-242
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.get_section
  lines: 246-250
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.section_qnames
  lines: 252-253
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.upsert_section
  lines: 257-289
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.set_section_role
  lines: 291-305
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.sort_sections
  lines: 307-329
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.remove_section
  lines: 331-336
- kind: method
  qualified_name: trie/sync/writer:TriefactFile._append_section
  lines: 338-349
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.render
  lines: 353-390
- kind: function
  qualified_name: trie/sync/writer:render_for_agent
  lines: 393-455
- kind: function
  qualified_name: trie/sync/writer:_section_signature
  lines: 458-472
- kind: function
  qualified_name: trie/sync/writer:_is_public_qname
  lines: 475-480
- kind: function
  qualified_name: trie/sync/writer:compact_triefact_view
  lines: 483-551
incoming_refs: 225
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
<!-- trie:section symbol=trie/sync/writer:hash_body fingerprint=ab22edfb13d8ba9c75b86d2384923163f1c839f46c4a2ed06ca566491fc6f96d body_fp=f25338f018538e622517fca4e08a07b5ffe6b8ebe068f7ae63b1691e726cd353 source_ref=f889eae6ac8fb78e9f35b521cfd5dd3cb5a4de2e role=util -->
## `hash_body(body: str) -> str`

Computes SHA-256 hash of section body with leading/trailing whitespace stripped.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:_HEADING_RE fingerprint=b171a12459c1801f28b3970483335daeacef5462126ceb123ef5793ee735f80b body_fp=99086de5a8a2b5859b8df2d8e8d7c98da3d839a0666ffea2c1e8fe95524ea5d3 source_ref=f889eae6ac8fb78e9f35b521cfd5dd3cb5a4de2e role=util -->
Regex pattern matching Markdown headings with optional leading whitespace (0-3 spaces) followed by 1-6 hash characters and whitespace.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:_SENTENCE_END_RE fingerprint=46839332c70a94fc506bb56b7637497fd1a8b3a93af0eb5c4ff8390ddeb08946 body_fp=9af3df6824cb757c005266be172ce35df7bbb6674cedd309eb1036f48d8565f1 source_ref=f889eae6ac8fb78e9f35b521cfd5dd3cb5a4de2e role=util -->
Regex pattern that matches sentence boundaries: punctuation (`.!?`) followed by whitespace or end of string.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:extract_one_liner fingerprint=fb87254713b9705aec49bf5aaed06df13d5765c8d66d19dd661b746b0045cd82 body_fp=02fa734880039fc4ef9072150fd1772cf409ddd6755a5fe60ce70a149dc18bbb source_ref=f889eae6ac8fb78e9f35b521cfd5dd3cb5a4de2e role=util -->
Extracts the first sentence from a triefact section body, skipping headings and truncating to a character limit.

- Returns empty string if no usable text is found
- Collapses whitespace and adds ellipsis when truncated
- Stops at first paragraph break or sentence-ending punctuation
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:AGENT_FRONT_MATTER_KEYS fingerprint=4ffdf447d675342eb7e62f591eb81f0dbe4b8236a7ecbc21145d49565aaf7fa7 body_fp=8294eda21e5594b41824b5d4aa60944267192f07531bea2c9d8f94d349761f2e source_ref=f889eae6ac8fb78e9f35b521cfd5dd3cb5a4de2e role=config -->
Defines the frontmatter keys that are preserved when rendering triefacts for agents, filtering out trie's internal bookkeeping fields.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:Section fingerprint=734c957605002e25718f8ced8d064dac205226486fbad13ec4c1646c788be4d8 body_fp=3eb9e6cf4fd70190a23a9f722f673c8dba968031714e50e3ff4ee5aa8c2b05f7 source_ref=cc69b7ec423280f825f4e5afc67e408d002041ae role=model -->
Frozen dataclass representing a parsed triefact section with its fingerprinting and role metadata.

- `body_fingerprint`: SHA-256 over section body; None for legacy sections without body fingerprints
- `source_ref`: git blob hash of the source file when this section was generated
- `role`: architectural role tag inferred by LLM, persisted to survive graph DB rebuilds
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:Prose fingerprint=cf49910dc87437bc09897192fbd13b0a347f9433a85c94f1e599b18c7eceaf2b body_fp=fd56063975571280ad2d77243aa239a8192343d0f034c017b0805986b90a94ed source_ref=f889eae6ac8fb78e9f35b521cfd5dd3cb5a4de2e role=model -->
Represents verbatim text content between trie sections in a triefact file.

- `text`: Raw string content preserved exactly as written in the source file
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:Chunk fingerprint=27a576a701491dcbdfeae28c3b7f87ee71a034e04c90aa8a336c241cf4a788c1 body_fp=053f0d0a4910d0fbf1cc2bf6dca20f21cc062ed857b3a63b85cbf21506ec62b0 source_ref=f889eae6ac8fb78e9f35b521cfd5dd3cb5a4de2e role=model -->
Type alias for a triefact file component that is either a documentation section or human-written prose.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:_dedupe_sections fingerprint=e73e778d47cb90bc42312db46f5c9edcdcff2d282e48ca058689657619c8938d body_fp=eed963feb425248d1ae93862069990eef93f2dd2fa10e5e00e550c0317f88423 source_ref=f889eae6ac8fb78e9f35b521cfd5dd3cb5a4de2e role=util -->
## `_dedupe_sections(chunks: list[Chunk]) -> list[Chunk]`

Removes duplicate sections with the same qualified_name, keeping the last occurrence at the first occurrence's position.

- Preserves source-order layout while using the most recently written section body
- Passes through non-section prose chunks unchanged
- Enables self-healing of accumulated duplicates on next read/render cycle
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile fingerprint=6e2d23c3db6e183942fa57199c36e8b04e3e790707622505fc471b7ee4872dee body_fp=1f9bbf16557b370d6309f656d973e74d1d9ba1647c3154d51acb9e04c8fce7bf source_ref=5b7825700eebcfd1cf76905d45abb17aa8ccbe06 role=persistence -->
Parses, manipulates, and renders triefact files containing YAML frontmatter and trie-managed documentation sections.

- `front_matter`: YAML metadata dictionary at file start
- `chunks`: sequence of Section and Prose objects representing file structure
- `parse()`: extracts frontmatter and HTML-delimited sections from raw text; accepts `parse_front_matter=False` to skip YAML loading entirely for fingerprint-only consumers
- `upsert_section()`: replaces existing section or appends new one; no longer preserves historical mass from the existing section
- `set_section_role()`: updates only the role field of existing section
- `sort_sections()`: reorders sections by source line number while preserving prose
- `render()`: serializes back to text with HTML sentinels and YAML frontmatter; no longer emits `hist_mass=` field
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile.parse fingerprint=5547ae2066907fa2bff6eb30e98cbb4c4b9e9a979a7cae47197b030bee59efa1 body_fp=b6ddec0f3ab3a759eae6200d766ac5103eb301eba22385a5ff2deca0efbb5e82 source_ref=5b7825700eebcfd1cf76905d45abb17aa8ccbe06 role=parsing -->
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
<!-- trie:section symbol=trie/sync/writer:TriefactFile.empty fingerprint=cc0676809bee8efb34856efbd9c950ae148db930ab90e76ebd3d17bd1eefbc7e body_fp=f5a430dd711b25c171ed7dcbe83ddd8f6c49f33fbb7f08dcce14d7a3962cbf67 source_ref=f889eae6ac8fb78e9f35b521cfd5dd3cb5a4de2e role=util -->
Creates an empty `TriefactFile` instance with no front matter or chunks.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile.get_section fingerprint=aec43c04e2eaaaaf39f4d6be228e0198afa191d15abda68a3879b41b391204d8 body_fp=0d78a98a5ab1a3555da8743e5f000f27b169d4c225afdd399693ac5039a2b7ad source_ref=f889eae6ac8fb78e9f35b521cfd5dd3cb5a4de2e role=domain -->
Returns the first `Section` in `TriefactFile.chunks` matching the given `qualified_name`, or `None` if not found.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile.section_qnames fingerprint=b3198e06079669f9cdabe77cd2292e047d5fc68e79e8ecb7e0a9f7bff28f0f60 body_fp=86e2903008214db684f493e3eef6b2c24911be73d69480eaf399c7ba5388e046 source_ref=f889eae6ac8fb78e9f35b521cfd5dd3cb5a4de2e role=domain -->
Returns a list of qualified names for all Section chunks in the TriefactFile.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile.upsert_section fingerprint=f5c3375f4ca32ffb59e2513e49b00f2122e6cc7c95d3e57f4f28ecad0710d40d body_fp=33109e6e0b994394ed12ffb4fe824d3b4e405b7b0a00345daee0a2831daf6088 source_ref=cc69b7ec423280f825f4e5afc67e408d002041ae role=persistence -->
## `TriefactFile.upsert_section(*, qualified_name: str, fingerprint: str, body: str, source_ref: str | None = None, role: str = "") -> None`

TriefactFile method that replaces an existing section by qualified_name or appends new one at end.

- `body`: section content; body fingerprint computed automatically
- `source_ref`: git blob hash stamped in sentinel when non-None
- `role`: architectural role tag; empty string omits from sentinel
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile.set_section_role fingerprint=b32057736b75dff6ad04d492a7449b92d83d6a102a4787fecfd922b9fd27403a body_fp=bb48f4f0a5372c688e5c464944f38986aae9ea1e8c55ba7d5f2d188ef0ee09f1 source_ref=f889eae6ac8fb78e9f35b521cfd5dd3cb5a4de2e role=persistence -->
Update only the `role` tag of an existing `TriefactFile` section, leaving all other fields unchanged.

- Returns `False` if no section with `qualified_name` exists.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile.sort_sections fingerprint=3a5abfe00c1190b093875944af69f77a27689bb7a756b7a12c709e067e398038 body_fp=cfef4021f5a47b20f87f08420e8dd76e258fd075ea8f75961c34804d8d01ab14 source_ref=f889eae6ac8fb78e9f35b521cfd5dd3cb5a4de2e role=domain -->
## `TriefactFile.sort_sections(self, start_line_by_qname: dict[str, int]) -> None`

Reorders TriefactFile sections to match their source file line order based on provided line number mapping.

- `start_line_by_qname`: Maps qualified symbol names to their source line numbers
- Sections without mapping entries are placed at the end in original order
- Preserves non-whitespace prose chunks at the beginning
- Drops whitespace-only prose chunks (recreated during rendering)
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile.remove_section fingerprint=d8dc7a57db15d5144ac0f1cb113b03fbe74d7608b5e9b23572384079c5ce8032 body_fp=5996a343aba10297edc08202681264d31aa48a828166f217c0e477d2aaa9d56e source_ref=f889eae6ac8fb78e9f35b521cfd5dd3cb5a4de2e role=domain -->
Remove a section from TriefactFile chunks by qualified name, returning whether one was found.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile._append_section fingerprint=39d0ed815c7e15cf563957738a217245397a9ae9c72076762ea523a6b7cb189c body_fp=ad87f6b64e97ac718bc4115a03e680d7ec79e36773f752bac0d1c33121df28cd source_ref=f889eae6ac8fb78e9f35b521cfd5dd3cb5a4de2e role=domain -->
Appends a section to TriefactFile.chunks, ensuring proper blank-line separation from preceding content.

- Adds newlines to the last Prose chunk if it doesn't end with double newline
- Inserts a new Prose chunk with double newline after the last Section
- No prefix needed when appending to empty chunks or after front matter
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile.render fingerprint=65f4e4c0a8c735c21363d77fb9c5e6f88fd65de9d7c6e79f2e76a1e187ad7f3a body_fp=189a1d1e925401ca445319c8427381d2745c7c25ff8919f071b5ae56cf73b49e source_ref=cc69b7ec423280f825f4e5afc67e408d002041ae role=persistence -->
Converts `TriefactFile` to complete triefact text with YAML frontmatter and sentinel-wrapped sections.

- Emits `body_fp` field automatically, computing from body if missing for legacy sections
- Separates consecutive sections with blank lines to meet parser requirements
- Includes optional fields (`source_ref`, `role`) only when non-empty
- Maintains field order: `symbol`, `fingerprint`, `body_fp`, `source_ref`, `role`
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:render_for_agent fingerprint=092ba74e28cdec14b0df2de55c6ab0105f9f6c074da00f6bcccb774d76160d8c body_fp=9d61dda9056130e0aebb96b39bbd6cf24b52590324d5425be84b7f1f8216aaf3 source_ref=f889eae6ac8fb78e9f35b521cfd5dd3cb5a4de2e role=util -->
Strips trie machinery noise from triefact text to produce clean agent-readable Markdown.

- Removes frontmatter bookkeeping fields, keeping only `description`, `defines`, `incoming_refs`, `outgoing_refs`
- Strips HTML comment sentinels around sections, preserving only body content
- Maintains blank line separation between consecutive sections
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:_section_signature fingerprint=bd6271114fea47fad46d58665f45b0052ea3da58dc7e021825112fda62ac9684 body_fp=e4e87b82d197ff8bf40fe7cc64f45fd103c72134ce39635bacb40bf88b286af1 source_ref=f889eae6ac8fb78e9f35b521cfd5dd3cb5a4de2e role=util -->
Extract the signature string from a section body's leading `## ` heading, returning `""` for blank, non-heading, or empty bodies.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:_is_public_qname fingerprint=8ff55308ca377eb4bb43d890bd42be3fc6a7ce304fd98eeeebe7759f03b6e1cd body_fp=7958cd6c0b751f86627727562e6fcaceac9409014cc3c5eec87348f8ea614c73 source_ref=f889eae6ac8fb78e9f35b521cfd5dd3cb5a4de2e role=util -->
Return `True` if the local part of `qname` is public; dunder names (`__x__`) are treated as public, single-underscore-prefixed names are not.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:compact_triefact_view fingerprint=0721d84c43577a6d6edebf66527b23050645c4a1648b2611907e49c7dfc4c7d4 body_fp=6f93fdd0d7fa23ea7fa0b0a4af0b89c4316a7e4fd4c3895f7d83f6ec8d6b9251 source_ref=f889eae6ac8fb78e9f35b521cfd5dd3cb5a4de2e role=util -->
Render a triefact file as a compact, token-cheap overview listing each symbol's kind, line range, signature, and first-sentence intro.

- `text`: raw triefact Markdown to parse
- `lines_by_qname`: overrides per-symbol line ranges from the frontmatter `defines` manifest
- `kind_by_qname`: overrides per-symbol kind values from the frontmatter `defines` manifest
<!-- trie:end -->