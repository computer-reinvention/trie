---
trie_version: 0.1.0
source: trie/models.py
file_fingerprint: f9f6bbe69c2c96fdd7486115feea561f00ae6b58096e1c8fdf5cf6557c145dce
last_synced_at: '2026-05-16T10:51:54Z'
defines:
- kind: class
  qualified_name: trie/models:GenerationRequest
  lines: 24-31
- kind: class
  qualified_name: trie/models:GenerationResponse
  lines: 35-40
- kind: class
  qualified_name: trie/models:ModelClient
  lines: 43-48
- kind: method
  qualified_name: trie/models:ModelClient.generate
  lines: 46-46
- kind: method
  qualified_name: trie/models:ModelClient.count_tokens
  lines: 48-48
- kind: function
  qualified_name: trie/models:_retry_after_seconds
  lines: 51-66
- kind: function
  qualified_name: trie/models:_is_retryable
  lines: 69-77
- kind: function
  qualified_name: trie/models:_backoff_delay
  lines: 80-94
- kind: function
  qualified_name: trie/models:_run_with_retry
  lines: 97-157
- kind: class
  qualified_name: trie/models:AnthropicClient
  lines: 160-241
- kind: method
  qualified_name: trie/models:AnthropicClient.__init__
  lines: 161-173
- kind: method
  qualified_name: trie/models:AnthropicClient._payload
  lines: 175-198
- kind: method
  qualified_name: trie/models:AnthropicClient.generate
  lines: 200-224
- kind: method
  qualified_name: trie/models:AnthropicClient.count_tokens
  lines: 226-241
- kind: function
  qualified_name: trie/models:make_client
  lines: 244-262
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

<!-- trie:section symbol=trie/models:ModelClient fingerprint=81529832a0d7a426971ab9d6b942c3a06c74067ec5af261fa1dcface3bf7a86d body_fp=5065cfd41539ba717c02cd2f3aef91ba6f836149f4f7ded4478979f684d872cb source_ref=e12e23ef268599c29347001c72ed8323b67a45bd -->
## `class ModelClient(Protocol)`

Structural protocol defining the interface any model client must satisfy.

- `model_id`: string identifier for the model being used
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

<!-- trie:section symbol=trie/models:AnthropicClient fingerprint=4a7a6aafb7628bfd34b5f6d8735668e722e81c121cbc81b4a3963e9ffd61ff2c body_fp=f31b8ea93cd93f45144b122f9a06d7b4bfe36dbd0685599a9f26128064d7e78b source_ref=0eace8ba1bfe42022eaa1c2bfa10076fcf325f1c -->
## `AnthropicClient(model_id: str, *, client: Anthropic | None = None, sync_cfg: Sync | None = None)`

Wrap the Anthropic Messages API to implement `ModelClient` with prompt-caching support and configurable retry behaviour.

- `model_id`: bare model name (without `anthropic/` prefix).
- `client`: injectable `Anthropic` instance; creates one with `max_retries=0` if omitted.
- `sync_cfg`: retry knobs (max attempts, backoff bounds); defaults to `Sync()` defaults.
<!-- trie:end -->

<!-- trie:section symbol=trie/models:AnthropicClient.generate fingerprint=758851da76b59aa834ad142c0482508de371025699a5c7e816ccdee5cccdb3de body_fp=a820616b0e562eea6c5d2cef05c91bba88653bba95a637bd3cdddbaa4072c56a source_ref=0eace8ba1bfe42022eaa1c2bfa10076fcf325f1c -->
## `generate(self, req: GenerationRequest) -> GenerationResponse`

Call the Anthropic messages API with retry logic, record telemetry, and return token usage with generated text.

- `req.max_tokens`: caps output length; passed directly to `messages.create`.
- Returns concatenated text from all `text`-type content blocks.
- Retries on rate-limit, server error, and timeout per `self._sync_cfg`.
<!-- trie:end -->

<!-- trie:section symbol=trie/models:AnthropicClient.count_tokens fingerprint=10285a7e87dbcd4ad78eb5971b5350b6d31ef2a2ccd6059dcb6c4987fc229db2 body_fp=c834ed496c7a7adc0682d438aacaa366111b8b6e19386686490c33f8361fbe3d source_ref=0eace8ba1bfe42022eaa1c2bfa10076fcf325f1c -->
## `count_tokens(self, req: GenerationRequest) -> int`

Return the input token count for `req` using the Anthropic token-counting API, with retry on rate-limit/overload/timeout errors.

- Returns the exact token count for the full payload (system + cached context + request), not a heuristic.
- Retries honour `retry-after` headers and exponential backoff per `self._sync_cfg`.
<!-- trie:end -->

<!-- trie:section symbol=trie/models:make_client fingerprint=12dc0080bffbf3920b3d2734b137bc532a0db1567ea00f8b25dfd3af8400ab86 body_fp=5cb7649cfd32ecb52ca698fbf5666aeaf91cd1819516a36be8ffe65172438841 source_ref=0eace8ba1bfe42022eaa1c2bfa10076fcf325f1c -->
## `make_client(model_id: str, *, sync_cfg: Sync | None = None) -> ModelClient`

Construct a `ModelClient` from a `"provider/model"` string, returning an `AnthropicClient` for the `anthropic/` provider.

- `model_id`: must contain `/`; only `"anthropic/<model>"` is supported.
- `sync_cfg`: retry knobs forwarded to the client; defaults to `Sync()` when omitted.
- Raises `ValueError` if no `/` present.
- Raises `NotImplementedError` for any provider other than `"anthropic"`.
<!-- trie:end -->

<!-- trie:section symbol=trie/models:AnthropicClient.__init__ fingerprint=cab5f6668a9d454606c3eda866dd9f2fad3e685c8208c8c4644a59c35fa21a7b body_fp=7f7f18c08013d2f5b356ae16f9560d93aabeead6b1149b14c15be3f54f0e3256 source_ref=0eace8ba1bfe42022eaa1c2bfa10076fcf325f1c -->
## `AnthropicClient.__init__(self, model_id: str, *, client: Anthropic | None = None, sync_cfg: Sync | None = None) -> None`

Initialize an `AnthropicClient`, creating a default `Anthropic` SDK client (with `max_retries=0`) and retry config if none are provided.

- `sync_cfg`: controls retry knobs; defaults to `Sync()` when omitted.
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