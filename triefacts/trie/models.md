---
trie_version: 0.1.0
source: trie/models.py
file_fingerprint: 633c70ba0083615574b83566baa11a4e2d89f259aa25213c06b5312abaaee1dd
last_synced_at: '2026-05-14T18:32:14Z'
defines:
- kind: class
  qualified_name: trie/models:GenerationRequest
  lines: 12-19
- kind: class
  qualified_name: trie/models:GenerationResponse
  lines: 23-28
- kind: class
  qualified_name: trie/models:ModelClient
  lines: 31-36
- kind: method
  qualified_name: trie/models:ModelClient.generate
  lines: 34-34
- kind: method
  qualified_name: trie/models:ModelClient.count_tokens
  lines: 36-36
- kind: class
  qualified_name: trie/models:AnthropicClient
  lines: 39-98
- kind: method
  qualified_name: trie/models:AnthropicClient.generate
  lines: 69-86
- kind: method
  qualified_name: trie/models:AnthropicClient.count_tokens
  lines: 88-98
- kind: function
  qualified_name: trie/models:make_client
  lines: 101-115
incoming_refs: 39
outgoing_refs: 0
---
<!-- trie:section symbol=trie/models:GenerationRequest fingerprint=ee00a8e1df60152e58509cf285b21002f69fc9b5031a0a0bad0a3e946cd47302 body_fp=cda362a4b85d926dc6c80be1647e94e2c65825c86bf5773c52778704cd29584a -->
## `GenerationRequest(system_prompt: str, cached_context: str, request: str, max_tokens: int = 1024)`

Frozen dataclass representing a single LLM call with prompt-caching support.

- `cached_context`: reused across calls in the same file via Anthropic prompt caching.
- `request`: small per-symbol delta appended after the cached prefix.
<!-- trie:end -->

<!-- trie:section symbol=trie/models:GenerationResponse fingerprint=e34ee246a929d5405ac0a3faa1b15e8c812e9f2b619f5aa767cd243fda1dc867 body_fp=e05ed9c36ee30e7e8526bf6b2343346362629d9e1130da9688136deaffc6d79a -->
## `GenerationResponse`

Frozen dataclass holding token-usage statistics and text returned from a single LLM call.

- `cache_creation_input_tokens`: tokens written to the prompt cache this call.
- `cache_read_input_tokens`: tokens read from an existing prompt cache entry.
<!-- trie:end -->

<!-- trie:section symbol=trie/models:ModelClient fingerprint=81529832a0d7a426971ab9d6b942c3a06c74067ec5af261fa1dcface3bf7a86d body_fp=5065cfd41539ba717c02cd2f3aef91ba6f836149f4f7ded4478979f684d872cb -->
## `class ModelClient(Protocol)`

Structural protocol defining the interface any model client must satisfy.

- `model_id`: string identifier for the model being used
- `generate`: invoke the model and return a `GenerationResponse`
- `count_tokens`: return token count without generating output
<!-- trie:end -->

<!-- trie:section symbol=trie/models:ModelClient.generate fingerprint=ab5df625bc76dbd4e163bed2dd888df828f90159bb93556525c31821b6541d46 body_fp=b95b7e83e656b3cc5d3c5fc0b52d0357bf17eb5b2ccbd9bf492d7a0392249bda -->
## `generate(self, req: GenerationRequest) -> GenerationResponse`

Send a generation request and return the model's response with token usage.
<!-- trie:end -->

<!-- trie:section symbol=trie/models:ModelClient.count_tokens fingerprint=ab5df625bc76dbd4e163bed2dd888df828f90159bb93556525c31821b6541d46 body_fp=3841152a494b28a5743b5ac33431f4dfa3da5c8d5ae9da5f638d4d76d532caf8 -->
## `count_tokens(self, req: GenerationRequest) -> int`

Return the token count for a generation request.
<!-- trie:end -->

<!-- trie:section symbol=trie/models:AnthropicClient fingerprint=47bb990db249583557415c96bab37367fc5b2e149d2f970e321dd09c8f2b7da6 body_fp=a111a16f21a70357b66d76c52164df097589d16408dd03c7f0bc04fcf396947b -->
## `AnthropicClient(model_id: str, *, client: Anthropic | None = None)`

Wrap the Anthropic Messages API to implement `ModelClient` with prompt-caching support.

- `model_id`: bare model name (without `anthropic/` prefix).
- `client`: injectable `Anthropic` instance; creates a default one if omitted.
<!-- trie:end -->

<!-- trie:section symbol=trie/models:AnthropicClient.generate fingerprint=86ce8139d0e7900053bc3269f43af4c6cb28b49cbd9387e4b16ccb53f70effef body_fp=1262c466906146daa002f7c0c7c565f537ed2e1cc96cd7e20bb499e271a748f2 -->
## `generate(self, req: GenerationRequest) -> GenerationResponse`

Call the Anthropic messages API, record telemetry, and return token usage with generated text.

- `req.max_tokens`: caps output length; passed directly to `messages.create`.
- Returns concatenated text from all `text`-type content blocks.
<!-- trie:end -->

<!-- trie:section symbol=trie/models:AnthropicClient.count_tokens fingerprint=bbe317b3b56c093abce60dc81fee8c7ce7e707f6e7acfb3a5a6daea29ed8fbda body_fp=d7f4f14ac04e0c1bdffe67237fecbe7fddb4eb239d51a5b406e208fe648bf885 -->
## `count_tokens(self, req: GenerationRequest) -> int`

Return the input token count for `req` using the Anthropic token-counting API.

- Returns the exact token count for the full payload (system + cached context + request), not a heuristic.
<!-- trie:end -->

<!-- trie:section symbol=trie/models:make_client fingerprint=b749387d16624608778a717364c5e46e842d8a732d4e1f76434dcf7b57ef3b44 body_fp=c358fafb7d1b12b14c9879bc9774dfa6f14c1c3abc3b60ce50d936050ea2aa57 -->
## `make_client(model_id: str) -> ModelClient`

Construct a `ModelClient` from a `"provider/model"` string, returning an `AnthropicClient` for the `anthropic/` provider.

- `model_id`: must contain `/`; only `"anthropic/<model>"` is supported.
- Raises `ValueError` if no `/` present.
- Raises `NotImplementedError` for any provider other than `"anthropic"`.
<!-- trie:end -->