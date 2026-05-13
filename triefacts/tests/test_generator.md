---
trie_version: 0.1.0
source: tests/test_generator.py
file_fingerprint: 9d2c435ebc73dfbbdecf1a5bc5060b1343eb3106e63e9ec5e820ab75de2ff674
last_synced_at: '2026-05-12T18:30:19Z'
defines:
- kind: class
  qualified_name: tests/test_generator:FakeClient
  lines: 20-35
- kind: method
  qualified_name: tests/test_generator:FakeClient.generate
  lines: 27-35
- kind: function
  qualified_name: tests/test_generator:test_cached_context_includes_source_and_filename
  lines: 38-43
- kind: function
  qualified_name: tests/test_generator:test_request_names_symbol_and_lines
  lines: 46-53
- kind: function
  qualified_name: tests/test_generator:test_generate_section_passes_correct_prompt
  lines: 56-72
- kind: function
  qualified_name: tests/test_generator:test_generate_section_strips_surrounding_whitespace
  lines: 75-83
- kind: function
  qualified_name: tests/test_generator:test_make_client_rejects_unknown_provider
  lines: 86-88
- kind: function
  qualified_name: tests/test_generator:test_make_client_requires_provider_prefix
  lines: 91-93
- kind: function
  qualified_name: tests/test_generator:test_make_client_anthropic_constructs
  lines: 96-107
incoming_refs: 0
outgoing_refs: 16
---
<!-- trie:section symbol=tests/test_generator:FakeClient fingerprint=ebec988fe34a3959e1dc4041622df9100811f16c13ee31cd51550585e35d2deb body_fp=c0e9109077d9f3d9ecc62deba257adef2e1b4401b8e79a67551f24ccce9f865f -->
## `FakeClient`

Test double that records the last `GenerationRequest` and returns a canned `GenerationResponse`.

- `response_text`: default Markdown snippet returned by `generate`.
- `last_request`: stores the most recent request for assertion in tests.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_generator:FakeClient.generate fingerprint=42d29f746c846f08569316c39868e14083913bde3de32fbf80aea806431cee3a body_fp=a3eb9ca7beb24153a300b50cda44a264c032ecc7dee0b71ab59a8837eb139405 -->
## `generate(self, req: GenerationRequest) -> GenerationResponse`

Record the request and return a canned `GenerationResponse` with fixed token counts.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_generator:test_cached_context_includes_source_and_filename fingerprint=05c2240c12cb32e9582df345efbc8008b1869ef148587ed7d624e7dec18248ff body_fp=85f706b395f03b00cdeb3017ca31be95eb22b06885970ff480d9f061abf998a0 -->
## `test_cached_context_includes_source_and_filename()`

Assert that `build_cached_context` embeds the file path, source code, and a Python fenced block in its output.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_generator:test_request_names_symbol_and_lines fingerprint=abfebb44b13552570306f37907d56c0e6acd08c47016a54dda802ef88ba398b4 body_fp=ea0dfac44410ac168c1dbf2daa22d2bcf90516ccd0ed49d337804475d7723acf -->
## `test_request_names_symbol_and_lines(tmp_path: Path)`

Assert that `_build_request` includes the symbol's qualified name, kind, and line reference.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_generator:test_generate_section_passes_correct_prompt fingerprint=795a74eedf9662289e987121ee0a7ceaf9d5554910b2acadc3934d7556b5cfb2 body_fp=88fa5b863fe67917e1de094fe1bf46736dfb4b74a7134d9a2a9ca91c480a9012 -->
## `test_generate_section_passes_correct_prompt(tmp_path: Path)`

Verify that `generate_section` sends the correct system prompt, cached context, and request, and returns a properly populated section.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_generator:test_generate_section_strips_surrounding_whitespace fingerprint=3bd204788338622df5251a6832f74b175b6480c415c0f2fdd8185cf4a015a702 body_fp=c62b99b8e09fbf4ae37f4e4ef73fac8829de3ffdb59e08ea98b2dda270501a55 -->
## `test_generate_section_strips_surrounding_whitespace(tmp_path: Path)`

Assert that `generate_section` strips leading and trailing whitespace from the model response body.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_generator:test_make_client_rejects_unknown_provider fingerprint=f872f29b5c63a1e81c80c37abf32fe8bb20662ff5ee60dcd7b0817015d657eef body_fp=a095f2fb142874717d69b3bac4b6c4ce54abed5cde4262ca8938af5c6743ab31 -->
## `test_make_client_rejects_unknown_provider()`

Assert that `make_client` raises `NotImplementedError` for an unrecognised provider prefix.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_generator:test_make_client_requires_provider_prefix fingerprint=df2b5275115453c8315d3057c0b82e0ee7f1cedc1b60219fc1624984efb88cda body_fp=315916c1f41b21afae611269fc89221e9784f685fc0d3607b0704774a7c9a7b6 -->
## `test_make_client_requires_provider_prefix()`

Assert `make_client` raises `ValueError` when the model string lacks a `provider/` prefix.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_generator:test_make_client_anthropic_constructs fingerprint=abb7663559910baa08ced366ecfdf3a45b7765fa1724004772179456482b1b31 body_fp=ae19325db905250c0c14a1bd9a6cfb0fbb2dfc719cdbed2a573c02f9e2f48999 -->
## `test_make_client_anthropic_constructs(monkeypatch: pytest.MonkeyPatch)`

Verify that `make_client` constructs an Anthropic client and propagates `model_id` without invoking the real SDK.
<!-- trie:end -->