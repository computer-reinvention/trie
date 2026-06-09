---
trie_version: 0.1.5
source: trie/models.py
file_fingerprint: 1b11dd46adbef17895fb99591d4897fe75f003573690f084020647f7e8a94994
last_synced_at: '2026-06-09T09:38:34Z'
defines:
- kind: module
  qualified_name: trie/models:__module__
  lines: 1-570
- kind: class
  qualified_name: trie/models:_LoopHolder
  lines: 42-55
- kind: method
  qualified_name: trie/models:_LoopHolder.__init__
  lines: 45-46
- kind: method
  qualified_name: trie/models:_LoopHolder.__del__
  lines: 48-55
- kind: constant
  qualified_name: trie/models:_thread_local
  lines: 58-58
- kind: function
  qualified_name: trie/models:_thread_event_loop
  lines: 61-66
- kind: constant
  qualified_name: trie/models:_inflight_lock
  lines: 81-81
- kind: constant
  qualified_name: trie/models:_inflight_sem
  lines: 82-82
- kind: constant
  qualified_name: trie/models:_inflight_bound
  lines: 83-83
- kind: function
  qualified_name: trie/models:configure_inflight_limit
  lines: 86-97
- kind: function
  qualified_name: trie/models:_inflight_slot
  lines: 101-111
- kind: class
  qualified_name: trie/models:SectionBody
  lines: 120-157
- kind: class
  qualified_name: trie/models:ProposedRole
  lines: 160-175
- kind: class
  qualified_name: trie/models:RoleTaxonomy
  lines: 178-195
- kind: class
  qualified_name: trie/models:RoleTag
  lines: 198-217
- kind: class
  qualified_name: trie/models:MergeNotesOutput
  lines: 220-224
- kind: class
  qualified_name: trie/models:SymbolEdit
  lines: 227-231
- kind: class
  qualified_name: trie/models:SymbolProse
  lines: 234-238
- kind: class
  qualified_name: trie/models:FileEdit
  lines: 241-245
- kind: class
  qualified_name: trie/models:CallerDecision
  lines: 248-254
- kind: class
  qualified_name: trie/models:BatchFilterOutput
  lines: 257-260
- kind: class
  qualified_name: trie/models:FixupOutput
  lines: 263-266
- kind: class
  qualified_name: trie/models:ModelResult
  lines: 274-305
- kind: method
  qualified_name: trie/models:ModelResult.__init__
  lines: 281-283
- kind: method
  qualified_name: trie/models:ModelResult.output
  lines: 286-287
- kind: method
  qualified_name: trie/models:ModelResult.input_tokens
  lines: 290-291
- kind: method
  qualified_name: trie/models:ModelResult.output_tokens
  lines: 294-295
- kind: method
  qualified_name: trie/models:ModelResult.cache_creation_input_tokens
  lines: 298-300
- kind: method
  qualified_name: trie/models:ModelResult.cache_read_input_tokens
  lines: 303-305
- kind: function
  qualified_name: trie/models:_retry_after_seconds
  lines: 314-324
- kind: function
  qualified_name: trie/models:_is_retryable
  lines: 327-333
- kind: function
  qualified_name: trie/models:_backoff_delay
  lines: 336-338
- kind: function
  qualified_name: trie/models:_run_with_retry
  lines: 341-395
- kind: constant
  qualified_name: trie/models:T
  lines: 398-398
- kind: constant
  qualified_name: trie/models:_MODEL_ID_ALIASES
  lines: 406-410
- kind: function
  qualified_name: trie/models:_pydantic_ai_model_id
  lines: 413-415
- kind: function
  qualified_name: trie/models:_anthropic_model_name
  lines: 418-422
- kind: class
  qualified_name: trie/models:TrieClient
  lines: 425-553
- kind: method
  qualified_name: trie/models:TrieClient.__init__
  lines: 436-455
- kind: method
  qualified_name: trie/models:TrieClient.run
  lines: 457-528
- kind: method
  qualified_name: trie/models:TrieClient.count_tokens
  lines: 530-553
- kind: function
  qualified_name: trie/models:make_client
  lines: 556-569
incoming_refs: 93
outgoing_refs: 6
---
<!-- trie:section symbol=trie/models:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=9b387fda13f0c60ba17cbe1d813fca36e81accdb48ac1477cbbc51fd87ee73ba source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 role=llm-client -->
Provides LLM client infrastructure with structured output models and retry logic for trie documentation generation.

- SectionBody, SymbolEdit, FileEdit: Pydantic models for structured LLM outputs
- TrieClient: Agent factory wrapping pydantic-ai with prompt caching and retry handling
- ModelResult: Wrapper combining structured output with token usage counters
- Per-thread event loop management to prevent file descriptor leaks in parallel execution
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_LoopHolder fingerprint=51950ccfb6ff20464fa838fd0ce832c84fd2e1b83e6baee1fec7a4575c051e25 body_fp=05cecdf8ec4e05370e11a21ba504e1b95af917ad5b5868b3c44685f57a14d059 source_ref=b80d20b1306fa37c369f12494d2c4a3fff683036 role=util -->
Holds an asyncio event loop and closes it on garbage collection to prevent file descriptor leaks.

- `__del__`: closes the held event loop when the holder is garbage collected
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_LoopHolder.__init__ fingerprint=58b2c05fdd50648b7c9635b9f41d52170568b748a682cce4380d2e689ce742d0 body_fp=46e0ea68860740b2b7885bf73b4f8f5456ad63c08e026f518a98611f1a85500d source_ref=b80d20b1306fa37c369f12494d2c4a3fff683036 role=model -->
Stores the given event loop in the `_LoopHolder` instance for later cleanup.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_LoopHolder.__del__ fingerprint=4154bab67f5828c4c2f71d31907c5c88efdb25733d90de5971af60a5a433b19b body_fp=12cfb1c8ca5b4a53dc5249d73390cd48065f8dd37c310422fe8ea99c55130001 source_ref=b80d20b1306fa37c369f12494d2c4a3fff683036 role=util -->
Closes the _LoopHolder's event loop during finalisation if it exists and isn't already closed.

- Swallows all exceptions to prevent teardown of worker threads from raising
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_thread_local fingerprint=75569d7b1b6c68e79f0dea5d5361a3b4eee93cb9a73570765a3f2ede6ca769e0 body_fp=fd490c0b1ea42acca479054ee3666f11d574aa7e09d1b8f93db04b5035d45872 source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 role=llm-client -->
Thread-local storage for per-thread event loops to prevent file descriptor leaks in parallel execution.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_thread_event_loop fingerprint=2346af89d961e3da6936d0d3eeb8e2d1aa8f3cb81f2a25219d787596c8593baf body_fp=e11ebe66b5eefa1002dd5523a6b0fd345ff7cba713912de43fe51f870be04ff3 source_ref=b80d20b1306fa37c369f12494d2c4a3fff683036 role=util -->
Returns a persistent event loop for the current thread, creating one if none exists or the existing one is closed.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_inflight_lock fingerprint=0b0591e19fe812560f6db6c78c194433716b609e388f21b34daf63dcc61a9ef9 body_fp=7b3cb3945c721fb91fcaea9dffaa2e74df60e7dffe043a2bc5d121f5ea33bba0 source_ref=7b6978ad15fe0381f84e0d22885ce10437c8dfb5 role=util -->
Protects access to global inflight semaphore state during reconfiguration.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_inflight_sem fingerprint=1b10af5b4853bfeda79e44b27896d47f8b35e04865242604cebb8925cbf691bd body_fp=7328494ab6525619948eb3fbc87f0ccd3f31a9a0ea11f658e7154348bdd637b0 source_ref=7b6978ad15fe0381f84e0d22885ce10437c8dfb5 role=config -->
Global semaphore that caps concurrent LLM requests across all worker threads.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_inflight_bound fingerprint=ff1b2dc25a706dfb27a819c7aa05a832873229bf8b8f59831e8aa5641cf6a194 body_fp=15ec0eb87902109ad8c5a682930e3dd98b5ae8e18a44648a6daeb35e17abec4a source_ref=7b6978ad15fe0381f84e0d22885ce10437c8dfb5 role=config -->
Global cap on concurrent LLM requests managed by the inflight semaphore system.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:configure_inflight_limit fingerprint=d8c1b49d8dd702a33e8ca276868cc130ab8b3ba4912fa6589cdf6d50a9e1a01f body_fp=ccbba4a60812841b852a869ebbb12ad5b3a10b5a3dd999aeaed0baf559ed76d8 source_ref=7b6978ad15fe0381f84e0d22885ce10437c8dfb5 role=config -->
Set the global cap on concurrent LLM requests process-wide, creating or rebuilding the semaphore when the bound changes.

- `bound`: Maximum concurrent requests; 0 disables throttling entirely
- Idempotent: repeated calls with same bound are no-ops
- Thread-safe via global lock for use before worker fan-out
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_inflight_slot fingerprint=0d3a9686426238175caadcbca2a164cf9e7972213c335ee205811f566295a048 body_fp=0f1e9ccf03e0b908457d0980bdd831b931a234c8af7dac13722eccce5634d664 source_ref=7b6978ad15fe0381f84e0d22885ce10437c8dfb5 role=util -->
Acquires and releases one slot from the global inflight request semaphore for the duration of a network attempt.

- Yields immediately without acquiring if no semaphore is configured
- Ensures slot is released even if an exception occurs during the network call
<!-- trie:end -->
<!-- trie:section symbol=trie/models:SectionBody fingerprint=f1c4c6eb19f0882dbf14ae82cd52931932109942e91db24865048776cea2d292 body_fp=0c65a7225c02dfb22172000eacfcb9790dcc05de641b3e7c350440d71083a623 source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 role=llm-client -->
Pydantic model representing triefact documentation output with architectural classification.

- `body`: markdown documentation text for the symbol
- `role`: architectural function tag (entrypoint, api, domain, etc.) with detailed standard vocabulary
- `boundary`: system boundary position (entry, exit, internal) based on external interaction patterns
<!-- trie:end -->
<!-- trie:section symbol=trie/models:ProposedRole fingerprint=495f5b5a00623eb05a4cd6cccf1fc0a018d6bf71d20bc221a4c34130c39f3c15 body_fp=47afbef558e2cfa0b560cfd4deba4597a585b028464686a2939439d31afd82a4 source_ref=523bc80dac1cf272d259a694f1e9dbe2f39b6818 role=model -->
Pydantic model representing a single role in a project-specific architectural taxonomy.

- `name`: Short lowercase identifier for the role, hyphenated if multiple words
- `description`: Concrete definition enabling unambiguous symbol classification
<!-- trie:end -->
<!-- trie:section symbol=trie/models:RoleTaxonomy fingerprint=c0840ea457e6a07c657efb1d60e7b4d8afbf93f56e060d24692fa7442362eb09 body_fp=3d2f15854b2ad282c553450dca5fe2de73befa7aee82825b074c729f7fc5a6cf source_ref=523bc80dac1cf272d259a694f1e9dbe2f39b6818 role=model -->
Defines a coherent set of project-specific architectural roles derived by analyzing the entire codebase.

- **roles**: List of ProposedRole objects representing the complete role vocabulary (6-14 roles preferred)
<!-- trie:end -->
<!-- trie:section symbol=trie/models:RoleTag fingerprint=888b91be326405a05aa86b22d6fc97a36e9bbc69d04edaf2792db9e6ab448f45 body_fp=6900222bf8617e0e3cf0eb1411e3c1b6a6b63bc386879e0a251a2a6b0eb691e3 source_ref=523bc80dac1cf272d259a694f1e9dbe2f39b6818 role=model -->
Pydantic model for classifying symbols against project-specific role vocabularies during pass 2 of role tagging.

- `role`: must match one of the role names from the injected taxonomy
- `boundary`: entry/exit/internal classification shared with SectionBody
<!-- trie:end -->
<!-- trie:section symbol=trie/models:MergeNotesOutput fingerprint=88ee7a8f24914ccaa2c1f516d5280519243c5c7c08ee77186fa40ebb85986a90 body_fp=2178661683f1b041f43c2d9e53bb7720bdc21bbceab3a500a90eb59e3ef8a27e source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 role=llm-client -->
Pydantic model containing deduplicated patch notes and their reasons.

- `notes`: list of deduplicated patch note strings
- `reasons`: explanations for why notes were deduplicated or modified
<!-- trie:end -->
<!-- trie:section symbol=trie/models:SymbolEdit fingerprint=57dd52b0d94825f3f668f3b1bfddd8bab7a14c45b43099c5f0ae6ab55384d356 body_fp=62c4bfadbdc802dd7409e8b1a85bd25e3b1b0017558ceeabd96d6a289ef75acf source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 role=llm-client -->
Pydantic model containing updated source code and documentation prose for a single symbol.

- `source`: The modified source code text
- `prose`: The generated documentation text
<!-- trie:end -->
<!-- trie:section symbol=trie/models:SymbolProse fingerprint=b7673717906ca3a3e22cb36409bfa01b9388954c8bdafa7dd74be9adc5eb8334 body_fp=0d300db78b96e71ada0dd11e07184ec8aabe40b94082b9b861b90e0e6458d6f1 source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 role=llm-client -->
Holds qualified name and prose for a single symbol within a multi-symbol file edit.

- `qname`: qualified name identifier of the symbol
- `prose`: documentation text content for the symbol
<!-- trie:end -->
<!-- trie:section symbol=trie/models:FileEdit fingerprint=18c6fde126dda842b172894a1d7969bffd6979a42427ef73a00befd2c1624c94 body_fp=8b1ef6ab01b141a7aeda9537a98d505feae0c618cd386e4ddcd069f10be54d92 source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 role=llm-client -->
Pydantic model for updated file content paired with prose documentation for each symbol.

- `content`: The modified file source code
- `prose`: List of symbol-specific documentation entries
<!-- trie:end -->
<!-- trie:section symbol=trie/models:CallerDecision fingerprint=46e38341622b99ce0e28e749efbcd233a39dc0623e5ee3987b3cf5c46a8d3c18 body_fp=0c6b553fbd53637897a908bf05845d110ad190859b08c7b43b60a45958d2703b source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 role=llm-client -->
Represents a decision for one callee→caller relationship in batch filtering operations.

- `action`: defaults to "skip"
- `note`: optional additional information
- `reason`: optional explanation for the decision
<!-- trie:end -->
<!-- trie:section symbol=trie/models:BatchFilterOutput fingerprint=a10dc059026469f9d748967d905a59299348a85f3d255cb47a79d9948a9455f5 body_fp=a4dde2e8fb5eff963bc94271b5e4ca60d9dbef0620027dc790a712dccd90144f source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 role=llm-client -->
Pydantic model containing a list of CallerDecision objects for batch filtering of callee-caller relationships.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:FixupOutput fingerprint=c316347f4b7a219db220fbf75660ccfe74b7cd20c5798bf4b17b5870cea277a0 body_fp=5d2a863fa6c16e748a081c54dc6522d1e366bcdeaf1fca96a4eac37810a3b01a source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 role=llm-client -->
Pydantic model containing corrected file content after diagnostic processing.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:ModelResult fingerprint=944e7a67fb921e06cfb00b9fdcc9087d211425e780245f8b9e055d1c8267ea8b body_fp=99a810d0650166cf9dfec1e6519258c92bfddffbfc3d5473d60c20996e5cf135 source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 role=llm-client -->
ModelResult wraps structured Pydantic output with token usage counters from LLM calls.

• `output` — the structured Pydantic model returned by the agent
• `cache_creation_input_tokens` — tokens used to create new cache entries
• `cache_read_input_tokens` — tokens read from existing cache entries
<!-- trie:end -->
<!-- trie:section symbol=trie/models:ModelResult.__init__ fingerprint=146d3b3c6c2599af53357ed723ae6a33d43fffa4ffd45827f8701b2f0a908133 body_fp=942c4d753b1786d9156f7a91801c7db40478afbe8233b5be486a974f7d8355d1 source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 role=llm-client -->
Initializes a ModelResult with structured output and usage statistics.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:ModelResult.output fingerprint=b42bf4ac160d131fa9fd50d941884f90328324a5719e9825e955198377283293 body_fp=485395b9293751519287116f50aa9cc9dae24d55bd8b71d7f14b501a6a6ac9d2 source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 role=llm-client -->
Returns the structured Pydantic model output from ModelResult.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:ModelResult.input_tokens fingerprint=a1b024dca62986b05239ba3a557a6a77cb6716142f9187eb02245c2c084fc341 body_fp=22feedb8cce7ae2add5e58dcfea9d3267ac36d28035a5838ea566f87fe796448 source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 role=llm-client -->
Returns input token count from ModelResult's usage data.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:ModelResult.output_tokens fingerprint=b6a524062960a03daf7217df2a7f2a3978267a80402019e11007fa11e0a04fec body_fp=6788e507a215020037654be94b6b143fcf5af911e1030c8ca98a60730c9f3365 source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 role=llm-client -->
Returns the number of output tokens from the ModelResult's usage statistics.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:ModelResult.cache_creation_input_tokens fingerprint=c412d39b13ce5aa8095b9c6acdf17de80fd32005bb29c200e9d44aaccdfa1ccc body_fp=33aa44bfaba7158d2ba9d38d5e401d595182aaf999c173a4a48522d16de0a467 source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 role=llm-client -->
Returns ModelResult's cache creation input token count from usage details, defaulting to zero.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:ModelResult.cache_read_input_tokens fingerprint=c6401a552c228d7d6a73e44517e411117af40bfb71c63e0df7e1edf3bc5b22df body_fp=56fbf6fafcf4104b9902c71779ec43267b051d5ffe7cf32772650a13bd169348 source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 role=llm-client -->
Returns the number of input tokens read from cache during ModelResult generation.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_retry_after_seconds fingerprint=eea4acb8b1e16f87411463e5b36f7296696e1226574047bf6b26e59be639801c body_fp=5400da1da68ecff033d8015e310ecf6ae1eb1f77d67ed65dbf8154f4d90d88ae source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 role=llm-client -->
Extracts the retry delay in seconds from an APIStatusError's retry-after header, returning None if unavailable or invalid.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_is_retryable fingerprint=bea2105277ba4c6f333f68b3b6c1ac502431df076d907eeda0a9b75455594da3 body_fp=324d787fad441b1b54feb99c36e82a91f14b7b09b395b2efb9c4d2798b84e0df source_ref=ab49f962e9a178707553fcf6ad796ef550b20bc2 role=util -->
Returns True if the exception is retryable (rate limit, internal server error, timeout, or connection error).
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_backoff_delay fingerprint=77f4e3c66b993cc965f7254cdc34761c6af37a46bcee27228820a1f4647a0475 body_fp=db499c0114246d369fa21a973c4cc466d777071d1f99d8535ad718efe61464f4 source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 role=llm-client -->
Calculates exponential backoff delay with jitter, returning a random duration between zero and the capped window.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_run_with_retry fingerprint=74ca4f2a16ec6fbc5e31d4fbce56fec10a5ebcd72eec0e14800b2f3690e1a2f2 body_fp=cafd3a5922db59b734b54de48ef860147f7595cafc2c321fa3a01f9b5b9bcb47 source_ref=ab49f962e9a178707553fcf6ad796ef550b20bc2 role=util -->
Executes a callable with exponential backoff retry logic for rate limits, timeouts, and server errors.

- Respects `retry-after` headers for rate limit exceptions
- Emits telemetry events on each retry attempt with delay and reason
- Stops retrying after `cfg.max_retries` attempts or non-retryable exceptions
<!-- trie:end -->
<!-- trie:section symbol=trie/models:T fingerprint=511f85b873237a1963584329b2ded56f290efb33b59ff4f1f52a3ff84742f48d body_fp=d54080f28b388848817988e57cc93775750bb1d46b147449f3fe09535a32e6c4 source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 role=llm-client -->
Type alias for Any used as a TypeVar placeholder in the retry helper function.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_MODEL_ID_ALIASES fingerprint=d436771cb40ad6b40d58029730c3e289ab040b962b73ae7492868749c08d6618 body_fp=5d9fcbfd1b775034361a99f4fae78c8a73ef555ffd4c78064d2c8488d9f2c319 source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 role=llm-client -->
Maps trie's `provider/model` format to pydantic_ai's `provider:model` format for model ID conversion.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_pydantic_ai_model_id fingerprint=a0a6b3d1a8febf77bc636de899705a5808a8091b4f9ec907ce9d9611400a53ec body_fp=3de559806ca1742ec8f60138929d9d4db6171d99971d8b00a183783b63e33a6f source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 role=llm-client -->
Converts trie's provider/model format to pydantic_ai's provider:model format using aliases or simple substitution.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_anthropic_model_name fingerprint=3c87d22ca61cada7c6dd2721cf27ba2000942a7010fc3dac57aeb0cd6ca74261 body_fp=9f60ebe4d744a72dcf3f42d216efade5c4613aa01f6d939ef3729a3781e6bf20 source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 role=llm-client -->
Extract the bare Anthropic model name from a full trie model ID by stripping the provider prefix.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:TrieClient fingerprint=2da7f35aa156533a5dca7719fcdfee550a547cebf03bc82b98f074fed245a606 body_fp=c04b1f1833c627020d2fc417defc12d426594c4c2fade96c1b2090070b1c9259 source_ref=b80d20b1306fa37c369f12494d2c4a3fff683036 role=model -->
Wraps Pydantic AI agent creation and execution with structured output, prompt caching, and retry logic.

- `run`: Creates one-shot agent with structured output type, handles prompt caching via cache_prefix
- `count_tokens`: Uses raw Anthropic SDK to estimate token costs without generation
- Manages per-thread event loops to avoid file descriptor leaks under parallel execution
- Applies exponential backoff retry on rate limits and server errors
- Pre-constructs and reuses a single AnthropicModel instance to prevent HTTP client fd exhaustion
<!-- trie:end -->
<!-- trie:section symbol=trie/models:TrieClient.__init__ fingerprint=1ba0bc94b18d62da77945c4fdbe64518d5dfe65ca6c6f72e5f414dc3dc56b26c body_fp=66bfa91c1ddb7f849fc942bea84f8dfc39a71cd618095507f03fd744198b78b2 source_ref=b80d20b1306fa37c369f12494d2c4a3fff683036 role=model -->
Initializes TrieClient with model ID conversion, configuration setup, and reusable pydantic-ai model.

- `full_model_id`: trie's provider/model format (e.g., "anthropic/claude-sonnet-4-6")
- `sync_cfg`: retry configuration, defaults to Sync() if None
- Creates raw Anthropic client with retries disabled (handled by wrapper)
- Constructs shared AnthropicModel instance to prevent file descriptor leaks from per-run model creation
<!-- trie:end -->
<!-- trie:section symbol=trie/models:TrieClient.run fingerprint=782c9f6e0e302f33b48a43dff97a55b1bfc395691722d575743fe9f7d33ca5e2 body_fp=2f9903af898f3d680b16c5fb4cce8dc43a619b18aa3efc684f7067a01eac9a31 source_ref=7b6978ad15fe0381f84e0d22885ce10437c8dfb5 role=io -->
TrieClient.run creates a pydantic-ai Agent with structured output and executes it with retry logic and rate limiting.

• cache_prefix: when provided, cached as a shared prefix across multiple calls for cost efficiency
• max_tokens: maximum tokens for the model output (default 1024)  
• Returns ModelResult containing structured output and token usage counters
<!-- trie:end -->
<!-- trie:section symbol=trie/models:TrieClient.count_tokens fingerprint=3c0147fbfd76558d6fd2a6176f921093c72e3ac31e6c8b6ad60f9438d78015cd body_fp=d1251490fb9cbe8f30a370fbf5d4fbabc0fa9e2d49a8416658826e62690ea73b source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 role=llm-client -->
TrieClient.count_tokens returns the number of input tokens via the Anthropic count_tokens API for system and user prompts.

- Empty user prompts are replaced with "." to avoid API rejection while preserving cost estimation accuracy
<!-- trie:end -->
<!-- trie:section symbol=trie/models:make_client fingerprint=3357d2c90a369504b954bcdaeda5dc66234fd60cb89e23082eda6f4ddc882612 body_fp=935d0255ccbde76f44c569ac5890436fb94c87c29377089e9f51358d32c9435d source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 role=llm-client -->
Constructs a TrieClient from a provider/model ID string, validating format and supporting only anthropic provider.
<!-- trie:end -->