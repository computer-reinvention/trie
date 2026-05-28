---
trie_version: 0.1.5
source: trie/models.py
file_fingerprint: eed971b1aee49803434c0744c5585a07ecf33c7018ba891ece9c67ea15a7f614
last_synced_at: '2026-05-28T01:40:30Z'
defines:
- kind: module
  qualified_name: trie/models:__module__
  lines: 1-272
- kind: constant
  qualified_name: trie/models:T
  lines: 20-20
- kind: class
  qualified_name: trie/models:GenerationRequest
  lines: 24-31
- kind: class
  qualified_name: trie/models:GenerationResponse
  lines: 35-40
- kind: class
  qualified_name: trie/models:ModelClient
  lines: 43-49
- kind: method
  qualified_name: trie/models:ModelClient.generate
  lines: 47-47
- kind: method
  qualified_name: trie/models:ModelClient.count_tokens
  lines: 49-49
- kind: function
  qualified_name: trie/models:_retry_after_seconds
  lines: 52-67
- kind: function
  qualified_name: trie/models:_is_retryable
  lines: 70-78
- kind: function
  qualified_name: trie/models:_backoff_delay
  lines: 81-95
- kind: function
  qualified_name: trie/models:_run_with_retry
  lines: 98-158
- kind: class
  qualified_name: trie/models:AnthropicClient
  lines: 161-250
- kind: method
  qualified_name: trie/models:AnthropicClient.__init__
  lines: 162-182
- kind: method
  qualified_name: trie/models:AnthropicClient._payload
  lines: 184-207
- kind: method
  qualified_name: trie/models:AnthropicClient.generate
  lines: 209-233
- kind: method
  qualified_name: trie/models:AnthropicClient.count_tokens
  lines: 235-250
- kind: function
  qualified_name: trie/models:make_client
  lines: 253-271
incoming_refs: 88
outgoing_refs: 6
---
<!-- trie:section symbol=trie/models:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=4308b81c01985cb94226de5b112b67fe8612ef329c9dea1313ec5761336f6a07 source_ref=474d1856e9eae610812aee137ef64ddc15dadb3f -->
## `trie.models`

Define LLM client abstractions, retry logic, and the `AnthropicClient` implementation for generating and token-counting documentation requests.

- `GenerationRequest`: frozen dataclass carrying prompt parts for a single LLM call
- `GenerationResponse`: frozen dataclass carrying token-usage stats alongside generated text
- `ModelClient`: structural protocol any client must satisfy
- `make_client`: factory entry-point; accepts `"provider/model"` strings
<!-- trie:end -->
<!-- trie:section symbol=trie/models:T fingerprint=d6131a915181abd7e0ca8fc2c3bed74bab33247b37a29f9660bd3f6ee42198ee body_fp=ebf13a5fed1af16825e5c9931ff010ae618fc9f39c9236219a5eef5f2ed642d4 source_ref=474d1856e9eae610812aee137ef64ddc15dadb3f -->
## `T = TypeVar("T")`

Generic return-type variable used by `_run_with_retry` to preserve the callable's return type.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:GenerationRequest fingerprint=ee00a8e1df60152e58509cf285b21002f69fc9b5031a0a0bad0a3e946cd47302 body_fp=1dc5389f0a5cc4993c7e0b03522890a4a560f76979f4d26c4fd96fb3b82f4741 source_ref=474d1856e9eae610812aee137ef64ddc15dadb3f -->
## `GenerationRequest(system_prompt: str, cached_context: str, request: str, max_tokens: int = 1024)`

Immutable descriptor for a single LLM call, splitting reusable context from per-symbol request content.

- `cached_context`: large shared prefix marked for Anthropic prompt-cache reuse across symbols in one file.
- `request`: small per-symbol delta appended after the cached prefix.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:GenerationResponse fingerprint=e34ee246a929d5405ac0a3faa1b15e8c812e9f2b619f5aa767cd243fda1dc867 body_fp=8ba303d2421cfd1b07dfaa11908f80f76ae001a183060842a08770b4665b09a6 source_ref=474d1856e9eae610812aee137ef64ddc15dadb3f -->
## `GenerationResponse`

Immutable dataclass holding the text and token-usage counters returned by a model call.

- `cache_creation_input_tokens`: tokens written into the prompt cache on this call.
- `cache_read_input_tokens`: tokens served from the prompt cache on this call.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:ModelClient fingerprint=a891b37089e10f77940f6eed6239c2b45cf3f81f2c93f1fa329331f8af0d0a62 body_fp=1c2511cd2c0223a4f987720568f026c2379afd2c944c7bf7e54eb2b33b8d41f1 source_ref=474d1856e9eae610812aee137ef64ddc15dadb3f -->
## `class ModelClient(Protocol)`

Structural protocol defining the interface all model clients must satisfy.

- `model_id`: bare name sent to the provider API, e.g. `"claude-sonnet-4-6"`.
- `full_model_id`: `"provider/model"` string used for telemetry and pricing lookups.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:ModelClient.generate fingerprint=ab5df625bc76dbd4e163bed2dd888df828f90159bb93556525c31821b6541d46 body_fp=578e09876b5596f58a77bcc1abd807157577a8f60faf553bbb76a9e29968b995 source_ref=474d1856e9eae610812aee137ef64ddc15dadb3f -->
## `generate(self, req: GenerationRequest) -> GenerationResponse`

Send a `GenerationRequest` to the model and return a `GenerationResponse`.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:ModelClient.count_tokens fingerprint=ab5df625bc76dbd4e163bed2dd888df828f90159bb93556525c31821b6541d46 body_fp=a954d5f1007b00086f9da7baee55ae2c73a5ee6109b172454f4021f0af555e62 source_ref=474d1856e9eae610812aee137ef64ddc15dadb3f -->
## `count_tokens(self, req: GenerationRequest) -> int`

Count input tokens for a `GenerationRequest` without generating a response.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_retry_after_seconds fingerprint=96c2a9811d4c848d011a6e73e795d5d315cdb7a88978e487f15181c5ef84ecf0 body_fp=df67e5051cb47921efaad0e66e30026b1a216fc5212409765f0fb04d1fa106a4 source_ref=474d1856e9eae610812aee137ef64ddc15dadb3f -->
## `_retry_after_seconds(exc: APIStatusError) -> float | None`

Parse the `retry-after` header from a 429 `APIStatusError` and return the delay in seconds.

- Returns `None` if the header is absent, unparseable, or `exc` has no `response`.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_is_retryable fingerprint=ee433c9d53f6f3c46e0ee319f3c9c52835be6b522acdf64c18434e6c8668eaed body_fp=5921869b6042edc7ba9299daa67b80e5927ace3ff9ce2be308514f71e86c7d32 source_ref=474d1856e9eae610812aee137ef64ddc15dadb3f -->
## `_is_retryable(exc: BaseException) -> bool`

Return `True` if the exception warrants a retry attempt in the retry loop.

- `RateLimitError`, `InternalServerError`, `APITimeoutError`: retryable; all other exceptions are not.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_backoff_delay fingerprint=5950207d3623ac55ea4283316d2680809dfe5b7829c612db3d43ed159842bb61 body_fp=ad02af1066595c26b85402a203b579b2ceda9bde68d53119d84bc1463a65e4ec source_ref=474d1856e9eae610812aee137ef64ddc15dadb3f -->
## `_backoff_delay(*, attempt: int, base: float, cap: float, rng: random.Random) -> float`

Compute a jittered exponential backoff delay in seconds.

- `attempt`: 0-indexed retry count; delay grows as `base * 2**attempt`, capped at `cap`.
- Returns `uniform(0, min(cap, base * 2**attempt))` to prevent thundering-herd.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_run_with_retry fingerprint=edc8f1f69cedccb9b4ecb226edf659e7f32eb54383f1d9b143138b7b01221b32 body_fp=7cda17fe931ac47c662aa11bba30920c9211598807c22d32d6317c5ffb90c50f source_ref=474d1856e9eae610812aee137ef64ddc15dadb3f -->
## `_run_with_retry(fn, *, cfg, kind, model_id, sleep=time.sleep, rng=None) -> T`

Invoke `fn`, retrying on rate-limit, overloaded, and timeout errors with bounded exponential backoff.

- `fn`: zero-argument callable whose return value is passed through on success.
- `cfg`: controls `max_retries`, `retry_base_delay_seconds`, and `retry_cap_seconds`.
- `kind`: label stamped into each `model_call_retry` telemetry event.
- `sleep`: injectable for testing; defaults to `time.sleep`.
- Honours `retry-after` headers on 429; falls back to full-jitter backoff otherwise.
- Re-raises immediately on non-retryable exceptions or after `cfg.max_retries` attempts.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:AnthropicClient fingerprint=4b02a2ac7e8b3de6f34fc290d9c804835e33e714d681be5630686431c7d4d7e5 body_fp=3853db16cb1397edba5d6f79affa4b223f00186c4dd89a2a8c2acbdfe7d83836 source_ref=474d1856e9eae610812aee137ef64ddc15dadb3f -->
## `AnthropicClient(model_id: str, *, client: Anthropic | None = None, sync_cfg: Sync | None = None, full_model_id: str | None = None)`

Implement `ModelClient` against the Anthropic Messages API with telemetry-visible retry logic.

- `model_id`: bare model name sent to the API (e.g. `"claude-sonnet-4-6"`).
- `full_model_id`: `"anthropic/<model>"` string for telemetry/pricing; inferred if omitted.
- `client`: injectable `Anthropic` instance; constructed with `max_retries=0` to suppress SDK retries.
- `sync_cfg`: retry knobs; defaults to `Sync()` dataclass defaults when omitted.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:AnthropicClient.__init__ fingerprint=14954523888082107ed1212c61a27cc5987f7f201f14589287cee12834e5512f body_fp=ff84faaaa97471cd9b70b49f4eeaa52c9fbc41e094ed74c697e52194a8ef2579 source_ref=474d1856e9eae610812aee137ef64ddc15dadb3f -->
## `AnthropicClient.__init__(self, model_id: str, *, client: Anthropic | None = None, sync_cfg: Sync | None = None, full_model_id: str | None = None) -> None`

Initialize an `AnthropicClient`, disabling the SDK's built-in retry loop in favour of trie's own.

- `model_id`: bare model name sent to the API (e.g. `"claude-sonnet-4-6"`).
- `full_model_id`: `"anthropic/model"` string for telemetry/pricing; inferred from `model_id` if omitted.
- `client`: injectable `Anthropic` instance; defaults to `Anthropic(max_retries=0)`.
- `sync_cfg`: retry knobs; defaults to `Sync()` defaults when omitted.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:AnthropicClient._payload fingerprint=5960421b7af1c3033a30ed3a6db0e0c36f5af7f5248046a8d1aa7c78ab2ca7a1 body_fp=f956b445ede27775154c66e64d304b684e8133420e8c1760e2440ec28d4f0527 source_ref=474d1856e9eae610812aee137ef64ddc15dadb3f -->
## `AnthropicClient._payload(self, req: GenerationRequest) -> dict`

Build the Anthropic API request dict from a `GenerationRequest`, applying ephemeral cache controls to system and context blocks.

- Omits the per-symbol `request` content block when empty to avoid API rejection.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:AnthropicClient.generate fingerprint=b1e5c1d97d7819149656f57eb7f6ed0c00a034d7d111b72ff06bf6a43363ac00 body_fp=d817e503137f56aa99f81f05d7d0ed89ae9bab95bc1ae3ab7eb860af6aa64b59 source_ref=474d1856e9eae610812aee137ef64ddc15dadb3f -->
## `AnthropicClient.generate(self, req: GenerationRequest) -> GenerationResponse`

Send a generation request to the Anthropic messages API and return the response with token usage.

- Emits a `model_call` telemetry event including all token counts.
- Retries on rate-limit/overloaded/timeout errors via `_run_with_retry`.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:AnthropicClient.count_tokens fingerprint=7c178f267e3119d197a891ba453210782970593c79b8e4e7c5a7768ba8af2bfb body_fp=fd0e3a8466fefe1c2da8421f707aa6df6c2b10a7ac8cb736b19ada2ecde59d16 source_ref=474d1856e9eae610812aee137ef64ddc15dadb3f -->
## `AnthropicClient.count_tokens(req: GenerationRequest) -> int`

Call the Anthropic token-counting API for `req` and return the input token count.

- Free but rate-limited separately from message creation.
- Counts the exact payload sent by `generate`, not a heuristic estimate.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:make_client fingerprint=3d0e19bae886b2171f8a2f2cf9e2458eda873da3602d0167f653f079cb102b7c body_fp=fe728cc94bea6627e94ba59bfff6731f86b30c550b1c757cf3d6d85d5186cbea source_ref=474d1856e9eae610812aee137ef64ddc15dadb3f -->
## `make_client(model_id: str, *, sync_cfg: Sync | None = None) -> ModelClient`

Construct a `ModelClient` from a `"provider/model"` string; only `anthropic/` is supported.

- `model_id`: must have the form `"provider/model"` — raises `ValueError` otherwise.
- `sync_cfg`: retry knobs; defaults to `Sync()` when omitted.
- Raises `NotImplementedError` for any provider other than `anthropic`.
<!-- trie:end -->