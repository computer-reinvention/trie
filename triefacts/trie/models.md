---
trie_version: 0.1.5
source: trie/models.py
file_fingerprint: c2a0f985eef9e000ac255cf153cc320b990793829ad1f4ca5e7e3f6c2ff0d690
last_synced_at: '2026-06-03T21:13:43Z'
defines:
- kind: module
  qualified_name: trie/models:__module__
  lines: 1-408
- kind: constant
  qualified_name: trie/models:_thread_local
  lines: 32-32
- kind: function
  qualified_name: trie/models:_thread_event_loop
  lines: 35-40
- kind: class
  qualified_name: trie/models:SectionBody
  lines: 49-86
- kind: class
  qualified_name: trie/models:MergeNotesOutput
  lines: 89-93
- kind: class
  qualified_name: trie/models:SymbolEdit
  lines: 96-100
- kind: class
  qualified_name: trie/models:SymbolProse
  lines: 103-107
- kind: class
  qualified_name: trie/models:FileEdit
  lines: 110-114
- kind: class
  qualified_name: trie/models:CallerDecision
  lines: 117-123
- kind: class
  qualified_name: trie/models:BatchFilterOutput
  lines: 126-129
- kind: class
  qualified_name: trie/models:FixupOutput
  lines: 132-135
- kind: class
  qualified_name: trie/models:ModelResult
  lines: 143-174
- kind: method
  qualified_name: trie/models:ModelResult.__init__
  lines: 150-152
- kind: method
  qualified_name: trie/models:ModelResult.output
  lines: 155-156
- kind: method
  qualified_name: trie/models:ModelResult.input_tokens
  lines: 159-160
- kind: method
  qualified_name: trie/models:ModelResult.output_tokens
  lines: 163-164
- kind: method
  qualified_name: trie/models:ModelResult.cache_creation_input_tokens
  lines: 167-169
- kind: method
  qualified_name: trie/models:ModelResult.cache_read_input_tokens
  lines: 172-174
- kind: function
  qualified_name: trie/models:_retry_after_seconds
  lines: 183-193
- kind: function
  qualified_name: trie/models:_is_retryable
  lines: 196-197
- kind: function
  qualified_name: trie/models:_backoff_delay
  lines: 200-202
- kind: function
  qualified_name: trie/models:_run_with_retry
  lines: 205-254
- kind: constant
  qualified_name: trie/models:T
  lines: 257-257
- kind: constant
  qualified_name: trie/models:_MODEL_ID_ALIASES
  lines: 265-269
- kind: function
  qualified_name: trie/models:_pydantic_ai_model_id
  lines: 272-274
- kind: function
  qualified_name: trie/models:_anthropic_model_name
  lines: 277-281
- kind: class
  qualified_name: trie/models:TrieClient
  lines: 284-391
- kind: method
  qualified_name: trie/models:TrieClient.__init__
  lines: 295-305
- kind: method
  qualified_name: trie/models:TrieClient.run
  lines: 307-366
- kind: method
  qualified_name: trie/models:TrieClient.count_tokens
  lines: 368-391
- kind: function
  qualified_name: trie/models:make_client
  lines: 394-407
incoming_refs: 71
outgoing_refs: 6
---
<!-- trie:section symbol=trie/models:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=9b387fda13f0c60ba17cbe1d813fca36e81accdb48ac1477cbbc51fd87ee73ba source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 -->
Provides LLM client infrastructure with structured output models and retry logic for trie documentation generation.

- SectionBody, SymbolEdit, FileEdit: Pydantic models for structured LLM outputs
- TrieClient: Agent factory wrapping pydantic-ai with prompt caching and retry handling
- ModelResult: Wrapper combining structured output with token usage counters
- Per-thread event loop management to prevent file descriptor leaks in parallel execution
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_thread_local fingerprint=75569d7b1b6c68e79f0dea5d5361a3b4eee93cb9a73570765a3f2ede6ca769e0 body_fp=fd490c0b1ea42acca479054ee3666f11d574aa7e09d1b8f93db04b5035d45872 source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 -->
Thread-local storage for per-thread event loops to prevent file descriptor leaks in parallel execution.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_thread_event_loop fingerprint=4d7ceb4962f72daf7b413e923780ae966597ef2c58cd59e2e52b3251b4c2004c body_fp=e11ebe66b5eefa1002dd5523a6b0fd345ff7cba713912de43fe51f870be04ff3 source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 -->
Returns a persistent event loop for the current thread, creating one if none exists or the existing one is closed.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:SectionBody fingerprint=f1c4c6eb19f0882dbf14ae82cd52931932109942e91db24865048776cea2d292 body_fp=0c65a7225c02dfb22172000eacfcb9790dcc05de641b3e7c350440d71083a623 source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 -->
Pydantic model representing triefact documentation output with architectural classification.

- `body`: markdown documentation text for the symbol
- `role`: architectural function tag (entrypoint, api, domain, etc.) with detailed standard vocabulary
- `boundary`: system boundary position (entry, exit, internal) based on external interaction patterns
<!-- trie:end -->
<!-- trie:section symbol=trie/models:MergeNotesOutput fingerprint=88ee7a8f24914ccaa2c1f516d5280519243c5c7c08ee77186fa40ebb85986a90 body_fp=2178661683f1b041f43c2d9e53bb7720bdc21bbceab3a500a90eb59e3ef8a27e source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 -->
Pydantic model containing deduplicated patch notes and their reasons.

- `notes`: list of deduplicated patch note strings
- `reasons`: explanations for why notes were deduplicated or modified
<!-- trie:end -->
<!-- trie:section symbol=trie/models:SymbolEdit fingerprint=57dd52b0d94825f3f668f3b1bfddd8bab7a14c45b43099c5f0ae6ab55384d356 body_fp=62c4bfadbdc802dd7409e8b1a85bd25e3b1b0017558ceeabd96d6a289ef75acf source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 -->
Pydantic model containing updated source code and documentation prose for a single symbol.

- `source`: The modified source code text
- `prose`: The generated documentation text
<!-- trie:end -->
<!-- trie:section symbol=trie/models:SymbolProse fingerprint=b7673717906ca3a3e22cb36409bfa01b9388954c8bdafa7dd74be9adc5eb8334 body_fp=0d300db78b96e71ada0dd11e07184ec8aabe40b94082b9b861b90e0e6458d6f1 source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 -->
Holds qualified name and prose for a single symbol within a multi-symbol file edit.

- `qname`: qualified name identifier of the symbol
- `prose`: documentation text content for the symbol
<!-- trie:end -->
<!-- trie:section symbol=trie/models:FileEdit fingerprint=18c6fde126dda842b172894a1d7969bffd6979a42427ef73a00befd2c1624c94 body_fp=8b1ef6ab01b141a7aeda9537a98d505feae0c618cd386e4ddcd069f10be54d92 source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 -->
Pydantic model for updated file content paired with prose documentation for each symbol.

- `content`: The modified file source code
- `prose`: List of symbol-specific documentation entries
<!-- trie:end -->
<!-- trie:section symbol=trie/models:CallerDecision fingerprint=46e38341622b99ce0e28e749efbcd233a39dc0623e5ee3987b3cf5c46a8d3c18 body_fp=0c6b553fbd53637897a908bf05845d110ad190859b08c7b43b60a45958d2703b source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 -->
Represents a decision for one callee→caller relationship in batch filtering operations.

- `action`: defaults to "skip"
- `note`: optional additional information
- `reason`: optional explanation for the decision
<!-- trie:end -->
<!-- trie:section symbol=trie/models:BatchFilterOutput fingerprint=a10dc059026469f9d748967d905a59299348a85f3d255cb47a79d9948a9455f5 body_fp=a4dde2e8fb5eff963bc94271b5e4ca60d9dbef0620027dc790a712dccd90144f source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 -->
Pydantic model containing a list of CallerDecision objects for batch filtering of callee-caller relationships.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:FixupOutput fingerprint=c316347f4b7a219db220fbf75660ccfe74b7cd20c5798bf4b17b5870cea277a0 body_fp=5d2a863fa6c16e748a081c54dc6522d1e366bcdeaf1fca96a4eac37810a3b01a source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 -->
Pydantic model containing corrected file content after diagnostic processing.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:ModelResult fingerprint=944e7a67fb921e06cfb00b9fdcc9087d211425e780245f8b9e055d1c8267ea8b body_fp=99a810d0650166cf9dfec1e6519258c92bfddffbfc3d5473d60c20996e5cf135 source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 -->
ModelResult wraps structured Pydantic output with token usage counters from LLM calls.

• `output` — the structured Pydantic model returned by the agent
• `cache_creation_input_tokens` — tokens used to create new cache entries
• `cache_read_input_tokens` — tokens read from existing cache entries
<!-- trie:end -->
<!-- trie:section symbol=trie/models:ModelResult.__init__ fingerprint=146d3b3c6c2599af53357ed723ae6a33d43fffa4ffd45827f8701b2f0a908133 body_fp=942c4d753b1786d9156f7a91801c7db40478afbe8233b5be486a974f7d8355d1 source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 -->
Initializes a ModelResult with structured output and usage statistics.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:ModelResult.output fingerprint=b42bf4ac160d131fa9fd50d941884f90328324a5719e9825e955198377283293 body_fp=485395b9293751519287116f50aa9cc9dae24d55bd8b71d7f14b501a6a6ac9d2 source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 -->
Returns the structured Pydantic model output from ModelResult.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:ModelResult.input_tokens fingerprint=a1b024dca62986b05239ba3a557a6a77cb6716142f9187eb02245c2c084fc341 body_fp=22feedb8cce7ae2add5e58dcfea9d3267ac36d28035a5838ea566f87fe796448 source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 -->
Returns input token count from ModelResult's usage data.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:ModelResult.output_tokens fingerprint=b6a524062960a03daf7217df2a7f2a3978267a80402019e11007fa11e0a04fec body_fp=6788e507a215020037654be94b6b143fcf5af911e1030c8ca98a60730c9f3365 source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 -->
Returns the number of output tokens from the ModelResult's usage statistics.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:ModelResult.cache_creation_input_tokens fingerprint=c412d39b13ce5aa8095b9c6acdf17de80fd32005bb29c200e9d44aaccdfa1ccc body_fp=33aa44bfaba7158d2ba9d38d5e401d595182aaf999c173a4a48522d16de0a467 source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 -->
Returns ModelResult's cache creation input token count from usage details, defaulting to zero.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:ModelResult.cache_read_input_tokens fingerprint=c6401a552c228d7d6a73e44517e411117af40bfb71c63e0df7e1edf3bc5b22df body_fp=56fbf6fafcf4104b9902c71779ec43267b051d5ffe7cf32772650a13bd169348 source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 -->
Returns the number of input tokens read from cache during ModelResult generation.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_retry_after_seconds fingerprint=eea4acb8b1e16f87411463e5b36f7296696e1226574047bf6b26e59be639801c body_fp=5400da1da68ecff033d8015e310ecf6ae1eb1f77d67ed65dbf8154f4d90d88ae source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 -->
Extracts the retry delay in seconds from an APIStatusError's retry-after header, returning None if unavailable or invalid.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_is_retryable fingerprint=3102381eafa779dde25bd3c1b78f96c2a221ecf27d9293d304a187bd683db7e9 body_fp=60c831a3cfe4324799d6eaafc47a1aced01594a4e73150e4c6db47ad7592ac93 source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 -->
Returns True if the exception is retryable (rate limit, internal server error, or timeout).
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_backoff_delay fingerprint=77f4e3c66b993cc965f7254cdc34761c6af37a46bcee27228820a1f4647a0475 body_fp=db499c0114246d369fa21a973c4cc466d777071d1f99d8535ad718efe61464f4 source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 -->
Calculates exponential backoff delay with jitter, returning a random duration between zero and the capped window.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_run_with_retry fingerprint=1f73637cad1c2281d26eaecd1c1730346db5df3a12e9f483704db5bddb25d204 body_fp=cafd3a5922db59b734b54de48ef860147f7595cafc2c321fa3a01f9b5b9bcb47 source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 -->
Executes a callable with exponential backoff retry logic for rate limits, timeouts, and server errors.

- Respects `retry-after` headers for rate limit exceptions
- Emits telemetry events on each retry attempt with delay and reason
- Stops retrying after `cfg.max_retries` attempts or non-retryable exceptions
<!-- trie:end -->
<!-- trie:section symbol=trie/models:T fingerprint=511f85b873237a1963584329b2ded56f290efb33b59ff4f1f52a3ff84742f48d body_fp=d54080f28b388848817988e57cc93775750bb1d46b147449f3fe09535a32e6c4 source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 -->
Type alias for Any used as a TypeVar placeholder in the retry helper function.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_MODEL_ID_ALIASES fingerprint=d436771cb40ad6b40d58029730c3e289ab040b962b73ae7492868749c08d6618 body_fp=5d9fcbfd1b775034361a99f4fae78c8a73ef555ffd4c78064d2c8488d9f2c319 source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 -->
Maps trie's `provider/model` format to pydantic_ai's `provider:model` format for model ID conversion.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_pydantic_ai_model_id fingerprint=a0a6b3d1a8febf77bc636de899705a5808a8091b4f9ec907ce9d9611400a53ec body_fp=3de559806ca1742ec8f60138929d9d4db6171d99971d8b00a183783b63e33a6f source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 -->
Converts trie's provider/model format to pydantic_ai's provider:model format using aliases or simple substitution.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_anthropic_model_name fingerprint=3c87d22ca61cada7c6dd2721cf27ba2000942a7010fc3dac57aeb0cd6ca74261 body_fp=9f60ebe4d744a72dcf3f42d216efade5c4613aa01f6d939ef3729a3781e6bf20 source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 -->
Extract the bare Anthropic model name from a full trie model ID by stripping the provider prefix.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:TrieClient fingerprint=62e7cfe1684440a1acdc792902342229d172d2e309783a52a9054e4f9871dd58 body_fp=54badb5facd07dd8c908c85345e3e69d6b80b7ea0def79ff64cbd622f1f705c1 source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 -->
Creates Pydantic AI agents for structured LLM output with prompt caching and token counting.

- `run()` — creates one-shot agent, executes with structured output, returns ModelResult with usage
- `count_tokens()` — estimates input tokens via Anthropic API before generation
- `cache_prefix` — caches file content prefix across symbols to reduce billing
- Uses per-thread event loop to prevent file descriptor leaks under parallelism
<!-- trie:end -->
<!-- trie:section symbol=trie/models:TrieClient.__init__ fingerprint=d18769f0cb06543ec3c26c27f3b81d9e8968f2fa1afef104dd869c06719801d8 body_fp=f2ccf6f2a7e1c9105dccdbfa5790e70f3e5f5a1b25f6db892278e2cc897bea54 source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 -->
Initializes TrieClient with model ID conversion and configuration setup.

- `full_model_id`: trie's provider/model format (e.g., "anthropic/claude-sonnet-4-6")
- `sync_cfg`: retry configuration, defaults to Sync() if None
- Creates raw Anthropic client with retries disabled (handled by wrapper)
<!-- trie:end -->
<!-- trie:section symbol=trie/models:TrieClient.run fingerprint=1a378cf2a7d48ab1f8d3177933158ab9d213d4aa88d7b8b83c35662c23f4e9d4 body_fp=2e261ba113d587a3af496103ab0db2988a4ab6214817fae0efb1ea970b33e66a source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 -->
TrieClient.run creates a pydantic-ai Agent with structured output and executes it with prompt caching optimization.

• cache_prefix: when provided, cached as a shared prefix across multiple calls for cost efficiency
• max_tokens: maximum tokens for the model output (default 1024)
• Returns ModelResult containing structured output and token usage counters
<!-- trie:end -->
<!-- trie:section symbol=trie/models:TrieClient.count_tokens fingerprint=3c0147fbfd76558d6fd2a6176f921093c72e3ac31e6c8b6ad60f9438d78015cd body_fp=d1251490fb9cbe8f30a370fbf5d4fbabc0fa9e2d49a8416658826e62690ea73b source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 -->
TrieClient.count_tokens returns the number of input tokens via the Anthropic count_tokens API for system and user prompts.

- Empty user prompts are replaced with "." to avoid API rejection while preserving cost estimation accuracy
<!-- trie:end -->
<!-- trie:section symbol=trie/models:make_client fingerprint=3357d2c90a369504b954bcdaeda5dc66234fd60cb89e23082eda6f4ddc882612 body_fp=935d0255ccbde76f44c569ac5890436fb94c87c29377089e9f51358d32c9435d source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 -->
Constructs a TrieClient from a provider/model ID string, validating format and supporting only anthropic provider.
<!-- trie:end -->