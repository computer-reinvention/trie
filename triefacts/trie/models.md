---
trie_version: 0.1.0
source: trie/models.py
file_fingerprint: c832b122814896ee994ddf04fe4e22864cd07ca77e5199daf421bbb2662a5127
last_synced_at: '2026-05-14T17:27:47Z'
defines:
- kind: class
  qualified_name: trie/models:GenerationRequest
  lines: 10-17
- kind: class
  qualified_name: trie/models:GenerationResponse
  lines: 21-26
- kind: class
  qualified_name: trie/models:ModelClient
  lines: 29-34
- kind: method
  qualified_name: trie/models:ModelClient.generate
  lines: 32-32
- kind: method
  qualified_name: trie/models:ModelClient.count_tokens
  lines: 34-34
- kind: class
  qualified_name: trie/models:AnthropicClient
  lines: 37-87
- kind: method
  qualified_name: trie/models:AnthropicClient.generate
  lines: 67-77
- kind: method
  qualified_name: trie/models:AnthropicClient.count_tokens
  lines: 79-87
- kind: function
  qualified_name: trie/models:make_client
  lines: 90-104
incoming_refs: 39
outgoing_refs: 0
---
<!-- trie:section symbol=trie/models:GenerationRequest fingerprint=ee00a8e1df60152e58509cf285b21002f69fc9b5031a0a0bad0a3e946cd47302 body_fp=a7e5e7846f328f0a67fa3ae6a4e287b8d86f687729d1ed4430e1b6f371b7ce69 -->
## `GenerationRequest(system_prompt: str, cached_context: str, request: str, max_tokens: int = 1024)`

Frozen dataclass representing a single LLM call with prompt-caching support.

- `cached_context`: large shared prefix intended for reuse across calls via Anthropic prompt caching.
- `request`: small per-symbol delta appended after the cached context.
<!-- trie:end -->

<!-- trie:section symbol=trie/models:GenerationResponse fingerprint=e34ee246a929d5405ac0a3faa1b15e8c812e9f2b619f5aa767cd243fda1dc867 body_fp=9a78fb021b836576e55298c7c1a1edc24bb545de8f115078569e6e90d983cacb -->
## `GenerationResponse`

Frozen dataclass holding token-usage statistics and text returned from a single LLM call.

- **`cache_creation_input_tokens`**: tokens billed for writing a new prompt cache entry.
- **`cache_read_input_tokens`**: tokens billed for reading an existing prompt cache entry.
<!-- trie:end -->

<!-- trie:section symbol=trie/models:ModelClient fingerprint=81529832a0d7a426971ab9d6b942c3a06c74067ec5af261fa1dcface3bf7a86d body_fp=7b9f25f0ecff9ddc06e2743c793722055a28e674271dca84c99dbb1d04930808 -->
## `class ModelClient(Protocol)`

Structural protocol defining the interface any model client must satisfy.

- `model_id`: string identifier for the deployed model
- `generate`: execute one LLM call, return text and token-usage metadata
- `count_tokens`: return input token count without generating a response
<!-- trie:end -->

<!-- trie:section symbol=trie/models:ModelClient.generate fingerprint=ab5df625bc76dbd4e163bed2dd888df828f90159bb93556525c31821b6541d46 body_fp=1b776315fd15fb1cb7c749bfcfb8ab2cdb788b4ef45a62d2d75f578fffad59a0 -->
## `generate(self, req: GenerationRequest) -> GenerationResponse`

Send a generation request to the model and return the response.
<!-- trie:end -->

<!-- trie:section symbol=trie/models:ModelClient.count_tokens fingerprint=ab5df625bc76dbd4e163bed2dd888df828f90159bb93556525c31821b6541d46 body_fp=3841152a494b28a5743b5ac33431f4dfa3da5c8d5ae9da5f638d4d76d532caf8 -->
## `count_tokens(self, req: GenerationRequest) -> int`

Return the token count for a generation request.
<!-- trie:end -->

<!-- trie:section symbol=trie/models:AnthropicClient fingerprint=4d3a27d2787aa5101bb4521ed2ae6218ad6c5dc295095253df68f2478472272c body_fp=a6534ff205be7bd1d42df9b713b7387ee7c1a411c867aaf3eb0f18bbc21bd6df -->
## `AnthropicClient(model_id: str, *, client: Anthropic | None = None)`

Wrap the Anthropic messages API to implement `ModelClient` with prompt-caching support.

- `model_id`: bare model name (without `anthropic/` prefix)
- `client`: injected `Anthropic` instance; creates a default one if `None`
<!-- trie:end -->

<!-- trie:section symbol=trie/models:AnthropicClient.generate fingerprint=e06fbfacaa03d607395afffc06b0d7d66a15371333b2899fef59eeeae0fd5cfa body_fp=2e87c9756813c8c68674b0a0e691d8e064c56f202db20f5df9160d9994d897e4 -->
## `generate(self, req: GenerationRequest) -> GenerationResponse`

Call the Anthropic messages API and return the response text with token-usage statistics.
<!-- trie:end -->

<!-- trie:section symbol=trie/models:AnthropicClient.count_tokens fingerprint=16678f6994490ac63d827ab1faab73ca976999be5c1fef242b4f5bf1e2fcd051 body_fp=b0abbf4a4a366e4848579fa231cfa42e0a720ea9a8d04b8a90494ff5e41b9c2c -->
## `count_tokens(self, req: GenerationRequest) -> int`

Return the input token count for `req` using the Anthropic `count_tokens` API.

- **`req.request`**: may be empty string; empty content block is omitted from payload.
<!-- trie:end -->

<!-- trie:section symbol=trie/models:make_client fingerprint=b749387d16624608778a717364c5e46e842d8a732d4e1f76434dcf7b57ef3b44 body_fp=3ac10ebb6e7c50c214fb10b2b6107d540e5ee000954df22d96fa0f595f0302a9 -->
## `make_client(model_id: str) -> ModelClient`

Construct a `ModelClient` from a `"provider/model"` string, currently supporting only the `anthropic/` provider.

- `model_id`: must follow `"provider/model"` format; raises `ValueError` otherwise.
- Raises `NotImplementedError` for any provider other than `anthropic`.
<!-- trie:end -->