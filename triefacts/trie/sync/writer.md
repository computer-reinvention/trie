---
trie_version: 0.1.5
source: trie/sync/writer.py
file_fingerprint: 39f9c3cbc014514a4516727959f1fdf5afafe18f49555064c60c72f26cc2e2a0
last_synced_at: '2026-06-06T14:18:54Z'
defines:
- kind: module
  qualified_name: trie/sync/writer:__module__
  lines: 1-441
- kind: constant
  qualified_name: trie/sync/writer:SECTION_OPEN_RE
  lines: 43-49
- kind: constant
  qualified_name: trie/sync/writer:SECTION_CLOSE_RE
  lines: 50-50
- kind: constant
  qualified_name: trie/sync/writer:SECTION_CLOSE
  lines: 51-51
- kind: constant
  qualified_name: trie/sync/writer:FRONT_MATTER_RE
  lines: 52-52
- kind: function
  qualified_name: trie/sync/writer:hash_body
  lines: 55-62
- kind: constant
  qualified_name: trie/sync/writer:_HEADING_RE
  lines: 65-65
- kind: constant
  qualified_name: trie/sync/writer:_SENTENCE_END_RE
  lines: 66-66
- kind: function
  qualified_name: trie/sync/writer:extract_one_liner
  lines: 69-100
- kind: constant
  qualified_name: trie/sync/writer:AGENT_FRONT_MATTER_KEYS
  lines: 108-113
- kind: class
  qualified_name: trie/sync/writer:Section
  lines: 117-126
- kind: class
  qualified_name: trie/sync/writer:Prose
  lines: 130-131
- kind: constant
  qualified_name: trie/sync/writer:Chunk
  lines: 134-134
- kind: function
  qualified_name: trie/sync/writer:_dedupe_sections
  lines: 137-165
- kind: class
  qualified_name: trie/sync/writer:TriefactFile
  lines: 169-375
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.parse
  lines: 174-223
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.empty
  lines: 226-227
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.get_section
  lines: 231-235
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.section_qnames
  lines: 237-238
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.upsert_section
  lines: 242-274
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.set_section_role
  lines: 276-290
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.sort_sections
  lines: 292-314
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.remove_section
  lines: 316-321
- kind: method
  qualified_name: trie/sync/writer:TriefactFile._append_section
  lines: 323-334
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.render
  lines: 338-375
- kind: function
  qualified_name: trie/sync/writer:render_for_agent
  lines: 378-440
incoming_refs: 75
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
<!-- trie:section symbol=trie/sync/writer:SECTION_OPEN_RE fingerprint=3f50547b6d4555044719d9bac0a620219f804497cc9855320036951ed893bfe6 body_fp=954df18dbb34b07e4a6925a7bf3659b20dce831002eb229fb8688b66c5eb1e06 source_ref=78bd950091facbb1608b4c2f45372223b3f4020f role=parsing -->
Regex pattern matching triefact section opening HTML comments with symbol name, fingerprint, and optional body_fp, source_ref, and role fields.

- Matches line-anchored comments like `<!-- trie:section symbol=foo.bar fingerprint=abc123 -->`
- Uses named groups for extracting `symbol`, `fp`, `body_fp`, `source_ref`, and `role` metadata
- Backward compatible: `body_fp`, `source_ref`, and `role` are optional for legacy sections
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
<!-- trie:section symbol=trie/sync/writer:Section fingerprint=734c957605002e25718f8ced8d064dac205226486fbad13ec4c1646c788be4d8 body_fp=719c347187a89bec0438311e26ebf66706c86a312b399b6202d9f15710005ea2 source_ref=78bd950091facbb1608b4c2f45372223b3f4020f role=model -->
Immutable data container representing a parsed trie documentation section.

- `body_fingerprint`: SHA-256 over the body text; None for sections written by trie ≤0.1
- `source_ref`: git blob hash of the file when section was generated
- `role`: LLM-inferred architectural role tag; empty string when unknown or legacy
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
<!-- trie:section symbol=trie/sync/writer:TriefactFile fingerprint=b9f8446562ff505ffb93542ff4d811eb16d6363ac25a030dbbe834ffefbe41b4 body_fp=dabbc978e912786294894f9a5dc809dcbcd094e94be70183b933987873770d33 source_ref=da9a7d97a5e4b6f64e1ffa28bc72b3d35a4327e5 role=model -->
Parses, manipulates, and renders triefact files containing YAML frontmatter and trie-managed documentation sections.

- `front_matter`: YAML metadata dictionary at file start
- `chunks`: sequence of Section and Prose objects representing file structure
- `parse()`: extracts frontmatter and HTML-delimited sections from raw text
- `upsert_section()`: replaces existing section or appends new one with computed body fingerprint
- `set_section_role()`: updates only the role field of existing section
- `sort_sections()`: reorders sections by source line number while preserving prose
- `render()`: serializes back to text with HTML sentinels and YAML frontmatter
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile.parse fingerprint=bcbf1948f3e759d430ff14a0bd5fe43fa6c27a4aab47687d732df5a5c5da3d1a body_fp=fa67cbb5443abab1235aa537752f2031694d56c3721555e2823c8b0f711e8c46 source_ref=da9a7d97a5e4b6f64e1ffa28bc72b3d35a4327e5 role=parsing -->
Creates TriefactFile from Markdown text by parsing YAML frontmatter and trie section sentinels.

- Extracts YAML frontmatter from opening `---` blocks, ignoring malformed YAML
- Parses trie sections between `<!-- trie:section -->` and `<!-- trie:end -->` sentinels
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
<!-- trie:section symbol=trie/sync/writer:TriefactFile.upsert_section fingerprint=f5c3375f4ca32ffb59e2513e49b00f2122e6cc7c95d3e57f4f28ecad0710d40d body_fp=89f8c715a4171931ea21018e756f2c99725b0d2db65420b6de3edf1e2164d613 source_ref=78bd950091facbb1608b4c2f45372223b3f4020f role=model -->
Replaces an existing section in TriefactFile by qualified name or appends a new section at the end.

- `body_fingerprint`: Computed automatically from `body` parameter
- `source_ref`: When None, field is omitted from rendered sentinel
- `role`: Empty string omits field from sentinel
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile.set_section_role fingerprint=b32057736b75dff6ad04d492a7449b92d83d6a102a4787fecfd922b9fd27403a body_fp=0a8f16b36110263bf571953e6b05febc48eddda4e4ef5c61b2507bb61c801833 source_ref=78bd950091facbb1608b4c2f45372223b3f4020f role=model -->
## set_section_role

Updates only the role tag of an existing section in TriefactFile, preserving all other fields and returning whether the section was found.
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
<!-- trie:section symbol=trie/sync/writer:TriefactFile.render fingerprint=65f4e4c0a8c735c21363d77fb9c5e6f88fd65de9d7c6e79f2e76a1e187ad7f3a body_fp=e6827f18cbb63a71a4ca8e9d6504c6cca8d02c33d7a0a2fa0790e297f45eedfc source_ref=78bd950091facbb1608b4c2f45372223b3f4020f role=persistence -->
Serializes TriefactFile to Markdown with YAML frontmatter and trie section sentinels.

- Emits frontmatter block if present, wrapped in `---` delimiters
- Preserves Prose chunks verbatim between sections
- Generates section sentinels with fingerprints, metadata, and role fields when present
- Ensures blank line separation between consecutive sections
- Auto-computes body fingerprints for legacy sections missing them
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:render_for_agent fingerprint=092ba74e28cdec14b0df2de55c6ab0105f9f6c074da00f6bcccb774d76160d8c body_fp=9d61dda9056130e0aebb96b39bbd6cf24b52590324d5425be84b7f1f8216aaf3 source_ref=b8bc54fd6dfe1be68bb60012cf18b620e9aac632 role=agent-integration -->
Strips trie machinery noise from triefact text to produce clean agent-readable Markdown.

- Removes frontmatter bookkeeping fields, keeping only `description`, `defines`, `incoming_refs`, `outgoing_refs`
- Strips HTML comment sentinels around sections, preserving only body content
- Maintains blank line separation between consecutive sections
<!-- trie:end -->