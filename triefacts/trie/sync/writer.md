---
trie_version: 0.1.5
source: trie/sync/writer.py
file_fingerprint: effac6fb890e9d219008a7be3f8b00ce2f15472fc77330e233801892ee25def0
last_synced_at: '2026-06-10T13:16:33Z'
defines:
- kind: module
  qualified_name: trie/sync/writer:__module__
  lines: 1-506
- kind: constant
  qualified_name: trie/sync/writer:SECTION_OPEN_RE
  lines: 43-50
- kind: constant
  qualified_name: trie/sync/writer:SECTION_CLOSE_RE
  lines: 51-51
- kind: constant
  qualified_name: trie/sync/writer:SECTION_CLOSE
  lines: 52-52
- kind: constant
  qualified_name: trie/sync/writer:FRONT_MATTER_RE
  lines: 53-53
- kind: function
  qualified_name: trie/sync/writer:parse_hist_mass
  lines: 56-68
- kind: function
  qualified_name: trie/sync/writer:format_hist_mass
  lines: 71-78
- kind: function
  qualified_name: trie/sync/writer:hash_body
  lines: 81-88
- kind: constant
  qualified_name: trie/sync/writer:_HEADING_RE
  lines: 91-91
- kind: constant
  qualified_name: trie/sync/writer:_SENTENCE_END_RE
  lines: 92-92
- kind: function
  qualified_name: trie/sync/writer:extract_one_liner
  lines: 95-126
- kind: constant
  qualified_name: trie/sync/writer:AGENT_FRONT_MATTER_KEYS
  lines: 134-139
- kind: class
  qualified_name: trie/sync/writer:Section
  lines: 143-159
- kind: class
  qualified_name: trie/sync/writer:Prose
  lines: 163-164
- kind: constant
  qualified_name: trie/sync/writer:Chunk
  lines: 167-167
- kind: function
  qualified_name: trie/sync/writer:_dedupe_sections
  lines: 170-198
- kind: class
  qualified_name: trie/sync/writer:TriefactFile
  lines: 202-440
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.parse
  lines: 207-259
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.empty
  lines: 262-263
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.get_section
  lines: 267-271
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.section_qnames
  lines: 273-274
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.upsert_section
  lines: 278-316
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.set_section_role
  lines: 318-332
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.set_section_historical_mass
  lines: 334-348
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.sort_sections
  lines: 350-372
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.remove_section
  lines: 374-379
- kind: method
  qualified_name: trie/sync/writer:TriefactFile._append_section
  lines: 381-392
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.render
  lines: 396-440
- kind: function
  qualified_name: trie/sync/writer:render_for_agent
  lines: 443-505
incoming_refs: 82
outgoing_refs: 0
---
<!-- trie:section symbol=trie/sync/writer:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=c90405d227a60d4babaab62f1bb7b669d2c3b15b35b0cccb025fb762135105f4 source_ref=b8bc54fd6dfe1be68bb60012cf18b620e9aac632 role=documentation-sync -->
Parses and renders triefact files with embedded trie sections delimited by HTML comment sentinels.

- **Section format**: `<!-- trie:section symbol=name fingerprint=hash ... -->` with optional `body_fp` and `source_ref`
- **Fingerprints**: SHA-256 hashes ensure source/triefact coherence and detect manual tampering
- **Parsing**: Extracts YAML frontmatter and alternating prose/section chunks while preserving human content
- **Rendering**: Reconstructs complete triefact files with proper sentinel formatting and blank line separation
- **Agent rendering**: Strips internal bookkeeping (fingerprints, sentinels) for clean agent-facing Markdown
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:SECTION_OPEN_RE fingerprint=0c4217b350044f22fe6f773e84a0f761b89e79027711e99d750d6f0ea3ab9c2e body_fp=3ae10a1bc7c77da9fc9e3d87fcc2ec5dc7b90e056f8726d3bd032eaf790aa3a5 source_ref=831f75c6754c4c40698fbf554c1887d6450d69e0 role=parsing -->
Compiled regex pattern for matching trie section opening HTML comments with embedded metadata.

- Captures `symbol`, `fp` (fingerprint), and optional `body_fp`, `source_ref`, `role`, `hist_mass` fields
- Anchored to line boundaries with multiline mode for standalone sentinel detection
- Trailing whitespace allowed but trailing text forbidden on sentinel lines
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:SECTION_CLOSE_RE fingerprint=49aa71874073d7e43da82cffb2e8446d3946ff6b664d86a74e4b8105f2ce602a body_fp=f7dc8b2dde7bd1b5c0eb62222998112d7b305d3cf65daa43bc1a4a882d08b964 source_ref=b8bc54fd6dfe1be68bb60012cf18b620e9aac632 role=documentation-sync -->
Regex pattern that matches HTML comment closing sentinels for trie documentation sections.

- Requires the comment to start at line beginning and end at line end
- Allows optional trailing horizontal whitespace after the comment
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:SECTION_CLOSE fingerprint=742e69c224d8d71b2d79094222e59b783d57ae9cf4e3a050b3874e1d05981d20 body_fp=520583f2b620aea2bbfaae9cdcb5f922e822c25036119e353ca6e7b3185c5f27 source_ref=b8bc54fd6dfe1be68bb60012cf18b620e9aac632 role=documentation-sync -->
Canonical HTML comment string used to close trie documentation sections in Markdown files.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:FRONT_MATTER_RE fingerprint=f100241e2f09e0c34d4dd9fbfafad078e9b2edeb64ad505b28512c83a51cdb48 body_fp=9254c9d02fb4b25f0638e2411d74cafb747378f61b30a224b651652875eecbbb source_ref=b8bc54fd6dfe1be68bb60012cf18b620e9aac632 role=documentation-sync -->
Matches YAML frontmatter at the start of a file, capturing the YAML content between `---` delimiters.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:parse_hist_mass fingerprint=ef11101bcafd0025aca68daf894c85762908823e7d2d201b6bcf45d61c32214b body_fp=d2a6664dbbff363ff59249b317a509c8143d8ef79bc822ccdd07aa4d6674c2e1 source_ref=831f75c6754c4c40698fbf554c1887d6450d69e0 role=parsing -->
Parse `hist_mass` sentinel token `<value>@<ts>` into (mass, ts) tuple.

- Returns (0.0, 0.0) for None/malformed tokens (legacy sentinels, corrupt values)
- Token format: decimal mass value, "@" separator, optional timestamp
- Missing timestamp defaults to 0.0
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:format_hist_mass fingerprint=84e149eebdff44553dad018b3e5d66b207f04c220acd9da266b062bd7f90063b body_fp=d8c8e1fb363aca6602d435bce63c6b5db535c23582451a7617b4abe593ffe555 source_ref=831f75c6754c4c40698fbf554c1887d6450d69e0 role=util -->
Serializes historical mass and timestamp into a sentinel token format.

- `mass`: quantized to one decimal place to avoid diff churn
- `ts`: converted to integer seconds for 21-day decay horizon
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:hash_body fingerprint=ab22edfb13d8ba9c75b86d2384923163f1c839f46c4a2ed06ca566491fc6f96d body_fp=f25338f018538e622517fca4e08a07b5ffe6b8ebe068f7ae63b1691e726cd353 source_ref=b8bc54fd6dfe1be68bb60012cf18b620e9aac632 role=documentation-sync -->
## `hash_body(body: str) -> str`

Computes SHA-256 hash of section body with leading/trailing whitespace stripped.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:_HEADING_RE fingerprint=b171a12459c1801f28b3970483335daeacef5462126ceb123ef5793ee735f80b body_fp=99086de5a8a2b5859b8df2d8e8d7c98da3d839a0666ffea2c1e8fe95524ea5d3 source_ref=b8bc54fd6dfe1be68bb60012cf18b620e9aac632 role=documentation-sync -->
Regex pattern matching Markdown headings with optional leading whitespace (0-3 spaces) followed by 1-6 hash characters and whitespace.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:_SENTENCE_END_RE fingerprint=46839332c70a94fc506bb56b7637497fd1a8b3a93af0eb5c4ff8390ddeb08946 body_fp=9af3df6824cb757c005266be172ce35df7bbb6674cedd309eb1036f48d8565f1 source_ref=b8bc54fd6dfe1be68bb60012cf18b620e9aac632 role=documentation-sync -->
Regex pattern that matches sentence boundaries: punctuation (`.!?`) followed by whitespace or end of string.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:extract_one_liner fingerprint=fb87254713b9705aec49bf5aaed06df13d5765c8d66d19dd661b746b0045cd82 body_fp=02fa734880039fc4ef9072150fd1772cf409ddd6755a5fe60ce70a149dc18bbb source_ref=b8bc54fd6dfe1be68bb60012cf18b620e9aac632 role=documentation-sync -->
Extracts the first sentence from a triefact section body, skipping headings and truncating to a character limit.

- Returns empty string if no usable text is found
- Collapses whitespace and adds ellipsis when truncated
- Stops at first paragraph break or sentence-ending punctuation
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:AGENT_FRONT_MATTER_KEYS fingerprint=4ffdf447d675342eb7e62f591eb81f0dbe4b8236a7ecbc21145d49565aaf7fa7 body_fp=8294eda21e5594b41824b5d4aa60944267192f07531bea2c9d8f94d349761f2e source_ref=b8bc54fd6dfe1be68bb60012cf18b620e9aac632 role=mcp-server -->
Defines the frontmatter keys that are preserved when rendering triefacts for agents, filtering out trie's internal bookkeeping fields.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:Section fingerprint=5f7b6ba0153d90edd1037820e51184f9b82fa1d5dba45d711ba55d8060aa7757 body_fp=d1583c6431ab8e875beae13cfbf580a8425fd0e2ffa11011005630e498bba5c0 source_ref=831f75c6754c4c40698fbf554c1887d6450d69e0 role=model -->
Represents a parsed triefact section with metadata for fingerprinting and attention tracking.

- `body_fingerprint`: SHA-256 over section body; None for legacy sections without body fingerprints
- `source_ref`: git blob hash of the source file when this section was generated
- `role`: architectural role tag inferred by LLM, persisted to survive graph DB rebuilds
- `historical_mass`: cross-session cognitive importance signal from attention tracking
- `historical_mass_ts`: unix timestamp when historical mass was last updated
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:Prose fingerprint=cf49910dc87437bc09897192fbd13b0a347f9433a85c94f1e599b18c7eceaf2b body_fp=311cfa243f31011d450423a58e02e9136ed13f215e8e825758d63429733d58d7 source_ref=b8bc54fd6dfe1be68bb60012cf18b620e9aac632 role=documentation-sync -->
Represents verbatim text content between trie sections in a triefact file.

- text: Raw string content preserved exactly as written in the source file
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:Chunk fingerprint=27a576a701491dcbdfeae28c3b7f87ee71a034e04c90aa8a336c241cf4a788c1 body_fp=053f0d0a4910d0fbf1cc2bf6dca20f21cc062ed857b3a63b85cbf21506ec62b0 source_ref=b8bc54fd6dfe1be68bb60012cf18b620e9aac632 role=documentation-sync -->
Type alias for a triefact file component that is either a documentation section or human-written prose.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:_dedupe_sections fingerprint=e73e778d47cb90bc42312db46f5c9edcdcff2d282e48ca058689657619c8938d body_fp=eed963feb425248d1ae93862069990eef93f2dd2fa10e5e00e550c0317f88423 source_ref=da9a7d97a5e4b6f64e1ffa28bc72b3d35a4327e5 role=util -->
## `_dedupe_sections(chunks: list[Chunk]) -> list[Chunk]`

Removes duplicate sections with the same qualified_name, keeping the last occurrence at the first occurrence's position.

- Preserves source-order layout while using the most recently written section body
- Passes through non-section prose chunks unchanged
- Enables self-healing of accumulated duplicates on next read/render cycle
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile fingerprint=d7ebe9e5f349408211b267ee9bee5bd42b0ca1ee59d72c3ba55ff23d9a6d7eda body_fp=1e3711dfb5d3338a3c9b232a841d54dd5e5d8c03f8f362cc85986e47f3eb0eda source_ref=831f75c6754c4c40698fbf554c1887d6450d69e0 role=model -->
Parses, manipulates, and renders triefact files containing YAML frontmatter and trie-managed documentation sections.

- `front_matter`: YAML metadata dictionary at file start
- `chunks`: sequence of Section and Prose objects representing file structure
- `parse()`: extracts frontmatter, HTML-delimited sections, and historical mass from raw text
- `upsert_section()`: replaces existing section or appends new one preserving historical mass
- `set_section_role()`: updates only the role field of existing section
- `set_section_historical_mass()`: stamps AGM historical mass on existing section
- `sort_sections()`: reorders sections by source line number while preserving prose
- `render()`: serializes back to text with HTML sentinels and YAML frontmatter
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile.parse fingerprint=ab5f100e4b1afc1d56b61c3b3d86c6942dc39063c14ed54cc4a40760fbe24dee body_fp=bfb530c1e9ba84a0611d056852d81833cbb300d9cd8237907ac2410c2d5b4858 source_ref=831f75c6754c4c40698fbf554c1887d6450d69e0 role=parsing -->
Creates TriefactFile from Markdown text by parsing YAML frontmatter and trie section sentinels.

- Extracts YAML frontmatter from opening `---` blocks, ignoring malformed YAML
- Parses trie sections between `<!-- trie:section -->` and `<!-- trie:end -->` sentinels
- Extracts historical mass and timestamp from `hist_mass=` sentinel field via parse_hist_mass
- Preserves prose chunks between sections as-is
- Strips leading/trailing newlines from section bodies
- Deduplicates sections with same qualified_name, keeping the last occurrence
- Raises ValueError for unterminated sections (missing close sentinel)
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile.empty fingerprint=cc0676809bee8efb34856efbd9c950ae148db930ab90e76ebd3d17bd1eefbc7e body_fp=6cf936ca08fbe35297aba62df1d57f17b36b1e42ae4b35ca3e713e0bed9c5270 source_ref=b8bc54fd6dfe1be68bb60012cf18b620e9aac632 role=documentation-sync -->
Creates an empty TriefactFile instance with no front matter or chunks.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile.get_section fingerprint=aec43c04e2eaaaaf39f4d6be228e0198afa191d15abda68a3879b41b391204d8 body_fp=f1c864958afa692856b1379850a494d51197d0666b7036e896565c4f556bcd1c source_ref=b8bc54fd6dfe1be68bb60012cf18b620e9aac632 role=documentation-sync -->
Returns the first Section in TriefactFile.chunks matching the given qualified_name, or None if not found.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile.section_qnames fingerprint=b3198e06079669f9cdabe77cd2292e047d5fc68e79e8ecb7e0a9f7bff28f0f60 body_fp=86e2903008214db684f493e3eef6b2c24911be73d69480eaf399c7ba5388e046 source_ref=b8bc54fd6dfe1be68bb60012cf18b620e9aac632 role=documentation-sync -->
Returns a list of qualified names for all Section chunks in the TriefactFile.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile.upsert_section fingerprint=fc0918a154c0b0a73fbf8fcede43990ba1602726068aae34ba72219910f66da7 body_fp=8fefa7663c4a69fd8a76e75547a70bac004fbf88e4e05d0b879906fe2f46717f source_ref=831f75c6754c4c40698fbf554c1887d6450d69e0 role=domain -->
## `TriefactFile.upsert_section(*, qualified_name: str, fingerprint: str, body: str, source_ref: str | None = None, role: str = "") -> None`

TriefactFile method that replaces an existing section by qualified_name or appends new one at end.

- `body`: section content; body fingerprint computed automatically
- `source_ref`: git blob hash stamped in sentinel when non-None
- `role`: architectural role tag; empty string omits from sentinel
- Preserves existing AGM historical mass when updating sections
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile.set_section_role fingerprint=b32057736b75dff6ad04d492a7449b92d83d6a102a4787fecfd922b9fd27403a body_fp=0a8f16b36110263bf571953e6b05febc48eddda4e4ef5c61b2507bb61c801833 source_ref=78bd950091facbb1608b4c2f45372223b3f4020f role=model -->
## set_section_role

Updates only the role tag of an existing section in TriefactFile, preserving all other fields and returning whether the section was found.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile.set_section_historical_mass fingerprint=d3e0e057671a6cc5c2fe8998b9c2e9b01dd0ab50441b44feac1097263e183f66 body_fp=f8f5f21d9f818c9cb591d34e12218fcb418b394611952039c34ed21574a05799 source_ref=831f75c6754c4c40698fbf554c1887d6450d69e0 role=model -->
Updates the historical attention mass for a section in TriefactFile without changing its body or other metadata.

- **mass**: Cross-session cognitive importance value to stamp into the section
- **ts**: Unix timestamp when the mass was last updated
- **return**: True if the section was found and updated, False otherwise
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile.sort_sections fingerprint=3a5abfe00c1190b093875944af69f77a27689bb7a756b7a12c709e067e398038 body_fp=cfef4021f5a47b20f87f08420e8dd76e258fd075ea8f75961c34804d8d01ab14 source_ref=b8bc54fd6dfe1be68bb60012cf18b620e9aac632 role=documentation-sync -->
## `TriefactFile.sort_sections(self, start_line_by_qname: dict[str, int]) -> None`

Reorders TriefactFile sections to match their source file line order based on provided line number mapping.

- `start_line_by_qname`: Maps qualified symbol names to their source line numbers
- Sections without mapping entries are placed at the end in original order
- Preserves non-whitespace prose chunks at the beginning
- Drops whitespace-only prose chunks (recreated during rendering)
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile.remove_section fingerprint=d8dc7a57db15d5144ac0f1cb113b03fbe74d7608b5e9b23572384079c5ce8032 body_fp=5996a343aba10297edc08202681264d31aa48a828166f217c0e477d2aaa9d56e source_ref=b8bc54fd6dfe1be68bb60012cf18b620e9aac632 role=documentation-sync -->
Remove a section from TriefactFile chunks by qualified name, returning whether one was found.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile._append_section fingerprint=39d0ed815c7e15cf563957738a217245397a9ae9c72076762ea523a6b7cb189c body_fp=ad87f6b64e97ac718bc4115a03e680d7ec79e36773f752bac0d1c33121df28cd source_ref=b8bc54fd6dfe1be68bb60012cf18b620e9aac632 role=documentation-sync -->
Appends a section to TriefactFile.chunks, ensuring proper blank-line separation from preceding content.

- Adds newlines to the last Prose chunk if it doesn't end with double newline
- Inserts a new Prose chunk with double newline after the last Section
- No prefix needed when appending to empty chunks or after front matter
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile.render fingerprint=4f7523e76271d7fdcd5e28210c4a2753df5b4b217aa8be49a2f772ef9f6f4712 body_fp=c9c85377d7c8a99c7e4048f5f8cd5cffc90ee3f52507180648b4b3765aa8f176 source_ref=831f75c6754c4c40698fbf554c1887d6450d69e0 role=persistence -->
Converts TriefactFile to complete triefact text with YAML frontmatter and sentinel-wrapped sections.

- Emits body_fp field automatically, computing from body if missing for legacy sections
- Separates consecutive sections with blank lines to meet parser requirements  
- Includes optional fields (source_ref, role, hist_mass) only when non-empty/non-zero
- Maintains field order: symbol, fingerprint, body_fp, source_ref, role, hist_mass
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:render_for_agent fingerprint=092ba74e28cdec14b0df2de55c6ab0105f9f6c074da00f6bcccb774d76160d8c body_fp=9d61dda9056130e0aebb96b39bbd6cf24b52590324d5425be84b7f1f8216aaf3 source_ref=b8bc54fd6dfe1be68bb60012cf18b620e9aac632 role=agent-integration -->
Strips trie machinery noise from triefact text to produce clean agent-readable Markdown.

- Removes frontmatter bookkeeping fields, keeping only `description`, `defines`, `incoming_refs`, `outgoing_refs`
- Strips HTML comment sentinels around sections, preserving only body content
- Maintains blank line separation between consecutive sections
<!-- trie:end -->