---
trie_version: 0.1.0
source: trie/models.py
file_fingerprint: c832b122814896ee994ddf04fe4e22864cd07ca77e5199daf421bbb2662a5127
last_synced_at: '2026-05-12T18:30:45Z'
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
<!-- trie:section symbol=trie/models:GenerationRequest fingerprint=ee00a8e1df60152e58509cf285b21002f69fc9b5031a0a0bad0a3e946cd47302 body_fp=9307dedd03eaa7d69fe6777c6fefa971a5a88e2b9d9ae3709ec6e72c5b151e05 -->
## `GenerationRequest(system_prompt: str, cached_context: str, request: str, max_tokens: int = 1024)`

Immutable dataclass representing one LLM call with a reusable cached prefix and a per-symbol delta.

- `cached_context`: large shared prefix; Anthropic prompt caching reuses it across calls in the same file.
- `request`: small per-symbol content appended after the cached prefix.
<!-- trie:end -->

<!-- trie:section symbol=trie/models:GenerationResponse fingerprint=e34ee246a929d5405ac0a3faa1b15e8c812e9f2b619f5aa767cd243fda1dc867 body_fp=46ad27ef06c3a5c348cd2c6957098e6639539abbf171729b69941c4de688ee48 -->
## `GenerationResponse`

Frozen dataclass holding token-usage statistics and text returned from a single LLM call.

- `cache_creation_input_tokens`: tokens written into the prompt cache this call.
- `cache_read_input_tokens`: tokens read from an existing prompt cache entry.
<!-- trie:end -->

<!-- trie:section symbol=trie/models:ModelClient fingerprint=81529832a0d7a426971ab9d6b942c3a06c74067ec5af261fa1dcface3bf7a86d body_fp=e106ee94bab1c90cb06d99dc0616a78862bd9a4046e5a059323b2cf85a4faf93 -->
## `class ModelClient(Protocol)`

Structural protocol defining the interface any model client must satisfy.

- `model_id`: string identifying the model being used
- `generate`: sends a request, returns a full `GenerationResponse`
- `count_tokens`: returns input token count without generating output
<!-- trie:end -->

<!-- trie:section symbol=trie/models:ModelClient.generate fingerprint=ab5df625bc76dbd4e163bed2dd888df828f90159bb93556525c31821b6541d46 body_fp=1b776315fd15fb1cb7c749bfcfb8ab2cdb788b4ef45a62d2d75f578fffad59a0 -->
## `generate(self, req: GenerationRequest) -> GenerationResponse`

Send a generation request to the model and return the response.
<!-- trie:end -->

<!-- trie:section symbol=trie/models:ModelClient.count_tokens fingerprint=ab5df625bc76dbd4e163bed2dd888df828f90159bb93556525c31821b6541d46 body_fp=3841152a494b28a5743b5ac33431f4dfa3da5c8d5ae9da5f638d4d76d532caf8 -->
## `count_tokens(self, req: GenerationRequest) -> int`

Return the token count for a generation request.
<!-- trie:end -->

<!-- trie:section symbol=trie/models:AnthropicClient fingerprint=4d3a27d2787aa5101bb4521ed2ae6218ad6c5dc295095253df68f2478472272c body_fp=d3418ab416b33de34dd36c21d8676e924d7ad8188b788ac6fcb2aca4d5528ee5 -->
## `AnthropicClient(model_id: str, *, client: Anthropic | None = None)`

Wrap the Anthropic Messages API to implement `ModelClient` with prompt-caching support.

- `model_id`: bare model name (without `anthropic/` prefix), e.g. `"claude-opus-4-5"`.
- `client`: injectable `Anthropic` instance; defaults to `Anthropic()` if omitted.
<!-- trie:end -->

<!-- trie:section symbol=trie/models:AnthropicClient.generate fingerprint=e06fbfacaa03d607395afffc06b0d7d66a15371333b2899fef59eeeae0fd5cfa body_fp=ca621c76bd58fccf9398ec1aad017006e70ae4fcb54f30edeb117816f8ad36ef -->
## `generate(self, req: GenerationRequest) -> GenerationResponse`

Call the Anthropic messages API and return the response text with token-usage statistics.

- `cache_creation_input_tokens` / `cache_read_input_tokens`: default to `0` if absent from usage.
<!-- trie:end -->

<!-- trie:section symbol=trie/models:AnthropicClient.count_tokens fingerprint=16678f6994490ac63d827ab1faab73ca976999be5c1fef242b4f5bf1e2fcd051 body_fp=dd87417a33fc32fb8201e77b6edbe50fb1bf8da6c09e10557aa1269e92710965 -->
## `count_tokens(self, req: GenerationRequest) -> int`

Return the input token count for `req` using the Anthropic `count_tokens` API.

- Returns the same token count as the actual generation payload would incur.
<!-- trie:end -->

<!-- trie:section symbol=trie/models:make_client fingerprint=b749387d16624608778a717364c5e46e842d8a732d4e1f76434dcf7b57ef3b44 body_fp=271c7d5ea50a84b53077073d10d413460e805b4216a4e4ff83ffbf4d6c6f4d18 -->
## `make_client(model_id: str) -> ModelClient`

Construct a `ModelClient` from a `"provider/model"` string, currently supporting only `anthropic/` as the provider.

- `model_id`: must contain `/`; raises `ValueError` otherwise.
- Raises `NotImplementedError` for any provider other than `anthropic`.
<!-- trie:end -->