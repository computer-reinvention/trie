---
trie_version: 0.1.5
source: trie/models.py
file_fingerprint: 5431a1a9cf40cacc822e4787179c1c0b411d187b8aba8fbf3c6b6ea16804554d
last_synced_at: '2026-05-28T14:27:04Z'
defines:
- kind: module
  qualified_name: trie/models:__module__
  lines: 1-315
- kind: class
  qualified_name: trie/models:SectionBody
  lines: 28-30
- kind: class
  qualified_name: trie/models:MergeNotesOutput
  lines: 33-37
- kind: class
  qualified_name: trie/models:SymbolEdit
  lines: 40-44
- kind: class
  qualified_name: trie/models:SymbolProse
  lines: 47-51
- kind: class
  qualified_name: trie/models:FileEdit
  lines: 54-58
- kind: class
  qualified_name: trie/models:CallerDecision
  lines: 61-67
- kind: class
  qualified_name: trie/models:BatchFilterOutput
  lines: 70-73
- kind: class
  qualified_name: trie/models:FixupOutput
  lines: 76-78
- kind: class
  qualified_name: trie/models:ModelResult
  lines: 86-117
- kind: method
  qualified_name: trie/models:ModelResult.__init__
  lines: 93-95
- kind: method
  qualified_name: trie/models:ModelResult.output
  lines: 98-99
- kind: method
  qualified_name: trie/models:ModelResult.input_tokens
  lines: 102-103
- kind: method
  qualified_name: trie/models:ModelResult.output_tokens
  lines: 106-107
- kind: method
  qualified_name: trie/models:ModelResult.cache_creation_input_tokens
  lines: 110-112
- kind: method
  qualified_name: trie/models:ModelResult.cache_read_input_tokens
  lines: 115-117
- kind: function
  qualified_name: trie/models:_retry_after_seconds
  lines: 126-136
- kind: function
  qualified_name: trie/models:_is_retryable
  lines: 139-140
- kind: function
  qualified_name: trie/models:_backoff_delay
  lines: 143-145
- kind: function
  qualified_name: trie/models:_run_with_retry
  lines: 148-197
- kind: constant
  qualified_name: trie/models:T
  lines: 200-200
- kind: constant
  qualified_name: trie/models:_MODEL_ID_ALIASES
  lines: 208-212
- kind: function
  qualified_name: trie/models:_pydantic_ai_model_id
  lines: 215-217
- kind: function
  qualified_name: trie/models:_anthropic_model_name
  lines: 220-224
- kind: class
  qualified_name: trie/models:TrieClient
  lines: 227-298
- kind: method
  qualified_name: trie/models:TrieClient.__init__
  lines: 238-248
- kind: method
  qualified_name: trie/models:TrieClient.run
  lines: 250-280
- kind: method
  qualified_name: trie/models:TrieClient.count_tokens
  lines: 282-298
- kind: function
  qualified_name: trie/models:make_client
  lines: 301-314
incoming_refs: 27
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
<!-- trie:section symbol=trie/models:SectionBody fingerprint=a04070955ec562e074e3183b2c19e0d880a3de9ab45513662522a42c935761d7 body_fp=d8dae9494bedd0b7d6c23a05c6a9b3276169afb188bc25580889a589c7122134 source_ref=9548dfb951e289478608c85e21d5016c0ebbc1a7 -->
## `SectionBody`

Pydantic model carrying the generated Markdown documentation body for one symbol.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:MergeNotesOutput fingerprint=88ee7a8f24914ccaa2c1f516d5280519243c5c7c08ee77186fa40ebb85986a90 body_fp=07010be8dd035ca7c7e5ebdc85027f68542d302757c95a4a99304a7882eea0bc source_ref=9548dfb951e289478608c85e21d5016c0ebbc1a7 -->
## `MergeNotesOutput`

Structured output model carrying deduplicated patch notes and their justifications.

- `notes`: deduplicated note strings after merging
- `reasons`: explanation for each deduplication decision
<!-- trie:end -->
<!-- trie:section symbol=trie/models:SymbolEdit fingerprint=57dd52b0d94825f3f668f3b1bfddd8bab7a14c45b43099c5f0ae6ab55384d356 body_fp=6cf64ef39822fc8a9e3c34423dafa95cef2908ba62d749769dc8312af70864f0 source_ref=9548dfb951e289478608c85e21d5016c0ebbc1a7 -->
## `class SymbolEdit(BaseModel)`

Pydantic model holding updated source code and documentation prose for a single symbol.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:SymbolProse fingerprint=b7673717906ca3a3e22cb36409bfa01b9388954c8bdafa7dd74be9adc5eb8334 body_fp=c98b23b071df7d3437df3a80c399b47d5ca40fd1c668d437a73965b41c6b61f1 source_ref=9548dfb951e289478608c85e21d5016c0ebbc1a7 -->
## `class SymbolProse(BaseModel)`

Pair a qualified symbol name with its documentation prose inside a `FileEdit`.

- `qname`: fully-qualified symbol name this prose describes.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:FileEdit fingerprint=18c6fde126dda842b172894a1d7969bffd6979a42427ef73a00befd2c1624c94 body_fp=28420e308442a0f0183e1054f9ff37c713090f549bb9c5f205f5689a2a7089ff source_ref=9548dfb951e289478608c85e21d5016c0ebbc1a7 -->
## `FileEdit`

Structured output model carrying updated file source and per-symbol prose entries.

- `prose`: one `SymbolProse` entry per modified symbol in the file.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:CallerDecision fingerprint=46e38341622b99ce0e28e749efbcd233a39dc0623e5ee3987b3cf5c46a8d3c18 body_fp=e369fa42db88717044fcfa32dd71fe7645a8c632fca875c67ff9193508e796a9 source_ref=9548dfb951e289478608c85e21d5016c0ebbc1a7 -->
## `CallerDecision`

Pydantic model representing a propagation decision for one callee→caller relationship.

- `action`: defaults to `"skip"`; expected values include `"skip"` or an update directive.
- `note`: optional human-readable annotation attached to the decision.
- `reason`: optional explanation for the chosen action.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:BatchFilterOutput fingerprint=a10dc059026469f9d748967d905a59299348a85f3d255cb47a79d9948a9455f5 body_fp=a00cbac363ca7e0e62c86c6e53472f31e33ea909d707b3dd27d383ef18f7a4ad source_ref=9548dfb951e289478608c85e21d5016c0ebbc1a7 -->
## `BatchFilterOutput`

Aggregate all `CallerDecision` results for a batch of callee→caller pairs.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:FixupOutput fingerprint=c316347f4b7a219db220fbf75660ccfe74b7cd20c5798bf4b17b5870cea277a0 body_fp=5f7c7374411451528cf66426ed18328da3d5f5ffbf19958cb12b397295436f38 source_ref=9548dfb951e289478608c85e21d5016c0ebbc1a7 -->
## `FixupOutput`

Structured output holding corrected file content returned after a diagnostics fixup pass.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:ModelResult fingerprint=944e7a67fb921e06cfb00b9fdcc9087d211425e780245f8b9e055d1c8267ea8b body_fp=7865b6a69c2be3f1166f95f92f9dd189f2e4fca8425922a3cd77aedb72e5e370 source_ref=9548dfb951e289478608c85e21d5016c0ebbc1a7 -->
## `class ModelResult`

Wrap a structured Pydantic model output together with Anthropic token usage counters.

- `output`: the validated Pydantic model returned by the agent.
- `cache_creation_input_tokens`: extracted from `usage.details`; returns `0` if absent.
- `cache_read_input_tokens`: extracted from `usage.details`; returns `0` if absent.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:ModelResult.__init__ fingerprint=146d3b3c6c2599af53357ed723ae6a33d43fffa4ffd45827f8701b2f0a908133 body_fp=3a6010733f08c83dc3f22f80e9281213d0d0c52f5db1568f6db19f18c7b715e7 source_ref=9548dfb951e289478608c85e21d5016c0ebbc1a7 -->
## `ModelResult.__init__(self, output: BaseModel, usage: Usage) -> None`

Initialise a `ModelResult` with a structured Pydantic output and its associated token usage.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:ModelResult.output fingerprint=b42bf4ac160d131fa9fd50d941884f90328324a5719e9825e955198377283293 body_fp=3e6dd34c329a7f3efcbc614a0017f7afe3dbf80c00670400ea73bd789ee2dd58 source_ref=9548dfb951e289478608c85e21d5016c0ebbc1a7 -->
## `ModelResult.output`

The structured Pydantic model instance returned by the LLM call.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:ModelResult.input_tokens fingerprint=a1b024dca62986b05239ba3a557a6a77cb6716142f9187eb02245c2c084fc341 body_fp=b46a5edff9c787fcc7e2d9ed38062cc6dd29c720b901667f875339bc1bdbe319 source_ref=9548dfb951e289478608c85e21d5016c0ebbc1a7 -->
## `ModelResult.input_tokens`

Number of input tokens reported by the model usage for this `ModelResult`.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:ModelResult.output_tokens fingerprint=b6a524062960a03daf7217df2a7f2a3978267a80402019e11007fa11e0a04fec body_fp=eed357a3cf880c07453c302c94e5fd96433d11cfc97c16607a75530ae54a3bd0 source_ref=9548dfb951e289478608c85e21d5016c0ebbc1a7 -->
## `ModelResult.output_tokens`

Number of output tokens from the `ModelResult` usage counters.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:ModelResult.cache_creation_input_tokens fingerprint=c412d39b13ce5aa8095b9c6acdf17de80fd32005bb29c200e9d44aaccdfa1ccc body_fp=3f3037f066f22c3b40ea250e3eb7bc637b9e47f4d1fbff512e8ea26aab1b15c9 source_ref=9548dfb951e289478608c85e21d5016c0ebbc1a7 -->
## `ModelResult.cache_creation_input_tokens`

Token count for newly created prompt-cache entries in this `ModelResult`'s usage.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:ModelResult.cache_read_input_tokens fingerprint=c6401a552c228d7d6a73e44517e411117af40bfb71c63e0df7e1edf3bc5b22df body_fp=21740ad8228add36ec7c8e91d9f90fdc56fedc00623ce592b2e5158b772aa6aa source_ref=9548dfb951e289478608c85e21d5016c0ebbc1a7 -->
## `ModelResult.cache_read_input_tokens`

Number of prompt-cache-read input tokens from the `ModelResult` usage details, defaulting to 0.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_retry_after_seconds fingerprint=eea4acb8b1e16f87411463e5b36f7296696e1226574047bf6b26e59be639801c body_fp=df67e5051cb47921efaad0e66e30026b1a216fc5212409765f0fb04d1fa106a4 source_ref=9548dfb951e289478608c85e21d5016c0ebbc1a7 -->
## `_retry_after_seconds(exc: APIStatusError) -> float | None`

Parse the `retry-after` header from a 429 `APIStatusError` and return the delay in seconds.

- Returns `None` if the header is absent, unparseable, or `exc` has no `response`.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_is_retryable fingerprint=3102381eafa779dde25bd3c1b78f96c2a221ecf27d9293d304a187bd683db7e9 body_fp=5921869b6042edc7ba9299daa67b80e5927ace3ff9ce2be308514f71e86c7d32 source_ref=9548dfb951e289478608c85e21d5016c0ebbc1a7 -->
## `_is_retryable(exc: BaseException) -> bool`

Return `True` if the exception warrants a retry attempt in the retry loop.

- `RateLimitError`, `InternalServerError`, `APITimeoutError`: retryable; all other exceptions are not.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_backoff_delay fingerprint=77f4e3c66b993cc965f7254cdc34761c6af37a46bcee27228820a1f4647a0475 body_fp=ad02af1066595c26b85402a203b579b2ceda9bde68d53119d84bc1463a65e4ec source_ref=9548dfb951e289478608c85e21d5016c0ebbc1a7 -->
## `_backoff_delay(*, attempt: int, base: float, cap: float, rng: random.Random) -> float`

Compute a jittered exponential backoff delay in seconds.

- `attempt`: 0-indexed retry count; delay grows as `base * 2**attempt`, capped at `cap`.
- Returns `uniform(0, min(cap, base * 2**attempt))` to prevent thundering-herd.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_run_with_retry fingerprint=1f73637cad1c2281d26eaecd1c1730346db5df3a12e9f483704db5bddb25d204 body_fp=7cda17fe931ac47c662aa11bba30920c9211598807c22d32d6317c5ffb90c50f source_ref=9548dfb951e289478608c85e21d5016c0ebbc1a7 -->
## `_run_with_retry(fn, *, cfg, kind, model_id, sleep=time.sleep, rng=None) -> T`

Invoke `fn`, retrying on rate-limit, overloaded, and timeout errors with bounded exponential backoff.

- `fn`: zero-argument callable whose return value is passed through on success.
- `cfg`: controls `max_retries`, `retry_base_delay_seconds`, and `retry_cap_seconds`.
- `kind`: label stamped into each `model_call_retry` telemetry event.
- `sleep`: injectable for testing; defaults to `time.sleep`.
- Honours `retry-after` headers on 429; falls back to full-jitter backoff otherwise.
- Re-raises immediately on non-retryable exceptions or after `cfg.max_retries` attempts.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:T fingerprint=511f85b873237a1963584329b2ded56f290efb33b59ff4f1f52a3ff84742f48d body_fp=497c5aff3784f7d37f510faf0b4066044f1ccb0ee3ef046f216bfda416430748 source_ref=9548dfb951e289478608c85e21d5016c0ebbc1a7 -->
## `T = Any`

Type alias placeholder used by `_run_with_retry`; previously a `TypeVar`, now `Any`, losing generic return-type inference.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_MODEL_ID_ALIASES fingerprint=d436771cb40ad6b40d58029730c3e289ab040b962b73ae7492868749c08d6618 body_fp=37e1f5504d10ae606c50f55d425859a6b5dfd353c2fa9af2e70a590a5adb6c3d source_ref=9548dfb951e289478608c85e21d5016c0ebbc1a7 -->
## `_MODEL_ID_ALIASES: dict[str, str]`

Maps trie's `provider/model` model ID format to pydantic_ai's `provider:model` format.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_pydantic_ai_model_id fingerprint=a0a6b3d1a8febf77bc636de899705a5808a8091b4f9ec907ce9d9611400a53ec body_fp=04e4e1e07ef49589aad0f012039eb857c14047b118bb65b424c5aeab8c0646f2 source_ref=9548dfb951e289478608c85e21d5016c0ebbc1a7 -->
## `_pydantic_ai_model_id(full_model_id: str) -> str`

Convert a `provider/model` model ID to pydantic_ai's `provider:model` format, consulting `_MODEL_ID_ALIASES` first.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_anthropic_model_name fingerprint=3c87d22ca61cada7c6dd2721cf27ba2000942a7010fc3dac57aeb0cd6ca74261 body_fp=768951d46b2c4bf2b651994e5d602cdcd72ef1834967c30c4f384c3efe488622 source_ref=9548dfb951e289478608c85e21d5016c0ebbc1a7 -->
## `_anthropic_model_name(full_model_id: str) -> str`

Extract the bare Anthropic model name by stripping the `provider/` prefix from a trie model ID.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:TrieClient fingerprint=5cdb3d02e1c48b5adc7847660d9dad80f0099660d6b0e0ca8b99121031335d79 body_fp=c3593157b550eaf7d2f15c463bb9b9b8552fc5227cf11de24ecfe3837954bfc8 source_ref=9548dfb951e289478608c85e21d5016c0ebbc1a7 -->
## `TrieClient(full_model_id: str, *, sync_cfg: Sync | None = None)`

Pydantic AI-powered LLM client for structured generation and token counting against Anthropic models.

- `full_model_id`: `provider/model` string, e.g. `anthropic/claude-sonnet-4-6`
- `sync_cfg`: retry/backoff settings; defaults to `Sync()` if omitted
- `run()`: creates a one-shot `Agent`, returns `ModelResult` with typed output and usage
- `count_tokens()`: hits the Anthropic count-tokens endpoint (no generation, no cost)
<!-- trie:end -->
<!-- trie:section symbol=trie/models:TrieClient.__init__ fingerprint=d18769f0cb06543ec3c26c27f3b81d9e8968f2fa1afef104dd869c06719801d8 body_fp=96baaa45847ab58206cb13c2063de9041f7819c8e266a0d3bb3f090bf7f33bc9 source_ref=9548dfb951e289478608c85e21d5016c0ebbc1a7 -->
## `TrieClient.__init__(self, full_model_id: str, *, sync_cfg: Sync | None = None) -> None`

Initialise a `TrieClient`, deriving pydantic-ai and raw Anthropic model identifiers from `full_model_id`.

- `full_model_id`: `provider/model` string, e.g. `anthropic/claude-sonnet-4-6`.
- `sync_cfg`: retry/backoff config; defaults to `Sync()` if omitted.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:TrieClient.run fingerprint=e39e69443a8a140e30cbef4aa0f86e4dfc4ca2bc5170f7bfb24f32e573fe6357 body_fp=059f0e5c5d4c0bb829b8a6839d595ee0435cebfd3c470b299b93e2c354a7c16c source_ref=9548dfb951e289478608c85e21d5016c0ebbc1a7 -->
## `TrieClient.run(self, output_type, system_prompt, user_prompt, *, max_tokens=1024) -> ModelResult`

Create a one-shot `Agent` and invoke it synchronously, returning validated structured output with token usage.

- `output_type`: Pydantic model class used as the agent's `output_type`.
- `system_prompt`: set on the agent; eligible for Anthropic prompt caching.
- `user_prompt`: sent as the user message to `agent.run_sync`.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:TrieClient.count_tokens fingerprint=47db757d38476c0f0fed949532da821489dbca03af8bfafd52c2f9a916d7d06a body_fp=617b144ce825749b79f1a5c459771ab8effc14b305e83e2ad87327da79a5d108 source_ref=9548dfb951e289478608c85e21d5016c0ebbc1a7 -->
## `TrieClient.count_tokens(self, system_prompt: str, user_prompt: str) -> int`

Call the Anthropic `count_tokens` endpoint to estimate prompt size without generating output.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:make_client fingerprint=3357d2c90a369504b954bcdaeda5dc66234fd60cb89e23082eda6f4ddc882612 body_fp=34db6e52e084570717d81814201143294d06f4e1b90a22728117958b2d366a9e source_ref=9548dfb951e289478608c85e21d5016c0ebbc1a7 -->
## `make_client(model_id: str, *, sync_cfg: Sync | None = None) -> TrieClient`

Construct a `TrieClient` from a `"provider/model"` string; only `anthropic/` is supported.

- `model_id`: must have the form `"provider/model"` — raises `ValueError` otherwise.
- `sync_cfg`: retry knobs; defaults to `Sync()` when omitted.
- Raises `NotImplementedError` for any provider other than `anthropic`.
<!-- trie:end -->