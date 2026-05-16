---
trie_version: 0.1.0
source: trie/models.py
file_fingerprint: eed971b1aee49803434c0744c5585a07ecf33c7018ba891ece9c67ea15a7f614
last_synced_at: '2026-05-16T11:23:08Z'
defines:
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
incoming_refs: 61
outgoing_refs: 2
---
<!-- trie:section symbol=trie/models:GenerationRequest fingerprint=ee00a8e1df60152e58509cf285b21002f69fc9b5031a0a0bad0a3e946cd47302 body_fp=cda362a4b85d926dc6c80be1647e94e2c65825c86bf5773c52778704cd29584a source_ref=e12e23ef268599c29347001c72ed8323b67a45bd -->
## `GenerationRequest(system_prompt: str, cached_context: str, request: str, max_tokens: int = 1024)`

Frozen dataclass representing a single LLM call with prompt-caching support.

- `cached_context`: reused across calls in the same file via Anthropic prompt caching.
- `request`: small per-symbol delta appended after the cached prefix.
<!-- trie:end -->

<!-- trie:section symbol=trie/models:GenerationResponse fingerprint=e34ee246a929d5405ac0a3faa1b15e8c812e9f2b619f5aa767cd243fda1dc867 body_fp=e05ed9c36ee30e7e8526bf6b2343346362629d9e1130da9688136deaffc6d79a source_ref=e12e23ef268599c29347001c72ed8323b67a45bd -->
## `GenerationResponse`

Frozen dataclass holding token-usage statistics and text returned from a single LLM call.

- `cache_creation_input_tokens`: tokens written to the prompt cache this call.
- `cache_read_input_tokens`: tokens read from an existing prompt cache entry.
<!-- trie:end -->

<!-- trie:section symbol=trie/models:ModelClient fingerprint=a891b37089e10f77940f6eed6239c2b45cf3f81f2c93f1fa329331f8af0d0a62 body_fp=7de28aadc3a53adece5ea1faef3ee158bcbc171dc333f5012abdfdd261dc1c83 source_ref=474d1856e9eae610812aee137ef64ddc15dadb3f -->
## `class ModelClient(Protocol)`

Structural protocol defining the interface any model client must satisfy.

- `model_id`: bare model name passed to the provider API (e.g. `"claude-sonnet-4-6"`)
- `full_model_id`: `"provider/model"` string used for telemetry and pricing lookups
- `generate`: invoke the model and return a `GenerationResponse`
- `count_tokens`: return token count without generating output
<!-- trie:end -->

<!-- trie:section symbol=trie/models:ModelClient.generate fingerprint=ab5df625bc76dbd4e163bed2dd888df828f90159bb93556525c31821b6541d46 body_fp=b95b7e83e656b3cc5d3c5fc0b52d0357bf17eb5b2ccbd9bf492d7a0392249bda source_ref=e12e23ef268599c29347001c72ed8323b67a45bd -->
## `generate(self, req: GenerationRequest) -> GenerationResponse`

Send a generation request and return the model's response with token usage.
<!-- trie:end -->

<!-- trie:section symbol=trie/models:ModelClient.count_tokens fingerprint=ab5df625bc76dbd4e163bed2dd888df828f90159bb93556525c31821b6541d46 body_fp=3841152a494b28a5743b5ac33431f4dfa3da5c8d5ae9da5f638d4d76d532caf8 source_ref=e12e23ef268599c29347001c72ed8323b67a45bd -->
## `count_tokens(self, req: GenerationRequest) -> int`

Return the token count for a generation request.
<!-- trie:end -->

<!-- trie:section symbol=trie/models:AnthropicClient fingerprint=4b02a2ac7e8b3de6f34fc290d9c804835e33e714d681be5630686431c7d4d7e5 body_fp=a20ebbe7d9882e860c5c841d307a2dc6a02ebe1b9a8cf20e94a99adc6713c341 source_ref=474d1856e9eae610812aee137ef64ddc15dadb3f -->
## `AnthropicClient(model_id: str, *, client: Anthropic | None = None, sync_cfg: Sync | None = None, full_model_id: str | None = None)`

Wrap the Anthropic Messages API to implement `ModelClient` with prompt-caching support and configurable retry behaviour.

- `model_id`: bare model name sent to the API (without `anthropic/` prefix).
- `full_model_id`: `"anthropic/..."` string used for telemetry and pricing; defaults to `f"anthropic/{model_id}"`.
- `client`: injectable `Anthropic` instance; creates one with `max_retries=0` if omitted.
- `sync_cfg`: retry knobs (max attempts, backoff bounds); defaults to `Sync()` defaults.
<!-- trie:end -->

<!-- trie:section symbol=trie/models:AnthropicClient.generate fingerprint=b1e5c1d97d7819149656f57eb7f6ed0c00a034d7d111b72ff06bf6a43363ac00 body_fp=a820616b0e562eea6c5d2cef05c91bba88653bba95a637bd3cdddbaa4072c56a source_ref=474d1856e9eae610812aee137ef64ddc15dadb3f -->
## `generate(self, req: GenerationRequest) -> GenerationResponse`

Call the Anthropic messages API with retry logic, record telemetry, and return token usage with generated text.

- `req.max_tokens`: caps output length; passed directly to `messages.create`.
- Returns concatenated text from all `text`-type content blocks.
- Retries on rate-limit, server error, and timeout per `self._sync_cfg`.
<!-- trie:end -->

<!-- trie:section symbol=trie/models:AnthropicClient.count_tokens fingerprint=7c178f267e3119d197a891ba453210782970593c79b8e4e7c5a7768ba8af2bfb body_fp=c834ed496c7a7adc0682d438aacaa366111b8b6e19386686490c33f8361fbe3d source_ref=474d1856e9eae610812aee137ef64ddc15dadb3f -->
## `count_tokens(self, req: GenerationRequest) -> int`

Return the input token count for `req` using the Anthropic token-counting API, with retry on rate-limit/overload/timeout errors.

- Returns the exact token count for the full payload (system + cached context + request), not a heuristic.
- Retries honour `retry-after` headers and exponential backoff per `self._sync_cfg`.
<!-- trie:end -->

<!-- trie:section symbol=trie/models:make_client fingerprint=3d0e19bae886b2171f8a2f2cf9e2458eda873da3602d0167f653f079cb102b7c body_fp=5cb7649cfd32ecb52ca698fbf5666aeaf91cd1819516a36be8ffe65172438841 source_ref=474d1856e9eae610812aee137ef64ddc15dadb3f -->
## `make_client(model_id: str, *, sync_cfg: Sync | None = None) -> ModelClient`

Construct a `ModelClient` from a `"provider/model"` string, returning an `AnthropicClient` for the `anthropic/` provider.

- `model_id`: must contain `/`; only `"anthropic/<model>"` is supported.
- `sync_cfg`: retry knobs forwarded to the client; defaults to `Sync()` when omitted.
- Raises `ValueError` if no `/` present.
- Raises `NotImplementedError` for any provider other than `"anthropic"`.
<!-- trie:end -->

<!-- trie:section symbol=trie/models:AnthropicClient.__init__ fingerprint=14954523888082107ed1212c61a27cc5987f7f201f14589287cee12834e5512f body_fp=b7a321db06903131c7b676df09627412d7a85b9d95268efb3a25fbe90c964705 source_ref=474d1856e9eae610812aee137ef64ddc15dadb3f -->
## `AnthropicClient.__init__(self, model_id: str, *, client: Anthropic | None = None, sync_cfg: Sync | None = None, full_model_id: str | None = None) -> None`

Initialize an `AnthropicClient`, creating a default `Anthropic` SDK client (with `max_retries=0`) and retry config if none are provided.

- `sync_cfg`: controls retry knobs; defaults to `Sync()` when omitted.
- `full_model_id`: "provider/model" string for telemetry/pricing; defaults to `"anthropic/{model_id}"`.
<!-- trie:end -->

<!-- trie:section symbol=trie/models:AnthropicClient._payload fingerprint=5960421b7af1c3033a30ed3a6db0e0c36f5af7f5248046a8d1aa7c78ab2ca7a1 body_fp=e7a8d99e27cfbdbf14c6d47de2d7685c6cfaa22d645800b6723619c57b883941 source_ref=e12e23ef268599c29347001c72ed8323b67a45bd -->
## `_payload(self, req: GenerationRequest) -> dict`

Build the Anthropic API payload dict from a `GenerationRequest`, applying prompt caching headers.

- Omits the `request` content block when empty to avoid API rejection.
<!-- trie:end -->

<!-- trie:section symbol=trie/models:_retry_after_seconds fingerprint=96c2a9811d4c848d011a6e73e795d5d315cdb7a88978e487f15181c5ef84ecf0 body_fp=ab8cd94458d1fbe039683c36e16caaac8c2d431f56de19a833baf28304e48bdb source_ref=0eace8ba1bfe42022eaa1c2bfa10076fcf325f1c -->
## `_retry_after_seconds(exc: APIStatusError) -> float | None`

Extract the `retry-after` header value from a 429 response as seconds.

- Returns `None` if header is absent, unparseable, or `exc` has no response.
<!-- trie:end -->

<!-- trie:section symbol=trie/models:_is_retryable fingerprint=ee433c9d53f6f3c46e0ee319f3c9c52835be6b522acdf64c18434e6c8668eaed body_fp=0d0c7a73e0d0da413cf3e9f1b195d82270917566546ff62237f5ca92e3a5ba35 source_ref=0eace8ba1bfe42022eaa1c2bfa10076fcf325f1c -->
## `_is_retryable(exc: BaseException) -> bool`

Return `True` if the exception warrants a retry attempt.

- Retryable: `RateLimitError`, `InternalServerError`, `APITimeoutError`.
- All other exceptions (4xx auth/permission/bad-request) return `False`.
<!-- trie:end -->

<!-- trie:section symbol=trie/models:_backoff_delay fingerprint=5950207d3623ac55ea4283316d2680809dfe5b7829c612db3d43ed159842bb61 body_fp=88d867a5e33860067ed84015bfc91cc1d842733d8a8984aefd260021f2f49911 source_ref=0eace8ba1bfe42022eaa1c2bfa10076fcf325f1c -->
## `_backoff_delay(*, attempt: int, base: float, cap: float, rng: random.Random) -> float`

Compute a full-jitter exponential backoff delay in seconds.

- `attempt`: 0-indexed retry count; first retry passes `0`.
- Returns `uniform(0, min(cap, base * 2**attempt))`.
<!-- trie:end -->

<!-- trie:section symbol=trie/models:_run_with_retry fingerprint=edc8f1f69cedccb9b4ecb226edf659e7f32eb54383f1d9b143138b7b01221b32 body_fp=c1b3a9f76462c180024627c4ef9934f2941e7c7b16d25688d29d6f0cdaaeee0d source_ref=0eace8ba1bfe42022eaa1c2bfa10076fcf325f1c -->
## `_run_with_retry(fn: Callable[[], T], *, cfg: Sync, kind: str, model_id: str, sleep: Callable[[float], None] = time.sleep, rng: random.Random | None = None) -> T`

Invoke `fn`, retrying on rate-limit, overloaded, or timeout errors with configurable backoff.

- `fn`: zero-argument callable whose return value is passed through on success.
- `cfg`: controls `max_retries`, `retry_base_delay_seconds`, and `retry_cap_seconds`.
- `kind`: label attached to emitted `model_call_retry` telemetry events.
- `rng`: seeded `Random` instance; a fresh one is created when `None`.
- Respects `retry-after` header on 429; falls back to exponential backoff with full jitter.
- Raises the last exception after `cfg.max_retries` attempts are exhausted.
<!-- trie:end -->